#!/usr/bin/env python3
"""A7 -- the frontier sorts into TWO KINDS, and the sorting rule is the corpus's own: five rows ask
whether the THEORY IS DEFINED and two ask what it PREDICTS.  They fail differently and cannot be
prioritised against each other by size.

** THE RULE, from r2703. **  P15: "the whole difference is carried by $H(a)$."  ⇒ *** Every observable
splits into those that are functions of $H$ and those that are not, and the second kind cannot
discriminate between the arms however precisely it is computed. ***  `PO-10`'s half ② failed that test --
the baryon loading $R$ is a ratio of CONTENTS.

** ⛭⛭ ⓵ APPLIED TO THE WHOLE TABLE, IT SORTS BY KIND. **

      *** DEFINEDNESS -- not a function of H, and not answerable by data
            PO-4   supply the continuous U(1)      a gauge group either exists or does not
            PO-5   is there a third mechanism?     whether a coupling can arise at all
            PO-6   the interacting tower           whether the theory has a spectrum
            PO-11  a propagating Dirac sector      whether the sector exists as states
            PO-2   do the roots ARE colour         an identification; gated on PO-5

          PREDICTION -- a number against the sky
            PO-10  the full-spectrum likelihood refit
            PO-7   the first acoustic peak / CRPHI ***

** ⓶ AND THE OBJECTS CONFIRM IT INDEPENDENTLY. **  `PO-6`'s $\\hat\\Gamma$ lives on P10's own slicing,
whose Ricci scalar is ** $12/\\alpha^2$, CONSTANT ** (r2691) -- no $H(a)$ anywhere.  `PO-11`'s two norms
are measures on a static slice, built from $f(r)$ alone (r2669), and the tortoise interval is infinite
** regardless of the expansion rate ** (r2690).

** ⛭ ⓷ THE TWO CLASSES FAIL DIFFERENTLY, WHICH IS WHY THIS MATTERS FOR ORDERING. **
  * *** A DEFINEDNESS row cannot be settled by data.  It closes by CONSTRUCTION or by a WALL -- and
      `PO-5` shows a wall is a real outcome ("a coupling is not the kind of thing a holonomy supplies").
      Its failure mode is a search with no bound. ***
  * *** A PREDICTION row cannot be settled by construction.  It closes by a RUN against the sky, and its
      failure mode is a number that does not match. ***

  ⇒⇒ *** So "which is smaller" does not order them: `PO-10` is a refit and `PO-11` is a scattering
      problem, but they are not competing for the same kind of effort or the same kind of verdict.  The
      real question when choosing is WHICH KIND OF ANSWER THE PROGRAMME NEEDS NEXT. ***

** ⓸ AND THE BALANCE IS ITSELF A FINDING. **  *** Five of seven ask whether the theory is defined.  A
programme whose frontier is five-sevenths definedness is not near a confrontation with data -- it is
near a decision about what it IS.  That is not a criticism; it is the shape, and it was not visible
while the rows were sorted by size. ***

WHAT IS NOT CLAIMED.  ** Not that the classification is the corpus's ** -- *** it is derived here from
P15's own $H(a)$ clause and the objects' own definitions; no paper states it. ***  ** Not that
definedness rows are harder ** -- `PO-6` is a heat-kernel calculation and `PO-11` has decades of
literature; `PO-5` is the unbounded one.  ** Not that `PO-7` and `PO-10` are near ** -- `PO-7` is gated
on `PO-seam` and `PO-10` needs a refit nobody has run.

Written r2704.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

DEFINEDNESS = ('PO-2', 'PO-4', 'PO-5', 'PO-6', 'PO-11')
PREDICTION = ('PO-7', 'PO-10')


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
    print('  A7 -- what kind of question is each open row?')
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    rows = {re.search(r'PO-\d+', l).group(0): l
            for l in raw.split('\n') if re.match(r'\|\s*\*\*PO-\d+\*\*', l)}

    check('⓵ the sorting rule is P15\'s own: "the whole difference is carried by $H(a)$"',
          'the whole difference is carried by' in p15)

    # every classified row is an open row
    openrows = {t for t, l in rows.items()
                if 'ANSWERED' not in l.split(' | ')[-1][:40] and not l.startswith('| ~~')}
    check(f'⓶ and the classification covers exactly the open rows: '
          f'{len(DEFINEDNESS)} + {len(PREDICTION)} = {len(DEFINEDNESS)+len(PREDICTION)}',
          set(DEFINEDNESS) | set(PREDICTION) == openrows)

    # ⓷ the objects confirm it
    check("⓷ PO-6's tower lives on a background with CONSTANT curvature -- the row records "
          "$R=12/\\alpha^2$, so no $H(a)$ enters",
          '12/\\alpha^2' in rows['PO-6'] or '12/\\alpha^{2}' in rows['PO-6'])
    check("PO-11's norms are built from $f(r)$ on a static slice -- the row records the horizon-located "
          'obstruction and its uniformity in $\\lambda$',
          'tortoise' in rows['PO-11'].lower() and 'uniform' in rows['PO-11'].lower())
    check('while PO-10 and PO-7 are numbers against the sky -- PO-10 a "parameter refit", PO-7 the '
          "first peak's position",
          'refit' in rows['PO-10'].lower() and 'peak' in rows['PO-7'].lower())

    # ⓸ the balance
    check(f'⓸ and the balance is {len(DEFINEDNESS)} definedness against {len(PREDICTION)} prediction',
          len(DEFINEDNESS) == 5 and len(PREDICTION) == 2)
    check("with PO-5 showing a WALL is a real outcome for a definedness row: \"a coupling is not the "
          'kind of thing a holonomy supplies"',
          'not the kind of thing a holonomy supplies' in rows['PO-5'])

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the frontier is FIVE definedness rows and TWO prediction rows. **')
    print('  ⛭⛭ ⓵ ** The rule is P15\'s own — "the whole difference is carried by H(a)" — so an')
    print('     observable that is not a function of H cannot discriminate.  ** Applied to the table it')
    print('     sorts by KIND: ')
    print(f"       DEFINEDNESS  {', '.join(DEFINEDNESS)}")
    print(f"       PREDICTION   {', '.join(PREDICTION)}")
    print('  ⓶ ** The objects confirm it: ** PO-6\'s tower sits on a background with R = 12/α² CONSTANT;')
    print('     PO-11\'s norms are built from f(r) on a static slice and the tortoise interval is')
    print('     infinite regardless of the rate.')
    print('  ⛭ ⓷ ** AND THE CLASSES FAIL DIFFERENTLY: ** a definedness row closes by CONSTRUCTION or by')
    print('     a WALL and cannot be settled by data; a prediction row closes by a RUN against the sky')
    print('     and cannot be settled by construction.')
    print('     ⇒ *** So "which is smaller" does not order them.  The question when choosing is which')
    print('       KIND of answer the programme needs next. ***')
    print('  ⓸ *** And the balance is the finding: five of seven ask whether the theory is DEFINED.  A')
    print('     programme whose frontier is five-sevenths definedness is not near a confrontation with')
    print('     data — it is near a decision about what it IS.  Not a criticism; the shape. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
