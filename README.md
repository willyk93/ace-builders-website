# Ace Builders of Canada Ltd. — Website

A 6-page static website for Ace Builders of Canada Ltd. (Edmonton, AB), built from the
company's business plan: Home, About, Services, Projects, Certifications, and Contact.

## Structure

```
index.html              Home
about.html               About / mission / vision / leadership
services.html            The 4 core service lines
projects.html            Project types / capabilities showcase
certifications.html      COR / WCB / WHMIS / First Aid
contact.html             Contact form + info + map
assets/
  css/style.css          Shared stylesheet (all colors as CSS variables at the top)
  js/script.js           Mobile nav toggle + contact form handling
  img/                   Logo, favicons, /illustrations (custom SVG artwork), /photos (real site photography)
generate_site.py         Regenerates all HTML pages from the shared header/footer/nav
pages.py                 Editable page content (edit here, then re-run generate_site.py)
icons.py                 Inline SVG icon library used throughout the site
gen_illustrations.py     Regenerates the custom brand-colored SVG illustrations
```

## Design system (v3)

The palette is green + cream only (no red) — see the CSS variables at the top of
`assets/css/style.css` (`--forest-*` greens, `--sage-*` and `--cream-*`/`--tan-300`
neutrals). All icons are inline SVGs from `icons.py` (no emoji).

Real photography is now wired in throughout (`assets/img/photos/`) — the Home hero and
Projects page-hero use a photo with a green gradient overlay for text contrast (see the
`photo_bg()` helper in `pages.py`), the 4 Services sections and Certifications page each
have a photo, the 6 Projects cards have a photo with a small icon badge, and the CTA
bands site-wide share one background photo. The original SVG illustrations are still in
`assets/img/illustrations/` (regenerate via `gen_illustrations.py`) in case you ever want
to fall back to the illustrated look for a section.

Founder identity is intentionally kept out of the site for now — the About page's
leadership cards show role titles only with a generic icon, no names or photos of
specific individuals.

## How to preview it locally

From this folder, run:

```
python3 -m http.server 8000
```

Then open http://localhost:8000 in your browser.

## How to edit content

The header, footer, and navigation are shared templates so they stay identical across
every page. To change page text/sections, edit `pages.py`, then regenerate the HTML:

```
python3 generate_site.py
```

Do not hand-edit the `<header>`/`<footer>` inside the .html files directly — those edits
will be overwritten next time you regenerate. If you don't plan to touch the content
again, you can safely ignore `generate_site.py`/`pages.py` and just edit the .html files
directly going forward.

## Before you launch — a few placeholders to confirm

- **Email address**: the site currently uses `info@acebuilderscan.com` (based on the
  domain in the business plan). Confirm this inbox exists/is monitored, or swap it site-wide.
- **Business hours**: set to Mon–Fri, 8:00 AM–5:00 PM MT as a placeholder — update if different.
- **Street address**: no specific office address was provided, so the map on the Contact
  page centers on Edmonton generally. Add a specific address if you want a pinned location.
- **Social links**: the footer icons (LinkedIn/Facebook/Instagram) currently point to `#`.
  Add real profile URLs once created.
- **Contact form**: pre-wired for **Netlify Forms** (`data-netlify="true"`), which works
  automatically if you host on Netlify — no code needed. If you host elsewhere (GitHub
  Pages, your own server, etc.), connect a service like Formspree or EmailJS: replace the
  form's `action`/attributes per that service's docs, and remove the `preventDefault`
  branch in `assets/js/script.js`.

## Swapping in different photography later

To replace any photo, just swap the `<img src>` (in a `.photo-block` or `.project-visual`)
or the filename inside a `photo_bg('filename.jpg')` call in `pages.py`, for example:

```html
<div class="photo-block">
  <img src="assets/img/photos/abatement-crew.jpg" alt="Ace Builders crew performing hazardous abatement">
</div>
```

`object-fit: cover` is already applied everywhere, so any reasonably landscape photo will
crop in cleanly. Drop new files into `assets/img/photos/`, update the reference, then run
`python3 generate_site.py` if you're editing `pages.py` (or just edit the .html directly
for a one-off swap).

One photo from the original batch — `home-renovation-interior2.jpg` — wasn't used (it's a
near-duplicate of `home-renovation-interior.jpg`, which is already on the Projects page).
It's still in `assets/img/photos/` if you'd like it placed somewhere.

## Deploying

This is a fully static site — no build step required. Drag-and-drop the whole folder into
Netlify, Vercel, or GitHub Pages, or upload via FTP to any standard web host.
