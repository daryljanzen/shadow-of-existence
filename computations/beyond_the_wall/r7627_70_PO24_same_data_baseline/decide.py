"""r7627+70: PO-24's strict 2-sigma test on same-data baselines.  For each arm and window:
   M = n_s(sky, tail) - n_s(baseline), D = n_s(signature mock from that baseline) - n_s(baseline), s = sigma(sky, tail).
   Decided AGAINST the signature if |M - D| > 2 s and |M| <= 2 s; FOR it if |M| > 2 s and |M - D| <= 2 s; else undecided,
   and the precision missing is the factor by which s must shrink for the larger of the two distances to reach 2 s.
Also printed beside it, the r7625 figures on Planck's off-tail baseline (0.96095)."""
import json, pathlib
H = pathlib.Path(__file__).resolve().parent
R25 = H.parent / 'r7625_70_PO24_gate_act_spt'
def ld(p): return json.loads(pathlib.Path(p).read_text())
base = {'sum': ld(H / 'w_sum_sky_2_800.json'), 'pcut': ld(H / 'w_pcut_sky_2_800.json')}
P0 = ld(H.parent / 'r7471_70_PO24_tilt_off_the_tail' / 'fit_primary.json')['best']['ns']
print(f"  baselines on l <= 800:  Planck alone {P0:.5f}   "
      + "   ".join(f"{k} {v['best']['ns']:.5f} +/- {v['sigma_fisher']['ns']:.5f} (vs Planck {v['best']['ns'] - P0:+.5f})" for k, v in base.items()))
print(f"\n  {'arm':>5} {'window':>10} {'base':>8} {'sky':>8} {'sigma':>7} {'M':>8} {'D':>8} {'D/s':>5} {'|M|/s':>6} {'|M-D|/s':>8}  verdict")
for arm, b in (('sum', 'sum'), ('pact', 'pcut')):
    for w in ('1000_2508', '700_1760'):
        sky = ld(H / f'w_{arm}_sky_{w}.json') if (H / f'w_{arm}_sky_{w}.json').exists() else ld(R25 / f'w_{arm}_sky_{w}.json')
        sig = ld(H / f'w_{arm}_sig_{w}_on_{b}_sky_2_800.json')
        n0 = base[b]['best']['ns']
        n = sky.get('ns_profile') or sky['best']['ns']; s = sky.get('sigma_profile') or sky['sigma_fisher']['ns']
        M, D = n - n0, sig['best']['ns'] - n0
        a, c = abs(M) / s, abs(M - D) / s
        if c > 2 and a <= 2: v = 'AGAINST the signature'
        elif a > 2 and c <= 2: v = 'FOR the signature'
        else: v = f'undecided; sigma must shrink {2 / max(a, c):.2f}x for the farther prediction to reach 2 sigma'
        print(f"  {arm:>5} {w:>10} {n0:>8.5f} {n:>8.5f} {s:>7.5f} {M:>+8.5f} {D:>+8.5f} {abs(D) / s:>5.2f} {a:>6.2f} {c:>8.2f}  {v}")
