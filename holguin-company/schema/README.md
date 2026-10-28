# Schema files for holguincompany.com

Three JSON-LD blocks. Replace every `REPLACE-` placeholder, validate at https://validator.schema.org and https://search.google.com/test/rich-results, then paste each into a `<script type="application/ld+json">` tag in the HighLevel site-level head tracking code (Sites → the website → Settings → Tracking code → Head).

- `organization.jsonld` — the firm. `@id` is `https://holguincompany.com/#organization`.
- `person-adrian-holguin.jsonld` — the founder. `@id` is `https://holguincompany.com/about-adrian-holguin#person`. The `sameAs` list is the owner "tether": only links that are verifiably you. Do not add the Brainz Magazine contributor page or anything for "Holguin Companies" (Southampton, NY).
- `website.jsonld` — the site, pointing to the organization.

Mirror on cannasharkconsulting.com: give its Organization schema `"founder": { "@id": "https://holguincompany.com/about-adrian-holguin#person" }` so both firms resolve to one person.

Per-page additions (not included here): `BreadcrumbList` on every inner page, `FAQPage` on each service page, `Article` with `author` → the Person `@id` on every Insights post.
