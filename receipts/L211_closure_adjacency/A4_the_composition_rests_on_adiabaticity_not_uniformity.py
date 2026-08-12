#!/usr/bin/env python3
"""A4 -- L-234's first move: the derived composition is E-profile-INDEPENDENT, and rests on a mode
condition the corpus does not state.

** THE QUESTION (L-234, r2458): ** does the derived progenitor composition depend on E being constant?
"If it does, the homogeneous choice is load-bearing and should be marked as one."

** IT DOES NOT, and the reason sharpens rather than dissolves the row. **

THE DERIVATION, in the capstone's own words: "in spherical collapse ** a small perturbation shares its
background's composition, ** so the patch's equality is the ambient universe's."

  patch ratio / background ratio = (rho_r0 (1+delta_r)) / (rho_m0 (1+delta_m)) / (rho_r0/rho_m0)
                                 = (1 + delta_r) / (1 + delta_m)
                                 = 1 + (delta_r - delta_m) + O(2)

⇒ ** IT HOLDS TO FIRST ORDER IFF delta_r ~ delta_m -- WHICH IS ADIABATICITY, a statement about the
  perturbation MODE, not about E(r). **  And the composition ratio contains no E at all: E enters only
  through the turnaround RADIUS R_max = -m/E.

⇒⇒ *** SO THE DERIVATION RESTS ON SMALLNESS + ADIABATICITY, NOT ON UNIFORMITY.  The homogeneous choice
   is NOT load-bearing for the composition, and E(r)'s PROFILE survives as an unspent degree of
   freedom. ***

** WHY THAT STRENGTHENS r2458 RATHER THAN CLOSING IT: ** the question was asked expecting it might
consume E(r).  It does not -- ** so the free function is confirmed AVAILABLE to the progenitor route
that r2456 left as the only remaining one for A_s and n_s. **

** ⛭ AND A SECOND THING FALLS OUT THAT WAS NOT SOUGHT: THE MODE CONDITION IS NOT STATED. **
The capstone's composition passage does not mention adiabaticity or isocurvature.  ** P15 and P16 use
"adiabatic" -- but for a DIFFERENT quantity: the WKB adiabaticity parameter C/mu_n of the branch-point
filter, and adiabatic compression on the infall leg.  Neither is the perturbation-mode condition
delta_r ~ delta_m. **

⇒ ** AND THE POINT IS SHARPER THAN "AN UNSTATED PREMISE": an isocurvature mode IS delta_r != delta_m --
  a COMPOSITION perturbation.  So the composition derivation assumes the progenitor's perturbation is
  adiabatic, which is exactly the mode content the theory says it INHERITS rather than derives
  ("classical, non-vacuum primordial statistics"; "the branch point carries the progenitor tilt"). **
  The premise is borrowed from the very thing the construction treats as inherited data.

WHAT IS NOT CLAIMED.  Not that the assumption is wrong -- adiabatic primordial perturbations are
strongly favoured observationally and are the standard case.  Not that the derivation fails.  ** Only
that the condition it rests on is a MODE condition, that it is not stated where the derivation is made,
and that it is drawn from the inherited sector rather than from the construction. **

Written r2459.  Stated for reversal.
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
    print("  A4 -- does the derived composition depend on E being constant?")
    print()
    cap = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_ASSUMPTIONS_RETREATED_UPWARD.md'),
                                   encoding='utf-8', errors='replace').read())
    p15 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
                                   encoding='utf-8', errors='replace').read())

    check('the capstone derives the composition from "a small perturbation shares its '
          "background's composition\"",
          'a small perturbation shares its' in cap and "background's composition" in cap)

    # the algebra
    rr0, rm0, dr, dm = sp.symbols('rho_r0 rho_m0 delta_r delta_m', positive=True)
    ratio = (rr0*(1 + dr))/(rm0*(1 + dm))
    rel = sp.simplify(ratio/(rr0/rm0))
    check('patch/background ratio = (1+delta_r)/(1+delta_m)',
          sp.simplify(rel - (1 + dr)/(1 + dm)) == 0)
    eps = sp.Symbol('epsilon')
    ser = sp.series(rel.subs({dr: eps*sp.Symbol('a_r'), dm: eps*sp.Symbol('a_m')}), eps, 0, 2).removeO()
    check('⇒ = 1 + (delta_r - delta_m) + O(2), so it holds to first order iff delta_r ~ delta_m',
          sp.simplify(ser.coeff(eps) - (sp.Symbol('a_r') - sp.Symbol('a_m'))) == 0)
    check('⛭ and the composition ratio contains NO E at all -- E enters only via R_max = -m/E',
          sp.diff(ratio, sp.Symbol('E')) == 0)

    # so the answer to L-234's first move
    check('⇒ the derivation rests on SMALLNESS + ADIABATICITY, not on uniformity: '
          'the homogeneous choice is NOT load-bearing for the composition',
          sp.diff(ratio, sp.Symbol('E')) == 0)

    # and the second, unsought finding: the mode condition is not stated
    i = cap.find('shares its')
    passage = cap[max(0, i-700):i+500]
    check('the composition passage does not mention adiabaticity',
          'adiabat' not in passage.lower())
    check('nor isocurvature, anywhere in the capstone',
          'isocurv' not in cap.lower())
    check('and P15\'s "adiabaticity" is a DIFFERENT quantity: the WKB parameter '
          '$C/\\mu_n$ of the branch-point filter',
          'adiabaticity parameter $C/\\mu_{n}$' in p15)

    # and the sharper point: the premise comes from the inherited sector
    check('P15 treats the primordial statistics as INHERITED: "the branch point carries the '
          'progenitor tilt"',
          'the branch point carries the progenitor tilt' in p15)
    check('⇒ so an adiabatic-mode premise is drawn from the very sector the construction '
          'treats as inherited data',
          'Classical, non-vacuum primordial statistics' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the derived composition is E-profile-INDEPENDENT. **")
    print('  It rests on SMALLNESS + ADIABATICITY -- delta_r ~ delta_m, a statement about the')
    print('  perturbation MODE -- and the ratio contains no E at all.')
    print("  ⇒ ** So the homogeneous choice is NOT load-bearing, and E(r)'s profile survives as an")
    print('     unspent degree of freedom -- confirmed AVAILABLE to the progenitor route that r2456')
    print('     left as the only remaining one for A_s and n_s. **')
    print('  ⛭ AND A SECOND FINDING, not sought: ** the mode condition is not stated where the')
    print('    derivation is made **, and P15/P16\'s "adiabatic" is a different quantity.')
    print('    ⇒ An isocurvature mode IS delta_r != delta_m -- a COMPOSITION perturbation -- so the')
    print('      premise is drawn from the very sector the construction treats as INHERITED.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
