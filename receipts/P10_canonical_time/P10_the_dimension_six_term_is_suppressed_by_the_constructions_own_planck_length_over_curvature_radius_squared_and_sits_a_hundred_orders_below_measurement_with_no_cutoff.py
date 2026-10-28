"""r7633+cc66 -- P10: sized by the construction's OWN scales rather than by a cutoff it does not
have, the dimension-six term is suppressed against dimension four by (ell_P/a)^2 and sits 110 to 120
orders BELOW what measurement resolves on all four observables, so PO-89 closes as its clause reads.

COMPUTES: no parameter of the construction is given a numeric value here.  The numeric inputs are of
  three kinds, all declared:
  (i) LANDED STATEMENTS OF THE CORPUS, located and reproduced rather than asserted -- "in the reduced
      theory the only scales are `a` and the Planck length", the vacuum energy being
      a^-1 sum_j f_j (ell_P/a)^j against a polynomial in ln(a/ell_P), with ONE VERTEX PAIR COSTING
      ell_P^2 (canonical_time l.1621-1623); ell_P as "a gauge-combination rather than a second
      physical length" (l.484); the dimension-four anomaly Theta ∝ (15/4) a^-4, scheme-independent
      (l.583-585); the dimension-six obstruction coefficient 6023/20160 (l.1283); and that on this
      background the dimension-six INVARIANT CANNOT BE NAMED, the five scalars collapsing to rank one
      and naming nothing (l.1283);
  (ii) ONE INHERITED DATUM, the MEASURED gravitational coupling as a length, ell_P = 1.616255e-35 m
      (CODATA).  ** It is a measured datum and NOT a cutoff, which is the whole point of the row **;
  (iii) COSMOLOGICAL INPUTS at each epoch, declared and varied by a decade -- H0 = 67.4 km/s/Mpc,
      Omega_m = 0.315, z_rec = 1089.9 -- plus the four measured precisions carried from r7629.

** WHAT THIS RECEIPT GATES IN ONE LINE: the dimension-six term's effect is below measurement on every
observable by more than a hundred orders, sized with NO cutoff anywhere -- and that absence is shown
by measurement rather than claimed. **

⌗ THE ROW'S OWN QUALIFICATION, gated so it cannot be dropped.  The order asked what multiplies "the
  dimension-six INVARIANT".  On this background there is none to multiply: P10 says the five
  dimension-six scalars collapse on the one-parameter family -- two vanish identically, the rest are
  pure numbers, rank one -- so the residue "is one equation on three directions ... and IT NAMES
  NOTHING", and the receipt carrying that is titled in exactly those terms.  ⇒ So what is sized here
  is the magnitude of the dimension-six OBSTRUCTION.  The suppression is dimensional and therefore
  unaffected; what it multiplies is not an invariant, and this row does not supply one.
  PREDICTION.md registered this as the outcome to report rather than paper over.
"""
import math
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
WALK = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7633_cc66_sizing_without_a_cutoff')
SRC = os.path.join(WALK, 'sizing.py')
CORPUS = os.path.join(ROOT, 'corpus')

checks = []


def ok(label, cond):
    checks.append((bool(cond), label))


res = subprocess.run([sys.executable, SRC], capture_output=True, text=True, timeout=900)
out = res.stdout
ok('the computation runs and exits zero (rc=%d)' % res.returncode, res.returncode == 0)


def num(pat, n=1):
    """the n-th capture of `pat` as a float, or None -- so a pin is a COMPARISON, not a grep."""
    m = re.search(pat, out)
    if not m:
        return None
    try:
        return float(m.group(n))
    except (TypeError, ValueError):
        return None


sys.path.insert(0, WALK)
import sizing as _mod  # noqa: E402

# --------------------------------------------------------------------------------------------
# Ⓐ THE INHERITED DATUM AND THE LANDED COEFFICIENTS
# --------------------------------------------------------------------------------------------
ok('Ⓐ① ell_P is carried as the MEASURED 1.616255e-35 m -- an inherited datum, not a cutoff',
   abs(_mod.ELL_P_M * 1e35 - 1.616255) < 2e-6)
ok('Ⓐ② the dimension-four anomaly coefficient is the corpus\'s 15/4',
   abs(_mod.C4 - 3.75) < 1e-12)
ok('Ⓐ③ the dimension-six obstruction coefficient is the corpus\'s 6023/20160 = 0.298760',
   abs(_mod.C6 - 6023.0 / 20160.0) < 1e-12 and abs(_mod.C6 - 0.298760) < 2e-6)

# --------------------------------------------------------------------------------------------
# Ⓑ CONTROL (1) -- THE DIMENSION-FOUR CONTROL, which validates the estimator on a term whose
#   order is INDEPENDENTLY KNOWN.  If this fails, every dimension-six number below is worthless.
# --------------------------------------------------------------------------------------------
_pref = _mod.C4 * 8.0 / 3.0
ok('Ⓑ① (15/4)(8/3) = 10 EXACTLY, so the anomaly-to-background prefactor is 10 pi -- arithmetic the '
   'row reproduces rather than asserts', abs(_pref - 10.0) < 1e-12)
_pref_pi = num(r'=  ([\d.]+) \(ell_P/a\)\^2')
ok('Ⓑ② and the printed prefactor is 31.415927 = 10 pi',
   _pref_pi is not None and abs(_pref_pi - 31.415927) < 2e-6
   and abs(_pref_pi - 10.0 * math.pi) < 1e-5)
_a_now = _mod.hubble_radius_m(0.0)
_anom = (_mod.C4 * 8.0 * math.pi / 3.0) * _mod.suppression(_a_now)
ok('Ⓑ③ the dimension-four anomaly sized against the classical background returns 4.357e-121 at the '
   'present epoch -- which IS the known order of a one-loop graviton correction, the familiar '
   '(ell_P H)^2 ~ 1e-122 times the 10 pi prefactor.  ** The estimator therefore returns the right '
   'order for a term whose order is known independently, which is the only reason to trust it on '
   'one that is not. **', abs(_anom * 1e121 - 4.357) < 0.002)
ok('Ⓑ④ and the row states the trap: 15/4 is scheme-INDEPENDENT while a logarithm\'s value is not, '
   'so the control checks the ORDER and never a digit',
   'checks the ORDER and never a digit' in out)

# --------------------------------------------------------------------------------------------
# Ⓒ STEP (1) -- THE SUPPRESSION IS (ell_P/a)^2, AND IT IS THE CONSTRUCTION'S OWN
# --------------------------------------------------------------------------------------------
_sup_now = _mod.suppression(_a_now)
_a_rec = _mod.hubble_radius_m(_mod.Z_REC)
_sup_rec = _mod.suppression(_a_rec)
ok('Ⓒ① the curvature radius today is c/H0 = 1.3725e26 m', abs(_a_now * 1e-26 - 1.3725) < 0.0002)
ok('Ⓒ② at recombination it is 6.7870e21 m', abs(_a_rec * 1e-21 - 6.7870) < 0.0002)
ok('Ⓒ③ so the suppression (ell_P/a)^2 is 1.3867e-122 today', abs(_sup_now * 1e122 - 1.3867) < 0.0002)
ok('Ⓒ④ and 5.6710e-114 at recombination', abs(_sup_rec * 1e114 - 5.6710) < 0.0002)
ok('Ⓒ⑤ the logarithm the construction fixes is ln(a/ell_P) -- 140.3 today and 130.4 at '
   'recombination, so it is of order 1e2 and cannot rescue a 1e-122',
   abs(_mod.log_factor(_a_now) - 140.3) < 0.05 and abs(_mod.log_factor(_a_rec) - 130.4) < 0.05)
ok('Ⓒ⑥ ** AND THE SUPPRESSION FUNCTION TAKES NO CUTOFF ARGUMENT AT ALL ** -- checked on the '
   'signature, not on the prose: its only parameter is the curvature radius',
   list(_mod.suppression.__code__.co_varnames[:_mod.suppression.__code__.co_argcount]) == ['a_m'])

# --------------------------------------------------------------------------------------------
# Ⓓ STEP (2) + (3) -- THE FOUR OBSERVABLES AT THEIR OWN EPOCHS, AGAINST MEASURED PRECISION
# --------------------------------------------------------------------------------------------
_r = _mod._r7629
_margins = {}
for _n, _e, _s, _d in _r.OBSERVABLES:
    _a = _a_now if 'rate' in _n else _a_rec
    _margins[_n] = math.log10(_s / (_mod.C6 * _mod.suppression(_a)))
ok('Ⓓ① the rate H0 sits 120.4 orders below its precision',
   abs(_margins['the rate H0'] - 120.4) < 0.05)
ok('Ⓓ② the acoustic scale 110.2, the tilt 111.4, the tensor amplitude 112.3',
   abs(_margins['the acoustic scale'] - 110.2) < 0.05
   and abs(_margins['the tilt n_s'] - 111.4) < 0.05
   and abs(_margins['the tensor amplitude'] - 112.3) < 0.05)
ok('Ⓓ③ the SMALLEST of the four margins is 110.2 orders and it is the ACOUSTIC SCALE -- the same '
   'observable that bound r7629\'s threshold, which is a consistency this row did not arrange',
   abs(min(_margins.values()) - 110.2) < 0.05
   and min(_margins, key=_margins.get) == 'the acoustic scale')
ok('Ⓓ④ every one of the four is more than 100 orders below measurement, so the verdict does not '
   'rest on the worst case', all(v > 100.0 for v in _margins.values()))

# --------------------------------------------------------------------------------------------
# Ⓔ THE ORDER'S REACHABLE NEGATIVE -- missed, and for a STRUCTURAL reason
# --------------------------------------------------------------------------------------------
_tight = min(s for _n, _e, s, _d in _r.OBSERVABLES)
_a_reach = _mod.ELL_P_M / math.sqrt(_tight / _mod.C6)
# ⌗ The tolerance here was first 0.02, which EXCEEDS check_figures_pinned's allowance for a figure
#   printed to two decimals (max(0.5e-2, 5e-4*32.1) = 0.016) -- so the gate did not count it as a pin
#   at all and the figure read as UNPINNED.  A pin looser than the gate's allowance is not a pin.
ok('Ⓔ① the term reaches the tightest precision only at a = 32.10 ell_P -- the Planck era',
   abs(_a_reach / _mod.ELL_P_M - 32.10) < 0.005)
ok('Ⓔ② and the earliest epoch any of the four observables reads, recombination, has a exceeding '
   'ell_P by 57 orders -- so the negative is missed by 55 orders of curvature radius, not by a '
   'close call', abs(math.log10(_a_rec / _mod.ELL_P_M) - 56.6) < 0.1)
ok('Ⓔ③ ⇒ the row reports the negative as MISSED STRUCTURALLY rather than numerically',
   'STRUCTURAL REASON RATHER THAN A' in out)

# --------------------------------------------------------------------------------------------
# Ⓕ CONTROL (3) -- THE CUTOFF SHOWN **ABSENT** BY MEASUREMENT.  This is the row's own claim and
#   the one control that could not be borrowed from r7629.
# --------------------------------------------------------------------------------------------
_theirs = [_r.C6 * (1.0 / lam) ** 2 for lam in (1e-3, 1.0, 1e3, 1e6, 1e9)]
ok('Ⓕ① r7629\'s estimator moves 24 orders as Lambda moves over 12 -- it DEPENDS on a cutoff',
   abs(math.log10(max(_theirs) / min(_theirs)) - 24.0) < 0.01)
# ⌗ ** Ⓕ② HAS NOW BEEN WRONG TWICE AND BOTH ARE RECORDED. **  ⑴ It first took max/min over five
#   IDENTICAL recomputations of one constant, which is 1.0 for any function whatever and could not
#   have failed.  ⑵ Repairing that by reading the printed table introduced `len(_printed) == 5` and
#   `len(set(_printed)) == 1` -- TWO PINS ON COUNTS, which check_prose_pins flagged (161 -> 163)
#   before this reached CI.  A count holds while the thing it counts moves.
#   ⇒ What is asserted now is a SET EQUALITY against the module's own sweep, a UNIVERSAL over the
#     reported values, and a MEASURED SPREAD -- no counts, and each moves if the row does.
#     ** Do not reintroduce a row count or a recomputation. **
_rows_p = re.findall(r'^      (1e[+-]\d+)\s+([\d.]+e[+-]\d+)\s+([\d.]+e[+-]\d+)\s*$', out, re.M)
_lams_p = {float(r[0]) for r in _rows_p}
_theirs_p = [float(r[1]) for r in _rows_p]
_mine_p = [float(r[2]) for r in _rows_p]
# ⌗ The spread's MAGNITUDE is pinned by Ⓕ① from the module.  What the printed side must add is that
#   r7629's reported value VARIES WITH Lambda while this row's does not -- expressed as strict
#   monotonicity in Lambda, which is scale-free and says exactly "depends on the cutoff".  A
#   threshold on a parsed value is a prose pin (check_prose_pins flagged `max/min > 1e20`); a
#   monotonicity over the reported series is not, and it is the stronger statement.
_by_lam = sorted(zip((float(r[0]) for r in _rows_p), _theirs_p, _mine_p))
_theirs_sorted = [t for _l, t, _m in _by_lam]
_mine_sorted = [m for _l, _t, m in _by_lam]
ok('Ⓕ② the printed table covers exactly the module\'s own cutoff sweep (set equality, not a row '
   'count); across it r7629\'s reported value is STRICTLY DECREASING in Lambda -- it depends on the '
   'cutoff -- while this row\'s is IDENTICAL at every Lambda.  ** Read off the output rather than '
   'recomputed, so what is checked is the number the row actually reports. **',
   _lams_p == set(_mod.CUTOFF_SWEEP)
   and bool(_mine_sorted) and all(v == _mine_sorted[0] for v in _mine_sorted)
   and all(_theirs_sorted[i] > _theirs_sorted[i + 1] for i in range(len(_theirs_sorted) - 1)))
ok('Ⓕ③ and the contrast is real rather than tautological: the two estimators are compared on the '
   'SAME coefficient and the same term, so what differs is only whether a cutoff enters',
   abs(_r.C6 - _mod.C6) < 1e-12)

# --------------------------------------------------------------------------------------------
# Ⓖ CONTROL (5) -- A DECADE OF `a`, since the epochs carry cosmological inputs
# --------------------------------------------------------------------------------------------
_spread = []
for f in (0.1, 1.0, 10.0):
    _spread.append(math.log10(1.0e-2 / (_mod.C6 * _mod.suppression(_a_now * f))))
    _spread.append(math.log10(2.9e-4 / (_mod.C6 * _mod.suppression(_a_rec * f))))
ok('Ⓖ① across a decade either way in `a`, at both epochs, every margin stays above 100 orders '
   '(range %.1f to %.1f) -- a factor of a few in a cosmological input cannot move this verdict'
   % (min(_spread), max(_spread)), min(_spread) > 100.0)
ok('Ⓖ② and the margin moves by exactly 2 orders per decade of `a`, which is the (ell_P/a)^2 '
   'scaling reproducing itself -- so the robustness check is measuring the right function',
   abs((_spread[2] - _spread[0]) - 2.0) < 1e-9)

# --------------------------------------------------------------------------------------------
# Ⓗ THE QUALIFICATION -- that no dimension-six invariant is nameable here, read from the paper
# --------------------------------------------------------------------------------------------
_ct = ' '.join(open(os.path.join(CORPUS, 'canonical_time.tex'), errors='replace').read().split())
# ⌗ ** THIS WAS FIRST A REGEX, AND check_paper_pins_present CAUGHT IT. **  A PAPER pin's literal
#   must be findable text in a paper; a regex with metacharacters appears in no `.tex` at all, so the
#   key read as "absent from every corpus/*.tex".  ⇒ A plain literal instead -- and this one occurs
#   EXACTLY ONCE, in canonical_time.tex alone, so it is a single-site pin on the sentence itself.
#   ⌗ The shorter phrase "and it names nothing" was rejected for the pin: it also appears in the
#     generated appendices, because THIS ROW'S OWN INDEX LINE quotes it, which would make the pin
#     partly self-referential.
_NAMES_NOTHING = 'the residue at an instant is one equation on three directions'
ok('Ⓗ① the paper\'s own words are READ, not recalled: P10 says the dimension-six residue on the '
   'one-parameter family "is one equation on three directions", and it is this sentence the row\'s '
   'qualification rests on -- so the qualification goes RED if 69 rewords it',
   _NAMES_NOTHING in _ct)
ok('Ⓗ② ⇒ so the row sizes the magnitude of the OBSTRUCTION and says so, rather than inventing an '
   'invariant for the coefficient to multiply',
   'OBSTRUCTION, not an' in out and 'does not supply one' in out)
ok('Ⓗ③ and the suppression is unaffected by that, being dimensional -- which the row also states',
   'dimensional and so unaffected' in out or 'suppression is dimensional' in out)

# --------------------------------------------------------------------------------------------
# Ⓙ THE DECLARED COSMOLOGICAL INPUTS, pinned because the row PRINTS them.
#
# ⌗ These were printed in the INDEX line and pinned nowhere, so check_figures_pinned read three
#   unpinned figures (1383 -> 1387 with 32.10's loose tolerance).  A figure a citing line prints is
#   pinned only by a COMPARISON in the receipt -- an input is not exempt for being an input.
# --------------------------------------------------------------------------------------------
ok('Ⓙ① H0 is carried as the declared 67.4 km/s/Mpc -- the same rate r7629 used, so the two rows of '
   'this programme read the same background', abs(_mod.H0_KM_S_MPC - 67.4) < 0.01)
ok('Ⓙ② Omega_m is the declared 0.315', abs(_mod.OMEGA_M - 0.315) < 1e-4)
ok('Ⓙ③ z_rec is the declared 1089.9', abs(_mod.Z_REC - 1089.9) < 0.01)
ok('Ⓙ④ and these three are INPUTS, not results: the row varies `a` by a decade either way around '
   'them (control 5) precisely because they are inherited rather than computed here',
   min(_spread) > 100.0)

# --------------------------------------------------------------------------------------------
# Ⓘ FAILABILITY -- every pinned figure must FAIL when the value moves
# --------------------------------------------------------------------------------------------
_probes = [
    ('ell_P', abs(_mod.ELL_P_M * 1.01 * 1e35 - 1.616255) < 2e-6),
    ('a today', abs(_a_now * 1.001 * 1e-26 - 1.3725) < 0.0002),
    ('suppression today', abs(_sup_now * 1.001 * 1e122 - 1.3867) < 0.0002),
    ('the rate margin', abs(_margins['the rate H0'] * 1.001 - 120.4) < 0.05),
    ('the reach radius', abs((_a_reach * 1.01) / _mod.ELL_P_M - 32.10) < 0.02),
    ('the log factor', abs(_mod.log_factor(_a_now) * 1.001 - 140.3) < 0.05),
    ('H0', abs(_mod.H0_KM_S_MPC * 1.001 - 67.4) < 0.01),
    ('Omega_m', abs(_mod.OMEGA_M * 1.001 - 0.315) < 1e-4),
    ('z_rec', abs(_mod.Z_REC * 1.001 - 1089.9) < 0.01),
    ('the reach radius, tightened', abs((_a_reach * 1.001) / _mod.ELL_P_M - 32.10) < 0.005),
]
_alive = [n for n, c in _probes if c]
ok('Ⓘ① each pinned figure FAILS its own comparison under a 0.1-1%% perturbation (%s)'
   % (','.join(_alive) or 'all failed as they must'), not _alive)
ok('Ⓘ② and the two exact rationals move when the coefficients they come from move: (15/4)(8/3) = 10 '
   'but (15/4)(8/3) with 15/4 -> 19/4 gives %.4f, not 10' % (4.75 * 8.0 / 3.0),
   abs(_pref - 10.0) < 1e-12 and abs(4.75 * 8.0 / 3.0 - 10.0) > 1e-6)

# --------------------------------------------------------------------------------------------
print()
print('=' * 96)
print('  r7633+cc66 -- P10: the dimension-six term sized by (ell_P/a)^2, a hundred orders below')
print('  measurement, with no cutoff anywhere')
print('=' * 96)
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
print('  ⇒ On this background the only scales are `a` and ell_P, so the dimension-six term is')
print('    suppressed against dimension four by (ell_P/a)^2 -- one vertex pair\'s ell_P^2 and two')
print('    more inverse powers of the only length there is -- with ln(a/ell_P) in the logarithm.')
print('    Sized that way it sits 110.2 to 120.4 orders BELOW what measurement resolves on all four')
print('    observables, the acoustic scale binding as it did at r7629.')
print('  ⇒ The estimator is validated FIRST on the dimension-four anomaly, where (15/4)(8/3) = 10')
print('    exactly gives 10 pi (ell_P/a)^2 = 4.357e-121 today -- the known one-loop graviton order.')
print('  ⇒ And the cutoff is shown ABSENT BY MEASUREMENT: r7629\'s estimator moves 24 orders as')
print('    Lambda moves 12, while this one moves by a factor of exactly 1.0.')
print('  ⇒ ** PO-89 CLOSES AS ITS CLAUSE NOW READS. **  The reachable negative is missed')
print('    structurally: the term would need a curvature radius of 32 ell_P, and the earliest epoch')
print('    any observable reads exceeds ell_P by 57 orders.')
print('  ⚠ With one qualification this row does not drop: on this background the dimension-six')
print('    INVARIANT cannot be named, so what is sized is the magnitude of the OBSTRUCTION.')
print()
