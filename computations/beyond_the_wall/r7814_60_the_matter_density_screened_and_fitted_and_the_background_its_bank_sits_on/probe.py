#!/usr/bin/env python3
r"""r7814 (60) -- PO-24's omega_m screen and fit, on order r7813 (69).

Same harness as r7800/r7804/r7806/r7808/r7812, with the free direction swapped to omega_m, read
from 70's r7809 bank as a RATIO to its own centre.

THE CENTRE IS TAKEN BY VALUE, and from the bank's OWN DECLARED centre rather than from the list's
shape: config.bank.LOM_centre is an Omega_m, converted to omega_m by the bank's own h, and the grid
value nearest that is the centre.  On this five-value symmetric grid the midpoint by index happens
to be the same point; that is measured, not assumed.
"""
import json
import os
import sys

import numpy as np
import scipy.linalg
from scipy.optimize import minimize, minimize_scalar
from scipy.interpolate import PchipInterpolator

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

R, LD = 1.0926, 1489.5783
K = R ** 2 - 1

# ---- the referents, every one of them established by r7810 ---------------------------------------
OM_BAO_ARM, H0_BAO_ARM = 0.2974, 68.62     # the arm's own BAO minimum
OM_USED, H0_USED = 0.2973, 68.60           # its rounding, which the spectra are computed at
SIG_WM_ARM = 0.004543                      # DESI DR2 BAO on the arm's own ruler
OM_CTRL, SIG_OM_CTRL = 0.2971, 0.0085      # DESI DR2 BAO on the control's own ruler
OM_TT_ARM = 0.2912                         # the arm's TT minimum
DISP_SIGMA, DCHI2_BAO = -0.673, 0.524      # where it sits from its own BAO minimum, and what it pays

H_USED = H0_USED / 100.0
WM_ARM = OM_USED * H_USED ** 2             # the arm's published point, as a physical density

SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
_z = np.load(os.path.join(SP, 'L820_lcdm_L2512_nk800.npz'))
LS, RAW = _z['ls'].astype(float), _z['Dl'].astype(float)


def _fisher(keep):
    cov = CS.COV_TT[np.ix_(keep, keep)]
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(cov), np.identity(int(keep.sum())))
    return 0.5 * (F + F.T)


_k0 = np.isfinite(CS.bin_spectrum(LS, RAW))
_F0 = _fisher(_k0)
_m0 = CS.bin_spectrum(LS, RAW)[_k0]
DL = RAW * float((_m0 @ _F0 @ CS.X_DATA[_k0]) / (_m0 @ _F0 @ _m0))


def window(lo, hi):
    return (np.isfinite(CS.bin_spectrum(LS, DL)) & (CS.BIN_LO >= lo) & (CS.BIN_HI <= hi))


MZ = np.load(os.path.join(SP, 'r7809_omm_response_lcdm.npz'), allow_pickle=True)
CFG = json.loads(str(MZ['config']))
BANK = CFG['bank']
H_BANK = BANK['LH0'] / 100.0
WS_ = np.array(sorted(float(x) for x in MZ['omega_m']))

#  the centre, BY VALUE, from the bank's OWN declared centre -- never from the list's midpoint
WC_DECLARED = float(BANK['LOM_centre']) * H_BANK ** 2
W0 = float(WS_[int(np.argmin(np.abs(WS_ - WC_DECLARED)))])
MIDPOINT_BY_INDEX = float(WS_[len(WS_) // 2])          # asserted equal here; it was NOT at r7805


def _key(pref, w):
    return next(k for k in MZ.files
                if k.startswith(pref + '__') and abs(float(k.split('__')[1]) - w) < 1e-9)


ML_ = MZ[_key('ls', W0)].astype(float)
MD = np.array([MZ[_key('Dl', w)].astype(float) for w in WS_])
WRAT = MD / MD[int(np.argmin(np.abs(WS_ - W0)))]
_WR = PchipInterpolator(WS_, WRAT, axis=0)

W_STEP = float(WS_[WS_ > W0].min())                    # the first grid point above the centre
W_STARTS = (float(WS_.min()), W0, W_STEP, float(WS_.max()))


def ratio_on_LS(w):
    rb = np.asarray(_WR(float(w)))
    return np.interp(LS, ML_, rb, left=rb[0], right=rb[-1])


print("=" * 100)
print("r7814 (60) -- omega_m SCREENED AND FITTED: the last inherited parameter, on 70's r7809 bank")
print("=" * 100)

# ---- Ⓐ① / Ⓑ② / Ⓒ③ / Ⓓ④  THE BANK AND ITS BACKGROUND -------------------------------------------
print("\n  Ⓐ①  70's bank, read before anything is fitted")
print(f"      grid  : {list(WS_)}")
print(f"      centre BY VALUE                 : {W0:.6f}   "
      f"(from config.bank.LOM_centre = {BANK['LOM_centre']} at the bank's own h)")
print(f"      midpoint BY INDEX               : {MIDPOINT_BY_INDEX:.6f}")
print(f"      offsets from the centre, per cent: "
      f"{', '.join('%+.4f' % (100 * (w / W0 - 1)) for w in WS_)}")
print(f"      l grid: {ML_[0]:.0f} to {ML_[-1]:.0f} step {ML_[1] - ML_[0]:.0f}, {len(ML_)} points")

INV = {}
for nm in ('lA', 'rs', 'DM'):
    INV[nm] = np.array([float(MZ[_key(nm, w)]) for w in WS_])
    sprd = float(INV[nm].max() - INV[nm].min())
    print(f"      {nm:>4s} across the grid: {INV[nm][0]:.6f} .. {INV[nm][-1]:.6f}"
          f"   spread {sprd:.4f} = {100 * sprd / float(INV[nm][2]):.3f} %")
MOVES_ALL = {nm: 100 * float(INV[nm].max() - INV[nm].min()) / float(INV[nm][2])
             for nm in ('lA', 'rs', 'DM')}
print("      ⌗ beside the four already banked: omega_b moved lA 4.589 / rs 2.213; N_eff moved")
print("        lA 10.14 / rs 4.984 / DM 8.716; Y_He and A_L moved all three by EXACTLY zero.")

MAXDEV = [float(np.abs(r - 1).max()) for r in WRAT]
print(f"\n      response size, per cent: {', '.join('%.2f' % (d * 100) for d in MAXDEV)}")

print("\n  Ⓒ③  THE BACKGROUND THIS BANK SITS ON IS NOT THE ARM'S PUBLISHED ONE")
print(f"      the bank    : H0 {BANK['LH0']:.6f}  (h = {H_BANK:.6f}),  "
      f"Omega_m centre {BANK['LOM_centre']},  omega_b h^2 {BANK['WBH2']},  n_s {BANK['NS']}")
print(f"      the arm     : H0 {H0_USED}  (h = {H_USED:.6f}),  Omega_m {OM_USED}   "
      f"-- r7810: where the spectra are computed")
print(f"      so the bank's centre is omega_m = {W0:.6f} and the arm's point is "
      f"omega_m = {WM_ARM:.6f}")
print(f"      gap = {W0 - WM_ARM:+.6f} = {(W0 - WM_ARM) / SIG_WM_ARM:+.4f} sigma on the arm's ruler")

print("\n  Ⓓ④  AND THE CONTROL'S RULER IS A FRACTION, SO IT NEEDS AN h BEFORE IT CAN BE APPLIED")
_at_bank = WM_ARM / H_BANK ** 2
_at_arm = WM_ARM / H_USED ** 2
print(f"      the arm's own omega_m = {WM_ARM:.6f} converts to")
print(f"        Omega_m = {_at_bank:.6f}  at the BANK's h = {H_BANK:.6f}")
print(f"        Omega_m = {_at_arm:.6f}  at the ARM's  h = {H_USED:.6f}")
print(f"      difference {abs(_at_bank - _at_arm):.6f} against sigma(Omega_m) = {SIG_OM_CTRL}"
      f"   ratio {abs(_at_bank - _at_arm) / SIG_OM_CTRL:.3f}")

REACH = float(ML_[-1])
WINDOWS = [(100, 1758), (700, 1760), (1000, 1760), (1000, 2508), (1400, 2508), (100, 2508)]
AVAIL = [(lo, hi) for lo, hi in WINDOWS if hi <= REACH]
print(f"\n      reach = {REACH:.0f}; available windows: {AVAIL}")

# ---- Ⓔ⑤ THE SCREEN, RUN FIRST -------------------------------------------------------------------
print("\n" + "=" * 100)
print("  Ⓔ⑤  THE SCREEN, RUN BEFORE THE FIT -- OVERLAP WITH THE RESIDUAL THE TILT LEAVES")
print("=" * 100)
print(f"\n      {'window':>12}{'corr(S,tilt)':>15}{'w_m vs resid':>15}"
      f"{'w_m removes':>14}{'tilt removes':>14}")
OVER = []
for lo, hi in AVAIL:
    keep = window(lo, hi)
    F = _fisher(keep)
    base = CS.bin_spectrum(LS, DL)[keep]

    def perp(v):
        return v - base * float((base @ F @ v) / (base @ F @ base))

    def corr(a, b):
        return float((a @ F @ b) / np.sqrt((a @ F @ a) * (b @ F @ b)))
    d_sig = perp(CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep])
    d_wm = perp(CS.bin_spectrum(LS, DL * np.interp(LS, ML_, np.asarray(_WR(W_STEP))))[keep])
    d_tl = perp(CS.bin_spectrum(LS, DL * (LS / 1000.0) ** 0.01)[keep])
    resid = d_sig - d_tl * float((d_tl @ F @ d_sig) / (d_tl @ F @ d_tl))

    def sh(d):
        return float((d_sig @ F @ d) ** 2 / ((d @ F @ d) * (d_sig @ F @ d_sig))) * 100.0
    OVER.append(dict(lbl=f'{lo}-{hi}', rem=sh(d_wm), tilt=sh(d_tl),
                     c_st=corr(d_sig, d_tl), r_wm=corr(d_wm, resid)))
    o = OVER[-1]
    print(f"      {o['lbl']:>12}{o['c_st']:>15.4f}{o['r_wm']:>15.4f}"
          f"{o['rem']:>13.2f}%{o['tilt']:>13.1f}%")
print("      ⌗ against the RESIDUAL the four already banked scored: A_L +0.359/+0.427/+0.160,")
print("        Y_He +0.303/+0.176/+0.306, N_eff -0.034/+0.134/+0.180, omega_b -0.343/-0.096/+0.134.")
print("        A_L was the first above 0.35 on the published window.")

# ---- Ⓕ⑥ / Ⓖ⑦ / Ⓗ⑧  THE FIT ---------------------------------------------------------------------


def fit2(target, keep, F):
    def at(dn):
        m = CS.bin_spectrum(LS, DL * (LS / 1000.0) ** dn)[keep]
        A = float((m @ F @ target) / (m @ F @ m))
        r = target - A * m
        return float(r @ F @ r)
    o = minimize_scalar(at, bounds=(-3.0, 3.0), method='bounded', options={'xatol': 1e-10})
    return float(o.x), float(at(float(o.x)))


def fit3(target, keep, F):
    def at(p):
        m = CS.bin_spectrum(LS, DL * (LS / 1000.0) ** float(p[0]) * ratio_on_LS(p[1]))[keep]
        A = float((m @ F @ target) / (m @ F @ m))
        r = target - A * m
        return float(r @ F @ r)
    runs = []
    for dn0 in (-0.30, -0.10, 0.0, 0.10):
        for w0 in W_STARTS:
            o = minimize(at, x0=[dn0, w0], method='L-BFGS-B',
                         bounds=[(-3.0, 3.0), (WS_[0], WS_[-1])],
                         options={'ftol': 1e-14, 'gtol': 1e-12})
            runs.append((float(o.fun), float(o.x[0]), float(o.x[1])))
    best = min(runs)
    spread = tuple(max(x[i] for x in runs) - min(x[i] for x in runs) for i in range(3))
    return best[1], best[2], best[0], spread


print("\n" + "=" * 100)
print("  Ⓕ⑥ / Ⓗ⑧ -- THE FIT, AND THE EXCURSION ON BOTH RULERS")
print("=" * 100)
ROWS = []
for lo, hi in AVAIL:
    keep = window(lo, hi)
    n = int(keep.sum())
    F = _fisher(keep)
    tgt = CS.bin_spectrum(LS, DL * np.exp(-K * (LS / LD) ** 2))[keep]
    m_amp = CS.bin_spectrum(LS, DL)[keep]
    r_amp = tgt - float((m_amp @ F @ tgt) / (m_amp @ F @ m_amp)) * m_amp
    c_amp = float(r_amp @ F @ r_amp)
    dn2, c2 = fit2(tgt, keep, F)
    dn3, wm3, c3, sp3 = fit3(tgt, keep, F)
    edge = min(abs(wm3 - WS_[0]), abs(wm3 - WS_[-1])) < 1e-9
    ROWS.append(dict(lo=lo, hi=hi, n=n, dn2=dn2, dn3=dn3, c2=c2, c3=c3, c_amp=c_amp, wm3=wm3,
                     sp3=sp3, edge=edge,
                     d_arm=(wm3 - WM_ARM) / SIG_WM_ARM,
                     d_bank=(wm3 - W0) / SIG_WM_ARM,
                     om_at_arm=wm3 / H_USED ** 2, om_at_bank=wm3 / H_BANK ** 2,
                     surv=abs(dn3) / abs(dn2) * 100.0,
                     a2=(1 - c2 / c_amp) * 100.0, a3=(1 - c3 / c_amp) * 100.0))
    r = ROWS[-1]
    print(f"\n      window {lo}-{hi}, {n} bins")
    print(f"        + tilt          : chi^2/bin {c2 / n:>8.4f}  Delta n {dn2:+.5f}"
          f"  absorbed {r['a2']:5.1f} %")
    print(f"        + tilt + omega_m: chi^2/bin {c3 / n:>8.4f}  Delta n {dn3:+.5f}"
          f"  absorbed {r['a3']:5.1f} %")
    print(f"        omega_m wanted  : {wm3:.6f}"
          + ("   ⛔ AT THE BANK'S EDGE -- A BOUND, NOT A FIT" if edge else "   (interior)"))
    print(f"          vs the ARM's published point {WM_ARM:.6f} : "
          f"{wm3 - WM_ARM:+.6f} = {r['d_arm']:+.3f} sigma(omega_m)")
    print(f"          vs the BANK's own centre     {W0:.6f} : "
          f"{wm3 - W0:+.6f} = {r['d_bank']:+.3f} sigma(omega_m)")
    print(f"          as Omega_m : {r['om_at_arm']:.6f} at the arm's h, "
          f"{r['om_at_bank']:.6f} at the bank's h")
    print(f"          the control's ruler {OM_CTRL} +/- {SIG_OM_CTRL} : "
          f"{(r['om_at_arm'] - OM_CTRL) / SIG_OM_CTRL:+.3f} sigma at the arm's h, "
          f"{(r['om_at_bank'] - OM_CTRL) / SIG_OM_CTRL:+.3f} at the bank's")
    print(f"          DIRECTION vs the standing {DISP_SIGMA:+.3f} sigma arm-TT-against-BAO gap: "
          f"{'TOWARD the arm''s own TT minimum' if wm3 < WM_ARM else 'AWAY from both'}")
    print(f"        SURVIVES        : {r['surv']:.3f} per cent   (multistart spread: "
          f"Delta n {sp3[1]:.1e}, omega_m {sp3[2]:.1e})")

print(f"\n      survival: {', '.join('%.3f' % r['surv'] for r in ROWS)} per cent")
print(f"      absorbed-share gain: {', '.join('%+.2f' % (r['a3'] - r['a2']) for r in ROWS)} points"
      f"   (A_L +4.18/+1.79/+0.15, Y_He +4.90/+0.40/+0.39, omega_b +4.4, N_eff <=+0.25)")

print("\n" + "=" * 100 + "\n  Ⓖ⑦  THE SCREEN'S PREDICTION AGAINST THE FIT, ON THE FIT'S OWN BASE\n"
      + "=" * 100)
print(f"\n      {'window':>12}{'PREDICTED':>12}{'MEASURED':>11}{'ratio':>8}{'interior':>10}")
PRED = []
for o, r in zip(OVER, ROWS):
    pred = float(o['r_wm']) ** 2 * (1.0 - float(o['c_st']) ** 2) * 100.0
    meas = r['a3'] - r['a2']
    PRED.append((pred, meas))
    print(f"      {o['lbl']:>12}{pred:>11.3f}%{meas:>10.3f}%"
          f"{(meas / pred if pred > 0 else float('nan')):>8.2f}{str(not r['edge']):>10}")

np.savez(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'runs', 'r7814_probe.npz'),
         grid=WS_, wrat=WRAT, surv=np.array([r['surv'] for r in ROWS]),
         wm3=np.array([r['wm3'] for r in ROWS]),
         a2=np.array([r['a2'] for r in ROWS]), a3=np.array([r['a3'] for r in ROWS]),
         r_wm=np.array([o['r_wm'] for o in OVER]), rem=np.array([o['rem'] for o in OVER]),
         c_st=np.array([o['c_st'] for o in OVER]),
         lA=INV['lA'], rs=INV['rs'], DM=INV['DM'],
         d_arm=np.array([r['d_arm'] for r in ROWS]),
         pred=np.array([p for p, _ in PRED]))
print("\n  ⌗ probe written to runs/r7814_probe.npz")
