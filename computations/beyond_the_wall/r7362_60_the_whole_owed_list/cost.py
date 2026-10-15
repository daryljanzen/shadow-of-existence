#!/usr/bin/env python3
"""`60`'s next revision -- THE WHOLE OWED LIST, MEASURED RATHER THAN REPAIRED: the arithmetic of the
registration, written and pushed BEFORE the measurement is taken.

** WHY A MEASUREMENT AND NOT A REPAIR. **  `r7360` closed the last block this seat can take: of the
`83` owed rows that remain, `74` carry `69`'s reading, three `70.1`'s and four `cc66`'s, and the last
two are this seat's own and routed.  ** Not one is takeable without reaching into another seat's
reading, and partitioning that is `66`'s to do, not this seat's. **  The other open frontier row is
blocked on a SAMPLE rather than on work.
  ⇒ *So the one piece of `PO-78` work left that collides with nobody is to READ the population.*

** AND IT ANSWERS A QUESTION ASKED TWICE AND ANSWERED THREE TIMES BADLY. **  `r7351` ③ asked whether
the owed list is a uniqueness backlog.  Three readings now exist on `r7358`'s refined arbiter --
`0.167`, `0.263`, `0.286` -- ** and every one is on a block chosen by WHO REPAIRED IT, which is this
seat. **  *That is the wrong sampling for a question about the class: a share measured on the rows one
seat noticed may be a fact about the noticing.*
  ⇒ ** Reading all `83` that remain measures the population; reading `69`'s `74` ALONE against a band
    drawn from this seat's own blocks decides which of the two it is. **

** COMPUTES: ** the three registered bands and their decisive fractions under an exact binomial, and
the census of the owed list read from the ledger AT A PINNED SHA.  No paper quantity, and no outcome:
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
#: ⛭ pinned from the start, as `r7356` learned and `r7358` learned twice: a measurement a revision
#: takes of a file the revision edits cannot be read live.  This one edits no ledger row at all,
#: which is the point -- and the sha is pinned anyway, so the reading is reproducible by anyone.
CENSUS = '8ddce199'            # r7360's last commit, where this population was read
READER = re.compile(r'r\d+\+([0-9a-z.]+)')

# ── arm ⒜: the refined uniqueness share over ALL the owed rows ───────────────────────────────────
#   The arbiter is `r7358`'s refinement in the form `r7360` used: max occurrences of the literal in
#   any single file of `corpus/`'s text, THE LEDGERS EXCLUDED, because a literal standing twice in a
#   baseline is twice adjudicated and not twice claimed.
#   Central from this seat's three block readings, weighted by their row counts: (5+5+10)/84 = 0.238.
A_SPACE = 83
A_CENTRAL = 0.24
A_BAND = (0.17, 0.31)          # 15 to 25 rows; decisive 0.157

# ── arm ⒝: THE SAMPLING TEST, and it is the one that matters ─────────────────────────────────────
#   The same share on the `74` rows `69` read, scored against a band drawn from THIS seat's blocks.
#   ** IN BAND means the share is a property of the CLASS -- two seats reading independently find the
#   same proportion.  OUT means it is a property of the READER: what a seat notices as owed carries
#   its own signature, and three block readings cannot be pooled into a corpus figure. **
#   ⚠ Either outcome is a result and neither is a defect; the arm exists because the question cannot
#   be settled by more of this seat's own blocks.
B_SPACE = 74
B_CENTRAL = 0.24
B_BAND = (0.16, 0.32)          # decisive 0.102

# ── arm ⒞: what the refined arbiter CANNOT SEE, as a share of the whole list ─────────────────────
#   The price `r7360` measured on its own block at `11` of `35` = `0.31`.  Here `48` of the `83` are
#   `SOURCE` pins -- into `scripts/`, the root registers and live instruments -- so the blind share
#   should be HIGHER, and how much higher is the cost of the refinement stated on the population
#   rather than on one block.
C_SPACE = 83
C_CENTRAL = 0.35
C_BAND = (0.27, 0.43)          # decisive 0.134

RESULT = {}


def decisive_share(n, central, band):
    lo, hi = band[0] * n, band[1] * n
    return sum(comb(n, k) * central ** k * (1 - central) ** (n - k)
               for k in range(n + 1) if k < lo or k > hi)


def _rows_at(sha):
    txt = subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:corpus/quote_pin_baseline.tsv'],
                         capture_output=True, text=True, errors='replace').stdout
    return [l.rstrip('\r').split('\t') for l in txt.split('\n') if l.startswith('receipts/')]


def owed(sha=CENSUS):
    """every REPAIR-OWED row at `sha`, whoever read it"""
    rows = _rows_at(sha) if sha else [
        l.rstrip('\n').split('\t') for l in io.open(BASELINE, encoding='utf-8')
        if l.startswith('receipts/')]
    return [r for r in rows if len(r) >= 6 and r[5] == 'REPAIR-OWED']


def reader_of(row):
    m = READER.match(row[6] if len(row) > 6 else '')
    return m.group(1) if m else '?'


def by_reader(sha=CENSUS):
    return collections.Counter(reader_of(r) for r in owed(sha))


def _corpus_texts(sha=None):
    """the text a row can be pinned into, LEDGERS EXCLUDED -- `r7358`'s registered refinement"""
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
    for key, (num, den, central, band) in {
            'a': ('A_MULTI', 'A_ROWS', A_CENTRAL, A_BAND),
            'b': ('B_MULTI', 'B_ROWS', B_CENTRAL, B_BAND),
            'c': ('C_BLIND', 'A_ROWS', C_CENTRAL, C_BAND)}.items():
        if RESULT.get(num) is None:
            continue
        s = RESULT[num] / RESULT[den]
        out[key] = (s, band, band[0] <= s <= band[1],
                    decisive_share(RESULT[den], central, band))
    return out


if __name__ == '__main__':
    _o = owed()
    _r = by_reader()
    print()
    print('  60 -- THE WHOLE OWED LIST, REGISTERED BEFORE THE MEASUREMENT')
    print()
    print(f'    the owed list at the pinned census {CENSUS}: {len(_o)} rows in '
          f'{len({r[0] for r in _o})} receipts over {len({r[0].split("/")[1] for r in _o})} prefixes')
    print(f'    by the seat that READ each row: {dict(_r)}')
    print(f'    by target: {dict(collections.Counter(r[2] for r in _o))}; '
          f'by tier: {dict(collections.Counter(r[3] for r in _o))}')
    print()
    print(f'    arm (a) refined share, ALL {A_SPACE}: central {A_CENTRAL}, band '
          f'{A_BAND[0]}-{A_BAND[1]}, two-sided, decisive '
          f'{decisive_share(A_SPACE, A_CENTRAL, A_BAND):.3f}')
    print(f'    arm (b) THE SAMPLING TEST, the {B_SPACE} rows the other reader filed: central '
          f'{B_CENTRAL}, band {B_BAND[0]}-{B_BAND[1]}, decisive '
          f'{decisive_share(B_SPACE, B_CENTRAL, B_BAND):.3f}')
    print(f'    arm (c) what the refined arbiter cannot SEE, of {C_SPACE}: central {C_CENTRAL}, '
          f'band {C_BAND[0]}-{C_BAND[1]}, decisive '
          f'{decisive_share(C_SPACE, C_CENTRAL, C_BAND):.3f}')
    print()
    print('    ⛔ NO REPAIR IS REGISTERED HERE.  *Every remaining row belongs to another seat\'s')
    print('      reading, and this revision reads rows and edits no receipt of anyone\'s.*')
    print()


# ══════════════════════════════════════════════════════════════════════════════════════════════════
# THE RESULT BLOCK, appended by the counting push.  ** Nothing above this line was changed. **
# ══════════════════════════════════════════════════════════════════════════════════════════════════
RESULT.update({
    # ── the population at the pinned census ──
    'A_ROWS': 83,              # 24 receipts over 21 prefixes
    'BY_READER': {'69': 74, '70.1': 3, 'cc66.185': 4, '60': 2},
    'BY_TARGET': {'PAPER': 35, 'SOURCE': 48},
    'BY_TIER': {'SENTENCE': 49, 'TOKEN': 34},

    # ── arm ⒜: the refined share over the whole list ──
    'A_MULTI': 23,             # 23 of 83 = 0.277, INSIDE the 0.17-0.31 band

    # ── arm ⒝: THE SAMPLING TEST ──
    #   ⛭⛭ IN BAND.  The share on the rows the OTHER reader filed lands inside a band drawn from
    #   this seat's own blocks, so the proportion is a property of the CLASS and not of the noticing.
    'B_ROWS': 74,
    'B_MULTI': 17,             # 17 of 74 = 0.230, INSIDE the 0.16-0.32 band

    # ── arm ⒞: what the refined arbiter cannot see ──
    'C_BLIND': 31,             # 31 of 83 = 0.373, INSIDE the 0.27-0.43 band
    #   ⌗ and the blind set is ENTIRELY a SOURCE phenomenon: 31 of the 48 SOURCE rows are unseen and
    #   0 of the 35 PAPER rows are.  The refinement's price falls on one target and not on both.
    'C_BLIND_SOURCE': 31,
    'C_BLIND_PAPER': 0,

    # ── the structure the arms were not registered to find ──
    #   ⛭⛭⛭ UNIQUENESS FAILURE IS A **TOKEN** PHENOMENON, five-fold: 18 of the 34 TOKEN rows are
    #   multi-site and 5 of the 49 SENTENCE rows are.  ⇒ The owed list is not "a uniqueness backlog";
    #   it is a TOKEN backlog, and non-uniqueness is what a token pin LOOKS LIKE from the arbiter's
    #   side.  That is the same identity r7356 claimed between its two arms and r7358 withdrew --
    #   arriving here on the population, between different quantities, and holding.
    'TOKEN_ROWS': 34, 'TOKEN_MULTI': 18,          # 0.529
    'SENTENCE_ROWS': 49, 'SENTENCE_MULTI': 5,     # 0.102
    'PAPER_MULTI': 13, 'SOURCE_MULTI': 10,        # 0.371 against 0.208
    'SEEN_ROWS': 52, 'SEEN_MULTI': 23,            # 0.442 over what the arbiter can see
    'MAX_OCCURRENCES': 9647,                      # one literal, in a single file: the word "no"
})

#: ⛭⛭⛭ THE ANSWER TO `r7351` ③, AND IT IS NOT THE ANSWER EITHER SEAT GAVE.
#: *`cc66` read `0` of `7` and called the owed list no uniqueness backlog; this seat read `17` of `30`
#: and called it one; `r7358` then found the second figure counting its own ledger and withdrew it.*
#:   ⇒ ** On the whole population, with the ledgers out: `23` of `83` = `0.277`. About one owed row in
#:     four. **  Neither "mainly" nor "not at all".
#:   ⇒⇒ *** AND THE FIGURE IS A PROPERTY OF THE CLASS RATHER THAN OF THE READER, WHICH IS THE PART
#:       NEITHER SEAT COULD HAVE SHOWN ALONE: the `74` rows the other reader filed come in at `0.230`,
#:       inside a band drawn from this seat's own three blocks. ***  Two seats reading independently
#:       find the same proportion, so the three block readings CAN be pooled -- which the arm was
#:       registered to test rather than to assume.
#:   ⌗ ** And the structure under it is sharper than the share: ** uniqueness failure is a TOKEN
#:     phenomenon five-fold over, `0.529` against `0.102`.  *The owed list is a TOKEN backlog, and
#:     non-uniqueness is what a token pin looks like from the arbiter's side.*
