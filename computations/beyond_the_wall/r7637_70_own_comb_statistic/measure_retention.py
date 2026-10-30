"""r7639+70: the retention statistic's own-comb form -- its gates (PREDICTION.md, r7639_70_second_bank) and its
twelve-setting slope on the old arm and the arm of record."""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own_comb as oc  # noqa: E402

SP = os.path.join(oc.ROOT, 'computations', 'beyond_the_wall', 'spectra')
FAILS = []


def check(name, ok, got=''):
    print(f"    [{'ok' if ok else 'FAIL'}]  {name}   {got}")
    if not ok:
        FAILS.append(name)


def banks(pairs_cr, src_cr, src_lcdm):
    out = {}
    for t, pn, sn in (('lcdm', 'r6915_pairs_lcdm', src_lcdm), ('cr', pairs_cr, src_cr)):
        P = np.load(os.path.join(SP, pn + '.npz'))
        S = np.load(os.path.join(SP, sn + '.npz'))
        out[t] = dict(QL=P['ls'].astype(float) / float(P['l_A']), Dl=np.asarray(P['Dl'], float),
                      QK=S['k'] * float(S['r_s']) / np.pi, S2=np.asarray(S['S_i'], float) ** 2)
    return out


SETS = {'old arm (LEAFREC=0)': banks('r6915_pairs_cr', 'r6911_source_cr', 'r6911_source_lcdm'),
        'arm of record (LEAFREC=1)': banks('r6915_pairs_cr_leafrec1', 'r6911_source_cr_leafrec1',
                                           'r6911_source_lcdm_leafrec1')}
own = lambda b, w, nb, hi, C=None: oc.retained_own(b, w, nb, hi, C)  # noqa: E731
R = {}
for lab, B in SETS.items():
    C = oc.retention_combs(B)
    sh = oc.slope12(oc.retained_shared, B)
    ow = oc.slope12(own, B, C=C)
    R[lab] = (B, C, sh, ow)
    print(f"\n  {lab}")
    print("    combs: " + ", ".join(f"{t} D_l T {C[t]['L'][0]:.4f} ph {C[t]['L'][1]:+.3f} / source T {C[t]['K'][0]:.4f} "
                                    f"ph {C[t]['K'][1]:+.3f}" for t in C))
    print(f"    shared comb: twelve-setting slope {sh[0]:+.5f} +- {sh[1]:.5f}")
    print(f"    own comb   : twelve-setting slope {ow[0]:+.5f} +- {ow[1]:.5f}")
    x, y = oc.retained_own(B, 1.0, 7, 5.75, C)
    print("    own comb, 7 bands at window 1: " + "  ".join(f"{v:.4f}" for v in y))

print("\n  Gr1 -- REPRODUCTION WHERE THE COMBS COINCIDE (each arm's comb parameters set to the control's)")
for lab, (B, C, sh, ow) in R.items():
    Cf = {'lcdm': C['lcdm'], 'cr': C['lcdm']}
    d = max(float(np.max(np.abs(oc.retained_own(B, w, nb, hi, Cf)[1] - oc.retained_shared(B, w, nb, hi)[1])))
            for w, nb, hi in oc.SETTINGS)
    check(f"Gr1 ({lab}): the own form equals cc66's `retained` on all twelve settings to 1e-12", d < 1e-12, f"{d:.1e}")
B, C, sh, ow = R['old arm (LEAFREC=0)']
check("and the shared form here IS the slope receipt's +0.01359 +- 0.00202", abs(sh[0] - 0.01359) < 5e-6
      and abs(sh[1] - 0.00202) < 5e-6, f"{sh[0]:+.5f} +- {sh[1]:.5f}")

print("\n  Gr2 -- THE NULL (both sides, identical amplitude, combs refitted inside the statistic)")
PH = np.linspace(0, 2 * np.pi, 24, endpoint=False)
for lab, (B, C, sh, ow) in R.items():
    aL = float(np.mean([oc.comb(B[t]['QL'], B[t]['Dl'])[3] for t in B]))
    aK = float(np.mean([oc.comb(B[t]['QK'], B[t]['S2'])[3] for t in B]))
    for an, (AL, AK) in (('0.5', (0.5, 0.5)), (f'own {aL:.3f}/{aK:.3f}', (aL, aK))):
        N = []
        for p in PH:
            Bn = oc.retention_null(B, AL, AK, p)
            N.append(oc.slope12(own, Bn, C=oc.retention_combs(Bn))[0])
        N = np.array(N)
        print(f"    {lab:26s} A {an:12s}: own slope {ow[0]:+.5f}; null real {N[0]:+.5f} ({N[0] / ow[0]:+.2f}), worst "
              f"{np.abs(N).max():.5f} ({np.abs(N).max() / abs(ow[0]):.2f}); slope - null(real) {ow[0] - N[0]:+.5f} "
              f"against 2 x spread {2 * ow[1]:.5f}")
        if lab.startswith('arm of record'):
            check(f"Gr2 (A {an}): the null at the real phase is under a third of the own-comb slope",
                  abs(N[0]) < abs(ow[0]) / 3, f"{N[0]:+.5f} against {ow[0]:+.5f}")

print("\n" + ("GATES: ALL PASS" if not FAILS else f"GATES: {len(FAILS)} FAILED"))
sys.exit(1 if FAILS else 0)
