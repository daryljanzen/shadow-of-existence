#!/usr/bin/env python3
"""P15 sec:diffusion-scale -- the damping signature's two routes reconciled, and its magnitude on the faithful one.

Imposing the diffusion-length ratio on the measured spectrum as exp[-(DAMPX-1)(l/l_D)^2] applies the damping
exponent once; inside the instrument's own source the ratio damps the photon amplitude, so the power sees it
through a square and the Doppler term through a derivative.  The instrument's banked DAMPX pairs measure the
effective exponent directly.

WHAT IS CHECKED.  70's measurement at r7577+70 (computations/beyond_the_wall/r7577_70_PO24_the_factor_of_three/
measure.py, registered before it was run in PREDICTION.md there) is run from source, on banked spectra and the
existing plik_lite TT likelihood only, and its printed figures are pinned:
  * the effective exponent from the r7099 pair is 1.70 (1.82 over l = 500-1200, 1.37 over 1200-2000), and the
    r4494 pair returns the same to 1.004, so ln R is linear in DAMPX - 1 across two configurations;
  * at DAMPX = 1.174 the imposed route as built gives 0.295 chi^2/bin over l = 100-1760, against the source
    route's 0.92; imposed with the measured exponent it gives 0.779, the factor of three closing to 1.18;
  * on the faithful exponent, at the adjudicated ratio r = 0.9918 over l = 100-1760, the signature costs 1.48 in
    chi^2 over 171 bins, 0.0087 per bin, with a tilt of +0.0059 +/- 0.0033.
COMPUTES: the effective damping exponent from two banked DAMPX pairs (1.000 against 1.174, and 1.000 against
1.157), the imposed route's chi^2 per bin at DAMPX 1.174 with exponent 1 and with the measured exponent, and the
magnitude at the one adjudicated ratio r = 0.9918 on three windows.  The ratio is the configuration P15 adjudicates;
the figures are claimed at it and at no other.
SCOPE.  The metric is plik_lite TT with amplitude and tilt free; the shape residual is an upper bound and the tilt
shift is not a bound.  The linear scaling of ln R from DAMPX = 1.174 to 0.984 rests on the two configurations.
"""
import contextlib
import io
import os
import re
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
COMP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7577_70_PO24_the_factor_of_three', 'measure.py')
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    runpy.run_path(COMP, run_name='__main__')
out = buf.getvalue()
print(out)


def num(pat, k=1):
    m = re.search(pat, out)
    return float(m.group(k)) if m else None


a7 = num(r"T1\s+alpha \(r7099 pair, l 500-2000\) = ([\d.]+)")
rat = num(r"T3\s+alpha \(r4494 pair\)\s*= [\d.]+\s+ratio ([\d.]+)")
a_lo = num(r"alpha over 500-1200: ([\d.]+)")
a_hi = num(r"alpha over 1200-2000: ([\d.]+)")
A1 = num(r"A as built \(alpha=1\)\s+100-1760: ([\d.]+) chi2/bin")
Am = num(r"A, alpha measured \(1\.70\)\s+100-1760: ([\d.]+) chi2/bin")
r_adj = num(r"MAGNITUDE at r = ([\d.]+)")
fac = num(r"DAMPX ([\d.]+) \(B, reproduce")
mag = re.search(r"100-1760: ([\d.]+) chi2/bin \(total ([\d.]+) over (\d+)\)\s+dn ([+-][\d.]+) \+/- ([\d.]+)", out)

gate("the instrument's effective damping exponent is 1.70 (1.82 over l 500-1200, 1.37 over 1200-2000), and a "
     "second banked pair returns it to 1.004",
     a7 is not None and abs(a7 - 1.700) < 0.0005 and a_lo is not None and abs(a_lo - 1.824) < 0.0005
     and a_hi is not None and abs(a_hi - 1.372) < 0.0005 and rat is not None and abs(rat - 1.004) < 0.0005)
gate("the imposed route as built gives 0.295 chi^2/bin at DAMPX 1.174 over l 100-1760, and 0.779 with the measured "
     "exponent, against the source route's 0.92: the factor of three closes to 1.18",
     A1 is not None and abs(A1 - 0.295) < 0.0005 and Am is not None and abs(Am - 0.779) < 0.0005
     and abs(0.92 / Am - 1.18) < 0.005)
gate("the configurations are the ones P15 names: the adjudicated ratio r = 0.9918 and the comparison at DAMPX 1.174",
     r_adj is not None and abs(r_adj - 0.9918) < 0.00005 and fac is not None and abs(fac - 1.174) < 0.0005)
gate("on the faithful exponent at r = 0.9918 over l 100-1760: 1.48 in chi^2 over 171 bins, 0.0087 per bin, and a "
     "tilt of +0.0059 +/- 0.0033",
     mag is not None and abs(float(mag.group(1)) - 0.0087) < 0.00005 and abs(float(mag.group(2)) - 1.48) < 0.005
     and int(mag.group(3)) == 171 and abs(float(mag.group(4)) - 0.0059) < 0.00005
     and abs(float(mag.group(5)) - 0.0033) < 0.00005)

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
