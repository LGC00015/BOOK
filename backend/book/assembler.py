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
        ("syllabus", "Syllabus Mapping (BP708T)", fm.syllabus_html()),
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


def full_html():
    body = "".join(html for _, _, html in build_sections())
    return """<!DOCTYPE html><html><head><meta charset="utf-8"><title>%s</title>
<style>%s</style></head>
<body style="string-set: booktitle '%s'">%s</body></html>""" % (
        BOOK_META["title"], PRINT_CSS, BOOK_META["title"].upper(), body)


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


def _render():
    from weasyprint import HTML
    doc = HTML(string=full_html(), base_url=str(BOOK_DIR)).render()
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
    }


def warm_pdf_async():
    threading.Thread(target=lambda: _safe_build(), daemon=True).start()


def _safe_build():
    try:
        build_pdf_sync()
    except Exception:
        pass
