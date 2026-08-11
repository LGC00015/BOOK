#!/usr/bin/env python3
"""Backend API Testing - Regulatory QA Corrections Verification
Tests all /api/book/* endpoints for:
1. Regression: meta, toc, pdf/status, pdf endpoints
2. Corrected wordings in chapter previews (51+3 QA corrections)
3. Vector SVG figure rendering
"""

import requests
import sys
import time

# Backend URL from frontend/.env
BASE_URL = "https://happy-kowalevski-8.preview.emergentagent.com/api"

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

def test_regression_meta():
    """Test GET /api/book/meta - 20/20 chapters, 156 figures, 6 phases complete, pdf ready"""
    print(f"\n{Colors.BLUE}=== REGRESSION TEST: GET /api/book/meta ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/meta", timeout=90)
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
        
        # Check phases
        phases = data.get("phases", [])
        phases_ok = len(phases) == 6 and all(p.get("status") == "complete" for p in phases)
        if not phases_ok:
            return log_test("Phases", False, f"Expected 6 complete phases, got {len(phases)} phases")
        log_test("Phases", True, "6 phases all complete")
        
        # Check PDF ready
        pdf = data.get("pdf", {})
        pdf_ok = pdf.get("ready") == True and pdf.get("pages") == 726
        if not pdf_ok:
            return log_test("PDF status", False, f"Expected ready=true, pages=726, got ready={pdf.get('ready')}, pages={pdf.get('pages')}")
        log_test("PDF status", True, "ready=true, pages=726")
        
        return True
    except Exception as e:
        return log_test("GET /api/book/meta", False, str(e))

def test_regression_toc():
    """Test GET /api/book/toc - 6 parts"""
    print(f"\n{Colors.BLUE}=== REGRESSION TEST: GET /api/book/toc ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/toc", timeout=30)
        if resp.status_code != 200:
            return log_test("GET /api/book/toc", False, f"Status {resp.status_code}")
        
        data = resp.json()
        
        # Check parts
        parts = data.get("parts", [])
        parts_ok = len(parts) == 6
        if not parts_ok:
            return log_test("Parts count", False, f"Expected 6 parts, got {len(parts)}")
        log_test("Parts count", True, "6 parts")
        
        return True
    except Exception as e:
        return log_test("GET /api/book/toc", False, str(e))

def test_regression_pdf_status():
    """Test GET /api/book/pdf/status - ready=true, pages=726"""
    print(f"\n{Colors.BLUE}=== REGRESSION TEST: GET /api/book/pdf/status ==={Colors.END}")
    try:
        # Poll up to 90s as per requirements
        max_wait = 90
        start = time.time()
        while time.time() - start < max_wait:
            resp = requests.get(f"{BASE_URL}/book/pdf/status", timeout=30)
            if resp.status_code != 200:
                return log_test("GET /api/book/pdf/status", False, f"Status {resp.status_code}")
            
            data = resp.json()
            if data.get("ready") == True:
                pages_ok = data.get("pages") == 726
                if not pages_ok:
                    return log_test("PDF pages", False, f"Expected 726 pages, got {data.get('pages')}")
                log_test("PDF status", True, f"ready=true, pages=726")
                return True
            
            time.sleep(2)
        
        return log_test("PDF status", False, "PDF not ready after 90s")
    except Exception as e:
        return log_test("GET /api/book/pdf/status", False, str(e))

def test_regression_pdf_download():
    """Test GET /api/book/pdf - 200, X-Page-Count=726, %PDF magic"""
    print(f"\n{Colors.BLUE}=== REGRESSION TEST: GET /api/book/pdf ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/pdf", timeout=60)
        if resp.status_code != 200:
            return log_test("GET /api/book/pdf", False, f"Status {resp.status_code}")
        
        # Check X-Page-Count header
        page_count = resp.headers.get("X-Page-Count")
        if page_count != "726":
            return log_test("X-Page-Count header", False, f"Expected 726, got {page_count}")
        log_test("X-Page-Count header", True, "726")
        
        # Check PDF magic bytes
        content = resp.content
        if not content.startswith(b'%PDF'):
            return log_test("PDF magic bytes", False, "Does not start with %PDF")
        log_test("PDF magic bytes", True, "Valid PDF format")
        
        return True
    except Exception as e:
        return log_test("GET /api/book/pdf", False, str(e))

def test_corrected_wordings_ch12():
    """Test ch12 QA corrections - QMSR terminology"""
    print(f"\n{Colors.BLUE}=== CORRECTED WORDINGS: ch12 (QMSR) ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch12", timeout=30)
        if resp.status_code != 200:
            return log_test("GET /api/book/preview/ch12", False, f"Status {resp.status_code}")
        
        html = resp.text
        
        # Must contain: "With effect from 2 February 2026, FDA replaced the former Quality System Regulation"
        check1 = "With effect from 2 February 2026, FDA replaced the former Quality System Regulation" in html
        if not check1:
            return log_test("ch12: QMSR effective date", False, "Missing: 'With effect from 2 February 2026, FDA replaced the former Quality System Regulation'")
        log_test("ch12: QMSR effective date", True)
        
        # Must contain: "Quality Management System Regulation (QMSR)"
        check2 = "Quality Management System Regulation (QMSR)" in html
        if not check2:
            return log_test("ch12: QMSR term", False, "Missing: 'Quality Management System Regulation (QMSR)'")
        log_test("ch12: QMSR term", True)
        
        # Must contain: "QMSR (Quality Management System Regulation)"
        check3 = "QMSR (Quality Management System Regulation)" in html
        if not check3:
            return log_test("ch12: QMSR abbreviation", False, "Missing: 'QMSR (Quality Management System Regulation)'")
        log_test("ch12: QMSR abbreviation", True)
        
        # Must NOT contain: "FDA is transitioning from QSR"
        check4 = "FDA is transitioning from QSR" not in html
        if not check4:
            return log_test("ch12: Old transition text removed", False, "Still contains: 'FDA is transitioning from QSR'")
        log_test("ch12: Old transition text removed", True)
        
        return True
    except Exception as e:
        return log_test("ch12 corrections", False, str(e))

def test_corrected_wordings_ch06():
    """Test ch06 QA corrections - 25 kGy and ETO parameters qualified"""
    print(f"\n{Colors.BLUE}=== CORRECTED WORDINGS: ch06 (25 kGy, ETO) ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch06", timeout=30)
        if resp.status_code != 200:
            return log_test("GET /api/book/preview/ch06", False, f"Status {resp.status_code}")
        
        html = resp.text
        
        # Must contain: "commonly referenced example; the minimum sterilization dose must be established"
        check1 = "commonly referenced example; the minimum sterilization dose must be established" in html
        if not check1:
            return log_test("ch06: 25 kGy qualified", False, "Missing: 'commonly referenced example; the minimum sterilization dose must be established'")
        log_test("ch06: 25 kGy qualified", True)
        
        # Must contain: "validated cycle-specific per ISO 11135"
        check2 = "validated cycle-specific per ISO 11135" in html
        if not check2:
            return log_test("ch06: ETO parameters qualified", False, "Missing: 'validated cycle-specific per ISO 11135'")
        log_test("ch06: ETO parameters qualified", True)
        
        return True
    except Exception as e:
        return log_test("ch06 corrections", False, str(e))

def test_corrected_wordings_ch03():
    """Test ch03 QA corrections - 510(k) qualified"""
    print(f"\n{Colors.BLUE}=== CORRECTED WORDINGS: ch03 (510(k)) ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch03", timeout=30)
        if resp.status_code != 200:
            return log_test("GET /api/book/preview/ch03", False, f"Status {resp.status_code}")
        
        html = resp.text
        
        # Must contain: "typically subject to 510(k); some device types are exempt"
        check1 = "typically subject to 510(k); some device types are exempt" in html
        if not check1:
            return log_test("ch03: 510(k) qualified", False, "Missing: 'typically subject to 510(k); some device types are exempt'")
        log_test("ch03: 510(k) qualified", True)
        
        return True
    except Exception as e:
        return log_test("ch03 corrections", False, str(e))

def test_corrected_wordings_ch13():
    """Test ch13 QA corrections - 510(k) qualified"""
    print(f"\n{Colors.BLUE}=== CORRECTED WORDINGS: ch13 (510(k)) ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch13", timeout=30)
        if resp.status_code != 200:
            return log_test("GET /api/book/preview/ch13", False, f"Status {resp.status_code}")
        
        html = resp.text
        
        # Must contain: "Usually requires 510(k) premarket notification"
        check1 = "Usually requires 510(k) premarket notification" in html
        if not check1:
            return log_test("ch13: 510(k) qualified", False, "Missing: 'Usually requires 510(k) premarket notification'")
        log_test("ch13: 510(k) qualified", True)
        
        return True
    except Exception as e:
        return log_test("ch13 corrections", False, str(e))

def test_corrected_wordings_ch02():
    """Test ch02 QA corrections - market projections dated"""
    print(f"\n{Colors.BLUE}=== CORRECTED WORDINGS: ch02 (market projections) ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch02", timeout=30)
        if resp.status_code != 200:
            return log_test("GET /api/book/preview/ch02", False, f"Status {resp.status_code}")
        
        html = resp.text
        
        # Must contain: "projected in industry estimates (c. 2024) to reach"
        check1 = "projected in industry estimates (c. 2024) to reach" in html
        if not check1:
            return log_test("ch02: market projections dated", False, "Missing: 'projected in industry estimates (c. 2024) to reach'")
        log_test("ch02: market projections dated", True)
        
        return True
    except Exception as e:
        return log_test("ch02 corrections", False, str(e))

def test_corrected_wordings_ch01():
    """Test ch01 QA corrections - imports dated, QMSR"""
    print(f"\n{Colors.BLUE}=== CORRECTED WORDINGS: ch01 (imports, QMSR) ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch01", timeout=30)
        if resp.status_code != 200:
            return log_test("GET /api/book/preview/ch01", False, f"Status {resp.status_code}")
        
        html = resp.text
        
        # Must contain: "imported (industry estimates, c. 2024)"
        check1 = "imported (industry estimates, c. 2024)" in html
        if not check1:
            return log_test("ch01: imports dated", False, "Missing: 'imported (industry estimates, c. 2024)'")
        log_test("ch01: imports dated", True)
        
        # Must contain: "Quality Management System Regulation (QMSR)"
        check2 = "Quality Management System Regulation (QMSR)" in html
        if not check2:
            return log_test("ch01: QMSR term", False, "Missing: 'Quality Management System Regulation (QMSR)'")
        log_test("ch01: QMSR term", True)
        
        return True
    except Exception as e:
        return log_test("ch01 corrections", False, str(e))

def test_corrected_wordings_stdindex():
    """Test stdindex QA corrections - ISO 13485:2016 incorporated"""
    print(f"\n{Colors.BLUE}=== CORRECTED WORDINGS: stdindex ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/stdindex", timeout=30)
        if resp.status_code != 200:
            return log_test("GET /api/book/preview/stdindex", False, f"Status {resp.status_code}")
        
        html = resp.text
        
        # Must contain: "ISO 13485:2016 incorporated by reference (eff. 2 Feb 2026)"
        check1 = "ISO 13485:2016 incorporated by reference (eff. 2 Feb 2026)" in html
        if not check1:
            return log_test("stdindex: ISO 13485 incorporation", False, "Missing: 'ISO 13485:2016 incorporated by reference (eff. 2 Feb 2026)'")
        log_test("stdindex: ISO 13485 incorporation", True)
        
        return True
    except Exception as e:
        return log_test("stdindex corrections", False, str(e))

def test_corrected_wordings_lists():
    """Test lists QA corrections - QMSR in abbreviations"""
    print(f"\n{Colors.BLUE}=== CORRECTED WORDINGS: lists ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/lists", timeout=30)
        if resp.status_code != 200:
            return log_test("GET /api/book/preview/lists", False, f"Status {resp.status_code}")
        
        html = resp.text
        
        # Must contain: "Quality Management System Regulation (US FDA, 21 CFR Part 820)"
        check1 = "Quality Management System Regulation (US FDA, 21 CFR Part 820)" in html
        if not check1:
            return log_test("lists: QMSR abbreviation", False, "Missing: 'Quality Management System Regulation (US FDA, 21 CFR Part 820)'")
        log_test("lists: QMSR abbreviation", True)
        
        return True
    except Exception as e:
        return log_test("lists corrections", False, str(e))

def test_corrected_wordings_ch11():
    """Test ch11 QA corrections - 25 kGy VDmax/overkill"""
    print(f"\n{Colors.BLUE}=== CORRECTED WORDINGS: ch11 (VDmax) ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch11", timeout=30)
        if resp.status_code != 200:
            return log_test("GET /api/book/preview/ch11", False, f"Status {resp.status_code}")
        
        html = resp.text
        
        # Must contain: "VDmax/overkill substantiation per ISO 11137-2"
        check1 = "VDmax/overkill substantiation per ISO 11137-2" in html
        if not check1:
            return log_test("ch11: VDmax/overkill", False, "Missing: 'VDmax/overkill substantiation per ISO 11137-2'")
        log_test("ch11: VDmax/overkill", True)
        
        return True
    except Exception as e:
        return log_test("ch11 corrections", False, str(e))

def test_vector_figures_ch12():
    """Test ch12 contains vector SVG figures"""
    print(f"\n{Colors.BLUE}=== VECTOR FIGURES: ch12 ==={Colors.END}")
    try:
        resp = requests.get(f"{BASE_URL}/book/preview/ch12", timeout=30)
        if resp.status_code != 200:
            return log_test("GET /api/book/preview/ch12", False, f"Status {resp.status_code}")
        
        html = resp.text
        
        # Must contain: '<svg'
        check1 = '<svg' in html
        if not check1:
            return log_test("ch12: Vector SVG figures", False, "Missing: '<svg' elements")
        log_test("ch12: Vector SVG figures", True, "Contains inline SVG elements")
        
        return True
    except Exception as e:
        return log_test("ch12 vector figures", False, str(e))

def main():
    print(f"\n{Colors.BLUE}{'='*80}{Colors.END}")
    print(f"{Colors.BLUE}BACKEND API TESTING - REGULATORY QA CORRECTIONS VERIFICATION{Colors.END}")
    print(f"{Colors.BLUE}Backend URL: {BASE_URL}{Colors.END}")
    print(f"{Colors.BLUE}{'='*80}{Colors.END}")
    
    results = []
    
    # REGRESSION TESTS
    results.append(("Regression: GET /api/book/meta", test_regression_meta()))
    results.append(("Regression: GET /api/book/toc", test_regression_toc()))
    results.append(("Regression: GET /api/book/pdf/status", test_regression_pdf_status()))
    results.append(("Regression: GET /api/book/pdf", test_regression_pdf_download()))
    
    # CORRECTED WORDINGS TESTS
    results.append(("Corrected wordings: ch12 (QMSR)", test_corrected_wordings_ch12()))
    results.append(("Corrected wordings: ch06 (25 kGy, ETO)", test_corrected_wordings_ch06()))
    results.append(("Corrected wordings: ch03 (510(k))", test_corrected_wordings_ch03()))
    results.append(("Corrected wordings: ch13 (510(k))", test_corrected_wordings_ch13()))
    results.append(("Corrected wordings: ch02 (market)", test_corrected_wordings_ch02()))
    results.append(("Corrected wordings: ch01 (imports, QMSR)", test_corrected_wordings_ch01()))
    results.append(("Corrected wordings: stdindex", test_corrected_wordings_stdindex()))
    results.append(("Corrected wordings: lists", test_corrected_wordings_lists()))
    results.append(("Corrected wordings: ch11 (VDmax)", test_corrected_wordings_ch11()))
    
    # VECTOR FIGURES TEST
    results.append(("Vector figures: ch12", test_vector_figures_ch12()))
    
    # SUMMARY
    print(f"\n{Colors.BLUE}{'='*80}{Colors.END}")
    print(f"{Colors.BLUE}TEST SUMMARY{Colors.END}")
    print(f"{Colors.BLUE}{'='*80}{Colors.END}")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
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
