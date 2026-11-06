"""`r7691` (cc66) arm 2 -- THE DIP TEST, registered before it was run.

Band the own-comb null's real-phase response on the same seven bands as the law-versus-own comparison
and ask whether it reproduces the departure at q ~ 1.9.

REGISTERED: it does NOT -- its band response has no feature there matching +0.019 -- moderate
confidence.  The licence ceiling was fixed in advance and holds whichever way it comes out: a positive
result licenses only consistency IN SHAPE, never "the departure is the drift".

Nothing here is a new instrument: the banks are built exactly as the phase-systematic receipt builds
them (l.220-223, l.306-307) and the null is 70's own `retention_null`.
"""
import os
import sys

import numpy as np

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                'r7637_70_own_comb_statistic'))
import own_comb as OC                                                        # noqa: E402

PR0 = {t: dict(np.load(os.path.join(SP, n))) for t, n in
       (('lcdm', 'r6915_pairs_lcdm.npz'), ('cr', 'r6915_pairs_cr_leafrec1.npz'))}
SO0 = {t: dict(np.load(os.path.join(SP, n))) for t, n in
       (('lcdm', 'r6911_source_lcdm_leafrec1.npz'), ('cr', 'r6911_source_cr_leafrec1.npz'))}
B = {t: dict(QL=PR0[t]['ls'].astype(float) / float(PR0[t]['l_A']),
             QK=SO0[t]['k'] * float(SO0[t]['r_s']) / np.pi,
             Dl=np.asarray(PR0[t]['Dl'], float),
             S2=np.asarray(SO0[t]['S_i'], float) ** 2) for t in PR0}
CB = OC.retention_combs(B)

AC = {t: dict(np.load(os.path.join(SP, f'r7041_accept_{n}.npz'), allow_pickle=True))
      for t, n in (('lcdm', 'lcdm'), ('cr', 'cr_leafrec1'))}
AQ = {t: AC[t]['ls__fixed'].astype(float) / float(AC[t]['l_A__fixed']) for t in AC}
AA = {t: np.asarray(AC[t]['A'], float) for t in AC}


def law_band(a, b):
    g = np.linspace(a, b, 400)
    return (np.interp(g, AQ['cr'], AA['cr']).mean()
            / np.interp(g, AQ['lcdm'], AA['lcdm']).mean())


# the seven bands of the comparison: window 1.0, 7 bands, hi 5.75
ED = np.linspace(0.35 + 0.5 + 1e-9, 5.75, 8)
X, MEAS = OC.retained_own(B, 1.0, 7, 5.75, C=CB)
LAW = np.array([law_band(a, b) for a, b in zip(ED[:-1], ED[1:])])

# the two amplitudes the phase receipt scans: the pre-registered 0.5 and the banks' own
AD0 = float(np.mean([OC.comb(B[t]['QL'], B[t]['Dl'])[3] for t in B]))
AS0 = float(np.mean([OC.comb(B[t]['QK'], B[t]['S2'])[3] for t in B]))
PHI0 = 0.0                                                   # PH[0]: the real phase


def detrend(y):
    return y - np.polyval(np.polyfit(X, y, 1), X)


DEP = MEAS - LAW                                             # the departure, as the receipt reports it
j19 = int(np.argmax(np.abs(DEP)))

print(f"the seven bands, window 1.0, hi 5.75;  worst departure at q = {X[j19]:.2f}\n")
print(f"  {'q':>6s} {'MEASURED':>9s} {'LAW':>8s} {'meas-law':>9s} {'meas detr':>10s}", end='')
rows = {}
for lab, AL, AK in (('null A=0.5', 0.5, 0.5), ('null A=own', AD0, AS0)):
    nb = OC.retention_null(B, AL, AK, PHI0)
    _, y = OC.retained_own(nb, 1.0, 7, 5.75, C=OC.retention_combs(nb))
    rows[lab] = y
    print(f" {lab:>11s} {lab + ' detr':>16s}", end='')
print()
for i in range(len(X)):
    print(f"  {X[i]:6.2f} {MEAS[i]:9.4f} {LAW[i]:8.4f} {DEP[i]:+9.4f} "
          f"{detrend(MEAS)[i]:+10.4f}", end='')
    for lab in rows:
        print(f" {rows[lab][i]:11.4f} {detrend(rows[lab])[i]:+16.4f}", end='')
    print()

print(f"\n  THE DEPARTURE:  {DEP[j19]:+.4f} at q = {X[j19]:.2f};  "
      f"detrended measurement there {detrend(MEAS)[j19]:+.4f}")
md = detrend(MEAS)
for lab in rows:
    nd = detrend(rows[lab])
    print(f"\n  {lab}:")
    print(f"    band response at q = {X[j19]:.2f}: raw {rows[lab][j19]:.4f}, "
          f"detrended {nd[j19]:+.4f}")
    print(f"    is that a feature there?  it is band {int(np.argmax(np.abs(nd))) + 1} of 7 by "
          f"|detrended|, worst {np.max(np.abs(nd)):+.4f} at q = {X[int(np.argmax(np.abs(nd)))]:.2f}")
    print(f"    fraction of the departure it reproduces at q = {X[j19]:.2f}: "
          f"{nd[j19] / md[j19]:+.3f} of the detrended measurement, "
          f"{nd[j19] / DEP[j19]:+.3f} of meas-law")
    print(f"    shape correlation with the detrended measurement over the seven bands: "
          f"{np.corrcoef(nd, md)[0, 1]:+.3f}")
    print(f"    shape correlation with meas-law: {np.corrcoef(nd, DEP)[0, 1]:+.3f}")
    print(f"    r.m.s. of its detrended shape {np.sqrt((nd ** 2).mean()):.4f} against the "
          f"measurement's {np.sqrt((md ** 2).mean()):.4f}")

# =====================================================================================================
# ⛔ THE REGISTERED PREDICTION IS FALSIFIED: the null DOES carry a positive feature at q ~ 1.9.
#   So the only question that matters now is the one the licence ceiling turns on: is the matching
#   shape a property of the PHASE DRIFT, or a property of the banding that ANY injection would give?
#   Scanned over all 24 phases -- if every phase correlates, the match says nothing about the drift.
PH = np.linspace(0, 2 * np.pi, 24, endpoint=False)
print("\n\n  THE NULL OF THE NULL: the same correlation at all 24 phases, not only the real one")
print(f"  {'phase/2pi':>10s}", end='')
for lab in rows:
    print(f" {lab + ' corr':>18s} {lab + ' @1.9':>18s}", end='')
print()
scan = {lab: {'c': [], 'f': []} for lab in rows}
for p in PH:
    print(f"  {p / (2 * np.pi):10.3f}", end='')
    for lab, AL, AK in (('null A=0.5', 0.5, 0.5), ('null A=own', AD0, AS0)):
        nb = OC.retention_null(B, AL, AK, p)
        _, y = OC.retained_own(nb, 1.0, 7, 5.75, C=OC.retention_combs(nb))
        nd = detrend(y)
        c = float(np.corrcoef(nd, md)[0, 1])
        f = float(nd[j19] / md[j19])
        scan[lab]['c'].append(c)
        scan[lab]['f'].append(f)
        print(f" {c:+18.3f} {f:+18.3f}", end='')
    print(" <- the real phase" if p == PH[0] else "")
for lab in scan:
    c = np.array(scan[lab]['c'])
    f = np.array(scan[lab]['f'])
    print(f"\n  {lab}: correlation over the 24 phases runs {c.min():+.3f} to {c.max():+.3f}, "
          f"mean {c.mean():+.3f};  the real phase is {c[0]:+.3f}, "
          f"rank {int(np.sum(c >= c[0]))} of 24")
    print(f"    the fraction reproduced at q = 1.9 runs {f.min():+.3f} to {f.max():+.3f};  "
          f"the real phase {f[0]:+.3f}, rank {int(np.sum(f >= f[0]))} of 24")
    print(f"    phases whose correlation exceeds +0.8: {int(np.sum(c > 0.8))} of 24")
    # ⌗ counted here and not off the printed table: the shape is one mode whose SIGN flips with
    #   phase, so the count that bears on "rank 1 of 24" is the ALIGNED-OR-ANTI-ALIGNED one.
    print(f"    ...and whose |correlation| exceeds 0.8: {int(np.sum(np.abs(c) > 0.8))} of 24 "
          f"({int(np.sum(c > 0.8))} aligned, {int(np.sum(c < -0.8))} anti-aligned) "
          f"-- the family visits every alignment, and it is the SIGN that selects the real phase")
