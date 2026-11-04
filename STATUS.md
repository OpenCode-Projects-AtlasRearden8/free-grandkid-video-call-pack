# STATUS — Free Grandkid Video Call Pack

## What was built

A free printable pack for staying close to grandkids over video calls, with six generated PDFs and a small static index site. Built for Asdale Dynamics, LLC (copyright (c) 2026 Asdale Dynamics, LLC, MIT License).

- `build.py` — one Python script (ReportLab) that generates every PDF deterministically.
- `pdfs/` — the six printables plus a `manifest.json` recording what was generated:
  - `call-invitation-cards.pdf` (1 page) — four cut-out invitation cards with fill-in blanks for day, time, and place.
  - `conversation-starters-ages-5-12.pdf` (2 pages) — 24 snip-apart question strips, ages 5–12.
  - `conversation-starters-teens.pdf` (2 pages) — 24 question strips written for teens.
  - `shared-activity-ideas.pdf` (2 pages) — read-alouds, story chains, show-and-tell, and quick screen-friendly games.
  - `keeper-notes-page.pdf` (1 page) — call-planning page: next call details, things to have ready, notes to keep.
  - `call-reminder-sheet.pdf` (1 page) — recurring-call rhythm planner plus a 12-month checkbox grid.
- `site/` — static index site (`index.html` + `styles.css`) linking every PDF, with usage steps, friendly calling tips, and an Asdale Dynamics, LLC credit. Plain HTML/CSS, relative links, no scripts, no trackers, no personal data.
- `README.md`, `LICENSE` (MIT, copyright line "Copyright (c) 2026 Asdale Dynamics, LLC"), `requirements.txt`.

## How to run it

Regenerate the PDFs (US Letter; they print on A4 with *fit to page*):

```bash
python3 -m pip install -r requirements.txt
python3 build.py
```

Serve or open the site (also works by double-clicking `site/index.html`):

```bash
python3 -m http.server 8000
# then visit http://localhost:8000/site/
```

## Verification results

- `python3 build.py` runs clean from an empty `pdfs/` directory and writes all six PDFs plus `manifest.json`.
- Rebuilt from scratch, then checked with `pypdf`: every PDF opens, has the expected page count, contains extractable text, and carries the Asdale Dynamics, LLC footer.

```
pdfs/call-invitation-cards.pdf: pages=1
pdfs/call-reminder-sheet.pdf: pages=1
pdfs/conversation-starters-ages-5-12.pdf: pages=2
pdfs/conversation-starters-teens.pdf: pages=2
pdfs/keeper-notes-page.pdf: pages=1
pdfs/shared-activity-ideas.pdf: pages=2
ALL PDF CHECKS PASS
```

- All 6 pages rendered to images with `pdftoppm` and visually inspected. Initial layout overflows on the cards, keeper-notes, and reminder pages were found and fixed (card height reduced, month-grid cell height reduced, keeper-notes line counts reduced, sun doodle no longer overlaps card headlines).
- Site link checker: 8 links checked (6 PDF links, stylesheet, external hub site), zero broken relative links.
- Static server test on a fresh port: `site/`, `styles.css`, and all six PDF paths return HTTP 200.
- `LICENSE` copyright line verified byte-for-byte as `Copyright (c) 2026 Asdale Dynamics, LLC`.
- No secrets, API keys, or personal data in any file; PDFs and site are static with no collection of any kind.

## Known gaps

- PDFs are tuned for US Letter; A4 printing works via "fit to page" but there are no separate A4-native layouts.
- The invitation cards use fill-in blanks only — no personalized pre-filled name variants (deliberate, for privacy and simplicity).
- The index site is intentionally script-free, so there is no dark-mode toggle or search; it is a single warm landing page.
- Print-at-home cutting of the strips has no guaranteed bleed margins beyond the dashed guides; a paper trimmer gives the cleanest results.
