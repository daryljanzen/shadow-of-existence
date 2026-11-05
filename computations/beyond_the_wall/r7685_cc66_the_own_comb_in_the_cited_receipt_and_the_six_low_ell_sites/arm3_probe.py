"""ARM (3): does `the_cross_term...` reproduce r7683's own-comb figures with ITS OWN bank choices?

r7683 read the control source as `r6911_source_lcdm_leafrec1.npz`; the cross-term receipt reads
`r6911_source_lcdm.npz`.  Every array the own-comb form consumes (S_i, k, r_s, ls, l_A, Dl) is
bit-identical between the two -- only `Dl_swap` and `xswap` differ -- so this must come out equal.
Measured rather than argued, because that is the whole of arm (3).
"""
import os, sys
import numpy as np
ROOT = '/home/user/shadow-of-existence'
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7637_70_own_comb_statistic'))
import own_comb as OC
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')

# r7683's choice (the phase-systematic receipt's) vs the cross-term receipt's choice
VARIANTS = {
    'r7683 / phase-systematic': 'r6911_source_lcdm_leafrec1.npz',
    'the_cross_term (as it reads today)': 'r6911_source_lcdm.npz',
}
PUBLISHED = dict(lowest=1.0280, highest=1.0753, slope=+0.01034, spread=0.00137,
                 icept=1.0263, icept_sd=0.0089)

def measure(lcdm_src):
    PR = {t: dict(np.load(os.path.join(SP, n))) for t, n in
          (('lcdm', 'r6915_pairs_lcdm.npz'), ('cr', 'r6915_pairs_cr_leafrec1.npz'))}
    SO = {t: dict(np.load(os.path.join(SP, n))) for t, n in
          (('lcdm', lcdm_src), ('cr', 'r6911_source_cr_leafrec1.npz'))}
    B = {t: dict(QL=PR[t]['ls'].astype(float) / float(PR[t]['l_A']),
                 QK=SO[t]['k'] * float(SO[t]['r_s']) / np.pi,
                 Dl=np.asarray(PR[t]['Dl'], float),
                 S2=np.asarray(SO[t]['S_i'], float) ** 2) for t in PR}
    C = OC.retention_combs(B)
    sl, ic, lo, hi = [], [], [], []
    for w, nb, h in OC.SETTINGS:
        x, y = OC.retained_own(B, w, nb, h, C=C)
        s, c = np.polyfit(x, y, 1)
        sl.append(s); ic.append(c); lo.append(y[0]); hi.append(y[-1])
    sl, ic, lo, hi = map(np.array, (sl, ic, lo, hi))
    shr, shrsd = OC.slope12(lambda b, w, nb, h: OC.retained_shared(b, w, nb, h), B)
    return dict(lowest=lo.mean(), highest=hi.mean(), slope=sl.mean(), spread=sl.std(),
                icept=ic.mean(), icept_sd=ic.std(), nneg=int((sl < 0).sum()),
                sigma=sl.mean() / sl.std(), shared=shr, shared_sd=shrsd,
                ic_min=ic.min(), ic_max=ic.max(), lo_min=lo.min(), hi_max=hi.max())

out = {}
for lab, src in VARIANTS.items():
    out[lab] = measure(src)
    r = out[lab]
    print(f"\n  {lab}   [control source: {src}]")
    print(f"    lowest band   {r['lowest']:.4f}        highest band  {r['highest']:.4f}")
    print(f"    slope         {r['slope']:+.5f} +- {r['spread']:.5f}   ({r['sigma']:.1f} sigma, negative in {r['nneg']})")
    print(f"    intercept     {r['icept']:.4f} +- {r['icept_sd']:.4f}   (range {r['ic_min']:.4f} to {r['ic_max']:.4f})")
    print(f"    shared slope  {r['shared']:+.5f} +- {r['shared_sd']:.5f}")

a, b = out['r7683 / phase-systematic'], out['the_cross_term (as it reads today)']
print("\n  ARM (3) -- the two bank choices against each other:")
worst = 0.0
for k in ('lowest', 'highest', 'slope', 'spread', 'icept', 'icept_sd'):
    d = abs(a[k] - b[k]); worst = max(worst, d)
    print(f"    {k:9s} r7683 {a[k]:+.6f}   cross-term {b[k]:+.6f}   |diff| {d:.3e}"
          f"   {'BIT-IDENTICAL' if a[k] == b[k] else 'DIFFERS'}")
print(f"\n    worst absolute difference over the six figures: {worst:.3e}")

print("\n  ARM (3) -- the cross-term's reading against what the paper would PRINT:")
FMT = dict(lowest='{:.3f}', highest='{:.3f}', slope='{:+.5f}', spread='{:.5f}',
           icept='{:.3f}', icept_sd='{:.3f}')
allok = True
for k, f in FMT.items():
    got, pub = f.format(b[k]), f.format(PUBLISHED[k])
    ok = got == pub
    allok &= ok
    print(f"    {k:9s} prints {got:>9s}   proposed {pub:>9s}   {'MATCH' if ok else 'MISMATCH'}")
print(f"\n    ARM (3): {'CONFIRMED -- the cited receipt can carry every printed figure' if allok else 'FALSIFIED'}")
