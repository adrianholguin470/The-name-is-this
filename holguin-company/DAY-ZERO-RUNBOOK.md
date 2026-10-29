# Day Zero runbook — Holguin & Company (one sitting, about 75 minutes)

Order matters. Each step unblocks the next. Times are working estimates.

| # | Minute | Action | Who | Effect, and how fast |
|---|---|---|---|---|
| 1 | 0–10 | Upload the deploy set to GoDaddy File Manager (index.html, principal/, the-diagnostic/, robots.txt, sitemap.xml, llms.txt, the IndexNow key file `6313b6e049fb4be43a5f506838e848e8.txt`, adrian-holguin-portrait.jpg). GA4 ID into index.html first. | Chrome extension or you | Live immediately |
| 2 | 10–15 | Search Console: add Domain property → TXT in GoDaddy DNS → verify. Submit sitemap. | you | Verified in ~1 min once DNS propagates (often instant at GoDaddy) |
| 3 | 15–20 | Search Console → URL Inspection → "Request indexing" for `/`, `/principal`, `/the-diagnostic`. | you | Googlebot usually fetches within minutes; index within hours to 2 days |
| 4 | 20–22 | Bing Webmaster → import from Search Console → submit sitemap. | you | Minutes |
| 5 | 22–23 | IndexNow ping (command below). | you or me, once the key file is live | Bing, and therefore ChatGPT search and Perplexity's Bing-backed retrieval, within minutes to hours |
| 6 | 23–33 | LinkedIn: personal headline → "Founder & Managing Principal, Holguin & Company"; add Holguin & Company as current Experience with the website; set the company page's website and tagline; put holguincompany.com/principal in every social bio. | you | Live immediately; LinkedIn is re-crawled by AI engines daily |
| 7 | 33–53 | Wikidata: create the two items from `WIKIDATA-ITEMS.md` (person, then firm). | you, or Chrome extension with you logged in | Live immediately; Google Knowledge Graph and several AI engines read Wikidata within days |
| 8 | 53–63 | Google Business Profile: service-area business, Santa Clarita verification, address hidden. | you | Verification by postcard/video: 1–5 days; profile live on verification |
| 9 | 63–70 | HighLevel social fields (values in social-fields.md); TikTok rename. | you | Immediate |
| 10 | 70–75 | Post Insights article #1 as a LinkedIn article (insights/01). Schedule #2 for next week. | you | Immediate; LinkedIn articles are among the most-cited sources in AI answers |

## IndexNow ping (step 5)
Once `https://holguincompany.com/6313b6e049fb4be43a5f506838e848e8.txt` loads in a browser, run (or paste into the Chrome extension):

```
curl -sS -X POST "https://api.indexnow.org/indexnow" -H "Content-Type: application/json; charset=utf-8" -d '{"host":"holguincompany.com","key":"6313b6e049fb4be43a5f506838e848e8","keyLocation":"https://holguincompany.com/6313b6e049fb4be43a5f506838e848e8.txt","urlList":["https://holguincompany.com/","https://holguincompany.com/principal","https://holguincompany.com/the-diagnostic"]}'
```
A 200 or 202 means accepted. Re-run after every content change. Google does not use IndexNow; step 3 is Google's fast path.

## What cannot be sped up, stated plainly
- Google's index: minutes to crawl, hours to days to show in results. Request Indexing is the only accelerator.
- Bing's index and the engines that read it (ChatGPT search, Perplexity): hours after IndexNow.
- AI answers that come from search (Perplexity, ChatGPT with browsing, Google AI Overviews, Claude with search): change as soon as the pages are indexed.
- AI answers from model memory (no search): change only when the models are retrained. Months. Nothing accelerates this except being cited widely in the meantime.
- The LLC name collision: a filing, not a crawl. Call the attorney today.
