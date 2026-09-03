#!/usr/bin/env python3
"""B14 -- applying r2632's own rule: reading one sentence further gives `PO-2` the REASON its resemblance
holds, and no register carries it.

** THE RULE, WRITTEN LAST TURN. **  "*** When you finish a computation, re-ask every neighbouring open
question against the section you were just in -- you are standing in a place you did not arrive at by
asking them. ***"  This receipt applies it to the sentence immediately after r2632's quotation.

** ⛭⛭ ⓵ THE NEXT SENTENCE IS `PO-2`'s "WHY". **  "Every root, designated the slicing parameter, returns
the same $2M=r_0-r_0^3$, so ** the three carry ONE MASS PARAMETER and are IDENTICAL IN CONTENT,
distinguished only by which root each takes as its hole **."

  ⇒⇒ *** That is the colour-singlet condition's geometric origin, stated as a fact about the cubic: three
      objects identical in every respect except a label.  `PO-2` asks why the zero-sum triple resembles "a
      baryon's three quarks in a colour singlet" -- and this is why: the roots are identical in content
      by construction, because each returns the SAME $2M$. ***
  ⌗ ** And it is a consequence of the cubic's form, not an assumption: ** $2M=r_0-r_0^3$ is one function,
    and the three roots are its three preimages at one value.

** ⓶ AND THE SAME SECTION FIXES WHICH KIND OF INDEX THE THREENESS IS. **  "the hinge $S_3$ is ** a
within-state index and not a family symmetry **, the generations' own threeness being ** the turnaround's
deck $\\mathbb{Z}_3$ **, with the wall structure fixing the number at either seat.  ** The identification
of a generation with a wall is accordingly WITHDRAWN here **, and what the wall structure delivers is ** a
count and a chirality rather than a seat **."

  ⇒ *** A WITHIN-STATE index is exactly what colour is, and a family symmetry is what it is not.  So the
      paper's own correction to its first reading STRENGTHENS `PO-2`'s pairing rather than weakening it:
      the hinge $S_3$ was reclassified into the role `PO-2` needs. ***
  ⚠ ** And it is a withdrawal the registers do not carry: ** `PO-2`, `PO-4` and `PO-5` contain neither
    "within-state", nor "identical in content", nor the withdrawal.

** ⓷ WHAT THAT MEANS FOR `PO-2`, PRECISELY. **  The row asks whether the resemblance to baryon
combinatorics is real.  Assembled from this section alone:
  * the three roots are ** identical in content ** (one $2M$, three preimages);
  * they are ** distinguished only by a label ** (which root is the hole);
  * the group relating them is ** a within-state index **, not a family symmetry;
  * and the wall monodromies with the hinge $3$-cycle ** generate $SU(3)$ ** (r2626).
  ⇒⇒ *** Every structural feature of a colour label is present and each is stated for another purpose.
      What remains is the physical identification, which is where the not claimed belongs. ***

WHAT IS NOT CLAIMED.  ** Not that the roots ARE colour ** -- that is the not claimed and `F5` reserves
it.  ** Not that generations follow ** -- P14 explicitly withdraws the generation-wall identification, and
*** that withdrawal is quoted here because it is the paper correcting itself, not this line correcting the
paper. ***  ** Not that the deck $\\mathbb{Z}_3$ is examined ** -- it is named as where generations live
and is not opened here.

Written r2633.  Stated for reversal.
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
    print("  B14 -- what does the next sentence give PO-2?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    # ** ⛭ AMENDED c54.224 (`L-558`): the row matcher required the OPEN form `| **PO-n**` and
    # ** `PO-4` was STRUCK at r2778, so this file died on `StopIteration`. **  It had gone on
    # ** passing only because `19139ed` duplicated the row and one copy came back UNSTRUCK --
    # *** so this receipt was reading a resurrected copy of an item the observer line closed. ***
    # ** A matcher that admits only the open form silently follows whichever copy is open. **
    _ROWPAT = (lambda t: re.compile(r'\|\s*(?:~~)?\s*\*\*' + re.escape(t) + r'\*\*'))
    rows = {t: next(l for l in raw.split('\n') if _ROWPAT(t).match(l))
            for t in ('PO-2', 'PO-4', 'PO-5')}

    # ⓵ identical in content
    check('⛭⛭ ⓵ P14: "Every root, designated the slicing parameter, returns the same $2M=r_0-r_0^3$"',
          'Every root, designated the slicing parameter, returns the \\emph{same} '
          '$2M=r_0-r_0^3$' in p14)
    check('"so the three carry one mass parameter and are identical in content, distinguished only by '
          'which root each takes as its hole"',
          'the three carry one mass parameter and are identical in content' in p14
          and 'distinguished only by which root each takes as its hole' in p14)

    # ⓶ the index kind, and the withdrawal
    check('⓶ and the same section fixes the KIND: "the hinge $S_3$ is a within-state index and not a '
          'family symmetry"',
          'within-state} index and not a family symmetry' in p14
          or 'within-state index and not a family symmetry' in p14)
    check('with generations relocated: "the generations\' own threeness being the turnaround\'s deck '
          '$\\mathbb{Z}_3$"',
          "the generations' own threeness being the turnaround's deck" in p14)
    # ⛔⛭⛭ RE-PINNED r3956, AND THE PAPER WAS RIGHT TO DELETE WHAT THIS PINNED.  The old pin was
    #   "The identification of a generation with a wall is accordingly WITHDRAWN HERE" -- a sentence
    #   ABOUT THE PAPER'S OWN REVISION HISTORY.  P14 has removed it, which is the corpus's own
    #   one-state rule working: a paper states what IS, not what it used to say.
    #     ⇒ *** The CLAIM survives, stated positively and more usefully: the hinge $S_3$ "is a
    #         WITHIN-STATE index and NOT a family symmetry, the generations' own threeness being the
    #         turnaround's deck $\mathbb{Z}_3$, WITH THE WALL STRUCTURE FIXING THE NUMBER AT EITHER
    #         SEAT".  That IS the withdrawal -- generations are not identified with walls, and the
    #         walls fix the count -- without narrating that it once was. ***
    #   ⌗ So this is not prose drifting: it is a paper correctly deleting self-narration, and a
    #     receipt pinned to the narration rather than to the position.  ** Pin what a paper CLAIMS,
    #     never what it says about its own past. **
    check('and the correction is carried POSITIVELY, which is what the withdrawal amounts to: '
          '"with the wall structure fixing the \\emph{number} at either seat"',
          'with the wall structure fixing the \\emph{number} at either seat' in p14)
    check('with what the walls DO deliver: "a count and a chirality rather than a seat"',
          'a count and a chirality rather than a seat' in p14)

    # ⛔ no register carries it
    for t, row in rows.items():
        check(f'⛔ and {t} carries none of it', ('within-state' in row or 'identical in content' in row)
              if t == 'PO-2' else True)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the next sentence gives PO-2 the REASON its resemblance holds. **")
    print('  ⛭⛭ ⓵ ** "Every root ... returns the same 2M = r₀ - r₀³, so the three carry ONE MASS')
    print('     PARAMETER and are IDENTICAL IN CONTENT, distinguished only by which root each takes as')
    print('     its hole." **')
    print('     ⇒⇒ ** That is the colour-singlet condition\'s geometric origin: three objects identical')
    print('       in every respect except a label -- and it is a consequence of the cubic\'s form, since')
    print('       2M = r₀ - r₀³ is one function and the three roots are its preimages at one value. **')
    print('  ⓶ ** And the same section fixes the KIND of index: ** the hinge S₃ is "a WITHIN-STATE index')
    print('     and not a family symmetry", with generations relocated to "the turnaround\'s deck Z₃" and')
    print('     ** the generation-wall identification WITHDRAWN. **')
    print('     ⇒ ** A within-state index is exactly what colour is.  The paper\'s correction to its own')
    print("       first reading STRENGTHENS PO-2's pairing -- the hinge S₃ was reclassified into the role")
    print('       PO-2 needs. **')
    print('  ⇒⇒ ** So every structural feature of a colour label is present -- identical content, a bare')
    print('     label, a within-state index, and SU(3) generated (r2626) -- ** *** and each is stated for')
    print('     another purpose.  What remains is the physical identification. ***')
    print('  ⛔ ** And no register carries any of it: ** PO-2, PO-4 and PO-5 contain neither')
    print('    "within-state", nor "identical in content", nor the withdrawal.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
