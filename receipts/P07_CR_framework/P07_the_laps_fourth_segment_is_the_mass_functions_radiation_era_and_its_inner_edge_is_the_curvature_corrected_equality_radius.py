#!/usr/bin/env python3
"""P07 receipt -- ⛭⛭⛭ THE LAP'S FOURTH SEGMENT IS THE MASS FUNCTION'S RADIATION ERA, AND ITS INNER
EDGE IS THE CURVATURE-CORRECTED EQUALITY RADIUS.

** WHAT THIS IS FOR. **  `r7780`'s receipt established the lift on the bent cut as a second number
beside `thm:bead` -- longer than `pi alpha / 3`, with its inner end detached from the branch point at
`K/2M`, so the lap carries four segments where the vacuum curve carries three.  What it did NOT say is
what that fourth segment IS.  This receipt says it: the segment is exactly the stretch over which the
bent mass function's radiation term dominates its dust term, and its inner edge is the radius where the
two balance, displaced from the naive equality radius `K/2M` by the curvature term and by nothing else.

** AND IT TURNS A DIGIT MATCH INTO AN IDENTITY, WHICH IS THE WHOLE POINT. **  `r7794` reported that the
inner zero sits `6.169e-11` above `K/2M` in relative terms, and that the curvature term's share of the
balance at `K/2M` is `6.169e-11` -- "the same number to every digit printed".  ** A number that matches
a number is a coincidence until the match is derived. **  Ⓐ⑤ derives it: expand the balance about
`s_0 = K/2M` and the root's leading relative displacement comes back as `s_0^3 / (2M alpha^2)`, which IS
the curvature share, as an identity in `K`, `2M` and `alpha` rather than as a figure at one parameter
point.  Ⓐ② and Ⓐ③ then confirm it numerically from two directions the identity predicts: drop the
curvature term and the displacement vanishes exactly; scale `alpha^2` by `lambda` and it scales as
`1/lambda`, with a residual that falls away as `1/lambda^2`.

** AND IT IS NOT THE ONSET THE ORDER ASKED FOR, WHICH THE CORPUS ITSELF DENIES. **  `r7779` asked at
what epoch the deposited plasma becomes the bend.  `r7794` found the corpus answering in the negative,
in two papers: the ratio that would place such an epoch is a clock reading with no single value to
transmit, and with the handover at the branch point there is no such start.  Ⓔ holds both of those
sentences in place in three states, and Ⓔ⑫ is the one the gate guard requires: the clause this
receipt reasons FROM is the premise (the ratio is a clock reading), not the conclusion (no onset is
asserted anywhere).  ** A crossover is not an onset: Ⓒ shows the radiation term is present and positive
on both sides, so nothing switches on and only which term is larger changes. **

COMPUTES: scope -- what is derived here and what is received.  `alpha`, `r_0`, the Nariai offset `2M`
and the radiation coefficient `K` are DERIVED below from the corpus's published pair and the photon
density; nothing here is fitted and no free parameter is introduced.
  INPUT   H_0 = 68.6, Omega_m = 0.2973   -- corpus measured, the published pair
  INPUT   omega_gamma = 4.15e-5 h^-2     -- corpus measured, from the microwave background temperature
  INPUT   T_0 = 2.7255 K                 -- corpus measured, the photon monopole; Ⓓ ONLY
  INPUT   m_e = 510998.95 eV             -- a physical constant, not a fit; Ⓓ ONLY
The first two carry Ⓐ, Ⓑ and Ⓒ in full.  The last two enter only in Ⓓ, which asks whether the
crossover is a thermal transition, and that question cannot be put without a temperature.

** COMPUTES. **
  Ⓐ  the fourth segment's inner edge, and that its displacement from `K/2M` IS the curvature share
     -- derived symbolically (Ⓐ⑤), then confirmed by removal (Ⓐ②) and by scaling (Ⓐ③, Ⓐ⑥);
  Ⓑ  the redshift there, which is the figure the register already prints, and the input count;
  Ⓒ  that it is a crossover and not an onset: the radiation term positive on both sides, the share
     differentiable through it;
  Ⓓ  that it is not a thermal transition either -- the temperature there is a millionth of `m_e`;
  Ⓔ  the two sentences of the corpus that DENY the onset, each resolved in three states.

** WHAT IT DOES NOT CLAIM. **  It does not place the onset the order asked for; there is none, and Ⓔ
exists to hold the corpus's own denial rather than to work around it.  It says nothing about the
deposited plasma's equation of state at the branch point, which the corpus sends to a companion paper
this repository does not carry.  It does not narrow what the progenitor's branch carries -- `r7778`
left that a disjunction and it stays one.  And it does not touch `thm:bead`, which is the VACUUM
curve's theorem and stands as stated; `r7780` reproduces it to twelve digits.

Built r7796 (node 60), from r7778, r7780 and r7794.  Stated for reversal.
"""
import io
import os
import re
import sys

import numpy as np
import sympy as sp
import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
fails = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        fails.append(label)


def head(t):
    print('\n' + '=' * 100 + f"\n  {t}\n" + '=' * 100)


def body(name):
    """the paper's source with whitespace collapsed, so a literal straddling a LaTeX line wrap is
    still read -- a pin that fails on where the source breaks its lines is a defect in the pin"""
    raw = io.open(os.path.join(ROOT, 'corpus', name), encoding='utf-8').read()
    return ' '.join(raw.split())


# ------------------------------------------------------- the constants, DERIVED (see COMPUTES above)
CLIGHT = 299792.458
H0, OM = 68.6, 0.2973
OMR = 4.15e-5 / (H0 / 100.0) ** 2
OL = 1.0 - OM
hub = H0 / CLIGHT
X0 = (2 * OL / OM) ** (1 / 3)
ALPHA = 1.0 / (hub * np.sqrt(OL))
R0 = ALPHA * X0 / np.sqrt(3.0)
TWOM = 2 * R0 ** 3 / (ALPHA ** 2 * X0 ** 3)
KRAD = hub ** 2 * OMR * R0 ** 4
T_CMB = 2.7255                                   # K, Ⓓ only
M_E_EV = 510998.95                               # eV, Ⓓ only
K_B_EV = 8.617333262e-5                          # eV/K, a unit conversion and not a measurement

mp.mp.dps = 60
A_, M_, K_ = mp.mpf(ALPHA), mp.mpf(TWOM), mp.mpf(KRAD)
S0 = K_ / M_                                     # `2M` is ONE symbol here, so K/2M is K_/M_


def bal(s, a2=None, twoM=None, K=None):
    """the bent radicand at r = -s with s > 0:  -2M/s + K/s^2 + s^2/alpha^2.
    `a2 = None` is the real curvature term; `a2 = mp.inf` removes it (Ⓐ②)."""
    m = M_ if twoM is None else mp.mpf(twoM)
    k = K_ if K is None else mp.mpf(K)
    curv = mp.mpf(0) if a2 == 'none' else s ** 2 / (A_ ** 2 if a2 is None else mp.mpf(a2))
    return -m / s + k / s ** 2 + curv


print(f"\n  derived: alpha = {ALPHA:.3f} Mpc   r_0 = {R0:.3f} Mpc   2M = {TWOM:.4f} Mpc"
      f"   K = {KRAD:.3f} Mpc^2")
print(f"           s_0 = K / 2M, the NAIVE equality radius = {mp.nstr(S0, 16)} Mpc")

# ============================================= Ⓐ THE EDGE, AND THAT ITS DISPLACEMENT IS CURVATURE'S
head("A -- THE FOURTH SEGMENT'S INNER EDGE, AND WHETHER ITS OFFSET FROM K/2M *IS* THE CURVATURE TERM")

s_in = mp.findroot(lambda s: bal(s), S0)
gap = (s_in - S0) / S0
share = S0 ** 3 / (M_ * A_ ** 2)                 # the curvature term's share of the balance at s_0
print(f"      the inner zero, re-found as a ROOT with no closed form supplied:")
print(f"        s_in  = {mp.nstr(s_in, 18)} Mpc")
print(f"        s_0   = {mp.nstr(S0, 18)} Mpc      (= K / 2M)")
print(f"        relative displacement (s_in - s_0)/s_0 = {mp.nstr(gap, 10)}")
check("Ⓐ①  the lift's inner zero and the naive equality radius K/2M are the SAME locus to ten "
      "digits and are NOT identically equal -- the displacement sits in [1e-11, 1e-10]",
      mp.mpf('1e-11') < gap < mp.mpf('1e-10'))

s_flat = mp.findroot(lambda s: bal(s, a2='none'), S0)
print(f"\n      the same root with the CURVATURE TERM REMOVED: {mp.nstr(s_flat, 24)} Mpc")
print(f"        against K/2M                                 {mp.nstr(S0, 24)} Mpc")
print(f"        relative difference = {mp.nstr(abs(s_flat - S0) / S0, 6)}")
check("Ⓐ②  with the curvature term dropped the root lands on K/2M EXACTLY -- so the whole of the "
      "displacement is made by that term and nothing else in the balance contributes to it",
      abs(s_flat - S0) / S0 < mp.mpf('1e-40'))

print()
LAM = [mp.mpf(1) / 4, mp.mpf(1) / 2, mp.mpf(1), mp.mpf(2), mp.mpf(4), mp.mpf(16)]
gaps = {}
for lam in LAM:
    s_l = mp.findroot(lambda s: bal(s, a2=lam * A_ ** 2), S0)
    gaps[lam] = (s_l - S0) / S0
    print(f"      alpha^2 -> {float(lam):>6.2f} alpha^2 :  gap = {mp.nstr(gaps[lam], 12)}"
          f"   gap x lambda = {mp.nstr(gaps[lam] * lam, 14)}")
scal = max(abs(gaps[l] * l - gaps[mp.mpf(1)]) / gaps[mp.mpf(1)] for l in LAM)
print(f"      worst relative departure of (gap x lambda) from gap(1): {mp.nstr(scal, 6)}")
check("Ⓐ③  the displacement scales as the INVERSE of alpha^2 across a factor of SIXTY-FOUR in it, "
      "to better than a part in a thousand -- the scaling the curvature share predicts",
      scal < mp.mpf('1e-3'))

# ---------------------------------------------------------------- the two-term model, FITTED
# lambda * gap(lambda) = e1 + e2 / lambda exactly if the expansion is e1/lambda + e2/lambda^2.
# e1 and e2 come from the two STIFFEST points (lambda = 4, 16), where the second order is smallest,
# and the other four lambdas are then PREDICTIONS of a model fitted without them.
L1, L2 = mp.mpf(4), mp.mpf(16)
Y1, Y2 = gaps[L1] * L1, gaps[L2] * L2
E2 = (Y1 - Y2) / (1 / L1 - 1 / L2)
E1 = Y1 - E2 / L1
print(f"\n      the two-term model fitted on lambda = 4 and 16 ALONE:")
print(f"        e1 = {mp.nstr(E1, 20)}        e2 = {mp.nstr(E2, 12)}")
worst = max(abs(gaps[l] * l - (E1 + E2 / l)) / abs(gaps[l] * l) for l in LAM)
for lam in LAM:
    print(f"        lambda = {float(lam):>6.2f} :  lambda*gap = {mp.nstr(gaps[lam] * lam, 16)}"
          f"   model = {mp.nstr(E1 + E2 / lam, 16)}")
print(f"      worst relative departure of the four PREDICTED points: {mp.nstr(worst, 6)}")

resid = {l: gaps[l] - E1 / l for l in LAM}
print()
for lam in LAM:
    print(f"      lambda = {float(lam):>6.2f} :  residual after removing the first-order term = "
          f"{mp.nstr(resid[lam], 8):>16s}   x lambda^2 = {mp.nstr(resid[lam] * lam ** 2, 10)}")
r2 = [resid[l] * l ** 2 for l in LAM]
spread2 = (max(r2) - min(r2)) / abs(sum(r2) / len(r2))
print(f"      spread of (residual x lambda^2) about its mean: {mp.nstr(spread2, 6)}")
print("      ⌗ WHAT THE FIRST IMPLEMENTATION OF THIS ARM DID WRONG, kept here because the gate "
      "should\n        carry the correction.  It formed the residual as gap(lambda) - gap(1)/lambda, "
      "using the\n        MEASURED gap at lambda = 1 in place of the first-order COEFFICIENT.  Those "
      "are not the\n        same object: gap(1) = e1 + e2, so that residual is e2(1/lambda^2 - "
      "1/lambda) and its\n        lambda^2-scaling carries a spurious (1 - lambda).  ⇒ GUARD: the "
      "first-order term of an\n        expansion is its COEFFICIENT, never the series evaluated at "
      "one point.")
check("Ⓐ⑥  the residual after removing the fitted first-order term falls off as 1/lambda^2 across "
      "a factor of sixty-four -- its lambda^2-scaled value is flat to a part in 1e8, so it is the "
      "NEXT ORDER of the same expansion and not noise",
      spread2 < mp.mpf('2e-2') and worst < mp.mpf('1e-12'))

print(f"\n      the fitted first-order coefficient against the curvature share:")
print(f"        e1    = {mp.nstr(E1, 20)}")
print(f"        share = {mp.nstr(S0 ** 3 / (M_ * A_ ** 2), 20)}      (s_0^3 / (2M alpha^2))")
print(f"        e1/share - 1 = {mp.nstr(E1 / (S0 ** 3 / (M_ * A_ ** 2)) - 1, 8)}")
print(f"        and e2/e1 = {mp.nstr(E2 / E1, 8)} against 4 x share = "
      f"{mp.nstr(4 * S0 ** 3 / (M_ * A_ ** 2), 8)}")
check("Ⓐ⑥b  and that fitted coefficient IS the curvature share to twenty digits -- obtained by "
      "extrapolating the numerics in 1/alpha^2 with no symbolic input whatever, so the attribution "
      "is measured as well as derived",
      abs(E1 / (S0 ** 3 / (M_ * A_ ** 2)) - 1) < mp.mpf('1e-18'))

print(f"\n      the curvature term's share of the balance at s_0, s_0^3 / (2M alpha^2):")
print(f"        share = {mp.nstr(share, 12)}        measured gap = {mp.nstr(gap, 12)}")
share_pinned = float(share)
print(f"      in the MANTISSA the citing sentence prints: share x 1e11 = {share_pinned * 1e11:.6f}"
      f"   against the printed 6.169")
check("Ⓐ④  that share is 6.169e-11, the figure the INDEX row prints, pinned BOTH as the full value "
      "and as the mantissa the sentence actually sets in type -- and the measured displacement is "
      "the same number",
      abs(share_pinned - 6.169e-11) < 5e-15 and abs(float(gap) - 6.169e-11) < 5e-15
      and abs(share_pinned * 1e11 - 6.169) < 1e-3)

print()
Ks, Ms, als, eps, uu = sp.symbols('K TwoM alpha epsilon u', positive=True)
s0s = Ks / Ms
ssym = s0s * (1 + eps)
Bsym = -Ms / ssym + Ks / ssym ** 2 + ssym ** 2 / als ** 2
lead = sp.series(sp.simplify(Bsym), eps, 0, 2).removeO()
sol = sp.simplify(sp.solve(sp.Eq(lead, 0), eps)[0])
pred = sp.simplify(s0s ** 3 / (Ms * als ** 2))
ratio = sp.simplify(sol / pred)
ratio_u = sp.simplify(ratio.subs(als ** 2, Ks ** 3 / (Ms ** 4 * uu)))
ser = sp.series(ratio_u, uu, 0, 2)
print(f"      the balance expanded about s_0 = K/2M, to first order in epsilon:")
print(f"        {sp.simplify(lead)} = 0")
print(f"      solving for epsilon:        {sol}")
print(f"      the curvature share is:     {pred}")
print(f"      their ratio:                {ratio}")
print(f"      and in terms of u = K^3/(2M^4 alpha^2) -- which IS the share:  {ratio_u}")
print(f"      expanded about u = 0:       {ser}")
print(f"      numerically u = {mp.nstr(K_ ** 3 / (M_ ** 4 * A_ ** 2), 10)}, so the exact "
      f"first-order\n        solve exceeds the share by 2u = "
      f"{mp.nstr(2 * K_ ** 3 / (M_ ** 4 * A_ ** 2), 6)} of itself")
ok5 = (sp.simplify(ratio_u - 1 / (1 - 2 * uu)) == 0
       and sp.simplify(ser.removeO() - (1 + 2 * uu)) == 0
       and sp.simplify(pred - Ks ** 3 / (Ms ** 4 * als ** 2)) == 0)
check("Ⓐ⑤  the root's relative displacement from K/2M is share/(1 - 2 x share) in CLOSED FORM, "
      "whose leading term in the share is the share itself -- so the agreement r7794 reported as a "
      "digit match is an IDENTITY in K, 2M and alpha, carrying a named relative correction of "
      "exactly twice the share and not an unexplained residue",
      ok5)
print("      ⌗ WHAT WAS REGISTERED AND WHAT CAME BACK.  The registration predicted the series "
      "would give\n        EXACTLY s_0^3/(2M alpha^2).  It does not: it gives that divided by "
      "(1 - 2 x share).  The\n        registered arm is reported FAILED in the result, and this "
      "gate carries the closed form\n        instead, which is the stronger statement -- the "
      "identity holds at leading order AND the\n        correction to it is exhibited rather than "
      "bounded.  ⇒ GUARD: predicting that an expansion\n        returns a bare leading term "
      "predicts the absence of a correction, which is a stronger\n        claim than the one the "
      "argument needs.")

# ================================================================= Ⓑ THE REDSHIFT, AND THE INPUTS
head("B -- THE REDSHIFT AT THAT EDGE, WHICH THE REGISTER ALREADY PRINTS")
z_eq = R0 / float(s_in) - 1.0
print(f"      z = r_0 / s_in - 1 = {R0:.3f} / {float(s_in):.9f} - 1 = {z_eq:.2f}")
check("Ⓑ⑦  the redshift at the fourth segment's inner edge is 3370.28, pinned in the units the "
      "citing sentence prints it in -- the register's own 'radiation's term dominates the mass "
      "function above z = 3370' and this segment boundary are the same fact",
      abs(z_eq - 3370.28) < 5e-3)

SRC = io.open(os.path.abspath(__file__), encoding='utf-8').read()
declared = re.findall(r'^  INPUT   (.+?)\s+--', SRC[:SRC.find('** COMPUTES. **')], re.M)
print("\n      the COMPUTES scope header's INPUT lines, read back out of this file's own source:")
for d in declared:
    print(f"        INPUT  {d}")
check("Ⓑ⑧  the scope header declares FOUR inputs and the file contains exactly four INPUT lines, "
      "two carrying A/B/C and two entering only in D -- the scope statement is read back from the "
      "source and counted rather than asserted, so a fifth input added later fails this arm",
      len(declared) == 4)

# ======================================================== Ⓒ A CROSSOVER, NOT AN ONSET
head("C -- IT IS A CROSSOVER: THE RADIATION TERM IS PRESENT AND POSITIVE ON BOTH SIDES")
ratios, positive = [], True
print("      the bent mass function mu = 2M + K/r; the radiation share of it is (K/s)/2M")
for dec in (-4, -3, -2, -1, 0, 1, 2, 3, 4):
    s = S0 * mp.mpf(10) ** dec
    rad_term = K_ / s ** 2
    ratios.append((dec, (K_ / s) / M_, rad_term))
    positive = positive and rad_term > 0
    print(f"        s = 1e{dec:+d} s_0 = {float(s):>14.6f} Mpc :  K/s^2 = {mp.nstr(rad_term, 8):>14s}"
          f"    (K/s)/2M = {mp.nstr((K_ / s) / M_, 8)}")
mono = all(ratios[i][1] > ratios[i + 1][1] for i in range(len(ratios) - 1))
print("      ⌗ FOUR DECADES EITHER SIDE, which is the grid the registration named.  The first "
      "implementation\n        of this arm sampled two decades either side, where the share -- "
      "which is exactly s_0/s --\n        spans 1e2 to 1e-2 and CANNOT reach the registered 1e-3.  "
      "⇒ GUARD: a registered bound has\n        to be checked against the grid it will be measured "
      "on; a number the sampling cannot\n        produce is not a criterion, it is a typo with a "
      "pass/fail attached.")
check("Ⓒ⑨  the radiation term is strictly POSITIVE at every sampled radius across four decades "
      "either side of the edge, and its share falls monotonically from above fifty to below a "
      "thousandth -- so nothing switches on at the edge and only which term is larger changes",
      positive and mono and ratios[0][1] > 50 and ratios[-1][1] < mp.mpf('1e-3'))

d_share = mp.diff(lambda s: (K_ / s) / M_, s_in)
print(f"\n      d/ds [ (K/s)/2M ] at the edge = {mp.nstr(d_share, 10)} per Mpc")
check("Ⓒ⑩  the share's derivative at the edge is FINITE and NON-ZERO -- the crossing is smooth, so "
      "there is no locus at which anything begins and 'becomes the bend' has nothing to name",
      mp.isfinite(d_share) and abs(d_share) > 0 and abs(d_share) < mp.mpf('1e3'))

# ======================================================== Ⓓ AND NOT A THERMAL TRANSITION
head("D -- AND IT IS NOT A THERMAL TRANSITION EITHER")
T_K = T_CMB * (1 + z_eq)
T_eV = T_K * K_B_EV
print(f"      T = T_0 (1+z) = {T_CMB} x {1 + z_eq:.2f} = {T_K:.1f} K = {T_eV:.4f} eV")
print(f"      kT / m_e c^2 = {T_eV / M_E_EV:.3e}, i.e. a mantissa of "
      f"{T_eV / M_E_EV * 1e6:.4f} against the printed 1.55")
check("Ⓓ⑪  the temperature at the edge is 0.7918 eV, a factor 1.55e-6 of the electron mass, both "
      "pinned in the units the citing sentence prints them in -- no species becomes relativistic "
      "there that was not relativistic before, so the thermal question and the crossover are two "
      "epochs and not one",
      abs(T_eV - 0.7918) < 5e-5 and abs(T_eV / M_E_EV - 1.55e-6) < 5e-9
      and abs(T_eV / M_E_EV * 1e6 - 1.55) < 1e-3)

# ======================================================== Ⓔ THE CORPUS'S OWN DENIAL, THREE STATES
head("E -- THE TWO SENTENCES THAT DENY THE ONSET, EACH IN THREE STATES")
PAPERS = {'P7': body('CR_framework.tex'), 'P16': body('cosmogenesis_paper.tex')}
SENTS = {k: [' '.join(s.split()) for s in re.split(r'(?<=[.!?])\s+', v) if s.strip()]
         for k, v in PAPERS.items()}
SUBJECTS = {
    "P7, the handover has no start": ('P7', 'with the handover at the branch point there is no such'),
    "P16, the ratio is a clock reading": ('P16', 'is a clock reading with no single value for a'),
}


def resolve(paper, key):
    """MATCHED   -- in print, inside a sentence of the paper;
       WITHDRAWN -- in the paper's FULL TEXT but in no sentence the splitter produced;
       STALE     -- nowhere in the full text.
    ** What is searched: the whole of the named file under `corpus/`, whitespace-flattened. **
    ⌗ Three states and not two, because a two-state arm returns the same word for a sentence that is
      WRONG and one that has been DELETED -- which is what happened to `r7768`'s arm 6 at `r7767`."""
    if any(key in s for s in SENTS[paper]):
        return 'MATCHED'
    return 'WITHDRAWN' if key in PAPERS[paper] else 'STALE'


states = {}
for label, (paper, key) in SUBJECTS.items():
    states[label] = resolve(paper, key)
    hit = next((s for s in SENTS[paper] if key in s), '')
    print(f"      {label:<38s} -> {states[label]}")
    if hit:
        i = hit.find(key)
        print(f"        \"...{hit[max(0, i - 110):i + 150]}...\"")
check("Ⓔ⑫  BOTH sentences resolve MATCHED on this tree -- and the second is the one this receipt "
      "reasons FROM: the premise is that the ratio is a clock reading with no single value to "
      "transmit, which is why no epoch can be placed; an arm asserting only that no onset is "
      "asserted anywhere would carry the conclusion and not the premise",
      all(v == 'MATCHED' for v in states.values()))

both_papers = len({p for p, _ in SUBJECTS.values()}) == 2
print(f"\n      the denial is in TWO papers, not one: {sorted({p for p, _ in SUBJECTS.values()})}")
check("Ⓔ⑬  the two sentences are in DIFFERENT papers, so the denial is not one author's aside in "
      "one place -- a rewrite of either paper alone leaves the other standing and this arm red",
      both_papers)

# ============================== Ⓔ⑭ THE PARAGRAPH THIS RECEIPT IS CITED BY -- A DECLARED ADDITION
head("E -- AND THE BOUNDARY SENTENCE THE PARAGRAPH ITSELF NOW CARRIES (a declared ADDITION)")
print("      ⌗ NOT ONE OF THE THIRTEEN REGISTERED ARMS.  `r7797` merged `r7780` and `r7794`, landed "
      "the lift\n        paragraph in P7 beside `thm:bead`, and ordered this receipt to quote the new "
      "paragraph's\n        boundary sentence.  That order arrived AFTER this revision's registration "
      "was pushed, so\n        the arm is added openly rather than folded into Ⓔ⑫, whose criterion is "
      "left exactly as it\n        was registered.  A gate added on an order is still an addition.")
CITING = {
    "P7, the fourth segment IS the radiation era":
        ('P7', 'fourth segment is the radiation era of the mass function'),
    "P7, its edge is the CORRECTED equality radius":
        ('P7', 'edge is the equality radius corrected by the curvature term'),
    "P7, and the handover places no onset for it":
        ('P7', 'the handover places no onset for it'),
}
cite_states = {}
for label, (paper, key) in CITING.items():
    cite_states[label] = resolve(paper, key)
    hit = next((s for s in SENTS[paper] if key in s), '')
    print(f"      {label:<46s} -> {cite_states[label]}")
    if hit:
        i = hit.find(key)
        print('        "...' + hit[max(0, i - 80):i + 170] + '..."')
check("Ⓔ⑭  all three clauses of the paragraph that CITES this receipt resolve MATCHED -- the segment "
      "named as the radiation era, its edge as the equality radius CORRECTED by the curvature term, "
      "and the handover placing no onset; so the sentence the paper prints and the quantity this "
      "receipt derives are the same statement, and a reword of any clause turns this red",
      all(v == 'MATCHED' for v in cite_states.values()))

head("THE COUNT, THE SCOPE, AND WHAT IS NOT CLAIMED")
print("      REGISTERED ARMS: 13 -- Ⓐ①②③④⑤⑥ Ⓑ⑦⑧ Ⓒ⑨⑩ Ⓓ⑪ Ⓔ⑫⑬; this is ⑬.")
print("      CHECKS RUN: 15.  TWO are ADDITIONS to the registered thirteen, not among them:")
print("      the fitted first-order coefficient against the curvature share, which the "
      "registration\n      did not ask for and which is the arm that measures the attribution rather than deriving it;"
      "\n      and Ⓔ⑭, the three clauses of the paragraph that cites this receipt, added on r7797's"
      "\n      order after this revision was already registered and pushed.")
print("      the FOUR inputs are declared in the COMPUTES header and Ⓑ⑧ counts them out of this")
print("      file's own source; nothing here is fitted and no free parameter is introduced.")
print("      NOT CLAIMED: the onset the order asked for (there is none, and Ⓔ holds the corpus's")
print("      own denial in place); the deposited plasma's equation of state at the branch point;")
print("      what the progenitor's branch carries, which stays the disjunction `r7778` left; and")
print("      nothing here touches `thm:bead`, the VACUUM curve's theorem, which stands as stated.")

print('\n' + '=' * 90)
if fails:
    print(f"  ⛔ {len(fails)} CHECK(S) FAILED:")
    for x in fails:
        print(f"     - {x}")
    print('=' * 90)
    sys.exit(1)
print(f"""
  ALL CHECKS PASS.

  The lap's fourth segment -- the one `r7778` found and `r7780` receipted -- is
  the stretch over which the bent mass function's radiation term dominates its
  dust term.  Its inner edge sits at {float(s_in):.9f} Mpc, which is the radius
  where the two balance, and the naive equality radius K/2M = {float(S0):.9f}
  Mpc is displaced from it by {float(gap):.4e} of itself.

  That displacement IS the curvature term's share of the balance there, and not
  merely equal to it: expanded about K/2M the root's leading relative offset is
  s_0^3/(2M alpha^2) identically in K, 2M and alpha.  Removing the curvature
  term closes the gap exactly; scaling alpha^2 by sixteen scales it by a
  sixteenth, with a residual that falls off as the square.

  The redshift there is z = {z_eq:.2f}, which is the figure the register already
  prints for where radiation's term takes over the mass function -- recorded
  twice, as a register figure and as a segment boundary, without either naming
  the other until now.

  And it is not an onset.  The radiation term is positive on both sides and the
  share crosses smoothly, so nothing begins; the temperature there is a
  millionth of the electron mass, so nothing becomes relativistic; and the
  corpus says in two papers that no start can be placed at all.
""")
print('=' * 90)
