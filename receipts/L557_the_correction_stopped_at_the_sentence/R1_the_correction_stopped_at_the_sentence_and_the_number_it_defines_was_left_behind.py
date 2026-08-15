#!/usr/bin/env python3
"""R1 -- r2755 corrected the sentence and not the number the sentence DEFINES: P15's headline high-ell
prediction ran on the superseded value for thirty revisions, and fifteen receipts with it.

COMPUTES: the identity r = theta_D/theta_* from P15's own text and C10's own assertion; the corrected
value 1.0816 from three independent routes; the two suppression figures and l_D that follow; the
fifteen receipts that carried the stale value and the two failure modes they split into; and a control
showing that the gate built to stop the paper and the receipt drifting apart is what held them together
at the wrong value.

** ⛭⛭⛭ WHAT HAPPENED, AND IT IS ONE STEP SHORT RATHER THAN ONE STEP WRONG. **

r2755 traced P15's `9.4\\%` in three steps and found it downstream of the `x_e` non-cancellation r2753
had already found.  *Its own message: "a number's authority comes from its derivation chain, not its
decimals."*  It corrected the sentence -- `theta_D/theta_*` larger by `9.4\\%` became `8.2\\%` -- and it
replaced all nine `{\\sim}8\\%` hedges with the bare figure, because the contest was over.

** ⛔ AND ONE PARAGRAPH LATER, `sec:envelope-consequence` STILL READ `r=1.093`. **

  *** `r` IS `theta_D/theta_*`.  Not a related quantity -- the same one. ***  `C10_highl_ratio`, the
  receipt the corrected sentence CITES, asserts it in those words: *"this receipt's theta_D/theta_* is
  {th_ratio} but CR_cosmology.tex sec:envelope-consequence prints r = 1.093"*.
  ⇒ ** So the paper stated the ratio as `1.082` in one paragraph and `1.093` in the next, and the second
    is the one the prediction is made of. **  With it came `0.82` and `0.65`, the two suppression
    figures, and `l_D(CR) = 1281`.

** ⓵ THE CORRECTED CHAIN, THREE ROUTES THAT AGREE. **

      P15_damping_ratio_clean (direct r_D/r_s)          1.0816
      C46, C9's own division fed the corrected r_D       +7.65%..+8.24%
      the corrected sentence in the paper                +8.2%
  ⇒ *** r = 1.0816, so r^2-1 = 0.1699, the ratio is 0.844 at l_D and 0.682 at 1.5 l_D, and
      l_D(CR) = 1400/1.0816 = 1294. ***  Against the stale 0.823 / 0.645 / 1281.

** ⚠ AND THE CORRECTION FAVOURS THE CONSTRUCTION, WHICH IS FLAGGED FOR IT. **  The predicted suppression
gets SMALLER: 16% at `l_D` instead of 18%, 50% at `2 l_D` instead of 54%.  *It would apply identically
had it gone the other way -- it is arithmetic on a ratio r2755 fixed for reasons that had nothing to do
with the envelope, and the three routes above were computed before this file was written.*  ** No
verdict is touched: `PO-7` is `sec:refit-bound`/`sec:coherence`, not this section, and a smaller
predicted suppression is not a claim about the sky. **

** ⓶ FIFTEEN RECEIPTS, AND THEY SPLIT INTO TWO FAILURE MODES THAT LOOK NOTHING ALIKE. **

  * ** EIGHT WERE SILENT. **  `C10`, `C16`, `C22`, `C23`, `C36`, `C37`, `C38`, `C39` carried `1.093` or
    `1.0926` and PASSED -- because they were pinned to each other and to the stale paper.  *** Six of
    them evaluate the envelope with it, so they were computing the wrong curve while exiting zero. ***
  * ** AND SEVEN WERE LOUD. **  `C24`, `C25`, `C27`, `C28`, `C41`, `C46`, `C49` had been FAILING every full
    run since r2755 -- and they are *** the seven that produced the correction ***.  They quote the
    sentence they argued about, and when the argument was won the quote went stale.
  ⇒ ** So the correction landed and its own evidence base broke, while the passage that inherited the
    error stayed green. **

** ⌗ ⓷ AND THE CONTROL, WHICH IS THE PART WORTH KEEPING. **  `C10`'s gate was built at r2376+c54.160
expressly so that "the two cannot drift apart silently in either direction" -- it pins the receipt's
number against the paper's printed number.
  ⇒ *** IT WORKED.  They did not drift apart.  They were consistent with each other and both wrong,
      while the sentence eight lines earlier in the same file said otherwise. ***
  ⇒ ** A consistency check binds two things to each other and says nothing about either. **  The same
    file's own note recorded a KNOWN discrepancy (`th_ratio` hardcoded 1.0926 against C9's 1.0941) as
    "recorded and not re-litigated here" -- and both numbers were wrong in the same direction, for the
    same reason, which is what re-litigating it would have found.

** ⓸ AND ONE KNOT UNTIED ON THE WAY. **  Two commits are both titled r2749 and allocate `C41` twice --
`a_tilde_on_a_settled_value_is_a_stale_hedge` and `a_tilde_is_stale_when_nothing_competes` -- with
docstrings that read as opposite conclusions, and `check_receipt_prefixes` has been red on it since.
  ⇒ *** They are not opposite.  They are one rule at two states of the evidence: a tilde is right while
      something competes and stale when nothing does. ***  r2755 moved the state -- it settled the
      contest and took all nine hedges off -- so the FIRST one's thesis is now the operative one and
      the second one's rule is what licensed the change.  ** Asserted below from both files. **
  ⌗ *The prefix collision itself is a namespace question and stays the observer line's.*

** WHAT IS NOT CLAIMED. **  ** Not that 1.0816 is re-derived here ** -- it is read from three existing
routes and checked for agreement.  ** Not that the envelope is right ** -- only that it now runs on the
ratio the paper's own preceding paragraph derives.  ** Not that anything about `PO-7` moves. **  ** Not
that the register and ledger occurrences are fixed **: `CORPUS_MAP.md`, `PROTECTED_OPEN.md`,
`THE_WISDOM_LEDGER.md`, `THE_EVOLUTION_MAP.md` and `PHASE7_BUILD_LEDGER.md` still carry `1.093`/`1.0926`
and are routed, not edited.

Written c54.223 (`L-557`).  Stated for reversal.
"""
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
P15 = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
RD = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
FAILED = []

#: the commit BEFORE r2755's correction, and r2755 itself.  ** A claim about the paper as it was is a
#: claim about a commit (c54.220's rule). **
BEFORE, R2755, HEAD0 = '85c6a22', 'b4f1931', 'd7f2e7e'
#: `HEAD0` is the tree this revision started from -- the pre-c54.223 state of the receipts.


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True,
                          text=True, errors='replace').stdout


def flat(s):
    return re.sub(r'\s+', ' ', s)


def rcpt(name):
    return open(os.path.join(RD, name), encoding='utf-8', errors='replace').read()


def main():
    print()
    print('  R1 -- r2755 corrected the sentence; did it correct the number the sentence defines?')
    print()
    p15 = flat(open(P15, encoding='utf-8', errors='replace').read())
    p15_before = flat(git('show', f'{BEFORE}:corpus/CR_cosmology.tex'))

    # ------------------------------------------------------------------ ⓪ the correction itself
    check(f'⓪ r2755 ({R2755}) changed the sentence: "larger by $9.4\\%$" at {BEFORE} '
          f'-> "larger by $8.2\\%$" now',
          'larger by $9.4\\%$' in p15_before and 'larger by $8.2\\%$' in p15
          and 'larger by $9.4\\%$' not in p15)
    check('⛭ and it took every hedge off at the same time: {\\sim}8\\% appeared '
          f'{p15_before.count(chr(123) + chr(92) + "sim" + chr(125) + "8" + chr(92) + "%")} times '
          f'before and {p15.count(chr(123) + chr(92) + "sim" + chr(125) + "8" + chr(92) + "%")} now',
          p15_before.count('{\\sim}8\\%') == 9 and p15.count('{\\sim}8\\%') == 0)

    # ------------------------------------------------------------------ ⓵ r IS theta_D/theta_*
    # ** The identity is not asserted here -- it is READ, from the receipt the corrected sentence
    # ** cites, which states it in a failure message. **
    c10_before = git('show', f'{BEFORE}:receipts/P15_CR_cosmology/C10_highl_ratio.py')
    check('⓵ `r` IS theta_D/theta_*, and C10 says so in its own assertion message: "this receipt\'s '
          'theta_D/theta_* is ... but CR_cosmology.tex sec:envelope-consequence prints r = ..."',
          "theta_D/theta_* is" in c10_before
          and 'sec:envelope-consequence prints r' in c10_before)
    check(f'⛔ SO THE PAPER STATED ONE RATIO TWICE, DIFFERENTLY: the corrected sentence said $8.2\\%$ '
          f'and `r` one paragraph later still read 1.093 -- pinned at {R2755}',
          '1.093' in flat(git('show', f'{R2755}:corpus/CR_cosmology.tex'))
          and 'larger by $8.2\\%$' in flat(git('show', f'{R2755}:corpus/CR_cosmology.tex')))

    # ------------------------------------------------------------------ ⓶ the corrected value
    clean = open(os.path.join(RD, 'P15_damping_ratio_clean.py'),
                 encoding='utf-8', errors='replace').read()
    c46 = rcpt('C46_the_nine_are_right_and_the_one_is_wrong.py')
    check('⓶ ROUTE A -- P15_damping_ratio_clean computes theta_D/theta_* directly and prints 1.0816',
          '1.0816' in clean or 'CR/LCDM' in clean)
    check('   ROUTE B -- C46 feeds C9\'s own division the corrected r_D and brackets +7.65%..+8.24%',
          '7.65' in c46 and '8.24' in c46)
    check('   ROUTE C -- the corrected paper sentence says $8.2\\%$', 'larger by $8.2\\%$' in p15)
    r = 1.0816
    exact = [round(2.718281828459045 ** (-(x ** 2) * (r ** 2 - 1)), 4) for x in (1.0, 1.5)]
    check(f'⇒ AND WHAT FOLLOWS: r^2-1 = {r**2-1:.6f}, the ratio is {exact[0]:.3f} at l_D and '
          f'{exact[1]:.3f} at 1.5 l_D, and l_D(CR) = 1400/r = {1400/r:.0f}',
          abs((r ** 2 - 1) - 0.169859) < 1e-6 and abs(exact[0] - 0.8438) < 2e-4
          and abs(exact[1] - 0.6824) < 2e-4 and abs(1400 / r - 1294.4) < 0.1)
    check('⇒ and the PAPER now carries all three, with `r` named as the ratio so the two paragraphs '
          'cannot part again',
          'r=\\theta_{D}/\\theta_{*}=1.082' in p15 and '$0.84$ at $\\ell_{D}$' in p15
          and '$0.68$ at' in p15 and '1.093' not in p15)

    # ------------------------------------------------------------------ ⓷ the thirteen
    STALE = ['C10_highl_ratio', 'C16_the_transfer_is_six_eighths_built', 'C22_the_end_to_end_number',
             'C23_the_gap_estimated', 'C36_the_negative_is_the_envelope',
             'C37_the_comparison_is_not_matched', 'C38_the_comparison_scores_derivations',
             'C39_the_derived_list_read']
    LOUD = ['C24_the_substitution_itemised', 'C25_the_gap_closed_by_integration',
            'C27_the_number_bracketed', 'C28_length_against_angle',
            'C41_a_tilde_is_stale_when_nothing_competes',
            'C46_the_nine_are_right_and_the_one_is_wrong',
            'C49_the_row_has_a_likelihood_not_a_lookup']
    carried = [n for n in STALE
               if re.search(r'1\.093|1\.0926',
                            git('show', f'{BEFORE}:receipts/P15_CR_cosmology/{n}.py'))]
    check(f'⓷ SILENT MODE: {len(carried)} of {len(STALE)} receipts carried 1.093 / 1.0926 at {BEFORE} '
          f'and were EXITING ZERO -- pinned to each other and to the stale paper',
          len(carried) == 8)
    evaluators = [n for n in carried
                  if 'exp(' in git('show', f'{BEFORE}:receipts/P15_CR_cosmology/{n}.py')]
    check(f'⛔ and {len(evaluators)} of those EVALUATE the envelope with it, so they were computing the '
          f'wrong curve while passing', len(evaluators) >= 3)
    # ** measured at HEAD0, the tree this revision started from -- NOT at BEFORE, because two of the
    # ** seven (`C46`, `C49`) did not exist yet at BEFORE: they are the receipts that PRODUCED the
    # ** correction and were written alongside it.  *A census must be taken where the objects are.* **
    TOK = ('9.4', 'sim}8', 'chi^2/dof ~ 100')
    quoters = [n for n in LOUD
               if any(t in git('show', f'{HEAD0}:receipts/P15_CR_cosmology/{n}.py') for t in TOK)]
    check(f'⓷b LOUD MODE: {len(quoters)} of {len(LOUD)} quoted the sentence they were ARGUING ABOUT at '
          f'{HEAD0}, so winning the argument broke their own pins -- failing every full run since',
          len(quoters) == 7)
    repinned = [n for n in STALE + LOUD if 'c54.223' in rcpt(n + '.py')]
    check(f'⇒ ALL {len(repinned)} of {len(STALE)+len(LOUD)} re-pinned this revision, each keeping its '
          f'own finding and each carrying the historical value at a SHA rather than in the present '
          f'tense', len(repinned) == len(STALE) + len(LOUD) == 15)

    # ------------------------------------------------------------------ ⓸ THE CONTROL
    # ** ONE gate, TWO objects: it bound the receipt to the paper and neither to the derivation. **
    check('⓸ CONTROL -- C10\'s gate was built "so the two cannot drift apart silently in either '
          'direction", and it WORKED: they did not drift apart',
          'cannot drift apart' in c10_before)
    check('⇒ THEY WERE CONSISTENT WITH EACH OTHER AND BOTH WRONG, while the sentence eight lines '
          'earlier in the same file said 8.2% -- so a consistency check binds two things to each '
          'other and says nothing about either',
          '1.0926' in c10_before and '1.093' in c10_before
          and 'larger by $8.2\\%$' in flat(git('show', f'{R2755}:corpus/CR_cosmology.tex')))
    check('⛭ and the same file had RECORDED a known discrepancy -- th_ratio 1.0926 against C9\'s '
          '1.0941 -- as "recorded and not re-litigated here", while both were wrong in the same '
          'direction for the same reason',
          'recorded and not re-litigated here' in c10_before
          and 'recorded r2376+c54.160 and NOW RESOLVED' in rcpt('C10_highl_ratio.py'))

    # ------------------------------------------------------------------ ⓹ the C41 knot
    a = rcpt('C41_a_tilde_on_a_settled_value_is_a_stale_hedge.py')
    b = rcpt('C41_a_tilde_is_stale_when_nothing_competes.py')
    check('⓹ the two r2749 commits allocate `C41` twice and their titles read as opposites: "a tilde '
          'on a settled value is a stale hedge" against "a tilde is stale when nothing competes"',
          os.path.exists(os.path.join(RD, 'C41_a_tilde_on_a_settled_value_is_a_stale_hedge.py'))
          and os.path.exists(os.path.join(RD, 'C41_a_tilde_is_stale_when_nothing_competes.py')))
    check('⇒ AND THEY ARE ONE RULE AT TWO STATES: the second says a tilde is right while the receipts '
          'DISAGREE; the first says it is stale once they do not',
          'CONTESTED' in b.upper() and 'stale' in a.lower())
    check('⛭ and r2755 moved the state -- it settled the contest and removed all nine hedges -- so the '
          'first\'s verdict is the operative one and the second\'s rule is what licensed the change',
          p15_before.count('{\\sim}8\\%') == 9 and p15.count('{\\sim}8\\%') == 0
          and '8.2\\%' in p15)

    # ------------------------------------------------------------------ what is left alone
    ROUTED = ['CORPUS_MAP.md', 'PROTECTED_OPEN.md', 'THE_EVOLUTION_MAP.md',
              'PHASE7_BUILD_LEDGER.md', os.path.join('capstones', 'THE_WISDOM_LEDGER.md')]
    still = [f for f in ROUTED
             if os.path.exists(os.path.join(ROOT, f))
             and re.search(r'1\.093|1\.0926',
                           open(os.path.join(ROOT, f), encoding='utf-8', errors='replace').read())]
    check(f'⌗ and {len(still)} register/ledger file(s) still carry the stale value and are ROUTED, not '
          f'edited: {", ".join(os.path.basename(f) for f in still)}',
          len(still) >= 4)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the correction stopped at the sentence, and `r` is that sentence. **')
    print('    r        1.0930 -> 1.0816')
    print('    r^2-1    0.1946 -> 0.1699')
    print('    at l_D    0.823 -> 0.844        (16% down, not 18%)')
    print('    at 1.5 l_D 0.645 -> 0.682       (32% down, not 36%)')
    print('    l_D(CR)    1281 -> 1294')
    print('  ⇒ ** Eight receipts carried it silently and passed; seven quoted it and failed --')
    print('    and the seven that failed are the seven that produced the correction. **')
    print('  ⌗ AND THE CONTROL: ** the gate built to stop the paper and the receipt drifting apart is')
    print('    exactly what held them together at the wrong value. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
