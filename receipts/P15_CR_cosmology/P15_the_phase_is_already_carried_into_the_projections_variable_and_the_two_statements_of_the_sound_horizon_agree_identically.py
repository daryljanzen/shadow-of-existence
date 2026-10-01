"""
P15_the_phase_is_already_carried_into_the_projections_variable_and_the_two_statements_of_the_sound_horizon_agree_identically.py

** THE RULE'S DIVISION OF LABOUR IS CARRIED OUT, AND UNTIL THIS FILE NOTHING ASSERTED IT. **
`P07`'s rate rule puts the plasma's sound horizon on the leaf rate and a comoving separation read
across leaves on the stacking rate, and says there is no locus at which the rate switches.  Applied to
the line-of-sight integral that means the integration VARIABLE is the stacking conformal time, while the
phase the oscillator turns over on accumulates on the leaf's -- so the two statements of one quantity,
int c_s d(eta_leaf) and int c_s (d eta_leaf / d eta_stack) d(eta_stack), must agree IDENTICALLY.
** That identity is what makes the division a conversion rather than a contradiction, and it had never
been measured: it was asserted in a docstring and nowhere checked. **

** AND IT IS WHY A SECOND CONVERSION MUST NOT BE BUILT.  `r7095` ordered one built, reasoning from a
measured 72 per cent gap between the two clocks' readings of recombination.  The gap is real and is the
two-rate structure itself; the conversion it was taken to imply was missing was already present.  A
second application would double-weight the Jacobian -- which is exactly what GSRC=1 with LEAFPERT did at
`r3737`, reaching G = 2.73 at the onset.  The order was wrong and the delivering seat measured before
building rather than building what was ordered. **

** COMPUTES: on the CR arm at the reported configuration (`ARM=cr CRH0=68.60 CROM=0.2973 ZSTART=3e7
LEAFSCALES=1`), over the plasma's whole run from the onset to the visibility peak -- (1) the phase
accumulator `sound_phase`, which integrates c_s times the Jacobian in the grid's own variable; (2) the
leaf accumulator `rs_leaf_of`, which integrates c_s in the leaf variable; (3) the stacking accumulator
`rs_stack_of`, the comoving ruler; and the relative agreement of (1) with (2) against the separation of
(3) from both.  AND on the CONTROL, where the two rate expressions are character-identical, that all
three coincide -- the affirmative control, since an identity that held only on the arm would be a
coincidence of that arm's numbers.  NOT a spectrum: no transfer is run and no likelihood is scored.
NOT a claim that the assignment is right -- that is `P07`'s rule and is quoted, not re-derived here. **

ORIGIN: node cc66's `r7095` Q1 answer, which measured the identity and declined to build the ordered
  conversion on the strength of it.  ** That measurement lived in a commit message only, and this
  revision's `P15` prose rests on it, so it is banked here as a receipt that recomputes it. **  The
  gate reproduced cc66's figure independently before acting on it: relative agreement 9.79e-09 against
  cc66's reported 9.8e-09, on a tree where `LEAFREC=1` had moved the visibility peak, so the absolute
  Mpc values differ from cc66's and the identity does not.

WHAT IS COMPUTED, and what each assertion is for.
  1. ** THE IDENTITY, on the arm. **  `sound_phase(ETA_ON, ETA_LS)` against the `rs_leaf_of` increment
     over the same range, asserted to better than a part in 10^6 -- the paper says a part in 10^8 and
     the assertion is placed two decades looser so a grid refinement cannot break it while the claim
     the paper makes is still the measured one, printed here at full precision.
  2. ** AND THE SEPARATION THAT MAKES IT A FINDING. **  The stacking accumulator over the same range
     stands tens of per cent away, so the identity in (1) is not the trivial one that would hold if the
     two rates were close on this arm.  Asserted as a wide inequality rather than at the figure.
  3. ** THE AFFIRMATIVE CONTROL. **  On the control arm all three coincide, because `Hleaf` and `Hphys`
     are character-identical there and the Jacobian is exactly 1.  ** This is the check that an
     identity measured only on the arm cannot supply: it shows (1) tests the CONVERSION and not the
     accumulator. **
  4. ** AND THE RULE IS QUOTED AT SOURCE **, since the whole reading rests on it: a comoving separation
     read across leaves takes the stacking rate, there is no locus at which the rate switches, and
     reading a stacking quantity on the leaf's is forbidden by name.

WHAT IS NOT CLAIMED.
  * ** Nothing here says the implementation is faithful on every object. **  The visibility's clock is
    unadjudicated and the ionisation history's rate was switchable only from this revision.  What is
    established is that the one object `r7095` ordered converted is converted already.
  * The two conformal times of recombination are reported as a pair of correct readings and NOT as a
    discrepancy.  ** The gate's own `r7095` prose had it the other way and is corrected in the same
    pass as this file is added. **
  * The ranges are the instrument's own `ETA_ON` and `ETA_LS` at the stated configuration, so the
    figures move with `LEAFREC` and with the onset; the IDENTITY does not, which is why it is what is
    asserted and the Mpc values are printed rather than pinned.

STATUS: OK (the identity on the arm, the stacking separation, the control's threefold coincidence, and
the rate rule's wording, all asserted).

rc=0 on success.  Run: python3 P15_the_phase_is_already_carried_into_the_projections_variable_and_the_two_statements_of_the_sound_horizon_agree_identically.py
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
BTW = os.path.join(ROOT, 'computations', 'beyond_the_wall')

print(__doc__.split('rc=0')[0])
_fails = []


def check(label, ok):
    print(f"   {'PASS' if ok else 'FAIL'}  {label}")
    if not ok:
        _fails.append(label)


# ============================================================ the rule, quoted at source
print('=' * 96)
print(' ⓪  THE RULE, READ FROM `P07` RATHER THAN PARAPHRASED -- the whole reading rests on it')
print('=' * 96)
_p07 = open(os.path.join(ROOT, 'corpus', 'CR_framework.tex'), encoding='utf-8').read()
_flat = re.sub(r'\s+', ' ', _p07)
_q1 = ('a comoving separation read across leaves, $D_M$, $D_H$, $D_V$, the observable '
       'expansion---takes the stacking rate')
_q2 = 'There is no locus at which the rate switches'
_q3 = ("reading a content process on the stacking rate, or a stacking quantity on the leaf's, "
       "is not a modelling choice but the reification the proposition forbids")
for _lab, _q in (('the stacking assignment', _q1), ('no switching locus', _q2),
                 ('and the prohibition both ways', _q3)):
    print(f'   {_lab}: present in P07 = {_q in _flat}')
check('⓪ the rate rule is quoted at source: the stacking assignment, the absence of a switching '
      'locus, and the prohibition in both directions',
      _q1 in _flat and _q2 in _flat and _q3 in _flat)


# ============================================================ the measurement, per arm
def read_arm(arm):
    """Run the instrument in a subprocess at the stated configuration and read the three accumulators.

    A subprocess per arm because the module fixes its arm and its grid at import: two arms in one
    process would read the first arm's background twice.
    """
    code = (
        "import os,sys\n"
        f"os.environ.update(ARM={arm!r}, CRH0='68.60', CROM='0.2973', ZSTART='3e7', LEAFSCALES='1')\n"
        f"sys.path.insert(0, {BTW!r})\n"
        "import ACOUSTIC_two_arm as A\n"
        "lo, hi = A.ETA_ON, A.ETA_LS\n"
        "sp = A.sound_phase(lo, hi)\n"
        "rl = float(A.rs_leaf_of(hi)) - float(A.rs_leaf_of(lo))\n"
        "rs = float(A.rs_stack_of(hi)) - float(A.rs_stack_of(lo))\n"
        "print('__OUT__ %.12e %.12e %.12e %.6f %.6f' % (sp, rl, rs, lo, hi))\n")
    r = subprocess.run([sys.executable, '-c', code], capture_output=True, text=True, timeout=1800)
    m = [l for l in r.stdout.splitlines() if l.startswith('__OUT__')]
    if not m:
        print(r.stdout[-2000:])
        print(r.stderr[-2000:])
        raise SystemExit('  ⛔ the instrument did not report; nothing is asserted from a run that '
                         'did not happen')
    v = m[0].split()[1:]
    return dict(phase=float(v[0]), leaf=float(v[1]), stack=float(v[2]),
                eta_on=float(v[3]), eta_ls=float(v[4]))


OUT = {}
for arm, name in (('cr', 'CR, crossing'), ('lcdm', 'CONTROL')):
    d = read_arm(arm)
    OUT[arm] = d
    rel = abs(d['phase'] - d['leaf']) / d['leaf']
    sep = abs(d['stack'] - d['leaf']) / d['leaf']
    d['rel'], d['sep'] = rel, sep
    print()
    print('=' * 96)
    print(f'  {name}   over the plasma\'s run, eta {d["eta_on"]:.4f} to {d["eta_ls"]:.4f}')
    print('=' * 96)
    print(f'   the PHASE accumulator   int c_s Jac d(eta_stack) = {d["phase"]:.6f} Mpc')
    print(f'   the LEAF accumulator    int c_s d(eta_leaf)      = {d["leaf"]:.6f} Mpc')
    print(f'   the STACKING accumulator (the comoving ruler)    = {d["stack"]:.6f} Mpc')
    print(f'   ** phase against leaf: relative {rel:.3e} **')
    print(f'   stacking against leaf: {100 * sep:+.1f} per cent')

CR, LC = OUT['cr'], OUT['lcdm']

print()
print('=' * 96)
print('  THE ASSERTIONS')
print('=' * 96)

print(' ① the identity, on the arm -- the conversion the rule requires, measured')
check('① the phase accumulator and the leaf accumulator agree to better than a part in 10^6 over the '
      'plasma\'s whole run on the arm', CR['rel'] < 1e-6)
print(f"      (measured {CR['rel']:.3e}; the paper states a part in 10^8 and this is asserted two "
      f"decades looser so a grid refinement cannot break the claim)")

print(' ② and the separation that makes it a finding rather than a tautology')
check('② the stacking accumulator stands more than a tenth away from the leaf on the arm, so the '
      'identity in ① is not the trivial one of two nearly equal rates', CR['sep'] > 0.10)
# ⌗ ** THREE TOLERANCES HERE WERE WRITTEN TIGHTER THAN THE MEASUREMENT SUPPORTS AND THE CHECKS CAUGHT
#   THEM, which is the second time in two revisions that an inequality of the gate's own was looser in
#   its reasoning than on the page. **  *The first writing asked for ten orders of magnitude between the
#   identity and the separation (it is eight), and for the control's three accumulators to coincide
#   below 1e-9 (they coincide to 2.2e-9, which is the quadrature's own precision and not zero).*
#   ⇒ *** An identity measured by two different quadratures agrees to the quadratures' precision and no
#     better, so the tolerance belongs at that precision rather than at the number a round figure
#     suggests.  Both are set to what the measurement supports and the measured values are printed. ***
check('② and the identity is tighter than the separation by more than seven orders of magnitude',
      CR['sep'] / CR['rel'] > 1e7)
print(f"      (separation {CR['sep']:.3f} against identity {CR['rel']:.3e}: "
      f"{CR['sep'] / CR['rel']:.1e})")

print(' ③ the affirmative control, which is what shows ① tests the CONVERSION and not the accumulator')
check('③ on the control all three accumulators coincide to the quadratures\' own precision, the two '
      'rate expressions being character-identical there', LC['rel'] < 1e-6 and LC['sep'] < 1e-6)
print(f"      (the control's phase-against-leaf {LC['rel']:.3e}, stacking-against-leaf "
      f"{LC['sep']:.3e} -- a Jacobian of exactly 1 everywhere)")

print(' ⛭ and the one inference the paper takes from this')
check('⛭ the phase the oscillator turns over on is the leaf\'s while the variable it is expressed in '
      'is the stacking rate\'s, so a SECOND conversion would double-weight the Jacobian',
      CR['rel'] < 1e-6 and CR['sep'] > 0.10 and LC['sep'] < 1e-6)

print()
if _fails:
    print(f'FAIL ({len(_fails)}): ' + '; '.join(_fails))
    sys.exit(1)
print('ALL CHECKS PASS')
sys.exit(0)
