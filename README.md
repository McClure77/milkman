# The Milkman of St. Gaff's — website

Static site. No build step: `index.html`, `style.css`, `script.js`, plus assets.

## Publishing on GitHub Pages
1. Create a repo and upload everything in this folder (keep the folder structure).
2. Settings → Pages → Source: "Deploy from a branch" → `main` / `/ (root)`.
3. Wait a minute; the site appears at `https://<username>.github.io/<repo>/`.

## Custom domain
Add a file named `CNAME` at the root containing one line:

    howiemilkman.com

Then at your registrar point the domain at GitHub Pages:
- Four A records for `@`: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
- One CNAME record for `www` → `<username>.github.io`

Tick "Enforce HTTPS" in Settings → Pages once the certificate is issued.

## Adding fan art
Images live in `images/fanart/` as two sizes: `thumb/` (grid) and `full/` (lightbox).

Easiest route — put new originals in a folder and run:

    python3 tools/process.py

(edit the `SRC` path at the top of the script first). Then add one block per image
inside `<div class="gallery">` in `index.html`:

    <a href="images/fanart/full/NAME.jpg">
      <img src="images/fanart/thumb/NAME.jpg" loading="lazy" decoding="async" alt="Fan art for The Milkman of St. Gaff's">
    </a>

## External links used
- Listen (top bar, support section, footer) → https://linktr.ee/howiemilkman
- Support → https://www.patreon.com/cw/howiemilkman
- One time donation → https://ko-fi.com/howiemilkman
