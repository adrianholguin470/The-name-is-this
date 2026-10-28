# JSON-LD patch for the live page

The page already has a `@graph` with `#firm`, `#principal`, `#diagnostic`, `#faq`, `#website`. Keep those `@id`s. Merge the properties below into the existing objects; do not add a second Organization or Person. Validate at validator.schema.org before deploying.

## Into `ProfessionalService` `#firm`
```json
"logo": { "@type": "ImageObject", "url": "https://holguincompany.com/REPLACE-wordmark-on-ink.png" },
"image": "https://holguincompany.com/og-image.png",
"foundingDate": "2026",
"sameAs": [
  "https://www.linkedin.com/company/holguincompany/",
  "https://www.youtube.com/@holguincompany",
  "https://www.instagram.com/holguincompany/",
  "https://www.pinterest.com/holguincompany/",
  "https://x.com/holguinandcompany",
  "https://www.facebook.com/profile.php?id=61594142139403"
]
```

## Into `Person` `#principal`
```json
"givenName": "Adrian",
"familyName": "Holguin",
"honorificSuffix": "J.D., M.B.A.",
"image": "https://holguincompany.com/REPLACE-adrian-holguin-portrait.jpg",
"email": "mail@holguincompany.com",
"url": "https://holguincompany.com/principal",
"alumniOf": [
  { "@type": "CollegeOrUniversity", "name": "University of San Francisco School of Law" },
  { "@type": "CollegeOrUniversity", "name": "University of San Francisco School of Management" }
],
"knowsLanguage": ["en", "es"],
"sameAs": [
  "https://www.linkedin.com/in/adrianholguin/",
  "https://www.youtube.com/watch?v=mjZhCb7-uQs"
]
```
The YouTube link is the TEDxCondado talk. No CannaShark or cannabis-framed URL goes in this list (Brand Book §VI). LinkedIn carries that connection off-site.

## New node: the film
```json
{
  "@type": "VideoObject",
  "@id": "https://holguincompany.com/#film",
  "name": "Holguin & Company — The Firm, In Ninety Seconds",
  "description": "A ninety-second introduction to Holguin & Company: the evaluation call, the Diagnostic across seven lenses, and Execute & Grow.",
  "thumbnailUrl": "https://holguincompany.com/og-image.png",
  "contentUrl": "https://holguincompany.com/holguin-company-vsl.mp4",
  "uploadDate": "2026-10-15",
  "duration": "PT1M30S",
  "publisher": { "@id": "https://holguincompany.com/#firm" }
}
```

## Meta description (replace; 149 characters)
`Holguin & Company, Beverly Hills: a private strategy and execution firm. One diagnostic across seven lenses, a 90-day roadmap, principal-led execution.`

## Head additions
```html
<!-- GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-REPLACE"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag('js',new Date());gtag('config','G-REPLACE');</script>
```
Search Console and Bing are verified by DNS TXT in GoDaddy; no meta tag needed.

The three standalone files in this folder (`organization.jsonld`, `person-adrian-holguin.jsonld`, `website.jsonld`) were written before the live graph was known. They are superseded by this patch; use them only as a reference for a page that does not already carry the graph.
