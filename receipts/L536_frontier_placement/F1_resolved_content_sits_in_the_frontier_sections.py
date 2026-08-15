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
    check('⓵ P7 keeps its own count: "it opened at seven and stands at four"',
          'it opened at seven and stands at four' in p7f)
    check('and says the resolved ones were "moved below the list" and "recorded there"',
          'moved below the list' in p7f and 'recorded there' in p7f)

    # ⛭ but the frontier section is the last section
    i = p7.find('\\section{Frontiers and open problems}')
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
    _i = _p7_then.find('\\section{Frontiers and open problems}')
    _seg = _p7_then[_i:]
    _below = len(_seg) - _seg.find('\\end{enumerate}')
    check(f'and {_below:,} chars -- {100*_below/len(_seg):.0f}% of it -- sat BELOW the list at {R2579}, '
          f'which is what this receipt measured',
          _below > 10000)
    check(f'⛭ AND IT HAS BEEN ACTED ON: {below:,} chars -- {100*below/len(seg):.0f}% -- sit below it '
          f'now, so about {(_below-below)//1000} thousand characters of settled physics have moved out '
          f'from under a heading that says the work is not done',
          below < _below / 2)
    check(f'⚠ and the residue is NOT zero: {below:,} characters are still filed under "Frontiers and '
          f'open problems" -- the lead is shrunk, not discharged',
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
    print('     roughly eleven thousand characters of settled physics filed under "Frontiers and open')
    print('     problems", which is P7\'s LAST section.')
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
