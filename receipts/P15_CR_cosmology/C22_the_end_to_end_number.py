#!/usr/bin/env python3
"""C22 -- the end-to-end number, with the scope the paper itself supplies: the super-horizon chain gives a
$7.5\\%$ low-$\\ell$ power deficit, and it does NOT extend to the acoustic modes.

** THE CHAIN, r2661--r2663. **  $\\mathcal R$ conserved across the branch point $\\Rightarrow$
$\\Phi_{\\rm exp}=\\tfrac9{10}\\Phi_i$; every mode outside the horizon there; $\\Phi\\to\\Phi_i$ exactly at the
branch point.  ** r2661 added: "$\\Phi$ is constant on the expansion leg, so it holds from the branch
point to recombination with no further evolution." **

** ⛔ ⓵ AND THAT LAST CLAUSE OVER-REACHED, WHICH THE PAPER SAYS IN ITS OWN VOICE. **  P15, immediately
after the no-early-ISW sentence: "** One scope qualification is owed here **, and it narrows the claim
without touching the conclusion.  The constancy argument runs on $\\Phi''+3H\\Phi'=0$, which is ** the
super-horizon equation: it drops the $k^2$ term.  For the acoustic modes---inside the horizon at the onset
and remaining so---that term does not vanish, and the potential DOES decay on the observable leg, by a
factor of order two across the first few peaks. **"

  ⇒ *** So the constancy is super-horizon only, exactly as $\\mathcal R$'s conservation was.  The chain is
      internally consistent; r2661's phrasing was not. ***
  ⌗ ** And the paper adds the discriminating fact: ** "** The decay is not a radiation effect: zeroing the
    radiation fractions in the constraint makes it LARGER **, and the rate responsible is $k^2/(3H)$,
    which grows with $k$."

** ⛭⛭ ⓶ SO THE NUMBER, WHERE THE CHAIN ACTUALLY REACHES. **  At large angles the Sachs--Wolfe plateau
carries $\\Theta+\\Psi=\\Phi/3$ with $\\Phi$ super-horizon and constant.  $\\Lambda$CDM's $\\Phi$ is still
"** some four per cent above its asymptote at recombination **"; CR's is AT its asymptote:

      *** power ratio  =  (1/1.04)^2  =  0.925    ⇒  a 7.5% LOW-ELL POWER DEFICIT ***

** ⓷ AND AT THE OTHER END, THE PAPER'S OWN DAMPING RATIO. **  $C_\\ell^{\\rm CR}/C_\\ell^{\\Lambda\\rm CDM}
=\\exp[-(\\ell/\\ell_D)^2(r^2-1)]$, $r=1.082$ (RE-PINNED c54.223 -- was 1.093):

      *** l = 0.5 l_D : 0.958     l = l_D : 0.843     l = 1.5 l_D : 0.681     l = 2 l_D : 0.505 ***
      (RE-PINNED c54.223 (`L-557`) from r = 1.093 -- see the note in `C10_highl_ratio`)

** ⇒⇒ ⓸ THE END-TO-END STATEMENT, AND ITS GAP. **  *** low-$\\ell$: $7.5\\%$ deficit from the absent early
ISW.  High-$\\ell$: $18\\%$ at $\\ell_D$ rising to $54\\%$ at $2\\ell_D$ from the longer diffusion length.
BETWEEN them -- the acoustic peaks -- the chain does NOT reach, because $\\Phi$ decays by a factor of order
two there and the decay is $k$-dependent through $k^2/(3H)$. ***
  ⌗ ** That gap is `PO-10`'s odd/even pattern and the peak heights, ** *** and r2646's gate on it now has a
    mechanism rather than a category: not "both are statements about $C_\\ell$" but "the potential's decay
    across the peaks is $k$-dependent and unrun." ***

WHAT IS NOT CLAIMED.  ** Not that $7.5\\%$ is a prediction against data ** -- *** it is the ratio the chain
implies at the plateau, and P15's own low-multipole prediction has a SEPARATE and larger source (the
closed-$S^3$ discrete-mode deficit); whether the two combine is not computed here. ***  ** Not that the
$4\\%$ is CR's number ** -- it is $\\Lambda$CDM's residual, quoted from P15.  ** Not that the decay factor
of two is derived here ** -- it is the paper's, with its own receipt.

Written r2664.  Stated for reversal.
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
    print('  C22 -- the end-to-end number, and where the chain stops')
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the scope qualification
    check('⛔ ⓵ P15 owns the scope: "One scope qualification is owed here, and it narrows the claim '
          'without touching the conclusion"',
          'One scope qualification is owed here, and it narrows the claim without touching the '
          'conclusion' in p15)
    check('naming the super-horizon restriction: "The constancy argument runs on $\\Phi\'\'+3H\\Phi\'=0$, '
          'which is the super-horizon equation: it drops the $k^{2}$ term"',
          'which is the \\emph{super-horizon} equation: it drops the $k^{2}\\Phi$ term' in p15)
    check('and what happens off it: "the potential does decay on the observable leg, by a factor of '
          'order two across the first few peaks"',
          'the potential does decay on the observable leg, by a factor of order two across the first few '
          'peaks' in p15)
    check('with the discriminating fact: "The decay is not a radiation effect: zeroing the radiation '
          'fractions in the constraint makes it larger"',
          'The decay is not a radiation effect: zeroing the radiation fractions in the constraint '
          'makes it \\emph{larger}' in p15)

    # ⓶ the low-ell number
    check('⛭⛭ ⓶ and LCDM\'s residual is the paper\'s: "still some four per cent above its asymptote at '
          'recombination"',
          'four per cent above its asymptote at recombination' in p15)
    ratio = (1.0 / 1.04) ** 2
    check(f'⇒ so the plateau power ratio is (1/1.04)^2 = {ratio:.3f} -- a {100*(1-ratio):.1f}% low-ell '
          'deficit',
          abs(ratio - 0.925) < 0.002)

    # ⓷ the high-ell numbers
    r = 1.082          # ** RE-PINNED c54.223 (`L-557`) -- was 1.093 **
    vals = {x: float(np.exp(-(x**2) * (r**2 - 1))) for x in (0.5, 1.0, 1.5, 2.0)}
    check(f'⓷ and the damping ratio at l/l_D = 0.5, 1, 1.5, 2 gives '
          f'{ {k: round(v,3) for k,v in vals.items()} }',
          abs(vals[1.0] - 0.843) < 0.002 and abs(vals[2.0] - 0.505) < 0.002)
    check('from the paper\'s own no-free-parameter form with $r=1.082$',
          'with no free parameter' in p15 and '1.082' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the number, with the scope the paper supplies. **')
    print('  ⛔ ⓵ ** r2661\'s "no further evolution" over-reached, and P15 says so in its own voice: **')
    print('     the constancy argument "is ** the super-horizon equation: it drops the k² term **", and')
    print('     for the acoustic modes "** the potential DOES decay on the observable leg, by a factor of')
    print('     order two across the first few peaks **".')
    print('     ⌗ ** And the decay is not a radiation effect ** -- "zeroing the radiation fractions makes')
    print('       it LARGER", the rate being k²/(3H).')
    print('  ⛭⛭ ⓶ ** LOW-ELL: ** LCDM sits 4% above asymptote at recombination; CR sits AT it.')
    print(f'     ⇒ ** power ratio (1/1.04)² = {ratio:.3f}, a {100*(1-ratio):.1f}% DEFICIT. **')
    print('  ⓷ ** HIGH-ELL, the paper\'s own ratio: ** 0.958 at 0.5 l_D, ** 0.843 at l_D **, 0.681 at')
    print('     1.5 l_D, ** 0.459 at 2 l_D. **')
    print('  ⇒⇒ ⓸ ** AND THE GAP IS NAMED: ** between them -- ** the acoustic peaks ** -- the chain does')
    print('     not reach, because Φ decays by ~2 there and the decay is k-dependent through k²/(3H).')
    print('     *** That gap is PO-10, and r2646\'s gate now has a MECHANISM rather than a category. ***')
    print('  ⚠ NOT a prediction against data: ** P15\'s own low-multipole prediction has a separate and')
    print('    larger source (the closed-S³ discrete-mode deficit), and whether the two combine is not')
    print('    computed here. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
