#!/usr/bin/env python3
"""G2_the_blind_run.py -- R-P station 34, probe G2: run the metric BLIND, and it breaks the metric.

WHY BLIND.  G1's three cases were all found by hand first and measured after.  ** That is validating
an instrument against itself: every case it was shown was a case someone had already judged. **  The
honest test is the reverse -- enumerate results with NO prior about any of them, measure, and see
whether the flags survive reading at source.

THE ENUMERATION, chosen mechanically: every \\begin{theorem|corollary|proposition|lemma} carrying a
\\label in P8 and P9.  Sixteen results, no selection.

WHAT IT FOUND, and it is a fault in the instrument rather than in the corpus:

  * ** Six of sixteen carry no \\begin{proof} at all. **  A distance-to-support metric reads that as
    maximum failure.
  * ** Five of those six justify IN-BODY, and correctly. **  thm:range names its own parts in the
    next sentence: "the upper bound is Theorem thm:bound; the filling is Proposition prop:surj
    realized class by class; the boundary statement is the corollary."  prop:typeI's are "these are
    computational facts".  cor:wall and cor:radiation argue inside themselves.
    ⇒ ** A result that carries its argument inside itself needs no proof environment. **
  * ** The sixth is cor:carter -- the one genuine case -- and the fork had ALREADY FIXED IT: **
    rem:carter-chain sits immediately after, draws all six links, and closes with "so the explanation
    does not rest on the separable ansatz", carrying \\rcpt{V1_carter_chain}.

⇒ ** G1 MEASURES DISTANCE, NOT READABILITY.  The quantity is wrong, not merely the threshold. **  And
the L-220 class had TWO live members, not three: L-209 and U1.  The third was inherited from V1's
DIAGNOSIS without reading the current text for its FIX.

** THE RULE THAT FALLS OUT, and it is this line's own rule broken one revision after writing it
(r2400, on the routing list): "the fork fixes things fast and the worst thing on a list like this is
an item it already did."  CHECK THE FIX, NOT JUST THE DIAGNOSIS -- a receipt that names a defect is
evidence the defect was FOUND, never evidence it is still THERE. **

Written r2417.  Stated for reversal.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PAPERS = ('range_paper.tex', 'slicing_operator.tex')
ENVS = ('theorem', 'corollary', 'proposition', 'lemma')

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  G2 -- the metric, run BLIND over every labelled result in P8 and P9')
    print()
    total, proofless, in_body, repaired = 0, [], [], []
    for paper in PAPERS:
        path = os.path.join(ROOT, 'corpus', paper)
        t = open(path, encoding='utf-8', errors='replace').read()
        pat = r'\\begin\{(' + '|'.join(ENVS) + r')\}(?:\[[^\]]*\])?\\label\{([^}]+)\}'
        for m in re.finditer(pat, t):
            kind, lab = m.group(1), m.group(2)
            total += 1
            end = t.find('\\end{' + kind + '}', m.start())
            nxt = t.find('\\begin{proof}', end)
            adjacent = nxt >= 0 and (nxt - end) < 60
            if adjacent:
                continue
            body = t[m.start():end]
            after = t[end:end + 400]
            justifies = bool(re.search(r'\b(because|since|follows|hence|therefore|computational '
                                       r'facts|the upper bound is)\b', body + after, re.I))
            drawn = 'chain, drawn' in after or 'rem:' in after
            proofless.append(lab)
            if drawn:
                repaired.append(lab)
            elif justifies:
                in_body.append(lab)

    check('sixteen labelled results enumerated with no selection', total == 16)
    print(f'      {total} results · {len(proofless)} without an adjacent proof environment')
    print(f'      of those: {len(in_body)} justify IN-BODY · {len(repaired)} carry a drawn-chain remark')
    for l in in_body:
        print(f'        in-body   {l}')
    for l in repaired:
        print(f'        REPAIRED  {l}  <- the fork already fixed it')

    check('a majority of the proofless results justify in-body, so the metric misreads them',
          len(in_body) >= 4)
    check('the one genuine case carries a drawn-chain remark in the current text',
          'cor:carter' in repaired)

    # and the repair is verifiable by content, not only by position
    t = open(os.path.join(ROOT, 'corpus', 'range_paper.tex'), encoding='utf-8',
             errors='replace').read()
    check('rem:carter-chain draws the Goldberg-Sachs link',
          'Goldberg' in t[t.find('rem:carter-chain'):t.find('rem:carter-chain') + 1400])
    # ** THIS CHECK FAILED ON ITS FIRST RUN, and the cause is worth the comment: the sentence is
    # LINE-WRAPPED in the .tex source -- "does not\nrest on the separable ansatz" -- so a literal
    # substring probe misses it.  ** A check that searches source for a phrase must normalise
    # whitespace, or it reports a defect in the paper that is really a defect in the probe. **
    # Same class as the encoding failure at r2412: the write reported success and the file was
    # unchanged.  Read the bytes; normalise before matching.
    flat = re.sub(r'\s+', ' ', t)
    check('rem:carter-chain closes the ansatz reading explicitly (whitespace-normalised)',
          'does not rest on the separable ansatz' in flat)
    check('and it carries the receipt marker for the diagnosis it answers',
          'V1_carter_chain}' in t)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: run blind, the metric flags six results and is WRONG about five of them --')
    print('  they justify in-body, which needs no proof environment.  ** The quantity is wrong, not')
    print('     merely the threshold: G1 measures DISTANCE, not READABILITY. **')
    print('  And the sixth was already repaired by the fork.  ⇒ The L-220 class has TWO live')
    print('  members, not three, and routing item 13 is withdrawn.')
    print('  ** CHECK THE FIX, NOT JUST THE DIAGNOSIS: a receipt naming a defect is evidence it was')
    print('     FOUND, never evidence it is still THERE. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
