"""r7805+cc66: would the receipt's gates have caught a wrong answer?

Each probe copies the receipt to a temp path with HERE/ROOT pinned (so it still reads the real tree),
makes ONE targeted mutation, runs it, and asserts the named gates go RED.  The expected gate set is
DERIVED from the receipt's own G_(n, ...) calls, not hardcoded -- the lesson r7803 paid for.

Run: python3 failability.py        (~15 min; the receipt re-runs the census each time)
"""
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
RCPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_po87s_list_grew_to_33_and_not_one_arrival_is_evidence_and_repointing_the_'
                    'control_to_plancks_omega_c_moves_the_0_918_to_0_957.py')
BASE = open(RCPT).read()
PIN = [("HERE = os.path.dirname(os.path.abspath(__file__))", f'HERE = {os.path.dirname(RCPT)!r}'),
       ("ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))", f'ROOT = {ROOT!r}')]
EXPECT = {int(m.group(1)) for m in re.finditer(r'^G_\((\d+),', BASE, re.M)}
assert EXPECT, 'no G_(n, ...) gate calls found'

PROBES = [
    ("the control's omega_c taken as Planck's, so there is no re-pointing left to price",
     "WC_CORPUS, WC_PLANCK = 0.3150 * HH ** 2 - WB, 0.1200",
     "WC_CORPUS, WC_PLANCK = 0.3150 * HH ** 2 - WB, 0.3150 * HH ** 2 - WB",
     {8, 9, 10, 11}),
    ("the grid's Omega_m step mis-stated as a tenth of itself, so the move is priced ten steps out",
     "STEP_OM = 0.0150\nX = (OM_PLANCK - OM_CORPUS) / STEP_OM",
     "STEP_OM = 0.0015\nX = (OM_PLANCK - OM_CORPUS) / STEP_OM",
     {8}),
    ("the LEAFGEOM spectrum's config read from the namesake twin instead, so the one-rate build is "
     "no longer identified",
     "_p = os.path.join(SP, 'r7749_leafgeom_refit_verify_cr.npz')",
     "_p = os.path.join(SP, 'cc66_r185_verify_cr_leafrec1.npz')",
     {5}),
    ("the banked LIST.md replaced by today's census output, so nothing appears to have moved",
     "_list = open(os.path.join(CEN, 'LIST.md')).read()",
     "_list = open(os.path.join(CEN, 'LIST.md')).read().replace('26 derived + 4 declared = 30', 'x')",
     {1}),
]


def run(text):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, 'probe.py')
        open(p, 'w').write(text)
        r = subprocess.run([sys.executable, p], capture_output=True, text=True, timeout=3600)
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
print(f'  CONTROL RUN (unmutated, from the temp path) -- expecting gates {sorted(EXPECT)} ------')
red, green, rc, out, err = run(pinned())
print(f'    gates green {sorted(green)}  red {sorted(red)}  rc {rc}')
if red or rc != 0 or green != EXPECT:
    bad.append(f'the unmutated receipt does not come back {len(EXPECT)}/{len(EXPECT)} green from a '
               f'temp path (rc {rc}, green {sorted(green)}, red {sorted(red)}); '
               f'stderr tail: {err.strip()[-300:]}')

for i, (name, old, new, want) in enumerate(PROBES, 1):
    t = pinned()
    if t.count(old) != 1:
        bad.append(f'probe {i} ({name}): target not unique ({t.count(old)} occurrences)')
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
      f'{len(EXPECT)}. **')
