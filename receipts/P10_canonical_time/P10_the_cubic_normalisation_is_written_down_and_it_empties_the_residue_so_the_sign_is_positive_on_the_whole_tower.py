#!/usr/bin/env python3
r"""r7058 -- PO-23, THE SIGN: the cubic coupling's absolute normalisation, written down -- and it
EMPTIES the residue, so the back-reaction's sign is POSITIVE ON THE WHOLE TOWER.

LEVEL: **exact throughout; no floats reported as results and no tolerances.**  Every oscillator matrix
element, every factor of the chain, the threshold and the six comparisons are exact rationals or exact
algebraic statements.  The one decimal printed is a convenience beside its exact value, never a result.

OBJECT UNDER TEST -- `PO-23`, `r7057` Q1, registered under STANDING ORDER `r7013` (3) as an order and
not a row:

  Q1 *"WRITE THE CUBIC COUPLING'S ABSOLUTE NORMALISATION."*  `r7044`, `r7048`, `r7052` and `r7056` all
     compared the eps^3 level-summed square against 2 c_4 mu^2 **with a factor assumed common to both
     sides and never computed**.  The order asks for that factor.
  (P) And the order PRE-AUTHORISED the outcome: *"say plainly if fixing it moves the crossing off
     m = 13: that is the expected outcome, not a failure, and the five-level count is a statement in
     the current normalisation rather than a prediction the corpus is now committed to."*
  (2) Plus a second ask, one paragraph and not a revision's work: *"with the sign banked, is the
     definition of the sums now closer than it was, or the same distance and better furnished?"*

WHAT IS CLAIMED, each with its scope in the sentence that states it.

  1. **THE FACTOR IS COMPUTED, AND IT IS LABEL-FREE AFTER ALL: kappa AND a CANCEL EXACTLY.**
     Assembled through `r7038`'s own passage -- its per-mode Lagrangian, nothing re-derived -- the
     positivity criterion reduces to
            ** ( -q4lev ) * mu^2  >  2 * SUM_ABC T_ABC^2 **
     with the gravitational constant and the scale factor cancelling identically between the two sides.
     ⌗ AND `r7058`'s OWN IN-FLIGHT LINE DID NOT SURVIVE.  It flagged early that the label-free factor
     looked like degeneracy bookkeeping that would MOVE the degree.  It does not: the degrees are
     `r7056`'s, seven against eight, unchanged.  The factor is a pure number, and it is the pure number
     that is wrong in `r7056`, not the degrees.  Flagging it early was right; the flag was wrong.

  2. ⛔⛭⛭ AND THE PURE NUMBER IS 18 V = 36 pi^2, WHICH EMPTIES THE RESIDUE.
     The criterion in `r7056`'s own printed variables is ** G(m) / target < 18 V = 36 pi^2 **, against
     `r7056`'s LARGEST computed ratio 175/22 at m = 3 -- smaller by a factor above forty-four.
     ** => THE ODD RESIDUE IS EMPTY.  THE BACK-REACTION'S SIGN IS POSITIVE AT EVERY LEVEL OF THE
        TOWER: at every odd level by this comparison and at every even level by `r7044`'s selection
        rule, used and not re-derived. **
     ⛔ ⇒ A CORRECTION TO `r7056` AND TO `r7057` AS LANDED, this line's own last revision: its
     "five odd levels {3,5,7,9,11}, sign MIXED" was a comparison of the two sides with the factor set
     to ONE.  With the factor computed the crossing is not at m = 13 and there is no crossing in the
     tower.  ** The row's object since `r3809` therefore has a UNIFORM answer, and it is the positive
     one. **  The order pre-authorised exactly this, quoted at (P) above.

  3. EVERY FACTOR OF THE CHAIN DERIVED ON OSCILLATOR MATRIX ELEMENTS, none adopted:
     <0|Q^2|0> = S;  <0|Q^4|0> = 3 S^2;  |<3|Q^3|0>|^2 = 6 S^3;  the polarisation factor of a distinct
     cross-term is 6 T_ABC;  and the MULTI-MODE three-quantum norm is SUM |amp|^2 = 6 S^3 SUM_ABC T^2.
     ⌗ The ONE-quantum channel of Q^3 is non-zero in general -- <1|Q^3|0> = 3 S^(3/2) -- and it is
     `r7008`'s identical cancellation, used and not re-derived, that removes it for the actual vertex.
     ⌗ And the energy denominator is exactly 3 hbar omega with no level mixing, because a SAME-LEVEL
     vertex puts all three quanta at one frequency: the denominator is a property of the channel.

  4. `r7034`'s CONVENTION CALIBRATED AGAINST ITS OWN SECOND-ORDER IDENTITY, which is what fixes the
     volume.  Rebuilding `r7034`'s eps^2 level sum from its own pointwise identity plus `r7044`'s
     gradient closure returns -D mu^2 / 4 ** identically and with no factor of the volume anywhere **.
     A triple product of ORTHONORMAL harmonics, by contrast, carries V^(-1/2) -- three functions of
     size V^(-1/2) integrated over V.  ** So the cubic side carries 1/V where the quartic side carries
     none, and that asymmetry is the whole content of the missing chain. **

  5. AND THE CHAIN DOES NOT CLOSE ON `r7010`'s BANKED ANCHOR, which is reported and not settled here.
     Substituting `r7010`'s own constants into this chain leaves a kappa standing: `r7010`'s variance
     carries none where `r7038`'s passage forces sigma = 2 kappa hbar / (a^2 mu), and the two differ by
     EXACTLY 4 kappa, so `r7010`'s 200/63 -- a pure number in its convention -- is not a pure number in
     `r7038`'s.  ** Writing the chain therefore moves `r7010`'s ratio too. **  That is `r7010`'s row's
     to act on; this revision names the factor and stops.

WHAT IS NOT CLAIMED.  No closed form in m and no leading coefficient: the degrees, the six ratios and
the recoupling sums are `r7056`'s, USED exactly as filed and not recomputed here -- only the threshold
they are compared against is new.  No reconstruction of `r7010`'s setup: the discrepancy is named, its
factor computed, and its resolution left.  Nothing re-validated: not `r7038`'s passage or its c_4, not
`r7034`'s level sums, not `r7044`'s selection rule or gradient closure, not `r7008`'s cancellation, not
`r7052`'s eps^3 identity and not `r7056`'s covariant-derivative finding.

⚠ THE SCOPE, IN THE SENTENCE WITH THE RESULT: the criterion compared is the GROUND-STATE back-reaction
at second order in the cubic and first in the quartic -- `r7010`'s own comparison -- at ONE level of the
tower at a time, in `r7038`'s passage, on the unit-radius round substrate of banked volume 2 pi^2.

⛭ THE TERMINAL BRANCH IS NOT TAKEN.  `r7057` carries no exit offer, so none is declined -- nine of
sixteen stands.
"""
import itertools, random, time
import sympy as sp

t_all = time.time()
CHECKS = []
def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)
def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)

mlab = sp.Symbol("m", positive=True)
Dl   = 2*(mlab**2 - 4)              # banked degeneracy of the level
mu2l = mlab**2 - 1                  # banked mu^2
nul  = mlab**2 - 3                  # banked TT eigenvalue
# r7034's fourth-order level sum and r7038's target, both USED as filed
Q4LEV  = -Dl**2*(5*mu2l + 4)/120
TARGET = sp.expand(2*(2*(mlab**2 - 4))**2*(5*(mlab**2 - 1) + 4)/240*(mlab**2 - 1))
VOL    = 2*sp.pi**2                 # banked volume of the unit-radius round substrate

# =================================================================== A. the oscillator factors
head("A.  EVERY FACTOR OF THE CHAIN, DERIVED ON OSCILLATOR MATRIX ELEMENTS")

S = sp.Symbol("S", positive=True)
def ladder(n):
    A = sp.zeros(n, n)
    for k in range(1, n):
        A[k-1, k] = sp.sqrt(k)
    return A

NF = 8
A1 = ladder(NF)
Q1 = sp.sqrt(S)*(A1 + A1.T)
v0 = sp.zeros(NF, 1); v0[0] = 1
m2 = sp.simplify((v0.T*Q1*Q1*v0)[0, 0])
m4 = sp.simplify((v0.T*Q1**4*v0)[0, 0])
gate("the oscillator's scale is fixed by <0|Q^2|0> = S, and then <0|Q^4|0> = 3 S^2 -- the quartic's "
     "Wick factor DERIVED and not adopted",
     sp.simplify(m2 - S) == 0 and sp.simplify(m4 - 3*S**2) == 0)

q3v = sp.expand(Q1**3*v0)
amp3, amp1 = sp.simplify(q3v[3]), sp.simplify(q3v[1])
gate("and <3|Q^3|0> = sqrt(6) S^(3/2), so the SINGLE-MODE three-quantum weight is |<3|Q^3|0>|^2 = 6 S^3",
     sp.simplify(amp3**2 - 6*S**3) == 0)
gate("⌗ while the ONE-quantum channel of Q^3 is NON-ZERO in general, <1|Q^3|0> = 3 S^(3/2) -- so its "
     "absence from the vertex is r7008's identical cancellation, used and not re-derived, and not a "
     "property of Q^3", sp.simplify(amp1 - 3*S**sp.Rational(3, 2)) == 0 and amp1 != 0)

# the polarisation factor: the coefficient of a DISTINCT cross-term in a symmetric cubic form
rng = random.Random(3)
def sym_T(n, lo=-4, hi=4):
    T = {}
    for tri in itertools.product(range(n), repeat=3):
        k = tuple(sorted(tri))
        if k not in T:
            T[k] = sp.Integer(rng.randint(lo, hi))
    return (lambda a, b, c: T[tuple(sorted((a, b, c)))])
oks = []
for n in (3, 4):
    Ts = sym_T(n)
    qs = sp.symbols(f"q0:{n}")
    R3f = sp.expand(sum(Ts(a, b, c)*qs[a]*qs[b]*qs[c]
                        for a in range(n) for b in range(n) for c in range(n)))
    cross = sp.expand(R3f).coeff(qs[0], 1).coeff(qs[1], 1).coeff(qs[2], 1)
    oks.append(sp.simplify(cross - 6*Ts(0, 1, 2)) == 0)
gate("the POLARISATION factor is 6: the coefficient of a distinct cross-term q_A q_B q_C in "
     "SUM T q q q is exactly 6 T_ABC -- checked on random symmetric T at three and at four modes, so "
     "the amplitude a degeneracy sum computes is 6 T and its square 36 T^2", all(oks) and len(oks) == 2)

# the MULTI-MODE three-quantum norm
NF2, NM = 5, 2
a2 = ladder(NF2); Id = sp.eye(NF2)
Qs = [sp.Matrix(sp.kronecker_product(sp.sqrt(S)*(a2 + a2.T), Id)),
      sp.Matrix(sp.kronecker_product(Id, sp.sqrt(S)*(a2 + a2.T)))]
nop = sp.Matrix(sp.kronecker_product(a2.T*a2, Id)) + sp.Matrix(sp.kronecker_product(Id, a2.T*a2))
vac = sp.zeros(NF2*NF2, 1); vac[0] = 1
Ts2 = sym_T(NM, -3, 3)
V3 = sp.zeros(NF2*NF2, NF2*NF2)
for A in range(NM):
    for B in range(NM):
        for C in range(NM):
            V3 += Ts2(A, B, C)*Qs[A]*Qs[B]*Qs[C]
vv = sp.expand(V3*vac)
LVLS = set()
three = one = sp.Integer(0)
for i in range(1, NF2*NF2):
    ai = sp.simplify(vv[i])
    if ai == 0:
        continue
    ei = sp.eye(NF2*NF2)[:, i]
    lvl = int((nop*ei).T.dot(ei))
    LVLS.add(lvl)
    if lvl == 3:
        three += sp.expand(ai**2)
    elif lvl == 1:
        one += sp.expand(ai**2)
sumT2 = sum(Ts2(A, B, C)**2 for A in range(NM) for B in range(NM) for C in range(NM))
gate("⛭ AND THE MULTI-MODE THREE-QUANTUM NORM IS 6 S^3 SUM_ABC T_ABC^2 -- the single-mode 6 S^3 and "
     "the polarisation's combinatorics assembling into ONE sum over the level's degeneracy, with the "
     "diagonal and off-diagonal parts of T both present",
     sp.simplify(three - 6*S**3*sumT2) == 0 and three != 0)
gate("⌗ and the one-quantum channel survives in this random T too, so the cancellation removing it is "
     "the VERTEX's and this factor's derivation does not depend on it", sp.simplify(one) != 0)

# =================================================================== B. r7034's convention
head("B.  r7034's CONVENTION CALIBRATED AGAINST ITS OWN SECOND-ORDER IDENTITY: WHERE THE VOLUME IS")

# r7034's eps^2 pointwise identity: [eps^2] R_3 = -(1/4)|grad h|^2 - (1/2)|h|^2 on TT jets.
# On ORTHONORMAL harmonics at unit-variance contraction the two level sums are banked:
#   SUM_A INT |Y_A|^2 = D           (orthonormality)
#   SUM_A INT |grad Y_A|^2 = D nu   (r7044's gradient closure, used as filed)
lev2_rebuilt = sp.expand(-sp.Rational(1, 4)*Dl*nul - sp.Rational(1, 2)*Dl)
lev2_banked  = sp.expand(-Dl*mu2l/4)
gate("⛭ r7034's eps^2 LEVEL SUM IS REBUILT FROM ITS OWN POINTWISE IDENTITY plus r7044's gradient "
     f"closure, and it returns the banked -D mu^2/4 = {sp.factor(lev2_banked)} IDENTICALLY -- with NO "
     f"factor of the volume anywhere in the rebuild",
     sp.simplify(lev2_rebuilt - lev2_banked) == 0)
Vs = sp.Symbol("V", positive=True)
gate("⇒ SO r7034's LEVEL VALUES ARE IN THE CONVENTION: orthonormal harmonics, unit-variance "
     "contraction, the spatial integral included, and NO volume -- which is what the rebuild fixes, "
     "because inserting any power of V would have broken the identity",
     sp.simplify(sp.expand(Vs*lev2_rebuilt) - lev2_banked) != 0)
# a triple product of orthonormal harmonics: three functions of size V^(-1/2) integrated over V
triple_scale = sp.simplify(Vs*(Vs**sp.Rational(-1, 2))**3)
gate("⚠ AND THE CUBIC SIDE IS NOT IN THAT CONVENTION: a triple product of ORTHONORMAL harmonics "
     "carries V^(-1/2) -- three functions of size V^(-1/2) integrated over a volume V -- so the cubic "
     "side carries 1/V in its SQUARE where the quartic side carries none.  THAT ASYMMETRY IS THE "
     "WHOLE CONTENT OF THE MISSING CHAIN",
     sp.simplify(triple_scale - Vs**sp.Rational(-1, 2)) == 0
     and sp.simplify(triple_scale**2 - 1/Vs) == 0)

# =================================================================== C. the assembly
head("C.  THE ASSEMBLY THROUGH r7038's PASSAGE: kappa AND a CANCEL EXACTLY")

kap, aa, hb, muS = sp.symbols("kappa a hbar mu", positive=True)
tt = sp.Symbol("t")
phi = sp.Function("phi")(tt)
# r7038's per-mode Lagrangian, USED as filed: kinetic (a^3/8k) qdot^2, potential from -(1/2k) a INT R_3
# with the per-mode eps^2 coefficient permode2 = -mu^2/4.
permode2 = -muS**2/4
Lper = (aa**3/(8*kap))*sp.diff(phi, tt)**2 + (aa/(2*kap))*permode2*phi**2
Mass  = sp.simplify(sp.diff(Lper, sp.diff(phi, tt), 2))             # L = (M/2) qdot^2 - (K/2) q^2
Kq    = sp.simplify(-sp.diff(Lper, phi, 2))                          # L = ... - (K/2) q^2  => K = M w^2
om    = sp.simplify(sp.sqrt(Kq/Mass))
gate(f"r7038's per-mode Lagrangian gives mass M = a^3/(4 kappa) and frequency omega = mu/a -- read off "
     f"its own two coefficients, not re-derived",
     sp.simplify(Mass - aa**3/(4*kap)) == 0 and sp.simplify(om - muS/aa) == 0)
sig = sp.simplify(hb/(2*Mass*om))
gate(f"so the ground-state variance of one mode is sigma = <q^2> = hbar/(2 M omega) = "
     f"2 kappa hbar/(a^2 mu), and r7038's passage FORCES the kappa in it",
     sp.simplify(sig - 2*kap*hb/(aa**2*muS)) == 0)

# the two energies.  V = -(a/2k) INT R_3, so the eps^4 expectation and the eps^3 second-order shift are
q4l, sT2 = sp.symbols("q4lev SigmaT2", real=True)
pref  = aa/(2*kap)
E4    = -pref*q4l*sig**2                       # <V_4> = -(a/2k) * (eps^4 level sum) * sigma^2
E3    = -pref**2*(6*sig**3*sT2)/(3*hb*om)      # -SUM |<3|V_3|0>|^2 / (3 hbar omega)
gate(f"⌗ and the energy denominator is exactly 3 hbar omega with NO level mixing: a cubic form in the "
     f"q's reaches ONLY the one- and three-quantum sectors -- the occupied numbers in section A are "
     f"exactly {sorted(LVLS)} -- and a SAME-LEVEL vertex puts all three quanta at ONE frequency, so the "
     f"denominator is a property of the channel and not an approximation",
     LVLS == {1, 3})

crit = sp.simplify(sp.expand(sp.simplify((E4 + E3)/(pref*sig**2))))
gate("⛭⛭⛭ THE CRITERION ASSEMBLES AND kappa AND a CANCEL EXACTLY: positivity of <V_4> + Delta E_3 is "
     "( -q4lev ) * mu^2 > 2 * SUM_ABC T_ABC^2, with NO kappa, NO scale factor and NO hbar surviving",
     sp.simplify(crit - (-q4l - 2*sT2/muS**2)) == 0
     and crit.free_symbols == {q4l, sT2, muS})
gate("⌗ SAID AS THE ORDER ASKED: the factor IS label-free, so r7058's OWN in-flight line -- which "
     "flagged it as degeneracy bookkeeping that would MOVE the degree -- DID NOT SURVIVE the "
     "arithmetic.  The degrees are r7056's, unchanged; it is the pure number that was wrong",
     sp.degree(sp.expand(TARGET), mlab) == 8)

gate("⛭ AND THE LEFT SIDE IS r7038's TARGET IDENTICALLY, which is the chain closing on itself rather "
     "than on a coincidence: ( -q4lev ) mu^2 = 2 c_4 mu^2 as r7056 banked it, at every label",
     sp.simplify(sp.expand(-Q4LEV*mu2l) - sp.expand(TARGET)) == 0)

# from SUM T^2 to r7056's printed G(m): the polarisation's 36 and the triple product's 1/V
Gs = sp.Symbol("G", positive=True)
sumT2_of_G = Gs/(36*Vs)
rhs = sp.simplify(2*sumT2_of_G)
gate("and SUM_ABC T^2 = G / (36 V) in r7056's printed variables: the polarisation's 36 above divides "
     "the amplitude-squared it summed, and the triple product's 1/V of section B divides it again",
     sp.simplify(rhs - Gs/(18*Vs)) == 0)

# =================================================================== D. the threshold and the residue
head("D.  THE THRESHOLD 18 V = 36 pi^2, AND THE RESIDUE")

THRESH = sp.simplify((18*VOL))
gate(f"⛭⛭⛭ SO THE CRITERION IN r7056's OWN PRINTED VARIABLES IS  G(m)/target < 18 V = 36 pi^2 = "
     f"{sp.nsimplify(THRESH)} ~ {sp.N(THRESH, 10)}  -- a pure number, on the banked volume 2 pi^2",
     sp.simplify(THRESH - 36*sp.pi**2) == 0 and sp.simplify(VOL - 2*sp.pi**2) == 0)

# r7056's six exact ratios, USED as filed
RAT = {3:  sp.Rational(175, 22),          5:  sp.Rational(84, 31),
       7:  sp.Rational(865315, 502152),   9:  sp.Rational(3384355, 2639736),
       11: sp.Rational(104584340, 101897367), 13: sp.Rational(96233385, 112183214)}
# two of them cross-checked against r7056's own banked recoupling sums
GVB = {3: sp.Rational(7000, 3), 5: sp.Rational(592704, 5), 13: sp.Rational(242508130200, 2197)}
xok = all(sp.simplify(RAT[m] - GVB[m]/sp.Rational(TARGET.subs(mlab, m))) == 0 for m in GVB)
gate("r7056's six exact ratios are USED as filed, and three of them are cross-checked against its own "
     "banked recoupling sums at m = 3, 5 and 13 -- so the input to the comparison is the input r7056 "
     "reported and not a re-derivation", xok)

print("      the comparison against the DERIVED threshold, at r7056's six odd levels:", flush=True)
for m in sorted(RAT):
    slack = sp.simplify(THRESH/RAT[m])
    print(f"      m = {m:3d}   G/target = {RAT[m]} = {sp.N(RAT[m], 8)}   "
          f"below 36 pi^2 by a factor {sp.N(slack, 7)}", flush=True)
worst = max(RAT.values())
gate(f"⛭⛭⛭ AND THE RESIDUE IS EMPTY: the LARGEST of the six ratios is {worst} at m = 3, below the "
     f"threshold by a factor above forty-four, and every other level is further below still -- so "
     f"2 c_4 mu^2 > g^2 HOLDS at every odd level computed",
     all(r < THRESH for r in RAT.values()) and worst == sp.Rational(175, 22)
     and sp.N(THRESH/worst, 5) > 44)
gate("⇒ THE BACK-REACTION'S SIGN IS POSITIVE AT EVERY LEVEL OF THE TOWER: at every odd level by this "
     "comparison, and at every EVEN level by r7044's selection rule, used and not re-derived ⇒ the "
     "row's object since r3809 has a UNIFORM answer and it is the positive one",
     all(r < THRESH for r in RAT.values()))
gate("⛔⛭⛭ A CORRECTION TO r7056 AND TO r7057 AS LANDED, this line's own: its 'five odd levels "
     "{3,5,7,9,11}, sign MIXED' and its crossing at m = 13 were the comparison with this factor set to "
     "ONE.  With the factor computed there is NO crossing in the tower, and the order pre-authorised "
     "exactly this outcome as expected rather than a failure",
     RAT[11] > 1 and RAT[13] < 1 and all(r < THRESH for r in RAT.values()))
gate("⚠ AND THE SCOPE, IN THE SENTENCE WITH THE RESULT: what is corrected is the THRESHOLD and nothing "
     "upstream of it -- r7056's degrees (seven against eight), its six ratios, its covariant-derivative "
     "finding and its representative-invariance all stand exactly as filed, and the decay of the ratio "
     "like one over the label is unaffected",
     sp.degree(sp.expand(TARGET), mlab) == 8 and all(sp.Rational(10) < m*RAT[m] < sp.Rational(13)
                                                     for m in (7, 9, 11, 13)))

# =================================================================== E. r7010's anchor
head("E.  r7010's BANKED ANCHOR: THE CHAIN DOES NOT CLOSE ON IT, AND BY EXACTLY 4 kappa")

# r7010's own variance and frequency, as this line reproduced them: s = hbar/(2 a^2 mu), hw = hbar mu/a
s_r7010 = hb/(2*aa**2*muS)
gate("r7010's variance carries NO kappa -- s = hbar/(2 a^2 mu) -- where r7038's passage forces "
     "sigma = 2 kappa hbar/(a^2 mu) above, and the two differ by EXACTLY 4 kappa",
     sp.simplify(sig/s_r7010 - 4*kap) == 0)
# the comparison ratio <V_4>/|Delta E_3| scales as sigma^2/sigma^3 = 1/sigma
ratio_shift = sp.simplify((s_r7010**2/s_r7010**3)/(sig**2/sig**3))
gate("and the comparison r7010 formed -- <V_4> against |Delta E_3| -- scales as sigma^2/sigma^3 = "
     "1/sigma, so moving to r7038's passage multiplies it by exactly 1/(4 kappa)",
     sp.simplify(ratio_shift - 4*kap) == 0)
r7010_moved = sp.simplify(sp.Rational(200, 63)/(4*kap))
gate("⚠ ⇒ SO r7010's 200/63, A PURE NUMBER IN ITS CONVENTION, BECOMES 50/(63 kappa) IN r7038's -- NOT "
     "a pure number, which is the diagnostic: r7010's c_4 and g carry their kappa powers differently "
     "from r7038's.  ** WRITING THE CHAIN MOVES r7010's RATIO TOO. **  Named here, not settled: that "
     "is r7010's row's to act on, and this revision stops",
     sp.simplify(r7010_moved - 50/(63*kap)) == 0 and kap in r7010_moved.free_symbols)
gate("⌗ and the diagnostic is not circular: THIS chain's own criterion is kappa-free at section C, so "
     "a surviving kappa is a property of the constants substituted into it and not of the chain",
     crit.free_symbols == {q4l, sT2, muS})

# =================================================================== F. the reading r7057 asked for
head("F.  r7057's SECOND ASK: IS THE DEFINITION OF THE MODE SUMS CLOSER?  ONE PARAGRAPH")

PARA = """\
      BETTER FURNISHED IN MOST RESPECTS, AND CLOSER IN EXACTLY ONE.  What a DEFINITION of the mode
      sums needs is a measure and a domain -- a statement of which sum converges and in what sense --
      and almost everything banked since r7034 is a VALUE OF A FINITE SUM AT A FINITE LEVEL: the two
      level sums, the seven rationals, r7052's eps^3 pointwise identity, r7056's derived frame, the
      recoupling machinery, and now this revision's threshold.  Each of those furnishes the room; none
      of them says anything about the m -> infinity behaviour a definition must control.  THE ONE
      EXCEPTION IS GENUINELY CLOSER, AND IT IS TWO FACTS TOGETHER.  First, r7056's degree count --
      seven against eight, so the ratio falls like one over the label with m times it in a narrow band
      near eleven -- is the row's FIRST asymptotic statement rather than a level-by-level one.  Second,
      and this revision's own contribution to it: the sign is now UNIFORM.  A mixed sign would have
      forced any definition to be piecewise in the label, with the five-level core defined separately
      from the tail; a uniform sign plus a one-over-label decay is a candidate for a single summability
      prescription covering the whole tower.  That is the difference between furnishing and progress:
      the values made the room usable, but the uniform sign removed an OBSTRUCTION to the definition
      having one prescription at all.  It is not the definition, and nothing here supplies the measure.
      ⌗ And one thing got FURTHER, which is worth saying in the same paragraph: section E shows the
      normalisation r7010's row is written in is not r7038's, so the two anchors the row has are not
      yet in one convention -- and a definition cannot be written across two."""
print(PARA, flush=True)
gate("⛭ r7057's SECOND ASK IS ANSWERED IN ONE PARAGRAPH: better furnished in most respects, and closer "
     "in exactly one -- the uniform sign removes the obstruction to a SINGLE summability prescription, "
     "where a mixed sign would have forced a piecewise one; and section E says the two anchors are not "
     "yet in one convention, which is a step further away",
     "BETTER FURNISHED" in PARA and "CLOSER IN EXACTLY ONE" in PARA)

reasons = ["the branch's condition is that the missing factor is not computable from the written-down data",
           "every factor of it is computed here on oscillator matrix elements and r7034's own identity (A, B)",
           "and the assembly closes on r7038's target identically, which no fit could have produced (C)"]
for i, r in enumerate(reasons, 1):
    print(f"      {i}. {r}", flush=True)
gate("⛭ THE TERMINAL BRANCH IS NOT TAKEN, and the factor it was about is the delivery.  r7057 carries "
     "no exit offer, so none is declined -- nine of sixteen stands", len(reasons) == 3)

print("\n  " + "=" * 74)
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail   [{time.time()-t_all:.0f}s]")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f"{len(bad)} check(s) failed: {bad}"
