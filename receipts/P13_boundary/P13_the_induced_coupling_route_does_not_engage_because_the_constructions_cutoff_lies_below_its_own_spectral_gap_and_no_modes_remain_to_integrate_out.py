#!/usr/bin/env python3
"""P13 sec:synthesis / sec:face-status -- PO-94's gauge half, B59's FIFTH and last route: the composite
or induced-coupling route does NOT engage on the face, and the missing datum is NEITHER of the two the
order named.  The species count IS fixed and the infrared scale IS fixed; what fails is that the cutoff
the construction supplies lies BELOW its own spectral gap, leaving no modes to integrate out.

WHAT IS CHECKED.  cc66's computation at r7621+cc66
(computations/beyond_the_wall/r7621_cc66_the_composite_route_and_the_induced_coupling/induced.py,
registered before it existed in PREDICTION.md there) is run from source; every one of its 17 checks
must pass, and the figures the row quotes are pinned BY COMPARISON against numbers parsed out of its
output -- never by a presence test on their digits, which cannot fail when the computation changes:
  * both scales are READ from the paper rather than recalled: the face's least Dirac eigenvalue
    5/2alpha, and the thermal period beta = 2 pi alpha from which r7619's Lambda = 1/beta is built;
  * the Sakharov form 1/g^2 = c N log(Lambda/mu) needs a species count, an ultraviolet cutoff and an
    infrared scale.  The order expected mu to be the free one.  It is NOT: the face is COMPACT, so its
    spectrum is GAPPED, and a gap is an infrared scale the construction fixes;
  * so every slot fills -- N = 4 from the spinor rank, mu = 5/2alpha from the gap, Lambda = 1/beta --
    and the mechanism fails for a different reason: Lambda/mu = 1/(5 pi) < 1, the cutoff lying BELOW
    the gap by a factor of 5 pi, with log(Lambda/mu) = -2.754168;
  * and the DECISIVE form is a count, not a sign: the number of face Dirac modes with |lambda| <= Lambda
    is ZERO.  A loop of a field with no modes under the cutoff induces nothing, so the mechanism does
    not come out one datum short -- it does not engage;
  * the counter is certified both ways: it returns 8 modes at 3/alpha and 210672 at 20/alpha, so it CAN
    count, and ZERO below the gap on a cutoff chosen for the test rather than on the construction's;
  * the order's own reading is run too, so the verdict does not rest on this row's one identification:
    with mu free, d(1/g^2)/d(mu) = -N/(12 pi^2 mu) is non-zero everywhere, so a free mu is a free
    coupling.  BOTH readings give no fixed coupling, by DIFFERENT mechanisms;
  * and the control the order asked for by name: with a window the right way up the coupling IS a
    number, 1/g^2 = 0.155534 at Lambda/mu = 100 and 0.233301 at 1000, so the coefficient MOVES with the
    data and "no window, no coupling" is a measurement rather than a form of words.
SCOPE.  Not a closure of B59's last route: outcome 3 ("the route does not apply to this face") is
AVAILABLE on the zero-mode reading while outcome 2 is what is reported, and WHICH of the two the
register takes is the coordinating seat's ruling, not this row's -- the pre-registration undertook not
to collapse that distinction and this receipt does not collapse it either.  Not a claim that the gap IS
the induced coupling's infrared scale as a matter of corpus doctrine: that identification is cc66's,
stated in the computation and in the WALK, and it wants adjudicating rather than inheriting -- which is
why the order's reading is run beside it.  Not a species count from PO-95's quantised field, which is on
the SLICING and not the face; that is a different object and this row does not supply it.
COMPUTES:  at NO numeric parameter value -- alpha is symbolic throughout and both scales are carried as
multiples of 1/alpha, so the ratio and the mode count are independent of the face's radius having a
value.  The parameters that ARE fixed are discrete: the sphere dimension is 5 (spinor rank 4), the
species count is that rank, and the two probe windows are Lambda/mu = 100 and 1000.
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
                    'r7621_cc66_the_composite_route_and_the_induced_coupling', 'induced.py')
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


def num(pat, n=1):
    """the n-th capture of `pat` as a float, or None -- so a pin is a COMPARISON and not a grep.

    ⌗ Every figure this row prints is pinned through here.  At r7619 check_figures_pinned caught this
    seat pinning 535.49 with a regex that found its digits, which cannot fail when the computation
    starts printing something else; a pin has to be a comparison against what the run produced.
    """
    m = re.search(pat, out)
    return float(m.group(n)) if m else None


gate(f"cc66's computation runs from source and every check it makes passes ({n_pass} pass, {n_fail} fail)",
     rc == 0 and n_pass == 17 and n_fail == 0 and 'ALL CHECKS PASS' in out)
gate("both scales are READ from the paper and not recalled: the face's least Dirac eigenvalue, and the "
     "thermal period from which r7619's Lambda is built",
     has(r'the least eigenvalue is \$5/2\\alpha\$"\s+->\s+found in boundary_paper\.tex',
         r'a Euclidean continuation of period \$\\beta=2\\pi\\alpha\$"\s+->\s+found in boundary_paper\.tex'))

_ratio = num(r'Lambda/mu = 1/\(5\*pi\) = ([0-9.]+)')
_fivepi = num(r'and 5 pi = ([0-9.]+)')
_log = num(r'log\(Lambda/mu\) = log\(1/\(5\*pi\)\) = (-[0-9.]+)')
gate('PINNED BY COMPARISON: the window is INVERTED -- Lambda/mu = 0.063662, which is 1/(5 pi) to the '
     'precision printed, with 5 pi = 15.7080, so the cutoff lies below the gap by that factor and the '
     'logarithm the induced coupling needs is -2.754168',
     _ratio is not None and abs(_ratio - 0.063662) < 5e-7
     and abs(_ratio - 1 / (5 * math.pi)) < 5e-6
     and _fivepi is not None and abs(_fivepi - 15.7080) < 5e-5
     and _log is not None and abs(_log - (-2.754168)) < 5e-7
     and abs(_log - math.log(1 / (5 * math.pi))) < 5e-6)

_cut = num(r'Lambda = 1/\(2\*pi\) / alpha = ([0-9.]+) / alpha')
_under = num(r'against a least eigenvalue of ([0-9.]+) / alpha')
_nmode = num(r'least eigenvalue of [0-9.]+ / alpha  ->  ([0-9]+) modes')
gate('PINNED BY COMPARISON, AND IT IS THE FINDING: the cutoff is 0.159155/alpha against a least '
     'eigenvalue of 2.5/alpha, so the number of face modes under it is ZERO -- a count, not a sign, and '
     'a loop of a field with no modes under the cutoff induces nothing',
     _cut is not None and abs(_cut - 0.159155) < 5e-6
     and abs(_cut - 1 / (2 * math.pi)) < 5e-6
     and _under is not None and abs(_under - 2.5) < 1e-9
     and _nmode is not None and _nmode == 0
     and _cut < _under)

_m3 = num(r'cut = 3/alpha -> ([0-9]+) modes')
_m20 = num(r'cut = 20/alpha -> ([0-9]+) modes')
_mbelow = num(r'cut = 2/alpha \(below 5/2\) -> ([0-9]+) modes')
gate('PINNED BY COMPARISON: the counter is certified BOTH ways -- 8 modes at 3/alpha and 210672 at '
     '20/alpha, so it can count and rises with the cutoff, and ZERO below the gap on a cutoff chosen '
     'for the test rather than on the construction\'s. A zero from a counter that cannot return '
     'non-zero would mean nothing',
     _m3 is not None and _m3 == 8 and _m20 is not None and _m20 == 210672
     and _m20 > _m3 > 0 and _mbelow is not None and _mbelow == 0)

_g100 = num(r'Lambda/mu = 100 -> ([0-9.]+);')
_g1000 = num(r'Lambda/mu = 1000 -> ([0-9.]+)')
_gneg = num(r'on Lambda/mu = 1/\(5 pi\): 1/g\^2 = (-[0-9.]+)')
gate('PINNED BY COMPARISON, the control the order asked for by name: with a window the right way up '
     'the coupling IS a number -- 0.155534 at Lambda/mu = 100 and 0.233301 at 1000, so it MOVES with '
     'the data -- while the same expression on the construction\'s own ratio returns -0.093019, so the '
     'two cases are told apart by the instrument and "no window, no coupling" is a measurement',
     _g100 is not None and abs(_g100 - 0.155534) < 5e-7
     and _g1000 is not None and abs(_g1000 - 0.233301) < 5e-7
     and _g1000 > _g100 > 0
     and _gneg is not None and abs(_gneg - (-0.093019)) < 5e-7 and _gneg < 0)

gate('PINNED: the species count is NOT the missing datum -- the spinor rank is 4 in dimension five '
     'with 4 states at the lowest level, and the multiplicities are recomputed here rather than '
     'carried from r7615',
     has(r'rank\(5\) = 4, rank\(6\) = 8', r'm_0 = 4, m_1 = 20',
         r'N = 4 from the rank, 4 states at the lowest level'))
gate("the order's OWN reading is run beside this row's, so the verdict does not rest on the one "
     'identification cc66 makes: with mu free the coupling is free, the derivative being non-zero for '
     'every mu, and BOTH readings give no fixed coupling by different mechanisms',
     has(r'd\(1/g\^2\)/d\(mu\) = -N/\(12\*pi\*\*2\*mu\), non-zero for all mu > 0',
         r'mu free -> free coupling; mu = gap -> zero modes'))
gate('and the verdict names the pre-registered outcome 2 while holding outcome 3 open: the missing '
     'datum is neither of the order\'s two, and whether this CLOSES the last route or merely fails to '
     'engage it here is routed rather than collapsed',
     has(r'THE REASON IS NOT THE ONE \n?.*THE ORDER NAMED|THE REASON IS NOT THE ONE THE ORDER NAMED',
         r'N = 4 fixed, mu = 5/2alpha fixed, Lambda/mu = 1/\(5 pi\) < 1, modes under cutoff = 0',
         r'the close-or-not-engage distinction is routed, not collapsed'))

bad = [n for n, ok in CHECKS if not ok]
print(f'\n  {len(CHECKS)} checks, {len(CHECKS) - len(bad)} pass, {len(bad)} fail')
for n in bad:
    print(f'    FAILED: {n}')
print(f"  GATES: {'ALL PASS' if not bad else 'FAILURES ABOVE'}")
assert not bad, f'{len(bad)} check(s) failed: {bad}'
