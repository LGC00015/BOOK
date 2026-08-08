"""Backend API tests for Medical Devices textbook production system."""
import os
import time
import pytest
import requests

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL", "").rstrip("/")
if not BASE_URL:
    # fallback: read frontend/.env
    with open("/app/frontend/.env") as f:
        for line in f:
            if line.startswith("REACT_APP_BACKEND_URL="):
                BASE_URL = line.split("=", 1)[1].strip().rstrip("/")
                break

API = f"{BASE_URL}/api"


# ---------- /api/book/meta ----------
class TestBookMeta:
    def test_meta_ok(self):
        r = requests.get(f"{API}/book/meta", timeout=30)
        assert r.status_code == 200
        data = r.json()
        assert "Medical Devices" in data.get("title", "")
        assert data.get("chapters_total") == 14
        assert data.get("chapters_complete") == 2
        assert data.get("figures_count") == 8
        assert data.get("tables_count") == 9
        assert isinstance(data.get("phases"), list) and len(data["phases"]) == 6
        assert isinstance(data.get("pdf"), dict)


# ---------- /api/book/toc ----------
class TestBookToc:
    def test_toc_structure(self):
        r = requests.get(f"{API}/book/toc", timeout=30)
        assert r.status_code == 200
        data = r.json()
        assert len(data.get("front_matter", [])) == 8
        parts = data.get("parts", [])
        assert len(parts) == 5
        assert len(data.get("back_matter", [])) == 4

        # verify ch01 & ch02 complete, others planned
        all_chapters = {c["id"]: c for p in parts for c in p.get("chapters", [])}
        assert all_chapters["ch01"]["status"] == "complete"
        assert all_chapters["ch02"]["status"] == "complete"
        for cid in ["ch03", "ch04", "ch05", "ch14"]:
            assert all_chapters[cid]["status"] == "planned", f"{cid} not planned"


# ---------- /api/book/preview/{section_id} ----------
class TestPreview:
    @pytest.mark.parametrize("sid", [
        "cover", "titlepage", "preface", "syllabus", "toc",
        "ch01", "ch02", "partI", "ch03", "glossary", "answerkeys",
    ])
    def test_preview_valid_sections(self, sid):
        r = requests.get(f"{API}/book/preview/{sid}", timeout=30)
        assert r.status_code == 200, f"section {sid} => {r.status_code}"
        assert "text/html" in r.headers.get("content-type", "").lower()
        assert "<" in r.text  # HTML content

    def test_preview_ch01_contains_intro(self):
        r = requests.get(f"{API}/book/preview/ch01", timeout=30)
        assert r.status_code == 200
        assert "Introduction to Medical Devices" in r.text

    def test_preview_unknown_404(self):
        r = requests.get(f"{API}/book/preview/bogus", timeout=30)
        assert r.status_code == 404


# ---------- /api/book/pdf/status ----------
class TestPdfStatus:
    def test_status_ready(self):
        # poll up to 60s
        deadline = time.time() + 90
        data = None
        while time.time() < deadline:
            r = requests.get(f"{API}/book/pdf/status", timeout=30)
            assert r.status_code == 200
            data = r.json()
            if data.get("ready"):
                break
            time.sleep(3)
        assert data and data.get("ready") is True, f"pdf not ready: {data}"
        assert data.get("pages") == 93, f"expected 93 pages, got {data.get('pages')}"


# ---------- /api/book/pdf ----------
class TestPdfDownload:
    def test_pdf_download(self):
        # ensure ready first
        for _ in range(30):
            s = requests.get(f"{API}/book/pdf/status", timeout=30).json()
            if s.get("ready"):
                break
            time.sleep(3)
        r = requests.get(f"{API}/book/pdf", timeout=120)
        assert r.status_code == 200
        ct = r.headers.get("content-type", "")
        assert "application/pdf" in ct.lower(), f"content-type={ct}"
        assert r.headers.get("X-Page-Count") == "93", f"X-Page-Count={r.headers.get('X-Page-Count')}"
        cd = r.headers.get("Content-Disposition", "")
        assert "attachment" in cd.lower()
        # PDF magic
        assert r.content[:4] == b"%PDF", "not a PDF"
        assert len(r.content) > 50_000, f"pdf too small: {len(r.content)}"
