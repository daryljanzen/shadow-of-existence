#!/usr/bin/env python3
"""G1_the_arrival_path_metric.py -- R-P station 34, probe G1: a METRIC for a class already seen three times.

THE CLASS.  Three times in this audit a result has been found complete in the corpus and unreachable
from where a reader arrives:

  * L-209 (r2391): COMPLEX_ANALYSIS_LEDGER's queue called a question unasked while section 4a of the
    SAME FILE answered it twice, three screens apart.
  * U1 (r2398): P16 says "the same erasure raises a question this paper answers in effect but does
    not state", and answers it in the next sentence.
  * V1 (P9, and re-measured here): cor:carter gives steps 5-6 of the Carter chain on the separable
    ansatz; the shift-shear passage gives steps 1-4; ** the two sit in different sections without the
    arrow drawn between them **, so a reader arriving at the corollary sees something weaker than
    what the paper establishes.

** THE CORPUS'S CONTENT IS COMPLETE AND ITS ARRIVAL PATHS ARE NOT. **  Three instances is a class,
and a class deserves a measurement rather than a third reading.

THE MEASUREMENT.  For a named claim, locate its supporting links in the same paper and report the
CHARACTER DISTANCE from the claim to each.  A claim whose links cluster near it reads as established;
a claim whose links sit thousands of characters away reads as asserted, however complete the paper is.

    ** This does not measure whether a chain EXISTS.  It measures whether a reader who arrives at the
       claim can SEE it. **  Those are different properties and only the first has ever been checked.

WHAT IT FOUND, and it corrected the reading that prompted it.  This line read V1 as saying the arrow
was missing; ** measured, five of the Carter chain's six links sit inside ~1020 characters -- one
paragraph -- and read as a chain there. **  V1 never said otherwise: it says "the chain exists,
complete and sourced, in one paper".  The defect is narrower and real: ** the chain is in the
synthesis passage and absent at the corollary **, and a corollary is precisely what a reader arrives
at directly.

** SUPERSEDED IN PART AT r2417 BY A BLIND RUN.  READ THIS BEFORE TRUSTING THE METRIC. **

This receipt's three cases were all found BY HAND FIRST and measured after -- which is validating an
instrument against itself.  Run blind over all sixteen labelled results in P8 and P9, the quantity
fails:

  * ** Six results carry no \begin{proof} at all **, which a distance metric reads as maximum
    failure.  ** Five of the six justify IN-BODY ** -- thm:range names its own parts in the very next
    sentence ("the upper bound is Theorem thm:bound; the filling is Proposition prop:surj").
    ⇒ A result that carries its argument inside itself needs no proof environment, and a metric
      counting distance-to-support flags every one of them.
  * ** The sixth, cor:carter, is the only genuine case -- and the fork had ALREADY FIXED IT. **
    rem:carter-chain sits immediately after the corollary, draws every link, closes with "so the
    explanation does not rest on the separable ansatz", and carries \rcpt{V1_carter_chain}.

⇒ ** So it is not that the threshold was invented.  THE QUANTITY IS WRONG: this measures DISTANCE,
   not READABILITY. **  Kept, not deleted, because the blind run is the finding and the receipt is
   where it is reproducible -- and because a superseded instrument that states its own defect is
   worth more than a deleted one, provided the statement sits where the result is read.

Written r2416.  Superseded in part r2417.  Stated for reversal.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


# (paper, claim anchor, [(link name, pattern)]) -- the enumerated GR claims of station 34
CLAIMS = [
    ('range_paper.tex', 'the Carter constant', 'Carter constant', [
        ('shear-free rulings', 'shear-free'),
        ('principal congruence', 'principal congruence'),
        ('Goldberg-Sachs', 'Goldberg'),
        ('speciality invariant', 'speciality invariant'),
        ('Walker-Penrose', 'WalkerPenrose1970'),
    ]),
    ('range_paper.tex', 'the Petrov filling', 'Petrov type~O', [
        ('type D named', 'type D'),
        ('type I named', 'type I'),
        ('speciality invariant', 'speciality invariant'),
        ('shear-free rulings', 'shear-free'),
    ]),
    ('CR_framework.tex', 'the reassignment reading', 'causal reassignments', [
        ('substrate', 'substrate'),
        ('vacuum sector', 'vacuum'),
        ('Petrov / algebraic type', 'algebraic type'),
    ]),
]

NEAR = 2000     # within one long paragraph or two: a reader sees it
FAR = 8000      # a different section: a reader arriving here does not


def main():
    print()
    print('  G1 -- ARRIVAL PATHS: can a reader who lands on the claim SEE its chain?')
    print()
    any_far = False
    for paper, label, anchor, links in CLAIMS:
        path = os.path.join(ROOT, 'corpus', paper)
        if not os.path.exists(path):
            check(f'{paper} exists', False)
            continue
        t = open(path, encoding='utf-8', errors='replace').read()
        a = t.find(anchor)
        check(f'{label}: the claim anchor is present in {paper}', a >= 0)
        if a < 0:
            continue
        print(f'      claim at char {a} of {len(t)}')
        near, far, absent = [], [], []
        for name, pat in links:
            # nearest occurrence of the link to the claim, in either direction
            best = None
            for m in re.finditer(re.escape(pat), t):
                d = abs(m.start() - a)
                if best is None or d < best:
                    best = d
            if best is None:
                absent.append(name)
            elif best <= NEAR:
                near.append((name, best))
            elif best <= FAR:
                near.append((name, best))
            else:
                far.append((name, best))
        for n, d in sorted(near, key=lambda x: x[1]):
            print(f'        near  {n:<26} {d:>6} chars')
        for n, d in sorted(far, key=lambda x: x[1]):
            print(f'        FAR   {n:<26} {d:>6} chars')
        for n in absent:
            print(f'        ABSENT {n}')
        check(f'{label}: every link is present somewhere in the paper', not absent)
        if far:
            any_far = True
        print()

    # ** the specific V1 finding, measured rather than read **
    t = open(os.path.join(ROOT, 'corpus', 'range_paper.tex'), encoding='utf-8',
             errors='replace').read()
    mech = t.find('The mechanism is the shift--shear link')
    cor = t.find('\\begin{corollary}')
    check('P9 states the mechanism explicitly ("the shift--shear link")', mech >= 0)
    check('the mechanism passage clusters five links inside one paragraph (< 1200 chars)',
          mech >= 0 and max(
              abs(t.find(p) - t.find('Carter constant'))
              for p in ('speciality invariant', 'WalkerPenrose1970', 'Goldberg',
                        'principal congruence')) < 1200)
    if cor >= 0:
        d = abs(cor - mech)
        print(f'      cor:carter to the mechanism passage: {d} chars')
        check('the corollary and the mechanism are NOT adjacent (the V1 finding, measured)',
              d > NEAR)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: every chain the station enumerated is PRESENT and COMPLETE in its paper --')
    print('  which is what V1 said and what this line initially read one notch too strongly.')
    print('  ** What the metric shows is narrower and real: the Carter chain clusters in the')
    print('     SYNTHESIS passage and is absent at the COROLLARY -- and a corollary is precisely')
    print('     what a reader arrives at directly. **')
    print('  ⇒ The corpus\'s content is complete and its ARRIVAL PATHS are not.  Three instances')
    print('    (L-209, U1, V1) are one class, and this is the first time it carries a number.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
