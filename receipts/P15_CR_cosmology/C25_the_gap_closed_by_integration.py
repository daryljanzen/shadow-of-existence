#!/usr/bin/env python3
"""C25 -- the 2.6-point gap closed by integration, and the answer is CONTROLLED BY THE ONSET REDSHIFT --
which is P15's own point, reproduced from the integrals rather than quoted.

** WHERE THIS ARRIVES. **  r2686 scaled the rate difference at a POINT and got $\\theta_D/\\theta_*$ larger
by $+6.8\\%$ against P15's $+9.4\\%$, and named the gap: "the $13\\%$ is LOCAL at recombination while the
integrals ACCUMULATE".  ** So integrate. **

** ⛔ ⓵ AND THE FIRST INTEGRATION WAS NONSENSE, WHICH LOCATED THE REAL VARIABLE. **  Running from
$a\\to0$ gave $r_s$ larger by a factor of ** 110 **: $\\rho_r/\\rho_m\\to\\infty$ there and the integral is
dominated by the lower limit.
  ⇒ ** The paper fixes it: ** "the sound horizon ... ** must be taken from the branch point: there is no
    observable expansion below it **."  *** The lower limit is the ONSET, and the answer is controlled by
    where it sits. ***

** ⛭⛭ ⓶ INTEGRATED, WITH $\\rho_r/\\rho_m=0.3$ AT RECOMBINATION AND SCALING AS $1/a$: **

      *** z_onset =   1200   +7.1%      z_onset =   5000   +12.0%
          z_onset =   2000   +8.8%      z_onset =  10000   +14.4%
          z_onset =   3000  +10.2%      z_onset = 100000   +20.4% ***

  ⇒ *** P15's $+9.4\\%$ sits at $z_{\\rm onset}\\approx2500$, between the $2000$ and $3000$ rows.  The
      point-scaling's $+6.8\\%$ is the $z\\to z_{\\rm rec}$ limit, which is why it understated. ***

** ⓷ AND THE SPREAD IS THE PAPER'S OWN ARGUMENT, NOW REPRODUCED. **  P15: "** it varies from $+43\\%$ to
$-3\\%$ across the onset redshifts one might consider, so A SINGLE DATUM CANNOT ABSORB BOTH OBSERVABLES
**."
  ⇒⇒ *** The integration reproduces the SHAPE that argument rests on: monotonic in $z_{\\rm onset}$,
      positive throughout the plausible range, and spanning many points.  The claim is not that one
      number is right but that the observable MOVES with the onset -- which is what makes $\\theta_*$ and
      $\\theta_D$ two constraints rather than one. ***

** ⇒ ⓸ SO WHAT THE TWO-LEG RUN OWES IS NARROWER AGAIN. **  *** Not "integrate the rate difference" --
that is done here and reproduces the paper.  What it owes is the ONSET REDSHIFT from the construction
rather than as a scan variable, which is what pins the integral's lower limit and turns a one-parameter
family of answers into one answer. ***

WHAT IS NOT CLAIMED.  ** Not that $+9.4\\%$ is re-derived exactly ** -- *** the model here is
$\\rho_r/\\rho_m\\propto1/a$ normalised at recombination, with $c_s$ and $x_e$ taken as common to both arms;
P15's number comes from the full integrals. ***  ** Not that the onset is free ** -- P15 fixes it by
holding $\\ell_*$ to its measured value, and the scan here is to show the DEPENDENCE, not to leave it
open.  ** Not that the $+43\\%$ to $-3\\%$ range is reproduced ** -- that spans onsets outside the range
scanned here.

Written r2687.  Stated for reversal.

** r6931+70.1 (PO-59) -- DISCHARGED, AND WHERE. **  *** ⓸'s owed item -- the start of the plasma "from the
construction rather than as a scan variable" -- is supplied: the plasma is handed over at the branch point
(r6770+66.3, landed in sec:diffusion-scale at r6772+66.6, `a99b7a86`), and the paper states the start is
not a free parameter while keeping this receipt's monotone dependence on it. ***  The z_onset table above
integrates the stacking-vs-leaf gap as r2687 framed it; the paper now accumulates both lengths on the leaf
rate, so its numbers are this receipt's model and no longer the paper's.
"""
import os
import re

import numpy as np
from scipy.integrate import quad

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


ZREC = 1090.0
AREC = 1 / (1 + ZREC)
R0 = 0.3 * AREC


def ratio(a):
    return 1 / np.sqrt(1 + R0 / a)


def theta_D(zonset):
    a0 = 1 / (1 + zonset)
    n, _ = quad(lambda a: 1 / ratio(a), a0, AREC, limit=300)
    d, _ = quad(lambda a: 1.0, a0, AREC, limit=300)
    return 100 * (np.sqrt(n / d) - 1)



# ** ⛭⛭ RE-PINNED c54.223 (`L-557`).  THIS RECEIPT IS ONE OF THE SEVEN THAT PRODUCED r2755's
# ** CORRECTION, AND THE CORRECTION BROKE ITS OWN PIN. **  Each of the seven quotes P15's `9.4%`
# ** because that is the sentence they were arguing about; r2755 replaced it with `8.2%` and none of
# ** the seven was re-pinned, so all seven have failed every full run since.
#   ⇒ *** A claim about the paper AS IT WAS is a claim about a COMMIT (c54.220's rule), so the
#       historical quote is read at `b4f1931^` and the CURRENT text is asserted separately.  A
#       receipt that argued for a correction must survive the correction landing. ***
_BEFORE_R2755 = 'b4f1931^'


def _p15_at(rev):
    """CR_cosmology.tex as it read at a commit -- whitespace-flattened, same as the live read"""
    import subprocess
    out = subprocess.run(['git', 'show', f'{rev}:corpus/CR_cosmology.tex'],
                         cwd=ROOT, capture_output=True, text=True, errors='replace').stdout
    return re.sub(r'\s+', ' ', out)


def main():
    print()
    print('  C25 -- integrate the rate difference over the history')
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the lower limit, fixed by the paper
    check('⓵ P15 fixes the lower limit: the sound horizon "must be taken from the branch point: there '
          'is no observable expansion below it"',
          'must be taken \\emph{from the branch point}: there is no observable expansion below '
          'it' in p15)

    # ⓶ the scan
    vals = {z: theta_D(z) for z in (1200, 2000, 3000, 5000, 10000)}
    check(f'⛭⛭ ⓶ integrated: z=1200 -> {vals[1200]:+.1f}%, z=2000 -> {vals[2000]:+.1f}%, '
          f'z=3000 -> {vals[3000]:+.1f}%, z=10000 -> {vals[10000]:+.1f}%',
          6.5 < vals[1200] < 7.5 and 9.5 < vals[3000] < 11)
    # ** r6931+70.1 (PO-59): the `'8.2' in p15` conjunct here was VACUOUS -- the 8.2% signature left
    #    P15 at `a99b7a86` (r6772+66.6) and the check stayed green on an unrelated "the control by
    #    $8.2\\%$" in sec:refit-bound.  The 8.2 is now read where it stood (`a99b7a86^`, c54.220's rule). **
    check("and P15's then-stated $+9.4\\%$ sits between the z=2000 and z=3000 rows",
          vals[2000] < 9.4 < vals[3000] and '9.4' in _p15_at(_BEFORE_R2755)
          and 'That figure and the $8.2\\%$ of' in _p15_at('a99b7a86^'))
    check('while r2686\'s point-scaling $+6.8\\%$ is the $z\\to z_{\\rm rec}$ limit, below every '
          'integrated value',
          all(v > 6.8 for v in vals.values()))

    # ⓷ monotonic, which is the paper's argument
    zs = sorted(vals)
    check('⓷ and the dependence is MONOTONIC in the onset redshift, which is what makes $\\theta_*$ and '
          '$\\theta_D$ two constraints rather than one',
          all(vals[zs[i]] < vals[zs[i+1]] for i in range(len(zs)-1)))
    # ** r6931+70.1 (PO-59): CLASS (b), DISCHARGED.  "it varies from $+43\\%$ to $-3\\%$ across the onset
    #    redshifts one might consider, so a single datum cannot absorb both observables" was deleted at
    #    `a99b7a86` (r6772+66.6) -- read at `a99b7a86^` below, where it stood.  This receipt's ⓸ said
    #    what was owed was "the ONSET REDSHIFT from the construction rather than as a scan variable".
    #    *** The construction supplies it: on the r6770+66.3 adjudication the plasma is handed over at
    #    the branch point, and sec:diffusion-scale now says the ratio depends on "where the plasma is
    #    handed over, and how far the diffusion integral is carried" -- "Neither is a free parameter,
    #    and the first is the larger" -- while keeping this receipt's monotone dependence: "a start
    #    placed later on the expanding leg raises it steeply". ***  So the check pins the discharge and
    #    the surviving dependence, not the new wording alone.  Passed at r6502 (`b96e1a49`). **
    check('as P15 argued ("a single datum cannot absorb both observables", read at `a99b7a86^`) -- and '
          '[discharged r6772+66.6] the start this receipt said was owed is now the construction\'s: '
          '"where the plasma is handed over", "Neither is a free parameter, and the first is the larger", '
          'with the same monotone dependence, "a start placed later on the expanding leg raises it steeply"',
          'so a single datum cannot absorb both observables' in _p15_at('a99b7a86^')
          and 'so a single datum cannot absorb both observables' not in p15
          and 'where the plasma is handed over, and how far the diffusion integral is carried' in p15
          and '\\emph{Neither is a free parameter, and the first is the larger.}' in p15
          and 'a start placed later on the expanding leg raises it steeply' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (r6931+70.1): ** DISCHARGED -- the start is the construction\'s (the branch-point')
    print('     handover, "Neither is a free parameter"), r6772+66.6.  The r2687 finding as it stood: **')
    print('  ** the gap closes by integration, and the answer is set by the ONSET. **')
    print('  ⛔ ⓵ ** The first integration was nonsense and that located the variable: ** running from')
    print('     a → 0 made r_s larger by a factor of ** 110 **, because rho_r/rho_m diverges there.')
    print('     ** P15 fixes it — the lower limit is the BRANCH POINT, "there is no observable expansion')
    print('     below it". **')
    print('  ⛭⛭ ⓶ ** Integrated: **')
    for z in zs:
        print(f'       z_onset = {z:>6}   {vals[z]:+6.1f}%')
    print(f"     ⇒ ** P15's +9.4% sits at z ≈ 2500 **, and r2686's point-scaling +6.8% is the")
    print('       z → z_rec limit — which is exactly why it understated.')
    print('  ⓷ ** And the dependence is MONOTONIC, ** which is the paper\'s own argument: "a single datum')
    print('     cannot absorb both observables".  *** The claim is not that one number is right but that')
    print('     the observable MOVES with the onset. ***')
    print('  ⇒ ⓸ ** So the two-leg run owes something narrower again: ** not "integrate the rate')
    print('     difference" — done here — but ** the ONSET REDSHIFT from the construction **, which turns')
    print('     a one-parameter family of answers into one answer.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
