#!/usr/bin/env python3
"""P15 sec:scope (the acoustic coherence item) -- the rate the projection's comoving distance is built on is
derived by the reassignment: the photon family crosses the leaves at unit cosmic-time rate, so a length
accumulated along it is a comoving separation read across leaves, the rate rule's first slot.

WHAT IS CHECKED.  60's computation at r7612 (computations/beyond_the_wall/r7612_60_whether_the_reassignment_
itself_fixes_the_rate_a_photon_path_distance_accumulates_at/photonfamily.py, registered before it existed in
PREDICTION.md there) is run from source; its own 13 checks must pass and the figures P15 quotes are pinned
against its output:
  * the reassignment sends the photon bundle to the constant-tau family, read off P15 sec:properframe (the
    control, which would put it on the constant-chi family, does not fire);
  * that family is spacelike in the proper frame -- (d_chi r)^2 >= 1 on the whole branch -- so it is not that
    frame's light cone and not r7580's proper-frame null ray;
  * it crosses the leaves advancing cosmic time at exactly the rate the matter congruence advances along
    them, both identically 1 (step (v)), with d_chi r = d_tau r to the difference's own truncation floor;
  * the accumulation along it, r_0 int dtilde tau / r, is the implementation's D_C, 14011.456 Mpc, to a part
    in 1e14; the separation read on a single leaf is r_0 z/(1+z) = 5046.857 Mpc, 0.360 of it.
SCOPE.  The derivation is carried on the construction's chart, the vacuum one (eq:scalefac), on which radiation
is a bend of the cut and no part of the rate.  Whether it holds on the cut as radiation bends it is not tested
here.  No likelihood is run; the sky's preference for the leaf-rate distance is not moved.
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
                    'r7612_60_whether_the_reassignment_itself_fixes_the_rate_a_photon_path_distance_accumulates_at',
                    'photonfamily.py')
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


m13 = re.search(r'(\d+) checks, (\d+) failures', out)
d_fam = num(r'r_0 \* int dtilde tau / r\s+over the photon family\'s crossing = ([\d.]+) Mpc')
d_imp = num(r"int c dz / H_stack, the implementation's own distance\s+= ([\d.]+) Mpc")
rel = num(r'relative difference = ([\d.e+-]+)')
leaf = num(r'r_0 z/\(1\+z\)\s+= ([\d.]+) Mpc')
ratio = num(r"ratio to the implementation's D_C\s+= ([\d.]+)")
worst = num(r'worst \|d_chi r / d_tau r - 1\| = ([\d.e+-]+)')
slopes = [float(x) for x in re.findall(r'g_chi chi = \(d_chi r\)\^2 =\s+([\d.]+)', out)]

gate("60's computation runs from source and its own checks all pass (13 checks, 0 failures)",
     rc == 0 and m13 is not None and int(m13.group(1)) == 13 and int(m13.group(2)) == 0)
gate("the photon bundle's image is the constant-tau family, read off P15 (the control does not fire), and every "
     "registered arm A-G holds",
     'H (control): does not fire' in out and all(f'{a}: HIT' in out for a in 'ABCDEFG'))
gate("that family is spacelike in the proper frame: (d_chi r)^2 >= 1 at every sampled redshift",
     len(slopes) == 5 and min(slopes) >= 1.0)
gate("it crosses the leaves at unit cosmic-time rate, as the matter congruence advances along them: "
     "d(tilde tau)/d chi = d(tilde tau)/d tau = 1, and d_chi r = d_tau r to under 1e-9",
     'd(tilde tau)/d chi = 1, d(tilde tau)/d tau = 1' in out and worst is not None and worst < 1e-9)
gate("the accumulation along it is the implementation's D_C, 14011.456 Mpc, to a part in 1e14",
     d_fam is not None and abs(d_fam - 14011.456) < 0.001 and d_imp is not None and abs(d_imp - 14011.456) < 0.001
     and rel is not None and rel < 1e-13)
gate("and the separation read on one leaf is r_0 z/(1+z) = 5046.857 Mpc, 0.360 of it",
     leaf is not None and abs(leaf - 5046.857) < 0.001 and ratio is not None and abs(ratio - 0.360) < 0.0005)

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
