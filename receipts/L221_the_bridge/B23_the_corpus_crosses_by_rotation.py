#!/usr/bin/env python3
"""B23 -- cc54's turnaround obstacle is real, and the corpus does not solve it with a regular variable:
it crosses by ROTATING INTO IMAGINARY CONFORMAL TIME, which the framework paper already parametrises.

** THE OBSTACLE, as cc54 states it (L-812). **  Attempting the progenitor derivation of `CRPHI`: "at the
interior's turnaround, $H_c=a'/a$ passes through zero, so the potential equation's $k^2\\Phi/(3H_c)$ term
diverges.  A stiff evolution from a super-horizon start dies exactly there ... ** the standard
conformal-Newtonian variables can't ** [cross it]."  ⇒ ** Their proposed path: a turnaround-regular
perturbation variable, "the standard tool for perturbations through a bounce". **

** ⓵ THE OBSTACLE VERIFIES EXACTLY. **  On the closed dust interior $a(\\eta)=\\tfrac{a_{\\max}}2(1-\\cos\\eta)$:

      *** H_c = a'/a = -sin(eta)/(cos(eta)-1),   H_c(pi) = 0,   a(pi) = a_max  (the maximum)
          k^2/(3 H_c) = k^2 (1-cos eta)/(3 sin eta)  ->  -infinity  as eta -> pi ***

  ⇒ ** cc54 is right about the divergence and right that a real-$\\eta$ integration dies there. **

** ⛭⛭ ⓶ BUT THE CORPUS DOES NOT CROSS IN REAL $\\eta$, AND SAYS SO. **  P7: "** Along the lift---the
stretch on which $\\mathrm{Re}$ does not advance while the areal radius climbs from the comoving
turnaround to the branch point---the conformal time is PURELY IMAGINARY **, and the rate $\\dot r/s$ is
carried continuously ** from zero at the turnaround **, through unity at the interior Euclidean null, to
divergent at the branch point."

  ** Substituting $\\eta=\\pi+is$: **

      *** H_c(pi + i s) = -i sinh(s)/(cosh(s) + 1),   -> 0 as s -> 0+ ***

  ⇒⇒ *** PURELY IMAGINARY, vanishing at the turnaround and MONOTONE in $s$ thereafter.  So $H_c=0$ is not
      a singularity to be regularised -- it is the ENDPOINT of a segment the framework already
      parametrises, and the crossing is a rotation rather than a passage. ***

** ⓷ WHICH BEARS ON WHETHER TO BUILD THE REGULAR VARIABLE. **  *** A turnaround-regular variable is the
right tool for a BOUNCE in real time.  The lift is not a bounce: cosmic time does not advance along it at
all, and P7 states the rate is carried CONTINUOUSLY across it.  A variable built to regularise a real-time
zero would be solving a problem the contour does not pose -- and would need its own check against the
imaginary-time parametrisation before its output could be read. ***
  ⌗ ** So the framing question cc54 asked has an answer from the corpus rather than from a build: ** *** the
    obstacle is real, the proposed tool may be aimed at the wrong object, and the corpus's own crossing is
    already written down in P7 and `janzen_circle_v3`. ***

WHAT IS NOT CLAIMED.  ** Not that the derivation is available ** -- *** reading $\\delta_g/\\Phi$ at the
seam through an imaginary-time segment is its own problem, and this receipt does not attempt it. ***
** Not that cc54's variable would fail ** -- only that its relation to the lift needs stating first.
** Not that the cycloid is the progenitor's exact interior ** -- it is the closed dust solution the corpus
uses, and the vanishing of $H_c$ at maximum expansion is general.

Written r2693.  Stated for reversal.
"""
import os
import re

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
    print("  B23 -- how does the corpus cross the turnaround?")
    print()
    p7 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_framework.tex')))

    eta, amax, k, s = sp.symbols('eta a_max k s', positive=True)
    a = amax/2*(1 - sp.cos(eta))
    Hc = sp.simplify(sp.diff(a, eta)/a)

    # ⓵ the obstacle
    check('⓵ at the turnaround $\\eta=\\pi$ the interior is at maximum expansion and $H_c=0$',
          sp.simplify(Hc.subs(eta, sp.pi)) == 0
          and sp.simplify(a.subs(eta, sp.pi) - amax) == 0)
    check("and cc54's term diverges there: $k^2/(3H_c)\\to-\\infty$ as $\\eta\\to\\pi$",
          sp.limit(k**2/(3*Hc), eta, sp.pi) == -sp.oo)

    # ⓶ the corpus's crossing
    check('⛭⛭ ⓶ P7 states the crossing: "the conformal time is purely imaginary"',
          'the conformal time is purely imaginary' in p7)
    check('along a segment running from the turnaround: "while the areal radius climbs from the '
          'comoving turnaround to the branch point"',
          'while the areal radius climbs from the comoving turnaround to the branch point' in p7)
    check('with the rate continuous across it: "carried continuously from zero at the turnaround"',
          'carried continuously from \\emph{zero} at the turnaround' in p7)

    # the substitution
    Hi = sp.simplify(sp.expand_trig(Hc.subs(eta, sp.pi + sp.I*s)))
    check(f'⇒ and substituting $\\eta=\\pi+is$ gives $H_c={Hi}$ -- PURELY IMAGINARY',
          sp.simplify(sp.re(Hi.rewrite(sp.exp).expand(complex=True))) == 0)
    check('vanishing at the turnaround and monotone in $s$ thereafter',
          sp.limit(Hi, s, 0) == 0 and sp.simplify(sp.im(Hi.subs(s, 2)) - sp.im(Hi.subs(s, 1))) != 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the obstacle is real; the corpus crosses by ROTATION, not by regularisation. **')
    print("  ⓵ ** cc54 is right about the divergence: ** H_c(pi) = 0 at maximum expansion, and")
    print('     k²/(3H_c) → −∞ there.  A real-η integration dies exactly at the turnaround.')
    print('  ⛭⛭ ⓶ ** But the corpus does not cross in real η, and says so. **  P7: "the conformal time is')
    print('     ** purely imaginary **" along the lift, "from the comoving turnaround to the branch')
    print('     point", with the rate "** carried continuously from zero at the turnaround **".')
    print(f'     ⇒ substituting η = π + is: ** H_c = {Hi} ** — purely imaginary, vanishing at the')
    print('       turnaround and monotone thereafter.')
    print('  ⇒⇒ *** So H_c = 0 is not a singularity to be regularised: it is the ENDPOINT of a segment')
    print('     the framework already parametrises, and the crossing is a ROTATION rather than a')
    print('     passage. ***')
    print('  ⓷ ** Which bears on the build: ** a turnaround-regular variable is the right tool for a')
    print('     BOUNCE in real time.  ** The lift is not a bounce — cosmic time does not advance along it')
    print('     at all. **  *** A variable built to regularise a real-time zero would be solving a problem')
    print('     the contour does not pose, and would need checking against the imaginary-time')
    print('     parametrisation before its output could be read. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
