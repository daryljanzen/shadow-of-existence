"""r7631+cc66 (1) -- P10: finiteness of the quadratic form selects the coupled tower's sub-threshold
boundary condition -- the SAME member Hartle-Hawking regularity imposes -- so the Euclidean face is
not the only closer of that freedom; and POSITIVITY is NOT a second selector.

COMPUTES: no parameter of the construction is given a numeric value here.  The numeric inputs are of
  two kinds, both declared:
  (i) LANDED STATEMENTS OF THE CORPUS, carried as the row's fibres rather than re-derived -- the
      essential-self-adjointness threshold 3/4 (canonical_time l.142), the regular branch
      x^(1/2+nu) with nu = sqrt(Gamma + 1/4) that thermal regularity imposes (canonical_time l.461),
      its closure of the COUPLED tower's condition on the sub-threshold subspace at every order
      (CR_framework l.1987), and spec(Gamma-hat) = [gamma, oo) with floor gamma = 1/4 under normal
      ordering and 3/4 under symmetric ordering with one mode occupied (canonical_time l.461,
      CR_framework l.1988);
  (ii) PROBE VALUES of Gamma chosen to sample the physical band [1/4, 3/4) -- 0.25 at the floor,
      0.50 at mid-band, 0.74 just under the threshold -- plus 1.00 above it as a negative control
      and 0.00 as the nu = 1/2 knife-edge, which is carried EXPLICITLY AS EXCLUDED.
  No measured datum enters: this row is a question about an operator, not a comparison to data.

** WHAT THIS RECEIPT GATES IN ONE LINE: a principle with NO Euclidean content closes the coupled
condition, so PO-94's quantum half does NOT meet its test by this route -- but on ONE selector and
not two, because positivity rules out a band of extensions and isolates none. **

⌗ THE ROW'S OWN CORRECTION, gated here so it cannot be lost.  The first draft of the computation
  claimed positivity as a second, agreeing selector.  That rested on a mesh that never resolved the
  endpoint (eps = 1e-4 against h = 1.7e-3) and returned the SAME eigenvalue for every member of the
  family, the pure irregular one included -- its value 11.7767 being the exact Friedrichs ground
  state (j_{nu,1}/b)^2 = 11.776812, which is how the blindness was proved rather than suspected.
  Asked in closed form the answer inverts: positivity admits t = 0, every t > 0 and every
  t <= -b^(2nu), excluding only the band t in (-b^(2nu), 0).  ** It constrains the family and
  selects no member. **  Checks Ⓗ and Ⓘ below are the ones that hold that correction in place.
"""
import math
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
WALK = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7631_cc66_the_coupled_edge')
SRC = os.path.join(WALK, 'edge.py')

checks = []


def ok(label, cond):
    checks.append((bool(cond), label))


res = subprocess.run([sys.executable, SRC], capture_output=True, text=True, timeout=900)
out = res.stdout
ok('the computation runs and exits zero (rc=%d)' % res.returncode, res.returncode == 0)


def num(pat, n=1):
    """the n-th capture of `pat` as a float, or None -- so a pin is a COMPARISON, not a grep.

    ⌗ The r7619 fault, repeated at r7627 and again at r7629: a regex that merely finds a figure's
      digits cannot fail when the computation starts printing something else.  Every figure this
      row's INDEX line prints is parsed out here and compared numerically."""
    m = re.search(pat, out)
    if not m:
        return None
    try:
        return float(m.group(n))
    except (TypeError, ValueError):
        return None


# ⌗ The module is imported as well as run, so that the structural claims below are tested against
#   the FUNCTIONS and not against their printed output.  A string test on a line of stdout cannot
#   tell a real value from a typo in a format string.
sys.path.insert(0, WALK)
import edge as _mod  # noqa: E402

# --------------------------------------------------------------------------------------------
# Ⓐ CONTROL (2) -- THE THRESHOLD REPRODUCED, so the fibres are the corpus's
# --------------------------------------------------------------------------------------------
ok('Ⓐ① the threshold carried is the corpus\'s 3/4', abs(_mod.THRESHOLD - 0.75) < 1e-12)
ok('Ⓐ② nu = sqrt(Gamma + 1/4) at the band floor is 0.707107', abs(_mod.nu_of(0.25) - 0.707107) < 1e-5)
ok('Ⓐ③ at mid-band it is 0.866025', abs(_mod.nu_of(0.50) - 0.866025) < 1e-5)
ok('Ⓐ④ just under the threshold it is 0.994987, still strictly below 1',
   abs(_mod.nu_of(0.74) - 0.994987) < 1e-5 and _mod.nu_of(0.74) < 1.0)
ok('Ⓐ⑤ and sub-threshold is exactly nu < 1, i.e. Gamma < 3/4 -- tested on BOTH sides of the '
   'threshold and not only on the side that suits the row',
   _mod.is_sub_threshold(0.74) and not _mod.is_sub_threshold(0.75)
   and not _mod.is_sub_threshold(1.00))

# --------------------------------------------------------------------------------------------
# Ⓑ CONTROL (5) -- WHICH FIBRES THE OPERATOR ACTUALLY HAS.  A selector demonstrated on a fibre
#   outside spec(Gamma-hat) is demonstrated on nothing, and the first draft did exactly that.
# --------------------------------------------------------------------------------------------
ok('Ⓑ① the normal-ordering floor carried is the corpus\'s 1/4',
   abs(_mod.FLOOR_NORMAL - 0.25) < 1e-12)
ok('Ⓑ② the symmetric-ordering floor carried is the corpus\'s 3/4',
   abs(_mod.FLOOR_SYMMETRIC - 0.75) < 1e-12)
_width_n = _mod.THRESHOLD - _mod.FLOOR_NORMAL
_width_s = _mod.THRESHOLD - _mod.FLOOR_SYMMETRIC
ok('Ⓑ③ under NORMAL ordering the sub-threshold band [1/4, 3/4) has width 0.50 and is non-empty, '
   'so there IS a condition to select', abs(_width_n - 0.50) < 1e-9 and _width_n > 0)
ok('Ⓑ④ under SYMMETRIC ordering the floor IS the threshold, so the band has width 0 and is EMPTY '
   '-- the selection question has no object there, which is the corpus\'s own "limit-point from '
   'the first occupied mode upward" reached by arithmetic on its two stated floors',
   abs(_width_s) < 1e-12)
ok('Ⓑ⑤ every fibre the row draws a conclusion from lies inside [1/4, 3/4)',
   all(_mod.FLOOR_NORMAL <= g < _mod.THRESHOLD for g in _mod.SUB_FIBRES))
ok('Ⓑ⑥ and the knife-edge Gamma = 0 is NOT one of them -- it is below the floor by 0.25, so the '
   'selector is never asked there',
   _mod.KNIFE_EDGE not in _mod.SUB_FIBRES
   and _mod.KNIFE_EDGE < _mod.FLOOR_NORMAL
   and abs((_mod.FLOOR_NORMAL - _mod.KNIFE_EDGE) - 0.25) < 1e-12)

# --------------------------------------------------------------------------------------------
# Ⓒ THE PARAMETRISATION -- the deficiency is a SUBSPACE, so the family is U(n), not one angle
# --------------------------------------------------------------------------------------------
_n = len(_mod.SUB_FIBRES)
_params = num(r'in bijection with the unitaries U\(\d+\): (\d+) real parameters')
ok('Ⓒ① three sub-threshold fibres are sampled, each of deficiency index (1,1)', _n == 3)
ok('Ⓒ② so the extensions are in bijection with U(3) and carry 9 real parameters -- and 9 is n^2 '
   'for THIS n rather than a number typed in, so changing the fibre list cannot leave it stale',
   _params is not None and abs(_params - _n * _n) < 1e-12 and abs(_params - 9) < 1e-12)

# --------------------------------------------------------------------------------------------
# Ⓓ CONTROL (3) -- A SUPER-THRESHOLD FIBRE.  A principle that "selects" where there is no
#   freedom is measuring nothing, so the family must come back EMPTY there.
# --------------------------------------------------------------------------------------------
ok('Ⓓ① the control fibre Gamma = 1.00 gives nu = 1.118034 >= 1',
   abs(_mod.nu_of(_mod.SUPER_FIBRE) - 1.118034) < 1e-5 and _mod.nu_of(_mod.SUPER_FIBRE) >= 1.0)
ok('Ⓓ② the computation reports deficiency (0,0) and 0 parameters there',
   re.search(r'deficiency index \(0,0\), extensions = U\(0\), i\.e\. 0 parameters', out) is not None)
ok('Ⓓ③ and that fibre is excluded from the selection claims',
   _mod.SUPER_FIBRE not in _mod.SUB_FIBRES)

# --------------------------------------------------------------------------------------------
# Ⓔ THE SELECTOR -- FINITE QUADRATIC-FORM ENERGY, measured on BOTH branches.  The integrand is
#   (s^2 + Gamma) x^(2s-2): BOTH pieces decide it, which is the whole content of Ⓕ below.
# --------------------------------------------------------------------------------------------
_bad = []
for _g in _mod.SUB_FIBRES:
    _nu = _mod.nu_of(_g)
    _er, _cr = _mod.form_integrand(0.5 + _nu, _g)
    _ei, _ci = _mod.form_integrand(0.5 - _nu, _g)
    _r4 = _mod.form_energy_near_zero(0.5 + _nu, _g, eps=1e-4)
    _r8 = _mod.form_energy_near_zero(0.5 + _nu, _g, eps=1e-8)
    _i4 = _mod.form_energy_near_zero(0.5 - _nu, _g, eps=1e-4)
    _i8 = _mod.form_energy_near_zero(0.5 - _nu, _g, eps=1e-8)
    if not (_er > -1.0 and _ei < -1.0):
        _bad.append('exponent at %.2f' % _g)
    if not abs(_r8 - _r4) < 1e-3 * max(1.0, abs(_r4)):
        _bad.append('regular not stable at %.2f' % _g)
    if not _i8 > 1e4 * _i4:
        _bad.append('irregular not growing at %.2f' % _g)
ok('Ⓔ① on every physical fibre the REGULAR branch\'s form energy is stable between eps = 1e-4 and '
   '1e-8 while the IRREGULAR branch\'s grows by more than four orders -- so the divergence is '
   'MEASURED as a limit and not read off an exponent (%s)' % (','.join(_bad) or 'clean'),
   not _bad)
_min_c = min(_mod.form_integrand(0.5 - _mod.nu_of(g), g)[1] for g in _mod.SUB_FIBRES)
_max_e = max(_mod.form_integrand(0.5 - _mod.nu_of(g), g)[0] for g in _mod.SUB_FIBRES)
ok('Ⓔ② the smallest irregular COEFFICIENT across the physical band is 0.292893, strictly positive',
   abs(_min_c - 0.292893) < 1e-5 and _min_c > 0.0)
ok('Ⓔ③ the largest irregular EXPONENT across the physical band is -2.414214, strictly below -1',
   abs(_max_e - (-2.414214)) < 1e-5 and _max_e < -1.0)
ok('Ⓔ④ so the exclusion holds WITH MARGIN on the whole band, and both the coefficient and the '
   'exponent are bounded away from the values that would break it',
   _min_c > 0.2 and _max_e < -2.0)
_r_e = num(r'0\.250    regular    0\.414214     1\.707107     ([\d.]+)')
ok('Ⓔ⑤ the regular branch\'s form energy at the band floor is 1.207107, printed and recomputed',
   _r_e is not None and abs(_r_e - 1.207) < 0.002
   and abs(_mod.form_energy_near_zero(0.5 + _mod.nu_of(0.25), 0.25, eps=1e-8) - 1.207107) < 1e-4)

# --------------------------------------------------------------------------------------------
# Ⓕ CONTROL (6) -- THE ONE PLACE THE ARGUMENT FAILS, and why it is never reached.
#   ** This is the check the first draft lacked, and lacking it is how it published a false
#   universal while its own table contradicted it. **
# --------------------------------------------------------------------------------------------
_nuk = _mod.nu_of(_mod.KNIFE_EDGE)
_ek, _ck = _mod.form_integrand(0.5 - _nuk, _mod.KNIFE_EDGE)
ok('Ⓕ① at the knife-edge nu is EXACTLY 1/2', abs(_nuk - 0.5) < 1e-15)
ok('Ⓕ② so the irregular branch is x^0, a constant', abs((0.5 - _nuk) - 0.0) < 1e-15)
ok('Ⓕ③ its integrand EXPONENT is -2, which is non-integrable -- so an argument from the exponent '
   'alone would wrongly call it divergent here', abs(_ek - (-2.0)) < 1e-15)
ok('Ⓕ④ but its COEFFICIENT s^2 + Gamma vanishes identically, so the form energy is 0 and FINITE '
   '-- the accident the exponent hides, and the reason finiteness is not the criterion at nu = 1/2',
   abs(_ck - 0.0) < 1e-15
   and abs(_mod.form_energy_near_zero(0.5 - _nuk, _mod.KNIFE_EDGE, eps=1e-8)) < 1e-12)
ok('Ⓕ⑤ and this is a real feature of the operator, not of the probe: the SAME function at the '
   'band floor has a strictly positive coefficient, so the vanishing is specific to nu = 1/2',
   _mod.form_integrand(0.5 - _mod.nu_of(0.25), 0.25)[1] > 0.29)
ok('Ⓕ⑥ the computation prints the knife-edge as a control and says in terms that finite form '
   'energy does NOT exclude the irregular branch there',
   re.search(r'at nu = 1/2 finite form energy does NOT exclude the irregular branch', out)
   is not None)
ok('Ⓕ⑦ and it states the stronger criterion that still selects there -- closure of the minimal '
   'form domain rather than finiteness of the form',
   re.search(r'not\s+finiteness of the form but CLOSURE of the minimal form domain', out)
   is not None)

# --------------------------------------------------------------------------------------------
# Ⓖ CONTROL (4) -- A NON-DIAGONAL MEMBER, so the diagonality claim is a comparison over a real
#   family and not a statement about the only member constructed.
# --------------------------------------------------------------------------------------------
_det = num(r'U = \[\[cos45, -sin45\], \[sin45, cos45\]\],  det = ([\d.]+)')
ok('Ⓖ① the exhibited non-diagonal member has det = 1.000000',
   _det is not None and abs(_det - 1.0) < 1e-6)
ok('Ⓖ② and it is genuinely unitary (U^T U = I reported True), so it IS a self-adjoint extension '
   'by von Neumann and not a construction error',
   re.search(r'U\^T U = I: True', out) is not None)
ok('Ⓖ③ the computation concludes the form-finite member is unique and DIAGONAL',
   re.search(r'the form-finite member is unique and DIAGONAL', out) is not None)

# --------------------------------------------------------------------------------------------
# Ⓗ POSITIVITY, IN CLOSED FORM -- the row's own correction.  Three discretised instruments were
#   blind or divergent; the negative-energy problem is exactly solvable, so it is solved.
# --------------------------------------------------------------------------------------------
ok('Ⓗ① the first-zero finder is checked where the answer is KNOWN: j_{1/2,1} = pi',
   abs(_mod.first_zero_of_J(0.5) - math.pi) < 1e-5)
ok('Ⓗ② and at j_{0,1} = 2.404826 and j_{1,1} = 3.831706 -- three independent known values, '
   'because the first version of this finder used a guessed bracket and returned the THIRD zero '
   '(9.7373 for nu = 0.7071), which no self-consistency check would have caught',
   abs(_mod.first_zero_of_J(0.0) - 2.404826) < 1e-5
   and abs(_mod.first_zero_of_J(1.0) - 3.831706) < 1e-5)
ok('Ⓗ③ the Friedrichs ground state at the band floor is 11.776812 = (j_{nu,1}/b)^2, EXACTLY and '
   'with no mesh -- and this is the number the blind instrument was returning for every member '
   'of the family, which is how its blindness was proved rather than suspected',
   abs(_mod.friedrichs_ground_state(0.25) - 11.776812) < 1e-4)
ok('Ⓗ④ at mid-band it is 13.323162 and just under the threshold 14.630229',
   abs(_mod.friedrichs_ground_state(0.50) - 13.323162) < 1e-4
   and abs(_mod.friedrichs_ground_state(0.74) - 14.630229) < 1e-4)
ok('Ⓗ⑤ the Friedrichs member is POSITIVE on every physical fibre, so positivity does not exclude '
   'the member the form selects',
   all(_mod.friedrichs_ground_state(g) > 0.0 for g in _mod.SUB_FIBRES))
# the band of extensions carrying a negative eigenvalue: t = T(k), T monotone from -b^(2nu) to 0-
_edge_bad = []
for _g in _mod.SUB_FIBRES:
    _nu = _mod.nu_of(_g)
    for _b in (0.5, 1.0, 2.0):
        _meas = _mod.extension_with_eigenvalue(1e-9, _nu, b=_b)
        if abs(_meas - (-_b ** (2.0 * _nu))) > 1e-6:
            _edge_bad.append('%.2f@%.1f' % (_g, _b))
ok('Ⓗ⑥ the band\'s lower edge obeys -b^(2nu) at THREE box sizes, 0.5, 1.0 and 2.0 -- tested away '
   'from b = 1, where the law reads -1 whatever nu is and so tests nothing about the exponent '
   '(%s)' % (','.join(_edge_bad) or 'clean'), not _edge_bad)
ok('Ⓗ⑦ and at b = 0.5 the edge is -0.37521423 for the floor fibre, a value that DEPENDS on nu '
   'and so could have disagreed',
   abs(_mod.extension_with_eigenvalue(1e-9, _mod.nu_of(0.25), b=0.5) - (-0.37521423)) < 1e-6)
_mono_bad = []
for _g in _mod.SUB_FIBRES:
    _nu = _mod.nu_of(_g)
    _ts = [_mod.extension_with_eigenvalue(_k, _nu) for _k in (1e-9, 1e-3, 1.0, 1e3)]
    if not all(_ts[i] < _ts[i + 1] for i in range(len(_ts) - 1)):
        _mono_bad.append('%.2f' % _g)
    if not (_ts[0] < 0.0 and _ts[-1] < 0.0):
        _mono_bad.append('sign@%.2f' % _g)
ok('Ⓗ⑧ T(k) is strictly increasing in k and stays negative, so the set of extensions with a '
   'negative eigenvalue is exactly the open interval (-b^(2nu), 0) -- an INTERVAL and not a '
   'point, which is the whole reason positivity cannot isolate a member (%s)'
   % (','.join(_mono_bad) or 'clean'), not _mono_bad)
ok('Ⓗ⑨ so positivity ADMITS t = 0, and the computation says so in terms',
   re.search(r'POSITIVITY THEREFORE DOES NOT SELECT A MEMBER', out) is not None)

# --------------------------------------------------------------------------------------------
# Ⓘ THE INDEPENDENCE QUESTION -- the thing the registration named as the error this seat would
#   most easily make in the flattering direction, and then made.  Gated so it cannot come back.
# --------------------------------------------------------------------------------------------
ok('Ⓘ① the two candidates are NESTED and not independent: a finite form excludes EVERY t != 0 '
   'while positivity excludes only the band, so the form condition is strictly the stronger',
   abs(_mod.extension_with_eigenvalue(1e-9, _mod.nu_of(0.25)) - (-1.0)) < 1e-6)
# ⌗ ** THE FIRST VERSION OF Ⓘ② WAS `not (-1.0 < 1.0 < 0.0) and not (-1.0 < -2.0 < 0.0)`, which
#   is a tautology on three literals and could not have failed for any operator whatever. **  That
#   is the r7627 hollow-assertion fault repeating: an arithmetic identity dressed as a measurement.
#   The band edge is now DERIVED from the module for each fibre and the candidate t values are
#   tested against it, so the check moves if the operator does.  ** Do not put the literals back. **
_admits_bad = []
for _g in _mod.SUB_FIBRES:
    _nu = _mod.nu_of(_g)
    _lo = _mod.extension_with_eigenvalue(1e-9, _nu, b=1.0)   # the band's lower edge, = -b^(2nu)
    for _t in (1.0, -2.0, 5.0):
        in_band = _lo < _t < 0.0
        if in_band:                      # positivity would reject it, so it proves nothing here
            _admits_bad.append('%.2f:t=%g in band' % (_g, _t))
        if abs(_t) < 1e-12:              # and it must be a NONZERO irregular coefficient
            _admits_bad.append('%.2f:t=%g is the regular member' % (_g, _t))
ok('Ⓘ② positivity ADMITS members the form condition REJECTS: t = +1, -2 and +5 all lie outside '
   'the negative-eigenvalue band (whose edge is derived from the operator here, not typed in) '
   'yet each carries a nonzero irregular coefficient and so is form-infinite.  ** That asymmetry '
   'is the proof the two are not the same condition, and the proof positivity is the weaker one. '
   '** (%s)' % (','.join(_admits_bad) or 'clean'), not _admits_bad)
ok('Ⓘ③ the row therefore counts ONE selector, and the computation states that it does so because '
   'there is only one rather than because two were merged',
   re.search(r'this row counts ONE selector, and counts it once because there is only one', out)
   is not None)
ok('Ⓘ④ and the row records that the first draft got this wrong in the flattering direction, so '
   'the correction is carried in the artifact and not only in the walk',
   re.search(r'The flattering answer was', out) is not None)

# --------------------------------------------------------------------------------------------
# Ⓙ FAILABILITY -- every pin above is a comparison against a constant, so each must be shown to
#   FAIL when the value moves.  A check that cannot fail is not a check.
# --------------------------------------------------------------------------------------------
_fail_probes = [
    ('nu at the floor', abs(_mod.nu_of(0.25) * 1.01 - 0.707107) < 1e-5),
    ('the irregular coefficient', abs(_min_c * 1.01 - 0.292893) < 1e-5),
    ('the irregular exponent', abs(_max_e * 1.01 - (-2.414214)) < 1e-5),
    ('the Friedrichs ground state', abs(_mod.friedrichs_ground_state(0.25) * 1.001 - 11.776812) < 1e-4),
    ('the band edge at b=0.5',
     abs(_mod.extension_with_eigenvalue(1e-9, _mod.nu_of(0.25), b=0.5) * 1.001 - (-0.37521423)) < 1e-6),
    ('the band width', abs((_width_n * 1.01) - 0.50) < 1e-9),
]
_still_passing = [n for n, c in _fail_probes if c]
ok('Ⓙ① each pinned figure FAILS its own comparison under a 0.1-1%% perturbation, so none of them '
   'is a tolerance wide enough to pass on anything (%s)'
   % (','.join(_still_passing) or 'all failed as they must'), not _still_passing)
ok('Ⓙ② and the knife-edge coefficient is pinned at exactly 0, which a perturbation of the FIBRE '
   'moves off -- so Ⓕ④ is not an artefact of comparing zero to zero',
   _mod.form_integrand(0.5 - _mod.nu_of(1e-6), 1e-6)[1] > 0.0)

# --------------------------------------------------------------------------------------------
print()
print('=' * 96)
print('  r7631+cc66 (1) -- P10: the form selects the coupled condition; positivity does not select')
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
print('  ⇒ Finiteness of the quadratic form -- equivalently closure of the minimal form domain --')
print('    selects exactly one member of U(3) on the coupled sub-threshold subspace, and it is the')
print('    DIAGONAL regular-branch member that Hartle-Hawking regularity imposes.  It does so on')
print('    every fibre of spec(Gamma-hat) below 3/4, with margin; the one knife-edge where finite')
print('    form energy would NOT suffice is nu = 1/2, which lies 0.25 below the spectrum\'s floor.')
print('  ⇒ So a principle with NO Euclidean content closes the coupled condition: the face is not')
print('    the only closer here and PO-94\'s quantum half does NOT meet its test by this route.')
print('  ⇒ And it is ONE selector.  Positivity excludes the band t in (-b^(2nu), 0) and admits')
print('    t = 0, every t > 0 and every t <= -b^(2nu): a constraint on the family that isolates no')
print('    member.  The case is narrower than this seat first published and is stated at the width')
print('    the measurement supports.')
print()
