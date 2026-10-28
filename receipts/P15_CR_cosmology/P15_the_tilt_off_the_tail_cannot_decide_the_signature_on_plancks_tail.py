#!/usr/bin/env python3
r"""
P15_the_tilt_off_the_tail_cannot_decide_the_signature_on_plancks_tail.py

** PO-24, FIRST HALF: IS THE TILT DISPLACEMENT A TENSION?  THE OFF-TAIL CONSTRAINT IS MEASURED AND
THE TAIL-ONLY COMPARISON IS RUN.  THE QUESTION IS DECIDABLE AND NOT DECIDED ON PLANCK'S TAIL. **

This receipt READS the banked fits; it runs no likelihood.  Sources (70):
  computations/beyond_the_wall/r7471_70_PO24_tilt_off_the_tail/   fit_primary.json, fit_control.json
  computations/beyond_the_wall/r7489_70_PO24_the_decisive_fit/    w_null_*, w_sig_*, w_sky_*.json
Each fit is Planck 2018 plik_lite TT/TE/EE (only the bins inside the window), Planck 2018 lensing and
the tau prior, flat LCDM with all six parameters free (omega_b included) plus A_planck.

What it pins, each re-derived from the JSONs:
  off the tail (l <= 800): n_s = 0.9611 +/- 0.0063 (profile)
  control, full pipeline to l = 2508: 0.9636 +/- 0.0040, within 1 sigma of Planck's 0.9649 +/- 0.0042
  null mock on 1000-2508: shift 0 (the pipeline is unbiased)
  decisive window l = 1000-2508 on the sky: 0.9639 +/- 0.0158; the signature mock's shift +0.025
  the 2 sigma rule: no window separates the two predictions; the nearest is 700-1760 at 1.94
  every window sits 0.1-0.4 sigma from no shift and 1.0-1.5 sigma from the signature's
  deciding needs the decisive window's sigma at Delta/2: 1.25 times Planck's precision there on the exponent-one
  mocks (1.44 on the instrument's exponent: P15_on_the_instruments_own_exponent_...)
It also checks that P15 states the result and no longer says the question is unsupplied.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
BW = ROOT / 'computations' / 'beyond_the_wall'
OFF = BW / 'r7471_70_PO24_tilt_off_the_tail'
DEC = BW / 'r7489_70_PO24_the_decisive_fit'
TEX = (ROOT / 'corpus' / 'CR_cosmology.tex').read_text()
fails = []


def check(ok, msg):
    print(f"  {'OK  ' if ok else 'FAIL'} {msg}")
    if not ok:
        fails.append(msg)


def load(p):
    return json.loads(p.read_text())


prim = load(OFF / 'fit_primary.json')
ctrl = load(OFF / 'fit_control.json')
null = load(DEC / 'w_null_1000_2508.json')
ns0 = prim['best']['ns']                      # the mocks start from the off-tail best fit
WIN = ['700_1760', '1000_1760', '1000_2508', '1400_2508']

check(prim['lmax'] == 800 and prim['spectra'] == 'TTTEEE' and prim['lensing'],
      "off-tail fit is TT/TE/EE to l = 800 with lensing")
check(round(prim['ns_profile'], 4) == 0.9611 and round(prim['sigma_profile'], 4) == 0.0063,
      f"off-tail n_s = {prim['ns_profile']:.4f} +/- {prim['sigma_profile']:.4f}  (0.9611 +/- 0.0063)")
c, cs = ctrl['best']['ns'], ctrl['sigma_fisher']['ns']
check(round(c, 4) == 0.9636 and round(cs, 3) == 0.004 and abs(c - 0.9649) < 0.0042,
      f"control {c:.4f} +/- {cs:.3f} within 1 sigma of Planck 0.9649 +/- 0.0042")
check(abs(null['best']['ns'] - ns0) < 0.1 * null['sigma_fisher']['ns'] and null['chi2'] < 1e-6,
      "null mock on 1000-2508 returns no shift (the pipeline is unbiased)")

rows = {}
for w in WIN:
    sky, sig = load(DEC / f'w_sky_{w}.json'), load(DEC / f'w_sig_{w}.json')
    check(sky['hess_posdef'] and sig['hess_posdef'], f"{w}: Hessians positive-definite")
    n = sky.get('ns_profile') or sky['best']['ns']
    s = sky.get('sigma_profile') or sky['sigma_fisher']['ns']
    D = sig['best']['ns'] - ns0
    M = n - ns0
    rows[w] = dict(n=n, s=s, D=D, M=M, sep=abs(D) / s, from0=abs(M) / s, fromD=abs(M - D) / s)
    r = rows[w]
    print(f"      {w:>9}: n_s {n:.4f} +/- {s:.4f}   M {M:+.4f}   Delta {D:+.4f}   "
          f"|M|/s {r['from0']:.2f}   |M-D|/s {r['fromD']:.2f}   |D|/s {r['sep']:.2f}")

d = rows['1000_2508']
check(round(d['n'], 4) == 0.9639 and round(d['s'], 4) == 0.0158,
      "decisive window 1000-2508: n_s = 0.9639 +/- 0.0158")
check(round(d['D'], 3) == 0.025, "the signature mock's shift on 1000-2508 is +0.025")
check(round(d['sep'], 1) == 1.6, "on 1000-2508 the exponent-one mocks put the two predictions 1.6 sigma apart (1.38 on the instrument's exponent)")
check(all(r['sep'] < 2 for r in rows.values()), "no window separates the two predictions at 2 sigma")
near = max(rows, key=lambda w: rows[w]['sep'])
check(near == '700_1760' and round(rows[near]['sep'], 2) == 1.94, "the nearest is 700-1760 at 1.94")
check(all(0.1 <= r['from0'] <= 0.45 for r in rows.values()), "every window 0.1-0.4 sigma from no shift")
check(all(0.95 <= r['fromD'] <= 1.55 for r in rows.values()), "every window 1.0-1.5 sigma from the signature's")
need = d['s'] / (d['D'] / 2)
check(round(need, 2) == 1.25, f"deciding needs the tail {need:.2f} times as precise (1.25)")

flat = re.sub(r'\s+', ' ', TEX)
# r7627 (69): the signature's shift, the nearest separation and the precision bar P15 prints are the FAITHFUL
# exponent's (+0.022, 1.65, 1.44), pinned in P15_on_the_instruments_own_exponent_..., and the gate's state is pinned
# in P15_the_damping_tail_data_now_reach_the_bar_...; this receipt keeps the measured fits and the figures they fix.
for s in ('$0.9611\\pm0.0063$', '$0.9639\\pm0.0158$', 'decidable and not decided'):
    check(s in flat, f"P15 states {s}")
check('where the question properly sits' not in flat, "P15 no longer leaves the off-tail constraint unsupplied")
check('a separate question this paper does not settle' not in flat,
      "P15 no longer calls the tension a question it does not settle")

print(f"\n  {'all checks hold' if not fails else 'FAILED: ' + '; '.join(fails)}")
sys.exit(1 if fails else 0)
