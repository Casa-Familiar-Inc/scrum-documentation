"""
generate_report.py
------------------
Convierte un archivo Markdown de reporte semanal (con frontmatter YAML)
a un HTML profesional listo para imprimir o exportar a PDF.

Uso:
    python generate_report.py                          # usa el MD mas reciente en la carpeta
    python generate_report.py 2026-03-18-Weekly-Activity-Report.md

Requiere:
    pip install markdown pyyaml
"""

import sys
import os
import re
import glob
import yaml
import markdown
from datetime import datetime

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------
LOGO_TEXT = "Casa Familiar"
ORG_SUBTITLE = "IT Department"
ACCENT_COLOR = "#1a3a5c"  # azul marino Casa Familiar
ACCENT_LIGHT = "#2e6da4"

STATUS_BADGES = {
    "completed":       ("#d4edda", "#155724", "Completed"),
    "in progress":     ("#cce5ff", "#004085", "In Progress"),
    "ongoing":         ("#fff3cd", "#856404", "Ongoing"),
    "attended":        ("#d1ecf1", "#0c5460", "Attended"),
    "blocked":         ("#f8d7da", "#721c24", "Blocked"),
    "in investigation":("#e2d9f3", "#4a235a", "In Investigation"),
    "scheduled":       ("#d6eaf8", "#154360", "Scheduled"),
    "waiting":         ("#fdebd0", "#784212", "Waiting"),
    "data phase":      ("#d5f5e3", "#1e8449", "Data Phase"),
    "technical":       ("#f2f3f4", "#424949", "Technical"),
}

CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
    font-family: 'Inter', sans-serif;
    font-size: 10.5pt;
    color: #1a1a2e;
    background: #f4f6f9;
}}

.page {{
    width: 8.5in;
    min-height: 11in;
    margin: 0 auto;
    background: #ffffff;
    padding: 0.55in 0.6in 0.5in 0.6in;
    box-shadow: 0 2px 20px rgba(0,0,0,0.12);
}}

/* ---- HEADER ---- */
.report-header {{
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    border-bottom: 3px solid {ACCENT_COLOR};
    padding-bottom: 14px;
    margin-bottom: 18px;
}}
.header-left h1 {{
    font-size: 20pt;
    font-weight: 700;
    color: {ACCENT_COLOR};
    line-height: 1.1;
}}
.header-left p.subtitle {{
    font-size: 10pt;
    color: #666;
    margin-top: 2px;
}}
.header-meta {{
    text-align: right;
    font-size: 9pt;
    color: #444;
    line-height: 1.8;
}}
.header-meta strong {{
    color: {ACCENT_COLOR};
}}
.week-badge {{
    display: inline-block;
    background: {ACCENT_COLOR};
    color: #fff;
    font-size: 9pt;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 4px;
    margin-top: 6px;
}}

/* ---- SECTIONS ---- */
.section {{
    margin-bottom: 20px;
}}
.section-title {{
    font-size: 11pt;
    font-weight: 700;
    color: {ACCENT_COLOR};
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-left: 4px solid {ACCENT_LIGHT};
    padding-left: 8px;
    margin-bottom: 10px;
}}

/* ---- TABLES ---- */
table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 9pt;
    margin-bottom: 4px;
}}
th {{
    background: {ACCENT_COLOR};
    color: #fff;
    font-weight: 600;
    text-align: left;
    padding: 7px 8px;
    font-size: 8.5pt;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}}
td {{
    padding: 6px 8px;
    border-bottom: 1px solid #e8ecf0;
    vertical-align: top;
    line-height: 1.4;
}}
tr:nth-child(even) td {{
    background: #f8fafd;
}}
tr:last-child td {{
    border-bottom: none;
}}
strong {{ font-weight: 600; }}

/* ---- STATUS BADGE ---- */
.badge {{
    display: inline-block;
    padding: 2px 8px;
    border-radius: 10px;
    font-size: 8pt;
    font-weight: 600;
    white-space: nowrap;
}}

/* ---- BULLET LISTS ---- */
ul.activity-list {{
    list-style: none;
    padding: 0;
}}
ul.activity-list li {{
    padding: 5px 0 5px 16px;
    border-bottom: 1px solid #eef0f3;
    position: relative;
    font-size: 9.5pt;
    line-height: 1.5;
}}
ul.activity-list li:last-child {{
    border-bottom: none;
}}
ul.activity-list li::before {{
    content: '';
    position: absolute;
    left: 0;
    top: 12px;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: {ACCENT_LIGHT};
}}

/* ---- PENDING CHECKLIST ---- */
ul.pending-list {{
    list-style: none;
    padding: 0;
}}
ul.pending-list li {{
    padding: 5px 0 5px 24px;
    border-bottom: 1px solid #eef0f3;
    position: relative;
    font-size: 9.5pt;
    line-height: 1.5;
}}
ul.pending-list li:last-child {{
    border-bottom: none;
}}
ul.pending-list li::before {{
    content: '';
    position: absolute;
    left: 0;
    top: 8px;
    width: 14px;
    height: 14px;
    border: 2px solid #aaa;
    border-radius: 3px;
    background: #fff;
}}

/* ---- NOTES / CALLOUTS ---- */
.callout {{
    background: #f0f5fb;
    border-left: 4px solid {ACCENT_LIGHT};
    border-radius: 0 6px 6px 0;
    padding: 10px 14px;
    margin-bottom: 10px;
    font-size: 9.5pt;
    line-height: 1.5;
}}
.callout-title {{
    font-weight: 700;
    color: {ACCENT_COLOR};
    margin-bottom: 4px;
    font-size: 9pt;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}}
.callout.warning {{
    background: #fffbf0;
    border-left-color: #e6a817;
}}
.callout.warning .callout-title {{
    color: #7a5000;
}}

/* ---- FOOTER ---- */
.report-footer {{
    margin-top: 28px;
    padding-top: 12px;
    border-top: 2px solid {ACCENT_COLOR};
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 8.5pt;
    color: #555;
}}
.report-footer .sig {{
    font-weight: 600;
    color: {ACCENT_COLOR};
}}

/* ---- PRINT ---- */
@media print {{
    body {{ background: white; }}
    .page {{ box-shadow: none; margin: 0; width: 100%; padding: 0.4in 0.5in; }}
}}
"""

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def status_badge(text: str) -> str:
    key = text.strip().lower()
    if key in STATUS_BADGES:
        bg, fg, label = STATUS_BADGES[key]
        return f'<span class="badge" style="background:{bg};color:{fg}">{label}</span>'
    return f'<span class="badge" style="background:#eee;color:#333">{text}</span>'


def md_inline(text: str) -> str:
    """Convierte bold/italic inline dentro de celdas."""
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    return text


def parse_md_table(lines):
    """Parsea una tabla MD y devuelve (headers, rows)."""
    rows = []
    for line in lines:
        line = line.strip().strip('|')
        if not line or re.match(r'^[\s:\-|]+$', line):
            continue
        cells = [c.strip() for c in line.split('|')]
        rows.append(cells)
    if not rows:
        return [], []
    return rows[0], rows[1:]


def render_table(headers, rows, status_col=None):
    html = '<table>\n<thead><tr>'
    for h in headers:
        html += f'<th>{h}</th>'
    html += '</tr></thead>\n<tbody>'
    for row in rows:
        html += '<tr>'
        for i, cell in enumerate(row):
            if status_col is not None and i == status_col:
                html += f'<td>{status_badge(cell)}</td>'
            else:
                html += f'<td>{md_inline(cell)}</td>'
        html += '</tr>'
    html += '</tbody></table>'
    return html


def parse_callouts(text: str):
    """
    Convierte bloques Obsidian [!NOTE] / [!WARNING] a HTML callout divs.
    Maneja bloques multi-linea de citas (>).
    """
    pattern = re.compile(
        r'(?m)^> \[!(NOTE|WARNING|IMPORTANT|CAUTION|TIP)\]\s+(.*?)(?=\n> \[!|\Z)',
        re.DOTALL
    )
    result = []
    last = 0
    for m in pattern.finditer(text):
        result.append(text[last:m.start()])
        kind = m.group(1).upper()
        css_cls = 'warning' if kind in ('WARNING', 'CAUTION') else ''
        # extraer lineas del bloque
        block_raw = m.group(0)
        lines = []
        for ln in block_raw.splitlines():
            stripped = re.sub(r'^>\s?', '', ln)
            if re.match(r'\[!(NOTE|WARNING|IMPORTANT|CAUTION|TIP)\]', stripped):
                title_match = re.match(r'\[!\w+\]\s*(.*)', stripped)
                title = title_match.group(1) if title_match else kind
                lines.append(('title', title))
            else:
                lines.append(('body', stripped))
        html = f'<div class="callout {css_cls}">'
        for t, v in lines:
            if t == 'title':
                html += f'<div class="callout-title">{kind} — {md_inline(v)}</div>'
            else:
                if v.strip():
                    html += f'<p>{md_inline(v)}</p>'
        html += '</div>'
        result.append(html)
        last = m.end()
    result.append(text[last:])
    return ''.join(result)


# ---------------------------------------------------------------------------
# PARSER PRINCIPAL
# ---------------------------------------------------------------------------

def parse_report(filepath: str):
    with open(filepath, encoding='utf-8') as f:
        raw = f.read()

    # Extraer frontmatter
    fm = {}
    body = raw
    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', raw, re.DOTALL)
    if fm_match:
        fm = yaml.safe_load(fm_match.group(1)) or {}
        body = raw[fm_match.end():]

    sections = {}
    current_key = None
    current_lines = []

    for line in body.splitlines():
        h2 = re.match(r'^## (.+)', line)
        if h2:
            if current_key:
                sections[current_key] = '\n'.join(current_lines).strip()
            current_key = h2.group(1).strip()
            current_lines = []
        elif re.match(r'^---+$', line) and current_key:
            pass  # ignorar separadores
        elif re.match(r'^# .+', line):
            pass  # ignorar H1
        else:
            current_lines.append(line)

    if current_key:
        sections[current_key] = '\n'.join(current_lines).strip()

    return fm, sections


def section_to_table_html(content: str, status_col: int = None) -> str:
    """Si el contenido tiene una tabla MD, la convierte a HTML."""
    table_lines = []
    in_table = False
    for line in content.splitlines():
        if line.strip().startswith('|'):
            in_table = True
            table_lines.append(line)
        elif in_table:
            break
    if not table_lines:
        return None
    headers, rows = parse_md_table(table_lines)
    return render_table(headers, rows, status_col=status_col)


def section_to_bullets(content: str, css_class: str = 'activity-list') -> str:
    items = []
    for line in content.splitlines():
        m = re.match(r'^-\s+\[ \]\s+(.*)', line)
        if m:
            items.append(md_inline(m.group(1)))
            continue
        m = re.match(r'^-\s+(.*)', line)
        if m:
            items.append(md_inline(m.group(1)))
    if not items:
        return None
    li = ''.join(f'<li>{i}</li>' for i in items)
    return f'<ul class="{css_class}">{li}</ul>'


# ---------------------------------------------------------------------------
# BUILD HTML
# ---------------------------------------------------------------------------

def build_html(fm: dict, sections: dict) -> str:
    analyst   = fm.get('it_analyst', '')
    director  = fm.get('it_director', '')
    week      = fm.get('week_covered', '')
    date_str  = datetime.now().strftime('%B %d, %Y')

    # Determine status column index for main tasks table (col 1 = Status)
    WORKING_SEC    = 'Currently Working On / New Tasks'
    COMPLETED_SEC  = 'Completed This Week'
    ONGOING_SEC    = 'Ongoing Activities and Projects'
    PENDING_SEC    = 'Pending / Blocked'
    NOTES_SEC      = 'Notes & Observations'

    # --- Currently Working On ---
    working_html = ''
    if WORKING_SEC in sections:
        t = section_to_table_html(sections[WORKING_SEC], status_col=1)
        if t:
            working_html = t

    # --- Completed ---
    completed_html = ''
    if COMPLETED_SEC in sections:
        t = section_to_table_html(sections[COMPLETED_SEC], status_col=None)
        if t:
            completed_html = t

    # --- Ongoing ---
    ongoing_html = ''
    if ONGOING_SEC in sections:
        b = section_to_bullets(sections[ONGOING_SEC], 'activity-list')
        if b:
            ongoing_html = b

    # --- Pending ---
    pending_html = ''
    if PENDING_SEC in sections:
        b = section_to_bullets(sections[PENDING_SEC], 'pending-list')
        if b:
            pending_html = b

    # --- Notes ---
    notes_html = ''
    if NOTES_SEC in sections:
        notes_html = parse_callouts(sections[NOTES_SEC])

    def section_block(title: str, content: str) -> str:
        if not content or not content.strip():
            return ''
        return f'''
        <div class="section">
            <div class="section-title">{title}</div>
            {content}
        </div>'''

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IT Weekly Activity Report — {week}</title>
<style>{CSS}</style>
</head>
<body>
<div class="page">

  <!-- HEADER -->
  <div class="report-header">
    <div class="header-left">
      <h1>IT Weekly Activity Report</h1>
      <p class="subtitle">{LOGO_TEXT} &mdash; {ORG_SUBTITLE}</p>
      <div class="week-badge">Week: {week}</div>
    </div>
    <div class="header-meta">
      <strong>IT Analyst:</strong> {analyst}<br>
      <strong>IT Director:</strong> {director}<br>
      <strong>Department:</strong> IT<br>
      <strong>Date:</strong> {date_str}
    </div>
  </div>

  {section_block("Currently Working On / New Tasks", working_html)}
  {section_block("Completed This Week", completed_html)}
  {section_block("Ongoing Activities &amp; Projects", ongoing_html)}
  {section_block("Pending / Blocked", pending_html)}
  {section_block("Notes &amp; Observations", notes_html)}

  <!-- FOOTER -->
  <div class="report-footer">
    <span><span class="sig">{analyst}</span> &nbsp;/&nbsp; <span class="sig">{director}</span></span>
    <span>{LOGO_TEXT} &mdash; IT Department &mdash; {date_str}</span>
  </div>

</div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    folder = os.path.dirname(os.path.abspath(__file__))

    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        if not os.path.isabs(filepath):
            filepath = os.path.join(folder, filepath)
    else:
        # Tomar el MD mas reciente en la misma carpeta
        md_files = sorted(glob.glob(os.path.join(folder, '*.md')), reverse=True)
        if not md_files:
            print("No se encontraron archivos .md en la carpeta.")
            sys.exit(1)
        filepath = md_files[0]

    if not os.path.exists(filepath):
        print(f"Archivo no encontrado: {filepath}")
        sys.exit(1)

    print(f"Procesando: {filepath}")
    fm, sections = parse_report(filepath)
    html = build_html(fm, sections)

    out_path = os.path.splitext(filepath)[0] + '.html'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Reporte generado: {out_path}")


if __name__ == '__main__':
    main()
