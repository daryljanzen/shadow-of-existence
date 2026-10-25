#!/usr/bin/env python3
"""P13 sec:synthesis / P18 sec:frontier / P7 frontier:realforms -- PO-94's quantum half carries a named test, a
SELECTION test, and it is unmet in all three slots where the compact face could meet it.

The gauge half's test asks the compact face to carry the sector's own structure (a field strength and a coupling);
the quantum claim is only that the face carries the sector's scale, the structure being Lorentzian.  A test for a
structure-claim cannot score a scale-claim, so the quantum half's test is a selection test: the face is physics'
actual quantum sector rather than a structural rhyme iff its data remove a freedom of the quantum theory, with
physically distinct members, that no other principle removes.

WHAT IS CHECKED.  60's computation at r7608 (computations/beyond_the_wall/r7608_60_whether_the_quantum_half_can_
carry_a_discriminator_at_all/discriminator.py, registered before it existed in PREDICTION.md there) is run from
source; its own 55 checks must pass, and the figures the papers and register quote are pinned against its output:
  * the value slot is empty: the thermal relation adds one equation and one unknown, net constraint zero;
  * the extension slot is not distinctive: on -psi'' + gamma psi/x^2 at gamma = 1/4 (nu = 1/sqrt 2, limit circle)
    the extension family's lowest eigenvalue runs 11.776812 -> 1.335962 strictly monotone, so the members are
    physically distinct, and the form energy converges at the one regular member alone (0.41748475) and diverges
    elsewhere at the slope -2 nu (measured -1.4127 and -1.4133 against -1.414214): the member Euclidean regularity
    selects is the member finite form energy selects;
  * the ordering slot is out of the face's reach, the thermal state acting downstream of the form;
  * no paper places a quantum structure on the face (the net over the papers, every candidate adjudicated).
SCOPE.  Finite form energy is a standard requirement and not one CR derives: what is established is that the face's
selection is reachable without Euclidean input, scored as non-distinctness and not as a refutation.  The placement
of hbar's register on the face is not touched.
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
                    'r7608_60_whether_the_quantum_half_can_carry_a_discriminator_at_all', 'discriminator.py')
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


m55 = re.search(r'(\d+) checks, (\d+) failures', out)
e_hi = num(r'E_0 runs ([\d.]+) ->')
e_lo = num(r'E_0 runs [\d.]+ -> ([\d.]+)')
mono = 'strictly monotone across the family: True' in out
s06 = num(r'theta=0\.6:\s+log-log slope in eps = (-[\d.]+)')
spi = num(r'theta=pi/2:\s+log-log slope in eps = (-[\d.]+)')
fe = num(r'1e-06\s+([\d.]+)\s')
nu2 = num(r'predicted -2nu = (-[\d.]+)\)')
form = fe is not None and abs(fe - 0.41748475) < 5e-9 and nu2 is not None and abs(nu2 - (-1.414214)) < 5e-7

gate("60's computation runs from source and its own checks all pass (55 checks, 0 failures)",
     rc == 0 and m55 is not None and int(m55.group(1)) == 55 and int(m55.group(2)) == 0)
gate("the arms the verdict turns on hold: the halves are two questions (A, B), no paper places a quantum structure on "
     "the face (C), the value slot is empty (D), the extension slot is the form's (E), the ordering slot is out of "
     "reach (F)",
     all(f"⇒ Ⓧ HIT".replace('Ⓧ', a) in out for a in 'ⒶⒷⒹⒺⒻ') and 'Ⓒ HIT' in out and 'Ⓗ does not fire' in out)
gate("the extension family is physically distinct: its lowest eigenvalue runs 11.776812 -> 1.335962, strictly monotone",
     mono and e_hi is not None and abs(e_hi - 11.776812) < 5e-7 and e_lo is not None and abs(e_lo - 1.335962) < 5e-7)
gate("and the form energy converges at the regular member alone (0.41748475), diverging elsewhere at slopes "
     "-1.4127 and -1.4133 against -2 nu = -1.414214",
     form and s06 is not None and abs(s06 - (-1.4127)) < 0.0001 and spi is not None and abs(spi - (-1.4133)) < 0.0001)

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
