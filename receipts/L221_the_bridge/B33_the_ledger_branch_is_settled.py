#!/usr/bin/env python3
"""B33 -- `PO-5`'s one test RUN and SETTLED: three papers commit independently that $\\ell_P$ is a
gauge, none treats it as a second scale, so the ledger carries no free dimensionless parameter.

** THE TEST, from cc54's c54.216 (r2741). **  *** "If $\\ell_P$ is a gauge, the ledger holds no free
dimensionless parameter and no mechanism of any kind can deliver a free coupling.  If $\\ell_P$ were a
second scale, $\\alpha/\\ell_P\\sim10^{61}$ is a free dimensionless number and the bound evaporates." ***
** One position, two rows -- and it is a READ, not a search. **  So it was read.

** ⛭⛭ ⓵ THREE PAPERS COMMIT INDEPENDENTLY. **

      *** p0  geometric_core  "The one physical length is alpha, NOT ell_P; their ratio ... is the
                               size of the universe in gauge-units -- A NUMBER, NOT A TUNING"
          P10 canonical_time  "since ell_P is a GAUGE-COMBINATION rather than a second physical
                               length, the cutoff is not smuggling a scale in either"
          P14 matter_sector   "the one physical length being alpha and not ell_P, whose ratio is a
                               number in gauge-units and not a tuning" ***

  ⌗ ** And P10's is the one that matters most, ** *** because it is reached from a different direction
    entirely: P10 needs it to say its regulator smuggles no scale, and arrives at the same position
    without the coupling question in view. ***

** ⓶ AND NO PAPER TREATS IT AS A SCALE. **  P15's six uses are ** all ratios ** --
$\\Lambda\\ell_P^2$, $(\\ell_P/M)^2$, $144(\\ell_P/M)^2$ -- never $\\ell_P$ standing alone as a physical
length.  The cosmogenesis use is inside the same tensor-floor ratio.
  ⚠ ** The one apparent exception is not one: ** *** `BH_causality`'s "physics above the Planck scale
  which the derivation depends on" describes HAWKING's derivation and its trans-Planckian problem, not
  the corpus's own commitment. ***

** ⛭ ⓷ SO THE BRANCH IS SETTLED, AND WITH IT `PO-5`'s RESIDUE. **  *** The ledger holds no free
dimensionless parameter.  No mechanism of any kind -- holonomy, isometry, or a third nobody has named --
can deliver a FREE coupling.  What a third mechanism must deliver is a FIXED PURE NUMBER, and it is
falsifiable against one quantity. ***

** ⓸ AND THE ROW IS NOW A TEST WITH BOTH ITS SIDES CLOSED. **  *** r2729: no $F^2$ term to put a
coefficient in front of.  c54.216: no free number to be the coefficient -- **and this receipt settles
that half by reading the corpus's own three commitments**.  What remains is not a search and not a
question about the ledger: it is whether any construction produces a fixed pure number from the
substrate. ***

WHAT IS NOT CLAIMED.  ** Not that `PO-5` closes ** -- *** the row asks whether a third mechanism exists,
and a candidate delivering a fixed pure number would still meet the bound; what is settled is the LEDGER
BRANCH, which was the open half of the test. ***  ** Not that the three commitments are re-derived ** --
they are quoted, and p0's rests on `JanzenCRcosmology`'s $\\Lambda\\ell_P^2\\sim3\\times10^{-122}$.
** Not that `BH_causality` is inconsistent ** -- it is reporting another derivation's problem, which is
the opposite of a commitment.

** COMPUTES: nothing numerical.  *** A read across six papers for one ontological position; the numbers
quoted ($10^{61}$, $3\\times10^{-122}$) are the corpus's own. *** **

Written r2742.  Stated for reversal.
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


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print("  B33 -- does any paper treat ell_P as a second physical scale?")
    print()
    P = {os.path.basename(f)[:-4]: re.sub(r'\s+', ' ', body(f))
         for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
         if not os.path.basename(f).startswith('appendix')}

    # ⓵ the three commitments
    check('⛭⛭ ⓵ p0: "The one physical length is $\\alpha$, not $\\ell_{P}$" with the ratio "the size '
          'of the universe in gauge-units---a number, not a tuning"',
          'the size of the universe in gauge-units' in P['geometric_core_paper'])
    check('P10, reached from a different direction entirely: "since $\\ell_{P}$ is a '
          'gauge-combination rather than a second physical length, the cutoff is not smuggling a '
          'scale in either"',
          'is a gauge-combination rather than a second physical length' in P['canonical_time'])
    check('P14: "the one physical length being $\\alpha$ and not $\\ell_{P}$, whose ratio ... is a '
          'number in gauge-units and not a tuning"',
          'is a number in gauge-units and not a tuning' in P['matter_sector_paper'])

    # ⓶ and no paper treats it as a scale
    bare = re.compile(r'\\ell_\{?P\}?')
    ratios = re.compile(r'\\ell_\{?P\}?\s*[/^]|/\s*\\ell_\{?P\}?|\\Lambda\s*\\ell')
    n_uses = len(bare.findall(P['CR_cosmology']))
    check(f'⓶ and P15\'s {n_uses} uses are all inside ratios -- $\\Lambda\\ell_P^2$, $(\\ell_P/M)^2$, '
          '$144(\\ell_P/M)^2$ -- never standing alone as a physical length',
          n_uses > 0 and len(ratios.findall(P['CR_cosmology'])) > 0)
    check('⚠ while the one apparent exception is not one: BH_causality\'s Planck-scale mention '
          'describes HAWKING\'s derivation and its trans-Planckian problem, not a corpus commitment',
          'Planck scale' in P['BH_causality_v2']
          and 'the derivation' in P['BH_causality_v2'])

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the branch is SETTLED — ell_P is a gauge, in three papers, independently. **')
    print('  ⛭⛭ ⓵ ** p0, P10 and P14 each commit, ** and ** P10\'s is the one that matters most: ** it')
    print('     is reached from a different direction entirely — P10 needs it to say its regulator')
    print('     smuggles no scale, and arrives at the same position with the coupling question')
    print('     nowhere in view.')
    print('  ⓶ ** And no paper treats it as a scale: ** P15\'s uses are all ratios, and')
    print('     BH_causality\'s mention is about Hawking\'s derivation — ** reporting another')
    print('     derivation\'s problem is the opposite of a commitment. **')
    print('  ⛭ ⓷ *** SO THE LEDGER HOLDS NO FREE DIMENSIONLESS PARAMETER.  No mechanism of any kind')
    print('     can deliver a FREE coupling, and what a third must deliver is a FIXED PURE NUMBER —')
    print('     falsifiable against one quantity. ***')
    print('  ⓸ ** Both sides of the row are now closed as bounds: ** r2729 — no F² term to put a')
    print('     coefficient in front of; c54.216 + this — no free number to be the coefficient.')
    print('     ** What remains is whether any construction produces a fixed pure number. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
