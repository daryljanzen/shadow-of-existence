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
OUT_LEDG = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'ledgers.html')
OUT_RCPT = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'receipts.html')
GH = 'https://github.com/daryljanzen/shadow-of-existence/blob/main'
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
    t = re.sub(r'\$([^$]*)\$',
               lambda m: '<span class="m">' + mathspan(m.group(1)) + '</span>', t)
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
    'neq': '\u2260', 'ne': '\u2260', 'equiv': '\u2261', 'perp': '\u22a5',
    'langle': '\u27e8', 'rangle': '\u27e9', 'nabla': '\u2207', 'ast': '*',
    'geq': '\u2265', 'ge': '\u2265', 'leq': '\u2264', 'le': '\u2264',
    'lesssim': '\u2272', 'propto': '\u221d', 'partial': '\u2202',
    'oplus': '\u2295', 'circ': '\u2218', 'subset': '\u2282',
    'supset': '\u2283', 'setminus': '\u2216', 'int': '\u222b',
    'hbar': '\u210f', 'ell': '\u2113', 'not': '\u00ac', 'cdot': '\u00b7',
    'ldots': '\u2026', 'dots': '\u2026', 'lvert': '|', 'rvert': '|',
    'sqrt': '\u221a', 'dd': 'd', 'rs': 'r_s', 'dS': 'dS', 'TD': 'TD', 'fh': 'f_h', 'fm': 'f_m',
}
# Macros whose ARGUMENT is the content and whose name is styling only.
_UNWRAP = ('mathrm', 'mathbb', 'mathbf', 'mathcal', 'mathfrak', 'mathscr',
           'text', 'textrm', 'operatorname', 'bar', 'tilde', 'hat', 'vec',
           'boldsymbol', 'mathsf')
# Function names that should simply print.
_WORDS = ('sin', 'cos', 'tan', 'sinh', 'cosh', 'tanh', 'ln', 'log',
          'exp', 'dim', 'ker', 'det', 'tr', 'su', 'so', 'SU', 'SO', 'S')


_SUP = {'0':'\u2070','1':'\u00b9','2':'\u00b2','3':'\u00b3','4':'\u2074','5':'\u2075',
        '6':'\u2076','7':'\u2077','8':'\u2078','9':'\u2079','+':'\u207a','-':'\u207b',
        '(':'\u207d',')':'\u207e','n':'\u207f','i':'\u2071'}
_SUB = {'0':'\u2080','1':'\u2081','2':'\u2082','3':'\u2083','4':'\u2084','5':'\u2085',
        '6':'\u2086','7':'\u2087','8':'\u2088','9':'\u2089','+':'\u208a','-':'\u208b',
        '(':'\u208d',')':'\u208e','a':'\u2090','e':'\u2091','h':'\u2095','i':'\u1d62',
        'k':'\u2096','l':'\u2097','m':'\u2098','n':'\u2099','o':'\u2092','p':'\u209a',
        'r':'\u1d63','s':'\u209b','t':'\u209c','u':'\u1d64','v':'\u1d65','x':'\u2093'}


def _script(t):
    """x^2 -> x<sup>2</sup>, r_h -> r<sub>h</sub>.

    ** HTML tags rather than Unicode superscript characters. **  Unicode has
    superscripts for the digits and a handful of letters and NOTHING for most of
    the alphabet -- no superscript b, c, d, g, q -- and subscripts are thinner
    still.  A table-based mapping therefore renders `r_h` and `q^{ab}` as a bare
    underscore and caret, which is what the abstracts and the introduction were
    showing.  `<sup>` and `<sub>` render every character, so the coverage
    question does not arise."""
    t = re.sub(r'\^\{([^{}]*)\}|\^(\S)',
               lambda m: '<sup>' + (m.group(1) or m.group(2)) + '</sup>', t)
    return re.sub(r'_\{([^{}]*)\}|_(\S)',
                  lambda m: '<sub>' + (m.group(1) or m.group(2)) + '</sub>', t)


_NEG = {'subset': '\u2284', 'supset': '\u2285', 'in': '\u2209', 'ni': '\u220c',
        'equiv': '\u2262', 'sim': '\u2241', 'cong': '\u2247', 'leq': '\u2270',
        'le': '\u2270', 'geq': '\u2271', 'ge': '\u2271', 'perp': '\u22ac'}



def _mathtail(t):
    """The last steps every math span needs, wherever it was converted: resolve
    the function-spacing marker, and keep a script attached to the name it
    belongs to.  Factored out because detex converts spans in one place and
    mathspan in another, and only one of them had it."""
    t = _fixspace(t)
    return re.sub(r'\s+(<su[pb]>)', r'\1', t)


def _prep(t):
    """Two things the table alone cannot do.

    `\\not\\subset` is ONE character, not a negation sign glued to a relation:
    it was rendering as the two symbols side by side.

    And a function name needs a space before it when a symbol runs into it --
    `\\alpha\\sin u` was coming out as `asin u`, which reads as a different
    function.  A marker is inserted and resolved after substitution, since at
    substitution time the preceding character is not known."""
    t = re.sub(r'\\not\\([a-zA-Z]+)',
               lambda m: _NEG.get(m.group(1), '\u00ac\\' + m.group(1)), t)
    return re.sub(r'\\(' + '|'.join(_WORDS) + r')\b',
                  lambda m: '\x00\\' + m.group(1), t)


def _fixspace(t):
    return re.sub(r'\s*\x00\s*',
                  lambda m: ' ' if m.start() else '', t).strip()


def mathspan(t):
    """`$...$` -> readable Unicode, using the same table the abstracts use."""
    t = _prep(t)
    t = re.sub(r'\\[dt]?frac\{([^{}]*)\}\{([^{}]*)\}', r'\1/\2', t)
    for _ in range(3):
        t = re.sub(r'\\(?:' + '|'.join(_UNWRAP) + r')\{([^{}]*)\}', r'\1', t)
    # \mathbb Z with no braces: take the next token as the argument, or the
    # wrapper's trailing space detaches it -- 'Z 2' instead of 'Z2'.
    # The wrapper name must END here: without the boundary, '\\times\\mathbb Z'
    # had its '\\mathbb ' eaten and left '\\timesZ', an unknown macro, dropped.
    # Keep a separator: '\\times\\mathbb Z' -> replacing '\\mathbb Z' with 'Z'
    # in place gives '\\timesZ', an unknown macro, silently dropped.
    t = re.sub(r'\\(?:' + '|'.join(_UNWRAP) + r')\b *(\w)', r' \1', t)
    t = re.sub(r'\\([a-zA-Z]+)\s*',
               lambda m: _SYM.get(m.group(1),
                                  m.group(1) + ' ' if m.group(1) in _WORDS else ' '), t)
    t = re.sub(r'\s+([_^])', r'\1', t)        # 'ker _+' -> 'ker_+'
    t = _script(t)
    t = re.sub(r'\s+([,.;:)\]])', r'\1', t)
    t = re.sub(r'([(,\[])\s+', r'\1', t)     # 'SO(6, C)' -> 'SO(6,C)'
    t = _fixspace(t)
    # sinh^{2/3}: the script belongs to the function name, so no space before it
    t = re.sub(r'\s+(<su[pb]>)', r'\1', t)
    return re.sub(r'\s+', ' ', t.replace('{', '').replace('}', '')).strip()


def detex(t):
    t = _prep(t)
    """LaTeX fragment -> readable HTML. Emphasis and bold are kept because the
    corpus uses them to carry weight; everything else is stripped."""
    t = re.sub(r'(?m)^\s*%.*$', '', t)
    t = re.sub(r'\\(?:label|rcpt|ldg|cite|citep|footnote)\{[^}]*\}', '', t)
    t = re.sub(r'\\(?:emph|textit)\{([^{}]*)\}', r'<em>\1</em>', t)
    t = re.sub(r'\\(?:textbf|strong)\{([^{}]*)\}', r'<strong>\1</strong>', t)
    t = re.sub(r'\$([^$]*)\$',
               lambda m: '<span class="m">' + mathspan(m.group(1)) + '</span>', t)
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



def ledger_rows():
    """The registry's rows in its own order, which is the numbering order:
    L1 the corpus's own instrument, L2-L20 mathematics, L21-L25 method."""
    fp = os.path.join(ROOT, 'corpus', 'ledgers_registry.md')
    if not os.path.exists(fp):
        return []
    out = []
    for line in open(fp, encoding='utf-8', errors='replace').read().split('\n'):
        if not line.startswith('| **L'):
            continue
        c = [x.strip() for x in line.split('|')]
        if len(c) < 6:
            continue
        out.append(dict(num=c[1].strip('*'), key=c[2].strip('`'),
                        file=c[3].strip('`'), kind=c[4],
                        what=re.sub(r'\*\*|`', '', c[5])))
    return out


def receipt_rows():
    """INDEX.md's rows grouped by the paper directory that owns them, which is
    the same home the appendix numbering uses -- so PxRn here is PxRn there."""
    fp = os.path.join(ROOT, 'receipts', 'INDEX.md')
    if not os.path.exists(fp):
        return {}, {}
    by, seen = {}, {}
    for line in open(fp, encoding='utf-8', errors='replace').read().split('\n'):
        if not line.startswith('|'):
            continue
        cells = [x.strip() for x in line.split('|')]
        path = claim = ''
        for x in cells:
            if re.match(r'`?P\d+_[A-Za-z0-9_]+/', x.strip('`')):
                path = x.strip('`')
                break
        if not path:
            continue
        for x in cells:
            if len(x) > 25 and '/' not in x and not x.startswith('`'):
                claim = re.sub(r'\*\*|`', '', x)
                break
        home = 'P%d' % int(re.match(r'P(\d+)_', path).group(1))
        stem = path.rsplit('/', 1)[-1]
        if stem in seen:
            continue
        seen[stem] = True
        by.setdefault(home, []).append(
            dict(num='%sR%d' % (home, len(by.get(home, [])) + 1),
                 path=path, stem=stem[:-3] if stem.endswith('.py') else stem,
                 claim=claim))
    return by, seen


def md_to_html(md, matrix_slot=True, stop_at_h2=None):
    """INTRODUCTION.md -> HTML. The introduction is mostly headings, paragraphs
    and one raw <figure> for the matrix; nothing else is used, checked at build."""
    out, para, in_fig, seen_h2 = [], [], False, 0

    def inline(t):
        t = t.replace('&', '&amp;').replace('<', '&lt;')
        t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
        t = re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
        t = re.sub(r'`(.+?)`', r'<code>\1</code>', t)
        # $...$ was printing as raw LaTeX in the introduction; render it the way
        # the abstracts already do rather than leaving markup on the page.
        return re.sub(r'\$([^$]+)\$',
                      lambda m: '<span class="m">' + mathspan(m.group(1)) + '</span>', t)

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
  .m {{ font-family:'Iowan Old Style',Georgia,serif; font-style:italic;
        white-space:nowrap; }}
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
      <p class="more"><a href="{PAGES}/introduction.html">Read more →</a></p></div>
    </details><a href="{PAGES}/introduction.html">READ</a></li>
{paper_list}
</ul>

<h2>The apparatus</h2>
<p class="lede">What the papers rest on, and what can be re-run.</p>
<ul class="papers">
    <li><span class="pn">L</span><span class="ti"><b>The ledgers</b><span class="sub">
      the knowledge ledgers, numbered once for the whole corpus and grouped by
      what they test</span></span><a href="{PAGES}/ledgers.html">INDEX</a></li>
    <li><span class="pn">R</span><span class="ti"><b>The receipts</b><span class="sub">
      every runnable computation the papers cite, by the paper that owns
      it</span></span><a href="{PAGES}/receipts.html">INDEX</a></li>
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
    el.innerHTML = '<p class="more"><a href="' + PAGES_URL + '/frontier.html">'
      + 'Read more \u2192</a></p>';
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
    el.innerHTML = '<p class="more"><a href="' + PAGES_URL + '/frontier.html">'
      + 'Read more \u2192</a></p>';
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
  html += '<p class="more"><a href="' + PAGES_URL + '/frontier.html">' +
          'Read more \u2192</a></p>';
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

    def page(title, lede, body_html):
        return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">'
                '\n<meta name="viewport" content="width=device-width, initial-scale=1">'
                f'\n<title>{title} \u2014 The Shadow of Existence</title>\n'
                '<style>' + css + '</style>\n</head>\n<body>\n<div class="wrap">\n'
                '<p class="note"><a href="' + PAGES.rstrip('/') +
                '/live_edition.html">\u2190 The Shadow of Existence</a></p>\n'
                f'<h1>{title}</h1>\n<p class="lede">{lede}</p>\n' + body_html +
                '\n<footer>Generated from the repository. '
                '<a href="https://github.com/daryljanzen/shadow-of-existence">'
                'Source.</a></footer>\n</div>\n</body>\n</html>\n')

    # ── the ledgers, in the three groups the registry's numbering follows ──
    lr = ledger_rows()
    GROUPS = [('L1', "The corpus\u2019s own instruments",
               'A ledger about the others: which classical theorem each figure carries.'),
              ('math', 'Mathematics',
               'The field bakes proper \u2014 what bit, what bounced, and what the '
               'corpus already had under another name.'),
              ('method', 'Method and evidence',
               'The fields that test the corpus against measurement and technique '
               'rather than against a mathematical field.')]
    def grp(n):
        i = int(n[1:])
        return 'L1' if i == 1 else ('math' if i <= 20 else 'method')
    body = ''
    for gid, gname, gdesc in GROUPS:
        rows = [r for r in lr if grp(r['num']) == gid]
        if not rows:
            continue
        body += f'<h2>{gname}</h2>\n<p class="note">{gdesc}</p>\n<ul class="papers">\n'
        for r in rows:
            body += ('<li><span class="pn">' + r['num'] + '</span>'
                     '<span class="ti"><b>' + r['file'].replace('_LEDGER.md', '')
                     .replace('_', ' ').title() + '</b><span class="sub">'
                     + r['what'][:190] + '</span></span>'
                     '<a href="' + GH + '/' + r['file'] + '">OPEN</a></li>\n')
        body += '</ul>\n'
    with open(OUT_LEDG, 'w', encoding='utf-8') as fh:
        fh.write(page('The ledgers',
                      f'{len(lr)} knowledge ledgers, numbered once for the whole '
                      'corpus \u2014 so <b>L7</b> is the same ledger in every paper '
                      'that cites it.', body))
    print(f'  ledgers.html written: {len(lr)} ledgers in 3 groups.')

    # ── the receipts, by the paper that owns them ──
    by, _ = receipt_rows()
    total = sum(len(v) for v in by.values())
    titles = {num: t for num, t, _u, _s in
              [(n, tt.partition(':')[0], 0, 0) for n, tt, _x, _y in
               [(a, b, c, d) for a, b, c, d in papers]]}
    body = ''
    for home in sorted(by, key=lambda k: int(k[1:])):
        rows = by[home]
        body += (f'<h2>{home} \u2014 {titles.get(home, "")}</h2>\n'
                 f'<p class="note">{len(rows)} receipts.</p>\n<ul class="papers">\n')
        for r in rows:
            body += ('<li><span class="pn">' + r['num'] + '</span>'
                     '<span class="ti"><b>' + r['stem'].replace('_', ' ') + '</b>'
                     + ('<span class="sub">' + r['claim'][:180] + '</span>'
                        if r['claim'] else '') + '</span>'
                     '<a href="' + GH + '/receipts/' + r['path'] + '">PY</a></li>\n')
        body += '</ul>\n'
    with open(OUT_RCPT, 'w', encoding='utf-8') as fh:
        fh.write(page('The receipts',
                      f'{total} runnable receipts, numbered by the paper that owns '
                      'them \u2014 so <b>P3R7</b> here is <b>P3R7</b> in the paper.',
                      body))
    print(f'  receipts.html written: {total} receipts across {len(by)} papers.')

    print(f'  introduction.html written: {len(intro_page)} bytes, '
          f'matrix fetched into its figure.')
    print(f'  live_edition.html written: {len(papers)} papers listed, '
          f'{n_abs} with abstracts, frontier fetched at read time '
          f'(not embedded).')


if __name__ == '__main__':
    main()
