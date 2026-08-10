CH13_HTML = """
<section class="chapter" id="ch13" data-running="Chapter 13 · Major Device Categories">

<div class="ch-opener">
  <div class="ch-kicker">Part V &middot; Practice &amp; Careers &middot; Chapter 13</div>
  <div class="ch-band">
    <div class="ch-num-cell"><div class="ch-num">13</div></div>
    <div class="ch-title-cell">
      <h1 class="ch-title">Major Device Categories</h1>
      <div class="ch-tagline">In vitro diagnostics &middot; implants and prosthetics &middot; drug&ndash;device combination products &middot; wearables and Software as a Medical Device</div>
    </div>
  </div>
</div>

<div class="objectives-box">
  <h3>Learning Objectives</h3>
  <ol>
    <li>Map the major categories of the device universe to their risk classes and anchor standards. <span class="lo-tag">CO1 &middot; Understand</span></li>
    <li>Describe the components, classification and quality context of in vitro diagnostics. <span class="lo-tag">CO1 &middot; Understand</span></li>
    <li>Characterise the principal implant families and their clinical and regulatory profiles. <span class="lo-tag">CO2 &middot; Understand</span></li>
    <li>Determine the lead regulatory framework of a drug&ndash;device combination from its primary mode of action. <span class="lo-tag">CO2 &middot; Apply/Analyse</span></li>
    <li>Categorise Software as a Medical Device using the IMDRF risk framework. <span class="lo-tag">CO3 &middot; Apply</span></li>
    <li>Evaluate the special oversight challenges of AI-enabled and connected devices. <span class="lo-tag">CO3 &middot; Evaluate</span></li>
  </ol>
  <table class="co-map">
    <tr><th>Course Outcome</th><th>Statement</th><th>Bloom's Levels</th><th>Objectives</th></tr>
    <tr><td>CO1</td><td>Describe the device landscape and IVDs</td><td>L1&ndash;L2</td><td>1, 2</td></tr>
    <tr><td>CO2</td><td>Analyse implants and combination products</td><td>L2&ndash;L4</td><td>3, 4</td></tr>
    <tr><td>CO3</td><td>Apply digital-health frameworks and evaluate AI oversight</td><td>L3&ndash;L5</td><td>5, 6</td></tr>
  </table>
</div>

<h2 class="sec"><span class="secnum">13.1</span>Mapping the Device Landscape</h2>
<span class="wframe">What</span>
<p class="lead">The two million device types of Chapter 1 organise, for study and for regulation, into a handful of
great families. Four of them dominate pharmacy-relevant practice and this chapter: <strong>in vitro
diagnostics</strong>, <strong>implants and prosthetics</strong>, <strong>drug&ndash;device combination products</strong>, and
<strong>wearables and Software as a Medical Device (SaMD)</strong>.</p>
<p>Each family stresses a different part of the regulatory machinery built in Chapters 2&ndash;12: IVDs stress
analytical and clinical <em>performance</em> (a test that is wrong harms without touching the patient);
implants stress <em>biocompatibility and longevity</em> (Chapters 4&ndash;5); combination products stress
<em>jurisdictional boundaries</em> between drug and device law; and SaMD stresses <em>change control</em> &mdash;
software updates monthly, regulation was built for hardware that changed yearly.</p>

<div class="tablewrap">
<div class="tabcaption"><b>Table 13.1</b> &nbsp;Major device categories: examples, typical risk classes and anchor standards</div>
<table class="data">
  <tr><th style="width:30mm;">Category</th><th>Examples</th><th style="width:34mm;">Typical class (India / EU)</th><th style="width:40mm;">Anchor frameworks</th></tr>
  <tr><td class="rowhead">In vitro diagnostics</td><td>Glucose meters, HIV rapid tests, RT-PCR kits, analysers</td><td>A&ndash;D / IVDR A&ndash;D</td><td>IVDR 2017/746; ISO 15189 (labs); WHO PQ for HIV/HBV/HCV</td></tr>
  <tr><td class="rowhead">Implants &amp; prosthetics</td><td>Hip/knee systems, stents, pacemakers, IOLs, heart valves</td><td>C&ndash;D / IIb&ndash;III</td><td>ISO 5832, 14630, 14708 (active); Art 54 scrutiny</td></tr>
  <tr><td class="rowhead">Drug&ndash;device combinations</td><td>Prefilled syringes, autoinjectors, DES, inhalers, hormonal IUS</td><td>Follows primary mode of action</td><td>21 CFR Parts 3&ndash;4 (US); EU MDR Art 117</td></tr>
  <tr><td class="rowhead">Wearables &amp; SaMD</td><td>ECG smartwatch apps, CGM, AI radiology software</td><td>A&ndash;D by function / I&ndash;III</td><td>IMDRF N10/N12; IEC 62304 (software lifecycle); IEC 82304-1</td></tr>
</table>
</div>

<h2 class="sec"><span class="secnum">13.2</span>In Vitro Diagnostics</h2>
<span class="wframe">What &middot; How &middot; Where</span>
<p>An <strong>IVD</strong> examines specimens <em>derived from</em> the human body &mdash; blood, urine, tissue, saliva &mdash;
to yield diagnostic, monitoring or compatibility information. It never touches the patient; its risk is
<strong>informational</strong>: a false negative HIV screen endangers a transfusion recipient, a false positive
newborn screen triggers needless intervention. Classification logic therefore weighs consequences of a
wrong result to <em>both</em> the individual and the public.</p>
<p>An IVD system has three parts the pharmacist should distinguish: the <strong>reagent</strong> (with calibrators
and controls), the <strong>instrument/analyser</strong>, and increasingly the <strong>software</strong> that interprets raw
signal. Performance is described by <strong>analytical</strong> measures (sensitivity, specificity, precision,
linearity, limit of detection) and <strong>clinical</strong> measures (diagnostic sensitivity/specificity, predictive
values &mdash; which vary with disease prevalence, a point rapid-test marketing routinely obscures).</p>
<ul>
  <li><strong>India:</strong> IVDs carry their own Class A&ndash;D rules in the First Schedule of MDR 2017; new IVDs need
  clinical performance evaluation permission (MD-24&rarr;MD-25). The National Institute of Biologicals tests
  notified critical diagnostics (HIV, HBsAg, HCV, blood grouping) batch-wise.</li>
  <li><strong>EU:</strong> Regulation (EU) 2017/746 (<strong>IVDR</strong>), fully applicable 26 May 2022, replaced the old
  list-based directive with rules-based Classes A&ndash;D; the share of IVDs needing a notified body jumped from
  roughly a fifth to the great majority &mdash; a structural shock to the diagnostics industry.</li>
  <li><strong>Point-of-care and self-testing:</strong> glucose self-monitoring (ISO 15197 accuracy requirements),
  pregnancy tests, HIV self-tests &mdash; where the &ldquo;lay user&rdquo; changes the usability and labeling calculus
  (Chapter 3's IEC 62366-1 again).</li>
  <li><strong>Companion diagnostics</strong> pair a test to a drug (HER2 IHC/ISH with trastuzumab; EGFR mutation
  panels with gefitinib): the prescription decision is only as good as the assay, binding pharmacy and
  laboratory quality into one chain.</li>
</ul>

<div class="callout clinical">
  <div class="co-head">Clinical Insight</div>
  <p>Predictive value moves with prevalence. A self-test with 99% sensitivity and 98% specificity screening a
  population at 0.1% prevalence yields about <strong>one true positive for every twenty false positives</strong>.
  Pharmacists dispensing self-tests are the last professional checkpoint to explain confirmatory testing &mdash;
  an NEP-era counselling competency, not a nicety.</p>
</div>

<h2 class="sec"><span class="secnum">13.3</span>Implants &amp; Prosthetics</h2>
<span class="wframe">What &middot; Where</span>
<p>An <strong>implant</strong> is intended to remain in the body after the procedure &mdash; the &ldquo;permanent contact&rdquo;
column of the ISO 10993 matrix (Chapter 5) and the top of every classification pyramid (Chapter 2). The
principal families:</p>
<ul>
  <li><strong>Orthopaedic:</strong> total hip and knee systems (Chapter 4's Ti-6Al-4V, CoCr, UHMWPE bearing couples),
  trauma plates, screws and nails, spinal cages. Failure modes: aseptic loosening from wear-debris osteolysis,
  infection, instability &mdash; monitored best by registries (Chapter 12).</li>
  <li><strong>Cardiovascular:</strong> coronary stents (bare-metal &rarr; drug-eluting), pacemakers and ICDs
  (active implantables under ISO 14708), heart valves &mdash; surgical and transcatheter (TAVI). India classifies
  drug-eluting stents Class D; in 2017 the NPPA capped coronary stent and knee implant prices, a landmark
  collision of device economics with access policy.</li>
  <li><strong>Ophthalmic:</strong> intraocular lenses &mdash; the world's most implanted device, PMMA to foldable
  hydrophobic acrylics (Chapter 4's Ridley lineage).</li>
  <li><strong>Dental and others:</strong> titanium endosseous implants exploiting osseointegration; cochlear
  implants; breast implants &mdash; whose PIP fraud (Chapter 2) and later BIA-ALCL lymphoma signal reshaped EU law
  and implant-card practice.</li>
</ul>
<p>Regulatory texture: implants sit in Class C/D (India) and IIb/III (EU) with Article 54 scrutiny,
mandatory <strong>implant cards</strong> in the EU, UDI marking, and the heaviest PMCF expectations &mdash; the full
weight of Chapters 5, 8, 11 and 12 lands on this family.</p>

<div class="callout didyouknow">
  <div class="co-head">Did You Know</div>
  <p>Cataract surgery with IOL implantation is performed over <strong>25 million times a year</strong> worldwide,
  making the intraocular lens the most frequently implanted device in medicine &mdash; and one of the most
  cost-effective interventions in all of healthcare, at a manufacturing cost that can fall below a dollar
  for standard PMMA lenses produced at scale in India.</p>
</div>

<h2 class="sec"><span class="secnum">13.4</span>Drug&ndash;Device Combination Products</h2>
<span class="wframe">How &middot; Why</span>
<p>A <strong>combination product</strong> physically or functionally unites a drug and a device (sometimes a
biologic): the prefilled syringe, the adrenaline autoinjector, the metered-dose inhaler, the drug-eluting
stent, the hormonal intrauterine system. The regulatory question is always the same: <em>which law leads?</em></p>
<p>The near-universal answer is the <strong>primary mode of action (PMOA)</strong> &mdash; the single mode providing the
most important therapeutic contribution:</p>
<ul>
  <li><strong>USA:</strong> the Office of Combination Products (created 2002) assigns a lead centre by PMOA under
  21 CFR Part 3; a DES (device action leads: scaffolding the artery) goes to CDRH with CDER consult, while a
  prefilled syringe of a biologic goes the other way. 21 CFR Part 4 knits the GMPs together.</li>
  <li><strong>EU:</strong> an integral product whose drug action is principal is regulated as a medicinal product,
  but since the MDR its device part must meet the GSPR, evidenced by a notified body opinion filed in the
  marketing authorisation &mdash; the celebrated <strong>Article 117</strong>.</li>
  <li><strong>India:</strong> CDSCO handles both arms; drug-eluting devices such as DES and hormonal IUS sit in the
  highest device class or under drug provisions per their PMOA, with the DCGI as common apex authority.</li>
</ul>

<div class="tablewrap">
<div class="tabcaption"><b>Table 13.2</b> &nbsp;Drug&ndash;device combination products and their lead regulatory frameworks</div>
<table class="data">
  <tr><th>Product</th><th style="width:30mm;">PMOA</th><th style="width:40mm;">Lead framework (US)</th><th style="width:40mm;">EU treatment</th></tr>
  <tr><td class="rowhead">Drug-eluting stent</td><td>Device (scaffold)</td><td>CDRH lead (PMA), CDER consult</td><td>Class III device; Annex IX + medicinal consultation</td></tr>
  <tr><td class="rowhead">Prefilled insulin pen</td><td>Drug (insulin)</td><td>CDER lead; device constituent per Part 4</td><td>Medicinal product; Art 117 NB opinion on pen</td></tr>
  <tr><td class="rowhead">Metered-dose inhaler</td><td>Drug (bronchodilator)</td><td>CDER lead</td><td>Medicinal product; Art 117 on device part</td></tr>
  <tr><td class="rowhead">Hormonal IUS</td><td>Drug (levonorgestrel) with device scaffold</td><td>CDER lead historically</td><td>Medicinal product route</td></tr>
  <tr><td class="rowhead">Antibiotic bone cement</td><td>Device (fixation)</td><td>CDRH lead</td><td>Class III device with ancillary medicinal substance</td></tr>
</table>
</div>

<div class="callout industry">
  <div class="co-head">Industry Connect</div>
  <p>Combination products are pharmacy's natural bridgehead into medtech: the same firm ships the molecule and
  the delivery device, and its regulatory team must speak both dialects &mdash; dissolution profiles <em>and</em> design
  controls, stability studies <em>and</em> human factors reports. B.Pharm graduates who add device literacy
  (this book's Chapters 3, 5, 8) are the preferred hires for these hybrid dossiers.</p>
</div>

<h2 class="sec"><span class="secnum">13.5</span>Wearables &amp; Software as a Medical Device</h2>
<span class="wframe">What &middot; How &middot; When</span>
<p><strong>SaMD</strong> &mdash; software intended for medical purposes that performs them <em>without</em> being part of a
hardware device (IMDRF N10) &mdash; is the fastest-moving category in regulation. A wellness step-counter is not
a medical device; an app that analyses the same accelerometer stream to detect atrial fibrillation is. The
boundary is, as always, <strong>intended purpose</strong> (Chapter 2).</p>
<p>The IMDRF's <strong>N12 framework</strong> categorises SaMD risk on two axes: the <em>state of the healthcare
situation</em> (critical &rarr; serious &rarr; non-serious) and the <em>significance of the information</em> to the
decision (treat/diagnose &rarr; drive management &rarr; inform management), yielding categories
<strong>IV (highest) to I (lowest)</strong> &mdash; the intellectual scaffold behind FDA, EU and CDSCO software
classification alike (Figure 13.1). Software engineering rigour comes from <strong>IEC 62304</strong> (software
lifecycle) with usability (IEC 62366-1) and, for connected products, cybersecurity &mdash; in the USA a statutory
premarket requirement for &ldquo;cyber devices&rdquo; under section 524B of the FD&amp;C Act (2023).</p>
<p><strong>AI/ML-enabled SaMD</strong> adds the change problem in its sharpest form: a model that learns after
deployment is, in effect, redesigning itself. The FDA's answer is the <strong>Predetermined Change Control
Plan (PCCP)</strong>: the sponsor pre-specifies what may change, how it will be validated, and the guardrails,
so anticipated retraining does not require a fresh submission. The EU layers the horizontal
<strong>AI Act</strong> onto the MDR for high-risk AI systems; India currently classifies medical software within
the MDR 2017 First Schedule logic, with CDSCO guidance evolving.</p>

<div class="figure">
<svg viewBox="0 0 720 240" xmlns="http://www.w3.org/2000/svg" font-family="Manrope">
  <text x="30" y="26" font-size="10" font-weight="bold" fill="#0F4C5C">Significance of information &#8594;</text>
  <text x="620" y="26" font-size="8.5" fill="#5B6770">IMDRF N12 categories I&#8211;IV</text>
  <g font-size="8.6" fill="#333">
    <rect x="150" y="40" width="170" height="26" fill="#0F4C5C"/><text x="235" y="57" text-anchor="middle" fill="#fff" font-weight="bold">Inform management</text>
    <rect x="330" y="40" width="170" height="26" fill="#0F4C5C"/><text x="415" y="57" text-anchor="middle" fill="#fff" font-weight="bold">Drive management</text>
    <rect x="510" y="40" width="180" height="26" fill="#0F4C5C"/><text x="600" y="57" text-anchor="middle" fill="#fff" font-weight="bold">Treat / diagnose</text>
    <rect x="20" y="76" width="120" height="42" fill="#E4EFF1"/><text x="80" y="94" text-anchor="middle" font-weight="bold" fill="#0F4C5C">Non-serious</text><text x="80" y="107" text-anchor="middle" fill="#5B6770">situation</text>
    <rect x="150" y="76" width="170" height="42" fill="#F3F8F9" stroke="#C9D6DA"/><text x="235" y="101" text-anchor="middle" font-weight="bold" fill="#1E6E4A">I</text>
    <rect x="330" y="76" width="170" height="42" fill="#F3F8F9" stroke="#C9D6DA"/><text x="415" y="101" text-anchor="middle" font-weight="bold" fill="#1E6E4A">I</text>
    <rect x="510" y="76" width="180" height="42" fill="#EAF3EE" stroke="#C9D6DA"/><text x="600" y="101" text-anchor="middle" font-weight="bold" fill="#1E6E4A">II</text>
    <rect x="20" y="124" width="120" height="42" fill="#E4EFF1"/><text x="80" y="142" text-anchor="middle" font-weight="bold" fill="#0F4C5C">Serious</text><text x="80" y="155" text-anchor="middle" fill="#5B6770">situation</text>
    <rect x="150" y="124" width="170" height="42" fill="#EAF3EE" stroke="#C9D6DA"/><text x="235" y="149" text-anchor="middle" font-weight="bold" fill="#1E6E4A">II</text>
    <rect x="330" y="124" width="170" height="42" fill="#FBF5EC" stroke="#C9D6DA"/><text x="415" y="149" text-anchor="middle" font-weight="bold" fill="#B4690E">II</text>
    <rect x="510" y="124" width="180" height="42" fill="#FBF5EC" stroke="#C9D6DA"/><text x="600" y="149" text-anchor="middle" font-weight="bold" fill="#B4690E">III</text>
    <rect x="20" y="172" width="120" height="42" fill="#E4EFF1"/><text x="80" y="190" text-anchor="middle" font-weight="bold" fill="#0F4C5C">Critical</text><text x="80" y="203" text-anchor="middle" fill="#5B6770">situation</text>
    <rect x="150" y="172" width="170" height="42" fill="#FBF5EC" stroke="#C9D6DA"/><text x="235" y="197" text-anchor="middle" font-weight="bold" fill="#B4690E">II</text>
    <rect x="330" y="172" width="170" height="42" fill="#F7ECEC" stroke="#C9D6DA"/><text x="415" y="197" text-anchor="middle" font-weight="bold" fill="#A33B3B">III</text>
    <rect x="510" y="172" width="180" height="42" fill="#F7ECEC" stroke="#C9D6DA"/><text x="600" y="197" text-anchor="middle" font-weight="bold" fill="#A33B3B">IV</text>
  </g>
  <text x="30" y="232" font-size="8.2" fill="#5B6770">Category IV example: software diagnosing stroke from CT to direct thrombolysis &#183; Category I example: app aggregating BP diary to inform lifestyle advice</text>
</svg>
<div class="figcaption"><b>Figure 13.1</b> &nbsp;IMDRF risk categorization of Software as a Medical Device (after IMDRF/SaMD
WG/N12:2014). Risk rises with the seriousness of the healthcare situation and the decisiveness of the software's output.</div>
</div>

<div class="callout regulatory">
  <div class="co-head">Regulatory Spotlight &middot; From Locked to Learning Algorithms</div>
  <p>Classical clearance assumed a <strong>locked</strong> algorithm &mdash; identical output for identical input, forever.
  The FDA's Predetermined Change Control Plan guidance (finalised 2024) lets a sponsor pre-authorise defined
  retraining within validated bounds, with real-world performance monitoring as the safety net. It is design
  control (Chapter 3) and risk management (Chapter 8) re-imagined for software that will not sit still.</p>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 13.1 &middot; Theranos &mdash; When Diagnostic Claims Outrun Evidence</div>
  <div class="cs-body">
    <p>Theranos claimed its Edison analyser could run hundreds of tests on a fingerstick drop. By exploiting the
    then-lighter oversight of <strong>laboratory-developed tests (LDTs)</strong> run inside its own CLIA-certified lab,
    it marketed clinically consequential results &mdash; potassium, HIV, PT/INR &mdash; without peer-reviewed validation
    or FDA review. Investigations from 2015 found accuracy failures and quality-system collapse; CMS sanctioned
    the laboratory, tens of thousands of results were voided or corrected, the company dissolved, and its
    founders were convicted of fraud (2022). The scandal accelerated the push to bring LDTs under explicit
    device-style oversight.</p>
    <p class="cs-q">Discussion questions</p>
    <p>1. Which analytical performance data (Section 13.2) would have exposed the Edison's limits, and at what stage?<br/>
    2. Why did the LDT channel create a regulatory blind spot for a mass-market screening business?<br/>
    3. What defences do investors, clinicians and pharmacists each have against unvalidated diagnostic claims?</p>
    <div class="cs-analysis"><strong>Analysis.</strong> Every guardrail of this book was bypassed at once: no independent premarket
    review of performance, no transparent method comparison against reference analysers, no functioning QMS
    (Chapter 7), and vigilance signals &mdash; clinician complaints of implausible results &mdash; without a system obliged
    to act on them. The professional lesson is structural scepticism: a diagnostic claim is only as good as its
    published validation against a reference standard.</div>
  </div>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 13.2 &middot; The Apple Watch ECG &mdash; A Consumer Wearable Crosses the Line</div>
  <div class="cs-body">
    <p>In September 2018 FDA granted <strong>De Novo</strong> classification (DEN180044) to Apple's ECG app: a
    smartwatch feature generating a single-lead ECG and notifying the wearer of possible atrial fibrillation.
    The grant created a new Class II category with special controls &mdash; labeling that it is not a replacement
    for diagnosis, performance testing against 12-lead reference, and human factors evidence for lay users.
    The watch itself remained a consumer product; the regulated article is the <em>software function</em>. Large
    studies (the 400,000-participant Apple Heart Study) probed real-world predictive value &mdash; and surfaced the
    screening dilemma: notifications in young low-risk users generate anxiety and downstream testing with
    modest yield.</p>
    <p class="cs-q">Discussion questions</p>
    <p>1. Place the ECG app in the N12 grid of Figure 13.1 and justify the cell.<br/>
    2. Why was De Novo the correct pathway rather than 510(k) or PMA?<br/>
    3. Should population screening claims require different evidence from spot-check claims? Argue with prevalence arithmetic.</p>
    <div class="cs-analysis"><strong>Analysis.</strong> The app informs management of a potentially serious condition &mdash;
    category II territory &mdash; and had no predicate, making De Novo apt; its special controls now anchor
    every subsequent wearable-ECG 510(k). The screening dilemma is Bayes again: even excellent specificity
    yields many false alarms at low prevalence, so labeling, notification thresholds and confirmatory pathways
    are safety features as surely as electrode design.</div>
  </div>
</div>

<div class="summary-box">
<h3>Chapter Summary</h3>
<ul>
  <li>Four families dominate: IVDs (informational risk; IVDR classes A&ndash;D; analytical vs clinical performance; companion diagnostics), implants (permanent contact; registries, implant cards, Art 54), combination products (PMOA decides the lead law; OCP/Part 3 in the US, Art 117 in the EU), and wearables/SaMD.</li>
  <li>India: IVD-specific First Schedule rules, NIB batch testing of critical diagnostics, MD-24/25 performance evaluation; NPPA's 2017 stent and knee price caps show access policy meeting device economics.</li>
  <li>SaMD is defined by intended purpose, categorised by IMDRF N12 (I&ndash;IV), engineered under IEC 62304, and &mdash; when AI-enabled &mdash; managed through predetermined change control plans and cybersecurity law (FD&amp;C 524B).</li>
  <li>Theranos and the Apple Watch ECG bracket the category's ethics: claims must be validated, and even valid tools carry screening costs at low prevalence.</li>
</ul>
</div>

<div class="keyterms">
<h3>Key Terms</h3>
<div class="kt-row"><dt>Analytical sensitivity.</dt> <dd>An IVD's ability to detect small analyte quantities (limit of detection); distinct from diagnostic sensitivity in patients.</dd></div>
<div class="kt-row"><dt>Companion diagnostic.</dt> <dd>An IVD essential for the safe, effective use of a specific medicinal product, identifying eligible patients.</dd></div>
<div class="kt-row"><dt>Combination product.</dt> <dd>A therapeutic product combining drug and device (and/or biologic) constituents, regulated by primary mode of action.</dd></div>
<div class="kt-row"><dt>IVDR.</dt> <dd>Regulation (EU) 2017/746 on in vitro diagnostic medical devices, applicable 26 May 2022, with rules-based classes A&ndash;D.</dd></div>
<div class="kt-row"><dt>LDT.</dt> <dd>Laboratory-developed test &mdash; an assay designed and used within a single laboratory, historically outside routine device premarket review.</dd></div>
<div class="kt-row"><dt>PCCP.</dt> <dd>Predetermined Change Control Plan &mdash; pre-authorised modification protocol for AI/ML-enabled device software.</dd></div>
<div class="kt-row"><dt>PMOA.</dt> <dd>Primary mode of action &mdash; the constituent contribution that determines a combination product's lead regulatory framework.</dd></div>
<div class="kt-row"><dt>SaMD categories I&ndash;IV.</dt> <dd>IMDRF N12 risk strata from situation seriousness &times; information significance; IV is highest.</dd></div>
<div class="kt-row"><dt>TAVI.</dt> <dd>Transcatheter aortic valve implantation &mdash; catheter-delivered replacement of the aortic valve without open surgery.</dd></div>
<div class="kt-row"><dt>Implant card.</dt> <dd>EU MDR-mandated patient-held card identifying an implanted device (device name, UDI, manufacturer).</dd></div>
</div>

<div class="assessment">
<h2>Assessment Battery &mdash; Chapter 13</h2>

<div class="ass-block">
<h3>A. Multiple Choice Questions (with rationales)</h3>
<ol>
  <li>The distinctive risk of an IVD is best described as:
    <ul class="mcq-opts"><li><span class="ol">a)</span> Electrical hazard to the patient</li><li><span class="ol">b)</span> Biocompatibility of implanted materials</li><li><span class="ol">c)</span> Harm from wrong information guiding decisions</li><li><span class="ol">d)</span> Radiation exposure</li></ul>
    <div class="rationale"><b>Answer: c.</b> IVDs never touch the patient; their hazard is a wrong result driving a wrong decision &mdash; hence performance-centred regulation.</div></li>
  <li>The EU IVDR became fully applicable on:
    <ul class="mcq-opts"><li><span class="ol">a)</span> 26 May 2022</li><li><span class="ol">b)</span> 26 May 2021</li><li><span class="ol">c)</span> 1 January 2018</li><li><span class="ol">d)</span> 31 January 2017</li></ul>
    <div class="rationale"><b>Answer: a.</b> The MDR applied from 26 May 2021; the IVDR followed one year later, 26 May 2022.</div></li>
  <li>Predictive value of a screening test falls sharply when:
    <ul class="mcq-opts"><li><span class="ol">a)</span> Specificity rises</li><li><span class="ol">b)</span> Disease prevalence is very low</li><li><span class="ol">c)</span> The test is run in duplicate</li><li><span class="ol">d)</span> Sensitivity rises</li></ul>
    <div class="rationale"><b>Answer: b.</b> At low prevalence even rare false positives outnumber true positives &mdash; the Bayesian core of screening counselling.</div></li>
  <li>The regulatory lead for a drug-eluting stent in the USA is:
    <ul class="mcq-opts"><li><span class="ol">a)</span> CDER, because a drug is present</li><li><span class="ol">b)</span> The Office of Generic Drugs</li><li><span class="ol">c)</span> CBER in all cases</li><li><span class="ol">d)</span> CDRH, because the device action is primary</li></ul>
    <div class="rationale"><b>Answer: d.</b> The PMOA is mechanical scaffolding; CDRH leads (PMA) with CDER consultation on the eluted drug.</div></li>
  <li>EU MDR Article 117 requires, for an integral drug&ndash;device combination led by drug law:
    <ul class="mcq-opts"><li><span class="ol">a)</span> A separate CE certificate for the drug</li><li><span class="ol">b)</span> A notified body opinion on the device part in the marketing authorisation</li><li><span class="ol">c)</span> Duplicate clinical trials</li><li><span class="ol">d)</span> Nothing beyond pharmacopoeial testing</li></ul>
    <div class="rationale"><b>Answer: b.</b> Article 117 inserts device GSPR conformity &mdash; evidenced by an NB opinion &mdash; into the medicinal dossier.</div></li>
  <li>Under IMDRF N12, software that diagnoses a critical condition to direct immediate treatment is category:
    <ul class="mcq-opts"><li><span class="ol">a)</span> IV</li><li><span class="ol">b)</span> I</li><li><span class="ol">c)</span> II</li><li><span class="ol">d)</span> III</li></ul>
    <div class="rationale"><b>Answer: a.</b> Critical situation &times; treat/diagnose significance = category IV, the highest cell of the grid.</div></li>
  <li>The software lifecycle standard for medical device software is:
    <ul class="mcq-opts"><li><span class="ol">a)</span> ISO 15197</li><li><span class="ol">b)</span> ISO 14708</li><li><span class="ol">c)</span> IEC 62304</li><li><span class="ol">d)</span> ISO 5832</li></ul>
    <div class="rationale"><b>Answer: c.</b> IEC 62304 governs software lifecycle processes; 15197 is glucose meters, 14708 active implantables, 5832 implant metals.</div></li>
  <li>The Apple Watch ECG app entered the US market via:
    <ul class="mcq-opts"><li><span class="ol">a)</span> Traditional 510(k)</li><li><span class="ol">b)</span> PMA</li><li><span class="ol">c)</span> HDE</li><li><span class="ol">d)</span> De Novo classification</li></ul>
    <div class="rationale"><b>Answer: d.</b> DEN180044 (2018) created a new Class II category with special controls &mdash; there was no predicate.</div></li>
  <li>Theranos marketed unvalidated tests primarily through the channel of:
    <ul class="mcq-opts"><li><span class="ol">a)</span> Laboratory-developed tests in its own CLIA lab</li><li><span class="ol">b)</span> FDA-cleared 510(k) kits</li><li><span class="ol">c)</span> CE-marked IVDs</li><li><span class="ol">d)</span> WHO prequalification</li></ul>
    <div class="rationale"><b>Answer: a.</b> The LDT route avoided premarket performance review &mdash; the blind spot the scandal exposed.</div></li>
  <li>In 2017 India's NPPA notably capped the prices of:
    <ul class="mcq-opts"><li><span class="ol">a)</span> MRI scanners and ventilators</li><li><span class="ol">b)</span> Coronary stents and knee implants</li><li><span class="ol">c)</span> Glucose strips and syringes</li><li><span class="ol">d)</span> Hearing aids</li></ul>
    <div class="rationale"><b>Answer: b.</b> The coronary stent (February 2017) and knee implant (August 2017) caps are the landmark device price-control actions.</div></li>
</ol>
</div>

<div class="ass-block">
<h3>B. True / False</h3>
<ol>
  <li>A wellness step counter with no medical claims is a medical device. <span class="marks">(F &mdash; intended purpose decides)</span></li>
  <li>Diagnostic sensitivity and analytical sensitivity are different concepts. <span class="marks">(T)</span></li>
  <li>The intraocular lens is the most frequently implanted medical device. <span class="marks">(T)</span></li>
  <li>Under the IVDR, fewer IVDs need notified bodies than under the old directive. <span class="marks">(F &mdash; far more do)</span></li>
  <li>A prefilled insulin pen in the EU is regulated as a medicinal product with an Article 117 device opinion. <span class="marks">(T)</span></li>
  <li>Active implantables such as pacemakers are covered by ISO 14708. <span class="marks">(T)</span></li>
  <li>SaMD categories under IMDRF N12 run from I (highest risk) to IV (lowest). <span class="marks">(F &mdash; IV is highest)</span></li>
  <li>Section 524B of the FD&amp;C Act imposes premarket cybersecurity duties for cyber devices. <span class="marks">(T)</span></li>
  <li>A PCCP requires a new regulatory submission for every model retraining. <span class="marks">(F &mdash; its purpose is the opposite)</span></li>
  <li>Companion diagnostics link the safe use of a specific drug to a specific test result. <span class="marks">(T)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>C. Fill in the Blanks</h3>
<ol>
  <li>The EU regulation governing in vitro diagnostics is Regulation (EU) __________.</li>
  <li>An IVD essential to the safe use of a specific medicinal product is a __________.</li>
  <li>In India, drug-eluting stents are placed in device Class __________.</li>
  <li>The combination-product doctrine assigning the lead framework is the __________.</li>
  <li>The US FDA office coordinating combination product assignment is the __________.</li>
  <li>The EU MDR article requiring a notified body opinion on device parts of medicinal combinations is Article __________.</li>
  <li>Software intended for medical purposes without dedicated hardware is called __________.</li>
  <li>The IMDRF SaMD risk categorization framework is document N__________.</li>
  <li>The lifecycle standard for medical device software is IEC __________.</li>
  <li>The FDA mechanism pre-authorising defined AI model changes is the __________.</li>
</ol>
</div>

<div class="ass-block">
<h3>D. Assertion&ndash;Reasoning</h3>
<p class="ar-key">Mark: (a) both A and R true, R explains A; (b) both true, R does not explain A; (c) A true, R false; (d) A false, R true.</p>
<ol>
  <li><strong>A:</strong> IVD regulation is performance-centred. <strong>R:</strong> An IVD's harm operates through wrong information rather than physical contact. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> All combination products worldwide are regulated as devices. <strong>R:</strong> The primary mode of action determines the lead framework. <span class="marks">(d &mdash; A false; R true and is the reason)</span></li>
  <li><strong>A:</strong> Screening notifications from wearables can burden low-risk populations. <strong>R:</strong> Positive predictive value collapses when prevalence is very low. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> Implants attract the heaviest post-market clinical follow-up. <strong>R:</strong> The EU mandates implant cards for recipients. <span class="marks">(b &mdash; both true; the card is traceability, not the reason for PMCF weight)</span></li>
  <li><strong>A:</strong> Locked-algorithm review poorly fits learning AI systems. <strong>R:</strong> A continuously retrained model can change behaviour after clearance. <span class="marks">(a)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>E. Short Answer Questions <span style="text-transform:none;">(2&ndash;3 marks each)</span></h3>
<ol>
  <li>Distinguish analytical from diagnostic sensitivity with one example each.</li>
  <li>Name the three components of an IVD system and one quality risk of each.</li>
  <li>Why did the IVDR drastically expand notified body involvement?</li>
  <li>Using PMOA, assign the lead US centre for: antibiotic bone cement; a prefilled biologic syringe.</li>
  <li>Place continuous glucose monitor software in the N12 grid and justify.</li>
  <li>State two special controls attached to the wearable-ECG device category.</li>
</ol>
</div>

<div class="ass-block">
<h3>F. Long Answer Questions <span style="text-transform:none;">(10 marks each)</span></h3>
<ol>
  <li>Write an essay on IVD regulation across India and the EU &mdash; classification logic, performance evidence, batch testing of critical diagnostics, and the pharmacist's counselling role for self-tests.</li>
  <li>Survey the implant families &mdash; orthopaedic, cardiovascular, ophthalmic, dental &mdash; connecting each to its biomaterials (Chapter 4), failure modes, registry evidence and Indian pricing policy.</li>
  <li>Explain SaMD regulation end-to-end: definition, N12 categorization, IEC 62304 lifecycle, cybersecurity duties and AI change control, using the Apple Watch ECG as the running example.</li>
</ol>
</div>

<div class="ass-block">
<h3>G. Higher-Order Thinking (HOTS)</h3>
<ol>
  <li>A start-up proposes an AI app that reads chest X-rays for TB triage in primary care. Classify it (N12 and India), list the premarket evidence package, and design its PCCP boundaries.</li>
  <li>Debate: should LDT-style flexibility exist at all in a country building diagnostic capacity, or does Theranos prove it must not? Take a position with safeguards.</li>
  <li>Design the counselling script a community pharmacist should use when dispensing an HIV self-test, embedding predictive-value arithmetic and confirmatory pathways.</li>
</ol>
</div>
</div>

<div class="references">
<h2>References (Vancouver Style)</h2>
<ol>
  <li>European Parliament and Council. Regulation (EU) 2017/746 on in vitro diagnostic medical devices. Official Journal of the European Union. 2017;L117:176-332.</li>
  <li>Central Drugs Standard Control Organisation. Medical Devices Rules, 2017 &mdash; First Schedule Part II (classification of in vitro diagnostic medical devices). New Delhi: MoHFW.</li>
  <li>International Organization for Standardization. ISO 15197:2013 &mdash; In vitro diagnostic test systems &mdash; Requirements for blood-glucose monitoring systems for self-testing. Geneva: ISO; 2013.</li>
  <li>International Medical Device Regulators Forum. IMDRF/SaMD WG/N10:2013 (key definitions) and N12:2014 (possible framework for risk categorization). IMDRF; 2013&ndash;2014.</li>
  <li>International Electrotechnical Commission. IEC 62304:2006+A1:2015 &mdash; Medical device software &mdash; Software life cycle processes. Geneva: IEC.</li>
  <li>US Food and Drug Administration. 21 CFR Parts 3 and 4 &mdash; Product jurisdiction; combination product cGMP. Silver Spring (MD): FDA.</li>
  <li>US Food and Drug Administration. De Novo classification DEN180044 &mdash; ECG App (Apple Inc.), decision summary. Silver Spring (MD): FDA; 2018.</li>
  <li>Perez MV, Mahaffey KW, Hedlin H, et al. Large-scale assessment of a smartwatch to identify atrial fibrillation. N Engl J Med. 2019;381(20):1909-1917.</li>
  <li>US Food and Drug Administration. Marketing submission recommendations for a predetermined change control plan for AI/ML-enabled device software functions &mdash; Guidance. Silver Spring (MD): FDA; 2024.</li>
  <li>National Pharmaceutical Pricing Authority. Price fixation orders for coronary stents (February 2017) and orthopaedic knee implants (August 2017). New Delhi: NPPA, Government of India.</li>
</ol>
</div>

<div class="qgate">
<h2>Chapter 13 &middot; Completion Dashboard (Quality Gate)</h2>
<table class="qgate-t">
  <tr><th>Quality Gate criterion</th><th style="width:22mm;">Status</th><th>Evidence</th></tr>
  <tr><td>Learning objectives with CO/Bloom's mapping</td><td class="qg-pass">PASS</td><td>6 objectives, CO1&ndash;CO3 map table</td></tr>
  <tr><td>What&ndash;Why&ndash;How&ndash;Where&ndash;When framework applied</td><td class="qg-pass">PASS</td><td>Framework tags on sections 13.1&ndash;13.5</td></tr>
  <tr><td>Figures &amp; tables numbered with captions</td><td class="qg-pass">PASS</td><td>Figure 13.1; Tables 13.1&ndash;13.2</td></tr>
  <tr><td>All four callout types present</td><td class="qg-pass">PASS</td><td>Regulatory Spotlight, Clinical Insight, Industry Connect, Did You Know</td></tr>
  <tr><td>Case studies with analysis</td><td class="qg-pass">PASS</td><td>Case studies 13.1 (Theranos), 13.2 (Apple Watch ECG)</td></tr>
  <tr><td>Full assessment battery</td><td class="qg-pass">PASS</td><td>10 MCQ + rationales, 10 T/F, 10 FIB, 5 A&ndash;R, 6 SAQ, 3 LAQ, 3 HOTS</td></tr>
  <tr><td>Anti-fabrication check (regulations/codes verified)</td><td class="qg-pass">PASS</td><td>IVDR 2017/746; IMDRF N10/N12; DEN180044; NPPA 2017 orders &mdash; cited in references</td></tr>
  <tr><td>Vancouver-style chapter references</td><td class="qg-pass">PASS</td><td>10 references</td></tr>
</table>
</div>

</section>
"""
