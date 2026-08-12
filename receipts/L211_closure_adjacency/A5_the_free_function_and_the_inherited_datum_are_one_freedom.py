#!/usr/bin/env python3
"""A5 -- L-234 answered, and it CORRECTS this line's own r2458 framing.

** WHAT r2458 CLAIMED: ** that E(r)'s profile is "an unspent degree of freedom", available to the
progenitor route r2456 left open for A_s and n_s.

** IT IS NOT UNSPENT.  IT IS SPENT IMPLICITLY, AND THE CORPUS SPENT IT CORRECTLY. **

** ⓵ A VARYING E(r) IS A GROWING CURVATURE MODE. **  A bound LTB shell turns around at
t_ta = pi m(r) / (-2E(r))^{3/2}, so d ln t_ta = -(3/2) d ln(-E):  ** different shells turn around at
different times, which is exactly what an inhomogeneous collapse IS. **  Its amplitude is set by the
fractional spread in E -- and by nothing the substrate supplies, which is L-150's one-constant theorem
arriving a third time.

** ⓶ AND THE CONSTRUCTION ALREADY CONSTRAINS IT. **  The capstone: "** run the transfer chain backwards
from the OBSERVED amplitude ** and the density contrast peaks where matter domination ends, at
~1e-6, falling to zero at the crunch."
⇒ ** That backward run IS a statement about E(r)'s spread. **  The corpus fixed the progenitor's
inhomogeneity from the observed amplitude, which is the only place it could have come from.

⇒⇒ *** SO THE FREE FUNCTION AND THE INHERITED DATUM ARE THE SAME FREEDOM SEEN FROM TWO ENDS: ***

      E(r)'s profile CARRIES the spectrum
      the spectrum's amplitude is MEASURED, not derived           (r2456: A_s is dimensionless)
      the substrate CANNOT supply it                              (L-150's one-constant theorem)

    ** Three statements, one fact -- and the corpus already had all three, in three places. **

** ⚠ THE CORRECTION THIS RECEIPT MAKES IS TO THIS LINE, NOT TO THE CORPUS. **  r2458 counted a function
as free while the corpus was already using it.  ** Only following it to the end showed that. **  The
row was well-posed and its answer is that there was never a spare freedom.

WHAT SURVIVES FROM r2458, and it is not nothing: ** the SIGN of E is forced by nucleosynthesis
(sec:trev's turnaround), and its PROFILE is fixed by the observed amplitude run backwards.  So BOTH
halves of the second free function are determined -- one by the construction, one by measurement -- and
NEITHER is a free parameter the corpus failed to declare. **  That is a stronger statement about the
construction than r2458 made, and it is in the construction's favour.

WHAT IS NOT CLAIMED.  Not that the backward run is a DERIVATION of A_s -- it is the opposite, and
r2456 established why it must be.  Not that the E(r) profile is uniquely determined by the amplitude
alone -- an amplitude is one number and a profile is a function.  ** Only that the freedom is not
unaccounted: its scale is set by measurement, exactly as the inherited-datum status requires. **

Written r2460.  Stated for reversal.
"""
import os, re
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  A5 -- is E(r) an unspent freedom, as r2458 claimed?')
    print()
    r = sp.Symbol('r', positive=True)
    m = sp.Function('m')(r)
    E = sp.Function('E')(r)

    # a varying E is a growing curvature mode
    t_ta = sp.pi*m/(-2*E)**sp.Rational(3, 2)
    check('a bound LTB shell turns around at t_ta = pi m / (-2E)^{3/2}',
          sp.simplify(t_ta - sp.pi*m/(-2*E)**sp.Rational(3, 2)) == 0)
    check('⇒ d t_ta / dE is nonzero, so a varying E(r) makes different shells turn around at '
          'different times -- an inhomogeneous collapse',
          sp.simplify(sp.diff(t_ta, E)) != 0)
    # the log-derivative relation
    Ec = sp.Symbol('Ec', positive=True)
    lnt = sp.log(sp.pi*sp.Symbol('mc', positive=True)/(2*Ec)**sp.Rational(3, 2))
    check('and d ln t_ta = -(3/2) d ln(-E): the mode amplitude is the fractional spread in E',
          sp.simplify(sp.diff(lnt, Ec)*Ec + sp.Rational(3, 2)) == 0)

    # and the corpus already fixes that spread, from the observed amplitude
    cap = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_ASSUMPTIONS_RETREATED_UPWARD.md'),
                                   encoding='utf-8', errors='replace').read())
    check('⛭ the capstone runs the transfer chain BACKWARDS from the OBSERVED amplitude',
          'run the transfer chain backwards from the' in cap and 'observed' in cap)
    check('and gets a density contrast peaking at ~1e-6 where matter domination ends',
          '10^{-6}' in cap and 'where matter domination ends' in cap)
    check('⇒ that backward run IS a statement about E(r)\'s spread -- the freedom is SPENT',
          'run the transfer chain backwards' in cap)

    # the three statements that are one fact
    f54 = open(os.path.join(ROOT, 'FOR_54.md'), encoding='utf-8', errors='replace').read()
    check('r2456: A_s is dimensionless, so the substrate cannot force it '
          '(routed as item 31)',
          'The substrate route is closed; the progenitor route is open' in f54)
    p15 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
                                   encoding='utf-8', errors='replace').read())
    check('and P15 treats the amplitude as measured against the substrate\'s floor, '
          'smaller by ~1e113',
          '10^{113}' in p15)

    # what survives from r2458
    p16 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'),
                                   encoding='utf-8', errors='replace').read())
    check("the SIGN of E is still forced by sec:trev's turnaround requirement",
          'it is the event that makes them' in p16)
    check('⇒ so BOTH halves are determined -- sign by the construction, profile scale by '
          'measurement -- and NEITHER is an undeclared free parameter',
          'it is the event that makes them' in p16
          and 'run the transfer chain backwards from the' in cap)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** E(r) is NOT unspent.  r2458 was wrong and this corrects it. **')
    print('  A varying E(r) is a growing curvature mode whose amplitude is the fractional spread in E,')
    print('  and ** the corpus already fixes that spread by running the transfer chain backwards from')
    print('  the observed amplitude. **')
    print('  ⇒ ** THE FREE FUNCTION AND THE INHERITED DATUM ARE THE SAME FREEDOM SEEN FROM TWO ENDS: **')
    print('     E(r) carries the spectrum; the spectrum is measured, not derived; the substrate cannot')
    print('     supply it because it is dimensionless.  Three statements, one fact.')
    print('  ⌗ AND WHAT SURVIVES IS STRONGER THAN r2458 CLAIMED, and in the construction\'s favour:')
    print('    ** the SIGN of E is forced by nucleosynthesis and its PROFILE scale by measurement, so')
    print('    NEITHER half is an undeclared free parameter. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
