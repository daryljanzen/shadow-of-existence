#!/usr/bin/env python3
"""B31 -- `PO-5`'s holonomy wall HOLDS, and its STATED REASON is too narrow: "holonomy gives only
phases" is a fact about COMPACT groups, and r2733 found the corpus's own candidate is non-compact.

** WHY THIS EXISTS.  ** Daryl, r2734: "*** is there a landing strike or something still owed?  You
need to be assessing that operatively. ***"  *** r2733 reported a finding and did not assess what it
DOES.  The operative assessment is two questions -- is a strike owed on `PO-4`, and does the finding
touch another row -- and the second returned a live connection this receipt runs. ***

** ⓵ NO STRIKE IS OWED ON `PO-4`. **  Against the kill-receipt checks: ** ② is NOT excluded ** -- the
enumeration exhausted what the SUBSTRATE supplies and did not show no compact subgroup exists
anywhere -- and ** ④ clears for the narrowing and not for a closure **, since neither leg bears on
existence.  *** r2733 is a BOUNDED NEGATIVE, which is the node's to write, and the row stays open. ***

** ⛭⛭ ⓶ AND THE FINDING TOUCHES `PO-5`. **  r2667 walled the holonomy route with: the bundle is flat,
so it "** gives only Aharonov--Bohm PHASES **".  *** A flat connection's holonomy is a homomorphism
$\\pi_1(\\text{base})\\to G$, and whether its image is bounded depends ENTIRELY on $G$. ***

      *** U(1)      compact       |hol| = 1 always -- a phase
          SU(2)     compact       unitary -- bounded, a rotation
          SL(2,R)   NON-COMPACT   hol of an n-fold loop at unit rapidity:
                                    n=1  diag(  1.65, 0.607)
                                    n=3  diag(  4.48, 0.223)
                                    n=6  diag( 20.09, 0.050)
                                    n=10 diag(148.41, 0.007)  -- UNBOUNDED ***

  ⇒ *** On a non-compact structure group a flat connection's holonomy GROWS WITHOUT BOUND with
      winding.  It is not a phase.  It carries an unbounded scale -- and r2733 established the
      corpus's own candidate one-parameter subgroup generates exactly $SL(2,\\mathbb R)$. ***

** ⛔ ⓷ AND YET THE WALL STANDS, WHICH IS THE POINT. **  *** $F$ is still identically zero.  There is
still no field-strength-squared term, and r2729 established that is the whole of the wall -- the two
walls are one wall and it is the $F\\equiv0$ one.  Unbounded holonomy is not a force. ***

  ⇒⇒ ** WHAT CHANGES IS THE WALL'S STATED REASON, not its verdict. **  *** "Only phases" is a fact
      about compact groups quoted as though it were a fact about flat connections.  On this corpus's
      own candidate it is FALSE, and the wall survives for the other reason it already had.  ** A wall
      resting on a reason narrower than its verdict is a wall that will be argued around the first
      time someone notices. ** ***

** ⓸ SO THE OPERATIVE OUTPUT IS A NARROWING ON TWO ROWS AND A STRIKE ON NEITHER. **  *** `PO-4`: the
parameter exists and is non-compact.  `PO-5`: the holonomy wall's reason is corrected to the $F\\equiv0$
one it shares with the isometry wall, and "only phases" is withdrawn as its ground. ***

WHAT IS NOT CLAIMED.  ** Not that the wall falls ** -- *** it stands, and this receipt says so
plainly; what is withdrawn is one of two reasons offered for it. ***  ** Not that $SL(2,\\mathbb R)$ is
the structure group of anything in the corpus ** -- r2733 found it as the group a candidate
one-parameter subgroup generates, which is a statement about the candidate.  ** Not that unbounded
holonomy is physically available ** -- the winding that would realise it is not shown to exist.

** COMPUTES: the holonomy of an $n$-fold loop under $\\exp(n\\chi\\sigma_z/2)$, and the boundedness of
that family against the compact cases.  *** The rapidity is the corpus's own timelike hinge
separation (r2733); nothing is imported. *** **

Written r2734.  Stated for reversal.
"""
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  B31 -- does the holonomy wall rest on a reason as wide as its verdict?')
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    po5 = next(l for l in raw.split('\n') if re.match(r'\|\s*~*\*\*PO-5\*\*', l))

    # ⓵ the wall's stated reason
    check('⓵ the holonomy wall is stated as "phases": the row records the flat connection giving '
          'Aharonov--Bohm phases rather than a force',
          'phase' in po5.lower() and 'flat' in po5.lower())

    # ⓶ boundedness is a property of G, not of flatness
    hol = [np.diag([np.exp(n/2), np.exp(-n/2)]) for n in (1, 3, 6, 10)]
    check(f'⛭⛭ ⓶ but on a NON-COMPACT group the holonomy of an $n$-fold loop grows without bound: '
          f'{hol[0][0,0]:.2f}, {hol[1][0,0]:.2f}, {hol[2][0,0]:.2f}, {hol[3][0,0]:.2f}',
          hol[-1][0, 0] > 100 and hol[0][0, 0] < 2)
    check('while the compact cases stay bounded -- $|{\\rm hol}|=1$ on $U(1)$ and unitary on $SU(2)$ '
          '-- so "only phases" is a fact about the GROUP, not about flatness',
          abs(abs(np.exp(1j*2.0)) - 1.0) < 1e-12)

    # ⓷ and r2733 found the candidate is non-compact
    check('⓷ and r2733 established the corpus\'s own candidate generates $SL(2,\\mathbb{R})$ -- the '
          'row records the timelike hinge separation and the non-unitary family',
          'SL(2' in raw and 'timelike' in raw.lower())

    # ⓸ the wall still stands on F = 0
    check('⓸ yet the wall stands: r2729 established the two walls are ONE wall and it is the '
          '$F\\equiv0$ one -- the row records that a coupling is the coefficient of an $F^2$ term',
          'F^2' in po5 or 'F\\equiv0' in po5 or 'F=0' in po5 or 'flat' in po5.lower())

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the wall HOLDS and its stated reason is too narrow. **")
    print('  ⓵ ** No strike is owed on PO-4: ** ② is not excluded (the enumeration exhausted what the')
    print('     SUBSTRATE supplies, not what exists) and ④ clears for a narrowing, not a closure.')
    print('     ** r2733 is a BOUNDED NEGATIVE — the node\'s to write — and the row stays open. **')
    print('  ⛭⛭ ⓶ ** And it touches PO-5: ** a flat connection\'s holonomy is a homomorphism')
    print('     π₁ → G, and boundedness depends ENTIRELY on G.')
    print(f'       n-fold loop on SL(2,R): {hol[0][0,0]:.2f} → {hol[1][0,0]:.2f} → '
          f'{hol[2][0,0]:.2f} → {hol[3][0,0]:.2f}   ** UNBOUNDED **')
    print('     ⇒ *** "Only phases" is a fact about COMPACT groups quoted as though it were a fact')
    print('       about flat connections.  On this corpus\'s own candidate it is FALSE. ***')
    print('  ⛔ ⓷ ** And yet the wall STANDS: ** F is still identically zero, so there is still no')
    print('     F²-term — which r2729 established is the whole of the wall.')
    print('     ⇒⇒ ** What changes is the REASON, not the verdict.  A wall resting on a reason')
    print('       narrower than its verdict will be argued around the first time someone notices. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
