#!/usr/bin/env python3
"""
gen_live_edition.py -- builds BOOK_INTRO_cosmiCave/live_edition.html

** THE ONE DESIGN RULE, AND IT IS THE CORPUS'S OWN LESSON. **  The page does NOT
embed the frontier.  It FETCHES `THE_FRONTIER.md` from the repository at read
time and renders it in the browser.

  A page that baked in the open-row count would be a SECOND HOME for that count,
  and every second home in this corpus has gone stale -- the register's masthead
  (r4487), THE_PLAN's grain cell (r4479), OPEN_PROBLEMS_MAP (r4515), THE_FRONTIER's
  own headline (r4551).  The frontier's LIVE ROWS are generated from THE_REGISTER by
  regen_frontier.py; its per-row RUNWAY PROSE is an editorial digest held in that
  script and is NOT derived from the register (see its header, and
  corpus/check_frontier_current.py).  This page reads the artefact and
  owns no copy of it.

The paper list IS baked, because it changes on the scale of years and a wrong
title is visible on sight.

** THE THIRD-PARTY CDN IS GONE (r6475 corrects this header to the code). **  The
site serves its own PDFs, figures and data from the repository -- `CDN = RAW_GH`
below, and the body has said `NO THIRD-PARTY CDN` since the migration.  ** This
header went on describing jsDelivr after the code stopped using it **, which is
the header-versus-body divergence this corpus keeps finding: the body was right
and the paragraph a node reads first was not.  The read-time fetches are
`raw.githubusercontent.com/.../main/THE_FRONTIER.md` and the dependency matrix,
both verified 200.

Usage:  python3 scripts/gen_live_edition.py        (from the repo root)
"""
import os
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'live_edition.html')
OUT_INTRO = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'introduction.html')
OUT_EXPL = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'explainer.html')
OUT_FRONT = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'frontier.html')
OUT_LEDG = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'ledgers.html')
OUT_RCPT = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'receipts.html')
OUT_FORM = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'formalisation.html')
OUT_MAP = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'sitemap.xml')
OUT_ROB = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'robots.txt')
OUT_PAGES = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'PAGES.txt')

# The public hostname, used only for the sitemap, which must carry absolute URLs
# by the standard.  Everything else on the site stays relative.
SITE = os.environ.get('SITE_URL', 'https://shadow.cosmicave.org').rstrip('/')
GH = 'https://github.com/daryljanzen/shadow-of-existence/blob/main'
# ** NO THIRD-PARTY CDN. **  The site serves its own PDFs, figures and data from
# GitHub Pages: one origin, no cache lag, nothing to purge, and -- the reason it
# matters here -- a same-origin download is COUNTED by analytics where an
# outbound CDN click is not.  RAW is kept only as a last-resort link target for
# a reader who has the page open outside the site.
RAW_GH = 'https://raw.githubusercontent.com/daryljanzen/shadow-of-existence/main'
CDN = RAW_GH
RAW = 'https://raw.githubusercontent.com/daryljanzen/shadow-of-existence/main'
# Where the generated pages link to each other.  On GitHub Pages they sit beside
# one another, so a bare filename is correct AND has no cache lag; the CDN base
# is kept for anyone opening these files outside the site.  PDFs always come
# from the CDN, which is what a CDN is good at.
PAGES = os.environ.get('PAGES_BASE', '.')

# Where the PDFs are served from.  On the site they sit beside the pages, which
# is what makes a download SAME-ORIGIN -- analytics counts a same-origin file
# download automatically and an outbound CDN click only as a click, so serving
# them here is what turns "someone left for a CDN" into "someone downloaded P15".
PDF_BASE = os.environ.get('PDF_BASE', './pdf')

# Analytics tag, supplied at build time.  Empty by default: nothing is hardcoded
# and a local build carries no tracking at all.
ANALYTICS = os.environ.get('ANALYTICS_ID', '').strip()
_TAG = ('' if not ANALYTICS else
        '<script async src="https://www.googletagmanager.com/gtag/js?id='
        + ANALYTICS + '"></script>\n<script>window.dataLayer=window.dataLayer||[];'
        'function gtag(){dataLayer.push(arguments);}gtag("js",new Date());'
        'gtag("config","' + ANALYTICS + '");</script>')

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
      '%%RAW%%/BOOK_INTRO_cosmiCave/assets/dependency_matrix.html',
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
    # r7207: the ten symbols a census of every `$\token$` in the corpus found
    # rendering as NOTHING.  Six are ordinary LaTeX and four are the corpus's own
    # macros, expanded here to what their \newcommand says rather than guessed:
    # `\Hphys` and `\Tpk` from canonical_time / cosmogenesis, `\C` and `\St` from
    # algebroid / canonical_time.
    'Theta': '\u0398', 'varrho': '\u03f1', 'varphi': '\u03c6',
    'cdots': '\u22ef', 'lozenge': '\u25ca', 'Diamond': '\u25c7',
    # the turnaround's marker in P7's lap figure (fig:F-killing); unmapped it rendered as nothing
    'square': '\u25a1', 'Box': '\u25a1',
    'Hphys': 'H<sub>phys</sub>', 'Tpk': 'T<sub>peak</sub>',
    'C': '\U0001d49e', 'St': '\U0001d4ae<sub>t</sub>',
    'nu': '\u03bd', 'xi': '\u03be', 'pi': '\u03c0', 'rho': '\u03c1',
    'sigma': '\u03c3', 'tau': '\u03c4', 'phi': '\u03c6', 'chi': '\u03c7',
    'psi': '\u03c8', 'omega': '\u03c9', 'Phi': '\u03a6', 'Psi': '\u03a8',
    'Gamma': '\u0393', 'Delta': '\u0394', 'Sigma': '\u03a3',
    'times': '\u00d7', 'pm': '\u00b1', 'to': '\u2192', 'mapsto': '\u21a6',
    'leftrightarrow': '\u2194', 'in': '\u2208', 'infty': '\u221e',
    'approx': '\u2248', 'simeq': '\u2243', 'sim': '\u223c', 'cong': '\u2245',
    'rightarrow': '\u2192', 'longrightarrow': '\u27f6', 'leftarrow': '\u2190',
    'Rightarrow': '\u21d2', 'Leftrightarrow': '\u21d4', 'mid': '|',
    'bigcup': '\u22c3', 'bigcap': '\u22c2', 'cup': '\u222a', 'cap': '\u2229',
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
    # .strip(): the wrapper-unwrap leaves a separator space, and inside a
    # script that shows as 'H_ leaf' rather than 'H_leaf'.
    t = re.sub(r'\^\{([^{}]*)\}|\^(\S)',
               lambda m: '<sup>' + (m.group(1) or m.group(2)).strip() + '</sup>', t)
    return re.sub(r'_\{([^{}]*)\}|_(\S)',
                  lambda m: '<sub>' + (m.group(1) or m.group(2)).strip() + '</sub>', t)


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
    # Thin-space and spacing macros are punctuation, not letters, so the
    # macro-name rule never saw them and they reached the page as `\,`.
    t = t.replace('\\{', '\x01').replace('\\}', '\x02')
    # Escaped literals: the backslash is markup, the character is the content.
    for _c in '%$&#_':
        t = t.replace('\\' + _c, _c)
    # A line break and an alignment mark inside a math span: the span is one
    # line here, so they become a space rather than reaching the page as source.
    t = re.sub(r'\\\\\\\\', ' ', t)
    # r7209: an alignment mark can arrive DOUBLY escaped -- `&amp;amp;` -- when the
    # caller escapes a block that is then handed on and escaped again, which is what
    # happens to a display equation carried inside a theorem.  The single-layer form
    # stripped one `&amp;` and left a literal `amp;` on the page: three such on P9,
    # reading `8\pi p_\chi amp;= ...`.  Collapse every layer before stripping.
    while '&amp;' in t:
        t = t.replace('&amp;', '&')
    t = re.sub(r'(?<!\\)&', ' ', t)
    t = re.sub(r'\\[,;:!>]|\\ ', ' ', t)
    t = re.sub(r'\\(?:qquad|quad|thinspace|;|,)\b', ' ', t)
    t = _prep(t)
    t = re.sub(r'\\[dt]?frac\{([^{}]*)\}\{([^{}]*)\}', r'\1/\2', t)
    for _ in range(3):
        # A separator is kept for the same reason the bare form keeps one:
        # '\\in\\mathbb{R}' unwrapped in place becomes '\\inR', an unknown macro,
        # and the membership sign is lost with it.
        t = re.sub(r'\\(?:' + '|'.join(_UNWRAP) + r')\{([^{}]*)\}', r' \1', t)
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
    t = t.replace('{', '').replace('}', '')
    t = t.replace('\x01', '{').replace('\x02', '}')
    return re.sub(r'\s+', ' ', t).strip()


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
        # A separator is kept for the same reason the bare form keeps one:
        # '\\in\\mathbb{R}' unwrapped in place becomes '\\inR', an unknown macro,
        # and the membership sign is lost with it.
        t = re.sub(r'\\(?:' + '|'.join(_UNWRAP) + r')\{([^{}]*)\}', r' \1', t)
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


# ──────────────────────────────────────────────────────────────────────────────
# ** THE FORMALISATION PAGE (r7425, on 69's proposal of 2026-10-16). **  The join
#   `receipt → row → theorem` became a FIELD at r7419+71.2 (`receipt` on every row,
#   `decl` on every row with something built).  This reads it and publishes it.
#
# ** THREE REFUSALS, AND EACH ONE IS A RULING AND NOT A PRECAUTION. **
#   ⒜ A STATUS WITH NO WORDING raises.  69's own rule: "a class the inventory adds
#      later gets a line here before it is published.  The generator should refuse a
#      status that has no line, rather than print the bare label."  The ground is
#      measured: the inventory GAINED a class inside one cycle (`DONE (chartable
#      half)`, from 71's campaigns 21 and 23), so a generator that printed the bare
#      label would have published a heading with no sentence under it.
#   ⒝ A `decl` CELL THAT DOES NOT PARSE raises, via `decl_cells.parse_decl`, which
#      raises rather than returning a short list.
#   ⒞ A PAIR THAT IS NOT DECLARED WHERE THE CELL SAYS raises.  The page does not
#      publish a join it has not checked, whatever a gate elsewhere says: at r7423
#      the join gate was RED on correct data because it had its own parser, so a
#      page that trusted the gate's verdict would have been wrong in the other
#      direction.  The grammar AND the check both come from `scripts/decl_cells.py`,
#      so this page, that gate and any audit read one implementation.
#
# ** AND THE PAGE INVENTS NO MARK. **  69 declined "proved where marked" for the
#   structure class, on the ground that it "asks the page for a mark the generator
#   would have to invent -- a link is already the thing a proved row carries."  So a
#   name with a link is proved and a name without one is not, and there is no third
#   signal anywhere on the page.
def formalisation_rows():
    """(rows, wording, counts) -- the inventory joined to its wording and checked."""
    import sys as _sys
    _sys.path.insert(0, os.path.join(ROOT, 'scripts'))
    import decl_cells as dc

    wording = {}
    wpath = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                         'r7419_69_status_wording', 'WORDING.tsv')
    for line in open(wpath, encoding='utf-8').read().split('\n'):
        if not line.strip() or line.startswith('#'):
            continue
        f = line.split('\t')
        if len(f) >= 3 and f[0] != 'status':
            wording[f[0]] = (f[1], f[2])

    gaps = {}
    gpath = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                         'r7419_69_status_wording', 'GAPS.tsv')
    for line in open(gpath, encoding='utf-8').read().split('\n'):
        f = line.split('\t')
        if len(f) >= 2 and f[0] not in ('gap', ''):
            gaps[f[0]] = f[1]

    # ** PER-ROW PUBLIC TEXT LIVES IN 69'S OWN DIRECTORY, keyed by row index. **  r7425 built
    #   this with a gap lookup only, and the probe that proved the positive path found there was
    #   nowhere for a per-row phrase to COME FROM -- so a class whose sentence promises text
    #   beside it could never be satisfied for any row outside `LIBRARY GAP`.  A refusal with no
    #   reachable remedy is not a refusal, it is a wall.  This file is the remedy's address.
    # ** AN OPTIONAL THIRD COLUMN: the .lean file the PHRASE links to (r7429, on 71's question). **
    #   69's sentence for the structure class promises "what can be calculated about it is named
    #   beside it, WITH A LINK TO THE PROOF WHERE ONE IS BUILT".  71 built row 18's residue at
    #   campaign 26, from P7's own order3_bridge, and correctly kept the row's `decl` EMPTY -- a
    #   decl would make the page say the ROW is proved, and the row's object is the full S_3
    #   monodromy, which 71 showed local transpositions do not give.  So the link belongs on the
    #   PHRASE and not on the row, which is exactly the distinction 69's sentence already draws.
    beside_by_row, beside_link = {}, {}
    bpath = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                         'r7419_69_status_wording', 'ROW_TEXT.tsv')
    if os.path.exists(bpath):
        for line in open(bpath, encoding='utf-8').read().split('\n'):
            f = line.split('\t')
            if len(f) >= 2 and f[0] not in ('index', '') and not f[0].startswith('#'):
                beside_by_row[f[0].strip()] = f[1].strip()
                if len(f) >= 3 and f[2].strip():
                    beside_link[f[0].strip()] = f[2].strip()

    # ** WHICH CLASSES PROMISE TEXT "BESIDE IT", read off 69's OWN SENTENCES and not
    #   from a list of mine -- so a reworded sentence changes this requirement with it. **
    promises = {st for st, (_h, sent) in wording.items() if 'beside it' in sent}

    _head, rows = dc.read_rows()
    out = []
    for r in rows:
        st = (r.get('status') or '').strip()
        if st not in wording:                                       # ⒜
            raise SystemExit(
                f"  ⛔ formalisation.html REFUSED: row {r.get('index')} carries the status "
                f"{st!r}, which has no line in WORDING.tsv.\n"
                f"     69 owns that file and the wording is its call.  The page is not written "
                f"rather than printing the bare label.")
        pairs = dc.parse_decl(r.get('decl'))                        # ⒝
        for path, name in pairs:
            ds = dc.declared_names(path)
            if ds is None:                                          # ⒞
                raise SystemExit(f"  ⛔ formalisation.html REFUSED: row {r.get('index')} names "
                                 f"{path}, which is not a file.")
            if name not in ds and name.split('.')[-1] not in ds:
                raise SystemExit(f"  ⛔ formalisation.html REFUSED: row {r.get('index')} names "
                                 f"{name}, which {path} does not declare.")
        # ** THE `what it needs next` CELL IS INTERNAL WORKING TEXT AND IS NOT PUBLISHED. **
        #   r7425 built this page once with that cell in it, looked at the result, and found
        #   `r7013 split ROW`, `REOPENABLE`, `r7411+71.2` and `CLASSIFICATION.tsv` on a public
        #   page -- node shorthand of exactly the kind the corpus bans from the papers.  The
        #   cell is used here only to LOOK UP a gap's plain name, never rendered.
        internal = (r.get('what it needs next') or '').strip()
        beside = beside_by_row.get((r.get('index') or '').strip(), '')
        if not beside and st == 'LIBRARY GAP':
            for g, plain in gaps.items():
                if g.lower() in internal.lower():
                    beside = plain
                    break
        if st in promises and not beside and not pairs:
            raise SystemExit(
                f"  \u26d4 formalisation.html REFUSED: row {r.get('index')} is {st!r}, whose "
                f"sentence promises a text 'beside it', and nothing plain is beside it.\n"
                f"     The `what it needs next` cell is internal working text and is not "
                f"published.\n     69 owns the public wording: add one line to "
                f"computations/beyond_the_wall/r7419_69_status_wording/ROW_TEXT.tsv\n"
                f"     as `<index>\\t<one plain phrase>`.")
        out.append(dict(index=r.get('index', ''), cls=r.get('class', ''), status=st,
                        beside=beside,
                        beside_link=beside_link.get((r.get('index') or '').strip(), ''), standin=(r.get('stand-in') or '').strip(),
                        receipts=dc.parse_receipt(r.get('receipt')), pairs=pairs))
    counts = {}
    for r in out:
        counts[r['status']] = counts.get(r['status'], 0) + 1
    return out, wording, counts


def receipts_with_a_proof():
    """{receipt stem: n_theorems} -- the mark receipts.html carries, from the same join."""
    try:
        rows, _w, _c = formalisation_rows()
    except SystemExit:
        raise
    mark = {}
    for r in rows:
        if not r['pairs']:
            continue
        for rc in r['receipts']:
            stem = os.path.splitext(os.path.basename(rc.rstrip('/')))[0]
            mark[stem] = mark.get(stem, 0) + len(r['pairs'])
    return mark


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


# ---------------------------------------------------------------- withdrawals, read not remembered
def _withdrawn_registry():
    """(assert-pattern, correction) from `corpus/check_withdrawn.py` -- imported, never copied"""
    try:
        import importlib.util
        p = os.path.join(ROOT, 'corpus', 'check_withdrawn.py')
        spec = importlib.util.spec_from_file_location('_cw', p)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return [(re.compile(e[1]), e[3]) for e in mod.REGISTRY if len(e) >= 4]
    except Exception:
        return []


_WD = None


def withdrawn_note(stem):
    """for a receipt whose NAME states a withdrawn claim, the correction to print beside it.

    ** The test is the REGISTRY's OWN assertion pattern, run against the title as the page prints
    it -- the same pattern `check_withdrawn` runs against the page -- and not a similarity between
    the slug and the filename.  A fuzzy name match would be a second, weaker registry maintained
    here by accident; this way a site the gate would flag is a site this function annotates, and
    the two cannot drift apart. **
    """
    global _WD
    if _WD is None:
        _WD = _withdrawn_registry()
    title = stem.replace('_', ' ')
    for pat, correction in _WD:
        if pat.search(title):
            return '\u2317 ' + correction
    return ''


def md_to_html(md, matrix_slot=True, stop_at_h2=None):
    """INTRODUCTION.md -> HTML. The introduction is mostly headings, paragraphs
    and one raw <figure> for the matrix; nothing else is used, checked at build."""
    # ** r7179: YAML frontmatter is TREE metadata and never page content. **  A published source
    #   is also a document of the tree -- it carries `kind:` for `classify_documents` and
    #   `current:` for `check_currency` -- and without this the first thing a reader of the page
    #   would see is those two lines.  Stripped here rather than at each call site, so a source
    #   that gains frontmatter later does not publish it.
    md = re.sub(r'\A---\n.*?\n---\n', '', md, count=1, flags=re.S)
    out, para, in_fig, seen_h2 = [], [], False, 0

    def inline(t):
        t = t.replace('&', '&amp;').replace('<', '&lt;')
        # [text](https://...) -> a link, so a document can point at its sources.
        t = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)', r'<a href="\2">\1</a>', t)
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

    in_comment = False
    for line in md.split('\n'):
        st = line.strip()
        # HTML comments are for the source, not the page: EXPLAINER.md's watch markers
        # (corpus/check_explainer_pins.py) sit on their own lines above the paragraphs they
        # pin, and inline() escapes '<', so without this skip they would print as text.
        if in_comment or st.startswith('<!--'):
            in_comment = '-->' not in st
            continue
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
        # The explainer's figures (69, r-explainer-figures): one source line
        #   `![caption](fig/explainer/NAME.png)` becomes a captioned image.  The src
        #   stays relative, so the page served from the site and the page printed to
        #   PDF from BOOK_INTRO_cosmiCave/ both resolve it; pages.yml copies the
        #   directory into `_site/fig/explainer/`.
        mi = re.match(r'^!\[(.+)\]\((fig/[\w./-]+\.(?:png|svg))\)$', st)
        if mi:
            flush()
            alt = re.sub(r'[*`$]', '', mi.group(1)).replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;')
            out.append(f'<figure class="ex"><img src="{mi.group(2)}" alt="{alt}" loading="lazy">'
                       f'<figcaption>{inline(mi.group(1))}</figcaption></figure>')
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
    # ** VALIDATE THE FORMALISATION JOIN BEFORE ANY PAGE IS WRITTEN. **  r7425 built this
    #   generator with the check beside the page it feeds, and the first refusal fired AFTER
    #   receipts.html had been written with a link to a formalisation.html that did not exist.
    #   A partial write is worse than a refusal, so the join is checked first and the whole
    #   run refuses together.
    #   ** AND THE REFUSAL IS SCOPED TO THIS ONE UNIT, NOT TO THE RUN. **  `pages.yml` runs
    #   this script to deploy the site, so refusing the whole run would take the published
    #   book down over the wording of three rows.  `formalisation.html` and the `receipts.html`
    #   proof mark are ONE unit -- the mark links to the page -- so they are skipped together
    #   and there is never a dead link.  The refusal prints, loudly, every run until it clears.
    try:
        _fcheck = formalisation_rows()
        _pmark = receipts_with_a_proof()
        _frefusal = None
    except SystemExit as e:
        _fcheck, _pmark, _frefusal = None, {}, str(e)

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
        papers.append((num, t, f'{PDF_BASE}/{stem}.pdf', stem))

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

    # The plain-language explainer: the same story the eighteen papers tell,
    # told without the formalism.  Generated from EXPLAINER.md by this same run,
    # like the introduction, so it is a live page of the book and is edited in
    # one place.  Its title is the source's own first heading, and the index and
    # the page both append the one subtitle that says what it is.
    src_e = os.path.join(ROOT, 'EXPLAINER.md')
    expl_full, expl_title, expl_excerpt = '', '', ''
    if os.path.exists(src_e):
        md_e = open(src_e, encoding='utf-8', errors='replace').read()
        mt = re.search(r'(?m)^# (.+)$', md_e)
        expl_title = mt.group(1).strip() if mt else 'The explainer'
        expl_full = md_to_html(md_e, matrix_slot=False)
        # The index shows the opening, everything before the first section.
        expl_excerpt = md_to_html(md_e.split('\n## ', 1)[0], matrix_slot=False)
    EXPL_SUB = 'A Plain Language Explainer of This Cosmology'
    print(f'  explainer: {len(expl_full)} chars of HTML from EXPLAINER.md')

    rows, n_abs = [], 0
    for num, t, url, stem in papers:
        head, _, tail = t.partition(':')
        sub = f'<span class="sub">{tail.strip()}</span>' if tail.strip() else ''
        chap = (PAGES.rstrip('/') + '/paper_' + num + '.html')
        link = ('<span class="two"><a href="' + chap + '">READ</a>'
                + (f'<a href="{url}">PDF</a>' if url else '') + '</span>')
        paras, cut = abstract_of(stem)
        if paras:
            n_abs += 1
            body = ''.join(f'<p>{x}</p>' for x in paras)
            if cut:
                body += ('<p class="more"><a href="' + PAGES.rstrip('/')
                         + '/paper_' + num + '.html">Read more \u2192</a></p>')
            rows.append(
                f'    <li><details><summary><span class="pn">{num}</span>'
                f'<span class="ti"><b>{head.strip()}</b>{sub}</span></summary>'
                f'<div class="abs">{body}</div></details>{link}</li>')
        else:
            rows.append(
                f'    <li><span class="pn">{num}</span>'
                f'<span class="ti"><b>{head.strip()}</b>{sub}</span>{link}</li>')
    paper_list = '\n'.join(rows)

    expl_row = ''
    if expl_full:
        expl_row = (
            '    <li><details><summary><span class="pn">PLAIN</span>'
            '<span class="ti"><b>' + expl_title + ': ' + EXPL_SUB + '</b>'
            '<span class="sub">the whole picture told without the formalism: '
            'where the universe comes from, what crosses its beginning, why it '
            'speeds up when it does, and what it says about matter</span></span>'
            '</summary><div class="abs">' + expl_excerpt +
            '<p class="more"><a href="' + PAGES.rstrip('/') +
            '/explainer.html">Read more \u2192</a></p></div></details>'
            '<span class="two"><a href="' + PAGES.rstrip('/') +
            '/explainer.html">READ</a><a href="' + PDF_BASE +
            '/explainer.pdf">PDF</a></span></li>')

    # ** the nav entry exists only if the page does -- a dead link on the index is the one
    #   defect a reader meets first. **
    formalisation_nav = ('' if not _fcheck else
        '    <li><span class="pn">F</span><span class="ti"><b>The formalisation</b>'
        '<span class="sub">\n      every calculation the papers rest on, and whether it is '
        'also proved in\n      Lean</span></span><a href="' + PAGES +
        '/formalisation.html">INDEX</a></li>')

    html = rf"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">{_TAG}
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
  .two {{ flex:0 0 5.4rem; text-align:right; padding-top:.6rem; }}
  .two a {{ display:inline-block; margin-left:.5rem; color:var(--pole);
            text-decoration:none; font-size:.78rem; letter-spacing:.06em; }}
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
  .intro figure.ex img {{ display:block; max-width:100%; max-height:30rem; width:auto; height:auto; margin:0 auto; }}
  .intro figure.ex {{ break-inside:avoid; }}
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
{expl_row}
    <li><details id="introbox"><summary><span class="pn">INTRO</span>
      <span class="ti"><b>Introduction</b><span class="sub">a map for reading the corpus
      proper: what the programme is, the eighteen chapters and how they depend on one another, where to come in,
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
{formalisation_nav}
</ul>

<h2>The open edge</h2>
<p class="lede">This is not a summary written for the page. It is fetched from the
programme's own frontier, which is generated from its register of open problems,
and it changes when the work does.</p>
<div id="frontier"><p class="status">Fetching the current frontier…</p></div>

<footer>
Source: <a href="https://github.com/daryljanzen/shadow-of-existence">the
repository</a>. Papers served from the repository; the frontier read live at page load.
</footer>

</div>
<script>
const PAGES_URL = '{PAGES}';
(async function () {{
  const el = document.getElementById('frontier');
  // Site-local first: the deploy rebuilds on every push, so this copy is as
  // current as the repository and needs no third party to serve it.
  const urls = ['./THE_FRONTIER.md', '{RAW}/THE_FRONTIER.md'];
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
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">' + _TAG + '\n'
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

    if expl_full:
        print_css = (
            '.expl { padding-left:0; font-size:1.04rem; line-height:1.7 } '
            '.expl h3 { font-size:1.3rem; margin:2.6rem 0 .7rem; font-weight:600 } '
            '.expl p { margin:0 0 1.05rem } '
            '@media print { .noprint { display:none } body { background:#fff } '
            '.wrap { max-width:none; padding:0 } '
            'h2 { break-after:avoid } p { orphans:3; widows:3 } '
            '@page { margin:22mm 20mm } }')
        expl_page = (
            '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">' + _TAG + '\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>' + expl_title + ': ' + EXPL_SUB + '</title>\n'
            '<style>' + css + print_css + '</style>\n</head>\n<body>\n<div class="wrap">\n'
            '<p class="note noprint"><a href="' + PAGES.rstrip('/') + '/live_edition.html">\u2190 The '
            'Shadow of Existence</a> \u00b7 <a href="' + PDF_BASE + '/explainer.pdf">PDF</a></p>\n'
            '<h1>' + expl_title + '</h1>\n'
            '<p class="lede">' + EXPL_SUB + '</p>\n'
            '<p class="note">Daryl Janzen</p>\n'
            '<div class="intro expl">\n' + expl_full + '\n</div>\n'
            '<footer>A live page of <i>The Shadow of Existence</i>, revised as the '
            'work is. The eighteen papers it draws on are at '
            '<a href="https://shadow.cosmicave.org">shadow.cosmicave.org</a>; '
            '<a href="https://github.com/daryljanzen/shadow-of-existence">source</a>.'
            '</footer>\n</div>\n</body>\n</html>\n')
        with open(OUT_EXPL, 'w', encoding='utf-8') as fh:
            fh.write(expl_page)
        print(f'  explainer.html written: {len(expl_page)} bytes.')

    # The frontier gets a page too, for the same reason: a reader following
    # "Read more" should land on a page of the book, never on a markdown file.
    fr = frontier_rows()
    body = ''.join(
        f'<div class="row"><span class="id">{i}</span>'
        f'<span class="what">{q}</span>'
        + (f'<span class="disc">{n}</span>' if n else '') + '</div>'
        for i, q, n in fr)
    front_page = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">' + _TAG + '\n'
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
        return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">' + _TAG + ''
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
    # ** r7425: the proof mark comes from the SAME join the formalisation page reads,
    #   so a receipt cannot be marked PROVED here and unproved there. **
    proof_mark = _pmark
    rcpt_marked = 0
    titles = {num: t for num, t, _u, _s in
              [(n, tt.partition(':')[0], 0, 0) for n, tt, _x, _y in
               [(a, b, c, d) for a, b, c, d in papers]]}
    body = ''
    for home in sorted(by, key=lambda k: int(k[1:])):
        rows = by[home]
        body += (f'<h2>{home} \u2014 {titles.get(home, "")}</h2>\n'
                 f'<p class="note">{len(rows)} receipts.</p>\n<ul class="papers">\n')
        for r in rows:
            # ** r7179: THIS PAGE PRINTS EVERY RECEIPT'S FILENAME AS A BOLD ASSERTION. **  A receipt
            #   whose headline claim was later withdrawn keeps its name -- the name is the record of
            #   what was tried -- so without the correction beside it the page ASSERTS on a public
            #   page what the corpus withdrew.  The correction is taken from the one registry that
            #   holds withdrawals (`corpus/check_withdrawn.py`), never written here, so a withdrawal
            #   recorded there reaches this page without anyone remembering to come back.
            sub = r['claim'][:180] if r['claim'] else ''
            wd = withdrawn_note(r['stem'])
            if wd:
                sub = (sub + ' \u2014 ' if sub else '') + wd
            nth = proof_mark.get(r['stem'])
            if nth:
                rcpt_marked += 1
                sub = ((sub + ' \u2014 ' if sub else '')
                       + ('proved in Lean: %d theorem%s'
                          % (nth, '' if nth == 1 else 's')))
            body += ('<li><span class="pn">' + r['num'] + '</span>'
                     '<span class="ti"><b>' + r['stem'].replace('_', ' ') + '</b>'
                     + ('<span class="sub">' + sub + '</span>' if sub else '') + '</span>'
                     + ('<a href="' + PAGES + '/formalisation.html">PROVED</a>'
                        if nth else '')
                     + '<a href="' + GH + '/receipts/' + r['path'] + '">PY</a></li>\n')
        body += '</ul>\n'
    with open(OUT_RCPT, 'w', encoding='utf-8') as fh:
        fh.write(page('The receipts',
                      f'{total} runnable receipts, numbered by the paper that owns '
                      'them \u2014 so <b>P3R7</b> here is <b>P3R7</b> in the paper. '
                      + ('A receipt whose calculation is also proved in Lean carries '
                         f'<b>PROVED</b>, linked to the theorem; <a href="{PAGES}/'
                         'formalisation.html">the formalisation index</a> lists every row.'
                         if _fcheck else ''),
                      body))
    print(f'  receipts.html written: {total} receipts across {len(by)} papers, '
          f'{rcpt_marked} of them carrying a proof mark.')

    # ** AND THE REFUSAL IS SCOPED TO THIS ONE UNIT, NOT TO THE RUN. **  `pages.yml` runs this
    #   script to deploy the site, so refusing the whole run would take the published book down
    #   over the wording of three rows.  `formalisation.html` and the `receipts.html` proof mark
    #   are ONE unit -- the mark links to the page -- so they are skipped TOGETHER and there is
    #   never a dead link.  The refusal prints every run until it clears.
    if _frefusal:
        print()
        print(_frefusal)
        print('  \u21d2 formalisation.html and the receipts.html proof mark are NOT written:'
              ' the two are one unit and are skipped together.  The rest of the site is built.')
        print()
    else:
        # \u2500\u2500 the formalisation, by status, in 69's own words \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
        frows, fwording, fcounts = _fcheck
        STATUS_ORDER = ['DONE', 'DONE (chartable half)', 'LIMIT OF A DONE ROW',
                        'ORDER: ENGINE-REACHABLE', 'GENERIC-METRIC IDENTITY',
                        'ROW: A DIFFERENT KIND', 'LIBRARY GAP']
        # ** THE ORDER IS DECLARED AND ASSERTED, for turn_gates.sh's own reason: a status
        #   the inventory adds later must not fall off the bottom of a hand-written list.
        missing = [s for s in fcounts if s not in STATUS_ORDER]
        if missing:
            raise SystemExit(f'  \u26d4 formalisation.html REFUSED: status(es) {missing} are worded '
                             f'but absent from this page\u2019s display order.')
        fbody = ''
        npairs = sum(len(r['pairs']) for r in frows)
        for st in STATUS_ORDER:
            rows_s = [r for r in frows if r['status'] == st]
            if not rows_s:
                continue
            heading, sentence = fwording[st]
            fbody += (f'<h2>{heading}</h2>\n<p class="note">{sentence}</p>\n'
                      f'<p class="note">{len(rows_s)} of {len(frows)} rows.</p>\n'
                      '<ul class="papers">\n')
            for r in rows_s:
                links = ''
                for path, name in r['pairs']:
                    short = name.rpartition('.')[2] or name
                    links += (f' <a href="{GH}/computations/formalisation/lean/{path}">'
                              f'{short}</a>')
                what = r['beside']
                if what and r['beside_link']:
                    what = (f'<a href="{GH}/computations/formalisation/lean/'
                            f'{r["beside_link"]}">{what}</a>')
                sub = (what + (' \u2014 ' if what and links else '')) if what else ''
                fbody += ('<li><span class="pn">' + r['index'] + '</span>'
                          '<span class="ti"><b>' + (r['standin'][:110] or r['cls']) + '</b>'
                          + ('<span class="sub">' + sub + links + '</span>'
                             if (sub or links) else '') + '</span>'
                          + ('<a href="' + GH + '/' + r['receipts'][0] + '">RECEIPT</a>'
                             if r['receipts'] else '<span class="pn">\u2014</span>') + '</li>\n')
            fbody += '</ul>\n'
        with open(OUT_FORM, 'w', encoding='utf-8') as fh:
            fh.write(page('The formalisation',
                          f'Each of these {len(frows)} rows is one calculation a receipt '
                          'performs and a paper relies on. This says, for each, whether that '
                          'calculation is also proved in Lean \u2014 and where a proof exists, '
                          'the theorem is linked. Beside a row, each theorem name links to its proof, and a description shown there without a link is a calculation not yet proved. '
                          f'{npairs} theorems are linked across '
                          f'{sum(1 for r in frows if r["pairs"])} rows.', fbody))
        print(f'  formalisation.html written: {len(frows)} rows, {npairs} theorems linked, '
              f'{len(fcounts)} statuses, all worded.')

    # ── the one page list, and the manifest the deploy copies from ────────
    # Without a sitemap a search engine has to FIND twenty-odd pages by
    # crawling, and with no inbound links it may not find them at all.
    #
    # ** THIS LIST HAS THREE CONSUMERS AND USED TO HAVE A FOURTH THAT WAS A
    #    COPY. **  The index's nav, the sitemap below and `PAGES.txt` are all
    #    built from `pages` here.  `pages.yml`'s assemble step carried its own
    #    hand-written list of the files to copy into `_site`, and `r7425` could
    #    add `formalisation.html` to this list and to the nav but not to a list
    #    it does not contain.  The page was generated, linked from the index,
    #    linked 68 times from `receipts.html` and listed in the sitemap -- and
    #    never copied.  The site served a 404 at a URL it was itself
    #    advertising to search engines, for ten hours and every deploy since.
    #    ⇒ *A copy of a list is a claim about the list at the moment it was
    #    copied* (`r7411`), and the workflow's copy was a claim from before the
    #    page existed.  The remedy is not to repair the copy but to delete it:
    #    the deploy now reads `PAGES.txt`.
    #
    # ** AND IT IS CHECKED AGAINST THE DISK, NOT AGAINST THE INTENTION. **  Two
    #    of the writes above are conditional -- `explainer.html` on there being
    #    an explainer, `formalisation.html` on the join clearing -- so a list of
    #    what this script MEANT to write is a third thing that can drift from
    #    what is there.  The old comment here claimed the sitemap was
    #    "generated from what was actually written": it was generated from what
    #    was INTENDED, which is the weaker claim and is the one that failed.
    #    Every entry is now stat'd before it is named.  Refusing is safe at
    #    this point because nothing has been deployed yet.
    import datetime
    today = datetime.date.today().isoformat()
    pages = ['', 'introduction.html', 'explainer.html', 'frontier.html',
             'ledgers.html', 'receipts.html']
    if _fcheck:
        pages.append('formalisation.html')
    pages += ['paper_%s.html' % num for num, _t, _u, _s in papers]

    manifest, bad = [], []
    for rel in pages:
        fn = 'live_edition.html' if rel == '' else rel
        fp = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', fn)
        if not os.path.exists(fp):
            bad.append(fn + ' (never written)')
        elif os.path.getsize(fp) == 0:
            bad.append(fn + ' (empty)')
        if fn not in manifest:
            manifest.append(fn)
    if bad:
        raise SystemExit(
            '  ⛔ PAGES.txt REFUSED: the page list names ' + ', '.join(bad)
            + '.\n  The sitemap and the deploy both read this list, so a name in '
              'it that is not\n  on disk is a 404 with a sitemap entry pointing '
              'straight at it.')
    with open(OUT_PAGES, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(manifest) + '\n')
    print(f'  PAGES.txt: {len(manifest)} pages, each verified non-empty on disk; '
          'the deploy copies these and keeps no list of its own.')

    urls = []
    for rel in pages:
        # The index is listed once, at the root, rather than twice.
        loc = SITE + '/' + rel
        pri = '1.0' if rel == '' else ('0.8' if rel.startswith('paper_')
                                       else '0.7')
        urls.append('  <url><loc>%s</loc><lastmod>%s</lastmod>'
                    '<priority>%s</priority></url>' % (loc, today, pri))
    with open(OUT_MAP, 'w', encoding='utf-8') as fh:
        fh.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                 + '\n'.join(urls) + '\n</urlset>\n')
    with open(OUT_ROB, 'w', encoding='utf-8') as fh:
        fh.write('User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % SITE)
    print(f'  sitemap.xml: {len(urls)} urls; robots.txt written.')

    print(f'  introduction.html written: {len(intro_page)} bytes, '
          f'matrix fetched into its figure.')
    print(f'  live_edition.html written: {len(papers)} papers listed, '
          f'{n_abs} with abstracts, frontier fetched at read time '
          f'(not embedded).')


if __name__ == '__main__':
    main()
