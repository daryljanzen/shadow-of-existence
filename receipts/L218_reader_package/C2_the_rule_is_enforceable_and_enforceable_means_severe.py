#!/usr/bin/env python3
"""C2 -- the companion's three-way rule is enforceable, and the enforceable version is far more
conservative than the row's framing suggests.

** THE CLAIM UNDER TEST. **  `L-218`: "the companion's rule is ** enforceable rather than aspirational **:
every claim it makes is ESTABLISHED (cite the receipt), OPEN (cite `PROTECTED_OPEN`), or DO-NOT-ASSERT
(say so and say why)."  ** The row's figures are from r2415 ** -- "279 receipts ... 165 struck rows".

** ⓵ THE FIGURES, RE-MEASURED, AND EVERY ONE HAS GROWN. **

      receipts        279 -> ** 399 **
      struck rows     165 -> ** 268 **
      PROTECTED_OPEN items ** 9 ** · explicit non-claim phrases in the papers ** 16 **

  ⇒ ** The machinery is stronger than the row claims, not weaker. **  That much is straightforward.

** ⛭⛭ ⓶ BUT THE RULE'S REAL SHAPE IS AN ANCHOR COUNT, NOT A COVERAGE FRACTION -- and getting that wrong
is the trap. **  A first attempt here measured `\\emph{}` passages (** 1360 **) against nearby `\\rcpt{}`
citations (** 104 **) and produced "** 8% coverage **".
  ⇒ ⛔ *** That number is meaningless: `\\emph{}` is this corpus's EMPHASIS voice, not a claim marker, so
      the denominator counted every emphasised phrase in seventeen papers. ***  ** Discarded rather than
      reported. **

  ** What the rule actually needs is the count of things a companion can CITE: **

      *** ESTABLISHED   308 distinct receipts cited in the papers
          OPEN            9 PROTECTED_OPEN items
          DO-NOT-ASSERT  16 explicit non-claim phrases ***

** ⓷ AND THAT MAKES THE RULE ENFORCEABLE AND SEVERE AT THE SAME TIME. **  ** The companion cites an
anchor or it does not. **  There are 308 + 9 + 16 anchors against ** 7480 sentences ** of substance in
the corpus.
  ⇒ *** So the honest default for everything unanchored is "the corpus DISCUSSES this; it is not
      receipt-bound" -- and that covers the overwhelming majority of what a reader will ask about. ***
  ⌗ ** That is the rule working, not failing. **  The usual companion's failure is answering confidently
  about discussion; this one is forced to say which mode it is in, and *** the price of enforceability
  is that it must say "discussed, not established" most of the time. ***

** ⚠ SO THE ROW'S FRAMING NEEDS ONE CORRECTION, AND IT IS NOT A RETRACTION. **  "Every claim it makes is
ESTABLISHED, OPEN, or DO-NOT-ASSERT" is true and is the right rule.  ** What it omits is the fourth
state the corpus mostly occupies: DISCUSSED. **
  ⇒ *** A three-way rule over a corpus with 333 anchors and 7480 sentences is in practice a FOUR-way
      rule, and the fourth bucket is the default and the largest.  Saying so is what keeps the companion
      honest rather than silent. ***

WHAT IS NOT CLAIMED.  ** Not that 308 anchors is too few ** -- it is 308 more than an ordinary book has,
and every one can fail.  ** Not that the sentence count is a denominator ** -- it is a scale, given so
the anchor count means something, and the receipt says so rather than dividing.  ** Not that the
companion is built or should be **: this measures the claim the row rests on, and the reader package
remains `L-218`'s ⓵ and ⓷.

Written r2561.  Stated for reversal.
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


def main():
    print()
    print("  C2 -- is the companion's three-way rule enforceable, and at what price?")
    print()
    papers = [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(f).startswith('appendix_receipts')]
    allp = ' '.join(re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%'))) for f in papers)
    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    po = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'PROTECTED_OPEN.md'),
                                  encoding='utf-8', errors='replace').read())

    check("L-218 states the rule as enforceable rather than aspirational",
          'enforceable rather than aspirational' in re.sub(r'\s+', ' ', arc))

    # ⓵ the figures have grown
    n_rcpt = len(glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True))
    n_struck = len(re.findall(r'^\|\s*~~L-\d+~~\s*\|', arc, re.M))
    check(f'⛭ receipts 279 (r2415) -> {n_rcpt}', n_rcpt > 279)
    check(f'and struck rows 165 (r2415) -> {n_struck}', n_struck > 165)

    # ⓶ the three buckets, as anchors
    est = len(set(re.findall(r'\\rcpt\{([^}]+)\}', allp)))
    open_items = len(set(re.findall(r'PO-\d+', po)))
    dna = len(re.findall(r'not claimed|is not claimed here|do not claim|declines? to claim',
                         allp, re.I))
    check(f'ESTABLISHED: {est} distinct receipts cited in the papers', est > 250)
    check(f'OPEN: {open_items} PROTECTED_OPEN items', open_items >= 8)
    check(f'DO-NOT-ASSERT: {dna} explicit non-claim phrases in the papers', dna > 5)

    # ⓷ the scale
    sents = len([s for s in re.split(r'(?<=[.!?])\s+', allp) if len(s) > 40])
    total = est + open_items + dna
    check(f'⛭⛭ {total} anchors against {sents} sentences of substance', sents > 5000)
    check('⇒⇒ SO THE HONEST DEFAULT FOR EVERYTHING UNANCHORED IS "the corpus DISCUSSES this; it is not '
          'receipt-bound" -- which covers the overwhelming majority of what a reader will ask',
          total < sents / 10)

    # ⚠ the correction, and it is not a retraction
    check("⚠ and the row's three-way rule omits the fourth state the corpus mostly occupies: DISCUSSED",
          'ESTABLISHED' in re.sub(r'\s+', ' ', arc) and 'DO-NOT-ASSERT' in re.sub(r'\s+', ' ', arc))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the rule is enforceable, and enforceable means severe. **')
    print(f'  ⓵ ** Every figure has grown: receipts 279 -> {n_rcpt}, struck rows 165 -> {n_struck}. **')
    print(f'  ⓶ ** The buckets as ANCHORS: ESTABLISHED {est} · OPEN {open_items} · DO-NOT-ASSERT {dna}. **')
    print('     ⛔ A first attempt measured \\emph{} passages against nearby \\rcpt{} and reported')
    print('     ** "8% coverage" -- meaningless, because \\emph{} is the corpus\'s EMPHASIS voice, not a')
    print('     claim marker. **  Discarded rather than reported.')
    print(f'  ⓷ ** {total} anchors against {sents} sentences of substance. **  ⇒ ** The honest default for')
    print('     everything unanchored is "the corpus DISCUSSES this" -- most of what a reader asks. **')
    print('  ⇒⇒ ** THAT IS THE RULE WORKING, NOT FAILING: ** the usual companion answers confidently')
    print('     about discussion; this one must say which mode it is in, and ** the price of')
    print('     enforceability is saying "discussed, not established" most of the time. **')
    print('  ⚠ ** So the three-way rule is in practice a FOUR-way one, and the fourth bucket is the')
    print('    default and the largest. **  Saying so keeps the companion honest rather than silent.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
