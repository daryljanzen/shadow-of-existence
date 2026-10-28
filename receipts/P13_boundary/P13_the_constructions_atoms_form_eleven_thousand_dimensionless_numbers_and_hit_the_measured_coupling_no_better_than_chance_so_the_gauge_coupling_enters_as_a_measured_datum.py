"""r7627+cc66 -- P13: the gauge half's atoms form 11049 dimensionless numbers, they hit the
measured strong coupling NO BETTER THAN CHANCE, and the construction supplies neither the
reference scale nor the matching condition a coupling would need.

COMPUTES: the face's radius `alpha` and the thermal length `beta` are carried SYMBOLICALLY, as at
  r7615, r7619 and r7621 -- no numeric value is assigned to either, and the row's conclusion is
  that no absolute scale is fixed, which a numeric alpha would destroy.  The one numeric physical
  parameter here is a MEASURED DATUM used as a comparison target and not a prediction:
  alpha_s(M_Z = 91.1876 GeV) = 0.1180 +- 0.0009, with 1/g^2 = 1/(4 pi alpha_s) = 0.674385 the same
  datum in a Lagrangian's normalisation.  It is quoted WITH its scale throughout; the row never
  compares a formed number against a bare coupling.

What this receipt gates, in one line: the order's named negative -- "a number formed from the data
lands near the measured strong coupling" -- IS observed, and is shown to carry no information,
because the count of candidates within the window matches what a random target in the same decades
collects.  ** The finding is the control, not the hit. **
"""
import math
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))          # receipts/P13_boundary -> repo root
WALK = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7627_cc66_the_atoms_and_the_coupling')
SRC = os.path.join(WALK, 'atoms.py')

checks = []


def ok(label, cond):
    checks.append((bool(cond), label))


# --------------------------------------------------------------------------------------------
# run the computation and capture what it printed
# --------------------------------------------------------------------------------------------
res = subprocess.run([sys.executable, SRC], capture_output=True, text=True, timeout=600)
out = res.stdout
ok('the computation runs and exits zero (rc=%d)' % res.returncode, res.returncode == 0)


def num(pat, n=1):
    """the n-th capture of `pat` as a float, or None -- so a pin is a COMPARISON and not a grep.

    ⌗ At r7619 check_figures_pinned caught this seat pinning 535.49 with a regex that found its
      digits, which cannot fail when the computation starts printing something else.  Every
      figure this row's INDEX line prints is parsed out here and compared numerically."""
    m = re.search(pat, out)
    if not m:
        return None
    try:
        return float(m.group(n))
    except (TypeError, ValueError):
        return None


# --------------------------------------------------------------------------------------------
# Ⓐ THE ENUMERATION -- the counts the row reports
# --------------------------------------------------------------------------------------------
counts = {d: num(r'sum\|exponent\| <= %d :\s+N =\s+(\d+) distinct values' % d) for d in (1, 2, 3, 4)}
ok('Ⓐ① the enumeration reports a count at every declared bound D = 1..4',
   all(v is not None for v in counts.values()))
ok('Ⓐ② the counts are 30, 374, 2481, 11049 and strictly increasing in D',
   counts[1] == 30 and counts[2] == 374 and counts[3] == 2481 and counts[4] == 11049
   and counts[1] < counts[2] < counts[3] < counts[4])
N = counts[4]
ok('Ⓐ③ the working bound is D = 4 with N = 11049 reported as the working N',
   num(r'the working bound is D = 4, N = (\d+)') == 11049)

# --------------------------------------------------------------------------------------------
# Ⓑ THE HIT THE ORDER NAMED -- it exists, and the row does not hide it
# --------------------------------------------------------------------------------------------
closest = num(r'(0\.\d+)\s+\(-0\.09%\)')
ok('Ⓑ① a formed number lands within 0.1 per cent of the measured alpha_s -- the order\'s '
   'named negative IS observed, at 0.117893',
   closest is not None and abs(closest - 0.117893) < 5e-6)
ok('Ⓑ② and it lies inside alpha_s(M_Z)\'s own experimental error, 0.1180 +- 0.0009, '
   'so it is not dismissible as a poor match',
   closest is not None and abs(closest - 0.1180) < 0.0009)

# --------------------------------------------------------------------------------------------
# Ⓒ THE CONTROL THAT KILLS IT -- observed vs expected, which is the row's whole finding
# --------------------------------------------------------------------------------------------
rows = re.findall(
    r'target (\S+)\s+window \+-\s*([\d.]+)%\s+OBSERVED\s+(\d+)\s+EXPECTED BY CHANCE\s+([\d.]+)', out)
ok('Ⓒ① all four target/window comparisons are reported (2 targets x 2 windows)', len(rows) == 4)
ratios = {}
for tgt, win, obs, exp in rows:
    ratios[(tgt, float(win))] = (int(obs), float(exp))
ok('Ⓒ② within +-1% of alpha_s(M_Z): 12 observed against 13.26 expected by chance',
   ratios.get(('alpha_s(M_Z)', 1.0), (None, None))[0] == 12
   and abs(ratios.get(('alpha_s(M_Z)', 1.0), (0, 0))[1] - 13.26) < 0.01)
ok('Ⓒ③ within +-1% of 1/g^2(M_Z): 12 observed against 13.73 expected by chance',
   ratios.get(('1/g^2(M_Z)', 1.0), (None, None))[0] == 12
   and abs(ratios.get(('1/g^2(M_Z)', 1.0), (0, 0))[1] - 13.73) < 0.01)
ok('Ⓒ④ ** THE FINDING: every observed/expected ratio lies in [0.8, 1.2], so the atoms hit the '
   'measured coupling NO BETTER THAN A RANDOM TARGET IN THE SAME DECADES **',
   len(rows) == 4 and all(0.8 <= obs / exp <= 1.2 for obs, exp in ratios.values()))
ok('Ⓒ⑤ and in the TIGHT window the atoms do slightly WORSE than chance on both targets, '
   'which is the opposite of a signal',
   ratios.get(('alpha_s(M_Z)', 1.0), (1, 1))[0] < ratios.get(('alpha_s(M_Z)', 1.0), (1, 1))[1]
   and ratios.get(('1/g^2(M_Z)', 1.0), (1, 1))[0] < ratios.get(('1/g^2(M_Z)', 1.0), (1, 1))[1])
ok('Ⓒ⑥ the chance expectation is a measurement over 4000 random targets, not an estimate',
   num(r'\((\d+) random targets in the same two decades\)') == 4000)

# --------------------------------------------------------------------------------------------
# Ⓓ THE ENUMERATION SHOWN ABLE TO MISS -- a counter that cannot miss counts nothing
# --------------------------------------------------------------------------------------------
miss_lo = num(r'target 1e-30\s+window \+-1%\s+->\s+(\d+) hit')
miss_hi = num(r'target 1e\+30\s+window \+-1%\s+->\s+(\d+) hit')
ok('Ⓓ① a target at 1e-30 collects 0 hits', miss_lo == 0)
ok('Ⓓ② a target at 1e+30 collects 0 hits', miss_hi == 0)
ok('Ⓓ③ ⇒ so the 12 hits near alpha_s are a real property of the set and not a counter that '
   'returns a hit for anything', miss_lo == 0 and miss_hi == 0 and N == 11049)

# --------------------------------------------------------------------------------------------
# Ⓔ THE POSITIVE CONTROL -- the machinery does return determinate numbers
# --------------------------------------------------------------------------------------------
ok('Ⓔ① beta/alpha = 2 pi is in the formed set, so "no coupling comes out" is not the machinery '
   'failing to produce numbers',
   re.search(r'beta/alpha = 2 pi = 6\.2831853072 is in the set: True', out) is not None)

# --------------------------------------------------------------------------------------------
# Ⓕ THE TOY CONTROL THE ORDER ASKED FOR BY NAME, and what makes it work
# --------------------------------------------------------------------------------------------
toy = num(r'1/g4\^2 = 2 pi R / g5sq = ([\d.]+)')
ok('Ⓕ① the toy construction\'s coupling IS determinate: 1/g4^2 = 2 pi R / g5sq = 12.566371',
   toy is not None and abs(toy - 12.566371) < 5e-6)
ok('Ⓕ② and it equals 2 pi for R/g5sq = 2, so the toy\'s number is the geometry TIMES an '
   'independent dimensionful datum rather than geometry alone',
   toy is not None and abs(toy - 4 * math.pi) < 1e-5)
ok('Ⓕ③ the receipt\'s own statement of why: the toy is GIVEN a dimensionful coupling and this '
   'construction is not',
   re.search(r'independent dimensionful coupling; this construction is given no such datum', out)
   is not None)

# --------------------------------------------------------------------------------------------
# Ⓖ THE THREE THINGS A MECHANISM NEEDS, AND THE ONE CARRIED FIGURE FROM r7621
# --------------------------------------------------------------------------------------------
lam_over_mu = num(r'Lambda/mu = 1/\(5 pi\) = ([\d.]+)')
ok('Ⓖ① r7621\'s figure is carried and still holds: Lambda/mu = 1/(5 pi) = 0.063662 < 1',
   lam_over_mu is not None and abs(lam_over_mu - 1.0 / (5 * math.pi)) < 5e-7 and lam_over_mu < 1)
ok('Ⓖ② the reference scale is reported NOT SUPPLIED, with the reason that alpha is symbolic',
   out.count('NOT SUPPLIED') >= 2)
ok('Ⓖ③ the matching condition is reported NOT SUPPLIED, naming the count it cannot choose among',
   re.search(r'picks WHICH of the 11049 numbers', out) is not None)

# --------------------------------------------------------------------------------------------
# Ⓗ THE GUARD THAT POINTS AGAINST THE ROW'S OWN CONCLUSION
# --------------------------------------------------------------------------------------------
# Deduping by VALUE rather than by SPELLING makes N smaller, which makes the chance expectation
# smaller, which makes a hit look MORE significant.  The row counts the harder way on purpose, and
# this check reads the source to confirm it, because the claim is about the method and not the
# output.
# ⌗ ** THESE TWO CHECKED THE SOURCE'S COMMENTS AND THAT WAS A HOLLOW ASSERTION. **  The first
#   version asserted that atoms.py's docstring SAYS it dedupes by value and recurses over the
#   support.  A comment is not behaviour: both checks would have passed with the code doing the
#   opposite so long as the prose stayed, and check_quote_pins was right to mint three keys on
#   them.  ** Do not put them back as string tests. **  Both are now BEHAVIOURAL.
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location('r7627_atoms', SRC)
_mod = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_mod)                     # atoms.py guards main() behind __main__

# ⓵ dedup by VALUE, tested on a collision the atom list actually contains: 9 is an atom and so
#    is 3, so `9` and `3^2` are two spellings of one number and both are formable at D = 2.
_t2 = _mod.enumerate_monomials(_mod.ATOMS, 2)
_nine = [v for (v, _d, _sp) in _t2.values() if abs(v - 9.0) < 1e-12]
ok('Ⓗ① the enumerator dedupes by VALUE and not by spelling, tested on a real collision: 9 is '
   'an atom and 3^2 is formable, and the table holds that value exactly ONCE',
   len(_nine) == 1)
ok('Ⓗ② and the collision is genuine -- both 3 and 9 are in the frozen atom list, so the two '
   'spellings really do exist for the enumerator to collapse',
   any(abs(a[0] - 3.0) < 1e-12 for a in _mod.ATOMS)
   and any(abs(a[0] - 9.0) < 1e-12 for a in _mod.ATOMS))

# ⓶ the support recursion, tested by what the grid version could not do: finish AT THE RIGHT COUNT.
# ⌗ ** THIS CHECK CARRIED A WALL-CLOCK TERM AND THE TOLERANCE SWEEP FLAGGED IT.  It was right. **
#   A clock measures the MACHINE, not the code: the same comparison read 0.0876 s on build A,
#   0.1232 s on build B and 0.0747 s on build C, so it was a numeric site that moves between
#   builds by construction.  Headroom of 487x and 685x did not make it stable; it made it
#   harmlessly unstable.  ** Never assert a duration in a receipt. **  The build-stable signature
#   of the support recursion is that the enumeration COMPLETES AT THE RIGHT COUNT; that the 9^15
#   grid could not finish is history, and history belongs in the docstring and the WALK, not in a
#   pinned comparison.
_t4 = _mod.enumerate_monomials(_mod.ATOMS, 4)
ok('Ⓗ③ the D = 4 enumeration COMPLETES and returns exactly 11049 values -- the build-stable '
   'signature of recursing over the support rather than over the 9^15 grid',
   len(_t4) == 11049)
ok('Ⓗ④ and it agrees with the count the computation printed, so the receipt and the run are '
   'enumerating the same set',
   len(_t4) == counts[4])

# --------------------------------------------------------------------------------------------
# Ⓘ THE CONCLUSION THE ROW ACTUALLY REACHES
# --------------------------------------------------------------------------------------------
ok('Ⓘ① the computation states the conclusion as "the coupling enters as a MEASURED DATUM"',
   re.search(r'coupling enters as a MEASURED DATUM', out) is not None)
ok('Ⓘ② and states that no monomial in these atoms is a coupling REGARDLESS of its value',
   re.search(r'No monomial in these atoms is a coupling REGARDLESS of its value', out) is not None)

# --------------------------------------------------------------------------------------------
# Ⓙ EVERY FIGURE THE INDEX LINE PRINTS, PINNED BY COMPARISON AND NOT BY A PRESENCE TEST
# --------------------------------------------------------------------------------------------
# ⌗ check_figures_pinned caught SEVEN of these unpinned on the first pass, and it was right about
#   all seven.  The worst was the offset: Ⓑ① matched the literal string "(-0.09%)", which is a
#   presence test on the digits and cannot fail when the computation starts printing something
#   else -- THE SAME FAULT THIS SEAT WAS CAUGHT FOR AT r7619 AND WROTE A RULE ABOUT.  Each figure
#   below is now recomputed or parsed and COMPARED.
alpha_s_printed = num(r'alpha_s\(M_Z = [\d.]+ GeV\) = ([\d.]+) \+- [\d.]+')
alpha_s_err = num(r'alpha_s\(M_Z = [\d.]+ GeV\) = [\d.]+ \+- ([\d.]+)')
ok('Ⓙ① the measured datum is the one this row compares against: alpha_s(M_Z) = 0.1180',
   alpha_s_printed is not None and abs(alpha_s_printed - 0.1180) < 5e-5)
ok('Ⓙ② with its quoted uncertainty 0.0009',
   alpha_s_err is not None and abs(alpha_s_err - 0.0009) < 5e-5)

inv_g2_printed = num(r'1/g\^2 = 1/\(4 pi alpha_s\) = ([\d.]+)')
ok('Ⓙ③ 1/g^2 = 1/(4 pi alpha_s) = 0.674385, RECOMPUTED here from the printed alpha_s rather '
   'than read off the line',
   inv_g2_printed is not None and alpha_s_printed is not None
   and abs(inv_g2_printed - 1.0 / (4 * math.pi * alpha_s_printed)) < 5e-6
   and abs(inv_g2_printed - 0.674385) < 5e-6)

# the offset itself, computed from the two numbers rather than matched as a string
ok('Ⓙ④ the closest hit lies -0.09 per cent from alpha_s -- the OFFSET computed from the two '
   'values, not a match on the printed digits',
   closest is not None and alpha_s_printed is not None
   and abs(100.0 * (closest / alpha_s_printed - 1.0) + 0.09) < 0.005)

# the two ratios the INDEX line prints
_r_as = ratios.get(('alpha_s(M_Z)', 1.0))
_r_g2 = ratios.get(('1/g^2(M_Z)', 1.0))
_printed = [float(x) for x in re.findall(r'ratio observed/expected = ([\d.]+)', out)]
ok('Ⓙ⑤ the alpha_s ratio observed/expected = 0.91 is the QUOTIENT OF THE PRINTED PAIR, '
   '12 / 13.26 = 0.9050, and not a number read off beside them',
   _r_as is not None and len(_printed) == 4
   and abs(_r_as[0] / _r_as[1] - _printed[0]) < 0.01
   and abs(_printed[0] - 0.91) < 1e-9)
ok('Ⓙ⑥ the 1/g^2 ratio observed/expected = 0.87 likewise, 12 / 13.73 = 0.8740',
   _r_g2 is not None and len(_printed) == 4
   and abs(_r_g2[0] / _r_g2[1] - _printed[2]) < 0.01
   and abs(_printed[2] - 0.87) < 1e-9)
ok('Ⓙ⑦ and both tight-window chance expectations are the figures the row prints, 13.26 and 13.73',
   _r_as is not None and _r_g2 is not None
   and abs(_r_as[1] - 13.26) < 0.005 and abs(_r_g2[1] - 13.73) < 0.005)
ok('Ⓙ⑧ ⌗ and the quotient is taken from the 2-dp expectation ON PURPOSE: at 1 dp the printed '
   '13.3 could not reproduce 0.91 at all (12/13.3 = 0.9023), which is the r7619 rounding fault '
   '-- a quotient of printed numbers is only as good as their rounding',
   _r_as is not None and abs(12.0 / 13.3 - 0.9023) < 5e-4
   and abs(12.0 / _r_as[1] - 0.9050) < 5e-4)

# --------------------------------------------------------------------------------------------
print()
print('=' * 94)
print('  r7627+cc66 -- P13: the atoms form %d numbers and hit the measured coupling at chance rate'
      % (N if N else -1))
print('=' * 94)
print()
fails = [l for good, l in checks if not good]
for good, label in checks:
    print('  %s  %s' % ('OK  ' if good else 'FAIL', label))
print()
print('  %d check(s), %d FAILED' % (len(checks), len(fails)))
print()
if fails:
    print('  ⛔ FAILED: ' + '; '.join(fails))
    sys.exit(1)
print('  ⇒ The order\'s named negative is observed and shown to be uninformative: 12 of %d formed'
      % N)
print('    numbers land within 1% of alpha_s(M_Z), against 13.3 expected by chance (ratio 0.91).')
print('    The construction supplies no reference scale and no matching condition, and the reason')
print('    is dimensional: a coupling is an action normalisation, the atoms are geometry.')
print('    ⇒ The gauge coupling enters as a MEASURED DATUM.')
print()
