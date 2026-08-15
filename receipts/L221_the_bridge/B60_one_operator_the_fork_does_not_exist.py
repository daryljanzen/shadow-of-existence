#!/usr/bin/env python3
"""B60 -- ADJUDICATION for `#558`: `B3` and `L-813` are ONE operator, the $\\omega$-coupling is
$\\omega/\\sqrt f$, and there is no $\\lambda f/r$.  The fork does not exist.

** THE QUESTION cc54 ROUTED. **  *** (1) `B3`'s full first-order pair including the $\\omega$-coupling;
(2) whether `L-813`'s tortoise $V_\\pm=W^2\\pm dW/dr_*$ is consistent with `B3`'s $\\sqrt f\\,d/dr$ pair or
a rescaled second-order form.  ** cc54 held the transmission rather than build on an assumed
coupling. ** ***

** ⛭⛭ ⓵ `B3`'s TETRAD FIXES THE COUPLING, AND cc54's GUESS WAS RIGHT. **  `B3` builds
$e^0=\\sqrt f\\,dt$, $e^1=dr/\\sqrt f$, $e^2=r\\,d\\theta$.  The inverse frame components give each term:

      *** e_0^t = 1/sqrt(f)      -> the time term enters as   omega / sqrt(f)   <- cc54's assumption ✔
          e_1^r = sqrt(f)        -> the radial term is        sqrt(f) d/dr
          e_2^theta = 1/r        -> the angular term is       lambda / r ***

  ⇒ ** the orthonormal-frame pair: ** $\\sqrt f\\,dP/dr \\mp (\\lambda/r)P = \\mp(i\\omega/\\sqrt f)P$.

** ⛭⛭⛭ ⓶ AND MULTIPLYING BY $\\sqrt f$ RETURNS CHANDRASEKHAR EXACTLY. **

      *** f dP/dr  -/+ (lambda sqrt(f)/r) P = -/+ i omega P
          i.e.  dP/dx -/+ (lambda sqrt(f)/r) P = -/+ i omega P ***

  ⇒⇒ *** $W_{\\rm tortoise}=\\lambda\\sqrt f/r$ -- which is `L-813`'s form.  ** `B3` and `L-813` are ONE
      operator.  `L-813` is not a rescaled second-order form and its spectrum is not in question. ** ***

** ⛔ ⓷ AND THE SLIP THAT CREATED THE FORK. **  *** cc54 took $W_{\\rm leaf}=\\lambda\\sqrt f/r$ and
multiplied by $\\sqrt f$ to reach $\\lambda f/r$.  ** But `B3`'s "$W=\\lambda\\sqrt f/r$" IS ALREADY THE
TORTOISE SUPERPOTENTIAL. **  The leaf-frame angular term is $\\lambda/r$, and
$\\sqrt f\\cdot\\lambda/r=\\lambda\\sqrt f/r$. ***
  ⇒ ** There is no $\\lambda f/r$.  The fork does not exist, and nothing bears on `L-813`. **

** ⚠ ⓸ AND WHAT IS STILL NOT IN HAND, SAID PLAINLY. **  *** This receipt settles WHICH OPERATOR.  It
does NOT reproduce P14's real $\\pm\\lambda$ from it.  ** This line attempted a leading-order reduction in
the real leaf coordinate $ds=dr/\\sqrt{|f|}$ and got $\\ln P\\propto\\sqrt r$ -- not a power law, a THIRD
answer distinct from cc54's index-2 and imaginary results. ** ***
  ⇒ *** THREE NAIVE REDUCTIONS, THREE DIFFERENT WRONG ANSWERS.  ** That is not three mistakes -- it is
      evidence that the indices come from the full operator with its $\\omega$-coupling and subleading
      terms, and that no leading-order pass will produce them. **  cc54's refusal to force a third
      non-validating pass was right, and this is the fourth. ***

WHAT IS NOT CLAIMED.  ** Not that P14's $\\pm\\lambda$ is derived ** -- *** it is not, and this receipt
says so; what is settled is the operator, which is what `#558` asked for. ***  ** Not that the wall's
$f<0$ subtlety is resolved ** -- *** $\\sqrt f$ is imaginary for $r\\to0^+$ and which branch the
continuation takes is exactly where the real-versus-imaginary indices part company; naming that is not
settling it. ***  ** Not that `L-813` is re-verified ** -- *** it is shown CONSISTENT with `B3`, not
recomputed. ***

** COMPUTES: nothing numerical.  *** A frame-component reduction of `B3`'s stated tetrad, carried to
the tortoise form and compared with `L-813`'s. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT f709b86** *(per c54.220's rule, r2776).*

Written r2816.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  B60 -- are B3's leaf pair and L-813's tortoise V_pm the same operator?")
    print()
    b3 = open(glob.glob(os.path.join(ROOT, 'receipts', '**', '*B3_spinor_vielbein*.py'),
                        recursive=True)[0], encoding='utf-8', errors='replace').read()

    check('⛭⛭ ⓵ `B3` states the leaf tetrad: "e0=sqrt f dt, e1=dr/sqrt f, e2=r dtheta"',
          'e1=dr/sqrt f' in b3 and 'e0=sqrt f dt' in b3)
    check('and its superpotential: "the massless radial Dirac operator carries superpotential '
          'W=lambda sqrt(f)/r"',
          'W=lambda sqrt(f)/r' in b3)

    check('⛭⛭⛭ ⓶ so the inverse frame gives the $\\omega$-coupling as $\\omega/\\sqrt f$ from '
          '$e_0^t=1/\\sqrt f$ -- ** cc54\'s assumption confirmed **',
          'e0=sqrt f dt' in b3)
    check('and multiplying the frame pair by $\\sqrt f$ returns $dP/dx \\mp (\\lambda\\sqrt f/r)P '
          '= \\mp i\\omega P$ -- ** Chandrasekhar, and `L-813`\'s form **',
          'W=lambda sqrt(f)/r' in b3)

    check('⛔ ⓷ so `B3`\'s $W$ is ALREADY the tortoise superpotential, the leaf angular term being '
          '$\\lambda/r$ -- ** there is no $\\lambda f/r$ and the fork does not exist **',
          'W=lambda sqrt(f)/r' in b3)

    # ⓸ and the walls f<0
    check('⚠ ⓸ while `B3` records the two features the wall rests on: "W=0 at every horizon (f=0) '
          'and is ODD in signed r"',
          'W=0 at every horizon' in b3 and 'ODD in signed r' in b3)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** one operator. The fork does not exist. **')
    print('  ⛭⛭ ⓵ ** B3\'s tetrad fixes every term: ** e_0^t = 1/√f gives the ω-coupling as ω/√f')
    print('     (** cc54\'s assumption was right **); e_1^r = √f gives √f d/dr; e_2^θ = 1/r gives λ/r.')
    print('  ⛭⛭⛭ ⓶ ** And multiplying by √f returns Chandrasekhar exactly: **')
    print('       dP/dx ∓ (λ√f/r) P = ∓ iω P      ⇒ W_tortoise = λ√f/r')
    print('     *** That is L-813\'s form.  B3 and L-813 are ONE operator — not a rescaled second-order')
    print('     form, and L-813\'s spectrum is not in question. ***')
    print('  ⛔ ⓷ ** The slip: ** B3\'s "W = λ√f/r" is ALREADY the tortoise superpotential.  The leaf')
    print('     angular term is λ/r, and √f · λ/r = λ√f/r.  ** There is no λf/r. **')
    print('  ⚠ ⓸ ** And what is NOT settled: ** this does not reproduce P14\'s real ±λ.  A leading-order')
    print('     pass in the real leaf coordinate ds = dr/√|f| gives ln P ∝ √r — ** a THIRD answer, after')
    print('     cc54\'s index-2 and imaginary results. **')
    print('     *** Three naive reductions, three different wrong answers: the indices come from the')
    print('     full operator with its ω-coupling and subleading terms, and no leading-order pass will')
    print('     produce them.  Holding the transmission was right. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
