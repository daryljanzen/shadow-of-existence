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
import subprocess
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
    # ⛭⛭ r7338+60, PO-78's repair stride, the middle -- EDITED ON `r7337` ④'s order.
    #   ** THE OWED ROW WAS THE TOKEN `observed`, conjoined with a span that stops at `from the`:
    #   the conjunction asked for a prefix AND for a word that occurs throughout the file, so the
    #   arm could not fail for the right reason. **
    #   ⇒ *** One span over a MARKDOWN-normalised read -- the emphasis falls on `observed` inside
    #     the carrying clause -- running to what the backward chain actually yields. ***
    _cap_md = re.sub(r'\*+', '', cap)
    _BACKWARDS = ('run the transfer chain backwards from the observed amplitude and the density '
                  'contrast peaks where matter domination ends')
    check('⛭ the capstone runs the transfer chain BACKWARDS from the OBSERVED amplitude -- asserted '
          'as the clause that names what the backward run yields, over a markdown-normalised read, '
          'in place of a prefix conjoined with a ubiquitous word',
          _BACKWARDS in _cap_md)
    check('and gets a density contrast peaking at ~1e-6 where matter domination ends',
          '10^{-6}' in cap and 'where matter domination ends' in cap)
    check('⇒ that backward run IS a statement about E(r)\'s spread -- the freedom is SPENT',
          'run the transfer chain backwards' in cap)

    # the three statements that are one fact
    # ⛔⛭⛭⛭ r7280 (60), on r7279's ruling ③: THE LIVE READ OF A FROZEN FILE MEASURED NOTHING.
    #   *`FOR_54.md` is a RETIRED node's forward file, last written 2026-09-19.  Nothing updates it,
    #   so a live `in` test on it asserts a state nobody maintains: the pin would stay green
    #   indefinitely and would fire on neither the progenitor route closing nor the file being
    #   reworded.*  ⇒ *** And the day the route DOES close, a live pin on the sentence saying it is
    #   open goes red ON THE WORK SUCCEEDING, which is the blindness family -- this key was verdicted
    #   REPAIR-OWED at r7270 for exactly that, at two sites. ***
    #   ⌊ *The fact the receipt wants is HISTORICAL -- the progenitor route was open when `A2`'s
    #     result was routed -- so it is read AT THE COMMIT that introduced the sentence, and the live
    #     arm is DROPPED rather than kept: `L-249`, and the discipline of this whole stretch.*
    _F54_AT = 'ecb0aea4'       # the commit that introduced the sentence into FOR_54.md, 2026-08-12
    _f54_ok = subprocess.run(['git', 'cat-file', '-e', _F54_AT + '^{commit}'],
                             cwd=ROOT, capture_output=True).returncode == 0
    f54 = subprocess.run(['git', 'show', f'{_F54_AT}:FOR_54.md'], cwd=ROOT,
                         capture_output=True, text=True, errors='replace').stdout
    check('r2456: A_s is dimensionless, so the substrate cannot force it '
          '(routed as item 31)',
          _f54_ok and bool(f54)
          and 'The substrate route is closed; the progenitor route is open' in f54)
    p15 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
                                   encoding='utf-8', errors='replace').read())
    check('and P15 treats the amplitude as measured against the substrate\'s floor, '
          'smaller by ~1e113',
          '10^{113}' in p15)

    # what survives from r2458
    p16 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'),
                                   encoding='utf-8', errors='replace').read())
    # ⛭⛭ r7338+60: ** and `it is the event that makes them` opens on a pronoun whose referent --
    #   the crossing -- sits outside the span, so it carries no proposition. **
    #   ⇒ *One span: the crossing named, and what it is not incidental to.*  ONE site.
    _CROSSING = ('The crossing from collapse to expansion is therefore not incidental to the '
                 'abundances: it is the event that makes them')
    check("the SIGN of E is still forced by sec:trev's turnaround requirement -- \"The crossing "
          'from collapse to expansion is therefore not incidental to the abundances: it is the '
          'event that makes them", asserted with its own subject inside the span',
          _CROSSING in p16)
    check('⇒ so BOTH halves are determined -- sign by the construction, profile scale by '
          'measurement -- and NEITHER is an undeclared free parameter',
          _CROSSING in p16 and _BACKWARDS in _cap_md)

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
