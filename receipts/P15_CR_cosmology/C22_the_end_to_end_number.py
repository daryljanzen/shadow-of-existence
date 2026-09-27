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
=\\exp[-(\\ell/\\ell_D)^2(r^2-1)]$, $r=1.082$ (RE-PINNED c54.223 -- was 1.093); ** r6931+70.3: the paper now carries $r=0.992$, a two per cent RISE at $\\ell_D$, so
 the numbers below are the retired fitted-onset configuration's, kept as arithmetic **:

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
import subprocess
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
    # ⛔⛭⛭ AMENDED r4518: ** THE PREMISE UNDER THIS NUMBER WAS WITHDRAWN BY THE PAPER. **  The
    #    sentence quoted here is P15's, and the contrast it served -- $\Lambda$CDM's $\Phi$ four per
    #    cent above asymptote against CR's AT its asymptote -- was retracted by `PO-24` (r4502,
    #    narrowed r4505): *"The early integrated Sachs--Wolfe contribution is present here, and the
    #    step that once denied it is worth setting out because the denial was an inference and not
    #    a measurement"*, measured at $0.348$ on the leaf congruence and $0.229$ on the stacking
    #    rate, non-zero on BOTH.  ⇒ *** So the $7.5\%$ low-$\ell$ deficit is an arithmetic
    #    consequence of a premise the paper no longer holds.  The arithmetic is kept -- it is
    #    correct arithmetic and it is what this receipt computed -- and it is LABELLED as resting on
    #    the withdrawn contrast rather than presented as a live prediction. ***
    _P15_THEN = re.sub(r'\s+', ' ', subprocess.run(
        ['git', 'show', '09d594f5^:corpus/CR_cosmology.tex'],
        cwd=ROOT, capture_output=True, text=True, errors='replace').stdout)
    _p15f = re.sub(r'\s+', ' ', p15)
    check('⛭⛭ ⓶ᵃ and LCDM\'s residual WAS the paper\'s, read where it stood (09d594f5^): "still some '
          'four per cent above its asymptote at recombination"',
          len(_P15_THEN) > 100000
          and 'four per cent above its asymptote at recombination' in _P15_THEN)
    check('⛔ ⓶ᵇ AND THE CR HALF OF THAT CONTRAST IS WITHDRAWN: P15 now measures the early ISW at '
          '$0.348$ on the leaf congruence and $0.229$ on the stacking rate, "non-zero on both", so '
          'CR\'s $\\Phi$ is NOT at its asymptote.  ** The deficit below follows from the old premise '
          'and is kept as arithmetic, not as a live prediction. **',
          'The early integrated Sachs--Wolfe contribution is present here' in _p15f
          and 'Non-zero on both' in _p15f)
    ratio = (1.0 / 1.04) ** 2
    check(f'⇒ so the plateau power ratio ON THE WITHDRAWN PREMISE is (1/1.04)^2 = {ratio:.3f} -- a '
          f'{100*(1-ratio):.1f}% low-ell deficit.  *Correct arithmetic from a contrast the paper no '
          f'longer draws.*',
          abs(ratio - 0.925) < 0.002)

    # ⓷ the high-ell numbers
    r = 1.082          # ** RE-PINNED c54.223 (`L-557`) -- was 1.093 **
    vals = {x: float(np.exp(-(x**2) * (r**2 - 1))) for x in (0.5, 1.0, 1.5, 2.0)}
    check(f'⓷ and the damping ratio at l/l_D = 0.5, 1, 1.5, 2 gives '
          f'{ {k: round(v,3) for k,v in vals.items()} }',
          abs(vals[1.0] - 0.843) < 0.002 and abs(vals[2.0] - 0.505) < 0.002)
    # ** r6931+70.3 (PO-60, the vacuous green): THIS CHECK WAS HELD UP BY A BARE NUMBER.  Class (a).
    #    `'1.082' in p15` has not matched the paper's no-free-parameter form since the fitted onset
    #    was retired (r6770+66.3) and the common visibility-peak endpoint set the ratio at $r=0.992$
    #    (sentence landed `2da9b74a`, merged at r6921).  It stayed green on three OTHER sentences --
    #    "a ratio of $1.082$ gives $160$", "$1.50$ per bin at a ratio of $1.082$", "seven tenths at
    #    $1.082$" -- which quote 1.082 as the counterfactual configuration.  *** So the pin now binds
    #    the formula to the r the paper states, and the arithmetic above is labelled as the retired
    #    configuration's, which is what C16's repair (r6931+70.1) did for the same number. ***
    r_now = 0.992
    at_lD = float(np.exp(-(r_now**2 - 1)))
    check('⓷ the arithmetic above is at the RETIRED $r=1.082$ (the fitted-onset configuration); the '
          'paper\'s no-free-parameter form now carries "$r=0.992$", a RISE of about two per cent at '
          f'$\\ell_D$ -- recomputed here as {at_lD:.3f}',
          'The high-$\\ell$ consequence follows with no free parameter' in p15
          and 'visibility function, $r=0.992$, it is a rise of about two per cent at $\\ell_{D}$' in p15
          and abs(at_lD - 1.016) < 0.002)

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
    print('  ⛔ ⓶ ** LOW-ELL, ON A PREMISE THE PAPER HAS WITHDRAWN: ** the contrast was LCDM 4% above')
    print('     asymptote against CR AT it.  ** PO-24 (r4502/r4505) MEASURED the early ISW instead of')
    print('     inferring it: 0.348 on the leaf congruence, 0.229 on the stacking rate, non-zero on')
    print('     BOTH ** -- so CR is not at its asymptote and the contrast is gone.')
    print(f'     ⇒ the arithmetic that followed, kept as arithmetic and not as a prediction:')
    print(f'       power ratio (1/1.04)² = {ratio:.3f}, a {100*(1-ratio):.1f}% deficit ON THAT PREMISE.')
    print('  ⓷ ** HIGH-ELL, at the RETIRED r = 1.082 (r6931+70.3): ** '
          + ', '.join(f'{v:.3f} at {k} l_D' for k, v in vals.items()) + '.')
    print(f'     ** At the paper\'s current r = 0.992 the ratio at l_D is {at_lD:.3f} -- a rise, not a')
    print('     deficit. **  The low/high contrast below was drawn on the retired configuration.')
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
