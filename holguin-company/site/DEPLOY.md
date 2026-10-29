# Deploying to GoDaddy (File Manager)

This folder is the deploy set. Upload to the web root, keeping the folder structure:

```
index.html                 (replaces the current one)
principal/index.html       → https://holguincompany.com/principal
the-diagnostic/index.html  → https://holguincompany.com/the-diagnostic
robots.txt
sitemap.xml
llms.txt
adrian-holguin-portrait.jpg  (add: the founder portrait, 1000×1250, from HighLevel media "Holguin-Adrian-Founder-Portrait.jpg")
```

Also upload the IndexNow key file `6313b6e049fb4be43a5f506838e848e8.txt` (in this folder) to the web root, then run the ping in ../DAY-ZERO-RUNBOOK.md.

Unchanged and already on the server: `favicon.svg`, `og-image.png`, `holguin-company-vsl.mp4`.

Before uploading `index.html`, replace `G-REPLACE` with the GA4 Measurement ID and remove the `<!-- ... -->` markers around the GA4 block (two places).

If the host serves directories without a trailing slash as `/principal/`, that is fine; the canonical tags use the no-slash form and GoDaddy's hosting resolves `/principal` to `principal/index.html`. If it instead 301s to `/principal/`, change the two canonical and og:url values to match.

After upload: run section 6 of `../SEO-GEO-audit-and-game-plan.md`.
