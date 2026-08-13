#!/usr/bin/env python3
"""V1 -- the variational ledger's premise is false: the corpus USES the Einstein--Hilbert action four
times, including a second-order expansion, and names the field it is doing nowhere.

** THE LEDGER'S PREMISE, opened r1901 and standing since. **  `VARIATIONAL_LEDGER.md`: "** THE
VARIATIONAL LEDGER --- the field with no footprint at all **", opened from the r1890 hole survey, with
Daryl's r1891 adjudication that "all absences so far are circumstantial --- not a commitment, so the
route is available and unthrown."

  ⇒ *** The route was never thrown, and the premise is wrong. ***

** ⓵ THE WORD COUNTS THAT MADE IT LOOK LIKE AN ABSENCE. **

      *** Lagrangian 0 · action principle 0 · Euler--Lagrange 0 · stationary action 0 ·
          least action 0 ***

  ** against the full Hamiltonian apparatus: ** constraint x138, lapse x118, Hamiltonian x107.  ⇒ ** On
  a word count the Lagrangian side is empty and the Hamiltonian side is enormous, which is exactly what
  the survey saw. **

** ⛭⛭ ⓶ BUT THE ACTION IS THERE, FOUR TIMES, AND IT IS LOAD-BEARING. **
  * ** P12's opening: ** "In the ADM decomposition, spacetime is foliated by spatial hypersurfaces and
    ** the Einstein--Hilbert action is recast in Hamiltonian form **" -- the starting point of the whole
    canonical programme.
  * ** An objection answered ON the action: ** "a Euclidean kernel needs a Hamiltonian bounded below,
    and Euclidean gravity notoriously lacks one --- ** the conformal factor entering the
    Einstein--Hilbert action with the opposite sign ** ... ** That objection does not reach this
    construction **".
  * ** A reduction: ** "the deparametrized gravitational Hamiltonian ** reduced from the
    Einstein--Hilbert action **".
  * ⛭ ** AND A COMPUTATION: ** "** The second-order Einstein--Hilbert action ** in the
    transverse-traceless sector ** reduces, mode by mode **, to that of a harmonic oscillator with
    time-dependent mass $a^3$ and frequency $\\mu_n/a$."

  ⇒ *** THAT LAST ONE IS VARIATIONAL WORK PERFORMED IN THE CORPUS.  Expanding an action to second order
      in a sector and reading off the mode Lagrangian is the field's own method, done, and the field is
      named nowhere. ***

** ⓷ SO IT IS NOT AN ABSENCE.  IT IS THE ARRIVAL-PATH SHAPE AT ITS LARGEST SCALE. **  The six earlier
instances were a missing name beside a held argument -- Lovelock, Type II/III, Unruh, Higgs, the baby
universe, N_eff.  ** This is a missing name beside a performed COMPUTATION, and it has stood for 656
revisions in a ledger whose title asserts the opposite. **

  ⌗ ** And the ledger is not idle: ** it was opened deliberately, from a survey, with an adjudication
  attached.  *** The failure was not neglect -- it was that "the field with no footprint" was written
  from a WORD COUNT, and the corpus's variational content is carried under a different name
  ("Einstein--Hilbert action"), which the word count could not see. ***

WHAT IS NOT CLAIMED.  ** Not that the corpus should derive its dynamics variationally ** -- P9 is
explicit that the construction leaves GR's dynamics unchanged, and adding an action principle is not on
any route.  ** Not that the four uses constitute a variational FORMULATION ** -- they are uses of a
standard action inside a canonical programme, which is the ordinary thing to do.  ** Not that the r1890
survey was careless **: a word-bounded count is the right first instrument, and *** this is a case where
the right first instrument gives the wrong answer, which is worth more than the finding. ***

Written r2558.  Stated for reversal.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  V1 -- is the variational field really absent from the corpus?')
    print()
    papers = [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(f).startswith('appendix_receipts')]
    allp = ' '.join(re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%'))) for f in papers)
    led = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'VARIATIONAL_LEDGER.md'),
                                   encoding='utf-8', errors='replace').read())

    check("the ledger's premise is 'the field with no footprint at all'",
          'the field with no footprint at all' in led)
    check("and Daryl's r1891 adjudication is recorded: the route is available and unthrown",
          'available and unthrown' in led)

    # ⓵ the counts that made it look empty
    for k in ('Lagrangian', 'action principle', 'Euler--Lagrange', 'stationary action',
              'least action'):
        n = len(re.findall(re.escape(k), allp, re.I))
        check(f'⛔ "{k}" appears ZERO times', n == 0)

    # ⓶ but the action is there
    n_eh = len(re.findall('Einstein--Hilbert', allp))
    check(f'⛭⛭ BUT "Einstein--Hilbert" appears {n_eh} times', n_eh >= 4)
    check("P12 opens on it: \"the Einstein--Hilbert action is recast in Hamiltonian form\"",
          'the Einstein--Hilbert action is recast in Hamiltonian form' in allp)
    check('an objection is answered ON it: "the conformal factor entering the Einstein--Hilbert '
          'action with the opposite sign"',
          'conformal factor entering the Einstein--Hilbert action with the opposite sign' in allp)
    check('and the Hamiltonian is "reduced from the Einstein--Hilbert action"',
          'reduced from the Einstein--Hilbert action' in allp)
    check('⛭ AND A COMPUTATION IS PERFORMED ON IT: "The second-order Einstein--Hilbert action in the '
          'transverse-traceless sector reduces, mode by mode, to that of a harmonic oscillator"',
          'The second-order Einstein--Hilbert action in the transverse-traceless sector reduces, mode '
          'by mode, to that of a harmonic oscillator' in allp)

    # ⓷ and the Hamiltonian side is enormous, which is what the survey saw
    ham = {k: len(re.findall(re.escape(k), allp, re.I))
           for k in ('constraint', 'lapse', 'Hamiltonian')}
    check(f'and the Hamiltonian apparatus is large: constraint {ham["constraint"]}, lapse '
          f'{ham["lapse"]}, Hamiltonian {ham["Hamiltonian"]}',
          all(v > 40 for v in ham.values()))
    check('⇒⇒ SO IT IS NOT AN ABSENCE -- the corpus performs variational work and names the field '
          'nowhere, which is the arrival-path shape at its largest scale',
          n_eh >= 4 and len(re.findall('Lagrangian', allp, re.I)) == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the ledger's premise is false. **")
    print('  ⓵ ** Lagrangian 0 · action principle 0 · Euler--Lagrange 0 ** against constraint '
          f'{ham["constraint"]}, lapse {ham["lapse"]}, Hamiltonian {ham["Hamiltonian"]}.')
    print('     ⇒ ** On a word count the Lagrangian side is empty, which is what the r1890 survey saw. **')
    print(f'  ⓶ ** BUT the Einstein--Hilbert action appears {n_eh} times and is load-bearing ** -- the ADM')
    print('     starting point, an objection answered on it, a Hamiltonian reduced from it, and')
    print('     ** a SECOND-ORDER expansion in the transverse-traceless sector reduced mode by mode. **')
    print('  ⇒⇒ ** That last is variational work PERFORMED in the corpus, with the field named nowhere. **')
    print('  ⓷ ** So it is the arrival-path shape at its largest scale ** -- and the earlier six were a')
    print('     missing name beside a held ARGUMENT; ** this is a missing name beside a performed')
    print('     COMPUTATION, standing 656 revisions in a ledger titled for the opposite. **')
    print('  ⌗ AND THE METHOD POINT IS WORTH MORE THAN THE FINDING: ** "the field with no footprint" was')
    print('    written from a WORD COUNT, and the content is carried under a different name. ** A')
    print('    word-bounded count is the right first instrument, and this is where it gives the wrong')
    print('    answer.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
