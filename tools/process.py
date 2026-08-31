import os, json, hashlib
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None

SRC = "/home/claude/work/FAN ART"
OUT = "/home/claude/milkman/images/fanart"

seen = {}
files = sorted(os.listdir(SRC))
manifest = []

for f in files:
    p = os.path.join(SRC, f)
    if not os.path.isfile(p):
        continue
    h = hashlib.md5(open(p, "rb").read()).hexdigest()
    if h in seen:
        print("skip dup:", f, "->", seen[h])
        continue
    seen[h] = f

    slug = os.path.splitext(f)[0]
    slug = "".join(c if c.isalnum() else "-" for c in slug).strip("-").lower()
    slug = "-".join(x for x in slug.split("-") if x)[:48]

    im = Image.open(p)
    im = ImageOps.exif_transpose(im)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        im = Image.alpha_composite(bg, im)
    im = im.convert("RGB")

    full = im.copy()
    full.thumbnail((1600, 1600), Image.LANCZOS)
    full.save(f"{OUT}/full/{slug}.jpg", "JPEG", quality=82, optimize=True, progressive=True)

    thumb = im.copy()
    thumb.thumbnail((700, 700), Image.LANCZOS)
    thumb.save(f"{OUT}/thumb/{slug}.jpg", "JPEG", quality=78, optimize=True, progressive=True)

    manifest.append({"slug": slug, "w": thumb.size[0], "h": thumb.size[1]})

json.dump(manifest, open("/home/claude/work/fanart.json", "w"), indent=1)
print("processed", len(manifest))
