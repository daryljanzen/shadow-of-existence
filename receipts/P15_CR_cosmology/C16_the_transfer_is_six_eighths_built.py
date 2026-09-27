#!/usr/bin/env python3
"""C16 -- `PO-12`'s step ② is smaller than its framing: six of the transfer's eight pieces are computed,
the projection is calibrated, and a $C_\\ell$ RATIO with no free parameter is already in the paper.

** THE DEBT AS FRAMED. **  `CR_cosmology`: "This is ** a genuine build, not a plug-in **: it requires first
*specifying how the fluctuations gravitate on the geometric stacking background* ... and then ** a bespoke
transfer against that specification **."  r2623 found step ① built (`sec:envelope`); r2646 found step ②
gates BOTH of `PO-10`'s runs.

** ⓵ AND SIX OF THE TRANSFER'S EIGHT PIECES ARE COMPUTED. **

      *** ✔ the driving in closed form      Phi = 3(sin x - x cos x)/x^3,  x = k*eta/sqrt3
          ✔ source removal                  Theta'' + (k^2/3)Theta = 0, exactly
          ✔ amplitude at horizon entry      "fixed by the construction rather than fitted"
          ✔ the sound horizon               r_s = 146.4 Mpc
          ✔ the diffusion scale             10.8% longer on the geometric stacking rate
          ✔ the baryon loading              R_b = 0.60 at recombination
          ⛔ the visibility function         not located
          ⛔ the k -> l projection           -- SEE (2) *** 

  ⌗ ** And the driving is verified here rather than taken: ** $\\Phi$ satisfies
    $\\Phi''+(4/x)\\Phi'+\\Phi=0$, is even in $x$, and $\\to1$ as $x\\to0$ so the normalisation is fixed.

** ⛭⛭ ⓶ AND THE PROJECTION IS ALREADY CALIBRATED. **  "$\\ell_*=D_M/r_s=302.2$ against the measured
$301$" -- *** so the $k\\to\\ell$ map's one CR-specific input, the comoving distance to last scattering, is
computed and lands within $0.4\\%$. ***

** ⛭⛭⛭ ⓷ AND A $C_\\ell$ RATIO WITH NO FREE PARAMETER IS ALREADY IN THE PAPER. **  "The high-$\\ell$
consequence follows with no free parameter: ** $C_\\ell^{\\rm CR}/C_\\ell^{\\Lambda\\rm CDM}
=\\exp[-(\\ell/\\ell_D)^2(r^2-1)]$ with $r=1.082$ **, so the ratio is $0.84$ at $\\ell_D$".

  ** Recomputed: ** $\\exp[-(1)(1.082^2-1)]=0.844$ -- *** matches the paper's $0.84$. ***
  ⇒⇒ *** That is a TRANSFER-LEVEL statement: a ratio of $C_\\ell$ spectra, no free parameter -- and it is
      exactly the shape r2647 identified as the transfer-free route (SAME multipole, two rates).  The
      route is not merely available; it has been walked at $C_\\ell$ level. ***

** ⇒ ⓸ SO WHAT `PO-12` STILL OWES IS NARROWER THAN "a bespoke transfer". **  *** The bespoke part is the
PHYSICS, and the physics is built.  What is absent is the ABSOLUTE spectrum -- the visibility-weighted
line-of-sight integral that turns $\\Theta(k)$ into $C_\\ell$ itself rather than into a ratio against
$\\Lambda$CDM. ***
  ⌗ ** And that reframes `PO-10`'s gate (r2646): ** *** `PO-10`'s odd/even PATTERN needs the absolute
    spectrum and stays gated; but any observable expressible as a CR/$\\Lambda$CDM ratio at fixed $\\ell$
    does not, because the ratio route is already built. ***

WHAT IS NOT CLAIMED.  ** Not that the transfer is done ** -- the absolute spectrum is not built and the
visibility function is not located.  ** Not that the ratio replaces it ** -- *** a ratio against
$\\Lambda$CDM inherits $\\Lambda$CDM's own transfer as its denominator, which is why the paper states it as
a consequence and not as the spectrum. ***  ** Not that $\\ell_*=302.2$ closes the calibration ** -- the
paper says "to that accuracy rather than exactly".

Written r2658.  Stated for reversal.

** r6931+70.1 (PO-59) -- DISCHARGED, AND WHERE. **  *** What this receipt found missing -- the visibility
function and the absolute line-of-sight spectrum -- is RUN: r6719 (`440623b6`) states the end-to-end
transfer as a two-arm line-of-sight integral on this cosmology's own background, and the visibility is
located and measured on both arms. ***  And ⓷'s ratio now carries the paper's current $r=0.992$ (a rise of
about two per cent at $\\ell_D$), not r2658's $1.082$ / $0.84$, which belonged to the fitted-onset handover
the corpus retired at r6770+66.3.
"""
import os
import re

import numpy as np
import sympy as sp

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


def main():
    print()
    print("  C16 -- how much of PO-12's transfer is already built?")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # the debt as framed
    # ** r6931+70.1 (PO-59): CLASS (b), DISCHARGED.  "This is a genuine build, not a plug-in" was
    #    deleted at `440623b6` (r6719, "the transfer is run") because the build was done.  This
    #    receipt's finding was that what PO-12 still owed was the ABSOLUTE spectrum -- "the
    #    visibility-weighted line-of-sight integral that turns Theta(k) into C_l itself" -- and that
    #    is exactly what P15 now states as run: a two-arm line-of-sight integral
    #    Delta_l(k) = int S j_l(k(eta_0-eta)) d eta on this cosmology's own background, with the
    #    visibility located on both arms (its width measured, 43.6 against 38.0 Mpc).  *** So the
    #    check pins the discharge, the two pieces this receipt marked NOT located, and the absence of
    #    the old framing -- not merely the new wording. ***  Passed at r6502 (`b96e1a49`). **
    check('⓵ [discharged r6719] the debt WAS framed as a build ("a genuine build, not a plug-in") and '
          'that framing is gone because the build is run: "The end-to-end branch-point-to-'
          'recombination transfer is run", the absolute spectrum as "a two-arm line-of-sight '
          'Boltzmann integral, $\\Delta_\\ell(k)=\\int S\\,j_\\ell(k(\\eta_0-\\eta))\\,d\\eta$", and '
          'the visibility located on both arms ("$43.6$ against $38.0$~Mpc")',
          'This is a genuine build, not a plug-in' not in p15
          and '\\emph{The end-to-end branch-point-to-recombination transfer is run}' in p15
          and 'a two-arm line-of-sight Boltzmann integral, $\\Delta_\\ell(k)=\\int S\\,j_\\ell(k(\\eta_0-\\eta))\\,d\\eta$' in p15
          and 'visibility is \\emph{wider}, $43.6$ against $38.0$~Mpc' in p15)

    # ⓵ the driving, verified rather than taken
    x = sp.symbols('x', positive=True)
    Phi = 3 * (sp.sin(x) - x * sp.cos(x)) / x**3
    check('⓶ the driving is given in closed form and verified here: it satisfies '
          "$\\Phi''+(4/x)\\Phi'+\\Phi=0$",
          sp.simplify(sp.diff(Phi, x, 2) + (4/x) * sp.diff(Phi, x) + Phi) == 0)
    check('is even in $x$, as the paper states', sp.simplify(Phi.subs(x, -x) - Phi) == 0)
    check('and tends to 1 as $x\\to0$, so the normalisation is fixed', sp.limit(Phi, x, 0) == 1)
    check('with the source removed exactly: the paper writes the free equation after $\\Theta_0+\\Phi$',
          'removes the source exactly' in p15)

    # ⓶ the projection is calibrated
    check('⛭⛭ ⓷ and the projection is calibrated: "$\\ell_{*}=D_{M}/r_{s}=302.2$ against the measured '
          '$301$"',
          '302.2' in p15 and '301' in p15)

    # ⓷ the ratio, recomputed
    # ** r6931+70.1 (PO-59): CLASS (a) -- this pair was passing VACUOUSLY at head and failed at r6774
    #    (`91751daa`).  The paper's $r$ in this formula is no longer 1.082: the branch-point handover
    #    (r6770+66.3, "the onset was a repair") and the common visibility-peak endpoint (r6797) put it
    #    at $r=0.992$, a RISE of about two per cent at $\\ell_D$ (sentence landed `2da9b74a`, merged
    #    at r6921), where 1.082 was the fitted-onset configuration's ratio.  The old pin
    #    `'1.082' in p15` came green again only because r6795/r6801 (`1cb0c1be`, `a21467b0`) added an
    #    unrelated "a ratio of $1.082$ gives $160$" sentence -- a bare number held the check up.  *** The finding (a C_l ratio with no free parameter is in the paper) is unchanged; the
    #    pin now binds the formula to its stated $r$ and the recomputation to the paper's stated
    #    size.  The 1.082 / 0.844 arithmetic is kept below as the value the paper carried then. ***
    r = 0.992          # ** RE-PINNED c54.223 (`L-557`) -- was 1.093; then 1.082; r6931+70.1: 0.992 **
    ratio = float(np.exp(-(1.0**2) * (r**2 - 1)))
    _then = float(np.exp(-(1.082**2 - 1)))
    check('⛭⛭⛭ ⓸ and a $C_\\ell$ ratio with no free parameter is already in the paper: '
          '"$C_{\\ell}^{\\rm CR}/C_{\\ell}^{\\Lambda\\rm CDM}=\\exp[-(\\ell/\\ell_{D})^{2}(r^{2}-1)]$ with '
          '$r=\\theta_{D}/\\theta_{*}$", and at the visibility peak "$r=0.992$"',
          'The high-$\\ell$ consequence follows with no free parameter' in p15
          and 'with $r=\\theta_{D}/\\theta_{*}$' in p15
          and 'visibility function, $r=0.992$, it is a rise of about two per cent at $\\ell_{D}$' in p15)
    check(f'and recomputing it at $\\ell=\\ell_D$ gives {ratio:.3f} -- the paper\'s "rise of about two '
          f'per cent" (at the retired $r=1.082$ it was {_then:.3f}, the old $0.84$)',
          abs(ratio - 1.016) < 0.002 and abs(_then - 0.844) < 0.002)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT (r6931+70.1): ** DISCHARGED -- the absolute spectrum is RUN (r6719) and the ratio's r is")
    print("     now 0.992 (a ~2% rise at l_D).  What follows is the r2658 finding as it stood: **")
    print("  ** PO-12's step ② is smaller than its framing. **")
    print('  ⓵ ** Six of the transfer\'s eight pieces are computed: ** the driving in closed form (verified')
    print('     here: satisfies its ODE, even in x, normalised at x=0), exact source removal, the')
    print('     amplitude at horizon entry, r_s = 146.4 Mpc, the diffusion scale 10.8% longer, and')
    print('     R_b = 0.60.')
    print('  ⛭⛭ ⓶ ** And the projection is calibrated: ** l_* = D_M/r_s = 302.2 against the measured 301')
    print('     -- ** the k -> l map\'s one CR-specific input, within 0.4%. **')
    print('  ⛭⛭⛭ ⓷ ** And a C_l RATIO with no free parameter is already in the paper: **')
    print('     C_l^CR/C_l^LCDM = exp[-(l/l_D)^2 (r^2-1)], r = 1.082 ⇒ ** 0.844 at l_D, matching its')
    print('     stated 0.84. **')
    print('     ⇒⇒ *** That is exactly the shape r2647 identified as the transfer-free route -- SAME')
    print('       multipole, two rates.  The route is not merely available; it has been walked at C_l')
    print('       level. ***')
    print('  ⇒ ⓸ ** So what remains is the ABSOLUTE spectrum ** -- the visibility-weighted line-of-sight')
    print('     integral turning Theta(k) into C_l itself rather than into a ratio.  ** The bespoke part')
    print('     is the PHYSICS, and the physics is built. **')
    print('  ⌗ ** And that reframes PO-10\'s gate: ** its odd/even PATTERN needs the absolute spectrum and')
    print('    stays gated; ** any observable expressible as a CR/LCDM ratio at fixed l does not. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
