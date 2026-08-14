#!/usr/bin/env python3
"""D3 -- ⛔⛔ **THIS RECEIPT'S CONCLUSION IS WITHDRAWN, r2671.**  Its arithmetic stands; its physics does
not.  *** The floor DOES survive, and P10 has said so since r2419. ***

** WHAT WENT WRONG. **  This receipt quoted P10 through "...the cubic and higher self-interactions enter
at the same inverse-square order at the origin" ** and stopped there **.  *** Four sentences on, in the
same paragraph, P10's own voice: "So the cubic term's apparent unboundedness is an artefact of
truncation: $\\pi^2(1-\\lambda\\varphi+\\cdots)$ is the expansion of $\\pi^2/(1+\\lambda\\varphi)$, whose
full coefficient is positive wherever the metric is non-degenerate" -- carrying
`\\rcpt{P10_gamma_hat_is_bounded_below}`, which passes. ***

  ⇒ ** This line's OWN r2632 rule: check the sentence after the one you quote. **  *** Third time this
      session, and the first time it cost a physics conclusion rather than a caveat. ***

** VERIFIED INDEPENDENTLY BEFORE ACCEPTING (r2671, per `INGESTION.md`): ** the series
$\\pi^2/(1+\\lambda\\varphi)=\\pi^2(1-\\lambda\\varphi+\\lambda^2\\varphi^2-\\cdots)$ checked termwise to
eighth order -- *** this receipt's "square times a signed field" IS its first-order term ***; and on
200,000 identical points the truncation reaches ** $-209.5$ ** while the resummed coefficient ** never
falls below $\\gamma=0.25$ **.  *** A truncation of a positive function is not a statement about the
function. ***

** WHAT STANDS. **  ** The arithmetic below is correct as arithmetic ** -- $\\gamma+\\pi^2(c+g_3\\varphi)$
does run to $-\\infty$ for signed $\\varphi$.  *** What it is not is $\\hat\\Gamma$. ***  ** And P10's own
scope is preserved: ** "the positivity speaks only of the interior, the degenerate boundary being what
the thermal condition above is for."

  ⌗ ** The checks are left RUNNING and PASSING ** -- they assert what the paper says about the truncation,
  and every one of them is true.  *** It is the VERDICT that was wrong, and it is struck here rather than
  the file deleted, so the error stays legible. ***

--- ORIGINAL DOCSTRING, RETAINED ---

`PO-6`'s floor question has a determinate answer at the order the paper names: $\\hat\\Gamma$ is
NOT bounded below once the cubic enters, and the condition is explicit.

** THE QUESTION, narrowed to one thing at r2619. **  P10 leaves it open in its own voice: "** whether the
complete $\\hat\\Gamma$ is bounded below is part of what this paragraph leaves open at its end, and is not
assumed here **".

** ⓵ AND THE PAPER NAMES EXACTLY WHAT ENTERS. **  "At leading order $\\hat\\Gamma=\\gamma+c\\sum_n
\\hat\\pi_n^2$; but ** the cubic and higher self-interactions enter at the same inverse-square order at the
origin ($\\pi_n^2\\phi_m/a^3$ in kind) **, so the complete boundary coefficient is the singular
p[art] ..."

  ⇒ *** So the completed operator is not a sum of squares.  It is a sum of squares PLUS a term of the form
      $\\hat\\pi^2\\hat\\phi$ -- and that changes the sign structure, not just the magnitude. ***

** ⛭⛭ ⓶ AND THAT TERM IS UNBOUNDED BELOW, BY INSPECTION OF ITS OWN FORM. **  Grouping,

      *** Gamma = gamma + pi^2 (c + g3 * phi) ***

  * ** $\\hat\\pi^2\\ge0$ ** -- it is a square;
  * ** $\\hat\\phi$ takes EITHER SIGN ** -- it is a field amplitude, not a modulus.

  ⇒⇒ *** So the coefficient of $\\pi^2$ turns NEGATIVE wherever $\\phi<-c/g_3$, and on that region
      $\\hat\\Gamma\\to-\\infty$ as $\\pi^2$ grows.  Sampled numerically over $200{,}000$ points at
      $\\gamma=0.25,\\;c=g_3=1$: minimum $-209$, and unbounded as the range widens. ***

** ⓷ SO THE ANSWER TO `PO-6`'s FLOOR QUESTION IS NO, AT THE ORDER THE PAPER ITSELF NAMES. **  *** The
"sum of squares" that makes the leading-order spectrum bounded below by $\\gamma$ is destroyed by the first
correction, because the correction is not a square -- it is a square times a signed field. ***

  ⌗ ** AND THIS IS WHY THE DECOMPOSITION WAS BUILT NOT TO NEED IT. **  r2619 found P10 saying the
  direct-integral decomposition "uses only that both sides of the threshold are occupied, ** and not that
  the spectrum has a floor **".  *** That caution now reads as foresight rather than modesty: the floor
  does not survive, and the construction was arranged so that nothing rests on it. ***

WHAT IS NOT CLAIMED.  ** Not that the interacting theory is ill-defined ** -- *** an operator unbounded
below is a standard situation and the question is what fixes the state, not whether the operator has a
minimum. ***  ** Not that the numerical sampling is the argument ** -- it illustrates; the argument is
that $\\pi^2\\phi$ is a square times a signed field.  ** Not that $g_3$'s magnitude is known ** -- the
paper gives the KIND ($\\pi_n^2\\phi_m/a^3$) and not the coefficient, and *** the conclusion needs only
that the coefficient is non-zero and $\\phi$ signed. ***

Written r2651.  Stated for reversal.
"""
import os
import re

import numpy as np

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
    print('  D3 -- is the complete Gamma-hat bounded below?')
    print()
    p10 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'canonical_time.tex')))

    # ⓵ the paper's own statement of the question and of what enters
    check('⓵ P10 leaves it open: "whether the complete $\\hat\\Gamma$ is bounded below is part of what '
          'this paragraph leaves open at its end, and is not assumed here"',
          'is part of what this paragraph leaves open at its end' in p10)
    check('and gives the leading order: "At leading order $\\hat\\Gamma=\\gamma+c\\sum_n\\hat\\pi_n^2$"',
          'At leading order $\\hat\\Gamma=\\gamma+c\\sum_n\\hat\\pi_n^2$' in p10)
    check('⛭⛭ and names what enters beyond it: "the cubic and higher self-interactions enter at the same '
          'inverse-square order at the origin ($\\pi_n^2\\phi_m/a^3$ in kind)"',
          'the cubic and higher self-interactions enter at the same inverse-square order at the origin'
          in p10 and '\\pi_n^2\\phi_m/a^3$ in kind' in p10)

    # ⓶ the sign structure
    rng = np.random.default_rng(0)
    gamma, c, g3 = 0.25, 1.0, 1.0
    vals = []
    for _ in range(200000):
        pi = rng.normal(0, 1.5)
        phi = rng.normal(0, 3.0)
        vals.append(gamma + pi**2 * (c + g3 * phi))
    lo = min(vals)
    check(f'⓶ and grouped as $\\gamma+\\pi^2(c+g_3\\phi)$ the sampled minimum is {lo:.1f} -- negative',
          lo < 0)
    check('because $\\pi^2\\ge0$ is a square while $\\phi$ takes either sign, so the coefficient of '
          '$\\pi^2$ turns negative wherever $\\phi<-c/g_3$',
          (gamma + 4.0 * (c + g3 * (-2.0 * c / g3))) < 0)
    check('and the divergence is in $\\pi^2$: at $\\phi=-2c/g_3$, $\\Gamma=\\gamma-c\\pi^2$',
          abs((gamma + 100.0 * (c + g3 * (-2.0 * c / g3))) - (gamma - c * 100.0)) < 1e-9)

    # ⓷ why the decomposition was built not to need it
    check('⓷ and P10 built the decomposition not to need it: it "uses only that both sides of the '
          'threshold are occupied, and not that the spectrum has a floor"',
          'uses only that both sides of the threshold are occupied' in p10
          and 'not that the spectrum has a floor' in p10)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  ⛔⛔ VERDICT WITHDRAWN r2671.  ** The floor DOES survive. **  P10, four sentences past')
    print('  the quotation below: "the cubic term\'s apparent unboundedness is an artefact of')
    print('  truncation: pi^2(1 - lam*phi + ...) is the expansion of pi^2/(1 + lam*phi), whose full')
    print('  coefficient is positive wherever the metric is non-degenerate."')
    print('  *** The arithmetic below is right about the TRUNCATION and wrong about Gamma-hat. ***')
    print('  ⓵ ** Leading order is a sum of squares: ** Gamma = gamma + c*sum(pi_n^2) >= gamma.')
    print('  ⛭⛭ ⓶ ** But the paper names what enters next: ** "the cubic and higher self-interactions')
    print('     enter at the same inverse-square order ... ** (pi_n^2 phi_m / a^3 in kind) **".')
    print('     ⇒ ** Grouped: Gamma = gamma + pi^2 (c + g3 phi). **  pi^2 is a SQUARE; phi is a signed')
    print('       FIELD AMPLITUDE.  ** So the coefficient of pi^2 turns negative wherever phi < -c/g3,')
    print('       and Gamma -> -infinity as pi^2 grows. **')
    print('  ⓷ ** AND THAT IS WHY THE DECOMPOSITION WAS BUILT NOT TO NEED IT. **  P10: it "uses only that')
    print('     both sides of the threshold are occupied, ** and not that the spectrum has a floor **".')
    print('     *** That caution reads as foresight rather than modesty: the floor does not survive, and')
    print('     the construction was arranged so nothing rests on it. ***')
    print('  ⚠ NOT claimed: that the interacting theory is ill-defined.  ** An operator unbounded below is')
    print('    a standard situation; the question is what fixes the STATE. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
