"""
DRAFT_P12_the_bianchi_stratum_is_six_of_nine.py -- P12 sec:strata / P8 K9 / P9 thm:bound:
** P12's ISOTROPY-3 STRATUM IS LABELLED "Bianchi".  EXACTLY SIX OF THE NINE BIANCHI SYMMETRY
   ALGEBRAS EMBED IN so(4,1).  AND THE SENTENCE "the isotropy dimensions are the Killing-vector
   counts" IS THE ONE THAT NOTICES THE DIFFERENCE. **

This is F05 (batch 1) landing at a SECOND site.  F05 established, against so(4,1) built
explicitly, which three-dimensional real Lie algebras embed:

    EMBED     : R^3 (I) · aff(1,R)+R · R (x)_I R^2 (V) · R (x)_{lambda I + rot} R^2 (VII_h, all h)
                · sl(2,R) (VIII) · su(2) (IX)
    DO NOT    : Heisenberg (II) · Jordan(lambda,lambda) (IV) · diag(1,h) for every real ratio
                outside {0,1} -- VI_0 among them

That list is COMPLETE for three-dimensional real Lie algebras: up to isomorphism they are the
abelian one, the Heisenberg one, the one-parameter family R (x)_A R^2 indexed by A's Jordan data
up to scale, and the two simple ones sl(2,R) and su(2).  F05's spectral lemma covers the whole
R (x)_A R^2 family in one statement, so nothing is left untested.

--------------------------------------------------------------------------------------------
WHAT P12 SAYS
--------------------------------------------------------------------------------------------
  "the cut-fixing isotropy drops, and its strata are the range/Petrov classes: Type O (de Sitter,
   isotropy so(4,1), dimension ten), Type D (Schwarzschild-de Sitter R_t x SO(3), dimension four;
   Kerr-de Sitter, dimension two), ** Type I (Bianchi, dimension three; ** Zipoy-Voorhees,
   dimension two), and the wall (Type N, isotropy zero)."

  and, later in the same paragraph:

  ** "The isotropy dimensions are the Killing-vector counts the construction establishes." **

--------------------------------------------------------------------------------------------
① THE STRATUM IS SIX OF NINE
--------------------------------------------------------------------------------------------
The isotropy of a cut is the subgroup of the substrate's isometries that FIXES it -- a subgroup of
so(4,1) by P9 thm:bound.  A Bianchi cut's isotropy is its three-dimensional symmetry algebra
realised there.  ** Three of the nine cannot be so realised, so the stratum P12 labels "Bianchi,
dimension three" is populated by six Bianchi types and not by nine. **

--------------------------------------------------------------------------------------------
② AND THE KILLING-VECTOR IDENTIFICATION IS WHERE IT BITES
--------------------------------------------------------------------------------------------
A Bianchi II geometry has ** three Killing vectors ** and matter that is perfectly homogeneous.
Its isotropy in the substrate is at most ** two **, because the Heisenberg algebra is not in
so(4,1) while its abelian R^2 subalgebras are.  So for that geometry

    ** isotropy dimension  <  Killing-vector count **

and P12's identification of the two, true on every stratum it tabulates, is not general.

** AND THE CORPUS ALREADY CARRIES THE REASON, one paper over. **  P8's `K9_isotropy_obstruction`
kills its own author's proposed general argument and gets the right statement out of it:

    Isotropy(c) ~= { phi in Isom(Psi(c)) : phi preserves the second fundamental form },

"a SUBGROUP of Isom(Psi(c)), and may be PROPER", holding with equality "at exactly the strata
whose symmetry is large enough to fix the extrinsic data too -- and P12 tabulates precisely the
high-symmetry strata."  ** K9 says the identification can fail and says where; this says which
geometries, and counts them. **  K9 even names the place: "the UNTABULATED ones are the
LOW-SYMMETRY ones: the Type-I classes, the wall."  Type I is exactly the Bianchi stratum.

--------------------------------------------------------------------------------------------
③ A CONDITIONAL PREDICTION, worth stating because it is checkable
--------------------------------------------------------------------------------------------
F05 left one question open and does not close it here either: whether a Bianchi II geometry is a
cut at all, via a G_2 sweep rather than its own G_3.  ** IF IT IS, it enters this filtration at
isotropy dimension TWO -- beside Kerr-de Sitter and Zipoy-Voorhees -- while carrying three Killing
vectors. **  That would be the first entry in P12's table whose stratum is lower than its
symmetry, and it is the concrete form of K9's abstract gap.

--------------------------------------------------------------------------------------------
④ AND ONE SMALL CLOSURE ON THE {6,7,10} ENUMERATION
--------------------------------------------------------------------------------------------
`K8_orbit_type_filtration` establishes the admissible symmetric-pair dimensions of so(5,1) as
{6,7,10} by enumerating so(p',q') + so(p'',q'') with p'+p''=5, q'+q''=1.  ** That is one family of
involutions. **  The other family available to an orthogonal algebra is the complex-structure
(u-type) involution, so(2m) -> u(m) and its real forms, which would give a symmetric subalgebra
u(a,b) of dimension (a+b)^2 -- for so(5,1) that would be u(2,1), dimension NINE, and would break
the {6,7,10} statement.

** It does not arise, and the reason is elementary: **  a u-type involution needs an orthogonal
complex structure J on the defining representation, and J-invariance of the metric forces the
signature to be (2a, 2b).  ** The signature here is (5,1) and 5 is odd, so no such J exists. **
So the enumeration is complete and {6,7,10} stands -- and the receipt's argument, which does not
mention the u-type family, is closed rather than corrected.

--------------------------------------------------------------------------------------------
HONEST WEIGHT
--------------------------------------------------------------------------------------------
** No new computation beyond F05's, which is re-run below rather than quoted. **  What is added is
that F05 lands on P12 as well as on P9, that it makes K9's abstract obstruction concrete and
countable, and that the three papers say one thing between them that none says alone.

STATED FOR REVERSAL.  No closure on any registered item.  If the Bianchi stratum's membership is
recorded somewhere I did not find, strike this: searched `bianchi` (14 hits, every one type I),
`isotropy`, `Killing-vector count`, `stratum` across corpus/, receipts/, computations/ and
storyboard_receipts/.
"""
import numpy as np
import itertools

print(__doc__)

ETA = np.diag([-1.0, 1, 1, 1, 1])


def _basis():
    B = []
    for i in range(5):
        for j in range(i + 1, 5):
            S = np.zeros((5, 5)); S[i, j] = 1.0; S[j, i] = -1.0
            B.append(np.linalg.inv(ETA) @ S)
    return np.array(B)


B = _basis()
G = np.array([b.flatten() for b in B]).T
coords = lambda A: np.linalg.lstsq(G, A.flatten(), rcond=None)[0]
mat = lambda v: np.tensordot(np.asarray(v, float), B, axes=(0, 0))
br = lambda X, Y: X @ Y - Y @ X
inalg = lambda A: np.allclose(A.T @ ETA + ETA @ A, 0, atol=1e-10)


def M(a, b):
    S = np.zeros((5, 5)); S[a, b] = 1.0; S[b, a] = -1.0
    return np.linalg.inv(ETA) @ S


H = M(0, 4)
Nn = [M(i, 0) + M(i, 4) for i in (1, 2, 3)]
Nb = [M(i, 0) - M(i, 4) for i in (1, 2, 3)]
rot23 = M(2, 3)


def ad(X):
    A = np.zeros((10, 10))
    for k in range(10):
        A[:, k] = coords(br(X, B[k]))
    return A


# ============================================================================
print("=" * 78)
print("PART 1 — F05's RESULT, RE-RUN (not quoted)")
print("=" * 78)
rng = np.random.default_rng(20260812)
maxnz = 0
for _ in range(2000):
    ev = np.linalg.eigvals(ad(mat(rng.standard_normal(10))))
    real = sorted(e.real for e in ev if abs(e.imag) < 1e-8)
    d = []
    for r in real:
        if not d or abs(r - d[-1]) > 1e-6:
            d.append(r)
    maxnz = max(maxnz, len([x for x in d if abs(x) > 1e-6]))
print(f"  spectral lemma: most distinct nonzero REAL eigenvalues of ad_X over 2000 draws = {maxnz}")
assert maxnz <= 2
print("     -> a real eigenvalue ratio of A = ad_X|_u can only be 0, +1 or -1")

worst = min(np.linalg.norm(br(sum(v[i] * Nn[i] for i in range(3)),
                              sum(w[i] * Nb[i] for i in range(3))))
            / (np.linalg.norm(sum(v[i] * Nn[i] for i in range(3)))
               * np.linalg.norm(sum(w[i] * Nb[i] for i in range(3))))
            for v, w in ((rng.standard_normal(3), rng.standard_normal(3)) for _ in range(5000)))
print(f"  ratio -1 needs an abelian n/n-bar pair; smallest normalised bracket over 5000 = {worst:.3e}")
assert worst > 1e-3

Z = Nn[0]
adZ = ad(Z)
cen = np.linalg.svd(adZ)[2][np.linalg.matrix_rank(adZ, tol=1e-9):]
CB = [mat(c) for c in cen]
D = np.array([coords(br(CB[i], CB[j])) for i in range(len(CB)) for j in range(i + 1, len(CB))])
rk = np.linalg.matrix_rank(D, tol=1e-9)
inside = np.linalg.matrix_rank(np.vstack([D, coords(Z)]), tol=1e-9) == rk
print(f"  Heisenberg: dim C(Z)={cen.shape[0]}, dim [C,C]={rk}, Z in [C,C]? {inside}")
assert not inside
kerH = np.linalg.svd(ad(H))[2][np.linalg.matrix_rank(ad(H), tol=1e-9):]
nilp = sum(1 for _ in range(5000)
           if np.linalg.norm(np.linalg.matrix_power(mat(rng.standard_normal(kerH.shape[0]) @ kerH), 5)) < 1e-9)
print(f"  Jordan(l,l): nonzero nilpotents in ker(ad_H) over 5000 draws = {nilp}")
assert nilp == 0

# ============================================================================
print()
print("=" * 78)
print("PART 2 — THE NINE BIANCHI SYMMETRY ALGEBRAS AGAINST so(4,1)")
print("=" * 78)


def check(gens, rel):
    return (all(np.allclose(x, 0, atol=1e-10) for x in rel(gens))
            and np.linalg.matrix_rank(np.array([g.flatten() for g in gens]), tol=1e-9) == len(gens)
            and all(inalg(g) for g in gens))


s = 1.0 if np.allclose(br(rot23, Nn[1]), Nn[2]) else -1.0
POS = [
    ("I", "R^3 (abelian)", [Nn[0], Nn[1], Nn[2]],
     lambda E: [br(E[i], E[j]) for i in range(3) for j in range(3)]),
    ("III*", "aff(1,R) + R  [A ~ diag(1,0)]", [H, Nn[0], rot23],
     lambda E: [br(E[0], E[1]) - E[1], br(E[0], E[2]), br(E[1], E[2])]),
    ("V", "R (x)_I R^2", [H, Nn[0], Nn[1]],
     lambda E: [br(E[0], E[1]) - E[1], br(E[0], E[2]) - E[2], br(E[1], E[2])]),
    ("VII_h", "R (x)_{lI+rot} R^2, h=1.0", [0.5 * H + rot23, Nn[1], Nn[2]],
     lambda E: [br(E[0], E[1]) - (0.5 * E[1] + s * E[2]),
                br(E[0], E[2]) - (0.5 * E[2] - s * E[1]), br(E[1], E[2])]),
    ("VIII", "sl(2,R) = so(2,1)", [M(0, 1), M(1, 4) + M(0, 4), M(1, 4) - M(0, 4)],
     lambda E: [br(E[0], E[1]) - E[1], br(E[0], E[2]) + E[2], br(E[1], E[2]) + 2 * E[0]]),
]
print(f"  {'Bianchi':>8} {'algebra':<34} {'embeds in so(4,1)?':>20}")
for name, desc, gens, rel in POS:
    ok = check(gens, rel)
    print(f"  {name:>8} {desc:<34} {str(ok):>20}")
    assert ok
_m = [M(1, 2), M(1, 3), M(2, 3)]
eps = [[[float(np.round(np.linalg.lstsq(np.array([g.flatten() for g in _m]).T,
                                        br(_m[i], _m[j]).flatten(), rcond=None)[0][k], 6))
         for k in range(3)] for j in range(3)] for i in range(3)]
isso3 = all(abs(abs(eps[i][j][k]) - (1.0 if len({i, j, k}) == 3 else 0.0)) < 1e-9
            for i in range(3) for j in range(3) for k in range(3))
print(f"  {'IX':>8} {'su(2) = so(3)':<34} {str(isso3):>20}")
assert isso3
print()
for name, why in (("II", "Heisenberg -- Z not in [C(Z),C(Z)]  (PART 1)"),
                  ("IV", "Jordan(l,l) -- no nilpotent commutes with cH  (PART 1)"),
                  ("VI_h", "diag(1,h), real ratio outside {0,1} -- spectral lemma  (PART 1)")):
    print(f"  {name:>8} {'':<34} {'DOES NOT EMBED':>20}   {why}")
print()
print("  ** SIX OF NINE.  The three-dimensional isotropy stratum P12 labels 'Bianchi' is six")
print("     Bianchi types, not the classification. **")
print("  ⚠ *label caution: the class-B Bianchi numbering differs between references; the result")
print("     is stated by the Jordan data of A and the labels are a reading of it (as in F05).*")

# ============================================================================
print()
print("=" * 78)
print("PART 3 — WHERE THE KILLING-VECTOR IDENTIFICATION PARTS FROM THE ISOTROPY")
print("=" * 78)
print(f"  {'stratum (P12)':<34} {'isotropy dim':>13} {'Killing vectors':>16} {'equal?':>8}")
for nm, iso, kv in (("Type O  (de Sitter)", 10, 10), ("Nariai  SO(2,1)xSO(3)", 6, 6),
                    ("Type D  SdS  R_t x SO(3)", 4, 4), ("Type I  Bianchi (the six)", 3, 3),
                    ("Type D  Kerr-dS / Zipoy", 2, 2), ("wall    Type N", 0, 0)):
    print(f"  {nm:<34} {iso:>13} {kv:>16} {'yes':>8}")
print(f"  {'Bianchi II / IV / VI_h':<34} {'<= 2':>13} {3:>16} {'** NO **':>8}")
print()
for line in [
 "** P12: 'The isotropy dimensions are the Killing-vector counts the construction establishes.' **",
 "   True on every stratum the paper tabulates.  Not general -- and P8's K9 already says why:",
 "   Isotropy(c) is the subgroup of Isom(Psi(c)) preserving the SECOND FUNDAMENTAL FORM, equal",
 "   only 'at the strata whose symmetry is large enough to fix the extrinsic data too'.",
 "",
 "   ⇒ ** K9 says the identification can fail and where.  This says WHICH geometries, and counts",
 "     them: exactly the three Bianchi types whose algebra is not in so(4,1). **",
 "",
 "⌗ *K9's own sentence names the place: 'the UNTABULATED ones are the LOW-SYMMETRY ones: the",
 "   Type-I classes, the wall.'  Type I IS the Bianchi stratum.*",
]:
    print("  " + line)

# ============================================================================
print()
print("=" * 78)
print("PART 4 — THE {6,7,10} ENUMERATION, CLOSED")
print("=" * 78)
print("  K8_orbit_type_filtration enumerates so(p',q') + so(p'',q''), p'+p''=5, q'+q''=1:")
dims = {}
for p1 in range(6):
    for q1 in range(2):
        p2, q2 = 5 - p1, 1 - q1
        d = p1 * (p1 + q1 - 1) // 2 + q1 * (p1 + q1 - 1) // 2
        d1 = (p1 + q1) * (p1 + q1 - 1) // 2
        d2 = (p2 + q2) * (p2 + q2 - 1) // 2
        if d1 + d2 == 15:
            continue
        dims.setdefault(d1 + d2, []).append(f"so({p1},{q1})+so({p2},{q2})")
for d in sorted(dims):
    print(f"     dim h = {d:>2} :  {' | '.join(dims[d])}")
print(f"\n  admissible dimensions from this family: {sorted(dims)}   -> {{6,7,10}} confirmed")
assert sorted(dims) == [6, 7, 10]
print()
for line in [
 "** But that is ONE family of involutions. **  An orthogonal algebra also admits the",
 "complex-structure (u-type) involution, which for so(5,1) would give u(2,1) -- ** dimension NINE",
 "-- and would break {6,7,10}. **",
 "",
 "It does not arise, elementarily: a u-type involution needs an orthogonal complex structure J on",
 "the defining representation, and J-invariance of the metric forces the signature to be (2a,2b).",
 "** The signature is (5,1) and 5 is odd, so no such J exists. **",
 "",
 "⇒ ** the enumeration is complete and {6,7,10} stands -- closed, not corrected. **",
]:
    print("  " + line)

print()
print("=" * 78)
print("NOT CLAIMED")
print("=" * 78)
for line in [
 "· No new computation beyond F05's, which is re-run above rather than quoted.",
 "· No claim that Bianchi II/IV/VI_h are outside the range -- F05 is explicit that a G_2 sweep",
 "  may still reach them, and cor:radiation puts the two-Killing-vector stratum inside.  PART 3's",
 "  entry is CONDITIONAL on that and is marked so.",
 "· No claim that P12's tabulated strata are wrong.  Every row of them is right.",
 "· Nothing about the physical universe: the sky is isotropic to 3e-6 (P4).",
 "· No closure on any registered item.",
]:
    print("  " + line)
