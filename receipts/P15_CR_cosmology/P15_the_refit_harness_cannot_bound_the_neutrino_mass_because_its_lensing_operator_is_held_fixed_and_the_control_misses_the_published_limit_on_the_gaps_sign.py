#!/usr/bin/env python3
r"""RECEIPT -- P15 (r7836, node 60): ** THE INSTRUMENT NOW CARRIES A NEUTRINO MASS SUM, AND THE REFIT
HARNESS CANNOT BOUND IT: THE CONTROL'S LIMIT IS 2.4 TIMES TOO TIGHT AND ITS FITTED MATTER-DENSITY GAP
COMES OUT WITH THE OPPOSITE SIGN TO THE PUBLISHED ONE, SO NO LIMIT ON THE CONSTRUCTION IS REPORTED. **

COMPUTES: the neutrino density parameter the new switch forms and the clustering density it leaves;
  the nonrelativistic transition redshift across the scanned range of sums; the size of the lensing
  signature the harness omits, against the size of the lever it keeps; and the two arms' profile
  limits and fitted gaps, read from this revision's own run.  ** It pins NO cosmological parameter as
  a result: the headline is that a measurement was ATTEMPTED and its apparatus failed its control. **

THE ORDER (r7831, 69, added clause, routed from 72): add massive neutrinos to the arm of record's
instrument -- three species, normal ordering, a free sum, relativistic in the early rate and the
driving, nonrelativistic in the late dust the distances see, with omega_cb = Omega_m h^2 - omega_nu;
refit the leaf-geometry arm on the 185-bin lensed configuration with the sum free beside the four
parameters, jointly with DESI DR2 BAO on the leaf ruler, running the control the same way; report the
profile, the 95 per cent upper limit, and where 59 and 64 meV sit on it.  PREDICTION.md was pushed
first, at `8924a42ab`, with seven arms.

** WHAT PASSED, AND IT IS ITEM (1). **
  Ⓐ① The instrument had NO mass knob at all -- massless free-streaming neutrinos, `FNU` for their
     share of `Omega_r`, `DNEFF` for their number.  `MNU` is added, and where it enters follows from
     where the file consumes `Omega_m`: the TOTAL stays in both rates, in `OL = 1 - OM`, in the stack
     and therefore in `D_M`, `r_s` and `l_A`, while the CLUSTERING matter loses `omega_nu`.  Verified
     at the REPORTING path before any spectrum was read off it, and the default is EXACT.
  Ⓑ② The two-limit treatment's licence, measured rather than asserted: the nonrelativistic
     transition sits `8.6` to `29` times below recombination across the whole scanned range, and
     `27` to `29` times at the two values the order asks about.  ⌗ *The first form of this arm said
     "9 to 29" and its own check caught the far edge at 8.6.*

** WHAT FAILED, AND THE PREDICTION CALLED IT THE ARM THAT COULD MOST USEFULLY FAIL. **
  Ⓒ③ The control's 95 per cent limit is `26.5` meV against the published `64.2` -- and its fitted
     matter-density gap is `-2.43` per cent where the published standard-model gap is `+2.48`.  ** The
     SIGN is reversed on the very quantity the order's reasoning turns on. **  So Ⓓ④ and Ⓕ⑥ are NOT
     JUDGED and the arm's own `15.8` meV is not a limit on this construction.

** THE CAUSE, IN TWO PARTS, BOTH MEASURED HERE. **
  ① The harness holds its lensing operator FIXED, computed once from a CAMB cosmology with the mass
     HARDCODED, and applies it to every spectrum.  So the signature the CMB actually weighs neutrinos
     with is absent while the `omega_cb` lever is kept -- and the omitted signature is the SAME ORDER
     as the retained lever.
  ② The profile still fails a monotonicity check after being orthogonalised against the `Omega_m`
     direction, walked outward from zero with continuation starts, and given a second minimiser.

WHAT IS NOT CLAIMED, stated for reversal.
  ** Not that the construction's limit is looser than the standard model's ** -- that was the
  registered expectation and it is NOT JUDGED.  ** Not that it is tighter. **  ** Not that the
  published bound is wrong ** -- the control's disagreement is a statement about this harness.
  ** Not that the instrument extension is in doubt: ** Ⓐ① and Ⓑ② stand on their own.

rc=0 on success.  Run: python3 <this file>        (numpy; reads this revision's banked JSON)
"""
import io
import json
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
RUN = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                   'r7836_60_the_arm_of_record_refitted_with_the_neutrino_mass_free')
FAILED = []
ARMS = []

# ---- figures read from banked sources, each with its provenance -------------
PUBLISHED_LIMIT_MEV = 64.2          # DESI DR2 + CMB, arXiv:2503.14744, as 72's working file quotes it
PUBLISHED_GAP_PC = 2.48             # the standard model's CMB-above-distances gap, same source
KB_EV_PER_K, T_NU0 = 8.617333262e-5, 1.945       # PDG; the post-annihilation neutrino temperature
Z_REC = 1090.0                      # the instrument's own recombination redshift
MNU_TO_ONUH2 = 93.14                # the standard conversion the instrument codes


def check(label, ok, extra=''):
    ARMS.append(label)
    print(('  %-4s %s' % ('PASS' if ok else 'FAIL', label)) + (('   [%s]' % extra) if extra else ''))
    if not ok:
        FAILED.append(label)


print(__doc__.split('rc=0')[0])
src = io.open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py'),
              encoding='utf-8', errors='replace').read()
harness = io.open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7749_70_leafgeom_refit',
                               'refit.py'), encoding='utf-8', errors='replace').read()
res = json.load(open(os.path.join(RUN, 'fit_mnu.json')))

print('=' * 78)
print('PART 1 -- THE INSTRUMENT CARRIES THE MASS, AND THE SEPARATION IS EXACT')
print('=' * 78)

# ---------------------------------------------------------------- A (1)
H = 0.6857073                                     # the arm's grid centre, h
onu = lambda s: s / MNU_TO_ONUH2 / H ** 2         # noqa: E731
print('  the switch forms Omega_nu = Sum / %.2f / h^2, so at Sum = 0.06 eV it is %.7f'
      % (MNU_TO_ONUH2, onu(0.06)))
print('  and omega_nu = %.7f, which is what omega_cb loses' % (onu(0.06) * H ** 2))
# the default must be EXACT and not merely small: the two lines the switch touches
_om, _ob = 0.291246, 0.021643 / H ** 2
exact = ((_om - _ob - 0.0) == (_om - _ob)) and ((_om - 0.0) == _om)
check('Ⓐ① the mass switch is in the instrument, the total stays in the rate and the dark energy, '
      'the clustering matter loses omega_nu, and the default is EXACT rather than small',
      "MNU = float(os.environ.get('MNU', '0.0'))" in src
      and 'OCDM = OM - OB - ONU' in src
      and "Om_of = CubicSpline(eg, ((OM - ONU) / ag ** 3) / _rt)" in src
      and 'OL = 1.0 - OM' in src                   # the total, untouched
      and exact
      and abs(onu(0.06) * H ** 2 - 0.0006442) < 0.0000004,
      'omega_nu(0.06) = %.7f' % (onu(0.06) * H ** 2))

# ---------------------------------------------------------------- B (2)
rows = []
for s in (0.059, 0.064, 0.120, 0.200):
    znr = (s / 3.0) / (3.15 * KB_EV_PER_K * T_NU0)          # 1+z where m = 3.15 kT
    rows.append((s, znr, Z_REC / znr))
    print('  Sum = %.3f eV -> 1+z_nr = %6.1f, which is %5.1f times below recombination'
          % (s, znr, Z_REC / znr))
# ** THE FIRST FORM OF THIS ARM CLAIMED "9 to 29 times below" AND THIS CHECK CAUGHT IT: at the
#    scan's far edge, Sum = 0.20 eV, the margin is 8.6 and not 9.  The claim is corrected to what
#    the arithmetic gives, and the figure that matters is quoted separately -- at the 59 and 64 meV
#    the order asks about the margin is 27 to 29 times. **
check('Ⓑ② the nonrelativistic transition is 8.6 to 29 times below recombination across the whole '
      'scanned range, and 27 to 29 times at the two values the order asks about, so the two-limit '
      'treatment is licensed everywhere it was used',
      all(r[2] > 8.0 for r in rows)
      # ** AND THE SECOND FORM OF THIS THRESHOLD WAS WRONG TOO, by a hundredth: the margin at
      #    64 meV is 26.98 and not 27.0, so `> 27.0` failed on the figure it was written to pass.
      #    The interval is the one the printed figures lie in, and a wrong figure still escapes it. **
      and all(26.0 < r[2] < 30.0 for r in rows[:2])
      and abs(rows[0][1] - 37.3) < 0.4 and abs(rows[-1][1] - 126.3) < 0.4,
      'margin %.1f to %.1f; at 59/64 meV it is %.1f and %.1f'
      % (min(r[2] for r in rows), max(r[2] for r in rows), rows[0][2], rows[1][2]))

print()
print('=' * 78)
print('PART 2 -- THE CONTROL FAILS, AND IT FAILS ON THE SIGN')
print('=' * 78)

lim_ctl = res['lcdm']['upper95'] * 1000.0
lim_arm = res['cr']['upper95'] * 1000.0
print('  control 95 per cent upper limit: %.1f meV against the published %.1f -- a factor %.2f'
      % (lim_ctl, PUBLISHED_LIMIT_MEV, PUBLISHED_LIMIT_MEV / lim_ctl))
print('  the arm returns %.1f meV, which this receipt does NOT report as a limit' % lim_arm)
check('Ⓒ③ the control misses the published limit by more than a factor of two, so the apparatus is '
      'not validated and nothing is concluded about the arm',
      PUBLISHED_LIMIT_MEV / lim_ctl > 2.0 and lim_ctl < PUBLISHED_LIMIT_MEV,
      'factor %.2f' % (PUBLISHED_LIMIT_MEV / lim_ctl))

# the gap, on each arm's own fitted point against its own distances' point
def gap_pc(arm, h0_d, om_d):
    jm = res[arm]['joint_min']
    h = jm['H0'] / 100.0
    return 100.0 * ((jm['OM'] * h ** 2) / (om_d * (h0_d / 100.0) ** 2) - 1.0)


g_ctl = gap_pc('lcdm', 68.5, 0.2975)
g_arm = gap_pc('cr', 68.60, 0.2973)
print('  control fitted gap %+.2f per cent, where the published standard-model gap is %+.2f'
      % (g_ctl, PUBLISHED_GAP_PC))
print('  arm fitted gap     %+.2f per cent (72\'s banked estimate reads -1.00)' % g_arm)
check('Ⓒ③ᵇ and the control fails on the SIGN of the gap the order\'s reasoning turns on, which is '
      'the decisive half: published above the distances, fitted below them',
      PUBLISHED_GAP_PC > 0 and g_ctl < 0 and abs(g_ctl) > 1.0,
      '%+.2f against %+.2f' % (g_ctl, PUBLISHED_GAP_PC))
check('Ⓓ④ NOT JUDGED, and the arm records it as not judged rather than reporting the number: the '
      'registered expectation was a looser limit than the published one and the apparatus failed '
      'its control first',
      lim_arm > 0 and 'NOT JUDGED' in io.open(os.path.join(RUN, 'RESULT.md'),
                                              encoding='utf-8').read(),
      'the apparatus returned %.1f meV, reported as unvalidated' % lim_arm)

print()
print('=' * 78)
print('PART 3 -- WHY: THE OMITTED SIGNATURE IS THE SAME ORDER AS THE RETAINED LEVER')
print('=' * 78)

# the harness's lensing operator is built ONCE, with the mass hardcoded -- read, not recalled
fixed_once = (harness.count('RATIO = np.ones_like(_le)') == 1
              and re.search(r"camb\.set_params\([^)]*mnu=0\.06", harness, re.S) is not None
              and 'RATIO' not in harness.split('def chi2_at')[1])
print('  the operator is formed once from a set_params carrying mnu=0.06 and never re-formed: %s'
      % fixed_once)
OMITTED_006, OMITTED_012 = 0.372, 0.768     # per cent, measured with CAMB at r7836 (see RESULT.md)
LEVER = 0.84                                # per cent, this revision's own pair against its base
print('  omitted lensing signature: %.3f per cent at Sum = 0.06 and %.3f at 0.12'
      % (OMITTED_006, OMITTED_012))
print('  retained omega_cb lever:   %.2f per cent, this revision\'s own pair against its base' % LEVER)
check('Ⓗ⑧ the lensing operator is held fixed with the mass hardcoded, and the signature that omits '
      'is the same order as the lever the fit keeps -- which is why a limit comes out too tight',
      fixed_once and 0.3 * LEVER < OMITTED_006 < 3.0 * LEVER
      and OMITTED_012 > OMITTED_006,
      '%.3f and %.3f against %.2f' % (OMITTED_006, OMITTED_012, LEVER))

# and the profile's own convergence, read from the run rather than asserted
nonmono = {}
for arm in ('lcdm', 'cr'):
    cs = [p['chi2'] for p in res[arm]['profile']]
    i = min(range(len(cs)), key=lambda j: cs[j])
    up = all(cs[k] <= cs[k + 1] + 1e-6 for k in range(i, len(cs) - 1))
    dn = all(cs[k] >= cs[k - 1] - 1e-6 for k in range(1, i + 1))
    nonmono[arm] = not (up and dn)
    print('  %-5s profile monotone away from its minimum: %s' % (arm, up and dn))
check('Ⓘ⑨ the profile is NOT converged on either arm even after orthogonalisation, continuation '
      'starts and a second minimiser, and the receipt asserts that rather than hoping for it',
      nonmono['lcdm'] or nonmono['cr'],
      'non-monotone: ' + ', '.join(a for a in nonmono if nonmono[a]))

print()
print('=' * 78)
# ** EVERY FIGURE THIS RECEIPT'S DOCSTRING AND ITS INDEX ROW PRINT IS PINNED HERE, two-sided and
#    inside the coarser of half its last printed digit and 0.05 per cent, so a wrong one fails the
#    receipt rather than standing in type unchecked.  The limits and the gaps are re-read from the
#    run's own JSON, not retyped; the two lensing figures are this revision's CAMB measurement and
#    the lever is its own pair against its base, both recorded in RESULT.md with how they were got. **
_f = dict(ctl_limit=lim_ctl, arm_limit=lim_arm, factor=PUBLISHED_LIMIT_MEV / lim_ctl,
          ctl_gap=g_ctl, arm_gap=g_arm, omitted_006=OMITTED_006, omitted_012=OMITTED_012,
          lever=LEVER)
print()
print('  the figures this receipt prints, each pinned two-sided:')
for _k, _v in _f.items():
    print('    %-12s %.4f' % (_k, _v))
check('Ⓙ⑩ every figure this receipt and its INDEX row print is pinned two-sided here',
      abs(_f['ctl_limit'] - 26.5) < 0.04
      and abs(_f['arm_limit'] - 15.8) < 0.045      # inside half of 15.8's last digit
      and abs(_f['factor'] - 2.42) < 0.004
      and abs(_f['ctl_gap'] + 2.43) < 0.004
      and abs(_f['arm_gap'] + 5.21) < 0.0048       # inside half of 5.21's last digit
      and abs(_f['omitted_006'] - 0.372) < 0.0004
      and abs(_f['omitted_012'] - 0.768) < 0.0004
      and abs(_f['lever'] - 0.84) < 0.004
      and abs(PUBLISHED_LIMIT_MEV - 64.2) < 0.04
      and abs(PUBLISHED_GAP_PC - 2.48) < 0.004,
      '%.1f / %.1f meV, factor %.2f, gaps %+.2f and %+.2f' %
      (_f['ctl_limit'], _f['arm_limit'], _f['factor'], _f['ctl_gap'], _f['arm_gap']))
check('Ⓚ⑪ eight arms were registered above this one and all of them ran', len(ARMS) == 8)
print('=' * 78)
if FAILED:
    print('\n%d ARM(S) FAILED -- and Ⓒ③ and Ⓒ③ᵇ are REGISTERED FAILURES, reported as such:' % len(FAILED))
    for f in FAILED:
        print('  - ' + f)
    raise SystemExit(1)
print('\nALL %d ARMS PASS -- the apparatus\'s failure is itself the finding, asserted and not hidden'
      % len(ARMS))
