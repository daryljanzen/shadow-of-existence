#!/usr/bin/env python3
"""
L-107 — IS THE TRANSVERSE SPACE AT THE WALL ROUND, AND DOES THE TOWER TRUNCATE IF NOT?

WHY THIS IS THE DECIDING COMPUTATION.  L-15 landed the quark/lepton distinction as a
GRADING (triality = -lambda mod 3) and could not land the COUNT, because two countings
disagree: the geometry has 12 legs + 3 walls = 15, matching one Standard Model generation,
while the mode tower over lambda is INFINITE.  L-15's PART 5 listed three ways out and bet
on (c) -- "the seats carry the states and the tower is a redundancy of the description" --
for one stated reason: the 3 walls and 12 legs are FORCED, while the tower's degeneracy
2|lambda| is the ROUND sphere's and L-90 records roundness as a CHOICE.  If the transverse
space is not round, the degeneracy changes and the tower may truncate.

** SO THIS COMPUTATION IS A FALSIFIER OF MY OWN PREFERRED READING, AND IT IS RUN AS ONE. **

  PART 1  Is roundness a choice?  CR's own operator, run with the transverse curvature LEFT FREE.
  PART 2  The second forcing, which is independent of the first: spin structure.
  PART 3  What if we allow an ORBIFOLD -- which CR, of all constructions, has a right to?
  PART 4  ** THE VERDICT ON THE TOWER, AND IT GOES AGAINST (c). **
  PART 5  What that does to L-15, to P14, to L-90, and to the base rate.  Nothing softened.

Run: python3 L107_is_the_transverse_space_round.py     (sympy, numpy)
"""
import itertools
import numpy as np
import sympy as sp

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — IS ROUNDNESS A CHOICE?  RUN CR'S OWN OPERATOR WITH k LEFT FREE.")
print("=" * 78)
print("  The corpus writes the cut as   ds^2 = -f dt^2 + dr^2/f + r^2 dOmega^2,")
print("  with dOmega^2 the UNIT ROUND two-sphere, and never derives the dOmega^2.  That is")
print("  what L-90 records.  So replace it by a transverse 2-space of CONSTANT CURVATURE k")
print("  left free -- k = +1 round, k = 0 flat, k = -1 hyperbolic -- and run L-01's")
print("  computation again.  ** If k comes out forced, roundness is an OUTPUT and L-90 is")
print("  discharged; if k is free, L-15's bet is live. **")
print()

r, t, chi, ph, Lam, M, k = sp.symbols('r t chi phi Lambda M k', real=True)
f = sp.Function('f')

def Gtt_transverse_k():
    """G^t_t for ds^2 = -f dt^2 + dr^2/f + r^2 (dchi^2 + S_k(chi)^2 dphi^2),
    computed from the metric.  S_k is any function with S_k'' = -k S_k, which is exactly
    the condition that the transverse 2-space have Gaussian curvature k."""
    S = sp.Function('S')
    F = f(r)
    coords = [t, r, chi, ph]
    g = sp.diag(-F, 1/F, r**2, r**2*S(chi)**2)
    gi = g.inv()
    n = 4
    Gam = [[[sum(gi[a, d]*(sp.diff(g[d, b], coords[c]) + sp.diff(g[d, c], coords[b])
                           - sp.diff(g[b, c], coords[d])) for d in range(n))/2
             for c in range(n)] for b in range(n)] for a in range(n)]
    def Ric(b, c):
        e = 0
        for a in range(n):
            e += sp.diff(Gam[a][b][c], coords[a]) - sp.diff(Gam[a][b][a], coords[c])
            for d in range(n):
                e += Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a]
        return sp.simplify(e)
    R = sp.simplify(sum(gi[a, b]*Ric(a, b) for a in range(n) for b in range(n)))
    Gtt_ = sp.simplify(sum(gi[0, a]*(Ric(a, 0) - g[a, 0]*R/2) for a in range(n)))
    # impose constant Gaussian curvature k on the transverse space:  S'' = -k S
    Gtt_ = Gtt_.subs(sp.Derivative(S(chi), (chi, 2)), -k*S(chi))
    return sp.simplify(sp.expand(Gtt_))

G = Gtt_transverse_k()
print("  G^t_t  =", sp.simplify(G))
print()
print("  CR's operator is P8 thm:kernel's:  T_{mu nu} = 0 on a cut in the construction gauge.")
print("  With a cosmological term that reads  G^t_t + Lambda = 0.  The ODE:")
ode = sp.simplify(sp.expand(sp.numer(sp.together(G + Lam))))
ode = sp.simplify(sp.expand(ode/sp.gcd(tuple(sp.Poly(ode, f(r), sp.Derivative(f(r), r)).coeffs()))))
print("     ", sp.Eq(sp.simplify(ode), 0))
sol = sp.dsolve(sp.Eq(sp.expand(G + Lam), 0), f(r))
print()
print("  ** THE ENTIRE SOLUTION SPACE: **")
fsol = sp.simplify(sol.rhs)
print("      f(r) =", fsol)
C1 = [s for s in fsol.free_symbols if s.name.startswith('C')]
fnice = fsol.subs({C1[0]: -2*M}) if C1 else fsol
print("      i.e.  f(r) = k - 2M/r - Lambda r^2/3      (C1 = -2M)")
print(f"      check: f = k - 2M/r - Lambda r^2/3 solves it?  "
      f"{sp.simplify((sp.expand(G + Lam)).subs(f(r), k - 2*M/r - Lam*r**2/3).doit()) == 0}")
print()
print("  ⌗ SO k SURVIVES AS THE CONSTANT TERM OF f, AND NOTHING IN THE OPERATOR FIXES IT.")
print("  ** The operator alone leaves roundness a choice, exactly as L-90 says. **")
print("  ⌗ BUT THE OPERATOR IS NOT ALL CR HAS, and the construction fixes k independently:")
print()
for s in [
 "  ① k is a constant of the FAMILY: it appears in f as an additive constant and does not",
 "     depend on M, so one member of the family fixes it for every member.",
 "  ② CR's family HAS a distinguished M = 0 member, and has it SIX TIMES: 2M = (2/3sqrt3) sin 3w",
 "     vanishes at w = 0, 60, 120, 180, 240, 300 degrees (P3 sec:tour).  At those marks the cut",
 "     is the SUBSTRATE ITSELF -- pure de Sitter, undeformed.",
 "  ③ And de Sitter in static form is f = 1 - r^2/alpha^2.  Its constant term is 1.",
 "  ⇒ ** k = +1, FORCED -- not by an ansatz but by the family passing through the substrate",
 "     six times per swing.  A cut with k != 1 could not degenerate to the substrate at",
 "     2M = 0, and CR's dial makes it do so at every sixty degrees. **",
]:
    print(s)
print()
print(f"  check ③: static de Sitter f = 1 - r^2/alpha^2 solves the ODE at M = 0 with k = 1 and")
al = sp.symbols('alpha', positive=True)
chk = sp.simplify((sp.expand(G + Lam)).subs({k: 1, Lam: 3/al**2}).subs(f(r), 1 - r**2/al**2).doit())
print(f"           Lambda = 3/alpha^2?  {chk == 0}     (and CR DEFINES alpha = sqrt(3/Lambda))")
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 1's CLAIM, ASSERTED.  (a) the ENTIRE solution space of CR's operator with the
# transverse curvature left free is f = k - 2M/r - Lambda r^2/3: the general solution
# returned by dsolve is C1/r - Lambda r^2/3 + k, and it solves the ODE identically once
# C1 = -2M, so k survives as the CONSTANT TERM and the operator alone does not fix it.
# (b) the M = 0 member does fix it: static de Sitter f = 1 - r^2/alpha^2 solves the ODE
# with Lambda = 3/alpha^2 -- and its constant term is 1, hence k = +1 as an OUTPUT.
assert len(C1) == 1 and sp.simplify(fnice - (k - 2*M/r - Lam*r**2/3)) == 0, \
    "the general solution must be exactly f = k - 2M/r - Lambda r^2/3"
assert sp.simplify((sp.expand(G + Lam)).subs(f(r), k - 2*M/r - Lam*r**2/3).doit()) == 0, \
    "f = k - 2M/r - Lambda r^2/3 must solve the operator's ODE for every k"
assert chk == 0, "static de Sitter with Lambda = 3/alpha^2 must solve the ODE at k = 1"
assert sp.simplify((sp.expand(G + Lam)).subs({k: 3, Lam: 3/al**2})
                   .subs(f(r), 1 - r**2/al**2).doit()) != 0, \
    "CONTROL: the de Sitter member must NOT solve it at k = 3, so the M = 0 member fixes k"
# -----------------------------------------------------------------------------------
print("  ⌗ ** L-90 IS DISCHARGED, AND IN THE DELETE DIRECTION: roundness was recorded as an")
print("  input and is an OUTPUT. **  Nothing is added; an apparent freedom is removed.")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE SECOND FORCING, INDEPENDENT OF THE FIRST: SPIN STRUCTURE")
print("=" * 78)
print("  k = +1 fixes the LOCAL geometry and not the global one: any quotient S^2/Gamma by a")
print("  finite Gamma acting freely by isometries has curvature +1 too.  So which are there?")
print()
print("  The finite subgroups of SO(3) are classified: cyclic Z_n, dihedral D_n, and the three")
print("  polyhedral groups A_4, S_4, A_5.  ** Every non-identity element of SO(3) is a rotation")
print("  about an AXIS, and that axis meets S^2 in two FIXED points. **  So:")
print()
print(f"  {'Gamma':>10} {'acts freely on S^2?':>21} {'quotient':>14} {'orientable':>11} {'spin':>6}")
for nm, free, quot, orient, spin in [
        ("Z_n (n>1)", "NO -- 2 fixed pts", "spindle orbifold", "yes", "orbifold"),
        ("D_n", "NO -- fixed pts", "orbifold", "yes", "orbifold"),
        ("A_4,S_4,A_5", "NO -- fixed pts", "orbifold", "yes", "orbifold"),
        ("Z_2 antipodal", "YES", "RP^2", "NO", "NONE"),
        ("trivial", "YES", "S^2", "yes", "YES")]:
    print(f"  {nm:>10} {free:>21} {quot:>14} {orient:>11} {spin:>6}")
print()
print("  ** The antipodal map is the ONLY free finite action on S^2, it is not in SO(3)")
print("     (det(-I) = -1 in three dimensions), its quotient RP^2 is NON-ORIENTABLE, and a")
print("     non-orientable surface carries NO SPIN STRUCTURE -- hence no Dirac operator. **")
print()
print("  ⇒ ** THE TRANSVERSE SPACE OF A SMOOTH SPIN CUT IS THE ROUND S^2 AND NOTHING ELSE.")
print("     Two independent forcings, neither of them an assumption: the family's own M = 0")
print("     member fixes k = +1, and the spin structure fixes Gamma = 1. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — BUT WHAT IF WE ALLOW AN ORBIFOLD?  CR HAS A RIGHT TO ASK.")
print("=" * 78)
print("  This branch is run rather than waved off, because CR is a construction that traffics")
print("  in branch points: r = 0 is one, of order three, and the corpus reads its monodromy")
print("  r -> omega r as the TRIALITY (L-78).  If any construction were entitled to a Z_3")
print("  orbifold in the transverse space it would be this one.  ** So suppose the transverse")
print("  space is the spindle S^2/Z_n. **  What happens to the tower?")
print()
print("  On the unit round S^2 the Dirac operator has eigenvalues +-(l+1), l = 0,1,2,...,")
print("  with multiplicity 2(l+1); writing lambda = l+1 = j+1/2 (P14's own labelling),")
print("  ** lambda runs over the POSITIVE INTEGERS with degeneracy 2 lambda. **  Within a")
print("  given lambda the states are labelled by an azimuthal number running over 2 lambda")
print("  values.  A Z_n quotient keeps the states invariant under phi -> phi + 2 pi/n, which")
print("  is a condition on the AZIMUTHAL label, not on lambda:")
print()
print(f"  {'lambda':>7} {'deg on S^2':>11} " +
      "".join(f"{'deg on S^2/Z_'+str(n):>16}" for n in (2, 3, 5)))
for lam in range(1, 9):
    row = f"  {lam:>7} {2*lam:>11} "
    for n in (2, 3, 5):
        kept = len([m for m in range(2*lam) if (m - (lam - 1)) % n == 0])
        row += f"{kept:>16}"
    print(row)
print()
# --- r2376+c54.159 -----------------------------------------------------------------
# PART 3's CLAIM, ASSERTED.  The table's last row is lambda = 8, where the round S^2 carries
# degeneracy 2 lambda = 16 and the Z_5 quotient still keeps 3 states -- about 2 lambda/5.
# The rung SURVIVES: the quotient thins the degeneracy and never empties it, which is the
# whole of "no value of n removes a single RUNG".
assert lam == 8 and 2*lam == 16, "the tower's last tabulated rung must be lambda = 8"
assert kept == 3 and kept >= 1, \
    "the Z_5 quotient must keep 3 of the 16 states at lambda = 8 -- thinned, not removed"
# -----------------------------------------------------------------------------------
print("  ** THE TOWER SURVIVES EVERY QUOTIENT.  lambda still runs over ALL positive integers;")
print("     only the degeneracy thins, from 2 lambda to about 2 lambda / n.  No value of n")
print("     removes a single RUNG. **  And that is not an accident of the arithmetic: lambda")
print("     indexes the transverse Dirac operator's eigenvalue, which is set by the LOCAL")
print("     geometry, and a quotient does not change the local geometry at all.  A quotient")
print("     can only DELETE STATES WITHIN A RUNG.  ** To truncate a tower one needs a")
print("     transverse space of different local curvature or of finite diameter cut off, and")
print("     PART 1 has just shown CR has neither available. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE VERDICT, AND IT GOES AGAINST THE READING I BET ON")
print("=" * 78)
for s in [
 "L-15 PART 5 offered three ways to reconcile 15 seats with an infinite tower:",
 "",
 "  (a) something truncates the tower to its lowest rungs;",
 "  (b) the tower IS the content and the SM's 15 is its lowest level  (L-88);",
 "  (c) the seats carry the states and the tower is a redundancy of the description.",
 "",
 "and it bet on (c), for the stated reason that the degeneracy 2|lambda| is the round",
 "sphere's and roundness is a choice.  ** The reason is now gone, and it is gone twice: **",
 "",
 "  * roundness is NOT a choice -- it is forced by the family's own M = 0 member and again,",
 "    independently, by the spin structure (PARTS 1-2);",
 "  * and even if it WERE a choice, no available alternative truncates the tower, because a",
 "    quotient thins rungs and cannot remove them (PART 3).",
 "",
 "** SO (a) IS DEAD AND (c) IS DEAD.  L-15's OWN FALSIFIER (5) FIRES: 'if (c) fails -- if the",
 "   modes at one seat cannot be identified -- then the seat count is decorative and F-11's",
 "   12 + 3 is a coincidence of small integers.' **",
 "",
 "⌗ AND I RECORD IT AS A LOSS RATHER THAN REDESCRIBING IT.  The 12 + 3 = 15 agreement with",
 "one Standard Model generation was the most striking numerical coincidence this stretch",
 "produced.  It is not explained by anything computed here, and the route I judged most",
 "likely to explain it is closed.  ** (b) is the only survivor, and (b) is L-88. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT THIS SETTLES ELSEWHERE.  Four ledgers move, two of them upward.")
print("=" * 78)
for s in [
 "① ** P14's NEGATIVE RESULT IS UPGRADED FROM OBSERVED TO FORCED. **  P14 records that 'the",
 "   angular decomposition does not supply multiplicity, since lambda = j+1/2 labels partial",
 "   waves and each contributes exactly one bound mode', and calls this 'one negative result'",
 "   that 'closes one source and leaves the bundle question open'.  ** It stated that as a",
 "   fact about the round sphere it had written down.  It is now a fact about the only",
 "   transverse space CR admits **, so the source is closed not by inspection but by",
 "   exhaustion, and P14's sentence can be strengthened rather than merely kept.",
 "",
 "② ** L-90 IS DISCHARGED, IN THE DELETE DIRECTION. **  'The transverse space is taken ROUND'",
 "   was registered as an unexamined input.  It is an output of the operator plus the M = 0",
 "   member.  ** An apparent freedom of the construction is removed, not a structure added. **",
 "",
 "③ ** L-15 IS DEMOTED FROM A LANDING TO A GRADING, WHICH IS WHAT IT ACTUALLY IS. **  The",
 "   triality reading -- a lepton is a wall-bound mode with lambda = 0 mod 3 -- is untouched",
 "   by any of this and remains the strongest thing in that lead, together with its account",
 "   of P14's 'only as a complete set'.  ** What dies is the COUNT, and only the count. **",
 "   And L-15's 2:1 over partial waves is now in open tension with P14's own statement that",
 "   the partial waves are not internal content; ** the tension is real, it is registered,",
 "   and this computation does not resolve it in L-15's favour. **",
 "",
 "④ ** THE BASE RATE TAKES A DATA POINT, AND IT IS AGAINST US. **  THE_BASE_RATE's finding is",
 "   that least-arbitrariness arguments which DELETE succeed and ones which ADD fail.  The",
 "   12 + 3 = 15 reading ADDED: it proposed that the seat structure explains a number.  It was",
 "   tested here and did not survive.  ** That is the discriminant working as advertised, on",
 "   the corpus's own claim, one turn after the corpus wrote the discriminant down. **",
 "   Meanwhile the roundness result DELETED, and it survived.  Two for two.",
]:
    print("  " + s)
print()
print("  ⌗ WHAT IS OWED NEXT, NAMED RATHER THAN GESTURED AT: (b) is the last survivor, so")
print("  ** L-88 -- 'does the tower have a Kaluza-Klein shape?' -- is now the count's only")
print("  remaining route **, and it should be worked with the knowledge that the tower is")
print("  infinite, its rungs are the positive integers, and its degeneracy is exactly 2 lambda.")
