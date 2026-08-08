def glossary_html():
    terms = [
        ("Accessory", "An article intended by its manufacturer to be used together with a medical device to enable or assist that device to be used in accordance with its intended purpose."),
        ("Adverse event", "Any untoward medical occurrence, unintended disease or injury, or untoward clinical signs in patients, users or other persons, whether or not related to the medical device."),
        ("Biocompatibility", "The ability of a material to perform with an appropriate host response in a specific application."),
        ("CE marking", "The marking by which a manufacturer indicates that a device conforms with the applicable requirements of EU regulations, permitting free movement within the European market."),
        ("Central Licensing Authority (CLA)", "Under MDR 2017, the Drugs Controller General of India, responsible for licensing Class C and D manufacturing, all imports, and clinical investigations."),
        ("Class A–D (India)", "The four risk classes of CDSCO MDR 2017: A (low), B (low-moderate), C (moderate-high), D (high risk)."),
        ("Classification rules", "The rule set (e.g., First Schedule of MDR 2017; Annex VIII of EU MDR) that assigns a device to a risk class based on duration, invasiveness, and body system affected."),
        ("Conformity assessment", "The systematic examination of evidence and procedures demonstrating that a device meets regulatory requirements."),
        ("De Novo pathway", "A US FDA pathway providing risk-based classification of novel low-to-moderate risk devices without a valid predicate."),
        ("General controls", "Baseline US FDA requirements applying to all device classes: establishment registration, device listing, labeling, GMP/QSR and misbranding/adulteration provisions."),
        ("GHTF", "Global Harmonization Task Force (1992–2011); a voluntary regulators–industry group whose guidance documents seeded modern device regulation; succeeded by IMDRF."),
        ("IMDRF", "International Medical Device Regulators Forum (est. 2011); a regulators-only forum accelerating international medical device regulatory harmonization."),
        ("Intended use / intended purpose", "The objective use of a device according to the manufacturer's labeling, instructions and promotional materials; the anchor of classification and conformity decisions."),
        ("In vitro diagnostic (IVD)", "A device, reagent, instrument or system intended for the in vitro examination of specimens derived from the human body to provide diagnostic, monitoring or compatibility information."),
        ("Materiovigilance", "The coordinated monitoring, collection, and analysis of medical device-associated adverse events to protect patient safety; in India operationalized as MvPI (launched 6 July 2015, coordinated by IPC Ghaziabad)."),
        ("Medical Device Amendments 1976", "The US law that created the three-class, risk-based device framework within the FD&C Act following the Dalkon Shield injuries."),
        ("MDR 2017 (India)", "The Medical Devices Rules, 2017 (G.S.R. 78(E), 31 January 2017), effective 1 January 2018, made under the Drugs and Cosmetics Act, 1940."),
        ("EU MDR", "Regulation (EU) 2017/745 on medical devices, fully applicable from 26 May 2021, replacing Directives 93/42/EEC and 90/385/EEC."),
        ("Notified body", "An organization designated by an EU member state to assess the conformity of medium and higher-risk devices before CE marking."),
        ("Notified device", "Historically in India, one of the limited device categories regulated as 'drugs' by notification before the comprehensive MDR 2017 regime."),
        ("Predicate device", "A legally marketed US device to which substantial equivalence is claimed in a 510(k) submission."),
        ("Premarket approval (PMA)", "The most stringent US FDA marketing pathway, requiring valid scientific evidence — typically clinical data — of safety and effectiveness for Class III devices."),
        ("Post-market surveillance (PMS)", "Systematic activities by manufacturers and regulators to collect and act on experience from devices on the market."),
        ("Risk-based classification", "The universal principle that regulatory scrutiny should be proportionate to the potential of a device to harm patients or users."),
        ("SaMD", "Software as a Medical Device — software intended for medical purposes that performs these purposes without being part of a hardware medical device (IMDRF definition)."),
        ("Substantial equivalence", "The 510(k) finding that a new device is as safe and effective as a predicate: same intended use and same technological characteristics (or different ones that raise no new safety questions)."),
        ("State Licensing Authority (SLA)", "Under MDR 2017, the state-level authority responsible for licensing manufacture for sale of Class A and B devices and retail matters."),
        ("Unique Device Identification (UDI)", "A system of globally unambiguous device identifiers enabling traceability across distribution and use."),
    ]
    dl = "".join("<dt>%s.</dt> <dd>%s</dd><br/>" % (t, d) for t, d in terms)
    return """
<section class="backmatter-section glossary" id="glossary" data-running="Glossary">
  <h1 class="fm-title">Glossary of Key Terms</h1>
  <p style="color:#5B6770;font-size:9pt;">Consolidated from Chapters 1&ndash;2. The glossary grows with each production phase.</p>
  <dl>%s</dl>
</section>""" % dl


def standards_index_html():
    rows = [
        ("Drugs and Cosmetics Act, 1940", "India", "Parent statute under which medical devices are regulated as 'drugs'", "Ch 1, 2"),
        ("Medical Devices Rules, 2017 — G.S.R. 78(E)", "India", "Comprehensive risk-based device rules; Class A–D; effective 1 Jan 2018", "Ch 1, 2"),
        ("Medical Devices (Amendment) Rules, 2020", "India", "Extended MDR 2017 to all devices via mandatory registration", "Ch 2"),
        ("National Medical Device Policy, 2023", "India", "Six-strategy sector policy; $50 bn sector ambition by 2030", "Ch 1"),
        ("Federal Food, Drug, and Cosmetic Act (1938), as amended", "USA", "Statutory basis of FDA device authority; §201(h) device definition", "Ch 2"),
        ("Medical Device Amendments, 1976", "USA", "Created Class I–III risk framework", "Ch 1, 2"),
        ("21 CFR Parts 800–898", "USA", "FDA device regulations incl. classification panels", "Ch 2"),
        ("Regulation (EU) 2017/745 (EU MDR)", "EU", "Device regulation; Classes I, IIa, IIb, III; CE marking", "Ch 2"),
        ("Directive 93/42/EEC (MDD) — repealed", "EU", "Predecessor directive replaced by EU MDR", "Ch 2"),
        ("ISO 13485:2016", "International", "QMS requirements for medical devices", "Ch 2 (preview); Ch 7"),
        ("ISO 14971:2019", "International", "Application of risk management to medical devices", "Ch 2 (preview); Ch 8"),
        ("ISO 10993 series", "International", "Biological evaluation of medical devices", "Ch 5 (planned)"),
        ("IEC 60601 series", "International", "Basic safety & essential performance of medical electrical equipment", "Ch 9 (planned)"),
        ("IMDRF/SaMD WG/N10:2013", "IMDRF", "SaMD: key definitions", "Ch 2"),
        ("WHO Global Model Regulatory Framework (2017)", "WHO", "Model framework for medical device regulation incl. IVDs", "Ch 1, 2"),
    ]
    trs = "".join("<tr><td class='rowhead'>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % r for r in rows)
    return """
<section class="backmatter-section" id="stdindex" data-running="Standards &amp; Regulations Index">
  <h1 class="fm-title">Standards &amp; Regulations Index</h1>
  <div class="tablewrap"><table class="data">
    <tr><th>Instrument</th><th style="width:22mm;">Jurisdiction</th><th>Scope in this book</th><th style="width:20mm;">Chapters</th></tr>
    %s
  </table></div>
  <p style="color:#5B6770;font-size:8.6pt;">Verified against official CDSCO, US FDA, EUR-Lex, ISO, IEC and WHO sources. No qualification pack or occupational standard codes are cited in this edition; NSQF/LSSSDC touchpoints in Chapter 14 will reference only verifiable frameworks.</p>
</section>""" % trs


def answer_keys_html():
    return """
<section class="backmatter-section akey" id="answerkeys" data-running="Answer Keys">
  <h1 class="fm-title">Answer Keys</h1>

  <h3>Chapter 1 — Introduction to Medical Devices</h3>
  <p><strong>MCQs:</strong> 1-b&nbsp; 2-c&nbsp; 3-b&nbsp; 4-d&nbsp; 5-b&nbsp; 6-c&nbsp; 7-a&nbsp; 8-c&nbsp; 9-b&nbsp; 10-d</p>
  <p><strong>True/False:</strong> 1-T&nbsp; 2-F&nbsp; 3-T&nbsp; 4-F&nbsp; 5-T&nbsp; 6-F&nbsp; 7-T&nbsp; 8-F&nbsp; 9-T&nbsp; 10-T</p>
  <p><strong>Fill in the Blanks:</strong> 1. Ren&eacute; Laennec&nbsp; 2. Wilhelm Conrad R&ouml;ntgen&nbsp; 3. 1 January 2018&nbsp; 4. sunrise&nbsp; 5. 70&ndash;80%&nbsp; 6. Production Linked Incentive (PLI)&nbsp; 7. 2023&nbsp; 8. Andhra Pradesh (AMTZ, Visakhapatnam)&nbsp; 9. diagnostics/imaging equipment&nbsp; 10. Drugs and Cosmetics Act, 1940</p>
  <p><strong>Assertion–Reasoning:</strong> 1-a&nbsp; 2-a&nbsp; 3-d&nbsp; 4-b&nbsp; 5-a</p>

  <h3>Chapter 2 — Definitions &amp; Classification</h3>
  <p><strong>MCQs:</strong> 1-c&nbsp; 2-b&nbsp; 3-d&nbsp; 4-b&nbsp; 5-c&nbsp; 6-a&nbsp; 7-c&nbsp; 8-b&nbsp; 9-d&nbsp; 10-b</p>
  <p><strong>True/False:</strong> 1-F&nbsp; 2-T&nbsp; 3-T&nbsp; 4-F&nbsp; 5-T&nbsp; 6-F&nbsp; 7-F&nbsp; 8-T&nbsp; 9-T&nbsp; 10-F</p>
  <p><strong>Fill in the Blanks:</strong> 1. pharmacological, immunological, metabolic&nbsp; 2. Class D&nbsp; 3. State Licensing Authority&nbsp; 4. premarket approval (PMA)&nbsp; 5. substantial equivalence&nbsp; 6. Annex VIII&nbsp; 7. notified body&nbsp; 8. 26 May 2021&nbsp; 9. 2011&nbsp; 10. intended use / intended purpose</p>
  <p><strong>Assertion–Reasoning:</strong> 1-a&nbsp; 2-c&nbsp; 3-a&nbsp; 4-d&nbsp; 5-b</p>

  <p style="color:#5B6770;font-size:8.6pt;margin-top:6mm;">Keys for SAQ, LAQ and HOTS items are provided as model-answer frameworks in the Faculty Package (companion product, forthcoming).</p>
</section>"""


def consolidated_refs_html():
    refs = [
        "Central Drugs Standard Control Organisation. Medical Devices Rules, 2017 (G.S.R. 78(E), dated 31 January 2017), as amended. New Delhi: Ministry of Health and Family Welfare, Government of India; 2017.",
        "Government of India. Drugs and Cosmetics Act, 1940 and Rules thereunder. New Delhi: Ministry of Health and Family Welfare.",
        "Department of Pharmaceuticals. National Medical Device Policy, 2023. New Delhi: Ministry of Chemicals and Fertilizers, Government of India; 2023.",
        "US Food and Drug Administration. Federal Food, Drug, and Cosmetic Act, Section 201(h): definition of device. Silver Spring (MD): FDA.",
        "US Food and Drug Administration. Classify your medical device [Internet]. Silver Spring (MD): FDA. Available from: https://www.fda.gov/medical-devices",
        "US Food and Drug Administration. Premarket notification 510(k); Premarket approval (PMA); De Novo classification request [guidance documents]. Silver Spring (MD): FDA.",
        "European Parliament and Council. Regulation (EU) 2017/745 of 5 April 2017 on medical devices. Official Journal of the European Union. 2017;L117:1-175.",
        "European Commission. MDCG guidance documents on classification and conformity assessment. Brussels: DG SANTE.",
        "International Medical Device Regulators Forum. IMDRF/SaMD WG/N10:2013 — Software as a Medical Device: key definitions. IMDRF; 2013.",
        "World Health Organization. WHO Global Model Regulatory Framework for Medical Devices including in vitro diagnostic medical devices. Geneva: WHO; 2017.",
        "International Organization for Standardization. ISO 13485:2016 — Medical devices — Quality management systems — Requirements for regulatory purposes. Geneva: ISO; 2016.",
        "International Organization for Standardization. ISO 14971:2019 — Medical devices — Application of risk management to medical devices. Geneva: ISO; 2019.",
        "Indian Pharmacopoeia Commission. Materiovigilance Programme of India (MvPI) [Internet]. Ghaziabad: IPC, Ministry of Health and Family Welfare.",
        "Invest India / Department of Pharmaceuticals. Medical devices sector profile and Production Linked Incentive (PLI) scheme for medical devices (2020). New Delhi: Government of India.",
        "World Health Organization. Medical devices [fact sheets and landscape documents]. Geneva: WHO.",
    ]
    lis = "".join("<li>%s</li>" % r for r in refs)
    return """
<section class="backmatter-section" id="biblio" data-running="Consolidated References">
  <h1 class="fm-title">Consolidated References</h1>
  <p style="color:#5B6770;font-size:9pt;">Vancouver style. Chapter-level references appear at the end of each chapter; this consolidated list will grow as production phases complete.</p>
  <div class="references" style="border-top:none;padding-top:0;"><ol>%s</ol></div>
</section>""" % lis
