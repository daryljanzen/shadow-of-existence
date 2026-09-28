#!/usr/bin/env python3
"""r6959 ⓵ᵃ + the ⓵ᵇ prediction: read the two eta-profiles, report the FUNCTION, and solve the taper.

Run before the swap.  Prints the predicted interval and the `SRCTAPER` coefficient the swap needs;
writes nothing but the coefficient file the launcher reads, so the prediction cannot be edited after.
"""
import json
import os
import sys

import numpy as np

D = sys.argv[1] if len(sys.argv) > 1 else '/tmp/n66/r6959/eta'
NF = float(os.environ.get('NFWHM', '3'))
A = {t: np.load(os.path.join(D, f'eta_{t}.npz')) for t in ('lcdm', 'cr')}
QE = A['cr']['q_edges']
QC = 0.5 * (QE[:-1] + QE[1:])
TERMS = ('w2sw', 'w2dp', 'w2isw', 'w2pol')
MEAS = np.array([1.0215, 1.0574, 1.0519, 1.0606, 1.0748, 1.0659, 1.0762])   # cc66.46, r6941_fine_*


def cut(d, nf=NF):
    ee, els, w = d['eta'], float(d['eta_ls']), float(d['eta_ls_w'])
    return (ee >= els - nf * w) & (ee <= els + nf * w)


def amp(d, key='w2md', nf=NF, taper=0.0, s0=None):
    """the amplitude weight and its phase abscissa, over the window"""
    m = cut(d, nf)
    e, s = d['eta'][m], d['rs_leaf'][m]
    a = np.sqrt(np.maximum(d[key][m], 0.0))
    if taper != 0.0:
        _s0 = float(d['rs_leaf'][int(np.argmin(np.abs(d['eta'] - float(d['eta_ls']))))]) \
            if s0 is None else s0
        a = a * np.exp(-taper * (s - _s0) ** 2)[:, None]
    return e, s, a


def moments(d, b, **kw):
    e, s, a = amp(d, **kw)
    w = a[:, b]
    t = float(np.trapezoid(w, e))
    mu = float(np.trapezoid(w * s, e)) / t
    sg = float(np.sqrt(max(np.trapezoid(w * (s - mu) ** 2, e) / t, 0.0)))
    return mu, sg, t


def dfac(d, b, **kw):
    """the EXACT characteristic function of the phase variable under the measured weight"""
    e, s, a = amp(d, **kw)
    w = a[:, b]
    k = np.pi * QC[b] / float(d['r_s'])
    return abs(float(np.trapezoid(w * np.cos(k * s), e)) + 1j
               * float(np.trapezoid(w * np.sin(k * s), e))) / float(np.trapezoid(w, e))


print("=" * 100)
print("r6959 ⓵ᵃ -- THE SOURCE'S CONFORMAL-TIME DEPENDENCE ACROSS THE WINDOW, AS A FUNCTION")
print("=" * 100)
for t in ('lcdm', 'cr'):
    d = A[t]
    print(f"\n  {t}: eta_ls = {float(d['eta_ls']):.2f}  FWHM = {float(d['eta_ls_w']):.2f}  "
          f"r_s = {float(d['r_s']):.3f}  l_A = {float(d['l_A']):.2f}  "
          f"n_eta = {int(d['n_eta'])}  modes = {int(d['n_modes'])}  path = {str(d['path'])}")
    m = cut(d)
    print(f"     Jac over +-{NF:g} FWHM: {d['jac'][m].min():.4f} .. {d['jac'][m].max():.4f};  "
          f"d r_s,leaf / d eta: {np.gradient(d['rs_leaf'][m], d['eta'][m]).mean():.5f}")
    print("     band   sigma_s/r_s   centroid r_s,leaf   D(q)    monopole frac   Doppler   ISW    pol")
    for b in range(len(QC)):
        mu, sg, _ = moments(d, b)
        e = d['eta'][m]
        tot = sum(float(np.trapezoid(d[k][m][:, b], e)) for k in TERMS)
        fr = [float(np.trapezoid(d[k][m][:, b], e)) / tot for k in TERMS]
        print(f"     q={QC[b]:.2f}   {sg / float(d['r_s']):.5f}      {mu:9.3f}       "
              f"{dfac(d, b):.5f}   " + "  ".join(f"{x:.4f}" for x in fr))

print("\n" + "=" * 100)
print("⓵ᵇ THE PREDICTION -- D_cr/D_lcdm, band by band, against the measured excess")
print("=" * 100)
R1 = np.array([dfac(A['cr'], b) / dfac(A['lcdm'], b) for b in range(len(QC))])
print("  band    D_lcdm   D_cr    R1 = D_cr/D_lcdm   predicted interval [R1, R1^2]   measured")
for b in range(len(QC)):
    dl, dc = dfac(A['lcdm'], b), dfac(A['cr'], b)
    lo, hi = sorted((R1[b], R1[b] ** 2))
    print(f"  q={QC[b]:.2f}  {dl:.5f}  {dc:.5f}      {R1[b]:.5f}        "
          f"[{lo:.5f}, {hi:.5f}]         {MEAS[b]:.4f}")

q2 = QC ** 2
fit = np.polyfit(q2, np.log(MEAS), 1)
print(f"\n  R1 SHAPE CHECK (refutation R1): ln(measured excess) vs q^2 -- slope {fit[0]:.6f}, "
      f"intercept {fit[1]:.6f} (excess {np.exp(fit[1]):.4f} at q=0)")
print(f"     intercept / top-band ln excess = {fit[1] / np.log(MEAS[-1]):.3f}  "
      f"(refuted as the WHOLE channel above 0.5)")
f1 = np.polyfit(q2, np.log(R1), 1)
print(f"     the same fit on the PREDICTION: slope {f1[0]:.6f}, intercept {f1[1]:.6f} "
      f"(a smearing must pass through the origin)")
print(f"  R2 SIZE CHECK: ln R1 at the top band {np.log(R1[-1]):.5f} against the measured "
      f"{np.log(MEAS[-1]):.5f}  -> ratio {np.log(R1[-1]) / np.log(MEAS[-1]):.3f} "
      f"(refuted outside [0.5, 2])")
print(f"  R5 SIGN CHECK: D_cr > D_lcdm in every band: {bool(np.all(R1 > 1))}")

print("\n  STABILITY of the prediction in the window cut (the one judgement call in ⓵ᵃ):")
for nf in (2, 3, 4, 5, 6):
    r = [dfac(A['cr'], b, nf=nf) / dfac(A['lcdm'], b, nf=nf) for b in range(len(QC))]
    print(f"     +-{nf} FWHM: R1 = " + "  ".join(f"{x:.5f}" for x in r))
print("  and in WHICH TERM carries the weight -- the Doppler is a quarter period out of phase with")
print("  the monopole, so a weight built from their sum mixes two phases; the monopole alone does not:")
for ky in ('w2md', 'w2sw', 'w2'):
    r = [dfac(A['cr'], b, key=ky) / dfac(A['lcdm'], b, key=ky) for b in range(len(QC))]
    print(f"     {ky:6s}: R1 = " + "  ".join(f"{x:.5f}" for x in r))

print("\n" + "=" * 100)
print("⓵ᵇ THE SWAP -- the taper coefficient that imposes the ARM's spread on the CONTROL")
print("=" * 100)
# one coefficient for the whole spectrum, not one per band: the taper is a function of eta alone.
# It is solved on the band-averaged spread so the swap is a single, stated operation.


def sig_all(d, taper=0.0):
    """the amplitude weight summed over the bands -- the spread the single coefficient targets"""
    e, s, a = amp(d, taper=taper)
    w = a.sum(axis=1)
    t = float(np.trapezoid(w, e))
    mu = float(np.trapezoid(w * s, e)) / t
    return float(np.sqrt(max(np.trapezoid(w * (s - mu) ** 2, e) / t, 0.0)))


s_c, s_l = sig_all(A['cr']), sig_all(A['lcdm'])
tgt = s_c / float(A['cr']['r_s']) * float(A['lcdm']['r_s'])     # the arm's spread in the SAME units
print(f"  control's own spread {s_l:.4f} Mpc ({s_l / float(A['lcdm']['r_s']):.5f} of its r_s); "
      f"arm's {s_c:.4f} Mpc ({s_c / float(A['cr']['r_s']):.5f} of its r_s)")
print(f"  target for the control, matching the arm in units of its OWN r_s: {tgt:.4f} Mpc")
lo, hi = -0.5 / max(s_l, tgt) ** 2, 50.0 / max(s_l, tgt) ** 2
al = 0.0
for _ in range(80):
    al = 0.5 * (lo + hi)
    if sig_all(A['lcdm'], taper=al) > tgt:
        lo = al
    else:
        hi = al
print(f"  => SRCTAPER = {al:.8g} on the control gives {sig_all(A['lcdm'], taper=al):.4f} Mpc "
      f"(Gaussian estimate {(1 / tgt ** 2 - 1 / s_l ** 2) / 2:.8g})")
s0 = float(A['lcdm']['rs_leaf'][int(np.argmin(np.abs(A['lcdm']['eta']
                                                     - float(A['lcdm']['eta_ls']))))])
print(f"  SRCTAPERS0 defaults to r_s,leaf(eta_ls) = {s0:.4f} Mpc on this arm, which is what is used")
PR = np.array([dfac(A['lcdm'], b, taper=al) / dfac(A['lcdm'], b) for b in range(len(QC))])
print("\n  PREDICTED EFFECT OF THE SWAP, band by band -- from the measured weight times the known")
print("  taper, no free parameter.  The contrast is expected in [f, f^2] (see PREDICTION.md ⓵ᵇ4).")
print("  band    f = D_taper/D_own   interval [f, f^2]      R1 (what closing the excess needs)")
for b in range(len(QC)):
    lo2, hi2 = sorted((PR[b], PR[b] ** 2))
    print(f"  q={QC[b]:.2f}    {PR[b]:.5f}           [{lo2:.5f}, {hi2:.5f}]        {R1[b]:.5f}")
out = dict(alpha=al, s0=s0, R1=R1.tolist(), f=PR.tolist(), q=QC.tolist(),
           sigma_lcdm=s_l, sigma_cr=s_c, target=tgt, measured=MEAS.tolist(), nfwhm=NF)
with open(os.path.join(D, 'prediction.json'), 'w') as fh:
    json.dump(out, fh, indent=1)
print(f"\n  written -> {os.path.join(D, 'prediction.json')}")
