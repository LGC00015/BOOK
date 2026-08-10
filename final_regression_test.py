#!/usr/bin/env python3
"""
Final Regression Test - Medical Devices Textbook (Vector SVG Edition)
Tests all backend endpoints after figure conversion to inline vector SVG
Book: 726 pages, 156 vector figures, ~3.7MB PDF
"""

import requests
import time
import sys
import os
from pathlib import Path

# Backend URL from frontend/.env
BASE_URL = "https://happy-kowalevski-8.preview.emergentagent.com"
API_BASE = f"{BASE_URL}/api"

# Expected values for this edition
EXPECTED_PAGES = 726
EXPECTED_FIGURES = 156
EXPECTED_TABLES = 17
EXPECTED_CHAPTERS = 20
EXPECTED_PARTS = 6
EXPECTED_PDF_SIZE_MIN = 3.5 * 1024 * 1024  # 3.5 MB
EXPECTED_PDF_SIZE_MAX = 4.0 * 1024 * 1024  # 4.0 MB

# Color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

class TestResults:
    def __init__(self):
        self.passed = []
        self.failed = []
        self.total = 0
    
    def add_pass(self, test_name: str, details: str = ""):
        self.passed.append((test_name, details))
        self.total += 1
        print(f"{GREEN}✓{RESET} {test_name}")
        if details:
            print(f"  {BLUE}{details}{RESET}")
    
    def add_fail(self, test_name: str, error: str):
        self.failed.append((test_name, error))
        self.total += 1
        print(f"{RED}✗{RESET} {test_name}")
        print(f"  {RED}ERROR: {error}{RESET}")
    
    def summary(self):
        print(f"\n{'='*80}")
        print(f"FINAL REGRESSION TEST SUMMARY")
        print(f"{'='*80}")
        print(f"Total Tests: {self.total}")
        print(f"{GREEN}Passed: {len(self.passed)}{RESET}")
        print(f"{RED}Failed: {len(self.failed)}{RESET}")
        
        if self.failed:
            print(f"\n{RED}FAILED TESTS:{RESET}")
            for name, error in self.failed:
                print(f"  • {name}")
                print(f"    {error}")
        
        return len(self.failed) == 0

results = TestResults()

def test_1_book_meta():
    """Test 1: GET /api/book/meta - verify 20/20 chapters, 156 figures, 17 tables, 6 phases, pdf.ready"""
    print(f"\n{BLUE}TEST 1: GET /api/book/meta{RESET}")
    
    try:
        # Poll up to 90 seconds for PDF to be ready
        max_wait = 90
        start_time = time.time()
        pdf_ready = False
        
        while time.time() - start_time < max_wait:
            response = requests.get(f"{API_BASE}/book/meta", timeout=30)
            
            if response.status_code != 200:
                results.add_fail("GET /api/book/meta", f"Status code {response.status_code}")
                return
            
            data = response.json()
            
            # Check if PDF is ready
            if data.get("pdf", {}).get("ready"):
                pdf_ready = True
                break
            
            # If building, wait and retry
            if data.get("pdf", {}).get("building"):
                print(f"  {YELLOW}PDF building... waiting (elapsed: {int(time.time() - start_time)}s){RESET}")
                time.sleep(5)
            else:
                break
        
        # Final check
        response = requests.get(f"{API_BASE}/book/meta", timeout=30)
        data = response.json()
        
        # Verify all fields
        errors = []
        
        if data.get("chapters_total") != EXPECTED_CHAPTERS:
            errors.append(f"chapters_total={data.get('chapters_total')}, expected {EXPECTED_CHAPTERS}")
        
        if data.get("chapters_complete") != EXPECTED_CHAPTERS:
            errors.append(f"chapters_complete={data.get('chapters_complete')}, expected {EXPECTED_CHAPTERS}")
        
        if data.get("figures_count") != EXPECTED_FIGURES:
            errors.append(f"figures_count={data.get('figures_count')}, expected {EXPECTED_FIGURES}")
        
        if data.get("tables_count") != EXPECTED_TABLES:
            errors.append(f"tables_count={data.get('tables_count')}, expected {EXPECTED_TABLES}")
        
        phases = data.get("phases", [])
        if len(phases) != EXPECTED_PARTS:
            errors.append(f"phases count={len(phases)}, expected {EXPECTED_PARTS}")
        else:
            incomplete_phases = [p for p in phases if p.get("status") != "complete"]
            if incomplete_phases:
                errors.append(f"incomplete phases: {[p.get('title') for p in incomplete_phases]}")
        
        pdf = data.get("pdf", {})
        if not pdf.get("ready"):
            errors.append(f"pdf.ready={pdf.get('ready')}, expected True (waited {int(time.time() - start_time)}s)")
        
        if errors:
            results.add_fail("GET /api/book/meta", "; ".join(errors))
        else:
            details = (f"chapters: {data['chapters_complete']}/{data['chapters_total']}, "
                      f"figures: {data['figures_count']}, tables: {data['tables_count']}, "
                      f"phases: {len(phases)} complete, pdf.ready: {pdf.get('ready')}")
            results.add_pass("GET /api/book/meta", details)
    
    except Exception as e:
        results.add_fail("GET /api/book/meta", str(e))

def test_2_book_toc():
    """Test 2: GET /api/book/toc - verify 6 parts, 20 chapters, back_matter"""
    print(f"\n{BLUE}TEST 2: GET /api/book/toc{RESET}")
    
    try:
        response = requests.get(f"{API_BASE}/book/toc", timeout=30)
        
        if response.status_code != 200:
            results.add_fail("GET /api/book/toc", f"Status code {response.status_code}")
            return
        
        data = response.json()
        errors = []
        
        # Check parts
        parts = data.get("parts", [])
        if len(parts) != EXPECTED_PARTS:
            errors.append(f"parts count={len(parts)}, expected {EXPECTED_PARTS}")
        
        # Count total chapters across all parts
        total_chapters = sum(len(p.get("chapters", [])) for p in parts)
        if total_chapters != EXPECTED_CHAPTERS:
            errors.append(f"total chapters in parts={total_chapters}, expected {EXPECTED_CHAPTERS}")
        
        # Check back_matter
        back_matter = data.get("back_matter", [])
        expected_back = ["glossary", "stdindex", "biblio"]
        back_ids = [b.get("id") for b in back_matter]
        
        if back_ids != expected_back:
            errors.append(f"back_matter ids={back_ids}, expected {expected_back}")
        
        # Check front_matter exists
        front_matter = data.get("front_matter", [])
        if len(front_matter) < 8:
            errors.append(f"front_matter count={len(front_matter)}, expected at least 8")
        
        if errors:
            results.add_fail("GET /api/book/toc", "; ".join(errors))
        else:
            details = (f"parts: {len(parts)}, chapters: {total_chapters}, "
                      f"front_matter: {len(front_matter)}, back_matter: {len(back_matter)}")
            results.add_pass("GET /api/book/toc", details)
    
    except Exception as e:
        results.add_fail("GET /api/book/toc", str(e))

def test_3_preview_ch01_svg():
    """Test 3: GET /api/book/preview/ch01 - MUST contain '<svg' and 'class="figure vector"'"""
    print(f"\n{BLUE}TEST 3: GET /api/book/preview/ch01 (SVG figures){RESET}")
    
    try:
        response = requests.get(f"{API_BASE}/book/preview/ch01", timeout=30)
        
        if response.status_code != 200:
            results.add_fail("GET /api/book/preview/ch01", f"Status code {response.status_code}")
            return
        
        html = response.text
        errors = []
        
        # CRITICAL: Must contain SVG elements
        if '<svg' not in html:
            errors.append("HTML does NOT contain '<svg' - vector figures missing!")
        
        # CRITICAL: Must contain vector figure class
        if 'class="figure vector"' not in html:
            errors.append("HTML does NOT contain 'class=\"figure vector\"' - vector wrapper missing!")
        
        # Check for basic chapter structure
        if 'Introduction to Medical Devices' not in html:
            errors.append("Chapter title 'Introduction to Medical Devices' not found")
        
        # Check it's not broken/empty
        if len(html) < 1000:
            errors.append(f"HTML too short ({len(html)} bytes) - likely broken")
        
        if errors:
            results.add_fail("GET /api/book/preview/ch01", "; ".join(errors))
        else:
            svg_count = html.count('<svg')
            vector_count = html.count('class="figure vector"')
            details = f"HTML contains {svg_count} SVG elements, {vector_count} vector figures, {len(html)} bytes"
            results.add_pass("GET /api/book/preview/ch01", details)
    
    except Exception as e:
        results.add_fail("GET /api/book/preview/ch01", str(e))

def test_4_preview_404():
    """Test 4: GET /api/book/preview/ch99 - should return 404"""
    print(f"\n{BLUE}TEST 4: GET /api/book/preview/ch99 (404 test){RESET}")
    
    try:
        response = requests.get(f"{API_BASE}/book/preview/ch99", timeout=30)
        
        if response.status_code == 404:
            results.add_pass("GET /api/book/preview/ch99", "Correctly returns 404 for unknown section")
        else:
            results.add_fail("GET /api/book/preview/ch99", f"Expected 404, got {response.status_code}")
    
    except Exception as e:
        results.add_fail("GET /api/book/preview/ch99", str(e))

def test_5_pdf_status():
    """Test 5: GET /api/book/pdf/status - verify ready=true, pages=726, size ~3.7MB, error=null"""
    print(f"\n{BLUE}TEST 5: GET /api/book/pdf/status{RESET}")
    
    try:
        response = requests.get(f"{API_BASE}/book/pdf/status", timeout=30)
        
        if response.status_code != 200:
            results.add_fail("GET /api/book/pdf/status", f"Status code {response.status_code}")
            return
        
        data = response.json()
        errors = []
        
        if not data.get("ready"):
            errors.append(f"ready={data.get('ready')}, expected True")
        
        if data.get("pages") != EXPECTED_PAGES:
            errors.append(f"pages={data.get('pages')}, expected {EXPECTED_PAGES}")
        
        size_bytes = data.get("size_bytes", 0)
        size_mb = size_bytes / (1024 * 1024)
        if size_bytes < EXPECTED_PDF_SIZE_MIN or size_bytes > EXPECTED_PDF_SIZE_MAX:
            errors.append(f"size={size_mb:.2f}MB, expected ~3.7MB (3.5-4.0MB range)")
        
        if data.get("error") is not None:
            errors.append(f"error={data.get('error')}, expected null")
        
        if errors:
            results.add_fail("GET /api/book/pdf/status", "; ".join(errors))
        else:
            details = f"ready: {data['ready']}, pages: {data['pages']}, size: {size_mb:.2f}MB, error: {data['error']}"
            results.add_pass("GET /api/book/pdf/status", details)
    
    except Exception as e:
        results.add_fail("GET /api/book/pdf/status", str(e))

def test_6_pdf_download():
    """Test 6: GET /api/book/pdf - verify 200, application/pdf, X-Page-Count=726, %PDF magic, ~3.7MB"""
    print(f"\n{BLUE}TEST 6: GET /api/book/pdf (download){RESET}")
    
    try:
        response = requests.get(f"{API_BASE}/book/pdf", timeout=120)
        
        if response.status_code != 200:
            results.add_fail("GET /api/book/pdf", f"Status code {response.status_code}")
            return
        
        errors = []
        
        # Check content type
        content_type = response.headers.get("Content-Type", "")
        if "application/pdf" not in content_type:
            errors.append(f"Content-Type={content_type}, expected application/pdf")
        
        # Check X-Page-Count header
        page_count = response.headers.get("X-Page-Count")
        if page_count != str(EXPECTED_PAGES):
            errors.append(f"X-Page-Count={page_count}, expected {EXPECTED_PAGES}")
        
        # Check PDF magic bytes
        pdf_data = response.content
        if not pdf_data.startswith(b'%PDF'):
            errors.append("PDF does not start with %PDF magic bytes")
        
        # Check size
        size_bytes = len(pdf_data)
        size_mb = size_bytes / (1024 * 1024)
        if size_bytes < EXPECTED_PDF_SIZE_MIN or size_bytes > EXPECTED_PDF_SIZE_MAX:
            errors.append(f"PDF size={size_mb:.2f}MB, expected ~3.7MB (3.5-4.0MB range)")
        
        if errors:
            results.add_fail("GET /api/book/pdf", "; ".join(errors))
        else:
            details = f"Content-Type: {content_type}, X-Page-Count: {page_count}, size: {size_mb:.2f}MB, valid PDF"
            results.add_pass("GET /api/book/pdf", details)
    
    except Exception as e:
        results.add_fail("GET /api/book/pdf", str(e))

def test_7_disk_cache():
    """Test 7: Verify disk cache exists - /app/backend/book/build/book.pdf + book.meta.json"""
    print(f"\n{BLUE}TEST 7: Disk cache verification{RESET}")
    
    try:
        pdf_path = Path("/app/backend/book/build/book.pdf")
        meta_path = Path("/app/backend/book/build/book.meta.json")
        
        errors = []
        
        if not pdf_path.exists():
            errors.append(f"PDF cache file does not exist: {pdf_path}")
        else:
            size_mb = pdf_path.stat().st_size / (1024 * 1024)
            if size_mb < 3.5 or size_mb > 4.0:
                errors.append(f"PDF cache size={size_mb:.2f}MB, expected ~3.7MB")
        
        if not meta_path.exists():
            errors.append(f"Meta cache file does not exist: {meta_path}")
        else:
            import json
            meta = json.loads(meta_path.read_text())
            if meta.get("pages") != EXPECTED_PAGES:
                errors.append(f"Meta pages={meta.get('pages')}, expected {EXPECTED_PAGES}")
            if not meta.get("hash"):
                errors.append("Meta hash is missing")
        
        if errors:
            results.add_fail("Disk cache verification", "; ".join(errors))
        else:
            pdf_size_mb = pdf_path.stat().st_size / (1024 * 1024)
            details = f"book.pdf exists ({pdf_size_mb:.2f}MB), book.meta.json exists with pages={meta.get('pages')}"
            results.add_pass("Disk cache verification", details)
    
    except Exception as e:
        results.add_fail("Disk cache verification", str(e))

def test_8_sample_previews():
    """Test 8: Sample other preview sections to ensure they work"""
    print(f"\n{BLUE}TEST 8: Sample preview sections{RESET}")
    
    sections_to_test = ["cover", "toc", "ch05", "ch13", "ch20", "glossary", "biblio"]
    
    try:
        errors = []
        for section_id in sections_to_test:
            response = requests.get(f"{API_BASE}/book/preview/{section_id}", timeout=30)
            if response.status_code != 200:
                errors.append(f"{section_id}: status {response.status_code}")
            elif len(response.text) < 100:
                errors.append(f"{section_id}: HTML too short ({len(response.text)} bytes)")
        
        if errors:
            results.add_fail("Sample preview sections", "; ".join(errors))
        else:
            results.add_pass("Sample preview sections", f"All {len(sections_to_test)} sections return valid HTML")
    
    except Exception as e:
        results.add_fail("Sample preview sections", str(e))

def main():
    print(f"\n{'='*80}")
    print(f"FINAL REGRESSION TEST - Medical Devices Textbook")
    print(f"Vector SVG Edition: 726 pages, 156 figures, ~3.7MB")
    print(f"Backend: {BASE_URL}")
    print(f"{'='*80}\n")
    
    # Run all tests
    test_1_book_meta()
    test_2_book_toc()
    test_3_preview_ch01_svg()
    test_4_preview_404()
    test_5_pdf_status()
    test_6_pdf_download()
    test_7_disk_cache()
    test_8_sample_previews()
    
    # Print summary
    success = results.summary()
    
    if success:
        print(f"\n{GREEN}{'='*80}")
        print(f"ALL TESTS PASSED ✓")
        print(f"{'='*80}{RESET}\n")
        sys.exit(0)
    else:
        print(f"\n{RED}{'='*80}")
        print(f"SOME TESTS FAILED ✗")
        print(f"{'='*80}{RESET}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
