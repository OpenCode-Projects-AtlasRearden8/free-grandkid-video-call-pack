# The Free Grandkid Video Call Pack

A free printable pack for staying close to your grandkids over video calls. It bundles warm, ready-to-print PDFs — invitation cards, conversation starters, shared activity ideas, keeper notes, and a call reminder sheet — plus a small index site to guide people to each printable.

Everything is designed to be printed, cut, and used the same afternoon. No accounts, no sign-up, and no personal data: the PDFs collect nothing and are filled in by hand after printing.

## What's inside

| Printable | Pages | What it does |
| --- | --- | --- |
| [`call-invitation-cards.pdf`](pdfs/call-invitation-cards.pdf) | 1 | Four cut-out invitation cards with fill-in blanks for day, time, and place |
| [`conversation-starters-ages-5-12.pdf`](pdfs/conversation-starters-ages-5-12.pdf) | 2 | 24 snip-apart question strips for the 5–12 crowd |
| [`conversation-starters-teens.pdf`](pdfs/conversation-starters-teens.pdf) | 2 | 24 question strips made for teenagers — their shows, wins, and plans |
| [`shared-activity-ideas.pdf`](pdfs/shared-activity-ideas.pdf) | 2 | Read-alouds, story chains, show-and-tell, and quick screen-friendly games |
| [`keeper-notes-page.pdf`](pdfs/keeper-notes-page.pdf) | 1 | A planning page: the next call, what to have ready, and jokes worth keeping |
| [`call-reminder-sheet.pdf`](pdfs/call-reminder-sheet.pdf) | 1 | Pick a call rhythm and check the boxes each month so calls never slip away |

This pack pairs nicely with (but is completely independent of) a tech-setup manual — it deliberately skips all the "how to press the buttons" stuff and focuses on the *what to do once you're connected* part.

## How to use it

1. Print any PDF on US Letter (prints fine on A4 with *fit to page* selected).
2. Cut the invitation cards and conversation strips along the dashed lines.
3. Keep the keeper notes and reminder sheet near the computer, and start every call with one conversation strip.
4. Open [`site/index.html`](site/index.html) in a browser for a friendly front door to the pack.

## Regenerating the PDFs

The PDFs are generated with Python and [ReportLab](https://www.reportlab.com/):

```bash
python3 -m pip install -r requirements.txt
python3 build.py
```

Built PDFs land in `pdfs/`, along with a `manifest.json` listing what was generated.

## Serving the site

The site is plain HTML and CSS with relative links to the PDFs, so any static server works:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000/site/`. Opening `site/index.html` directly from your file manager works too.

## Privacy

There is nothing to collect here. The PDFs and site are static, contain no scripts, no trackers, and no personal data. Any names, dates, or details you write onto the printables stay in your home.

## Credits and license

This pack is brought to you by **Asdale Dynamics, LLC** — beginner-friendly AI books, guides, and practical tools, explained like a friend would. Find more at [dylanasdale.github.io](https://dylanasdale.github.io) and in *The Massive AI Manual* by Dylan Asdale.

Licensed under the MIT License — see [LICENSE](LICENSE).
