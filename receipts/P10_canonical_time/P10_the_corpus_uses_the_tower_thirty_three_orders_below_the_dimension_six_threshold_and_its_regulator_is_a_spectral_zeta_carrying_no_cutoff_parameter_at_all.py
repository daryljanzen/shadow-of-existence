"""r7631+cc66 (2) -- P10: the lowest energy at which the corpus uses the interacting tower is ~33
orders BELOW PO-89's 8.345 eV threshold, so the exit does NOT fire; and the sharper finding is that
the construction's regulator is a SPECTRAL ZETA carrying no cutoff parameter at all, so the exit is
not merely unsatisfied but not addressable from inside the construction as it stands.

COMPUTES: no parameter of the construction is given a numeric value here.  The numeric inputs are of
  three kinds, all declared:
  (i) LANDED STATEMENTS OF THE CORPUS, located by line and reproduced rather than quoted -- the
      tower's spectrum mu_n^2 = n(n+2), n >= 2 (canonical_time l.389), equivalently mu^2 = m^2 - 1
      with degeneracy d = 2(m^2 - 4) on labels m = n+1 >= 3 (l.488); the physical frequency
      omega_n = mu_n/a (l.373); the spectral zeta at the origin zeta(0) = 10 EXACTLY and the
      zero-point sum's logarithmic coefficient 15/4 (l.489-492); and the scale factor factoring out
      of the sum identically (l.493, receipt P10_the_scale_factor_factors_out_of_the_free_tower);
  (ii) THIS SEAT'S OWN LANDED THRESHOLD, 8.345 eV, CARRIED by importing r7629's module and calling
      its own `threshold_lambda` on its own OBSERVABLES -- never retyped, so if that row's
      coefficient or inputs move, this comparison moves with them;
  (iii) ONE COSMOLOGICAL INPUT, declared and varied: 1/a of order H0 = 1.44e-33 eV, also carried
      from r7629.  r7627 established the construction fixes no absolute scale, so `a` is not
      something it supplies; the answer is therefore reported in ORDERS OF MAGNITUDE and checked at
      three values of 1/a spanning a decade.

** WHAT THIS RECEIPT GATES IN ONE LINE: PO-89's exit does not fire on this route -- and not because
the cutoff is low, but because the construction has no cutoff for the exit to be about. **

⌗ THE ASYMMETRY THE REGISTRATION WROTE DOWN BEFORE THIS RAN, gated here so it cannot be smoothed
  over.  A lowest use ABOVE 8.345 eV would fire the exit.  A lowest use BELOW it establishes NOTHING
  about the cutoff: a construction can use a tower at the Hubble scale and still carry a Planck-scale
  cutoff, and the mode sums run over all labels regardless.  ** So the low answer below is NOT
  evidence against the exit, and check Ⓖ holds that distinction in place. **
"""
import math
import os
import re
import subprocess
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
WALK = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7631_cc66_the_coupled_edge')
SRC = os.path.join(WALK, 'cutoff.py')
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
import cutoff as _mod  # noqa: E402

# --------------------------------------------------------------------------------------------
# Ⓐ THE THRESHOLD, CARRIED -- recomputed by r7629's OWN function on its OWN observables
# --------------------------------------------------------------------------------------------
_r = _mod._r7629
_tab = [(nm, _r.threshold_lambda(e, s) / _r.GEV_PER_EV) for nm, e, s, _d in _r.OBSERVABLES]
_binding = max(_tab, key=lambda t: t[1])
ok('Ⓐ① the binding threshold recomputed from r7629\'s own function is 8.345 eV',
   abs(_binding[1] - 8.345) < 0.002)
ok('Ⓐ② and it is the ACOUSTIC SCALE that binds, as r7629 found -- so this row compares against '
   'that row\'s result and not against a number typed in here',
   'acoustic' in _binding[0])
ok('Ⓐ③ the threshold is a strict MAXIMUM over the four observables, so "binding" is measured',
   sum(1 for _n, v in _tab if v > _binding[1] - 1e-12) == 1)

# --------------------------------------------------------------------------------------------
# Ⓑ CONTROL (1) -- THE TOWER'S SPECTRUM, reproduced TWO WAYS from the corpus
# --------------------------------------------------------------------------------------------
_two_ways = all(abs(_mod.mu_sq_of_n(n) - _mod.mu_sq_of_m(n + 1)) < 1e-12 for n in range(2, 60))
ok('Ⓑ① mu^2 = n(n+2) and mu^2 = m^2-1 with m = n+1 agree on every label from 2 to 59 -- the two '
   'spellings the corpus uses at l.389 and l.488 are the same spectrum', _two_ways)
ok('Ⓑ② the lowest mode is n = 2 with mu^2 = 8, so mu_2 = 2.828427',
   _mod.N_MIN == 2 and abs(_mod.mu_sq_of_n(2) - 8.0) < 1e-12
   and abs(math.sqrt(_mod.mu_sq_of_n(2)) - 2.828427) < 1e-5)
ok('Ⓑ③ the degeneracy at the first label is d(m=3) = 10', abs(_mod.degeneracy(3) - 10.0) < 1e-12)
ok('Ⓑ④ and the tower begins at m = 3, which is why the regulator\'s simple pole at label 1 lies '
   'OUTSIDE it (l.1084) -- a structural fact and not a convenience',
   _mod.M_MIN == 3 and _mod.M_MIN > 1)

# --------------------------------------------------------------------------------------------
# Ⓒ THE REGULATOR'S TWO STATED VALUES, RECOMPUTED.  What the regulator IS decides whether a
#   cutoff energy exists to be found, so this is the row's hinge and not a flourish.
# --------------------------------------------------------------------------------------------
_m = sp.symbols('m', positive=True)
_ser = sp.expand(sp.series(2 * (_m ** 2 - 4) * sp.sqrt(_m ** 2 - 1), _m, sp.oo, 6).removeO())
_log_coeff = sp.nsimplify(_ser.coeff(_m, -1))
ok('Ⓒ① the zero-point summand d*mu = 2(m^2-4)sqrt(m^2-1) has 1/m coefficient EXACTLY 15/4, the '
   'corpus\'s logarithmic coefficient at l.492 -- reproduced symbolically from the spectrum, so '
   'this is a derivation of the corpus\'s number and not a restatement of it',
   _log_coeff == sp.Rational(15, 4))
ok('Ⓒ② and the leading terms are 2m^3 - 9m, so the expansion is the corpus\'s own',
   sp.nsimplify(_ser.coeff(_m, 3)) == 2 and sp.nsimplify(_ser.coeff(_m, 1)) == -9)
_z0 = sp.simplify(2 * ((sp.zeta(-2) - 1 - 2 ** 2) - 4 * (sp.zeta(0) - 1 - 1)))
ok('Ⓒ③ the spectral zeta at the origin, the frequency entering as unity (l.490), is '
   'zeta(0) = 2[zeta_H(-2,3) - 4 zeta_H(0,3)] = 10 EXACTLY -- the corpus\'s value at l.489, and a '
   'functional of the degeneracy alone exactly as it says', _z0 == 10)
ok('Ⓒ④ and 10 is also d(m=3), which is a COINCIDENCE of this spectrum and not the reason -- noted '
   'so the agreement in Ⓒ③ is not read as circular: the zeta is a regularised sum over ALL labels '
   'and happens to equal the first degeneracy',
   abs(_mod.degeneracy(3) - 10.0) < 1e-12 and _z0 == 10)

# --------------------------------------------------------------------------------------------
# Ⓓ AND THE SCALE FACTOR FACTORS OUT -- so the regularised sum carries NO ENERGY SCALE
# --------------------------------------------------------------------------------------------
_sums = []
for _inv in (1e-33, 1.0, 1e9):
    _sums.append(sum(_mod.degeneracy(k) * math.sqrt(_mod.mu_sq_of_m(k)) * _inv
                     for k in range(_mod.M_MIN, 41)))
_ratios = [_sums[1] / _sums[0], _sums[2] / _sums[1]]
ok('Ⓓ① the summand is exactly proportional to 1/a: the partial sum scales by 1e33 and 1e9 when '
   '1/a does, to 10 significant figures -- so `a` factors out identically (l.493) and this is '
   'MEASURED rather than quoted',
   abs(_ratios[0] - 1e33) < 1e33 * 1e-10 and abs(_ratios[1] - 1e9) < 1e9 * 1e-10)
ok('Ⓓ② ⇒ so the construction\'s regulated OUTPUT is a pure number -- 15/4, 10, and the rational '
   '-4/3 it returns (l.1090).  ** A quantity with no scale in it cannot name an energy at which it '
   'is used, which is why this row\'s answer about the cutoff is a statement about ABSENCE. **',
   _log_coeff == sp.Rational(15, 4) and _z0 == 10)

# --------------------------------------------------------------------------------------------
# Ⓔ THE ORDER'S QUESTION -- THE LOWEST ENERGY OF USE, and the margin
# --------------------------------------------------------------------------------------------
_h0 = _mod.H0_EV
ok('Ⓔ① H0 as an energy is 1.44e-33 eV, carried from r7629 rather than retyped',
   abs(_h0 * 1e33 - 1.44) < 0.002)
_w2 = _mod.omega(2, _h0)
ok('Ⓔ② the lowest mode\'s physical energy is omega_2 = sqrt(8)/a = 4.073e-33 eV at 1/a = H0 -- '
   'its mantissa recomputed from mu_2 and H0 and not read off the line',
   abs(_w2 * 1e33 - 4.073) < 0.002)
_orders = math.log10(_binding[1] / _w2)
ok('Ⓔ③ which is 33.31 orders of magnitude BELOW the 8.345 eV threshold',
   abs(_orders - 33.31) < 0.005)
_spread = [math.log10(_binding[1] / _mod.omega(2, f * _h0)) for f in (math.sqrt(0.7), 1.0, 10.0)]
ok('Ⓔ④ and the conclusion survives a DECADE of uncertainty in 1/a: across 1/a from H0*sqrt(0.7) '
   'to 10*H0 the margin runs %.2f to %.2f orders, never approaching zero -- which is why the row '
   'reports orders of magnitude and not three figures' % (min(_spread), max(_spread)),
   min(_spread) > 32.0 and max(_spread) < 34.0)
ok('Ⓔ⑤ ⇒ so the lowest use lies BELOW the threshold and the exit does NOT fire on this route',
   _w2 < _binding[1])
ok('Ⓔ⑥ the computation states that in those terms', 'THE EXIT DOES NOT FIRE ON THIS ROUTE' in out)

# --------------------------------------------------------------------------------------------
# Ⓕ CONTROL (2) -- BOTH DIRECTIONS ASKED.  The sum's terms DO reach above the threshold, and the
#   label at which they do is the number worth having.
# --------------------------------------------------------------------------------------------
_target = _binding[1] / _h0
_n_at = -1.0 + math.sqrt(1.0 + _target * _target)
ok('Ⓕ① the label at which a mode\'s own energy first reaches the threshold is n ~ 5.795e33 -- '
   'solved in CLOSED FORM from n > -1 + sqrt(1 + (Lambda* a)^2), because a search bounded at 1e7 '
   'returned None and crashed the first draft: the needed label is of order 1e33, so that was not '
   'a near miss but the wrong KIND of instrument',
   abs(_n_at * 1e-33 - 5.795) < 0.002)
ok('Ⓕ② and that closed form AGREES with the frequency it is supposed to invert: omega at that '
   'label returns the threshold itself, so the inversion is checked rather than trusted',
   abs(_mod.omega(_n_at, _h0) - _binding[1]) < 1e-9 * _binding[1])
ok('Ⓕ③ so the terms do reach above the threshold -- the row does NOT claim the tower is only ever '
   'used at low energy, which would be the convenient half of the truth', _n_at > 1.0)

# --------------------------------------------------------------------------------------------
# Ⓖ THE ASYMMETRY, GATED.  The registration named this as the reading most easily got wrong in
#   this row's favour, and these checks are what hold the distinction in place.
# --------------------------------------------------------------------------------------------
ok('Ⓖ① the row states that a low lowest-use is NOT evidence the cutoff is low',
   re.search(r'does not fire, and not because the cutoff is low', out, re.I) is not None)
ok('Ⓖ② and that an unbounded label range does NOT establish a cutoff above the threshold, because '
   'a continuation is the device that avoids committing to one',
   re.search(r'AND THAT DOES NOT FIRE THE EXIT', out) is not None
   and 'not a truncation' in out)
ok('Ⓖ③ ⇒ so NEITHER direction establishes a cutoff, and the row says so rather than banking the '
   'half that suits it', 'neither direction establishes a cutoff' in out)
ok('Ⓖ④ and the row declines to name the Planck scale, which the construction does not supply '
   'either -- the registration named reaching for it as inventing the datum the exit needs',
   'I do not name the Planck scale' in out)

# --------------------------------------------------------------------------------------------
# Ⓗ THE CORPUS'S TWO STATED VALUES, READ OUT OF THE PAPER AS NUMBERS AND COMPARED.
#
# ⌗ ** THIS GROUP HAS NOW BEEN WRONG TWICE, IN OPPOSITE DIRECTIONS, AND BOTH ARE RECORDED. **
#   ⑴ It first ran five `literal in canonical_time.tex` PRESENCE TESTS, which minted five quote-pin
#     keys (2744 -> 2749) on another seat's sentences -- the r7627 fault.
#   ⑵ Repairing that by DELETING the paper reads produced two new faults, both caught by CI gates
#     this seat's lean batch LEAN-SKIPS: `check_unread_figure` flagged a label attributing 15/4 and
#     zeta(0) = 10 to the paper while nothing read the paper (so the check would stay green if the
#     paper moved), and `check_prose_pins` flagged `len(re.findall(r'l\.\d{3,4}', out)) >= 6` as a
#     PIN ON A COUNT -- a count that holds while the thing it counts moves.
#   ⇒ ** So the repair for a hollow check was two more hollow checks. **  The right form is the one
#     check_unread_figure itself names: READ THE FIGURE FROM THE PAPER.  Each value below is parsed
#     out of canonical_time.tex AS A NUMBER and compared numerically to what the spectrum gives.
#     That is failable in both directions -- if 69 changes 15/4 in the paper this goes red, and if
#     the spectrum changes it goes red -- and a numeric extraction is not a literal-sentence
#     presence test, so it mints no quote-pin key.  ** Do not replace these with string tests, and
#     do not replace them with counts. **
# --------------------------------------------------------------------------------------------
_ct = ' '.join(open(os.path.join(CORPUS, 'canonical_time.tex'), errors='replace').read().split())

_m_zeta = re.search(r'spectral zeta at the origin is \$\\zeta\(0\)=(\d+)\$', _ct)
_paper_zeta = int(_m_zeta.group(1)) if _m_zeta else None
ok('Ⓗ① the paper\'s spectral zeta at the origin is READ OUT of canonical_time.tex as a number and '
   'equals the %s this receipt derives from the degeneracy -- so if that figure moves in the paper, '
   'this check goes red' % _z0,
   _paper_zeta is not None and sp.Integer(_paper_zeta) == _z0)

_m_log = re.search(r'logarithmic coefficient is \$\\tfrac\{(\d+)\}\{(\d+)\}\$', _ct)
_paper_log = sp.Rational(int(_m_log.group(1)), int(_m_log.group(2))) if _m_log else None
ok('Ⓗ② the paper\'s logarithmic coefficient is READ OUT as a rational and equals the %s this '
   'receipt derives from d*mu\'s large-label expansion' % _log_coeff,
   _paper_log is not None and _paper_log == _log_coeff)

# the paper prints the whole expansion; read its leading coefficients too, so the agreement is not
# resting on one number that could coincide
_m_exp = re.search(r'd\\,\\mu=(\d+)m\^\{3\}-(\d+)m\+\\tfrac\{(\d+)\}\{(\d+)\}m\^\{-1\}', _ct)
if _m_exp:
    _lead, _lin = int(_m_exp.group(1)), int(_m_exp.group(2))
    _lead_ok = (sp.nsimplify(_ser.coeff(_m, 3)) == _lead
                and sp.nsimplify(_ser.coeff(_m, 1)) == -_lin
                and sp.Rational(int(_m_exp.group(3)), int(_m_exp.group(4))) == _log_coeff)
else:
    _lead, _lin, _lead_ok = None, None, False
ok('Ⓗ③ and the paper\'s WHOLE printed expansion is read and matched term by term -- leading %s m^3, '
   'linear -%s m, and the 1/m term -- so the agreement rests on three coefficients and not on one '
   'number that might coincide' % (_lead, _lin), _lead_ok)

ok('Ⓗ④ the row names the open frontier -- the completion of the ultraviolet definition of the mode '
   'sums -- as the place a cutoff would enter, rather than supplying one',
   'COMPLETION of the ultraviolet definition of the mode sums' in out)

# --------------------------------------------------------------------------------------------
# Ⓘ FAILABILITY -- every pinned figure must FAIL its comparison when the value moves
# --------------------------------------------------------------------------------------------
_probes = [
    ('the threshold', abs(_binding[1] * 1.001 - 8.345) < 0.002),
    ('mu_2', abs(math.sqrt(_mod.mu_sq_of_n(2)) * 1.01 - 2.828427) < 1e-5),
    ('H0', abs(_h0 * 1.01 * 1e33 - 1.44) < 0.002),
    ('omega_2', abs(_w2 * 1.001 * 1e33 - 4.073) < 0.002),
    ('the margin', abs(_orders * 1.001 - 33.31) < 0.005),
    ('the label', abs(_n_at * 1.001 * 1e-33 - 5.795) < 0.002),
]
_alive = [n for n, c in _probes if c]
ok('Ⓘ① each pinned figure FAILS its own comparison under a 0.1-1%% perturbation (%s)'
   % (','.join(_alive) or 'all failed as they must'), not _alive)
# ⌗ ** THE FIRST VERSION OF Ⓘ② ENDED `nsimplify(_log_coeff + Rational(1,1000)) != Rational(15,4)`,
#   which is constant arithmetic -- 15/4 + 1/1000 differs from 15/4 for every operator in the
#   world. **  That is the r7627 hollow-assertion class and the same fault Ⓘ② of part ① carried.
#   The exact values are instead shown FAILABLE by perturbing the SPECTRUM they come from: move the
#   degeneracy's constant by one and both stated values must move.  ** Do not put the literal
#   arithmetic back. **
_m2 = sp.symbols('m', positive=True)
_ser_bad = sp.expand(sp.series(2 * (_m2 ** 2 - 5) * sp.sqrt(_m2 ** 2 - 1), _m2, sp.oo, 6).removeO())
_log_bad = sp.nsimplify(_ser_bad.coeff(_m2, -1))
_z0_bad = sp.simplify(2 * ((sp.zeta(-2) - 1 - 2 ** 2) - 5 * (sp.zeta(0) - 1 - 1)))
ok('Ⓘ② the two EXACT values are compared symbolically, and both MOVE when the spectrum they come '
   'from moves: with the degeneracy 2(m^2-5) instead of 2(m^2-4) the logarithmic coefficient '
   'becomes %s rather than 15/4 and the zeta becomes %s rather than 10 -- so neither is an '
   'identity that would hold for any tower' % (_log_bad, _z0_bad),
   _log_coeff == sp.Rational(15, 4) and _z0 == 10
   and _log_bad != sp.Rational(15, 4) and _z0_bad != 10)

# --------------------------------------------------------------------------------------------
print()
print('=' * 96)
print('  r7631+cc66 (2) -- P10: the tower is used 33 orders below 8.345 eV, and the regulator is a')
print('  spectral zeta with no cutoff parameter at all')
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
print('  ⇒ The lowest energy at which the corpus uses the interacting tower is omega_2 = sqrt(8)/a')
print('    ~ 4.07e-33 eV, about 33.3 orders of magnitude BELOW PO-89\'s 8.345 eV threshold.  So the')
print('    order\'s firing condition is MISSED and PO-89 does not close as a stated limit by it.')
print('  ⇒ And the stronger finding: the construction\'s regulator is a SPECTRAL ZETA -- zeta(0) = 10')
print('    exactly, the logarithmic coefficient 15/4, the interacting sum returning the rational')
print('    -4/3 -- whose values are pure numbers and from which the scale factor factors out')
print('    identically.  ** The construction has no cutoff parameter, so the exit is not merely')
print('    unsatisfied: it is not addressable from inside the construction as it stands. **')
print('  ⇒ Nothing the construction contains bounds the cutoff.  What would is its own named open')
print('    frontier -- the COMPLETION of the ultraviolet definition of the mode sums.  A completion')
print('    that truncates rather than continues would carry a Lambda, and only then is there')
print('    something to compare to 8.345 eV.')
print()
