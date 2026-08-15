#!/usr/bin/env python3
"""D1 -- the degeneracy that carries `PO-6`'s quartic divergence was ASSERTED in P10, ASSERTED and
explicitly UNCHECKED in `D2`, and derived nowhere.  Derived here: $g(n)=2(n-1)(n+3)$, $n\\ge2$ --
and the constant in front of $n^{2}$ is the PROPAGATING-COMPONENT COUNT, which makes `D2`'s "any
tensor rank" false.

** WHAT RESTS ON IT. **  P10 measures the tower's ultraviolet degree from three inputs:
*** "with $\\mu_n\\sim n$, $\\langle\\hat\\pi_n^2\\rangle\\sim n$ in the instantaneous ground state, and
a degeneracy growing as $n^{2}$, the shell contribution goes as $n^{3}$ and the sum diverges
quartically". ***  ⇒ ** Two of the three are computed in `D2`.  The third is not: **
*`D2` carries it as a bare line -- "Degeneracy of $S^3$ harmonics at level $n$ grows like $n^{2}$
(any tensor rank)" -- with no check, and the closed form appears NOWHERE in the corpus.*

** ⛭⛭ ⓵ DERIVED, AND THE ROUTE NEEDS NO SPECIAL FUNCTIONS.  **  $S^{3}=SU(2)$ is PARALLELIZABLE, so a
frame-indexed field of frame-spin $s$ is $L^{2}(SU(2))\\otimes V_{s}$.  Peter--Weyl gives
$L^{2}(SU(2))=\\bigoplus_j V_j^{(L)}\\otimes V_j^{(R)}$, and tensoring the $R$-factor with $V_s$:

      *** level-j totals:  scalar 1 x (2j+1)^2 ,  vector 3 x (2j+1)^2 ,  sym-tracefree 5 x (2j+1)^2 ***

  ⌗ ** and those three multiplicities ARE the component counts 1, 3, 5 ** -- a check the decomposition
    had to pass and did.

** ⓶ THE TRANSVERSE-TRACELESS PART IS THE TWO EXTREME SUMMANDS. **  The divergence $\\nabla^i h_{ij}$
shifts the $R$-spin by at most one, so $V_{j+2}$ and $V_{j-2}$ cannot be reached from a vector and
are exactly the TT content:

      *** TT at level j = (2j+1)[(2j+5) + (2j-3)] = 2(2j+1)^2,  which is EXACTLY 2/5 of the
          sym-tracefree total -- the propagating-component fraction. ***

** ⛭ ⓷ ORGANISED BY EIGENVALUE, WHICH IS WHAT THE SUM NEEDS. **  The two helicities at one eigenvalue
are the mirror pair $(m,m+2)$ and $(m+2,m)$, each of dimension $(2m+1)(2m+5)$.  With $n=2m+2$, so
that $m=0,\\tfrac12,1,\\ldots$ gives $n=2,3,4,\\ldots$:

      *** g(n) = 2 (n-1)(n+3),   n >= 2,   with g(2) = 10 ***

  ⇒ ** The floor is $n\\ge2$, which P10 asserts independently ** ("there are no modes below $n=2$ on
    $S^{3}$") -- *the derivation returns the paper's own floor rather than being fitted to it.*

** ⓸ SO THE QUARTIC STANDS, AND ITS LEADING CONSTANT IS NO LONGER ASSERTED. **
$\\sum_{n=2}^{N}g(n)=N(N-1)(2N+11)/3$, leading $\\tfrac23N^{3}$.  ** Independently required by Weyl's
law ** with $d=2$ propagating components -- and the Weyl normalisation is calibrated here on the
SCALAR case, whose degeneracy $(k+1)^{2}$ follows exactly from Peter--Weyl: the ratio of the true
count to $d\\lambda^{3/2}/3$ runs $1.0150\\to1.0030\\to1.00075\\to1.00038$.
  ⇒ *** The shell contribution is $2n^{3}$ and not merely "$n^{3}$ up to a constant". ***

** ⛔ ⓹ AND `D2`'s "ANY TENSOR RANK" IS FALSE. **  The constant in front of $n^{2}$ is the number of
PROPAGATING components, not a universal: *** the scalar tower's Weyl leading coefficient is $1/3$ and
the TT tower's is $2/3$ ***, so a scalar degeneracy grows as $n^{2}$ and a TT one as $2n^{2}$.
  ⌗ *The scaling `D2` needed is right and the parenthetical is not, which is why this changes the
    coefficient and not the degree.*

** ⚠ AND ONE METHOD THAT FAILED, REPORTED BECAUSE IT WAS TRIED. **  I attempted to pin the CLOSED FORM
by matching Weyl's law to SUBLEADING order -- $2(n^{2}-1)$ gives $N^{2}$, $2(n-1)(n+3)$ gives $3N^{2}$,
and $\\tfrac23\\lambda^{3/2}$ expands to $2N^{2}$, so none matches.  *** That discrimination is invalid:
on a CLOSED CURVED manifold the subleading counting term is not the next term of
$\\tfrac23\\lambda^{3/2}$ -- it carries the curvature through the heat kernel. ***  ⇒ ** Weyl's law
fixes the LEADING coefficient and nothing beyond it; the representation theory is what fixes the
closed form. **  *Recorded so nobody re-runs the discriminator expecting it to work.*

WHAT IS NOT CLAIMED.  ** Not that the eigenvalue assignment is re-derived ** -- $\\mu_n^2=n(n+2)-2$ is
P10's and is taken as given; what is derived is the DEGENERACY attached to it, its floor, and its
leading constant.  ** Not a heat-kernel coefficient ** -- still none computed anywhere.  ** Not the
interacting tower ** -- this is the free spectrum's mode count.  ** And not a closure ** -- `PO-6`
stays open; this replaces an unchecked input with a derived one.

Written c54.220, `L-554`.  Stated for reversal.
"""
import os
import re
import subprocess

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

J = sp.Symbol('j', nonnegative=True)
M = sp.Symbol('m', nonnegative=True)
N_ = sp.Symbol('n', positive=True)
NN = sp.Symbol('N', positive=True, integer=True)


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def field_total(s):
    """Level-j dimension of a frame-valued field of frame-spin s on S^3 = SU(2)."""
    return sp.expand((2*J + 1)*sum(2*(J + q) + 1 for q in range(-s, s + 1)))


def main():
    print()
    print('  D1 -- the degeneracy that carries the quartic: asserted, or derived?')
    print()

    p10 = flat(os.path.join(ROOT, 'corpus', 'canonical_time.tex'))
    d2 = flat(os.path.join(ROOT, 'receipts', 'L165_interacting_tower',
                           'D2_the_UV_degree_is_quartic_and_the_IR_is_free.py'))

    # ------------------------------------------------------- (0) what rests on it
    check('⓪ P10 measures the UV degree from three inputs, the third being "a degeneracy growing as '
          '$n^2$, the shell contribution goes as $n^3$ and the sum \\emph{diverges quartically}"',
          'a degeneracy growing as $n^2$, the shell contribution goes as $n^3$ and the sum '
          '\\emph{diverges quartically}' in p10)
    # ⛔ ALSO PINNED.  This revision amends D2 with a correction note, so the quote is asked of the
    #   commit at which the assertion stood unqualified -- not of the live file this turn edits.
    d2_before = re.sub(r'\s+', ' ', subprocess.run(
        ['git', '-C', ROOT, 'show', 'a0c1121:receipts/L165_interacting_tower/'
         'D2_the_UV_degree_is_quartic_and_the_IR_is_free.py'],
        capture_output=True, text=True).stdout)
    check('   and D2 carried that third input as a BARE ASSERTION at a0c1121: "Degeneracy of $S^3$ '
          'harmonics at level $n$ grows like ** $n^2$ ** (any tensor rank)" -- with no check anywhere '
          'in the file, and none of "logarithm", "subleading", "counterterm" present either',
          'Degeneracy of $S^3$ harmonics at level $n$ grows like ** $n^2$ ** (any tensor rank)'
          in d2_before
          and not any(w in d2_before.lower() for w in ('logarithm', 'subleading', 'counterterm')))
    check('   and D2 now carries the correction, so the assertion does not outlive this revision: '
          '"CORRECTED c54.220 (`L-554`)"',
          'CORRECTED c54.220 (`L-554`)' in d2)
    # ⛔ PINNED TO A SHA, NOT TO THE LIVE FILE.  The first draft asserted the closed form "appears
    #   nowhere in P10" against the working tree -- which THIS revision falsifies by banking it
    #   there.  *** Items 28/30/32's class a fifth time, and the first where the check's own subject
    #   was changed by the same turn.  The absence is a claim about the corpus BEFORE c54.220, so it
    #   is asked of the commit that was current when it was made. ***
    BEFORE = 'a0c1121'          # c54.219's tip
    p10_before = re.sub(r'\s+', ' ', subprocess.run(
        ['git', '-C', ROOT, 'show', BEFORE + ':corpus/canonical_time.tex'],
        capture_output=True, text=True).stdout)
    check(f'   and the closed form appeared NOWHERE in P10 at {BEFORE} (c54.219\'s tip): no '
          '"2(n-1)(n+3)", no "2(n^{2}-1)", no "(2m+1)(2m+5)"',
          len(p10_before) > 1000 and '2(n-1)(n+3)' not in p10_before
          and '2(n^{2}-1)' not in p10_before and '(2m+1)(2m+5)' not in p10_before)

    # ------------------------------------------------------- (1) Peter-Weyl, with the component check
    print()
    mult = {}
    for s, ncomp, name in ((0, 1, 'scalar'), (1, 3, 'vector'), (2, 5, 'sym-tracefree')):
        tot = field_total(s)
        mult[s] = sp.simplify(tot/(2*J + 1)**2)
        check(f'⓵ Peter-Weyl on the parallelizable S^3: {name} fields have level-j total '
              f'{sp.factor(tot)} = {mult[s]} x (2j+1)^2 -- and {mult[s]} IS the component count '
              f'{ncomp}',
              sp.simplify(mult[s] - ncomp) == 0)

    # ------------------------------------------------------- (2) TT = the extreme summands
    print()
    TT_j = sp.expand((2*J + 1)*((2*(J + 2) + 1) + (2*(J - 2) + 1)))
    frac = sp.simplify(TT_j/field_total(2))
    check(f'⓶ the TT part is the two EXTREME summands (the divergence shifts the R-spin by at most '
          f'one): TT at level j = {sp.factor(TT_j)}',
          sp.simplify(TT_j - 2*(2*J + 1)**2) == 0)
    check(f'   and that is exactly {frac} of the sym-tracefree total -- the propagating-component '
          'fraction, which is the check the identification had to pass',
          frac == sp.Rational(2, 5))

    # ------------------------------------------------------- (3) by eigenvalue
    print()
    g_pair = sp.expand(2*(2*M + 1)*(2*M + 5))
    g_n = sp.factor(sp.expand(g_pair.subs(M, (N_ - 2)/2)))
    check(f'⓷ organised by eigenvalue, the two helicities are the mirror pair (m,m+2) and (m+2,m), '
          f'each of dimension (2m+1)(2m+5); with n = 2m+2 this is g(n) = {g_n}',
          sp.simplify(g_n - 2*(N_ - 1)*(N_ + 3)) == 0)
    check(f'   with g(2) = {g_n.subs(N_, 2)} at the floor, and the floor n >= 2 is P10\'s own, '
          'asserted independently: "there are no modes below $n=2$ on $S^{3}$"',
          g_n.subs(N_, 2) == 10 and 'there are no modes below $n=2$ on $S^{3}$' in p10)

    # ------------------------------------------------------- (4) the quartic, with its constant
    print()
    S = sp.simplify(sp.summation(sp.expand(g_n), (N_, 2, NN)))
    lead = sp.limit(sp.expand(S)/NN**3, NN, sp.oo)
    check(f'⓸ cumulative sum_2^N g(n) = {sp.factor(S)}, leading coefficient {lead} of N^3',
          lead == sp.Rational(2, 3))

    # Weyl's law, calibrated on the exactly-derivable scalar case
    k = np.arange(0, 4001)
    Ns = np.cumsum((k + 1.0)**2)
    lam_s = k*(k + 2.0)
    ratios = [Ns[i]/(1*lam_s[i]**1.5/3) for i in (100, 500, 2000, 4000)]
    check(f'   and the Weyl normalisation N(lam) = d lam^(3/2)/3 is CALIBRATED on the scalar tower, '
          f'whose degeneracy (k+1)^2 follows exactly from Peter-Weyl: ratio runs '
          f'{", ".join(f"{r:.5f}" for r in ratios)}',
          all(r > 1 for r in ratios) and ratios[-1] < 1.001 and ratios[0] > ratios[-1])
    check('   ⇒ so Weyl with d = 2 propagating components INDEPENDENTLY requires leading 2/3, which '
          'the derived g(n) gives -- the shell contribution is 2n^3, not "n^3 up to a constant"',
          lead == sp.Rational(2, 3))

    # ------------------------------------------------------- (5) "any tensor rank" is false
    print()
    S_scalar = sp.simplify(sp.summation((N_ + 1)**2, (N_, 0, NN)))
    lead_scalar = sp.limit(sp.expand(S_scalar)/NN**3, NN, sp.oo)
    check(f'⛔ ⓹ AND D2\'s "any tensor rank" IS FALSE: the scalar tower\'s leading coefficient is '
          f'{lead_scalar} against the TT tower\'s {lead} -- the constant is the PROPAGATING-COMPONENT '
          'count, so a scalar degeneracy grows as n^2 and a TT one as 2n^2',
          lead_scalar == sp.Rational(1, 3) and lead == sp.Rational(2, 3)
          and lead_scalar != lead)
    check('   ⌗ the SCALING D2 needed is right and the parenthetical is not -- so this changes the '
          'coefficient and not the degree, and the quartic stands',
          lead > 0)

    # ------------------------------------------------------- (6) the method that failed
    print()
    weyl_sub = sp.expand(sp.series(sp.Rational(2, 3)*(NN**2 + 2*NN - 2)**sp.Rational(3, 2),
                                   NN, sp.oo, 3).removeO())
    c_weyl = sp.limit((weyl_sub - sp.Rational(2, 3)*NN**3)/NN**2, NN, sp.oo)
    subs_of = {}
    for lbl, cand in (('2(n^2-1)', 2*(N_**2 - 1)), ('2(n-1)(n+3)', 2*(N_ - 1)*(N_ + 3))):
        Sc = sp.expand(sp.summation(cand, (N_, 2, NN)))
        subs_of[lbl] = sp.limit((Sc - sp.Rational(2, 3)*NN**3)/NN**2, NN, sp.oo)
    check(f'⚠ AND A METHOD THAT FAILED, reported because it was tried: matching Weyl to SUBLEADING '
          f'order gives {subs_of} against the naive expansion\'s {c_weyl} -- NEITHER candidate '
          'matches, so the discriminator is invalid',
          c_weyl == 2 and subs_of['2(n^2-1)'] == 1 and subs_of['2(n-1)(n+3)'] == 3)
    check('   ⇒ on a CLOSED CURVED manifold the subleading counting term is not the next term of '
          '(2/3)lam^(3/2) -- it carries the curvature through the heat kernel. Weyl fixes the '
          'LEADING coefficient and nothing beyond; the representation theory fixes the closed form',
          c_weyl != subs_of['2(n-1)(n+3)'])

    # ------------------------------------------------------- (7) banked
    print()
    check('⛭ and the derived degeneracy is BANKED in P10: "the degeneracy is $2(n-1)(n+3)$"',
          'the degeneracy is $2(n-1)(n+3)$' in p10)
    check('   ⚠ with the constant named for what it is: "the constant is the propagating-component '
          'count rather than a universal"',
          'the constant is the propagating-component count rather than a universal' in p10)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the degeneracy carrying the quartic was never derived; derived here it is')
    print('  2(n-1)(n+3), and its constant is the propagating-component count. **')
    print('  ⓵ ** Peter-Weyl on the parallelizable S^3 ** returns level-j totals 1, 3, 5 times')
    print('     (2j+1)^2 for frame-spin 0, 1, 2 — *** and those multiplicities ARE the component')
    print('     counts, which is the check the decomposition had to pass. ***')
    print('  ⓶ ** TT is the two extreme summands, ** 2(2j+1)^2 — *** exactly 2/5 of the')
    print('     sym-tracefree total, the propagating fraction. ***')
    print('  ⓷ ** By eigenvalue: g(n) = 2(n-1)(n+3), n >= 2, g(2) = 10 ** — and the floor is P10\'s')
    print('     own, asserted independently, so the derivation returns it rather than fitting it.')
    print('  ⓸ ** The quartic stands and its constant is now fixed: ** the shell contribution is')
    print('     2n^3, with Weyl\'s law calibrated on the exactly-derivable scalar tower agreeing.')
    print('  ⛔ ⓹ ** And D2\'s "any tensor rank" is false ** — scalar 1/3 against TT 2/3.  The')
    print('     constant is the component count, so this moves the coefficient and not the degree.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
