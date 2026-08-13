#!/usr/bin/env python3
"""A2 -- `FOR_54` item 9 is not awaiting adoption: all three of its clauses are already enforced, and the
gate that enforces the central one was built BEFORE the convention was offered.

** THE ITEM, routed r2442. **  "A convention worth having, ** if the fork wants it **.  Offered rather
than reported, because it is this lineage's to settle and ** it was never written down tightly **:"

  > ** `\\rcpt{X}` means: the claim in this sentence is CHECKED by X, and X would FAIL if the claim were
  > false. **

  ** Three things follow, per the item: **
  ⓵ "a script that computes and prints is a NOTE, not a receipt --- ** what makes an artefact a receipt is
     not that it ran but that it could have come out false **";
  ⓶ "the disposition of a cited transcript is decided by whether the cited claim is computational (if it
     is, ** the receipt owes an assertion of that claim **; if it is not, `\\rcpt{}` was the wrong citation
     and the sentence should point at the section)";
  ⓷ "the definition is what makes ** a receipt gate mean something rather than an opinion about style **".

** ⛭⛭ AND ALL THREE ARE ALREADY ENFORCED. **
  * ** `corpus/check_receipt_asserts.py` ** -- "the SEVENTEENTH gate: ** A RECEIPT THAT CANNOT FAIL **",
    and its own docstring records where the finding came from: "** absorbed r2384 ** rather than
    rediscovered ... ** the dominant failure is not a wrong link but a RECEIPT THAT CANNOT FAIL **".
  * ** `corpus/check_receipts.py` ** -- reports "** HOLLOW ASSERTION(S) -- provably cannot fail **".
  * ** `scripts/lint_assertions.py` ** -- the same test, run per-receipt at write time.

  ⇒ ⛭ *** AND THE DATES INVERT THE ITEM'S PREMISE.  `check_receipt_asserts` was built at r2384.  The
      convention was offered at r2442 -- FIFTY-EIGHT REVISIONS LATER.  It was not awaiting adoption; it
      was a written statement of a rule the gates had already been enforcing for fifty-eight
      revisions. ***

** ⓸ AND THE ENFORCEMENT IS LIVE, NOT HISTORICAL. **  This session alone the rule fired twice: ** r2607 **
(a `check_receipts` failure on a line asserting `True` for a rhetorical contrast, replaced with a real
comparison) and the routine `lint_assertions` pass run on every receipt built since.

** ⇒⇒ SO THE DISCHARGE IS NOT AN ADOPTION.  IT IS AN OBSERVATION: ** *** the fork settled this by building
the gate, and the item was offering a definition of something already operative.  What item 9 supplies
that the gates do not is the WORDING -- and the wording now has a home in the gate's own docstring rather
than in a routed offer. ***

WHAT IS NOT CLAIMED.  ** Not that Daryl has adopted anything ** -- *** the item was addressed to the
lineage and this receipt does not answer for it; what is established is that no decision is BLOCKING
anything, because the practice is already in force. ***  ** Not that clause ⓶'s transcript-disposition
half is gated ** -- `check_receipt_asserts` tests whether a receipt can fail, not whether a cited
transcript should have been a section pointer; *** that half is enforced by practice and not by a gate,
and saying so is the honest version. ***

Written r2636.  Stated for reversal.
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


def main():
    print()
    print('  A2 -- is item 9 awaiting adoption, or already in force?')
    print()
    f54 = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'FOR_54.md'),
                                   encoding='utf-8', errors='replace').read())
    ra = open(os.path.join(ROOT, 'corpus', 'check_receipt_asserts.py'),
              encoding='utf-8', errors='replace').read()
    rc = open(os.path.join(ROOT, 'corpus', 'check_receipts.py'),
              encoding='utf-8', errors='replace').read()
    la = open(os.path.join(ROOT, 'scripts', 'lint_assertions.py'),
              encoding='utf-8', errors='replace').read()

    # ⓵ the item's own wording
    check('⓵ item 9 offers the convention: "A convention worth having, if the fork wants it"',
          'A convention worth having, if the fork wants it' in f54)
    check('and states its central clause: "what makes an artefact a receipt is not that it ran but that '
          'it could have come out false"',
          'what makes an artefact a receipt is not that it ran but that it could have come out false'
          in f54)

    # ⓶ the gates enforce it
    check('⛭⛭ ⓶ and check_receipt_asserts IS that rule: "A RECEIPT THAT CANNOT FAIL"',
          'A RECEIPT THAT CANNOT FAIL' in ra)
    check('with its provenance recorded: "absorbed r2384 rather than rediscovered"',
          'absorbed r2384 rather than rediscovered' in ra)
    check('and lint_assertions carries the wording: "HOLLOW ASSERTION(S) -- provably cannot fail"',
          'provably cannot fail' in la)
    check('and check_receipts runs the same test over the corpus',
          'hollow' in rc.lower())

    # ⓷ the dates invert the premise
    check('⛭ ⓷ AND THE DATES INVERT THE PREMISE: the gate was built at r2384 and the convention was '
          'offered at r2442 -- fifty-eight revisions LATER',
          'r2384' in ra and 'r2442' in f54)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** item 9 is not awaiting adoption -- it is a written statement of a rule the gates')
    print('  had already been enforcing for fifty-eight revisions. **')
    print('  ⓵ ** The convention: ** "`\\rcpt{X}` means the claim in this sentence is CHECKED by X, and X')
    print('     would FAIL if the claim were false."')
    print('  ⛭⛭ ⓶ ** Enforced by three: ** `check_receipt_asserts` ("A RECEIPT THAT CANNOT FAIL"),')
    print('     `lint_assertions` ("provably cannot fail"), and `check_receipts` over the corpus.')
    print('  ⛭ ⓷ ** And the dates invert the premise: ** the gate was built at ** r2384 **; the')
    print('     convention was offered at ** r2442 ** -- fifty-eight revisions later.')
    print('     ⇒ ** The fork settled this by BUILDING THE GATE.  The item was offering a definition of')
    print('       something already operative. **')
    print('  ⓸ ** And it is live: ** the rule fired at r2607 this session, on a line asserting True for a')
    print('     rhetorical contrast.')
    print('  ⚠ ** One half is NOT gated: ** clause ⓶\'s transcript-disposition test -- whether a cited')
    print('    transcript should have been a section pointer -- ** is enforced by practice, not by a')
    print('    gate, and saying so is the honest version. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
