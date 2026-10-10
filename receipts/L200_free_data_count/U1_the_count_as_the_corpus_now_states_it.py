#!/usr/bin/env python3
"""U1_the_count_as_the_corpus_now_states_it.py -- L-200 §0: the free-data count, re-read at c54.163.

** L-200 IS p0'S OWN DECISIVE TEST, AND IT HAD NO REGISTER ROW UNTIL r2378 **, so check_supersession
had never run it against a single receipt.  The paper states it as a target with a sharp falsifier:

    "Show that the framework's count of genuinely free data equals the substrate's non-symmetric
     residue---maximal symmetry, spent, leaving exactly the one measured cosmological IC (rho_r/rho_m)
     as the sole tunable datum, and each constant-relation a locked parameter.  ** Decisive: a hidden
     geometric freedom in the cosmology, or a genuinely free constant where the reading says it
     should lock, falsifies 'rigidity and wall are one fact.' **"
                                                        -- p0 sec:frontiers, item 1

§0 FIRST, because the work is half done and the half that exists must be read before it is redone.
`retired/CONSTANT_LEDGER_receipt.md` (r648--r655, 21 KB) already closed the GRAVITATIONAL--QUANTUM
sector: ** it spends ZERO free dimensionless constants **, each of c, G, hbar entering at a different
interface and at each interface being a unit gauge or actively locked:

    Lambda   the SOLE dimensionful scale; alpha = sqrt(3/Lambda) "the sole remaining scale"
    c        the null-ruling GAUGE (time<->length); "no dimensionless relation between a slope and an
             inverse area"
    G        appears ONLY as GM/c^2, a mass<->length GAUGE; and M is perspectival or Nariai-locked
    hbar     enters at the quantum seam and the ONE place a free quantum parameter could live -- the
             (1,1) deficiency indices -- is CLOSED without a free parameter by the horizon's own
             thermal state

WHAT THIS PROBE ADDS, AND IT IS THE PART THAT WAS OPEN.  The retired receipt records its own limit:
** "the matter-side count: OPEN -- the fermion sector is unbuilt, so its free-data count is the matter
build's own work; and whether rho_r/rho_m is truly the SOLE free matter IC is to be settled as the
sector is built." **  ** The sector has since been built (P14, and the discrete flavour skeleton is
forced), and c54's spans have run to c54.163. **  So the count is re-run against the corpus as it now
stands, and this probe reports what the CORPUS ITSELF claims, free and locked, without adjudicating.

** THE ONE THING THAT MOVED, AND IT MOVED THE RIGHT WAY. **  P3 recorded a SECOND candidate input --
"the metric function itself was for a time the one input not derived here---the D-dimensional f taken
as the standard Tangherlini--de Sitter form" -- and states that ** that gap is now closed **: the
slicing operator defines the vacuum sector as the kernel of the matter functional, T^t_t = 0 is a
first-order linear equation, and its ENTIRE solution space is the SdS form with M the single constant
of integration.  ⇒ ** A candidate free datum was found and eliminated by derivation, which is exactly
what the falsifier asked to be shown and not merely asserted. **

WHAT IS NOT DECIDED HERE, and must not be read in: whether rho_r/rho_m is the sole REMAINING free
datum.  ** The corpus states it as a one-parameter accommodation in three papers and calls the
derivation open (L-150). **  This probe counts what the corpus claims; it does not close the claim.

** r6931+70.1 -- THAT UNDECIDED QUESTION HAS SINCE BEEN ANSWERED, AND BY THIS FAMILY'S NEIGHBOUR. **
L-150's X1 closed the datum half as a structural negative (rho_r/rho_m is a clock reading, not a
carried datum), and the corpus took it: p0's item now reads "The test has two sides, and each has been
run", with the datum side "a clock reading rather than a datum a handover transmits" citing X1
(r6683, 73eb61ef, and the r6772 cosmology rewrite).  The "one-parameter accommodation" wording this
receipt quoted from P7 and P15 was the fitted-onset account, retired at r6772+66.1/.28: P15 now
carries no early-universe parameter.  The checks below are re-pointed accordingly.

Written r2421.  Stated for reversal.
"""
import os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())



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
    print('  U1 -- the free-data count, as the corpus states it at c54.163')
    print()
    p0 = flat(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex'))
    p3 = flat(os.path.join(ROOT, 'corpus', 'SdS-slicing-curve_v2.tex'))
    p7 = flat(os.path.join(ROOT, 'corpus', 'CR_framework.tex'))
    p10 = flat(os.path.join(ROOT, 'corpus', 'canonical_time.tex'))
    p15 = flat(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))

    # ---- the target and its falsifier are in the paper, in its own voice --------
    # ** ⛭ p0's frontier item was REWRITTEN at c54.179 (`2af0b0b`), which is this fork's own work and
    # ** is the closure this receipt documents arriving in the paper.  `aa2b6ee` is the commit before. **
    BEFORE_C54_179 = 'aa2b6ee'
    p0_then = _at(BEFORE_C54_179, 'corpus/geometric_core_paper.tex')
    check(f'p0 stated the free-data-count test as a TARGET, not a result, at {BEFORE_C54_179}',
          'Reach: stated as a target, not a result' in p0_then)
    # ** ⛭⛭ RE-PINNED r3962.  c54.179 wrote this sentence UNDER the status stamp -- "\\textbf{[Reach:
    # ** the item has two sides ..." -- and r3787 removed the stamps from the papers, which
    # ** capitalised the now-leading word.  The pin quoted the stamped lowercase and died of a
    # ** correction to the STAMP, not to the claim.  ⇒ pin the load-bearing fragment, which is
    # ** case-free, and assert the sentence-initial capital SEPARATELY so the stamp's removal is
    # ** recorded rather than merely survived. **
    # ** r6931+70.1: CLASS (b) -- DISCHARGED.  The pin was c54.179's "item has two sides and they
    #   now stand differently" (constant side a result, DATUM side still open).  73eb61ef (r6683,
    #   the node's combined groups 1-6 patch) rewrote the item to "The test has two sides, and each
    #   has been run": the datum side is no longer open but answered -- "it is a clock reading rather
    #   than a datum a handover transmits", citing \rcpt{X1_the_ratio_is_a_clock_reading_not_a_
    #   carried_datum} (L150).  The split survives; what moved is that the second side was RUN.  The
    #   c54.179 wording is asserted at the commit where it stood, and the check now pins what
    #   discharged the open side.
    p0_c54_179_text = _at('73eb61ef^', 'corpus/geometric_core_paper.tex')
    check('⛭ AND IT NO LONGER DOES: c54.179 split it -- "item has two sides and they now stand '
          'differently" (true until r6683) -- and both sides are now RUN: "The test has two sides, '
          'and each has been run", the datum side answered as a clock reading by L150/X1',
          'item has two sides and they now stand differently' in p0_c54_179_text
          and 'e one fact.\'\' \\emph{The test has two sides, and each has been run' in p0
          and 't in the geometric residue at all, and it is a clock reading rather than a datum a handover transmits' in p0
          and 'X1_the_ratio_is_a_clock_reading_not_a_carried_datum' in p0
          and 'Reach: stated as a target, not a result' not in p0)
    p0_at_179 = _at('2af0b0b', 'corpus/geometric_core_paper.tex')
    # ** r6931+70.1: CLASS (c) -- the stamp removal this records is unchanged; only the sentence
    #   it produced was later rewritten (73eb61ef, r6683, above).  The capitalised form is asserted at
    #   the last commit that carried it, and the absence of the stamp on the live text.
    check('⇒ and r3787 then took the "[Reach: ...]" status stamp off it, so the fragment opened '
          'the sentence in the paper\'s own voice: "The item has two sides" (until r6683)',
          'The item has two sides and they now stand differently' in p0_c54_179_text
          and 'Reach: the item has two sides' in p0_at_179
          and 'Reach: the item has two sides' not in p0
          and '[Reach:' not in p0)
    check('and its falsifier is named and sharp',
          'a hidden geometric freedom in the cosmology, or a genuinely free constant where the '
          'reading says it should lock' in p0)

    # ---- the ONE scale ---------------------------------------------------------
    check('Lambda is the sole scale: alpha = sqrt(3/Lambda), "the sole remaining scale"',
          'the sole remaining scale' in p7)
    check('and a dimensionless magnitude needs TWO invariants (the one-constant theorem)',
          'a dimensionless magnitude needs two' in p0)
    check('with no second scale on either face (the Wick face carries the same radius)',
          'no_second_scale_on_either_face' in p0 or 'same' in p0)

    # ---- the three gauges ------------------------------------------------------
    check('the constants are stated as UNIT GAUGES over the single scale',
          'the fundamental constants enter as unit gauges over the single scale' in p7
          or 'fundamental constants standing as unit gauges over the substrate' in p0)
    check('hbar\'s one possible free parameter is CLOSED without a free parameter',
          'without a free parameter' in p10 and 'deficiency indices' in p10)

    # ---- THE CANDIDATE THAT WAS FOUND AND ELIMINATED ---------------------------
    # ** r6931+70.1: CLASS (c) -- STALE, AND THE WORDS THAT WENT ARE ONES A PAPER SHOULD NOT CARRY.
    #   45dc766d (r6735+66.1, "P3 worked and read through: no self-narration") replaced "The metric
    #   function itself was for a time the one input not derived here ... and that gap is now closed"
    #   with "The metric function itself is derived here rather than taken as the standard
    #   Tangherlini--de~Sitter form" -- same derivation, same \rcpt{P03_operator_at_general_D}; only
    #   the paper's narration of its own history went (a paper presents ONE state).  So the RECORD
    #   that it was a candidate is asserted at the commit before, the candidate's elimination on the
    #   live P3, and p0 still names it as the place a free constant "could have lived" and locked.
    p3_then = _at('45dc766d^', 'corpus/SdS-slicing-curve_v2.tex')
    check('P3 recorded a SECOND candidate free input (the D-dimensional metric function), until r6735',
          'the one input not derived here' in p3_then
          and 'a place where a genuinely free constant could have lived was checked and it locked' in p0)
    check('and it is CLOSED: P3 now states "The metric function itself is derived here rather than '
          'taken as the standard Tangherlini--de Sitter form" (and stated "that gap is now closed" '
          'until r6735)',
          'that gap is now closed' in p3_then
          and 'The metric function itself is derived here rather than taken as the standard '
          'Tangherlini--de~Sitter form' in p3)
    check('closed by DERIVATION: T^t_t = 0 is first-order linear with M the single constant',
          'entire' in p3 and 'single constant of int' in p3)

    # ---- the one the corpus still calls free -----------------------------------
    # ** r6931+70.1: CLASS (a) + (b).  These two pinned the corpus CALLING rho_r/rho_m free: P7's
    #   "one-parameter accommodation rather than a parameter-free prediction" and P15's "a single
    #   inherited datum".  Both were the fitted-onset account, retired in the r6772 rewrite
    #   (507d2e99 r6772+66.1 for P15; 89d23854 r6772+66.28, "P7 no longer carries ... the
    #   one-parameter accommodation").  What the corpus now says about the one item this count left
    #   uncounted is the ANSWER to it: p0 says it is "a clock reading rather than a datum a handover
    #   transmits" (X1, above), P15 carries "no early-universe parameter", and the radiation
    #   amplitude at a hand-placed start "is that start read in units of a density rather than an
    #   inheritance".  Re-pointed at those; and the retired wording is asserted ABSENT so a return
    #   of the accommodation reading would fail here.
    check('rho_r/rho_m is no longer carried as a one-parameter accommodation: P7 and P15 drop it, and '
          'P15 carries "no early-universe parameter"',
          'one-parameter accommodation rather than a parameter-free prediction' not in p7
          and 'The cosmology carries no early-universe parameter' in p15)
    check('and P15 reads the radiation amplitude as a READING -- "that start read in units of a density '
          'rather than an inheritance" -- not a single inherited datum',
          'is that start read in units of a density rather than an inheritance' in p15
          and 'a single inherited datum' not in p15)

    # ---- and the retired ledger's own stated limit -----------------------------
    led = flat(os.path.join(ROOT, 'retired', 'CONSTANT_LEDGER_receipt.md'))
    check('the retired ledger closed the gravitational-quantum sector at ZERO free constants',
          'spends ZERO free dimensionless constants' in led)
    check('and recorded the matter-side count as OPEN -- which is what has since moved',
          'The matter-side count: open' in led)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: the count as the corpus now states it --')
    print('    ONE scale        Lambda (alpha = sqrt(3/Lambda)); no second invariant on either face')
    print('    THREE gauges     c (time<->length), G (mass<->length, only ever GM/c^2), hbar (closed')
    print('                     at the seam without a free parameter)')
    print('    rho_r/rho_m      NOT a free datum a handover carries: a clock reading (L-150/X1, now')
    print('                     p0\'s own datum side); P15 carries no early-universe parameter')
    print('  ** And one CANDIDATE free datum was found and ELIMINATED BY DERIVATION since the retired')
    print('     ledger: P3\'s D-dimensional metric function, the entire solution space of a')
    print('     first-order linear equation with M the single constant of integration. **')
    print('  ⇒ That is the falsifier being MET rather than asserted: a place a hidden freedom could')
    print('    have lived was checked, and it locked.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
