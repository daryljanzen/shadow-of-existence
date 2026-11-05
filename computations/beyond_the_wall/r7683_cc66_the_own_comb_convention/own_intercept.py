"""The own-comb intercept, its spread and the endpoint range -- nothing has measured these."""
import os, sys
import numpy as np
ROOT = '/home/user/shadow-of-existence'
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7637_70_own_comb_statistic'))
import own_comb as OC
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
PR0 = {t: dict(np.load(os.path.join(SP, n))) for t, n in
       (('lcdm', 'r6915_pairs_lcdm.npz'), ('cr', 'r6915_pairs_cr_leafrec1.npz'))}
SO0 = {t: dict(np.load(os.path.join(SP, n))) for t, n in
       (('lcdm', 'r6911_source_lcdm_leafrec1.npz'), ('cr', 'r6911_source_cr_leafrec1.npz'))}
B = {t: dict(QL=PR0[t]['ls'].astype(float) / float(PR0[t]['l_A']),
             QK=SO0[t]['k'] * float(SO0[t]['r_s']) / np.pi,
             Dl=np.asarray(PR0[t]['Dl'], float),
             S2=np.asarray(SO0[t]['S_i'], float) ** 2) for t in PR0}
C = OC.retention_combs(B)

def fits(fn, **kw):
    sl, ic, lo, hi = [], [], [], []
    for w, nb, h in OC.SETTINGS:
        x, y = fn(B, w, nb, h, **kw)
        s, c = np.polyfit(x, y, 1)
        sl.append(s); ic.append(c); lo.append(y[0]); hi.append(y[-1])
    return map(np.array, (sl, ic, lo, hi))

for lab, fn, kw in (('OWN comb', OC.retained_own, dict(C=C)),
                    ('SHARED comb', OC.retained_shared, {})):
    sl, ic, lo, hi = fits(fn, **kw)
    print(f"\n  {lab}, over {len(sl)} settings:")
    print(f"    slope      {sl.mean():+.5f} +- {sl.std():.5f}   (range {sl.min():+.5f} to {sl.max():+.5f})"
          f"   {sl.mean()/sl.std():.1f} sigma   negative in {int((sl<0).sum())}")
    print(f"    intercept  {ic.mean():.4f} +- {ic.std():.4f}    (range {ic.min():.4f} to {ic.max():.4f})"
          f"   straddles one: {bool(ic.min() < 1.0 < ic.max())}")
    print(f"    lowest band  {lo.mean():.4f}  (range {lo.min():.4f} to {lo.max():.4f})")
    print(f"    highest band {hi.mean():.4f}  (range {hi.min():.4f} to {hi.max():.4f})")
    print(f"    endpoint span at the 7-band window-1 setting: ", end='')
    x, y = fn(B, 1.0, 7, 5.75, **kw)
    print(" ".join(f"{v:.4f}" for v in y))

# the over-phase null on the own comb, and the real-phase one
print("\n  THE OWN-COMB NULL over 24 phases, both amplitudes:")
CPD = {t: OC.comb(B[t]['QL'], B[t]['Dl']) for t in B}
CPK = {t: OC.comb(B[t]['QK'], B[t]['S2']) for t in B}
AD = float(np.mean([CPD[t][3] for t in CPD])); AK = float(np.mean([CPK[t][3] for t in CPK]))
own12, ownsd = OC.slope12(OC.retained_own, B, C=C)
PH = np.linspace(0, 2 * np.pi, 24, endpoint=False)
for nm, aL, aK in (('pre-registered 0.5', 0.5, 0.5), (f"banks' own {AD:.3f}/{AK:.3f}", AD, AK)):
    ns = np.array([OC.slope12(OC.retained_own, OC.retention_null(B, aL, aK, p))[0] for p in PH])
    print(f"    {nm:28s} real {ns[0]:+.5f} ({100*ns[0]/own12:.0f}% of the slope)"
          f"  worst {np.abs(ns).max():+.5f} ({np.abs(ns).max()/own12:.2f} of it)"
          f"  survives at {own12-ns[0]:+.5f}")
print(f"    own-comb slope {own12:+.5f} +- {ownsd:.5f}")
