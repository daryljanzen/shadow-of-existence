#!/usr/bin/env python3
"""P15 sec:diffusion-scale -- PO-24: THE DATA GATE IS OPEN ON ACT DR6.  Deciding whether the damping signature's tilt
displacement is a tension needs the tail tilt measured 1.44 times as precisely as Planck's on l = 1000-2508 (the bar
on the instrument's own exponent).  ACT DR6 clears it, and the test it allows leans against the signature without
deciding it.

WHAT IS CHECKED.  70's fits at r7625+70 (computations/beyond_the_wall/r7625_70_PO24_gate_act_spt/, registered before
any data was downloaded at 9baf92f) are read from their JSON records -- this receipt runs no likelihood.  The fitter is
r7489's: flat LCDM with all six parameters free, Planck plik_lite TT/TE/EE inside the window, Planck lensing and the
tau prior, with ACT DR6 CMB-only TT/TE/EE added through its own bandpower windows and calibration parameters.  The
signature mock multiplies every spectrum by the faithful S (l_eff 1497, r = 0.9918).  Pinned:
  * the off-tail best fit n_s = 0.96095 the mocks start from (r7471; its profile value is 0.9611), and the null mock with ACT added returning a shift of exactly 0;
  * Planck + ACT summed (an upper bound: the shared sky counted twice): n_s 0.9701 +/- 0.0087, 1.82 times Planck,
    the signature's shift +0.0275 at 3.2 sigma, the sky 1.1 sigma from no shift and 2.1 sigma from the signature;
  * ACT alone on the window (the P-ACT convention, Planck cut where ACT measures): 0.9736 +/- 0.0094, 1.67 times,
    shift +0.0269 at 2.8-2.9 sigma, the sky 1.3 sigma from no shift and 1.5 sigma from the signature;
  * both clear the 1.44 bar, and on Planck alone the same quantities are 1.00, 1.38 sigma, 0.19 and 1.20.
SCOPE.  The no-shift baseline is Planck's off-tail tilt, and ACT DR6 prefers a higher n_s than Planck across its whole
range; part of the sky's offset from the baseline is that known difference, which pushes the sky toward the
signature, so the lean against it is conservative.  A baseline from the same combination off the tail is the next
measurement and is not run here.
INHERITED.  The six-parameter flat-LCDM fit is adopted as the standard instrument for reading a tilt off a window,
not derived here; the tilt is inherited boundary data in P15, and what is compared is the shift the signature would
impose on it, which does not depend on the fit's other parameters beyond their being free.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
BW = ROOT / 'computations' / 'beyond_the_wall'
H = BW / 'r7625_70_PO24_gate_act_spt'
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def ld(p):
    return json.loads(p.read_text())


ns0 = ld(BW / 'r7471_70_PO24_tilt_off_the_tail' / 'fit_primary.json')['best']['ns']
gate(f"the mocks start from the off-tail best fit, n_s = {ns0:.5f} (0.96095; its profile value is the 0.9611 P15 quotes)",
     abs(ns0 - 0.96095) < 5e-6)
null = ld(H / 'w_sum_null_1000_2508.json')
gate("null mock with ACT added returns a shift of exactly 0", abs(null['best']['ns'] - ns0) < 1e-6 and null['chi2'] < 1e-6)

arms = {'planck': (ld(BW / 'r7489_70_PO24_the_decisive_fit' / 'w_sky_1000_2508.json'),
                   ld(BW / 'r7611_70_faithful_exponent' / 'w_sig_1000_2508.json')),
        'sum': (ld(H / 'w_sum_sky_1000_2508.json'), ld(H / 'w_sum_sig_1000_2508.json')),
        'pact': (ld(H / 'w_pact_sky_1000_2508.json'), ld(H / 'w_pact_sig_1000_2508.json'))}
R = {}
for k, (sky, sig) in arms.items():
    n = sky.get('ns_profile') or sky['best']['ns']
    s = sky.get('sigma_profile') or sky['sigma_fisher']['ns']
    D = sig['best']['ns'] - ns0
    M = n - ns0
    R[k] = dict(n=n, s=s, D=D, sep=abs(D) / s, from0=abs(M) / s, fromD=abs(M - D) / s)
    print(f"    {k:>6}: n_s {n:.4f} +/- {s:.4f}  shift {D:+.4f}  |D|/s {abs(D)/s:.2f}  |M|/s {abs(M)/s:.2f}  |M-D|/s {abs(M-D)/s:.2f}")
for k in R:
    R[k]['x'] = R['planck']['s'] / R[k]['s']

p, s_, a = R['planck'], R['sum'], R['pact']
gate("Planck alone: 0.9639 +/- 0.0158, shift +0.0218 at 1.38 sigma, sky 0.19 / 1.20",
     round(p['n'], 4) == 0.9639 and round(p['s'], 4) == 0.0158 and round(p['D'], 4) == 0.0218
     and round(p['sep'], 2) == 1.38 and round(p['from0'], 2) == 0.19 and round(p['fromD'], 2) == 1.20)
gate("Planck + ACT summed: 0.9701 +/- 0.0087, 1.82 times Planck, shift +0.0275 at 3.2 sigma, sky 1.1 / 2.1 sigma",
     round(s_['n'], 4) == 0.9701 and round(s_['s'], 4) == 0.0087 and round(s_['x'], 2) == 1.82
     and round(s_['D'], 4) == 0.0275 and round(s_['sep'], 1) == 3.2 and round(s_['from0'], 1) == 1.1
     and round(s_['fromD'], 1) == 2.1)
gate("ACT alone: 0.9736 +/- 0.0094, 1.67 times Planck, shift +0.0269 at 2.85 sigma, sky 1.3 / 1.5 sigma",
     round(a['n'], 4) == 0.9736 and round(a['s'], 4) == 0.0094 and round(a['x'], 2) == 1.67
     and round(a['D'], 4) == 0.0269 and round(a['sep'], 2) == 2.85 and round(a['from0'], 1) == 1.3
     and round(a['fromD'], 1) == 1.5)
gate("both configurations clear the 1.44 bar; Planck alone does not", s_['x'] >= 1.44 and a['x'] >= 1.44 and p['x'] < 1.44)
gate("with ACT the two predictions are separated by more than 2 sigma, and the sky decides neither at 2 sigma "
     "on the arm that does not double-count the sky",
     s_['sep'] > 2 and a['sep'] > 2 and a['from0'] < 2 and a['fromD'] < 2)

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
