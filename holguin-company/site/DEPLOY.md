# Deploying to GoDaddy (File Manager)

This folder is the deploy set. Upload to the web root, keeping the folder structure:

```
index.html                 (replaces the current one)
principal/index.html       → https://holguincompany.com/principal/
the-diagnostic/index.html  → https://holguincompany.com/the-diagnostic/
robots.txt
sitemap.xml
llms.txt
fonts/                     (folder: six .woff2 files, self-hosted Cormorant Garamond and Archivo)
adrian-holguin-portrait.jpg  (add: the founder portrait, 1000×1250, from HighLevel media "Holguin-Adrian-Founder-Portrait.jpg")
```

Performance pass (28 Oct 2026), after PageSpeed showed mobile LCP 3.1 s and a 12.7 MB page:
- Fonts are self-hosted from `/fonts/` with the `@font-face` rules inline in each page's first `<style>` block; the Google Fonts stylesheet and preconnects are gone. The two above-the-fold files are preloaded.
- The film uses `preload="none"`; nothing is fetched until the overlay is pressed. The overlay is 94% opaque, so no poster is needed.
- The HighLevel booking iframe and `form_embed.js` load only when the booking section is within 800 px of the viewport, or when a `#book` link is followed.
Upload `fonts/` together with the three pages; the pages reference `/fonts/...` by absolute path.

Unchanged and already on the server: `favicon.svg`, `og-image.png`, `holguin-company-vsl.mp4`.

`index.html` carries the live GA4 Measurement ID (G-B9JPVD9YSY); nothing to edit before upload.

GoDaddy 301s `/principal` to `/principal/` (confirmed live 28 Oct 2026), so the canonical, og:url, JSON-LD ids, sitemap and llms.txt all use the trailing-slash form. Keep it that way.

After upload: run section 6 of `../SEO-GEO-audit-and-game-plan.md`.
