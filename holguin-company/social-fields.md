# Social fields for the Holguin & Company sub-account

HighLevel → Holguin & Company sub-account → Settings → Business Profile → "Social" section. Paste exactly. These are the accounts already connected in Social Planner, so the handles are confirmed; only the Facebook vanity URL and LinkedIn slug are not yet set and use the numeric ID form, which resolves correctly.

| Field | Value |
|---|---|
| Facebook | https://www.facebook.com/1230439726830382 |
| Instagram | https://www.instagram.com/holguincompany/ |
| LinkedIn | https://www.linkedin.com/company/146545905/ |
| YouTube | https://www.youtube.com/@holguincompany |
| Pinterest | https://www.pinterest.com/holguincompany/ |
| Twitter / X | (leave empty; no account) |
| Yelp | (leave empty; see plan, section 5 Phase 0) |
| Google Places ID | (leave empty; no Google Business Profile by design) |
| Blog RSS | https://holguincompany.com/insights/rss.xml once Insights is live in HighLevel Blogs |

Also do, in the same session:

- TikTok: rename the business account from `user4755468219169` to `holguincompany` inside TikTok, then reconnect it in Social Planner so the new handle shows.
- Facebook page: set a vanity username `holguincompany` (Page settings → Username), then replace the numeric URL above with https://www.facebook.com/holguincompany.
- LinkedIn company page: set the public URL slug to `holguin-company` (Admin → Edit page → Public URL), then replace the numeric URL above with https://www.linkedin.com/company/holguin-company/. Update `schema/organization.jsonld` `sameAs` to match.

Why this session could not write them: the HighLevel connection used here is scoped for reading sub-account settings but not for updating them (the `locations.write` scope is not granted to the connector). Granting that scope on the connector would let it be done from here next time.
