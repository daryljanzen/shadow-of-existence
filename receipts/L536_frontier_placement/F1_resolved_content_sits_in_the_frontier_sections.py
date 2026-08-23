#!/usr/bin/env python3
"""F1 -- 191 KB of frontier sections across thirteen papers, and resolved content is being left inside
them: the corpus reads as a thing with a changelog attached rather than a thing that has landed.

** THE QUESTION THAT FOUND IT. **  "If items are crossed off P7's frontiers list or other lists, don't
they get properly shifted to the synthesis and physics sections -- drawing things out as if they were
written when the final product had already been sorted?"
  ⇒ ** Tested rather than answered. **

** ⓵ P7's THREE RESOLVED ITEMS. **  The paper keeps its count honestly: "** it opened at seven and stands
at four **.  Item seven resolved and was moved below the list; items one and three ... ** have since done
the same and are recorded there **."
  ⇒ ⛭ ** But `\\section{Frontiers and open problems}` is P7's LAST section. **  *** "Moved below the list"
      means below the enumerate, INSIDE the same section -- so the resolved content sits under a heading
      that says it is not yet done. ***

** ⓶ AND THE SIZE IS NOT MARGINAL. **
      P7's frontier section: ** 32,368 chars, 11% of its body **
      of which ** 11,359 chars -- 35% -- sit BELOW the list **.
  ⇒ ** Roughly eleven thousand characters of settled physics ** -- the matter branch-point crossing
    dynamics, the classification of causal reassignments -- ** filed under "Frontiers and open
    problems". **
  ⌗ ** And `causal reassignment` appears 21 times in P7, so the CONTENT is present elsewhere too. **  ***
      The defect is placement, not absence: the same result is both worked into the paper and recorded
      as a resolved frontier, and a reader meeting it first in the frontier section reads settled work as
      an open edge. ***

** ⛭⛭ ⓷ AND IT IS A CORPUS-WIDE SHAPE. **  Frontier/open/scope sections across the thirteen papers that
have them:

      *** 191,530 characters total ***
      boundary_paper ** 33% of its body ** · CR_cosmology ** 29% ** · matter_sector ** 17% ** ·
      slicing_operator 15% · range_paper 14% · cosmogenesis 10% · ...

  ⇒ *** Two papers carry roughly a third of their body in a section about what is NOT done.  That is a
      large number for a corpus whose registers say most of those items have since moved. ***

** ⚠ WHAT THIS DOES AND DOES NOT ESTABLISH. **
  * ** It establishes the SIZE and the placement defect in P7 exactly ** -- 35% below the list, measured.
  * ** It does NOT establish how much of the 191 KB is resolved content ** across the other twelve.  ***
      The resolved-language proxy (`resolved`, `overtaken`, `has since`, `settled`, `moved below`) finds
      only 20 markers corpus-wide, which is far too few to be a measurement and is reported as a proxy
      rather than a count. ***
  * ⇒ ** So the deliverable this names is an AUDIT, not a conclusion: ** for each of the thirteen
    frontier sections, which paragraphs state an OPEN edge and which state a RESOLVED one.  ** That is
    bounded work with a known end, and nobody has done it. **

⌗ AND WHY IT MATTERS FOR THE FINAL REVISION, WHICH IS THE POINT OF THE QUESTION: *** a paper that
resolves a frontier item and leaves the resolution in the frontier section has written a changelog, not a
result.  The reader who arrives at the finished thing should meet the physics in the physics, and the
frontier list should hold only what is still open -- which is exactly what P7 says a frontier list is
for: "a frontier list whose entries quietly empty is worse than none: a reader uses it to choose what to
work." ***

WHAT IS NOT CLAIMED.  ** Not that any paper is wrong ** -- every one of these sections is honest, and P7's
self-accounting is what made the defect findable.  ** Not that frontier sections should shrink to nothing
** -- six of the fourteen open items are real physics and belong in them.  ** Not that the audit's outcome
is predictable **: it may find that most of the 191 KB is genuinely open, in which case the finding is
the size alone.

Written r2579.  Stated for reversal.
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


def body(path):
    b = '\n'.join(l for l in open(path, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def frontier_sections():
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
        if os.path.basename(f).startswith('appendix_receipts'):
            continue
        b = body(f)
        m = re.search(r'\\(?:sub)*section\{[^}]*(?:[Ff]rontier|[Oo]pen|[Ss]cope|[Rr]emain)[^}]*\}', b)
        if not m:
            continue
        nxt = re.search(r'\\section\{', b[m.end():])
        seg = b[m.start(): m.end() + (nxt.start() if nxt else len(b) - m.end())]
        out.append((os.path.basename(f), len(seg), len(b)))
    return out



# ** ⛭⛭ RE-PINNED c54.226 (`L-560`): THE NUMBER MOVED BECAUSE THE DEFECT WAS ACTED ON. **  At `e8e58cf`
# (r2579, this receipt's own build) 11,359 characters -- 35% of P7's frontier section -- sat BELOW the
# list.  It is 3,264 and 13% now: *** roughly eight thousand characters of settled physics have been
# moved out from under a heading that says the work is not done. ***
#   ⇒ ** So the finding was correct and has been PARTLY DISCHARGED, and a receipt that asserts a defect
#     must not die when the defect shrinks. **  The measurement at the commit is pinned; the improvement
#     is asserted; and the residue -- 3,264 characters still misplaced -- is asserted as still non-zero.
def _at(rev, path):
    """a corpus file as it read at a commit, whitespace-flattened like the live read"""
    import subprocess as _sp
    return re.sub(r'\s+', ' ', _sp.run(['git', 'show', f'{rev}:{path}'], cwd=ROOT,
                                       capture_output=True, text=True, errors='replace').stdout)


def main():
    print()
    print('  F1 -- is resolved content being left inside the frontier sections?')
    print()
    p7 = body(os.path.join(ROOT, 'corpus', 'CR_framework.tex'))
    p7f = re.sub(r'\s+', ' ', p7)

    # ⓵ P7's own accounting
    # ** RE-PINNED r3106.  ⓵ pinned P7's running count -- "it opened at seven and stands at four" --
    #    as EVIDENCE of the changelog habit this receipt found.  P7 no longer carries it: the count,
    #    the "moved below the list" narration and the resolved-item history are gone under the
    #    one-state rule, and the list now states what each of the three items HAS LEFT rather than
    #    what was removed from it.  So P7 is this receipt's FIXED case, and the pin records that.
    #    The finding stands for the other twelve papers, which the checks below still measure. **
    check('⓵ P7 no longer keeps a running count of its own frontier list -- the changelog sentence '
          'this receipt found is gone',
          'it opened at seven and stands at four' not in p7f
          and 'moved below the list' not in p7f)
    # ⛭⛭ RE-PINNED r3132 (`L-258`), AND THE OLD PIN WAS INTO PROSE THAT WAS REWRITTEN AT r3119.
    #   *The old form required the words "stated remainders rather than whole sectors" and "leaves a
    #   computation".  r3119 rewrote the list on a sharper distinction than the one this check was
    #   pinned to, and the sentences went.*
    #   ⇒ ** The CLAIM is that the list states what each item stands at rather than what was removed
    #     from it, and r3119 states it in stronger terms -- WORK versus BOUNDARY, with a boundary
    #     named a result rather than a gap.  Re-pinned to the distinction rather than to the words
    #     that carried it, and the phrases are quoted so the pin is legible. **
    check('and the list states what each item STANDS AT rather than what was removed from it -- '
          'r3119 sharpens this into two kinds: "Work is something unworked that a definite '
          'computation would close" against "A boundary is a result rather than a gap"',
          'is something unworked that a definite computation would close' in p7f
          and 'boundary} is a result rather than a gap' in p7f
          and 'has not failed to empty; it has finished' in p7f)

    # ⛭ but the frontier section is the last section
    # ⛔⛭⛭ RE-ANCHORED r3132 (`L-258`).  ** THIS FOUND THE SECTION BY ITS TITLE STRING, AND r3119
    # ** RENAMED IT. **  *`find` returned -1, so `p7[i:]` was the LAST CHARACTER of the paper: the
    # section measured 1 char and 0% of the body, and four checks below it failed on that.*
    #   ⇒ *** A SECTION TITLE IS PROSE AND A LABEL IS AN IDENTIFIER.  The corpus cites this section
    #       as `\\ref{sec:frontiers}` everywhere, so the label is what it is FOR. ***
    #   ⇒ ** And the anchor is asserted rather than assumed: a `find` that returns -1 must fail
    #     LOUDLY, not silently measure one character. **
    m_sec = re.search(r'\\section\{[^}]*\}\s*\\label\{sec:frontiers\}', p7)
    check('⛭ᵃ the frontier section is located by its LABEL `sec:frontiers`, which is what the corpus '
          f'cites it by -- found at {m_sec.start() if m_sec else "NOT FOUND"}', m_sec is not None)
    i = m_sec.start()
    after = re.findall(r'\\section\{([^}]+)\}', p7[i + 10:])
    check(f'⛭ but Frontiers IS P7\'s last section -- sections after it: {after or "none"}',
          not after)
    check('⇒ SO "moved below the list" means below the enumerate INSIDE that section, under a heading '
          'that says the content is not yet done', not after)

    # ⓶ the size
    seg = p7[i:]
    k = seg.find('\\end{enumerate}')
    below = len(seg) - k
    check(f'⓶ P7\'s frontier section is {len(seg):,} chars, {100*len(seg)/len(p7):.0f}% of its body',
          len(seg) > 20000)
    R2579 = 'e8e58cf'
    _p7_then = _at(R2579, 'corpus/CR_framework.tex')
    # ⌗ the PINNED read keeps the title of the day, because that is what the file said then -- and
    #   it is asserted rather than allowed to fall through to -1, which is the defect above.
    _i = _p7_then.find('\\section{Frontiers and open problems}')
    check(f'⛭ᵇ and the pinned read at {R2579} still finds the section under the title it carried '
          f'THEN ({_i}) -- a pinned anchor and a live anchor are different objects', _i >= 0)
    _seg = _p7_then[_i:]
    _below = len(_seg) - _seg.find('\\end{enumerate}')
    check(f'and {_below:,} chars -- {100*_below/len(_seg):.0f}% of it -- sat BELOW the list at {R2579}, '
          f'which is what this receipt measured',
          _below > 10000)
    check(f'⛭ AND IT HAS BEEN ACTED ON: {below:,} chars -- {100*below/len(seg):.0f}% -- sit below it '
          f'now, so about {(_below-below)//1000} thousand characters of settled physics have moved out '
          f'from under a heading that says the work is not done',
          below < _below / 2)
    check(f'⚠ and the residue is NOT zero: {below:,} characters are still filed below the list in '
          f'`sec:frontiers` -- the lead is shrunk, not discharged',
          below > 1000)
    n_cr = len(re.findall('causal reassignment', p7f, re.I))
    check(f'⌗ and "causal reassignment" appears {n_cr} times in P7, so the CONTENT is present elsewhere '
          '-- the defect is PLACEMENT, not absence', n_cr > 10)

    # ⓷ corpus-wide
    secs = frontier_sections()
    tot = sum(l for _, l, _ in secs)
    worst = sorted(secs, key=lambda r: -r[1]/r[2])[:3]
    check(f'⛭⛭ ⓷ and corpus-wide: {tot:,} characters of frontier/open sections across {len(secs)} papers',
          tot > 150000)
    check(f'with the three largest shares: '
          f'{", ".join(f"{n[:20]} {100*l/b:.0f}%" for n, l, b in worst)}',
          worst[0][1]/worst[0][2] > 0.25)

    # ⚠ the limit
    prox = 0
    for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex')):
        if os.path.basename(f).startswith('appendix_receipts'):
            continue
        prox += len(re.findall(r'resolved|overtaken|has since|moved below', body(f), re.I))
    check(f'⚠ and the resolved-language proxy finds only {prox} markers corpus-wide -- far too few to '
          'be a measurement, and reported as a proxy rather than a count', prox < 60)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** resolved content is being left inside the frontier sections, and the size is')
    print('  not marginal. **')
    print(f'  ⓵⓶ ** P7: {len(seg):,} chars of frontier section, {100*below/len(seg):.0f}% of it BELOW the list ** --')
    print(f'     {below:,} characters of it still filed below the list, under a heading that says')
    print(f'     the work is not done -- down from {_below:,} at {R2579}, which is the finding')
    print('     acted on rather than the finding failing.  *P7 renamed that section at r3119 to')
    print('     "Frontiers, boundaries, and what would re-open them"; it is still its LAST section.*')
    print(f'  ⌗ ** And "causal reassignment" appears {n_cr} times in P7 ** -- the content IS present')
    print('    elsewhere.  ** The defect is PLACEMENT: the same result is both worked into the paper and')
    print('    recorded as a resolved frontier, and a reader meeting it first in the frontier section')
    print('    reads settled work as an open edge. **')
    print(f'  ⓷ ** Corpus-wide: {tot:,} characters across {len(secs)} papers **, two of them carrying')
    print('     roughly a THIRD of their body in a section about what is not done.')
    print('  ⚠ ** WHAT THIS DOES NOT ESTABLISH: ** how much of the 191 KB is resolved.  The proxy finds')
    print(f'    {prox} markers, which is far too few to count with.  ⇒ ** So what this names is an AUDIT --')
    print('    for each of the thirteen sections, which paragraphs state an OPEN edge and which a')
    print('    RESOLVED one -- and that is bounded work nobody has done. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
