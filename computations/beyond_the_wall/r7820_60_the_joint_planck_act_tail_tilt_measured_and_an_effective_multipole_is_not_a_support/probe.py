#!/usr/bin/env python3
r"""r7820 (60) -- the joint Planck + ACT DR6 tail-tilt measurement, on order r7819 (69).

Registered at r7816 before any of this ran.  Eight arms; this probe measures them.

THE CONSTRUCTION, and the one place it had to change from the registration:
  Planck plik_lite TT below the PlanckActCut multipole, ACT DR6 CMB-only TT above it, each with
  its OWN free amplitude, and NO cross-covariance term because no multipole is used twice.

  Ⓒ③ registered the assertion that no bandpower pair shares a multipole.  Selecting ACT by
  EFFECTIVE multipole >= 1000 does NOT satisfy it: the l_eff = 1000.5 bandpower's window support
  starts at l = 976 and puts 48 per cent of its weight below 1000, while Planck's last used bin
  ends at l_hi = 999.  The split is therefore made on WINDOW SUPPORT, which costs one bandpower
  and leaves l 1000-1025 used by neither.  => An effective multipole is not a support.

  A_act is a free overall amplitude on the ACT side (flat 0.5-1.5) against Planck's A_planck
  (Normal(1, 0.0025)), and P_act does not enter TT at all -- both read from the likelihood source
  banked at data/act_dr6_cmbonly/likelihood_source/.  So each block carries its own amplitude,
  marginalised analytically; a single pooled amplitude would impose a cross-calibration neither
  experiment claims.
"""
import json
import os
import sys

import numpy as np
import scipy.linalg
from scipy.optimize import minimize_scalar

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

R, LD = 1.0926, 1489.5783
K = R ** 2 - 1
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
AD = os.path.join(ROOT, 'computations', 'planck_tt_likelihood', 'data', 'act_dr6_cmbonly')

# ---- the baseline, normalised to plik_lite exactly as every earlier revision does -------------
BASE_PUB = 'L820_lcdm_L2512_nk800.npz'      # what every published PO-24 figure was computed on
BASE_USE = 'L824_lcdm_L3200_nk960.npz'      # further reach, finer k -- measured against it below
_z = np.load(os.path.join(SP, BASE_USE))
LS, RAW = _z['ls'].astype(float), _z['Dl'].astype(float)


def _fisher(cov):
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(cov.shape[0]))
    return 0.5 * (F + F.T)


_k0 = np.isfinite(CS.bin_spectrum(LS, RAW))
_F0 = _fisher(CS.COV_TT[np.ix_(_k0, _k0)])
_m0 = CS.bin_spectrum(LS, RAW)[_k0]
DL = RAW * float((_m0 @ _F0 @ CS.X_DATA[_k0]) / (_m0 @ _F0 @ _m0))

# ---- ACT, as 70 banked it ----------------------------------------------------------------------
AZ = np.load(os.path.join(AD, 'act_dr6_cmbonly.npz'), allow_pickle=True)
A_ELL, A_DL, A_WIN, A_WL = AZ['ell_TT'], AZ['Dl_TT'], AZ['win_TT'], AZ['win_ell']
A_COV = AZ['cov'][:45, :45]                 # the TT block, in the banked TT/TE/EE order

# PlanckActCut, read from the banked source and not from the paper's prose
CUT = int(open(os.path.join(AD, 'likelihood_source', 'PlanckActCut.yaml'),
               encoding='utf-8').read().split('lmax_cuts:')[1].split()[0])

print("=" * 100)
print("r7820 (60) -- the joint Planck + ACT DR6 tail tilt, and the split that had to be remade")
print("=" * 100)

# ================================================= Ⓐ① THE LAYOUT, AND Ⓑ② THE CUT FROM SOURCE
print(f"\n  Ⓑ②  PlanckActCut, read from the shipped yaml: lmax_cuts TT = {CUT}")
print(f"  Ⓐ①  ACT binning is a WINDOW MATRIX, {A_WIN.shape[1]} bandpowers over l = "
      f"{A_WL[0]:.0f}..{A_WL[-1]:.0f} ({A_WIN.shape[0]} points); column sums "
      f"{A_WIN.sum(axis=0).min():.6f}..{A_WIN.sum(axis=0).max():.6f}")
print(f"      plik_lite binning is top-hat ranges + weights, {len(CS.BIN_LO)} bins over "
      f"l = {CS.BIN_LO[0]}..{CS.BIN_HI[-1]}")
_tophat = []
for i in range(A_WIN.shape[1]):
    w = A_WIN[:, i]
    nz = w > 0
    ls_nz = A_WL[nz]
    contiguous = (len(ls_nz) == int(ls_nz.max() - ls_nz.min() + 1))
    flat = bool(np.allclose(w[nz], w[nz][0]))
    _tophat.append(contiguous and flat)
print(f"      is each ACT window a FLAT top-hat? {sum(_tophat)} of {len(_tophat)} "
      f"-- contiguous-and-flat")

# ================================================= Ⓒ③ NO MULTIPOLE USED TWICE
print("\n" + "=" * 100)
print("  Ⓒ③  NO MULTIPOLE MAY BE USED TWICE -- and the effective-multipole split FAILS it")
print("=" * 100)
P_KEEP = np.isfinite(CS.bin_spectrum(LS, DL)) & (CS.BIN_HI < CUT)
P_LMAX = int(CS.BIN_HI[P_KEEP].max())
print(f"\n      Planck: {int(P_KEEP.sum())} bins with l_hi < {CUT}; highest l used = {P_LMAX}")

A_SUPP_MIN = np.array([A_WL[A_WIN[:, i] > 0].min() for i in range(A_WIN.shape[1])])
naive = A_ELL >= CUT
bad = naive & (A_SUPP_MIN <= P_LMAX)
print(f"      ACT by EFFECTIVE multipole >= {CUT}: {int(naive.sum())} bandpowers, of which "
      f"{int(bad.sum())} have window support reaching l <= {P_LMAX}")
for i in np.where(bad)[0]:
    w = A_WIN[:, i]
    print(f"        l_eff {A_ELL[i]:.1f}: support starts at l = {A_SUPP_MIN[i]:.0f}, "
          f"weight below {CUT} = {float(w[A_WL < CUT].sum()):.6f}")

A_SUPP_MAX = np.array([A_WL[A_WIN[:, i] > 0].max() for i in range(A_WIN.shape[1])])
REACH = float(LS.max())
A_KEEP = (A_SUPP_MIN > P_LMAX) & (A_SUPP_MAX <= REACH)
print(f"\n      ⛔ AND THE BASELINE'S REACH BINDS: it ends at l = {REACH:.0f} while ACT's windows")
print(f"         need theory to l = {A_WL[-1]:.0f}.  np.interp flat-extrapolates past the end, so")
print(f"         a bandpower whose support leaves the reach is modelled with a CONSTANT.")
print(f"         bandpowers with support above the reach, excluded: "
      f"{int(((A_SUPP_MIN > P_LMAX) & (A_SUPP_MAX > REACH)).sum())}")
print(f"\n      ⇒ the split is remade on WINDOW SUPPORT: {int(A_KEEP.sum())} ACT bandpowers, "
      f"support starting at l = {A_SUPP_MIN[A_KEEP].min():.0f}")
print(f"      the price: l {P_LMAX + 1}..{A_SUPP_MIN[A_KEEP].min() - 1:.0f} is used by NEITHER, "
      f"and one bandpower is dropped")
print(f"      ⇒ ** AN EFFECTIVE MULTIPOLE IS NOT A SUPPORT. **")

# ================================================= THE TWO BLOCKS
P_F = _fisher(CS.COV_TT[np.ix_(P_KEEP, P_KEEP)])
P_D = CS.X_DATA[P_KEEP]
A_F = _fisher(A_COV[np.ix_(A_KEEP, A_KEEP)])
A_D = A_DL[A_KEEP]
A_W = A_WIN[:, A_KEEP]


def act_bin(dl_on_LS):
    """bin a theory spectrum with ACT's own window matrix, on ACT's own l grid"""
    return A_W.T @ np.interp(A_WL, LS, dl_on_LS)


def planck_bin(dl_on_LS):
    return CS.bin_spectrum(LS, dl_on_LS)[P_KEEP]


def block_chi2(d, F, m):
    """chi2 with that block's OWN amplitude marginalised analytically"""
    A = float((m @ F @ d) / (m @ F @ m))
    r = d - A * m
    return float(r @ F @ r), A


def joint_chi2(dn):
    """the joint chi2 at tilt dn, each block carrying its own free amplitude"""
    th = DL * (LS / 1000.0) ** dn
    cp, ap = block_chi2(P_D, P_F, planck_bin(th))
    ca, aa = block_chi2(A_D, A_F, act_bin(th))
    return cp + ca, cp, ca, ap, aa


# ================================================= Ⓓ④ WHICH RULER IS SHARPER WHERE IT MATTERS
print("\n" + "=" * 100)
print("  Ⓓ④  IS ACT THE SHARPER RULER WHERE IT REPLACES PLANCK?")
print("=" * 100)
_pm = np.isfinite(CS.bin_spectrum(LS, DL)) & (CS.BIN_LO >= 1000) & (CS.BIN_HI <= 1760)
_ps = np.sqrt(np.diag(CS.COV_TT))[_pm]
_pc = CS.bin_spectrum(LS, DL)[_pm]
_am = A_KEEP & (A_ELL <= 1760)
_as_ = np.sqrt(np.diag(A_COV))[_am]
_ac = A_DL[_am]
print(f"\n      over l 1000-1760, fractional error per bandpower:")
print(f"      ⌗ a weight sum is NOT comparable between these two blocks: the Planck vector is")
print(f"        binned C_l (the harness says so in capitals) and ACT's bandpowers are D_l.")
print(f"        What IS comparable is the fractional error, and each block's own sigma on the tilt.")
print(f"        Planck : {int(_pm.sum()):>3d} bins,  median fractional error "
      f"{np.median(_ps / np.abs(_pc)) * 100:.3f} %")
print(f"        ACT    : {int(_am.sum()):>3d} bands, median fractional error "
      f"{np.median(_as_ / np.abs(_ac)) * 100:.3f} %")

# ================================================= Ⓔ⑤ THE MEASUREMENT
print("\n" + "=" * 100)
print("  Ⓔ⑤  THE SIGNATURE'S DISTANCE FROM THE SKY'S TILT")
print("=" * 100)

SIG = DL * np.exp(-K * (LS / LD) ** 2)


def fit_tilt(target_P, target_A):
    """the tilt a given pair of data vectors prefers, and its 1-sigma width from the curvature"""
    def at(dn):
        th = DL * (LS / 1000.0) ** dn
        return (block_chi2(target_P, P_F, planck_bin(th))[0]
                + block_chi2(target_A, A_F, act_bin(th))[0])
    o = minimize_scalar(at, bounds=(-3.0, 3.0), method='bounded', options={'xatol': 1e-10})
    dn0, c0 = float(o.x), float(o.fun)
    h = 1e-3
    d2 = (at(dn0 + h) - 2 * c0 + at(dn0 - h)) / h ** 2
    return dn0, c0, float(np.sqrt(2.0 / d2))


def fit_tilt_one(target, F, binner):
    def at(dn):
        return block_chi2(target, F, binner(DL * (LS / 1000.0) ** dn))[0]
    o = minimize_scalar(at, bounds=(-3.0, 3.0), method='bounded', options={'xatol': 1e-10})
    dn0 = float(o.x)
    h = 1e-3
    d2 = (at(dn0 + h) - 2 * float(o.fun) + at(dn0 - h)) / h ** 2
    return dn0, float(np.sqrt(2.0 / d2))


_dnp, _sgp = fit_tilt_one(P_D, P_F, planck_bin)
_dna, _sga = fit_tilt_one(A_D, A_F, act_bin)
SHARPER = _sga < _sgp
print(f"\n      EACH BLOCK'S OWN 1-sigma ON THE TILT -- unit-free, and the quantity in use:")
print(f"        Planck below the split : Delta n = {_dnp:+.6f} +/- {_sgp:.6f}")
print(f"        ACT above it           : Delta n = {_dna:+.6f} +/- {_sga:.6f}")
print(f"      ⇒ on the tilt, ACT is the {'SHARPER' if SHARPER else 'WORSE'} ruler "
      f"by a factor {max(_sgp, _sga) / min(_sgp, _sga):.2f}")

DN_SKY, C_SKY, SIG_SKY = fit_tilt(P_D, A_D)
DN_SIG, C_SIG, _ = fit_tilt(planck_bin(SIG), act_bin(SIG))
NDOF = int(P_KEEP.sum()) + int(A_KEEP.sum()) - 3        # tilt + two amplitudes

print(f"\n      the joint data vector: {int(P_KEEP.sum())} Planck bins + {int(A_KEEP.sum())} ACT "
      f"bandpowers = {int(P_KEEP.sum()) + int(A_KEEP.sum())}")
print(f"      THE SKY'S TILT        : Delta n = {DN_SKY:+.6f} +/- {SIG_SKY:.6f}"
      f"   chi2 = {C_SKY:.3f} over {NDOF} dof = {C_SKY / NDOF:.4f}")
print(f"      THE SIGNATURE'S TILT  : Delta n = {DN_SIG:+.6f}"
      f"   (the tilt baseline x S(l) itself prefers on this same arm)")
DIST = abs(DN_SIG - DN_SKY) / SIG_SKY
print(f"\n      DISTANCE              : |{DN_SIG:+.6f} - ({DN_SKY:+.6f})| / {SIG_SKY:.6f}"
      f" = {DIST:.3f} sigma")
print(f"      THE STRICT 2-SIGMA RULE: {'EXCEEDED -- the signature is excluded on this arm' if DIST > 2.0 else 'NOT exceeded -- this arm does not exclude the signature'}")

# and the direct comparison, which needs no tilt at all
cs_P, _ = block_chi2(P_D, P_F, planck_bin(SIG))
cs_A, _ = block_chi2(A_D, A_F, act_bin(SIG))
cb_P, _ = block_chi2(P_D, P_F, planck_bin(DL))
cb_A, _ = block_chi2(A_D, A_F, act_bin(DL))
print(f"\n      ⌗ and the DIRECT comparison, with no tilt freed at all:")
print(f"        baseline  : chi2 {cb_P + cb_A:.3f}   (Planck {cb_P:.3f} + ACT {cb_A:.3f})")
print(f"        x S(l)    : chi2 {cs_P + cs_A:.3f}   (Planck {cs_P:.3f} + ACT {cs_A:.3f})")
print(f"        Delta chi2 = {cs_P + cs_A - cb_P - cb_A:+.3f}  "
      f"=> {np.sqrt(abs(cs_P + cs_A - cb_P - cb_A)):.2f} sigma-equivalent on one dof")

# ================================================= Ⓖ⑦ THE PLANCK HALF IS THE HARNESS'S
print("\n" + "=" * 100)
print("  Ⓖ⑦  BELOW THE SPLIT THE JOINT ARM'S PLANCK HALF IS THE HARNESS'S OWN")
print("=" * 100)
_h = CS.bin_spectrum(LS, DL)[P_KEEP]
_j = planck_bin(DL)
print(f"\n      max |difference| over {int(P_KEEP.sum())} bins: {float(np.abs(_h - _j).max()):.3e}")

# ================================================= Ⓕ⑥ / Ⓗ⑧
print("\n" + "=" * 100)
print("  Ⓕ⑥  THE INHERITED LIMIT, STATED WITH ITS SIZE")
print("=" * 100)
print("\n      DR6 neglects the Planck x ACT covariance and estimates computing it would improve")
print("      sigma(N_eff) at the <5 per cent level.  This construction inherits that neglect for")
print("      DIFFERENT multipoles of the two experiments; no pair shares one (Ⓒ③).")

np.savez(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'runs', 'r7820_probe.npz'),
         dn_sky=DN_SKY, sig_sky=SIG_SKY, dn_sig=DN_SIG, dist=DIST,
         chi2_sky=C_SKY, ndof=NDOF, cut=CUT, p_lmax=P_LMAX,
         n_planck=int(P_KEEP.sum()), n_act=int(A_KEEP.sum()),
         act_supp_min=A_SUPP_MIN, act_keep=A_KEEP,
         chi2_base=cb_P + cb_A, chi2_sig=cs_P + cs_A, sharper=SHARPER)
print("\n  ⌗ probe written to runs/r7820_probe.npz")


# ================================================= THE BASELINE ITSELF, MEASURED BOTH WAYS
print("\n" + "=" * 100)
print("  ⛔ THE BASELINE IS THE BINDING LIMIT, AND IT IS MEASURED AGAINST PLANCK ALONE")
print("=" * 100)
print("\n      Neither banked control is a best fit to plik_lite; each is a control computed at a")
print("      particular cosmology, compared with ONE free amplitude.  So before any joint number")
print("      is quoted, here is what each control does against Planck's own TT, by band:")
_sig_p = np.sqrt(np.diag(CS.COV_TT))
for nm in (BASE_PUB, BASE_USE):
    _zz = np.load(os.path.join(SP, nm))
    _ls, _raw = _zz['ls'].astype(float), _zz['Dl'].astype(float)
    _kk = np.isfinite(CS.bin_spectrum(_ls, _raw))
    _FF = _fisher(CS.COV_TT[np.ix_(_kk, _kk)])
    _mm = CS.bin_spectrum(_ls, _raw)[_kk]
    _dl = _raw * float((_mm @ _FF @ CS.X_DATA[_kk]) / (_mm @ _FF @ _mm))
    _mod = CS.bin_spectrum(_ls, _dl)
    print(f"\n      {nm}  (reach {_ls.max():.0f})")
    for lo, hi in ((1000, 1500), (1500, 1760), (1760, 2200), (2200, 2508)):
        m = np.isfinite(_mod) & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi)
        if not m.sum():
            continue
        F = _fisher(CS.COV_TT[np.ix_(m, m)])
        A = float((_mod[m] @ F @ CS.X_DATA[m]) / (_mod[m] @ F @ _mod[m]))
        r = CS.X_DATA[m] - A * _mod[m]
        print(f"        l {lo:>5}-{hi:<5} {int(m.sum()):>3d} bins   mean residual "
              f"{float(((CS.X_DATA[m] - _mod[m]) / _sig_p[m]).mean()):+6.2f} sigma"
              f"   chi2/bin at its own amplitude {float(r @ F @ r) / m.sum():7.3f}")
print(f"\n      ⇒ the published control carries a SYSTEMATIC tail deficit of about +3.2 sigma per")
print(f"        bin from l = 1500 up, which the higher-reach control removes (to about +0.8).")
print(f"        ⚠ BUT NEITHER fits at chi2/bin near one, so a tilt fitted against the SKY absorbs")
print(f"        baseline shape error as well as any signature.")

# ================================================= THE PLANCK-ONLY ARM, BESIDE IT, AS ORDERED
print("\n" + "=" * 100)
print("  THE PLANCK-ONLY ARM, REPORTED BESIDE THE JOINT ONE AS THE ORDER ASKS")
print("=" * 100)
for lbl, lo, hi in (('100-1758', 100, 1758), ('700-1760', 700, 1760), ('1000-1760', 1000, 1760)):
    m = np.isfinite(CS.bin_spectrum(LS, DL)) & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi)
    F = _fisher(CS.COV_TT[np.ix_(m, m)])

    def _fit(target):
        def at(dn):
            return block_chi2(target, F, CS.bin_spectrum(LS, DL * (LS / 1000.0) ** dn)[m])[0]
        o = minimize_scalar(at, bounds=(-3.0, 3.0), method='bounded', options={'xatol': 1e-10})
        dn0 = float(o.x)
        h = 1e-3
        d2 = (at(dn0 + h) - 2 * float(o.fun) + at(dn0 - h)) / h ** 2
        return dn0, float(np.sqrt(2.0 / d2))
    dn_s, sg_s = _fit(CS.X_DATA[m])
    dn_g, _ = _fit(CS.bin_spectrum(LS, SIG)[m])
    print(f"\n      Planck TT {lbl}, {int(m.sum())} bins")
    print(f"        the sky's tilt      {dn_s:+.6f} +/- {sg_s:.6f}")
    print(f"        the signature's     {dn_g:+.6f}")
    print(f"        distance            {abs(dn_g - dn_s) / sg_s:.3f} sigma")
