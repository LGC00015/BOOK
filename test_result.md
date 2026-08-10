#====================================================================================================
# START - Testing Protocol - DO NOT EDIT OR REMOVE THIS SECTION
#====================================================================================================

# THIS SECTION CONTAINS CRITICAL TESTING INSTRUCTIONS FOR BOTH AGENTS
# BOTH MAIN_AGENT AND TESTING_AGENT MUST PRESERVE THIS ENTIRE BLOCK

# Communication Protocol:
# If the `testing_agent` is available, main agent should delegate all testing tasks to it.
#
# You have access to a file called `test_result.md`. This file contains the complete testing state
# and history, and is the primary means of communication between main and the testing agent.
#
# Main and testing agents must follow this exact format to maintain testing data. 
# The testing data must be entered in yaml format Below is the data structure:
# 
## user_problem_statement: {problem_statement}
## backend:
##   - task: "Task name"
##     implemented: true
##     working: true  # or false or "NA"
##     file: "file_path.py"
##     stuck_count: 0
##     priority: "high"  # or "medium" or "low"
##     needs_retesting: false
##     status_history:
##         -working: true  # or false or "NA"
##         -agent: "main"  # or "testing" or "user"
##         -comment: "Detailed comment about status"
##
## frontend:
##   - task: "Task name"
##     implemented: true
##     working: true  # or false or "NA"
##     file: "file_path.js"
##     stuck_count: 0
##     priority: "high"  # or "medium" or "low"
##     needs_retesting: false
##     status_history:
##         -working: true  # or false or "NA"
##         -agent: "main"  # or "testing" or "user"
##         -comment: "Detailed comment about status"
##
## metadata:
##   created_by: "main_agent"
##   version: "1.0"
##   test_sequence: 0
##   run_ui: false
##
## test_plan:
##   current_focus:
##     - "Task name 1"
##     - "Task name 2"
##   stuck_tasks:
##     - "Task name with persistent issues"
##   test_all: false
##   test_priority: "high_first"  # or "sequential" or "stuck_first"
##
## agent_communication:
##     -agent: "main"  # or "testing" or "user"
##     -message: "Communication message between agents"

# Protocol Guidelines for Main agent
#
# 1. Update Test Result File Before Testing:
#    - Main agent must always update the `test_result.md` file before calling the testing agent
#    - Add implementation details to the status_history
#    - Set `needs_retesting` to true for tasks that need testing
#    - Update the `test_plan` section to guide testing priorities
#    - Add a message to `agent_communication` explaining what you've done
#
# 2. Incorporate User Feedback:
#    - When a user provides feedback that something is or isn't working, add this information to the relevant task's status_history
#    - Update the working status based on user feedback
#    - If a user reports an issue with a task that was marked as working, increment the stuck_count
#    - Whenever user reports issue in the app, if we have testing agent and task_result.md file so find the appropriate task for that and append in status_history of that task to contain the user concern and problem as well 
#
# 3. Track Stuck Tasks:
#    - Monitor which tasks have high stuck_count values or where you are fixing same issue again and again, analyze that when you read task_result.md
#    - For persistent issues, use websearch tool to find solutions
#    - Pay special attention to tasks in the stuck_tasks list
#    - When you fix an issue with a stuck task, don't reset the stuck_count until the testing agent confirms it's working
#
# 4. Provide Context to Testing Agent:
#    - When calling the testing agent, provide clear instructions about:
#      - Which tasks need testing (reference the test_plan)
#      - Any authentication details or configuration needed
#      - Specific test scenarios to focus on
#      - Any known issues or edge cases to verify
#
# 5. Call the testing agent with specific instructions referring to test_result.md
#
# IMPORTANT: Main agent must ALWAYS update test_result.md BEFORE calling the testing agent, as it relies on this file to understand what to test next.

#====================================================================================================
# END - Testing Protocol - DO NOT EDIT OR REMOVE THIS SECTION
#====================================================================================================



#====================================================================================================
# Testing Data - Main Agent and testing sub agent both should log testing data below this section
#====================================================================================================
user_problem_statement: >
  Continuation: user shared their complete 20-chapter Medical Devices book manuscript (.docx with
  156 embedded figures, tables, per-chapter CLOs/keywords/roadmap/case studies/industry insights/
  glossary/quick recap/references). Task: build the WHOLE book from their manuscript, replacing the
  earlier 14-chapter agent-drafted outline, keeping the professional A4 print design system and
  production dashboard. All phases complete: extraction pipeline (scripts/extract_docx.py ->
  backend/book/content/chNN.json + images/), renderer (book/docx_chapters.py), new outline
  (6 parts / 20 chapters), regenerated front matter (TOC, lists of 156 figures & 17 tables) and
  back matter (consolidated glossary ~300 terms, standards index, chapter-by-chapter references).
  PDF: 754 A4 pages, ~5.1MB, ~36s build, pre-warmed at startup. .env files were missing in this
  fork and were recreated (frontend REACT_APP_BACKEND_URL, backend MONGO_URL placeholders).

backend:
  - task: "GET /api/book/meta returns 20/20 chapters, 156 figures, 17 tables, 6 phases complete, pdf status"
    implemented: true
    working: true
    file: "backend/server.py"
    stuck_count: 0
    priority: "high"
    needs_retesting: false
    status_history:
      - working: "NA"
        agent: "main"
        comment: "Rewired to manifest-driven outline (20 chapters, 6 parts)."
      - working: true
        agent: "testing"
        comment: "✓ PASSED - Returns correct metadata: chapters_total=20, chapters_complete=20, figures_count=156, tables_count=17, phases list has 6 entries all with status='complete', pdf object present with ready=true."
  - task: "GET /api/book/toc returns 6 parts with 20 chapters + front matter (8 items) + back matter (glossary, stdindex, biblio - answerkeys removed)"
    implemented: true
    working: true
    file: "backend/server.py"
    stuck_count: 0
    priority: "high"
    needs_retesting: false
    status_history:
      - working: "NA"
        agent: "main"
        comment: "Parts: I(1-3) II(4-6) III(7-9) IV(10-11) V(12-17) VI(18-20)."
      - working: true
        agent: "testing"
        comment: "✓ PASSED - Correct structure verified: front_matter has 8 items (cover, titlepage, copyright, preface, howto, syllabus, toc, lists), parts has 6 entries with correct chapter distribution (I=[1,2,3], II=[4,5,6], III=[7,8,9], IV=[10,11], V=[12,13,14,15,16,17], VI=[18,19,20]), back_matter has exactly 3 items (glossary, stdindex, biblio) - answerkeys correctly removed."
  - task: "GET /api/book/preview/{section_id} serves HTML for all sections incl. ch01..ch20, cover, toc, glossary, biblio; 404 for unknown"
    implemented: true
    working: true
    file: "backend/book/assembler.py"
    stuck_count: 0
    priority: "high"
    needs_retesting: false
    status_history:
      - working: "NA"
        agent: "main"
        comment: "Chapters rendered from content JSON via book/docx_chapters.py."
      - working: true
        agent: "testing"
        comment: "✓ PASSED - All 38 sections tested (9 front matter, 6 parts, 20 chapters, 3 back matter) return 200 with valid HTML. Chapter HTML contains required elements ('ch-title', 'objectives-box'). ch01 specifically contains image reference to 'images/ch01_fig01.jpg'. Unknown section 'ch99' correctly returns 404."
  - task: "GET /api/book/preview/images/* serves figure JPEGs (static mount)"
    implemented: true
    working: true
    file: "backend/server.py"
    stuck_count: 0
    priority: "high"
    needs_retesting: false
    status_history:
      - working: "NA"
        agent: "main"
        comment: "New static mount for 156 extracted images."
      - working: true
        agent: "testing"
        comment: "✓ PASSED - Image serving verified for ch01_fig01.jpg, ch13_fig05.jpg, and ch20_fig01.jpg. All return 200 with correct content-type (image/jpeg) and valid image data."
  - task: "GET /api/book/pdf/status and GET /api/book/pdf (754 pages, ~5.1MB, X-Page-Count header)"
    implemented: true
    working: true
    file: "backend/book/assembler.py"
    stuck_count: 0
    priority: "high"
    needs_retesting: false
    status_history:
      - working: "NA"
        agent: "main"
        comment: "Warm build at startup ~36s; verify status transitions and PDF download."
      - working: true
        agent: "testing"
        comment: "✓ PASSED - GET /api/book/pdf/status returns ready=true, pages=754, size_bytes=5,181,440 (4.94MB), error=null. GET /api/book/pdf returns 200 with content-type=application/pdf, X-Page-Count header=754, body size 4.94MB, starts with %PDF magic bytes. PDF generation working correctly."

frontend:
  - task: "Dashboard shows 754 pages, 20/20 chapters, TOC with 6 parts, live preview iframes, PDF download"
    implemented: true
    working: "NA"
    file: "frontend/src/App.js"
    stuck_count: 0
    priority: "high"
    needs_retesting: false
    status_history:
      - working: "NA"
        agent: "main"
        comment: "Verified visually via screenshots; do not auto-test without user permission."

metadata:
  created_by: "main_agent"
  version: "2.0"
  test_sequence: 2
  run_ui: false

test_plan:
  current_focus:
    - "All backend book endpoints after 20-chapter rebuild"
  stuck_tasks: []
  test_all: false
  test_priority: "high_first"

agent_communication:
  - agent: "main"
    message: >
      Rebuilt entire book from user's 20-chapter docx manuscript. Backend endpoints unchanged in
      shape but data fully regenerated; answerkeys section removed from toc/back matter; new
      images static mount. PDF pre-warms at startup (~36s). Please test all /api/book/* endpoints.
      Frontend NOT to be tested (user permission pending).
  - agent: "testing"
    message: >
      ✓ ALL BACKEND TESTS PASSED (8/8) - Comprehensive testing completed for all /api/book/* endpoints.
      Health check working. Book metadata correct (20/20 chapters, 156 figures, 17 tables, 6 phases complete).
      TOC structure verified (6 parts with correct chapter distribution, 8 front matter items, 3 back matter items
      with answerkeys removed). All 38 preview sections return valid HTML with required elements. Image serving
      working for all tested figures. PDF status and download working correctly (754 pages, 4.94MB, valid PDF format).
      No issues found. Backend is production-ready.
