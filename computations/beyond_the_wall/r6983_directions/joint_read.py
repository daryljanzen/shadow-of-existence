"""read the r6983 JOINT bank against the four pre-registered conditions -- r6983+cc66.49.

⌗ A READER, not a receipt: it prints the numbers the receipt will gate on, with the machinery
  (`r6911+cc66.40`'s envelope, `cc66.45`'s anchored locator, `cc66.46`'s heights and depths)
  imported by copy from the r6975 receipt so the two read the same way.  ⛔ *The four conditions
  and their tolerances are `PREDICTION.md`'s, committed before this run; nothing here is fitted.*
"""
import os
import sys

import numpy as np
from scipy.interpolate import CubicSpline

# ⌗ four levels: this file sits in computations/beyond_the_wall/r6983_directions/, one deeper than
#   the receipts, which is where the three-level form in the receipt comes from.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                             # noqa: E402

A = {t: np.load(os.path.join(SP, f'r6959_eta_{t}.npz')) for t in ('lcdm', 'cr')}
F = {t: np.load(os.path.join(SP, f'r6941_fine_{t}.npz')) for t in ('lcdm', 'cr')}
WIN = np.load(os.path.join(SP, 'r6959_nswap_lcdm.npz'))
MIX = np.load(os.path.join(SP, 'r6975_mix_lcdm.npz'))
JNT = np.load(os.path.join(SP, 'r6983_joint_lcdm.npz'))

QE = A['cr']['q_edges']
QC = 0.5 * (QE[:-1] + QE[1:])
Q2 = QC ** 2
LF = np.arange(100.0, 1300.0, 1.0)
TR = np.array([396.0, 674.0, 994.0])
PK = np.array([238.0, 537.0, 828.0])
SKY4 = np.array([220.6, 538.1, 809.8, 1121.9])
SKYW = np.array([1.00, 1.20, 1.60, 2.36])
LC, _FAC = CS.bin_center_and_fac()


def env_a(x, y, win=1.0):
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(x, y):
    e = env_a(x, y)
    return (y - e) / e


def band_std(d):
    q = d['ls'].astype(float) / float(d['l_A'])
    o = osc(q, d['Dl'])
    return np.array([float(np.std(np.interp(np.linspace(a, b, 400), q, o)))
                     for a, b in zip(QE[:-1], QE[1:])])


def spl(Db):
    m = (LC >= 100) & np.isfinite(Db)
    return CubicSpline(LC[m], Db[m])(LF)


def anchored(o, a, W, kind):
    return np.array([float(abs(np.min(o[(LF >= x - W) & (LF <= x + W)]))) if kind == 'min'
                     else float(np.max(o[(LF >= x - W) & (LF <= x + W)])) for x in a])


def hd_of(Dl_ls, Dl):
    o = osc(LF / 301.6, spl(CS.bin_spectrum(Dl_ls, Dl)))
    return anchored(o, PK, 40, 'max').mean(), anchored(o, TR, 40, 'min').mean()


def hd(d):
    return hd_of(d['ls'].astype(float), d['Dl'])


def peaks_sub(d, W=40):
    ls, Dl = d['ls'].astype(float), d['Dl']
    out = []
    for a in SKY4:
        m = (ls >= a - W) & (ls <= a + W)
        x, y = ls[m], Dl[m]
        i = int(np.argmax(y))
        dd = 0.5 * (y[i - 1] - y[i + 1]) / (y[i - 1] - 2 * y[i] + y[i + 1]) if 0 < i < len(x) - 1 else 0.
        out.append(float(x[i] + dd * (x[1] - x[0])))
    return np.array(out)


C0 = {t: band_std(F[t]) for t in F}
MEAS = C0['cr'] / C0['lcdm']
RW = band_std(WIN) / C0['lcdm']
RM = band_std(MIX) / C0['lcdm']
RJ = band_std(JNT) / C0['lcdm']

PROD = RW * RM
SUM = RW + RM - 1.0
QUAD = 1.0 + np.sqrt((RW - 1) ** 2 + (RM - 1) ** 2)

print("\n⓵ T-SIZE -- the joint response against the three rules, band by band")
print("  q       window    term mix  |  product   sum       quadrature |  JOINT     measured")
for b in range(len(QC)):
    print(f"  {QC[b]:.2f}   {RW[b]:.5f}   {RM[b]:.5f}  |  {PROD[b]:.5f}   {SUM[b]:.5f}   "
          f"{QUAD[b]:.5f}    |  {RJ[b]:.5f}   {MEAS[b]:.5f}")
for nm, P in (('product', PROD), ('sum', SUM), ('quadrature', QUAD)):
    d = np.abs(RJ - P)
    print(f"    |joint - {nm:10s}|  max {d.max():.5f}   within 0.005 in {int((d < 0.005).sum())}/7 bands")

print("\n⓶ T-WEIGHT -- the anchored heights and depths")
H0, T0 = hd(F['lcdm'])


def read_d(d):
    h, t = hd(d)
    return h / H0 - 1, t / T0 - 1


for nm, d in (('the whole excess', F['cr']), ('window', WIN), ('term mix', MIX), ('JOINT', JNT)):
    dh, dt = read_d(d)
    print(f"    {nm:18s} {100 * dh:+8.3f}%  {100 * dt:+8.3f}%   ratio {dh / dt:6.2f}")
dhw, dtw = read_d(WIN)
dhm, dtm = read_d(MIX)
print(f"    pre-registered additive prediction  ({100*dhw:+.2f}+{100*dhm:+.2f})/"
      f"({100*dtw:+.2f}+{100*dtm:+.2f}) = {(dhw + dhm) / (dtw + dtm):.2f}")

print("\n⓷ T-COMB -- the peaks")
P0 = peaks_sub(F['lcdm'])
MVW = peaks_sub(WIN) - P0
MVM = peaks_sub(MIX) - P0
MVJ = peaks_sub(JNT) - P0
for nm, mv in (('window', MVW), ('term mix', MVM), ('additive', MVW + MVM), ('JOINT', MVJ),
               ("the arm's own", peaks_sub(F['cr']) - P0)):
    print(f"    {nm:15s} " + "  ".join(f"{x:+7.3f}" for x in mv)
          + f"   outside the sky's widths: {int(np.sum(np.abs(mv) > SKYW))}/4")

print("\n⓸ T-INTERCEPT -- the fit against q^2")
for nm, R in (('window', RW), ('term mix', RM), ('JOINT', RJ), ('measured excess', MEAS)):
    s, i = np.polyfit(Q2, np.log(R), 1)
    print(f"    {nm:16s} slope {s:+.6f}  intercept {np.exp(i):.4f} at q=0  "
          f"|slope x <q^2>|/|intercept| = {abs(s * Q2.mean()) / abs(i):.3f}")
print("    pre-registered: product 1.1035, sum 1.1019, quadrature 1.0839; "
      "the measured excess's own 1.0400")

print("\n⓹ THE COMPOSITION RULE, READ AS A FRACTION OF EACH RULE'S OWN PREDICTED EXCESS")
for nm, P in (('product', PROD), ('sum', SUM), ('quadrature', QUAD)):
    f = (RJ - 1) / (P - 1)
    print(f"    joint / {nm:11s} " + "  ".join(f"{x:.4f}" for x in f) + f"   mean {f.mean():.4f}")
print(f"    joint below product in all 7: {bool(np.all(RJ < PROD))};  below sum in all 7: "
      f"{bool(np.all(RJ < SUM))};  above quadrature in all 7: {bool(np.all(RJ > QUAD))}")

print("\n⓺ AND WHAT THE JOINT IS AGAINST THE MEASURED EXCESS -- the arithmetic the row turns on")
OV = (RJ - 1) / (MEAS - 1)
print("    joint / measured, band by band  " + "  ".join(f"{x:.2f}" for x in OV) + f"   mean {OV.mean():.2f}")
_s, _i = np.polyfit(Q2, np.log(RJ), 1)
_sm, _im = np.polyfit(Q2, np.log(MEAS), 1)
print(f"    at q=0: joint offset {np.exp(_i) - 1:.4f} against the measured {np.exp(_im) - 1:.4f}"
      f"  ->  {(np.exp(_i) - 1) / (np.exp(_im) - 1):.2f}x")
print(f"    band-mean: joint {100 * (RJ - 1).mean():.3f}%  measured {100 * (MEAS - 1).mean():.3f}%"
      f"  ->  {(RJ - 1).mean() / (MEAS - 1).mean():.2f}x")
print(f"    the two channels summed ALONE (cc66.48's reading): "
      f"{100 * ((RW - 1).mean() + (RM - 1).mean()):.3f}%"
      f"  ->  {((RW - 1).mean() + (RM - 1).mean()) / (MEAS - 1).mean():.2f}x")
