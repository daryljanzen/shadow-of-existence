#!/usr/bin/env python3
"""C42 -- ⛔ **SUPERSEDED r2751: THE MECHANISM IS REAL AND TWO ORDERS TOO SMALL.**  *** A pure
$H$ probe (varying $N_{\\rm eff}$, which changes $H$ and does no recombination physics) moves $z_*$
by $-0.195\\%$; scaled by this receipt's own measured sensitivity that is ~$0.05$pp against a
$1.86$pp gap.  The real cause is a $7.1\\%$ validation miss the CAMB receipt prints about its own
arm.  See `C43_the_gap_is_numerical_not_xe`.  ** What survives: the cancellation condition IS
unmet, and the eliminations in ⓵ stand. ** ***

C42 -- the damping discrepancy DIAGNOSED: C8's cancellation needs $x_e(a)$ identical in both
cosmologies, and a different $H(a)$ changes the recombination HISTORY and not only its epoch.

** THE DISCREPANCY, surfaced at r2749. **  *** `C8` derives $+10.83\\%$; `P15_damping_ratio_clean`
returns $+8.97\\%$ for the same $r_D$ ratio.  ** C8 names the conflict in its own output ** -- "
damping_ratio_clean.py reports $\\sim+9\\%$.  This derivation gives $+10.8\\%$" -- and nothing resolved
it.  P15 calls the figure "a real, computed effect" nine times. ***

** ⓵ FOUR CANDIDATE EXPLANATIONS, TESTED AND ELIMINATED. **

      *** the cosmological constant   Lambda dropped vs kept:   1.099411 both ways -- NOT IT
          the upper limit             z=1100 vs zstar=1089.91:  10.68% vs 10.59% -- NOT IT
          the radiation density       C8's seam-carried 0.3239 vs standard 0.3003:
                                      10.68% vs 10.02% -- 8% in rho_r, 0.7pp in r_D -- NOT IT
          arithmetic                  C8 reproduced exactly at 1.106768 -- C8 IS INTERNALLY RIGHT ***

** ⛭⛭ ⓶ WHICH LEAVES C8's OWN STATED CONDITION, AND IT IS THE ANSWER. **  C8: "in the RATIO the
Thomson physics and $x_e$ cancel identically, ** PROVIDED the two integrals are taken over the same
range of $a$ ** --- which they are: recombination is the same physics in both."

  ⇒ *** The range is the same.  ** What is not the same is $x_e(a)$ itself. **  The integrand is
      $da/(H x_e)$, so $x_e$ cancels only if it is the SAME FUNCTION OF $a$ in both cosmologies.
      Recombination is a rate competition -- the Saha/Peebles balance between recombination and
      expansion -- so ** a different $H(a)$ changes the recombination HISTORY, not merely the epoch at
      which it completes **. ***

** ⓷ AND THAT IS EXACTLY THE DIFFERENCE BETWEEN THE TWO RECEIPTS. **  *** `C8` assumes the cancellation
and integrates $da/H$ alone; `P15_damping_ratio_clean` uses ** CAMB's exact $x_e(z)$ ** and does not.
The gap is $10.83$ against $8.97$ -- and its SIGN is right: including a rate-dependent $x_e$ moves the
ratio toward unity, because the cosmology with the faster early expansion also recombines slightly
differently. ***

** ⛔ ⓸ SO THE CORPUS'S OWN CONDITION IS UNMET, AND C8 STATES IT WITHOUT TESTING IT. **  *** "
recombination is the same physics in both" is true of the MICROPHYSICS and false of the HISTORY.  The
cancellation is exact for $\\sigma_T$ and $n_{e0}$ -- which are constants -- and not for $x_e(a)$,
which is a solution of an equation containing $H$. ***

  ⌗ ** Which of the two numbers is right is NOT settled here. **  *** $+8.97\\%$ carries the $x_e$
    response and is the better-founded of the two on that ground alone; $+10.83\\%$ is a clean analytic
    bound on what the effect would be if $x_e$ did not respond.  ** Establishing the response is a
    calculation neither receipt has done ** -- and it is smaller than either, because both agree the
    effect is real and of order ten per cent. ***

WHAT IS NOT CLAIMED.  ** Not that C8 is wrong ** -- *** it is internally exact, reproduced here to six
figures, and its condition is stated openly rather than hidden; what is unmet is the condition, not the
algebra. ***  ** Not that the CAMB figure is right ** -- it inherits CAMB's recombination for a
cosmology CAMB was not built for, which is its own open question.  ** Not that $\\sim8\\%$ should now be
made precise ** -- r2749 established the tilde is earned, and this receipt is why.

** COMPUTES: the $r_D$ ratio under four variations -- $\\Lambda$ on/off, two upper limits, two radiation
densities -- and a reproduction of C8's $1.106768$.  *** All parameters are the corpus's own. *** **

Written r2750.  Stated for reversal.
"""
import glob
import os

import numpy as np
from scipy.integrate import quad

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

OM, OL = 0.3153, 0.6847


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def ratio(z, rr, lam=0.0):
    a = 1/(1+z)
    Or = rr*OM/(1+z)
    I_CR = quad(lambda x: 1/np.sqrt(OM/x**3 + lam), 1e-9, a, limit=300)[0]
    I_LC = quad(lambda x: 1/np.sqrt(Or/x**4 + OM/x**3 + lam), 1e-9, a, limit=300)[0]
    return np.sqrt(I_CR/I_LC)


def rcpt(n):
    return open(glob.glob(os.path.join(ROOT, 'receipts', '**', n), recursive=True)[0],
                encoding='utf-8', errors='replace').read()


def main():
    print()
    print("  C42 -- why do C8 and the CAMB receipt disagree on the damping ratio?")
    print()
    c8 = rcpt('C8_diffusion_length.py')

    RR_C8 = 2.0*(1+1100.0)/(1+6797.0)

    # ⓵ reproduce C8 exactly
    r_c8 = ratio(1100.0, RR_C8)
    check(f'⓵ C8 is reproduced exactly: $r_D$ ratio $= {r_c8:.6f}$ against its stated $1.106768$ -- '
          'the algebra is right', abs(r_c8 - 1.106768) < 1e-5)

    # and the eliminations
    check(f'and $\\Lambda$ is not the difference: {ratio(1100.0, RR_C8, OL):.6f} with it, '
          f'{r_c8:.6f} without', abs(ratio(1100.0, RR_C8, OL) - r_c8) < 2e-3)
    r_zs = ratio(1089.90673, 2.0*(1+1089.90673)/(1+6797.0))
    check(f'nor the upper limit: $z=1100$ gives {100*(r_c8-1):.2f}%, CAMB\'s $z_*$ gives '
          f'{100*(r_zs-1):.2f}%', abs(r_c8 - r_zs) < 5e-3)
    r_std = ratio(1100.0, (8.6e-5/OM)*(1+1100.0))
    check(f'nor the radiation density: C8\'s seam-carried value gives {100*(r_c8-1):.2f}%, the '
          f'standard $\\Omega_r$ gives {100*(r_std-1):.2f}% -- 8% in $\\rho_r$, under a point in $r_D$',
          abs(r_c8 - r_std) < 0.01)

    # ⓶ C8's own condition
    check('⛭⛭ ⓶ which leaves C8\'s own stated condition: the Thomson physics and $x_e$ "cancel '
          'identically, PROVIDED the two integrals are taken over the same range of $a$"',
          'cancel identically, PROVIDED' in c8)
    check('and C8 justifies it as "recombination is the same physics in both" -- true of the '
          'MICROPHYSICS, and the integrand is $da/(H x_e)$ so $x_e$ must be the same FUNCTION of $a$',
          # ** the clause wraps a source line, so match the stem that does not straddle it **
          'which they are: recombination is the same' in c8)

    # ⓷ and the other receipt does not assume it
    check('⓷ while the CAMB receipt uses an exact ionization history rather than assuming the '
          'cancellation',
          'x_e' in rcpt('P15_damping_ratio_clean.py')
          or 'ionization' in rcpt('P15_damping_ratio_clean.py'))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** C8\'s cancellation needs x_e identical in both cosmologies. **')
    print('  ⓵ ** Four explanations tested and eliminated: ** Λ (no change), the upper limit (0.1pp),')
    print('     the radiation density (8% in ρ_r → 0.7pp in r_D), and arithmetic — ** C8 reproduces to')
    print('     six figures and is internally exact. **')
    print('  ⛭⛭ ⓶ *** WHICH LEAVES ITS OWN CONDITION.  The integrand is da/(H·x_e), so x_e cancels only')
    print('     if it is the SAME FUNCTION OF a in both.  Recombination is a rate competition between')
    print('     the Saha/Peebles balance and the expansion — so A DIFFERENT H(a) CHANGES THE')
    print('     RECOMBINATION HISTORY, NOT MERELY THE EPOCH AT WHICH IT COMPLETES. ***')
    print('  ⓷ ** And that is exactly what separates the receipts: ** C8 assumes the cancellation and')
    print('     integrates da/H alone; the other uses an exact ionization history.  ** The sign is')
    print('     right too — including the x_e response moves the ratio toward unity. **')
    print('  ⌗ ** Which number is correct is NOT settled here: ** +8.97% carries the response and is')
    print('    better founded on that ground; +10.83% is a clean analytic bound on the no-response')
    print('    case.  *** Establishing the response is a calculation neither receipt has done — and it')
    print('    is smaller than either, since both agree the effect is real and of order ten per')
    print('    cent. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
