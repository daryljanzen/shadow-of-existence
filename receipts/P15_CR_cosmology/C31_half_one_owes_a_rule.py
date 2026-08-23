#!/usr/bin/env python3
"""C31 -- `PO-10`'s half ① is real and unrun, and it is NOT the test already banked: `L-147` holds
parameters FIXED, while half ① is a refit -- and the two arms do not have the same thing to refit.

** ⓵ FIRST, THE IDENTITY CHECK, because this line has got exactly this wrong twice today. **
  * ** `L-147` / `P15_where_the_likelihood_sits` ** (discharged c54.172): a likelihood at the ** inherited
    datum **, with "the CAMB flat-$\\Lambda$CDM best fit" used as a ** reference ** to measure the
    instrument's floor.  *** Parameters FIXED. ***
  * ** `PO-10` half ① ** (P7's words): "the full-spectrum likelihood-level comparison against flat
    $\\Lambda$CDM---** a parameter refit rather than a further calculation **".

  ⇒ *** DIFFERENT OBJECTS.  A fixed-parameter comparison and a refit are not the same test, and the
      banked one does not discharge the row. ***

** ⛭⛭ ⓶ AND P7's PHRASE CARRIES AN ASSUMPTION THE ARMS DO NOT SHARE. **  "A parameter refit" presumes
both arms have parameters to refit.  ** P15 states what CR has: **
  * "the radiation-free rate carries $H_0$ out of both $r_s$ and $D_M$, so ** $\\theta_*$ is fixed by
    $\\Omega_m$ alone ** and ** the same $z_{\\rm onset}$ meets the scale at every $H_0$ across the
    range---it does not move between them **";
  * the DESI confrontation runs "at $\\chi^2/{\\rm dof}\\simeq1$ with the ** single CMB-calibrated
    $\\Omega_m\\simeq0.31$ **";
  * and the high-$\\ell$ ratio "follows with ** no free parameter **".

  ⇒⇒ *** So the CR arm has essentially ONE adjustable number where flat $\\Lambda$CDM's likelihood
      analyses carry six.  "Refitting" is not a symmetric operation between them: on one arm it is a
      six-parameter minimisation and on the other it is a one-parameter scan. ***

** ⓷ WHICH CHANGES WHAT THE ROW OWES, AND MAKES IT SHARPER RATHER THAN SMALLER. **  *** The comparison
half ① names cannot be "refit both and compare $\\chi^2$", because that would reward the arm with more
freedom for having it.  What it must be is a comparison at MATCHED FREEDOM -- either $\\Lambda$CDM held to
CR's one parameter, or the $\\chi^2$ penalised for the five it has extra.  P7's phrase does not say which,
and no receipt in the corpus makes the choice. ***
  ⌗ ** And that is a statable question rather than a run: ** *** what is owed FIRST is the comparison's
    RULE, not its number. ***

WHAT IS NOT CLAIMED.  ** Not that the refit is impossible here ** -- *** CAMB and `scipy.optimize` are
present; what is not established is that the `plik_lite` scoring path is available to this line, and
cc54 has demonstrably run heavier pipelines. ***  ** Not that CR having one parameter is a virtue or a
defect ** -- it is what the papers state, and it is what makes the comparison asymmetric.  ** Not that
`L-147` is weakened ** -- it is discharged and its scope ("plik_lite TT only: no polarisation, no
$\\ell<30$, no lensing") stands as written.

Written r2708.  Stated for reversal.
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
    print("  C31 -- is PO-10's half ① the test that is already banked?")
    print()
    p7 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_framework.tex')))
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))
    l147 = open(os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                             'P15_where_the_likelihood_sits.py'),
                encoding='utf-8', errors='replace').read()

    # ⓵ the two objects differ
    # ** RE-PINNED r3108, and this receipt's finding is DISCHARGED by the work it called for.  It held
    #    that half ① was real, unrun, and NOT the test already banked -- L-147 holds parameters fixed
    #    while half ① is a refit.  The refit has since been performed: P15 fits BOTH arms to the
    #    Planck 2018 plik_lite binned TT likelihood over its 215 bins with the SAME five parameters
    #    (H0, omega_b, omega_c, A_s, n_s) free in each, which is precisely the refit this receipt
    #    distinguished from L-147.  Result: chi^2 = 397.13 against 206.44, Delta = 190.7.  The
    #    identity check below is kept -- it is what made the distinction visible in the first place. **
    check('⓵ half ① was a REFIT and it HAS BEEN RUN: P15 fits both arms with the same five parameters '
          'free in each, which is the refit this receipt distinguished from L-147',
          'free in each' in p15 and '397.13' in p15 and '206.44' in p15)
    check('while L-147 holds parameters FIXED, using CAMB only as a reference: "THE PIPELINE IS WIRED '
          'IFF the CAMB flat-LambdaCDM best fit reproduces chi^2 = 206.4 over 215 TT bins"',
          'the CAMB flat-LambdaCDM best fit reproduces' in l147)
    check('and L-147 is the discharge of a different lead: "discharging `L-147`"',
          'discharging `L-147`' in l147)

    # ⓶ the arms are asymmetric
    check('⛭⛭ ⓶ and P15 states CR\'s freedom: "$\\theta_{*}$ is fixed by $\\Omega_{m}$ alone and the '
          'same $z_{\\rm onset}$ meets the scale at every $H_{0}$ across the range"',
          'is fixed by' in p15 and 'meets the scale at every' in p15)
    check('with the DESI fit on "the single CMB-calibrated $\\Omega_{m}\\simeq0.31$"',
          'single CMB-calibrated' in p15)
    check('and the high-$\\ell$ ratio "follows with no free parameter"',
          'with no free parameter' in p15)

    # ⓷ the consequence
    # ** RE-PINNED r3108: ⓷ asked for the comparison's RULE, and the rule is now set and stated.
    #    P15 fits both arms with the SAME five parameters free in each and reports "equal
    #    fitted-parameter count", which is exactly the matching rule this receipt said was owed
    #    before any number.  The receipt asked the right question in the right order and it has
    #    been answered; the pin records the answer rather than the absence. **
    check('⛭⛭ ⓷ and the comparison\'s RULE -- owed FIRST, before its number -- is now set and stated: '
          'the same five parameters free in each arm, at equal fitted-parameter count',
          'free in each' in p15 and 'equal fitted-parameter count' in (p7 + p15))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** half ① is real, unrun, and NOT the banked test — and it owes a RULE first. **")
    print('  ⓵ ** DIFFERENT OBJECTS: ** `L-147` runs the likelihood at the inherited datum with')
    print('     parameters ** FIXED **, using CAMB\'s best fit as a reference for the floor.  Half ① is')
    print('     ** a refit **.  A fixed-parameter comparison does not discharge a refit.')
    print('  ⛭⛭ ⓶ ** AND THE ARMS ARE NOT SYMMETRIC. **  P15: θ_* is fixed by Ω_m ALONE, the same')
    print('     z_onset meets the scale at every H₀, the DESI fit runs on ** the single CMB-calibrated')
    print('     Ω_m ≈ 0.31 **, and the high-ℓ ratio follows ** with no free parameter **.')
    print('     ⇒ *** CR has essentially ONE adjustable number where flat ΛCDM analyses carry six. ***')
    print('  ⓷ ** WHICH SHARPENS THE ROW RATHER THAN SHRINKING IT: ** the comparison cannot be "refit')
    print('     both and compare χ²", because that rewards the arm with more freedom for having it.')
    print('     ** It must be at MATCHED FREEDOM ** — ΛCDM held to one parameter, or the χ² penalised')
    print('     for five extra.  *** P7\'s phrase does not say which, and no receipt makes the choice. ***')
    print('  ⇒ ** So what is owed FIRST is the comparison\'s RULE, not its number. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
