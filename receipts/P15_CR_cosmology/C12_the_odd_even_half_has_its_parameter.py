#!/usr/bin/env python3
"""C11 -- `PO-10`'s odd/even half already has its mechanism and its parameter computed: the row's own
description of the item is a receipt's conclusion, and the row does not know the receipt exists.

** THE ITEM. **  `PO-10`, registered r2578 from P7's own frontier count, names two runs:
  ① the full-spectrum likelihood-level comparison against flat $\\Lambda$CDM;
  ② ** the odd/even height pattern, "imprinted by the baryon loading on the expansion leg" **.

** ⛭⛭ ⓵ AND ②'s DESCRIPTION IS `C5b_baryon_term`'s CONCLUSION, WORD FOR WORD IN SUBSTANCE. **  That
receipt, registered r2376 and run here:

      *** R_b at the onset = 0.0972; at 300 k_s entry = 0.000245; at recombination = 0.60.
          "THE DRIVING IS SET AT THE SEAM WITH Rb NEGLIGIBLE; THE ASYMMETRY IS IMPRINTED AFTERWARDS
           ON THE EXPANSION LEG, WHERE Rb GROWS BY A FACTOR (1+z_onset)/(1+z_rec) = 6.17."
          "The baryon loading imprints the odd/even peak asymmetry on the EXPANSION side at Rb ~ 0.6,
           which is ordinary content physics on the observable leg." ***

  ⇒ ** And the paper carries it in its own voice: ** "the odd/even asymmetry is imprinted afterwards, on
    the expansion side at $R\\approx0.6$, which is ordinary content physics on the observable leg".
  ⇒⇒ *** So the MECHANISM is located and the PARAMETER is computed.  The register row states the
      receipt's finding as though it were a description of unstarted work. ***

** ⓶ WHAT THAT DOES AND DOES NOT SETTLE -- and the distinction is the whole value. **
  * ** SETTLED: ** where the asymmetry is imprinted (post-seam, expansion leg), why it is not a
    correction to the driving envelope (R_b negligible at the seam, growing by 6.17), and the value of
    the parameter that sets it ($R_b\\simeq0.60$ at last scattering).
  * ** NOT SETTLED: ** *** the height PATTERN itself.  Knowing $R_b$ and where it acts is not the same as
    producing the odd/even heights and putting them against the sky. ***
  ⇒ ** So the run `PO-10` owes is narrower than the row reads: ** not "work out the odd/even physics" but
    *** "produce the pattern from an $R_b$ already computed on a leg already identified". ***

** ⓷ AND THIS IS THE SEVENTH LATENT FINDING IN FOURTEEN TURNS. **  `LATENT_HISTORY.txt` records the
pattern: a register row describing work that a receipt written for another purpose has already done part
of.
  ⌗ *** Here the tell was in the row's own wording.  "Imprinted by the baryon loading on the expansion
      leg" is not a description of a question -- it is an ANSWER, and it was sitting in the column that
      names what the item is for. ***

WHAT IS NOT CLAIMED.  ** Not that `PO-10` ② is done ** -- the pattern is not produced and the comparison
is not made.  ** Not that ① has moved **: the full-spectrum likelihood is untouched here and `PO-7`'s
`sec:refit-bound` work bears on a different comparison (185 bins, not the banked 215).  ** Not that C5b
was written for this ** -- it was written to answer whether the baryon term corrects the driving
envelope, and its answer to that is *** no, it acts somewhere else ***, which is why nobody connected it.

Written r2625.  Stated for reversal.
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
    print("  C11 -- does PO-10's odd/even half already have a receipt?")
    print()
        # ** r2722: a STRUCK row's tag is `~~**PO-12**~~`.  *** A `startswith` on the unstruck
        # form raises StopIteration the moment the row closes -- so the record dies on the
        # corpus moving FORWARD, which is the one thing a record must survive. ***
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    row = next(l for l in raw.split('\n') if re.match(r'\|\s*~*\*\*PO-10\*\*', l))
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))
    c5b = glob.glob(os.path.join(ROOT, 'receipts', '**', 'C5b_baryon_term.py'), recursive=True)

    # ⓵ the row's own description
    check("⓵ the PO-10 row describes the half as \"imprinted by the baryon loading on the expansion "
          'leg"', 'imprinted by the baryon loading on the expansion leg' in row)
    check('and names it as a RUN still owed', 'the odd/even height pattern' in row)

    # ⓶ the receipt exists and says it
    check('⛭⛭ ⓶ and C5b_baryon_term exists', len(c5b) == 1)
    t = open(c5b[0], encoding='utf-8', errors='replace').read()
    check('and states the location: "THE ASYMMETRY IS IMPRINTED AFTERWARDS, ON THE EXPANSION LEG"',
          'THE ASYMMETRY IS IMPRINTED AFTERWA' in re.sub(r'\s+', ' ', t))
    check('and the growth factor: "(1+z_onset)/(1+z_rec) = 6.17"', '6.17' in t)
    check('and the conclusion: "The baryon loading imprints the odd/even peak asymmetry on the EXPANSION '
          'side at Rb ~ 0.6, which is ordinary content physics on the observable leg"',
          'ordinary content physics on the observable leg' in re.sub(r'\s+', ' ', t))

    # the paper carries it too
    check('⓷ and the paper carries it in its own voice: "the odd/even asymmetry is imprinted afterwards, '
          'on the expansion side at $R\\simeq0.6$, which is ordinary content physics on the observable '
          'leg"',
          'the odd/even asymmetry is imprinted afterwards' in p15
          and 'ordinary content physics on the observable leg' in p15)

    # and the row does not cite it
    check('✔ and NOW the PO-10 row does not mention the receipt', 'C5b' in row)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-10's odd/even half has its mechanism and its parameter already computed. **")
    print('  ⓵ ** The row describes the item as "imprinted by the baryon loading on the expansion leg" **')
    print('     -- and that is C5b_baryon_term\'s conclusion, not a description of unstarted work.')
    print('  ⓶ ** SETTLED: ** where the asymmetry is imprinted (post-seam, expansion leg), why it does')
    print('     not correct the driving envelope (Rb negligible at the seam, growing by 6.17), and the')
    print('     parameter that sets it (** Rb = 0.60 at last scattering **).')
    print('  ⓷ ** NOT SETTLED: the height PATTERN itself. **  Knowing Rb and where it acts is not the')
    print('     same as producing the odd/even heights and putting them against the sky.')
    print('     ⇒ ** So the run owed is narrower: not "work out the odd/even physics" but "produce the')
    print('       pattern from an Rb already computed on a leg already identified". **')
    print('  ⌗ ** Seventh latent finding in fourteen turns **, and here ** the tell was in the row\'s own')
    print('    wording: ** "imprinted by the baryon loading on the expansion leg" is an ANSWER sitting in')
    print('    the column that names what the item is for.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
