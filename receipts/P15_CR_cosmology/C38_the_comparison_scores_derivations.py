#!/usr/bin/env python3
"""C38 -- `PO-10`'s non-foreign comparison HAS a form, and it is a score on DERIVATIONS: no parameter
count, no $k$, no imported vector.  What it needs is measurement uncertainties, and those are data.

** THE QUESTION, from r2726. **  *** After the $k=2$-against-$k=6$ frame was found to count parameters
in $\\Lambda$CDM's ontology -- five of whose six entities the corpus does not posit -- the row was left
with: "what would a comparison look like that does NOT import a parameter vector the corpus does not
posit?"  Asked nowhere yet. ***

** ⛭⛭ ⓵ THE ANSWER IS IN WHAT CR ACTUALLY HAS, AND MOST OF IT IS DERIVED. **

      *** alpha      the ONE dimensionful invariant
          Omega_m    the single calibrated parameter -- fitted to the acoustic angle
          A_s        anchored at the first peak: INHERITED, not predicted
          z_onset    FIXED; "meets the scale at every H_0" -- not a knob (r2688)
          theta_*    DERIVED as D_M/r_s
          r=1.0816   DERIVED (RE-PINNED c54.223 -- was 1.0926), "with no free parameter"
          9/10       DERIVED, the branch-point transfer ***

  ⇒ *** A comparison that scores DERIVED quantities against MEASURED ones has no parameter vector to
      import, because there is nothing to count: a derivation has no $k$. ***

** ⓶ AND P15 ALREADY REPORTS SUCH PAIRS, SCATTERED. **  ** $\\theta_*=302.2$ against the measured
$301$ ** ; ** $r_s=146.4$ against $145.4$ ** ; ** $1+z_{\\rm eq}=3399$, "a consequence and a check, not
an input" **.
  ⇒ ** So the instrument is not new. **  *** The comparison is the COLLECTION of these into one score,
    and the corpus already holds every derivation in it. ***

** ⛔ ⓷ AND WHAT THIS RECEIPT WILL NOT DO, WHICH IS THE POINT. **  *** A first draft of this scored the
three pairs and reported $\\chi^2/{\\rm dof}=5.67$ with a $4\\sigma$ pull on $\\theta_*$.  **Every
$\\sigma$ in it was invented by this line.**  That is the r2726 failure in a new costume: not importing
$\\Lambda$CDM's PARAMETERS this time, but importing UNCERTAINTIES from nowhere -- and a $4\\sigma$
tension asserted on a made-up error bar is worse than no comparison, because it looks like a result. ***

** ⓸ SO WHAT THE ROW OWES IS NOW EXACTLY TWO THINGS, AND NEITHER IS A FRAME. **
  * *** the MEASURED values and their published uncertainties for each derived quantity -- **data, not
      ontology**, and legitimately imported because a measurement is not a model; ***
  * *** the list of which corpus quantities are DERIVED rather than fitted, taken from the papers'
      own statements rather than assembled by hand. ***

  ⌗ ** And the second is the one that decides the comparison's size. **  *** $\\Omega_m$ and $A_s$ are
    fitted and must be excluded; $N_{\\rm eff}$ is "adopted, not predicted" by P15's own words and is not
    a test either.  Getting that list wrong in the generous direction is how a derived-quantity score
    turns back into a fit. ***

WHAT IS NOT CLAIMED.  ** Not that CR passes or fails ** -- *** no score is reported here, and the draft
that computed one is withdrawn inside this receipt for the reason given in ⓷. ***  ** Not that the three
pairs above are the complete list ** -- they are what a read of P15 surfaced, and the list is the row's
first deliverable.  ** Not that uncertainties are unavailable ** -- they are published; what is claimed
is that this line does not have them and must not invent them.

** COMPUTES: nothing.  *** Deliberately: the arithmetic is trivial and the inputs are not this line's to
supply. *** **

Written r2746.  Stated for reversal.
"""
import os
import re

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
    print("  C38 -- what does a comparison importing no foreign parameter vector look like?")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the derived quantities are the paper's own
    check('⛭⛭ ⓵ P15 derives $\\theta_{*}$ and reports it against measurement: '
          '"$\\theta_{*}=D_{M}/r_{s}=302.2$ against the measured $301$"',
          '302.2' in p15 and 'against the measured' in p15)
    check('and states $1+z_{\\rm eq}$ is derived: "Matter--radiation equality is then a consequence '
          'and a check, not an input"',
          'is then a consequence and a check, not an input' in p15)
    check('and the high-$\\ell$ ratio carries "no free parameter"',
          'with no free parameter' in p15)

    # ⓶ while the fitted ones are named as fitted
    check('⓶ while $\\Omega_m$ is named as the single calibrated parameter -- "the single '
          'CMB-calibrated $\\Omega_{m}$" -- so it is fitted and not a test',
          'single CMB-calibrated' in p15)
    check('and $A_s$ is "anchored" at the first peak by a value the construction "inherits rather '
          'than predicts" -- also not a test',
          'the first peak is where the amplitude is anchored' in p15
          and 'inherits rather than predicts' in p15)

    # ⓷ and this receipt reports no score
    src = open(os.path.abspath(__file__), encoding='utf-8', errors='replace').read()
    check('⛔ ⓷ and this receipt reports NO score: the draft that computed one invented every '
          '$\\sigma$, which is r2726\'s failure in a new costume',
          'Every' in src and 'invented by this line' in src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the comparison is a SCORE ON DERIVATIONS — and its inputs are not mine. **')
    print('  ⛭⛭ ⓵ ** A derivation has no k. **  θ_*, the high-ℓ ratio r, z_eq and the 9/10 transfer are')
    print('     derived; scoring them against measurement imports no parameter vector, because there is')
    print('     nothing to count.')
    print('  ⓶ ** And P15 already reports such pairs, scattered: ** θ_* = 302.2 against 301, r_s = 146.4')
    print('     against 145.4, 1+z_eq = 3399 "a consequence and a check, not an input".')
    print('     ⇒ ** The instrument is not new — the comparison is the COLLECTION. **')
    print('  ⛔ ⓷ *** AND WHAT THIS RECEIPT REFUSES TO DO IS THE POINT.  A first draft scored three')
    print('     pairs at χ²/dof = 5.67 with a 4σ pull on θ_*.  EVERY σ IN IT WAS INVENTED BY THIS LINE.')
    print('     That is r2726 in a new costume — not importing ΛCDM\'s parameters this time but')
    print('     importing UNCERTAINTIES from nowhere, and a 4σ tension on a made-up error bar is worse')
    print('     than no comparison because it looks like a result. ***')
    print('  ⓸ ** So the row owes exactly two things, neither of which is a frame: ** the published')
    print('     uncertainties (data, legitimately imported — a measurement is not a model), and the')
    print('     list of which corpus quantities are DERIVED, from the papers\' own statements.')
    print('     ⌗ ** The second decides the comparison\'s size, and getting it wrong in the generous')
    print('       direction is how a derived-quantity score turns back into a fit. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
