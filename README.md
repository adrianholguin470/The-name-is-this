# Macro Polo

Food and recovery tracker for Adrian and Katie. The live app is a Claude Artifact:

https://claude.ai/artifact/YNW3ggSSi4RMyuVomw4ms9

`app/macro-polo.html` is the page source as published (the Artifact tool wraps it in the
document skeleton at publish time). Edits go through the artifact, not through this file;
this copy is here so the app has a home in the repository.

## Two profiles, one app

- The first time a phone opens the app it asks whose phone it is and remembers the answer.
  The toggle at the top switches, and the camera sheet shows who the photo is being logged for.
- Adrian's log lives at `data/users/<id>/root`, Katie's at `data/users/<id>/root-b`.
  Each holds `meals`, `labs`, `insights`, `settings/profile` and `days/<YYYY-MM-DD>`
  (`{water, moves:[ids]}`).
- Katie's profile runs in postpartum mode. Her settings doc carries
  `postpartum:{born, delivery, breastfeeding, cleared}`; the targets default to
  2,300 kcal / 95 g protein / 28 g fiber while breastfeeding (1,900 / 85 / 28 otherwise),
  and Claude's meal analysis is told she is N weeks postpartum.
- The Today screen opens with a suggestions card: for Katie, three daily movement picks
  (breath and pelvic floor, deep core, gentle yoga, nursing-posture stretches, walks) with a
  video to watch, a water counter and nutrition nudges; for Adrian, nudges from his numbers
  and bloodwork plus one movement pick.
