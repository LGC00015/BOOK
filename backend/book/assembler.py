import hashlib
import json
import threading
from functools import lru_cache
from pathlib import Path

from .styles import PRINT_CSS, PREVIEW_EXTRA_CSS
from .outline import BOOK_META, PARTS, CHAPTERS, part_divider_html, part_of
from . import front_matter as fm
from . import back_matter as bm
from . import docx_chapters

BOOK_DIR = Path(__file__).parent
BUILD_DIR = BOOK_DIR / "build"
PDF_FILE = BUILD_DIR / "book.pdf"
PDF_META_FILE = BUILD_DIR / "book.meta.json"


def _chapter_html(ch):
    part_num, part_title = part_of(ch["num"])
    label = "Part %s &middot; %s" % (part_num, part_title)
    return docx_chapters.chapter_html(ch["num"], label)


def build_sections():
    return list(_sections_cached())


@lru_cache(maxsize=1)
def _sections_cached():
    sections = [
        ("cover", "Cover", fm.cover_html()),
        ("halftitle", "Half Title", fm.halftitle_html()),
        ("titlepage", "Title Page", fm.titlepage_html()),
        ("copyright", "Copyright", fm.copyright_html()),
        ("preface", "Preface", fm.preface_html()),
        ("howto", "How to Use This Book", fm.howto_html()),
        ("syllabus", "Syllabus Mapping", fm.syllabus_html()),
        ("toc", "Table of Contents", fm.toc_html()),
        ("lists", "Figures, Tables & Abbreviations", fm.lists_html()),
    ]
    for part in PARTS:
        sections.append(("part%s" % part["num"], "Part %s — %s" % (part["num"], part["title"]), part_divider_html(part)))
        for ch in CHAPTERS:
            if ch["num"] in part["chapters"]:
                sections.append((ch["id"], "Chapter %d — %s" % (ch["num"], ch["title"]), _chapter_html(ch)))
    sections += [
        ("glossary", "Glossary", bm.glossary_html()),
        ("stdindex", "Standards & Regulations Index", bm.standards_index_html()),
        ("biblio", "Consolidated References", bm.consolidated_refs_html()),
    ]
    return tuple(sections)


PRESS_CSS = """
/* PRESS VARIANT — 3mm bleed + crop/registration marks for commercial printing */
@page { bleed: 3mm; marks: crop cross; }
"""


def full_html(press=False):
    body = "".join(html for _, _, html in build_sections())
    extra = PRESS_CSS if press else ""
    meta = BOOK_META
    return """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>%s — %s</title>
<meta name="author" content="%s">
<meta name="description" content="%s. %s, %s. %s.">
<meta name="keywords" content="medical devices, pharmacy, allied health, regulatory affairs, ISO 13485, CDSCO, FDA, EU MDR, quality management, biocompatibility, textbook">
<meta name="generator" content="Medical Devices Academic Ecosystem — A4 Print Edition, Layout v2.0">
<style>%s%s</style></head>
<body style="string-set: booktitle '%s'">%s</body></html>""" % (
        meta["title"], meta["subtitle"], meta["author"],
        meta["subtitle"], meta["edition"], meta["year"], meta["publisher"],
        PRINT_CSS, extra, meta["title"].upper(), body)


def preview_html(section_id):
    for sid, label, html in build_sections():
        if sid == section_id:
            dark = ' dark' if sid in ("cover",) or sid.startswith("part") else ''
            wrapped = html if sid in ("cover",) or sid.startswith("part") else '<div class="sheet%s">%s</div>' % (dark, html)
            if sid == "cover" or sid.startswith("part"):
                wrapped = '<div class="sheet dark" style="padding:0">%s</div>' % html
            fit_js = ("<script>function fit(){var s=document.querySelector('.sheet');"
                      "if(s){document.body.style.zoom=Math.min(1,(window.innerWidth-16)/s.offsetWidth);}}"
                      "window.addEventListener('load',fit);window.addEventListener('resize',fit);</script>")
            return """<!DOCTYPE html><html><head><meta charset="utf-8"><title>%s</title>
<style>%s%s</style></head><body>%s%s</body></html>""" % (label, PRINT_CSS, PREVIEW_EXTRA_CSS, wrapped, fit_js)
    return None


_lock = threading.Lock()
_cache = {"pdf": None, "pages": 0, "building": False, "error": None}
_press_lock = threading.Lock()
_press_cache = {"pdf": None, "pages": 0, "building": False, "error": None}
PRESS_PDF_FILE = BUILD_DIR / "book_press.pdf"
PRESS_META_FILE = BUILD_DIR / "book_press.meta.json"
_pdfx_lock = threading.Lock()
_pdfx_cache = {"pdf": None, "building": False, "error": None}
PDFX_PDF_FILE = BUILD_DIR / "book_pdfx.pdf"
PDFX_META_FILE = BUILD_DIR / "book_pdfx.meta.json"
PDFX_DEF_FILE = BOOK_DIR / "pdfx_def.ps"
GS_ICC_DIR = "/usr/share/color/icc/ghostscript/"


def _content_hash():
    return hashlib.md5(full_html().encode("utf-8")).hexdigest()


def _load_disk_cache():
    """Reuse the last compiled PDF if the book content is unchanged."""
    try:
        if not (PDF_FILE.exists() and PDF_META_FILE.exists()):
            return False
        meta = json.loads(PDF_META_FILE.read_text())
        if meta.get("hash") != _content_hash():
            return False
        pdf = PDF_FILE.read_bytes()
        if len(pdf) < 1000:
            return False
        _cache.update(pdf=pdf, pages=meta.get("pages", 0), error=None)
        return True
    except Exception:
        return False


def _save_disk_cache(pdf, pages):
    try:
        BUILD_DIR.mkdir(exist_ok=True)
        PDF_FILE.write_bytes(pdf)
        PDF_META_FILE.write_text(json.dumps({"hash": _content_hash(), "pages": pages}))
    except Exception:
        pass


def _render(press=False):
    from weasyprint import HTML
    doc = HTML(string=full_html(press=press), base_url=str(BOOK_DIR)).render()
    return doc.write_pdf(), len(doc.pages)


def build_pdf_sync():
    with _lock:
        if _cache["pdf"] is not None:
            return _cache["pdf"], _cache["pages"]
        if _load_disk_cache():
            return _cache["pdf"], _cache["pages"]
        _cache["building"] = True
        try:
            pdf, pages = _render()
            _cache.update(pdf=pdf, pages=pages, error=None)
            _save_disk_cache(pdf, pages)
        except Exception as e:
            _cache["error"] = str(e)
            raise
        finally:
            _cache["building"] = False
        return _cache["pdf"], _cache["pages"]


def pdf_status():
    return {
        "ready": _cache["pdf"] is not None,
        "building": _cache["building"],
        "pages": _cache["pages"],
        "size_bytes": len(_cache["pdf"]) if _cache["pdf"] else 0,
        "error": _cache["error"],
        "press": {
            "ready": _press_cache["pdf"] is not None or _press_disk_valid(),
            "building": _press_cache["building"],
            "pages": _press_cache["pages"],
        },
    }


def _press_hash():
    return hashlib.md5(full_html(press=True).encode("utf-8")).hexdigest()


def _press_disk_valid():
    try:
        if not (PRESS_PDF_FILE.exists() and PRESS_META_FILE.exists()):
            return False
        return json.loads(PRESS_META_FILE.read_text()).get("hash") == _press_hash()
    except Exception:
        return False


def build_press_pdf_sync():
    """Press-production variant: 3mm bleed + crop/registration marks.
    Built on demand (first request ~40s), then cached in memory and on disk."""
    with _press_lock:
        if _press_cache["pdf"] is not None:
            return _press_cache["pdf"], _press_cache["pages"]
        if _press_disk_valid():
            try:
                pdf = PRESS_PDF_FILE.read_bytes()
                meta = json.loads(PRESS_META_FILE.read_text())
                if len(pdf) > 1000:
                    _press_cache.update(pdf=pdf, pages=meta.get("pages", 0), error=None)
                    return _press_cache["pdf"], _press_cache["pages"]
            except Exception:
                pass
        _press_cache["building"] = True
        try:
            pdf, pages = _render(press=True)
            _press_cache.update(pdf=pdf, pages=pages, error=None)
            try:
                BUILD_DIR.mkdir(exist_ok=True)
                PRESS_PDF_FILE.write_bytes(pdf)
                PRESS_META_FILE.write_text(json.dumps({"hash": _press_hash(), "pages": pages}))
            except Exception:
                pass
        except Exception as e:
            _press_cache["error"] = str(e)
            raise
        finally:
            _press_cache["building"] = False
        return _press_cache["pdf"], _press_cache["pages"]


def warm_pdf_async():
    threading.Thread(target=lambda: _safe_build(), daemon=True).start()


def _safe_build():
    try:
        build_pdf_sync()
    except Exception:
        pass
