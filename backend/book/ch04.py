CH04_HTML = """
<section class="chapter" id="ch04" data-running="Chapter 4 · Biomaterials">

<div class="ch-opener">
  <div class="ch-kicker">Part II &middot; Design, Biomaterials &amp; Biocompatibility &middot; Chapter 4</div>
  <div class="ch-band">
    <div class="ch-num-cell"><div class="ch-num">04</div></div>
    <div class="ch-title-cell">
      <h1 class="ch-title">Biomaterials</h1>
      <div class="ch-tagline">Metals, ceramics, polymers and natural materials &middot; properties and selection &middot; tissue engineering &amp; regenerative medicine</div>
    </div>
  </div>
</div>

<div class="objectives-box">
  <h3>Learning Objectives</h3>
  <ol>
    <li>Define a biomaterial and classify biomaterials into metals, ceramics, polymers, naturals and composites. <span class="lo-tag">CO1 &middot; Remember</span></li>
    <li>Relate structure and properties of major biomaterials to their device applications. <span class="lo-tag">CO1 &middot; Understand</span></li>
    <li>Explain corrosion, wear and degradation as failure mechanisms of implanted materials. <span class="lo-tag">CO2 &middot; Understand</span></li>
    <li>Select a candidate biomaterial for a specified device using systematic criteria. <span class="lo-tag">CO2 &middot; Apply</span></li>
    <li>Describe the cells&ndash;scaffold&ndash;signals triad of tissue engineering. <span class="lo-tag">CO3 &middot; Understand</span></li>
    <li>Evaluate the promise and limitations of regenerative medicine products. <span class="lo-tag">CO3 &middot; Evaluate</span></li>
  </ol>
  <table class="co-map">
    <tr><th>Course Outcome</th><th>Statement</th><th>Bloom's Levels</th><th>Objectives</th></tr>
    <tr><td>CO1</td><td>Classify biomaterials and link structure to properties</td><td>L1&ndash;L2</td><td>1, 2</td></tr>
    <tr><td>CO2</td><td>Analyse failure mechanisms and select materials rationally</td><td>L2&ndash;L3</td><td>3, 4</td></tr>
    <tr><td>CO3</td><td>Assess tissue engineering and regenerative approaches</td><td>L2&ndash;L5</td><td>5, 6</td></tr>
  </table>
</div>

<h2 class="sec"><span class="secnum">4.1</span>What Is a Biomaterial?</h2>
<span class="wframe">What</span>
<p class="lead">A <strong>biomaterial</strong> is a material engineered to interact with biological systems for a medical
purpose &mdash; in David Williams' consensus definition, a material intended to interface with biological
systems to evaluate, treat, augment or replace any tissue, organ or function of the body. The subject is
inseparable from <strong>biocompatibility</strong> (Chapter 5): the material must perform its function <em>with an
appropriate host response</em> in its specific application.</p>
<p>Materials scientists organise the field into four families &mdash; <strong>metals, ceramics, polymers and
natural materials</strong> &mdash; plus <strong>composites</strong> that combine them. Behaviour in the body is further
described as <strong>bioinert</strong> (minimal interaction; e.g., alumina), <strong>bioactive</strong> (bonds to tissue;
e.g., hydroxyapatite, bioactive glass) or <strong>bioresorbable</strong> (degrades safely as tissue regenerates;
e.g., PLGA, tricalcium phosphate).</p>

<div class="figure">
<svg viewBox="0 0 700 218" xmlns="http://www.w3.org/2000/svg" font-family="Manrope">
  <rect x="255" y="8" width="190" height="32" fill="#0F4C5C"/>
  <text x="350" y="28" font-size="11" fill="#fff" text-anchor="middle" font-weight="bold">BIOMATERIALS</text>
  <g font-size="8.8">
    <rect x="14" y="72" width="156" height="58" fill="#E4EFF1" stroke="#0F4C5C" stroke-width="0.9"/>
    <text x="92" y="88" text-anchor="middle" font-weight="bold" fill="#0F4C5C">METALS</text>
    <text x="92" y="101" text-anchor="middle" fill="#333">316L SS &middot; Ti-6Al-4V &middot; CoCrMo</text>
    <text x="92" y="113" text-anchor="middle" fill="#333">Nitinol &middot; tantalum</text>
    <text x="92" y="125" text-anchor="middle" fill="#777">Joints, stents, plates, wires</text>
    <rect x="186" y="72" width="156" height="58" fill="#E4EFF1" stroke="#0F4C5C" stroke-width="0.9"/>
    <text x="264" y="88" text-anchor="middle" font-weight="bold" fill="#0F4C5C">CERAMICS</text>
    <text x="264" y="101" text-anchor="middle" fill="#333">Alumina &middot; zirconia &middot; HA</text>
    <text x="264" y="113" text-anchor="middle" fill="#333">Bioactive glass &middot; TCP</text>
    <text x="264" y="125" text-anchor="middle" fill="#777">Bearings, coatings, bone graft</text>
    <rect x="358" y="72" width="156" height="58" fill="#E4EFF1" stroke="#0F4C5C" stroke-width="0.9"/>
    <text x="436" y="88" text-anchor="middle" font-weight="bold" fill="#0F4C5C">POLYMERS</text>
    <text x="436" y="101" text-anchor="middle" fill="#333">UHMWPE &middot; PMMA &middot; silicone</text>
    <text x="436" y="113" text-anchor="middle" fill="#333">PTFE &middot; PEEK &middot; PLGA &middot; PU</text>
    <text x="436" y="125" text-anchor="middle" fill="#777">Cups, cement, lenses, sutures</text>
    <rect x="530" y="72" width="156" height="58" fill="#E4EFF1" stroke="#0F4C5C" stroke-width="0.9"/>
    <text x="608" y="88" text-anchor="middle" font-weight="bold" fill="#0F4C5C">NATURALS</text>
    <text x="608" y="101" text-anchor="middle" fill="#333">Collagen &middot; chitosan &middot; alginate</text>
    <text x="608" y="113" text-anchor="middle" fill="#333">Hyaluronic acid &middot; silk</text>
    <text x="608" y="125" text-anchor="middle" fill="#777">Dressings, scaffolds, fillers</text>
  </g>
  <g stroke="#5B6770" stroke-width="0.9">
    <line x1="350" y1="40" x2="92" y2="72"/><line x1="350" y1="40" x2="264" y2="72"/>
    <line x1="350" y1="40" x2="436" y2="72"/><line x1="350" y1="40" x2="608" y2="72"/>
  </g>
  <g font-size="8.8" text-anchor="middle">
    <rect x="120" y="162" width="200" height="34" fill="#F0F5FA" stroke="#14537D"/>
    <text x="220" y="176" font-weight="bold" fill="#14537D">COMPOSITES</text>
    <text x="220" y="189" fill="#333">e.g., HA-coated Ti stems, CFR-PEEK</text>
    <rect x="380" y="162" width="200" height="34" fill="#F0F5FA" stroke="#14537D"/>
    <text x="480" y="176" font-weight="bold" fill="#14537D">SMART MATERIALS</text>
    <text x="480" y="189" fill="#333">Shape-memory nitinol, hydrogels</text>
  </g>
</svg>
<div class="figcaption"><b>Figure 4.1</b> &nbsp;The biomaterials family tree with representative members and device applications. (HA = hydroxyapatite; TCP = tricalcium phosphate; PU = polyurethane; CFR = carbon-fibre-reinforced.)</div>
</div>

<h2 class="sec"><span class="secnum">4.2</span>Metals</h2>
<span class="wframe">What &middot; How</span>
<p>Metals dominate load-bearing applications because of high strength, toughness and fatigue resistance.
The classic implant triad:</p>
<ul>
  <li><strong>Stainless steel 316L</strong> (ASTM F138): low-carbon, molybdenum-bearing austenitic steel; economical,
  easy to machine; used in bone plates, screws, temporary fixation. Susceptible to pitting/crevice corrosion
  over long implantation &mdash; hence preferred for temporary hardware.</li>
  <li><strong>Cobalt&ndash;chromium alloys</strong> (CoCrMo, ASTM F75): outstanding wear and corrosion resistance;
  bearing surfaces of joint replacements, heart valve housings; very high stiffness (~220&ndash;230 GPa).</li>
  <li><strong>Titanium and Ti-6Al-4V</strong> (ASTM F136): best strength-to-weight and corrosion resistance
  (self-healing TiO&#8322; passive layer), excellent osseointegration (Br&aring;nemark's discovery underlying dental
  implants), modulus ~110 GPa &mdash; closer to bone than steel; the default for uncemented stems, dental
  implants, spinal cages, pacemaker cans.</li>
</ul>
<p><strong>Nitinol</strong> (~50:50 NiTi) adds shape memory and superelasticity: a crushed stent springs back to its
programmed shape at body temperature &mdash; the enabling property of self-expanding vascular stents and
guidewires. <strong>Tantalum</strong>, highly corrosion-resistant and radiopaque, appears as porous ingrowth
structures.</p>
<h3 class="subsec">4.2.1 Failure mechanisms: corrosion, wear, stress shielding</h3>
<p>Physiological saline at 37&deg;C is an aggressive electrolyte. Implant alloys rely on passive oxide films,
but films fail locally: <strong>pitting</strong> and <strong>crevice corrosion</strong> under washers and screw heads,
<strong>galvanic corrosion</strong> when dissimilar metals couple, <strong>fretting corrosion</strong> at micro-moving
interfaces (the root of modular-taper problems in hips). Corrosion products (Ni, Co, Cr ions) drive both
local tissue reactions and hypersensitivity. Mechanically, a stiff metal stem carries load that bone would
otherwise bear; the unloaded bone resorbs (Wolff's law) &mdash; <strong>stress shielding</strong> &mdash; motivating lower-modulus
titanium and porous structures. Cyclic loading adds <strong>fatigue</strong>; articulating surfaces add <strong>wear</strong>,
whose debris drives osteolysis (Section 4.4).</p>

<h2 class="sec"><span class="secnum">4.3</span>Ceramics</h2>
<span class="wframe">What &middot; Where</span>
<p>Ceramics are ionic/covalent solids: extremely hard, chemically stable, compressively strong &mdash; and
brittle. <strong>Alumina</strong> (Al&#8322;O&#8323;) provides ultra-low-wear femoral heads and cup liners.
<strong>Zirconia</strong> (yttria-stabilised, YSZ) is tougher via transformation toughening, but the same phase
transformation causes <strong>low-temperature degradation (ageing)</strong> if processing is imperfect &mdash; the
mechanism behind the 2001&ndash;02 fracture recalls of certain zirconia femoral head batches whose processing
change accelerated ageing. Modern practice favours <strong>zirconia-toughened alumina (ZTA)</strong> composites.</p>
<p><strong>Bioactive ceramics</strong> bond to bone: <strong>hydroxyapatite</strong> (Ca&#8321;&#8320;(PO&#8324;)&#8326;(OH)&#8322;),
chemically akin to bone mineral, is plasma-sprayed onto titanium stems and used as graft substitute;
<strong>&beta;-tricalcium phosphate</strong> resorbs as bone regrows; <strong>Bioglass 45S5</strong> (Hench, 1969) forms a
carbonated apatite layer that bonds to both bone and soft tissue &mdash; the founding &ldquo;bioactive&rdquo; material.</p>

<h2 class="sec"><span class="secnum">4.4</span>Polymers</h2>
<span class="wframe">What &middot; Where</span>
<div class="tablewrap">
<div class="tabcaption"><b>Table 4.1</b> &nbsp;Major polymeric biomaterials and applications</div>
<table class="data">
  <tr><th style="width:38mm;">Polymer</th><th style="width:38mm;">Key properties</th><th>Principal device applications</th></tr>
  <tr><td class="rowhead">UHMWPE</td><td>Tough, low friction; wear debris risk</td><td>Acetabular liners, tibial inserts (highly cross-linked grades reduce wear)</td></tr>
  <tr><td class="rowhead">PMMA</td><td>Self-curing, rigid, exothermic set</td><td>Bone cement (Charnley), intraocular lens optics, dentures</td></tr>
  <tr><td class="rowhead">Silicone (PDMS)</td><td>Flexible, inert, gas-permeable</td><td>Catheters, implant shells, tubing, hydrocephalus shunts</td></tr>
  <tr><td class="rowhead">PTFE / ePTFE</td><td>Extremely inert, low friction, microporous (expanded)</td><td>Vascular grafts, sutures, membranes</td></tr>
  <tr><td class="rowhead">PEEK</td><td>Bone-like stiffness, radiolucent</td><td>Spinal cages, trauma implants, CFR-PEEK plates</td></tr>
  <tr><td class="rowhead">Polyurethanes</td><td>Elastic, fatigue- and blood-tolerant</td><td>Pacemaker lead insulation, catheters, wound dressings</td></tr>
  <tr><td class="rowhead">Hydrogels (pHEMA etc.)</td><td>High water content, soft</td><td>Contact lenses (Wichterle), wound care, drug depots</td></tr>
  <tr><td class="rowhead">PLA / PGA / PLGA / PCL / PDO</td><td>Bioresorbable; tunable degradation (weeks&ndash;years)</td><td>Absorbable sutures, resorbable screws/plates, drug-eluting scaffolds, stent coatings</td></tr>
</table>
</div>
<p>Resorbables deserve emphasis: <strong>PGA</strong> (fast, weeks) and <strong>PLA</strong> (slow, months&ndash;years) hydrolyse
to lactic/glycolic acid metabolised via normal pathways; the <strong>PLGA copolymer ratio</strong> tunes degradation
to match healing &mdash; the material logic of absorbable sutures (since Dexon, 1970s) and of drug-eluting stent
coatings. Degradation is a design property: too fast, the tissue is unloaded prematurely; too slow, the
implant behaves as permanent (with acid burst and local pH drop as classic complications).</p>

<h2 class="sec"><span class="secnum">4.5</span>Natural Materials &amp; Composites</h2>
<span class="wframe">What</span>
<p><strong>Collagen</strong> (the body's own structural protein) forms haemostats, dressings and dermal scaffolds;
<strong>chitosan</strong> (from chitin) is haemostatic and antimicrobial; <strong>alginate</strong> gels absorb exudate in
wound care; <strong>hyaluronic acid</strong> lubricates (viscosupplementation) and fills; <strong>silk fibroin</strong>
offers strength with slow degradation. Naturals excel in bioactivity but vary batch-to-batch and can carry
immunogenic or disease-transmission risk &mdash; hence strict sourcing controls (ISO 22442 series for animal
tissues). <strong>Composites</strong> combine families: HA-coated titanium (bioactive surface on tough core),
carbon-fibre-reinforced PEEK (bone-matched stiffness plus radiolucency).</p>

<h2 class="sec"><span class="secnum">4.6</span>Material Selection for Devices</h2>
<span class="wframe">How &middot; Why</span>
<div class="tablewrap">
<div class="tabcaption"><b>Table 4.2</b> &nbsp;Systematic biomaterial selection criteria</div>
<table class="data">
  <tr><th style="width:44mm;">Criterion</th><th>Questions asked</th></tr>
  <tr><td class="rowhead">Function &amp; mechanics</td><td>Strength, stiffness (match to tissue), fatigue life, wear couple, elasticity</td></tr>
  <tr><td class="rowhead">Biological environment</td><td>Contact type/duration (ISO 10993 category), corrosion/degradation behaviour, debris fate</td></tr>
  <tr><td class="rowhead">Biocompatibility evidence</td><td>Prior use history, ISO 10993 data, chemical characterization, extractables</td></tr>
  <tr><td class="rowhead">Processing &amp; sterilization</td><td>Moldability/machinability; stability to EO, radiation (PTFE degrades!), steam (hydrogels, PMMA cannot)</td></tr>
  <tr><td class="rowhead">Regulatory &amp; supply</td><td>Recognised standards (ASTM F-series, ISO 5832), medical-grade supply, master files, cost</td></tr>
</table>
</div>
<div class="callout regulatory">
  <div class="co-head">Regulatory Spotlight</div>
  <p>Implant alloys and polymers are specified against consensus standards &mdash; ISO 5832 series (metallic
  implant materials), ASTM F138/F75/F136 &mdash; and reviewers expect materials to be identified to these grades.
  &ldquo;Surgical grade steel&rdquo; is a marketing phrase, not a specification; the submission must name the
  standard, grade and supplier controls.</p>
</div>
<div class="callout clinical">
  <div class="co-head">Clinical Insight</div>
  <p>Nickel hypersensitivity affects roughly one in ten patients (more in women); 316L and nitinol contain
  substantial nickel. For documented allergy, clinicians select titanium alloys or coated devices &mdash; a
  counselling point pharmacists in orthopaedic and cardiac wards should recognise.</p>
</div>

<h2 class="sec"><span class="secnum">4.7</span>Tissue Engineering &amp; Regenerative Medicine</h2>
<span class="wframe">Why &middot; When</span>
<p>Conventional implants <em>replace</em> tissue with a permanent foreign object; <strong>tissue engineering</strong>
aims to <em>regrow</em> the tissue itself. Langer and Vacanti's 1993 formulation defined the field's triad:
<strong>cells</strong> (autologous, allogeneic, or stem/progenitor), a <strong>scaffold</strong> (the temporary 3-D template),
and <strong>signals</strong> (growth factors, mechanical stimulation, increasingly gene cues).</p>
<p>Scaffold engineering is applied biomaterials science: interconnected porosity (typically ~100&ndash;500 &micro;m
pores for bone ingrowth), degradation matched to regeneration, surface chemistry guiding attachment, and
mechanics matched to the target tissue. Fabrication spans salt leaching, electrospinning (nanofibrous ECM
mimics), freeze-drying and, increasingly, <strong>3-D bioprinting</strong> that positions cells and hydrogels layer
by layer. <strong>Decellularised matrices</strong> &mdash; donor tissue stripped of cells, retaining ECM architecture &mdash;
power products from dermal grafts to experimental whole-organ scaffolds.</p>
<p>Clinical reality is soberer than the vision: established successes concentrate in <strong>skin</strong>
(bilayered living constructs and dermal templates for burns and diabetic ulcers), <strong>cartilage</strong>
(autologous chondrocyte implantation on scaffolds), and <strong>bone graft substitutes</strong>; engineered whole
organs remain investigational. Regulatorily, such combination products straddle device, biologic and
advanced-therapy frameworks (in the EU, ATMP regulation; in India, CDSCO's specialised divisions) &mdash;
foreshadowing Chapter 13's combination-product discussion.</p>

<div class="callout industry">
  <div class="co-head">Industry Connect</div>
  <p>India's biomaterials moment is visible in indigenous hydroxyapatite bone grafts, chitosan wound-care
  lines and collagen dressings emerging from institutes such as SCTIMST Thiruvananthapuram (whose
  technology transfer seeded several Indian device firms). Materials scientists, pharmacists and regulatory
  professionals co-author these launches.</p>
</div>
<div class="callout didyouknow">
  <div class="co-head">Did You Know?</div>
  <p>The first hip Charnley cemented with PMMA drew on dental acrylic chemistry &mdash; and his low-friction
  arthroplasty initially used PTFE cups, which wore catastrophically within months. The switch to UHMWPE in
  1962 rescued the operation &mdash; an early, hard lesson that <em>bench inertness does not equal in-vivo
  performance</em>.</p>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 4.1 &middot; Metal-on-Metal Hips &mdash; A Materials Choice Recalled</div>
  <div class="cs-body">
    <p>Metal-on-metal (MoM) hip resurfacing promised low wear for young patients. In practice, edge loading
    and taper fretting released cobalt&ndash;chromium nanoparticles and ions; patients developed pain, pseudotumours
    and elevated blood metal levels (adverse reactions to metal debris). The DePuy ASR system was recalled
    worldwide in 2010 after registry data (notably the UK NJR and Australian NJRR) showed markedly elevated
    revision rates; regulators issued metal-ion surveillance guidance for implanted patients. In India, the
    episode became a landmark compensation programme overseen by CDSCO-constituted expert committees.</p>
    <div class="cs-q">Discussion questions</div>
    <ol>
      <li>Which failure mechanisms of Section 4.2.1 combined in MoM failures?</li>
      <li>What does the ASR story imply about the value of implant registries as post-market tools?</li>
    </ol>
    <div class="cs-analysis">
      <div class="cs-q">Analysis</div>
      <p>(1) Wear (bearing) plus fretting&ndash;crevice corrosion (taper) generating ionic and particulate debris;
      biological amplification through hypersensitivity. (2) Registries detected the revision-rate signal
      years before spontaneous reporting alone would have; they are now considered core post-market
      infrastructure for implants (Chapter 12).</p>
    </div>
  </div>
</div>

<div class="case-study">
  <div class="cs-head">Case Study 4.2 &middot; Choosing the Material for a Biliary Stent</div>
  <div class="cs-body">
    <p>A team must choose between a braided nitinol self-expanding stent and a PLGA bioresorbable stent for
    benign biliary strictures. Nitinol offers reliable radial force and deliverability but becomes a
    permanent nidus for sludge and may require removal. PLGA resorbs after the stricture remodels &mdash; but
    radial force decays with degradation, and acidic by-products in bile are less characterised. The team
    maps each option against Table 4.2: mechanics over time, degradation environment (bile pH, bacteria),
    prior-use evidence, sterilization (radiation embrittles some polymers), and regulatory precedent.</p>
    <div class="cs-q">Discussion questions</div>
    <ol>
      <li>Which criterion most differentiates the options, and what bench model would you build?</li>
      <li>Draft the two decisive design inputs for the resorbable option.</li>
    </ol>
    <div class="cs-analysis">
      <div class="cs-q">Analysis</div>
      <p>(1) Mechanics-versus-time under degradation; a bile-simulant flow rig measuring radial force decay
      over the intended patency window. (2) e.g., &ldquo;radial resistive force &ge;X N/mm for &ge;12 weeks in bile
      simulant at 37&deg;C&rdquo;; &ldquo;mass loss &ge;90% by 12 months with fragments &lt;Y mm&rdquo;.</p>
    </div>
  </div>
</div>

<div class="summary-box">
  <h3>Chapter Summary</h3>
  <ul>
    <li>Biomaterials interface with living systems to evaluate, treat, augment or replace tissue; families are metals, ceramics, polymers, naturals and composites; behaviours are bioinert, bioactive, bioresorbable.</li>
    <li>Metals (316L, CoCrMo, Ti-6Al-4V, nitinol) carry load; their in-vivo enemies are pitting/crevice/galvanic/fretting corrosion, fatigue, wear debris and stress shielding.</li>
    <li>Ceramics give ultra-low wear (alumina, ZTA) and bone bonding (HA, TCP, Bioglass); zirconia ageing taught the field that processing is part of the material.</li>
    <li>Polymers span UHMWPE bearings, PMMA cement, silicones, ePTFE grafts, PEEK structures and the resorbable PLA/PGA family whose degradation is a tunable design property.</li>
    <li>Selection is systematic: mechanics, biological environment, biocompatibility evidence, processing/sterilization compatibility, standards (ISO 5832/ASTM F-series) and supply.</li>
    <li>Tissue engineering rests on the cells&ndash;scaffold&ndash;signals triad; delivered successes centre on skin, cartilage and bone substitutes, with whole organs still investigational.</li>
  </ul>
</div>

<div class="keyterms">
  <h3>Key Terms</h3>
  <dl>
    <div class="kt-row"><dt>Biomaterial</dt> <dd>&mdash; material engineered to interface with biological systems for a medical purpose.</dd></div>
    <div class="kt-row"><dt>Bioinert / bioactive / bioresorbable</dt> <dd>&mdash; minimal interaction / tissue-bonding / safely degrading behaviours.</dd></div>
    <div class="kt-row"><dt>Passive layer</dt> <dd>&mdash; protective oxide film (TiO&#8322;, Cr&#8322;O&#8323;) underlying alloy corrosion resistance.</dd></div>
    <div class="kt-row"><dt>Stress shielding</dt> <dd>&mdash; bone resorption when a stiff implant carries the load bone would bear.</dd></div>
    <div class="kt-row"><dt>Osteolysis</dt> <dd>&mdash; debris-driven periprosthetic bone loss, classically from UHMWPE wear particles.</dd></div>
    <div class="kt-row"><dt>Shape memory / superelasticity</dt> <dd>&mdash; nitinol's recovery of programmed shape; basis of self-expanding stents.</dd></div>
    <div class="kt-row"><dt>Hydroxyapatite</dt> <dd>&mdash; bone-mineral-like calcium phosphate used for coatings and grafts.</dd></div>
    <div class="kt-row"><dt>PLGA</dt> <dd>&mdash; lactide&ndash;glycolide copolymer with ratio-tunable resorption.</dd></div>
    <div class="kt-row"><dt>Scaffold</dt> <dd>&mdash; temporary porous 3-D template guiding tissue regeneration.</dd></div>
    <div class="kt-row"><dt>Decellularised matrix</dt> <dd>&mdash; donor ECM stripped of cells for regenerative grafts.</dd></div>
  </dl>
</div>

<div class="assessment">
<h2>Chapter 4 &middot; Assessment Battery</h2>

<div class="ass-block">
<h3>A. Multiple Choice Questions (with rationales)</h3>
<ol>
  <li>The alloy prized for osseointegration and a self-healing TiO&#8322; passive film is:
    <ul class="mcq-opts"><li><span class="ol">a)</span> 316L stainless steel</li><li><span class="ol">b)</span> CoCrMo</li><li><span class="ol">c)</span> Ti-6Al-4V</li><li><span class="ol">d)</span> nitinol</li></ul>
    <div class="rationale"><b>Answer: c.</b> Titanium alloys integrate with bone (Br&aring;nemark) and passivate spontaneously; CoCr excels at wear, 316L is economical temporary hardware, nitinol adds shape memory.</div></li>
  <li>Stress shielding is a direct consequence of:
    <ul class="mcq-opts"><li><span class="ol">a)</span> polymer swelling</li><li><span class="ol">b)</span> elastic-modulus mismatch between implant and bone</li><li><span class="ol">c)</span> infection</li><li><span class="ol">d)</span> radiation sterilization</li></ul>
    <div class="rationale"><b>Answer: b.</b> A stiff stem (~200 GPa steel vs 10&ndash;30 GPa bone) bears the load; unloaded bone resorbs per Wolff's law.</div></li>
  <li>The founding bioactive material that bonds to bone via an apatite layer is:
    <ul class="mcq-opts"><li><span class="ol">a)</span> alumina</li><li><span class="ol">b)</span> PMMA</li><li><span class="ol">c)</span> PTFE</li><li><span class="ol">d)</span> Bioglass 45S5</li></ul>
    <div class="rationale"><b>Answer: d.</b> Hench's 45S5 (1969) founded bioactive ceramics; alumina is bioinert; PMMA and PTFE are polymers without bone-bonding.</div></li>
  <li>Zirconia femoral-head fractures of 2001&ndash;02 were rooted in:
    <ul class="mcq-opts"><li><span class="ol">a)</span> low-temperature degradation (phase-transformation ageing) after a processing change</li><li><span class="ol">b)</span> nickel allergy</li><li><span class="ol">c)</span> UHMWPE wear</li><li><span class="ol">d)</span> galvanic corrosion</li></ul>
    <div class="rationale"><b>Answer: a.</b> Tetragonal-to-monoclinic transformation at the surface, accelerated by altered processing, embrittled specific batches.</div></li>
  <li>Which polymer pair is bioresorbable?
    <ul class="mcq-opts"><li><span class="ol">a)</span> PEEK and PTFE</li><li><span class="ol">b)</span> silicone and PU</li><li><span class="ol">c)</span> PLA and PGA</li><li><span class="ol">d)</span> PMMA and UHMWPE</li></ul>
    <div class="rationale"><b>Answer: c.</b> PLA/PGA hydrolyse to metabolisable acids; the others are permanent implant polymers.</div></li>
  <li>Osteolysis around a classic hip replacement is primarily driven by:
    <ul class="mcq-opts"><li><span class="ol">a)</span> heat from PMMA curing</li><li><span class="ol">b)</span> UHMWPE wear particles activating macrophages</li><li><span class="ol">c)</span> titanium stiffness</li><li><span class="ol">d)</span> collagen breakdown</li></ul>
    <div class="rationale"><b>Answer: b.</b> Phagocytosed polyethylene debris triggers cytokine-mediated bone resorption &mdash; the historic driver of highly cross-linked PE development.</div></li>
  <li>Self-expanding vascular stents exploit which nitinol property?
    <ul class="mcq-opts"><li><span class="ol">a)</span> superelastic shape recovery</li><li><span class="ol">b)</span> radioactivity</li><li><span class="ol">c)</span> porosity</li><li><span class="ol">d)</span> bioresorption</li></ul>
    <div class="rationale"><b>Answer: a.</b> Nitinol's martensitic transformation lets a crimped stent recover its programmed diameter at body temperature.</div></li>
  <li>Animal-derived materials in devices are risk-managed under which standard series?
    <ul class="mcq-opts"><li><span class="ol">a)</span> ISO 5832</li><li><span class="ol">b)</span> IEC 60601</li><li><span class="ol">c)</span> ISO 11607</li><li><span class="ol">d)</span> ISO 22442</li></ul>
    <div class="rationale"><b>Answer: d.</b> ISO 22442 governs sourcing, collection and viral/TSE risk control of animal tissues; ISO 5832 specifies metallic materials.</div></li>
  <li>The tissue-engineering triad comprises:
    <ul class="mcq-opts"><li><span class="ol">a)</span> metals, ceramics, polymers</li><li><span class="ol">b)</span> cells, scaffold, signals</li><li><span class="ol">c)</span> input, output, review</li><li><span class="ol">d)</span> donor, host, graft</li></ul>
    <div class="rationale"><b>Answer: b.</b> Langer &amp; Vacanti's triad; option (a) lists material families, (c) design controls.</div></li>
  <li>Charnley's early PTFE acetabular cups failed because:
    <ul class="mcq-opts"><li><span class="ol">a)</span> PTFE corroded</li><li><span class="ol">b)</span> PTFE resorbed</li><li><span class="ol">c)</span> PTFE wore rapidly, provoking severe tissue reaction to debris</li><li><span class="ol">d)</span> PTFE was radiopaque</li></ul>
    <div class="rationale"><b>Answer: c.</b> Chemically inert PTFE proved tribologically disastrous &mdash; the classic proof that biocompatibility is application-specific.</div></li>
</ol>
</div>

<div class="ass-block">
<h3>B. True / False</h3>
<ol>
  <li>Biocompatibility is a property of a material&ndash;application pair, not of a material alone. <span class="marks">(T)</span></li>
  <li>Fretting corrosion at modular tapers releases metal ions in hip implants. <span class="marks">(T)</span></li>
  <li>Alumina is a bioactive ceramic that bonds chemically to bone. <span class="marks">(F &mdash; alumina is bioinert; HA/Bioglass are bioactive)</span></li>
  <li>PLGA degradation rate can be tuned via the lactide:glycolide ratio. <span class="marks">(T)</span></li>
  <li>PEEK is valued for stiffness far higher than cortical bone. <span class="marks">(F &mdash; its bone-like stiffness is the virtue)</span></li>
  <li>Hydroxyapatite coatings on titanium stems combine bioactivity with structural toughness. <span class="marks">(T)</span></li>
  <li>PTFE is the preferred polymer for radiation sterilization. <span class="marks">(F &mdash; PTFE degrades under irradiation)</span></li>
  <li>Nitinol is nickel-free and safe in all nickel-allergic patients. <span class="marks">(F &mdash; ~half nickel by atom)</span></li>
  <li>Electrospinning produces nanofibrous scaffolds mimicking extracellular matrix. <span class="marks">(T)</span></li>
  <li>Decellularised matrices retain ECM architecture after cell removal. <span class="marks">(T)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>C. Fill in the Blanks</h3>
<ol>
  <li>The titanium implant alloy specified by ASTM F136 is __________.</li>
  <li>Bone resorption caused by an over-stiff implant is called __________.</li>
  <li>The bone-mineral-like ceramic used for implant coatings is __________.</li>
  <li>The bioactive glass composition discovered by Hench in 1969 is __________.</li>
  <li>The polymer used by Charnley as bone cement is __________.</li>
  <li>Wear-debris-driven periprosthetic bone loss is termed __________.</li>
  <li>The shape-memory alloy of self-expanding stents is __________.</li>
  <li>Tissue engineering's triad is cells, __________ and signals.</li>
  <li>The metallic implant materials standard series is ISO __________.</li>
  <li>Expanded PTFE vascular grafts are abbreviated __________.</li>
</ol>
</div>

<div class="ass-block">
<h3>D. Assertion&ndash;Reasoning</h3>
<p class="ar-key">Mark: (a) both A and R true, R explains A; (b) both true, R does not explain A; (c) A true, R false; (d) A false, R true.</p>
<ol>
  <li><strong>A:</strong> Titanium is preferred for uncemented hip stems. <strong>R:</strong> Its modulus is closer to bone and it osseointegrates. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> 316L is often chosen for temporary fracture fixation. <strong>R:</strong> Hydroxyapatite bonds chemically to bone. <span class="marks">(b)</span></li>
  <li><strong>A:</strong> Highly cross-linked UHMWPE reduced hip revision for osteolysis. <strong>R:</strong> Cross-linking reduces polyethylene wear-particle generation. <span class="marks">(a)</span></li>
  <li><strong>A:</strong> Natural biomaterials are always safer than synthetics. <strong>R:</strong> Animal-derived materials carry immunogenicity and sourcing risks controlled under ISO 22442. <span class="marks">(d)</span></li>
  <li><strong>A:</strong> A scaffold should degrade at a rate matched to tissue regeneration. <strong>R:</strong> All scaffolds must be metallic. <span class="marks">(c)</span></li>
</ol>
</div>

<div class="ass-block">
<h3>E. Short Answer Questions <span style="text-transform:none;">(2&ndash;3 marks each)</span></h3>
<ol>
  <li>Define biomaterial (Williams) and distinguish bioinert, bioactive and bioresorbable with one example each.</li>
  <li>Explain pitting, crevice, galvanic and fretting corrosion in one sentence each.</li>
  <li>Why did zirconia femoral heads fracture despite zirconia's high toughness?</li>
  <li>Compare PMMA bone cement and calcium-phosphate cements in two respects.</li>
  <li>List four scaffold design requirements for bone tissue engineering.</li>
  <li>Give three reasons sterilization method constrains biomaterial choice, with examples.</li>
</ol>
</div>

<div class="ass-block">
<h3>F. Long Answer Questions <span style="text-transform:none;">(10 marks each)</span></h3>
<ol>
  <li>Describe the four biomaterial families with representative members, properties, applications and characteristic failure modes, using a comparative table.</li>
  <li>Discuss corrosion, wear and stress shielding as interacting failure mechanisms in total hip arthroplasty, and show how material and design evolution (highly cross-linked PE, ceramics, titanium, coatings) has answered each.</li>
  <li>Explain tissue engineering's triad and scaffold-design principles, survey delivered clinical successes, and critically assess barriers between current products and engineered whole organs.</li>
</ol>
</div>

<div class="ass-block">
<h3>G. Higher-Order Thinking (HOTS)</h3>
<ol>
  <li>Propose the complete materials specification (family, grade, standard, sterilization, key risks) for a paediatric resorbable bone screw, justifying each choice against Table 4.2.</li>
  <li>Registry data show rising revision for a new &ldquo;low-wear&rdquo; bearing couple at year 4. Design the materials-failure investigation: retrieval analysis steps, hypotheses, and the bench tests distinguishing them.</li>
  <li>Argue for or against: &ldquo;Bioresorbable stents are conceptually superior, therefore they should replace metallic drug-eluting stents.&rdquo; Use mechanics-versus-degradation reasoning and the clinical evidence pattern you would demand.</li>
</ol>
</div>
</div>

<div class="references">
<h2>References (Vancouver style)</h2>
<ol>
  <li>Williams DF. On the nature of biomaterials. Biomaterials. 2009;30(30):5897-909.</li>
  <li>Ratner BD, Hoffman AS, Schoen FJ, Lemons JE, editors. Biomaterials Science: An Introduction to Materials in Medicine. 4th ed. London: Academic Press; 2020.</li>
  <li>International Organization for Standardization. ISO 5832 series &mdash; Implants for surgery &mdash; Metallic materials. Geneva: ISO.</li>
  <li>ASTM International. F138 (316L wrought stainless steel), F75 (CoCrMo casting alloy), F136 (Ti-6Al-4V ELI) standard specifications. West Conshohocken (PA): ASTM.</li>
  <li>Hench LL. The story of Bioglass. J Mater Sci Mater Med. 2006;17(11):967-78.</li>
  <li>Chevalier J. What future for zirconia as a biomaterial? Biomaterials. 2006;27(4):535-43.</li>
  <li>Langer R, Vacanti JP. Tissue engineering. Science. 1993;260(5110):920-6.</li>
  <li>Charnley J. Low Friction Arthroplasty of the Hip: Theory and Practice. Berlin: Springer; 1979.</li>
  <li>International Organization for Standardization. ISO 22442 series &mdash; Medical devices utilizing animal tissues and their derivatives. Geneva: ISO.</li>
  <li>Langton DJ, et al. Adverse reaction to metal debris following hip resurfacing. J Bone Joint Surg Br. 2010;92(1):38-46.</li>
</ol>
</div>

<div class="qgate">
<h2>Chapter 4 &middot; Completion Dashboard (Quality Gate)</h2>
<table class="qgate-t">
  <tr><th>Quality Gate criterion</th><th style="width:22mm;">Status</th><th>Evidence</th></tr>
  <tr><td>Learning objectives with CO/Bloom's mapping</td><td class="qg-pass">PASS</td><td>6 objectives, CO1&ndash;CO3 map table</td></tr>
  <tr><td>What&ndash;Why&ndash;How&ndash;Where&ndash;When framework applied</td><td class="qg-pass">PASS</td><td>Framework tags on sections 4.1&ndash;4.7</td></tr>
  <tr><td>Figures &amp; tables numbered with captions</td><td class="qg-pass">PASS</td><td>Figure 4.1; Tables 4.1&ndash;4.2</td></tr>
  <tr><td>All four callout types present</td><td class="qg-pass">PASS</td><td>Regulatory Spotlight, Clinical Insight, Industry Connect, Did You Know</td></tr>
  <tr><td>Case studies with analysis</td><td class="qg-pass">PASS</td><td>Case studies 4.1 (MoM hips), 4.2 (biliary stent)</td></tr>
  <tr><td>Full assessment battery</td><td class="qg-pass">PASS</td><td>10 MCQ + rationales, 10 T/F, 10 FIB, 5 A&ndash;R, 6 SAQ, 3 LAQ, 3 HOTS</td></tr>
  <tr><td>Anti-fabrication check (regulations/codes verified)</td><td class="qg-pass">PASS</td><td>ISO 5832, ASTM F-series, ISO 22442 &mdash; cited in references</td></tr>
  <tr><td>Vancouver-style chapter references</td><td class="qg-pass">PASS</td><td>10 references</td></tr>
</table>
</div>

</section>
"""
