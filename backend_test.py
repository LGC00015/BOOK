#!/usr/bin/env python3
"""Backend API Testing - Layout v2.0 Verification
Tests all /api/book/* endpoints for Layout v2.0 changes:
1. Metadata: pages=728, syllabus_anchor updated
2. TOC: syllabus title updated (BP708T removed)
3. PDF status: pages=728, new "press" sub-object
4. PDF download: X-Page-Count=728
5. NEW: Press variant endpoint
6. Preview sections regression
7. BP708T removal verification
8. Layout markers in HTML
9. QA corrections still intact
"""

import requests
import sys
import time

# Backend URL from frontend/.env
BASE_URL = "https://med-devices-layout.preview.emergentagent.com/api"

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def log_test(name, passed, details=""):
    status = f"{Colors.GREEN}✓ PASS{Colors.END}" if passed else f"{Colors.RED}✗ FAIL{Colors.END}"
    print(f"{status} - {name}")
    if details:
        print(f"  {details}")
    return passed

def test_meta():
    """Test GET /api/book/meta - pages=728, syllabus_anchor updated"""
    print(f"\n{Colors.BLUE}=== TEST 1: GET /api/book/meta ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/meta", timeout=30)
        if resp.status_code != 200:
            return log_test("GET /api/book/meta", False, f"Status {resp.status_code}")
        
        data = resp.json()
        
        # Check chapters
        chapters_ok = data.get("chapters_total") == 20 and data.get("chapters_complete") == 20
        if not chapters_ok:
            return log_test("Chapters count", False, f"Expected 20/20, got {data.get('chapters_complete')}/{data.get('chapters_total')}")
        log_test("Chapters count", True, "20/20 chapters")
        
        # Check figures
        figures_ok = data.get("figures_count") == 156
        if not figures_ok:
            return log_test("Figures count", False, f"Expected 156, got {data.get('figures_count')}")
        log_test("Figures count", True, "156 figures")
        
        # Check tables
        tables_ok = data.get("tables_count") == 17
        if not tables_ok:
            return log_test("Tables count", False, f"Expected 17, got {data.get('tables_count')}")
        log_test("Tables count", True, "17 tables")
        
        # Check phases
        phases = data.get("phases", [])
        phases_ok = len(phases) == 6 and all(p.get("status") == "complete" for p in phases)
        if not phases_ok:
            return log_test("Phases", False, f"Expected 6 complete phases, got {len(phases)} phases")
        log_test("Phases", True, "6 phases all complete")
        
        # Check PDF ready and pages=728
        pdf = data.get("pdf", {})
        pdf_ready = pdf.get("ready") == True
        pdf_pages = pdf.get("pages") == 728
        if not pdf_ready:
            return log_test("PDF ready", False, f"Expected ready=true, got {pdf.get('ready')}")
        if not pdf_pages:
            return log_test("PDF pages", False, f"Expected pages=728, got {pdf.get('pages')}")
        log_test("PDF status", True, "ready=true, pages=728")
        
        # Check syllabus_anchor (NEW in Layout v2.0)
        syllabus_anchor = data.get("syllabus_anchor", "")
        expected_anchor = "B.Pharm and Allied Health Medical Devices curricula"
        if syllabus_anchor != expected_anchor:
            return log_test("Syllabus anchor", False, f"Expected '{expected_anchor}', got '{syllabus_anchor}'")
        log_test("Syllabus anchor", True, f"'{expected_anchor}'")
        
        return True
    except Exception as e:
        return log_test("GET /api/book/meta", False, str(e))

def test_toc():
    """Test GET /api/book/toc - syllabus title updated, 6 parts structure"""
    print(f"\n{Colors.BLUE}=== TEST 2: GET /api/book/toc ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/toc", timeout=30)
        if resp.status_code != 200:
            return log_test("GET /api/book/toc", False, f"Status {resp.status_code}")
        
        data = resp.json()
        
        # Check parts structure
        parts = data.get("parts", [])
        if len(parts) != 6:
            return log_test("Parts count", False, f"Expected 6 parts, got {len(parts)}")
        
        # Verify part structure: I=[1,2,3], II=[4,5,6], III=[7,8,9], IV=[10,11], V=[12..17], VI=[18,19,20]
        expected_structure = {
            0: [1, 2, 3],
            1: [4, 5, 6],
            2: [7, 8, 9],
            3: [10, 11],
            4: [12, 13, 14, 15, 16, 17],
            5: [18, 19, 20]
        }
        
        for i, part in enumerate(parts):
            chapters = part.get("chapters", [])
            chapter_nums = [ch.get("num") for ch in chapters]
            if chapter_nums != expected_structure[i]:
                return log_test(f"Part {i+1} structure", False, f"Expected {expected_structure[i]}, got {chapter_nums}")
        
        log_test("Parts structure", True, "6 parts with correct chapter distribution")
        
        # Check front matter (8 items)
        front_matter = data.get("front_matter", [])
        if len(front_matter) != 8:
            return log_test("Front matter count", False, f"Expected 8 items, got {len(front_matter)}")
        log_test("Front matter count", True, "8 items")
        
        # Check back matter (3 items)
        back_matter = data.get("back_matter", [])
        if len(back_matter) != 3:
            return log_test("Back matter count", False, f"Expected 3 items, got {len(back_matter)}")
        log_test("Back matter count", True, "3 items")
        
        # Check syllabus title (NEW in Layout v2.0 - BP708T removed)
        syllabus_item = next((item for item in front_matter if item.get("id") == "syllabus"), None)
        if not syllabus_item:
            return log_test("Syllabus item", False, "Syllabus item not found in front_matter")
        
        syllabus_title = syllabus_item.get("title", "")
        expected_title = "Syllabus Mapping"
        if syllabus_title != expected_title:
            return log_test("Syllabus title", False, f"Expected '{expected_title}', got '{syllabus_title}'")
        log_test("Syllabus title", True, f"'{expected_title}' (BP708T removed)")
        
        return True
    except Exception as e:
        return log_test("GET /api/book/toc", False, str(e))

def test_pdf_status():
    """Test GET /api/book/pdf/status - pages=728, new press sub-object"""
    print(f"\n{Colors.BLUE}=== TEST 3: GET /api/book/pdf/status ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/pdf/status", timeout=30)
        if resp.status_code != 200:
            return log_test("GET /api/book/pdf/status", False, f"Status {resp.status_code}")
        
        data = resp.json()
        
        # Check ready
        if not data.get("ready"):
            return log_test("PDF ready", False, f"Expected ready=true, got {data.get('ready')}")
        log_test("PDF ready", True)
        
        # Check building
        if data.get("building"):
            return log_test("PDF building", False, f"Expected building=false, got {data.get('building')}")
        log_test("PDF building", True, "false")
        
        # Check pages=728
        if data.get("pages") != 728:
            return log_test("PDF pages", False, f"Expected 728, got {data.get('pages')}")
        log_test("PDF pages", True, "728")
        
        # Check size_bytes > 3MB
        size_bytes = data.get("size_bytes", 0)
        if size_bytes < 3 * 1024 * 1024:
            return log_test("PDF size", False, f"Expected >3MB, got {size_bytes / (1024*1024):.2f}MB")
        log_test("PDF size", True, f"{size_bytes / (1024*1024):.2f}MB")
        
        # Check error=null
        if data.get("error") is not None:
            return log_test("PDF error", False, f"Expected null, got {data.get('error')}")
        log_test("PDF error", True, "null")
        
        # Check NEW press sub-object
        press = data.get("press")
        if press is None:
            return log_test("Press sub-object", False, "Press sub-object not found")
        
        # Press should have ready, building, pages keys
        if "ready" not in press or "building" not in press or "pages" not in press:
            return log_test("Press sub-object keys", False, f"Missing keys in press object: {press}")
        log_test("Press sub-object", True, f"ready={press.get('ready')}, building={press.get('building')}, pages={press.get('pages')}")
        
        return True
    except Exception as e:
        return log_test("GET /api/book/pdf/status", False, str(e))

def test_pdf_download():
    """Test GET /api/book/pdf - X-Page-Count=728, valid PDF"""
    print(f"\n{Colors.BLUE}=== TEST 4: GET /api/book/pdf ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/pdf", timeout=60)
        if resp.status_code != 200:
            return log_test("GET /api/book/pdf", False, f"Status {resp.status_code}")
        log_test("Status code", True, "200")
        
        # Check content-type
        content_type = resp.headers.get("content-type", "")
        if "application/pdf" not in content_type:
            return log_test("Content-Type", False, f"Expected application/pdf, got {content_type}")
        log_test("Content-Type", True, "application/pdf")
        
        # Check X-Page-Count=728
        page_count = resp.headers.get("X-Page-Count")
        if page_count != "728":
            return log_test("X-Page-Count", False, f"Expected 728, got {page_count}")
        log_test("X-Page-Count", True, "728")
        
        # Check PDF magic bytes
        content = resp.content
        if not content.startswith(b'%PDF'):
            return log_test("PDF magic bytes", False, "Does not start with %PDF")
        log_test("PDF magic bytes", True, "Valid PDF format")
        
        return True
    except Exception as e:
        return log_test("GET /api/book/pdf", False, str(e))

def test_pdf_press_variant():
    """Test NEW GET /api/book/pdf?variant=press - X-Variant header, PRESS filename, 120s timeout"""
    print(f"\n{Colors.BLUE}=== TEST 5: GET /api/book/pdf?variant=press (NEW) ==={Colors.END}")
    try:
        # Use 120s timeout as specified (can take ~60s first build)
        resp = requests.get(f"{BASE_URL}/book/pdf?variant=press", timeout=120)
        if resp.status_code != 200:
            return log_test("GET /api/book/pdf?variant=press", False, f"Status {resp.status_code}")
        log_test("Status code", True, "200")
        
        # Check content-type
        content_type = resp.headers.get("content-type", "")
        if "application/pdf" not in content_type:
            return log_test("Content-Type", False, f"Expected application/pdf, got {content_type}")
        log_test("Content-Type", True, "application/pdf")
        
        # Check X-Variant header
        variant = resp.headers.get("X-Variant")
        if variant != "press":
            return log_test("X-Variant header", False, f"Expected 'press', got '{variant}'")
        log_test("X-Variant header", True, "press")
        
        # Check X-Page-Count=728
        page_count = resp.headers.get("X-Page-Count")
        if page_count != "728":
            return log_test("X-Page-Count", False, f"Expected 728, got {page_count}")
        log_test("X-Page-Count", True, "728")
        
        # Check Content-Disposition filename contains "PRESS"
        content_disposition = resp.headers.get("Content-Disposition", "")
        if "PRESS" not in content_disposition.upper():
            return log_test("Filename contains PRESS", False, f"Content-Disposition: {content_disposition}")
        log_test("Filename contains PRESS", True, f"{content_disposition}")
        
        # Check PDF magic bytes
        content = resp.content
        if not content.startswith(b'%PDF'):
            return log_test("PDF magic bytes", False, "Does not start with %PDF")
        log_test("PDF magic bytes", True, "Valid PDF format")
        
        return True
    except Exception as e:
        return log_test("GET /api/book/pdf?variant=press", False, str(e))

def test_preview_sections():
    """Test preview sections regression - all sections return 200, ch99 returns 404"""
    print(f"\n{Colors.BLUE}=== TEST 6: Preview sections regression ==={Colors.END}")
    
    # Test sections that should return 200
    sections_200 = [
        "cover", "halftitle", "titlepage", "copyright", "preface", "syllabus", 
        "toc", "lists", "partI", "ch01", "ch03", "ch12", "ch20", 
        "glossary", "stdindex", "biblio"
    ]
    
    all_passed = True
    for section_id in sections_200:
        try:
            resp = requests.get(f"{BASE_URL}/book/preview/{section_id}", timeout=30)
            if resp.status_code != 200:
                log_test(f"Preview {section_id}", False, f"Status {resp.status_code}")
                all_passed = False
            else:
                # Check it's valid HTML
                html = resp.text
                if not html or len(html) < 100:
                    log_test(f"Preview {section_id}", False, "HTML too short or empty")
                    all_passed = False
                else:
                    log_test(f"Preview {section_id}", True, f"{len(html)} bytes")
        except Exception as e:
            log_test(f"Preview {section_id}", False, str(e))
            all_passed = False
    
    # Test ch01 contains inline SVG and figure vector class
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch01", timeout=30)
        html = resp.text
        
        svg_count = html.count("<svg")
        if svg_count == 0:
            log_test("ch01 contains <svg elements", False, "No SVG elements found")
            all_passed = False
        else:
            log_test("ch01 contains <svg elements", True, f"{svg_count} SVG elements")
        
        vector_class_count = html.count('class="figure vector"')
        if vector_class_count == 0:
            log_test("ch01 contains figure vector wrappers", False, "No figure vector wrappers found")
            all_passed = False
        else:
            log_test("ch01 contains figure vector wrappers", True, f"{vector_class_count} wrappers")
    except Exception as e:
        log_test("ch01 SVG/vector checks", False, str(e))
        all_passed = False
    
    # Test ch99 returns 404
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch99", timeout=30)
        if resp.status_code != 404:
            log_test("Preview ch99 (should 404)", False, f"Expected 404, got {resp.status_code}")
            all_passed = False
        else:
            log_test("Preview ch99 (should 404)", True, "404")
    except Exception as e:
        log_test("Preview ch99", False, str(e))
        all_passed = False
    
    return all_passed

def test_bp708t_removal():
    """Test BP708T removal - verify BP708T and PCI strings are NOT in cover, titlepage, preface, syllabus, toc"""
    print(f"\n{Colors.BLUE}=== TEST 7: BP708T removal verification ==={Colors.END}")
    
    sections_to_check = ["cover", "titlepage", "preface", "syllabus", "toc"]
    all_passed = True
    
    for section_id in sections_to_check:
        try:
            resp = requests.get(f"{BASE_URL}/book/preview/{section_id}", timeout=30)
            if resp.status_code != 200:
                log_test(f"{section_id} BP708T check", False, f"Status {resp.status_code}")
                all_passed = False
                continue
            
            html = resp.text
            
            # Check BP708T is NOT present
            if "BP708" in html:
                log_test(f"{section_id} BP708T removal", False, "Still contains 'BP708'")
                all_passed = False
            else:
                log_test(f"{section_id} BP708T removal", True, "No 'BP708' found")
            
            # Check PCI is NOT present
            if "PCI" in html:
                log_test(f"{section_id} PCI removal", False, "Still contains 'PCI'")
                all_passed = False
            else:
                log_test(f"{section_id} PCI removal", True, "No 'PCI' found")
        except Exception as e:
            log_test(f"{section_id} BP708T/PCI check", False, str(e))
            all_passed = False
    
    # Check syllabus contains the new text
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/syllabus", timeout=30)
        html = resp.text
        
        expected_text = "Medical Devices (B.Pharm Elective)"
        if expected_text not in html:
            log_test("Syllabus contains new text", False, f"Missing: '{expected_text}'")
            all_passed = False
        else:
            log_test("Syllabus contains new text", True, f"'{expected_text}'")
    except Exception as e:
        log_test("Syllabus new text check", False, str(e))
        all_passed = False
    
    return all_passed

def test_layout_markers():
    """Test layout markers in HTML - data-running attributes, thead/tbody, @page divider-first"""
    print(f"\n{Colors.BLUE}=== TEST 8: Layout markers in HTML ==={Colors.END}")
    
    all_passed = True
    
    # (a) ch01 preview contains data-running attribute on section AND ch-opener div
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch01", timeout=30)
        html = resp.text
        
        # Check data-running on section
        if 'data-running' not in html:
            log_test("ch01 data-running attribute", False, "No data-running attribute found")
            all_passed = False
        else:
            # Count occurrences - should be on section and ch-opener div
            count = html.count('data-running')
            if count < 2:
                log_test("ch01 data-running attribute", False, f"Expected at least 2 occurrences, found {count}")
                all_passed = False
            else:
                log_test("ch01 data-running attribute", True, f"{count} occurrences (section + ch-opener)")
    except Exception as e:
        log_test("ch01 data-running check", False, str(e))
        all_passed = False
    
    # (b) ch03 preview contains <thead> and <tbody> inside table.data
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch03", timeout=30)
        html = resp.text
        
        if '<thead>' not in html:
            log_test("ch03 contains <thead>", False, "No <thead> found")
            all_passed = False
        else:
            log_test("ch03 contains <thead>", True)
        
        if '<tbody>' not in html:
            log_test("ch03 contains <tbody>", False, "No <tbody> found")
            all_passed = False
        else:
            log_test("ch03 contains <tbody>", True)
    except Exception as e:
        log_test("ch03 thead/tbody check", False, str(e))
        all_passed = False
    
    # (c) Full print CSS contains @page divider-first and string(sectitle)
    # CSS is embedded in preview HTML, so check any preview
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch01", timeout=30)
        html = resp.text
        
        if '@page divider-first' not in html:
            log_test("CSS contains @page divider-first", False, "Not found in preview HTML")
            all_passed = False
        else:
            log_test("CSS contains @page divider-first", True)
        
        if 'string(sectitle)' not in html:
            log_test("CSS contains string(sectitle)", False, "Not found in preview HTML")
            all_passed = False
        else:
            log_test("CSS contains string(sectitle)", True)
    except Exception as e:
        log_test("CSS layout markers check", False, str(e))
        all_passed = False
    
    return all_passed

def test_qa_corrections_intact():
    """Test QA corrections still intact - verify specific strings in ch12, ch06, ch03"""
    print(f"\n{Colors.BLUE}=== TEST 9: QA corrections still intact ==={Colors.END}")
    
    all_passed = True
    
    # ch12: QMSR corrections
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch12", timeout=30)
        html = resp.text
        
        checks = [
            ("With effect from 2 February 2026", "QMSR effective date"),
            ("Quality Management System Regulation (QMSR)", "QMSR term")
        ]
        
        for text, label in checks:
            if text not in html:
                log_test(f"ch12: {label}", False, f"Missing: '{text}'")
                all_passed = False
            else:
                log_test(f"ch12: {label}", True)
    except Exception as e:
        log_test("ch12 QA corrections", False, str(e))
        all_passed = False
    
    # ch06: 25 kGy and ETO corrections
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch06", timeout=30)
        html = resp.text
        
        checks = [
            ("validated cycle-specific per ISO 11135", "ETO parameters qualified")
        ]
        
        for text, label in checks:
            if text not in html:
                log_test(f"ch06: {label}", False, f"Missing: '{text}'")
                all_passed = False
            else:
                log_test(f"ch06: {label}", True)
    except Exception as e:
        log_test("ch06 QA corrections", False, str(e))
        all_passed = False
    
    # ch03: 510(k) corrections
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch03", timeout=30)
        html = resp.text
        
        checks = [
            ("typically subject to 510(k); some device types are exempt", "510(k) qualified")
        ]
        
        for text, label in checks:
            if text not in html:
                log_test(f"ch03: {label}", False, f"Missing: '{text}'")
                all_passed = False
            else:
                log_test(f"ch03: {label}", True)
    except Exception as e:
        log_test("ch03 QA corrections", False, str(e))
        all_passed = False
    
    return all_passed

def main():
    print(f"\n{Colors.BLUE}{'='*80}{Colors.END}")
    print(f"{Colors.BLUE}BACKEND API TESTING - LAYOUT v2.0 VERIFICATION{Colors.END}")
    print(f"{Colors.BLUE}Backend URL: {BASE_URL}{Colors.END}")
    print(f"{Colors.BLUE}{'='*80}{Colors.END}")
    
    results = []
    
    # Run all tests
    results.append(("Test 1: GET /api/book/meta (pages=728, syllabus_anchor)", test_meta()))
    results.append(("Test 2: GET /api/book/toc (syllabus title, 6 parts)", test_toc()))
    results.append(("Test 3: GET /api/book/pdf/status (pages=728, press sub-object)", test_pdf_status()))
    results.append(("Test 4: GET /api/book/pdf (X-Page-Count=728)", test_pdf_download()))
    results.append(("Test 5: GET /api/book/pdf?variant=press (NEW)", test_pdf_press_variant()))
    results.append(("Test 6: Preview sections regression", test_preview_sections()))
    results.append(("Test 7: BP708T removal verification", test_bp708t_removal()))
    results.append(("Test 8: Layout markers in HTML", test_layout_markers()))
    results.append(("Test 9: QA corrections still intact", test_qa_corrections_intact()))
    
    # SUMMARY
    print(f"\n{Colors.BLUE}{'='*80}{Colors.END}")
    print(f"{Colors.BLUE}TEST SUMMARY{Colors.END}")
    print(f"{Colors.BLUE}{'='*80}{Colors.END}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\nTotal: {passed}/{total} test scenarios passed")
    
    if passed == total:
        print(f"{Colors.GREEN}✓ ALL TESTS PASSED{Colors.END}")
        return 0
    else:
        print(f"\n{Colors.RED}FAILED TESTS:{Colors.END}")
        for name, result in results:
            if not result:
                print(f"  {Colors.RED}✗ {name}{Colors.END}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
