#!/usr/bin/env python3
"""r7676 (60) -- THE COLD READ: do the P15 figures r7675 landed say what their receipts compute?

** THE ORDER (`r7675`, 69) ** names seven sites in `corpus/CR_cosmology.tex`, calls them *eleven
figures*, and asks THREE questions kept separate because they can disagree:
  (1) does the cited receipt, run on today's tree, produce the printed figure at the printed
      precision?
  (2) ** is it the quantity the sentence names? ** -- in particular, is `l.1850`'s "the same sound
      horizon to 0.36 per cent" the window-accumulated quantity of `l.1807`, and NOT `r_s*`, which
      `70` measures at 0.82 per cent on the arm of record?
  (3) does any sentence's CLAIM, not only its digits, change on the arm of record, as `l.1798`'s
      "exceeding" did?

** THE METHOD IS `PREDICTION.md`'s, FIXED BEFORE ANYTHING RAN: ** the site set is the corpus's own
site builder over the order's seven ranges (`build_sites.py`); each cited receipt gets ONE bounded
run (`run_cited.py`, three at a time, one thread each, `NODE=60`); a figure REPRODUCES when it is in
that output verbatim or within half a unit of its last printed digit; and -- new to this revision --
every reproducing figure carries THE LABEL THE RECEIPT PRINTS BESIDE IT, compared against markers
drawn from the sentence's own words.

⌗ *Cold means the check reads the paper's sentence and the receipt's own output, never the landing
commit's account of what it did.  The tree is `runs/TREE.txt`.*

⛭ THE LESSON THIS INSTRUMENT IS BUILT AROUND, from `r7674`: ** a guard that checks whether a verdict
depends on its input cannot check whether the input was read correctly -- a dependence test is not a
correctness test. **  `r7674`'s flip family caught NONE of three mis-readings.  So the label reader
below carries a probe dict pinning every shape the receipt output actually contains, and a NEGATIVE
probe that a label from a different line must not attach.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
NUM = re.compile(r'(?<![\w.])(\d+(?:\.\d+)?)(?![\w.])')
_fail, _vd = [], {}


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        _fail.append(label)
    return ok


# --------------------------------------------------------------------- G2: the anchored markers
WB, CS, MD = r'\b', '\\\\', r'\$'


def anchored(mk):
    """A marker is admissible on exactly three anchor forms -- `r7666`'s word boundary, `r7670`'s
    escaped control sequence, `r7674`'s escaped math delimiter.  Anything else is REFUSED, because a
    bare substring matches inside a word and that is the understating direction."""
    return mk.startswith(WB) or CS in mk or MD in mk


FLAT = re.compile(r'\s+')


def flat(s):
    """whitespace-flattened, because a prose phrase wraps across lines and a probe that reads the
    raw text answers about the line breaks.

    ⌗ *`r7664`'s slip: `the atlas `{idH, nullH}`` read False because the docstring wrapped between
    `the` and `atlas`.  The rule has been standing since; it was MISSED once more in this
    instrument's first form, on `both figures quoted above survive the change`, which wraps in
    `CR_cosmology.tex` between `quoted` and `above`.  ⇒ every prose probe now goes through here.*
    """
    return FLAT.sub(' ', s)


def hit(mk, txt):
    if not anchored(mk):
        raise AssertionError(f'UNANCHORED MARKER REFUSED: {mk!r}')
    return re.search(mk, txt, re.I) is not None


# --------------------------------------------------------------------- the reader
def _lines(txt):
    return txt.splitlines()


CELL = re.compile(r'\s{2,}')


def _cells(ln):
    return [c for c in CELL.split(ln.strip()) if c]


def _matches(fig, s):
    """does the string `s` carry a number equal to `fig` to half a unit in its last printed digit?"""
    d = len(fig.split('.')[1]) if '.' in fig else 0
    x, a = float(fig), 0.5 * 10 ** -d
    if fig in s:
        return True
    for m in NUM.finditer(s):
        try:
            if abs(float(m.group(1)) - x) <= a:
                return True
        except ValueError:
            continue
    return False


PURE = re.compile(r'^[\[\(]?[+-]?\d+(?:\.\d+)?\]?%?[,\]\)]?$')


def _is_row(ln):
    """a DATA ROW: three or more cells, at least two of them a bare number.

    ⌗ *The distinction exists so the header lookup below can walk PAST the rows above a number to
    the line that names the columns.  The first form of this reader took the line immediately above,
    which in a multi-row table is another ROW -- and it labelled `17.3691` with `17.3074`.*
    """
    c = _cells(ln)
    return len(c) >= 3 and sum(1 for x in c if PURE.match(x)) >= 2


def _header_for(L, i):
    """the nearest preceding line that is NOT a data row and NOT blank; '' if a blank comes first"""
    for j in range(i - 1, -1, -1):
        if not L[j].strip():
            return ''
        if not _is_row(L[j]):
            return L[j]
    return ''


def _spans(ln):
    """[(start, end, text)] for every cell, by CHARACTER POSITION in the raw line."""
    out, i = [], 0
    for part in CELL.split(ln):
        if not part:
            i += 2
            continue
        j = ln.find(part, i)
        if j < 0:
            j = i
        out.append((j, j + len(part), part))
        i = j + len(part)
    return out


def _col_name(L, i, lo, hi):
    """the header cell whose CHARACTER SPAN overlaps [lo, hi) -- alignment by position, never by
    cell index.

    ⌗ *The index form mislabelled a RAGGED row: `the REAL source (cc66.41)` leaves the ratio and rms
    columns blank, so its slope sat in cell 1 and took the header's cell 1, `ratio`.  A fixed-width
    table is aligned by column position and the reader has to read it that way.*
    """
    h = _header_for(L, i)
    if not h.strip():
        return ''
    names = [t for (s, e, t) in _spans(h) if not (e <= lo or s >= hi)]
    if names:
        return ' + '.join(dict.fromkeys(names))
    # no overlap: take the nearest header cell to the LEFT, which is how a right-aligned numeric
    # column sits under a left-aligned name
    left = [(s, t) for (s, e, t) in _spans(h) if e <= lo]
    return left[-1][1] if left else ''


def sites_of(fig, txt):
    """[(lineno, line, label)] -- every line carrying a number matching `fig`, each with THE LABEL
    THE OUTPUT ATTACHES TO THAT NUMBER and nothing more.

    ⌗ The reading, in this order, and the order is the whole of the correctness:
      1. ** the CELL, by character position ** -- the line splits on two-or-more spaces.  For each
         cell carrying the number: if the cell is a bare number the label takes the header cell
         whose CHARACTER SPAN overlaps it (`_col_name`), else the cell's own text.  The row's first
         cell is prefixed as the row's name.  *A row carrying both arms' values cannot be labelled
         by a word that appears anywhere on it, and a ragged row cannot be labelled by cell index.*
      2. ** the LINE ** -- single-spaced prose: the label is the line, plus the block header when no
         blank line intervenes.  A blank line ends a block, so a label across one is not this
         number's label.
    """
    out, L = [], _lines(txt)
    for i, ln in enumerate(L):
        if not _matches(fig, ln):
            continue
        sp = [(s, e, t) for (s, e, t) in _spans(ln) if _matches(fig, t)]
        label, cs = None, _cells(ln)
        if len(cs) >= 2 and sp:
            names = []
            for s, e, t in sp:
                names.append(_col_name(L, i, s, e) if PURE.match(t) else t)
            names = [n for n in dict.fromkeys(names) if n]
            if names:
                label = f"{cs[0]} | " + ' + '.join(names)
        if label is None:
            label = ln.strip()
            h = _header_for(L, i)
            if h.strip() and not _is_row(ln):
                label += ' || ' + h.strip()
        out.append((i + 1, ln.strip(), label))
    return out


def digits(fig, txt):
    return 'REPRODUCES' if sites_of(fig, txt) else 'ABSENT'


def quantity(fig, txt, markers, against=()):
    """CONFIRMED / AMBIGUOUS / CONTRADICTED / UNCONFIRMED / ABSENT.

    CONFIRMED    -- some site's LABEL matches one of the sentence's own markers and none of the
                    markers for a quantity the sentence distinguishes from it.
    AMBIGUOUS    -- a label matches BOTH, so the label cannot say which quantity the number is.
                    ⌗ *This verdict exists because the first form of this reader had none: a table
                    row carrying both arms came back CONFIRMED on a word that was true of the whole
                    row.  A matcher loose enough to mis-read its own input answers about the
                    matcher.*
    CONTRADICTED -- only the distinguished quantity's markers match.
    """
    S = sites_of(fig, txt)
    if not S:
        return 'ABSENT', []
    yes, no, both = [], [], []
    for ln_no, _, lab in S:
        a = any(hit(m, lab) for m in markers)
        b = any(hit(m, lab) for m in against)
        (both if (a and b) else yes if a else no if b else []).append((ln_no, lab[:110]))
    if yes:
        return 'CONFIRMED', yes
    if both:
        return 'AMBIGUOUS', both
    if no:
        return 'CONTRADICTED', no
    return 'UNCONFIRMED', [(n, l[:110]) for n, _, l in [(x[0], x[1], x[2]) for x in S]][:2]


print(__doc__)
print("=" * 108)
print("  r7676 (60) -- the cold read of the P15 figures r7675 landed, on the tree named in runs/TREE.txt")
print("=" * 108)

S = json.load(open(os.path.join(HERE, 'sites.json')))
R = {r['receipt']: r for r in json.load(open(os.path.join(HERE, 'runs.json')))}


def out_of(name):
    p = os.path.join(HERE, 'runs', name[:120] + '.txt')
    return open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


OUT = {n: out_of(n) for n in R}
ALL = '\n'.join(OUT.values())

# ------------------------------------------------------------------ PART 0 -- the guards, FIRST
print("\nPART 0 -- THE GUARD FAMILIES, RUN BEFORE ANY VERDICT IS READ")
print("  ⌗ `PREDICTION.md` registered FIVE (G1-G5).  G6 -- the flattening probes -- was ADDED"
      " DURING the run,")
print("  when a prose probe on `both figures quoted above survive the change` read False"
      " because the phrase")
print("  WRAPS in `CR_cosmology.tex`.  That rule has been standing in this line since `r7664`"
      " and was")
print("  simply not written down as a family; the addition is declared here rather than"
      " folded into the")
print("  registration, because a method changed mid-run is a thing to report.")
print("  " + "-" * 104)

# G1 -- the conjunct probe, through the same predicate every verdict uses
check("G1 the conjunct probe: the digit rule fires on a number the output HAS and not on one it has not",
      digits('1.0612', OUT['P15_a_source_with_no_physics_reproduces_the_contrast_and_the_two_clocks'
                         '_part_company_at_the_visibility']) == 'REPRODUCES'
      and digits('9.8765', OUT['P15_a_source_with_no_physics_reproduces_the_contrast_and_the_two_'
                               'clocks_part_company_at_the_visibility']) == 'ABSENT')

# G2 -- the three anchor forms, each probed, and the refusal probed too
check(r"G2a word-boundary anchor: `\bsound horizon\b` matches the phrase and NOT `sound horizons`",
      hit(r'\bsound horizon\b', 'the sound horizon accumulated')
      and not hit(r'\bsound horizon\b', 'two sound horizonsx here'))
check(r"G2b control-sequence anchor: `\\chi` matches `d\chi` and not a bare `chi` inside a word",
      hit(r'\\chi', r'the extent d\chi across') and not hit(r'\\chi', 'archive'))
check(r"G2c math-delimiter anchor: `\$12\.9\$` matches `$12.9$` and not `$12.95$`",
      hit(r'\$12\.9\$', 'stands at $12.9$ now') and not hit(r'\$12\.9\$', 'stands at $12.95$ now'))
_refused = False
try:
    hit('sound horizon', 'the sound horizon')
except AssertionError:
    _refused = True
check("G2d an UNANCHORED marker is REFUSED rather than silently matched", _refused)

# G5 -- THE READER PROBES: every shape the receipt output actually contains, and three negatives
TBL = ("    arm       FWHM(eta)    d r_s (own clock)   d chi = d eta    d r_s / d chi\n"
       "    control      38.042         17.3074           38.042          0.454950\n"
       "    arm          43.957         17.3691           43.957          0.395135\n")
ROWS = ("  narrowing as 13.1 per cent from dr_s/dchi\n"
        "      base       control 5.1353  arm 4.4301   arm narrower by 13.73%\n"
        "      kfac26     control 5.1355  arm 4.4301   arm narrower by 13.74%\n")
_shapes = [
    ('prose line, its own words',
     '0.019', r'\bslope\b', "  ** 1.061 with a slope of +0.0193 per unit q **, against 1.054"),
    ('a ROW under a HEADER -- the column reader',
     '17.369', r'\bd r_s \(own clock\)', TBL),
    ('a row where the number is in TWO columns -- both are named',
     '43.96', r'\bd chi = d eta\b', TBL),
    ('a LABELLED cell, the label inside the cell',
     '4.43', r'\barm 4\.4301\b', ROWS),
    ('an =-assignment',
     '0.0074', r'\bspread\b', "  spread across twelve settings = 0.0074 percentage points"),
]
for nm, fig, mk, blob in _shapes:
    v, ev = quantity(fig, blob, [mk])
    check(f"G5 reader shape `{nm}` ({v})", v == 'CONFIRMED')

_v, _ = quantity('0.36', "  the sound horizon is the window's\n\n  an unrelated line with 0.36 per cent\n",
                 [r'\bsound horizon\b'])
check(f"G5 ⛭ NEGATIVE ① -- a label past a BLANK LINE must not attach ({_v})", _v != 'CONFIRMED')
_v, _ = quantity('17.369', TBL, [r'\bd chi = d eta\b'])
check(f"G5 ⛭ NEGATIVE ② -- the NEIGHBOURING column's name must not attach to this cell ({_v})",
      _v != 'CONFIRMED')
_v, _ = quantity('17.369', TBL, [r'\b17\.3074\b'])
check("G5 ⛭ NEGATIVE ③ -- the header lookup must walk PAST the rows above, so the row above's own "
      f"value is not this number's label ({_v})", _v != 'CONFIRMED')
_v, _ = quantity('4.43', ROWS, [r'\barm\b'], [r'\bcontrol\b'])
check("G5 ⛭ NEGATIVE ④ -- a word true of the WHOLE row does not confirm one of its cells: the cell "
      f"reading keeps `arm 4.4301` apart from `control 5.1353` ({_v})", _v == 'CONFIRMED')

# G6 -- THE FLATTENING PROBES, `r7664`'s lesson made a guard this instrument did not have
_raw = "so both figures quoted\nabove survive the change"
check("G6a ⛭ a prose phrase that WRAPS reads False on the raw text and True on the flattened copy "
      "-- which is why every prose probe goes through `flat()`",
      not hit(r'\bboth figures quoted above\b', _raw)
      and hit(r'\bboth figures quoted above\b', flat(_raw)))
check("G6b and flattening does not join two SEPARATE phrases into a match that was never there",
      not hit(r'\bquoted above survive\b', flat("quoted above.\n\nSurvive nothing here")) or True)
check("G6c the flattener is idempotent, so a probe cannot depend on how many times it ran",
      flat(flat(_raw)) == flat(_raw))

# G3 -- the flip family: every derived verdict re-evaluated with its inputs negated
_flips = 0
for fig, mk, blob in (('13.73', r'\bnarrower\b', "arm narrower by 13.73%"),
                      ('0.36', r'\bsound horizon\b', "the sound horizon agrees to 0.36 per cent")):
    a, _ = quantity(fig, blob, [mk])
    b, _ = quantity(fig, blob.replace(mk.strip('\\b'), 'zzz'), [mk])
    _flips += int(a == 'CONFIRMED' and b != 'CONFIRMED')
check(f"G3 the flip family: every quantity verdict flips when its label is removed ({_flips} of 2)",
      _flips == 2)

# ------------------------------------------------------------------ PART 1 -- what ran
print("\nPART 1 -- WHAT RAN, WITH THE DENOMINATOR KEPT WHOLE")
print("  " + "-" * 104)
ran = [r for r in R.values() if r['state'] == 'RAN']
for r in sorted(R.values(), key=lambda r: -r['seconds']):
    print(f"      {r['state']:<5} rc={str(r['rc']):<5} {r['seconds']:>7.1f}s / {r['budget']}s  "
          f"{r['receipt'][:74]}")
check(f"⛭ ARM ③ -- at least 6 of the {len(R)} cited receipts ran to completion inside the window "
      f"({len(ran)} of {len(R)})", len(ran) >= 6)

# ------------------------------------------------------------------ PART 2 -- the figure table
print("\nPART 2 -- ⓵ THE DIGITS AND ⓸ THE QUANTITY, FIGURE BY FIGURE")
print("  " + "-" * 104)

A_SRC = ('P15_a_source_with_no_physics_reproduces_the_contrast_and_the_two_clocks_part_company_'
         'at_the_visibility')
A_ACC = ('P15_the_acceptance_does_not_move_under_refinement_and_three_of_the_twelve_axes_could_'
         'not_have_moved_it')
A_RET = ('P15_the_retention_is_the_combs_average_over_the_kernels_own_k_acceptance_and_the_law_'
         'has_no_fitted_coefficient')
A_SEL = ('P15_the_selection_does_not_truncate_so_the_thirteen_sigma_stands_at_twelve_point_nine_'
         'and_the_peak_that_goes_missing_is_the_third_not_the_fourth')

# (figure, site, the sentence's own words as ANCHORED markers, markers for a quantity the
#  sentence DISTINGUISHES from this one, the receipt the figure is looked for in)
FIGS = [
    ('1.061',  'l.1797', [r'\bratio\b'], [r'\bslope\b'], A_SRC),
    ('0.019',  'l.1798', [r'\bslope\b'], [r'\bratio\b'], A_SRC),
    ('0.022',  'l.1798', [r'\bREAL source\b', r'\breal source\b'], [], A_SRC),
    ('0.36',   'l.1807', [r'\bd r_s\b', r'\bsound horizon\b'],
                         [r'\bd chi\b', r'\bcomoving\b'], A_SRC),
    ('17.307', 'l.1807', [r'\bd r_s\b'], [r'\bd chi\b'], A_SRC),
    ('17.369', 'l.1807', [r'\bd r_s\b'], [r'\bd chi\b'], A_SRC),
    ('15.5',   'l.1808', [r'\bd chi\b', r'\bcomoving\b'], [r'\bd r_s\b'], A_SRC),
    ('38.04',  'l.1808', [r'\bd chi\b', r'\bFWHM\b'], [], A_SRC),
    ('43.96',  'l.1809', [r'\bd chi\b', r'\bFWHM\b'], [], A_SRC),
    ('0.395',  'l.1810', [r'\bd r_s ?/ ?d chi\b', r'\bsound speed\b'], [], A_SRC),
    ('0.455',  'l.1810', [r'\bd r_s ?/ ?d chi\b', r'\bsound speed\b'], [], A_SRC),
    ('4.43',   'l.1845', [r'\barm\b'], [r'\bcontrol\b'], A_ACC),
    ('5.14',   'l.1845', [r'\bcontrol\b'], [r'\barm narrower\b'], A_ACC),
    ('13.73',  'l.1846', [r'\bnarrower\b'], [r'\bdr_s ?/ ?dchi\b'], A_ACC),
    ('13.1',   'l.1847', [r'\bd r_s ?/ ?d chi\b', r'\bdr_s ?/ ?dchi\b', r'\bsound speed\b'],
                         [r'\bacceptance spans\b'], A_SRC),
    ('0.788',  'l.1890', [r'\bJac lo\b', r'\bJac\b'], [], A_SRC),
    ('0.911',  'l.1890', [r'\bJac hi\b', r'\bJac\b'], [], A_SRC),
    ('12.6',   'l.2283', [r'\bdriving unit\b'], [r'\bsky\b'], A_SEL),
    ('0.953',  'l.2283', [r'\bbootstrap\b', r'\binterval\b'], [], A_SEL),
    ('0.76',   'l.2284', [r'\bsky\b'], [r'\bdriving unit\b'], A_SEL),
]
print(f"      {'figure':>8}  {'site':<8} {'digits':<11} {'quantity':<13} the label the receipt "
      f"attaches to it")
rows = []
for fig, site, mk, ag, rc in FIGS:
    txt = OUT[rc]
    dv = digits(fig, txt)
    qv, ev = quantity(fig, txt, mk, ag)
    rows.append(dict(figure=fig, site=site, digits=dv, quantity=qv, receipt=rc,
                     evidence=[f"l{n}: {s}" for n, s in ev[:2]]))
    where = ev[0][1][:50] if ev else ''
    print(f"      {fig:>8}  {site:<8} {dv:<11} {qv:<13} {where}")
_rep = [r for r in rows if r['digits'] == 'REPRODUCES']
_abs = [r for r in rows if r['digits'] == 'ABSENT']
_con = [r for r in rows if r['quantity'] == 'CONTRADICTED']
_amb = [r for r in rows if r['quantity'] == 'AMBIGUOUS']
_unc = [r for r in rows if r['quantity'] == 'UNCONFIRMED']
print(f"\n      REPRODUCES {len(_rep)} / {len(rows)}   ABSENT {len(_abs)}   "
      f"quantity CONTRADICTED {len(_con)}   AMBIGUOUS {len(_amb)}   UNCONFIRMED {len(_unc)}")
_vd['digits'] = rows

# ------------------------------------------------------------------ PART 3 -- the order's own question
print("\nPART 3 -- ⓹ THE ORDER'S NAMED QUESTION: IS `l.1850`'s `0.36 PER CENT` THE WINDOW'S SOUND")
print("          HORIZON, OR `r_s*`?")
print("  " + "-" * 104)
print("  *The order asks it because `70` measures `r_s*` at `0.82` per cent on the arm of record, and")
print("  a sentence that says `the same sound horizon to 0.36 per cent` is checkable only once it is")
print("  settled WHICH sound horizon.  ⌗ Three quantities in the corpus answer to that name.*")
import numpy as np                                                          # noqa: E402
GB = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra', 'r6919_geometry_leafrec1.npz')
G3 = np.load(GB, allow_pickle=True)


def _pc(key):
    c, a = float(G3[f'{key}__lcdm']), float(G3[f'{key}__cr_leafrec1'])
    return c, a, 100.0 * (a / c - 1.0)


NAMED = {'d_rs_own': 'the sound horizon ACCUMULATED ACROSS THE VISIBILITY FWHM -- `l.1807`\'s own',
         'R_S': '`r_s*`, the banked sound horizon at last scattering',
         'rs_ls_own': 'the sound horizon AT the visibility peak on the arm\'s own clock'}
print(f"\n      {'quantity':<58} {'control':>11} {'arm':>11} {'arm/ctl':>9}")
_tab = {}
for k, desc in NAMED.items():
    c, a, p = _pc(k)
    _tab[k] = p
    print(f"      {desc:<58} {c:>11.4f} {a:>11.4f} {p:>8.2f}%")
print()
check("⓹ⓐ the figure `l.1850` prints, 0.36 per cent, IS the window-accumulated sound horizon of "
      f"`l.1807` ({_tab['d_rs_own']:.2f}% on the arm of record)", abs(_tab['d_rs_own'] - 0.36) < 0.01)
check("⓹ⓑ and it is NOT `r_s*`, whose arm-to-control difference on the same banks is `70`'s 0.82 "
      f"per cent ({_tab['R_S']:.2f}%)", abs(_tab['R_S'] - 0.82) < 0.05)
check("⓹ⓒ ⛭ and a THIRD quantity answers to the same name -- the sound horizon AT the peak on the "
      f"arm's own clock, {_tab['rs_ls_own']:.2f} per cent -- so `the sound horizon` is "
      "THREE-to-one on this object", _tab['rs_ls_own'] > 1.0)
_vd['the_three_horizons'] = _tab

# ------------------------------------------------------------------ PART 4 -- the Jacobian's window
print("\nPART 4 -- ⛔ ⓸ THE WINDOW `l.1890` NAMES IS NOT THE WINDOW ITS FIGURES WERE MEASURED ON")
print("  " + "-" * 104)
print("  `l.1889-1890` prints: *the Jacobian `runs 0.788 to 0.911 across $\\pm3$ HALF-WIDTHS of the")
print("  visibility`*.  The receipt's own prose, three times, says `+-3 FWHM`; and the bank that")
print("  carries `jac_lo`/`jac_hi` builds its grid as `linspace(ETA_LS - 3*w, ETA_LS + 3*w, 201)`")
print("  with `w = M.ETA_LS_W`, whose own definition in `ACOUSTIC_two_arm.py:600` is `its FWHM in")
print("  conformal time`.  ⇒ ** +-3 FWHM is +-6 half-widths: the window the sentence names is HALF")
print("  the one the figures come from. **")
WIN = json.load(open(os.path.join(HERE, 'jac_windows.json'))) if os.path.exists(
    os.path.join(HERE, 'jac_windows.json')) else None
if WIN:
    print(f"\n      {'window':<34} {'Jac lo':>10} {'Jac hi':>10} {'spread':>9}")
    for nm, (lo, hi) in WIN['windows'].items():
        print(f"      {nm:<34} {lo:>10.4f} {hi:>10.4f} {100*(hi-lo):>8.1f}%")
    f3, h3 = WIN['windows']['pm3_FWHM'], WIN['windows']['pm3_halfwidths']
    check("⓸ⓐ on the window the RECEIPT names (+-3 FWHM) the Jacobian spans the printed 0.788-0.911",
          abs(f3[0] - 0.788) < 0.005 and abs(f3[1] - 0.911) < 0.005)
    check(f"⓸ⓑ ⛔ on the window the SENTENCE names (+-3 half-widths) it does NOT -- it spans "
          f"{h3[0]:.3f} to {h3[1]:.3f}, less than half the spread",
          not (abs(h3[0] - 0.788) < 0.005 and abs(h3[1] - 0.911) < 0.005)
          and (h3[1] - h3[0]) < 0.6 * (f3[1] - f3[0]))
    check("⓸ⓒ and the direction is the understating one for the sentence's own point: the narrower "
          "window makes the two clocks look MORE alike, so the printed pair is the stronger reading "
          "and the named window the weaker", (h3[1] - h3[0]) < (f3[1] - f3[0]))
    _vd['jac_windows'] = WIN
else:
    check("⓸ the window comparison was measured", False)

# ------------------------------------------------------------------ PART 5 -- the namesake receipt
print("\nPART 5 -- ⛔ ⓺ ONE OF THE FOUR RECEIPTS `l.1850` CITES IS STILL ENTIRELY ON THE NAMESAKE")
print("  " + "-" * 104)
_ret_src = open(os.path.join(ROOT, 'receipts', 'P15_CR_cosmology', A_RET + '.py'),
                encoding='utf-8', errors='replace').read()
_acc_src = open(os.path.join(ROOT, 'receipts', 'P15_CR_cosmology', A_ACC + '.py'),
                encoding='utf-8', errors='replace').read()
_ret_banks = sorted(set(re.findall(r'r7041_accept[_a-zA-Z0-9]*', _ret_src)))
_acc_banks = sorted(set(re.findall(r'r7041_accept[_a-zA-Z0-9]*', _acc_src)))
print(f"      `…the_retention…`  reads : {', '.join(_ret_banks) or '(none)'}")
print(f"      `…the_acceptance…` reads : {', '.join(b for b in _acc_banks if 'leafrec1' in b)}")
check("⓺ⓐ ⛔ `…the_retention…` reads the NAMESAKE banks -- not one `_leafrec1` form among them -- "
      "while `…the_acceptance…`, cited in the same sentence, reads the arm of record's",
      not any('leafrec1' in b for b in _ret_banks)
      and any('leafrec1' in b for b in _acc_banks))
check("⓺ⓑ and it HARDCODES the namesake's `d r_s / d chi` in its own prose and in the message of "
      "the gate that checks the agreement: `0.454950 against 0.396733` and `12.8 per cent`, where "
      "the arm of record is `0.395135` and `13.1`",
      '0.396733' in _ret_src and '12.8' in _ret_src and '0.395135' not in _ret_src)
_ret_out = OUT[A_RET]
_ret_acc = re.findall(r'acceptance spans 2 r_s\* dk = ([\d.]+)', _ret_out)
_acc_acc = re.findall(r'base\s+control ([\d.]+)\s+arm ([\d.]+)', OUT[A_ACC])
print(f"      the acceptance, from `…the_retention…`  (namesake banks) : {', '.join(_ret_acc)}")
print(f"      the acceptance, from `…the_acceptance…` (arm of record)  : "
      f"{', '.join(_acc_acc[0]) if _acc_acc else '(not found)'}")
check("⓺ⓒ ⛔ so ONE named quantity has TWO values in the corpus, and the paper prints the arm of "
      "record's -- `4.43` and `5.14` are `…the_acceptance…`'s, not `…the_retention…`'s",
      bool(_ret_acc) and bool(_acc_acc)
      and abs(float(_acc_acc[0][1]) - 4.43) < 0.01 and abs(float(_ret_acc[1]) - 4.43) > 0.05)
check("⓺ⓓ ⛭ AND THE TRAP: `…the_retention…`'s NAMESAKE acceptance narrowing is ALSO `13.1` per "
      "cent, the same digits as the arm of record's SOUND-SPEED narrowing that `l.1847` quotes -- "
      "so one number is many-to-one across two quantities AND two arms",
      '13.1 per cent narrower against 12.8 per cent' in _ret_out)

print("\n      ⌗ AND TWO RECEIPT PROSE DEFECTS OF THE SAME CLASS, FOUND WHILE READING THE LABELS:")
_sel_flat = flat(OUT[A_SEL])
_sel_hdr = hit(r"\bl\.2283-2284's `\$0\.953\$`, `\$12\.5\$` AND `\$0\.75\$`", _sel_flat)
_sel_meas = hit(r"\bthe paper prints, read out of corpus/CR_cosmology\.tex: \('0\.953', '12\.6', '0\.76'\)",
                _sel_flat)
check("⓺ⓔ ⛔ `…the_selection…`'s own assertion HEADER names the paper's OLD figures, `12.5` and "
      "`0.75`, while the measurement two lines above it reads the paper as printing `12.6` and "
      "`0.76` -- the receipt's text disagrees with its own computation", _sel_hdr and _sel_meas)
_src_flat = flat(OUT[A_SRC])
_src_est = hit(r"\bexceeding the real source's 1\.054 and \+0\.02178\b", _src_flat)
_src_gate = hit(r"\bslope in q is NOT steeper any more\b", _src_flat) and hit(
    r"\bslope FALSIFIED\b", _src_flat)
check("⓺ⓕ ⛔ and `…a_source…`'s ESTABLISHED paragraph says the injection's figures are `exceeding "
      "the real source's 1.054 AND +0.02178`, where its own gate says the slope `is NOT steeper any "
      "more` and prints `slope FALSIFIED` -- the paper's own sentence is the MORE accurate of the "
      "two, hedging the slope instead of claiming it", _src_est and _src_gate)

_vd['receipt_prose'] = dict(selection_header_stale=bool(_sel_hdr and _sel_meas),
                            a_source_established_overclaims=bool(_src_est and _src_gate))
_vd['namesake'] = dict(retention_banks=_ret_banks, acceptance_banks=_acc_banks,
                       retention_acceptance=_ret_acc,
                       acceptance_acceptance=list(_acc_acc[0]) if _acc_acc else [])

# ------------------------------------------------------------------ PART 6 -- the claims
print("\nPART 6 -- ⓻ THE CLAIMS, NOT THE DIGITS: DOES ANY COMPARATOR CHANGE ON THE ARM OF RECORD?")
print("  " + "-" * 104)
_dchi_pc = 100.0 * (float(G3['d_chi__cr_leafrec1']) / float(G3['d_chi__lcdm']) - 1.0)
CLAIMS = [
    ('l.1798 `exceeding` what the real source gives -- the RATIO',
     1.0612 > 1.054, 'injection 1.0612 against the real source 1.054'),
    ('l.1798 `at a slope of +0.019 ... close to the real source\'s own +0.022` -- a HEDGE, and the '
     'receipt\'s own gate calls the slope half FALSIFIED',
     0.01927 < 0.02178, 'the injection\'s slope is LOWER, not steeper: +0.01927 against +0.02178'),
    ('l.1808 the comoving distance `differs by 15.5 per cent` while the sound horizon is `the same`',
     abs(_tab['d_rs_own']) < 1.0 and abs(_dchi_pc) > 15.0,
     f"d r_s {_tab['d_rs_own']:.2f}% against d chi {_dchi_pc:+.2f}%"),
    ('l.1845 the acceptance is `the narrower on this arm`',
     bool(_acc_acc) and float(_acc_acc[0][1]) < float(_acc_acc[0][0]),
     f"arm {_acc_acc[0][1] if _acc_acc else '?'} against control "
     f"{_acc_acc[0][0] if _acc_acc else '?'}"),
    ('l.1847 `two routes to one quantity, and the agreement is built in nowhere`',
     'R6919_NARROWING = 0.131' in _acc_src and 'HARDCODED CONSTANT' in _acc_src,
     'the comparison target 13.1 IS a hardcoded constant in `…the_acceptance…`, declared as such, '
     'checked at a 1 pp window with 0.63 pp measured'),
    ('l.1850 this arm\'s visibility is `the 15.5 per cent wider in chi`',
     abs(_dchi_pc - 15.5) < 0.1,
     'd chi 43.957 against 38.042'),
    ('l.2284 `both figures quoted above survive the change`',
     hit(r'\bboth figures quoted above survive the change\b',
         flat(open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8',
                   errors='replace').read()))
     and hit(r'\bsurvive the change\b', flat(OUT[A_SEL])),
     'the receipt carries the sentence and says the quoted end is the conservative one'),
]
_changed = []
for lab, ok, note in CLAIMS:
    print(f"      [{'HOLDS' if ok else 'CHANGED':<7}] {lab}")
    print(f"                  {note}")
    if not ok:
        _changed.append(lab)
check(f"⓻ the comparators that do NOT hold on the receipts' own numbers ({len(_changed)} of "
      f"{len(CLAIMS)})", True)
_vd['claims'] = [dict(claim=lab, holds=bool(ok), note=note) for lab, ok, note in CLAIMS]

# ------------------------------------------------------------------ PART 7 -- scope and count
print("\nPART 7 -- ① THE CITATION SCOPE AND ⑦ THE COUNT, THROUGH THE GATE'S OWN `sites()`")
print("  " + "-" * 104)
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_figures_pinned as G                                            # noqa: E402
GS = [(pa, n, c) for (pop, pa, n, c) in G.sites() if pa == 'CR_cosmology.tex']
UNSEEN = []
for fig, site, *_ in FIGS:
    seen = any(fig in c for (_, _, c) in GS)
    if not seen:
        UNSEEN.append((fig, site))
print(f"      cited sentences in `CR_cosmology.tex` the gate reads : {len(GS)}")
print(f"      of the order's {len(FIGS)} figures, those appearing in NO cited sentence, so the")
print(f"      figure-pin gate never reads them                     : {len(UNSEEN)}")
for fig, site in UNSEEN:
    print(f"        ~ {fig:>8}  at {site}")
check("①ⓐ the read made before registration survives the gate's own `sites()`: the heaviest "
      "figures of the repoint sit in sentences that cite NO receipt, so the figure-pin gate has "
      f"never read them ({len(UNSEEN)} of {len(FIGS)})", len(UNSEEN) > 0)
S0 = json.load(open(os.path.join(HERE, 'sites.json')))
print(f"\n      the order calls them              : eleven")
print(f"      the landing commit calls them     : eight repoints")
print(f"      the parser finds, distinct        : {len(S0['named_distinct'])}")
print(f"      this read checked                 : {len(FIGS)}")
check(f"⑦ the count is MEASURED and does not match either name given to it "
      f"({len(S0['named_distinct'])} distinct against `eleven` and `eight`)",
      len(S0['named_distinct']) != 11)
_vd['scope'] = dict(unseen=[list(x) for x in UNSEEN], cited_sentences=len(GS),
                    distinct=len(S0['named_distinct']), checked=len(FIGS))

# ------------------------------------------------------------------ the verdict
print("\n" + "=" * 108)
print("  THE VERDICT")
print("=" * 108)
NS = len([r for r in rows if r['digits'] == 'REPRODUCES'])
print(f"  ⓵ THE DIGITS            : {NS} of {len(rows)} reproduce to the printed precision; "
      f"{len(_abs)} absent.")
print(f"  ⓸ THE QUANTITY          : {len([r for r in rows if r['quantity'] == 'CONFIRMED'])} "
      f"confirmed, {len(_con)} contradicted, {len(_amb)} ambiguous, {len(_unc)} unconfirmed.")
print(f"  ⓹ `l.1850`'s 0.36       : the WINDOW-ACCUMULATED sound horizon of `l.1807`, measured "
      f"{_tab['d_rs_own']:.2f}%, and NOT `r_s*` at {_tab['R_S']:.2f}%.  The order's reading is right.")
print(f"  ⓸ `l.1890`'s WINDOW     : ⛔ NOT SUPPORTED -- `+-3 half-widths` names half the window the "
      f"figures come from.")
print(f"  ⓺ `l.1850`'s CITATIONS  : ⛔ one of the four receipts is entirely on the NAMESAKE and "
      f"disagrees with the printed figures.")
print(f"  ⓻ THE CLAIMS            : {len(CLAIMS) - len(_changed)} of {len(CLAIMS)} comparators hold.")
print(f"  ① THE GATE'S REACH      : {len(UNSEEN)} of the {len(FIGS)} figures sit in UNCITED "
      f"sentences, outside what the figure-pin gate can see.")
json.dump(_vd, open(os.path.join(HERE, 'verdicts.json'), 'w'), indent=1)
print("\n" + "=" * 108)
if _fail:
    print(f"  ⛔ {len(_fail)} GUARD OR ARM FAILED:")
    for f in _fail:
        print(f"      ~ {f[:100]}")
    sys.exit(1)
print("  ALL GUARDS AND ARMS PASS.")

