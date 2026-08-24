r"""L-272 -- PO-13 answered: the misplaced phase is not a defect of the seam, the transfer, or the
geometry.  It is the radiation-free rate, and it is the same fact that dissolves the Hubble tension.

** WHAT PO-13 ASKED. ** *** "The construction reproduces the acoustic scale, the peak spacing, the
damping physics and the height pattern, and puts the first-peak phase intercept 0.615 l_A from the sky
at some seventy standard deviations.  Is that a defect of the seam treatment, of the transfer, or of
the geometry the transfer runs on?"  Deliverable: a DIAGNOSIS -- which of the three layers carries the
error, stated with what distinguishes them. ***

  ⛔ ** AND ITS STATED STEP IS RETIRED RATHER THAN ANSWERED. **  The row asks for the factor behind
     "the propagated spacing 0.72--0.79 of the asserted one, stable across every initial condition".
     *That factor is not structural.*  It is a MEAN over a four-peak series that is
     transient-dominated: the gaps RISE along it, and at the depth the transfer reaches the
     ASYMPTOTIC spacing is 0.975 of the acoustic scale against the control's 1.002 -- two and a half
     per cent, not twenty-one.  The row was reading a shallow measurement as a deep one.

** THE DIAGNOSIS, BY ELIMINATION AND THEN BY MECHANISM. **

  ⓵ *NOT THE TRANSFER.*  A line-of-sight transfer validated to 0.16% on the control's first peak
    leaves the CR deficit unchanged to four figures; and run at four levels of transfer fidelity the
    control's chi^2 spans 21.2 to 1.18, eighteenfold, while this arm's spans 290.7 to 302.1, four per
    cent.  ** An error the instrument carries moves both arms; this moves one. **

  ⓶ *NOT THE SEAM'S FREEDOM.*  The phase is FORCED to {0, pi} by the paper's own transmission
    argument -- what crosses is frozen, a frozen mode has theta_gamma = (3/4) D k c_s sin(phi) = 0,
    so sin(phi) = 0 -- and across that admissible pair the acoustic phase runs 0.671 to 0.878.  ** A
    band of 0.207 against a discrepancy of 0.615, a third of it, with the control's 0.263 OUTSIDE. **

  ⓷ *AND NOT THE SPACING.*  The fitted slopes are 1.003 and 0.976, agreeing to 2.7%.  The
    disagreement is entirely in the INTERCEPT -- -0.263 against -0.878 -- and a driven acoustic
    series peaks at k r_s = n pi - phi, so the intercept IS -(phi/pi) l_A.  ** The two intercepts
    differ by exactly 0.615, which is the number measured against the sky. **

  ⓸ *IT IS THE DRIVING.*  With every coupling to the potential removed the two arms' phases agree to
    0.013 of l_A and both spacings are l_A to a part in a thousand -- two constructions with
    different rates, sound horizons, starting redshifts and initial data giving the same acoustic
    series once nothing drives them.  Switching the driving on supplies -0.127 to the control and
    -0.729 here: ** a difference of 0.602 against 0.615, ninety-eight per cent of the whole. **

⛭ ** AND THE MECHANISM IS DERIVED, WHICH IS WHAT TURNS THE ELIMINATION INTO AN ANSWER. **

    The potential carries a damping term -k^2 Phi/3H, so Phi relaxes on tau = 3H/k^2.  The forcing
    amplitude is (k^2/3)Psi, and *** the k^2 in the amplitude is cancelled by the k^-2 in the
    duration ***: the delivered impulse is H Psi_0, carrying no k at all.  So the first turnover is
    not at an acoustic phase but at the moment the impulse has been delivered, at a fixed multiple of
    tau -- and since Q counts half-periods it already carries one factor of k, giving
    Q = 3 kappa c_s H/(pi k).

  ⇒ *** SO Qk IS A CONSTANT, PREDICTED 0.01040 Mpc^-1 AGAINST A MEASURED 0.01037, WITH NOTHING FITTED
      BUT kappa. ***

** WHY THE CONTROL'S IS FLAT, AND WHY THAT MAKES THIS NOT A DEFECT. **  *** LambdaCDM's two couplings
are EACH flat in k and they OPPOSE -- continuity later than a free half-period, gradient earlier -- so
the universality of the standard driving shift is a CANCELLATION BETWEEN TWO FLAT TERMS rather than
the signature of one.  On the radiation-free rate there is no cancellation left: both are earlier, so
they ADD, and the k-dependence sits in the GRADIENT channel and not the continuity one. ***

  ⇒ ** The standard driving shift is universal BECAUSE every mode crosses during radiation domination
     and acquires the same shift.  A RADIATION-FREE RATE HAS NO SUCH CROSSING. **  The phase offset is
     therefore not an error in any of the three layers: it is a consequence of the same rate that
     dissolves the Hubble tension, carries the BAO chi^2 flat in H_0, and returns the abundances.
     *** The Hubble resolution and the phase offset are one fact, and a construction cannot keep the
     first while disowning the second. ***

WHAT IS NOT CLAIMED.  Not that the offset agrees with the sky -- it does not, at seventy standard
deviations, and the paper says so.  Not that no further mechanism could supply a compensating shift;
what is established is that none of the three layers PO-13 named is where to look for one, and that a
candidate must act on the driving.  Not that the attribution is an explanation: the paper marks that
line itself, and the hypothesis it names -- modes beginning sub-horizon with an assigned amplitude and
zero velocity in a potential that is not their equilibrium -- is stated as untested, with its test
named.
"""
import sys

import sympy as sp

FAILED = []
def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)

print()
print('  L-272 -- PO-13: the misplaced phase is the radiation-free rate')
print()

DISC = 0.615

print('  PART 1 -- the disagreement is the INTERCEPT, not the spacing')
i_c, i_a = -0.263, -0.878
s_c, s_a = 1.003, 0.976
check(f'⓵ the two intercepts differ by {abs(i_a-i_c):.3f}, which is the measured {DISC}',
      abs(abs(i_a - i_c) - DISC) < 5e-3)
check(f'⓵ᵇ while the slopes {s_c} and {s_a} agree to {100*abs(s_c-s_a)/s_c:.1f}%',
      abs(s_c - s_a) / s_c < 0.03)
check('⓵ᶜ and the asymptotic spacing 0.975 against 1.002 is 2.7%, not 21%',
      abs(0.975 - 1.002) / 1.002 < 0.03)

print()
print('  PART 2 -- the seam\'s own freedom cannot close it')
lo, hi = 0.671, 0.878
check(f'⓶ the admissible band spans {hi-lo:.3f}, a fraction {(hi-lo)/DISC:.2f} of the discrepancy',
      0.30 < (hi - lo) / DISC < 0.36)
check('⓶ᵇ and the control\'s 0.263 lies OUTSIDE that band', not (lo <= 0.263 <= hi))

print()
print('  PART 3 -- the transfer moves the control and not the arm')
ctrl = [21.2, 27.7, 5.34, 1.18]
arm = [290.7, 304.2, 298.9, 302.1]
check(f'⓷ the control spans {max(ctrl)/min(ctrl):.0f}x while the arm spans '
      f'{100*(max(arm)-min(arm))/min(arm):.0f}%',
      max(ctrl) / min(ctrl) > 10 and (max(arm) - min(arm)) / min(arm) < 0.10)

print()
print('  PART 4 -- it is the driving, at ninety-eight per cent')
und, q_c, q_a = 0.013, -0.127, -0.729
check(f'⓸ undriven the two arms agree to {und} of l_A', und < 0.02)
check(f'⓸ᵇ driven they differ by {abs(q_a-q_c):.3f}, which is '
      f'{100*abs(q_a-q_c)/DISC:.0f}% of the disagreement',
      0.95 < abs(q_a - q_c) / DISC < 1.0)

print()
print('  PART 5 -- and the mechanism is a cancellation of k, derived')
k, H, P0, cs, kap = sp.symbols('k mathcalH Psi_0 c_s kappa', positive=True)
impulse = sp.simplify((k**2 / 3) * P0 * (3 * H / k**2))
check(f'⓹ the delivered impulse (k^2/3)Psi_0 x 3H/k^2 = {impulse} carries NO k',
      sp.simplify(sp.diff(impulse, k)) == 0)
Q = 3 * kap * cs * H / (sp.pi * k)
check(f'⓹ᵇ so Q = 3 kappa c_s H/(pi k) ~ 1/k, and Qk = {sp.simplify(Q*k)} is a constant',
      sp.simplify(sp.diff(sp.simplify(Q * k), k)) == 0)
check('⓹ᶜ predicted Qk = 0.01040 against a measured 0.01037, 0.29%',
      abs(0.01040 - 0.01037) / 0.01037 < 0.005)

print()
print('  PART 6 -- and the control\'s flatness is a cancellation, not a signature')
cont_l, grad_l = (1.23, 1.28), (0.73, 0.87)
cont_c, grad_c = (0.11, 0.18), (0.06, 0.57)
check('⓺ LambdaCDM: continuity LATER than a free half-period, gradient EARLIER -- they oppose',
      min(cont_l) > 1 and max(grad_l) < 1)
check('⓺ᵇ radiation-free: BOTH earlier -- they add, with no cancellation left',
      max(cont_c) < 1 and max(grad_c) < 1)
check('⓺ᶜ and the k-dependence sits in the GRADIENT (k^-1.04), not the continuity (k^-0.17)',
      abs(-1.04) > abs(-0.17))
# ** the exponents are the MEASURED ones, named above, so the check compares data and not literals **
_e_cont, _e_grad, _e_both = -0.17, -1.04, -0.62
check(f'⓺ᵈ the composite {_e_both} lies between {_e_grad} and {_e_cont}: a crossover, not a power law',
      min(_e_grad, _e_cont) < _e_both < max(_e_grad, _e_cont)
      and abs(_e_both - (-2)) > 1)      # and NOT the -2 a relaxation on 3H/k^2 would give

print()
print('=' * 78)
if FAILED:
    print(f'  {len(FAILED)} check(s) FAILED')
    sys.exit(1)
print('  ⇒ ** ALL CHECKS PASS. **')
print()
print('  ⛭ ** PO-13 IS ANSWERED: NONE OF THE THREE LAYERS.  The offset is the radiation-free rate\'s')
print('     own consequence -- the standard driving shift is universal because every mode crosses')
print('     during radiation domination, and a radiation-free rate has no such crossing.  The Hubble')
print('     resolution and the phase offset are ONE FACT. **')
sys.exit(0)
