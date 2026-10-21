#!/usr/bin/env python3
"""
P03_the_hubble_eddington_radius_tracks_the_dynamical_mass_on_virgo.py

** PO-93, ANSWERED IN DIRECTION ON ONE CLUSTER: WHICH MASS THE HUBBLE-EDDINGTON RADIUS TRACKS. **

The radius r_HE = (M alpha^2)^(1/3) is the bound on a structure's turnaround radius.  A radius set by
the baryonic mass alone is smaller by f_b^(1/3).  On Virgo -- the one system found whose turnaround
radius is located kinematically (from galaxy motions, not a fixed-overdensity definition) and whose
baryonic mass (Planck-SZ gas plus stars) is measured independently of that radius -- four independent
determinations of the turnaround radius are read against both bounds.

This receipt runs node 60's sample (computations/beyond_the_wall/r7484_60_the_sample_po93s_discharge_
clause_names/sample.py) unchanged, which imports r_HE and its constants from P03_which_mass_sets_the_
hubble_eddington_radius.py, and asserts the figures P3 prints:
  all four determinations exceed the baryon-only bound, by 19 to 33 per cent;
  all four lie inside the bound the dynamical mass allows; the bound-to-attained factor is 0.74 to 0.82;
  for the baryon-only bound to hold, the baryons inside the turnaround radius would have to be 1.70 to
  2.35 times those measured inside the smaller aperture, 33 to 56 per cent of the measured total.
Every input is a quoted literature value with its source in sample.py.  It also checks P3 states it.
"""
import pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SAMPLE = ROOT / 'computations' / 'beyond_the_wall' / 'r7484_60_the_sample_po93s_discharge_clause_names' / 'sample.py'
TEX = (ROOT / 'corpus' / 'SdS-slicing-curve_v2.tex').read_text()
fails = []


def check(ok, msg):
    print(f"  {'OK  ' if ok else 'FAIL'} {msg}")
    if not ok:
        fails.append(msg)


r = subprocess.run([sys.executable, '-I', str(SAMPLE)], capture_output=True, text=True, cwd=SAMPLE.parent)
out = r.stdout
check(r.returncode == 0, "node 60's sample runs and its own assertions hold")

m = re.search(r'(\d) OF (\d) DETERMINATIONS, BY ([0-9.]+) TO ([0-9.]+)', out)
check(bool(m) and m.group(1) == m.group(2) == '4', 'all four determinations exceed the baryon-only bound')
if m:
    lo, hi = float(m.group(3)), float(m.group(4))
    check(round((lo - 1) * 100) == 19 and round((hi - 1) * 100) == 33, f'by {lo:.2f} to {hi:.2f}: 19 to 33 per cent')
m = re.search(r'DYNAMICAL MASS ALLOWS IN (\d) OF (\d)', out)
check(bool(m) and m.group(1) == m.group(2) == '4', 'all four lie inside the dynamical-mass bound')
m = re.search(r'R0 / r_HE\(M_dyn\) = ([0-9.]+) to ([0-9.]+)', out)
check(bool(m) and abs(float(m.group(1)) - 0.74) <= 0.005 and abs(float(m.group(2)) - 0.82) <= 0.005,
      'the bound-to-attained factor is 0.74 to 0.82')
m = re.search(r'would have to be ([0-9.]+) to ([0-9.]+) times', out)
check(bool(m) and abs(float(m.group(1)) - 1.70) <= 0.005 and abs(float(m.group(2)) - 2.35) <= 0.005,
      'the baryons needed inside R0: 1.70 to 2.35 times')
m = re.search(r'That is (\d+) to (\d+) per cent of the independently measured', out)
check(bool(m) and abs(float(m.group(1)) - 33) <= 0.5 and abs(float(m.group(2)) - 56) <= 0.5, '33 to 56 per cent of the measured total')

flat = re.sub(r'\s+', ' ', TEX)
for s in ('$19$ to $33$ per cent', '$0.74$ to $0.82$', '$1.70$ to $2.35$', 'tracks the dynamical mass'):
    check(s in flat, f'P3 states {s}')
check('until the mass question is settled' not in flat, 'P3 no longer carries the mass question as unsettled')

print(f"\n  {'all checks hold' if not fails else 'FAILED: ' + '; '.join(fails)}")
sys.exit(1 if fails else 0)
