#!/usr/bin/env python3
r"""r7812 (60) -- PO-24's A_L screen and fit, and tau's exact degeneracy, on order r7807 (69).

Same harness as r7800/r7804/r7806, with the free direction swapped to A_L, read from 70's r7805
bank as a RATIO to its own centre.  The grid is taken from the config's own ALENS list, NOT from the
file's Dl__ keys, because the file also holds an A_L = 0.00 entry that is the unlensed INPUT kept for
reference: including it would distort a monotone spline across the 0.0-to-0.8 gap and move the centre.
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

# ---- the referents.  THE CORPUS CARRIES NO A_L; these are Planck's, and the metric picks which. ---
AL_TT, AL_TT_SIG = 1.243, 0.096          # TT+lowE -- the like-for-like one: this metric is TT alone
AL_JOINT, AL_JOINT_SIG = 1.180, 0.065    # TT,TE,EE+lowE -- the headline, reported beside it

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


AZ = np.load(os.path.join(SP, 'r7805_alens_response_lcdm.npz'), allow_pickle=True)
CFG = json.loads(str(next(AZ[k] for k in AZ.files if k.startswith('config'))))
AS_ = np.array(sorted(float(x) for x in CFG['ALENS']))
A0 = float(AS_[int(np.argmin(np.abs(AS_ - 1.0)))])  # BY VALUE, never the midpoint
ALL_KEYS = sorted({float(k.split('__')[1]) for k in AZ.files if k.startswith('Dl__')})


def _key(pref, w):
    return next(k for k in AZ.files
                if k.startswith(pref + '__') and abs(float(k.split('__')[1]) - w) < 1e-12)


AL_ = AZ[_key('ls', A0)].astype(float)
AD = np.array([AZ[_key('Dl', w)].astype(float) for w in AS_])
ARAT = AD / AD[int(np.argmin(np.abs(AS_ - 1.0)))]
_AR = PchipInterpolator(AS_, ARAT, axis=0)


# ⌗ r7812: EVERY pick off this grid is now BY VALUE.  r7808 took the centre as the midpoint by
#   index, which was 1.0 only because the five-value grid was symmetric about it; on seven values
#   the midpoint is 1.1.  The same hazard sits on the screen's direction (one step ABOVE the centre)
#   and on the multistart seeds, both of which r7808 took as AS_[3] and AS_[1].  They happen to be
#   right on this grid too -- and "happen to be" is the whole problem, so none of them is left to
#   an index.  The seeds also now SPAN the grid: a taller grid whose optimum may sit above the old
#   maximum must be seeded near its top, or the fit can only reach the new region by walking.
A_STEP = float(AS_[AS_ > A0].min())          # the first grid point above the centre
A_STARTS = (float(AS_.min()), A0, A_STEP, float(AS_.max()))


def ratio_on_LS(a):
    rb = np.asarray(_AR(float(a)))
    return np.interp(LS, AL_, rb, left=rb[0], right=rb[-1])


print("=" * 100)
print("r7812 (60) -- A_L REFITTED on the widened 0.8-1.4 grid: does the lensing amplitude absorb the displacement?")
print("=" * 100)
print(f"\n  Ⓑ②  THE REFERENT.  The corpus carries NO A_L, so Planck's is used, and 'Planck's A_L' is")
print(f"      itself several numbers.  THE METRIC PICKS: this harness scores plik_lite TT bandpowers,")
print(f"      temperature alone, so the like-for-like constraint is TT+lowE.")
print(f"        TT+lowE          : {AL_TT} +/- {AL_TT_SIG}   "
      f"({AL_TT_SIG / AL_TT * 100:.1f} %,  {(AL_TT - 1) / AL_TT_SIG:+.1f} sigma from unity)")
print(f"        TT,TE,EE+lowE    : {AL_JOINT} +/- {AL_JOINT_SIG}   "
      f"({AL_JOINT_SIG / AL_JOINT * 100:.1f} %,  {(AL_JOINT - 1) / AL_JOINT_SIG:+.1f} sigma)")
print(f"      ⌗ WIDEST of the four in fractional terms: {AL_TT_SIG / AL_TT * 100:.1f} % against")
print(f"        N_eff's 5.7, omega_b's 0.65 and Y_He's 0.6 -- AND not centred on unity.")

print(f"\n  Ⓐ①  70's bank: the config's ALENS grid is {list(AS_)}, centre {A0}")
print(f"      the file also holds Dl keys at {ALL_KEYS} -- the {ALL_KEYS[0]} entry is the unlensed")
print(f"      INPUT kept for reference and is EXCLUDED from the interpolation grid")
print(f"      its l grid: {AL_[0]:.0f} to {AL_[-1]:.0f} step {AL_[1] - AL_[0]:.0f}, {len(AL_)} points")
print(f"      the lensing potential is a DIFFERENT COSMOLOGY from the arm: "
      f"H0 {CFG['bank']['phiphi']['H0']:.2f}, Om {CFG['bank']['phiphi']['Om']:.4f}")
print(f"      against the construction's 68.6 and 0.2973 -- a LCDM stand-in, declared not assumed")

INV = {}
for nm in ('lA', 'rs', 'DM'):
    INV[nm] = np.array([float(AZ[_key(nm, w)]) for w in AS_])
    print(f"      {nm:>4s} across the grid: {INV[nm][0]:.6f} .. {INV[nm][-1]:.6f}"
          f"   spread {float(INV[nm].max() - INV[nm].min()):.3e}")

MAXDEV = [float(np.abs(r - 1).max()) for r in ARAT]
print(f"\n      response size, per mille: "
      f"{', '.join('%.2f' % (d * 1000) for d in MAXDEV)}")
_top = ARAT[-1] - 1.0
_sgn = np.sign(_top)
_ch = [float(AL_[i]) for i in np.where(np.diff(_sgn) != 0)[0]]
_gaps = np.diff(_ch)
LA = float(INV['lA'][0])
print(f"      SIGN CHANGES of the A_L={AS_[-1]} response: {len(_ch)} of them, at l = "
      f"{[int(x) for x in _ch]}")
print(f"      mean spacing {float(_gaps.mean()):.1f} against half the acoustic scale "
      f"{LA / 2:.1f} -- ratio {float(_gaps.mean()) / (LA / 2):.3f}")
print(f"      ⇒ it oscillates at the PEAK-TROUGH period, which is what a smoothing operator does:")
print(f"        power moves from peaks to troughs, so the sign flips at every extremum.  The order")
print(f"        said 'changes sign near l = 1600'; that is ONE of {len(_ch)}, and the structure is")
print(f"        the whole comb rather than a single crossing.")

REACH = float(AL_[-1])
WINDOWS = [(100, 1758), (700, 1760), (1000, 1760), (1000, 2508), (1400, 2508), (100, 2508)]
AVAIL = [(lo, hi) for lo, hi in WINDOWS if hi <= REACH]
print(f"\n      reach = {REACH:.0f}; available windows: {AVAIL}")

# ---- Ⓔ⑤ TAU: AN EXACT DEGENERACY WITH THE AMPLITUDE THE HARNESS ALREADY FREES -------------------
print("\n" + "=" * 100)
print("  Ⓔ⑤  TAU IS NOT A CANDIDATE IN THIS METRIC -- A DERIVATION, MEASURED")
print("=" * 100)
TAU = []
for lo, hi in AVAIL:
    keep = window(lo, hi)
    F = _fisher(keep)
    base = CS.bin_spectrum(LS, DL)[keep]
    for dt in (0.01, 0.02, 0.05):
        sc = CS.bin_spectrum(LS, DL * np.exp(-2 * dt))[keep]
        A = float((sc @ F @ base) / (sc @ F @ sc))
        r = base - A * sc
        TAU.append(dict(lbl=f'{lo}-{hi}', dt=dt, chi2=float(r @ F @ r),
                        A=A, want=float(np.exp(2 * dt))))
        t = TAU[-1]
        print(f"      window {t['lbl']:>10}  d_tau {dt:.2f} : residual chi2 {t['chi2']:.3e}   "
              f"A {t['A']:.9f}  vs exp(+2 d_tau) {t['want']:.9f}")
print("      ⇒ exact to machine precision on every window: tau's whole TT effect above the")
print("        reionisation bump IS the one amplitude this harness already marginalises.")

# ---- Ⓒ③ THE SCREEN ------------------------------------------------------------------------------
print("\n" + "=" * 100)
print("  Ⓒ③  THE SCREEN, RUN FIRST -- OVERLAP WITH THE RESIDUAL THE TILT LEAVES")
print("=" * 100)
print(f"\n      {'window':>12}{'corr(S,tilt)':>15}{'A_L vs resid':>15}"
      f"{'A_L removes':>14}{'tilt removes':>14}")
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
    d_al = perp(CS.bin_spectrum(LS, DL * np.interp(LS, AL_, np.asarray(_AR(A_STEP))))[keep])
    d_tl = perp(CS.bin_spectrum(LS, DL * (LS / 1000.0) ** 0.01)[keep])
    resid = d_sig - d_tl * float((d_tl @ F @ d_sig) / (d_tl @ F @ d_tl))

    def sh(d):
        return float((d_sig @ F @ d) ** 2 / ((d @ F @ d) * (d_sig @ F @ d_sig))) * 100.0
    OVER.append(dict(lbl=f'{lo}-{hi}', rem=sh(d_al), tilt=sh(d_tl),
                     c_st=corr(d_sig, d_tl), r_al=corr(d_al, resid)))
    o = OVER[-1]
    print(f"      {o['lbl']:>12}{o['c_st']:>15.4f}{o['r_al']:>15.4f}"
          f"{o['rem']:>13.2f}%{o['tilt']:>13.1f}%")
print("      ⌗ read beside: of the SIGNATURE, Y_He removed 53.5/32.3/10.5 per cent, omega_b")
print("        3.3/5.7/20.0 and N_eff 0.1/0.2/1.9; against the RESIDUAL, Y_He scored")
print("        0.303/0.176/0.306, N_eff -0.034/0.134/0.180 and omega_b -0.343/-0.096/0.134.")

# ---- Ⓓ④ THE FIT ---------------------------------------------------------------------------------


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
        for a0 in A_STARTS:
            o = minimize(at, x0=[dn0, a0], method='L-BFGS-B',
                         bounds=[(-3.0, 3.0), (AS_[0], AS_[-1])],
                         options={'ftol': 1e-14, 'gtol': 1e-12})
            runs.append((float(o.fun), float(o.x[0]), float(o.x[1])))
    best = min(runs)
    spread = tuple(max(x[i] for x in runs) - min(x[i] for x in runs) for i in range(3))
    return best[1], best[2], best[0], spread


print("\n" + "=" * 100)
print("  Ⓓ④ / Ⓖ⑦ / Ⓗ⑧ -- THE FIT")
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
    dn3, al3, c3, sp3 = fit3(tgt, keep, F)
    ROWS.append(dict(lo=lo, hi=hi, n=n, dn2=dn2, dn3=dn3, c2=c2, c3=c3, c_amp=c_amp, al3=al3,
                     dtt=al3 - AL_TT, djo=al3 - AL_JOINT, sp3=sp3,
                     surv=abs(dn3) / abs(dn2) * 100.0,
                     a2=(1 - c2 / c_amp) * 100.0, a3=(1 - c3 / c_amp) * 100.0,
                     edge=min(abs(al3 - AS_[0]), abs(al3 - AS_[-1])) < 1e-9))
    r = ROWS[-1]
    print(f"\n      window {lo}-{hi}, {n} bins")
    print(f"        + tilt         : chi^2/bin {c2 / n:>8.4f}  Delta n {dn2:+.5f}"
          f"  absorbed {r['a2']:5.1f} %")
    print(f"        + tilt + A_L   : chi^2/bin {c3 / n:>8.4f}  Delta n {dn3:+.5f}"
          f"  absorbed {r['a3']:5.1f} %")
    print(f"        A_L wanted     : {al3:.5f}"
          + ("   ⛔ AT THE BANK'S EDGE -- A BOUND, NOT A FIT" if r['edge'] else ""))
    print(f"          vs TT+lowE   {AL_TT} +/- {AL_TT_SIG} : {r['dtt']:+.5f} = "
          f"{r['dtt'] / AL_TT_SIG:+.2f} sigma")
    print(f"          vs the joint {AL_JOINT} +/- {AL_JOINT_SIG} : {r['djo']:+.5f} = "
          f"{r['djo'] / AL_JOINT_SIG:+.2f} sigma")
    print(f"        SURVIVES       : {r['surv']:.3f} per cent   (multistart spread: "
          f"Delta n {sp3[1]:.1e}, A_L {sp3[2]:.1e})")

print(f"\n      survival: {', '.join('%.3f' % r['surv'] for r in ROWS)} per cent")
print(f"      absorbed-share gain: {', '.join('%+.2f' % (r['a3'] - r['a2']) for r in ROWS)} points"
      f"   (Y_He +4.90/+0.40/+0.39, omega_b +4.4, N_eff <=+0.25)")

print("\n" + "=" * 100 + "\n  Ⓕ⑥  THE SCREEN'S PREDICTION AGAINST THE FIT, ON THE FIT'S OWN BASE\n"
      + "=" * 100)
print(f"\n      {'window':>12}{'PREDICTED':>12}{'MEASURED':>11}{'ratio':>8}")
PRED = []
for o, r in zip(OVER, ROWS):
    pred = float(o['r_al']) ** 2 * (1.0 - float(o['c_st']) ** 2) * 100.0
    meas = r['a3'] - r['a2']
    PRED.append((pred, meas))
    print(f"      {o['lbl']:>12}{pred:>11.3f}%{meas:>10.3f}%"
          f"{(meas / pred if pred > 0 else float('nan')):>8.2f}")

np.savez(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'runs', 'r7808_probe.npz'),
         grid=AS_, arat=ARAT, surv=np.array([r['surv'] for r in ROWS]),
         al3=np.array([r['al3'] for r in ROWS]),
         a2=np.array([r['a2'] for r in ROWS]), a3=np.array([r['a3'] for r in ROWS]),
         r_al=np.array([o['r_al'] for o in OVER]), rem=np.array([o['rem'] for o in OVER]),
         c_st=np.array([o['c_st'] for o in OVER]),
         tau_chi2=np.array([t['chi2'] for t in TAU]),
         signchanges=np.array(_ch))
print("\n  ⌗ probe written to runs/r7808_probe.npz")
