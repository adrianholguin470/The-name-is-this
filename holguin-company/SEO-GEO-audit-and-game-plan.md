# Holguin & Company — SEO + GEO audit and 90-day game plan

Prepared 2026-10-26 for Adrian Holguin, Founder & Managing Principal, Holguin & Company (Beverly Hills, CA).

Scope: holguincompany.com, the HighLevel sub-account that hosts it, the owner's existing author footprint, and the entity picture that Google and AI answer engines (ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews) currently hold.

Method note: this session's network policy blocks holguincompany.com, so the on-page audit of the live HTML (title, meta, H1, speed, schema) could not be run. Everything below comes from the HighLevel record of the site, search-index checks, and third-party listings. Section 7 is the on-page checklist to run the moment the host is reachable.

---

## 1. Executive summary

| Area | Status | Severity |
|---|---|---|
| Site indexed by Google / Bing | **No pages indexed.** Exact-domain search returns nothing. | Critical |
| Custom domain attached to the HighLevel site | **Not attached** (`domainId` empty on the funnel, `domain` empty on the sub-account). Whether holguincompany.com resolves to this site is unverified. | Critical |
| Site depth | **One page** ("Home", created 2026-09-13). No About, Services, Insights, or Contact pages. | Critical |
| Blog / Insights | None (HighLevel blog list is empty). | High |
| Structured data (Organization, Person, WebSite) | None known; nothing in the record. | High |
| Entity confusion in search and AI engines | **Severe.** "Adrian Holguin" + "Holguin Company" resolves to a different Adrian Holguin in Southampton, NY (holguin-companies.com, luxury estate management). | Critical for GEO |
| Google Business Profile for Holguin & Company | None. Address (9903 Santa Monica Blvd, STE 199) is a mailbox-style suite, which Google's policy makes ineligible unless staffed. | Medium (needs a decision, not a listing) |
| Social profiles | Facebook page, Instagram @holguincompany, LinkedIn company page, LinkedIn personal, Pinterest @holguincompany, YouTube @holguincompany, TikTok (unbranded handle `user4755468219169`). None are linked from the business profile; none are indexed yet. | Medium |
| Owner authority assets | Strong but unlinked: Forbes quote (2020), SWAGGER Magazine profile (2020), Cannabis Today podcast (2021), Mariposa Technology (2022), Missouri Independent author page and op-ed (Oct 2026), Marijuana Moment op-ed, CannaShark site bio, verified CannaShark Google Business Profile. | Opportunity |

The short version: Holguin & Company does not yet exist as an entity on the web. There is nothing for Google or an AI model to retrieve, and the name is already occupied in their memory by someone else. The plan therefore puts entity establishment and disambiguation ahead of classic keyword work.

---

## 2. What exists today (inventory)

### 2.1 Holguin & Company (from the HighLevel sub-account `hLql8kZCEo7GMT34NQdL`)

- Name: Holguin & Company
- Website field: https://holguincompany.com
- Address: 9903 Santa Monica Blvd, STE 199, Beverly Hills, CA 90212
- Phone: +1 424-402-5670
- Email: mail@holguincompany.com
- Created: 2026-09-13
- Site: one HighLevel "website" funnel named "Holguin & Company", one step "Home" at `/home`, `autoGenerateSchema: true`, no favicon URL, no head/body tracking code, no custom domain.
- Blogs: none.
- Business-profile social fields: all empty. `googlePlacesId`: empty.
- Connected social accounts (HighLevel Social Planner): Facebook page "Holguin & Company", Instagram `holguincompany`, LinkedIn page "Holguin & Company" (org 146545905), LinkedIn profile "Adrian Holguin", Pinterest `holguincompany`, YouTube `@holguincompany`, TikTok business `user4755468219169`.

### 2.2 CannaShark Consulting (sub-account `ei9azGLkgzf0iZFkQrJo`)

- Same address and owner. Website cannasharkconsulting.com.
- Verified Google Business Profile connected (location `18275021280132883975`).
- Connected: Facebook, Instagram `cannasharkconsulting`, LinkedIn profile "Adrian Holguin J.D., M.B.A.", LinkedIn page "CannaShark Cannabis Consulting", TikTok `adrianholguin93`, YouTube `@adrianholguin3936`.
- Indexed pages include: /about-us/, /cannabis-consulting-firm/, /licensing-regulatory-compliance/, /cannabis-licensing-consultant/, /cannabis-operations-consultant/, /expert-witness-services/, /proven-results-trusted-by-the-industry/. Third-party listings: Yelp, Alignable, MapQuest, ZoomInfo, LinkedIn company page, Issuu deck, YouTube welcome video.

### 2.3 Owner's existing third-party references (the "tether" candidates)

These are real, already published, and attributable to you. They are the raw material for the Person entity.

| Source | What it establishes | Link |
|---|---|---|
| LinkedIn profile | "Founder & Managing Principal"; Beverly Hills; strategy-to-execution positioning | https://www.linkedin.com/in/adrianholguin/ |
| CannaShark About page | Founder bio, J.D., M.B.A., strategy/finance/market entry/facility development | https://cannasharkconsulting.com/about-us/ |
| Forbes, 2020-10-03 (Paul Armstrong) | Quoted expert on AI in regulated cultivation | https://www.forbes.com/sites/paularmstrongtech/2020/10/03/big-issues-face-the-cannabis-industry-but-ai-is-here-to-help/ |
| SWAGGER Magazine, Nov 2020 | Founder profile | https://www.swaggermagazine.com/style/kings-of-swagger/california-cannabis-entrepreneur-adrian-holguin/ |
| Cannabis Today podcast, ep. 79 (2021) | Long-form interview | https://canna-today.com/2021/10/ep-79-w-adrian-holguin-from-cannashark-consulting/ |
| Mariposa Technology, Apr 2022 | Quoted as CEO | https://mariposatechnology.com/artificial-intelligence-in-hemp-growing-systems/ |
| Missouri Independent author page + Oct 2, 2026 commentary | Byline as "Adrian A. Holguin"; most recent authority signal | https://missouriindependent.com/author/adrianholguin/ |
| Marijuana Moment op-ed | Byline, contracts / microbusiness advice | https://www.marijuanamoment.net/advice-for-missouri-marijuana-microbusinesses-on-how-not-to-get-scammed-when-signing-contracts-op-ed/ |
| CannaShark LinkedIn company page | Organization entity | https://www.linkedin.com/company/cannashark-cannabis-consulting |

Do **not** tether these (they are other people with your name):

- Brainz Magazine "Adrian Holguin, Business & Life Coach" (food-industry entrepreneur, Ecuador).
- LinkedIn `adrian-holguin-148023234` "Founder & CEO at Holguin Companies" (Southampton, NY).
- Any Houzz, Angi, Nextdoor, or Facebook listing for "Holguin Companies" or "Holguin Estate Management".
- intro.co/AdrianHolguin unless you confirm it is yours.

---

## 3. The entity problem (why GEO comes first)

Searches run during this sweep:

- `"Holguin Company" holguincompany.com` → no result from your domain; returns Holguin & Holguin Inc, Holguin Consulting Inc, Holguin Group LLC, and others.
- `Adrian Holguin "Holguin Company"` → top result is the Southampton "Holguin Companies" LinkedIn profile.
- `"Holguin & Company" Beverly Hills` → your LinkedIn profile, plus a California filing for "Holguin & Company, LLC" (June 21, 2025, CEO listed as Michael Anthony Holguin, Sacramento address).
- `"holguincompany.com"` → nothing.
- Category queries (strategy execution consultant Los Angeles, fractional COO Beverly Hills) → no Holguin of any kind.

What this means for AI answer engines: when someone asks "Who is Adrian Holguin?" or "What is Holguin & Company?", the retrievable evidence points to the Hamptons estate-management firm. Your evidence (Forbes, Missouri Independent, LinkedIn) exists but is not connected to the name "Holguin & Company" anywhere on the web.

Three distinct name collisions to manage:

1. **Holguin Companies (Southampton, NY).** Same first and last name, same company name minus the ampersand, active site with reviews. This is the one AI models currently "know".
2. **Holguin & Company, LLC (California SOS, June 2025, Michael Anthony Holguin).** If this is your entity under a different registered manager, fine. If it is not, your legal/brand name collides inside the California registry. Verify at bizfileonline.sos.ca.gov (document B20250175407 per the directory listing).
3. **Adrian Holguin, Business & Life Coach (Brainz).** Different person, same name, same "coach/strategy" vocabulary.

Disambiguation strategy: make the *person* entity unambiguous (middle initial, credentials, city, two founded organizations, consistent headshot) and let the organization inherit from it. Every page, profile, and byline should use the same string: **Adrian A. Holguin, J.D., M.B.A., Founder & Managing Principal, Holguin & Company (Beverly Hills, CA)**, with "founder of CannaShark Consulting" as the second identifying fact.

---

## 4. The "tether" decision (your instruction, with the caveat)

You asked to tether reference articles to the owner where it helps, and to skip it where it would hurt. Here is the line:

**Tether the person, not the cannabis brand.**

- Put a Person schema on holguincompany.com with `sameAs` links to the LinkedIn profile, the Missouri Independent author page, the Forbes article, the SWAGGER profile, the podcast episode, and the CannaShark About page. These are facts about *you* and they carry the authority signals (major outlet, byline, credentials).
- Put `founder` → that same Person `@id` on both the Holguin & Company Organization schema and the CannaShark Organization schema. One person, two firms. This is accurate and it is exactly how knowledge graphs resolve ambiguity.
- Do **not** make Holguin & Company's own description, headline, or service pages about cannabis. The homepage positioning stays "strategy to disciplined execution for owners and leadership teams". Cannabis appears once, in the bio, as regulated-industry operating experience (licensing 100+ facilities is a CannaShark claim; cite it there, not on H&C service pages).
- Do **not** link the Brainz contributor page, the Southampton profile, or any listing you cannot confirm is yours. A wrong `sameAs` is worse than none: it teaches the graph the confusion you are trying to undo.

If you want a harder wall between the two brands, drop the CannaShark About page and the two cannabis-outlet op-eds from `sameAs` and keep LinkedIn, Forbes, and SWAGGER. The entity still resolves; it just resolves more slowly.

---

## 5. 90-day game plan

### Phase 0 — Lock the foundation (this week)

1. **Attach the domain.** In HighLevel: Sites → Domains → connect `holguincompany.com` and `www.holguincompany.com`, set one as primary (recommend non-www), confirm SSL, and set the "Holguin & Company" website as the default funnel for the domain. Then confirm in a browser that `https://holguincompany.com/` returns the Home page and `www` 301-redirects.
2. **Verify ownership in Google Search Console and Bing Webmaster Tools.** Bing matters because ChatGPT search reads Bing's index. Submit `/sitemap.xml` (HighLevel generates one for connected website domains; confirm it loads) and request indexing of every page.
3. **Fix the sub-account business profile.** Fill the empty social URL fields (Facebook, Instagram, LinkedIn, YouTube, Pinterest, TikTok) so HighLevel's auto-generated schema carries them. Rename the TikTok handle from `user4755468219169` to `holguincompany`.
4. **Resolve the California name collision.** Check the June 2025 "Holguin & Company, LLC" filing. If it is not yours, decide whether to register your own entity or DBA now, before the brand accumulates equity.
5. **Decide Google Business Profile.** Do not create one at the Santa Monica Blvd suite. Google's guidelines exclude virtual offices unless staffed during business hours, and a suspension there could spill onto the CannaShark profile at the same address. Options: (a) skip GBP for H&C and let LinkedIn + Bing Places + the CannaShark GBP carry local signals, or (b) if you have a real staffed or home office, create a service-area profile with the address hidden. Pick (a) unless (b) is true.
6. **Add analytics.** Put GA4 (and the Search Console link) in the funnel's head tracking code so the baseline starts now.

### Phase 1 — Make the site an entity home (weeks 1–3)

Expand from one page to a minimum viable site. Each page gets a unique title (≤60 chars), meta description (≤155), one H1, and a canonical.

| URL | Title | Job |
|---|---|---|
| `/` | Holguin & Company — Strategy to Execution for Owner-Led Companies | Thesis, who it is for, proof, one CTA |
| `/about-adrian-holguin` | Adrian A. Holguin, J.D., M.B.A. — Founder, Holguin & Company | **The person entity page.** Full bio, credentials, headshot, press list with links, both firms named |
| `/services/strategy-execution` | Strategy Execution Consulting | Answer-first: what it is, who, how, outcomes, FAQ |
| `/services/operating-cadence` (or your real second service) | Operating Cadence and Leadership Team Rhythm | Same pattern |
| `/services/business-performance-diagnostic` | Business Performance Diagnostic and 90-Day Roadmap | Same pattern (this service already exists on CannaShark; make the general-business version live here) |
| `/approach` | How Holguin & Company Works | The method, named steps, what a first 90 days looks like |
| `/insights` | Insights | Blog index |
| `/contact` | Contact Holguin & Company | Address, phone, email as text, form |

Add to every page:

- JSON-LD from `schema/organization.jsonld`, `schema/person-adrian-holguin.jsonld`, `schema/website.jsonld` (edit the placeholders, then paste into the HighLevel site-level head code). Add `BreadcrumbList` on inner pages and `FAQPage` on service pages.
- Open Graph and Twitter card tags with a real image.
- A footer with the full NAP string exactly as it appears in the HighLevel profile.

Add at the root:

- `llms.txt` (template in this folder) so AI crawlers get a clean summary and canonical links.
- `robots.txt` that allows Googlebot, Bingbot, GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, and Google-Extended. If HighLevel does not let you edit robots.txt, confirm it is not blocking these by default.

Cross-link the two brands:

- CannaShark About page: add one sentence and a link, "Adrian is also the founder of Holguin & Company, a strategy-execution advisory for owner-led companies."
- Holguin & Company About page: link back to cannasharkconsulting.com/about-us/.
- LinkedIn profile: add Holguin & Company as a current Experience entry with the website; set it as the headline company. LinkedIn company page: add website, tagline, and location.
- Every social bio (IG, YouTube, Pinterest, TikTok, Facebook): link to holguincompany.com and use the same one-line description.

### Phase 2 — Authority and citations (weeks 2–8)

AI engines cite third-party sources far more than owned pages. The goal is a dozen independent pages that say "Adrian A. Holguin, founder of Holguin & Company" within 60 days.

1. **Update bylines you control.** Ask Missouri Independent to update the author bio to include Holguin & Company. Do the same with Marijuana Moment and the Cannabis Today show notes. These are the fastest wins because the pages already rank.
2. **Directory and profile layer** (consistent NAP, same description, link to site): Crunchbase (person + organization), Clutch, Alignable (you already have a CannaShark listing), Bing Places, Apple Business Connect, LinkedIn company page, Beverly Hills Chamber of Commerce, LA Business Journal "Book of Lists" where applicable. Skip Yelp for H&C unless you want reviews there.
3. **Bylines in general-business outlets**, one per month, each signed "Adrian A. Holguin, founder of Holguin & Company": Entrepreneur, Fast Company Executive Board, Inc., Forbes Councils (paid), LA Business Journal op-ed. Topics should be the Holguin & Company thesis (execution discipline, operating cadence, owner-led growth), not cannabis.
4. **Podcasts**, one per month, with show notes that spell the name and link the site. Prior appearance on Cannabis Today is the proof-of-guest.
5. **Reviews and recommendations.** Request LinkedIn recommendations that name Holguin & Company. Ask three current or past clients for Clutch reviews. Keep Google reviews flowing on the CannaShark profile; it is the only verified Google entity you have.
6. **Wikidata (optional, 30 minutes).** Create an item for Adrian A. Holguin citing Forbes, SWAGGER, and Missouri Independent, with "founder of" Holguin & Company and CannaShark Consulting. Wikidata is read directly by several knowledge graphs. Do not attempt Wikipedia; the sourcing is not there yet.

### Phase 3 — Content engine (weeks 3–12, then ongoing)

Two Insights posts per month, written answer-first for the questions AI engines are asked. Each post: a one-paragraph direct answer at the top, a named author with Person schema, at least two cited statistics, one quoted expert (can be you), a dated "last updated" line, and an FAQ block. Then republish each as a LinkedIn article (LinkedIn articles are among the most-cited sources in AI answers) and a short YouTube explainer.

Starter topics mapped to intent:

| Query cluster | Post |
|---|---|
| "what is strategy execution consulting" | What a strategy-execution consultant actually does (and when you need one) |
| "fractional COO vs consultant" | Fractional COO or execution advisor: how owner-led companies should choose |
| "operating cadence small business" | The 90-day operating cadence: a template for leadership teams |
| "business performance diagnostic" | How to run a business performance diagnostic in 30 days |
| "why strategies fail to execute" | Why strategy fails in owner-led companies (with the numbers) |
| "regulated industry operations" | What regulated industries teach every operator about discipline (your bridge piece from CannaShark) |

Keyword volumes were not pulled in this sweep (no keyword tool reachable from this session). Validate with Google Keyword Planner or Ahrefs before committing, and prefer long-tail phrases where a new domain can rank.

### Phase 4 — Measure (monthly)

- Google Search Console: indexed pages, impressions for brand and service queries.
- Bing Webmaster: same.
- AI visibility log: once a month, ask ChatGPT, Perplexity, Gemini, Claude, and Google (AI Overview) these prompts and record the answer and the sources cited:
  1. "Who is Adrian Holguin?"
  2. "What is Holguin & Company in Beverly Hills?"
  3. "Adrian Holguin J.D. M.B.A. consultant"
  4. "Strategy execution consultant Los Angeles"
  5. "Who founded CannaShark Consulting?"
- Success at 60 days: prompts 1–3 return you, not the Southampton firm, and cite at least one page on holguincompany.com. Success at 90 days: prompt 4 mentions Holguin & Company at least once in one engine.

---

## 6. Quick wins I can execute on request

These are HighLevel writes and were not done without your go-ahead:

- Fill the six social URL fields on the Holguin & Company sub-account business profile.
- Add the JSON-LD and llms.txt to the site head / root once the domain is attached.
- Draft the eight pages above as copy you can paste into the HighLevel builder.
- Draft the updated Missouri Independent / Marijuana Moment author bio and the CannaShark cross-link sentence.

---

## 7. On-page checklist to run once the site is reachable

Run these against `https://holguincompany.com/` and each inner page:

- [ ] Returns 200; `www` redirects to non-www with a single 301; HTTP redirects to HTTPS.
- [ ] `<title>` unique per page, ≤60 characters, brand last.
- [ ] Meta description unique, ≤155 characters, includes the page's primary phrase.
- [ ] Exactly one `<h1>`; H2s outline the page.
- [ ] Canonical tag present and self-referencing.
- [ ] JSON-LD validates at validator.schema.org and Google Rich Results Test.
- [ ] Every image has descriptive alt text; hero image under 200 KB; modern format.
- [ ] Core Web Vitals in PageSpeed Insights: LCP under 2.5 s on mobile, CLS under 0.1.
- [ ] No render-blocking third-party scripts from HighLevel widgets you do not use (chat widget is off; keep it off until needed).
- [ ] Favicon present (currently empty in the funnel record).
- [ ] `/sitemap.xml` and `/robots.txt` load and are correct.
- [ ] Phone, email, and address appear as text (not images) and match the HighLevel profile exactly.
- [ ] Internal links: every page reachable within two clicks of Home; About page linked from the header or footer on every page.

---

## 8. Sources consulted

- HighLevel API: sub-accounts `hLql8kZCEo7GMT34NQdL` (Holguin & Company) and `ei9azGLkgzf0iZFkQrJo` (CannaShark Consulting Group), funnels, blogs, Social Planner accounts.
- Google guidance on virtual offices and service-area businesses: https://support.google.com/business/answer/3038177
- Third-party listings and press: see tables in sections 2.3 and 3.
