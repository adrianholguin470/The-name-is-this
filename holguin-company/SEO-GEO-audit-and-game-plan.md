# Holguin & Company — SEO + GEO audit and game plan

**Revision 2 · 2026-10-27.** Supersedes the 2026-10-26 draft. Revision 1 audited the HighLevel funnel and treated it as the live site. It is not. The live site is a single static page deployed to GoDaddy from the artifact "Holguin & Company — Business Strategy & Execution, Beverly Hills" (version of 2026-10-15), and it already carries a title, meta, canonical, Open Graph, and a JSON-LD graph. Everything below is rebuilt from that source, the Brand Book (Second Edition, September 2026), the Profile Pack (13 September 2026), the HighLevel records, and search-index checks.

**Still unverified, because this session's network policy blocks holguincompany.com:** that the deployed page matches the 15 October artifact, HTTP→HTTPS and www→apex redirects, `/robots.txt`, `/sitemap.xml`, the `og-image.png` and `favicon.svg` paths resolving, page weight, and Core Web Vitals. Section 6 is the two-minute check for those. To let a future session fetch the site directly, add `holguincompany.com` under Allowed domains in the environment's Network access settings.

Prepared for Adrian A. Holguin, Principal.

---

## 1. Executive summary

| Area | Status | Severity |
|---|---|---|
| Indexing | **Zero pages indexed** in Google or Bing (exact-domain search returns nothing). Site went up mid-September; no evidence of Search Console or Bing Webmaster verification. | Critical |
| Entity confusion | "Adrian Holguin" + "Holguin Company" resolves to a different Adrian Holguin ("Holguin Companies", Southampton NY) in every search run. Nothing on the web yet says "Adrian A. Holguin, J.D., M.B.A., Beverly Hills, Holguin & Company" in one place. | Critical for GEO |
| On-page SEO (live page) | **Good.** Title, meta, canonical, robots meta, OG and Twitter cards, SVG favicon, one H1, clean H2 outline, NAP in footer, `tel:` and `mailto:` links. Meta description runs ~190 characters (truncates at ~155). | Low |
| Structured data (live page) | **Present:** ProfessionalService `#firm`, Person `#principal`, Service with AggregateOffer ($5,000–$24,000), FAQPage (6 Q&A), WebSite. **Missing:** `sameAs` on both firm and person, `image`/`logo` on the firm (required for LocalBusiness rich results), credentials and `image` on the Person, VideoObject for the film. | High |
| Site structure | One URL. Everything is an anchor on `/`. No dedicated URL for the Principal (the entity page) or the product. For a brand that wants to be quoted by AI engines, the one fact per URL pattern matters. | High |
| Analytics / verification | No GA4, GTM, or Search Console tag in the page source. | High |
| Google Business Profile | Not created. The Profile Pack already reserves the Santa Clarita address for verification only and never publishes it: that is the correct service-area setup. | Medium |
| Social profiles | LinkedIn `/company/holguincompany`, YouTube `@holguincompany`, Facebook page dressed; Instagram claimed; X `@holguinandcompany`, Pinterest, TikTok staged. TikTok is connected to HighLevel under the raw handle `user4755468219169`. The HighLevel business profile has every social field empty. | Medium |
| HighLevel funnel "Holguin & Company" | One-page draft created 13 Sept, no domain attached. **Do not attach the domain to it**; the GoDaddy page is the site. Leave the funnel unpublished or delete it so two versions never compete. | Note |
| Owner authority | Forbes (2020), SWAGGER (2020), TEDxCondado talk, Cannabis Today podcast (2021), Mariposa (2022), Missouri Independent byline (Oct 2026), Marijuana Moment op-ed. Real, but all except LinkedIn and TEDx are cannabis-framed, and the Brand Book forbids any CannaShark or cannabis reference on Holguin & Company surfaces. | Decision (section 3) |

---

## 2. What is actually live (from the deploy source)

- **Page:** `https://holguincompany.com/`, title "Holguin & Company — Business Strategy & Execution, Beverly Hills", H1 "Strategy, executed."
- **Sections (all anchors):** hero with the three-step spine (01 Evaluate · 02 Diagnose · 03 Execute), the ninety-second film (self-hosted `holguin-company-vsl.mp4`), three testimonies (the founder's line; Kevin Doud; Bobby D. Pugh Sr., both "Client of the Principal"), The Diagnostic with the seven lenses and "what you leave with", The Principal (bio + facts panel: Founded 2026, Beverly Hills), six FAQs, the close with a LeadConnector booking iframe and a `mailto:` button, footer with the canonical NAP block.
- **JSON-LD graph:** ProfessionalService (`#firm`, address, phone, email, priceRange, knowsAbout, areaServed North America / Latin America / Europe), Person (`#principal`, name "Adrian A. Holguin", jobTitle "Founder & Managing Principal", no sameAs, no image, no credentials), Service (`#diagnostic`, AggregateOffer 5000–24000 USD), FAQPage (the same six questions), WebSite.
- **Brand constraints that govern every recommendation here** (Brand Book §VI): never "advisory"; never any CannaShark or cannabis reference; never a claim of industry breadth; the offer is always 01 The Business Evaluation Call · 02 The Diagnostic & 90-Day Roadmap · 03 Execute & Grow; the price line reads exactly "The Diagnostic scales with your company — $5,000 to $24,000+ — applied in full when we move to execution"; the founder's line appears once per surface; legal line "Adrian A. Holguin d/b/a Holguin & Company" until the LLC exists; domains holguincompany.com (primary) and holguinco.com (redirect).
- **HighLevel:** sub-account `hLql8kZCEo7GMT34NQdL`, phone +1 424-402-5670, email mail@holguincompany.com, 39 social posts published since 30 Sept across LinkedIn page, Instagram and Facebook (the "Ten Decisions" series and the "constraint" posts), all in brand voice, all pointing at holguincompany.com. Zero blog posts. No knowledge base.

---

## 3. The entity problem and the tether decision

The disambiguation problem is unchanged from Revision 1: three other people share the name in search and AI memory (the Southampton estate-management founder; a California "Holguin & Company, LLC" filed June 2025 under Michael Anthony Holguin; the Ecuador business coach on Brainz Magazine). Until the web carries a page that says who *this* Adrian A. Holguin is, AI engines will keep answering with the Hamptons firm.

Revision 1 proposed tethering the Forbes, SWAGGER, podcast, and Missouri Independent pieces to the Person entity on holguincompany.com. **That conflicts with the Brand Book**, which keeps the firm 100% free of CannaShark and cannabis references, including in materials. Your instruction was to tether where it helps and not where it hurts. The resolution:

**On holguincompany.com (strict):** the Person `#principal` gets `sameAs` → the LinkedIn profile, the LinkedIn company page, the YouTube channel, and the TEDxCondado talk (not cannabis-framed). Add `honorificSuffix: "J.D., M.B.A."`, `alumniOf` (University of San Francisco School of Law; University of San Francisco School of Management), and `image` → the founder portrait. Nothing else. The credentials and two alma maters alone separate you from every other Adrian Holguin in the graph.

**Off-site (the bridge):** LinkedIn is the one place both firms legitimately sit on one profile, and it is the page AI engines already return for your name. Keep the LinkedIn profile headline on Holguin & Company, keep CannaShark in Experience, and let the knowledge graph connect the two there. The Missouri Independent, Marijuana Moment, Forbes, and SWAGGER pages stay in CannaShark's entity (its site already links them). Do not add them to Holguin & Company's schema or copy.

**Never tether:** the Brainz contributor page, the Southampton profile, any "Holguin Companies" or "Holguin Estate Management" listing, intro.co unless confirmed.

---

## 4. Game plan (compressed: see `DAY-ZERO-RUNBOOK.md` for the one-sitting version)

### Phase 0 — This week, in GoDaddy and Google

1. **GoDaddy, DNS and hosting.** Confirm `holguincompany.com` and `www` both serve the page over HTTPS with one 301 from `www` to apex and from `http` to `https`. Confirm `holguinco.com` 301s to the apex (Brand Book §VIII). In File Manager, upload the three files from this folder: `robots.txt`, `sitemap.xml`, `llms.txt`.
2. **Search Console + Bing Webmaster.** Verify by DNS TXT record in GoDaddy (no page edit needed). Submit `https://holguincompany.com/sitemap.xml`. Request indexing of `/`. Bing feeds ChatGPT search.
3. **Analytics.** Add GA4 to the page head in the deploy source (`schema/head-additions.html` has the snippet slot) and redeploy.
4. **Google Business Profile.** Create as a service-area business, verify with the Santa Clarita address, hide the address, set the service area to Greater Los Angeles, category "Business management consultant", website holguincompany.com, phone 424-402-5670. Never publish the Santa Clarita address and never use the Santa Monica Blvd suite for verification (Google's rule on virtual offices). Then Bing Places and Apple Business Connect with the canonical NAP block from the Profile Pack.
5. **HighLevel.** Fill the social fields on the sub-account (values in `social-fields.md`); rename TikTok to `holguincompany`. Leave the HighLevel funnel unpublished.
6. **Name check.** Verify the June 2025 "Holguin & Company, LLC" filing at bizfileonline.sos.ca.gov. If it is not yours, file the LLC or a DBA now; the d/b/a line in the Brand Book assumes the name is free.

### Phase 1 — Weeks 1–3: schema patch and two new URLs

The page stays as designed. Three changes to the deploy source, then redeploy:

1. **Schema patch** (`schema/jsonld-patch.md`): `sameAs`, `logo`, `image` on `#firm`; `sameAs`, `honorificSuffix`, `alumniOf`, `image`, `email` on `#principal`; a `VideoObject` for the film; shorten the meta description to ≤155 characters.
2. **`/principal`** — the entity page. Draft in `pages/principal.md`. Same bio as the homepage plus credentials, education, the TEDx talk, the two client testimonies, and the disambiguation line. `ProfilePage` + `BreadcrumbList`. This is the URL every profile and byline will point to.
3. **`/the-diagnostic`** — the product page. Draft in `pages/the-diagnostic.md`. The seven lenses with a paragraph each, what you leave with, the price line, the FAQ. `Service` + `FAQPage` + `BreadcrumbList`. This is the URL that answers "what is a business performance diagnostic".

Optional, only if the content program in Phase 3 starts: `/insights` as a HighLevel blog on a subdomain or a static index on GoDaddy.

### Phase 2 — Weeks 2–8: citations that name the firm

The CannaShark PR routine is already pitching governance, lower-middle-market M&A, lean operations, and franchising podcasts (per the 15–25 October study passes) and tracking "Entity Named Correctly" and "AI-Citation Potential". Those shows are Holguin & Company's audience, not CannaShark's.

1. **Split the lane.** Add a column to the PR tracker: Brand = CannaShark | Holguin & Company. Any pitch to a non-cannabis outlet goes out as Adrian A. Holguin, Principal, Holguin & Company, with the `/principal` URL in the bio. Cannabis outlets stay CannaShark.
2. **Directories with the canonical block:** LinkedIn company page (done), Crunchbase person + organization, Clutch, Bing Places, Apple Business Connect, Beverly Hills Chamber. Reuse the Profile Pack long description verbatim.
3. **One byline a month** in a general-business outlet, on the firm's own vocabulary (the constraint, the seven lenses, the 90-day roadmap). Signed "Adrian A. Holguin, Principal, Holguin & Company".
4. **Wikidata, day one.** Two items (the person and the firm) from `WIKIDATA-ITEMS.md`, with Forbes, SWAGGER, TEDx and Missouri Independent as references. Read directly by Google's Knowledge Graph, Bing, Perplexity and others. Not Wikipedia.

Reviews are deliberately not part of this plan.

### Phase 3 — Weeks 3–12: content, in the voice already running

The social cadence (39 posts since 30 Sept) is the content engine; it just has no home URL. Two options:

- **Minimal:** keep posting; add the `/principal` link to every bio; nothing else.
- **Recommended:** two Insights pieces a month, each a longer version of a post that performed (the "If revenue doubled next quarter, what breaks first?" post is the model), answer-first, with the Person as author in schema, republished as a LinkedIn article. Topics map to the seven lenses, one lens per piece.

### Phase 4 — Monthly measurement

Search Console and Bing Webmaster for indexed pages and brand impressions, plus the five-prompt AI log (ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews): "Who is Adrian Holguin?", "What is Holguin & Company in Beverly Hills?", "Adrian A. Holguin J.D. M.B.A.", "business performance diagnostic consultant Los Angeles", "Who founded Holguin & Company?". Target at 60 days: prompts 1, 2, 3 and 5 return you and cite holguincompany.com.

---

## 5. What I could do from here, on request

- Produce the patched JSON-LD graph as a drop-in replacement for the `<script type="application/ld+json">` block (the patch is written; the merged block is a five-minute step).
- Produce `/principal` and `/the-diagnostic` as full HTML pages built from the site's own CSS, ready for File Manager.
- Republish the deploy-source artifact with the patch applied, if you want the artifact to stay canonical.

HighLevel writes (social fields) still need the `locations.write` scope on the connector.

---

## 6. Two-minute live check (run in a browser, since this session cannot)

1. `https://holguincompany.com/` loads over HTTPS; `http://` and `www.` each redirect once to it.
2. `https://holguincompany.com/robots.txt`, `/sitemap.xml`, `/llms.txt` load after upload.
3. `https://holguincompany.com/og-image.png` and `/favicon.svg` load.
4. View source: the JSON-LD block is present (search for `#principal`).
5. PageSpeed Insights, mobile: LCP under 2.5 s. If not, the self-hosted film is the first suspect; keep `preload="metadata"` and confirm the file is under ~15 MB.
6. Google: `site:holguincompany.com` returns the page within a week of submitting the sitemap.
