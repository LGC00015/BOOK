"""QA corrections layer — Final Regulatory & Editorial QA (controlled revision).

Minimum-necessary text corrections applied to the extracted chapter JSONs.
Master Prompt v5.4 architecture untouched: no chapters, sections, figures or
pedagogy are altered — only the exact statements listed in the QA report.

Each entry: (find, replace). Applied as plain-text substitution on the JSON
files (content is stored ensure_ascii=False, so strings match verbatim).
"""

QMSR_REF = "Quality Management System Regulation (QMSR; formerly Quality System Regulation)"

CORRECTIONS = {
    "ch01": [
        # C-1 global: QSR -> QMSR (FDA QMSR effective 2 Feb 2026)
        ("Good Manufacturing Practices (GMP) / Quality System Regulation (QSR)",
         "Good Manufacturing Practices (GMP) / Quality Management System Regulation (QMSR)"),
        # M-11: time-sensitive market statistic made date-explicit
        ("used in India are currently imported",
         "used in India are imported (industry estimates, c. 2024)"),
    ],
    "ch02": [
        ("<strong>FDA 21 CFR 820 </strong>– Quality System Regulation (USA)",
         "<strong>FDA 21 CFR Part 820 </strong>– Quality Management System Regulation (QMSR, USA)"),
        ("FDA 21 CFR Part 820 – Quality System Regulation U.S. Food and Drug Administration",
         "FDA 21 CFR Part 820 – " + QMSR_REF + ". U.S. Food and Drug Administration"),
        ("<strong>Projected Growth (2030): </strong>USD 50 billion",
         "<strong>Projected market size (2030; industry estimate, c. 2024): </strong>approximately USD 50 billion"),
        ("is projected to reach <strong>USD 50 billion by 2030</strong>",
         "is projected in industry estimates (c. 2024) to reach <strong>approximately USD 50 billion by 2030</strong>"),
        ("Market expansion to USD 50 billion by 2030",
         "Market expansion projected toward USD 50 billion by 2030 (industry estimate, c. 2024)"),
    ],
    "ch03": [
        ("Compliance with Quality System Regulation (QSR)",
         "Compliance with the Quality Management System Regulation (QMSR)"),
        ("QSR compliance and FDA inspections", "QMSR compliance and FDA inspections"),
        ("\"QSR compliance\"", "\"QMSR compliance\""),
        # M-3: absolute 510(k) claims qualified
        ("FDA: Class II (510(k) required)",
         "FDA: Class II (typically subject to 510(k); some device types are exempt)"),
        ("Class II (Special controls for accuracy; 510(k) required)",
         "Class II (Special controls for accuracy; typically subject to 510(k))"),
        ("Class II (510(k) required with comprehensive testing)",
         "Class II (510(k) typically required, with comprehensive testing)"),
        ("projected to reach <strong>USD 50 billion by 2030</strong>",
         "projected in industry estimates (c. 2024) to reach <strong>approximately USD 50 billion by 2030</strong>"),
    ],
    "ch04": [
        ("<strong>FDA 21 CFR 820 </strong>– Quality System Regulation (Design Controls)",
         "<strong>FDA 21 CFR Part 820 </strong>– Quality Management System Regulation (QMSR; design controls)"),
        ("FDA 21 CFR Part 820 – Quality System Regulation U.S. Food and Drug Administration",
         "FDA 21 CFR Part 820 – " + QMSR_REF + ". U.S. Food and Drug Administration"),
    ],
    "ch05": [
        ("(Quality System Regulation - QSR in the United States)",
         "(Quality Management System Regulation — QMSR, United States; incorporates ISO 13485:2016 by reference, effective 2 February 2026)"),
        ("FDA 21 CFR Part 820 — Quality System Regulation (United States)",
         "FDA 21 CFR Part 820 — Quality Management System Regulation (QMSR, United States)"),
        ("FDA Guidance — Quality System Regulation; Medical Device Reporting",
         "FDA Guidance — Quality Management System Regulation (QMSR); Medical Device Reporting"),
    ],
    "ch06": [
        ("<strong>FDA 21 CFR 820 </strong>(Quality System Regulation)",
         "<strong>FDA 21 CFR Part 820 </strong>(Quality Management System Regulation, QMSR)"),
        # M-5: 25 kGy universality qualified (ISO 11137)
        ("<strong>Typical Dose</strong>: 25 kGy (minimum sterilization dose)",
         "<strong>Typical dose</strong>: 25 kGy is a commonly referenced example; the minimum sterilization dose must be established and validated for the specific product per ISO 11137"),
        ("<strong>Yes </strong>→ Use Gamma Radiation (25 kGy)",
         "<strong>Yes </strong>→ Use gamma radiation (commonly 25 kGy; dose validated per ISO 11137)"),
        # M-6: ETO parameters marked as typical, standard-dependent
        ("ETO concentration: 450-1200 mg/L",
         "ETO concentration: typically 450–1200 mg/L (illustrative; validated cycle-specific per ISO 11135)"),
    ],
    "ch07": [
        ("<strong>Dose</strong>: Typically 25 kGy",
         "<strong>Dose</strong>: commonly 25 kGy; the product-specific dose is established per ISO 11137"),
    ],
    "ch09": [
        ("compliance with FDA QSR and ISO 13485 requirements",
         "compliance with the FDA QMSR and ISO 13485 requirements"),
        ("FDA 21 CFR 820 (Quality System Regulation) mandate",
         "FDA 21 CFR Part 820 (Quality Management System Regulation, QMSR) mandate"),
        ("21 CFR Part 820 — Quality System Regulation.",
         "21 CFR Part 820 — " + QMSR_REF + "."),
    ],
    "ch10": [
        ("<strong>FDA 21 CFR Part 820 </strong>– Quality System Regulation (United States)",
         "<strong>FDA 21 CFR Part 820 </strong>– Quality Management System Regulation (QMSR, United States)"),
        ("FDA 21 CFR Part 820 – Quality System Regulation (United States)",
         "FDA 21 CFR Part 820 – Quality Management System Regulation (QMSR, United States)"),
        ("Gas concentration: 450–1200 mg/L",
         "Gas concentration: typically 450–1200 mg/L (illustrative; validated cycle-specific per ISO 11135)"),
    ],
    "ch11": [
        ("<strong>FDA 21 CFR 820 </strong>(Quality System Regulation)",
         "<strong>FDA 21 CFR Part 820 </strong>(Quality Management System Regulation, QMSR)"),
        ("FDA 21 CFR Part 820 — Quality System Regulation",
         "FDA 21 CFR Part 820 — Quality Management System Regulation (QMSR)"),
        ("25 kGy Standard dose for SAL",
         "25 kGy — commonly referenced dose; substantiated per ISO 11137 for the required SAL"),
        ("Typical result: 25 kGy minimum dose",
         "Typical result: e.g., 25 kGy minimum dose (product- and bioburden-specific)"),
        ("<strong>Standard dose: </strong>25 kGy (most common for overkill method)",
         "<strong>Commonly referenced dose: </strong>25 kGy (VDmax/overkill substantiation per ISO 11137-2)"),
    ],
    "ch12": [
        ("(ISO 13485, QSR)", "(ISO 13485, QMSR)"),
        ("Comply with Quality System Regulation (QSR)",
         "Comply with the Quality Management System Regulation (QMSR)"),
        ("Quality System Regulation (QSR) — 21 CFR Part 820",
         "Quality Management System Regulation (QMSR) — 21 CFR Part 820"),
        ("The QSR establishes comprehensive quality management requirements",
         "The QMSR establishes comprehensive quality management requirements"),
        # C-2: transition note corrected — QMSR is in effect since 2 Feb 2026
        ("<strong>Note: </strong>FDA is transitioning from QSR to <strong>Quality Management System Regulation (QMSR)</strong>",
         "<strong>Note: </strong>With effect from 2 February 2026, FDA replaced the former Quality System Regulation (QSR) with the <strong>Quality Management System Regulation (QMSR)</strong>"),
        ("aligned with ISO 13485:2016, improving harmonization",
         "The QMSR incorporates ISO 13485:2016 by reference, improving global harmonization"),
        ("<strong>USA </strong>21 CFR Part 820 (QSR)",
         "<strong>USA </strong>21 CFR Part 820 (QMSR)"),
        ("\"Quality System Regulation\"", "\"Quality Management System Regulation (QMSR)\""),
        ("Design controls mandatory; transitioning to QMSR",
         "Design controls mandatory; QMSR (ISO 13485-aligned) effective 2 February 2026"),
        ("QSR (Quality System Regulation)", "QMSR (Quality Management System Regulation)"),
        ("FDA regulation (21 CFR 820) establishing quality system requirements",
         "FDA quality system regulation (21 CFR Part 820); with effect from 2 February 2026 it incorporates ISO 13485:2016 by reference, replacing the former Quality System Regulation (QSR)"),
    ],
    "ch13": [
        ("Requires 510(k) premarket notification",
         "Usually requires 510(k) premarket notification (some device types are exempt)"),
    ],
    "ch15": [
        ("<strong>FDA 21 CFR 820 </strong>(Quality System Regulation)",
         "<strong>FDA 21 CFR Part 820 </strong>(Quality Management System Regulation, QMSR)"),
    ],
    "ch16": [
        ("<strong>FDA 21 CFR 820 </strong>– Quality System Regulation (packaging controls)",
         "<strong>FDA 21 CFR Part 820 </strong>– Quality Management System Regulation (QMSR; packaging controls)"),
        ("21 CFR Part 820 – Quality System Regulation (US FDA)",
         "21 CFR Part 820 – Quality Management System Regulation (QMSR, US FDA)"),
    ],
    "ch20": [
        ("projected to reach <strong>USD 50 billion by 2030</strong>",
         "projected in industry estimates (c. 2024) to reach <strong>approximately USD 50 billion by 2030</strong>"),
    ],
}
