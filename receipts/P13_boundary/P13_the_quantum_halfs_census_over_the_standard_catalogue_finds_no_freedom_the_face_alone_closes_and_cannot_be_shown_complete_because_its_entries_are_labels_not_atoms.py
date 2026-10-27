#!/usr/bin/env python3
"""P7 frontier:realforms / P18 sec:frontier -- PO-94's quantum half, the terminal clause as a census: over the
standard catalogue of freedoms for a field on a fixed background, no entry is closed by the compact face alone,
and the census cannot be shown complete because the catalogue's entries are labels and not independent freedoms.

WHAT IS CHECKED.  60's computation at r7620 (computations/beyond_the_wall/r7620_60_the_quantum_halfs_terminal_
clause_as_a_census_over_the_standard_catalogue/census.py, registered before it existed in PREDICTION.md there) is
run from source, and the figures the papers quote are pinned against its output:
  * the face is the papers' own S^5 = SO(6)/SO(5), and the catalogue ranges over it (the voiding control does not
    void);
  * the eight entries return six verdicts: the state, the self-adjoint extension and the value of the scale EMPTY;
    the operator ordering UNREACHABLE; inequivalent representations DERIVATIVE on the state; the spin structure
    NOT A FREEDOM; the vacuum angle NOT AVAILABLE; the renormalisation ambiguities CLOSED BY NOTHING;
  * no entry is closed only by the face (3 closed elsewhere, 5 the face could not close, 0 closed only by it);
  * the spin structure counted from the cellular cochain complex: 1 on S^5 and on S^4, with seeds 2 (RP^5) and
    0 (RP^4, non-orientable);
  * the Gauss-Bonnet variation zero in four dimensions and not in five; on a = e^{Ht} the three quadratic
    invariants vanish identically and the two survivors (the volume term and the Einstein term) are proportional,
    so there the ambiguities collapse onto the scale;
  * the period of imaginary time: the smooth period 2*pi*alpha, the conical deficit 2*pi - beta/alpha vanishing
    only there -- a freedom the face closes and the Hadamard condition closes too, and one that lives inside the
    first entry, which is therefore not an atom;
  * the one failure is 60's registered negative (the curvature coupling, out of the order's domain), asserted to
    stay a MISS.
SCOPE.  The terminal clause does not fire: its verdict stands as a reading, and what it lacks is the standing of a
demonstration.  The placement of hbar's register on the face is not touched.
"""
import contextlib
import io
import os
import re
import runpy

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
COMP = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7620_60_the_quantum_halfs_terminal_clause_as_a_census_over_the_standard_catalogue',
                    'census.py')
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

gate("60's census runs from source: 25 checks, the one failure being its registered negative, asserted to stay a MISS",
     '25 checks, 1 failures.' in out
     and 'FAILED: Ⓕ as registered: the dimensionless coupling is a counterexample to completeness' in out
     and 'Ⓕ MISS on the registered negative' in out)
gate("the face is the papers' own S^5 and the catalogue ranges over it",
     'Ⓐ HIT' in out and 'Ⓘ does not void' in out and 'Ⓗ HIT' in out)
verdicts = dict(re.findall(r'^   (the state|the self-adjoint extension|the operator ordering|the value of the scale'
                           r'|inequivalent representations, i\.e\. superselection|the spin structure on the face'
                           r'|the vacuum angle, if there is one|the renormalisation ambiguities of the stress tensor)'
                           r'\s+([A-Z-]+)\s', out, re.M))
want = {'the state': 'EMPTY', 'the self-adjoint extension': 'EMPTY', 'the operator ordering': 'UNREACHABLE',
        'the value of the scale': 'EMPTY', 'inequivalent representations, i.e. superselection': 'DERIVATIVE',
        'the spin structure on the face': 'NOT-A-FREEDOM', 'the vacuum angle, if there is one': 'NOT-AVAILABLE',
        'the renormalisation ambiguities of the stress tensor': 'CLOSED-BY-NOTHING'}
gate("the eight entries return the six verdicts the papers state", verdicts == want)
gate("no entry is closed only by the face: 3 closed elsewhere, 5 the face could not close, 0 closed only by it",
     re.search(r'closed elsewhere : 3\b', out) is not None and re.search(r'could NOT close\s+: 5\b', out) is not None
     and re.search(r'closed ONLY by the face\s+: 0\b', out) is not None and 'THE TERMINAL CLAUSE DOES NOT FIRE' in out)
gate("the spin structure: 1 on S^5 and on S^4, seeds 2 and 0",
     re.search(r'S\^5\s+\(the face\)\s+0\s+True\s+1\b', out) is not None
     and re.search(r'S\^4\s+\(the other candidate\)\s+0\s+True\s+1\b', out) is not None
     and re.search(r'RP\^5 .*\s1\s+True\s+2\b', out) is not None and re.search(r'RP\^4 .*\s1\s+False\s+0\b', out) is not None)
gate("Gauss-Bonnet zero in 4d and not in 5d; on de Sitter the quadratic invariants vanish and the survivors are proportional",
     'in 4d: (0, 0)' in out and 'in 5d: nonzero = True' in out
     and 'all identically zero = True' in out and 'and they are mutually proportional: True' in out)
gate("the period of imaginary time: smooth at 2*pi*alpha only, and the first entry is not an atom",
     'beta_H = 2*pi*alpha' in out and 'delta = 0 only there: [2*pi*alpha]' in out and 'ENTRY 1 IS NOT AN ATOM' in out)

bad = [n for n, ok in CHECKS if not ok]
print(f"\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail")
for n in bad:
    print(f"    FAILED: {n}")
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
