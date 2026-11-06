"""`PO-87`: does the acceptance law predict the own-comb offset and slope?

ARM (5) FIRST, as registered: are the two objects commensurable at all?
  * the LAW's A_l = |INT W exp(2 i k r_s*) dk| / INT W dk is the fraction of the COMB's own amplitude
    that survives the kernel's k-integration at multipole l.  Banked as `A` per arm, 238 multipoles.
  * the OWN-COMB reading is a band-RMS of the D_l oscillation over the band-RMS of the SOURCE
    oscillation, arm over control, on each arm's own fitted comb.
Both are dimensionless retentions, and the arm/control RATIO of the first is the natural analogue of
the second.  THE BRIDGE IS STATED RATHER THAN ASSUMED: the law is banded by its BAND MEAN (it is
already an amplitude fraction, not an oscillation to take an RMS of), on the same twelve settings.
"""
import os
import sys
import numpy as np
ROOT = '/home/user/shadow-of-existence'
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7637_70_own_comb_statistic'))
import own_comb as OC
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')

AC = {t: np.load(os.path.join(SP, f'r7041_accept_{n}.npz'), allow_pickle=True)
      for t, n in (('lcdm', 'lcdm'), ('cr', 'cr_leafrec1'))}
Q = {t: AC[t]['ls__fixed'].astype(float) / float(AC[t]['l_A__fixed']) for t in AC}
A = {t: np.asarray(AC[t]['A'], float) for t in AC}

PUB = dict(icept=1.026, slope=0.0103, lo=1.028, hi=1.075, spread=0.0089)

print("  THE LAW, AS BANKED")
for t in AC:
    print(f"    {t:5s} l from {int(AC[t]['ls__fixed'][0]):4d} to {int(AC[t]['ls__fixed'][-1]):4d}, "
          f"q from {Q[t].min():.3f} to {Q[t].max():.3f};  A from {A[t].min():.4f} to {A[t].max():.4f}"
          f"  (r_s* {float(AC[t]['r_s__fixed']):.5f})")

# ---- ARM (5): COMMENSURABILITY, BEFORE ANY ACCOUNTING -------------------------------------------
gq = np.linspace(max(Q['lcdm'].min(), Q['cr'].min()) + 1e-9,
                 min(Q['lcdm'].max(), Q['cr'].max()) - 1e-9, 4000)
Ai = {t: np.interp(gq, Q[t], A[t]) for t in A}
rat = Ai['cr'] / Ai['lcdm']
print(f"\n  ARM (5) -- COMMENSURABILITY CHECK, RUN FIRST")
print(f"    the law's arm/control ratio over the shared q range: {rat.min():.4f} to {rat.max():.4f}"
      f"   (mean {rat.mean():.4f})")
print(f"    the measured own-comb band ratios run {PUB['lo']:.3f} to {PUB['hi']:.3f}")
_wors = max(abs(rat.max() - 1) / max(abs(PUB['hi'] - 1), 1e-9),
            abs(PUB['hi'] - 1) / max(abs(rat.max() - 1), 1e-9))
print(f"    worst ratio-of-excesses between the two objects: {_wors:.2f}  "
      f"(registered threshold: report ILL-POSED above 2)")
COMM = _wors <= 2.0
print(f"    => {'COMMENSURABLE -- the accounting below is licensed' if COMM else 'ILL-POSED -- the accounting below is NOT licensed and is reported as such'}")

# ---- the law banded on the SAME twelve settings ---------------------------------------------------
rows = []
for w, nb, hi in OC.SETTINGS:
    lo = 0.35 + 0.5 * w + 1e-9
    ed = np.linspace(lo, hi, nb + 1)
    xs, ys = [], []
    for a, b in zip(ed[:-1], ed[1:]):
        g = np.linspace(a, b, 400)
        r = np.interp(g, Q['cr'], A['cr']).mean() / np.interp(g, Q['lcdm'], A['lcdm']).mean()
        xs.append((a + b) / 2); ys.append(r)
    xs, ys = np.array(xs), np.array(ys)
    s, c = np.polyfit(xs, ys, 1)
    rows.append((s, c, ys[0], ys[-1]))
SL, IC, LO, HI = (np.array(v) for v in zip(*rows))

print(f"\n  THE LAW ON THE SAME TWELVE SETTINGS")
print(f"    {'':22s} {'the LAW':>12s} {'MEASURED':>12s} {'law / measured excess':>22s}")
for nm, got, pub in (('slope per period', SL.mean(), PUB['slope']),
                     ('intercept', IC.mean(), PUB['icept']),
                     ('lowest band', LO.mean(), PUB['lo']),
                     ('highest band', HI.mean(), PUB['hi'])):
    if nm == 'slope per period':
        frac = got / pub
        print(f"    {nm:22s} {got:+12.5f} {pub:+12.5f} {frac:21.1%}")
    else:
        frac = (got - 1) / (pub - 1)
        print(f"    {nm:22s} {got:12.4f} {pub:12.4f} {frac:21.1%}")
print(f"    spread of the law's slope over the twelve settings: {SL.std():.5f}")
print(f"    the law's intercept is above one in {int((IC > 1).sum())} of {len(IC)} settings")

# ---- band by band, at the 7-band window-1 setting -------------------------------------------------
print(f"\n  BAND BY BAND at the 7-band window-1 setting (the own comb's reference)")
lo = 0.35 + 0.5 * 1.0 + 1e-9
ed = np.linspace(lo, 5.75, 8)
print(f"    {'q band':>13s} {'law A cr':>9s} {'law A ctl':>10s} {'law ratio':>10s}")
for a, b in zip(ed[:-1], ed[1:]):
    g = np.linspace(a, b, 400)
    ac = np.interp(g, Q['cr'], A['cr']).mean()
    al = np.interp(g, Q['lcdm'], A['lcdm']).mean()
    print(f"    {a:5.2f}-{b:5.2f} {ac:9.4f} {al:10.4f} {ac/al:10.4f}")

# ---- the MEASURED own-comb bands beside the law's, band by band -----------------------------------
PR0 = {t: dict(np.load(os.path.join(SP, n))) for t, n in
       (('lcdm', 'r6915_pairs_lcdm.npz'), ('cr', 'r6915_pairs_cr_leafrec1.npz'))}
SO0 = {t: dict(np.load(os.path.join(SP, n))) for t, n in
       (('lcdm', 'r6911_source_lcdm_leafrec1.npz'), ('cr', 'r6911_source_cr_leafrec1.npz'))}
B = {t: dict(QL=PR0[t]['ls'].astype(float) / float(PR0[t]['l_A']),
             QK=SO0[t]['k'] * float(SO0[t]['r_s']) / np.pi,
             Dl=np.asarray(PR0[t]['Dl'], float),
             S2=np.asarray(SO0[t]['S_i'], float) ** 2) for t in PR0}
CB = OC.retention_combs(B)
mx, my = OC.retained_own(B, 1.0, 7, 5.75, C=CB)

print(f"\n  THE ACCOUNTING, BAND BY BAND (7-band window-1 setting)")
print(f"    {'q centre':>9s} {'LAW':>8s} {'MEASURED':>9s} {'law-meas':>9s} "
      f"{'law excess / meas excess':>25s}")
lo = 0.35 + 0.5 * 1.0 + 1e-9
ed = np.linspace(lo, 5.75, 8)
lawb = []
for (a, b) in zip(ed[:-1], ed[1:]):
    g = np.linspace(a, b, 400)
    lawb.append(np.interp(g, Q['cr'], A['cr']).mean() / np.interp(g, Q['lcdm'], A['lcdm']).mean())
lawb = np.array(lawb)
over = 0
for i, (xc, lw, mv) in enumerate(zip(mx, lawb, my)):
    d = lw - mv
    fr = (lw - 1) / (mv - 1) if abs(mv - 1) > 1e-9 else float('nan')
    flag = '  <-- beyond the setting spread 0.0089' if abs(d) > PUB['spread'] else ''
    over += abs(d) > PUB['spread']
    print(f"    {xc:9.2f} {lw:8.4f} {mv:9.4f} {d:+9.4f} {fr:24.1%}{flag}")
print(f"\n    bands disagreeing by more than the own-comb setting spread: {over} of {len(my)}")
print(f"    the law rises monotonically: {bool(np.all(np.diff(lawb) > 0))};  "
      f"the measurement does: {bool(np.all(np.diff(my) > 0))}")
print(f"    law excess summed over bands / measured excess summed: "
      f"{(lawb - 1).sum() / (my - 1).sum():.1%}")
