# SDVsolution — website

Static marketing site for **sdvsolution.com** (single file, no build step, no dependencies).

## Contents
- `index.html` — the site.
- `.nojekyll` — tells GitHub Pages to serve files as-is (skip Jekyll).
- `CNAME` — custom domain for GitHub Pages (`sdvsolution.com`).
- `terms.html` · `privacy.html` — legal pages (linked from the footer; template — have counsel review).

## Deploy on GitHub Pages

1. Create a repo (e.g. `sdvsolution-site`) and upload these files to the repo **root** (keep `index.html`, `.nojekyll`, `CNAME`).
   - CLI:
     ```
     git init
     git add .
     git commit -m "SDVsolution website"
     git branch -M main
     git remote add origin https://github.com/<you>/sdvsolution-site.git
     git push -u origin main
     ```
2. Repo → **Settings → Pages** → Source: **Deploy from a branch** → Branch: `main` / folder `/ (root)` → **Save**.
3. Wait ~1–2 min. Your site publishes at `https://<you>.github.io/sdvsolution-site/` (or at the custom domain once DNS is set).

## Point the Squarespace domain at GitHub Pages

In **Squarespace → Settings → Domains → sdvsolution.com → DNS settings**, add:

- Apex `sdvsolution.com` — four **A** records to GitHub Pages:
  ```
  185.199.108.153
  185.199.109.153
  185.199.110.153
  185.199.111.153
  ```
  (optional IPv6 **AAAA**: 2606:50c0:8000::153, :8001::153, :8002::153, :8003::153)
- `www` — a **CNAME** to `<you>.github.io.`

> Verify the current GitHub Pages IPs in GitHub's docs before entering them (they rarely change but always confirm).

Then in **Settings → Pages** set **Custom domain** = `sdvsolution.com`, tick **Enforce HTTPS** once the certificate is issued (can take up to ~24 h after DNS propagates).

## Connect the "Book a demo" form (Formspree)

The demo form is wired for **Formspree** (works on static hosts like GitHub Pages):

1. Create a free account at formspree.io and add a new form; it gives you an endpoint like `https://formspree.io/f/abcdwxyz`.
2. In `index.html`, replace `https://formspree.io/f/yourFormID` (the `action` on `<form id="demoForm">`) with your endpoint.
3. Submissions are sent by AJAX; the page shows an inline "Thanks…" message (no redirect). A honeypot field (`_gotcha`) reduces spam.
4. Until you set the endpoint, submitting shows a "not connected yet" note instead of failing silently.

Prefer email only? Replace the form with `<a href="mailto:hello@sdvsolution.com">`. Other backends (Getform, Basin, Netlify Forms) work the same way — just change the `action`.

## Before launch — wire these links in `index.html`
- **Start free trial / Choose plan** buttons → your app sign-up URL.
- **Login** → your app login URL.
- **Book a demo** → a form or `mailto:hello@sdvsolution.com`.
- **Terms / Privacy / Security** footer links → real pages.

## Edit
It's one file — open `index.html` and edit text/colors inline. Colors are CSS variables at the top of the `<style>` block.
