"""Chat-seat order step 3: PO-24's decisive window (l 1000-2508) with ACT DR6 added.  Reads this directory's
w_<arm>_<mode>_1000_2508.json (wfit_act.py) beside r7611's Planck-only faithful mock and r7489's Planck-only sky fit.
sigma is the profile's where the sky fit carries one, else the Fisher one (both printed)."""
import json, pathlib
H = pathlib.Path(__file__).resolve().parent
BW = H.parent
ns0 = json.loads((BW / 'r7471_70_PO24_tilt_off_the_tail' / 'fit_primary.json').read_text())['best']['ns']
def ld(p): return json.loads(p.read_text())
rows = [('Planck alone (r7489 sky, r7611 faithful mock)', ld(BW / 'r7489_70_PO24_the_decisive_fit' / 'w_sky_1000_2508.json'),
         ld(BW / 'r7611_70_faithful_exponent' / 'w_sig_1000_2508.json'))]
for arm, lab in (('sum', 'Planck + ACT DR6, summed (bound)'), ('pact', 'ACT DR6 alone (P-ACT convention)')):
    rows.append((lab, ld(H / f'w_{arm}_sky_1000_2508.json'), ld(H / f'w_{arm}_sig_1000_2508.json')))
null = H / 'w_sum_null_1000_2508.json'
if null.exists():
    n = ld(null); print(f"  null mock (Planck + ACT): shift {n['best']['ns'] - ns0:+.5f}, chi2 {n['chi2']:.2e}  (must be 0)")
print(f"  off-tail n_s0 = {ns0:.5f}; bar: sigma <= 0.0110 (1.44x Planck's 0.0158)\n")
print(f"  {'':>46} {'n_s sky':>8} {'sigma':>7} {'(Fisher)':>8} {'x Planck':>8} {'shift D':>8} {'|D|/s':>6} {'|M|/s':>6} {'|M-D|/s':>8}")
s_P = None
for lab, sky, sig in rows:
    n = sky.get('ns_profile') or sky['best']['ns']; sF = sky['sigma_fisher']['ns']; s = sky.get('sigma_profile') or sF
    s_P = s_P or s
    D = sig['best']['ns'] - ns0; M = n - ns0
    print(f"  {lab:>46} {n:>8.4f} {s:>7.4f} {sF:>8.4f} {s_P / s:>8.2f} {D:>+8.4f} {abs(D) / s:>6.2f} {abs(M) / s:>6.2f} {abs(M - D) / s:>8.2f}")
