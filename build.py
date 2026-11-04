"""Builds the printable PDFs for the Free Grandkid Video Call Pack."""

import json
import os

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "pdfs")

W, H = letter

CREAM = HexColor("#FDF6EC")
PAPER = HexColor("#FFFFFF")
RUST = HexColor("#B85C38")
RUST_SOFT = HexColor("#E8A87C")
COCOA = HexColor("#5B4636")
GRANITE = HexColor("#8A7A6E")
LINE = HexColor("#C9B4A0")
TEAL = HexColor("#4E7A6A")
TEAL_SOFT = HexColor("#A7C4BC")
PLUM = HexColor("#6D4C5B")
PLUM_SOFT = HexColor("#C3A5B0")
GOLD = HexColor("#E0A100")

FOOTER_TEXT = (
    "The Free Grandkid Video Call Pack  \u2022  a free printable from "
    "Asdale Dynamics, LLC  \u2022  dylanasdale.github.io"
)


def footer(c):
    c.setFont("Helvetica", 8.5)
    c.setFillColor(GRANITE)
    c.drawCentredString(W / 2.0, 26, FOOTER_TEXT)


def banner(c, title, subtitle):
    bx, by, bw, bh = 43, H - 122, W - 86, 64
    c.setFillColor(CREAM)
    c.setStrokeColor(LINE)
    c.roundRect(bx, by, bw, bh, 12, stroke=1, fill=1)
    c.setFillColor(COCOA)
    c.setFont("Helvetica-Bold", 21)
    c.drawCentredString(W / 2.0, by + 39, title)
    c.setFillColor(GRANITE)
    c.setFont("Helvetica-Oblique", 11)
    c.drawCentredString(W / 2.0, by + 17, subtitle)


def heart(c, x, y, s, fill=RUST):
    c.setFillColor(fill)
    p = c.beginPath()
    p.moveTo(x, y)
    p.curveTo(x - s * 0.9, y + s * 0.9, x - s, y - s * 0.5, x, y - s * 1.5)
    p.curveTo(x + s, y - s * 0.5, x + s * 0.9, y + s * 0.9, x, y)
    c.drawPath(p, stroke=0, fill=1)


def sun(c, x, y, r, fill=GOLD):
    c.setFillColor(fill)
    c.circle(x, y, r, stroke=0, fill=1)
    c.setStrokeColor(fill)
    c.setLineWidth(1.6)
    for i in range(8):
        import math

        a = i * (math.pi / 4)
        x1 = x + math.cos(a) * (r + 3)
        y1 = y + math.sin(a) * (r + 3)
        x2 = x + math.cos(a) * (r + 8)
        y2 = y + math.sin(a) * (r + 8)
        c.line(x1, y1, x2, y2)


def wrap(text, font, size, maxw):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        test = (cur + " " + word).strip()
        if stringWidth(test, font, size) <= maxw:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def ruled_line(c, x1, x2, y, color=LINE):
    c.setStrokeColor(color)
    c.setLineWidth(0.8)
    c.line(x1, y, x2, y)


def check_square(c, x, y, s=11):
    c.setStrokeColor(COCOA)
    c.setFillColor(PAPER)
    c.setLineWidth(1)
    c.rect(x, y, s, s, stroke=1, fill=1)


def new_canvas(path, title):
    c = canvas.Canvas(path, pagesize=letter)
    c.setTitle(title)
    c.setAuthor("Asdale Dynamics, LLC")
    c.setSubject("Free Grandkid Video Call Pack")
    return c


def start_page(c, doc_title, page_title, page_subtitle):
    banner(c, page_title, page_subtitle)
    c.setFillColor(PAPER)
    footer(c)


def invitation_cards(path):
    c = new_canvas(path, "Call Invitation Cards")
    start_page(c, "invitation-cards", "Call Invitation Cards", "cut, fill out, and send a little surprise of sunshine")

    layouts = [
        ("You're invited!", RUST, RUST_SOFT),
        ("Video call time!", TEAL, TEAL_SOFT),
        ("You're invited!", PLUM, PLUM_SOFT),
        ("Video call time!", RUST, RUST_SOFT),
    ]
    cw, ch = 251, 270
    xs = [43, 43 + cw + 24]
    ytop = H - 150
    for i, (headline, main, soft) in enumerate(layouts):
        row, col = divmod(i, 2)
        x = xs[col]
        y = ytop - row * (ch + 22) - ch
        c.setStrokeColor(LINE)
        c.setDash(4, 3)
        c.setLineWidth(1)
        c.roundRect(x - 6, y - 6, cw + 12, ch + 12, 10, stroke=1, fill=0)
        c.setDash()
        c.setFillColor(CREAM)
        c.setStrokeColor(main)
        c.setLineWidth(2)
        c.roundRect(x, y, cw, ch, 10, stroke=1, fill=1)

        cx = x + cw / 2.0
        sun(c, cx, y + ch - 24, 9)
        c.setFillColor(main)
        c.setFont("Helvetica-Bold", 19)
        c.drawCentredString(cx, y + ch - 64, headline)
        c.setFillColor(COCOA)
        c.setFont("Helvetica", 12.5)
        c.drawCentredString(cx, y + ch - 84, "to a cozy video call with")
        ruled_line(c, x + 40, x + cw - 40, y + ch - 96, main)

        labels = [("Day", "day"), ("Time", "time"), ("Where", "where we chat")]
        ly = y + ch - 120
        for label, hint in labels:
            c.setFillColor(GRANITE)
            c.setFont("Helvetica", 10)
            c.drawString(x + 34, ly + 4, label + ":")
            c.setStrokeColor(LINE)
            c.setLineWidth(0.9)
            c.line(x + 78, ly, x + cw - 34, ly)
            c.setFont("Helvetica-Oblique", 7.5)
            c.drawRightString(x + cw - 36, ly + 3, hint)
            ly -= 26

        c.setFillColor(COCOA)
        c.setFont("Helvetica-Oblique", 12)
        c.drawCentredString(cx, ly - 6, "Can't wait to see your smile!")
        heart(c, cx, ly - 28, 8, main)
        ruled_line(c, x + 60, cx - 16, y + 26, LINE)
        c.setFont("Helvetica", 10.5)
        c.drawString(x + 62, y + 30, "Love,")
    c.showPage()
    c.save()


def starter_strips(path, doc_title, page_title, subtitle, items, accent, soft):
    c = new_canvas(path, doc_title)
    per_page = 12
    pages = (len(items) + per_page - 1) // per_page
    sw, sh, gap_x, gap_y = 251, 86, 24, 16
    xs = [43, 43 + sw + gap_x]
    ytop = H - 150
    for page in range(pages):
        start_page(c, doc_title, page_title, subtitle)
        chunk = items[page * per_page : (page + 1) * per_page]
        for i, text in enumerate(chunk):
            row, col = divmod(i, 2)
            x = xs[col]
            y = ytop - row * (sh + gap_y) - sh
            c.setStrokeColor(LINE)
            c.setDash(3, 3)
            c.setLineWidth(0.9)
            c.line(x, y + sh + 8, x + sw, y + sh + 8)
            c.setDash()
            c.setFillColor(CREAM)
            c.setStrokeColor(soft)
            c.setLineWidth(1.4)
            c.roundRect(x, y, sw, sh, 8, stroke=1, fill=1)
            c.setFillColor(accent)
            c.roundRect(x, y, 18, sh, 8, stroke=0, fill=1)
            c.rect(x + 12, y, 6, sh, stroke=0, fill=1)
            c.setFillColor(PAPER)
            num = "%02d" % (page * per_page + i + 1)
            c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(x + 9, y + sh / 2.0 - 3, num)
            lines = wrap(text, "Helvetica", 11.5, sw - 46)
            total_h = len(lines) * 15
            ty = y + sh / 2.0 + total_h / 2.0 - 10
            c.setFillColor(COCOA)
            c.setFont("Helvetica", 11.5)
            for line in lines:
                c.drawString(x + 30, ty, line)
                ty -= 15
        if page < pages - 1:
            c.showPage()
    c.showPage()
    c.save()


AGES_512 = [
    "What made you smile today?",
    "If our pets could talk, what would yours say?",
    "What's the silliest word you know right now?",
    "Tell me about the best (or worst) lunch you had this week.",
    "If you could add one slide to the playground, what would it do?",
    "What book, show, or game are you into these days?",
    "What's something that surprised you lately?",
    "Hide something behind your back and let me guess what it is.",
    "Teach me a hand game we could play through the screen.",
    "If you built a robot, what three buttons would it have?",
    "What would you do with a whole rainy Saturday indoors?",
    "What's your favorite spot in your room or classroom?",
    "Show me your happy dance, quick!",
    "What do you think I was like at your age?",
    "If we swapped dinners tonight, what would I be eating?",
    "What song should I learn the words to before we talk again?",
    "What's something you're looking forward to soon?",
    "If your toys came alive at night, what would they do first?",
    "What's a sound you love hearing?",
    "Draw a quick doodle and show it to me in one minute.",
    "What's the funniest thing that happened this week?",
    "If you were in charge of school for a day, what's the first rule you'd make?",
    "What are you really good at that we haven't talked about yet?",
    "Invent a brand-new ice cream flavor for me. What's in it?",
]

TEENS = [
    "What song, show, or game has your attention right now?",
    "What's something you've gotten better at this month?",
    "If you could master any skill overnight, which one would you pick?",
    "What's a plan you're excited about?",
    "Who's someone at school who quietly makes everything better?",
    "What's a trend you secretly find ridiculous?",
    "What did you learn recently that most grown-ups don't know?",
    "Free Saturday, no chores allowed — what's the move?",
    "What's a song on repeat for you these days?",
    "What's something you're proud of but never brag about?",
    "What should I know about that happened this week?",
    "What advice would you give me about phones or technology?",
    "If you could redesign one school rule, which one?",
    "What's a goal you're working toward, even quietly?",
    "What do you wish adults understood better?",
    "What's the funniest thing you've seen online lately?",
    "Which class would you shorten, and which would you make longer?",
    "What hobby would you try if time and money weren't a problem?",
    "Where do you want to travel someday, and why there?",
    "What's a meal someone makes that always feels like home?",
    "What would you recommend I watch or read next, and why?",
    "If you started a shop or channel someday, what would it be about?",
    "What's a kind thing you saw someone do recently?",
    "What's a question you wish I'd ask you?",
]

ACTIVITY_TIPS = {
    "Read-alouds": [
        "Pick a short chapter book and read one chapter per call — and stop at a good cliffhanger, so next call comes fast.",
        "Let the kid read a page and do all the voices. Then swap, and you do your best dragon impression.",
        "For little ones, choose picture books you can hold up to the camera and point at together.",
        "One short poem per call, then make up your own silly poem about something you can both see.",
        "Let the grandkid pick the book from a small menu of three choices — choosing is half the fun.",
    ],
    "Story chains": [
        "One person starts with \"Once upon a time…\" and each of you adds two sentences per turn.",
        "Keep the same silly characters from call to call, and grow the saga over months.",
        "Pick a theme bag — outer space, a dragon bakery, a traveling taco truck — and stay inside it.",
        "Write the story down in your keeper notes so it never gets lost between calls.",
        "Roll an imaginary dice to see who narrates next, or take turns by alphabet.",
    ],
    "Show-and-tell": [
        "Keep the rule simple: each person shows exactly one thing, so turns stay quick and special.",
        "Do a VIP item of the week — two minutes to explain why it deserves the crown.",
        "Tour the trophy shelf: drawings, medals, and crafts. Your side counts too!",
        "Do a slow, wiggly room tour and let the other side ask one question at every stop.",
        "Adults can join in — show a keepsake and tell the story behind it (talk about it, no need to show private photos).",
    ],
    "Quick games": [
        "I Spy, backdrop edition: spy things in each other's rooms.",
        "Twenty Questions — animal, mineral, or household object.",
        "Screen scavenger hunt: find something red, something soft, something that makes a sound.",
        "Copy-cat freeze dance: one person strikes a pose, the other copies it and freezes.",
        "Two truths and a dream: two true facts and one wish — everyone guesses the dream.",
    ],
}


def activity_ideas(path):
    doc_title = "Shared Activity Ideas"
    c = new_canvas(path, doc_title)
    page_plan = [
        ("read-alouds and story chains that kids love",
         ["Read-alouds", "Story chains"]),
        ("show-and-tell and quick games that work over any screen",
         ["Show-and-tell", "Quick games"]),
    ]
    x = 57
    maxw = W - 114
    for subtitle, sections in page_plan:
        start_page(c, doc_title, "Shared Activity Ideas", subtitle)
        y = H - 168
        for section in sections:
            tips = ACTIVITY_TIPS[section]
            accent, soft = (TEAL, TEAL_SOFT) if section == "Quick games" else (RUST, RUST_SOFT)
            c.setFillColor(accent)
            c.setFont("Helvetica-Bold", 15)
            c.drawString(x, y, section)
            c.setStrokeColor(soft)
            c.setLineWidth(1.4)
            c.line(x, y - 8, x + maxw, y - 8)
            y -= 26
            for tip in tips:
                lines = wrap(tip, "Helvetica", 11, maxw - 26)
                c.setFillColor(RUST)
                c.circle(x + 5, y + 4, 3, stroke=0, fill=1)
                c.setFillColor(COCOA)
                c.setFont("Helvetica", 11)
                for line in lines:
                    c.drawString(x + 18, y, line)
                    y -= 15
                y -= 7
            y -= 12
        c.setFillColor(CREAM)
        c.setStrokeColor(LINE)
        c.roundRect(57, 44, maxw, 34, 8, stroke=1, fill=1)
        c.setFillColor(COCOA)
        c.setFont("Helvetica-Oblique", 10.5)
        if sections[0] == "Read-alouds":
            c.drawString(73, 57, "Golden rule of every activity: it should make both of you laugh before it ends.")
        else:
            c.drawString(73, 57, "Mix and match: one read-aloud, one game, and one chat-starter is a perfect call.")
        c.showPage()
    c.save()


def keeper_notes(path):
    c = new_canvas(path, "Keeper Notes Page")
    start_page(c, "keeper-notes", "Keeper Notes Page", "plan the next call before the screen even turns on")

    bx, by, bw, bh = 57, H - 250, W - 114, 128
    c.setFillColor(CREAM)
    c.setStrokeColor(RUST)
    c.setLineWidth(1.6)
    c.roundRect(bx, by, bw, bh, 12, stroke=1, fill=1)
    c.setFillColor(COCOA)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(bx + 20, by + bh - 28, "Our next big call")
    fields = ["Day & time (mind the time zones!):", "What we planned to do:", "Grown-up to ask for a tech test-run:"]
    fy = by + bh - 52
    for label in fields:
        c.setFillColor(GRANITE)
        c.setFont("Helvetica", 10.5)
        c.drawString(bx + 20, fy, label)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.9)
        label_w = stringWidth(label, "Helvetica", 10.5)
        c.line(bx + 30 + label_w, fy - 2, bx + bw - 20, fy - 2)
        fy -= 26



    sections = [
        ("Remember for next time", 4),
        ("New since last call (names, wins, news)", 3),
        ("Jokes, words & stories to keep forever", 4),
        ("Things to have ready (book, prop, snack, doodle pad)", 3),
    ]
    y = H - 312
    for title, n_lines in sections:
        heart(c, 63, y - 3, 6)
        c.setFillColor(COCOA)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(76, y, title)
        y -= 24
        for _ in range(n_lines):
            ruled_line(c, 76, W - 70, y)
            y -= 19
        y -= 10
    c.setFillColor(GRANITE)
    c.setFont("Helvetica-Oblique", 9.5)
    c.drawCentredString(W / 2.0, y + 2, "Tape this page inside a folder you actually open. Future-you says thanks.")
    c.showPage()
    c.save()


def reminder_sheet(path):
    c = new_canvas(path, "Recurring Call Reminder Sheet")
    start_page(c, "reminder-sheet", "Recurring Call Reminder Sheet", "pick a rhythm, own it, and never let three weeks slip by")

    bx, bw = 57, W - 114
    y = H - 176
    rows = [
        "Day we call:",
        "Time we call (with time zones!):",
        "Where we call (app or service):",
        "Backup plan if the call won't connect:",
    ]
    c.setFillColor(COCOA)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(bx, y, "Our call rhythm")
    y -= 8
    c.setStrokeColor(RUST)
    c.setLineWidth(1.2)
    c.line(bx, y, bx + bw, y)
    y -= 24
    for label in rows:
        c.setFillColor(GRANITE)
        c.setFont("Helvetica", 10.5)
        c.drawString(bx, y, label)
        label_w = stringWidth(label, "Helvetica", 10.5)
        ruled_line(c, bx + 12 + label_w, bx + bw, y - 2)
        y -= 25

    y -= 10
    c.setFillColor(TEAL)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(bx, y, "If life happens")
    c.setFillColor(COCOA)
    c.setFont("Helvetica", 10.5)
    y -= 17
    for tip in [
        "A missed call isn't a broken promise — send a voice note or a photo and catch up next time.",
        "If a call gets skipped twice in a row, text one single question and pick the call back up.",
    ]:
        for line in wrap(tip, "Helvetica", 10.5, bw - 20):
            c.drawString(bx + 14, y, line)
            y -= 14
        y -= 5

    y -= 6
    c.setFillColor(COCOA)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(bx, y, "Check the boxes each month")
    y -= 12
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    cell_w, cell_h = (bw - 14) / 2.0, 50
    for i, month in enumerate(months):
        col, row = divmod(i, 6)
        x = bx + col * (cell_w + 14)
        top = y - row * (cell_h + 10)
        cy = top - cell_h
        c.setFillColor(CREAM)
        c.setStrokeColor(LINE)
        c.setLineWidth(1.1)
        c.roundRect(x, cy, cell_w, cell_h, 8, stroke=1, fill=1)
        c.setFillColor(COCOA)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(x + 10, top - 14, month)
        for k in range(4):
            check_square(c, x + 10 + k * 19, top - 31, 10)
        c.setFillColor(GRANITE)
        c.setFont("Helvetica", 8)
        c.drawString(x + 96, top - 23, "dates & notes:")
        ruled_line(c, x + 10, x + cell_w - 10, cy + 7, LINE)

    c.showPage()
    c.save()


def main():
    os.makedirs(OUT, exist_ok=True)
    files = []
    invitation_cards(os.path.join(OUT, "call-invitation-cards.pdf"))
    files.append("call-invitation-cards.pdf")
    starter_strips(
        os.path.join(OUT, "conversation-starters-ages-5-12.pdf"),
        "Conversation Starters: Ages 5 to 12", "Conversation Starters", "snip, shuffle, and pull one on every call \u2014 ages 5 to 12",
        AGES_512, RUST, RUST_SOFT,
    )
    files.append("conversation-starters-ages-5-12.pdf")
    starter_strips(
        os.path.join(OUT, "conversation-starters-teens.pdf"),
        "Conversation Starters: Teens", "Conversation Starters", "snip, shuffle, and pull one on every call \u2014 for teens",
        TEENS, TEAL, TEAL_SOFT,
    )
    files.append("conversation-starters-teens.pdf")
    activity_ideas(os.path.join(OUT, "shared-activity-ideas.pdf"))
    files.append("shared-activity-ideas.pdf")
    keeper_notes(os.path.join(OUT, "keeper-notes-page.pdf"))
    files.append("keeper-notes-page.pdf")
    reminder_sheet(os.path.join(OUT, "call-reminder-sheet.pdf"))
    files.append("call-reminder-sheet.pdf")

    manifest = {"generated": [os.path.basename(f) for f in files]}
    with open(os.path.join(OUT, "manifest.json"), "w") as fh:
        json.dump(manifest, fh, indent=2)
    print("Built %d PDFs in %s" % (len(files), OUT))


if __name__ == "__main__":
    main()
