# Preventing and recovering from oversized requests

Added 2026-09-22 after the user identified prompt size as an explicit lesson from the second Dale attempt. Use this guidance throughout image-heavy modeling, and consult the recovery steps if a size error interrupts work.

## What the incident establishes

The user reported this exact error in the task **Fix oversized session error** (conversation `6ab1caa1-86b8-83e8-b0a9-0bdf76fdbd9a`):

```text
{"error":"decompressed request body exceeds 67108864 bytes"}
```

67,108,864 bytes equals 64 MiB. This message identifies a decompressed request-body size rejection in that incident. It does not identify a token limit, a maximum project/mesh size, or a universal limit for every app/model. The user's follow-up in **Draft diorama pipeline skill** associates the incident with the second Dale attempt.

Accumulated images and verbose tool results are plausible contributors, but no captured request breakdown establishes their individual shares. Do not present the old troubleshooting response's guesses about the client, network, or particular tools as a verified diagnosis.

Compaction reduces model context while carrying forward state, as described in the [official OpenAI compaction documentation](https://developers.openai.com/api/docs/guides/compaction). That API documentation does not establish that a desktop client's oversized request will be repaired by compaction. Treat request bytes and model context as separate constraints; do not assume a larger-context model or compressed network transfer solves this incident.

## Prevention during ordinary work

1. **Keep heavy assets on disk.** Preserve original reference images, full-resolution renders, meshes, scene files, and detailed audits. Return paths and concise findings. Creating a large local artifact does not require loading its full contents into conversation.
2. **Make a review derivative before loading images.** Assemble the views needed for the decision into one JPEG contact sheet, normally 1,200–1,600 pixels on its longest edge and below 500 KB when practical. Inspect its pixel dimensions and file size. These are workspace review targets, not guaranteed service limits. If detail is illegible, add a focused crop instead of loading every full-resolution view.
3. **Avoid repeated image ingestion.** Do not reopen unchanged references every iteration. Compare the new revision with the relevant baseline on one sheet. Do not repeatedly attach the same image through several tools or presentations without a reason.
4. **Reduce tool results before they enter the conversation.** Save complete logs, mesh arrays, scene dumps, and large JSON locally. Return selected fields: path, dimensions, counts, changed/protected scope, pass/fail, limitations, and relevant error excerpts. Never print base64 image data. When orchestrating tools, parse/filter their results before emitting them; wrapping a huge result in another tool call does not make it small.
5. **Retrieve history selectively.** Read the current checkpoint first, then the current element's notes. Use targeted searches and bounded excerpts. For historical task retrieval, emit only the relevant user decisions and outcomes; omit command bodies and irrelevant tool transcripts. Do not dump every prior stage or conversation to reconstruct a decision already recorded on disk.
6. **Maintain restartable state before trouble.** Update the checkpoint at meaningful revision/stage boundaries, especially before an extended render, generation, or repair cycle. Keep it concise and link to details. Record accepted scope, rejected branches, actual next action, and any active job so a new session cannot silently restart or duplicate work.

There is no proven safe number of turns or images. Repeated size failures, oversized tool results, or difficulty retaining the active baseline are reasons to reduce payloads and prepare a handoff, not to delete project assets or lower model quality.

## Recovery after a size rejection

1. Record the exact error and the failed operation if available. Stop repeating the unchanged failing request or adding large attachments to it.
2. Preserve local work and determine which operations actually completed. Read file/audit/job status where tools remain available. A request error does not prove a render or reconstruction failed; avoid launching duplicate jobs.
3. Write or refresh the checkpoint if the current session can still act. If it cannot, use the last on-disk checkpoint plus actual saved artifacts; do not make recovery depend on getting the broken conversation to generate a summary.
4. Use a supported compaction mechanism only if available and functional; do not promise it repairs the byte-size failure. If continuation still fails, prepare a small restart message for a fresh task in the same workspace. Create that task only when the user explicitly asks. Prefer a fresh task with this handoff over copying the full transcript or assuming a history-carrying fork will reduce the payload.
5. In the fresh session, load workspace instructions and the current checkpoint, verify the named editable file, and inspect only the relevant compact review. Carry forward reference authority and accepted decisions for the active attempt only; consult its carryover/exclusion record before retrieving older work. Retrieve older evidence selectively only if something is missing.
6. If a fresh minimal session also fails, retain the exact error, app/version, time, affected task identifier, and minimal reproduction for support. Do not assert that old conversation growth explains that broader failure.

Do not delete local originals, rewrite internal app history, clear application data, or reinstall as an automatic part of this workflow.

## Small restart message

Use this form with real paths and the actual next action; do not paste all linked files into the message.

```text
Continue the diorama in [workspace path]. Read AGENTS.md and [project CHECKPOINT.md]
first. Active design attempt: [ID/root; continuing or restarting specified scope].
Allowed sources/carryovers: [checkpoint section]. Current editable candidate: [path]. Last accepted baseline: [path and scope].
Next action: [specific edit/review]. Preserve [critical approved properties].
Do not reuse [rejected source identities]. Latest compact review: [path].
Check [job/status record] before starting another generation or render.
The previous task hit [exact error]. Keep images and tool output compact; load
older history only for a specific missing decision.
```

## Evidence still needed

These practices reduce what we add to conversation and make recovery independent of a working old session. Their effectiveness against recurrence has not been measured. For another incident, record the last successful checkpoint, failing operation, images/tool-output sizes where observable, recovery attempted, and whether the minimal restart worked. Do not invent total request-size telemetry when the client does not expose it.
