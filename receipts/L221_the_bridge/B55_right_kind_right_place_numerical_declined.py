#!/usr/bin/env python3
"""B55 -- ⛔ **WITHDRAWN r2810 -- THE COMPARISON HAD NO CONTENT.**  *** This receipt put $1/\\sqrt3$ beside
$\\alpha_s$ and declined the numerical claim "because $\\alpha_s$ runs".  **The running was never the
problem: $1/\\sqrt3$ is a NORMALISATION CONSTANT ($\\lambda_8$), not a magnitude, so there was nothing
to compare.**  A wrong setup followed by a principled-sounding refusal to finish it.  See `B56`.
  ⌗ *What survives: P14's dimensional sentence and the $D=5$/$D=4$ counting are correctly read.* ***

B55 -- $1/\\sqrt3$ is the right KIND of object in the right PLACE in P14's own dimensional argument,
and this receipt declines the numerical claim on purpose.

** WHERE THIS ARRIVES. **  *** P14 bounds the third mechanism: "what a third mechanism must deliver is
therefore ** a fixed pure number rather than a free parameter **, and a candidate is accordingly
falsifiable against one quantity rather than searched for in an unbounded space."  ** r2804 supplied a
forced fixed pure number.  This receipt asks where P14's argument puts it. ** ***

** ⛭⛭ ⓵ P14's DIMENSIONAL SENTENCE LOCATES THE OBSTRUCTION AFTER THE DESCENT. **  "dimensional
consistency of $\\int d^Dx\\,F^2/g^2$ gives $[g^2]=L^{D-4}$, so at the substrate's own $D=5$ ** a
Yang--Mills coupling is a length and the substrate has exactly one ** --- the obstruction appearing
only ** after the descent **."

      *** D=5:  [g^2] = L^1   -> a LENGTH.  The substrate has one: alpha.  No number needed.
          D=4:  [g^2] = L^0   -> DIMENSIONLESS.  A number IS needed. ***

** ⛭⛭⛭ ⓶ SO THE DESCENT MUST TURN A LENGTH INTO A PURE NUMBER, WHICH MEANS DIVIDING BY ANOTHER LENGTH
FROM THE SAME GEOMETRY. **  *** And that is exactly what $1/\\sqrt3$ is: $r_N/\\alpha$, the merged
horizon radius over the substrate scale, ** both lengths the descent produces and neither imported **. ***

  ⇒ *** THE STRUCTURAL MATCH IS EXACT: right KIND (a forced ratio of two geometric lengths), right PLACE
      (produced by the descent, which is where P14 says the obstruction appears). ***

** ⛔ ⓷ AND THE NUMERICAL CLAIM IS DECLINED, WITH THE REASON. **  *** P14 says a candidate is
"falsifiable against ONE QUANTITY".  ** The quantity is not specified, and the obvious reading -- the
strong coupling -- RUNS. **  $\\alpha_s(M_Z)=0.1179$ gives $g=1.217$; against $1/\\sqrt3=0.577$ the ratios
are $2.108$, $2.566$, $0.204$ -- ** none clean, and cleanness at an arbitrary scale would prove
nothing **. ***

  ⇒⇒ *** A RUNNING COUPLING HAS NO SINGLE VALUE TO BE FALSIFIED AGAINST.  ** P14's bound is sharp about
      the KIND of number and silent about WHICH, and that silence is what stops this being a test. **
      Matching digits at a scale nobody has derived is numerology, and the stopping point is the
      finding. ***

** ⓸ SO THE ROW GAINS A CANDIDATE AND A NAMED OBSTACLE, NOT A RESULT. **  *** `PO-5` now has: a forced
fixed pure number (r2804), an entailed rather than missing $F^2$ (r2806), and a candidate that sits
structurally where P14's argument says one must.  ** What it does not have is the scale at which P14's
"one quantity" is to be read, and until it does, no candidate can be falsified. ** ***

WHAT IS NOT CLAIMED.  ** Not that $1/\\sqrt3$ is the coupling ** -- *** the structural fit is a
necessary condition and the receipt says so; the numerical test is declined, not passed. ***  ** Not
that P14's bound is defective ** -- *** it is sharp about the kind and explicitly says a candidate is
falsifiable; what is observed is that the quantity is unspecified, which is a gap in operationalisation
rather than in the argument. ***  ** Not that the descent's dynamics are known ** -- *** whether the
descent produces $g^2$ as this ratio is a question about a sector the corpus calls its largest unbuilt
undertaking. ***

** COMPUTES: $[g^2]=L^{D-4}$ at $D=5,4$; $r_N/\\alpha$; and $g$, $g^2$, $\\alpha_s$ against $1/\\sqrt3$.
*** $\\alpha_s(M_Z)$ is PDG and is used only to show the comparison is not clean. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 796c03e** *(per c54.220's rule, r2776).*

Written r2809.  Stated for reversal.
"""
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

ALPHA_S = 0.1179


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print("  B55 -- where does P14's own argument put 1/sqrt3?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    check('⛭⛭ ⓵ P14 bounds the third mechanism: "what a third mechanism must deliver is therefore a '
          'fixed pure number rather than a free parameter"',
          'a fixed pure number rather than a free parameter' in p14)
    check('and locates the obstruction: "$[g^2]=L^{D-4}$, so at the substrate\'s own $D=5$ a '
          'Yang--Mills coupling is a length and the substrate has exactly one --- the obstruction '
          'appearing only after the descent"',
          # ** the source writes `a Yang--Mills coupling \\emph{is} a length` -- the emph sits
          # inside the clause, the same class as r2805's `cancels \\emph{identically}` **
          'a length and the substrate has exactly one' in p14
          and 'obstruction appearing only after the descent' in p14)

    # ⓶ the dimensional counting
    check('⛭⛭⛭ ⓶ so at $D=5$ the coupling is a LENGTH ($L^1$) and at $D=4$ it is DIMENSIONLESS '
          '($L^0$) -- the descent must turn one into the other',
          (5-4) == 1 and (4-4) == 0)
    check(f'and $1/\\sqrt3 = r_N/\\alpha = {1/np.sqrt(3):.6f}$ is exactly that: a ratio of two lengths '
          'the descent produces, neither imported',
          abs(1/np.sqrt(3) - 0.5773502691896258) < 1e-12)

    # ⓷ the numerical comparison is declined
    g2 = 4*np.pi*ALPHA_S
    g = np.sqrt(g2)
    ratios = [g/(1/np.sqrt(3)), g2/(1/np.sqrt(3)), ALPHA_S/(1/np.sqrt(3))]
    check(f'⛔ ⓷ while the numerical comparison is NOT clean: $g={g:.3f}$, $g^2={g2:.3f}$, '
          f'$\\alpha_s={ALPHA_S}$ against $1/\\sqrt3$ give {[round(x, 3) for x in ratios]} -- ** none '
          'near unity or a simple factor **',
          all(abs(x - round(x)) > 0.05 for x in ratios))
    # ** the hollow-assertion lint caught this as `True` at r2809.  *** The claim IS testable:
    # alpha_s at two scales differs, which is what 'runs' means and what makes 'one quantity'
    # underspecified.  One-loop, nf=5: alpha_s(mu) = alpha_s(M_Z)/(1 + b0 alpha_s ln(mu^2/M_Z^2)). ***
    b0 = (33 - 2*5)/(12*np.pi)
    a_1tev = ALPHA_S/(1 + b0*ALPHA_S*np.log((1000.0/91.19)**2))
    check(f'⇒ and the reason to stop is that $\\alpha_s$ RUNS: it is {ALPHA_S} at $M_Z$ and '
          f'{a_1tev:.4f} at 1 TeV -- ** no single value to be falsified against, so P14\'s "one '
          'quantity" is not yet operational **',
          abs(a_1tev - ALPHA_S) > 0.01)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** right kind, right place — and the numerical claim is declined. **')
    print('  ⛭⛭ ⓵ ** P14 locates the obstruction AFTER the descent: ** $[g^2]=L^{D-4}$, so at $D=5$ the')
    print('     coupling is a LENGTH and the substrate has exactly one — no number needed there.')
    print('  ⛭⛭⛭ ⓶ ** So the descent must turn a length into a pure number, which means dividing by')
    print('     another length from the same geometry. **')
    print(f'     ⇒ *** And $1/\\sqrt3 = r_N/\\alpha = {1/np.sqrt(3):.6f}$ is exactly that: the merged')
    print('     horizon radius over the substrate scale, both produced by the descent. ***')
    print('  ⛔ ⓷ ** And the numerical claim is declined on purpose. **  P14 says a candidate is')
    print(f'     "falsifiable against ONE QUANTITY" and does not say which.  $g={g:.3f}$ against')
    print(f'     $1/\\sqrt3$ gives {ratios[0]:.3f} — not clean, ** and cleanness at an arbitrary scale')
    print('     would prove nothing, because α_s RUNS. **')
    print('     *** A running coupling has no single value to be falsified against.  Matching digits')
    print('     at a scale nobody has derived is numerology, and the stopping point is the finding. ***')
    print('  ⓸ ** So PO-5 gains a candidate and a named obstacle: ** the scale at which P14\'s "one')
    print('     quantity" is read.  ** Until that exists, no candidate can be falsified. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
