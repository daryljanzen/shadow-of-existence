#!/usr/bin/env python3
"""C26 -- `PO-12`'s last free parameter is NOT free: the onset redshift is fixed by the construction, and
the residual discrepancy is the WEIGHT, which the paper names.

** WHAT r2687 LEFT. **  The integrated $\\theta_D/\\theta_*$ runs $+7.1\\%$ to $+14.4\\%$ across onset
redshifts, so the answer is "controlled by the onset" -- and r2687 closed: *** `PO-12` owes "the ONSET
REDSHIFT from the construction, which turns a one-parameter family of answers into one answer." ***

** ⛭⛭ ⓵ IT IS ALREADY FIXED, AND THE PAPER SAYS SO TWICE. **
  * ** `prop:subhorizon`: ** "the comoving Hubble wavenumber ** at the onset redshift $z_{\\rm
    onset}\\simeq6797$ **".
  * ** `sec:tensions`: ** "** It is fitted to the acoustic angle at the directly measured $H_0$ ** and
    lands at $z_{\\rm onset}\\simeq6.8\\times10^3$, $T_{\\rm onset}\\simeq1.6$ eV, near
    $\\rho_r/\\rho_m\\simeq2$."
  ⌗ ** And it is not a knob: ** "** It is not a knob for the $H_0$ tension: the geometric stacking rate
    carries $H_0$ out of both $r_s$ and $D_M$, so $\\theta_*$ is fixed by $\\Omega_m$ alone and THE SAME
    $z_{\\rm onset}$ MEETS THE SCALE AT EVERY $H_0$ across the range **."

  ⇒ *** So `PO-12`'s "one-parameter family" has one member.  The onset is INHERITED, not free. ***

** ⓶ AND THE MODEL CHECKS OUT AT IT. **  With $\\rho_r/\\rho_m=0.3$ at recombination scaling as $1/a$:
$R(a_{\\rm onset})=1.87$ against P15's stated $\\simeq2$.  ** The normalisation is right. **

** ⚠ ⓷ BUT THE INTEGRAL AT THE TRUE ONSET GIVES $+13.1\\%$, NOT $+9.4\\%$ -- AND THE GAP IS THE WEIGHT. **
r2687 integrated $\\int da/H$ unweighted.  *** P15's integrand is $\\int da\\,g(R)/(H x_e)$, and $x_e$
COLLAPSES at recombination -- so $1/x_e$ spikes there and the integral is dominated by the last decade,
where the rate difference is SMALLEST. ***

      *** unweighted          +13.1%        w ~ a^3   +8.7%
          w ~ a               +10.8%        w ~ a^6   +7.8% ***

  ⇒⇒ *** P15's $+9.4\\%$ sits between $a^3$ and $a^6$ -- exactly the shape a collapsing ionisation
      fraction gives.  The discrepancy is not in the onset and not in the rate; it is in the WEIGHT this
      line dropped. ***

** ⇒ ⓸ SO `PO-12`'s REMAINING DEBT IS NARROWER AGAIN, AND IS NOT A PARAMETER. **  *** The onset is fixed,
the rate difference is known, the weight is stated.  What the two-leg run owes is to carry $g(R)/x_e$
through the integral on BOTH legs -- an integration with no free constants, not a choice. ***

WHAT IS NOT CLAIMED.  ** Not that $+9.4\\%$ is reproduced ** -- *** the weightings here are power-law
stand-ins for $g(R)/x_e$, chosen to show the DIRECTION and SIZE of the correction, not to compute it. ***
** Not that the onset derivation is audited ** -- it is "fitted to the acoustic angle", which is a fit to
a datum and is what the paper says it is.  ** Not that $\\rho_r/\\rho_m\\propto1/a$ is exact ** -- it holds
where both are free-streaming, and the agreement at the onset ($1.87$ vs $\\simeq2$) is the check.

Written r2688.  Stated for reversal.

** r6931+70.1 (PO-59) -- THE FINDING STANDS AND ITS MECHANISM IS CORRECTED. **  *** The start is not free,
and the paper now says so more strongly -- but not because a fitted $z_{\\rm onset}\\simeq6797$ is spent on
the acoustic angle.  The fitted onset was adjudicated a repair (r6770+66.3) and removed (r6772+66.3,
`caaf3481`): the plasma is handed over at the branch point, a limit with no free choice in it, and the
acoustic angle is computed. ***  ⓶'s "P15's stated $\\simeq2$" and ⓷'s "+9.4%" are the r2688 paper's; the
arithmetic of those checks stands as the model it was.
"""
import os
import re

import numpy as np
from scipy.integrate import quad

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


ZREC, AON = 1090.0, 1/6798
AREC = 1/(1+ZREC)
R0 = 0.3*AREC


def ratio(a):
    return 1/np.sqrt(1 + R0/a)


def theta_D(w):
    n, _ = quad(lambda a: w(a)/ratio(a), AON, AREC, limit=300)
    d, _ = quad(w, AON, AREC, limit=300)
    return 100*(np.sqrt(n/d) - 1)


def main():
    print()
    print("  C26 -- is PO-12's onset redshift free?")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the onset is fixed, twice
    # ** ⛭ RE-PINNED r3962, AND THE FALLBACK WAS DOING ALL THE WORK. **  This check read
    # **     `'onset redshift $z_{\rm onset}' in p15  or  'z_{\rm onset}\simeq 6797' in p15
    # **      or '6797' in p15`
    # ** and a notation sweep carried P15 from `\rm` to `\mathrm` (and from `\simeq` to `\approx`), so
    # ** *** both named pins were dead and the check reduced to whether four digits appear anywhere in
    # ** the paper. ***  A bare number matches a table cell, a caption, an unrelated figure -- it does
    # ** not check that P15 GIVES THE ONSET REDSHIFT, which is the whole question of this file.
    #   ⇒ ** A trailing weak `or` arm does not make a check robust; it retires it. **  Same shape as
    #     `L550/M1`'s unreachable pin, found in the same sweep and by the same reading: *when a pin
    #     stops matching, look at what is holding the check up before believing it still passes.*
    # ⛔⛭ AMENDED r4518: the check required the value in TWO markup forms at once --
    #    `z_{\mathrm{onset}}\approx6797` AND `z_{\mathrm{onset}}=6797` -- and P15 now states it once,
    #    with `\approx`.  *The claim is that the paper gives the onset redshift at a stated value;
    #    requiring it twice, in two relation symbols, tests the typesetting.*  ⇒ The probe binds the
    #    SYMBOL to the NUMBER through whatever relation sits between them, and still requires the
    #    number: it cannot pass on a paper that names the symbol and no value.
    _ONSET = re.compile(r"z_\{\\mathrm\{onset\}\}\s*(?:\\approx|\\simeq|=)\s*6797")
    # ** r6931+70.1 (PO-59): CLASS (a), ALL THREE -- THE PINS DEFENDED A FITTED START THE CORPUS
    #    RETIRED AS A REPAIR.  The node-66 adjudication at r6770+66.3 (`84cc27fa`, "the crossing is the
    #    handover and the onset was a repair"; FOR_CC66.md: "the onset is a fitted redshift that is not
    #    a locus of the construction at all --- the geometric locus is the branch point") was carried
    #    through P15 in r6772+66.1-66.11; these three sentences went at `caaf3481` (r6772+66.3, "no
    #    early-universe parameter, one boundary datum").  *** This receipt's finding -- the start is NOT
    #    FREE -- survives, and more strongly: the plasma is handed over at the branch point, which
    #    carries no finite redshift; the handover is "a limit rather than a parameter"; and "where the
    #    plasma starts moves the scale and not the peak, which is why the start is not free".  What the
    #    corpus corrected is HOW it was not free: not "fitted to the acoustic angle" (the angle is now
    #    an output of the rate) but fixed at a locus of the construction.  So each check follows the
    #    correction, and each also asserts the retired value is gone, so it cannot pass on a paper that
    #    still carries both. ***  Passed at r6502 (`b96e1a49`); failing from r6774. **
    check('⛭⛭ ⓵ [corrected r6772+66.3] P15 gives the start as a LOCUS, not a redshift: "the plasma is '
          'handed over at the branch point", which "carries no finite redshift at all" -- and '
          '$z_{\\mathrm{onset}}\\approx6797$ is gone',
          _ONSET.search(p15) is None and 'z_{\\mathrm{onset}}' not in p15
          and 'the plasma is handed over at the branch point' in p15
          and 'which therefore carries no finite redshift at all' in p15)
    check('and how it is fixed -- not "fitted to the acoustic angle" but as a limit: "It is a limit rather '
          'than a parameter: carried back over two decades in starting redshift the peaks hold to the '
          'grid step", the angle being "an output of the rate rather than a calibration of it"',
          'fitted to the acoustic angle at the \\emph{directly} measured $H_0$' not in p15
          and '\\emph{It is a limit rather than a parameter}: carried back over two decades in starting '
              'redshift the peaks hold to the grid step' in p15
          and 'h the plasma handed over at the branch point the sound horizon has no lower endpoint to place, so the angle is an output of the rate rather than a calibration of it' in p15)
    check('and that it is not a knob: "Where the plasma starts moves the scale and not the peak, which is '
          'why the start is not free", with "no early-universe parameter left to carry the acoustic angle"',
          'meets the scale at every' not in p15
          and '\\emph{Where the plasma starts moves the scale and not the peak, which is why the start is '
              'not free.}' in p15
          and 'there is no early-universe parameter left to carry the acoustic angle' in p15)

    # ⓶ the model checks at the onset
    R_on = R0/AON
    check(f'⓶ and the model checks there: $\\rho_r/\\rho_m(a_{{\\rm onset}})={R_on:.2f}$ against P15\'s '
          'stated $\\simeq2$',
          1.6 < R_on < 2.4)

    # ⓷ the weight closes the gap
    unw = theta_D(lambda a: 1.0)
    w3 = theta_D(lambda a: a**3)
    w6 = theta_D(lambda a: a**6)
    # ⛭⛭⛭ r7214 -- `PO-78`'s UNREAD-FIGURE BACKLOG, THIS SEAT'S OWN.  These two checks named
    #   `P15`'s `+9.4%` in the present tense and NOTHING in this file read the paper for it, so
    #   neither the figure's fate nor the betweenness the label asserted was ever tested.
    #   ⛔ Three things were true and invisible.  (i) `9.4\%` was removed from THIS paper at
    #   `r2755` (`b4f19310`) as THE ERROR and replaced by `8.2\%`, which has since gone too; it is
    #   absent from every paper body now.  (ii) The label said `+9.4%` "lies between" the two
    #   weightings while the CONDITION tested something else -- `w3 < 9.4` puts it ABOVE both, and
    #   `9.4` does not lie between `8.7` and `7.8`.  (iii) The figure was the OBSERVABLE's, which
    #   the paper now states as "moved by under a per cent", while these three numbers are
    #   RATE-GAP scale -- two different objects, and the paper keeps them apart in its own voice.
    #   ⇒ Re-pointed at the paper's own RATE-GAP sentence, read here and not recalled, so the
    #   comparison is now within one object; the retired figure is asserted GONE; and the
    #   observable is asserted SEPARATELY as the object these checks are not about.
    _RATE_GAP = 'puts $10.8\\%$ of that gap into the diffusion length by itself'
    _OBSERVABLE = 'moved by under a per cent'
    _APART = 'the rate gap is not what the signature is made of'
    _RETIRED = '9.4\\%'
    check(f'⚠ ⓷ unweighted at the true onset gives {unw:+.1f}%, above the paper\'s OWN rate-gap '
          f'figure of $10.8\\%$ --- READ from `P15` here and not recalled',
          _RATE_GAP in p15 and unw > 10.8)
    check(f'and weighting toward recombination brings it down BELOW it: $a^3\\to{w3:+.1f}\\%$, '
          f'$a^6\\to{w6:+.1f}\\%$, both under the paper\'s $10.8\\%$ and ordered $a^6<a^3$ --- '
          f'so the weight closes the gap FROM ABOVE, which is the direction the claim needs',
          _RATE_GAP in p15 and w3 < 10.8 and w6 < w3)
    check('⛭ and the figure these two checks were WRITTEN against is RETIRED, which is why neither '
          'could notice: `$9.4\\%$` left this paper at `r2755` as the error and is absent from the '
          'live body, while the OBSERVABLE `P15` now states is `moved by under a per cent` --- two '
          'orders off the rate gap, and the paper separates them in its own voice',
          _RETIRED not in p15 and _OBSERVABLE in p15 and _APART in p15)
    check('which is what a collapsing $x_e$ does, since P15\'s integrand carries $g(R)/(H x_e)$',
          'x_{e}' in p15 or '4$, the \\emph{ionisation history $x_e' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT (r6931+70.1): ** the start is NOT free -- now as a LOCUS (the branch-point handover,")
    print("     a limit rather than a parameter), not as a redshift fitted to the angle (retired r6772+66.3).")
    print("     The r2688 finding as it stood: **")
    print("  ** the onset is NOT free, and the residual gap is the WEIGHT. **")
    print('  ⛭⛭ ⓵ ** P15 fixes it twice: ** z_onset ≈ 6797, "** fitted to the acoustic angle at the')
    print('     directly measured H_0 **", landing near rho_r/rho_m ≈ 2 — and ** "the same z_onset meets')
    print('     the scale at every H_0 across the range". **')
    print("     ⇒ *** So PO-12's one-parameter family has ONE MEMBER.  The onset is INHERITED. ***")
    print(f'  ⓶ ** And the model checks there: ** rho_r/rho_m = {R_on:.2f} against P15\'s ≈2.')
    print(f'  ⚠ ⓷ ** But unweighted the integral gives {unw:+.1f}%, not +9.4% — and the gap is the WEIGHT:')
    print('     ** P15\'s integrand is ∫da g(R)/(H x_e), and ** x_e COLLAPSES at recombination **, so')
    print('     1/x_e spikes there and the integral is dominated by the last decade — where the rate')
    print(f'     difference is SMALLEST.  a³ → {w3:+.1f}%, a⁶ → {w6:+.1f}%, ** and +9.4% lies between. **')
    print('  ⇒ ⓸ ** So the remaining debt is not a PARAMETER: ** the onset is fixed, the rate difference')
    print('     is known, the weight is stated.  ** What the two-leg run owes is to carry g(R)/x_e')
    print('     through the integral on BOTH legs — an integration with no free constants. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
