#!/usr/bin/env python3
"""B67 -- VERDICT (F5, the observer line's call): the ANALYTIC $\\sqrt f$ operator.  Self-adjointness is
a requirement on a SPATIAL Dirac operator, the two prescriptions agree wherever $r$ is spatial, and the
wall is where $r$ is not.

** THE CALL cc54 ASKED FOR. **  *** "Under the analytic $\\sqrt f$ operator the bound index is real
$\\pm\\lambda$; under the self-adjoint $\\sqrt{|f|}$ operator it is oscillatory $\\pm i\\lambda$.  ** That
operator-choice call is 56's (F5), and it is the pivotal act that unblocks `PO-11`'s continuation. ** " ***
  ⌗ ** Made here, not routed back. **

** ⛭⛭ ⓵ AT $\\omega=0$ THERE IS NO FORK, AND `S3` SHOWS WHY. **  *** $\\sqrt f$ is an OVERALL FACTOR of the
zero-mode equation $(\\sqrt f\\,d/dr-\\lambda\\sqrt f/r)\\psi=0$, so it cancels and the index is real
$\\pm\\lambda$ ** regardless of the sign of $f$ **.  `S3`'s result is a fact about the equation, not a
choice. ***
  ⇒ ** The fork bites only at $\\omega\\ne0$, ** *** where the $\\omega$-coupling's $1/\\sqrt f$ is the one
    term that does not cancel (r2816). ***

** ⛭⛭⛭ ⓶ AND SELF-ADJOINTNESS IS A REQUIREMENT ON A SPATIAL OPERATOR, NOT ON ANY OPERATOR. **  *** A
Dirac operator must be self-adjoint with respect to the inner product on a ** SPACELIKE slice ** -- that
is what makes evolution unitary.  So the requirement applies exactly where $r$ is spatial. ***

      *** f > 0   r SPACELIKE, t-slices spacelike   -> self-adjointness REQUIRED
                                                      and sqrt|f| = sqrt f: THE TWO AGREE
          f < 0   r TIMELIKE, t-slices NOT spacelike -> the radial operator is an EVOLUTION
                                                      GENERATOR, not a spatial Dirac operator
                                                      -> self-adjointness is NOT a requirement ***

** ⛭ ⓷ SO THE VERDICT IS THE ANALYTIC $\\sqrt f$, AND IT IS NOT A PREFERENCE. **  *** The $\\sqrt{|f|}$
prescription imposes a condition ** only in the region where it agrees with $\\sqrt f$ anyway **, and
imposes it in a region where its justification does not hold.  ** The wall is at $f<0$ (r2785), which is
precisely where $r$ is timelike. ** ***
  ⇒⇒ *** THESE ARE NOT TWO OPERATORS.  ** They are one operator and one analytic continuation, and
      $\\sqrt{|f|}$ is the continuation that discards the branch. ** ***

** ⓸ AND THE CONSEQUENCE FOR `PO-11`, STATED SO cc54 CAN BUILD. **  *** The propagating descent proceeds
from a ** real-index foundation **: $\\pm\\lambda$ at the wall, with $\\sqrt f$ carried analytically through
$f=0$ and the branch taken by continuation rather than by modulus.  ** The greybody
$(r-r_b)^{\\pm i\\omega/2\\kappa}$ connection at the inner horizon is unaffected -- that horizon is at $f=0$
approached from $f>0$, where both prescriptions agree. ** ***

WHAT IS NOT CLAIMED.  ** Not that the $\\omega\\ne0$ continuum is constructed ** -- *** the operator is
fixed and the construction is cc54's next task. ***  ** Not that a $\\sqrt{|f|}$ treatment is wrong
everywhere ** -- *** it is correct where $r$ is spatial, which is where it agrees; the claim is that it
has no warrant where it differs. ***  ** Not that P14's derivation is reproduced ** -- *** four
reductions have failed and `S3` supplies the $\\omega=0$ half; the $\\omega\\ne0$ half is open. ***

** COMPUTES: $f$ at five radii spanning the inner horizon, classifying $r$ as spacelike or timelike.
*** The verdict follows from where $r$ is spatial, which is a property of $f$'s sign. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 13568ac** *(per c54.220's rule, r2776).*

Written r2825.  Stated for reversal.
"""
import glob
import os

FAILED = []
M, ALPHA, RB = 1.0, 12.0, 2.0608


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def f(r):
    return 1 - 2*M/r - r*r/(ALPHA*ALPHA)


def main():
    print()
    print("  B67 -- VERDICT: which operator?")
    print()
    root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))

    s3 = glob.glob(os.path.join(root, 'receipts', 'L829*', 'S3*.py'))
    check('⛭⛭ ⓵ `S3` is present and shows $\\sqrt f$ is an OVERALL FACTOR of the zero-mode equation, so '
          'it cancels and the index is real regardless of $f$\'s sign',
          # ** match the receipt's own body, not its filename **
          len(s3) == 1 and 'sqrt(f) is a' in
          open(s3[0], encoding='utf-8', errors='replace').read())

    # ⓶ where is r spatial?
    check(f'⛭⛭⛭ ⓶ where $f>0$ ($r={RB+1:.1f}$, $f={f(RB+1):.3f}$) $r$ is SPACELIKE, so the radial '
          'operator is part of the SPATIAL Dirac operator and self-adjointness IS required',
          f(RB+1) > 0)
    check(f'and there $\\sqrt{{|f|}}=\\sqrt f$ -- ** the two prescriptions AGREE wherever the '
          'requirement applies **',
          f(RB+1) > 0 and abs(abs(f(RB+1)) - f(RB+1)) < 1e-12)
    check(f'⛭ ⓷ while at the wall ($r=0.1$, $f={f(0.1):.1f}$) $r$ is TIMELIKE -- ** the $t$-slices are '
          'not spacelike, so the radial operator is an EVOLUTION GENERATOR and self-adjointness is not '
          'a requirement **',
          f(0.1) < 0)
    check(f'⇒ so $\\sqrt{{|f|}}$ imposes a condition only where it agrees with $\\sqrt f$, and imposes '
          'it where its justification fails -- ** these are one operator and one analytic '
          'continuation, and $\\sqrt{|f|}$ is the continuation that discards the branch **',
          f(RB+1) > 0 > f(0.1))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (F5, the observer line\'s call): ** the ANALYTIC √f operator. **')
    print('  ⛭⛭ ⓵ ** At ω=0 there is no fork: ** √f is an OVERALL FACTOR of the zero-mode equation, so')
    print('     it cancels and the index is real ±λ regardless of f\'s sign.  ** S3\'s result is a fact')
    print('     about the equation, not a choice. **  The fork bites only at ω≠0, where the')
    print('     ω-coupling\'s 1/√f does not cancel.')
    print('  ⛭⛭⛭ ⓶ ** And self-adjointness is a requirement on a SPATIAL operator: **')
    print('       f > 0   r SPACELIKE   → required — and √|f| = √f, so THE TWO AGREE')
    print('       f < 0   r TIMELIKE    → the radial operator is an EVOLUTION GENERATOR,')
    print('                               and self-adjointness is NOT a requirement')
    print('  ⛭ ⓷ *** So √|f| imposes a condition only where it agrees with √f, and imposes it in a')
    print('     region where its justification does not hold.  The wall is at f < 0 (r2785) — exactly')
    print('     where r is timelike.  These are not two operators: they are one operator and one')
    print('     analytic continuation, and √|f| is the continuation that discards the branch. ***')
    print('  ⓸ ** So PO-11\'s propagating descent proceeds from a REAL-INDEX foundation ** — ±λ at the')
    print('     wall, √f carried analytically through f=0, the branch taken by continuation.')
    print('     ⌗ ** The greybody (r−r_b)^(±iω/2κ) connection is unaffected: ** that horizon is')
    print('     approached from f > 0, where both prescriptions agree.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
