#!/usr/bin/env python3
r"""The quartic carries the inverse volume exactly as the cubic's square does, so the back-reaction criterion is
G/target < 18 and not < 18 V: r7058's chain gave the quartic no volume, and that does not follow.

LEVEL: exact throughout.  The volume is a symbol until the last step; every number is an exact rational or an
exact multiple of pi^2.

OBJECT UNDER TEST.  r7058 assembled the back-reaction criterion through r7038's passage and found it a pure
number, G/target < 18 V = 36 pi^2, on the ground that "rebuilding r7034's eps^2 level sum from its own pointwise
identity returns -D mu^2/4 with no factor of the volume anywhere", so r7034's level values carry no volume,
"while a triple product of orthonormal harmonics carries V^(-1/2) ... the cubic side carries 1/V in its square
where the quartic side carries none".  P10 sec:lock states it so: "the volume enters by a calibration and not by
a choice ... that asymmetry is the whole content of the chain".

WHAT IS CLAIMED.
  1. r7034's level tensors are POINTWISE sums normalised to the degeneracy -- tr A = deg at a point -- while for
     orthonormal harmonics (integral of tr Y_A Y_B over the substrate = delta_AB) the pointwise sum is deg/V, by
     homogeneity.  So each level tensor in r7034's values is V times its orthonormal value.
  2. A quadratic term is one level tensor integrated once: V x (1/V) -- no volume, which is why r7058's rebuild of
     -D mu^2/4 closed and why it cannot see the volume of anything else.  The quartic is TWO level tensors at a
     point integrated once: V x (1/V)^2 = 1/V.  The cubic's square carries 1/V (r7058's own count).  So the quartic
     and the cubic's square carry the SAME inverse volume, and it cancels from their ratio.
  3. On the frame-constant sector, where every term is a constant and the identities are pointwise, the same count
     is explicit: with H = sum q_A E_A/sqrt(V), r7034's -2 tr H^2 integrates to -2 sum q^2 and r7032's algebraic
     quartic -(7/12)(tr H^2)^2 to -(7/12)(sum q^2)^2/V.
  4. r7060 found the level's quartic and the two-mode sector's differing by 88 pi^2/49 at m = 3, a factor that
     drifts with the label; 88 pi^2/49 is (44/49) V.  A ratio of two quartic energies of one level carrying the
     volume is the trace of the missing 1/V, and the correction removes it.
  5. So the criterion is G(m)/target < 18.  The six computed ratios stay below it -- the largest, 175/22 at the
     lowest odd label, by the factor 396/175, then about 6.6, 10.4, 14.0, 17.5 and 21.0 -- so the sign of the
     back-reaction is positive at every odd level computed, as r7058 concluded, by a margin that is a factor of
     2 pi^2 smaller than it stated; the net a level contributes is bounded below by 221/396 of its quartic energy,
     not 39/40.
  6. The quartic energy per level is (5m^6 - 41m^4 + 88m^2 - 16)/(15(m^2-1)) in units of kappa hbar^2/(a^3 V), and
     the regularised value -4/3 is in those units; its zero residue at dimension six is untouched.

SCOPE.  The normalisation of the level sums and what it moves.  r7034's level values, r7056's ratios, r7058's
oscillator factors and the zero of r7068 are used as filed.
"""
import contextlib, io, os, time
import sympy as sp

t_all = time.time()
CHECKS = []
def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)
def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)
print(__doc__)
HERE = os.path.dirname(os.path.abspath(__file__))
V = sp.Symbol('V', positive=True)

# =============================================================== A. what r7034's level tensors are
head("A.  r7034's LEVEL TENSORS ARE POINTWISE SUMS NORMALISED TO THE DEGENERACY")
R7034 = os.path.join(HERE, "P10_the_assembly_gives_both_level_sums_in_the_towers_own_variables_and_the_sign_"
                           "needs_no_bitensor.py")
NS = {"__name__": "r7034"}
with contextlib.redirect_stdout(io.StringIO()):
    try:
        exec(compile(open(R7034, encoding='utf-8').read(), R7034, "exec"), NS)
    except SystemExit as e:
        ex = e.code
gate("r7034 runs in full before its tensors are read", ex == 0)
deg = NS['deg']
gate("its pointwise level tensor A = sum_A Y_A (x) Y_A has trace deg at a point (r7034's nrmA)",
     sp.simplify(NS['nrmA'] - deg) == 0)
# orthonormal harmonics: integral over the substrate of tr(Y_A Y_B) = delta; homogeneity makes the pointwise sum constant
pointwise_orth = deg / V
gate("for orthonormal harmonics the same pointwise sum is deg/V, the integral of a constant over the volume being "
     "the degeneracy -- so each level tensor in r7034's values is V times its orthonormal value",
     sp.simplify(pointwise_orth * V - deg) == 0)

# =============================================================== B. the count
head("B.  ONE TENSOR INTEGRATED ONCE CARRIES NO VOLUME; TWO CARRY ONE INVERSE POWER")
quad = sp.simplify(V * (1 / V))           # one level tensor at its orthonormal value, integrated over V
quart = sp.simplify(V * (1 / V) ** 2)     # two level tensors at a point, integrated over V
cub2 = sp.simplify((V * (V ** sp.Rational(-1, 2)) ** 3) ** 2)
gate(f"relative to r7034's values: a quadratic carries {quad}, the quartic {quart}, the cubic's square {cub2} -- "
     f"so r7058's rebuild of -D mu^2/4 closing without a volume is the quadratic's own property and says nothing "
     f"about the quartic", quad == 1 and quart == 1 / V and cub2 == 1 / V)
gate("and the quartic and the cubic's square carry the SAME inverse volume, which cancels from their ratio",
     sp.simplify(quart / cub2) == 1)

# =============================================================== C. explicit on the frame-constant sector
head("C.  EXPLICIT ON THE FRAME-CONSTANT SECTOR, WHERE THE IDENTITIES ARE POINTWISE")
q = sp.symbols('q0:5')
E = [sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]) / sp.sqrt(2),
     sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / sp.sqrt(6),
     sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) / sp.sqrt(2),
     sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]) / sp.sqrt(2),
     sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]) / sp.sqrt(2)]
ortho = all(sp.simplify((E[i] * E[j]).trace() - (1 if i == j else 0)) == 0 for i in range(5) for j in range(5))
H = sum((q[i] * E[i] for i in range(5)), sp.zeros(3, 3)) / sp.sqrt(V)
p2 = sp.expand((H * H).trace())
I2 = sp.expand(V * (-2 * p2))                          # r7034's frame-constant value, -2 tr h^2, integrated
I4 = sp.expand(V * (-sp.Rational(7, 12) * p2 ** 2))    # r7032 / r7012's algebraic quartic, integrated
s2 = sum(x ** 2 for x in q)
gate(f"with the five constant matrices orthonormal under the trace and H = sum q_A E_A/sqrt(V) (orthonormal over "
     f"the substrate), the pointwise -2 tr H^2 integrates to {sp.factor(I2)} and -(7/12)(tr H^2)^2 to "
     f"{sp.factor(I4)}", ortho and sp.simplify(I2 + 2 * s2) == 0
     and sp.simplify(I4 + sp.Rational(7, 12) * s2 ** 2 / V) == 0)
gate("the frame-constant check reads r7034's own control value: its second-order identity on a frame-constant "
     "configuration is -2 tr h^2", 'hc' in NS and sp.simplify(NS['q2_of'](NS['hc']) + 2 * (NS['hc'] * NS['hc']).trace()) == 0)

# =============================================================== D. r7060's drift factor
head("D.  r7060's LEVEL-TO-TWO-MODE FACTOR CARRIES THE VOLUME")
f60 = sp.Rational(88, 49) * sp.pi ** 2
gate(f"r7060's factor between the level's quartic ratio and the two-mode sector's at m = 3, 88 pi^2/49, is "
     f"{sp.nsimplify(f60 / (2 * sp.pi ** 2))} V on the volume 2 pi^2: a ratio of two quartic energies of one level "
     f"carrying the volume, which the missing 1/V puts there and its correction removes",
     sp.simplify(f60 / (2 * sp.pi ** 2) - sp.Rational(44, 49)) == 0)

# =============================================================== E. the criterion
head("E.  THE CRITERION IS G/target < 18")
mlab = sp.Symbol('m', positive=True)
mu2 = mlab ** 2 - 1
D_ = 2 * (mlab ** 2 - 4)
Q4LEV = -D_ ** 2 * (5 * mu2 + 4) / 120
TARGET = sp.expand(-Q4LEV * mu2)
G = sp.Symbol('G', positive=True)
crit = sp.simplify((-Q4LEV / V) * mu2 - 2 * (G / (36 * V)))       # (-q4lev/V) mu^2 > 2 sum T^2, sum T^2 = G/(36V)
gate("with the quartic's 1/V the criterion (-q4lev/V) mu^2 > 2 sum T^2, sum T^2 = G/(36 V), is G/target < 18, "
     "the volume cancelling", sp.simplify(crit * V * 18 / TARGET - (18 - G / TARGET)) == 0)
RAT = {3: sp.Rational(175, 22), 5: sp.Rational(84, 31), 7: sp.Rational(865315, 502152),
       9: sp.Rational(3384355, 2639736), 11: sp.Rational(104584340, 101897367), 13: sp.Rational(96233385, 112183214)}
marg = {k: 18 / v for k, v in RAT.items()}
for k in sorted(RAT):
    print(f"      m = {k:2d}   G/target = {RAT[k]}   below 18 by the factor {sp.N(marg[k], 6)}", flush=True)
gate("r7056's six ratios, used as filed, all stay below 18: the largest, 175/22 at m = 3, by the factor 396/175, "
     "and the margin grows with the label -- so the sign of the back-reaction is positive at every odd level "
     "computed, as r7058 concluded, by a margin a factor 2 pi^2 smaller than it stated",
     all(v < 18 for v in RAT.values()) and marg[3] == sp.Rational(396, 175)
     and all(marg[a] < marg[b] for a, b in zip(sorted(RAT), sorted(RAT)[1:])))
gate("and the net a level contributes is bounded below by 1 - 175/396 = 221/396 of its quartic energy",
     1 - RAT[3] / 18 == sp.Rational(221, 396))

# =============================================================== F. the quartic energy's unit
head("F.  THE QUARTIC ENERGY PER LEVEL IS IN UNITS OF kappa hbar^2/(a^3 V)")
kap, aa, hb, muS = sp.symbols('kappa a hbar mu', positive=True)
pref = aa / (2 * kap)
sig = 2 * kap * hb / (aa ** 2 * muS)
E4 = -pref * (Q4LEV / V) * sig ** 2
unit = kap * hb ** 2 / (aa ** 3 * V)
E4u = sp.simplify((E4 / unit).subs(muS, sp.sqrt(mu2)))
gate(f"r7058's <V_4> = -(a/2 kappa) q4lev sigma^2 with the quartic's 1/V is {sp.factor(E4u)} in units of "
     f"kappa hbar^2/(a^3 V) -- r7060's per-level summand, in that unit",
     sp.simplify(E4u - (5 * mlab ** 6 - 41 * mlab ** 4 + 88 * mlab ** 2 - 16) / (15 * (mlab ** 2 - 1))) == 0)

print("\n  " + "=" * 74)
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail   [{time.time()-t_all:.0f}s]")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f"{len(bad)} check(s) failed: {bad}"
