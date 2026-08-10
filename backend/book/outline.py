import json
from pathlib import Path

_MANIFEST = json.loads((Path(__file__).parent / "content" / "manifest.json").read_text(encoding="utf-8"))

BOOK_META = {
    "title": "Medical Devices",
    "subtitle": "A Comprehensive Textbook for Pharmacy and Allied Health Sciences",
    "edition": "First Edition",
    "author": "Author Name",
    "affiliation": "Department of Pharmaceutics, Institution Name",
    "publisher": "Emergent Academic Press",
    "year": "2026",
    "isbn": "ISBN 978-X-XXXXX-XXX-X (placeholder — assigned on registration)",
    "syllabus_anchor": "PCI NEP 2020 B.Pharm — BP708T (Medical Devices, Elective)",
    "series": "Medical Devices Academic Ecosystem · Core Textbook",
}

_PART_DEFS = [
    ("I", "Foundations of Medical Devices", [1, 2, 3], 2),
    ("II", "Lifecycle, Quality Systems & Manufacturing Environments", [4, 5, 6], 3),
    ("III", "Materials, Biocompatibility & Design", [7, 8, 9], 3),
    ("IV", "Manufacturing & Quality Control", [10, 11], 4),
    ("V", "Regulation, Clinical Evidence & Market Oversight", [12, 13, 14, 15, 16, 17], 4),
    ("VI", "Emerging Technologies, Data & Careers", [18, 19, 20], 5),
]

PARTS = [{"num": n, "title": t, "chapters": chs} for n, t, chs, _ in _PART_DEFS]


def _phase_of(num):
    for _, _, chs, phase in _PART_DEFS:
        if num in chs:
            return phase
    return 5


def part_of(num):
    for n, t, chs, _ in _PART_DEFS:
        if num in chs:
            return n, t
    return "", ""


CHAPTERS = [
    {
        "num": c["num"],
        "id": c["id"],
        "title": c["title"],
        "subtitle": c.get("subtitle", ""),
        "status": "complete",
        "phase": _phase_of(c["num"]),
        "sections": c.get("sections", [])[:6],
    }
    for c in _MANIFEST["chapters"]
]

PHASES = [
    {"num": 1, "title": "Design system + book skeleton", "detail": "Cover, front matter, TOC, chapter template, A4 PDF pipeline", "status": "complete"},
    {"num": 2, "title": "Source manuscript ingestion", "detail": "20-chapter author manuscript extracted: text, 156 figures, tables", "status": "complete"},
    {"num": 3, "title": "Parts I\u2013III typeset (Ch 1\u20139)", "detail": "Foundations, lifecycle & quality, materials & design", "status": "complete"},
    {"num": 4, "title": "Parts IV\u2013V typeset (Ch 10\u201317)", "detail": "Manufacturing, QC, regulatory, clinical, post-market", "status": "complete"},
    {"num": 5, "title": "Part VI typeset (Ch 18\u201320)", "detail": "Emerging technologies, health data & careers", "status": "complete"},
    {"num": 6, "title": "Back matter & final typeset", "detail": "Consolidated glossary, references, standards index, A4 PDF", "status": "complete"},
]

FIGURES = [(num, cap) for c in _MANIFEST["chapters"] for num, cap in c.get("figures", [])]
TABLES = [(num, cap or "Data table") for c in _MANIFEST["chapters"] for num, cap in c.get("tables", [])]


def part_divider_html(part):
    chapters = [c for c in CHAPTERS if c["num"] in part["chapters"]]
    ch_rows = "".join(
        '<div class="pd-ch"><span class="n">%02d</span> %s</div>' % (c["num"], c["title"])
        for c in chapters
    )
    return """
<section class="part-divider" id="part%s">
  <div class="pd-inner">
    <div class="pd-num">%s</div>
    <div class="pd-label">Part %s</div>
    <div class="pd-title">%s</div>
    <div class="pd-chapters">%s</div>
  </div>
</section>""" % (part["num"], part["num"], part["num"], part["title"], ch_rows)
