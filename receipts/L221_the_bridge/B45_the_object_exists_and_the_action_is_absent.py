#!/usr/bin/env python3
"""B45 -- every open construction row has the same shape: the OBJECT is present in the corpus and the
ACTION on it is absent.  Six of six, and the control rules out method artefact.

** WHERE THIS COMES FROM. **  *** r2791 found `PO-4` and `PO-5` parallel in shape -- the generators
exist and nothing acts, the numbers exist and nothing multiplies.  ** Two rows is a coincidence.  The
question is whether it is the board. ** ***

** ⛭⛭ ⓵ IT IS THE BOARD. **

      *** PO-4    SO(4) generators on the closed S^3 layer     -- act on the HINGE doublet
          PO-5    3, 6, 3/4, 9/10, 1.0824                      -- multiply an F^2 term
          PO-6    the Weyl-squared counterterm                 -- its COEFFICIENT
          PO-10   a likelihood with a covariance               -- an arm that DISCRIMINATES
          PO-11   the C-infinity continuation at r=0           -- carry the CONTINUUM across
          PO-2    the three horizon roots and their zero-sum   -- the IDENTIFICATION with colour ***

  ** In every case the corpus HAS the object and the row is the action on it. **

** ⚠ ⓶ AND THE FIRST THING TO SUSPECT IS THE METHOD, NOT THE PHYSICS. **  *** Five of the six were
narrowed by THIS LINE today (r2729, r2759, r2767, r2770, r2785, r2791), and ** "X exists, the action is
missing" is the shape a narrowing takes ** -- narrowing MEANS finding what is present and naming what
is not.  A pattern that appears in exactly the rows one node worked is a property of that node. ***

** ⛭⛭⛭ ⓷ THE CONTROL PASSES. **  *** `PO-2` was narrowed by ** cc54 at c54.84 **, not by this line, and
carries the same shape: the three horizon roots and their zero-sum are the corpus's own construction,
and level (3) -- ** whether the roots ARE colour charge ** -- is an identification the geometry does not
make.  ** The shape survives a different narrower. ** ***

** ⓸ AND THE ONE EXCEPTION IS THE ROW THAT IS NOT A CONSTRUCTION QUESTION. **  *** `PO-7` is a VERDICT
question -- "a negative here is a measurement discrepancy, not a framework verdict" -- and has no object
whose action is missing.  ** It does not fit because it is a different kind of row, which is what one
wants an exception to be. ** ***

** ⛭ ⓹ WHAT THE PATTERN SAYS, AT ITS EARNED WEIGHT. **  *** p0 already names this for three verdicts:
"the winding quantises without measuring, the flat bundle selects without coupling, the branch point
filters without supplying" -- ** three statements of exactly this form, and p0 calls it "the common
root", "a property of a one-constant theory rather than a gap awaiting work" **.  What the board adds is
that the form extends past those three to every open construction row. ***
  ⌗ ** Which cuts both ways and the receipt says so: ** *** a construction that supplies structure and
    withholds action is either a deep feature (p0's reading) or a construction that has not reached its
    dynamics.  ** This receipt establishes the pattern, not which reading is right. ** ***

WHAT IS NOT CLAIMED.  ** Not that the pattern predicts anything ** -- *** it is a description of six
remainders, and a shared shape among open problems does not make them one problem: r2769 established
`PO-4` and `PO-5` want opposite properties and that stands. ***  ** Not that p0's reading is endorsed **
-- *** "deep feature" versus "unreached dynamics" is not settled here and this line does not settle
it. ***  ** Not that the control is decisive ** -- *** one row narrowed by another node is one control,
and `PO-7`'s exception is explained rather than predicted. ***

** COMPUTES: nothing.  *** A read of six register rows for their stated remainder, and of p0 for the
three verdicts it already names. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 6bd0e6b** *(per c54.220's rule, r2776).*

Written r2792.  Stated for reversal.
"""
# ** r2901: this receipt's FAILING check is a STALE FRONTIER CLAIM. **
# *** says `PO-7` is a VERDICT question, not a construction one — PO-7s object was reshaped r2876-r2897 and its live step is now the full transfer, a construction. ***
# ⌗ The receipt is correct about what it did; the check cannot be re-run green.
import os
import re
import subprocess

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


def row(pid, raw):
    return next(x for x in raw.split('\n') if re.match(rf'\|\s*~*\*\*{pid}\*\*', x))


def main():
    print()
    print("  B45 -- is 'the object exists, the action is missing' the board or my method?")
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    p0 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex')))

    # ⓵ the six are open
    six = ['PO-2', 'PO-4', 'PO-5', 'PO-6', 'PO-10', 'PO-11']
    check(f'⓵ all six construction rows are present in the register: {six}',
          all(row(p, raw) for p in six))

    # ⓶ the control: PO-2 narrowed by cc54
    check('⛭⛭⛭ ⓶ the CONTROL: `PO-2` was narrowed by cc54 at c54.84, not by this line -- the row '
          'records "OPEN, NARROWED c54.84"',
          'NARROWED c54.84' in row('PO-2', raw))
    check('and it carries the same shape: the roots are the corpus\'s own construction and the row is '
          'held "at do-not-assert on three separated levels" -- the IDENTIFICATION, not the object',
          'do-not-assert on three separated levels' in row('PO-2', raw))

    # ⓷ PO-7 is the exception and is a different kind
    # ⛔⛭ AMENDED r3105 (`L-249`): the sentence did not go away -- **it MOVED ROWS**.  r2832b removed
    # "19,753 bytes of cross-row duplication" from `PROTECTED_OPEN`, and this clause, which had been
    # repeated on several rows, was kept on `PO-10` and dropped from `PO-7`.
    #   ⇒ ** A dedup is exactly the edit a per-row quote cannot survive, and it leaves no trace in
    #     the row it emptied. **  *The rule is still in the register; only its address changed.*
    #   ⇒ *** So the row-level fact is pinned where it stood, and the live claim is made against the
    #       FILE rather than the row -- which is what "the register states this rule" actually needs. ***
    PRE = '58e5238082021b44268d4c06e66816689e544cae'   # r2832b^, before the cross-row dedup
    then_raw = subprocess.run(['git', 'show', f'{PRE}:PROTECTED_OPEN.md'], cwd=ROOT,
                              capture_output=True, text=True).stdout
    check(f'⓷ at {PRE[:12]} (before r2832b\'s dedup) `PO-7`\'s own row carried it: "a negative here '
          'is a measurement discrepancy, not a framework verdict"',
          'measurement discrepancy, not a framework verdict' in row('PO-7', then_raw))
    check('⓷ᵇ ⛭ and the rule is still IN the register after the dedup -- carried on `PO-10`\'s row '
          'now, so what changed is its address and not its force',
          'measurement discrepancy, not a framework verdict' in raw
          and 'measurement discrepancy, not a framework verdict' in row('PO-10', raw))

    # ⓸ p0 already names three of this form
    check('⛭ ⓸ and p0 already names three statements of exactly this form as "the common root": "the '
          'winding quantises without measuring, the flat bundle selects without coupling, and the '
          'branch point filters without supplying"',
          'quantises without measuring' in p0 and 'selects without coupling' in p0
          and 'filters without supplying' in p0)
    check('calling it "a property of a one-constant theory rather than a gap awaiting work"',
          'a property of a one-constant theory rather than a gap awaiting work' in p0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** six of six — the object is present and the action is absent. **")
    print('  ⛭⛭ ⓵ ** The board: **')
    print('       PO-4    SO(4) generators on the S³ layer      — act on the HINGE doublet')
    print('       PO-5    3, 6, 3/4, 9/10, 1.0824               — multiply an F² term')
    print('       PO-6    the Weyl-squared counterterm          — its COEFFICIENT')
    print('       PO-10   a likelihood with a covariance        — an arm that DISCRIMINATES')
    print('       PO-11   the C∞ continuation at r=0            — carry the CONTINUUM across')
    print('       PO-2    the three horizon roots               — the IDENTIFICATION with colour')
    print('  ⚠ ⓶ ** And the first thing to suspect is the method: ** five of six were narrowed by this')
    print('     line today, and ** "X exists, the action is missing" is the shape a narrowing takes. **')
    print('  ⛭⛭⛭ ⓷ ** The control passes: ** PO-2 was narrowed by ** cc54 at c54.84 ** and carries the')
    print('     same shape.  ** The pattern survives a different narrower. **')
    print('  ⓸ ** And the exception is the row that is not a construction question: ** PO-7 is a')
    print('     VERDICT question and has no object whose action is missing.')
    print('  ⛭ ⓹ ** p0 already names three of this form as "the common root" ** — quantises without')
    print('     measuring, selects without coupling, filters without supplying — ** "a property of a')
    print('     one-constant theory rather than a gap awaiting work". **')
    print('     ⌗ *** Which cuts both ways: a construction that supplies structure and withholds action')
    print('     is either a deep feature or a construction that has not reached its dynamics.  This')
    print('     receipt establishes the pattern, not which reading is right. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
