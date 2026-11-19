#!/usr/bin/env python3
r"""r7829 (cc66) -- PO-24's discharge test: the in-force refit on a second, independently built arm.

COMPUTES: whether the refit at the configuration P15 adjudicates reproduces on an arm built
  separately from r7828's, which is what PO-24's clause -- as r7827 rewrote it -- defines discharge
  to be; and what the two arms do and do not agree on.
  INPUT  the arm:        r7823's split, IMPORTED as a module and not re-described: Planck plik_lite
                         TT below the shipped PlanckActCut multipole (114 bins) plus ACT DR6 cmbonly
                         TT bandpowers selected on WINDOW SUPPORT (28) = 142 points, against
                         r7828's 150 bandpowers
  INPUT  the configuration: r = 0.9918, lD = 1489.5783 HELD FIXED, exponent ONE, A_s9 = 2.1 -- taken
                         from r7828's own banked run and PARSED from it here, not re-derived
  INPUT  this arm's LCDM: r7827's banked fit_lcdm_a21, the same convention and the same code
  OUTPUT the refitted chi2, its Delta against this arm's LCDM, whether the minimum is INTERIOR, and
         which of the seven registered checks held

** IT REPRODUCES, AND THAT IS THE DISCHARGE. **

  construction, refitted   111.0027  (Planck 85.2746, ACT 25.7282)   r7828: 137.4859
  LCDM on the same arm     114.8370                                  r7828: 139.8557
  Delta chi2                -3.8343                                  r7828:  -2.3697
  H0 / n_s           67.7407 / 0.962136                   r7828: 67.3934 / 0.959284
  minimum            INTERIOR -- 160 of 160 evaluations in bounds, no parameter on a box edge

The two arms were built separately, differ by eight bandpowers, each selected on its own window
support, and agree on H0 to 0.35, on n_s to 0.003, and on the sign and size of the refit: the
Deltas are apart by 1.4646, inside the +/- 2.0 this revision registered BEFORE running.
=> ** So PO-24, by the clause as r7827 rewrote it -- decided by a refit, discharged when the refit
   at the adjudicated configuration reproduces on a second, independently built arm -- IS
   DISCHARGED.  Striking the row is 69's; THE_REGISTER.md is untouched here. **

** AND WHAT IT IS NOT, registered as (6) BEFORE the run so a reproducing result could not be read
   as more than it is. **  -3.8343 on 142 points is TWO MODELS BEING LEVEL.  It is not a preference
   for the construction, not a detection, and not evidence that the construction is correct.  What
   is discharged is the clause, and nothing wider.

** ONE REGISTERED PREDICTION FAILED, AND ITS FAILURE IS THE SECOND FINDING. **
(5) said the in-force lD and the per-trial lD would be "genuinely different objects, apart by more
than 0.3" in the refitted Delta chi2.  They are apart by 0.2347 -- in-force -3.8343 against
r7827's per-trial -3.5996, about six per cent.  ** So the refit is almost INSENSITIVE to which lD
estimator is used, even though the fixed-cosmology tilt figures were wrecked by the neighbouring
exponent error. **  My reasoning behind (5) was wrong: I assumed the estimator choice would surface
in the refit the way alpha's double-count surfaced in the tilt, and it does not, because the refit
absorbs it.  => GUARD: a statistic's sensitivity to a nuisance choice has to be MEASURED on the
statistic that decides, never inherited from a different one.  I inherited it; the measurement
corrected me.  ⌗ The failure strengthens the verdict rather than weakening it -- the statistic
PO-24 now turns on is robust to the choice that made the tilt numbers unreliable.

** THE WITHDRAWALS THIS RECEIPT CARRIES. **  r7826's 9.02 and this seat's own r7827 1.0569 are
withdrawn as DOUBLE-COUNTED: 60 established at r7828 that alpha = 1.70 is already folded into the
in-force lD (1951.9/sqrt(1.70) = 1497.0390, then 1489.5783 after the one-rate move).  => The 8.53x
"arm-sensitivity" this seat routed to 69 was TWO ARMS APPLYING ONE ERROR AT DIFFERENT STRENGTHS,
not two arms disagreeing.  GUARD (60's): a folded parameter is folded once.

⚠ SCOPE.  TT only; tau held at 0.054 in every arm so it absorbs in none; A_s9 held at 2.1, exactly
  degenerate under a per-block profiled amplitude (measured at r7827 (4)); the Planck-by-ACT
  covariance neglected between DIFFERENT multipoles of the two experiments and never within one, as
  r7820's split guarantees by using no multipole twice.  And this receipt does NOT adjudicate which
  arm is the better arm: two arms agreeing BOUNDS a figure's arm-dependence and does not make
  either one correct.
"""
import json
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R7829 = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                     'r7829_cc66_the_in_force_refit_on_an_independent_arm', 'out',
                     'r7829_in_force_refit.json')
R7828 = os.path.join(
    ROOT, 'computations', 'beyond_the_wall',
    'r7828_60_po24_recomputed_at_the_papers_own_configuration_and_the_size_is_a_seventh_with_the_'
    'opposite_sign', 'runs', 'r7828_refit.json')
R7827_LCDM = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                          'r7827_cc66_the_adjudicated_endpoint_on_an_independent_arm', 'out',
                          'fit_lcdm_a21.npz')

PASSED, FAILED = [], []


def head(t):
    print("\n" + "=" * 92 + f"\n  {t}\n" + "=" * 92)


def check(label, ok):
    (PASSED if ok else FAILED).append(label)
    print(f"\n  [{'PASS' if ok else 'FAIL'}] {label}")


J = json.load(open(R7829, encoding='utf-8'))
# ** 60's FIGURES ARE PARSED OUT OF ITS OWN BANKED RUN, not remembered. **  A discharge test that
# hardcodes the thing it must reproduce compares against a memory of it and stays green if it moves.
S = json.load(open(R7828, encoding='utf-8'))
LC = float(np.load(R7827_LCDM)['chi2'])
X, SX = J['x'], S['x']
D, SD = J['dchi2'], S['dchi2']

# ======================================================= Ⓐ① THE PRECONDITION
head("A -- THE PRECONDITION: IS THE LCDM REFERENCE THE SAME OBJECT r7827 BANKED")
print(f"\n      LCDM read from r7827's bank   {LC:.4f}")
print(f"      the figure this run used      {J['chi2_lcdm']:.4f}")
check("Ⓐ① the LCDM reference is r7827's own banked fit on the same arm under the same convention, "
      "114.8370, read from the bank here rather than re-fitted -- so the Delta below is against a "
      "number this seat has already published and not against a fresh fit that could have drifted",
      abs(LC - 114.8370) < 0.05 and abs(LC - J['chi2_lcdm']) < 1e-9)

# ======================================================= Ⓑ② THE DISCHARGE
head("B -- THE DISCHARGE: DOES THE REFIT REPRODUCE, IN SIGN AND IN SIZE")
print(f"\n      {'':30}{'this arm':>12}{'r7828 (60)':>14}")
print(f"      {'construction, refitted':<30}{J['chi2']:>12.4f}{S['chi2']:>14.4f}")
print(f"      {'  its Planck block':<30}{J['chi2_planck']:>12.4f}")
print(f"      {'  its ACT block':<30}{J['chi2_act']:>12.4f}")
print(f"      {'LCDM on the same arm':<30}{J['chi2_lcdm']:>12.4f}{S['chi2_lcdm']:>14.4f}")
print(f"      {'Delta chi2':<30}{D:>+12.4f}{SD:>+14.4f}")
print(f"      Deltas apart by {abs(D - SD):.4f}   registered bound 2.0")
check("Ⓑ② IT REPRODUCES: the construction refitted on this arm reaches 111.0027 against this arm's "
      "LCDM 114.8370, Delta chi2 = -3.8343, against r7828's -2.3697 -- the same sign and apart by "
      "1.4646, inside the +/- 2.0 registered BEFORE the run. ⇒ PO-24's clause as r7827 rewrote it "
      "is satisfied, and its registered negative (a POSITIVE Delta, which would mean no "
      "reproduction and no strike) did NOT fire",
      abs(J['chi2'] - 111.0027) < 0.05 and abs(D + 3.8343) < 1.8e-3
      and abs(SD + 2.3697) < 6.0e-4 and abs(abs(D - SD) - 1.4646) < 7.0e-4
      and abs(J['chi2_planck'] - 85.2746) < 0.04 and abs(J['chi2_act'] - 25.7282) < 0.012
      and D < 0.0 and abs(D - SD) < 2.0)

# ======================================================= Ⓒ③ INTERIOR
head("C -- INTERIOR, WHICH THE ORDER REQUIRES: A MINIMUM ON AN EDGE WOULD BE A LIMIT")
print(f"\n      edges reported: {J['edge'] if J['edge'] else 'NONE'}")
print(f"      evaluations {J['nfev']} ({J['nfev_inbounds']} in bounds)")
print(f"      H0 {X[0]:.4f}  omega_b {X[1]:.6f}  omega_c {X[2]:.6f}  n_s {X[3]:.6f}")
check("Ⓒ③ the minimum is INTERIOR -- no parameter within 1e-4 of a box bound, and 160 of 160 "
      "evaluations landed in bounds, so the simplex never worked against a wall. ⌗ This gate exists "
      "because this row keeps producing boundary-truncated minima: the geometric-part ratio's is on "
      "omega_b's upper and omega_c's lower bound on BOTH arms, which is what makes that figure a "
      "limit and not a value. Here there is no edge, so -3.8343 is a value",
      not J['edge'] and J['nfev'] == 160 and J['nfev_inbounds'] == 160)

# ======================================================= Ⓓ④ THE SAME POINT
head("D -- TWO ARMS, ONE POINT")
print(f"\n      {'':12}{'this arm':>12}{'r7828':>14}")
for i, nm in enumerate(('H0', 'omega_b', 'omega_c', 'n_s')):
    print(f"      {nm:<12}{X[i]:>12.6f}{SX[i]:>14.6f}")
check("Ⓓ④ the two arms land on the same point: H0 67.7407 against 67.3934 and n_s 0.962136 against "
      "0.959284, inside the registered |dH0| < 2.5 and |dn_s| < 0.025. ⇒ Measured against r7828's "
      "own banked run, parsed here, so this comparison moves if 60's figures move",
      abs(X[0] - 67.7407) < 0.03 and abs(X[1] - 0.022206) < 1.1e-5
      and abs(X[2] - 0.118237) < 5.5e-5 and abs(X[3] - 0.962136) < 4.5e-4
      and abs(SX[0] - 67.3934) < 0.03 and abs(SX[3] - 0.959284) < 4.5e-4
      and abs(X[0] - SX[0]) < 2.5 and abs(X[3] - SX[3]) < 0.025)

# ======================================================= Ⓔ⑤ THE PREDICTION THAT FAILED
head("E -- ⚠ THE REGISTERED PREDICTION THAT FAILED, AND IT IS THE SECOND FINDING")
print(f"\n      in-force lD {J['lD']}, held fixed   Delta chi2 {D:+.4f}")
print(f"      per-trial lD, r7827's adj_a100     Delta chi2 {J['r7827_pertrial_dchi2']:+.4f}")
print(f"      apart by {J['estimators_apart']:.4f}   registered threshold 0.3  -> FAILED")
check("Ⓔ⑤ ⚠ THIS PREDICTION FAILED AND IS RECORDED AS FAILED: the two lD estimators are apart by "
      "only 0.2347 in the refitted Delta chi2, not the > 0.3 registered. ⇒ The refit is almost "
      "INSENSITIVE to which lD estimator is used -- about six per cent -- even though the "
      "fixed-cosmology tilt figures were wrecked by the neighbouring exponent error. My reasoning "
      "was wrong: I assumed the estimator choice would surface in the refit the way alpha's "
      "double-count surfaced in the tilt, and it does not, because the refit absorbs it. ⇒ GUARD: "
      "measure a statistic's sensitivity to a nuisance choice ON the statistic that decides, never "
      "inherit it from a different one. ⌗ The failure STRENGTHENS the verdict: what PO-24 now turns "
      "on is robust to the choice that made the tilt numbers unreliable",
      J['estimators_apart'] < 0.3 and abs(J['estimators_apart'] - 0.2347) < 1.1e-4)

# ======================================================= Ⓕ⑥ lD IS HELD, MEASURED NOT READ
head("F -- lD IS HELD FIXED, MEASURED ON THE BUILDER'S OWN OUTPUT")
# ** THIS TESTS THE PROPERTY, NOT A VARIABLE NAME. **  The first version asserted the string
# 'LD_INFORCE' appeared in the builder's source and that 'cr_supp' did not.  That is a weak proxy:
# a rename defeats it, a name in the body does not prove the constant reaches the returned
# expression, and it minted a SOURCE/TOKEN quote-pin key on another file's source text.  ⇒ What
# "held fixed" MEANS is that the suppression at a given multipole depends only on r and lD and NOT
# on the cosmology.  So it is measured: build the theory at two well-separated cosmologies, divide
# out each one's own unsuppressed spectrum, and the recovered suppression must be THE SAME curve --
# and must equal the analytic fixed-lD form.  A per-trial lD would make the two differ, because
# r7827's own per-trial lD moved with the fit.
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                'r7829_cc66_the_in_force_refit_on_an_independent_arm'))
import refit as RF                                                         # noqa: E402

PV_A = (67.740724, 0.022206, 0.118237, 0.962136)        # the fitted point
PV_B = (72.000000, 0.024000, 0.100000, 1.020000)        # deliberately far from it
LPROBE = 2000
_i = LPROBE - 2


def _recovered(pv):
    H0, ombh2, omch2, ns = pv
    d, _dp = RF.FJ.run(H0, ombh2, omch2, RF.AS9_FIXED * 1e-9, ns)
    unsup = d[2:RF.FJ.LMAX + 1, 0]
    return float(RF.spectrum(pv)[_i] / unsup[_i])


SA, SB = _recovered(PV_A), _recovered(PV_B)
ANALYTIC = float(np.exp(-1.0 * (0.9918 ** 2 - 1.0) * (LPROBE / 1489.5783) ** 2))
print(f"\n      suppression recovered at l = {LPROBE}:")
print(f"        at the fitted point   {SA:.12f}")
print(f"        at a far cosmology    {SB:.12f}")
print(f"        analytic, fixed lD    {ANALYTIC:.12f}")
print(f"        the two cosmologies differ by {abs(SA - SB):.3e}")
check("Ⓕ⑥ lD is HELD FIXED, and that is MEASURED rather than read off a variable name: the "
      "suppression recovered from the builder's own output at l = 2000, by dividing out each "
      "cosmology's own unsuppressed spectrum, is the SAME at the fitted point and at a deliberately "
      "far cosmology -- identical to better than 1e-12 -- and equals the analytic fixed-lD form "
      "exp(-(r^2-1)(l/1489.5783)^2). ⇒ A per-trial lD could not do that, because r7827's per-trial "
      "lD moved with the fit. ⌗ The first version of this gate asserted a STRING was present in "
      "another file's source; that is defeated by a rename, does not prove the constant reaches the "
      "returned expression, and minted a quote-pin key for a claim better made by measurement",
      abs(SA - SB) < 1e-12 and abs(SA - ANALYTIC) < 1e-12
      and abs(J['lD'] - 1489.5783) < 1e-9 and abs(J['r'] - 0.9918) < 1e-12
      and abs(J['as9'] - 2.1) < 1e-12 and J['n_points'] == 142)

# ======================================================= Ⓖ⑦ THE COUNT AND WHAT IS NOT CLAIMED
head("G -- THE SEVEN REGISTERED CHECKS, AND WHAT IS NOT CLAIMED")
for k, v in sorted(J['predictions'].items()):
    print(f"      {'HELD  ' if v else 'FAILED'}  {k}")
print(f"\n      reproduces: {J['reproduces']}")
check("Ⓖ⑦ six of the seven registered checks held and ONE FAILED, and the failed one is in this "
      "receipt's own gate text rather than only in RESULT.md. ⇒ And the claim is kept to its "
      "registered size: -3.8343 on 142 points is TWO MODELS BEING LEVEL -- not a preference for "
      "the construction, not a detection, not evidence it is correct. What is discharged is PO-24's "
      "clause and nothing wider, and STRIKING THE ROW IS 69's: THE_REGISTER.md is untouched here",
      sum(1 for v in J['predictions'].values() if v) == 6
      and sum(1 for v in J['predictions'].values() if not v) == 1
      and J['reproduces'] is True)

# ============== THE PRINTED FIGURES, PINNED BY COMPARISON SO A GATE CAN SEE THEM.  Each is a
# ============== two-sided comparison on a quantity computed above, inside the coarser of half the
# ============== last printed digit and 0.05 per cent of |X| -- the corpus's own allowance.
PINS = {
    'the refitted chi2, 111.0027':        abs(J['chi2'] - 111.0027) < 0.05,
    'its Planck block, 85.2746':          abs(J['chi2_planck'] - 85.2746) < 0.04,
    'its ACT block, 25.7282':             abs(J['chi2_act'] - 25.7282) < 0.012,
    "this arm's LCDM, 114.8370":          abs(J['chi2_lcdm'] - 114.8370) < 0.05,
    'the Delta, -3.8343':                 abs(D + 3.8343) < 1.8e-3,
    "r7828's Delta, -2.3697":             abs(SD + 2.3697) < 6.0e-4,
    'the Deltas apart by 1.4646':         abs(abs(D - SD) - 1.4646) < 7.0e-4,
    "r7828's refit, 137.4859":            abs(S['chi2'] - 137.4859) < 0.06,
    "r7828's LCDM, 139.8557":             abs(S['chi2_lcdm'] - 139.8557) < 0.06,
    'H0, 67.7407':                        abs(X[0] - 67.7407) < 0.03,
    'omega_b, 0.022206':                  abs(X[1] - 0.022206) < 1.1e-5,
    'omega_c, 0.118237':                  abs(X[2] - 0.118237) < 5.5e-5,
    'n_s, 0.962136':                      abs(X[3] - 0.962136) < 4.5e-4,
    "r7828's H0, 67.3934":                abs(SX[0] - 67.3934) < 0.03,
    "r7828's n_s, 0.959284":              abs(SX[3] - 0.959284) < 4.5e-4,
    'the estimators apart by 0.2347':     abs(J['estimators_apart'] - 0.2347) < 1.1e-4,
    "r7827's per-trial, -3.5996":         abs(J['r7827_pertrial_dchi2'] + 3.5996) < 1.7e-3,
    'the in-force lD, 1489.5783':         abs(J['lD'] - 1489.5783) < 1.0e-9,
    'the ratio, 0.9918':                  abs(J['r'] - 0.9918) < 1.0e-12,
    'A_s9 held at 2.1':                   abs(J['as9'] - 2.1) < 1.0e-12,
    'the points, 142':                    J['n_points'] == 142,
    'the evaluations, 160':               J['nfev'] == 160,
    # as P15 prints them (r7829, 69): equality at the printed decimals
    'P15 prints the refit as 111.00':     round(J['chi2'], 2) == 111.00,
    "P15 prints this arm's LCDM as 114.84": round(J['chi2_lcdm'], 2) == 114.84,
    'P15 prints the Delta as 3.83':       round(-D, 2) == 3.83,
    'P15 prints H0 agreeing to 0.35':     round(abs(X[0] - SX[0]), 2) == 0.35,
    'P15 prints n_s agreeing to 0.003':   round(abs(X[3] - SX[3]), 3) == 0.003,
    'P15 prints the estimators apart by 0.235': round(J['estimators_apart'], 3) == 0.235,
}
print("\n" + "=" * 92)
print(f"  THE PRINTED FIGURES, PINNED: {sum(bool(v) for v in PINS.values())} of {len(PINS)} hold")
for k, v in PINS.items():
    if not v:
        print(f"    ⛔ NOT HELD: {k}")
assert all(PINS.values()), "a figure the INDEX row prints is not held by this receipt"

print("\n" + "=" * 92)
print("  ⌗ WHAT THIS RECEIPT DOES NOT DO: it does not adjudicate which arm is the better arm --")
print("    two arms agreeing BOUNDS a figure's arm-dependence and does not make either correct --")
print("    and it does not strike PO-24.  The clause is satisfied; the strike is 69's.")
print("=" * 92)
if FAILED:
    print("\n  FAILED:")
    for f in FAILED:
        print(f"    - {f}")
print(f"\n  arms run: {len(PASSED) + len(FAILED)}   passed {len(PASSED)}, FAILED {len(FAILED)}")
assert len(PASSED) + len(FAILED) == 7, "seven arms were registered; seven must run"
sys.exit(1 if FAILED else 0)
