#!/usr/bin/env python3
"""P13 sec:synthesis / sec:face-status -- PO-94's gauge half: the construction's own thermal trace is
NOT a spectral action of the r7615 face triple, because the thermal weight's generator is not a
FUNCTION of the face's Dirac operator -- and it fails on the FAVOURABLE reading, where the generator
lives on the face itself.  But the construction does supply the spectral action's SCALE, which the
r7615 row's dimensional argument never reached.

WHAT IS CHECKED.  cc66's computation at r7619+cc66
(computations/beyond_the_wall/r7619_cc66_whether_the_thermal_trace_is_the_spectral_action/thermal.py,
registered before it existed in PREDICTION.md there) is run from source; every one of its 19 checks
must pass, and the figures the row quotes are pinned against its output:
  * the thermal datum is READ from the papers, not recalled: P13 says beta = 2 pi alpha is a Euclidean
    continuation of that period and that the Euclidean section is the SAME face -- which is what makes
    the order non-trivial, the thermal circle being a great circle of the very manifold D lives on --
    and CR_framework gives the construction's own generator as the deparametrized true Hamiltonian on
    COSMIC TIME;
  * the trap is real and measured rather than talked past: D COMMUTES with the great-circle generator
    EXACTLY, and a reading that stops there concludes the coupling is fixed;
  * but commuting is not being a function of.  A function of D is constant on every D-eigenspace, and
    on the face's lowest one -- FOUR-dimensional, a number the multiplicity formula and the Spin(6)
    chirality split agree on independently -- the generator takes TWO values, +-1/2;
  * and in the construction's own number: with beta/alpha = 2 pi EXACTLY the thermal weight takes the
    values e^-pi and e^+pi on that single D-eigenspace, a ratio of e^(2 pi) = 535.49, where any
    f(D/Lambda) is constant by construction;
  * the scale IS supplied: Lambda is an inverse length, not a dimensionless number, and the same
    exponent solve r7615 ran returns beta^-1 = 1/(2 pi alpha) for it -- so what the spectral action
    lacks here is f alone;
  * and f is what a coupling needs: the Yang-Mills order moment is 6 for the exponential cutoff and
    1/2 for the Gaussian, both INTEGRATED, a ratio of 12 -- so "no f, no coupling" is a measurement.
SCOPE.  Not a closure of the gauge half: it narrows to B59's composite/emergent route, the only one of
the five unexamined.  Not an argument that no spectral action exists over the face -- one does for any
f; the finding is that the construction's thermal trace is not one of them.  Not a claim about
H_phys's reading, which is reported as a DISTINCT outcome: there the weight does not act on spinors
over the face at all, so the question is ill-posed rather than answered negatively.  Three standard
five-sphere facts are taken as INPUT and declared in the computation's own source -- the lowest Dirac
eigenspace is the Killing spinors, it carries one chirality 4 of Spin(6), and the ambient (1,2)-rotation
is the great circle of circumference beta with spinorial lift Sigma_12; the second's dimension is
cross-checked against the multiplicity formula and the other two are not checked here.
COMPUTES:  at NO numeric parameter value -- alpha is symbolic throughout and beta = 2 pi alpha is kept
as a ratio, which is the point of the Lambda slot.  The discrete parameters that ARE fixed: the Clifford
algebra is the 6-dimensional one on 8 components, the chirality-4 is 4-dimensional, the moment index is
4 (the Yang-Mills order), and the rotation plane is the ambient (1,2).
"""
import contextlib
import io
import math
import os
import re
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
COMP = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7619_cc66_whether_the_thermal_trace_is_the_spectral_action', 'thermal.py')
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
     rc == 0 and n_pass == 19 and n_fail == 0 and 'ALL CHECKS PASS' in out)
gate('the thermal datum is READ from the papers: that beta = 2 pi alpha is a Euclidean continuation of '
     'that period, that the Euclidean section IS the face, and that the construction\'s own generator '
     'is the deparametrized true Hamiltonian on cosmic time',
     has(r'a Euclidean continuation of period \$\\beta=2\\pi\\alpha\$"\s+->\s+found in boundary_paper\.tex',
         r'that Euclidean is the \\emph\{same\} face" \*\*\s+->\s+found in boundary_paper\.tex',
         r'\\hat H_\{\\mathrm\{phys\}\}\\Psi\$"\s+->\s+found in CR_framework\.tex'))
gate('PINNED: the trap is MEASURED, not talked past -- the great-circle generator commutes with D '
     'exactly, which is the step a naive reading stops at',
     has(r'\|\|\[D, H_theta\]\|\| = 0\.0e\+00'))
gate('PINNED: and it is still NOT a function of D -- two weights -0.5 and 0.5 on a FOUR-dimensional '
     'D-eigenspace, with the multiplicity formula and the Spin(6) chirality split agreeing on the 4 '
     'independently, so the zero of the commutator decides nothing',
     has(r'weights on the 4 = \[-0\.5, 0\.5\], spread = 1\.0 on a 4-dimensional',
         r'dim\(\+\) = 4, multiplicity formula = 4'))
# ⌗ The three Gibbs figures are pinned by COMPARISON against the numbers parsed out of cc66's own
#   output, not by a presence test on their digits: a regex that merely finds "535.49" in a line
#   cannot fail if the computation starts printing a different number, which is the whole point of a
#   pin.  The ratio is additionally checked against exp(2 pi) computed here, so the identity the row
#   claims -- that the spread IS e^(2 pi) and not merely close to it -- is what is asserted.
_m = re.search(r'weights ([0-9.]+) and ([0-9.]+), ratio = ([0-9.]+) = e\^\(2 pi\)', out)
_lo, _hi, _rat = (float(x) for x in _m.groups()) if _m else (0.0, 0.0, 0.0)
gate("PINNED BY COMPARISON, in the construction's own number: with beta/alpha = 2 pi the thermal "
     'weight takes the values 0.0432 and 23.1407 on that single D-eigenspace, a ratio of '
     'e^(2 pi) = 535.49, where any f(D/Lambda) is constant by construction',
     _m is not None
     and abs(_lo - 0.0432) < 5e-5 and abs(_hi - 23.1407) < 5e-5
     and abs(_rat - 535.49) < 5e-3
     and abs(_rat - math.exp(2 * math.pi)) < 5e-3
     # the quotient of the two PRINTED weights is only as good as their rounding -- 0.0432 carries
     # three significant figures, so this arm is tolerant to 0.1% and no tighter; it is here to catch
     # a ratio that stops being the quotient of the pair, not to re-measure them
     and abs(_hi / _lo - _rat) / _rat < 1e-3)
gate('and the strain is recorded rather than suppressed: one of those weights exceeds 1, so the '
     'generator is not a positive Hamiltonian either',
     has(r'max weight = 23\.14 > 1'))
gate("PINNED: the SCALE is supplied -- Lambda is an inverse length, the same exponent solve returns "
     'p_a = -p_b - 1 for it, and the construction gives Lambda = 1/(2 pi alpha) exactly, so what is '
     "missing is f alone and r7615's dimensional argument did not reach this slot",
     has(r'length\^-1: p_a = -p_b - 1, so beta\^-1 qualifies',
         r'Lambda = 1/beta = 1/\(2\*pi\*alpha\)'))
gate('PINNED: and f is what a coupling needs -- the Yang-Mills order moment is 6 for the exponential '
     'cutoff against 1/2 for the Gaussian, both integrated, a ratio of 12, so the coefficient is fixed '
     'by f and MOVES with it',
     has(r'exponential: 6;\s+Gaussian: 1/2', r'ratio = 12\b'))
gate('the instrument is certified BOTH ways: it passes a true function pair (B = A^2 - 2A, constant on '
     'every A-eigenspace including the degenerate one) and refuses a pair that commutes exactly but is '
     'NOT a function pair, which is the discriminator the whole row turns on',
     has(r'function_of = True, spread = 0\.00e\+00, largest eigenspace = 2',
         r'\|\|\[A,B\]\|\| = 0\.0e\+00 yet function_of = False, spread = 1\.0 on a 2-dimensional'))
gate('the non-vacuity guard is at the INSTRUMENT and reports the eigenspace it used, since on a '
     'one-dimensional eigenspace every operator is scalar and the test could not fail',
     has(r'NON-VACUITY.*\n?.*dim = 4', r'the eigenspace tested is of dimension 4 > 1'))
gate('and the verdict is the pre-registered outcome 2 with outcome 3 held SEPARATE: the thermal trace '
     'is not this triple\'s spectral action, the gauge half narrows to the composite route, and the '
     "H_phys reading is ill-posed rather than negative",
     has(r'THE FAVOURABLE READING FAILS ON ITS OWN TERMS',
         r'pre-registered outcome 2, with outcome 3 holding separately for H_phys'))

bad = [n for n, ok in CHECKS if not ok]
print(f'\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail')
for n in bad:
    print(f'    FAILED: {n}')
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
