#!/usr/bin/env python3
"""`60`'s next revision -- THE HAND-OFF QUEUE: the arithmetic of the registration, written and pushed BEFORE
the first repair of the block.

** WHAT WAS ORDERED. **  `r7353` ①: *your `11` receipts first, then the queue -- and `S7` before
either.*  `S7` and `S10` landed as `r7354`; this file registers the block.

⛔ ** AND ONE OF THE ELEVEN IS ON THIS SEAT'S OWN DO-NOT-EDIT LIST. **  `L257…/V1` carries `5` of the
`30` rows and is ROUTED with a patch, never edited.  *The arm's population is therefore the `10`
receipts this seat may edit; the uniqueness arm keeps all `30` rows, because its question is why a row
is OWED and not who repairs it.*

** COMPUTES: ** the three registered bands and their decisive fractions under an exact binomial, and
the census of the block read from the stride file and the ledger.  No paper quantity, and no outcome:
`scored()` returns `None` until the result block is appended by the counting push.
"""
import collections
import io
import os
import re
import subprocess
from math import comb

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', '..', '..'))
STRIDE = os.path.join(ROOT, 'THE_REPAIR_STRIDE.tsv')
BASELINE = os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv')
SEAT = '60'
#: the queue, in the order `r7353` ② gives it
QUEUE = ('L259_the_distance_from_the_present', 'P08_slicing_operator',
         'L248_the_strike_broke_its_readers', 'L256_the_band_taken',
         'L280_the_decidable_claims', 'L556_registry_from_rows',
         'L276_the_representation_theory_probe', 'L560_pins_into_moving_prose',
         'L815_seam_phase_derived')
#: ⛔ two of the nine are on this seat's own DO-NOT-EDIT list -- the queue's FIRST item among them --
#: so their rows are ROUTED with patches and the arms are scored on the rest.
ROUTED_PREFIXES = ('L259_the_distance_from_the_present', 'L256_the_band_taken')

#: ⛔⛭ AND THE CENSUS IS PINNED FROM THE START THIS TIME.  *`r7356`'s registration read the LIVE
#: ledger and would have returned nothing to its own scoring push; the lesson is applied here rather
#: than repaired afterwards.*
CENSUS = ''                     # '' means HEAD-at-write; the landing push pins it to the sha below
CENSUS_SHA = None               # filled by the first repair commit's parent

# ── arm ⒜: the uniqueness share of the queue's 19 owed rows ──────────────────────────────────────
#   Same arbiter as `r7356`: a row is a uniqueness problem when its literal occurs MORE THAN ONCE in
#   a single file of the text it is pinned into.
#   ⚠ The two existing measurements STRADDLE this central: `cc66` read 0 of 7 on its block, this seat
#   read 17 of 30 on its own.  ⇒ The band can fail toward either seat's reading.
A_SPACE = 19
A_CENTRAL = 0.30
A_BAND = (0.20, 0.55)

# ── arm ⒝: receipts whose FIRST repair form was UNKEYABLE ────────────────────────────────────────
#   `r7356`'s last finding, four faces deep: the instrument keys a literal standing to the left of an
#   `in` and nothing else, so a condition that strengthens membership into a count -- or a literal
#   whose escaping decodes to a control character -- leaves the ledger describing nothing.
#   ** A receipt counts when its FIRST form, written before the gate ran, would have done that --
#   measured by running the gate, not by recalling what was written. **
B_SPACE = 7
B_CENTRAL = 2
B_BAND = (1, 4)

# ── the effort reading, reported and not banded (`r7351` ②) ──────────────────────────────────────
EFFORT_MEASURED = (0.7, 1.6, 6.96)   # the other seat's two, and this seat's own from `r7356`
EFFORT_SUPERSEDES = 8.0

RESULT = {}


def decisive(space, central, band):
    p = central / space
    return sum(comb(space, k) * p ** k * (1 - p) ** (space - k)
               for k in range(space + 1) if k < band[0] or k > band[1])


def decisive_share(n, central, band):
    lo, hi = band[0] * n, band[1] * n
    return sum(comb(n, k) * central ** k * (1 - central) ** (n - k)
               for k in range(n + 1) if k < lo or k > hi)


def _rows(path):
    return [l.rstrip('\n').split('\t') for l in io.open(path, encoding='utf-8')
            if l.startswith('receipts/')]


def prefixes():
    return {l.split('\t')[1] for l in io.open(STRIDE, encoding='utf-8')
            if l.strip() and not l.startswith('#') and l.split('\t')[0] == SEAT}


def block(sha=None):
    """{receipt: owed rows} for the QUEUE, read at `sha` when one is given"""
    rows = _rows_at(sha) if sha else _rows(BASELINE)
    return collections.Counter(r[0] for r in rows
                               if r[5] == 'REPAIR-OWED'
                               and any(r[0].split('/')[1].startswith(q[:14]) for q in QUEUE))


def _rows_at(sha):
    txt = subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:corpus/quote_pin_baseline.tsv'],
                         capture_output=True, text=True, errors='replace').stdout
    return [l.rstrip('\r').split('\t') for l in txt.split('\n') if l.startswith('receipts/')]


def owed(sha=None):
    """the queue's owed rows.  ** Pass the census sha to read them where they stood. **"""
    rows = _rows_at(sha) if sha else _rows(BASELINE)
    return [r for r in rows if r[5] == 'REPAIR-OWED'
            and any(r[0].split('/')[1].startswith(q[:14]) for q in QUEUE)]


def routed(sha=None):
    return [r for r in owed(sha)
            if any(r[0].split('/')[1].startswith(q[:14]) for q in ROUTED_PREFIXES)]


def _corpus_texts():
    """the corpus text a row can be pinned into: the papers, and the registers under `corpus/`"""
    out = {}
    for d in (os.path.join(ROOT, 'corpus'),):
        for f in sorted(os.listdir(d)):
            if f.endswith(('.tex', '.md', '.tsv', '.txt')):
                out[f] = io.open(os.path.join(d, f), encoding='utf-8', errors='replace').read()
    return out


def uniqueness(rows=None, texts=None):
    """{(receipt, literal): max occurrences in any single corpus file} -- the arbiter, fixed here"""
    rows = owed() if rows is None else rows
    texts = _corpus_texts() if texts is None else texts
    out = {}
    for r in rows:
        lit = r[1][1:-1] if r[1].startswith('"') else r[1]
        lit = lit.replace('\\"', '"').replace('\\\\', '\\')
        flat = re.sub(r'\s+', ' ', lit)
        best = 0
        for name, body in texts.items():
            n = re.sub(r'\s+', ' ', body).count(flat) if flat else 0
            best = max(best, n)
        out[(r[0], r[1])] = best
    return out


def scored():
    """the two arms against their bands -- None until the result block is appended"""
    if not RESULT:
        return None
    out = {}
    if RESULT.get('A_MULTI') is not None:
        share = RESULT['A_MULTI'] / RESULT['A_ROWS']
        out['a'] = (share, A_BAND, A_BAND[0] <= share <= A_BAND[1],
                    decisive_share(RESULT['A_ROWS'], A_CENTRAL, A_BAND))
    if RESULT.get('B_UNKEYABLE') is not None:
        b = RESULT['B_UNKEYABLE']
        out['b'] = (b, B_BAND, B_BAND[0] <= b <= B_BAND[1], decisive(B_SPACE, B_CENTRAL, B_BAND))
    return out


if __name__ == '__main__':
    _o = owed()
    _r = routed()
    print()
    print("  60 -- THE HAND-OFF QUEUE, REGISTERED BEFORE THE FIRST REPAIR")
    print()
    print(f'    the queue, {len(QUEUE)} prefixes in the order given: {len(_o)} owed rows')
    print(f'    \u26d4 of those, {len(_r)} row(s) in '
          f'{len({r[0] for r in _r})} receipt(s) are on this seat\'s DO-NOT-EDIT list and are ROUTED')
    print(f'    \u21d2 the arms are scored on {len(_o) - len(_r)} rows in '
          f'{len({r[0] for r in _o}) - len({r[0] for r in _r})} receipts')
    print()
    print(f'    arm (a): central {A_CENTRAL}, band {A_BAND[0]}-{A_BAND[1]}, two-sided, '
          f'decisive {decisive_share(A_SPACE, A_CENTRAL, A_BAND):.3f} at {A_SPACE} rows')
    print(f'    arm (b): central {B_CENTRAL} of {B_SPACE}, band {B_BAND[0]}-{B_BAND[1]}, '
          f'two-sided, decisive {decisive(B_SPACE, B_CENTRAL, B_BAND):.3f}')
    print(f'    effort: reported in minutes a receipt, beside {EFFORT_MEASURED} and the '
          f'{EFFORT_SUPERSEDES} the phase was priced on -- NOT banded')
    print()
    for _p, _n in sorted(block().items(), key=lambda kv: (-kv[1], kv[0])):
        _flag = 'ROUTED' if any(_p.split('/')[1].startswith(q[:14]) for q in ROUTED_PREFIXES) else ''
        print(f'      {_n:2d}  {_p.split("/")[1][:34]:34s} {_flag}')
    print()
