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
    check('⓵ the debt is framed as a build: "This is a genuine build, not a plug-in"',
          'This is a genuine build, not a plug-in' in p15)

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
    r = 1.082          # ** RE-PINNED c54.223 (`L-557`) -- was 1.093; see the note below **
    ratio = float(np.exp(-(1.0**2) * (r**2 - 1)))
    check('⛭⛭⛭ ⓸ and a $C_\\ell$ ratio with no free parameter is already in the paper: '
          '"$C_{\\ell}^{\\rm CR}/C_{\\ell}^{\\Lambda\\rm CDM}=\\exp[-(\\ell/\\ell_{D})^{2}(r^{2}-1)]$ with '
          '$r=1.082$"',
          'with no free parameter' in p15 and '1.082' in p15)
    check(f'and recomputing it at $\\ell=\\ell_D$ gives {ratio:.3f}, matching the paper\'s $0.84$',
          abs(ratio - 0.84) < 0.005)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-12's step ② is smaller than its framing. **")
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
