#!/usr/bin/env python3
"""`60`'s next revision -- THE ROWS THIS SEAT ITSELF READ: the arithmetic of the registration, written
and pushed BEFORE the first repair.

** WHY THIS BLOCK, AND WHY IT CANNOT COLLIDE. **  `r7353` ② wrote a hand-off queue *"so you never idle
and no two seats can collide"*, and `r7358` closed the last of it.  ** The queue is exhausted and no
order names what follows, so the block is chosen by the one property the ledger itself records: WHO
READ THE ROW. **  Every owed row carries the stride that filed it (`rNNNN+<seat>`), and `37` of the
`118` still open say `+60`.
  ⇒ *A row this seat read is a row no other seat's queue was built from -- `70`'s list produced the
    queue just closed, and `69`'s `74` rows are `69`'s own reading.*  ** So this is the largest block
    that is collision-free by the ledger rather than by coordination, and taking it needs no ruling. **
⛔ *Two of the `37` sit on `L256…/B1`, this seat's own do-not-edit list, and are ROUTED with patches --
the same two `r7358` routed.  The arms are scored on the `35` editable rows in `11` prefixes.*

** COMPUTES: ** the three registered bands and their decisive fractions under an exact binomial, and
the census of the block read from the ledger AT A PINNED SHA.  No paper quantity, and no outcome:
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
BASELINE = os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv')
SEAT = '60'
#: ⛭ the census is PINNED from the start, as `r7356`'s lesson requires and `r7358` confirmed twice:
#: a measurement a revision takes of a file the revision EDITS cannot be read live.
CENSUS = '34cc9f9b'            # r7358's landing head, the commit this block was read at
#: ⛔ the seat's own do-not-edit list, intersected with this block
ROUTED_PREFIXES = ('L256_the_band_taken',)
READER = re.compile(r'r\d+\+([0-9a-z.]+)')

# ── arm ⒜: the refined uniqueness share, on the refinement r7358 REGISTERED ──────────────────────
#   `r7358` found the registered arbiter counting `corpus/`'s own LEDGERS -- the baselines that hold
#   the adjudication rows -- so closing a row deleted occurrences of the literal that row was about.
#   The refinement excludes them, and read that way the two scored blocks give 0.263 (the queue) and
#   0.167 (the eleven).  ** This is the first revision to USE it rather than report it. **
#   ⚠ And it is a weaker guarantee than an untouched arbiter: the refinement was found by this seat
#   in the course of failing its own arm, so the band is set wide around the two readings it has.
#   ⌗ The band is set so the arm can DECIDE: two-sided at 0.145, which is above the 0.10 this phase
#   has held every arm to.  A wider band around two readings would have been honest and useless.
A_SPACE = 35
A_CENTRAL = 0.21
A_BAND = (0.10, 0.31)          # 4 to 10 of the 35 rows

# ── arm ⒝: the share whose repair is REPAIRED-AND-INVISIBLE ──────────────────────────────────────
#   `r7353` ③ ruled the form: where no pin is ADMISSIBLE the repair is a STRUCTURAL ASSERTION and the
#   row retires as repaired-and-invisible.  `r7338` measured the invisible share at 0.051 on 59 rows
#   and `cc66` read 0.70 on its own, which is the widest disagreement of the phase.
#   ⚠ The two readings are so far apart because the quantity is partly a CHOICE: a seat that prefers
#   parsing to pinning reads high while making the corpus stronger.  So the band is set around what
#   THIS block looks like -- five of the 35 rows are code spellings on sight -- and a failure in
#   either direction is a reading of this seat's own preference, not of the class.
B_SPACE = 35
B_CENTRAL = 0.20
B_BAND = (0.10, 0.31)          # 4 to 10 of the 35 rows, decisive 0.135

# ── arm ⒞: the effort, BANDED for the first time (`r7351` ②) ─────────────────────────────────────
#   Two strides of this seat are measured -- 6.96 minutes a receipt at `r7356`, 3.63 at `r7358` --
#   and `r7358` refused to band on two.  ** A third measurement scores a band, so the band is
#   declared here, before the work, from the two that exist. **
#   ⚠ Wall-clock on one container with the trunk moving under it, so the band is wide and two-sided.
C_SPACE = 13                   # receipts, the unit both measurements were taken in
C_CENTRAL = 5.0                # minutes a receipt
C_BAND = (3.0, 8.0)
EFFORT_MEASURED = (0.7, 1.6, 6.96, 3.63)
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


def _rows_at(sha):
    txt = subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:corpus/quote_pin_baseline.tsv'],
                         capture_output=True, text=True, errors='replace').stdout
    return [l.rstrip('\r').split('\t') for l in txt.split('\n') if l.startswith('receipts/')]


def _rows(path):
    return [l.rstrip('\n').split('\t') for l in io.open(path, encoding='utf-8')
            if l.startswith('receipts/')]


def owed(sha=CENSUS):
    """the owed rows THIS SEAT read, at `sha` -- the whole block, routed rows included"""
    rows = _rows_at(sha) if sha else _rows(BASELINE)
    out = []
    for r in rows:
        if len(r) < 6 or r[5] != 'REPAIR-OWED':
            continue
        m = READER.match(r[6] if len(r) > 6 else '')
        if m and m.group(1) == SEAT:
            out.append(r)
    return out


def routed(sha=CENSUS):
    return [r for r in owed(sha)
            if any(r[0].split('/')[1].startswith(p) for p in ROUTED_PREFIXES)]


def block(sha=CENSUS):
    return collections.Counter(r[0] for r in owed(sha))


def _corpus_texts(sha=None):
    """the corpus text a row can be pinned into, LEDGERS EXCLUDED -- `r7358`'s registered refinement:
    a literal standing twice in a baseline is twice ADJUDICATED, not twice claimed."""
    names = sorted(f for f in os.listdir(os.path.join(ROOT, 'corpus'))
                   if f.endswith(('.tex', '.md', '.tsv', '.txt'))
                   and 'baseline' not in f and 'annotation' not in f)
    if sha:
        out = {f: subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:corpus/{f}'],
                                 capture_output=True, text=True, errors='replace').stdout
               for f in names}
        return {k: v for k, v in out.items() if v}
    return {f: io.open(os.path.join(ROOT, 'corpus', f), encoding='utf-8',
                       errors='replace').read() for f in names}


def uniqueness(rows=None, texts=None):
    """{(receipt, literal): max occurrences in any single corpus file} -- the REFINED arbiter"""
    rows = owed() if rows is None else rows
    texts = _corpus_texts(CENSUS) if texts is None else texts
    out = {}
    for r in rows:
        lit = r[1][1:-1] if r[1].startswith('"') else r[1]
        lit = lit.replace('\\"', '"').replace('\\\\', '\\')
        flat = re.sub(r'\s+', ' ', lit)
        best = 0
        for body in texts.values():
            best = max(best, re.sub(r'\s+', ' ', body).count(flat) if flat else 0)
        out[(r[0], r[1])] = best
    return out


def scored():
    """the three arms against their bands -- None until the result block is appended"""
    if not RESULT:
        return None
    out = {}
    if RESULT.get('A_MULTI') is not None:
        s = RESULT['A_MULTI'] / RESULT['A_ROWS']
        out['a'] = (s, A_BAND, A_BAND[0] <= s <= A_BAND[1],
                    decisive_share(RESULT['A_ROWS'], A_CENTRAL, A_BAND))
    if RESULT.get('B_INVISIBLE') is not None:
        s = RESULT['B_INVISIBLE'] / RESULT['A_ROWS']
        out['b'] = (s, B_BAND, B_BAND[0] <= s <= B_BAND[1],
                    decisive_share(RESULT['A_ROWS'], B_CENTRAL, B_BAND))
    if RESULT.get('EFFORT_PER_RECEIPT') is not None:
        e = RESULT['EFFORT_PER_RECEIPT']
        out['c'] = (e, C_BAND, C_BAND[0] <= e <= C_BAND[1], None)
    return out


if __name__ == '__main__':
    _o, _r = owed(), routed()
    print()
    print('  60 -- THE ROWS THIS SEAT ITSELF READ, REGISTERED BEFORE THE FIRST REPAIR')
    print()
    print(f'    read at the pinned census {CENSUS}: {len(_o)} owed rows the ledger credits to this '
          f'seat’s own strides, in {len({r[0] for r in _o})} receipts')
    print(f'    ⛔ of those, {len(_r)} row(s) are on this seat’s DO-NOT-EDIT list and are ROUTED')
    print(f'    ⇒ the arms are scored on {len(_o) - len(_r)} rows in '
          f'{len({r[0] for r in _o}) - len({r[0] for r in _r})} receipts')
    print()
    print(f'    arm (a) refined uniqueness share: central {A_CENTRAL}, band {A_BAND[0]}-{A_BAND[1]}, '
          f'two-sided, decisive {decisive_share(A_SPACE, A_CENTRAL, A_BAND):.3f} at {A_SPACE} rows')
    print(f'    arm (b) repaired-and-invisible share: central {B_CENTRAL}, band '
          f'{B_BAND[0]}-{B_BAND[1]}, two-sided, decisive '
          f'{decisive_share(B_SPACE, B_CENTRAL, B_BAND):.3f}')
    print(f'    arm (c) effort: central {C_CENTRAL} minutes a receipt, band {C_BAND[0]}-{C_BAND[1]}, '
          f'BANDED for the first time from the measured {EFFORT_MEASURED[2]} and '
          f'{EFFORT_MEASURED[3]}')
    print()
    for _p, _n in sorted(block().items(), key=lambda kv: (-kv[1], kv[0])):
        _f = 'ROUTED' if any(_p.split('/')[1].startswith(q) for q in ROUTED_PREFIXES) else ''
        print(f'      {_n:2d}  {_p.split("/")[1][:38]:38s} {_f}')
    print()


# ══════════════════════════════════════════════════════════════════════════════════════════════════
# THE RESULT BLOCK, appended by the counting push.  ** Nothing above this line was changed. **
# ══════════════════════════════════════════════════════════════════════════════════════════════════
RESULT.update({
    # ── the block as it stood at the census ──
    'A_ROWS': 35,              # the editable rows, 13 receipts over 11 prefixes
    'ROUTED_ROWS': 2,          # on L256/B1 -- routed with the patches r7358 already routed
    'CLOSED': 13,              # receipts taken and closed, every editable row of each
    'CLOSED_ROWS': 35,

    # ── arm (a): the REFINED uniqueness share, r7358's refinement in use for the first time ──
    'A_MULTI': 10,             # 10 of 35 = 0.286, INSIDE the 0.10-0.31 band
    'A_UNSEEN': 11,            # the refinement's price: SOURCE pins into scripts and root registers
    'A_MAX': 42,               # one literal ('stale') occurring 42 times in a single file

    # ── arm (b): the share whose repair is REPAIRED-AND-INVISIBLE ──
    #   ⌗ THE ARBITER, stated: a retired row counts when its claim is now carried by an assertion
    #   that pins NO text at all -- a syntax-tree read, or a read at a commit the instrument cannot
    #   trace.  A row whose span was merely NORMALISED, or that merged into a sibling's minted span,
    #   does NOT count: it is still pinned, and the ledger still holds it.
    'B_INVISIBLE': 7,          # 7 of 35 = 0.200, INSIDE the band and ON the central
    'B_MINTED': 24,            # keys minted at this revision, in 12 of the 13 receipts
    #   ⛔ and one more retired row pinned NOTHING to begin with, so it cannot be counted as
    #   invisible: there was nothing visible to lose.  See B_DEAD_REGEX below.
    'B_DEAD_REGEX': 1,

    # ── arm (c): the effort, banded for the first time -- and the band FAILS LOW ──
    'EFFORT_MINUTES': 28.8,        # census commit to the last take commit
    'EFFORT_PER_RECEIPT': 2.22,    # against the band 3.0-8.0: OUTSIDE, LOW
    'EFFORT_SERIES': (6.96, 3.63, 2.22),   # r7356, r7358, r7360 -- three consecutive falls
})

#: ⛔⛭⛭ WHAT ARM ⒞ ACTUALLY MEASURED, AND IT IS NOT WHAT IT WAS REGISTERED TO MEASURE.
#: *The band was drawn from the only two measurements that existed, `6.96` and `3.63`, and the third
#: came in at `2.22` -- below it.*
#:   ⇒ ** The three readings are `6.96`, `3.63`, `2.22`: a MONOTONE FALL, not three draws from a
#:     fixed per-receipt cost. **  The registration's own caveat says the binomial assumes a constant
#:     cost; the series says there is no constant to assume yet.
#:   ⇒ *** A BAND DRAWN FROM TWO CONSECUTIVE POINTS OF A FALLING SERIES FAILS LOW ON THE THIRD BY
#:     CONSTRUCTION. ***  That is a fact about the arm and not about the work, and it is reported as
#:     that: the honest figure is the series, and a band becomes possible when the fall stops.
#:   ⌗ `r7351` ② asked for a central from the measured strides.  This is the answer: **not yet** --
#:     and the reason is measurable rather than a hedge.

#: ⛔⛭ AND A NINTH DEFECT KIND, FOUND BY THE ARBITER REFUSING TO COUNT A ROW.
#: *One retired arm of `L548`'s three-way disjunction was a REGEX whose pattern does not match its
#: own target: it looked for `\delta{2}` where the paper writes `\delta^{2}`, so it matched nothing,
#: ever, on any tree.*
#:   ⇒ ** Not a weak arm -- a DEAD one, dead by construction rather than by the corpus moving. **
#:     The disjunction it stood in had three arms and all three were defective: this one could never
#:     fire, and the other two were clipped fragments.
#:   ⌗ It is excluded from arm ⒝ rather than counted: a row that pinned nothing cannot be
#:     repaired-and-invisible, because there was nothing visible to lose.
