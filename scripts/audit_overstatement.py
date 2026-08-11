#!/usr/bin/env python3
"""audit_overstatement.py -- does every open item still say what its paper says?

** THE FINDING THIS INSTRUMENT EXISTS FOR, and it is nine instances deep before the instrument was
built: **

    L-209 (r2391)  the answer sat two sections above the question, in the same file
    B1    (r2400)  P8's "principal open problem" is a CROSS-REFERENCE -- P9 answers it
    B2    (r2400)  "the matter sector is unbuilt" is NOT what P7 says: the flavour skeleton is BUILT
    B21   (r2401)  "the reach established ..." is a SCOPE DECLARATION wearing open-language
    U1    (r2398)  P16 answers a question in the next sentence and never asks it
    V1/G1 (r2416)  cor:carter's chain is complete; the corollary is 23,281 chars from the mechanism
    G3    (r2418)  the axis objection was a MISPARSE; the corpus defines the axis three times
    L-200 (r2422)  the residue was already counted in sec:ledger, two sections from the item asking
    L-207 (r2424)  the row's framing came from a % COMMENT the published text contradicts

⇒ ** THE PROGRAMME'S OPEN ITEMS ARE SYSTEMATICALLY OVERSTATED RELATIVE TO WHAT THE CORPUS
   ESTABLISHES, AND THE OVERSTATEMENT LIVES IN THE NAVIGATION LAYER -- comments, maps, register rows,
   frontier lists -- NOT IN THE PAPERS. **

WHAT THIS CHECKS, and it is deliberately narrow.  For every OPEN register row that cites a labelled
result (`thm:`, `cor:`, `prop:`, `sec:`, `rem:`, `lem:`), it asks three mechanical questions:

    (1) DOES THE LABEL STILL EXIST?      A row citing a label no longer in the corpus is stale by
                                         construction.
    (2) IS THE CITED SITE A % COMMENT?   The L-207 class: a working note quoted as though published.
    (3) [REMOVED r2425] DID THE PAPER CARRY CLOSING LANGUAGE NEAR THE CITED LABEL?  ** Tried, and
                                         7/7 false positives.  See the CLOSING note below. **
                                         What (1) and (2) have that (3) lacked: they are BINARY and
                                         need no threshold and no judgement about a subject.

** IT FLAGS FOR READING AND DECIDES NOTHING. **  (3) in particular is a POINTER: closing language near
a label is a reason to read, never a verdict that the item closed.  The register's own first lesson
applies -- ** an advertised door is a claim to dig, never a fact ** -- and its converse applies here
just as hard: ** a closure phrase near a label is a claim to dig, not a strike. **

⚠ AND ONE THING THIS DELIBERATELY DOES NOT DO: it does not score DISTANCE.  G1 tried that and G2's
blind run broke it -- ** the quantity was wrong, not the threshold **, because a result that carries
its argument inside itself needs no nearby support.  This checks EXISTENCE and LANGUAGE, both of which
are binary and neither of which needs a threshold this line invented.

    python3 scripts/audit_overstatement.py
    python3 scripts/audit_overstatement.py --check    # exit 1 if any row cites a dead label

Written r2425.  Stated for reversal.
"""
import os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

LABEL = re.compile(r'`((?:sec|thm|cor|prop|rem|lem|eq|fig):[A-Za-z0-9:_-]+)`')

# ** THE PHRASE TEST IS REMOVED, r2425, ON 7/7 EVIDENCE.  Its first run flagged seven
# rows and ALL SEVEN were false positives, each for a different reason:
#     "is built"    -> "the background geometry on which the cosmology IS BUILT"
#     "is settled"  -> a HOLONOMY being genuine rather than a branch convention
#     "resolved"    -> the title of a NEIGHBOURING remark (rem:perroot)
#     "is settled"  -> a CONNECTION PROBLEM at the branch point
#     "no longer"   -> "at Nariai the mass is NO LONGER FREE"
#     "is answered" -> the range cross-reference, already worked at B1
# ** A phrase test measures a string whose meaning depends entirely on its subject.  It is
#    the distance metric's error (G1/G2) in a new costume: the QUANTITY is wrong, not the
#    threshold. **
#
# ⌗ AND IT EARNED ITS COST ANYWAY, SIDEWAYS, WHICH IS WORTH RECORDING RATHER THAN DRESSING
# UP AS SUCCESS: reading one of its false positives found that P15 sec:predictions WITHDRAWS
# "the construction has no scale-invariant attractor at all" and the unqualified phrase then
# survives TWICE in the paper's own verdict passages.  ** A cheap noisy instrument can pay
# for itself by making you read a passage you would not have opened -- but that is a property
# of the READING, not evidence for the instrument. **
CLOSING = []   # deliberately empty; see above.  Do not repopulate without new evidence.


def papers():
    out = {}
    for p in glob.glob(os.path.join(ROOT, 'corpus', '*.tex')):
        b = os.path.basename(p)
        if b.startswith('appendix'):
            continue
        out[b] = open(p, encoding='utf-8', errors='replace').read()
    return out


def open_rows():
    t = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    rows = []
    for ln in t.split('\n'):
        m = re.match(r'^\|\s*\*\*(L-\d+)\*\*\s*\|', ln)
        if not m:
            continue
        labels = sorted(set(LABEL.findall(ln)))
        if labels:
            rows.append((m.group(1), labels))
    return rows


def locate(pap, label):
    """(paper, index, is_comment) for each occurrence of \\label{label}."""
    hits = []
    for name, src in pap.items():
        for m in re.finditer(r'\\label\{' + re.escape(label) + r'\}', src):
            ls = src.rfind('\n', 0, m.start())
            hits.append((name, m.start(), src[ls:m.start()].lstrip().startswith('%')))
    return hits


def main():
    pap = papers()
    rows = open_rows()
    print()
    print(f'  OVERSTATEMENT AUDIT -- {len(rows)} open row(s) citing a labelled result, '
          f'against {len(pap)} paper(s)')
    print()
    print('  ** Flags are POINTERS TO A READING, never verdicts.  A closure phrase near a label is')
    print('     a claim to dig, not a strike -- the register\'s own first lesson, run the other way. **')
    print()

    dead, commented, flagged = [], [], []
    for lid, labels in rows:
        lines = []
        for lab in labels:
            hits = locate(pap, lab)
            if not hits:
                dead.append((lid, lab))
                lines.append(f'      ⛔ DEAD    {lab}  -- no \\label in any paper')
                continue
            name, at, is_comment = hits[0]
            if is_comment:
                commented.append((lid, lab, name))
                lines.append(f'      ⚠ COMMENT {lab}  -- defined inside a % line ({name})')
                continue
            src = pap[name]
            window = re.sub(r'\s+', ' ', src[at:at + 3000]).lower()
            found = [c for c in CLOSING if c in window]
            if found:
                flagged.append((lid, lab, name, found[:3]))
                lines.append(f'      ⌗ READ    {lab}  ({name}) -- closing language near it: '
                             f'{", ".join(found[:3])}')
        if lines:
            print(f'    {lid}')
            for x in lines:
                print(x)
    print()
    print(f'  {len(dead)} dead label(s) · {len(commented)} defined in comments · '
          f'{len(flagged)} carrying closing language nearby')
    print()
    if dead:
        print('  ⛔ A row citing a label that no longer exists is stale BY CONSTRUCTION -- that is the')
        print('     only category here that is a finding rather than a pointer.')
        for lid, lab in dead:
            print(f'     [FAIL] {lid} cites {lab}')
        print()
    if flagged:
        print('  ⌗ And the pointers: each is a row whose cited section sits near language the corpus')
        print('    uses when it CLOSES something.  ** Read the paper, not the flag. **')
        print()
    if '--check' in sys.argv and dead:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
