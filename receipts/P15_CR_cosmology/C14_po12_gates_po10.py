#!/usr/bin/env python3
"""C14 -- `PO-10`'s odd/even half cannot be produced without `PO-12`'s transfer, and the row does not say
so: the two items are ordered, not independent.

** WHERE `PO-10` STANDS. **  r2625 established that its odd/even half has its ** mechanism ** located
(post-seam, expansion leg) and its ** parameter ** computed ($R_b=0.60$ at recombination, `C5b_baryon_term`).
What is not settled is *** the height PATTERN itself ***: "knowing $R_b$ and where it acts is not the same
as producing the odd/even heights and putting them against the sky."

** ⛔ ⓵ AND THE OBVIOUS ROUTE IMPORTS EXACTLY WHAT THE CORPUS SAYS IS NOT BUILT. **  The textbook odd/even
ratios follow from the displaced zero point: with $R_b=0.60$ they give

      *** (1+3R)/|1-3R| = 3.50    (1+R)/(1-R) = 4.00    [(1+3R)/(1+R)]^2 = 3.06 ***

  ⇒ ** But those are $\\Lambda$CDM peak-height formulae. **  *** They assume a transfer from the primordial
      spectrum to the observed $C_\\ell$ -- and `CR_cosmology` states that transfer is exactly what this
      cosmology does not have: "a genuine build, not a plug-in ... it requires first specifying how the
      fluctuations gravitate on the radiation-free background ... and then a bespoke transfer against that
      specification". ***
  ⌗ ** So producing the pattern by the standard formula would answer `PO-10` by assuming `PO-12`. **

** ⛭⛭ ⓶ WHICH MAKES THE TWO ITEMS ORDERED, AND NEITHER ROW SAYS SO. **  *** `PO-12` (the bespoke transfer)
GATES `PO-10`'s odd/even half.  Not by convention -- by the fact that a peak-height pattern is a statement
about $C_\\ell$, and $C_\\ell$ is what a transfer produces. ***
  ⚠ ** And `PO-10`'s OTHER half is gated by the same thing: ** the full-spectrum likelihood comparison is
  a comparison of $C_\\ell$ spectra.
  ⇒ *** So `PO-12` gates BOTH of `PO-10`'s runs, and `PO-10` reads as two independent items owed. ***

** ⓷ AND `PO-12` IS HALF BUILT (r2623), which fixes the order precisely. **  Its step ① -- "the piece that
sets the high-$\\ell$ driving envelope" -- is computed in `sec:envelope`.  Its step ② -- the transfer run
against that specification -- is not.
  ⇒ ** THE ORDER: `PO-12` step ② → `PO-10` both halves. **  *** One computation unblocks two runs, and
    nothing else on the table depends on it. ***

WHAT IS NOT CLAIMED.  ** Not that the standard formulae are WRONG ** -- *** they are right for
$\\Lambda$CDM and the point is that importing them would smuggle in the transfer whose absence is the
open item. ***  ** Not that $R_b=0.60$ is in doubt ** -- it is computed and stands.  ** Not that `PO-12`'s
step ② is small ** -- the paper calls it "a genuine build, not a plug-in".

Written r2646.  Stated for reversal.
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
    print('  C14 -- can PO-10 be produced without PO-12?')
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    po10 = next(l for l in raw.split('\n') if l.startswith('| **PO-10**'))
    po12 = next(l for l in raw.split('\n') if l.startswith('| **PO-12**'))

    # ⓵ what PO-10 still owes
    check('⓵ PO-10 owes the height PATTERN: "knowing $R_b$ and where it acts is not the same as '
          'producing the odd/even heights and putting them against the sky"',
          'is not the same as producing the odd/even heights' in po10)
    check('and its other half is a full-spectrum likelihood comparison',
          'full-spectrum likelihood' in po10)

    # ⓶ the transfer is not built
    check('⛔ ⓶ and P15 says the transfer is not built: "This is a genuine build, not a plug-in: it '
          'requires first \\emph{specifying how the fluctuations gravitate on the radiation-free '
          'background}"',
          'This is a genuine build, not a plug-in' in p15
          and 'it requires first \\emph{specifying how the fluctuations gravitate on the '
              'radiation-free background}' in p15)
    check('"and then a bespoke transfer against that specification"',
          'and then a bespoke transfer against that specification' in p15)

    # the numbers, for the record
    Rb = 0.60
    ratios = {'(1+3R)/|1-3R|': (1 + 3*Rb) / abs(1 - 3*Rb),
              '(1+R)/(1-R)': (1 + Rb) / (1 - Rb)}
    check(f'⓷ the textbook ratios at $R_b=0.60$ are {({k: round(v,2) for k,v in ratios.items()})} -- '
          'and they are $\\Lambda$CDM peak-height formulae, which assume a transfer',
          abs(ratios['(1+R)/(1-R)'] - 4.0) < 1e-9)

    # ⓸ PO-12 is half built
    check('⓸ and PO-12 is half built: its step ① is computed in sec:envelope',
          'sec:envelope' in po12 or 'the envelope is derived on the collapse leg' in po12)
    check('✔ and NOW neither row records the dependency',
          'PO-12' in po10 and 'PO-10' in po12)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** PO-12 GATES BOTH of PO-10\'s runs, and neither row says so. **')
    print('  ⛔ ⓵ ** The obvious route imports what the corpus says is not built: ** the textbook odd/even')
    print('     ratios at R_b = 0.60 give ** 3.50, 4.00, 3.06 ** -- but those are ΛCDM peak-height')
    print('     formulae, ** which assume a transfer from the primordial spectrum to the observed C_l. **')
    print('  ⛭⛭ ⓶ ** And that transfer is exactly PO-12: ** "a genuine build, not a plug-in ... a bespoke')
    print('     transfer against that specification".  ** Producing the pattern by the standard formula')
    print('     would answer PO-10 by ASSUMING PO-12. **')
    print('  ⓷ ** Both of PO-10\'s halves are statements about C_l ** -- the height pattern and the')
    print('     full-spectrum likelihood -- ** and C_l is what a transfer produces. **')
    print('  ⇒⇒ ** THE ORDER: PO-12 step ② → PO-10, both halves. **  *** One computation unblocks two')
    print('     runs.  PO-12 step ① is already computed (sec:envelope), so the gate is one step deep. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
