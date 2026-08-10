"""Extract the 20-chapter Medical Devices book from the source .docx into
structured JSON (one file per chapter) + compressed figure images + manifest.

Run:  python3 /app/scripts/extract_docx.py
Outputs:
  /app/backend/book/content/chNN.json
  /app/backend/book/content/manifest.json
  /app/backend/book/images/chNN_figMM.jpg
"""
import io
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

import docx
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph
from PIL import Image

SRC = Path("/app/source/book_source.docx")
OUT_CONTENT = Path("/app/backend/book/content")
OUT_IMAGES = Path("/app/backend/book/images")
OUT_CONTENT.mkdir(parents=True, exist_ok=True)
OUT_IMAGES.mkdir(parents=True, exist_ok=True)

# Canonical clean chapter titles (source has typos / inconsistent dashes)
TITLES = {
    1: "Introduction to Medical Devices",
    2: "Structure of the Medical Device Industry",
    3: "Classification of Medical Devices",
    4: "Medical Device Lifecycle & Development Process",
    5: "Quality Management Systems (QMS) in Medical Devices",
    6: "Cleanrooms & Sterile Manufacturing Environment",
    7: "Materials Used in Medical Devices",
    8: "Biomechanics & Biocompatibility of Medical Devices",
    9: "Design & Development of Medical Devices",
    10: "Manufacturing of Medical Devices",
    11: "Quality Control & Testing of Medical Devices",
    12: "Regulatory Requirements for Medical Devices",
    13: "Software as a Medical Device (SaMD), AI/ML Devices & Digital Health Regulation",
    14: "Clinical Evaluation & Clinical Trials for Medical Devices",
    15: "Post-Market Surveillance (PMS), Vigilance & Recalls",
    16: "Packaging, Labeling & UDI Requirements",
    17: "Import, Export & Supply Chain Management",
    18: "Emerging Technologies in Medical Devices",
    19: "Healthcare Data, AI Analytics & Interoperability",
    20: "Career Pathways, Job Roles & Skill Development",
}

CH_RE = re.compile(r"^CHAPTER\s+(\d+)\s*[-–—]")
FIG_RE = re.compile(r"^(?:Figure|Fig\.?)[\s]*(\d+)\.(\d+)\s*[—–:.\-]*\s*(.*)$", re.I)
CS_RE = re.compile(r"Case Study\s*(\d+\.\d+)\s*[—–:\-]*\s*(.*)$")
II_RE = re.compile(r"Industry Insight\s*(\d+\.\d+)\s*[—–:\-]*\s*(.*)$")
EB_RE = re.compile(r"Example Box\s*(\d+\.\d+)\s*[—–:\-]*\s*(.*)$")

# ---- copy-editing rules for source-conversion artifacts --------------------
# table-header rows that leaked into the text as pseudo-headings: drop them
DROP_HEADINGS = {
    "diagnostic monitoring therapeutic surgical",
    "term definition",
}

# headings that fused two levels together in the source: split cleanly
CURATED_SPLITS = {
    "business and commercial roles sales and marketing executive": [
        ("h3", "Business and Commercial Roles"), ("h4", "Sales and Marketing Executive")],
    "emerging roles software validation specialist": [
        ("h3", "Emerging Roles"), ("h4", "Software Validation Specialist")],
    "field and application roles field service engineer": [
        ("h3", "Field and Application Roles"), ("h4", "Field Service Engineer")],
    "regulatory and compliance roles regulatory affairs (ra) associate": [
        ("h3", "Regulatory and Compliance Roles"), ("h4", "Regulatory Affairs (RA) Associate")],
    "engineering and development roles r&d engineer / design engineer": [
        ("h3", "Engineering and Development Roles"), ("h4", "R&D Engineer / Design Engineer")],
    "review questions multiple choice questions": [
        ("h2", "Review Questions"), ("h4", "Multiple Choice Questions")],
    "capa (corrective and preventive action) corrective action:": [
        ("h3", "CAPA (Corrective and Preventive Action)"), ("h4", "Corrective Action")],
    "risk management (iso 14971) integrated throughout device lifecycle:": [
        ("h3", "Risk Management (ISO 14971)"), ("h4", "Integrated Throughout Device Lifecycle")],
    "airflow patterns two primary types:": [
        ("h3", "Airflow Patterns"), ("h4", "Two Primary Types")],
}

EXAMPLES_SPLIT_RE = re.compile(r"^(.{6,}?[^\s:])\s+(Examples?):$")
# short "Label: long sentence" headings are really lead-in body lines
LEADIN_RE = re.compile(r"^([A-Z][\w\)\(&/ ]{1,28}?):\s+(.{25,})$")
LEADIN_EXCLUDE = re.compile(
    r"^(Clause|Step|Phase|Stage|Unit|Rule|Part|Annex|Level|Grade|Class|Q\d|Question|"
    r"Section|Module|Article|Schedule|Form|Chapter|Table|Figure|Fig|Tier|Zone|Route)\b", re.I)

# Chapter 11's glossary table was destroyed in the source conversion;
# reassembled here from the source's own fragments (author wording kept).
GLOSSARY_OVERRIDES = {
    11: [
        ["AQL", "Acceptable Quality Limit — maximum tolerable defect percentage in a lot."],
        ["Bioburden", "Population of viable microorganisms on a product before sterilization."],
        ["Burst Pressure", "Maximum internal pressure before device rupture."],
        ["CAPA", "Corrective and Preventive Action — systematic approach to eliminate problem causes."],
        ["Cpk", "Process capability index measuring ability to meet specifications."],
        ["DHR", "Device History Record — complete production and QC documentation for a specific lot."],
        ["Fatigue Testing", "Cyclic loading test simulating long-term device use."],
        ["Leakage Current", "Unwanted electrical current flowing from device to patient or ground."],
        ["SAL", "Sterility Assurance Level — probability of viable microorganism presence (typically 10\u207b\u2076)."],
        ["Tensile Strength", "Maximum stress a material withstands before breaking under tension."],
    ],
}

# figure-prompt residue: descriptive text used to create the figures, which
# duplicates the visible figure; removed near figures during post-processing
VISUAL_HINT_RE = re.compile(r"^(Colors?[ :]|Arrows indicate|Visual layout|Visual style|Layout shows|Diagram shows)", re.I)

# pass 2: prose blocks that narrate the figure itself (chart-description residue)
FP_ANCHOR_P = re.compile(
    r"^(An? (comparative|vertical|horizontal|three-column|two-panel|three-panel|circular|"
    r"flowchart|diagram|timeline|schematic|visual|multi-panel|stepped|layered|comprehensive)\b|"
    r"Flowchart |Diagram \d|Matrix comparing|Circular lifecycle|X-axis|Y-axis)", re.I)
FP_HINT = re.compile(
    r"X-axis|Y-axis|[Cc]olor-cod|[Cc]olor cod|[Aa]nnotations (show|indicat)|[Bb]ars show|"
    r"[Aa]rrows? (show|indicat|point)|[Ee]ach (panel|column|segment) (show|display|represent)")
FP_CONT_P = re.compile(
    r"^(Branching|Sub-branches|Further branches|End nodes|Color-coding|Colors?[ :]|Organized by|"
    r"Force magnitudes|Annotations|Bars |Arrows )", re.I)
FP_CONT_H = re.compile(r"^Level \d|^(Top|Middle|Bottom|Base|Apex)\b.*\)$|(Yellow|Red|Green|Blue|Orange|Grey|Gray)\)$")
FP_UL0 = re.compile(r'^\s*(Column \d|Row \d|Label\s*[:"]|Subtitle\s*[:"])', re.I)


def strip_figure_prompt_residue(blocks):
    """Remove chart-narration paragraphs that ride along after figures."""
    def plain(s):
        return re.sub(r"<[^>]+>", "", s)

    dels = set()
    fig_positions = [i for i, b in enumerate(blocks) if b["t"] == "fig"]
    for fi in fig_positions:
        for j in range(fi + 1, min(len(blocks), fi + 4)):
            b = blocks[j]
            anchored = (
                (b["t"] == "p" and (FP_ANCHOR_P.match(plain(b["html"])) or FP_HINT.search(plain(b["html"]))))
                or (b["t"] == "ul" and b["items"] and FP_UL0.match(plain(b["items"][0])))
            )
            if not anchored:
                continue
            k = j
            while k < len(blocks) and k < j + 12:
                bb = blocks[k]
                if bb["t"] == "p" and (k == j or FP_CONT_P.match(plain(bb["html"]))
                                       or FP_HINT.search(plain(bb["html"]))
                                       or FP_ANCHOR_P.match(plain(bb["html"]))):
                    dels.add(k)
                elif bb["t"] in ("h3", "h4") and FP_CONT_H.match(plain(bb["text"])):
                    dels.add(k)
                elif bb["t"] == "ul" and bb["items"] and FP_UL0.match(plain(bb["items"][0])):
                    dels.add(k)
                else:
                    break
                k += 1
            break
    if dels:
        return [b for i, b in enumerate(blocks) if i not in dels]
    return blocks


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def norm(t):
    t = t.replace("\t", " ").replace("\u00a0", " ").replace("★", "")
    t = re.sub(r"[\uf000-\uf8ff]", "", t)  # symbol-font bullets etc.
    t = re.sub(r"\s+", " ", t).strip()
    t = t.replace(" -- ", " — ")
    # fix pdf-conversion hyphen splits:  "Post- Market" -> "Post-Market"
    t = re.sub(r"(?<=[A-Za-z])- (?=[a-z])", "-", t)
    return t


def para_html(p):
    """Paragraph runs -> escaped html with bold/italic preserved."""
    parts = []
    for r in p.runs:
        t = r.text
        if not t:
            continue
        t = esc(t)
        if r.bold and r.italic:
            parts.append("<strong><em>%s</em></strong>" % t)
        elif r.bold:
            parts.append("<strong>%s</strong>" % t)
        elif r.italic:
            parts.append("<em>%s</em>" % t)
        else:
            parts.append(t)
    html = "".join(parts)
    html = html.replace("</strong><strong>", "").replace("</em><em>", "")
    html = html.replace("\t", " ").replace("\u00a0", " ").replace("★", "")
    html = re.sub(r"[\uf000-\uf8ff]", "", html)
    html = re.sub(r"\s+", " ", html).strip()
    html = html.replace(" -- ", " — ").replace(">-- ", ">— ").replace(" --<", " —<")
    html = re.sub(r"(?<=[A-Za-z])- (?=[a-z])", "-", html)
    return html


def is_list(p):
    if p.style is not None and p.style.name == "List Paragraph":
        return True
    return p._p.find(qn("w:pPr")) is not None and p._p.find(qn("w:pPr")).find(qn("w:numPr")) is not None


def is_heading(p):
    return p.style is not None and p.style.name.startswith("Heading")


def get_images(p, doc):
    out = []
    for blip in p._p.findall(".//" + qn("a:blip")):
        rid = blip.get(qn("r:embed"))
        if rid:
            part = doc.part.related_parts[rid]
            out.append(part.blob)
    return out


def save_image(blob, ch, seq):
    name = "ch%02d_fig%02d.jpg" % (ch, seq)
    try:
        im = Image.open(io.BytesIO(blob))
        if im.mode in ("RGBA", "P", "LA"):
            bg = Image.new("RGB", im.size, (255, 255, 255))
            im2 = im.convert("RGBA")
            bg.paste(im2, mask=im2.split()[-1])
            im = bg
        elif im.mode != "RGB":
            im = im.convert("RGB")
        if im.width > 1400:
            h = int(im.height * 1400 / im.width)
            im = im.resize((1400, h), Image.LANCZOS)
        im.save(OUT_IMAGES / name, "JPEG", quality=78, optimize=True)
        return name, im.width, im.height
    except Exception as e:
        print("  ! image save failed ch%d seq%d: %s" % (ch, seq, e))
        return None, 0, 0


def fuzzy(a, b):
    a = re.sub(r"[^a-z0-9 ]", "", a.lower())
    b = re.sub(r"[^a-z0-9 ]", "", b.lower())
    if not a or not b:
        return 0
    if a in b or b in a:
        return 1
    return SequenceMatcher(None, a, b).ratio()


# ----------------------------------------------------------------------------
def build_stream(doc):
    stream = []
    for child in doc.element.body.iterchildren():
        tag = child.tag.split("}")[1]
        if tag == "p":
            stream.append(("p", Paragraph(child, doc)))
        elif tag == "tbl":
            stream.append(("tbl", Table(child, doc)))
    return stream


SPECIALS = [
    ("overview", re.compile(r"^Chapter Overview\b[:\s—–\-]*(.*)$", re.I)),
    ("clos", re.compile(r"^(?:Chapter )?Learning Outcomes\s*(?:\(CLOs?\))?\b[:\s—–\-]*(.*)$", re.I)),
    ("keywords", re.compile(r"^Key\s?words\b[:\s—–\-]*(.*)$", re.I)),
    ("roadmap", re.compile(r"^Chapter Roadmap\b[:\s—–\-]*(.*)$", re.I)),
    ("glossary", re.compile(r"^Glossary\b[:\s—–\-]*(?:Chapter\s*\d+)?[:\s—–\-]*(.*)$", re.I)),
    ("recap", re.compile(r"^(?:Quick Recap|Chapter Summary)\b[:\s—–\-]*(.*)$", re.I)),
    ("references", re.compile(r"^References(?:\s+and\s+Further\s+Reading)?\b[:\s]*(.*)$", re.I)),
    ("end", re.compile(r"^End of Chapter\b(.*)$", re.I)),
]

# these modes may only start in the tail of a chapter (guards against
# mid-chapter lines like "References:" inside boxes)
TAIL_MODES = {"glossary", "recap", "references", "end"}


def special_of(text):
    for mode, rx in SPECIALS:
        m = rx.match(text)
        if m:
            remainder = norm(m.group(1)) if m.groups() else ""
            # if a huge remainder rides on the marker, it is content merged in
            if mode == "glossary" and len(remainder) > 120 and not re.match(r"^[^:]{2,60}:\s", remainder):
                return None
            if mode == "references" and remainder and not (
                remainder.endswith(":") or (len(remainder) <= 45 and remainder[:1].isupper())
            ):
                return None
            if mode == "references" and len(remainder) > 60:
                return None
            return mode, remainder
    return None


def parse_chapter(items, ch_num, doc):
    """items: list of ('p', Paragraph) / ('tbl', Table) belonging to one chapter
    (first item is the chapter heading paragraph)."""
    ch = {
        "num": ch_num,
        "id": "ch%02d" % ch_num,
        "title": TITLES[ch_num],
        "subtitle": "",
        "overview": [],
        "clos": [],
        "keywords": [],
        "roadmap": [],
        "blocks": [],
        "glossary": [],
        "recap_intro": "",
        "recap_items": [],
        "references": [],
    }
    mode = "opener"
    fig_seq = 0
    tab_seq = 0
    pending_caption = None  # (num, caption) waiting for an image
    uncaptioned_fig = None  # index into blocks of last figure without caption
    box = None  # open case-study/insight/example box
    ref_current = None
    ref_group = None
    last_heading_text = ""

    def target():
        return box["blocks"] if box is not None else ch["blocks"]

    def close_box():
        nonlocal box
        if box is not None:
            ch["blocks"].append(box)
            box = None

    def add_para(html):
        blocks = target()
        if blocks and blocks[-1]["t"] == "ul_open":
            pass
        blocks.append({"t": "p", "html": html})

    def add_li(html):
        blocks = target()
        if blocks and blocks[-1]["t"] == "ul":
            blocks[-1]["items"].append(html)
        else:
            blocks.append({"t": "ul", "items": [html]})

    def open_box(kind, label, title):
        nonlocal box
        close_box()
        box = {"t": "box", "kind": kind, "label": label, "title": title, "blocks": []}

    def flush_ref():
        nonlocal ref_current
        if ref_current:
            txt = re.sub(r"^\d+[\.\)]\s*", "", ref_current.strip(" ,;"))
            if len(txt) > 3 and not re.match(r"^\[?End of Chapter", txt, re.I):
                ch["references"].append({"group": ref_group, "text": txt})
        ref_current = None

    def feed_special(new_mode, remainder):
        """Process remainder text that was merged onto a special marker line."""
        nonlocal ref_current, ref_group
        if not remainder:
            return
        if new_mode == "overview":
            ch["overview"].append(esc(remainder))
        elif new_mode == "clos":
            for s in re.split(r"(?<=[.;])\s+(?=[A-Z])", remainder):
                if len(s.strip()) > 8:
                    ch["clos"].append(esc(s.strip()))
        elif new_mode == "keywords":
            for kw in re.split(r"[,;]\s*", remainder):
                kw = kw.strip(" .")
                if kw:
                    ch["keywords"].append(esc(kw))
        elif new_mode == "roadmap":
            for item in re.split(r"(?<=[a-z\)]) (?=[A-Z])", remainder):
                if item.strip():
                    ch["roadmap"].append(esc(item.strip()))
        elif new_mode == "glossary":
            m = re.match(r"^([^:]{2,60}):\s+(.*)$", remainder)
            if m:
                ch["glossary"].append([norm(m.group(1)), norm(m.group(2))])
        elif new_mode == "recap":
            ch["recap_intro"] = esc(remainder)
        elif new_mode == "references":
            if len(remainder) < 45 and not remainder.rstrip(":").endswith("."):
                ref_group = remainder.rstrip(":")
            else:
                ref_current = remainder

    n_items = max(len(items), 1)
    idx = -1
    for kind, obj in items:
        idx += 1
        # ---------------- TABLE ----------------
        if kind == "tbl":
            rows = []
            for r in obj.rows:
                cells = [norm(c.text) for c in r.cells]
                rows.append(cells)
            if mode == "references":
                for r in rows:
                    joined = norm(" ".join(x for x in r if x))
                    if len(joined) > 5:
                        flush_ref()
                        ref_current = joined
                        flush_ref()
                continue
            tab_seq += 1
            cap = last_heading_text if 0 < len(last_heading_text) <= 80 else ""
            tbl = {"t": "table", "num": "%d.%d" % (ch_num, tab_seq), "caption": cap, "rows": rows}
            target().append(tbl)
            continue

        # ---------------- PARAGRAPH ----------------
        p = obj
        text = norm(p.text)
        images = get_images(p, doc)

        # images first (they may sit in empty or text paragraphs)
        if images and mode == "references":
            mode = "content"  # a figure means we were fooled by a pseudo-marker
        for blob in images:
            fig_seq += 1
            name, w, h = save_image(blob, ch_num, fig_seq)
            if name:
                fig = {"t": "fig", "src": "images/" + name, "w": w, "h": h,
                       "num": None, "caption": None, "ctx": last_heading_text}
                if pending_caption:
                    fig["num"], fig["caption"] = pending_caption
                    pending_caption = None
                    uncaptioned_fig = None
                else:
                    close_box()
                    ch["blocks"].append(fig)
                    uncaptioned_fig = len(ch["blocks"]) - 1
                    continue
                close_box()
                ch["blocks"].append(fig)

        if not text:
            continue

        if idx == 0:
            continue  # the CHAPTER N heading itself
        if mode == "opener" and text.startswith("(") and text.endswith(")"):
            ch["subtitle"] = text.strip("()")
            mode = "content_wait"
            continue

        sp = special_of(text)
        if sp:
            new_mode, remainder = sp
            in_tail = idx > 0.55 * n_items
            bare_list_marker = (
                is_list(p) and not is_heading(p)
                and re.match(r"^(References?|Quick Recap|Glossary|Chapter Summary)\s*:?\s*$", text, re.I)
            )
            if new_mode in TAIL_MODES and (not in_tail or bare_list_marker):
                sp = None  # a mid-chapter pseudo-marker; treat as content
            else:
                close_box()
                flush_ref()
                mode = "done" if new_mode == "end" else new_mode
                ref_group = None
                if mode != "done":
                    feed_special(new_mode, remainder)
                continue
        if mode == "done":
            continue
        if mode in ("opener", "content_wait"):
            mode = "content"

        # exit early front-matter modes when real content headings begin
        if mode in ("overview", "clos", "keywords", "roadmap"):
            exhausted = (
                (mode == "overview" and len(ch["overview"]) >= 4)
                or (mode == "roadmap" and len(ch["roadmap"]) >= 14)
                or (mode == "keywords" and ch["keywords"] and "," not in text)
            )
            if (is_heading(p) and not text.endswith(":")) or exhausted:
                mode = "content"

        # tail modes can be polluted by mid-content pseudo-markers; rescue
        if mode in ("glossary", "recap", "references"):
            if CS_RE.search(text) or II_RE.search(text) or EB_RE.search(text):
                mode = "content"
            elif mode in ("glossary", "recap") and is_heading(p) and not text.endswith(":") \
                    and not re.match(r"^[^:]{2,60}:\s", text) and len(text) < 80:
                mode = "content"

        # figure caption?
        fm = FIG_RE.match(text)
        if fm and len(text) < 160:
            num = "%s.%s" % (fm.group(1), fm.group(2))
            cap = norm(fm.group(3)) or ""
            if uncaptioned_fig is not None:
                ch["blocks"][uncaptioned_fig]["num"] = num
                ch["blocks"][uncaptioned_fig]["caption"] = cap
                uncaptioned_fig = None
            else:
                pending_caption = (num, cap)
            continue

        # ---------------- mode handling ----------------
        if mode == "overview":
            ch["overview"].append(para_html(p) or esc(text))
            continue
        if mode == "clos":
            if re.match(r"^(After|Upon|On) .{0,80}(chapter|learners|will be able)", text, re.I) and text.endswith(":"):
                continue
            # split multi-sentence CLO paragraphs
            sentences = re.split(r"(?<=[.;])\s+(?=[A-Z])", text)
            for s in sentences:
                s = s.strip()
                if len(s) > 8:
                    ch["clos"].append(esc(s))
            continue
        if mode == "keywords":
            for kw in re.split(r"[,;]\s*", text):
                kw = kw.strip(" .")
                if kw:
                    ch["keywords"].append(esc(kw))
            continue
        if mode == "roadmap":
            for item in re.split(r"(?<=[a-z\)]) (?=[A-Z])", text):
                if item.strip():
                    ch["roadmap"].append(esc(item.strip()))
            continue
        if mode == "glossary":
            if ch_num in GLOSSARY_OVERRIDES:
                continue  # source glossary destroyed; curated override applied below
            raw = p.text.replace("\u00a0", " ")
            entry = None
            m = re.match(r"^([^:]{2,60}):\s+(.*)$", text)
            if m:
                entry = (norm(m.group(1)), norm(m.group(2)))
            if entry is None:
                parts = re.split(r"\t+|\s{2,}", re.sub(r"[\uf000-\uf8ff]", "", raw).strip(), maxsplit=1)
                if len(parts) == 2 and 2 <= len(parts[0].strip()) <= 45 and len(parts[1].strip()) > 2:
                    entry = (norm(parts[0]), norm(parts[1]))
            if entry is None:
                m = re.match(r"^(.{2,60}?)\s+(?:--|–|—)\s+(.*)$", text)
                if m:
                    entry = (norm(m.group(1)), norm(m.group(2)))
            if entry is not None:
                if entry[0].lower() != "term" or entry[1].lower() != "definition":
                    ch["glossary"].append([entry[0], entry[1]])
            elif ch["glossary"] and len(text) < 120:
                ch["glossary"][-1][1] += " " + text
            continue
        if mode == "recap":
            if is_heading(p) and text.endswith(":"):
                ch["recap_items"].append("<strong>%s</strong>" % esc(text.rstrip(":")))
            elif is_list(p):
                ch["recap_items"].append(para_html(p) or esc(text))
            elif not ch["recap_items"] and not ch["recap_intro"]:
                ch["recap_intro"] = esc(text)
            else:
                ch["recap_items"].append(para_html(p) or esc(text))
            continue
        if mode == "references":
            if text.endswith(":") and len(text) < 45:
                flush_ref()
                ref_group = text.rstrip(":")
                continue
            if is_list(p):
                flush_ref()
                ref_current = text
            elif is_heading(p):
                flush_ref()
                ref_current = text
            else:
                if ref_current and (
                    re.search(r"https?://\S+$", ref_current)
                    or len(ref_current) > 180
                    or (len(ref_current) > 40 and ref_current.rstrip().endswith(".")
                        and re.match(r"^[A-Z0-9]", text))
                ):
                    flush_ref()
                if ref_current:
                    ref_current += " " + text
                else:
                    ref_current = text
            continue

        # ---------------- content mode ----------------
        mode = "content"

        # case study / insight / example box markers (possibly embedded mid-text)
        for rx, kindname, labelname in ((CS_RE, "case", "Case Study"),
                                        (II_RE, "insight", "Industry Insight"),
                                        (EB_RE, "example", "Example Box")):
            m = rx.search(text)
            if m:
                before = text[: m.start()].strip()
                if before:
                    if is_list(p):
                        add_li(esc(before))
                    else:
                        add_para(esc(before))
                open_box(kindname, "%s %s" % (labelname, m.group(1)), norm(m.group(2)))
                text = None
                break
        if text is None:
            continue

        if is_heading(p) or (p.style is not None and p.style.name == "Title"):
            if len(text) > 95 or (text.endswith(".") and len(text) > 60):
                add_para(para_html(p) or esc(text))
                continue
            key = text.strip().lower()
            if key in DROP_HEADINGS:
                continue
            if key in CURATED_SPLITS:
                if box is not None:
                    close_box()
                for tag, htext in CURATED_SPLITS[key]:
                    target().append({"t": tag, "text": esc(htext)})
                    if tag in ("h2", "h3"):
                        last_heading_text = htext
                continue
            m = EXAMPLES_SPLIT_RE.match(text)
            if m:
                if box is not None and not m.group(1).endswith(":"):
                    close_box()
                last_heading_text = m.group(1)
                target().append({"t": "h3", "text": esc(m.group(1))})
                target().append({"t": "h4", "text": esc(m.group(2))})
                continue
            m = LEADIN_RE.match(text)
            if m and not LEADIN_EXCLUDE.match(m.group(1)):
                add_para("<strong>%s:</strong> %s" % (esc(m.group(1)), esc(m.group(2))))
                continue
            if box is not None and not text.endswith(":"):
                close_box()
            last_heading_text = text.rstrip(":")
            if text.endswith(":"):
                target().append({"t": "h4", "text": esc(text.rstrip(":"))})
            else:
                target().append({"t": "h3", "text": esc(text)})
            continue

        if is_list(p):
            add_li(para_html(p) or esc(text))
            continue

        # Normal / Body text
        html = para_html(p) or esc(text)
        # bold lead-in "Label: rest"
        m = re.match(r"^([A-Z][^:<]{2,45}):\s+(.+)$", text)
        if m and "<strong>" not in html:
            html = "<strong>%s:</strong> %s" % (esc(m.group(1)), esc(m.group(2)))
        add_para(html)

    close_box()
    flush_ref()

    if ch_num in GLOSSARY_OVERRIDES:
        ch["glossary"] = [list(e) for e in GLOSSARY_OVERRIDES[ch_num]]

    # split glossary definitions that fused multiple terms (source artifact)
    fixed_gloss = []
    for term, d in ch["glossary"]:
        parts = re.split(r"(?<=[a-z\)]) ([A-Z][A-Za-z0-9\(\)\- ]{3,42}) — (?=[A-Z])", d)
        if len(parts) > 1 and len(d) > 130:
            fixed_gloss.append([term, parts[0].strip()])
            for k in range(1, len(parts) - 1, 2):
                fixed_gloss.append([parts[k].strip(), parts[k + 1].strip()])
        else:
            fixed_gloss.append([term, d])
    ch["glossary"] = fixed_gloss

    # -------- remove figure-prompt residue near figures --------
    blocks = ch["blocks"]
    to_del = set()
    fig_positions = [i for i, b in enumerate(blocks) if b["t"] == "fig"]
    for fi in fig_positions:
        lo, hi = max(0, fi - 6), min(len(blocks), fi + 6)
        for j in range(lo, hi):
            b = blocks[j]
            plain = ""
            if b["t"] == "h4":
                plain = b["text"].strip().lower()
            elif b["t"] == "p":
                plain = re.sub(r"<[^>]+>", "", b["html"]).strip().lower()
            if b["t"] in ("h4", "p") and plain in ("description", "description:", "descriptions"):
                to_del.add(j)
                k = j + 1
                while k < len(blocks) and k < j + 8 and blocks[k]["t"] in ("p", "ul"):
                    to_del.add(k)
                    k += 1
            elif b["t"] == "p" and VISUAL_HINT_RE.match(re.sub(r"<[^>]+>", "", b["html"])):
                to_del.add(j)
    if to_del:
        ch["blocks"] = [b for i, b in enumerate(blocks) if i not in to_del]

    # pass 2: remove chart-narration residue anchored right after figures
    ch["blocks"] = strip_figure_prompt_residue(ch["blocks"])

    # figure caption fallback: use nearest preceding heading captured at parse time
    for b in ch["blocks"]:
        if b["t"] == "fig":
            ctx = b.pop("ctx", "")
            if not b.get("caption"):
                b["caption"] = ctx or ""

    # -------- promote h3 -> numbered h2 via roadmap fuzzy matching --------
    roadmap_items = []
    for r in ch["roadmap"]:
        roadmap_items.extend([x for x in re.split(r"\s{2,}", r) if x])
    promoted = 0
    if roadmap_items:
        used = set()
        for b in ch["blocks"]:
            if b["t"] == "h3":
                for ri, r in enumerate(roadmap_items):
                    if ri in used:
                        continue
                    if fuzzy(b["text"], r) >= 0.72:
                        b["t"] = "h2"
                        used.add(ri)
                        promoted += 1
                        break
    # assign section numbers
    sec = 0
    for b in ch["blocks"]:
        if b["t"] == "h2":
            sec += 1
            b["num"] = "%d.%d" % (ch_num, sec)
    # figures/tables without numbers -> assign sequentially, avoid duplicates
    seen_f = set()
    fseq = 0
    for b in ch["blocks"]:
        if b["t"] == "fig":
            fseq += 1
            if not b["num"] or b["num"] in seen_f:
                b["num"] = "%d.%d" % (ch_num, fseq)
            seen_f.add(b["num"])
            if not b["caption"]:
                b["caption"] = ""
    return ch, promoted


def main():
    doc = docx.Document(str(SRC))
    stream = build_stream(doc)

    # split into chapters
    bounds = []
    for i, (kind, obj) in enumerate(stream):
        if kind == "p":
            m = CH_RE.match(norm(obj.text))
            if m:
                bounds.append((i, int(m.group(1))))
    print("chapter boundaries:", [(b, n) for b, n in bounds])
    assert len(bounds) == 20, "expected 20 chapters, got %d" % len(bounds)

    manifest = {"chapters": []}
    for bi, (start, ch_num) in enumerate(bounds):
        end = bounds[bi + 1][0] if bi + 1 < len(bounds) else len(stream)
        ch, promoted = parse_chapter(stream[start:end], ch_num, doc)
        figs = [(b["num"], b["caption"] or "(untitled figure)") for b in ch["blocks"] if b["t"] == "fig"]
        tabs = []
        for b in ch["blocks"]:
            if b["t"] == "table":
                tabs.append((b["num"], b["caption"] or ""))
            elif b["t"] == "box":
                for nb in b["blocks"]:
                    if nb["t"] == "table":
                        tabs.append((nb["num"], nb["caption"] or ""))
        (OUT_CONTENT / ("ch%02d.json" % ch_num)).write_text(
            json.dumps(ch, ensure_ascii=False, indent=1), encoding="utf-8")
        nblocks = len(ch["blocks"])
        print("Ch%02d: blocks=%d h2=%d figs=%d tables=%d clos=%d gloss=%d refs=%d recap=%d kw=%d"
              % (ch_num, nblocks, promoted, len(figs), len(tabs), len(ch["clos"]),
                 len(ch["glossary"]), len(ch["references"]), len(ch["recap_items"]), len(ch["keywords"])))
        manifest["chapters"].append({
            "num": ch_num, "id": ch["id"], "title": ch["title"], "subtitle": ch["subtitle"],
            "figures": figs, "tables": tabs,
            "sections": [b["text"] for b in ch["blocks"] if b["t"] == "h2"],
            "glossary_count": len(ch["glossary"]),
            "references_count": len(ch["references"]),
        })
    (OUT_CONTENT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    total_figs = sum(len(c["figures"]) for c in manifest["chapters"])
    total_tabs = sum(len(c["tables"]) for c in manifest["chapters"])
    print("\nTOTAL figures=%d tables=%d" % (total_figs, total_tabs))


if __name__ == "__main__":
    sys.exit(main())
