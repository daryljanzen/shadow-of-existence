#!/usr/bin/env python3
"""
gen_live_edition.py -- builds BOOK_INTRO_cosmiCave/live_edition.html

** THE ONE DESIGN RULE, AND IT IS THE CORPUS'S OWN LESSON. **  The page does NOT
embed the frontier.  It FETCHES `THE_FRONTIER.md` from the CDN at read time and
renders it in the browser.

  A page that baked in the open-row count would be a SECOND HOME for that count,
  and every second home in this corpus has gone stale -- the register's masthead
  (r4487), THE_PLAN's grain cell (r4479), OPEN_PROBLEMS_MAP (r4515), THE_FRONTIER's
  own headline (r4551).  The frontier is generated from THE_REGISTER by
  regen_frontier.py, which is the one source; this page reads that artefact and
  owns no copy of it.

The paper list IS baked, because it changes on the scale of years and a wrong
title is visible on sight.  The PDFs are served from jsDelivr, a CDN over the
repo: raw.githubusercontent is not built for reader traffic and rate-limits.

Usage:  python3 scripts/gen_live_edition.py        (from the repo root)
"""
import os
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'live_edition.html')
OUT_INTRO = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'introduction.html')
OUT_FRONT = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'frontier.html')
CDN = 'https://cdn.jsdelivr.net/gh/daryljanzen/shadow-of-existence@main'
RAW = 'https://raw.githubusercontent.com/daryljanzen/shadow-of-existence/main'
# Where the generated pages link to each other.  On GitHub Pages they sit beside
# one another, so a bare filename is correct AND has no cache lag; the CDN base
# is kept for anyone opening these files outside the site.  PDFs always come
# from the CDN, which is what a CDN is good at.
PAGES = os.environ.get('PAGES_BASE', '.')

# P-number -> tex stem, in the corpus's own numbering.  The geometric core is
# P17 and sits seventeenth; the older `p0` tag put it first and is deprecated.
ORDER = [
    ('P1', 'BH_causality_v2'),
    ('P2', 'janzen_circle_v3'), ('P3', 'SdS-slicing-curve_v2'),
    ('P4', 'modern_parallax'), ('P5', 'groupoid_paper'),
    ('P6', 'shadow_of_existence'), ('P7', 'CR_framework'),
    ('P8', 'slicing_operator'), ('P9', 'range_paper'),
    ('P10', 'canonical_time'), ('P11', 'dynamics_paper'),
    ('P12', 'algebroid_paper'), ('P13', 'boundary_paper'),
    ('P14', 'matter_sector_paper'), ('P15', 'CR_cosmology'),
    ('P16', 'cosmogenesis_paper'), ('P17', 'geometric_core_paper'),
    ('P18', 'CR_synthesis'),
]


MATRIX_JS = '''// The matrix belongs INSIDE the introduction, at the figure the introduction
// already carries for it -- not as a sibling accordion.  It is fetched for the
// same reason everything else here is.
async function placeMatrix() {
  const slot = document.getElementById('matrixslot');
  if (!slot) return;
  try {
    // Beside the page on Pages; from the CDN when opened anywhere else.
    let r = await fetch('assets/dependency_matrix.html', {cache: 'no-cache'})
              .catch(() => null);
    if (!r || !r.ok) r = await fetch(
      '%%CDN%%/BOOK_INTRO_cosmiCave/assets/dependency_matrix.html',
      {cache: 'no-cache'});
    if (!r.ok) throw 0;
    const doc = new DOMParser().parseFromString(await r.text(), 'text/html');
    const tbl = doc.querySelector('table');
    if (!tbl) throw 0;
    slot.innerHTML = '';
    slot.appendChild(tbl);
  } catch (e) {
    slot.innerHTML = '<p class="status">The matrix is at ' +
      '<a href="%%RAW%%/BOOK_INTRO_cosmiCave/assets/dependency_matrix.html">' +
      'dependency_matrix.html</a>.</p>';
  }
}'''.replace('%%CDN%%', CDN).replace('%%RAW%%', RAW)


def title_of(stem):
    p = os.path.join(ROOT, 'corpus', stem + '.tex')
    if not os.path.exists(p):
        return None
    s = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'\\title\{(.+?)\}\s*\n\s*\\author', s, re.S)
    if not m:
        return None
    t = re.sub(r'\\\\|\s+', ' ', m.group(1))
    t = re.sub(r'\$([^$]*)\$', r'<code>\1</code>', t)   # $r=0$ leaked before
    t = re.sub(r'\\[a-zA-Z]+\{?', '', t).replace('}', '')
    t = t.replace('---', '\u2014').replace('--', '\u2013')
    return re.sub(r'\s+', ' ', t).strip()



# ── LaTeX -> Unicode.  The previous pass STRIPPED unknown macros, which deleted
#    the symbol rather than the markup: `z \in [0,\pi]` came out as `z [0, ]`.
#    Anything not mapped here is now kept as a word rather than dropped.
_SYM = {
    'Lambda': '\u039b', 'Omega': '\u03a9', 'alpha': '\u03b1', 'beta': '\u03b2',
    'gamma': '\u03b3', 'delta': '\u03b4', 'epsilon': '\u03b5',
    'varepsilon': '\u03b5', 'zeta': '\u03b6', 'eta': '\u03b7',
    'theta': '\u03b8', 'kappa': '\u03ba', 'lambda': '\u03bb', 'mu': '\u03bc',
    'nu': '\u03bd', 'xi': '\u03be', 'pi': '\u03c0', 'rho': '\u03c1',
    'sigma': '\u03c3', 'tau': '\u03c4', 'phi': '\u03c6', 'chi': '\u03c7',
    'psi': '\u03c8', 'omega': '\u03c9', 'Phi': '\u03a6', 'Psi': '\u03a8',
    'Gamma': '\u0393', 'Delta': '\u0394', 'Sigma': '\u03a3',
    'times': '\u00d7', 'pm': '\u00b1', 'to': '\u2192', 'mapsto': '\u21a6',
    'leftrightarrow': '\u2194', 'in': '\u2208', 'infty': '\u221e',
    'approx': '\u2248', 'simeq': '\u2243', 'sim': '\u223c', 'cong': '\u2245',
    'geq': '\u2265', 'ge': '\u2265', 'leq': '\u2264', 'le': '\u2264',
    'lesssim': '\u2272', 'propto': '\u221d', 'partial': '\u2202',
    'oplus': '\u2295', 'circ': '\u2218', 'subset': '\u2282',
    'supset': '\u2283', 'setminus': '\u2216', 'int': '\u222b',
    'hbar': '\u210f', 'ell': '\u2113', 'not': '\u00ac', 'cdot': '\u00b7',
    'ldots': '\u2026', 'dots': '\u2026', 'lvert': '|', 'rvert': '|',
    'dd': 'd', 'rs': 'r_s', 'dS': 'dS', 'TD': 'TD', 'fh': 'f_h', 'fm': 'f_m',
}
# Macros whose ARGUMENT is the content and whose name is styling only.
_UNWRAP = ('mathrm', 'mathbb', 'mathbf', 'mathcal', 'mathfrak', 'mathscr',
           'text', 'textrm', 'operatorname', 'bar', 'tilde', 'hat', 'vec',
           'boldsymbol', 'mathsf')
# Function names that should simply print.
_WORDS = ('sqrt', 'sin', 'cos', 'tan', 'sinh', 'cosh', 'tanh', 'ln', 'log',
          'exp', 'dim', 'ker', 'det', 'tr', 'su', 'so', 'SU', 'SO', 'S')


def detex(t):
    """LaTeX fragment -> readable HTML. Emphasis and bold are kept because the
    corpus uses them to carry weight; everything else is stripped."""
    t = re.sub(r'(?m)^\s*%.*$', '', t)
    t = re.sub(r'\\(?:label|rcpt|ldg|cite|citep|footnote)\{[^}]*\}', '', t)
    t = re.sub(r'\\(?:emph|textit)\{([^{}]*)\}', r'<em>\1</em>', t)
    t = re.sub(r'\\(?:textbf|strong)\{([^{}]*)\}', r'<strong>\1</strong>', t)
    t = re.sub(r'\$([^$]*)\$', r'<code>\1</code>', t)
    # \tfrac{a}{b} -> a/b, then unwrap styling macros, then map symbols.
    t = re.sub(r'\\[dt]?frac\{([^{}]*)\}\{([^{}]*)\}', r'\1/\2', t)
    for _ in range(3):
        t = re.sub(r'\\(?:' + '|'.join(_UNWRAP) + r')\{([^{}]*)\}', r'\1', t)
    t = re.sub(r'\\([a-zA-Z]+)\s*',
               lambda m: _SYM.get(m.group(1),
                                  m.group(1) + ' ' if m.group(1) in _WORDS
                                  else ' '), t)
    t = t.replace('---', '\u2014').replace('--', '\u2013')
    t = re.sub(r'[{}]', '', t).replace('~', ' ')
    # TeX quoting: ``x'' -> curly quotes, and \, \; thin spaces already gone.
    t = re.sub(r'``([^\']*)\'\'', '\u201c\\1\u201d', t)
    t = t.replace("``", '\u201c').replace("''", '\u201d')
    t = re.sub(r'\s+([,.;:)\]])', r'\1', t)      # space before punctuation
    t = re.sub(r'\(\s+', '(', t)
    t = re.sub(r'[ \t]+', ' ', t)
    paras = [x.strip() for x in re.split(r'\n\s*\n', t) if x.strip()]
    return paras


def abstract_of(stem, max_paras=3, cap=1400):
    """The abstract's opening, not the whole thing: several run past ten
    thousand characters, which is a paper rather than a preview."""
    fp = os.path.join(ROOT, 'corpus', stem + '.tex')
    if not os.path.exists(fp):
        return None, False
    s = open(fp, encoding='utf-8', errors='replace').read()
    m = re.search(r'\\begin\{abstract\}(.+?)\\end\{abstract\}', s, re.S)
    if not m:
        return None, False
    paras = detex(m.group(1))
    if not paras:
        return None, False
    kept, total, truncated = [], 0, False
    for para in paras:
        if kept and (len(kept) >= max_paras or total + len(para) > cap):
            truncated = True
            break
        kept.append(para)
        total += len(para)
    if len(kept) < len(paras):
        truncated = True
    return kept, truncated




def frontier_rows():
    """THE_FRONTIER.md's open rows -> (id, question, note).  Read at build time
    from the generated artefact, which regen_frontier.py writes from the register."""
    fp = os.path.join(ROOT, 'THE_FRONTIER.md')
    if not os.path.exists(fp):
        return []
    rows = []
    for line in open(fp, encoding='utf-8', errors='replace').read().split('\n'):
        if not line.startswith('|'):
            continue
        c = [x.strip() for x in line.split('|')]
        if len(c) < 4 or '~~' in c[1]:
            continue
        m = re.search(r'PO-\d+', c[1])
        if not m:
            continue
        note = c[9] if len(c) > 10 else ''
        clean = lambda x: re.sub(r'\*\*|`', '', x).replace('<', '&lt;').strip()
        rows.append((m.group(0), clean(c[2]), clean(note)))
    return rows


def md_to_html(md, matrix_slot=True, stop_at_h2=None):
    """INTRODUCTION.md -> HTML. The introduction is mostly headings, paragraphs
    and one raw <figure> for the matrix; nothing else is used, checked at build."""
    out, para, in_fig, seen_h2 = [], [], False, 0

    def inline(t):
        t = t.replace('&', '&amp;').replace('<', '&lt;')
        t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
        t = re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
        return re.sub(r'`(.+?)`', r'<code>\1</code>', t)

    def flush():
        if para:
            out.append('<p>' + inline(' '.join(para)) + '</p>')
            para.clear()

    for line in md.split('\n'):
        st = line.strip()
        if st.startswith('<figure>'):
            flush()
            in_fig = True
            if matrix_slot:
                out.append('<figure class="matrix"><div id="matrixslot">'
                           '<p class="status">Loading the matrix\u2026</p></div>')
            continue
        if in_fig:
            cap = re.search(r'<figcaption>([\s\S]*)', line)
            if cap and matrix_slot:
                out.append('<figcaption>' +
                           re.sub(r'</figcaption>.*', '', cap.group(1)) +
                           '</figcaption>')
            if '</figure>' in line:
                if matrix_slot:
                    out.append('</figure>')
                in_fig = False
            continue
        m = re.match(r'^(#{1,4}) (.*)$', st)
        if m:
            flush()
            lvl = len(m.group(1))
            if lvl == 2:
                seen_h2 += 1
                if stop_at_h2 and seen_h2 > stop_at_h2:
                    break
            if lvl == 1:
                continue                       # the page supplies its own title
            out.append(f'<h{min(lvl + 1, 4)}>' + inline(m.group(2)) +
                       f'</h{min(lvl + 1, 4)}>')
        elif not st:
            flush()
        else:
            para.append(st)
    flush()
    return '\n'.join(out)


def main():
    papers = []
    for num, stem in ORDER:
        t = title_of(stem)
        if not t:
            print(f'  [WARN] no title for {stem}, skipped')
            continue
        pdf = f'corpus/{stem}.pdf'
        if not os.path.exists(os.path.join(ROOT, pdf)):
            print(f'  [WARN] no PDF for {stem}, listed without a link')
            papers.append((num, t, None, stem))
            continue
        papers.append((num, t, f'{CDN}/{pdf}', stem))

    # The introduction becomes a page of its own, generated from the same source
    # by the same run -- a build artefact like the PDFs, not a hand copy, so it
    # cannot drift from INTRODUCTION.md.  The index shows its opening section and
    # sends a reader to the page for the rest.
    src = os.path.join(ROOT, 'INTRODUCTION.md')
    intro_full = intro_excerpt = ''
    if os.path.exists(src):
        md = open(src, encoding='utf-8', errors='replace').read()
        intro_full = md_to_html(md)
        intro_excerpt = md_to_html(md, matrix_slot=False, stop_at_h2=1)
    print(f'  introduction: {len(md) if intro_full else 0} source chars -> '
          f'{len(intro_full)} full, {len(intro_excerpt)} excerpt')

    rows, n_abs = [], 0
    for num, t, url, stem in papers:
        head, _, tail = t.partition(':')
        sub = f'<span class="sub">{tail.strip()}</span>' if tail.strip() else ''
        link = f'<a href="{url}">PDF</a>' if url else '<span class="nolink">—</span>'
        paras, cut = abstract_of(stem)
        if paras:
            n_abs += 1
            body = ''.join(f'<p>{x}</p>' for x in paras)
            if cut:
                body += ('<p class="more">The abstract continues in the paper '
                         f'itself. <a href="{url}">Open the PDF.</a></p>'
                         if url else '<p class="more">The abstract continues in '
                                     'the paper itself.</p>')
            rows.append(
                f'    <li><details><summary><span class="pn">{num}</span>'
                f'<span class="ti"><b>{head.strip()}</b>{sub}</span></summary>'
                f'<div class="abs">{body}</div></details>{link}</li>')
        else:
            rows.append(
                f'    <li><span class="pn">{num}</span>'
                f'<span class="ti"><b>{head.strip()}</b>{sub}</span>{link}</li>')
    paper_list = '\n'.join(rows)

    html = rf"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Shadow of Existence — the live edition</title>
<style>
  :root {{ --ink:#1c2733; --faint:#8b98a6; --line:#e2e8ee; --pole:#b5462a; --bg:#fbfcfd; }}
  * {{ box-sizing:border-box }}
  body {{ margin:0; background:var(--bg); color:var(--ink);
         font:16px/1.6 Georgia,'Iowan Old Style',serif; }}
  .wrap {{ max-width:52rem; margin:0 auto; padding:3rem 1.25rem 5rem; }}
  h1 {{ font-size:1.9rem; line-height:1.25; margin:0 0 .4rem; font-weight:600; }}
  h2 {{ font-size:1.15rem; margin:2.8rem 0 .3rem; font-weight:600;
        letter-spacing:.01em; }}
  .lede {{ color:#4a5765; margin:0 0 .2rem; }}
  .note {{ color:var(--faint); font-size:.86rem; }}
  ul.papers {{ list-style:none; padding:0; margin:1rem 0 0; }}
  ul.papers li {{ display:flex; align-items:baseline; gap:.7rem;
                  border-bottom:1px solid var(--line); }}
  ul.papers li > details {{ flex:1 1 auto; border-bottom:none; min-width:0; }}
  .pn {{ flex:0 0 3.2rem; color:var(--pole); font-weight:600; font-size:.82rem;
         letter-spacing:.04em; }}
  .ti {{ flex:1 1 auto; }}
  .ti .sub {{ display:block; color:var(--faint); font-size:.88rem; }}
  ul.papers a {{ flex:0 0 3rem; text-align:right; color:var(--pole);
                 text-decoration:none; font-size:.78rem; letter-spacing:.06em;
                 padding-top:.6rem; }}
  ul.papers > li > .nolink {{ flex:0 0 3rem; }}
  ul.papers a:hover {{ text-decoration:underline; }}
  .nolink {{ color:var(--line); }}
  details {{ border-bottom:1px solid var(--line); }}
  summary {{ cursor:pointer; padding:.55rem 0; display:flex; gap:.7rem;
             align-items:baseline; list-style:none; }}
  summary::-webkit-details-marker {{ display:none }}
  summary::before {{ content:'\203A'; color:var(--faint); flex:0 0 .6rem;
                     transition:transform .15s; }}
  details[open] > summary::before {{ transform:rotate(90deg); }}
  summary .sub {{ display:block; color:var(--faint); font-size:.88rem; }}
  .abs {{ padding:.2rem 0 1.1rem 1.3rem; font-size:.95rem; }}
  .abs p {{ margin:0 0 .7rem; }}
  .intro {{ font-size:1rem; padding:.4rem 0 1.6rem 1.3rem; }}
  .intro p {{ margin:0 0 1rem; }}
  .intro h3 {{ font-size:1.08rem; margin:2rem 0 .6rem; font-weight:600;
               color:var(--ink); }}
  .intro figure {{ margin:1.4rem 0; }}
  .intro figcaption {{ color:var(--faint); font-size:.86rem; margin-top:.5rem;
                       line-height:1.5; }}
  .intro .more {{ color:var(--faint); font-size:.86rem; font-style:italic; }}
  .intro code {{ font-size:.9em; background:#f1f4f7; padding:.05em .3em;
                 border-radius:3px; }}
  .abs .more {{ color:var(--faint); font-size:.88rem; }}
  .intro h2, .intro h3 {{ font-size:1rem; margin:1.2rem 0 .3rem; }}
  .matrix table {{ border-collapse:collapse; font-size:.72rem; }}
  .matrix td, .matrix th {{ border:1px solid var(--line); padding:.15rem .3rem;
                            text-align:center; }}
  .matrix {{ overflow-x:auto; }}
  #frontier {{ margin-top:1rem; }}
  .row {{ padding:.7rem 0 .8rem; border-bottom:1px solid var(--line); }}
  .row .id {{ color:var(--pole); font-weight:600; font-size:.85rem;
              margin-right:.5rem; }}
  .row .what {{ font-weight:600; }}
  .row .disc {{ display:block; color:#4a5765; font-size:.92rem; margin-top:.2rem; }}
  .status {{ color:var(--faint); font-size:.86rem; }}
  footer {{ margin-top:3.5rem; padding-top:1rem; border-top:1px solid var(--line);
            color:var(--faint); font-size:.84rem; }}
  a {{ color:var(--pole); }}
</style>
</head>
<body>
<div class="wrap">

<h1>The Shadow of Existence</h1>
<p class="lede">The live edition. Every paper below is served from the repository
itself, so what you open is what the work currently is — not a copy taken on a
date.</p>
<p class="note">For a citable, frozen version, use a tagged release rather than
this page.</p>

<p class="note">Click any entry to open it. Chapters link to the paper itself.</p>
<ul class="papers">
    <li><details id="introbox"><summary><span class="pn">INTRO</span>
      <span class="ti"><b>Introduction</b><span class="sub">what the programme is,
      the eighteen chapters and how they depend on one another, where to come in,
      and at what weight each claim is held</span></span></summary>
      <div class="intro">{intro_excerpt}
      <p class="more"><a href="{PAGES}/introduction.html" target="_blank"
         rel="noopener">Read more →</a></p></div>
    </details><a href="{PAGES}/introduction.html" target="_blank" rel="noopener">READ</a></li>
{paper_list}
</ul>

<h2>The open edge</h2>
<p class="lede">This is not a summary written for the page. It is fetched from the
programme's own frontier, which is generated from its register of open problems,
and it changes when the work does.</p>
<div id="frontier"><p class="status">Fetching the current frontier…</p></div>

<footer>
Source: <a href="https://github.com/daryljanzen/shadow-of-existence">the
repository</a>. Papers via jsDelivr; the frontier read live at page load.
</footer>

</div>
<script>
const PAGES_URL = '{PAGES}';
(async function () {{
  const el = document.getElementById('frontier');
  const urls = ['{CDN}/THE_FRONTIER.md', '{RAW}/THE_FRONTIER.md'];
  let text = null;
  for (const u of urls) {{
    try {{
      const r = await fetch(u, {{cache: 'no-cache'}});
      if (r.ok) {{ text = await r.text(); break; }}
    }} catch (e) {{ /* try the next source */ }}
  }}
  if (text === null) {{
    el.innerHTML = '<p class="more"><a href="' + PAGES_URL + '/frontier.html" '
      + 'target="_blank" rel="noopener">Read more \u2192</a></p>';
    return;
  }}
  // Rows are markdown table lines: | **PO-n** | what | ... | discharge |
  const rows = [];
  for (const line of text.split('\\n')) {{
    if (!line.startsWith('|')) continue;
    const c = line.split('|').map(s => s.trim());
    if (c.length < 4) continue;
    const id = (c[1].match(/PO-\\d+/) || [])[0];
    if (!id) continue;
    if (c[1].includes('~~')) continue;          // struck
    // c[2] is the question; c[9] is the row's own note, which carries the
    // discharge condition.  Indexed by position rather than from the end so a
    // trailing column added later cannot silently shift what is read.
    rows.push({{id: id, what: c[2] || '', disc: c[9] || ''}});
  }}
  if (!rows.length) {{
    el.innerHTML = '<p class="more"><a href="' + PAGES_URL + '/frontier.html" '
      + 'target="_blank" rel="noopener">Read more \u2192</a></p>';
    return;
  }}
  const clean = s => s.replace(/\\*\\*/g, '').replace(/`/g, '')
                      .replace(/</g, '&lt;').trim();
  const n = rows.length;
  let html = '<p class="status">' + n + ' open ' +
             (n === 1 ? 'question' : 'questions') + ', read from the register.</p>';
  for (const r of rows) {{
    const d = clean(r.disc);
    html += '<div class="row"><span class="id">' + r.id + '</span>' +
            '<span class="what">' + clean(r.what) + '</span>' +
            (d && d.length > 3 ? '<span class="disc">' + d.slice(0, 400) +
             '</span>' : '') + '</div>';
  }}
  html += '<p class="more"><a href="' + PAGES_URL + '/frontier.html" target="_blank" ' +
          'rel="noopener">Read more \u2192</a></p>';
  el.innerHTML = html;
}})();

{MATRIX_JS}
</script>
</body>
</html>
"""
    with open(OUT, 'w', encoding='utf-8') as fh:
        fh.write(html)

    # The introduction's own page: same stylesheet, so it reads as another page
    # of the book rather than a loose file.
    css = re.search(r'<style>(.*?)</style>', html, re.S).group(1)
    intro_page = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>Introduction \u2014 The Shadow of Existence</title>\n'
        '<style>' + css + '</style>\n</head>\n<body>\n<div class="wrap">\n'
        '<p class="note"><a href="' + PAGES.rstrip('/') + '/live_edition.html">\u2190 The '
        'Shadow of Existence</a></p>\n<h1>Introduction</h1>\n'
        '<div class="intro">\n' + intro_full + '\n</div>\n'
        '<footer>Generated from the repository\u2019s own introduction. '
        '<a href="https://github.com/daryljanzen/shadow-of-existence">Source.</a>'
        '</footer>\n</div>\n<script>\n' + MATRIX_JS + '\nplaceMatrix();\n'
        '</script>\n</body>\n</html>\n')
    with open(OUT_INTRO, 'w', encoding='utf-8') as fh:
        fh.write(intro_page)

    # The frontier gets a page too, for the same reason: a reader following
    # "Read more" should land on a page of the book, never on a markdown file.
    fr = frontier_rows()
    body = ''.join(
        f'<div class="row"><span class="id">{i}</span>'
        f'<span class="what">{q}</span>'
        + (f'<span class="disc">{n}</span>' if n else '') + '</div>'
        for i, q, n in fr)
    front_page = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>The open edge \u2014 The Shadow of Existence</title>\n'
        '<style>' + css + '</style>\n</head>\n<body>\n<div class="wrap">\n'
        '<p class="note"><a href="' + PAGES.rstrip('/') + '/live_edition.html">\u2190 The '
        'Shadow of Existence</a></p>\n<h1>The open edge</h1>\n'
        '<p class="lede">The programme\u2019s own open questions, each with what '
        'would discharge it. Generated from its register, not written for this '
        'page \u2014 ' + str(len(fr)) + ' stand open.</p>\n'
        + body +
        '\n<footer>Generated from the repository\u2019s register of open '
        'problems. <a href="https://github.com/daryljanzen/shadow-of-existence">'
        'Source.</a></footer>\n</div>\n</body>\n</html>\n')
    with open(OUT_FRONT, 'w', encoding='utf-8') as fh:
        fh.write(front_page)
    print(f'  frontier.html written: {len(fr)} open rows, {len(front_page)} bytes.')

    print(f'  introduction.html written: {len(intro_page)} bytes, '
          f'matrix fetched into its figure.')
    print(f'  live_edition.html written: {len(papers)} papers listed, '
          f'{n_abs} with abstracts, frontier fetched at read time '
          f'(not embedded).')


if __name__ == '__main__':
    main()
