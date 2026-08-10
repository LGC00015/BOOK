#!/usr/bin/env python3
"""
Backend API Test Suite for Medical Devices Textbook Production System
Tests all /api/book/* endpoints after 20-chapter rebuild
"""

import requests
import time
import sys
from typing import Dict, Any, List

# Backend URL from frontend/.env
BASE_URL = "https://happy-kowalevski-8.preview.emergentagent.com"
API_BASE = f"{BASE_URL}/api"

# Test configuration
TIMEOUT = 60  # Standard timeout
PDF_TIMEOUT = 120  # Extended timeout for PDF operations

# Color codes for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

class TestResults:
    def __init__(self):
        self.passed = []
        self.failed = []
        self.warnings = []
    
    def add_pass(self, test_name: str, details: str = ""):
        self.passed.append((test_name, details))
        print(f"{GREEN}✓{RESET} {test_name}")
        if details:
            print(f"  {details}")
    
    def add_fail(self, test_name: str, error: str):
        self.failed.append((test_name, error))
        print(f"{RED}✗{RESET} {test_name}")
        print(f"  {RED}Error: {error}{RESET}")
    
    def add_warning(self, test_name: str, warning: str):
        self.warnings.append((test_name, warning))
        print(f"{YELLOW}⚠{RESET} {test_name}")
        print(f"  {YELLOW}Warning: {warning}{RESET}")
    
    def summary(self):
        print(f"\n{'='*80}")
        print(f"{BLUE}TEST SUMMARY{RESET}")
        print(f"{'='*80}")
        print(f"{GREEN}Passed: {len(self.passed)}{RESET}")
        print(f"{RED}Failed: {len(self.failed)}{RESET}")
        print(f"{YELLOW}Warnings: {len(self.warnings)}{RESET}")
        
        if self.failed:
            print(f"\n{RED}FAILED TESTS:{RESET}")
            for test_name, error in self.failed:
                print(f"  • {test_name}")
                print(f"    {error}")
        
        return len(self.failed) == 0

results = TestResults()

def test_health_check():
    """Test 1: GET /api/ returns health check"""
    try:
        response = requests.get(f"{API_BASE}/", timeout=TIMEOUT)
        
        if response.status_code != 200:
            results.add_fail("GET /api/ health check", f"Status code {response.status_code}, expected 200")
            return False
        
        data = response.json()
        
        if "message" not in data or "status" not in data:
            results.add_fail("GET /api/ health check", f"Missing required fields. Got: {data}")
            return False
        
        if data["status"] != "ok":
            results.add_fail("GET /api/ health check", f"Status is '{data['status']}', expected 'ok'")
            return False
        
        results.add_pass("GET /api/ health check", f"Status: {data['status']}, Message: {data['message']}")
        return True
        
    except Exception as e:
        results.add_fail("GET /api/ health check", str(e))
        return False

def test_book_meta():
    """Test 2: GET /api/book/meta returns correct metadata"""
    try:
        response = requests.get(f"{API_BASE}/book/meta", timeout=TIMEOUT)
        
        if response.status_code != 200:
            results.add_fail("GET /api/book/meta", f"Status code {response.status_code}, expected 200")
            return False
        
        data = response.json()
        
        # Check chapters
        if data.get("chapters_total") != 20:
            results.add_fail("GET /api/book/meta", f"chapters_total is {data.get('chapters_total')}, expected 20")
            return False
        
        if data.get("chapters_complete") != 20:
            results.add_fail("GET /api/book/meta", f"chapters_complete is {data.get('chapters_complete')}, expected 20")
            return False
        
        # Check figures
        if data.get("figures_count") != 156:
            results.add_fail("GET /api/book/meta", f"figures_count is {data.get('figures_count')}, expected 156")
            return False
        
        # Check tables
        if data.get("tables_count") != 17:
            results.add_fail("GET /api/book/meta", f"tables_count is {data.get('tables_count')}, expected 17")
            return False
        
        # Check phases
        phases = data.get("phases", [])
        if len(phases) != 6:
            results.add_fail("GET /api/book/meta", f"phases list has {len(phases)} entries, expected 6")
            return False
        
        # Check all phases are complete
        incomplete_phases = [p for p in phases if p.get("status") != "complete"]
        if incomplete_phases:
            results.add_fail("GET /api/book/meta", f"Some phases not complete: {incomplete_phases}")
            return False
        
        # Check PDF object
        pdf = data.get("pdf")
        if not pdf:
            results.add_fail("GET /api/book/meta", "PDF object missing")
            return False
        
        details = (f"Chapters: {data['chapters_total']}/{data['chapters_complete']}, "
                  f"Figures: {data['figures_count']}, Tables: {data['tables_count']}, "
                  f"Phases: {len(phases)} all complete, PDF ready: {pdf.get('ready', False)}")
        
        results.add_pass("GET /api/book/meta", details)
        return True
        
    except Exception as e:
        results.add_fail("GET /api/book/meta", str(e))
        return False

def test_book_toc():
    """Test 3: GET /api/book/toc returns correct structure"""
    try:
        response = requests.get(f"{API_BASE}/book/toc", timeout=TIMEOUT)
        
        if response.status_code != 200:
            results.add_fail("GET /api/book/toc", f"Status code {response.status_code}, expected 200")
            return False
        
        data = response.json()
        
        # Check front_matter (8 items)
        front_matter = data.get("front_matter", [])
        if len(front_matter) != 8:
            results.add_fail("GET /api/book/toc", f"front_matter has {len(front_matter)} items, expected 8")
            return False
        
        expected_front = ["cover", "titlepage", "copyright", "preface", "howto", "syllabus", "toc", "lists"]
        front_ids = [item["id"] for item in front_matter]
        if front_ids != expected_front:
            results.add_fail("GET /api/book/toc", f"front_matter ids mismatch. Got: {front_ids}, Expected: {expected_front}")
            return False
        
        # Check parts (6 parts)
        parts = data.get("parts", [])
        if len(parts) != 6:
            results.add_fail("GET /api/book/toc", f"parts has {len(parts)} entries, expected 6")
            return False
        
        # Check part structure
        expected_parts = {
            "I": [1, 2, 3],
            "II": [4, 5, 6],
            "III": [7, 8, 9],
            "IV": [10, 11],
            "V": [12, 13, 14, 15, 16, 17],
            "VI": [18, 19, 20]
        }
        
        for part in parts:
            part_num = part.get("num")
            chapters = [ch["num"] for ch in part.get("chapters", [])]
            expected = expected_parts.get(part_num, [])
            
            if chapters != expected:
                results.add_fail("GET /api/book/toc", 
                               f"Part {part_num} chapters mismatch. Got: {chapters}, Expected: {expected}")
                return False
        
        # Check back_matter (3 items: glossary, stdindex, biblio - NO answerkeys)
        back_matter = data.get("back_matter", [])
        if len(back_matter) != 3:
            results.add_fail("GET /api/book/toc", f"back_matter has {len(back_matter)} items, expected 3")
            return False
        
        expected_back = ["glossary", "stdindex", "biblio"]
        back_ids = [item["id"] for item in back_matter]
        if back_ids != expected_back:
            results.add_fail("GET /api/book/toc", f"back_matter ids mismatch. Got: {back_ids}, Expected: {expected_back}")
            return False
        
        # Check that answerkeys is NOT present
        if "answerkeys" in back_ids:
            results.add_fail("GET /api/book/toc", "answerkeys found in back_matter but should be removed")
            return False
        
        details = (f"Front matter: {len(front_matter)} items, "
                  f"Parts: {len(parts)} (I-VI with correct chapter distribution), "
                  f"Back matter: {len(back_matter)} items (glossary, stdindex, biblio - answerkeys removed)")
        
        results.add_pass("GET /api/book/toc", details)
        return True
        
    except Exception as e:
        results.add_fail("GET /api/book/toc", str(e))
        return False

def test_preview_sections():
    """Test 4: GET /api/book/preview/{section_id} for all sections"""
    
    # All sections to test
    sections_to_test = [
        # Front matter
        "cover", "halftitle", "titlepage", "copyright", "preface", "howto", "syllabus", "toc", "lists",
        # Parts
        "partI", "partII", "partIII", "partIV", "partV", "partVI",
        # Chapters
        *[f"ch{i:02d}" for i in range(1, 21)],
        # Back matter
        "glossary", "stdindex", "biblio"
    ]
    
    all_passed = True
    
    for section_id in sections_to_test:
        try:
            response = requests.get(f"{API_BASE}/book/preview/{section_id}", timeout=TIMEOUT)
            
            if response.status_code != 200:
                results.add_fail(f"GET /api/book/preview/{section_id}", 
                               f"Status code {response.status_code}, expected 200")
                all_passed = False
                continue
            
            html = response.text
            
            # Basic HTML validation
            if not html or len(html) < 100:
                results.add_fail(f"GET /api/book/preview/{section_id}", 
                               f"HTML too short ({len(html)} chars)")
                all_passed = False
                continue
            
            # Chapter-specific validation
            if section_id.startswith("ch"):
                # Check for required elements in chapter HTML
                required_elements = ["ch-title", "objectives-box"]
                missing = [elem for elem in required_elements if elem not in html]
                
                if missing:
                    results.add_fail(f"GET /api/book/preview/{section_id}", 
                                   f"Missing required elements: {missing}")
                    all_passed = False
                    continue
                
                # Special check for ch01 - should have an image
                if section_id == "ch01":
                    if 'images/ch01_fig01.jpg' not in html:
                        results.add_fail(f"GET /api/book/preview/{section_id}", 
                                       "ch01 should contain image reference to images/ch01_fig01.jpg")
                        all_passed = False
                        continue
            
        except Exception as e:
            results.add_fail(f"GET /api/book/preview/{section_id}", str(e))
            all_passed = False
            continue
    
    if all_passed:
        results.add_pass("GET /api/book/preview/{section_id} for all sections", 
                        f"All {len(sections_to_test)} sections returned valid HTML")
    
    # Test 404 for unknown section
    try:
        response = requests.get(f"{API_BASE}/book/preview/ch99", timeout=TIMEOUT)
        if response.status_code != 404:
            results.add_fail("GET /api/book/preview/ch99 (unknown)", 
                           f"Status code {response.status_code}, expected 404")
            all_passed = False
        else:
            results.add_pass("GET /api/book/preview/ch99 (unknown)", "Correctly returns 404")
    except Exception as e:
        results.add_fail("GET /api/book/preview/ch99 (unknown)", str(e))
        all_passed = False
    
    return all_passed

def test_preview_images():
    """Test 5: GET /api/book/preview/images/* serves images"""
    
    # Test specific images
    test_images = [
        "ch01_fig01.jpg",
        "ch13_fig05.jpg",
        "ch20_fig01.jpg"
    ]
    
    all_passed = True
    
    for image_name in test_images:
        try:
            response = requests.get(f"{API_BASE}/book/preview/images/{image_name}", timeout=TIMEOUT)
            
            if response.status_code != 200:
                results.add_fail(f"GET /api/book/preview/images/{image_name}", 
                               f"Status code {response.status_code}, expected 200")
                all_passed = False
                continue
            
            # Check content type
            content_type = response.headers.get("content-type", "")
            if "image/jpeg" not in content_type and "image/jpg" not in content_type:
                results.add_fail(f"GET /api/book/preview/images/{image_name}", 
                               f"Content-Type is '{content_type}', expected image/jpeg")
                all_passed = False
                continue
            
            # Check content size
            content_length = len(response.content)
            if content_length < 1000:  # Images should be at least 1KB
                results.add_fail(f"GET /api/book/preview/images/{image_name}", 
                               f"Image too small ({content_length} bytes)")
                all_passed = False
                continue
            
        except Exception as e:
            results.add_fail(f"GET /api/book/preview/images/{image_name}", str(e))
            all_passed = False
            continue
    
    if all_passed:
        results.add_pass("GET /api/book/preview/images/*", 
                        f"All {len(test_images)} test images served correctly with image/jpeg content-type")
    
    return all_passed

def test_pdf_status():
    """Test 6: GET /api/book/pdf/status"""
    try:
        # Poll for up to 120 seconds if building
        max_wait = 120
        start_time = time.time()
        
        while True:
            response = requests.get(f"{API_BASE}/book/pdf/status", timeout=TIMEOUT)
            
            if response.status_code != 200:
                results.add_fail("GET /api/book/pdf/status", f"Status code {response.status_code}, expected 200")
                return False
            
            data = response.json()
            
            # Check if ready
            if data.get("ready") is True:
                # Validate pages
                pages = data.get("pages", 0)
                if pages < 700:
                    results.add_fail("GET /api/book/pdf/status", 
                                   f"pages is {pages}, expected >700 (target ~754)")
                    return False
                
                # Validate size
                size_bytes = data.get("size_bytes", 0)
                if size_bytes < 3 * 1024 * 1024:  # 3MB
                    results.add_fail("GET /api/book/pdf/status", 
                                   f"size_bytes is {size_bytes}, expected >3MB")
                    return False
                
                # Check error is null
                if data.get("error") is not None:
                    results.add_fail("GET /api/book/pdf/status", 
                                   f"error field is not null: {data.get('error')}")
                    return False
                
                size_mb = size_bytes / (1024 * 1024)
                details = f"Ready: true, Pages: {pages}, Size: {size_mb:.2f}MB, Error: null"
                results.add_pass("GET /api/book/pdf/status", details)
                return True
            
            # Check if building
            if data.get("building") is True:
                elapsed = time.time() - start_time
                if elapsed > max_wait:
                    results.add_fail("GET /api/book/pdf/status", 
                                   f"PDF still building after {max_wait}s timeout")
                    return False
                
                print(f"  PDF building... waiting ({elapsed:.0f}s elapsed)")
                time.sleep(5)
                continue
            
            # Neither ready nor building - unexpected state
            results.add_fail("GET /api/book/pdf/status", 
                           f"Unexpected state: ready={data.get('ready')}, building={data.get('building')}")
            return False
        
    except Exception as e:
        results.add_fail("GET /api/book/pdf/status", str(e))
        return False

def test_pdf_download():
    """Test 7: GET /api/book/pdf downloads PDF"""
    try:
        print(f"  Downloading PDF (may take up to 60s)...")
        response = requests.get(f"{API_BASE}/book/pdf", timeout=PDF_TIMEOUT)
        
        if response.status_code != 200:
            results.add_fail("GET /api/book/pdf", f"Status code {response.status_code}, expected 200")
            return False
        
        # Check content type
        content_type = response.headers.get("content-type", "")
        if "application/pdf" not in content_type:
            results.add_fail("GET /api/book/pdf", 
                           f"Content-Type is '{content_type}', expected application/pdf")
            return False
        
        # Check X-Page-Count header
        page_count = response.headers.get("X-Page-Count")
        if not page_count:
            results.add_fail("GET /api/book/pdf", "Missing X-Page-Count header")
            return False
        
        page_count = int(page_count)
        if page_count < 700:
            results.add_fail("GET /api/book/pdf", 
                           f"X-Page-Count is {page_count}, expected ~754 (>700)")
            return False
        
        # Check content size
        content_length = len(response.content)
        size_mb = content_length / (1024 * 1024)
        
        if content_length < 3 * 1024 * 1024:  # 3MB
            results.add_fail("GET /api/book/pdf", 
                           f"PDF size is {size_mb:.2f}MB, expected >3MB")
            return False
        
        # Check PDF magic bytes
        if not response.content.startswith(b'%PDF'):
            results.add_fail("GET /api/book/pdf", 
                           "Content does not start with %PDF magic bytes")
            return False
        
        details = f"Content-Type: application/pdf, Pages: {page_count}, Size: {size_mb:.2f}MB, Valid PDF format"
        results.add_pass("GET /api/book/pdf", details)
        return True
        
    except Exception as e:
        results.add_fail("GET /api/book/pdf", str(e))
        return False

def main():
    print(f"\n{'='*80}")
    print(f"{BLUE}Medical Devices Textbook Backend API Test Suite{RESET}")
    print(f"Testing: {API_BASE}")
    print(f"{'='*80}\n")
    
    # Run all tests
    test_health_check()
    test_book_meta()
    test_book_toc()
    test_preview_sections()
    test_preview_images()
    test_pdf_status()
    test_pdf_download()
    
    # Print summary
    success = results.summary()
    
    print(f"\n{'='*80}\n")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
