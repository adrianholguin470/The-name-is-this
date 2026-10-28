# GoDaddy — what to do while signed in (10 minutes)

Signing in on your side does not give this session access, so these are for you to run.

**DNS (holguincompany.com)**
1. Add the Google Search Console TXT record (Search Console → Add property → Domain → copy the TXT) and the Bing Webmaster TXT/CNAME. Verification is then done without touching the page.
2. Confirm `www` is a CNAME or forward to the apex, and that the host forces HTTPS. Test: `http://www.holguincompany.com` should land on `https://holguincompany.com/` in one hop.

**holguinco.com**
3. If registered: Domain → Forwarding → permanent (301) to `https://holguincompany.com`, forward only (no masking). If not registered: register it; the Brand Book names it as the redirect domain.

**File Manager (the site)**
4. Upload `robots.txt`, `sitemap.xml`, `llms.txt` from this folder to the web root, next to the page.
5. Confirm `og-image.png`, `favicon.svg`, and `holguin-company-vsl.mp4` are in the root (the page references them by relative path).
6. When the schema patch and the two new pages are ready, upload them the same way: `principal/index.html` and `the-diagnostic/index.html` so the URLs are `/principal` and `/the-diagnostic`.

**Then, in a browser**
7. Run the two-minute check in the audit, section 6.
