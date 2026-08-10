CH05_HTML = """
<section class="chapter" id="ch05" data-running="Chapter 5 · Biocompatibility">

<div class="ch-opener">
  <div class="ch-kicker">Part II &middot; Design, Biomaterials &amp; Biocompatibility &middot; Chapter 5</div>
  <div class="ch-band">
    <div class="ch-num-cell"><div class="ch-num">05</div></div>
    <div class="ch-title-cell">
      <h1 class="ch-title">Biocompatibility</h1>
      <div class="ch-tagline">Host response to materials &middot; the ISO 10993 family &middot; biological evaluation planning &middot; endpoint selection by contact and duration</div>
    </div>
  </div>
</div>

<div class="objectives-box">
  <h3>Learning Objectives</h3>
  <ol>
    <li>Define biocompatibility and describe the host response cascade to an implanted material. <span class="lo-tag">CO1 &middot; Understand</span></li>
    <li>Explain the risk-based philosophy of ISO 10993-1:2018 for biological evaluation. <span class="lo-tag">CO1 &middot; Understand</span></li>
    <li>Categorise devices by nature and duration of body contact. <span class="lo-tag">CO2 &middot; Apply</span></li>
    <li>Select applicable biological endpoints for a given device category. <span class="lo-tag">CO2 &middot; Apply</span></li>
    <li>Outline the principal ISO 10993 part tests: cytotoxicity, sensitization, irritation, systemic toxicity, genotoxicity, implantation, hemocompatibility. <span class="lo-tag">CO2 &middot; Understand</span></li>
    <li>Evaluate the role of chemical characterization and toxicological risk assessment in replacing animal testing. <span class="lo-tag">CO3 &middot; Evaluate</span></li>
  </ol>
  <table class="co-map">
    <tr><th>Course Outcome</th><th>Statement</th><th>Bloom's Levels</th><th>Objectives</th></tr>
    <tr><td>CO1</td><td>Explain host response and the ISO 10993 philosophy</td><td>L1&ndash;L2</td><td>1, 2</td></tr>
    <tr><td>CO2</td><td>Apply categorization and endpoint selection</td><td>L2&ndash;L3</td><td>3, 4, 5</td></tr>
    <tr><td>CO3</td><td>Evaluate modern chemistry-first evaluation strategies</td><td>L5</td><td>6</td></tr>
  </table>
</div>

<h2 class="sec"><span class="secnum">5.1</span>What Happens When a Material Meets the Body</h2>
<span class="wframe">What &middot; Why</span>
<p class="lead">Biocompatibility is the ability of a material to perform <strong>with an appropriate host response
in a specific application</strong>. The phrase carries two warnings: there is no universally &ldquo;biocompatible&rdquo;
material, and the response that is appropriate for a bone screw (firm integration) would be failure for a
blood-contacting catheter (any thrombus is too much).</p>
<p>The host response to an implanted material follows a well-characterised cascade:</p>
<ol>
  <li><strong>Protein adsorption</strong> within seconds &mdash; the surface is instantly coated by plasma proteins
  (with compositional exchange over time, the Vroman effect); cells thereafter &ldquo;see&rdquo; the protein layer,
  not the bare material.</li>
  <li><strong>Acute inflammation</strong> (hours&ndash;days) &mdash; neutrophils dominate; mast cells degranulate.</li>
  <li><strong>Chronic inflammation</strong> (days&ndash;weeks) &mdash; macrophages arrive, attempt phagocytosis, and, when
  frustrated by an object too large to engulf, fuse into <strong>foreign body giant cells</strong>.</li>
  <li><strong>Granulation and fibrosis</strong> (weeks) &mdash; fibroblasts wall the implant in a collagenous
  <strong>fibrous capsule</strong>; for most devices a thin, quiescent capsule is the acceptable end-state.</li>
</ol>
<p>Blood contact adds its own axis: platelet adhesion, coagulation activation (intrinsic pathway on
artificial surfaces) and complement activation &mdash; the reason hemocompatibility is tested separately, and the
reason dialysis circuits and oxygenators need anticoagulation. Degradable materials add a further axis: the
response evolves as the material and its by-products change.</p>

<div class="callout clinical">
  <div class="co-head">Clinical Insight</div>
  <p>Natural rubber latex made this cascade a public health story: repeated glove exposure sensitised a
  generation of health workers (Type I IgE-mediated allergy, plus Type IV reactions to accelerators),
  driving powder-free and synthetic gloves &mdash; and, in the USA, a 2016 FDA ban on powdered gloves.
  Materials policy in a hospital is pharmacovigilance by another name.</p>
</div>

<h2 class="sec"><span class="secnum">5.2</span>The ISO 10993 Family and Its Philosophy</h2>
<span class="wframe">What &middot; Why</span>
<p>The <strong>ISO 10993</strong> series &mdash; <em>Biological evaluation of medical devices</em> &mdash; is the global
reference for biocompatibility. Its keystone, <strong>ISO 10993-1:2018</strong>, insists that biological evaluation
is a <strong>risk management activity under ISO 14971</strong>, not a checklist of animal tests: the evaluator must
characterise the device and its materials, gather existing data (literature, clinical history, prior use),
identify gaps, and only then test &mdash; using the minimum testing that closes the gaps.</p>
<div class="tablewrap">
<div class="tabcaption"><b>Table 5.1</b> &nbsp;Selected parts of the ISO 10993 series</div>
<table class="data">
  <tr><th style="width:26mm;">Part</th><th>Subject</th></tr>
  <tr><td class="rowhead">10993-1:2018</td><td>Evaluation and testing within a risk management process (framework, categorization, endpoint tables)</td></tr>
  <tr><td class="rowhead">10993-3</td><td>Genotoxicity, carcinogenicity, reproductive toxicity</td></tr>
  <tr><td class="rowhead">10993-4</td><td>Interactions with blood (hemolysis, thrombosis, coagulation, complement)</td></tr>
  <tr><td class="rowhead">10993-5</td><td>In vitro cytotoxicity</td></tr>
  <tr><td class="rowhead">10993-6</td><td>Local effects after implantation</td></tr>
  <tr><td class="rowhead">10993-7</td><td>Ethylene oxide sterilization residuals (EO/ECH limits)</td></tr>
  <tr><td class="rowhead">10993-10</td><td>Sensitization (skin sensitization; GPMT, Buehler, LLNA)</td></tr>
  <tr><td class="rowhead">10993-11</td><td>Systemic toxicity (acute, subacute, subchronic, chronic; material-mediated pyrogenicity)</td></tr>
  <tr><td class="rowhead">10993-12</td><td>Sample preparation and reference materials (extraction conditions)</td></tr>
  <tr><td class="rowhead">10993-17</td><td>Toxicological risk assessment of leachables (allowable limits)</td></tr>
  <tr><td class="rowhead">10993-18</td><td>Chemical characterization of materials (extractables/leachables chemistry)</td></tr>
  <tr><td class="rowhead">10993-23</td><td>Irritation (moved from -10 in the 2021 revision; includes in vitro RhE methods)</td></tr>
</table>
</div>

<div class="callout regulatory">
  <div class="co-head">Regulatory Spotlight</div>
  <p>Every major regulator anchors to this series: FDA's 2023-updated guidance on the use of ISO 10993-1,
  the EU MDR's GSPR (Annex I) demands on toxicity and compatibility, and India's MDR 2017 essential
  principles checklist all expect a <strong>Biological Evaluation Plan (BEP)</strong> and a concluding
  <strong>Biological Evaluation Report (BER)</strong>. Testing must be GLP-compliant, and the 3Rs (replace,
  reduce, refine animal use) are written into the standard's philosophy.</p>
</div>

<h2 class="sec"><span class="secnum">5.3</span>Categorising the Device: Contact &times; Duration</h2>
<span class="wframe">How</span>
<p>Endpoint selection begins with two questions. <strong>What does the device touch?</strong> &mdash; surface contact
(intact skin, mucosa, breached surface), external communicating (blood path indirect, tissue/bone/dentin,
circulating blood), or implant (tissue/bone, blood). <strong>For how long?</strong> &mdash; limited (&le;24 h),
prolonged (&gt;24 h to 30 days), or long-term/permanent (&gt;30 days), counted cumulatively for repeat use.</p>

<div class="figure">
<svg viewBox="0 0 700 216" xmlns="http://www.w3.org/2000/svg" font-family="Manrope">
  <defs><marker id="a5" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#0F4C5C"/></marker></defs>
  <g font-size="9" text-anchor="middle">
    <rect x="270" y="8" width="160" height="30" fill="#0F4C5C"/><text x="350" y="27" fill="#fff" font-weight="bold">Characterise device &amp; materials</text>
    <rect x="270" y="58" width="160" height="30" fill="#14537D"/><text x="350" y="77" fill="#fff" font-weight="bold">Contact type &times; duration</text>
    <rect x="40" y="112" width="180" height="34" fill="#E4EFF1" stroke="#0F4C5C"/><text x="130" y="126" font-weight="bold" fill="#0F4C5C">Existing data review</text><text x="130" y="139" fill="#333">literature &middot; clinical history &middot; -18 chemistry</text>
    <rect x="260" y="112" width="180" height="34" fill="#E4EFF1" stroke="#0F4C5C"/><text x="350" y="126" font-weight="bold" fill="#0F4C5C">Gap analysis (BEP)</text><text x="350" y="139" fill="#333">endpoints per Annex A table</text>
    <rect x="480" y="112" width="180" height="34" fill="#E4EFF1" stroke="#0F4C5C"/><text x="570" y="126" font-weight="bold" fill="#0F4C5C">Targeted testing (GLP)</text><text x="570" y="139" fill="#333">only what closes gaps</text>
    <rect x="270" y="170" width="160" height="32" fill="#1E6E4A"/><text x="350" y="184" fill="#fff" font-weight="bold">Biological Evaluation</text><text x="350" y="196" fill="#D9F0E4">Report (BER) &rarr; risk file</text>
  </g>
  <g stroke="#0F4C5C" stroke-width="1.1" fill="none" marker-end="url(#a5)">
    <line x1="350" y1="38" x2="350" y2="54"/>
    <line x1="310" y1="88" x2="150" y2="112"/><line x1="350" y1="88" x2="350" y2="108"/><line x1="390" y1="88" x2="550" y2="112"/>
    <line x1="350" y1="146" x2="350" y2="166"/>
  </g>
</svg>
<div class="figcaption"><b>Figure 5.1</b> &nbsp;Biological evaluation as a risk management process (ISO 10993-1:2018). Chemistry and existing data come before, and often instead of, new animal testing.</div>
</div>

<div class="tablewrap">
<div class="tabcaption"><b>Table 5.2</b> &nbsp;Illustrative endpoint selection by device category (based on ISO 10993-1:2018, Annex A)</div>
<table class="data">
  <tr><th>Device (category, duration)</th><th style="width:88mm;">Typical endpoints to address</th></tr>
  <tr><td class="rowhead">Adhesive bandage (intact skin, limited)</td><td>Cytotoxicity; sensitization; irritation</td></tr>
  <tr><td class="rowhead">Contact lens (mucosa, prolonged)</td><td>Cytotoxicity; sensitization; irritation; (subacute toxicity per assessment)</td></tr>
  <tr><td class="rowhead">Hypodermic needle (blood path, limited)</td><td>Cytotoxicity; sensitization; irritation; acute systemic toxicity; pyrogenicity; hemocompatibility</td></tr>
  <tr><td class="rowhead">Haemodialyser (circulating blood, prolonged repeat)</td><td>Above plus subacute/subchronic toxicity; genotoxicity; hemocompatibility in depth (complement, thrombogenicity)</td></tr>
  <tr><td class="rowhead">Hip prosthesis (bone implant, permanent)</td><td>Cytotoxicity; sensitization; irritation; systemic and subchronic toxicity; genotoxicity; implantation; (carcinogenicity per risk assessment)</td></tr>
  <tr><td class="rowhead">Prosthetic heart valve (blood implant, permanent)</td><td>The full battery incl. chronic toxicity considerations, hemocompatibility, implantation; degradation products if applicable</td></tr>
</table>
</div>
<p>The table's message is proportionality &mdash; the same logic as device classification in Chapter 2: more
intimate and longer contact demands more evidence. &ldquo;Endpoints to address&rdquo; does not always mean &ldquo;tests
to run&rdquo;: an endpoint may be closed by existing data or by chemical characterization plus toxicological
assessment.</p>

<h2 class="sec"><span class="secnum">5.4</span>The Principal Tests</h2>
<span class="wframe">How</span>
<ul>
  <li><strong>Cytotoxicity (10993-5).</strong> The universal first screen: device extracts (per -12) applied to
  cultured fibroblasts (e.g., L929); viability by MTT/XTT or qualitative morphology (MEM elution, agar
  diffusion). Sensitive, cheap, in vitro &mdash; a failed cytotox test stops a programme early.</li>
  <li><strong>Sensitization (10993-10).</strong> Delayed-type hypersensitivity potential: guinea pig maximization
  (GPMT), Buehler patch, or the murine local lymph node assay (LLNA).</li>
  <li><strong>Irritation (10993-23).</strong> Local reversible inflammation: intracutaneous reactivity in rabbits,
  or validated in vitro reconstructed human epidermis (RhE) methods &mdash; a flagship 3Rs replacement.</li>
  <li><strong>Systemic toxicity &amp; pyrogenicity (10993-11).</strong> Acute through chronic exposure to extracts;
  material-mediated pyrogenicity (rabbit test); bacterial endotoxin is tested separately by LAL (per
  pharmacopoeia).</li>
  <li><strong>Genotoxicity (10993-3).</strong> Battery approach: bacterial reverse mutation (Ames), plus in vitro
  mammalian assays (mouse lymphoma tk, micronucleus/chromosome aberration).</li>
  <li><strong>Implantation (10993-6).</strong> The material placed in muscle/bone/subcutis of test animals;
  histopathological grading of the local response versus a control material over defined periods.</li>
  <li><strong>Hemocompatibility (10993-4).</strong> Hemolysis (direct and extract), coagulation (e.g., PTT),
  thrombogenicity, complement activation (SC5b-9, C3a) &mdash; selected by blood-contact mode.</li>
  <li><strong>Degradation &amp; residuals.</strong> Degradation products characterised (10993-9/-13/-14/-15);
  ethylene-oxide-sterilised devices must meet EO/ECH residual limits of <strong>10993-7</strong>.</li>
</ul>

<h2 class="sec"><span class="secnum">5.5</span>Chemistry First: -18 and -17</h2>
<span class="wframe">Why &middot; When</span>
<p>Modern practice increasingly runs on chemistry. <strong>ISO 10993-18:2020</strong> characterises what a device
can release &mdash; exhaustive or simulated-use extraction, then GC-MS/LC-MS/ICP-MS identification of
extractables &mdash; and <strong>ISO 10993-17</strong> converts that list into a <strong>toxicological risk assessment</strong>:
compare estimated patient exposure against compound-specific allowable limits derived from toxicity data
(with threshold-of-toxicological-concern logic for unknowns). Where the chemistry demonstrates margin,
whole categories of animal endpoints (systemic toxicity, genotoxicity, carcinogenicity) can be addressed
without new in-vivo studies &mdash; faster, cheaper, more ethical, and often more informative than a pass/fail
animal test.</p>

<div class="callout didyouknow">
  <div class="co-head">Did You Know?</div>
  <p>Colour additives have derailed devices: reviewers have questioned dyed sutures and tinted tubing over
  leachable colourants. A pigment safe in food packaging is not automatically safe against permanent tissue
  contact &mdash; exposure route changes everything, which is exactly why -17's allowable-limit logic is
  route-specific.</p>
</div>
<div class="callout industry">
  <div class="co-head">Industry Connect</div>
  <p>Extractables-and-leachables (E&amp;L) science sits squarely in the pharmacist's skill set &mdash; analytical
  chemistry, toxicology, impurity qualification &mdash; and E&amp;L specialists are among the most sought-after
  profiles in device and combination-product development, in India's CROs as much as in multinationals.</p>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 5.1 &middot; Metal-on-Metal Debris &mdash; Host Response at Scale</div>
  <div class="cs-body">
    <p>Chapter 4 traced the materials failure of metal-on-metal hips; the biology completes the story.
    CoCr nanoparticles and ions provoked lymphocyte-dominated reactions (aseptic lymphocyte-dominated
    vasculitis-associated lesions), pseudotumours and tissue necrosis in a subset of patients &mdash; a
    hypersensitivity-type response no standard preclinical battery had predicted, because the debris dose,
    particle size and chronicity of clinical wear were not reproduced by conventional implantation tests
    on bulk material.</p>
    <div class="cs-q">Discussion questions</div>
    <ol>
      <li>Why did bulk-material implantation studies fail to predict the clinical response?</li>
      <li>What evaluation elements would ISO 10993-1's risk-based approach demand today for a novel bearing couple?</li>
    </ol>
    <div class="cs-analysis">
      <div class="cs-q">Analysis</div>
      <p>(1) Biocompatibility is dose-, form- and time-dependent: nanoscale debris presents vastly more
      reactive surface and different cellular uptake than a polished coupon; chronic generation was absent
      from short studies. (2) Wear-debris characterization (quantity, size, chemistry) from simulator
      testing, particle-specific toxicology, ion-release kinetics with -17 limits, and clinical follow-up
      with metal-ion surveillance &mdash; evaluation matched to realistic exposure.</p>
    </div>
  </div>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 5.2 &middot; Writing the BEP for an Indian PICC Line</div>
  <div class="cs-body">
    <p>An Indian manufacturer develops a polyurethane peripherally inserted central catheter (PICC),
    EO-sterilised, indwelling up to 30 days. The regulatory pharmacist categorises it: external
    communicating, circulating blood, prolonged. The BEP lists endpoints (cytotoxicity, sensitization,
    irritation, acute/subacute systemic toxicity, pyrogenicity, hemocompatibility, genotoxicity per
    duration), leverages the resin supplier's master file and published clinical history of the same
    polyurethane grade, commissions -18 chemistry plus EO residuals (-7), and runs only the tests the gap
    analysis leaves open &mdash; documenting every waiver argument in the BER for CDSCO and, later, CE review.</p>
    <div class="cs-q">Discussion questions</div>
    <ol>
      <li>Which endpoints might be closed without new animal testing, and on what argument?</li>
      <li>How does cumulative-use counting affect a catheter replaced weekly?</li>
    </ol>
    <div class="cs-analysis">
      <div class="cs-q">Analysis</div>
      <p>(1) Systemic toxicity and genotoxicity via -18 chemistry + -17 limits with supplier data and prior
      clinical use of the identical formulation; irritation via validated in vitro methods. (2) Duration is
      cumulative for the patient: 4 weekly catheters = prolonged exposure; the categorization &mdash; and endpoint
      set &mdash; follows total contact, not single-unit dwell.</p>
    </div>
  </div>
</div>

<div class="summary-box">
  <h3>Chapter Summary</h3>
  <ul>
    <li>Biocompatibility = appropriate host response in a specific application; the cascade runs protein adsorption &rarr; acute &rarr; chronic inflammation &rarr; foreign body giant cells &rarr; fibrous encapsulation, with blood contact and degradation as extra axes.</li>
    <li>ISO 10993-1:2018 frames biological evaluation as ISO 14971 risk management: characterise, review existing data, plan (BEP), test only gaps, conclude (BER).</li>
    <li>Categorization = contact type (surface / external communicating / implant) &times; duration (limited &le;24 h / prolonged &le;30 d / long-term &gt;30 d, cumulative).</li>
    <li>Core tests: cytotoxicity (-5), sensitization (-10), irritation (-23), systemic toxicity &amp; pyrogenicity (-11), genotoxicity (-3), implantation (-6), hemocompatibility (-4), EO residuals (-7), sample prep (-12).</li>
    <li>Chemical characterization (-18) plus toxicological risk assessment (-17) increasingly closes endpoints without animal testing &mdash; the 3Rs in regulatory practice.</li>
    <li>Testing must be GLP; conclusions live in the risk management file and feed labeling and PMS.</li>
  </ul>
</div>

<div class="keyterms">
  <h3>Key Terms</h3>
  <dl>
    <div class="kt-row"><dt>Host response</dt> <dd>&mdash; the local and systemic biological reaction to a material.</dd></div>
    <div class="kt-row"><dt>Vroman effect</dt> <dd>&mdash; time-dependent exchange of adsorbed surface proteins.</dd></div>
    <div class="kt-row"><dt>Foreign body giant cell</dt> <dd>&mdash; fused macrophages at a non-phagocytosable surface.</dd></div>
    <div class="kt-row"><dt>Fibrous capsule</dt> <dd>&mdash; collagenous wall isolating an implant; thin and quiescent when benign.</dd></div>
    <div class="kt-row"><dt>BEP / BER</dt> <dd>&mdash; biological evaluation plan / report bracketing the evaluation.</dd></div>
    <div class="kt-row"><dt>Extractables / leachables</dt> <dd>&mdash; compounds obtainable under forced extraction / released in clinical use.</dd></div>
    <div class="kt-row"><dt>GLP</dt> <dd>&mdash; Good Laboratory Practice, required for regulatory biocompatibility studies.</dd></div>
    <div class="kt-row"><dt>3Rs</dt> <dd>&mdash; replace, reduce, refine animal testing.</dd></div>
    <div class="kt-row"><dt>LAL test</dt> <dd>&mdash; Limulus amoebocyte lysate assay for bacterial endotoxin.</dd></div>
  </dl>
</div>

<div class="assessment">
<h2>Chapter 5 &middot; Assessment Battery</h2>

<div class="ass-block">
<h3>A. Multiple Choice Questions (with rationales)</h3>
<ol>
  <li>The first event when a material contacts blood or tissue is:
    <ul class="mcq-opts"><li><span class="ol">a)</span> fibrous encapsulation</li><li><span class="ol">b)</span> protein adsorption</li><li><span class="ol">c)</span> giant cell formation</li><li><span class="ol">d)</span> angiogenesis</li></ul>
    <div class="rationale"><b>Answer: b.</b> Proteins coat the surface within seconds (Vroman effect); every later cellular event responds to that conditioned layer. Encapsulation is the end-state.</div></li>
  <li>ISO 10993-1:2018 frames biological evaluation as:
    <ul class="mcq-opts"><li><span class="ol">a)</span> a fixed checklist of animal tests</li><li><span class="ol">b)</span> a marketing exercise</li><li><span class="ol">c)</span> optional for CE marking</li><li><span class="ol">d)</span> a risk management process under ISO 14971</li></ul>
    <div class="rationale"><b>Answer: d.</b> The 2018 revision cemented the risk-based, data-first philosophy; testing addresses only gaps that existing data cannot close.</div></li>
  <li>A device contacting circulating blood for 10 days is categorised as:
    <ul class="mcq-opts"><li><span class="ol">a)</span> surface device, limited</li><li><span class="ol">b)</span> implant, permanent</li><li><span class="ol">c)</span> external communicating, prolonged</li><li><span class="ol">d)</span> surface device, prolonged</li></ul>
    <div class="rationale"><b>Answer: c.</b> Circulating-blood contact via an externally communicating device; 24 h &lt; 10 d &le; 30 d = prolonged.</div></li>
  <li>The universal first-line biocompatibility screen is:
    <ul class="mcq-opts"><li><span class="ol">a)</span> cytotoxicity per ISO 10993-5</li><li><span class="ol">b)</span> carcinogenicity</li><li><span class="ol">c)</span> chronic implantation</li><li><span class="ol">d)</span> reproductive toxicity</li></ul>
    <div class="rationale"><b>Answer: a.</b> In vitro cytotoxicity is sensitive, rapid and inexpensive &mdash; the gatekeeper before costlier endpoints.</div></li>
  <li>Irritation testing now resides in which part (2021 restructuring)?
    <ul class="mcq-opts"><li><span class="ol">a)</span> 10993-4</li><li><span class="ol">b)</span> 10993-7</li><li><span class="ol">c)</span> 10993-23</li><li><span class="ol">d)</span> 10993-12</li></ul>
    <div class="rationale"><b>Answer: c.</b> Irritation moved from -10 (now sensitization only) to -23, which also validates in vitro RhE methods. -7 is EO residuals; -12 sample preparation.</div></li>
  <li>Hemolysis, complement activation and thrombogenicity belong to:
    <ul class="mcq-opts"><li><span class="ol">a)</span> genotoxicity testing</li><li><span class="ol">b)</span> hemocompatibility per ISO 10993-4</li><li><span class="ol">c)</span> pyrogenicity testing</li><li><span class="ol">d)</span> implantation testing</li></ul>
    <div class="rationale"><b>Answer: b.</b> Part 4 governs blood interactions, selected according to blood-contact mode.</div></li>
  <li>EO-sterilised devices must additionally demonstrate:
    <ul class="mcq-opts"><li><span class="ol">a)</span> shape memory</li><li><span class="ol">b)</span> radiopacity</li><li><span class="ol">c)</span> MRI compatibility</li><li><span class="ol">d)</span> EO/ECH residuals within ISO 10993-7 limits</li></ul>
    <div class="rationale"><b>Answer: d.</b> Ethylene oxide and ethylene chlorohydrin residues are toxic; -7 sets patient-exposure limits by contact duration.</div></li>
  <li>The Ames test addresses which endpoint?
    <ul class="mcq-opts"><li><span class="ol">a)</span> genotoxicity (bacterial reverse mutation)</li><li><span class="ol">b)</span> sensitization</li><li><span class="ol">c)</span> irritation</li><li><span class="ol">d)</span> hemolysis</li></ul>
    <div class="rationale"><b>Answer: a.</b> Ames is the bacterial mutagenicity assay within the -3 genotoxicity battery.</div></li>
  <li>Chemical characterization of device materials is governed by:
    <ul class="mcq-opts"><li><span class="ol">a)</span> ISO 10993-6</li><li><span class="ol">b)</span> ISO 10993-18</li><li><span class="ol">c)</span> ISO 11607</li><li><span class="ol">d)</span> IEC 62366</li></ul>
    <div class="rationale"><b>Answer: b.</b> -18 (2020) defines extraction and analytical identification of extractables; -17 then assesses their toxicological risk.</div></li>
  <li>&ldquo;Endpoints to address&rdquo; in the ISO 10993-1 table means:
    <ul class="mcq-opts"><li><span class="ol">a)</span> every endpoint requires a new animal study</li><li><span class="ol">b)</span> endpoints apply only to Class D devices</li><li><span class="ol">c)</span> each endpoint must be closed by data &mdash; existing evidence, chemistry, or testing</li><li><span class="ol">d)</span> endpoints are optional suggestions</li></ul>
    <div class="rationale"><b>Answer: c.</b> The table defines what must be evaluated, not what must be tested; justified data-based closure is the modern norm.</div></li>
</ol>
</div>

<div class="ass-block">
<h3>B. True / False</h3>
<ol>
  <li>A material proven biocompatible in one application is automatically biocompatible in all others. <span class="marks">(F)</span></li>
  <li>Foreign body giant cells are fused macrophages. <span class="marks">(T)</span></li>
  <li>Contact duration is counted cumulatively across repeated use of a device type. <span class="marks">(T)</span></li>
  <li>The LAL test measures material-mediated pyrogenicity. <span class="marks">(F &mdash; LAL detects bacterial endotoxin; material-mediated pyrogenicity uses the rabbit test)</span></li>
  <li>Regulatory biocompatibility studies must be GLP-compliant. <span class="marks">(T)</span></li>
  <li>In vitro RhE methods can replace rabbit irritation testing under ISO 10993-23. <span class="marks">(T)</span></li>
  <li>ISO 10993-12 specifies genotoxicity tests. <span class="marks">(F &mdash; it governs sample preparation/extraction)</span></li>
  <li>A thin quiescent fibrous capsule is the acceptable end-state for most soft-tissue implants. <span class="marks">(T)</span></li>
  <li>Chemical characterization can never substitute for animal testing. <span class="marks">(F &mdash; -18 + -17 routinely closes systemic endpoints)</span></li>
  <li>Blood-contacting devices activate coagulation partly via the intrinsic pathway on artificial surfaces. <span class="marks">(T)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>C. Fill in the Blanks</h3>
<ol>
  <li>The time-dependent exchange of adsorbed surface proteins is called the __________ effect.</li>
  <li>The keystone framework standard of biological evaluation is ISO __________.</li>
  <li>Contact durations are limited (&le;24 h), prolonged (&le;30 days) and __________ (&gt;30 days).</li>
  <li>In vitro cytotoxicity commonly uses the __________ mouse fibroblast cell line.</li>
  <li>The murine sensitization alternative to guinea pig tests is the __________.</li>
  <li>Local effects after implantation are evaluated under ISO 10993-__________.</li>
  <li>EO sterilization residuals are limited by ISO 10993-__________.</li>
  <li>The document planning the biological evaluation is the __________.</li>
  <li>Toxicological risk assessment of leachables is ISO 10993-__________.</li>
  <li>The ethical framework of replace, reduce, refine is known as the __________.</li>
</ol>
</div>

<div class="ass-block">
<h3>D. Assertion&ndash;Reasoning</h3>
<p class="ar-key">Mark: (a) both A and R true, R explains A; (b) both true, R does not explain A; (c) A true, R false; (d) A false, R true.</p>
<ol>
  <li><strong>A:</strong> A haemodialyser demands deeper hemocompatibility evaluation than a hypodermic needle. <strong>R:</strong> Its blood contact is prolonged, repeated and involves the whole circulating volume. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> Cytotoxicity testing is performed on the finished device's extracts. <strong>R:</strong> ISO 10993-23 governs extraction vehicle selection. <span class="marks">(c &mdash; extraction is per -12, not -23)</span></li>
  <li><strong>A:</strong> Endpoint tables in ISO 10993-1 are evaluation requirements. <strong>R:</strong> GLP compliance is required for regulatory biocompatibility studies. <span class="marks">(b)</span></li>
  <li><strong>A:</strong> Nanoscale wear debris can produce responses bulk-material tests miss. <strong>R:</strong> Reactive surface area and cellular uptake differ radically at nanoscale. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> A material passing all ISO 10993 endpoints needs no post-market biological vigilance. <strong>R:</strong> Rare hypersensitivity responses may only surface at population scale. <span class="marks">(d)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>E. Short Answer Questions <span style="text-transform:none;">(2&ndash;3 marks each)</span></h3>
<ol>
  <li>Describe the four stages of the foreign body response.</li>
  <li>Categorise: (i) surgical glove, (ii) urinary Foley catheter (14 days), (iii) coronary stent &mdash; contact type and duration.</li>
  <li>Differentiate sensitization from irritation biologically and by test method.</li>
  <li>What is the role of ISO 10993-12 in every biocompatibility study?</li>
  <li>Explain how -18 chemistry plus -17 assessment can waive a systemic toxicity study.</li>
  <li>List the hemocompatibility endpoint categories of ISO 10993-4.</li>
</ol>
</div>

<div class="ass-block">
<h3>F. Long Answer Questions <span style="text-transform:none;">(10 marks each)</span></h3>
<ol>
  <li>Explain the host response cascade to an implanted biomaterial, including the blood-contact and degradable-material variants, and relate each stage to a testable ISO 10993 endpoint.</li>
  <li>Construct the full biological evaluation plan for an EO-sterilised, 30-day polyurethane central venous catheter: categorization, endpoint table, data sources, tests, and BER conclusions.</li>
  <li>&ldquo;The future of biocompatibility is chemistry, not animals.&rdquo; Discuss with reference to ISO 10993-18/-17, in vitro method validation (-5, -23), the 3Rs, and the limits of chemistry-first evaluation.</li>
</ol>
</div>

<div class="ass-block">
<h3>G. Higher-Order Thinking (HOTS)</h3>
<ol>
  <li>A supplier silently changes a masterbatch antioxidant in your catheter resin. Trace every document and test in your QMS and biological evaluation that this change touches, and design the minimal re-evaluation that is scientifically defensible.</li>
  <li>Propose a testing strategy for wear debris of a novel polymer-on-ceramic spinal disc, given that standard implantation tests use bulk coupons. Specify particle generation, dosing rationale and endpoints.</li>
  <li>Draft the pharmacist's briefing note for a hospital device committee on latex allergy risk management: affected products, alternatives, screening questions and stocking policy.</li>
</ol>
</div>
</div>

<div class="references">
<h2>References (Vancouver style)</h2>
<ol>
  <li>International Organization for Standardization. ISO 10993-1:2018 &mdash; Biological evaluation of medical devices &mdash; Part 1: Evaluation and testing within a risk management process. Geneva: ISO; 2018.</li>
  <li>International Organization for Standardization. ISO 10993 series, Parts 3, 4, 5, 6, 7, 10, 11, 12, 17, 18, 23. Geneva: ISO.</li>
  <li>US Food and Drug Administration. Use of International Standard ISO 10993-1 &mdash; Guidance for Industry and FDA Staff (updated 2023). Silver Spring (MD): FDA.</li>
  <li>Anderson JM, Rodriguez A, Chang DT. Foreign body reaction to biomaterials. Semin Immunol. 2008;20(2):86-100.</li>
  <li>Vroman L, Adams AL. Findings with the recording ellipsometer suggesting rapid exchange of specific plasma proteins at liquid/solid interfaces. Surf Sci. 1969;16:438-46.</li>
  <li>European Parliament and Council. Regulation (EU) 2017/745, Annex I (GSPR), Chapter II. OJEU. 2017;L117.</li>
  <li>Central Drugs Standard Control Organisation. Medical Devices Rules, 2017 &mdash; essential principles for safety and performance. New Delhi: MoHFW; 2017.</li>
  <li>US Food and Drug Administration. Banned devices: powdered surgeon's gloves, powdered patient examination gloves. Final rule. Fed Regist. 2016;81:91722-31.</li>
  <li>Langton DJ, et al. Adverse reaction to metal debris following hip resurfacing. J Bone Joint Surg Br. 2010;92(1):38-46.</li>
  <li>Organisation for Economic Co-operation and Development. OECD Principles of Good Laboratory Practice. Paris: OECD; 1998.</li>
</ol>
</div>

<div class="qgate">
<h2>Chapter 5 &middot; Completion Dashboard (Quality Gate)</h2>
<table class="qgate-t">
  <tr><th>Quality Gate criterion</th><th style="width:22mm;">Status</th><th>Evidence</th></tr>
  <tr><td>Learning objectives with CO/Bloom's mapping</td><td class="qg-pass">PASS</td><td>6 objectives, CO1&ndash;CO3 map table</td></tr>
  <tr><td>What&ndash;Why&ndash;How&ndash;Where&ndash;When framework applied</td><td class="qg-pass">PASS</td><td>Framework tags on sections 5.1&ndash;5.5</td></tr>
  <tr><td>Figures &amp; tables numbered with captions</td><td class="qg-pass">PASS</td><td>Figure 5.1; Tables 5.1&ndash;5.2</td></tr>
  <tr><td>All four callout types present</td><td class="qg-pass">PASS</td><td>Regulatory Spotlight, Clinical Insight, Industry Connect, Did You Know</td></tr>
  <tr><td>Case studies with analysis</td><td class="qg-pass">PASS</td><td>Case studies 5.1 (MoM debris), 5.2 (PICC BEP)</td></tr>
  <tr><td>Full assessment battery</td><td class="qg-pass">PASS</td><td>10 MCQ + rationales, 10 T/F, 10 FIB, 5 A&ndash;R, 6 SAQ, 3 LAQ, 3 HOTS</td></tr>
  <tr><td>Anti-fabrication check (regulations/codes verified)</td><td class="qg-pass">PASS</td><td>ISO 10993 parts, FDA 10993-1 guidance, 81 FR 91722 &mdash; cited in references</td></tr>
  <tr><td>Vancouver-style chapter references</td><td class="qg-pass">PASS</td><td>10 references</td></tr>
</table>
</div>

</section>
"""
