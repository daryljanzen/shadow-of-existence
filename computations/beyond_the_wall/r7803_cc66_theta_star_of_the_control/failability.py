"""r7803+cc66: would the receipt's gates have caught a wrong answer?

Each probe copies the receipt to a temp path with its HERE/ROOT anchors pinned (so it still reads the
real tree), makes ONE targeted mutation, runs it, and asserts the named gates go RED.  A probe that
leaves every gate green is a gate that proves nothing.

Run: python3 failability.py        (~5 min; runs the receipt six times)
"""
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_the_control_pays_the_same_theta_star_pull_at_the_distances_point_so_the_4_8_'
                    'is_the_background_and_what_the_construction_owns_is_the_16_8_between_its_two_'
                    'rate_assignments.py')
BASE = open(RCPT).read()

PIN = [("HERE = os.path.dirname(os.path.abspath(__file__))", f'HERE = {os.path.dirname(RCPT)!r}'),
       ("ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))", f'ROOT = {ROOT!r}')]

PROBES = [
    ('the radiation density in the independently written LCDM E(z) moved 3 per cent',
     'return np.sqrt(Om * (1.0 + z) ** 3 + (WR / h ** 2) * (1.0 + z) ** 4 + (1.0 - Om))',
     'return np.sqrt(Om * (1.0 + z) ** 3 + (1.03 * WR / h ** 2) * (1.0 + z) ** 4 + (1.0 - Om))',
     {1, 4}),
    ("the sound-horizon integral capped at z=1e9, so the 'infinity' limit is taken before it has "
     "converged (the convergence test still passes -- both witnesses are capped alike -- and it is "
     "the measured REACH that catches it)",
     "    span, ref = np.log(1 + z_hi) - np.log(1 + ZREC), np.log(1 + 3e7) - np.log(1 + ZREC)",
     "    z_hi = min(z_hi, 1e9)\n"
     "    span, ref = np.log(1 + z_hi) - np.log(1 + ZREC), np.log(1 + 3e7) - np.log(1 + ZREC)",
     {3}),
    ("the two rate assignments swapped, so the swing the construction owns vanishes",
     'P_DIST_STACK = pull(theta_at(*DIST, 3e7, E_stack))',
     'P_DIST_STACK = pull(theta_at(*DIST, 3e7, E_leaf))',
     {6}),
    ("z_rec moved by one, so the definition is no longer the corpus's",
     'ZREC, TOBS, TSIG = CORPUS[\'ZREC\'], CORPUS[\'THETA_OBS\'], CORPUS[\'THETA_SIG\']',
     'ZREC, TOBS, TSIG = 1091.0, CORPUS[\'THETA_OBS\'], CORPUS[\'THETA_SIG\']',
     {1, 2}),
    ("CAMB's exact theta_* given an Omega_m-DEPENDENT offset, so the bias spread and the gap "
     "between the two refit minima are both wrong (a CONSTANT offset would not mislead gate 8, "
     "which reads only differences of CAMB pulls, and gate 8 is right to be blind to it)",
     "    return camb.get_background(pars).get_derived_params()['thetastar'] / 100.0",
     "    return (camb.get_background(pars).get_derived_params()['thetastar'] / 100.0\n"
     "            + 3.1e-6 * 50.0 * (Om - 0.30))",
     {7, 8, 10}),
    ("the control's refit point read from the ARM's recipe line instead of the control's",
     "verify_lcdm\\s+ARM=lcdm LH0=([\\d.]+) LOM=([\\d.]+) WBH2=([\\d.]+) NS=([\\d.]+)",
     "verify_cr\\s+ARM=cr CRH0=([\\d.]+) CROM=([\\d.]+) ZSTART=\\S+ LEAFSCALES=1 WBH2=([\\d.]+) NS=([\\d.]+)",
     {5}),
]


def run(text):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, 'probe.py')
        open(p, 'w').write(text)
        r = subprocess.run([sys.executable, p], capture_output=True, text=True, timeout=1800)
    red = {int(m.group(1)) for m in re.finditer(r'⛔ GATE (\d+)', r.stdout)}
    green = {int(m.group(1)) for m in re.finditer(r'✅ GATE (\d+)', r.stdout)}
    return red, green, r.returncode, r.stdout, r.stderr


def pinned():
    t = BASE
    for old, new in PIN:
        assert t.count(old) == 1, f'anchor not unique: {old}'
        t = t.replace(old, new)
    return t


bad = []
# The expected gate set is DERIVED from the receipt's own G(n, ...) calls, not hardcoded -- a count
# written here goes stale the moment a gate is added, which is exactly what it did when gate 11
# arrived and this probe reported a failability problem that was its own arithmetic.
EXPECT = {int(m.group(1)) for m in re.finditer(r'^G\((\d+),', BASE, re.M)}
assert EXPECT, 'no G(n, ...) gate calls found in the receipt'
print(f'  CONTROL RUN (unmutated, from the temp path) -- expecting gates {sorted(EXPECT)} -------')
red, green, rc, out, err = run(pinned())
print(f'    gates green {sorted(green)}  red {sorted(red)}  rc {rc}')
if red or rc != 0 or green != EXPECT:
    bad.append(f'the unmutated receipt does not come back {len(EXPECT)}/{len(EXPECT)} green from a '
               f'temp path (rc {rc}, green {sorted(green)}, red {sorted(red)}); '
               f'stderr tail: {err.strip()[-300:]}')

for i, (name, old, new, want) in enumerate(PROBES, 1):
    t = pinned()
    if t.count(old) != 1:
        bad.append(f'probe {i} ({name}): its target is not unique in the receipt '
                   f'({t.count(old)} occurrences) -- the probe proves nothing')
        print(f'  ⛔ PROBE {i}  {name}: TARGET NOT UNIQUE')
        continue
    red, green, rc, out, err = run(t.replace(old, new))
    ok = want <= red
    print(f"  {'✅' if ok else '⛔'} PROBE {i}  {name}")
    print(f'      expected red {sorted(want)}; got red {sorted(red)}  (rc {rc})')
    if not ok:
        bad.append(f'probe {i} ({name}): gates {sorted(want - red)} stayed GREEN under a mutation '
                   f'that makes the answer wrong')

print()
if bad:
    print(f'  ⛔ {len(bad)} FAILABILITY PROBLEM(S):')
    for b in bad:
        print(f'     - {b}')
    raise SystemExit(1)
print(f'  ⇒ ✅ ** ALL {len(PROBES)} PROBES BITE AND THE UNMUTATED RECEIPT IS {len(EXPECT)}/'
      f'{len(EXPECT)}. **  Every gate named above fails')
print('    when the thing it asserts is made false, so none of them is decoration.')
