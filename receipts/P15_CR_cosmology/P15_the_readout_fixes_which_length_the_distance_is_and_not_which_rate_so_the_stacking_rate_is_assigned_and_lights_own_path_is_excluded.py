#!/usr/bin/env python3
"""P15 sec:refit-bound -- the observer's-readout identification fixes WHICH LENGTH the projection's comoving
distance is and not WHICH RATE it is built on, so the stacking rate is assigned rather than forced; and
light's own integrated path, a third object, is excluded by the acoustic comb.

WHAT IS CHECKED.  60's computation at r7580 (computations/beyond_the_wall/r7580_60_whether_the_observers_
readout_identification_forces_the_stacking_rate_distance/lightpath.py, registered before it was run in
PREDICTION.md there) is run from source and its arms are read, with the figures P15 and the receipt index
quote pinned against its own output:
  * the chart, calibrated: min over r of (d_chi r)^2 is exactly 1, at exactly the merged Nariai radius
    alpha/sqrt3; the implementation's rate is the layer-time rate, so its distance is the layer-time
    light-travel integral (14011.456 Mpc both ways);
  * the flatness half of the identification is rate-neutral: D_M = chi at Omega_k = 0 holds for a distance
    built on either rate, and fails at Omega_k = +-0.01;
  * the three-metric half carries no rate: every constant-tau slice, reparameterised by r, is one fixed flat
    R^3, so the stack carries no expansion of its own metric;
  * the rate rule's two slots do not cover light's path: the criterion that puts the optical depth on the
    stacking rate, photon-path observable, is absent where the rule is stated and present where it is used;
  * light's own integrated path, the proper length read in each fundamental observer's own frame, is
    8787 Mpc against the implementation's 14011 (ratio 0.627), and puts the acoustic scale at 190 against
    the sky's 298.4, so the comb excludes it; the leaf-rate distance is 13942 Mpc, acoustic scale 301.4.
The registered arm Hb (that the identification equates objects from the rule's two slots) is the one
60 withdrew; it is asserted here to stay withdrawn, and its corrected form to hold.

SCOPE.  Not a refutation of the stacking-rate assignment: what is established is that the identification
does not force it.  No likelihood is run.
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
                    'r7580_60_whether_the_observers_readout_identification_forces_the_stacking_rate_distance',
                    'lightpath.py')

CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    ns = runpy.run_path(COMP, run_name='__main__')
out = buf.getvalue()
A = ns['ARMS']
print(f"  arms read from the computation: {A}")


def num(pat):
    m = re.search(pat, out)
    return float(m.group(1)) if m else None


D_stack = num(r"the implementation's distance\s+D_C\^stack\s*=\s*([\d.]+)")
D_path = num(r"light's real integrated path\s+D_path\s*=\s*([\d.]+)")
D_leaf = num(r"the leaf-rate distance\s+D_C\^leaf\s*=\s*([\d.]+)")
ratio = num(r"ratio D_path / D_C\^stack\s*=\s*([\d.]+)")
lA_path = num(r"light's real integrated path\s+D =\s*[\d.]+ Mpc\s+l_A =\s*([\d.]+)")
lA_leaf = num(r"the leaf-rate distance the fit prefers\s+D =\s*[\d.]+ Mpc\s+l_A =\s*([\d.]+)")
rN = num(r"attained at r = ([\d.]+) Mpc")
sky = num(r"vs the sky's ([\d.]+):")

gate("the chart calibrated: min (d_chi r)^2 is exactly 1 at exactly alpha/sqrt3 = 3009.892488 Mpc, and the "
     "implementation's distance is the layer-time light-travel integral, 14011.456 Mpc",
     A.get('Ⓐ') == 'HIT' and A.get('Ⓑ') == 'HIT' and A.get('Ⓒ') == 'HIT'
     and rN is not None and abs(rN - 3009.892488) < 1e-6
     and D_stack is not None and abs(D_stack - 14011.456) < 0.001)
gate("the identification's flatness half is rate-neutral (D_M = chi at Omega_k = 0 for every candidate rate)",
     A.get('Ⓖ') == 'HIT')
gate("and its three-metric half carries no rate: every constant-tau slice is one fixed flat R^3", A.get('Ⓘ') == 'HIT')
gate("the rate rule's two slots do not cover light's path (the corrected arm Hb'), the registered form Hb "
     "staying withdrawn", A.get('Ⓗ′') == 'HIT' and A.get('Ⓗ') == 'MISS')
gate("light's own integrated path is 8787 Mpc against 14011 (ratio 0.627) and is not the leaf-rate distance, "
     "13942 Mpc",
     A.get('Ⓓ') == 'HIT' and A.get('Ⓔ') == 'HIT'
     and D_path is not None and abs(D_path - 8787.241) < 0.001
     and ratio is not None and abs(ratio - 0.627147) < 1e-6
     and D_leaf is not None and abs(D_leaf - 13941.629) < 0.001)
gate("and the comb excludes it: acoustic scale 189.94 against the sky's 298.4, where the leaf-rate distance "
     "gives 301.36",
     A.get('Ⓕ') == 'HIT' and lA_path is not None and abs(lA_path - 189.94) < 0.005
     and sky is not None and abs(sky - 298.4) < 0.05
     and lA_leaf is not None and abs(lA_leaf - 301.36) < 0.005)

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
