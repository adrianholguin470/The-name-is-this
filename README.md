# Macro Polo

A personal food, macro and bloodwork tracker on the road to 150. Think MyFitnessPal,
except the logging is done by Claude from photos sent in chat.

**Live app:** https://claude.ai/artifact/YNW3ggSSi4RMyuVomw4ms9

## What it does

- **Today**: calorie ring, protein / carbs / fat / fiber against targets, daily ceilings
  for added sugar, saturated fat, cholesterol and sodium, and a blood-sugar impact chart
  (estimated glycemic load per meal).
- **Log**: meals by day with per-item breakdowns and Claude's notes. Add foods by hand.
- **Trends**: 7 / 14 / 30 day calorie and macro charts and daily averages vs target.
- **Labs**: every bloodwork marker with its reference range, flagged when out of range.
- **Coach**: Claude's daily recaps, weekly reviews and bloodwork read-outs.

## How logging works

1. Take a photo of the plate, menu, label or receipt and send it to Claude in chat.
2. Claude identifies the items, estimates the nutrition, asks if something is unclear,
   and writes the meal into the app's database.
3. Bloodwork screenshots go the same way and land in the Labs tab.
4. Ask Claude for a rundown of the day or week any time.

## Files

- `index.html` is the whole app: one page, no build step, inline SVG charts. Opened as a
  plain file it stores data in the browser only; published as a Claude artifact it uses
  the shared database so Claude can write to it.
- `CLAUDE.md` documents the database schema and the workflow for Claude.
