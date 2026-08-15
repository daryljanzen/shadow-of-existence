#!/usr/bin/env python3
"""C39 -- ⛔ **CORRECTED r2758: THE FOURTH PAIR IS NOT A PAIR.**  *** The onset ratio "returns
1.99 ... the quoted value to one per cent, from standard thermodynamics" -- an IDENTITY on
$\\eta$ and $\\omega_m/\\omega_b$, both inherited.  **Same class as $N_{\\rm eff}$ and $A_s$, which
this receipt correctly excluded** -- and the receipt it was read from says so in the sentence
quoted.  See `C48_the_pairs_are_three`.  ⌗ *This receipt named the risk correctly ("the
exclusion list decides the comparison's size") and then took the generous read on the one entry
it had just discovered.*  ** What survives: the marker-phrase SEARCH METHOD, and the three
genuine pairs. ** ***

C39 -- `PO-10`'s derived-quantity list, taken from P15's OWN marker language: four pairs, each with
the paper's own accuracy statement attached, and each fitted quantity excluded by the paper's own words.

** THE OWED HALF. **  r2746 left the row owing two things: ** the published uncertainties ** (data, not
this line's) and ** the list of which corpus quantities are DERIVED rather than fitted, from the papers'
own statements **.  *** The second is a read of P15, and this is it. ***

** ⛭⛭ ⓵ THE FOUR PAIRS, EACH WITH P15's OWN ACCURACY CLAUSE. **

      *** theta_*      "theta_* = D_M/r_s = 302.2 against the measured 301"
          r_s          "returns r_s = 146.4 Mpc against 145.4 ... within 0.7% of each other"
          1+z_eq       "a consequence and a check, NOT AN INPUT --- 1+z_eq = 3399, exactly half
                        the onset"
          eta_ratio    "the ratio at onset is [...] which returns 1.99 at T_onset = 1.6 eV
                        --- THE QUOTED DATUM, TO ONE PER CENT" ***

  ⌗ ** The fourth was not in r2746's draft. **  *** It is the baryon-to-photon ratio at onset, and P15
    states its accuracy in the same breath as its value -- which is what makes it usable without this
    line supplying anything. ***

** ⓶ AND THE EXCLUSIONS ARE THE PAPER'S OWN, NOT A JUDGEMENT. **
  * ** $\\Omega_m$: ** "the single CMB-calibrated $\\Omega_m$" -- ** fitted **, and P15 says to what;
  * ** $A_s$: ** "the first peak is where the amplitude is anchored, by an $A_s$ this construction
    ** inherits rather than predicts **";
  * ** $N_{\\rm eff}$: ** adopted, and the corpus carries a receipt named for the fact that CR ** makes
    no $N_{\\rm eff}$ prediction **.
  ⇒ *** Three quantities excluded, each on a sentence the paper wrote about itself.  ** That is the
      test r2746 said decides the comparison's size, and it is decided by reading rather than by
      choosing. ** ***

** ⛭ ⓷ AND ONE MORE THE PAPER MARKS AS DERIVED WITHOUT A MEASURED PARTNER. **  *** The high-$\\ell$
ratio: "the high-$\\ell$ consequence follows ** with no free parameter **", $r=1.0816$ (RE-PINNED c54.223 -- was 1.0926).  It has no
single measured number to sit against -- it is a spectrum-shape prediction -- so it belongs in the
comparison as a SHAPE test rather than a pair, and r2725 already established that scoring it wrongly is
how the last attempt failed. ***

** ⓸ SO THE ROW'S REMAINING DEBT IS NOW ONE ITEM. **  *** The derived list is read and the exclusions
are the paper's own.  What is still owed is the published uncertainties for four measured values --
$301$, $145.4$, the equality redshift, and the onset ratio -- which are data and not this line's to
invent (r2746). ***

WHAT IS NOT CLAIMED.  ** Not that the four pairs are scored ** -- *** no $\\chi^2$ here, for r2746's
reason: every $\\sigma$ would be invented. ***  ** Not that the list is exhaustive ** -- it is what P15's
own marker language surfaces; another paper may mark more.  ** Not that the high-$\\ell$ ratio is
excluded ** -- it is derived and belongs in the comparison, as a shape rather than a pair.

** COMPUTES: nothing.  *** A read of P15 for its own derived/fitted markers. *** **

Written r2747.  Stated for reversal.
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
    print("  C39 -- which quantities does P15 itself mark as derived?")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the four pairs, each with the paper's own accuracy clause
    check('⛭⛭ ⓵ $\\theta_*$: "$\\theta_{*}=D_{M}/r_{s}=302.2$ against the measured $301$"',
          '302.2' in p15 and 'against the measured' in p15)
    check('$r_s$: "returns $r_{s}=146.4$Mpc against $145.4$ ... within $0.7\\%$ of each other"',
          '146.4' in p15 and 'within $0.7\\%$ of each other' in p15)
    check('$1+z_{\\rm eq}$: "a consequence and a check, not an input---$1+z_{\\rm eq}=3399$, exactly '
          'half the onset"',
          'is then a consequence and a check, not an input' in p15 and '3399' in p15)
    check('and the onset ratio -- NOT in r2746\'s draft: "which returns $1.99$ at '
          '$T_{\\rm onset}=1.6$eV---the quoted datum, to one per cent"',
          'returns $1.99$ at $T_{\\mathrm{onset' in p15
          and 'the quoted datum, to one per' in p15)

    # ⓶ the exclusions are the paper's own
    check('⓶ and the exclusions are P15\'s own words: $\\Omega_m$ is "the single CMB-calibrated" one',
          'single CMB-calibrated' in p15)
    check('and $A_s$ is anchored "by an $A_{s}$ this construction inherits rather than predicts"',
          'inherits rather than predicts' in p15)

    # ⓷ the shape test
    check('⛭ ⓷ while the high-$\\ell$ ratio is derived without a measured partner: "the high-$\\ell$ '
          'consequence follows with no free parameter"',
          'consequence follows with no free parameter' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the derived list is READ — four pairs, three exclusions, all P15\'s own. **')
    print('  ⛭⛭ ⓵ ** FOUR PAIRS, each with the paper\'s own accuracy clause attached: **')
    print('       theta_*   302.2 against the measured 301')
    print('       r_s       146.4 Mpc against 145.4, "within 0.7% of each other"')
    print('       1+z_eq    3399, "a consequence and a check, NOT AN INPUT"')
    print('       eta       1.99 at T_onset=1.6 eV, "the quoted datum, TO ONE PER CENT"')
    print('     ⌗ ** The fourth was not in r2746\'s draft ** — and P15 states its accuracy in the same')
    print('       breath as its value, which is what makes it usable without this line supplying')
    print('       anything.')
    print('  ⓶ ** And the exclusions are the paper\'s own sentences, not a judgement: ** Ω_m "the single')
    print('     CMB-calibrated", A_s "inherits rather than predicts", N_eff adopted.')
    print('     ⇒ *** That is the test r2746 said decides the comparison\'s size — decided by READING')
    print('       rather than by choosing. ***')
    print('  ⛭ ⓷ ** And the high-ℓ ratio is derived with no measured partner ** — a SHAPE test, not a')
    print('     pair, and r2725 established that scoring it wrongly is how the last attempt failed.')
    print('  ⇒ ⓸ ** So the row owes ONE item: ** the published uncertainties for four measured values.')
    print('    ** Data, and not this line\'s to invent. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
