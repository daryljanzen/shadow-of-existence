#!/usr/bin/env python3
"""`r7675` (cc66) ITEM 3 -- THE EIGHT ONE-SENTENCE-AWAY SITES, READ.

** THE ORDER (`r7675`, 69) item 3: ** "The eight one-sentence-away sites you measured (`l.1736`,
`l.2050`, `l.2066` twice, `l.2301`, `l.2343` three times; the `l.2792` item is one site).  Read each,
as `r7671` did, and add any real miss to the list.  The acceptance item showed the channel is real."

** THE CHANNEL. **  `r7673+cc66.1` named a gap in my own census: a figure printed ONE SENTENCE from
its citation is invisible to a test that reads the citing sentence only.  Measured there at 16
candidate (sentence, receipt) pairs on 6 rows, 8 of them hanging off the single `\\item` at `l.2792`,
leaving 8 actionable pairs.  ** This file reproduces that measurement off the shared definitions and
then READS each pair, which is the part no instrument can do. **

⛔⛭⛭⛭ ** AND THE READ FOUND THE CAUSE, WHICH IS WORSE THAN THE CHANNEL. **  Four of the eight are
explained by a SECOND defect, in my census's load-site classifier: the arm of record is carried by the
DIRECTORY (`r7093_directions/grid_oneclock` vs `..._leafrec1`), the directory is held in a MODULE
VARIABLE, and the load reads `np.load(path)` through a parameter whose caller passes
`os.path.join(GO, 'cr_base.npz')`.  No literal in that call names the arm, so the site reads
UNDECIDABLE and the receipt records NO namesake load at all.  *That is `r7667+cc66.2`'s own lesson --
the arm is carried by the directory -- reappearing one level further in, inside the load site, where
cut 2's fix does not reach.*

⛭⛭ ** THE TWO DEFECTS COMPOSE, AND THAT IS THE FINDING. **  Each of the four misses needs BOTH to be
missed, which gate ③ asserts rather than asserts rhetorically:
  * widen the sentence scope alone and the receipt is still not a namesake candidate -- the classifier
    does not see its namesake read;
  * fix the classifier alone and the receipt is still off the list -- its OWN citing sentence prints
    no figure.
⇒ So neither fix would have surfaced these four, and no single-cause account of the gap is true.

Registered at `PREDICTION.md` arms ⑦ (this file's verdicts) and ⑧/⑨ (its addendum, own commit).
"""
import ast
import collections
import contextlib
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
R7667 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7667_cc66_po87_the_unfiltered_list')
sys.path.insert(0, R7667)

#: ⛭ THE CENSUS IS IMPORTED, NOT RE-IMPLEMENTED.  Its `cand`/`prints_fig`/`sel` ARE PO-87's list and
#:   its classifier; a second copy of either would be the drift `sentence.py`'s header is about.  Its
#:   own report is captured rather than printed: this file's output is the READ, not the census.
_cap = io.StringIO()
with contextlib.redirect_stdout(_cap):
    import census                                   # noqa: E402
from sentence import depth0_sentences               # noqa: E402

TEX = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
           encoding='utf-8', errors='replace').read()

fail = []


def check(label, ok, got=None):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}" + (f"   ({got})" if got is not None else ""))
    if not ok:
        fail.append(label)


def head(t):
    print('\n' + '=' * 100)
    print('  ' + t)
    print('=' * 100 + '\n')


# ══ ① THE CHANNEL, REPRODUCED OFF THE SHARED SPLITTER ════════════════════════════════════════════
head('\u2460  THE CHANNEL -- a figure printed one sentence from its citation')
_NUM = re.compile(r'\d+\.\d+|\b\d{2,}\b')
_RC = re.compile(r'\\rcpt\{([A-Za-z0-9_]+)\}')
_BODY_FROM = TEX[:TEX.find('\\begin{document}')].count('\n') + 1


def _prose(x):
    """a depth-0 span is PROSE if, with its macros stripped, it still carries five English words."""
    y = re.sub(r'\\[A-Za-z]+\*?(\{[^{}]*\})?', '', x)
    return len(re.findall(r'\b[a-z]{3,}\b', y)) >= 5


SENTS = [(ln, x) for ln, x in depth0_sentences(TEX) if ln > _BODY_FROM and _prose(x)]
_CANDBASE = {os.path.basename(p)[:-3]: p for p in census.cand}
_FIGBASE = {os.path.basename(p)[:-3] for p in census.prints_fig}

ROWS = []                       # (line, uncited sentence, [candidate receipt bases off the list])
for i, (ln, x) in enumerate(SENTS):
    if not (_NUM.search(x) and not _RC.search(x)) or i + 1 >= len(SENTS):
        continue
    nxt = _RC.findall(SENTS[i + 1][1])
    off = [b for b in nxt if b in _CANDBASE and b not in _FIGBASE]
    if off:
        ROWS.append((ln, x, off))
_PAIRS = sum(len(o) for _l, _x, o in ROWS)
_BIG = [r for r in ROWS if len(r[2]) > 3]
print(f'      depth-0 prose sentences in the body: {len(SENTS)}')
print(f'      rows (uncited figure, next sentence cites a namesake-resting receipt off the list): '
      f'{len(ROWS)};  (sentence, receipt) pairs: {_PAIRS}')
for ln, _x, o in ROWS:
    print(f'        l.{ln:<6d} {len(o)} receipt(s)')
#: ⛔ THE LINE NUMBERS DIFFER FROM THE ORDER'S BY ONE OR TWO AND THAT IS THIS FILE'S CONVENTION, not
#:   a different site: `depth0_sentences` reports the line where the SPAN begins, which is the line
#:   after the previous sentence's closing brace run; `r7673+cc66.1` reported the line the FIGURE
#:   sits on.  `l.2066`/`l.2068`, `l.2301`/`l.2303` and `l.2343`/`l.2344` are the same three sites.
_SHAPE = {1736: 1, 2050: 1, 2068: 2, 2303: 1, 2344: 3, 2792: 8}
check('\u2460 the channel reproduces `r7673+cc66.1`\'s measurement off the SHARED splitter: 16 pairs '
      'on 6 rows, 8 of them on the single `\\item` at `l.2792`, leaving 8 actionable pairs -- and '
      'the shape is pinned per row, so a row moving between sites would redden this rather than '
      'cancel in the total',
      {ln: len(o) for ln, _x, o in ROWS} == _SHAPE and _PAIRS == 16 and len(_BIG) == 1,
      f'{_PAIRS} pairs on {len(ROWS)} rows: ' + ', '.join(f'l.{ln}x{len(o)}' for ln, _x, o in ROWS))

# ══ THE LOAD PATHS, RESOLVED THROUGH THE DIRECTORY VARIABLE ══════════════════════════════════════
#: ⛔⛭⛭ WHY THIS RESOLVER IS HERE AND NOT IN `census.py`.  It is the fix for the classifier gap this
#:   read found, and it belongs in the census -- but the census IS PO-87's list, 69's artefact, and
#:   § ⑤ below measures that the gap adds ** zero ** items to the list by the list's own criterion.
#:   ⇒ So the fix is ROUTED and not merged: a change that moves 69's list without changing what is
#:     on it is 69's call, and `PREDICTION.md` already says rebuilding the census is not mine.
def _resolve(tree, here):
    """module-level string variables, by fixed point over `os.path.join`/`dirname` and literals."""
    env = {'ROOT': ROOT, 'HERE': here}
    assigns = [(n.targets[0].id, n.value) for n in tree.body
               if isinstance(n, ast.Assign) and len(n.targets) == 1
               and isinstance(n.targets[0], ast.Name)]

    def ev(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.Name):
            return env.get(node.id)
        if isinstance(node, ast.Call):
            nm = (node.func.attr if isinstance(node.func, ast.Attribute)
                  else getattr(node.func, 'id', ''))
            if nm == 'join':
                parts = [ev(a) for a in node.args]
                return os.path.join(*parts) if all(isinstance(p, str) for p in parts) else None
            if nm in ('dirname', 'abspath', 'realpath'):
                p = ev(node.args[0]) if node.args else None
                if isinstance(p, str):
                    return os.path.dirname(p) if nm == 'dirname' else p
            return None
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            a, b = ev(node.left), ev(node.right)
            return a + b if isinstance(a, str) and isinstance(b, str) else None
        return None

    for _ in range(8):
        for name, val in assigns:
            if name not in env:
                v = ev(val)
                if isinstance(v, str):
                    env[name] = v
    return env, ev


def _npz_paths(src, here):
    """every `os.path.join(<resolvable dir>, '...npz')` in the module, resolved against the tree."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    _env, ev = _resolve(tree, here)
    out = []
    for n in ast.walk(tree):
        if not isinstance(n, ast.Call):
            continue
        nm = n.func.attr if isinstance(n.func, ast.Attribute) else getattr(n.func, 'id', '')
        if nm != 'join':
            continue
        parts = [ev(a) for a in n.args]
        if all(isinstance(p, str) for p in parts):
            p = os.path.join(*parts)
            if p.endswith('.npz') and os.path.exists(p):
                out.append(p)
    return sorted(set(out))


def _aor_sibling(path):
    """the arm-of-record twin of a namesake path -- by its own name OR by ANY ancestor directory."""
    d, b = os.path.split(path)
    cands = [os.path.join(d + '_leafrec1', b), os.path.join(d, b.replace('.npz', '_leafrec1.npz'))]
    rel = os.path.relpath(d, ROOT).split(os.sep)
    for i in range(len(rel)):
        alt = list(rel)
        alt[i] = alt[i] + '_leafrec1'
        cands.append(os.path.join(ROOT, *alt, b))
    return [c for c in cands if os.path.exists(c)]


def _blind(pth):
    """(namesake paths with a banked arm-of-record sibling, resolved through the directory)"""
    fp = os.path.join(ROOT, pth)
    if not os.path.exists(fp):
        return []
    src = open(fp, encoding='utf-8', errors='replace').read()
    out = []
    for p in _npz_paths(src, os.path.dirname(fp)):
        if 'leafrec1' in os.path.relpath(p, ROOT):
            continue
        sib = _aor_sibling(p)
        if sib:
            out.append((os.path.relpath(p, ROOT), os.path.relpath(sib[0], ROOT)))
    return out


# ══ ② THE READ -- one declared verdict per pair, with its reason ═════════════════════════════════
head('\u2461  THE READ -- a verdict per (sentence, receipt) pair, declared and reasoned')
MISS, CLEAR = 'REAL MISS', 'NOT A MISS'
READ = {
    (1736, 'P15_the_three_instruments_with_no_noise_model_one_can_be_given_a_floor_and_ten_passages'
           '_quote_a_significance_or_share_the_instrument_cannot_bear'): (CLEAR,
        "the per-band floor the sentence prints ($0.043$-$0.086$) is built from "
        "`cc66_r185_verify_lcdm` -- the CONTROL -- drawn through the likelihood's own covariance, "
        "with the band edges taken from `r6959_eta_cr_leafrec1`, the ARM OF RECORD.  The receipt's "
        "one namesake read, `r6915_pairs_lcdm`, is a control leg used in the SRCDEC section and "
        "carries nothing in this sentence; and `r7669+70.1` settles that LEAFREC does not touch the "
        "control at all, bit for bit and by construction.  So every namesake read here is "
        "control-side and already the arm of record's control, which is why the thirteen HELD items "
        "left the split for the same reason"),
    (2050, 'P15_the_combs_resolution_is_four_multipoles_and_the_skys_own_value_lies_outside_the'
           '_family'): (CLEAR,
        "the height ratio the sentence prints ($2.135 \\to 2.009$ against the sky's $2.217$) is "
        "`R[0.0]['p12']` and `R[1.0]['p12']`, gated at $2.1345$/$2.0093$ to $5\\times10^{-5}$ and "
        "computed on `_A = '_leafrec1'` throughout -- the arm of record.  Its five namesake reads "
        "are a convention GATE (`r6929_geometry.npz`, read only so that pointing the arm key back "
        "at `cr` fails gate \u24AA), two no-op bases the receipt's own header says stay WHOLLY on "
        "the namesake arm, and two control legs.  This is `r7669`'s limit exactly: the census "
        "cannot tell a figure read from a gate read, and here it is a gate read"),
    (2068, 'P15_the_crossing_spectrum_reproduces_on_a_second_instrument_and_the_172_is_the'
           '_radiation_free_ruler'): (CLEAR,
        "the only figure in the uncited sentence this receipt carries is the BIN COVERAGE -- $185$ "
        "covered bins against $133$ -- which its own source calls \"the instrument's coverage and "
        "not a choice\" and which no arm can move.  Its peak and height figures are not the "
        "sentence's: those are read below.  ⛔ But the receipt IS namesake-resting and the census "
        "cannot see it: `c54.178_cr`, `r6784_cr_crossing_hier`, `..._noCRIC` and `..._los` all have "
        "banked `_leafrec1` siblings, and all four are loaded as `load(f)` with `f` a loop variable "
        "over a dict of names, so not one literal reaches the load site.  It is a member of \u2464's "
        "class that \u2464's own resolver ALSO misses, found here by hand"),
    (2068, 'P15_the_locator_is_good_to_three_hundredths_and_the_fourth_peaks_residual_is_the'
           '_controls_too'): (CLEAR,
        "it reads `r6941_fine_cr_leafrec1`, `r6941_fine_cr_visleaf_leafrec1`, "
        "`r6929_scan_cr_leafrec1`, `r6929_geometry_leafrec1` and `cc66_r185_verify_cr_leafrec1` -- "
        "the arm of record on every CR leg -- and its one namesake read is the same convention gate "
        "as `l.2050`'s.  The sub-bin peaks the sentence prints ($220.03$, $536.27$, $811.58$, "
        "$1125.02$ against $220.03$, $536.25$, $811.59$, $1125.11$) and the height ratios "
        "($2.291$/$2.348$ against $2.291$/$2.349$) are not this receipt's at all: they are rows of "
        "`P15_at_its_own_preferred_H0...`, both labelled `the ARM OF RECORD` in its own source and "
        "read off `cc66_cr_x_h686_L2000_leafrec1_distances` and "
        "`refit_grid185_leafrec1_distances/cr_base`.  ⇒ The channel named two receipts at this site "
        "and the producer is a THIRD it does not cite -- which is a citation question for 69, not a "
        "namesake one"),
    (2303, 'P15_the_three_parameter_comb_fails_its_validation_because_the_peak_spacing_DRIFTS_and'
           '_the_missing_parameter_is_the_one_the_sector_is_about'): (MISS,
        "the sentence's `factor of $542$` and `a further $24$ points` are this receipt's own gate "
        "\u24B9\u2460, printed as `chi2 improves {_d_chi / _rg.fun:.0f}x` and `by "
        "{100 * (_g_lA - _d_lA):+.1f} points`, computed on `binned(os.path.join(GO, "
        "'cr_base.npz'))` -- `r7093_directions/grid_oneclock/cr_base.npz`, a NAMESAKE whose "
        "`grid_oneclock_leafrec1/cr_base.npz` is banked.  The citing sentence's `five spectra of "
        "six` and `a fifth away` are gate \u24B9\u2460's, on the same banks plus "
        "`r7201_cc66_loading_lever/`, also banked `_leafrec1`.  ⇒ A figure in print resting on a "
        "namesake with its rebuild already in the tree: on the list, and CHEAP"),
    (2344, 'P15_the_carrier_separation_on_L_p_is_the_combs_peak_count_not_the_carrier_and_the'
           '_closure_has_no_number_because_the_degeneracy_is_sampling_invariant'): (MISS,
        "the sentence prints this receipt's headline verbatim -- `$[0.939, 0.977]$ across THIRTEEN "
        "fits, $78$-$176$ points, five windows, six spectra`, and `halving the point count leaves "
        "it at $-0.9549$ against $-0.9548$`, the fourth decimal the sentence names -- and every one "
        "of the six spectra is a namesake read through `GO`/`LEV`: "
        "`r7093_directions/grid_oneclock/cr_base.npz` and four files of "
        "`r7201_cc66_loading_lever/`, all with banked `_leafrec1` siblings.  ⇒ On the list, and "
        "CHEAP"),
    (2344, 'P15_the_fourth_parameter_recovers_the_drift_the_gaps_show_but_the_spacing_and_the_drift'
           '_are_not_separable_so_the_data_half_still_does_not_happen'): (MISS,
        "it carries the same `$-0.94$`-`$-0.98$` range the sentence prints, as its own stop "
        "condition (`$\\rho(\\ell_A, d)$ between $-0.94$ and $-0.98$`), off the same six namesake "
        "spectra through `GO`/`LEV`.  ⇒ A co-producer of the printed range, on the same banks, so "
        "it is on the list for the same reason and not a duplicate of the row above: PO-87's list "
        "is keyed on the RECEIPT, and this is a second receipt resting on a namesake for a figure "
        "in print"),
    (2344, 'P15_centring_removes_the_correlation_exactly_and_closes_the_route_anyway_because_the'
           '_decorrelated_parameter_is_not_the_acoustic_scale'): (MISS,
        "likewise: its gate \u24B9\u2460 is `$-0.94$`-`$-0.98$ BECOMES $10^{-16}$`, so the range the "
        "sentence prints is the quantity this receipt is about, measured on the same six namesake "
        "spectra through `GO`/`LEV`, every one with a banked `_leafrec1` sibling.  ⇒ On the list, "
        "and CHEAP"),
    (2792, '_THE_ITEM'): (CLEAR,
        "read as ONE site, as the order has it.  The uncited sentence's figure is the stretch "
        "$2.774$ between $r_0$ and $D_C$; the `\\item`'s citation run is eight receipts about the "
        "term mix, the step and the Doppler, and ⛔ NOT ONE OF THE EIGHT CONTAINS `2.774` AT ALL.  "
        "So the figure cannot rest on their namesake reads, and arm \u2468 is a HIT -- but its "
        "stated REASON was wrong: I registered that the figure would be carried by a receipt "
        "already on the list or already on the arm of record, and the truth is that the eight do "
        "not carry it in either state.  ⇒ What this site actually shows is a CITATION gap and not a "
        "namesake one: a figure in print whose producers are not cited in its own `\\item`.  "
        "Routed to 69 as such.  *The eight do each rest on a namesake (`r6941_fine_cr`, "
        "`r6959_eta_cr`, `r6975_mix_lcdm`) and are off PO-87's list correctly, because their own "
        "citing sentences print no figure*"),
}
_SEEN = collections.Counter()
for (ln, b), (v, why) in sorted(READ.items(), key=lambda kv: (kv[0][0], kv[0][1])):
    _SEEN[v] += 1
    print(f'      l.{ln:<6d} {v:<10s} {b[:76]}')
_misses = sorted(b for (ln, b), (v, _w) in READ.items() if v == MISS)
print(f'\n      verdicts: {_SEEN[MISS]} real miss(es), {_SEEN[CLEAR]} cleared, '
      f'{len(READ)} pairs read (the 8 actionable plus `l.2792` as one site)')
check('\u2461 every pair the channel produced carries a DECLARED verdict with a reason long enough '
      'to say WHY, and the two are separable: the verdict set covers the channel\'s rows exactly '
      'and no pair is left unread',
      len(READ) == 9 and all(len(w) > 150 for _v, w in READ.values())
      and {ln for ln, _b in READ} == set(_SHAPE)
      and all((ln, b) in READ for ln, _x, o in ROWS for b in o if len(o) <= 3),
      f'{len(READ)} read; shortest reason {min(len(w) for _v, w in READ.values())} chars')
#: ⛭ ARM ⑦ IS SCORED HERE, AT THE TOP OF ITS BAND AND NOT AT ITS CENTRE.  Registered 1-4 real
#:   misses, central guess 2; the read gives 4.  *The band holds and the central guess is wrong by
#:   two, which is the honest way to report it: the channel yields twice what I thought it would.*
check('\u2461\u1d43 arm \u2466 (1-4 real misses, central 2) is scored: the read gives 4, so the BAND '
      'HOLDS AT ITS TOP EDGE and the central guess MISSES BY TWO -- the channel yields twice what I '
      'registered',
      _SEEN[MISS] == 4 and 1 <= _SEEN[MISS] <= 4,
      f'{_SEEN[MISS]} of 8 actionable pairs are real misses; central guess 2')

# ══ ③ THE TWO DEFECTS COMPOSE ════════════════════════════════════════════════════════════════════
head('\u2462  WHY THESE FOUR NEEDED BOTH DEFECTS -- neither fix alone surfaces them')
_rows = []
for b in _misses:
    pth = _CANDBASE[b]
    sites = census.cand[pth]['sites']
    own = census.body_cited.get(pth, {})
    own_fig = [s for ss in own.values() for s in ss if _NUM.search(s)]
    bl = _blind(pth)
    _rows.append((b, sites, len(own_fig), bl))
    print(f'      {b[:72]}')
    print(f'         classifier sites: {dict(sites)};  namesake sites recorded: '
          f'{sites.get("namesake", 0)}')
    print(f'         its OWN citing sentence(s) printing a figure: {len(own_fig)}')
    print(f'         namesake paths resolved through the directory: {len(bl)}, '
          f'every one with a banked sibling')
    for p, s in bl[:2]:
        print(f'            {p}')
        print(f'               -> {s}')
check('\u2462 ⛭⛭ NEITHER FIX ALONE WOULD HAVE FOUND THESE FOUR, and that is asserted rather than '
      'argued: for every one of them the classifier records ZERO namesake load sites (so widening '
      'the sentence scope leaves it off the candidate set) AND its own citing sentence prints no '
      'figure (so fixing the classifier leaves it off the list).  ⇒ The two defects are '
      'independent and they compose',
      all(s.get('namesake', 0) == 0 and nf == 0 and len(bl) > 0 for _b, s, nf, bl in _rows)
      and len(_rows) == 4,
      '; '.join(f'{b[:22]}: namesake-sites={s.get("namesake", 0)}, own-fig-sentences={nf}, '
                f'resolved-namesakes={len(bl)}' for b, s, nf, bl in _rows))

# ══ ④ THE MISSES ARE CHEAP, WHICH IS THE PART 69 PAYS FOR ════════════════════════════════════════
head('\u2463  THE FOUR MISSES, PRICED -- every namesake they read is already rebuilt')
_banks = collections.Counter()
for _b, _s, _nf, bl in _rows:
    for p, _sib in bl:
        _banks[os.path.dirname(p)] += 1
print(f'      namesake DIRECTORIES the four read: {len(_banks)}')
for d, n in sorted(_banks.items()):
    sib = d + '_leafrec1'
    print(f'        {d}  ({n} file reads)  sibling banked: '
          f'{os.path.isdir(os.path.join(ROOT, sib))}')
check('\u2463 all four are CHEAP by the census\'s own counterpart test: every namesake path they read '
      'has a banked `_leafrec1` twin, and the twins are whole DIRECTORIES already in the tree -- so '
      'the repointing is `_gd(gdir, arm)` per arm, the convention `r7645+cc66.68` set, and not a '
      'wholesale directory swap',
      len(_banks) == 2
      and all(os.path.isdir(os.path.join(ROOT, d + '_leafrec1')) for d in _banks),
      ', '.join(sorted(_banks)))

# ══ ⑤ ARM ⑧ -- THE SIZE OF THE CLASSIFIER GAP ════════════════════════════════════════════════════
head('\u2464  ARM \u2467 -- how many receipts in scope the classifier is directory-blind to')
_BY_HAND = ['receipts/P15_CR_cosmology/P15_the_crossing_spectrum_reproduces_on_a_second_instrument'
            '_and_the_172_is_the_radiation_free_ruler.py']
blind_all, blind_inv = {}, {}
for _paper, pth in census.sel:
    bl = _blind(pth)
    if not bl:
        continue
    blind_all[pth] = bl
    if census.cand.get(pth, {}).get('sites', {}).get('namesake', 0) == 0:
        blind_inv[pth] = bl
_on_list = [p for p in blind_inv if os.path.basename(p)[:-3] in _FIGBASE]
_own_fig = {}
for pth in list(blind_inv) + _BY_HAND:
    own = census.body_cited.get(pth, {})
    _own_fig[pth] = len([s for ss in own.values() for s in ss if _NUM.search(s)])
print(f'      receipts in scope with a RESOLVED namesake path that has a banked sibling: '
      f'{len(blind_all)}')
print(f'      of those, the classifier records NO namesake load site (DIRECTORY-BLIND): '
      f'{len(blind_inv)}')
print(f'      plus the one the resolver ALSO misses, found by hand at `l.2068`: {len(_BY_HAND)}')
print(f'      ⇒ the class, as measured: {len(blind_inv) + len(_BY_HAND)}')
print(f'      of the class, already on PO-87\'s list by another route: {len(_on_list)}')
print(f'      of the class, with a figure-printing citing sentence of their OWN: '
      f'{sum(1 for v in _own_fig.values() if v)}')
check('\u2464 ⛭⛭ arm \u2467 (4-12 receipts, central 6) is scored: the resolver finds '
      f'{len(blind_inv)} directory-blind receipts in scope and the read found a '
      f'{len(blind_inv) + len(_BY_HAND)}th the resolver also misses -- so the BAND HOLDS AT ITS TOP '
      'EDGE and the central guess MISSES BY SIX.  The class is real and it is twice the size I '
      'registered',
      4 <= len(blind_inv) + len(_BY_HAND) <= 12 and len(blind_inv) == 11,
      f'{len(blind_inv)} by the resolver + {len(_BY_HAND)} by hand = '
      f'{len(blind_inv) + len(_BY_HAND)}; central guess 6')
#: ⛭⛭⛭ ** AND THE RESULT THAT MATTERS TO 69 IS THE OTHER ONE: THE GAP ADDS NOTHING TO THE LIST BY
#:   THE LIST'S OWN CRITERION. **  Of the class, two are already on PO-87's list through a namesake
#:   read the classifier DOES see, and of the rest not one is cited by a body sentence that prints a
#:   figure -- which is the list's membership test.  ⇒ * So fixing the classifier alone would move
#:   `len(cand)` and change nothing about what the papers print.  That is why the fix is routed and
#:   not merged, and why the FOUR arrivals below come from the READ and not from the resolver. *
check('\u2464\u1d43 ⛭⛭ AND THE GAP ADDS ZERO ITEMS TO PO-87\'S LIST BY THE LIST\'S OWN CRITERION: of '
      'the directory-blind class, the two already on the list got there through a namesake read the '
      'classifier DOES see, and not one of the others is cited by a body sentence that prints a '
      'figure.  ⇒ The classifier fix is a correction to `len(cand)`, not to what the papers print, '
      'which is why it is routed to 69 rather than merged here',
      len(_on_list) == 2
      and all(_own_fig[p] == 0 for p in blind_inv if p not in _on_list),
      f'{len(_on_list)} of {len(blind_inv) + len(_BY_HAND)} on the list; '
      f'{sum(1 for p in blind_inv if p not in _on_list and _own_fig[p])} of the rest have a '
      f'figure-printing citing sentence')

# ══ ⑥ THE ARRIVALS, AS THE ORDER ASKS ════════════════════════════════════════════════════════════
head('\u2465  THE FOUR ARRIVALS -- what goes on PO-87\'s list, and by which test')
print('      PO-87\'s list, as `census.py` DERIVES it: '
      f'{len(census.prints_fig)} figure-printing items')
print(f'      arrivals from this read, by the ONE-SENTENCE-AWAY test: {len(_misses)}')
for b in _misses:
    print(f'        + {b[:88]}')
print(f'      ⇒ PO-87\'s list, derived plus declared: '
      f'{len(census.prints_fig)} + {len(_misses)} = {len(census.prints_fig) + len(_misses)}')
check('\u2465 the arrivals are DECLARED and DISJOINT from the derived set: none of the four is '
      'already on it, each is a candidate the census already holds (so nothing new is invented '
      'about the tree), and the list goes '
      f'{len(census.prints_fig)} -> {len(census.prints_fig) + len(_misses)}',
      len(_misses) == 4 and not (set(_misses) & _FIGBASE)
      and all(b in _CANDBASE for b in _misses),
      f'{len(census.prints_fig)} derived + {len(_misses)} declared')

print('\n' + '=' * 100)
if fail:
    print('  FAILED:')
    for f in fail:
        print(f'    - {f}')
    sys.exit(1)
print('  \u2713 ALL CHECKS PASSED')
print('=' * 100)
