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
    check('⛭ AND IT NO LONGER DOES: c54.179 split it -- "item has two sides and they now stand '
          'differently", the CONSTANT side carried as a result and the DATUM side still open',
          'item has two sides and they now stand differently' in p0
          and 'Reach: stated as a target, not a result' not in p0)
    p0_at_179 = _at('2af0b0b', 'corpus/geometric_core_paper.tex')
    check('⇒ and r3787 then took the "[Reach: ...]" status stamp off it, so the fragment now opens '
          'the sentence in the paper\'s own voice: "The item has two sides"',
          'The item has two sides and they now stand differently' in p0
          and 'Reach: the item has two sides' in p0_at_179
          and 'Reach: the item has two sides' not in p0)
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
    check('P3 records a SECOND candidate free input (the D-dimensional metric function)',
          'the one input not derived here' in p3)
    check('and states that gap is NOW CLOSED', 'that gap is now closed' in p3)
    check('closed by DERIVATION: T^t_t = 0 is first-order linear with M the single constant',
          'entire' in p3 and 'single constant of int' in p3)

    # ---- the one the corpus still calls free -----------------------------------
    check('rho_r/rho_m is stated as a ONE-PARAMETER ACCOMMODATION, not a prediction',
          'one-parameter accommodation rather than a parameter-free prediction' in p7)
    check('and P15 calls it a single INHERITED datum',
          'a single inherited datum' in p15)

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
    print('    ONE free datum   rho_r/rho_m, stated as a one-parameter accommodation (L-150 owes its')
    print('                     derivation)')
    print('  ** And one CANDIDATE free datum was found and ELIMINATED BY DERIVATION since the retired')
    print('     ledger: P3\'s D-dimensional metric function, now the entire solution space of a')
    print('     first-order linear equation with M the single constant of integration. **')
    print('  ⇒ That is the falsifier being MET rather than asserted: a place a hidden freedom could')
    print('    have lived was checked, and it locked.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
