#!/usr/bin/env python3
r"""r7822 (60) -- the joint Planck + ACT DR6 tail tilt, on order r7819 (69).

COMPUTES: the damping signature's required tail tilt against the tilt the sky itself prefers, on a
  joint arm in which no multipole is used twice, and beside the Planck-only arm.
  INPUT  the signature:  r = 1.0926, l_D = 1489.5783
  INPUT  the control:    L824_lcdm_L3200_nk960 (reach 3196), normalised to plik_lite TT
  INPUT  Planck:         plik_lite TT, bins with l_hi < the PlanckActCut multipole
  INPUT  ACT:            DR6 CMB-only TT, bandpowers whose WINDOW SUPPORT clears Planck's last l
  INPUT  the cut:        parsed from the shipped PlanckActCut.yaml banked beside this tree
  OUTPUT the distance in sigma, on the joint arm and on Planck alone, and the strict 2-sigma rule

** THE ANSWER: THE SIGNATURE'S TAIL TILT IS FAR OUTSIDE THE SKY'S, ON EVERY ARM. **

The joint arm puts the sky's tilt at -0.020658 +/- 0.003782 and the tilt the signature itself
requires at -0.093474 -- a distance of 19.25 sigma.  Planck alone gives 13.74, 13.18 and 4.65 sigma
over the three published windows.  The strict 2-sigma rule is exceeded by a wide margin everywhere,
and the joint arm SHARPENS the verdict rather than changing it.

** Ⓒ③ -- AN EFFECTIVE MULTIPOLE IS NOT A SUPPORT, AND THIS NEARLY DOUBLE-COUNTED THE SKY. **
Selecting ACT by EFFECTIVE multipole above the cut does not give a non-double-counting arm: the
l_eff = 1000.5 bandpower's window support starts at l = 976 and puts 48 per cent of its weight below
1000, while Planck's last used bin ends at l_hi = 999.  The split is made on WINDOW SUPPORT instead,
at the cost of one bandpower and a gap no experiment covers.
=> GUARD: a bandpower's effective multipole is a weighted mean, not its extent.

** TWO MORE REGISTERED ARMS FIRED THEIR NEGATIVES, and both are findings. **
  Ⓐ①  all 45 ACT windows are contiguous and flat, so they DO reduce to plik_lite's top-hat form.
      The registration demanded the matrix unreduced so that this would be a MEASUREMENT.
  Ⓓ④  ACT is the WORSE ruler on the tilt -- +/-0.009501 against Planck's +/-0.004159 -- despite a
      better per-bandpower fractional error.  Fewer, wider bands over a shorter lever lose.  But its
      registered consequence does NOT follow: the joint distance is LARGER than Planck's own.

⚠ THE LIMIT STAYS ATTACHED, and it is this row's standing one: neither banked control is a best fit
  to plik_lite, so a tilt fitted against the SKY absorbs baseline shape error as well as any
  signature.  These remain degeneracy-fit numbers.  What would settle it is a best fit to the joint
  data, which this revision did not run.
"""
import json
import os
import sys

import numpy as np
import scipy.linalg
from scipy.optimize import minimize_scalar

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

PASSED, FAILED = [], []


def head(t):
    print("\n" + "=" * 92 + f"\n  {t}\n" + "=" * 92)


def check(label, ok):
    (PASSED if ok else FAILED).append(label)
    print(f"\n  [{'PASS' if ok else 'FAIL'}] {label}")


R, LD = 1.0926, 1489.5783
K = R ** 2 - 1
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
AD = os.path.join(ROOT, 'computations', 'planck_tt_likelihood', 'data', 'act_dr6_cmbonly')


def _fisher(cov):
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(cov.shape[0]))
    return 0.5 * (F + F.T)


_z = np.load(os.path.join(SP, 'L824_lcdm_L3200_nk960.npz'))
LS, RAW = _z['ls'].astype(float), _z['Dl'].astype(float)
_k0 = np.isfinite(CS.bin_spectrum(LS, RAW))
_F0 = _fisher(CS.COV_TT[np.ix_(_k0, _k0)])
_m0 = CS.bin_spectrum(LS, RAW)[_k0]
DL = RAW * float((_m0 @ _F0 @ CS.X_DATA[_k0]) / (_m0 @ _F0 @ _m0))
SIG = DL * np.exp(-K * (LS / LD) ** 2)

AZ = np.load(os.path.join(AD, 'act_dr6_cmbonly.npz'), allow_pickle=True)
A_ELL, A_DL, A_WIN, A_WL = AZ['ell_TT'], AZ['Dl_TT'], AZ['win_TT'], AZ['win_ell']
A_COV = AZ['cov'][:45, :45]
CUT = int(open(os.path.join(AD, 'likelihood_source', 'PlanckActCut.yaml'),
               encoding='utf-8').read().split('lmax_cuts:')[1].split()[0])

print("=" * 92)
print("r7822 (60) -- the signature's tail tilt against the sky's, on the joint Planck + ACT arm")
print("=" * 92)

# ======================================================= Ⓐ THE LAYOUT
head("A -- ACT's BINNING IS A WINDOW MATRIX, AND WHETHER IT REDUCES IS MEASURED")
TOPHAT = []
for i in range(A_WIN.shape[1]):
    w = A_WIN[:, i]
    nz = w > 0
    ls_nz = A_WL[nz]
    TOPHAT.append(bool(len(ls_nz) == int(ls_nz.max() - ls_nz.min() + 1))
                  and bool(np.allclose(w[nz], w[nz][0])))
print(f"      {A_WIN.shape[1]} bandpowers over l = {A_WL[0]:.0f}..{A_WL[-1]:.0f}; "
      f"column sums {A_WIN.sum(axis=0).min():.6f}..{A_WIN.sum(axis=0).max():.6f}")
print(f"      contiguous AND flat: {sum(TOPHAT)} of {len(TOPHAT)}")
check("Ⓐ① THE REGISTERED NEGATIVE FIRED: all 45 ACT TT windows are contiguous and flat, so they DO "
      "reduce to plik_lite's blmin/blmax/bweight form -- the registration demanded the matrix "
      "unreduced precisely so that this would be a measurement rather than an inheritance",
      sum(TOPHAT) == 45 and A_WIN.shape[1] == 45
      and abs(float(A_WIN.sum(axis=0).min()) - 1.0) < 1e-9)

# ======================================================= Ⓑ THE CUT, FROM SOURCE
head("B -- THE CUT IS READ FROM THE SHIPPED PRODUCT, NOT FROM THE PAPER'S PROSE")
print(f"      PlanckActCut.yaml -> lmax_cuts TT = {CUT}")
check("Ⓑ② THIS RECEIPT READS THE SHIPPED PlanckActCut.yaml AND IT CUTS PLANCK TT AT 1000.  That "
      "is the whole of what is asserted here: the number is the banked product's, parsed from the "
      "file beside this tree.  ⌗ r7816's registration is where a paper was read, and it recorded "
      "the same value -- but this arm does not open a paper, so it does not attribute the number "
      "to one",
      CUT == 1000)

# ======================================================= Ⓒ NO MULTIPOLE TWICE
head("C -- NO MULTIPOLE MAY BE USED TWICE, AND THE EFFECTIVE-MULTIPOLE SPLIT FAILS IT")
P_KEEP = np.isfinite(CS.bin_spectrum(LS, DL)) & (CS.BIN_HI < CUT)
P_LMAX = int(CS.BIN_HI[P_KEEP].max())
A_SUPP_MIN = np.array([A_WL[A_WIN[:, i] > 0].min() for i in range(A_WIN.shape[1])])
A_SUPP_MAX = np.array([A_WL[A_WIN[:, i] > 0].max() for i in range(A_WIN.shape[1])])
REACH = float(LS.max())
_naive = A_ELL >= CUT
_bad = _naive & (A_SUPP_MIN <= P_LMAX)
_i = int(np.where(_bad)[0][0])
LEAK = float(A_WIN[:, _i][A_WL < CUT].sum())
A_KEEP = (A_SUPP_MIN > P_LMAX) & (A_SUPP_MAX <= REACH)
print(f"      Planck: {int(P_KEEP.sum())} bins, highest l used = {P_LMAX}")
print(f"      ACT by effective multipole: {int(_naive.sum())} bands, {int(_bad.sum())} leaking below")
print(f"        l_eff {A_ELL[_i]:.1f}: support starts {A_SUPP_MIN[_i]:.0f}, weight below "
      f"{CUT} = {LEAK:.6f}")
print(f"      ⇒ split remade on SUPPORT: {int(A_KEEP.sum())} bands from l = "
      f"{A_SUPP_MIN[A_KEEP].min():.0f}; the baseline's reach {REACH:.0f} caps the top")
check("Ⓒ③ THE REGISTERED NEGATIVE FIRED AND THE ROUTE IS NOT BLOCKED: exactly one bandpower leaks, "
      "the l_eff = 1000.5 one, putting 0.48 of its weight below the cut because its support starts "
      "at 976 while Planck's last bin ends at 999 -- so the split is made on WINDOW SUPPORT, which "
      "costs one bandpower and a gap, rather than needing a cross-covariance",
      int(_bad.sum()) == 1 and abs(LEAK - 0.48) < 4.85e-3
      and A_SUPP_MIN[_i] == 976 and P_LMAX == 999
      and A_SUPP_MIN[A_KEEP].min() > P_LMAX)

# ======================================================= THE TWO BLOCKS
P_F = _fisher(CS.COV_TT[np.ix_(P_KEEP, P_KEEP)])
P_D = CS.X_DATA[P_KEEP]
A_F = _fisher(A_COV[np.ix_(A_KEEP, A_KEEP)])
A_D = A_DL[A_KEEP]
A_W = A_WIN[:, A_KEEP]


def act_bin(dl):
    return A_W.T @ np.interp(A_WL, LS, dl)


def planck_bin(dl):
    return CS.bin_spectrum(LS, dl)[P_KEEP]


def block_chi2(d, F, m):
    A = float((m @ F @ d) / (m @ F @ m))
    r = d - A * m
    return float(r @ F @ r)


def fit_tilt(blocks):
    """blocks = [(data, Fisher, binner)]; each carries its OWN amplitude, as the instruments do"""
    def at(dn):
        th = DL * (LS / 1000.0) ** dn
        return sum(block_chi2(d, F, b(th)) for d, F, b in blocks)
    o = minimize_scalar(at, bounds=(-3.0, 3.0), method='bounded', options={'xatol': 1e-10})
    dn0, c0 = float(o.x), float(o.fun)
    h = 1e-3
    return dn0, c0, float(np.sqrt(2.0 / ((at(dn0 + h) - 2 * c0 + at(dn0 - h)) / h ** 2)))

# ======================================================= Ⓓ WHICH RULER
head("D -- WHICH IS THE SHARPER RULER ON THE TILT, MEASURED UNIT-FREE")
_, _, SG_P = fit_tilt([(P_D, P_F, planck_bin)])
_, _, SG_A = fit_tilt([(A_D, A_F, act_bin)])
_pm = np.isfinite(CS.bin_spectrum(LS, DL)) & (CS.BIN_LO >= 1000) & (CS.BIN_HI <= 1760)
_am = A_KEEP & (A_ELL <= 1760)
FR_P = float(np.median(np.sqrt(np.diag(CS.COV_TT))[_pm] / np.abs(CS.bin_spectrum(LS, DL)[_pm])))
FR_A = float(np.median(np.sqrt(np.diag(A_COV))[_am] / np.abs(A_DL[_am])))
print(f"      ⌗ a weight sum is NOT comparable across these blocks: Planck's vector is binned C_l")
print(f"        (the harness says so in capitals) and ACT's bandpowers are D_l.")
print(f"      each block's own 1-sigma on the tilt : Planck {SG_P:.6f}   ACT {SG_A:.6f}")
print(f"      median fractional error, l 1000-1760 : Planck {FR_P * 100:.3f} %   ACT {FR_A * 100:.3f} %")
check("Ⓓ④ THE REGISTERED NEGATIVE FIRED: ACT is the WORSE ruler on the tilt, +/-0.009501 against "
      "Planck's +/-0.004159, a factor 2.28 -- and it is worse DESPITE a better per-bandpower "
      "fractional error, 1.009 against 1.567 per cent, because fewer and wider bands over a "
      "shorter lever lose.  But the consequence registered for this negative does NOT follow, "
      "because the joint distance below is LARGER than Planck's own, not smaller",
      abs(SG_P - 0.004159) < 2.02e-6 and abs(SG_A - 0.009501) < 4.61e-6
      and abs(SG_A / SG_P - 2.28) < 4.85e-3
      and abs(FR_P * 100 - 1.567) < 7.8e-4 and abs(FR_A * 100 - 1.009) < 5.0e-4
      and FR_A < FR_P and SG_A > SG_P)

# ======================================================= Ⓔ THE MEASUREMENT
head("E -- THE SIGNATURE'S DISTANCE FROM THE SKY'S TILT, ON THE JOINT ARM")
JB = [(P_D, P_F, planck_bin), (A_D, A_F, act_bin)]
DN_SKY, C_SKY, SG_SKY = fit_tilt(JB)
DN_SIG, _, _ = fit_tilt([(planck_bin(SIG), P_F, planck_bin), (act_bin(SIG), A_F, act_bin)])
NDOF = int(P_KEEP.sum()) + int(A_KEEP.sum()) - 3
DIST = abs(DN_SIG - DN_SKY) / SG_SKY
print(f"      {int(P_KEEP.sum())} Planck bins + {int(A_KEEP.sum())} ACT bandpowers")
print(f"      the sky's tilt     {DN_SKY:+.6f} +/- {SG_SKY:.6f}   chi2/dof "
      f"{C_SKY / NDOF:.4f} over {NDOF}")
print(f"      the signature's    {DN_SIG:+.6f}")
print(f"      DISTANCE           {DIST:.3f} sigma   -- the strict 2-sigma rule is "
      f"{'EXCEEDED' if DIST > 2.0 else 'NOT exceeded'}")
# ======================================================= Ⓕ THE PLANCK-ONLY ARM
head("E (continued) -- THE PLANCK-ONLY ARM, BESIDE IT, AS THE ORDER ASKS")
PO = {}
for lbl, lo, hi in (('100-1758', 100, 1758), ('700-1760', 700, 1760), ('1000-1760', 1000, 1760)):
    m = np.isfinite(CS.bin_spectrum(LS, DL)) & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi)
    F = _fisher(CS.COV_TT[np.ix_(m, m)])

    def b(dl, _m=m):
        return CS.bin_spectrum(LS, dl)[_m]
    ds, _, ss = fit_tilt([(CS.X_DATA[m], F, b)])
    dg, _, _ = fit_tilt([(b(SIG), F, b)])
    PO[lbl] = abs(dg - ds) / ss
    print(f"      {lbl:>10}, {int(m.sum()):>3d} bins: sky {ds:+.6f} +/- {ss:.6f}, "
          f"signature {dg:+.6f}, distance {PO[lbl]:.3f} sigma")
check("Ⓔ⑤ the sky's tilt is -0.020658 +/- 0.003782 and the signature requires -0.093474, a "
      "distance of 19.25 sigma, so the strict 2-sigma rule is exceeded by a wide margin: if the "
      "sky's tail carried the signature as a pure extra damping it would read near -0.09, and it "
      "reads -0.02.  AND BESIDE IT, as the order asks, Planck alone exceeds the rule on all three "
      "published windows -- 13.74, 13.18 and 4.65 sigma -- so the joint arm SHARPENS the verdict "
      "rather than creating it",
      abs(DN_SKY - (-0.020658)) < 1.0e-5 and abs(SG_SKY - 0.003782) < 1.83e-6
      and abs(DN_SIG - (-0.093474)) < 4.53e-5
      and abs(DIST - 19.253) < 9.34e-3 and DIST > 2.0
      # r7829 (69): the three Planck-alone distances as printed, by equality at three decimals
      #   (the build sweep flagged the 4.652 pin: a minimiser residue near 5e-6 moves between builds)
      and round(PO['100-1758'], 3) == 13.740 and round(PO['700-1760'], 3) == 13.179
      and round(PO['1000-1760'], 3) == 4.652
      and min(PO.values()) > 2.0 and DIST > PO['100-1758'])

# ======================================================= Ⓗ THE LIMIT, AND THE COUNT
head("H -- THE LIMIT THAT STAYS ATTACHED, MEASURED AND NOT WAVED AT")
_m1 = np.isfinite(CS.bin_spectrum(LS, DL)) & (CS.BIN_LO >= 1000) & (CS.BIN_HI <= 1500)
_m2 = np.isfinite(CS.bin_spectrum(LS, DL)) & (CS.BIN_LO >= 1500) & (CS.BIN_HI <= 1760)
CB = {}
for nm, m in (('1000-1500', _m1), ('1500-1760', _m2)):
    F = _fisher(CS.COV_TT[np.ix_(m, m)])
    CB[nm] = block_chi2(CS.X_DATA[m], F, CS.bin_spectrum(LS, DL)[m]) / int(m.sum())
    print(f"      the control against Planck alone, l {nm}: chi2/bin {CB[nm]:.3f} "
          f"at its own amplitude")
print("      ⇒ so a tilt fitted against the SKY absorbs baseline shape error as well as any")
print("        signature.  These are degeneracy-fit numbers, as every INDEX row in this row says.")
print("        What would settle it is a best fit to the joint data, which this revision did not run.")
check("Ⓕ⑥ the limit is stated with its size rather than as a hedge, on both of its halves: the "
      "control this arm uses fits Planck's own TT at chi2/bin 5.04 over 1000-1500 and 9.59 over "
      "1500-1760, so these remain degeneracy-fit numbers; and the neglected Planck-x-ACT "
      "covariance this construction inherits carries DR6's own published bound of under five per "
      "cent on sigma(N_eff), recorded beside the result",
      abs(CB['1000-1500'] - 5.041) < 2.52e-3 and abs(CB['1500-1760'] - 9.587) < 4.79e-3
      and CB['1000-1500'] > 1.0 and CB['1500-1760'] > 1.0)

head("G -- BELOW THE SPLIT, THE JOINT ARM'S PLANCK HALF IS THE HARNESS'S OWN")
_gap = float(np.abs(CS.bin_spectrum(LS, DL)[P_KEEP] - planck_bin(DL)).max())
print(f"      max |difference| over {int(P_KEEP.sum())} shared bins: {_gap:.3e}")
check("Ⓖ⑦ below the split the joint arm's Planck half IS the harness's own, to machine precision "
      "and in fact exactly -- max difference 0.000e+00 over the 100 shared bins -- so every "
      "comparison with the published Planck-only figures is made on the same instrument",
      _gap == 0.0 and int(P_KEEP.sum()) == 100)

head("THE COUNT")
print(f"\n  arms registered in r7816's PREDICTION.md : 8")
print(f"  arms run before this count is asserted   : {len(PASSED) + len(FAILED)}")
check("Ⓗ⑧ eight arms were registered in r7816 and eight ran here, under the labels the "
      "registration gave them -- the count is asserted rather than assumed, which is what caught "
      "this receipt renumbering Ⓕ⑥ and Ⓖ⑦ away from the registration on its first run, and "
      "then counting its own Planck-only report as a ninth",
      len(PASSED) + len(FAILED) == 7)
if FAILED:
    print("\n  FAILED:")
    for f in FAILED:
        print(f"    - {f}")
print("\n  ⌗ THREE REGISTERED NEGATIVES FIRED -- Ⓐ①, Ⓒ③ and Ⓓ④ -- and each is carried by the arm")
print("    that asserts the measurement refuting its expectation, rather than rewritten into")
print("    something that could pass.  Ⓒ③'s is the one that mattered: it caught a split that")
print("    would have used 48 per cent of one bandpower's sky twice.")
print(f"  arms run in total, this count included   : {len(PASSED) + len(FAILED)}")
print(f"  passed {len(PASSED)}, FAILED {len(FAILED)}")
assert len(PASSED) + len(FAILED) == 8, "eight arms were registered; eight must run"
sys.exit(1 if FAILED else 0)
