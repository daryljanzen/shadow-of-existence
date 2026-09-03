#!/usr/bin/env python3
"""A1 -- two checks asserted that a request was still unanswered, and node 57 answered it.  They went
red on the settlement they existed to ask for.

COMPUTES: both sites read from the commit that carried them; the sentence each required and that the
gate no longer carries it; that the gate carries the ANSWER instead, in the other line's own words;
that the replacement property survives the answer, shown by a seed that unsets the answer and checks
the gate's wording changes while both receipts stay green.  No parameter is pinned.

** ⛭ ⓵ THE TWO SITES. **  `L-256`'s `B1` ⓺ and `L-251`'s `N1` ⓹ᶜ each required the band gate to say
*"is a REQUEST, not an assumption"* -- that the other line taking the odd half was **not presumed
answered**.  *Both were written to be careful: they were checking that a claim had NOT been
overstated.*

** ⛔⛭⛭ ⓶ AND THE ANSWER BROKE THEM. **  Node 57: *"The band is accepted.  This tree now runs
`PARITY = 1`, so your gate is answered rather than presumed."*  The gate stopped saying the half was
unanswered, because it no longer was.
  ⇒ *** A CHECK ON WHETHER A QUESTION IS STILL OPEN PUNISHES THE QUESTION BEING ANSWERED.  It is
      r3105's rule with "still open" as the thing that moves -- and the fourth disguise of it in one
      turn, after a live directory, a live register, a section title and a distance from HEAD. ***

** ⌗ ⓷ THE REPAIR IS THE SAME SHAPE EVERY TIME: ASSERT THE PROPERTY THE REQUEST WAS FOR, NOT THE
STATE OF THE REQUEST. **  *The request existed so that the gate could not call itself prevention on a
half it did not hold.*  ⇒ ** That property is a fact about the gate, it is what was actually wanted,
and it SURVIVES the answer -- which is exactly what "the half is still unheld" did not. **
  ⌗ *And it is the stronger check: the old form passed on a gate that said the right words and did
  nothing; the new one fails unless the gate's behaviour changes when the half is taken away.*

WHAT IS NOT CLAIMED.  ** Not that a check may never read a request's state ** -- a receipt recording
that something was routed and unanswered AT A COMMIT is a pinned historical fact and is fine; what
fails is reading it live.  ** Not that this is a new class ** -- it is `L-258`'s, and the reason to
register it separately is that the disguise is new and the corpus's record of a class is a list of
its disguises.  ** And not that the sweep is complete ** -- the same limit as `L-258`: "pins" is not
mechanically separable from "checks", so these are found by running the suite, not by a detector.

    python3 receipts/L261_the_question_was_answered/A1_a_check_on_whether_a_question_is_still_open_punishes_the_answer.py

Written r3142, `L-261`.  Stated for reversal.
"""
import contextlib
import glob
import io
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
# ** ⛭⛭ NODE IS SET HERE, BEFORE THE IMPORT (r3964, with `L251/N1`). **  `check_revision_collisions`
# ** reads `NODE` AT IMPORT TIME and *refuses to default* when unset -- r3679's rule, written after an
# ** unset NODE silently certified the EVEN half on odd-banded trees and passed 21 collisions.  The
# ** refusal is right; what was wrong is this file inheriting the answer from whoever ran it: unset in
# ** a plain shell, `ci` under `sweep_gates.sh`.  ** A receipt asserting anything about a band is
# ** making a claim about a NAMED line and must name it. **  Four receipts shared this defect and all
# ** four were on the failure list; they are fixed together because it is one fault, not four.
# ⛔ *** SET, NOT `setdefault` (r3988). ***  `setdefault` defers to the caller, and the suite runner
# and CI both export `NODE=ci` -- for which the gate's own table gives `PARITY = None`, "the runner
# is not a line and holds no half".  ** So under CI this receipt still read the caller's answer and
# still failed, which is the exact defect the note above says it is fixing. **  A receipt asserting
# `C.PARITY == 0` is making a claim about node 60's band; it must NAME that line unconditionally.
#   ⌗ *I wrote the reasoning and then implemented the opposite of it.  The verb was the whole fix.*
os.environ['NODE'] = '60'
import check_revision_collisions as C                                     # noqa: E402

FAILED = []
BEFORE = '0b9e6c87'          # r3140 -- B1 repaired there, N1 not yet
B1 = glob.glob(os.path.join(ROOT, 'receipts', 'L256_the_band_taken', 'B1_*.py'))[0]
N1 = glob.glob(os.path.join(ROOT, 'receipts', 'L251_the_numbering_collides', 'N1_*.py'))[0]
GATE = os.path.join(ROOT, 'corpus', 'check_revision_collisions.py')
#: ** the two sites required DIFFERENT literals for the same fact, which is itself the point: the
#: shape is "the request is still open", and it was spelled two ways in two files. **
SENT_B1 = 'not presumed answered'
SENT_N1 = 'is a REQUEST, not an assumption'


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a), capture_output=True, text=True,
                          errors='replace').stdout


def run(path):
    return subprocess.run([sys.executable, path], cwd=os.path.dirname(path), capture_output=True,
                          text=True, errors='replace', timeout=900).returncode


def main():
    print()
    print('  A1 -- the question was answered, and two checks went red for it')
    print()

    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ BOTH SITES REQUIRED THE REQUEST TO BE STILL OPEN')
    print('  ' + '=' * 74)
    b1_was = git('show', f'{BEFORE}^:{os.path.relpath(B1, ROOT)}')
    n1_was = git('show', f'{BEFORE}:{os.path.relpath(N1, ROOT)}')
    check(f'⓵ `B1` ⓺ required the gate to carry "{SENT_B1}"',
          f"'{SENT_B1}' in text" in b1_was)
    check(f'⓵ᵇ `N1` ⓹ᶜ required "{SENT_N1}" -- the same fact spelled differently, in a second file',
          SENT_N1 in n1_was)
    check('⓵ᶜ ⌗ and both were written to be CAREFUL -- each was checking that a claim had not been '
          'overstated, which is the habit that usually makes a check safe',
          'not presumed answered' in b1_was and 'not presumed assumed' not in n1_was
          and 'said rather than assumed' in n1_was)

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔ AND THE ANSWER BROKE THEM')
    print('  ' + '=' * 74)
    gate = open(GATE, encoding='utf-8').read()
    check(f'⓶ the gate carries NEITHER spelling now -- "{SENT_B1}": {SENT_B1 in gate}, '
          f'"{SENT_N1}": {SENT_N1 in gate} -- because the half is no longer unheld',
          SENT_B1 not in gate and SENT_N1 not in gate)
    check('⓶ᵇ and it carries the ANSWER instead, in the other line\'s own words',
          C.OTHER_HALF is not None and 'PARITY = 1' in C.OTHER_HALF
          and 'node 57' in C.OTHER_HALF)
    check('⓶ᶜ ⇒ *** so a check on whether a question is still OPEN punishes the question being '
          'answered -- r3105\'s rule with "still open" as the thing that moves ***',
          f"'{SENT_B1}' in text" in b1_was and SENT_N1 in n1_was
          and SENT_B1 not in gate and SENT_N1 not in gate)

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⌗ THE REPAIR: THE PROPERTY THE REQUEST WAS FOR, NOT THE REQUEST')
    print('  ' + '=' * 74)
    b1, n1 = open(B1, encoding='utf-8').read(), open(N1, encoding='utf-8').read()
    check('⓷ both now assert the gate\'s BEHAVIOUR -- that it refuses the word "prevention" while '
          '`OTHER_HALF` is unset -- rather than the state of the request',
          'THE BAND IS A PROPOSAL, NOT A PREVENTION' in b1
          and 'THE BAND IS A PROPOSAL, NOT A PREVENTION' in n1
          and SENT_N1 not in b1 and SENT_N1 not in n1)
    check(f'⓷ᵇ and both exit 0', run(B1) == 0 and run(N1) == 0)

    # ** THE SEED, AND IT IS WHAT SHOWS THE NEW FORM IS STRONGER RATHER THAN MERELY DIFFERENT:
    #   take the answer away and the gate's BEHAVIOUR must change.  The old form checked a
    #   sentence, which a gate can carry while doing nothing. **
    keep = C.OTHER_HALF
    try:
        C.OTHER_HALF = None
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            C.check_band()
        unheld = buf.getvalue()
        C.OTHER_HALF = keep
        buf2 = io.StringIO()
        with contextlib.redirect_stdout(buf2):
            C.check_band()
        held = buf2.getvalue()
    finally:
        C.OTHER_HALF = keep
    # ** ⛭⛭⛭ RE-PINNED r3966, AND THE PHRASE IT PINNED WAS WITHDRAWN ON THIS FILE'S OWN ARGUMENT. **
    # ** The held branch used to print *"the prevention is real"*.  r3640 struck that: the gate had
    # ** printed it *** THROUGH TEN OUT-OF-BAND COMMITS FROM THE OTHER LINE *** -- `r3622..r3638`,
    # ** ten consecutive ids in this line's half, written by the other, while the gate reassured the
    # ** reader the partition was whole.  It now says what is TRUE instead: ** "the other half is
    # ** DECLARED held.  That is a claim by the other line, not a measurement made here, and it has
    # ** been wrong." **
    #   ⇒ *** THIS FILE'S WHOLE THESIS IS THAT A CHECK MUST ASSERT BEHAVIOUR AND NOT A FORM OF WORDS
    #       A GATE COULD CARRY WHILE DOING NOTHING -- and "the prevention is real" turned out to be
    #       exactly such a form of words.  The pin outlived the sentence by holding the reassurance
    #       the gate had already learned not to make. ***
    #   ⌗ The seeded discrimination is kept and is SHARPER for it: the two branches must differ, the
    #     unheld one must refuse the word `prevention`, and the held one must claim DECLARATION
    #     rather than measurement.  A gate that went back to reassuring would fail this.
    check('⓸ SEEDED: with the answer removed the gate says "PROPOSAL, NOT A PREVENTION"; with it '
          'restored it says the half is DECLARED held and that the declaration "has been wrong" -- '
          'so the replacement checks BEHAVIOUR, and neither branch offers a reassurance the gate '
          'has not measured (r3640 withdrew "the prevention is real" for being exactly that)',
          'PROPOSAL, NOT A PREVENTION' in unheld
          and 'the other half is DECLARED held' in held
          and 'not a measurement made here, and it has been wrong' in held
          and 'PROPOSAL, NOT A PREVENTION' not in held
          and 'prevention is real' not in held and 'prevention is real' not in unheld)
    check('⓸ᵇ and the answer is RESTORED -- verified, not trusted to the `finally`',
          C.OTHER_HALF == keep and C.OTHER_HALF is not None)
    check('⓹ ⌗ and the pinned historical fact is untouched: `N1` still records that it ROUTED the '
          'band and that the routing was withdrawn, which is a claim about commits and not about '
          'the present', 'WITHDRAWN r3128' in n1)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** a check on whether a question is still OPEN punishes the question being')
    print('  answered. **  *Two checks required the band gate to say the odd half was "not presumed')
    print('  answered"; node 57 answered it, the gate stopped saying so, and both went red on the')
    print('  settlement they existed to ask for.*')
    print('  ⌗ ** The repair is the shape it always is: assert the property the request was FOR --')
    print('     that the gate cannot call itself prevention on a half it does not hold -- and not')
    print('     the state of the request. **  *That property survives the answer.*')
    print('  ⛭ ** And it is the stronger check: ** the old form passed on a gate that said the')
    print('     right words and did nothing; the new one fails unless the behaviour changes when')
    print('     the half is taken away, which the seed shows it does.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
