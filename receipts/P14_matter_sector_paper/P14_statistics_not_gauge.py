"""
P14_statistics_not_gauge.py -- P14 sec:count / sec:openquestions: the three wall modes are the
kernel of ONE Dirac operator, hence identical particles, and second quantisation -- a step this
construction never took -- removes the invariant over-count outright.  ** It also SELECTS the
configuration group uniquely, which is more than was asked for: exactly one of three candidates
survives, and it is the same group the su(3) entailment reached by an unrelated argument. **

THE QUESTION.  P14_no_choice_of_group_works closed on "an account of when two constituents at
different vantages are the same particle -- a question about the OPERATOR whose zero-modes they
are, not about the bundle."

WHAT IS ESTABLISHED.
  1. ** THIS PAPER ANSWERS IT IN ITS OWN CONSTRUCTION. **  Proposition prop:wall binds one
     chiral zero-mode per wall, and the index computed is the index of A Dirac operator, one
     mode per wall per internal state: three modes, ONE operator, ONE kernel.  Excitations of a
     single field are identical particles by construction -- not an extra postulate but what
     having a single operator means.
  2. ** THE STEP NEVER TAKEN IS THE ORDINARY ONE: SECOND QUANTISATION. **  Everything in this
     sector has treated the modes as classical labels and asked which TENSORS are invariant.  A
     three-fermion state is not a general tensor; it lives in the EXTERIOR cube of the kernel,
     and most of the tensor cube is not a state at all.
  3. ** SO THE SPURIOUS INVARIANTS OF P14_the_gap_is_antisymmetry ARE NOT STATES A SYMMETRY
     FAILS TO FORBID -- THEY DO NOT EXIST. **  Lambda^3 of a three-dimensional space is
     one-dimensional and its generator is the totally antisymmetric combination, which is
     epsilon.  The all-on-one-vantage state is a-dagger three times over and vanishes by the
     Pauli principle; the symmetric one-per-vantage sum is not in Lambda^3 at all.
  4. ** THE TABLE REDONE, AND EXACTLY ONE ROW IS RIGHT -- asserted in the run, so it fails
     rather than prints if that changes. **
       Gamma_full  (81): baryon 0 -- the determinant map onto the cube roots is onto, so no
                         three-fermion invariant exists at all; meson 1.
       Gamma_SU    (27): ** baryon 1, diquark 0, meson 1 -- every channel exactly SU(3)'s. **
       Gamma_rigid  (9): baryon 1, diquark 0, but meson 3 -- the meson is still lost, and
                         nothing should expect statistics to help there, a particle and an
                         antiparticle being neither identical nor antisymmetrised.
  5. ** AND THE DIQUARK IS A PREDICTION RATHER THAN A FIT: Lambda^2 K carries no invariant under
     any candidate, matching SU(3), and nothing in this construction asked for that. **  It is
     the one row that could have come out wrong without anyone having noticed in advance.
  6. ** SO WHICH GROUP SINGLE-VALUEDNESS IS DEMANDED UNDER IS NOT A CONVENTION TO BE PICKED --
     IT IS DETERMINED, by the one input that had been left out.  And the selected group is the
     unimodular one, which is exactly the group P14_the_wall_is_a_wall_of_a_hinge used to reach
     su(3), reached there by an entirely different argument (the smallest connected group
     containing the wall monodromies and the hinge cycle).  Two routes, no shared premises, one
     group. **

** A WORRY RAISED IN DRAFT AND THEN ANSWERED, RECORDED RATHER THAN DELETED.  Both the baryon
line and a lone constituent's line are one-dimensional, so both would seem to return to
themselves up to a PHASE -- and a state is a ray, so a phase is a Berry phase and not an
inconsistency, which would leave the confinement sentence resting on a field/state distinction
never argued for.  ** That is not the situation, and the error was comparing holonomies from two
different groups: gamma_A belongs to Gamma_full, which is not the selected group.  Under
Gamma_SU every element has determinant one, so the baryon line has TRIVIAL holonomy and the
baryon is invariant on the nose; while the invariants in K number ZERO and the action on K is
irreducible, so a lone constituent has no invariant line at all and comes back a DIFFERENT
VECTOR.  It is phase versus PERMUTATION, not phase versus phase -- so the escape hatch is not
needed and P14_route_or_point is stronger than it was written. **

** WHAT REMAINS IS NOT A DEFECT BUT A DESCRIPTION: all of this is HOLONOMY -- a flat bundle and
exact selection rules, with no interaction.  The geometry now supplies the full hadron selection
content of colour and still supplies no force. **

ORIGIN: computations/baryon_edge/L130_statistics_not_gauge.py -- built r2376 (c54.56); edit the
origin, not this copy."""
import sympy as sp
import itertools

print(__doc__.split("Run:")[0])

w = sp.exp(2 * sp.pi * sp.I / 3)


def W(k):
    return sp.simplify(sp.expand_complex(w**(k % 3)))


ID, CYC = (0, 1, 2), (1, 2, 0)


def mul(g, h):
    (gs, gd), (hs, hd) = g, h
    return (tuple(gs[hs[i]] for i in range(3)),
            tuple((hd[i] + gd[hs[i]]) % 3 for i in range(3)))


def sgn(s):
    return 1 if list(s) in ([0, 1, 2], [1, 2, 0], [2, 0, 1]) else -1


def det(g):
    return sgn(g[0]) * W(sum(g[1]))


def trace(g):
    s, d = g
    return sp.simplify(sp.expand_complex(sum((W(d[i]) for i in range(3) if s[i] == i),
                                             sp.Integer(0))))


def sq(g):
    return mul(g, g)


def close(gens):
    idt = (ID, (0, 0, 0))
    G, fr = {idt}, [idt]
    while fr:
        x = fr.pop()
        for g in gens:
            y = mul(x, g)
            if y not in G:
                G.add(y)
                fr.append(y)
    return sorted(G)


gam = [(ID, tuple(2 if i == c else 0 for i in range(3))) for c in range(3)]
Pgen = (CYC, (0, 0, 0))
lap = mul(mul(gam[0], gam[1]), gam[2])
G_full = close(gam + [Pgen])
G_su = close([mul(gam[0], (ID, tuple((-gam[1][1][i]) % 3 for i in range(3)))),
              mul(gam[1], (ID, tuple((-gam[2][1][i]) % 3 for i in range(3)))), Pgen])
G_rigid = close([Pgen, lap])

# =====================================================================
print("=" * 78)
print("PART 1 — THE QUESTION, AND THE CORPUS ALREADY HAS THE ANSWER")
print("=" * 78)
for s in [
 "`L-129b`: 'what is owed is an account of when two constituents at different vantages are the",
 "SAME PARTICLE -- a question about the OPERATOR whose zero-modes they are, not about the bundle.'",
 "",
 "** AND P14 ANSWERS IT IN ITS OWN CONSTRUCTION, WITHOUT HAVING BEEN ASKED. **  `prop:wall` binds",
 "ONE chiral zero-mode per wall, and it is one operator's zero-modes: the index P14 computes is",
 "'the index of A Dirac operator', returning 'one mode per wall per internal state'.  ** Three",
 "modes, ONE operator, ONE kernel. **",
 "",
 "⇒ ** SO THE THREE CONSTITUENTS ARE NOT THREE FIELDS.  They are three basis vectors of ONE",
 "   field's kernel, and excitations of one field are IDENTICAL PARTICLES by construction. **",
 "   That is not an extra postulate; it is what having a single operator MEANS.",
 "",
 "⌗ ** AND THE STEP THE CORPUS HAS NEVER TAKEN IS THE ORDINARY ONE: SECOND QUANTISATION. **",
 "   Everything from `L-96` onwards has treated the modes as classical labels and asked which",
 "   TENSORS of them are invariant.  ** A three-fermion state is not a general tensor.  It lives",
 "   in the EXTERIOR cube of the kernel, and most of the tensor cube is not a state at all. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — WHAT SECOND QUANTISATION DOES TO THE COUNT")
print("=" * 78)
print("  The one-particle space is the kernel, K = C^3 (one mode per wall).  Then:")
print()
print(f"     {'n particles':>12} {'space':>12} {'dimension':>10}")
for n, nm, d in [(1, "K", 3), (2, "Lambda^2 K", 3), (3, "Lambda^3 K", 1), (4, "Lambda^4 K", 0)]:
    print(f"     {n:>12} {nm:>12} {d:>10}")
assert sp.binomial(3, 3) == 1 and sp.binomial(3, 4) == 0
print()
for s in [
 "** Lambda^3 OF A THREE-DIMENSIONAL SPACE IS ONE-DIMENSIONAL, AND ITS GENERATOR IS THE TOTALLY",
 "   ANTISYMMETRIC COMBINATION -- WHICH IS epsilon. **  So:",
 "",
 "   * the 'all three constituents on ONE vantage' state is a-dagger_j a-dagger_j a-dagger_j |0>,",
 "     ** which is ZERO by the Pauli principle **, not merely non-invariant;",
 "   * the SYMMETRIC one-per-vantage sum ** is not in Lambda^3 at all **;",
 "   * epsilon is the ONLY three-particle state there is.",
 "",
 "⇒ ** SO `L-129`'s TWO SPURIOUS INVARIANTS ARE NOT STATES THAT A SYMMETRY FAILS TO FORBID.",
 "   THEY DO NOT EXIST. **  The over-counting was an artefact of counting tensors where the",
 "   physics counts fermionic states, and ** the corpus produced it by never second-quantising",
 "   a construction whose whole content is a Dirac kernel. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE TABLE REDONE WITH STATISTICS")
print("=" * 78)


def inv_dim(G, chi):
    v = sp.simplify(sp.expand_complex(sum((chi(g) for g in G), sp.Integer(0)) / len(G)))
    assert sp.im(v) == 0 and v == int(v), f"invariant count must be an integer: {v}"
    return int(v)


def chi_L3(g):
    return det(g)                                   # character of Lambda^3 is the determinant


def chi_L2(g):
    t, t2 = trace(g), trace(sq(g))
    return sp.expand_complex((t**2 - t2) / 2)       # character of Lambda^2


def chi_meson(g):
    t = trace(g)
    return sp.expand_complex(t * sp.conjugate(t))   # V (x) V*


def chi_T3(g):
    return sp.expand_complex(trace(g)**3)           # the OLD, tensor-cube count


print(f"  {'group':>14} {'|G|':>4} | {'baryon L^3 K':>13} {'diquark L^2 K':>14} "
      f"{'meson V(x)V*':>13} | {'old tensor cube':>16} {'all right?':>11}")
res = []
for nm, G in (("Gamma_full", G_full), ("Gamma_SU", G_su), ("Gamma_rigid", G_rigid)):
    b, dq, m, old = (inv_dim(G, chi_L3), inv_dim(G, chi_L2),
                     inv_dim(G, chi_meson), inv_dim(G, chi_T3))
    ok = (b == 1 and dq == 0 and m == 1)
    res.append((nm, b, dq, m, ok))
    print(f"  {nm:>14} {len(G):>4} | {b:>13} {dq:>14} {m:>13} | {old:>16} {str(ok):>11}")
print(f"  {'SU(3) itself':>14} {'inf':>4} | {1:>13} {0:>14} {1:>13} | {1:>16} {'True':>11}")
print()
winners = [r[0] for r in res if r[4]]
assert winners == ["Gamma_SU"], f"expected a unique survivor, got {winners}"
print(f"  ** EXACTLY ONE ROW IS RIGHT, AND IT IS {winners[0]} -- asserted, so the run fails")
print(f"     rather than prints if that changes. **")
print()
for s in [
 "   * ** Gamma_SU gives baryon 1, diquark 0, meson 1 -- every channel exactly SU(3)'s answer. **",
 "   * Gamma_full gives baryon ZERO: the determinant map onto the cube roots is onto, so the",
 "     determinants cancel in the average.  ** No three-fermion invariant exists at all. **",
 "   * Gamma_rigid gets the baryon but still ** loses the meson at 3 **, exactly as before:",
 "     statistics does not touch the particle-antiparticle channel, and nothing should expect it",
 "     to -- a particle and an antiparticle are not identical and are not antisymmetrised.",
 "",
 "⌗ ** AND THE DIQUARK IS A PREDICTION, NOT A FIT: Lambda^2 K carries NO invariant under any of",
 "   the three, matching SU(3), and the corpus never asked for that. **  It is the one row of",
 "   this table that could have come out wrong without anybody having noticed in advance.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND IT SELECTS THE CONFIGURATION SPACE")
print("=" * 78)
for s in [
 "`L-129b` asked the corpus to choose among three configuration groups and found that no choice",
 "worked.  ** With statistics included the choice is not free: the requirement that both",
 "channels come out right SELECTS Gamma_SU, uniquely. **",
 "",
 "⇒ ** SO THE ANSWER TO 'WHICH GROUP IS SINGLE-VALUEDNESS DEMANDED UNDER' IS NOT A CONVENTION",
 "   THE CORPUS PICKS.  IT IS DETERMINED, BY THE ONE INPUT THE CORPUS HAD LEFT OUT. **  And the",
 "   selected group is the unimodular one -- which is exactly the group `L-128` used to reach",
 "   su(3) in the first place, reached there by a different argument entirely (the smallest",
 "   connected group containing the wall monodromies and the hinge cycle).",
 "",
 "⌗ *Two routes, no shared premises, one group.  That is the strongest thing in this file.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — A WORRY I RAISED AND THEN COULD ANSWER, WHICH STRENGTHENS `L-74`")
print("=" * 78)
for s in [
 "⚠ ** THE WORRY, WRITTEN BEFORE IT WAS CHECKED: both the baryon line and a lone constituent's",
 "   line are ONE-DIMENSIONAL, so both would return to themselves UP TO A PHASE -- and in quantum",
 "   mechanics a state is a RAY, so a phase is a Berry phase and not an inconsistency.  If that",
 "   were the situation, `L-74`'s 'a lone coloured constituent is not single-valued' could not do",
 "   its work at the level of states, because the baryon would be in the same position, and the",
 "   whole confinement sentence would be resting on a field/state distinction never argued for. **",
 "",
 "⌗ ** IT IS NOT THE SITUATION, AND THE ERROR WAS MINE: I COMPARED HOLONOMIES FROM TWO DIFFERENT",
 "   GROUPS.  gamma_A is an element of Gamma_full, and Gamma_full is not the selected group. **",
 "   Under the group PART 3 selects, the two objects are not alike at all:",
]:
    print("  " + s)
print()


def inv_dim2(G, chi):
    v = sp.simplify(sp.expand_complex(sum((chi(g) for g in G), sp.Integer(0)) / len(G)))
    return int(v)


print(f"  Under the SELECTED Gamma_SU (|G| = {len(G_su)}):")
print()
print(f"     {'object':>34} {'lives in':>12} {'invariant dim':>14}")
for nm, sp_, chi in [("one lone constituent", "K", trace),
                     ("two constituents (diquark)", "Lambda^2 K", chi_L2),
                     ("three, one per vantage (baryon)", "Lambda^3 K", chi_L3),
                     ("constituent + antiparticle (meson)", "V (x) V*", chi_meson)]:
    print(f"  {nm:>34} {sp_:>12} {inv_dim2(G_su, chi):>14}")
alldet1 = all(sp.simplify(det(g) - 1) == 0 for g in G_su)
lone = inv_dim2(G_su, trace)
print()
print(f"     every element of Gamma_SU has det = 1: {alldet1}  ⇒ ** the baryon line Lambda^3 K")
print(f"     has TRIVIAL holonomy -- the baryon is invariant on the nose, not up to a phase. **")
print(f"     invariants in K: {lone}  ⇒ ** and Gamma_SU acts IRREDUCIBLY on K (`L-128`: its")
print(f"     commutant is the scalars), so a lone constituent has NO invariant line at all. **")
assert alldet1 and lone == 0
print()
for s in [
 "⇒ ** SO IT IS NOT PHASE VERSUS PHASE.  IT IS PHASE VERSUS PERMUTATION. **  A lone constituent",
 "   transported around does not come back as itself times a number -- ** it comes back as a",
 "   DIFFERENT VECTOR **, because the group mixes the three vantages irreducibly.  The baryon,",
 "   being the determinant line of an irreducible unimodular action, comes back as itself exactly.",
 "",
 "⌗ ** THAT REMOVES THE ESCAPE HATCH RATHER THAN USING IT: `L-74` does NOT need a field/state",
 "   distinction, because the lone constituent's failure is not a phase ambiguity that a ray",
 "   could absorb. **  The confinement sentence is stronger than it was written, and the worry",
 "   above is withdrawn -- ** recorded rather than deleted, because it was a real question and",
 "   the answer is a computation rather than a preference. **",
 "",
 "⌗ ⇒ ** AND THE SECTOR'S OPEN ITEM: not 'no curvature', not 'no antisymmetry', not 'which",
 "   group' -- all three answered across c54.54-56.  What remains is that all of this is",
 "   HOLONOMY: a flat bundle, exact selection rules, no interaction.  ** The geometry now gives",
 "   the full hadron selection content of colour and still gives no force, and after this file",
 "   that is a clean statement rather than a symptom of something unfinished. **",
]:
    print("  " + s)
