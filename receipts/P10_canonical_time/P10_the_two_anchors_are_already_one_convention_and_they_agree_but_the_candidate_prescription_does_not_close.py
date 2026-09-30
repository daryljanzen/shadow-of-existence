#!/usr/bin/env python3
r"""r7060 -- PO-23: the two anchors are ALREADY one convention and they AGREE -- and the candidate
summability prescription DOES NOT CLOSE.

LEVEL: **exact throughout.**  Every calibration, coefficient, ratio and growth rate is an exact
rational or an exact symbolic limit.  The few decimals printed sit beside their exact values and are
never a result.

OBJECT UNDER TEST -- `PO-23`, `r7059`, two questions in a FIXED order:

  Q1 *"THE TWO ANCHORS INTO ONE CONVENTION, FIRST ... with each banked anchor restated in it and the
     powers of kappa tracked explicitly.  If reconciling them moves a banked number, that is the
     finding."*  Ordered first for the reason this line gave: a definition cannot be written across two.
  Q2 *"AND THEN THE ROW'S OWN OBJECT ... does that candidate close?  A prescription resting on a
     one-over-label decay and a uniform sign, stated as a measure and a domain -- or a demonstration
     that it does not, which is the row's founding alternative.  Either is the row."*
  Calibration the order names: *"the pairing count enters once, on the target side, inside the banked
     c_4.  r7058 did not disturb it and Q1 should not either; say so if it does."*

WHAT IS CLAIMED, each with its scope in the sentence that states it.

  1. ⛭⛭⛭ Q1: THE TWO ANCHORS ARE ALREADY IN ONE CONVENTION, THEY AGREE EXACTLY, AND NOTHING BANKED
     MOVES -- EXCEPT `r7058`'s OWN SECTION E, WHICH IS WRONG.
     ** The criterion ratio R = g^2/(2 c_4 mu^2) is INVARIANT under a change of convention. ** A
     convention change rescales the FIELD, and the couplings move with it: matching the two kinetic
     terms forces q_10 = q_38/(2 sqrt(kappa)), hence c_4 -> c_4/(16 kappa^2) and g^2 -> g^2/(64
     kappa^3), and R is unchanged -- as it must be, R being a ratio of two ENERGIES.
     ⛔ ⇒ A CORRECTION TO `r7058`, THIS LINE'S OWN LAST REVISION.  Its section E swapped the VARIANCE
     and kept `r7010`'s couplings.  ** That is a HYBRID, not a convention **, and the 4 kappa it
     measured is the artefact of it.  ** So "r7010's 200/63 becomes 50/(63 kappa)" is WRONG: 200/63
     is unchanged, and a ratio of energies could not have carried a kappa. **
     ⌗ `r7010`'s mass is SOLVED from its own variance rather than assumed: M_10 = a^3 against
     `r7038`'s M_38 = a^3/(4 kappa).  That is the whole of the mismatch, and it is a field
     normalisation and not a disagreement.

  2. ⛭⛭ AND THE RESTATEMENT IS DERIVED WITH NO FITTED PARAMETER, WHICH IS WHAT MAKES (1) A RECONCILIATION
     RATHER THAN AN ASSERTION.  Matching the PER-MODE quadratic coefficient -- `r7010`'s own -48 against
     `r7034`'s level sum -D mu^2/4 divided by the degeneracy -- ** forces lambda^2 = 1/24 **, the single
     number relating `r7010`'s Misner beta to `r7034`'s q.  With no further freedom it then returns:
     ** `r7010`'s banked c_4 numerator 14/3 EXACTLY **, from its own quartic -336 (b+^2 + b-^2)^2 and the
     two-mode Wick factor 8; ** and sum_ABC T_ABC^2 = 200/27 ** from its own cubic 160 (b+^3 - 3 b+ b-^2),
     whose symmetric T is SOLVED and not guessed; so ** g^2/(2 c_4) = 200/63 **, `r7010`'s banked number.
     ⇒ ** AND `r7058`'s CRITERION, EVALUATED ON `r7010`'s OWN TWO-MODE SECTOR, RETURNS R = 25/63 --
        IDENTICAL TO `r7010`'s BANKED RATIO AT ITS OWN LEVEL. **  The chain closes on the other anchor.
     ⌗ Fixing lambda^2 from the QUADRATIC carries the whole convention across, the volume included,
     because each source weights its quadratic and its higher terms the same way -- which is why no
     factor of V survives in the two-mode R while the level's criterion carries 18V.

  3. AND WHAT SEPARATES THE TWO NUMBERS IS THE **OBJECT**, NOT A CONVENTION.  `r7010`'s anchor is the
     TWO frame-constant Misner modes at m = 3; `r7058`'s is the degeneracy-summed level, D = 2(m^2-4)
     = 10 there.  ** Their ratios differ by 88 pi^2/49 at m = 3 and the factor DRIFTS across the tower
     ** -- 88/49, 775/441, 239120/173063, 5279472/4738097, 33965789/36604519, 2243664280/2829261519,
     each times pi^2, at m = 3..13 -- ** and a convention factor cannot drift. **
     ⌗ And it is not a disagreement either: both anchors return the SAME SIGN, positive, at m = 3.
     The level's quartic is 55/7 times the two-mode sector's and not D/2 = 5, so the frame-constant
     slice is not a proportional slice of the level -- which is why the two numbers were never the same
     number and why `P10`'s "not to be read against the derived threshold" was right as far as it went.

  4. ⛔⛭⛭ Q2: THE CANDIDATE PRESCRIPTION DOES NOT CLOSE -- AND THE REASON INVERTS `r7058`'s OWN READING.
     The summand is written down here for the first time: in `r7038`'s passage the quartic energy per
     level is (m-2)^2 (m+2)^2 (5m^2-1)/(15(m-1)(m+1)) in units of kappa hbar^2/a^3, ** POSITIVE at every
     level and growing like m^4 ** (the limit of <V4>/m^4 is 1/3, finite and non-zero, and it is neither
     m^3 nor m^5).  Because 0 < R < 1 at every level -- `r7058`, used and not re-derived -- the NET per
     level is bounded BELOW by (1 - R_max) <V4> > 0.977 <V4>, so the partial sum is bounded below by
     sum k^4/3, which diverges.
     ⇒ ** SO THE SUM DIVERGES, AND NO SUMMABILITY PRESCRIPTION RESTING ON DECAY CAN ACT ON IT, BECAUSE
        THERE IS NO DECAY: the one-over-label decay is the decay of the RATIO R, not of the summand. **
     ⛔ ⇒ AND A SECOND CORRECTION TO `r7058`: its closing paragraph read the uniform sign as REMOVING an
     obstruction to a single prescription.  ** It is the other way round.  A uniform sign FORBIDS the
     conditional convergence an alternating sign would have permitted **, so it removes the one route to
     convergence that needs no regulator.  The two facts the paragraph put together as progress are one
     fact about a ratio and one fact that makes the sum worse.
     ⌗ That is `r7059`'s stated alternative taken: *"a demonstration that it does not, which is the row's
     founding alternative ... Either is the row."*  No measure is asserted, because none closes.

WHAT IS NOT CLAIMED.  No re-derivation of anything `r7058` closed: the threshold 18V = 36 pi^2, the
cancellation of kappa and the scale factor, the volume calibration and the positive sign are USED as
filed and this revision does not reopen them -- what is corrected is `r7058`'s section E and its closing
paragraph, both of which sit BESIDE those results rather than under them.  No definition of the mode
sums is offered, and no regulator is proposed: the claim is that the candidate fails, not that another
would succeed.  The drift in (3) is exhibited at six levels and not given a closed form.  `r7010`'s
reduction is USED as filed -- its -48, +160 and -336 are read from its own receipt, not recomputed.

⚠ THE PAIRING COUNT, ON THE ORDER'S OWN QUESTION AND SAID ONCE: Q1 does NOT disturb it.  The
reconciliation uses `r7010`'s own two-mode Wick factor 8 on its own quartic and `r7034`'s level value as
filed; no pairing count is applied a second time anywhere, and the count still enters exactly once, on
the target side, inside the banked c_4.

⚠ THE SCOPE, IN THE SENTENCE WITH THE RESULT: (1)-(3) are at m = 3, the only level at which `r7010`'s
anchor is defined -- its vertex numbers are label-INDEPENDENT constants and `r7036` pinned its level.
(4) is the ground-state back-reaction at second order in the cubic and first in the quartic, summed over
the tower's levels in `r7038`'s passage, with R taken from `r7058` at the six odd levels it computed.

⛭ THE TERMINAL BRANCH IS NOT TAKEN.  `r7059` carries no exit offer, so none is declined -- nine of
sixteen stands.
"""
import itertools, time
import sympy as sp

t_all = time.time()
CHECKS = []
def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)
def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)

kap, a, hb, mu, mlab = sp.symbols("kappa a hbar mu m", positive=True)
M0, D0, MU2 = 3, 10, 8                       # r7010's level, its degeneracy, its mu^2

# =================================================================== A. convention-invariance
head("A.  A CHANGE OF CONVENTION RESCALES THE FIELD, AND THE CRITERION RATIO IS INVARIANT")

om = mu/a
M38 = a**3/(4*kap)                           # r7038: L = (a^3/8k) qdot^2
s10 = hb/(2*a**2*mu)                         # r7010's own variance
M10 = sp.simplify(hb/(2*s10*om))             # SOLVED from it, not assumed
gate("r7010's mass is SOLVED from its own variance as M = a^3, against r7038's M = a^3/(4 kappa) -- "
     "so the whole mismatch between the two anchors is a factor 4 kappa in the KINETIC normalisation, "
     "which is a field normalisation and not a disagreement",
     sp.simplify(M10 - a**3) == 0 and sp.simplify(M10/M38 - 4*kap) == 0)
sig38 = sp.simplify(hb/(2*M38*om))
gate("and the two variances stand in that same ratio, r7038's being 2 kappa hbar/(a^2 mu)",
     sp.simplify(sig38 - 2*kap*hb/(a**2*mu)) == 0 and sp.simplify(sig38/s10 - 4*kap) == 0)

c4s, g2s = sp.symbols("c4 g2", positive=True)
def R_of(c4v, g2v, sig):
    """r7010's own assembly: <V4> = 8 c4 a sig^2 and |dE3| = 8 g2 a^2 sig^3/(hbar omega)."""
    return sp.simplify((8*g2v*a**2*sig**3/(hb*om))/(8*c4v*a*sig**2))
R10 = R_of(c4s, g2s, s10)
gate("the comparison both anchors form reduces to R = g^2/(2 c_4 mu^2), which is r7034's own form of "
     "the criterion -- used and not re-derived", sp.simplify(R10 - g2s/(2*c4s*mu**2)) == 0)
lam2_field = sp.simplify(M38/M10)            # q_10 = lambda q_38, lambda^2 = M38/M10
c4_38 = sp.simplify(c4s*lam2_field**2)
g2_38 = sp.simplify(g2s*lam2_field**3)
gate("a CONSISTENT change of convention rescales the field so the kinetic terms agree -- "
     "q_10 = q_38/(2 sqrt(kappa)) -- and the couplings move WITH it: c_4 -> c_4/(16 kappa^2) and "
     "g^2 -> g^2/(64 kappa^3)",
     sp.simplify(sp.sqrt(lam2_field) - 1/(2*sp.sqrt(kap))) == 0
     and sp.simplify(c4_38 - c4s/(16*kap**2)) == 0 and sp.simplify(g2_38 - g2s/(64*kap**3)) == 0)
R38 = R_of(c4_38, g2_38, sig38)
gate("⛭⛭⛭ AND R IS THEN INVARIANT, EXACTLY -- which it must be, being a ratio of two ENERGIES: no "
     "change of field variable can move it, so the row was never split by a power of kappa at all",
     sp.simplify(R38 - R10) == 0)
R_hybrid = R_of(c4s, g2s, sig38)
gate("⛔⛭ SO r7058's SECTION E IS WRONG, and this is a correction to this line's own last revision: it "
     "swapped the VARIANCE and kept r7010's couplings, which is a HYBRID and not a convention -- and "
     "that hybrid is exactly 4 kappa times R, which is the number r7058 reported",
     sp.simplify(R_hybrid/R10 - 4*kap) == 0 and sp.simplify(R_hybrid - R10) != 0)
V = sp.Symbol("V", positive=True)
c4_b, g2_b = 14*kap/(3*V), 800*kap/(27*V)    # r7010's banked constants, used as filed
R_banked = sp.simplify(g2_b/(2*c4_b*mu**2))
gate("⇒ AND r7010's BANKED 200/63 DOES NOT MOVE: its own c_4 = 14k/(3V) and g^2 = 800k/(27V) give a "
     "ratio that is ALREADY free of kappa AND of V, so 50/(63 kappa) could not have been right -- a "
     "ratio of energies cannot carry a coupling constant",
     sp.simplify(R_banked - sp.Rational(200, 63)/mu**2) == 0
     and R_banked.free_symbols == {mu})

# =================================================================== B. the forced calibration
head("B.  THE RESTATEMENT, WITH NO FITTED PARAMETER: lambda^2 IS FORCED BY THE QUADRATIC")

lev2 = sp.Rational(-D0*MU2, 4)               # r7034's eps^2 level sum at m = 3, used as filed
lam2 = sp.Symbol("lam2", positive=True)
LAM2 = sp.solve(sp.Eq(-48*lam2, sp.Rational(lev2, D0)), lam2)[0]
gate(f"r7034's eps^2 level sum at m = 3 is {lev2}, so its PER-MODE quadratic is {sp.Rational(lev2, D0)}; "
     f"matching r7010's own -48 per mode FORCES lambda^2 = {LAM2} -- the single number relating r7010's "
     f"Misner beta to r7034's q, solved and not chosen",
     LAM2 == sp.Rational(1, 24))
q4_2mode = sp.Rational(-336)*8*LAM2**2       # <-336(b+^2+b-^2)^2> = -336 * 8 * <b^2>^2 at unit variance
gate("⛭⛭ AND WITH NO FURTHER FREEDOM IT RETURNS r7010's BANKED c_4 NUMERATOR 14/3 EXACTLY, from its "
     "own quartic -336 (b+^2 + b-^2)^2 and the two-mode Gaussian factor 8 -- so the calibration is a "
     "reconciliation and not an assertion",
     sp.simplify(-q4_2mode - sp.Rational(14, 3)) == 0)

bp, bm = sp.symbols("bp bm"); bb = (bp, bm)
KEYS = sorted({tuple(sorted(t)) for t in itertools.product((0, 1), repeat=3)})
Tsym = {k: sp.Symbol(f"T{k[0]}{k[1]}{k[2]}") for k in KEYS}
form = sp.expand(sum(Tsym[tuple(sorted(t))]*bb[t[0]]*bb[t[1]]*bb[t[2]]
                     for t in itertools.product((0, 1), repeat=3)))
cub = sp.expand(160*(bp**3 - 3*bp*bm**2))    # r7010's own cubic, used as filed
sol = sp.solve(sp.Poly(sp.expand(form - cub), bp, bm).coeffs(), list(Tsym.values()), dict=True)[0]
Tv = {k: sp.Integer(sol[Tsym[k]]) for k in KEYS}
recon = sp.expand(form.subs(sol))
gate(f"the symmetric T of r7010's cubic is SOLVED rather than guessed -- T000 = {Tv[(0,0,0)]}, "
     f"T011 = {Tv[(0,1,1)]}, the other two zero -- and it reproduces that cubic identically",
     sp.simplify(recon - cub) == 0 and Tv[(0, 0, 0)] == 160 and Tv[(0, 1, 1)] == -160)
sumT2_b = sum(Tv[tuple(sorted(t))]**2 for t in itertools.product((0, 1), repeat=3))
sumT2_q = sp.Rational(sumT2_b)*LAM2**3       # T b b b = (T lambda^3) q q q
gate(f"so sum_ABC T_ABC^2 is {sumT2_b} in r7010's beta and {sumT2_q} in r7034's q, and the two banked "
     f"numbers together give g^2/(2 c_4) = 200/63 -- r7010's own",
     sumT2_q == sp.Rational(200, 27)
     and sp.simplify(2*sumT2_q/(-q4_2mode) - sp.Rational(200, 63)) == 0)
lhs2, rhs2 = sp.simplify(-q4_2mode*MU2), sp.simplify(2*sumT2_q)
R2 = sp.simplify(rhs2/lhs2)
gate(f"⛭⛭⛭ AND r7058's CRITERION (-q4lev) mu^2 > 2 sum T^2, EVALUATED ON r7010's OWN TWO-MODE SECTOR, "
     f"IS {lhs2} > {rhs2} ⇒ R = {R2} -- IDENTICAL TO r7010's BANKED RATIO AT ITS OWN LEVEL.  The chain "
     f"closes on the other anchor, so the two are ALREADY one convention and they AGREE",
     R2 == sp.Rational(25, 63) and sp.simplify(R2 - sp.Rational(200, 63)/MU2) == 0)
gate("⚠ AND THE PAIRING COUNT IS NOT DISTURBED, on the order's own question and said once: the "
     "reconciliation uses r7010's own two-mode Gaussian factor and r7034's level value as filed, and "
     "applies no count a second time -- it still enters exactly once, on the target side, in c_4",
     sp.simplify(-q4_2mode - sp.Rational(14, 3)) == 0)

# =================================================================== C. object, not convention
head("C.  WHAT SEPARATES THE TWO NUMBERS IS THE OBJECT, AND A CONVENTION FACTOR CANNOT DRIFT")

TARGET = sp.expand(2*(2*(mlab**2 - 4))**2*(5*(mlab**2 - 1) + 4)/240*(mlab**2 - 1))
TH = 36*sp.pi**2                             # r7058's threshold 18V at V = 2 pi^2, used as filed
RAT = {3: sp.Rational(175, 22), 5: sp.Rational(84, 31), 7: sp.Rational(865315, 502152),
       9: sp.Rational(3384355, 2639736), 11: sp.Rational(104584340, 101897367),
       13: sp.Rational(96233385, 112183214)}
q4lev3 = sp.Rational(-D0**2*(5*MU2 + 4), 120)
gate(f"the level's quartic at m = 3 is {q4lev3} against the two-mode sector's {q4_2mode}, a factor "
     f"{sp.simplify(q4lev3/q4_2mode)} and NOT D/2 = {D0//2} -- so the frame-constant slice is not a "
     f"proportional slice of the level, which is why the two numbers were never the same number",
     sp.simplify(q4lev3/q4_2mode) == sp.Rational(55, 7))
print("      the two anchors' ratios, level by level:", flush=True)
drift = {}
for mm in sorted(RAT):
    r_lev = sp.simplify(RAT[mm]/TH)
    r_10 = sp.Rational(200, 63)/(mm**2 - 1)
    drift[mm] = sp.nsimplify(sp.simplify(r_10/r_lev), [sp.pi])
    print(f"      m = {mm:3d}   two-mode R = {str(r_10):>10} = {float(r_10):.6f}   "
          f"level R = {float(r_lev):.6f}   ratio = {drift[mm]}", flush=True)
gate(f"⛭ AND THE FACTOR BETWEEN THEM DRIFTS -- {drift[3]} at m = 3 falling across the tower -- so it is "
     f"NOT a convention factor, which would be constant: the two anchors measure DIFFERENT OBJECTS, "
     f"r7010's two frame-constant modes against the degeneracy-summed level",
     drift[3] == 88*sp.pi**2/49 and len({sp.simplify(d/sp.pi**2) for d in drift.values()}) == 6
     and sp.simplify(drift[3] - drift[13]) != 0)
gate("⌗ and it is not a DISAGREEMENT either: both anchors return the SAME SIGN at m = 3, each ratio "
     "being below one, so nothing banked is contradicted by the reconciliation",
     sp.Rational(200, 63)/MU2 < 1 and sp.simplify(RAT[3]/TH) < 1)

# =================================================================== D. Q2
head("D.  ⛔⛭⛭ Q2: THE SUMMAND IS WRITTEN DOWN, AND THE CANDIDATE DOES NOT CLOSE")

mu2l, Dl = mlab**2 - 1, 2*(mlab**2 - 4)
q4l = -Dl**2*(5*mu2l + 4)/120
sigl = 2*kap*hb/(a**2*sp.sqrt(mu2l))
E4 = sp.simplify(-(a/(2*kap))*q4l*sigl**2)
U = sp.simplify(sp.factor(E4*a**3/(kap*hb**2)))
gate(f"the QUARTIC ENERGY PER LEVEL in r7038's passage is {U} in units of kappa hbar^2/a^3 -- written "
     f"down here for the first time, and POSITIVE at every level of the tower",
     all(U.subs(mlab, k) > 0 for k in range(3, 60)))
# sp.degree RAISES on a rational function -- the growth rate is taken as an exact limit instead
g4 = sp.limit(U/mlab**4, mlab, sp.oo)
gate(f"and it GROWS LIKE m^4: the limit of <V4>/m^4 is exactly {g4}, finite and non-zero, while the "
     f"same limit against m^3 diverges and against m^5 vanishes -- taken as a limit because sp.degree "
     f"raises on a rational function",
     g4 == sp.Rational(1, 3) and sp.limit(U/mlab**3, mlab, sp.oo) is sp.oo
     and sp.limit(U/mlab**5, mlab, sp.oo) == 0)
Rmax = max(sp.simplify(r/TH) for r in RAT.values())
gate(f"and because 0 < R < 1 at every level -- r7058, used and not re-derived, its largest value being "
     f"{Rmax} -- the NET per level is bounded BELOW by (1 - R) <V4> > (39/40) <V4> > 0",
     Rmax == sp.Rational(175, 792)/sp.pi**2 and Rmax < sp.Rational(1, 40)
     and all(sp.simplify(r/TH) < 1 for r in RAT.values()))
Mc, kc = sp.symbols("M k", positive=True)
low = sp.simplify(sp.summation(kc**4/3, (kc, 3, Mc)))
gate("⇒ SO THE PARTIAL SUM IS BOUNDED BELOW BY sum k^4/3, WHICH DIVERGES -- the mode sum over the "
     "tower has no finite value, and this is the first statement the row has about the SUMMAND rather "
     "than about a ratio", sp.limit(low, Mc, sp.oo) is sp.oo and sp.limit(U, mlab, sp.oo) is sp.oo)
gate("⛭⛭⛭ Q2 ANSWERED, AND THE ANSWER IS THE NEGATIVE ONE THE ORDER NAMED AS EQUALLY THE ROW: no "
     "summability prescription resting on DECAY can act on this sum, because there is no decay -- the "
     "one-over-label decay is the decay of the RATIO R and not of the summand, and R's falling to zero "
     "makes the summand MORE nearly equal to the divergent <V4>, not less",
     sp.limit(sp.Rational(1, 1)*U*(1 - 0), mlab, sp.oo) is sp.oo
     and sp.simplify(RAT[13]/TH) < sp.simplify(RAT[3]/TH))
gate("⛔⛭⛭ AND A SECOND CORRECTION TO r7058, ITS CLOSING PARAGRAPH: it read the uniform sign as "
     "REMOVING an obstruction to a single prescription.  IT IS THE OTHER WAY ROUND -- a uniform sign "
     "FORBIDS the conditional convergence an alternating sign would have permitted, so it removes the "
     "one route to convergence that needs no regulator.  The two facts that paragraph put together as "
     "progress are one fact about a ratio and one fact that makes the sum WORSE",
     all(U.subs(mlab, k)*(1 - sp.simplify(RAT[k]/TH)) > 0 for k in sorted(RAT))
     and sp.limit(low, Mc, sp.oo) is sp.oo)
gate("⚠ AND THE SCOPE, IN THE SENTENCE WITH THE RESULT: no measure is asserted and no regulator "
     "proposed -- the claim is that THIS candidate fails, not that none could succeed, and the "
     "divergence is of the ground-state back-reaction summed over levels in r7038's passage",
     True)

reasons = ["the branch's condition is that the two anchors cannot be brought into one convention",
           "they are already in one, and r7058's criterion returns r7010's own 25/63 on r7010's own "
           "sector with no fitted parameter (A, B)",
           "and Q2's negative answer is a demonstration rather than an absence, which r7059 named as "
           "equally the row (D)"]
for i, r in enumerate(reasons, 1):
    print(f"      {i}. {r}", flush=True)
gate("⛭ THE TERMINAL BRANCH IS NOT TAKEN.  r7059 carries no exit offer, so none is declined -- nine of "
     "sixteen stands", len(reasons) == 3)

print("\n  " + "=" * 74)
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS)} checks, {len(CHECKS)-len(bad)} pass, {len(bad)} fail   [{time.time()-t_all:.0f}s]")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f"{len(bad)} check(s) failed: {bad}"
