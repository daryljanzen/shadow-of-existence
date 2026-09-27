#!/usr/bin/env python3
"""C33 -- the model-selection comparison set up against the literature, with r2709's parameter count
CORRECTED: CR is $k=2$, not $k=1$, and the verdict survives it by a factor of three.

** WHY THIS EXISTS. **  r2709 established that `PO-10`'s half ① is an AIC/BIC comparison and computed
$\\Delta$BIC $=26.9$ at $k=1$ against $k=6$.  *** Reading the standard literature corrected two things and
the corpus corrected a third. ***

** ⛔ ⓵ THE PARAMETER COUNT WAS WRONG, AND P15 SAYS SO. **  r2709 put CR at $k=1$ on "$\\theta_*$ is
fixed by $\\Omega_m$ alone".  ** But a TT likelihood scores $C_\\ell$, which carries an amplitude: ** P15,
"the first peak is where the amplitude is ** anchored, by an $A_s$ this construction inherits rather than
predicts **", and "** the framework paper's scoping of this as a ONE-PARAMETER ACCOMMODATION stands
unchanged **".

  ⇒ *** Anchored to the data IS fitted.  The CR arm carries $\\Omega_m$ AND $A_s$: $k=2$. ***

** ⛭⛭ ⓶ AND THE LITERATURE SUPPLIES THE INTERPRETATION SCALE, WHICH r2709 DID NOT HAVE. **  Liddle
(2004), quoting Jeffreys (1961): ** a $\\Delta$BIC of 2 is POSITIVE evidence and 6 or more is STRONG
evidence ** against the model with the larger value.
  ⌗ ** And Liddle's own count is 5, not 6: ** "a minimal description of the Universe requires just five
  fundamental parameters" -- with $n=1$ held.  *** At Planck precision $n_s\\ne1$ is significant, so 6 is
  right for a modern comparison; both are computed below because the choice must be stated with the
  result. ***

** ⓷ THE TABLE, and the verdict is robust across every count: **

      *** N = 215 TT bins        dAIC = 2(k_L - k_C)      dBIC = (k_L - k_C) ln N

          CR k=1 vs LCDM k=5 :  dAIC  8.0   dBIC 21.5   STRONG
          CR k=1 vs LCDM k=6 :  dAIC 10.0   dBIC 26.9   STRONG      <- r2709's, wrong k_C
          CR k=2 vs LCDM k=5 :  dAIC  6.0   dBIC 16.1   STRONG
          CR k=2 vs LCDM k=6 :  dAIC  8.0   dBIC 21.5   STRONG      <- the corrected pair ***

  ⇒⇒ *** At the honest count the threshold is $\\Delta$BIC $=21.5$, which is still ** three and a half
      times ** the "strong evidence" line.  The correction moved the number by five and did not touch the
      conclusion. ***

** ⓸ AND THE AICc CORRECTION IS NEGLIGIBLE HERE. **  $2k(k+1)/(N-k-1)$ at $N=215$: ** $0.06$ at $k=2$
and $0.40$ at $k=6$ **, so the second-order form shifts $\\Delta$AIC by $0.34$.  *** Worth computing
because the literature warns it matters when $N$ is small relative to $k$; here it does not. ***

WHAT IS NOT CLAIMED.  ** Not that CR is preferred ** -- *** nothing here scores a $\\chi^2$.  What is
established is the RULE and the THRESHOLD: CR is preferred on BIC unless its best-fit $\\chi^2$ exceeds
flat $\\Lambda$CDM's by more than $21.5$. ***  ** Not that $k=2$ is final ** -- if a refit touches $n_s$ or
the baryon density the count rises again, and the count must be stated with any result.  ** Not that BIC
settles it ** -- Liddle notes AIC and BIC can disagree and that AIC "tends to favour models which have
more parameters than the true model"; here they agree.

Written r2710.  Stated for reversal.

** r6931+70.1 (PO-59) -- THE COUNT IS SETTLED BY THE CORPUS, AND NOT AT $k=2$ AGAINST $6$. **  *** The refit
P15 runs frees the same four parameters in each arm with the amplitude in closed form (r6799), and P15
states that no information criterion separates them (r6811): at equal $k$ the penalty difference is zero,
so this receipt's threshold ($\\Delta$BIC $21.5$) is the arithmetic of a count asymmetry the corpus no longer
carries.  And the $\\chi^2$ "nothing here scores" is scored: the arm at $1.57$ times the control. ***  The
Jeffreys scale, the table and the AICc arithmetic stand as arithmetic.
"""
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
N = 215


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
    print('  C33 -- the comparison set up properly, with the parameter count corrected')
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the count correction
    check('⛔ ⓵ P15 puts the amplitude in the fit: "the first peak is where the amplitude is anchored, '
          'by an $A_{s}$ this construction inherits rather than predicts"',
          'the first peak is where the amplitude is anchored' in p15)
    # ** r6931+70.1 (PO-59): CLASS (c), STALE.  `b27e8293` (r6772+66.24, "the transmission accommodation
    #    brought to what the paper carries") rewrote "the framework paper's scoping of this as a
    #    one-parameter accommodation stands unchanged" as "the inherited quantity is $P_{\\Psi}$ and the
    #    map from it to $A_{s}$ is derived, so what the construction takes from the progenitor here is
    #    the potential power and nothing about the map".  *** Same finding for this check: the amplitude
    #    is ONE quantity taken from outside, not derived -- so it is counted.  Re-pinned to the new
    #    sentence's load-bearing clause. ***
    check('and names what is taken from outside: "what the construction takes from the progenitor here is '
          'the potential power and nothing about the map"',
          'one-parameter accommodation stands unchanged' not in p15
          and 'That factor is computed rather than fitted: the inherited quantity is $P_{\\Psi}$' in p15
          and 'what the construction takes from the progenitor here is the potential power and nothing '
              'about the map' in p15)
    # ** r6931+70.1 (PO-59): CLASS (a) THEN (b).  "fitted to the acoustic angle" -- the fitted onset,
    #    which this receipt read as the arm's first fitted quantity -- went at `caaf3481` (r6772+66.3)
    #    when the onset was retired as a repair (r6770+66.3).  *** And the count question this receipt
    #    corrected from $k=1$ to $k=2$ was then settled by the corpus in a different way: the refit
    #    frees THE SAME FOUR parameters in each arm with the amplitude in closed form (`2007dc1e`,
    #    r6799), "so no information criterion separates them" (`8a627481`, r6811) -- equal $k$, so the
    #    threshold this receipt computed (ΔBIC 21.5) is not the comparison's; and the $\\chi^2$ it said
    #    "nothing here scores" IS scored: the arm at $1.57$ times the control. ***  So the check follows
    #    both: the amplitude still fitted ("anchored"), the counts equal, and the number scored.
    #    Passed at r6502 (`b96e1a49`). **
    check('⇒ [corrected r6772+66.3, settled r6799/r6811] the CR arm does carry $A_s$ as fitted ("anchored" at '
          'the peak) -- but not against $k=6$: the refit frees "the expansion rate, the matter and baryon '
          'densities and the tilt" in EACH arm, amplitude in closed form, "so no information criterion '
          'separates them", and the $\\chi^2$ is scored: the arm at $1.57$ times the control',
          'fitted to the acoustic angle' not in p15
          and 'the first peak is where the amplitude is anchored' in p15
          and 'With the expansion rate, the matter and baryon densities and the tilt free in each arm and '
              'the amplitude in closed form' in p15
          and 'The two arms fit the same four parameters, so no information criterion separates them' in p15
          and "\\emph{the arm at $1.57$ times the control's distance" in p15)

    # ⓶ the table
    rows = {}
    for kc in (1, 2):
        for kl in (5, 6):
            rows[(kc, kl)] = (2*(kl-kc), (kl-kc)*np.log(N))
    check(f'⛭⛭ ⓶ at the corrected pair (CR $k=2$, $\\Lambda$CDM $k=6$): $\\Delta$AIC '
          f'{rows[(2,6)][0]:.1f}, $\\Delta$BIC {rows[(2,6)][1]:.1f}',
          abs(rows[(2, 6)][1] - 21.5) < 0.1)
    check('and every count in the table clears the Jeffreys "strong evidence" line of 6',
          all(b >= 6 for _, b in rows.values()))
    check(f'while r2709\'s figure was {rows[(1,6)][1]:.1f} -- the correction moved it by '
          f'{rows[(1,6)][1]-rows[(2,6)][1]:.1f} and did not touch the conclusion',
          abs(rows[(1, 6)][1] - rows[(2, 6)][1] - 5.4) < 0.1)

    # ⓸ AICc
    aicc = {k: 2*k*(k+1)/(N-k-1) for k in (2, 6)}
    check(f'⓸ and the AICc correction is negligible at $N={N}$: {aicc[2]:.2f} at $k=2$ against '
          f'{aicc[6]:.2f} at $k=6$, shifting $\\Delta$AIC by {aicc[6]-aicc[2]:.2f}',
          aicc[6] - aicc[2] < 0.5)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (r6931+70.1): ** SETTLED DIFFERENTLY BY THE CORPUS -- the refit frees the same four')
    print('     parameters in each arm (r6799) and no information criterion separates them (r6811); the')
    print('     chi^2 is scored at 1.57x the control.  The r2710 table as it stood: **')
    print('  ** the threshold is 21.5, not 26.9 — and the verdict survives by 3.5x. **')
    print('  ⛔ ⓵ ** r2709\'s k=1 was wrong and P15 says so: ** "the first peak is where the amplitude is')
    print('     ** anchored **, by an A_s this construction inherits rather than predicts", and the')
    print('     framework scopes it as ** a one-parameter accommodation **.  ** Anchored to the data IS')
    print('     fitted. **  ⇒ CR carries Ω_m AND A_s: ** k = 2. **')
    print('  ⛭⛭ ⓶ ** And the literature supplies the scale r2709 lacked ** — Liddle 2004 quoting')
    print('     Jeffreys: ** ΔBIC of 2 is POSITIVE evidence, 6 or more is STRONG **.')
    print('     ⌗ Liddle\'s own count is 5 (with n=1 held); at Planck precision 6 is right, and both are')
    print('       tabled because the choice must be stated with the result.')
    print('  ⓷ ** THE TABLE: **')
    for (kc, kl), (a, b) in sorted(rows.items()):
        mark = '   <- corrected' if (kc, kl) == (2, 6) else ('   <- r2709' if (kc, kl) == (1, 6) else '')
        print(f'       CR k={kc} vs ΛCDM k={kl}:  ΔAIC {a:>4.1f}   ΔBIC {b:>5.1f}   STRONG{mark}')
    print('     ⇒⇒ *** At the honest count the threshold is ΔBIC = 21.5 — still THREE AND A HALF TIMES')
    print('       the strong-evidence line.  The correction moved the number by 5.4 and did not touch')
    print('       the conclusion. ***')
    print(f'  ⓸ ** AICc negligible here: ** {aicc[6]-aicc[2]:.2f} shift at N={N}.')
    print('  ⚠ ** Nothing here scores a χ². **  What is established is the RULE and the THRESHOLD.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
