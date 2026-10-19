"""Fit an image into a target aspect ratio WITHOUT cropping.
The full source image is scaled to fit inside the frame and centered over a
blurred, darkened, edge-to-edge version of itself, so no content is lost."""
import sys
from PIL import Image, ImageFilter, ImageEnhance

def fit(src, dst, W, H, blur=40, dim=0.55):
    im = Image.open(src).convert("RGB")
    # background: cover-fill, blur, dim
    scale = max(W / im.width, H / im.height)
    bg = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    bg = bg.crop(((bg.width - W) // 2, (bg.height - H) // 2, (bg.width - W) // 2 + W, (bg.height - H) // 2 + H))
    bg = bg.filter(ImageFilter.GaussianBlur(blur))
    bg = ImageEnhance.Brightness(bg).enhance(dim)
    # foreground: contain-fit
    scale = min(W / im.width, H / im.height)
    fg = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    bg.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2))
    bg.save(dst, "PNG", optimize=True)
    print(dst, bg.size, "fg", fg.size)

if __name__ == "__main__":
    src, dst, W, H = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    fit(src, dst, W, H)
