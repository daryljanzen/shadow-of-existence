#!/usr/bin/env python3
"""P7 frontier:realforms / P18 sec:frontier -- PO-94's quantum half: the catalogue's first entry, the state, is an atom on
the domain the corpus fixes for it.  The papers scope it to de Sitter-INVARIANT vacua (P7, the sentence carrying the
alpha-vacua result); that family has two real parameters, and what excludes a member of it is blind to one of them, so
one reading closes the whole family.  A state at another period of imaginary time is not in that family: a period
other than the face's own makes the Euclidean section a cone, which keeps four of the smooth section's ten isometry
generators.  So no entry of the standard catalogue is shown to be a label over several freedoms, and the terminal
clause does not fire for the plainer reason that the list is not yet shown complete.

WHAT IS CHECKED.  60's computation at r7628 (computations/beyond_the_wall/r7628_60_whether_the_state_entry_is_an_atom_
depends_on_which_symmetry_the_state_is_invariant_under/atomdomain.py, registered before it existed at 871af72) is run
from source; 16 checks, 0 failures.  Pinned against its output:
  * the voiding control fires: the entry's domain is located verbatim in P7 as the de Sitter-invariant vacua;
  * the invariant family is a two-parameter family of functions of the de Sitter invariant alone;
  * both exclusion criteria (the antipodal pair's magnitude e^a, the particle-content coefficient e^{2a}/(1-e^{2a}))
    have derivative identically zero in the phase, so one reading excludes every member but the limit;
  * the cone's translation Killing fields survive only at integer multiples of the face's period, solved over the
    reals; the isometry dimensions are 10 against 4 (imported: SO(5) against the rotation times SO(3)).
COMPUTES: the alpha-vacuum two-point function's parameter count and its phase derivatives; the Killing condition on
the cone at periods c = 1, 1/2, 3/4.
"""
import contextlib
import io
import os
import re
import runpy

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                 'r7628_60_whether_the_state_entry_is_an_atom_depends_on_which_symmetry_the_state_is_invariant_under')
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


buf = io.StringIO()
rc = 0
cwd = os.getcwd()
try:
    os.chdir(D)
    with contextlib.redirect_stdout(buf):
        runpy.run_path(os.path.join(D, 'atomdomain.py'), run_name='__main__')
except SystemExit as e:
    rc = e.code or 0
except AssertionError:
    rc = 1
finally:
    os.chdir(cwd)
out = buf.getvalue()

gate("60's computation runs from source: 16 checks, 0 failures", rc == 0 and '16 checks, 0 failures.' in out)
gate("the voiding control fires: the entry's domain is fixed in the papers, to the de Sitter-invariant vacua",
     'Ⓕ VOIDS' in out)
gate("the invariant family is two-parameter, every member a function of the invariant alone", 'Ⓐ HIT' in out)
gate("one phase-blind reading scores both parameters", 'Ⓑ HIT' in out)
gate("the period lies outside the domain: Killing fields survive only at integer periods; 10 against 4 generators",
     'Ⓒ HIT' in out and re.search(r'their intersection:\s+Integers', out) is not None and 'computed: 10 against 4.' in out)
gate("the controls still sort the verdicts apart", 'Ⓔ HIT' in out)

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
