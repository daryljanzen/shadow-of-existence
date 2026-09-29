"""ⓐⓑⓒ THE ACCOUNTING -- cc66.65's OWN INSTRUMENT TURNED ON THE TERM MIX -- r7035+cc66.67.

⛔ *`PREDICTION.md` was committed as its own commit before this file was run.*

** THE FORK IS WITHDRAWN AND THE MEASUREMENT STANDS. **  66: a noise null asks whether a quantity is
distinguishable from noise, and EVERY acoustically structured quantity in this decomposition is.  A test every
candidate passes cannot identify a carrier.

** AND A SHARE OF A MODULATION IS ADDITIVE ONLY UNDER VECTOR SUBTRACTION AT THE MEASURED PHASE. **
Two combs at one period combine as A^2 = A1^2 + A2^2 + 2 A1 A2 cos(D), so AMPLITUDES DO NOT ADD.  The
accounting is done complex (primary) AND as the naive amplitude ratio, so the gap between them is visible.
"""
import os
import sys

import numpy as np
import scipy.linalg

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
sys.path.insert(0, os.path.join(HERE, '..', '..', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                             # noqa: E402

QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr.npz'))['q_edges'], float)
LC, _FAC = CS.bin_center_and_fac()


def load(n):
    d = np.load(os.path.join(SP, n))
    return d['ls'].astype(float), d['Dl'], float(d['l_A'])


print(__doc__)
print('=' * 104)

LSC, DLC, AAC = load('r6941_fine_lcdm.npz')
LSA, DLA, _ = load('r6941_fine_cr.npz')
MC, MA = CS.bin_spectrum(LSC, DLC), CS.bin_spectrum(LSA, DLA)
KN = {}
for nm, fn in (('window', 'r6959_nswap_lcdm.npz'), ('term mix', 'r6975_mix_lcdm.npz')):
    ls, dl, _ = load(fn)
    KN[nm] = CS.bin_spectrum(ls, dl)
OK = np.isfinite(MC) & np.isfinite(MA) & np.all([np.isfinite(v) for v in KN.values()], axis=0)
QB = (LC / AAC)[OK]
COV = CS.COV_TT[np.ix_(OK, OK)]
F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(COV), np.identity(int(OK.sum())))
F = 0.5 * (F + F.T)
mc, dat, LL = MC[OK], CS.X_DATA[OK], LC[OK]
SPEC = {'the ARM': MA[OK], 'window': KN['window'][OK], 'term mix': KN['term mix'][OK]}
MSK = [(QB >= a) & (QB < b) for a, b in zip(QE[:-1], QE[1:])]
HI = MSK[3] | MSK[4] | MSK[5] | MSK[6]
qh = QB[HI]
x = np.log(qh / qh.mean())
_xf = np.log(LL / LL.mean())


def shape_fit(m, data):
    X = m.reshape(-1, 1)
    return X @ scipy.linalg.solve(X.T @ F @ X, X.T @ F @ data, assume_a='sym')


RC = dat - shape_fit(mc, dat)


def parts(m):
    d = shape_fit(m, dat) - shape_fit(mc, dat)
    return d * (F @ d), -2.0 * d * (F @ RC), d


def detrend(v):
    return v - np.polyval(np.polyfit(x, v, 1), x)


_X1 = np.column_stack([np.cos(2.0 * np.pi * qh), np.sin(2.0 * np.pi * qh)])


def vec(v):
    """⛭ THE COMB AS A VECTOR (c, s) rather than an amplitude -- this is what makes it an accounting"""
    return scipy.linalg.lstsq(_X1, detrend(v))[0]


def amp(v):
    c = vec(v)
    return float(np.hypot(*c))


def phase(v):
    c = vec(v)
    return float(np.arctan2(-c[1], c[0]))


def wrap(a):
    return float((a + np.pi) % (2.0 * np.pi) - np.pi)


QD, CR, DD = {}, {}, {}
for k, m in SPEC.items():
    QD[k], CR[k], DD[k] = parts(m)
EX = {k: (QD[k] + CR[k]) for k in SPEC}

# ---------------------------------------------------------------- the noise null, 70's construction
rng = np.random.default_rng(7035)
Lc = np.linalg.cholesky(COV)
base = shape_fit(mc, dat)
NDRAW = 2000


def null_amp(which):
    out = []
    for _ in range(NDRAW):
        ds = base + Lc @ rng.standard_normal(len(dat))
        rc = ds - shape_fit(mc, ds)
        d = shape_fit(SPEC[which], ds) - shape_fit(mc, ds)
        out.append(amp((d * (F @ (d - 2.0 * rc)))[HI]))
    return np.array(out)


print("\n  ⛔ GATE 1: DOES cc66.65's WINDOW ACCOUNTING REPRODUCE?  If not, this is not the same instrument.")
print('-' * 104)
d_arm, d_win, d_mix = DD['the ARM'][HI], DD['window'][HI], DD['term mix'][HI]
pw = wrap(phase(d_win) - phase(d_arm))
rw = amp(d_win) / amp(d_arm)
pred_w = rw * amp(CR['the ARM'][HI])
print(f"    window, spectrum level : phase {pw:+.2f} rad (cc66.65: +0.27), ratio {rw:.3f} (0.264)")
print(f"    and the prediction     : {rw:.3f} x {amp(CR['the ARM'][HI]):.3f} = {pred_w:.3f} "
      f"against a measured {amp(CR['window'][HI]):.3f}  (cc66.65: 1.646 vs 1.893)")
print(f"    ⇒ *** {'REPRODUCED' if abs(pw - 0.27) < 0.05 and abs(rw - 0.264) < 0.01 else 'NOT REPRODUCED -- STOP'} ***")

print("\n  ⛭⛭⛭ ⓐ THE TERM MIX'S MODULATED PART AGAINST THE ARM'S")
print('-' * 104)
pm = wrap(phase(d_mix) - phase(d_arm))
rm = amp(d_mix) / amp(d_arm)
print(f"    {'quantity':26s}{'amp':>12s}{'phase-arm':>12s}{'ratio to arm':>14s}")
for nm, v in (('d_arm  (spectrum)', d_arm), ('d_termmix', d_mix), ('d_window', d_win)):
    print(f"    {nm:26s}{amp(v):>12.4e}{wrap(phase(v) - phase(d_arm)):>+12.2f}"
          f"{amp(v) / amp(d_arm):>14.3f}")
print(f"    ⇒ the term mix's spectrum-level modulation sits {pm:+.2f} rad from the arm's at a ratio of "
      f"{rm:.3f}")

print("\n  ⛭⛭ ⓑ DOES THAT RATIO PREDICT THE ARM'S MEASURED MODULATION, AS IT DID FOR THE WINDOW?")
print('-' * 104)
A_ARM_X = amp(CR['the ARM'][HI])
pred_m = rm * A_ARM_X
meas_m = amp(CR['term mix'][HI])
print(f"    the arm's cross-term modulation      : {A_ARM_X:.3f}")
print(f"    predicted for the term mix           : {rm:.3f} x {A_ARM_X:.3f} = {pred_m:.3f}")
print(f"    measured for the term mix            : {meas_m:.3f}")
print(f"    ⇒ the prediction is off by {abs(pred_m - meas_m) / meas_m:.0%}   "
      f"(the window's was off by {abs(pred_w - amp(CR['window'][HI])) / amp(CR['window'][HI]):.0%})")

print("\n  ⛭⛭⛭ ⓒ THE RESIDUE -- AND IT IS A VECTOR SUBTRACTION, WHICH IS WHAT MAKES IT AN ACCOUNTING")
print('-' * 104)
va, vm, vw = vec(EX['the ARM'][HI]), vec(EX['term mix'][HI]), vec(EX['window'][HI])
print("    *the arm's modulation as a vector in the (cos, sin) plane, and each channel's, at the same "
      "period -- so the subtraction is done AT THE MEASURED PHASE and the parts close exactly.*")
print(f"\n    {'quantity':26s}{'c':>11s}{'s':>11s}{'amp':>9s}{'phase-arm':>12s}")
for nm, v in (('the ARM excess', va), ('term mix', vm), ('window', vw)):
    print(f"    {nm:26s}{v[0]:>11.3f}{v[1]:>11.3f}{np.hypot(*v):>9.3f}"
          f"{wrap(np.arctan2(-v[1], v[0]) - np.arctan2(-va[1], va[0])):>+12.2f}")

SCALES = {'spectrum-level ratio': rm,
          'least-squares projection': float(va @ vm / (vm @ vm))}
print(f"\n    ⛔ TWO SCALE CHOICES, BOTH DECLARED IN ADVANCE, NEITHER CHOSEN:")
print(f"      {'scale':28s}{'k':>9s}{'k*channel':>12s}{'residue':>10s}{'share':>9s}{'closes?':>10s}")
OUT = {}
for nm, k in SCALES.items():
    contrib = k * vm
    res = va - contrib
    share = float(np.hypot(*contrib) / np.hypot(*va))
    closes = abs(np.hypot(*(contrib + res)) - np.hypot(*va)) < 1e-9
    OUT[nm] = (k, float(np.hypot(*contrib)), float(np.hypot(*res)), share, closes)
    print(f"      {nm:28s}{k:>9.3f}{np.hypot(*contrib):>12.3f}{np.hypot(*res):>10.3f}"
          f"{share:>9.1%}{'EXACT' if closes else 'NO':>10s}")
print("      ⌗ *`closes?` is the gate: the contribution plus the residue must reconstruct the arm's own "
      "vector to numerical precision, or the subtraction is not what it claims.*")

print(f"\n    ⌗ AND THE NAIVE AMPLITUDE RATIO ALONGSIDE, so the gap the phase offset makes is visible:")
naive = np.hypot(*vm) / np.hypot(*va)
dphi = wrap(np.arctan2(-vm[1], vm[0]) - np.arctan2(-va[1], va[0]))
print(f"      amplitude ratio |v_mix| / |v_arm|            : {naive:.1%}")
print(f"      the phase offset between them                : {dphi:+.2f} rad")
for nm, (k, ca, ra, sh, _) in OUT.items():
    print(f"      vector share on the {nm:26s}: {sh:.1%}   "
          f"(naive - vector = {naive - sh:+.1%})")

print(f"\n    ⛭ AND THE TWO-CHANNEL PICTURE, since the window's numbers are in hand:")
kw = float(va @ vw / (vw @ vw))
print(f"      {'channel':16s}{'k (least-sq)':>14s}{'contribution':>14s}{'share of arm':>14s}"
      f"{'phase-arm':>12s}")
for nm, v in (('term mix', vm), ('window', vw)):
    k = float(va @ v / (v @ v))
    print(f"      {nm:16s}{k:>14.3f}{np.hypot(*(k * v)):>14.3f}"
          f"{np.hypot(*(k * v)) / np.hypot(*va):>13.1%}{wrap(np.arctan2(-v[1], v[0]) - np.arctan2(-va[1], va[0])):>+12.2f}")
both = np.column_stack([vm, vw])
kk = scipy.linalg.lstsq(both, va)[0]
res_both = va - both @ kk
print(f"      {'BOTH together':16s}{'':>14s}{np.hypot(*(both @ kk)):>14.3f}"
       f"{np.hypot(*(both @ kk)) / np.hypot(*va):>13.1%}")
print(f"      ⇒ residue after BOTH channels: {np.hypot(*res_both):.3f} of the arm's "
      f"{np.hypot(*va):.3f}  ({np.hypot(*res_both) / np.hypot(*va):.1%})")
print("      ⌗ *two channels span the (cos, sin) plane, so together they can reach ANY vector -- **that is "
      "arithmetic, not attribution**, and it is printed to be discounted rather than quoted.*")

print("\n  ⛔⛔ AND HERE IS WHY NEITHER SHARE CAN ATTRIBUTE, AND IT IS AN IDENTITY RATHER THAN A DOUBT")
print('-' * 104)
print("    *In a two-dimensional (cos, sin) plane the least-squares scale is k = (v_a . v)/(v . v), so the "
      "contribution's length is |k v| = |v_a . v| / |v| = |v_a| |cos D|.*")
print("    ⇒ *** THE LEAST-SQUARES SHARE IS |cos D| EXACTLY.  IT DEPENDS ONLY ON THE PHASE OFFSET AND NOT "
      "AT ALL ON THE CHANNEL'S AMPLITUDE. ***")
print(f"\n      {'channel':16s}{'phase offset D':>16s}{'|cos D|':>10s}{'measured share':>16s}{'agree?':>9s}")
for nm, v in (('term mix', vm), ('window', vw)):
    dd = wrap(np.arctan2(-v[1], v[0]) - np.arctan2(-va[1], va[0]))
    k = float(va @ v / (v @ v))
    sh = float(np.hypot(*(k * v)) / np.hypot(*va))
    print(f"      {nm:16s}{dd:>+16.3f}{abs(np.cos(dd)):>10.4f}{sh:>16.4f}"
          f"{'EXACT' if abs(abs(np.cos(dd)) - sh) < 1e-9 else 'no':>9s}")
print(f"\n    ⇒ *** AND THE WINDOW IS THE PROOF: it sits in ANTIPHASE, {wrap(np.arctan2(-vw[1], vw[0]) - np.arctan2(-va[1], va[0])):+.2f} rad from the arm, "
      f"and scores {float(np.hypot(*((va @ vw / (vw @ vw)) * vw)) / np.hypot(*va)):.1%} -- at a scale of "
      f"{float(va @ vw / (vw @ vw)):+.3f}, which turns its cost UPSIDE DOWN to get there. ***")
print("      ⌗ *A quantity that assigns a channel 100% of the authorship for pointing the OPPOSITE way is "
      "not measuring authorship.  This is `cc66.65`'s own guard a third time: **an arithmetic identity is "
      "not a measurement**, and the time to say so is before the run -- which `PREDICTION.md` did.*")
print("\n    ⛔ AND THE OTHER SCALE IS THE ONE `ⓑ` JUST INVALIDATED FOR THIS CHANNEL:")
print(f"      the spectrum-level ratio predicts the window's cost modulation to "
      f"{abs(pred_w - amp(CR['window'][HI])) / amp(CR['window'][HI]):.0%} and the term mix's to "
      f"{abs(pred_m - meas_m) / meas_m:.0%}")
print("      ⇒ *so the scale 66's window template used does NOT carry over to the term mix, and the "
      "68.3% share built on it rests on a ratio this revision has shown fails by a factor of two.*")

print(f"\n  ⛔ AND THE UNCERTAINTY, from the noise null where one is needed")
print('-' * 104)
for k in ('the ARM', 'term mix'):
    n = null_amp(k)
    a = amp(EX[k][HI])
    print(f"    {k:12s} amp {a:>7.3f}   null median {np.median(n):>7.3f}   max {n.max():>7.3f}   "
          f"{int((n >= a).sum())} of {NDRAW} reach it")
print('\n' + '=' * 104)
