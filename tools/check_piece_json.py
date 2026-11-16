#!/usr/bin/env python3
"""Check the piece.json of every locked version folder; standalone, standard library only.

    python check_piece_json.py [--metadata-only] [--hoard FILE] PATH [PATH ...]

Copy this one file into a repo that makes pieces and run it in that repo's PR check or a
pre-commit hook. Each PATH is a piece.json or a folder searched for them (.git skipped).
It checks what a repo can check on its own: the required fields and closed values, that
every component file exists beside the piece.json, and that every print file there is
named by a component. --metadata-only skips the two file checks, for repos whose print
files live outside git (a release asset, or the Mac). A version that holds only its changed
parts names each unchanged one in an earlier sibling version folder ("../v1/print/roof.3mf");
import_piece copies it in at its path there ("print/roof.3mf"). The library's import_piece applies
the full piece schema on top; run it with dry_run to see that verdict.

It also checks the repo's hoard.json (by default ./hoard.json, run from the repo root): the
family The Hoard offers new ideas to, and the project folders it scans for locked versions.

The lists below are the library's own (bookwyrm-rpg services/library, piece_schema.py and
piece_import.py); a test there pins this copy to them. Exit status: 0 clean, 1 problems,
2 neither a piece.json nor a hoard.json found.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from pathlib import Path, PurePosixPath

MANIFEST = "piece.json"
FORMAT = 1
HOARD = "hoard.json"
HOARD_FORMAT = 1
REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
KINDS = ("diorama", "figurine", "lamp", "ornament", "terrain", "prop", "container")
STATUSES = ("concept", "digitally-validated", "prototype", "interface-fit-tested", "qualified")
DESIGNS = ("original", "ai-assisted")
LICENCES = (
    "personal-use-only",
    "all-rights-reserved",
    "CC0",
    "CC-BY",
    "CC-BY-SA",
    "CC-BY-NC",
    "CC-BY-NC-SA",
)
NO_IP = "none"
COMPONENT_KEYS = ("name", "file", "part_id", "quantity", "printer", "material")
PRINT_EXTENSIONS = ".stl .3mf .obj .goo .ctb .gcode .bgcode .step .stp".split()  # role "print"
SKIP_DIRS = ("__pycache__", "tmp", "scratch")
SKIP_SUFFIX = ".blend1"
SKIP_NAMES = (".DS_Store",)
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,79}$")
TAG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
VERSION_RE = re.compile(r"^v[0-9]+(\.[0-9]+)*$")


def print_files(folder: Path) -> list[str]:
    """Relative paths of the print files an import of folder would copy."""
    found = []
    for top, dirs, names in os.walk(folder):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not (Path(top) / d).is_symlink())
        for name in names:
            if name.endswith(SKIP_SUFFIX) or name in SKIP_NAMES:
                continue
            if PurePosixPath(name).suffix.lower() in PRINT_EXTENSIONS:
                found.append((Path(top) / name).relative_to(folder).as_posix())
    return sorted(found)


def problems_for(path: Path, metadata_only: bool = False) -> tuple[list[str], tuple | None]:
    """Every problem with one piece.json, and its (slug, version) when both are readable."""
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return [f"not valid JSON: {exc}"], None
    if not isinstance(manifest, dict):
        return ["expected an object"], None
    problems = [
        f"{k}: required"
        for k in ("piece_json", "slug", "version", "title", "kind", "status", "rights")
        if k not in manifest
    ]
    get = manifest.get
    if "piece_json" in manifest and get("piece_json") != FORMAT:
        problems.append(f"piece_json: {get('piece_json')!r} is not {FORMAT}")
    if "slug" in manifest and not (isinstance(get("slug"), str) and SLUG_RE.match(get("slug"))):
        problems.append(f"slug: {get('slug')!r} is not a lowercase-kebab id of 1-80 characters")
    if "version" in manifest and not (
        isinstance(get("version"), str) and VERSION_RE.match(get("version"))
    ):
        problems.append(f"version: {get('version')!r} is not v<N> or v<N>.<M>")
    if "title" in manifest and not (
        isinstance(get("title"), str) and 1 <= len(get("title").strip()) <= 200
    ):
        problems.append(f"title: {get('title')!r} is not 1-200 characters")
    for field, allowed in (("kind", KINDS), ("status", STATUSES)):
        if field in manifest and get(field) not in allowed:
            problems.append(f"{field}: {get(field)!r} is not one of {', '.join(allowed)}")
    rights = get("rights")
    if "rights" in manifest:
        if not isinstance(rights, dict):
            problems.append("rights: expected {design, ip, licence}")
        else:
            problems += [
                f"rights.{k}: required" for k in ("design", "ip", "licence") if k not in rights
            ]
            if "design" in rights and rights["design"] not in DESIGNS:
                problems.append(
                    f"rights.design: {rights['design']!r} is not one of {', '.join(DESIGNS)}"
                )
            ip, licence = rights.get("ip"), rights.get("licence")
            if "ip" in rights and not (isinstance(ip, str) and TAG_RE.match(ip)):
                problems.append(f"rights.ip: {ip!r} is not lowercase kebab")
            if "licence" in rights and licence not in LICENCES:
                problems.append(f"rights.licence: {licence!r} is not one of {', '.join(LICENCES)}")
            elif isinstance(ip, str) and ip != NO_IP and licence not in (None, "personal-use-only"):
                why = "third-party IP is personal-use-only"
                problems.append(f"rights.licence: {licence!r} with ip {ip!r}; {why}")
    components = get("components", [])
    if not isinstance(components, list):
        problems.append("components: expected a list")
        components = []
    for i, component in enumerate(components):
        label = f"components[{i}]"
        if not isinstance(component, dict):
            problems.append(f"{label}: expected an object")
            continue
        problems += [f"{label}.{k}: unknown field" for k in component if k not in COMPONENT_KEYS]
        quantity = component.get("quantity", 1)
        if type(quantity) is not int or quantity < 1:
            problems.append(f"{label}.quantity: {quantity!r} is not a positive integer")
    named = {c.get("file") for c in components if isinstance(c, dict)}
    imported = {}  # revision path -> component file
    for file in sorted(f for f in named if isinstance(f, str)):
        parts = file.split("/")
        earlier = parts[0] == ".." and len(parts) > 2 and VERSION_RE.match(parts[1])
        if ".." not in parts:
            stored = file
        elif earlier and ".." not in parts[2:]:
            stored = "/".join(parts[2:])
        else:
            problems.append(f"components: {file!r} may only reach up into ../<version>/<path>")
            continue
        if stored in imported:
            twin = imported[stored]
            problems.append(f"components: {file!r} and {twin!r} both import as {stored!r}")
        imported[stored] = file
    if not metadata_only:
        folder = path.parent
        for i, component in enumerate(components):
            file = component.get("file") if isinstance(component, dict) else None
            if isinstance(file, str) and not (folder / file).is_file():
                problems.append(f"components[{i}].file: {file!r} does not exist")
        uncovered = [p for p in print_files(folder) if p not in named]
        if uncovered:
            problems.append(
                "components: no component names print file(s) "
                + ", ".join(repr(p) for p in uncovered)
            )
    key = (get("slug"), get("version")) if isinstance(get("slug"), str) else None
    return problems, key


def _relative(value) -> bool:
    return (
        isinstance(value, str)
        and bool(value)
        and not value.startswith("/")
        and ".." not in value.split("/")
    )


def hoard_problems(path: Path) -> list[str]:
    """Every problem with a repo's hoard.json; paths in it are relative to its folder."""
    try:
        hoard = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        return [f"not valid JSON: {exc}"]
    if not isinstance(hoard, dict):
        return ["expected an object"]
    root = path.parent
    problems = [f"{k}: required" for k in ("hoard_json", "family", "projects") if k not in hoard]
    known = {"hoard_json", "family", "projects", "ignore", "new_projects", "releases"}
    problems += [f"{k}: unknown field" for k in sorted(set(hoard) - known)]
    if "hoard_json" in hoard and hoard["hoard_json"] != HOARD_FORMAT:
        problems.append(f"hoard_json: {hoard['hoard_json']!r} is not {HOARD_FORMAT}")
    family = hoard.get("family")
    if "family" in hoard and not isinstance(family, dict):
        problems.append("family: expected {name, builds, skill, kinds?}")
    elif isinstance(family, dict):
        for k in ("name", "builds"):
            if not (isinstance(family.get(k), str) and family[k].strip()):
                problems.append(f"family.{k}: required text")
        skill = family.get("skill")
        if not isinstance(skill, dict) or not _relative(skill.get("path")):
            problems.append("family.skill: expected {path, repo?} with a relative path")
        elif "repo" in skill and not (
            isinstance(skill["repo"], str) and REPO_RE.match(skill["repo"])
        ):
            problems.append(f"family.skill.repo: {skill['repo']!r} is not owner/name")
        elif "repo" not in skill and not (root / skill["path"]).is_file():
            problems.append(f"family.skill.path: {skill['path']!r} does not exist")
        kinds = family.get("kinds", [])
        if not isinstance(kinds, list) or any(k not in KINDS for k in kinds):
            problems.append(f"family.kinds: each must be one of {', '.join(KINDS)}")
    projects = hoard.get("projects")
    if "projects" in hoard and not (
        isinstance(projects, list) and (projects or hoard.get("new_projects"))
    ):
        problems.append("projects: expected a list of folder globs, empty only with new_projects")
    elif isinstance(projects, list):
        for pattern in projects:
            if not (pattern == "." or _relative(pattern)):
                problems.append(f"projects: {pattern!r} is not a relative folder glob")
            elif not [p for p in glob.glob(str(root / pattern)) if Path(p).is_dir()]:
                problems.append(f"projects: {pattern!r} matches no folder")
    ignore = hoard.get("ignore", [])
    if not isinstance(ignore, list) or not all(_relative(i) for i in ignore):
        problems.append("ignore: expected a list of relative folders")
    new = hoard.get("new_projects")
    if new is not None and not (_relative(new) and "<slug>" in new):
        problems.append(f"new_projects: {new!r} is not a relative folder containing <slug>")
    if "releases" in hoard and not isinstance(hoard["releases"], bool):
        problems.append("releases: expected true or false")
    return problems


def manifests(paths: list[Path]) -> list[Path]:
    found = []
    for path in paths:
        if path.is_file():
            found.append(path)
            continue
        for top, dirs, names in os.walk(path):
            dirs[:] = sorted(d for d in dirs if d != ".git")
            if MANIFEST in names:
                found.append(Path(top) / MANIFEST)
    return sorted(found)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--metadata-only", action="store_true", help="skip the file checks")
    parser.add_argument("--hoard", type=Path, default=Path(HOARD), help="the repo's hoard.json")
    args = parser.parse_args(argv)
    found = manifests(args.paths)
    failed = False
    if args.hoard.is_file():
        for problem in hoard_problems(args.hoard):
            print(f"{args.hoard}: {problem}")
            failed = True
        print(f"{args.hoard} checked, {'problems found' if failed else 'clean'}")
    elif not found:
        print(
            f"no {MANIFEST} or {HOARD} found under: {', '.join(map(str, args.paths))}",
            file=sys.stderr,
        )
        return 2
    seen = {}
    for path in found:
        problems, key = problems_for(path, args.metadata_only)
        if key is not None and key in seen:
            problems.append(f"slug {key[0]!r} version {key[1]!r} is also in {seen[key]}")
        elif key is not None:
            seen[key] = path
        for problem in problems:
            print(f"{path}: {problem}")
        failed = failed or bool(problems)
    print(f"{len(found)} {MANIFEST} checked, {'problems found' if failed else 'all clean'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
