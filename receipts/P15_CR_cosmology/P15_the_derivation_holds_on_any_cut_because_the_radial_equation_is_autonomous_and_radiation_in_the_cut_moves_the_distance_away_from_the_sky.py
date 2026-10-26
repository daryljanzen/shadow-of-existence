#!/usr/bin/env python3
"""P15 sec:scope (the acoustic coherence item) -- the derivation that puts the projection's distance on the
stacking rate holds on any cut, bent or straight, because at E = 1 the radial equation is autonomous in r;
and putting radiation into the cut as the bend P8 and P15 describe moves the distance away from the sky's
preference, not toward it.

WHAT IS CHECKED.  60's computation at r7614 (computations/beyond_the_wall/r7614_60_the_proper_frame_derivation_
on_a_cut_the_radiation_bends/bentcut.py, registered before it existed in PREDICTION.md there) is run from
source; its arms are read and the figures P15 quotes are pinned against its output:
  * the bend is the papers' own: f = 1 - 2m(r)/r - Lambda r^2/3 with m(r) a mass function, rho = m'/4 pi r^2
    (P8), radiation a bend of the cut (P15);
  * at E = 1 the radial equation dr/dtau = r H(r)/c depends on r alone, so its solutions are translates:
    two integrations from different radii agree after a shift to under 1e-10, and d_chi r = d_tau r
    exactly -- the unit cosmic-time rate survives the bend;
  * the bend's rate is H^2 = H_0^2 [Omega_m (1+z)^3 + Omega_Lambda - 3 Omega_r z (1+z)^3], the registered
    closed form, matched by quadrature to 2e-15; its radiation term is -3z/(1+z) times the leaf's
    (-2.997250 at z = 1089.9), and it vanishes at z = 1123.760571;
  * the length along the photon family on that cut is 14397.425 Mpc, +2.75 % on the stacking distance
    (14011.456) and +3.27 % on the leaf distance (13941.629): longer, on the far side of both;
  * with the rate normalised at the present the anchor of the mass function moves nothing (the same
    14397.424755 Mpc at three anchors), and the registered arm F that treated the anchor as free is a MISS
    asserted to stay one;
  * the control: with m' = 0 the machinery returns 14011.456369 Mpc, the stacking distance, exactly.
SCOPE.  The bend is radiation as a radial profile rho_r(r_0/r)^4 on the cut, the papers' description; no
likelihood is run on the bent distance.
"""
import contextlib
import io
import os
import re
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
COMP = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7614_60_the_proper_frame_derivation_on_a_cut_the_radiation_bends', 'bentcut.py')
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


buf = io.StringIO()
rc = 0
cwd = os.getcwd()
try:
    os.chdir(os.path.dirname(COMP))
    with contextlib.redirect_stdout(buf):
        runpy.run_path(COMP, run_name='__main__')
except (AssertionError, SystemExit) as e:
    rc = 1 if not isinstance(e, SystemExit) else (e.code or 0)
finally:
    os.chdir(cwd)
out = buf.getvalue()


def num(pat):
    m = re.search(pat, out)
    return float(m.group(1)) if m else None


arm = {a: v for a, v in re.findall(r'^\s+([A-H]): (HIT|MISS)\s*$', out, re.M)}
tr = num(r'worst translate mismatch ([\d.e+-]+)')
dv = num(r'worst derivative mismatch ([\d.e+-]+)')
cf = num(r'Ⓓ HIT: worst relative difference ([\d.e+-]+)')
rr = num(r'1089\.9\s+[\d.]+\s+[\d.]+\s+[\d.e+-]+\s+(-[\d.]+)')
_zm = re.search(r'^\s+(\d+\.\d)\s+\d+\.\d+\s+\d+\.\d+\s+[\d.e+-]+\s+-2\.99725', out, re.M)
zr = float(_zm.group(1)) if _zm else None
z0 = num(r'real zero of H\^2_bent: z = ([\d.]+)')
db = num(r'on the bent cut = int c dz / H_bent = ([\d.]+) Mpc')
ps = num(r'against the stacking distance\s+[\d.]+ Mpc\s+\(\+([\d.]+) %\)')
pl = num(r'against the leaf distance\s+[\d.]+ Mpc\s+\(\+([\d.]+) %\)')
anchors = [float(x) for x in re.findall(r'H\(0\) = 68\.600000, D = ([\d.]+) Mpc', out)]
ctl = num(r'with the bend switched off, the same machinery returns ([\d.]+) Mpc')

gate("60's computation runs from source; arms A-E, G, H HIT and the registered F a MISS, asserted to stay one",
     rc == 0 and all(arm.get(a) == 'HIT' for a in 'ABCDEGH') and arm.get('F') == 'MISS'
     and "Ⓕ′ HIT" in out and '16 checks, 1 failures' in out)
gate("the bend is the papers' own: m(r) a mass function, the bend m' != 0, rho = m'/4 pi r^2 (P8), radiation a "
     "bend of the cut (P15)", 'Ⓐ HIT' in out and out.count('[HIT ] P') == 4)
gate("the unit cosmic-time rate survives: translates agree to under 1e-10 and d_chi r = d_tau r exactly",
     tr is not None and tr < 1e-10 and dv is not None and dv == 0.0)
gate("the bend's rate is the registered closed form to 2e-15, its radiation term -2.997250 times the leaf's at "
     "z = 1089.9, and it vanishes at z = 1123.760571",
     cf is not None and cf < 1e-14 and rr is not None and abs(rr + 2.997250) < 5e-7 and zr is not None and abs(zr - 1089.9) < 1e-9
     and z0 is not None and abs(z0 - 1123.760571) < 5e-7)
gate("the length on the bent cut is 14397.425 Mpc, +2.75 % on the stacking distance and +3.27 % on the leaf "
     "distance", db is not None and abs(db - 14397.425) < 0.001 and ps is not None and abs(ps - 2.75) < 0.005
     and pl is not None and abs(pl - 3.27) < 0.005)
gate("with the rate normalised at the present, three anchors give the same 14397.424755 Mpc",
     len(anchors) == 3 and all(abs(a - 14397.424755) < 1e-6 for a in anchors))
gate("and the control: with m' = 0 the machinery returns the stacking distance, 14011.456369 Mpc",
     ctl is not None and abs(ctl - 14011.456369) < 1e-6)

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
