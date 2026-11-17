"""Spend-guarded helpers for the Battle of Five Armies diorama: Tripo (3D) and OpenAI gpt-image (2D).

Runs inside Blender on David's Mac (Blender MCP execute_code), like bk.py/cv.py did for
Meshy. Keys are read from the bookwyrm-rpg builder .env and passed to curl on stdin, never
printed. Every paid call is appended to tripo_ledger.json before it is submitted; the cap
check refuses a call that would take committed Tripo credits past CAP.

    import importlib, sys; sys.path.insert(0, ROOT); import tp; importlib.reload(tp)
"""
import json, os, subprocess, threading, time

_LOCK = threading.Lock()

ROOT = "/Users/dave/code/bookwyrm-rpg-lantern-art/battle-of-five-armies"
ENV = "/Users/dave/code/bookwyrm-rpg/services/builder/.env"
LEDGER = os.path.join(ROOT, "tripo_ledger.json")
CAP = 700  # Tripo credits, agreed by David 2026-11-17 (planned 600-700)
TRIPO = "https://api.tripo3d.ai/v2/openapi"
OPENAI = "https://api.openai.com/v1"
IMG_MODEL = "gpt-image-2.5-flare"
IMG_USD = {"medium": 0.06, "high": 0.20}


def _key(name):
    for line in open(ENV):
        if line.startswith(name + "="):
            return line.split("=", 1)[1].strip().strip('"\'')
    raise RuntimeError(name + " not set in builder .env")


def _curl(args, key_name, timeout=300):
    cfg = 'header = "Authorization: Bearer %s"\n' % _key(key_name)
    p = subprocess.run(["/usr/bin/curl", "-sS", "-m", str(timeout), "-K", "-"] + args,
                       input=cfg, capture_output=True, text=True)
    if p.returncode:
        raise RuntimeError("curl %d: %s" % (p.returncode, p.stderr[:300]))
    return p.stdout


def load():
    return json.load(open(LEDGER)) if os.path.exists(LEDGER) else []


def save(L):
    json.dump(L, open(LEDGER, "w"), indent=1)


def _log(entry):
    with _LOCK:
        L = load(); L.append(entry); save(L)


def committed():
    """Tripo credits committed: actual where known, else the estimate; failed tasks count 0."""
    return sum(e.get("credits", e.get("est", 0)) for e in load()
               if e["api"] == "tripo" and e["status"] not in ("failed", "cancelled", "banned"))


def usd():
    return round(sum(e.get("usd", 0) for e in load() if e["api"] == "openai"), 2)


# ---------------------------------------------------------------- Tripo
def tripo(method, path, body=None):
    args = ["-X", method, TRIPO + path]
    if body is not None:
        args += ["-H", "Content-Type: application/json", "--data-binary", json.dumps(body)]
    out = json.loads(_curl(args, "TRIPO_API_KEY"))
    if out.get("code") != 0:
        raise RuntimeError("tripo %s: %s" % (path, json.dumps(out)[:400]))
    return out["data"]


def balance():
    return tripo("GET", "/user/balance")


def upload(path):
    out = json.loads(_curl(["-X", "POST", TRIPO + "/upload", "-F", "file=@" + path],
                           "TRIPO_API_KEY", 120))
    if out.get("code") != 0:
        raise RuntimeError("upload: " + json.dumps(out)[:300])
    return out["data"]["image_token"]


def submit(body, label, node, est):
    if committed() + est > CAP:
        raise RuntimeError("Budget cap: committed %d + %d > %d" % (committed(), est, CAP))
    before = balance()["balance"]
    tid = tripo("POST", "/task", body)["task_id"]
    _log({"api": "tripo", "label": label, "node": node, "type": body["type"], "task": tid,
          "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "est": est,
          "balance_before": before, "status": "queued", "out": None,
          "body": {k: v for k, v in body.items() if k not in ("file", "files")}})
    return tid


def poll():
    """Refresh unfinished Tripo tasks, download finished models. Returns a summary list."""
    L = load(); summ = []
    for e in L:
        if e["api"] != "tripo" or (e["status"] in ("success", "failed", "cancelled", "banned") and e.get("out")):
            continue
        t = tripo("GET", "/task/" + e["task"])
        e["status"] = t["status"]
        for k in ("consumed_credit", "credits_consumed", "consumed_credits"):
            if k in t:
                e["credits"] = t[k]
        if t["status"] == "success" and not e.get("out"):
            o = t.get("output", {})
            url = o.get("pbr_model") or o.get("model") or o.get("base_model")
            d = os.path.join(ROOT, e["node"]); os.makedirs(d, exist_ok=True)
            ext = os.path.splitext(url.split("?")[0])[1] or ".glb"
            p = os.path.join(d, e["label"] + ext)
            subprocess.run(["/usr/bin/curl", "-sS", "-m", "600", "-o", p, url], check=True)
            e["out"] = [p]
            if o.get("rendered_image"):
                pr = os.path.join(d, e["label"] + "_tripo.webp")
                subprocess.run(["/usr/bin/curl", "-sS", "-m", "120", "-o", pr, o["rendered_image"]])
        if t["status"] in ("failed", "banned", "cancelled", "expired"):
            e["out"] = ["FAILED: " + t["status"]]
        summ.append((e["label"], e["status"], t.get("progress"), e.get("credits", e["est"])))
    save(L)
    return summ


# ---------------------------------------------------------------- OpenAI images
def _img_log(label, node, kind, prompt, quality, out):
    _log({"api": "openai", "label": label, "node": node, "type": kind, "model": IMG_MODEL,
          "quality": quality, "usd": IMG_USD.get(quality, 0.2), "prompt": prompt,
          "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "status": "success", "out": [out]})


def _save_b64(resp, out):
    import base64
    j = json.loads(resp)
    if "data" not in j:
        raise RuntimeError("openai: " + json.dumps(j)[:400])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "wb").write(base64.b64decode(j["data"][0]["b64_json"]))
    return out


def leaf(image_path, label, node, detailed=True, model="v3.1-20260211", face_limit=None):
    """Untextured image-to-model. 20 credits, +20 for detailed (HD) geometry."""
    ext = os.path.splitext(image_path)[1].lower().strip(".").replace("jpg", "jpeg")
    body = {"type": "image_to_model", "model_version": model,
            "file": {"type": ext, "file_token": upload(image_path)},
            "texture": False, "pbr": False}
    if detailed:
        body["geometry_quality"] = "detailed"
    if face_limit:
        body["face_limit"] = face_limit
    return submit(body, label, node, 40 if detailed else 20)


def image(prompt, label, node, size="1536x1024", quality="high"):
    out = os.path.join(ROOT, node, label + ".png")
    body = {"model": IMG_MODEL, "prompt": prompt, "size": size, "quality": quality, "n": 1}
    r = _curl(["-X", "POST", OPENAI + "/images/generations", "-H", "Content-Type: application/json",
               "--data-binary", json.dumps(body)], "OPENAI_API_KEY", 600)
    _save_b64(r, out); _img_log(label, node, "generate", prompt, quality, out)
    return out


def edit(refs, prompt, label, node, size="1024x1024", quality="high", background="opaque"):
    out = os.path.join(ROOT, node, label + ".png")
    args = ["-X", "POST", OPENAI + "/images/edits", "-F", "model=" + IMG_MODEL, "-F", "prompt=" + prompt,
            "-F", "size=" + size, "-F", "quality=" + quality, "-F", "background=" + background]
    for r in refs:
        args += ["-F", "image[]=@" + r]
    _save_b64(_curl(args, "OPENAI_API_KEY", 600), out); _img_log(label, node, "edit", prompt, quality, out)
    return out


def entry(label):
    for e in load():
        if e["label"] == label:
            return e


# ---------------------------------------------------------------- queue (account concurrency limit)
_Q = {"jobs": [], "done": [], "errors": [], "running": False}


def enqueue(jobs, wait=30):
    """jobs: [(image_path, label, node, detailed)]. A daemon thread submits each one as soon
    as Tripo accepts it (code 2000 = account concurrency limit: wait and retry), and polls
    and downloads results. State in _queue.json."""
    _Q["jobs"] += list(jobs)
    if _Q["running"]:
        return
    _Q["running"] = True

    def loop():
        while _Q["jobs"] or any(e["api"] == "tripo" and not e.get("out") for e in load()):
            if _Q["jobs"]:
                img, label, node, det = _Q["jobs"][0]
                try:
                    leaf(img, label, node, detailed=det); _Q["done"].append(label); _Q["jobs"].pop(0)
                    continue
                except RuntimeError as ex:
                    if "2000" not in str(ex):
                        _Q["errors"].append((label, str(ex)[:300])); _Q["jobs"].pop(0)
            try:
                with _LOCK:
                    poll()
            except Exception as ex:
                _Q["errors"].append(("poll", str(ex)[:300]))
            json.dump({k: _Q[k] for k in ("jobs", "done", "errors")}, open(os.path.join(ROOT, "_queue.json"), "w"), indent=0)
            time.sleep(wait)
        _Q["running"] = False
        json.dump({k: _Q[k] for k in ("jobs", "done", "errors")} | {"finished": True}, open(os.path.join(ROOT, "_queue.json"), "w"), indent=0)

    threading.Thread(target=loop, daemon=True).start()
