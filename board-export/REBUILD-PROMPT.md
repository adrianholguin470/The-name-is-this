# Paste this into a new Claude session (Claude Code with the Artifact tools, or claude.ai with the repository attached)

```
Rebuild "Adrian & Kevin's Action Dashboard" from the bundle in board-export/ of this repository.

1. Read board-export/README.md and board-export/manifest.json.
2. Publish board-export/board/page.html with the Artifact tool. Pass the object in
   board-export/board/capabilities.json as `capabilities` and use icon "checklist".
   Tell me the new URL.
3. Load the database with ArtifactData batch writes (op "set") from
   board-export/board/data/groups.json, items.json, updates.json, files.json and meta.json,
   in that order. Each document's doc_id and data are given in the file. Keep batches at
   50 writes or fewer.
4. Verify with ArtifactData list: groups 4, items 60, updates 11, files 26, meta 1.
5. Remind me to share the new page with kmdgroupla@gmail.com as Editor from the Share menu
   (you cannot do that step).
6. Recreate the nightly sweep: call create_trigger with the name, cron_expression and prompt
   from board-export/routine/daily-kevin-sweep.json, after replacing the old board URL in the
   prompt with the new one. Bind it to this session.
7. Do not change any item text, status or id while loading. Do not republish the page after
   the first publish unless I ask.
```
