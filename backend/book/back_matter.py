from .docx_chapters import all_glossary_terms, all_references, esc


def glossary_html():
    terms = all_glossary_terms()
    rows = []
    for term, definition, chs in terms:
        chtag = ", ".join(str(c) for c in sorted(chs))
        rows.append("<dt>%s.</dt> <dd>%s <span class='gl-ch'>(Ch %s)</span></dd><br/>"
                    % (esc(term), esc(definition), chtag))
    return """
<section class="backmatter-section glossary" id="glossary" data-running="Glossary">
  <h1 class="fm-title">Glossary of Key Terms</h1>
  <p style="color:#5B6770;font-size:9pt;">Consolidated from the chapter glossaries of all 20 chapters.
  Chapter numbers in parentheses locate the term's primary discussion.</p>
  <dl>%s</dl>
</section>""" % "".join(rows)


def standards_index_html():
    rows = [
        ("Drugs and Cosmetics Act, 1940", "India", "Parent statute under which medical devices are regulated", "Ch 1, 12"),
        ("Medical Devices Rules, 2017 — G.S.R. 78(E)", "India", "Comprehensive risk-based device rules; Class A–D", "Ch 1, 3, 12"),
        ("National Medical Device Policy, 2023", "India", "Six-strategy sector policy; USD 50 bn ambition by 2030", "Ch 1, 2, 20"),
        ("Federal Food, Drug, and Cosmetic Act, as amended", "USA", "Statutory basis of FDA device authority; §201(h) definition", "Ch 1, 3, 12"),
        ("21 CFR Part 820 — Quality System Regulation", "USA", "US GMP / quality system requirements for devices", "Ch 5, 9, 10, 12"),
        ("Regulation (EU) 2017/745 (EU MDR)", "EU", "Device regulation; Classes I, IIa, IIb, III; CE marking", "Ch 1, 3, 12, 14"),
        ("ISO 13485:2016", "International", "QMS requirements for medical devices", "Ch 5, 9, 10, 11"),
        ("ISO 14971:2019", "International", "Application of risk management to medical devices", "Ch 5, 9, 13"),
        ("ISO 10993 series", "International", "Biological evaluation of medical devices", "Ch 8, 11"),
        ("ISO 14644 series", "International", "Cleanrooms and associated controlled environments", "Ch 6"),
        ("IEC 60601 series", "International", "Basic safety & essential performance of medical electrical equipment", "Ch 11, 12"),
        ("IEC 62304:2006+AMD1:2015", "International", "Medical device software — life cycle processes", "Ch 13"),
        ("IEC 62366-1:2015", "International", "Usability engineering for medical devices", "Ch 9, 13"),
        ("ISO 14155:2020", "International", "Clinical investigation of medical devices — GCP", "Ch 14"),
        ("ISO 11135 / ISO 11137 / ISO 17665", "International", "Sterilization: ethylene oxide / radiation / moist heat", "Ch 10, 11"),
        ("ISO 11607-1/-2:2019", "International", "Packaging for terminally sterilized medical devices", "Ch 10, 16"),
        ("ISO 15223-1:2021", "International", "Symbols for medical device labels and information", "Ch 9, 16"),
        ("IMDRF SaMD framework (N10/N12/N23/N41)", "IMDRF", "SaMD definitions, risk categorization, QMS, clinical evaluation", "Ch 13"),
        ("WHO Global Model Regulatory Framework (2017)", "WHO", "Model framework for medical device regulation incl. IVDs", "Ch 1, 12"),
    ]
    trs = "".join("<tr><td class='rowhead'>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % r for r in rows)
    return """
<section class="backmatter-section" id="stdindex" data-running="Standards &amp; Regulations Index">
  <h1 class="fm-title">Standards &amp; Regulations Index</h1>
  <div class="tablewrap"><table class="data">
    <tr><th>Instrument</th><th style="width:22mm;">Jurisdiction</th><th>Scope in this book</th><th style="width:24mm;">Chapters</th></tr>
    %s
  </table></div>
  <p style="color:#5B6770;font-size:8.6pt;">Chapter references indicate principal coverage; many standards recur
  throughout the text. Always verify the current edition of any standard or regulation before professional use.</p>
</section>""" % trs


def consolidated_refs_html():
    parts = []
    for num, title, refs in all_references():
        lis = "".join("<li>%s</li>" % esc(r) for r in refs)
        parts.append('<h3 class="subsec" style="margin-top:5mm;">Chapter %d — %s</h3>'
                     '<div class="references" style="border-top:none;padding-top:0;margin-top:1mm;"><ol>%s</ol></div>'
                     % (num, esc(title), lis))
    return """
<section class="backmatter-section" id="biblio" data-running="Consolidated References">
  <h1 class="fm-title">Consolidated References</h1>
  <p style="color:#5B6770;font-size:9pt;">Chapter-by-chapter consolidated listing of the regulatory documents,
  international standards, guidance documents and technical publications cited across the book.</p>
  %s
</section>""" % "".join(parts)
