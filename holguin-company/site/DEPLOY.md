# Deploying to GoDaddy (File Manager)

This folder is the deploy set. Upload to the web root, keeping the folder structure:

```
index.html                 (replaces the current one)
principal/index.html       → https://holguincompany.com/principal/
the-diagnostic/index.html  → https://holguincompany.com/the-diagnostic/
robots.txt
sitemap.xml
llms.txt
adrian-holguin-portrait.jpg  (add: the founder portrait, 1000×1250, from HighLevel media "Holguin-Adrian-Founder-Portrait.jpg")
```

Unchanged and already on the server: `favicon.svg`, `og-image.png`, `holguin-company-vsl.mp4`.

`index.html` carries the live GA4 Measurement ID (G-B9JPVD9YSY); nothing to edit before upload.

GoDaddy 301s `/principal` to `/principal/` (confirmed live 28 Oct 2026), so the canonical, og:url, JSON-LD ids, sitemap and llms.txt all use the trailing-slash form. Keep it that way.

After upload: run section 6 of `../SEO-GEO-audit-and-game-plan.md`.
