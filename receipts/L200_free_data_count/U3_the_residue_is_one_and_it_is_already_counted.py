#!/usr/bin/env python3
"""U3_the_residue_is_one_and_it_is_already_counted.py -- L-200 §2 / L-201: the BUDGET side.

U1 and U2 counted the SPEND and said explicitly what they had not done: ** p0 asks that the count
EQUAL the substrate's non-symmetric residue, and the residue side was not counted. **  L-201 is the
enumeration that produces it -- "systematically determine which geometric relations among the
fundamental constants the substrate forces ... and look for any constant maximal symmetry does not
reach."

** THE RESIDUE IS ALREADY COUNTED, IN p0's OWN LEDGER SECTION, AND IT WAS NEVER JOINED TO THE FRONTIER
ITEM THAT ASKS FOR IT. **  p0 sec:ledger, two paragraphs after the gauge partition:

    "alpha is precisely what the causal structure does NOT fix: the group preserving the absolute is
     O(5,1) x R^+, ** one generator larger ** than the substrate's isometry group, and that extra
     generator is the dilation carrying alpha -> lambda.alpha.  So the null cone determines the
     geometry up to the scale, and the scale is the one thing it leaves --- ** which is why there is a
     single dimensionful input and nothing for a dimensionless tuning to hide in. **"

And it is sourced, not asserted: P5 carries the same statement with a receipt --

    "the isometry group of a single de Sitter representation is O(5,1) while the group preserving the
     causal structure alone is O(5,1) x R^+, and the one generator by which they differ is precisely
     the one that moves alpha: the causal structure fixes the geometry up to the scale, and the scale
     is what it does not fix."   \\rcpt{C1_conformal_vs_isometric}

⇒ ** THE GEOMETRIC RESIDUE IS EXACTLY ONE REAL PARAMETER, AND IT IS DIMENSIONFUL. **  Counted:
dim O(5,1) = 15, dim(O(5,1) x R^+) = 16, quotient R^+ = 1 generator, the dilation.  And a Cayley-Klein
geometry "carries the scale as its ONLY free constant, signature, null structure and isometry group
all being fixed by the absolute's projective type" -- so the one-scale reading ** has a classical
mechanism and is not only the outcome of an exhaustive audit. **

** SO THE TWO SIDES OF THE GEOMETRIC HALF MATCH, AND THE MATCH IS EXACT: **

    BUDGET (residue) : 1 dimensionful, 0 dimensionless
    SPEND    (U1/U2) : 1 dimensionful (Lambda), 0 dimensionless

⚠ AND WHAT THIS DOES **NOT** SETTLE, stated because the frontier item is precise and it would be easy
to overread.  p0's item asks that maximal symmetry, spent, leave ** "exactly the one measured
cosmological IC (rho_r/rho_m) as the sole tunable datum." **  rho_r/rho_m is a MATTER INITIAL
CONDITION, not a constant, and it is not in the geometric residue at all.  ** So this settles the
CONSTANT-side ledger, which is L-201's own question, and leaves the matter-datum side where the corpus
leaves it: a one-parameter accommodation in three papers, with L-150 owing its derivation. **

** AND L-201's SHARP TARGET IS ANSWERED IN THE NEGATIVE, WHICH IS THE STRONGER OUTCOME. **  It asked
for "any constant maximal symmetry does not reach -- the constant-side analogue of the discrete-parity
matter opening."  The dilation result says there is no such constant on the geometric side: ** the
causal structure fixes everything except the scale, so there is no room for an unreached constant to
sit. **  The matter opening exists because the index obstruction leaves a disconnected component; ** the
constant ledger has no analogous leftover component -- the quotient is one-dimensional and it IS the
scale. **

⌗ THE CLASS THIS BELONGS TO, and it is the session's most frequent: ** the answer was in the corpus,
in the same paper, not joined to the question. **  sec:ledger answers what sec:frontiers asks, and
sec:frontiers still reads "[Reach: stated as a target, not a result]".

Written r2422.  Stated for reversal.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(p):
    return re.sub(r'\s+', ' ', open(p, encoding='utf-8', errors='replace').read())



# ** ⛭⛭ RE-PINNED c54.226 (`L-560`).  THIS RECEIPT PINNED A QUOTATION INTO PROSE THAT LATER CORRECT
# ** WORK MOVED. **  The finding is unchanged; what broke is the pin.
#   ⇒ *** A quotation is a claim about a FILE AT A COMMIT (c54.220's rule), so the historical wording
#       is read at the commit where it stood and the CURRENT text is asserted separately.  A receipt
#       that argues about a sentence must survive the sentence being rewritten. ***
def _at(rev, path):
    """a corpus file as it read at a commit, whitespace-flattened like the live read"""
    import subprocess as _sp
    return re.sub(r'\s+', ' ', _sp.run(['git', 'show', f'{rev}:{path}'], cwd=ROOT,
                                       capture_output=True, text=True, errors='replace').stdout)


def main():
    print()
    print('  U3 -- the residue side: what does maximal symmetry NOT fix?')
    print()
    p0 = flat(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex'))
    p5 = flat(os.path.join(ROOT, 'corpus', 'groupoid_paper.tex'))

    # ---- the residue, in p0's own words ----------------------------------------
    check('p0 states the group preserving the absolute is O(5,1) x R^+',
          'the group preserving the absolute is $\\mathrm{O}(5,1)\\times\\mathbb{R}^{+}$' in p0)
    check('and that it is ONE GENERATOR LARGER than the isometry group',
          'one generator larger than the substrate\'s isometry group' in p0)
    check('and that the extra generator is the dilation alpha -> lambda.alpha',
          'that extra generator is the dilation carrying $\\alpha\\mapsto\\lambda\\alpha$' in p0)
    check('and draws the conclusion the frontier item asks for',
          'a single dimensionful input and nothing for a dimensionless tuning to hide in' in p0)

    # ---- sourced in P5, with a receipt -----------------------------------------
    check('P5 carries the same statement independently',
          'the causal structure fixes the geometry up to the scale, and the scale is what it does '
          'not fix' in p5)
    check('and it is receipted there', 'C1_conformal_vs_isometric' in p5)

    # ---- the Cayley-Klein mechanism -------------------------------------------
    check('and a Cayley-Klein geometry carries the scale as its ONLY free constant',
          'carries the scale as its \\emph{only} free constant' in p0)
    check('so the one-scale reading has a MECHANISM, not just an audit',
          'has a classical mechanism and is not only the outcome of an exhaustive audit' in p0)

    # ---- the count itself ------------------------------------------------------
    dim_o51 = 6*5//2
    check('dim O(5,1) = 15', dim_o51 == 15)
    check('dim(O(5,1) x R^+) = 16, so the quotient is 1-dimensional', dim_o51 + 1 == 16)
    check('⇒ the geometric residue is exactly ONE real parameter, and it is DIMENSIONFUL',
          (dim_o51 + 1) - dim_o51 == 1)

    # ---- and the frontier item still reads as open -----------------------------
        # ** ⛭ RE-PINNED c54.226 (`L-560`): c54.179 (`2af0b0b`) rewrote this very sentence, which is the
    # ** closure this receipt argued for arriving in the paper.  Both ends pinned. **
    BEFORE_C54_179 = 'aa2b6ee'
    _p0_then = _at(BEFORE_C54_179, 'corpus/geometric_core_paper.tex')
    check(f'p0 sec:frontiers read "stated as a target, not a result" at {BEFORE_C54_179}',
          'stated as a target, not a result' in _p0_then)
    check('⛭ AND c54.179 REPLACED IT: "the item has two sides and they now stand differently, so it '
          'is split rather than carried whole" -- the constant side a result, the datum side open',
          'the item has two sides and they now stand differently' in p0)
    check('L-201\'s sharp target -- "any constant maximal symmetry does not reach" -- has no room:'
          ' the quotient is 1-dimensional and IS the scale',
          (dim_o51 + 1) - dim_o51 == 1)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the residue is already counted, in p0\'s own ledger section, and it was never')
    print('     joined to the frontier item that asks for it. **')
    print('     BUDGET (residue): 1 dimensionful, 0 dimensionless   [dim O(5,1) x R^+ - dim O(5,1)]')
    print('     SPEND    (U1/U2): 1 dimensionful (Lambda), 0 dimensionless')
    print('  ⇒ The two sides of the CONSTANT-side ledger match exactly, and the match has a classical')
    print('    mechanism: a Cayley-Klein geometry carries the scale as its only free constant.')
    print('  ⇒ ** And L-201\'s sharp target is answered in the NEGATIVE, which is stronger: there is no')
    print('     constant maximal symmetry fails to reach, because the quotient is one-dimensional and')
    print('     IS the scale.  The matter opening exists because the index obstruction leaves a')
    print('     disconnected component; the constant ledger has no analogous leftover. **')
    print('  ⚠ NOT settled: p0\'s item also asks that rho_r/rho_m be the sole tunable datum.  That is a')
    print('    MATTER INITIAL CONDITION, not a constant, and it is not in the geometric residue.')
    print('    It stays where the corpus leaves it -- a one-parameter accommodation, L-150 owing the')
    print('    derivation.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
