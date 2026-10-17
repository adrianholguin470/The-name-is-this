# Adrian & Kevin's Action Dashboard — reproduction bundle

Everything needed to rebuild the shared action board, its data, the nightly sweep routine, and Kevin's Board Playbook on a fresh Claude account or session. Exported 2026-10-16, 6:50 PM Pacific.

Live original: https://claude.ai/artifact/37akxGp77L8HE1miRxPVDT

## What is in here

| Path | What it is |
|---|---|
| `manifest.json` | Index of the bundle, source URLs, people, data model |
| `board/page.html` | The whole board page (single HTML file) |
| `board/capabilities.json` | Runtime capabilities for the first publish |
| `board/data/*.json` | One file per collection: groups, items, updates, files, meta |
| `board/data/by-id/<collection>/<id>.json` | The same documents, one per file |
| `routine/daily-kevin-sweep.json` | The 6:45 PM Pacific sweep: cron, binding, full prompt |
| `playbook/` | Playbook HTML source, diagram SVG/PNG, PDF render script, both email versions |
| `../Kevins-Board-Playbook.pdf` | The finished PDF (repository root) |
| `REBUILD-PROMPT.md` | A prompt you can paste into a new Claude session to do all of the below |

## Rebuild steps (for a Claude session with the Artifact tools and Gmail)

1. **Publish the page.** Call the Artifact tool with `file_path: board/page.html`, `icon: "checklist"`, and `capabilities` set to the object in `board/capabilities.json`. Note the new URL.
2. **Load the data.** For each collection, use `ArtifactData` with `action: "batch"` and `op: "set"` entries built from `board/data/<collection>.json` (`doc_id` and `data` are given per document). Batches take up to 50 writes, so items need two batches. Or write one document at a time with `file_path` pointing at the `by-id` files. Load `groups` first, then `items`, `updates`, `files`, `meta`.
3. **Verify.** `ArtifactData list` on `items` should return 60 documents. Open the page: four groups, items grouped by section, the file register and the thread notes should render.
4. **Share.** From the page's Share menu, add kmdgroupla@gmail.com as Editor. Sharing cannot be set from the tools.
5. **Recreate the routine.** From inside the session that will run it, call `create_trigger` with the name, `cron_expression` and `prompt` from `routine/daily-kevin-sweep.json`. If the board URL changed, replace it in the prompt first. If the routine should start a fresh session each run instead, set `create_new_session_on_fire: true` and `connectors: ["Gmail"]`.
6. **Playbook (optional).** `playbook/playbook.html` renders to the PDF with `playbook/render-pdf.js` (Playwright + Chromium). The finished PDF is already at the repository root.

## Rules the system runs under

- Only Adrian (owner) and Kevin (editor) edit the board. Viewers can read everything, write nothing.
- The sweep never deletes items, never changes access rules, never republishes the page. It only adds items, updates items with evidence, adds thread notes and file rows, and updates `meta/sweep`.
- Kevin's status changes are authoritative. The sweep never overrides a status without saying so in that item's thread.
- Item ids continue from the highest existing number (next is `i64`); file rows from `f27`.

## Data model

See `manifest.json` → `data_model`. Timestamps `createdAt`/`updatedAt` are epoch milliseconds; `due`, `date` and `completedAt` are `YYYY-MM-DD`; `lastSweepAt` is ISO 8601 UTC.
