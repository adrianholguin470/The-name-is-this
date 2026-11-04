# Macro Polo

A personal food, macro and bloodwork tracker on the road to 150. Point the camera at your
plate, Claude reads it, and the app keeps score.

**Live app:** https://claude.ai/artifact/YNW3ggSSi4RMyuVomw4ms9

## What it does

- **Camera button**: shoot a plate, menu, label or receipt. Claude analyzes it right in the
  app, asks if something is unclear, and logs calories, macros, fiber, sugar, saturated fat,
  cholesterol, sodium and a blood-sugar spike estimate, stamped with the time you ate.
- **Today**: calorie ring, macros against targets, a 24-hour timeline of your meals, eating
  window, overnight fast, and a live "fasting now" counter. Daily ceilings for added sugar,
  saturated fat, cholesterol and sodium. Glycemic load per meal. Chronological log with
  photo thumbnails. Add by hand when you want.
- **Trends**: 7 / 14 / 30 day eating windows, calories and macros per day, averages vs target.
- **Labs**: every bloodwork marker on its reference range, flagged when out of range.
- **Coach**: Claude's daily recaps, weekly reviews and bloodwork read-outs.

## Put it on your phone

Open the live link on your phone, then:

- **iPhone (Safari)**: tap the Share button, then "Add to Home Screen".
- **Android (Chrome)**: tap the three-dot menu, then "Add to Home screen" (or "Install app").

## Files

- `index.html` is the whole app: one page, no build step, inline SVG charts. Opened as a
  plain file it stores data in the browser only; published as a Claude artifact it uses
  the shared database, Claude for photo analysis, and asset storage for the photos.
- `CLAUDE.md` documents the database schema and the workflow for Claude.
