#!/usr/bin/env python3
"""P13 sec:synthesis / sec:face-status -- PO-94's gauge half, the fifth and last of B59's five routes to
be examined bar one: the almost-commutative triple over the FACE, the locus r7613 left open, SUPPLIES a
gauge field and does NOT fix its coupling; and the Hilbert space the order specifies admits no real
structure at all, which is a correction to the specification rather than a closure of the route.

WHAT IS CHECKED.  cc66's computation at r7615+cc66
(computations/beyond_the_wall/r7615_cc66_the_triple_over_the_face/face.py, registered before it existed
in PREDICTION.md there) is run from source; every one of its 22 checks must pass, and the figures the row
quotes are pinned against its output:
  * the pieces the order left to "as the face's dimension allows" are READ from P13, not recalled: the
    face is odd-dimensional, being the five-sphere, and the grading exists only in even dimension -- so
    gamma does not exist, and that is the paper's own sentence and not a finding of this row;
  * on the order's own H = spinors tensor C^3 there is NO real structure, because M_3(C) acts
    IRREDUCIBLY on C^3: the commutant is ONE-dimensional, the scalars, with nowhere for J a* J^-1 to
    live, against NINE on the bimodule M_3(C) where the room exists -- a dimension solved for, not
    quoted, and the bimodule is the control that says the obstruction is the order's choice of H;
  * on the triple that repair gives, the order-one condition holds EXACTLY -- defect 0 over all 81
    generator pairs -- and it is NOT vacuous: max ||[D,a]|| = 4.33 on the same algebra, the guard
    r7613 earned, with the order's own C^3 coming back NON-zero (3.536) as the control;
  * the face is FIVE-dimensional and carries TEN independent two-forms where r7613's one-dimensional
    leaf carried ZERO -- the same counter, the same file, opposite answers -- and a generic su(3)-valued
    one-form there has non-vanishing F = dA + A^A, zero on a constant commuting control;
  * and the real test answers AGAINST the construction, as pre-registered: no power of alpha or beta
    alone is dimensionless (the exponents are forced to p_a = -p_b), so the only dimensionless monomial
    the pair admits is the ratio beta/alpha, which the construction fixes EXACTLY at 2 pi -- and a ratio
    of lengths is not a moment of a cutoff function.  The route supplies a gauge sector the construction
    does not determine.
  * The operator is certified before it is used: the face's least eigenvalue 5/(2 alpha) is DERIVED by
    saturating Friedrich's bound on S^5's own scalar curvature at k = 0, strictly exceeded at k = 1 and
    k = 2, and it is GAPPED -- which is why P13's "no Dirac zero modes" does not close this route, a
    triple needing the OPERATOR and the face having one.
COMPUTES:  at NO numeric parameter value at all -- the face's radius alpha is carried as a SYMBOL from
end to end, and the two figures that read like parameter pins (beta/alpha = 2 pi, and the control
alpha/alpha = 1) are DIMENSIONLESS RATIOS solved for rather than a radius chosen; that is the point of
question (2), so a numeric alpha would destroy the argument rather than instance it.  The parameters
that ARE fixed are discrete: the finite algebra is M_3(C) acting on C^3 and on M_3(C), the base
dimension p runs over 1, 2, 3 and 5 in the two-form counter, the spectrum index k over 0, 1 and 2, and
the order-one sweep covers all 81 generator pairs.
SCOPE.  Not a derivation of a coupling: that half is PO-5's row and is not annexed here.  Not that the
route is closed -- the opposite: it is the one route of B59's five that survives, with a field and no
coupling.  Not that B61 is weakened; its absence list wants a third set-aside now that the face is
examined, which is 69's amendment and not taken here.  B59's composite/emergent route remains the only
one of the five untouched.  The two faults cc66 caught in its own working are recorded in the WALK.
"""
import contextlib
import io
import os
import re
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
COMP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7615_cc66_the_triple_over_the_face',
                    'face.py')
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

n_pass = len(re.findall(r'^\s+\[PASS\]', out, re.M))
n_fail = len(re.findall(r'^\s+\[FAIL\]', out, re.M))


def has(*pats):
    return all(re.search(p, out) for p in pats)


gate(f"cc66's computation runs from source and every check it makes passes ({n_pass} pass, {n_fail} fail)",
     rc == 0 and n_pass == 22 and n_fail == 0 and 'ALL CHECKS PASS' in out)
gate("the pieces the order left to the face's dimension are READ from P13 and not recalled: that the "
     'face is odd-dimensional being the five-sphere, that the grading exists only in even dimension, '
     'and the spectrum the triple is built on',
     has(r'odd-dimensional\}, being the five-sphere"\s+->\s+found in boundary_paper\.tex',
         r'the grading exists only in even dimension"\s+->\s+found in boundary_paper\.tex',
         r'the least eigenvalue is \$5/2\\alpha\$"\s+->\s+found in boundary_paper\.tex'))
gate('PINNED: the commutant of M_3(C) on the order\'s own C^3 is ONE-dimensional, the scalars, against '
     'NINE on the bimodule M_3(C) -- so the order\'s H admits no real structure and the bimodule does, '
     'which places the obstruction in the choice of H and not in M_3(C) or in the solver',
     has(r'dim commutant = 1 \(scalars only\)', r'dim commutant = 9\b',
         r"commutant of M_3\(C\) on C\^3 \(the order's H\):\s+dim = 1"))
gate('PINNED: the order-one condition holds EXACTLY on the repaired triple, defect 0 over all 81 '
     'generator pairs, and the arm is NOT vacuous -- max ||[D,a]|| = 4.33 on the same algebra -- with '
     "the order's own C^3 returning 3.536 as the control that comes back the other way",
     has(r'max \|\|\[D,a\]\|\| = 4\.33\b',
         r'max \|\|\[\[D,a\],b\^o\]\|\| = 0\.00e\+00 over 81 pairs',
         r'max \|\|\[\[D,a\],b\^o\]\|\| = 3\.536\b'))
gate('PINNED: the face is five-dimensional and carries TEN independent two-forms where r7613\'s '
     'one-dimensional leaf carried ZERO, the same counter returning 1 and 3 at p = 2 and 3, and a '
     'generic su(3)-valued one-form there has non-vanishing curvature against zero on a constant '
     'commuting control',
     has(r'p=1 -> 0, p=2 -> 1, p=3 -> 3, p=5 -> 10\b', r'p=5 -> 10, p=1 -> 0 \(r7613\)',
         r'F_12 has 2 free symbol\(s\) and is not the zero matrix', r'->\s+F = 0\n'))
gate('PINNED: no power of alpha or beta alone is dimensionless -- the exponents are FORCED to '
     'p_a = -p_b -- so the only dimensionless monomial the pair admits is the ratio, which the '
     'construction fixes exactly at beta/alpha = 2 pi, and a ratio of lengths is not a moment of a '
     'cutoff function',
     has(r'p_a = -p_b forced', r'beta/alpha = 2\*pi\b',
         r'beta/alpha = 2 pi is fixed; the cutoff moment is not a ratio of lengths',
         r'alpha/alpha = 1 dimensionless, alpha is not'))
gate('the operator is certified before it is used: the least eigenvalue is DERIVED by saturating '
     "Friedrich's bound on S^5's own scalar curvature at k = 0, STRICTLY exceeded at k = 1 and k = 2, "
     'and it is gapped -- which is why P13\'s "no zero modes" sentence does not close this route',
     has(r'R = 20/alpha\*\*2', r'lambda_min = 5/\(2\*alpha\), saturates = True',
         r'k=1: 49/\(4\*alpha\*\*2\) > 25/\(4\*alpha\*\*2\)',
         r'\|lambda\| >= 5/\(2\*alpha\) > 0'))
gate('the checker is certified on a triple that IS one -- the two-point bimodule, J^2 = +1, JD = DJ, '
     'order-one defect 0 exactly and [D,a] up to 17 so that arm is not vacuous -- and the same '
     'expression is shown able to FAIL, defect 81.2 on a generic non-commutative pair',
     has(r'\|\|J\^2-1\|\| = 0\.0e\+00, \|\|JDJ\^-1-D\|\| = 0\.0e\+00, max\|\|\[D,a\]\|\| = 17, '
         r'order-one = 0\.0e\+00',
         r'defect = 81\.2\b'))
gate('and the verdict is the pre-registered outcome 2 with both halves named: the order\'s H corrected '
     'rather than the route closed, and a gauge field the construction does not couple, the coupling '
     "half left to PO-5's row",
     has(r'commutant 1 vs 9; gamma absent by P13', r'field yes, coupling no; outcome 2',
         r'THE ROUTE SUPPLIES A GAUGE SECTOR THE CONSTRUCTION DOES NOT DETERMINE'))

bad = [n for n, ok in CHECKS if not ok]
print(f'\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail')
for n in bad:
    print(f'    FAILED: {n}')
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
