# In the News section (cannasharkconsulting.com)

Files in this folder are the source for the website's **In the News** section.

| File | What it is |
|------|------------|
| `press.json` | Source of truth: one entry per published article, newest first. |
| `in-the-news.html` | Drop-in section block. Paste into a Custom HTML element on the site. Includes scoped CSS and JSON-LD. |
| `index.html` | Optional standalone `/press/` page wrapper around the block. |

## Adding the next article

1. Add an entry to the top of `articles` in `press.json` (headline, outlet, URL, date, two or three sentence summary, four or five key facts in plain sentences).
2. Copy the newest `<li class="cs-press__item">` block in `in-the-news.html`, paste it above the others, and fill it from the JSON entry.
3. In the JSON-LD at the bottom of `in-the-news.html`, add a `ListItem` at `position: 1`, renumber the rest, and bump `numberOfItems`.
4. Re-paste the whole block into the site.

## Why it is written this way

- Key facts are full sentences with the number, the date and the outlet, so answer engines can quote them without the surrounding article.
- JSON-LD links the author, the organization and each `NewsArticle` so the site, not the outlet, is the entity hub for "Adrian A. Holguin" and "CannaShark Consulting".
- Every item links to the original with the outlet named. No copy of the article body lives here; the outlet owns the canonical text.
- Brand rules from the Brand Source of Truth apply: no phone number, no hype language, "CannaShark Consulting" never "Group", teal `#7ED4D0` accent.
