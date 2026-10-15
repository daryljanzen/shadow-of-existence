#!/usr/bin/env python3
"""`60`'s next revision -- THE ELEVEN: the arithmetic of the registration, written and pushed BEFORE
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
ROUTED = 'L257'                 # the do-not-edit receipt's prefix: routed, never edited

# ── arm ⒜: receipts of the TEN closed in this revision ───────────────────────────────────────────
A_SPACE = 10
A_CENTRAL = 7
A_BAND = (6, 9)

# ── arm ⒝: the share of the 30 owed rows that are UNIQUENESS problems ────────────────────────────
#   `r7351` ③ registered rather than asserted.  ** A row is a uniqueness problem when its literal
#   occurs MORE THAN ONCE in a single file of the corpus text it is pinned into. **  Claim-completeness
#   is the complement: the literal is unique and the row is owed for what the span does not say.
B_SPACE = 30
B_CENTRAL = 0.15
B_BAND = (0.08, 0.33)

# ── arm ⒞: guards of the CANNOT-FAIL shape in the ten ────────────────────────────────────────────
#   `r7349` ②'s rate.  ** A guard counts when its condition is true of EVERY member of the class the
#   claim's subject belongs to, so it cannot distinguish the member the claim is about. **
C_SPACE = 10
C_CENTRAL = 1
C_BAND = (1, 3)

# ── the effort reading, drawn from the two measured strides and NOT banded (r7351 ②) ─────────────
EFFORT_CENTRAL_MIN_PER_RECEIPT = 1.5
EFFORT_SUPERSEDES = 8.0         # the figure the phase was priced on, not used as a central here

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


def block():
    """{receipt: owed rows} for this seat's remaining stride"""
    pref = prefixes()
    return collections.Counter(r[0] for r in _rows(BASELINE)
                               if r[5] == 'REPAIR-OWED' and r[0].split('/')[1] in pref)


def owed():
    pref = prefixes()
    return [r for r in _rows(BASELINE)
            if r[5] == 'REPAIR-OWED' and r[0].split('/')[1] in pref]


#: ⛭⛭ r7365 ③ + r7366: THE SELECTOR OF THIS MEASUREMENT'S TEXT SET, COMMITTED BESIDE THE
#: MEASUREMENT.  *`r7365` made it standing that **the selector of a measured population is committed
#: with the measurement, or the measurement is a claim and not a re-runnable fact** -- and arm ⒝'s
#: text frame was being supplied by `S50`'s own prose and a constant inside the receipt.*
#:   ⇒ *** The frame is this constant, and `_corpus_texts` takes it, so the arm is re-runnable by
#:     anyone holding this file alone. ***  ⚠ The default is unchanged, so nothing that read this
#:     function before reads anything different now: the registered arithmetic is untouched.
#:   ⌗ *And the frame is `r7356`'s OWN first commit, not its census: the arbiter was scored on the
#:     tree as it stood when the arm was taken, which is not the tree the OWED ROWS were read at.
#:     Two different pins in one measurement, and they are now both written down.*
FRAME = '5b76f80a'              # the tree arm (b)'s arbiter was scored on: r7356's own first commit


def _corpus_texts(sha=None):
    """the corpus text a row can be pinned into: the papers, and the registers under `corpus/`.
    With `sha`, the set AS IT STOOD at that commit -- the frame is `FRAME` and is committed here
    rather than described in a receipt's prose (`r7365` ③)."""
    if sha:
        names = subprocess.run(['git', '-C', ROOT, 'ls-tree', '--name-only', f'{sha}:corpus'],
                               capture_output=True, text=True, errors='replace').stdout.split()
        return {f: subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:corpus/{f}'],
                                  capture_output=True, text=True, errors='replace').stdout
                for f in sorted(names) if f.endswith(('.tex', '.md', '.tsv', '.txt'))}
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
    """the three arms against their bands -- None until the result block is appended"""
    if not RESULT:
        return None
    a = RESULT.get('A_CLOSED')
    b = RESULT.get('B_MULTI')
    c = RESULT.get('C_GUARDS')
    out = {}
    if a is not None:
        out['a'] = (a, A_BAND, A_BAND[0] <= a <= A_BAND[1], decisive(A_SPACE, A_CENTRAL, A_BAND))
    if b is not None:
        share = b / B_SPACE
        out['b'] = (share, B_BAND, B_BAND[0] <= share <= B_BAND[1],
                    decisive_share(B_SPACE, B_CENTRAL, B_BAND))
    if c is not None:
        out['c'] = (c, C_BAND, C_BAND[0] <= c <= C_BAND[1], decisive(C_SPACE, C_CENTRAL, C_BAND))
    return out


if __name__ == '__main__':
    _b = block()
    _o = owed()
    _routed = [r for r in _o if f'/{ROUTED}' in r[0]]
    print()
    print('  60 -- THE ELEVEN, REGISTERED BEFORE THE FIRST REPAIR')
    print()
    print(f'    prefixes assigned: {len(prefixes())};  owed receipts {len(_b)};  owed rows '
          f'{sum(_b.values())}, {sum(_b.values()) / len(_b):.2f} a receipt')
    print(f'    ⛔ of those, {len(_routed)} row(s) in {len({r[0] for r in _routed})} receipt(s) '
          f'are on this seat\'s DO-NOT-EDIT list and are ROUTED, never edited')
    print(f'    by target {dict(collections.Counter(r[2] for r in _o))};  '
          f'by tier {dict(collections.Counter(r[3] for r in _o))}')
    print()
    print(f'    arm (a): central {A_CENTRAL} of {A_SPACE}, band {A_BAND[0]}-{A_BAND[1]}, two-sided, '
          f'decisive {decisive(A_SPACE, A_CENTRAL, A_BAND):.3f}')
    print(f'    arm (b): central {B_CENTRAL}, band {B_BAND[0]}-{B_BAND[1]}, two-sided, '
          f'decisive {decisive_share(B_SPACE, B_CENTRAL, B_BAND):.3f} at {B_SPACE} rows')
    print(f'    arm (c): central {C_CENTRAL} of {C_SPACE}, band {C_BAND[0]}-{C_BAND[1]}, two-sided, '
          f'decisive {decisive(C_SPACE, C_CENTRAL, C_BAND):.3f}')
    print(f'    effort:  reported in minutes a receipt against {EFFORT_CENTRAL_MIN_PER_RECEIPT}, '
          f'drawn from the two measured strides and NOT from the {EFFORT_SUPERSEDES} the phase was '
          f'priced on -- reported, not banded')
    print()
    for _r, _n in sorted(_b.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f'      {_n:2d}  {_r.split("/")[1][:30]:30s} '
              f'{"ROUTED" if f"/{ROUTED}" in _r else ""}')
    print()


# ══════════════════════════════════════════════════════════════════════════════════════════════════
# THE RESULT, appended after the block closed.  ** No band, central or decisive fraction above is
# touched. **
#
# ⛔⛭⛭ AND ONE THING THE REGISTRATION GOT WRONG IN ITS OWN MACHINERY, DECLARED HERE RATHER THAN
# QUIETLY FIXED: `owed()` and `block()` above read the LIVE ledger.  ** The moment the block closed
# they returned nothing -- the census would have gone empty exactly when the work succeeded. **  That
# is the fail-on-success class this seat has now met five times, and this is the first time in a
# REGISTRATION rather than a receipt.  ⇒ The arbiter is unchanged; the population is simply read at
# `CENSUS`, the commit the block stood at before the first repair, and the receipt asserts it there.
# ══════════════════════════════════════════════════════════════════════════════════════════════════
CENSUS = 'af33966d'             # the tree before the first repair of this block


def owed_at(sha=CENSUS):
    """the block's owed rows, read at the commit they stood at -- what `owed()` should have been"""
    def _at(path):
        return subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:{path}'],
                              capture_output=True, text=True, errors='replace').stdout
    pref = {l.split('\t')[1] for l in _at('THE_REPAIR_STRIDE.tsv').split('\n')
            if l.strip() and not l.startswith('#') and l.split('\t')[0] == SEAT}
    return [l.rstrip('\r').split('\t') for l in _at('corpus/quote_pin_baseline.tsv').split('\n')
            if l.startswith('receipts/')
            and l.rstrip('\r').split('\t')[5] == 'REPAIR-OWED'
            and l.split('\t')[0].split('/')[1] in pref]


RESULT.update({
    # ── arm ⒜ -- receipts of the ten closed.  ⛔ OUTSIDE THE BAND, HIGH.
    'A_CLOSED': 10,
    # ── arm ⒝ -- the uniqueness share of the 30 owed rows.  ⛔ OUTSIDE THE BAND, HIGH, and it
    #   contradicts the expectation the order carried: `cc66` found 0 of 7 of its own block's
    #   literals occurring more than once, and this block reads 17 of 30.
    'B_MULTI': 17,
    'B_ROWS': 30,
    # ⚠ the arbiter's own blind spot, measured rather than described: 7 of the 30 literals occur
    #   NOWHERE in the text set it reads (`corpus/` only), because they are SOURCE pins into
    #   `scripts/`, `kills/` and the root registers.  Those 7 are counted as NOT multi-site, so the
    #   share is a LOWER BOUND and the arm fails high either way: over the 23 the arbiter can see it
    #   is 17 of 23.
    'B_UNSEEN': 7,
    # ── arm ⒞ -- receipts carrying a guard of the CANNOT-FAIL shape.  ⛔ OUTSIDE THE BAND, HIGH.
    'C_GUARDS': 7,
    # ⛭⛭ AND THE TWO ARMS TURNED OUT TO MEASURE ONE QUANTITY, WHICH NEITHER REGISTRATION SAW:
    #   a literal occurring more than once in the file its check reads CANNOT DISTINGUISH the site
    #   the claim is about, so every uniqueness failure IS a class-where-the-claim-is-about-a-member
    #   guard.  ⇒ Arm ⒞'s 7 is arm ⒝'s 17 projected onto receipts, and they are not independent.
    'C_IS_B_PROJECTED': True,
    # ── the effort reading, from the commit stamps rather than from an impression
    'EFFORT_MINUTES': 69.6,
    'EFFORT_PER_RECEIPT': 6.96,
    'REALISED': 10,
    # ── and the eleventh, routed rather than repaired
    'ROUTED_ROWS': 5,
})

if __name__ == '__main__':
    _o = owed_at()
    _u = uniqueness(_o)
    print('  THE RESULT')
    print()
    print(f'    owed at the census commit {CENSUS}: {len(_o)} rows')
    print(f'    arm (a): {RESULT["A_CLOSED"]} of {A_SPACE} closed, band {A_BAND} -- '
          f'{"INSIDE" if A_BAND[0] <= RESULT["A_CLOSED"] <= A_BAND[1] else "OUTSIDE, HIGH"}')
    _share = RESULT['B_MULTI'] / RESULT['B_ROWS']
    print(f'    arm (b): {RESULT["B_MULTI"]} of {RESULT["B_ROWS"]} = {_share:.4f}, band {B_BAND} -- '
          f'{"INSIDE" if B_BAND[0] <= _share <= B_BAND[1] else "OUTSIDE, HIGH"}; '
          f'{RESULT["B_UNSEEN"]} of the rows are outside the arbiter\'s text set, so this is a '
          f'LOWER bound')
    print(f'    arm (c): {RESULT["C_GUARDS"]} of {C_SPACE}, band {C_BAND} -- '
          f'{"INSIDE" if C_BAND[0] <= RESULT["C_GUARDS"] <= C_BAND[1] else "OUTSIDE, HIGH"}')
    print(f'    effort: {RESULT["EFFORT_MINUTES"]} minutes for {RESULT["REALISED"]} receipts = '
          f'{RESULT["EFFORT_PER_RECEIPT"]} a receipt, against the {EFFORT_CENTRAL_MIN_PER_RECEIPT} '
          f'drawn from the two measured strides (and the {EFFORT_SUPERSEDES} the phase was priced '
          f'on)')
    print(f'    routed, not repaired: {RESULT["ROUTED_ROWS"]} rows on the do-not-edit receipt')
    print()
