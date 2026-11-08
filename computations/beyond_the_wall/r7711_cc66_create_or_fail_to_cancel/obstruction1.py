#!/usr/bin/env python3
"""`r7711+cc66` OBSTRUCTION 1: does ANY smoothing resolve a tenth of the step in the source ratio while
leaving a low plateau to measure it against?

Registered expectation: the window closes before the resolution arrives.  Measured here as a sweep of the
half-width, reporting at every setting the low-plateau count, the pooled plateau scatter, the source
ratio's own low-to-high change, and the size a tenth of the SPECTRA's step would have in units of that
scatter.  ⛔ A setting with fewer than three low-plateau centres is reported as UNMEASURABLE rather than
given a scatter, because a standard deviation of two numbers is not a scatter.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7639_cc66_P15_repoint_paper'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7637_70_own_comb_statistic'))
import own_comb_kinds as OCK                                                 # noqa: E402

GRID, LO_Q, HI_Q, SCAN_LO, SCAN_HI = 0.05, 1.4, 2.2, 0.85, 3.0
MIN_PLATEAU = 3


def banks(kind):
    out = {}
    if kind == 'spectra':
        for t, n in (('lcdm', 'r6941_fine_lcdm'), ('cr', 'r6941_fine_cr_leafrec1')):
            d = np.load(os.path.join(SP, n + '.npz'), allow_pickle=True)
            out[t] = (d['ls'].astype(float) / float(d['l_A']), np.asarray(d['Dl'], float))
    else:
        for t, n in (('lcdm', 'r6911_source_lcdm_leafrec1'), ('cr', 'r6911_source_cr_leafrec1')):
            d = np.load(os.path.join(SP, n + '.npz'), allow_pickle=True)
            out[t] = (np.asarray(d['k'], float) * float(d['r_s']) / np.pi,
                      np.asarray(d['S_i'], float) ** 2)
    return out


def read(st, half):
    cs = np.arange(SCAN_LO + half, SCAN_HI, GRID)
    R = np.array([OCK._rms(st['ua'], st['oa'], c - half, c + half)
                  / OCK._rms(st['xc'], st['oc'], c - half, c + half) - 1.0 for c in cs])
    L, H = R[cs < LO_Q], R[cs > HI_Q]
    if len(L) < MIN_PLATEAU or len(H) < MIN_PLATEAU:
        return dict(half=float(half), n_lo=int(len(L)), n_hi=int(len(H)), measurable=False)
    sd = float(np.sqrt((L.var(ddof=1) + H.var(ddof=1)) / 2))
    return dict(half=float(half), n_lo=int(len(L)), n_hi=int(len(H)), measurable=True,
                lo=float(L.mean()), hi=float(H.mean()), step=float(H.mean() - L.mean()), sd=sd)


def main():
    SPB, SRB = banks('spectra'), banks('source')
    STS, STK = OCK.own_state(SPB, 'mean', 1.0), OCK.own_state(SRB, 'mean', 1.0)
    ref = read(STS, 0.25)
    TENTH = ref['step'] / 10.0
    print(f"\n  ⛭ `r7711` the SPECTRA's step at half=0.250 is {ref['step']:+.4f}; a tenth of it is "
          f"{TENTH:.5f}")
    print(f"      the low plateau is q < {LO_Q} and the scan starts at {SCAN_LO} + half on a "
          f"{GRID} grid, so it empties as half grows\n")
    print("      half   n_lo  n_hi     source sd    source's own step      a TENTH of the spectra's"
          "       verdict")
    rows = []
    for half in np.round(np.arange(0.175, 0.701, 0.025), 4):
        r = read(STK, half)
        rows.append(r)
        if not r['measurable']:
            print(f"      {half:.3f}  {r['n_lo']:4d}  {r['n_hi']:4d}        --             --     "
                  f"                   --                   ⛔ UNMEASURABLE "
                  f"(<{MIN_PLATEAU} plateau centres)")
            continue
        r['tenth_in_sd'] = TENTH / r['sd']
        r['own_in_sd'] = abs(r['step']) / r['sd']
        v = ('RESOLVES a tenth' if r['tenth_in_sd'] >= 3.0 else
             'marginal' if r['tenth_in_sd'] >= 2.0 else 'cannot resolve a tenth')
        print(f"      {half:.3f}  {r['n_lo']:4d}  {r['n_hi']:4d}      {r['sd']:.5f}      "
              f"{r['step']:+.4f} ({r['own_in_sd']:.2f} sd)        {TENTH:.5f} = "
              f"{r['tenth_in_sd']:5.2f} sd        {v}")
    ok = [r for r in rows if r.get('measurable') and r.get('tenth_in_sd', 0) >= 3.0]
    print()
    if ok:
        print(f"  ⛭ {len(ok)} setting(s) resolve a tenth of the step with a plateau intact: "
              + ", ".join(f"half={r['half']:.3f}" for r in ok))
    else:
        best = max((r for r in rows if r.get('measurable')), key=lambda r: r['tenth_in_sd'])
        print(f"  ⛔ NO setting resolves a tenth of the step with a plateau intact.  The best is "
              f"half={best['half']:.3f} at {best['tenth_in_sd']:.2f} sd, with {best['n_lo']} low-plateau "
              f"centres; beyond it the plateau empties before the scatter falls.")
    json.dump(dict(spectra_step=ref['step'], tenth=TENTH, rows=rows),
              open(os.path.join(HERE, 'obstruction1.json'), 'w'), indent=1)
    return 0


if __name__ == '__main__':
    sys.exit(main())
