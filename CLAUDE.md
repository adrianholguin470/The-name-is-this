# Macro Polo — working notes for Claude

Adrian's food, macro and bloodwork tracker. Goal: live to 150. Adrian photographs meals
inside the app (the camera button analyzes the photo with Claude in-page and logs it) or
sends photos and bloodwork screenshots in chat; Claude turns those into records in the
app's shared database. Meals are logged by time of day, not by meal category, so the app
can compute eating windows and fasts.

## Where the app lives

- Source: `index.html` in this repo (single page, no build step, dark single theme).
- Published artifact (the live app, with the shared database):
  https://claude.ai/artifact/YNW3ggSSi4RMyuVomw4ms9
- Republish after editing `index.html`: Artifact publish with that `url` (read it first if
  this session has not published it). Keep
  `capabilities: {db: {}, user: {}, sample: {images: true}, assets: {upload: "interact"}}`.
- Data is written with the `ArtifactData` tool against that URL. Never hardcode data
  into the page.
- **Every person has a private log.** The app is shared with Adrian's wife; each signed-in
  viewer reads and writes only `data/users/<their id>/root/...`, invisible to everyone else,
  the owner included. From Adrian's chat, address his data with the `me` segment:
  collections `data/users/me/root/meals`, `data/users/me/root/labs`,
  `data/users/me/root/insights`, and the settings doc at collection
  `data/users/me/root/settings`, doc id `profile`. The top-level `meals`, `labs`,
  `insights`, `settings` collections are no longer used (they were migrated on 2026-11-04).
  His wife's data cannot be reached from his chat; she uses the in-app camera, or her own
  Claude account.
- A meal photo the app saved is an asset; `photoId` on the meal doc is its id. To look at
  it from chat: Artifact `read` with that `url` and `path: <photoId>`.

## Database collections

All dates are local calendar dates as `YYYY-MM-DD`. Times are `HH:MM` 24h.

Collection names below are relative to the person's root (`data/users/me/root/`).

### `meals` — one document per logged meal or food

```json
{
  "date": "2026-11-04", "time": "12:30",
  "name": "Chicken burrito bowl",
  "source": "photo|claude|manual", "createdAt": "ISO timestamp",
  "items": [
    {"name": "Grilled chicken", "qty": "4 oz",
     "cal": 190, "protein": 35, "carbs": 0, "fat": 4, "fiber": 0, "sugar": 0,
     "satfat": 1, "chol": 110, "sodium": 390}
  ],
  "analysis": "Short note on what this meal does. **bold** and - bullets allowed.",
  "glycemic": {"gl": 14, "impact": "low|moderate|high", "note": "why"},
  "confidence": "high|medium|low",
  "userNote": "what Adrian typed when he shot it",
  "photoId": "asset id, when the app stored the photo",
  "pending": false,
  "notes": "optional", "example": false
}
```

- Totals are summed from `items` by the page. Grams for macros; mg for `chol` and `sodium`;
  `sugar` means added/free sugar.
- `time` matters: it drives the day timeline, eating window, overnight fast and
  "fasting now". Always set it. (`meal` category is no longer used; old docs may carry it.)
- `glycemic` is optional. If absent the page estimates glycemic load from net carbs, sugar
  share, fiber, protein and fat. Set it when you have a better read (e.g. juice, white rice).
- `pending: true` means the app could not reach Claude when the photo was taken. The entry
  shows "waiting for Claude" with zero numbers. When Adrian sends that photo in chat, read
  the doc, fill `items`, `analysis`, `glycemic`, set `pending: false`, keep `photoId`, and
  write with `if_version`.
- Doc id: `YYYY-MM-DD-<slug>-<4 chars>`; the app uses the same pattern.
- Mark seeded samples with `"example": true` so they show an "example" chip.

### `labs` — one document per blood panel date

```json
{
  "date": "2026-10-20", "lab": "Quest Diagnostics",
  "summary": "Two or three lines on the headline findings.",
  "markers": [
    {"group": "Lipid panel", "name": "LDL cholesterol", "value": 148, "unit": "mg/dL",
     "low": null, "high": 99, "flag": "high|low|borderline|normal (optional)",
     "note": "optional one-liner"}
  ]
}
```

Group names that read well: Lipid panel, Metabolic, Blood sugar, Liver, Kidney, Thyroid,
CBC, Vitamins & minerals, Inflammation, Hormones. Copy the lab's own reference range.
Doc id: the date. The in-app photo analysis reads the latest panel's flagged markers, so
loading labs also sharpens every meal note.

### `insights` — Claude's notes to Adrian (Coach tab)

```json
{"kind": "daily|weekly|labs|meal|tip|welcome", "date": "2026-11-04",
 "createdAt": "ISO", "title": "Tuesday recap", "body": "markdown-lite: paragraphs, - bullets, **bold**"}
```

Newest first in the app. Doc id: `<kind>-<date>`.

### `settings/profile` — targets

```json
{"name": "Adrian", "goal": "Live to 150",
 "targets": {"cal": 2000, "protein": 150, "carbs": 200, "fat": 65, "fiber": 30,
             "sugar": 36, "satfat": 20, "chol": 300, "sodium": 2300}}
```

Protein and fiber are floors; cal, carbs, fat are budgets; sugar, satfat, chol, sodium are
ceilings. Adjust from bloodwork (e.g. high LDL: satfat 13 g, chol 200 mg, fiber 38 g).
Always read the doc first and pass `if_version` when updating.

## How to handle what Adrian sends

1. **Food photo in chat**: identify every item and portion. Estimate per-item nutrition
   from standard references. If an item, portion, or preparation is unclear, ask one short
   question before logging rather than guessing wildly; log what is certain. Write one
   `meals` doc per meal (several items inside) with the time he ate it (ask if he did not
   say; default to the photo's time if he gives it), and a two or three line `analysis`
   that names the biggest cholesterol, sodium or blood-sugar driver and one easy swap.
2. **Bloodwork screenshots**: transcribe every marker with the lab's reference range into
   one `labs` doc. Add an `insights` doc of kind `labs` explaining what matters and what
   food changes follow. Update `settings/profile` targets to match.
3. **"How did today go" / weekly review**: read `meals` for the window, compare to
   targets and labs, include eating-window and overnight-fast lengths, and write an
   `insights` doc (kind `daily` or `weekly`). Be specific: what he did well, where the
   day went sideways, and the likely effect on LDL, triglycerides, A1c and blood pressure.
4. Medical framing: this is nutrition tracking and general guidance, not diagnosis.
   Point to his doctor for medication or abnormal-result decisions.

## Branch

Develop on `claude/jolly-ride-9l7rts`; push there with `git push -u origin`.
