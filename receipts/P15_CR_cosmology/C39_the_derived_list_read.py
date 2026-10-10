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
                        (r6931+70.1: now "fixed by the same epoch", and "equality falls within a
                        couple of per cent of flat LCDM's with nothing fitted to a spectrum" --
                        the onset, and 3399 with it, left P15 at r6772)
          eta_ratio    "the ratio at onset is [...] which returns 1.99 at T_onset = 1.6 eV
                        --- THE QUOTED DATUM, TO ONE PER CENT" ***
                        (r6931+70.1: NOT A PAIR -- r2758's correction above; P15 now says the same:
                        the amplitude "follows from standard thermodynamics alone" and is "not a
                        feature of this construction")

  ⌗ ** The fourth was not in r2746's draft. **  *** It is the baryon-to-photon ratio at onset, and P15
    states its accuracy in the same breath as its value -- which is what makes it usable without this
    line supplying anything. ***

** ⓶ AND THE EXCLUSIONS ARE THE PAPER'S OWN, NOT A JUDGEMENT. **
  * ** $\\Omega_m$: ** "the single CMB-calibrated $\\Omega_m$" -- ** fitted **, and P15 says to what;
    (r6931+70.1: "CMB-calibrated" was P15's error, corrected at r6625; it is the epoch $x_0$ "which
    the rate carries and the baryon-acoustic data fix" -- fitted still, to the distances)
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
          '146.4$~Mpc against $145.4$ on the radiation-i' in p15 and 'within $0.7\\%$ of each other' in p15)
    # ** r6931+70.1: STALE (c).  Pinned "a consequence and a check, not an input---$1+z_{\\rm
    #   eq}=3399$, exactly half the onset", removed by `caaf3481` (r6772+66.3) when P15 dropped the
    #   fitted onset for the branch-point handover.  z_eq is still marked derived and still carries
    #   the paper's own accuracy clause, now against LCDM rather than against the onset: "Matter--
    #   radiation equality is then fixed by the same epoch" (the abstract-level summary) and, in
    #   sec:tensions, "equality falls within a couple of per cent of flat $\\Lambda$CDM's with
    #   nothing fitted to a spectrum".  ** Same pair, same marker; the "half the onset" relation and
    #   the number 3399 went with the onset and are not re-pinned. **
    check('$1+z_{\\rm eq}$: "Matter--radiation equality is then fixed by the same epoch", and '
          '"equality falls within a couple of per cent of flat $\\Lambda$CDM\'s with nothing fitted '
          'to a spectrum"',
          'Matter--radiation equality is then fixed by the same epoch' in p15
          and 'equality falls within a couple of per cent of flat $\\Lambda$CDM\'s with nothing '
              'fitted to a spectrum' in p15)
    # ** r6931+70.1: FROZE AN ERROR (a) -- and the error was this receipt's own, withdrawn in its
    #   header at r2758 ("THE FOURTH PAIR IS NOT A PAIR", see C48) while this check went on pinning
    #   the sentence that had been misread as a pair.  `de97f96e` (r6772+66.11) removed "which
    #   returns $1.99$ at $T_{\\rm onset}=1.6$eV---the quoted datum, to one per cent" with the rest
    #   of the fitted-onset reading, and P15 now states r2758's correction in its own words: the
    #   amplitude a start placed by hand would carry "is not a feature of this construction ... it
    #   follows from standard thermodynamics alone", and "with the plasma handed over at the branch
    #   point there is no such start and no such amplitude".  ** So the check is re-pointed at the
    #   IDENTITY -- the reason the fourth entry is excluded -- rather than at a pair that is not one. **
    check('and the onset ratio is NOT a fourth pair (r2758): P15 says the amplitude at a placed start '
          '"follows from standard thermodynamics alone", "not a feature of this construction", and '
          'that with the branch-point handover "there is no such start and no such amplitude"',
          'is not a feature of this construction either' in p15
          and 'h of which the composition inherits regardless, it follows from standard thermodynamics alone, $[1' in p15
          and 'there is no such start and no such amplitude' in p15)

    # ⓶ the exclusions are the paper's own
    # ** r6931+70.1: FROZE AN ERROR (a), same site as C38 ⓶.  "the single CMB-calibrated" was
    #   P15's wrong adjective (its body fits Omega_m to the distances), corrected by `174202ab`
    #   (r6625) and restated at r6772 as the epoch x_0 "which the rate carries and the
    #   baryon-acoustic data fix".  ** The exclusion is still P15's own sentence, and still says
    #   fitted -- only now to the right data. **
    check('⓶ and the exclusions are P15\'s own words: $\\Omega_m$ is the epoch "which the rate '
          'carries and the baryon-acoustic data fix" -- fitted, to the distances',
          'The quantities this cosmology actually uses are the epoch $x_{0}$ (equivalently '
          '$\\Omega_m=2/(x_{0}^{3}+2)$' in p15
          and 't the offset itself, which the Nariai condition fixes at $\\alpha/\\sqrt3$}), which the rate carries and the baryon-acoustic data fix' in p15)
    check('and $A_s$ is anchored "by an $A_{s}$ this construction inherits rather than predicts"',
          's where the amplitude is anchored, by an $A_s$ this construction inherits rather than predicts' in p15)

    # ⓷ the shape test
    check('⛭ ⓷ while the high-$\\ell$ ratio is derived without a measured partner: "the high-$\\ell$ '
          'consequence follows with no free parameter"',
          'consequence follows with no free parameter' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    # r6931+70.1: the verdict carried r2747's four pairs after r2758 withdrew the fourth, and
    # P15's "CMB-calibrated"; both corrected here to what the checks above now establish.
    print('  VERDICT: ** the derived list is READ — three pairs, and the exclusions are P15\'s own. **')
    print('  ⛭⛭ ⓵ ** THREE PAIRS, each with the paper\'s own accuracy clause attached: **')
    print('       theta_*   302.2 against the measured 301')
    print('       r_s       146.4 Mpc against 145.4, "within 0.7% of each other"')
    print('       1+z_eq    "fixed by the same epoch", "within a couple of per cent of flat LCDM\'s"')
    print('     ⛔ ** r2747 read a FOURTH, the onset ratio, and it is not a pair (r2758, C48): ** an')
    print('       identity on inherited η and ω_m/ω_b — and P15 now says so, "from standard')
    print('       thermodynamics alone", "not a feature of this construction".')
    print('  ⓶ ** And the exclusions are the paper\'s own sentences, not a judgement: ** Ω_m the epoch')
    print('     "the baryon-acoustic data fix", A_s "inherits rather than predicts", N_eff adopted.')
    print('     ⇒ *** That is the test r2746 said decides the comparison\'s size — decided by READING')
    print('       rather than by choosing. ***')
    print('  ⛭ ⓷ ** And the high-ℓ ratio is derived with no measured partner ** — a SHAPE test, not a')
    print('     pair, and r2725 established that scoring it wrongly is how the last attempt failed.')
    print('  ⇒ ⓸ ** So the row owes ONE item: ** the published uncertainties for three measured values (r6931+70.1: was four, r2758).')
    print('    ** Data, and not this line\'s to invent. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
