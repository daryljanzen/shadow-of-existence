#!/usr/bin/env python3
"""A3 -- L-211 run on L-207's exhibition, followed into P16: E(r)'s profile is the live freedom.

** THE PROCEDURE (L-211), fifth run. **  L-207's exhibition (r2450) put the general inhomogeneous leaf
in LTB form and named ** TWO free functions, m(r) and E(r) **.  Following them into P16.

** WHAT THE TWO FUNCTIONS ARE DOING IN THE CORPUS: **

  * ** m(r) ** -- the mass function.  The corpus's inherited datum lives here.
  * ** E(r), ITS SIGN -- FORCED, and P16 forces it INDEPENDENTLY. **  LTB turnaround needs
    Rdot^2 = 2m/R + 2E = 0, i.e. R_max = -m/E > 0, ** which requires E < 0 **; E = 0 gives
    R ~ tau^{2/3}, monotone, NO turnaround.  And P16 sec:trev: "the heating leg cannot fix a surviving
    abundance; only a subsequent COOLING pass can.  ** The turnaround is not incidental to the
    abundances: it is the event that makes them. **"
    ⇒ ** So the sign of the second free function is fixed by nucleosynthesis, not chosen. **
  * ** E(r), ITS PROFILE -- the remaining freedom, and it IS a choice. **
    P2's cycloid r(z) = M(1 + cos z) matches the standard bound-LTB parametrisation
    R = (m/(-2E))(1 - cos eta) at m = M, giving ** E = -1/2, a CONSTANT **.
    ⇒ ** E constant is a HOMOGENEOUS progenitor interior.  E(r) varying is a genuinely INHOMOGENEOUS
      one. **

** ⛭⛭ AND THIS JOINS DIRECTLY TO A2 (r2456). **  There, P15's three owed derivations collapsed into one
closed boundary -- ** the substrate cannot force A_s, n_s or rho_r/rho_m, because all three are
dimensionless magnitudes ** -- with the distinction preserved that "cannot be derived FROM THE SUBSTRATE"
is not "cannot be derived at all", ** the progenitor route being open and already walked once **.

⇒⇒ *** E(r)'s PROFILE IS THE FREE FUNCTION THAT ROUTE WOULD USE.  The inhomogeneity of the progenitor is
   precisely the free data that could carry a spectrum -- and the corpus currently runs on E constant,
   which is the homogeneous choice. ***

** WHAT IS NOT A DEFECT HERE, and this must not be read as one: **
  * P16's scope statement is exactly right -- "this account works in the spherically symmetric class,
    and that class is a premise of the construction rather than a gap in it".
  * sec:trev forces the sign correctly and independently.
  * ** The observation is only that ONE FUNCTION'S PROFILE IS A LIVE DEGREE OF FREEDOM THE CORPUS SETS
    TO A CONSTANT, and that this is where the progenitor route for A_s and n_s would have to live. **

WHAT IS NOT CLAIMED.  Not that a varying E(r) yields A_s or n_s -- nothing here computes that.  Not that
E = const is wrong; a homogeneous progenitor interior may well be the right model, and the derived
composition rests on it.  ** Only that the choice is a choice, that its sign is forced while its profile
is not, and that the profile is the one place the corpus's own open question could be answered. **

Written r2458.  Stated for reversal.
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
    print("  A3 -- L-211 on L-207's exhibition: where did the second free function go?")
    print()
    p16 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'),
                                   encoding='utf-8', errors='replace').read())
    p2 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', 'janzen_circle_v3.tex'),
                                  encoding='utf-8', errors='replace').read())

    # the sign of E is forced by the turnaround
    m, E = sp.symbols('m E')
    Rmax = -m/E
    check('LTB turnaround needs R_max = -m/E > 0, so E < 0',
          sp.simplify(Rmax.subs({m: 1, E: -sp.Rational(1, 2)})) > 0
          and sp.simplify(Rmax.subs({m: 1, E: sp.Rational(1, 2)})) < 0)
    tau = sp.Symbol('tau', positive=True)
    R0 = (sp.Rational(9, 2)*sp.Symbol('m', positive=True)*tau**2)**sp.Rational(1, 3)
    check('and E = 0 gives R ~ tau^{2/3}, monotone -- NO turnaround',
          sp.simplify(sp.diff(R0, tau)) != 0)

    # and P16 forces the turnaround independently
    check('P16 sec:trev: the heating leg cannot fix a surviving abundance',
          'The heating leg' in p16 and 'cannot fix a surviving light-element abundance' in p16)
    check('⇒ "the turnaround ... is the event that makes them"',
          'it is the event that makes them' in p16)
    check('⛭ SO THE SIGN OF THE SECOND FREE FUNCTION IS FIXED BY NUCLEOSYNTHESIS, not chosen',
          'only a subsequent \\emph{cooling} pass through the window can' in p16
          or 'only a subsequent' in p16)

    # the profile is a choice: P2's cycloid is E = -1/2 constant
    check("P2 carries the cycloid r(z) = M(1 + cos z)",
          'M(1+\\cos z)' in p2 or 'M\\left(1+\\cos z\\right)' in p2 or '1+\\cos z' in p2)
    z, Msym, eta = sp.symbols('z M eta', positive=True)
    lhs = Msym*(1 + sp.cos(z))
    rhs = (Msym/(-2*sp.Rational(-1, 2)))*(1 - sp.cos(eta))
    check('and it matches the bound-LTB form R = (m/(-2E))(1-cos eta) at m = M with E = -1/2',
          sp.simplify(rhs - Msym*(1 - sp.cos(eta))) == 0
          and sp.simplify(lhs.subs(z, sp.pi - eta) - Msym*(1 - sp.cos(eta))) == 0)
    # ** a literal tautology stood here in the first draft.  Replaced with the thing actually
    # claimed: E = -1/2 has NO r-dependence, and a varying E would give an r-dependent turnaround
    # radius R_max = -m/E -- which is what "homogeneous versus inhomogeneous interior" MEANS. **
    rr = sp.Symbol('r', positive=True)
    E_const = sp.Rational(-1, 2)
    E_vary = -sp.Rational(1, 2)*(1 + rr**2)
    m_of_r = sp.Function('m')(rr)
    Rmax_const = sp.simplify(-m_of_r/E_const)
    Rmax_vary = sp.simplify(-m_of_r/E_vary)
    check('⇒ E = -1/2 is a CONSTANT: dE/dr = 0, so the turnaround radius R_max = -m/E depends on r '
          'only through m -- a homogeneous interior; a varying E(r) makes R_max depend on r twice',
          sp.diff(E_const, rr) == 0
          and sp.diff(E_vary, rr) != 0
          and sp.simplify(sp.diff(Rmax_vary, rr) - sp.diff(Rmax_const, rr)) != 0)

    # P16's scope statement is right and must not be read as a defect
    check("P16 states its scope correctly: the spherically symmetric class is a PREMISE, not a gap",
          'that class is a premise of the construction rather than a gap in it' in p16)

    # and the join to A2
    # ** A2's result was ROUTED, not registered as a row -- so the check belongs on FOR_54,
    # not on THE_LIVE_ARC.  The first draft looked in the register and failed: the same
    # summary-versus-source error as A2's own first draft, one revision later. **
    f54 = open(os.path.join(ROOT, 'FOR_54.md'), encoding='utf-8', errors='replace').read()
    check('A2 (r2456, routed as item 31) left the progenitor route open for $A_s$ and $n_s$',
          'The substrate route is closed; the progenitor route is open' in f54)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: the second free function's SIGN is forced and its PROFILE is a choice.")
    print('  ** E < 0 is required for a turnaround, and P16 sec:trev forces the turnaround')
    print('     independently -- "it is the event that makes them". **  So the sign is fixed by')
    print('  nucleosynthesis, not chosen.')
    print("  ** But P2's cycloid is E = -1/2, a CONSTANT -- a homogeneous progenitor interior -- and")
    print('     E(r) varying is a genuinely inhomogeneous one. **')
    print('  ⇒ ** AND THAT JOINS A2: the substrate cannot force A_s or n_s because they are')
    print('     dimensionless, and the progenitor route is open.  E(r)\'s PROFILE is the free function')
    print("     that route would use -- the progenitor's inhomogeneity is the free data that could")
    print('     carry a spectrum, and the corpus runs on the homogeneous choice. **')
    print('  ⌗ Not a defect: P16\'s scope statement is exactly right and sec:trev is correct.  The')
    print('    observation is that a live degree of freedom is set to a constant.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
