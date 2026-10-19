# Social media image sizing

Instagram (and Facebook/LinkedIn) feed posts can't be taller than 4:5.
Anything taller is center-cropped at publish time, cutting the top and
bottom off the artwork. The Business Health campaign art is 1024x1536 (2:3),
so about 17% of each image was being cut.

`tools/fit_social.py` fits the full image inside a target frame over a
blurred version of itself, so nothing is cropped:

    python3 tools/fit_social.py SRC.png OUT.png 1080 1350   # Instagram / Facebook / LinkedIn
    python3 tools/fit_social.py SRC.png OUT.png 1200 900    # Google Business Profile

Rule for every scheduled post: image must already be 4:5 (1080x1350) for
Instagram, Facebook and LinkedIn, and 4:3 (1200x900) for Google Business
Profile, before it goes into HighLevel's Social Planner.
