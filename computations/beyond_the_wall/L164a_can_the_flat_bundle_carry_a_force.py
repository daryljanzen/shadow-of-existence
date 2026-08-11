#!/usr/bin/env python3
"""
`L-164`, THE CONTINUOUS SIDE.  ** CAN THE MATTER SECTOR'S FLAT BUNDLE CARRY A FORCE? **

The corpus states the negative and does not prove it: *"the bundle above is flat, so the
construction supplies colour's exact selection rules and no force---it quantises and does not
couple"* (P14 `sec:intro`).  `L-125` closed the same question for the WINDING and ended by pointing
here: *"if it comes from this geometry at all it must come from the BUNDLE, not the LABEL."*  Nobody
followed the pointer.  This is the bundle.

** THE QUESTION, POSED SO IT CAN TERMINATE: the holonomy data fixes a flat connection up to moduli.
Is there anything in that moduli space, or reachable from it, that could be a COUPLING? **  `L-125`
supplies the criterion: a MODULUS labels which solution you are on; a COUPLING sits inside an
interaction and sets a strength.

  PART 1  ** THE MONODROMY DATA, REBUILT FROM THE CORPUS RATHER THAN QUOTED. **
  PART 2  ** THE HOLONOMY GROUP IS FINITE — and for a finite group $H^1(\\Gamma,\\mathrm{ad})=0$,
          computed here rather than cited. **
  PART 3  ** THE RELATIVE CHARACTER VARIETY: every deformation keeping the wall classes fixed. **
  PART 4  ** AND EVERY POINT OF IT IS FLAT.  The moduli are moduli in exactly `L-125`'s sense. **
  PART 5  ** SO CURVATURE NEEDS AN ACTION, AND AN ACTION NEEDS A COUPLING — and the substrate's one
          scale sits forty-one orders below the strong scale. **
  PART 6  The verdict, with its bound stated.

Run: python3 L164a_can_the_flat_bundle_carry_a_force.py      (numpy)
"""
import itertools

import numpy as np

print(__doc__.split("Run:")[0])
np.set_printoptions(precision=4, suppress=True)
W = np.exp(2j * np.pi / 3)

# =====================================================================
print("=" * 78)
print("PART 1 — THE MONODROMY DATA, REBUILT")
print("=" * 78)
print("  P14 `P14_mode_monodromy_at_the_wall`: near the wall r ~ l^(2/3), a CROSSING sends")
print("  r -> omega r, and the bound mode psi ~ r^(-lambda) picks up omega^(-lambda).  The three")
print("  vantages have disjoint support and 'crossing a wall branches only the vantage that owns")
print("  it', so on the fibre C^3 = span(v_A, v_B, v_C) the wall monodromies are DIAGONAL, each")
print("  moving one vantage.  Take the triality-one mode:")
gA = np.diag([W, 1, 1])
gB = np.diag([1, W, 1])
gC = np.diag([1, 1, W])
P = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)   # the hinge three-cycle
I3 = np.eye(3, dtype=complex)

print(f"     gamma_A = diag(w,1,1)   gamma_B = diag(1,w,1)   gamma_C = diag(1,1,w)")
print()
print("  ** and the corpus's four stated properties are REPRODUCED, not assumed: **")
checks = [
    ("a single wall monodromy has determinant omega",
     abs(np.linalg.det(gA) - W) < 1e-12),
    ("gamma_A gamma_B^-1 is a non-central diagonal of determinant one",
     abs(np.linalg.det(gA @ np.linalg.inv(gB)) - 1) < 1e-12
     and np.linalg.norm(gA @ np.linalg.inv(gB) - (gA @ np.linalg.inv(gB))[0, 0] * I3) > 1e-9),
    ("a full lap, the product of all three, is CENTRAL",
     np.linalg.norm(gA @ gB @ gC - W * I3) < 1e-12),
    ("the hinge three-cycle permutes the vantages and has order three",
     np.linalg.norm(np.linalg.matrix_power(P, 3) - I3) < 1e-12),
]
for s, ok in checks:
    print(f"     {'✔' if ok else '⛔'}  {s}: {ok}")
    assert ok, s
Q = gA @ np.linalg.inv(gC)                      # = diag(w,1,w^-1), the clock, up to a phase
kQP = [j for j in range(3) if np.linalg.norm(Q @ P - (W ** j) * P @ Q) < 1e-9]
print(f"\n  the clock from the RATIOS:  Q = gamma_A gamma_C^-1 = diag(w,1,w^-1)")
print(f"     Q P = w^{kQP[0]} P Q  ⇒ NON-COMMUTING, so <P,Q> is the order-27 Heisenberg group")
assert kQP and kQP[0] != 0

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE HOLONOMY GROUP IS FINITE")
print("=" * 78)
# ** THE GROUP IS ENUMERATED EXACTLY, NOT NUMERICALLY.  A first pass closed the group on rounded
# float matrices and returned |Gamma| = 1185 -- not a group order at all, and the assert caught it:
# products of cube roots of unity accumulate error and round apart.  Every element here is MONOMIAL
# with entries in {omega^k}, so it is carried as (permutation, exponent triple) over Z_3. **
def mono(sigma, e):
    """matrix with M[i, sigma[i]] = omega^{e[i]}"""
    M = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        M[i, sigma[i]] = W ** e[i]
    return M


def mul(x, y):
    """(sigma1,e1)*(sigma2,e2) as monomial matrices"""
    s1, e1 = x
    s2, e2 = y
    s = tuple(s2[s1[i]] for i in range(3))
    e = tuple((e1[i] + e2[s1[i]]) % 3 for i in range(3))
    return (s, e)


ID = ((0, 1, 2), (0, 0, 0))
GENS = [((0, 1, 2), (1, 0, 0)),          # gamma_A = diag(w,1,1)
        ((0, 1, 2), (0, 1, 0)),          # gamma_B
        ((0, 1, 2), (0, 0, 1)),          # gamma_C
        ((2, 0, 1), (0, 0, 0))]          # the hinge three-cycle
for g, Mref in zip(GENS, [gA, gB, gC, None]):
    if Mref is not None:
        assert np.linalg.norm(mono(*g) - Mref) < 1e-12, "the exact carrier must reproduce the matrix"
seen, frontier = {ID}, [ID]
while frontier:
    nxt = []
    for m in frontier:
        for g in GENS:
            p = mul(m, g)
            if p not in seen:
                seen.add(p)
                nxt.append(p)
    frontier = nxt
ELT = sorted(seen)
GRP = [mono(*g) for g in ELT]
print(f"  the group generated by the three wall monodromies and the hinge cycle:")
print(f"     ** |Gamma| = {len(GRP)} , FINITE **   "
      f"(the diagonal $\\mathbb{{Z}}_3^3$ extended by the hinge $\\mathbb{{Z}}_3$)")
assert len(GRP) == 81, len(GRP)

# ---- H^0 and H^1 of Gamma with coefficients in the adjoint --------------------------------
# su(3) as a REAL 8-dimensional space; ad acts by X -> g X g^{-1}
GM = [np.array(m, dtype=complex) for m in [
    [[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]],
    [[1, 0, 0], [0, -1, 0], [0, 0, 0]], [[0, 0, 1], [0, 0, 0], [1, 0, 0]],
    [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]],
    np.diag([1, 1, -2]) / np.sqrt(3)]]
BAS = [1j * g / 2 for g in GM]                       # a real basis of su(3)


def vec(X):
    """coordinates of X in BAS -- real, 8 numbers"""
    return np.array([np.real(np.trace(X.conj().T @ b)) / np.real(np.trace(b.conj().T @ b))
                     for b in BAS])


def Ad(g):
    return np.column_stack([vec(g @ b @ np.linalg.inv(g)) for b in BAS])


for b in BAS:                                        # the basis is orthogonal, so vec() is exact
    assert np.linalg.norm(sum(vec(b)[i] * BAS[i] for i in range(8)) - b) < 1e-9
print(f"  su(3) carried as a real 8-dimensional space; Ad(g) as real 8x8 matrices.")

# H^0 = invariants of the whole group
Amats = [Ad(g) for g in GRP]
Hzero = np.vstack([A - np.eye(8) for A in Amats])
dim_H0 = 8 - np.linalg.matrix_rank(Hzero, tol=1e-8)
print(f"     dim H^0(Gamma, ad) = {dim_H0}   "
      f"(the representation is irreducible, so its centraliser is the scalars: 0 in su(3))")
assert dim_H0 == 0

# H^1: cochains c: Gamma -> su(3) with c(gh) = c(g) + Ad(g) c(h).
# ** rows for (g in GENERATORS, h in Gamma) suffice: a cocycle is determined on generators and the
# remaining pairs are consequences.  All indices come from the EXACT carrier. **
idx = {e: i for i, e in enumerate(ELT)}
rows = []
for g in GENS:
    ig = idx[g]
    Ag = Ad(mono(*g))
    for h in ELT:
        jh, kgh = idx[h], idx[mul(g, h)]
        R = np.zeros((8, 8 * len(GRP)))
        R[:, 8 * kgh:8 * kgh + 8] += np.eye(8)
        R[:, 8 * ig:8 * ig + 8] -= np.eye(8)
        R[:, 8 * jh:8 * jh + 8] -= Ag
        rows.append(R)
M = np.vstack(rows)
dim_Z1 = 8 * len(GRP) - np.linalg.matrix_rank(M, tol=1e-7)
dim_B1 = 8 - dim_H0
dim_H1 = dim_Z1 - dim_B1
print(f"     dim Z^1 = {dim_Z1} , dim B^1 = {dim_B1}  ⇒  ** dim H^1(Gamma, ad) = {dim_H1} **")
assert dim_H1 == 0
print()
for s in [
 "⇒⇒ ** THE REPRESENTATION IS RIGID AS A REPRESENTATION OF ITS OWN HOLONOMY GROUP. **  *And the",
 "   reason is a theorem rather than an accident of these matrices: $\\Gamma$ is FINITE, so",
 "   averaging over it splits every extension — $H^1(\\Gamma,V)=0$ for any $\\Gamma$-module $V$ in",
 "   characteristic zero.  **The construction's holonomy is finite because it is BRANCHING, and a",
 "   branch structure has finitely many sheets.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE RELATIVE CHARACTER VARIETY")
print("=" * 78)
print("  Deformations of the FUNDAMENTAL GROUP's representation need not factor through Gamma.")
print("  The base is the wall-punctured throat: three punctures, product of the loops central.")
print("  Deform A -> exp(a)A, B -> exp(b)B, C -> exp(c)C keeping each conjugacy CLASS fixed")
print("  (a in Im(1-Ad_A), etc.) and the product fixed (a + Ad_A b + Ad_AB c = 0).")
AdA, AdB, AdC = Ad(gA), Ad(gB), Ad(gC)
AdAB = Ad(gA @ gB)
E = np.eye(8)
# parametrise a = (1-Ad_A)X, b = (1-Ad_B)Y, c = (1-Ad_C)Z  and impose the product constraint
Kmat = np.hstack([(E - AdA), AdA @ (E - AdB), AdAB @ (E - AdC)])
dim_sol = 24 - np.linalg.matrix_rank(Kmat, tol=1e-8)
# trivial deformations: simultaneous conjugation V -> ((1-Ad_A)V, (1-Ad_B)V, (1-Ad_C)V)
Triv = np.vstack([(E - AdA), (E - AdB), (E - AdC)])
dim_triv = np.linalg.matrix_rank(Triv, tol=1e-8)
# but (X,Y,Z) -> a,b,c is not injective: kernel of X -> (1-Ad_A)X is the centraliser of A
kerA = 8 - np.linalg.matrix_rank(E - AdA, tol=1e-8)
kerB = 8 - np.linalg.matrix_rank(E - AdB, tol=1e-8)
kerC = 8 - np.linalg.matrix_rank(E - AdC, tol=1e-8)
print(f"\n  {'object':>52} {'dim':>5}")
for nm, v in [("tangent to the class of a wall monodromy", 8 - kerA),
              ("(so each wall class has dimension)", 8 - kerA),
              ("solutions (X,Y,Z) of the product constraint", dim_sol),
              ("of which map to zero deformation", kerA + kerB + kerC),
              ("trivial (simultaneous conjugation)", dim_triv)]:
    print(f"  {nm:>52} {v:>5}")
dim_M = dim_sol - (kerA + kerB + kerC) - dim_triv
print(f"\n  ** dim (moduli of flat connections, wall classes fixed) = {dim_M} **")
print(f"     each wall class is SUBREGULAR — gamma_A = diag(w,1,1) has a repeated eigenvalue, so")
print(f"     its class is SU(3)/U(2), of dimension {8 - kerA}, not the regular {8 - 2}.")
assert dim_M == 0, dim_M
print()
for s in [
 "⇒⇒ ** ZERO.  THE FLAT CONNECTION IS ISOLATED: there is no continuous parameter in it at all. **",
 "   *And the reason is the eigenvalue structure, which the physics fixed and nobody chose: a wall",
 "   branches ONE vantage and leaves the other two alone, so its monodromy has a repeated",
 "   eigenvalue and its conjugacy class is small.  **Three small classes cannot span a positive-",
 "   dimensional moduli space on a three-punctured base.***",
 "",
 "⌗ *Had the walls acted with three distinct eigenvalues the classes would be regular, of",
 "   dimension six, and the count would give $3\\times6-16=2$ — a two-parameter family.  **The",
 "   disjointness of the vantages' supports is what removes it.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND EVERY POINT OF IT IS FLAT")
print("=" * 78)
for s in [
 "** THE MODULI SPACE OF FLAT CONNECTIONS CONSISTS OF FLAT CONNECTIONS.  This is a tautology and",
 "   it is the decisive step, because it means the question 'is there a modulus?' was never the",
 "   question. **  *Even a positive-dimensional moduli space would carry $F\\equiv0$ at every",
 "   point: moving in it changes WHICH flat bundle one has, not whether there is a field strength.*",
 "",
 "⇒ ** SO `L-125`'s DISTINCTION APPLIES WITH NOTHING LEFT OVER.  A point of the moduli space is a",
 "   MODULUS in exactly its sense — it labels which solution — and the space is a point anyway. **",
 "",
 "⌗⌗ *This is why PART 3's answer being zero is a bonus rather than the argument.  **The argument",
 "   would go through at any dimension**: to get curvature one must LEAVE the flat locus, and no",
 "   holonomy datum can take you off it, because holonomy is precisely the invariant a flat",
 "   connection has.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — SO CURVATURE NEEDS AN ACTION, AND AN ACTION NEEDS A COUPLING")
print("=" * 78)
print("  Leaving the flat locus means SELECTING a non-flat connection, which means a variational")
print("  principle.  A Yang-Mills term (1/2g^2) tr F^2 in four dimensions has a DIMENSIONLESS g.")
print("  The substrate supplies exactly one invariant, the length alpha = sqrt(3/Lambda).  A")
print("  dimensionless number cannot be built from one length, so g is either free — which the")
print("  corpus's own admissibility criterion rejects, a structure carrying an unforced parameter")
print("  answering 'what is the world?' with a family — or it comes from a SECOND scale by")
print("  dimensional transmutation.  ** That is checkable, and it is the only route left. **")
LAM = 1.1056e-52                 # m^-2, the observed cosmological constant
alpha = np.sqrt(3.0 / LAM)
HBARC = 1.97327e-7               # eV m
E_alpha = HBARC / alpha
LQCD = 2.1e8                     # eV, ~210 MeV
print(f"\n  {'quantity':>44} {'value':>18}")
for nm, v, u in [("alpha = sqrt(3/Lambda)", alpha, "m"),
                 ("the substrate's one energy, hbar c / alpha", E_alpha, "eV"),
                 ("the strong scale, Lambda_QCD", LQCD, "eV")]:
    print(f"  {nm:>44} {v:>18.4g} {u}")
orders = np.log10(LQCD / E_alpha)
print(f"\n  ** Lambda_QCD / (hbar c / alpha) = 10^{orders:.1f} — FORTY-ONE ORDERS OF MAGNITUDE. **")
assert 40 < orders < 42
print()
for s in [
 "⇒⇒ ** AND THE DIRECTION IS WRONG, NOT ONLY THE SIZE. **  *Dimensional transmutation runs a",
 "   coupling DOWN from an ultraviolet scale to produce an infrared one.  $\\alpha$ is the",
 "   infrared end of the whole construction — the largest length there is.  **To produce",
 "   $\\Lambda_{\\rm QCD}$ from it one would have to run upward through forty-one decades, and the",
 "   value of $g$ at $1/\\alpha$ that did so would be a number tuned to forty-one decades: an",
 "   unforced parameter wearing a geometric costume.***",
 "",
 "⌗ *Stated at its honest weight: this does not prove no theory relates the two scales.  It shows",
 "   THE SUBSTRATE DOES NOT, because relating them needs a second input and the substrate's whole",
 "   claim is that it has one.*",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 6 — THE VERDICT")
print("=" * 78)
print(f"  {'step':>56} {'result':>16}")
for nm, v in [
    ("the holonomy group", f"FINITE ({len(GRP)})"),
    ("H^1 of it with adjoint coefficients", f"{dim_H1}"),
    ("moduli of flat connections, wall classes fixed", f"{dim_M}"),
    ("field strength at every point of that moduli space", "ZERO"),
    ("a coupling from the substrate's one scale", "41 decades short"),
]:
    print(f"  {nm:>56} {v:>16}")
print()
for s in [
 "✔✔ ** THE ANSWER IS NO, AND IT IS A STRUCTURAL NO RATHER THAN A GAP. **  *The construction's",
 "   gauge content is HOLONOMY, holonomy is the complete invariant of a FLAT connection, and a flat",
 "   connection has no field strength by definition.  **The bundle cannot supply a force for the",
 "   same reason the winding could not supply a charge strength (`L-125`): a topological datum",
 "   quantises and does not measure.***",
 "",
 "⇒ ** WHAT THIS BUYS, WHICH IS MORE THAN A CLOSED DOOR: the corpus can now say WHY its matter",
 "   sector stops where it does, in one sentence with a proof behind it. **  *Not 'the coupling is",
 "   not built yet' — which invites the reader to expect it next revision — but **'the coupling is",
 "   not the kind of thing this construction produces, and here is the invariant that says so'.***",
 "",
 "⚠ ** AND THE BOUND, STATED SO IT IS NOT OVER-READ: this settles that the FLAT BUNDLE cannot",
 "   carry a force.  It does not settle that no other structure in the substrate can. **  *The",
 "   isometry route is separately walled ($\\su(3)\\not\\subset\\so(5,1)$, four ways).  What is NOT",
 "   excluded here is a mechanism that is neither holonomy nor isometry — and the honest position",
 "   is that the corpus has never named one.*",
 "",
 "⌗ **THE ONE THING THAT WOULD OVERTURN THIS: a second scale forced by the substrate.**  *That is",
 "   a sharp falsifier and it is the same one `L-125` left: the construction has one invariant, and",
 "   a force needs two.  **`L-166` — whether the empirical Standard Model motivates the compact",
 "   face — is the place a second scale would have to come from, and it is now the only live route",
 "   from this row.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 7 — THE FALSIFIER, RUN IN THE SAME REVISION IT WAS NAMED")
print("=" * 78)
# ** THE FALSIFIER: a SECOND dimensionless invariant forced by the substrate.  If one exists the
# verdict above is overturned, so it is run here rather than left as a sentence. **
print("  A coupling is dimensionless.  The substrate supplies the length alpha.  Any second")
print("  dimensionful quantity in the construction would supply a ratio -- so the question is")
print("  whether the construction has one, and whether it is an INVARIANT or a MODULUS.")
print()
print(f"  {'candidate':>34} {'dimensionless partner':>24} {'invariant of the substrate?':>30}")
CAND = [
    ("alpha = sqrt(3/Lambda)", "-- (the unit itself)", "YES, the one invariant"),
    ("M, the progenitor mass", "2M/alpha", "NO -- labels which member"),
    ("r_0, the vantage offset", "r_0/alpha", "NO -- labels which vantage"),
    ("the Nariai mass alpha/(3 sqrt 3)", "2/(3 sqrt 3) = 0.3849", "forced, but of ONE member"),
]
for a, b, c in CAND:
    print(f"  {a:>34} {b:>24} {c:>30}")
print()
NAR = 2.0 / (3.0 * np.sqrt(3.0))
print(f"  ** THE ONE FORCED DIMENSIONLESS NUMBER THE CONSTRUCTION CARRIES IS {NAR:.6f}, at Nariai,")
print(f"     and it must be REFUSED as a coupling for a reason that is structural and not a taste: **")
for s in [
 "   ⌗ *`C·1` established that the only alpha-BUILT mass in the family is the Nariai member",
 "     $M=\\alpha/3\\sqrt3$, so $2M/\\alpha=2/3\\sqrt3$ there and nowhere else.*",
 "   ⛔ ** BUT THE MATTER SECTOR IS NOT BUILT ON NARIAI.  It is built on the equatorial section of",
 "      the GENERAL member, whose $2M/\\alpha$ runs over the whole family. **  *A quantity that",
 "      takes a different value on every solution is a MODULUS by `L-125`'s own criterion -- it",
 "      labels which solution you are on -- and a coupling that differed from one black hole to the",
 "      next would not be a coupling.*",
 "   ⚠⚠ ** AND THE TEMPTATION IS NAMED AND REFUSED IN THE SAME BREATH, because this corpus has a",
 "      recorded history with exactly this move: ** *$0.3849$ is a number, and with a scale and a",
 "      normalisation neither of which the construction supplies one could land it near a coupling.",
 "      **That is numerology, and the base rate says so: a match earns nothing without a stated",
 "      scale, a stated normalisation, and a reason the two objects are the same object.***",
]:
    print(s)
assert abs(NAR - 0.38490017945975) < 1e-12
print()
print("  ⇒⇒ ** THE FALSIFIER DOES NOT FIRE.  Every dimensionless number the construction carries is")
print("     a modulus, and the single forced one belongs to a member the matter sector is not built")
print("     on.  The substrate has one invariant, and a force needs two. **")
