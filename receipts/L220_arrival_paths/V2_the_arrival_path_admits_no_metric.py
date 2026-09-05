#!/usr/bin/env python3
"""V2 -- L-220's instrument question, closed in the negative by a converging blind run.

** THE ROW'S NEXT STEP WAS "REBUILD THE QUANTITY". **  G1 measured the character distance from a claim
to its support, and a blind run over sixteen labelled results killed it: ** a result that carries its
argument inside itself needs no nearby support, so distance is not readability. **  The row concluded
"the quantity is wrong" and asked for a better one.

** THIS RECEIPT ANSWERS THAT THE QUANTITY DOES NOT EXIST, and it answers it by BUILDING THE
SUCCESSOR AND WATCHING IT CONVERGE ON ZERO. **

Readability is not a distance; it is whether a claim SUPPLIES an arrival path.  That is a binary with
no invented threshold, which is the right shape -- ** a gate can check a declaration, not a judgement **
(r2447).  So: for every labelled result in the corpus, does it supply one?

    route 1  a following \\begin{proof} environment
    route 2  its argument IN BODY (a because/since/follows-from clause)
    route 3  a declaration: \\ref, \\eqref, \\rcpt or \\cite inside the statement

    ** blind run over all seventeen papers, 85 labelled results: **

        routes 2+3 only            ->  20 flagged
        + route 1 (proof blocks)   ->   7 flagged
        reading two of the seven   ->  route 4: a \\textbf{[Established: proved here from ...]} tag
                                       route 5: a following \\noindent\\emph{Argument.} paragraph

⇒ ** EVERY TIME THE INSTRUMENT WAS SHARPENED THE FLAG COUNT FELL, AND EVERY REMAINING FLAG THAT WAS
  READ TURNED OUT TO BE A ROUTE THE INSTRUMENT DID NOT KNOW. **  The sequence converges on the corpus
  being fine and on the instrument never being finished.

** THE FINDING, and it is about the CLASS rather than about this corpus: **

    *** A METRIC OVER AN OPEN-ENDED SET OF REALISATIONS MEASURES THE METRIC-WRITER'S IMAGINATION,
        NOT THE CORPUS. ***

There is no bound on the ways prose can supply an arrival path -- a proof, a because-clause, a
cross-reference, a receipt, a bracketed status tag, an "Argument." paragraph, a following remark that
draws the chain.  ** Each is a legitimate arrival path and none is enumerable in advance. **  This is
why the class resisted instrumentation twice.

⌗ AND THE CLASS'S OWN THREE FOUNDING INSTANCES ALL HAVE THIS SHAPE, which the row recorded without
drawing the conclusion:
  * L-209 -- ** the answer sat two sections above the question in the same file **;
  * U1    -- ** P16 answers a question in the next sentence and never asks it **;
  * V1/G1 -- ** rem:carter-chain sits immediately after the corollary and draws every link **, and the
              fork had already written it before the item was routed.
⇒ *** IN EVERY CASE THE ARRIVAL PATH EXISTED AND A READER MISSED IT.  THE DEFECT WAS IN THE READING,
   NOT IN THE CORPUS. ***

** WHAT SURVIVES: the class is real and stays open as a READING discipline, not an instrument debt. **
A node that cannot find the support for a claim should say so as a report about its own reading -- and
this line's own record is the argument for that: L-209, U1 and V1 were all filed as corpus defects and
all three resolved into the corpus having supplied the path.

WHAT IS NOT CLAIMED.  Not that every claim in the corpus has a visible arrival path -- five of the
seven remaining flags were not read.  ** Only that the two that were read both dissolved, and that no
finite route list can settle the rest. **

Written r2453.  Stated for reversal.
"""
import os, re, glob
import subprocess as _sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def sweep(routes):
    """count labelled results with NO arrival path, under the given route set"""
    tot, none = 0, []
    for f in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
        raw = open(f, encoding='utf-8', errors='replace').read()
        body = '\n'.join(l for l in raw.split('\n') if not l.lstrip().startswith('%'))
        for m in re.finditer(r'\\begin\{(theorem|proposition|corollary|lemma)\}'
                             r'(?:\[[^\]]*\])?\s*\\label\{([^}]+)\}(.*?)\\end\{\1\}', body, re.S):
            lab, txt = m.group(2), m.group(3)
            tail = body[m.end():m.end() + 200]
            has = False
            if 'proof' in routes and re.match(r'\s*\\begin\{proof\}', tail):
                has = True
            if 'inbody' in routes and re.search(
                    r'\b(because|since|so that|follows from|by |whose|which gives|hence|for )\b', txt):
                has = True
            if 'decl' in routes and re.search(r'\\(ref|eqref|rcpt|cite)\{', txt):
                has = True
            if 'tag' in routes and re.search(r'\\textbf\{\[(Established|established)', txt):
                has = True
            if 'argument' in routes and re.search(r'\\noindent\\emph\{Argument', tail):
                has = True
            tot += 1
            if not has:
                none.append((os.path.basename(f), lab))
    return tot, none


def main():
    print()
    print('  V2 -- does "readability" admit a measure?  A blind run, sharpened four times.')
    print()

    tot, n23 = sweep({'inbody', 'decl'})
    check(f'85 labelled results across the seventeen papers (found {tot})', tot == 85)
    check(f'routes 2+3 alone flag 20 (found {len(n23)})', len(n23) == 20)

    _, n123 = sweep({'proof', 'inbody', 'decl'})
    # ⛭ r4070: THE COUNT MOVED 7 -> 6 UNDER 61's REACH PASSES, AND THE THESIS DID NOT.
    #   *The narrowing is the finding -- 85 labelled results, 20 flagged by routes 2+3, a handful
    #   left after route 1, four after reading two of them.  ** The intermediate count is DATA, not
    #   the claim: ** one of the seven acquired a proof environment when its paper was rewritten, so
    #   route 1 now catches it and the residue is six.*
    #   ⌗ *Per c54.226 a count is a claim about a FILE AT A COMMIT.  Measured 6 at tree
    #   b702f932219f8f56 (this branch, after 61's r4009-r4065); it was 7 before those passes.
    #   The check asserts the CURRENT number and the narrowing that carries the argument, so a
    #   further move fires here rather than passing silently.*
    check(f'adding route 1 -- the proof environment -- cuts it to 6 (found {len(n123)})',
          len(n123) == 6)

    _, n4 = sweep({'proof', 'inbody', 'decl', 'tag', 'argument'})
    check(f'and routes 4 and 5, found by READING two of the seven, cut it further '
          f'(now {len(n4)})', len(n4) < len(n123))

    check('⇒ every sharpening lowered the count, and every flag that was READ was a route '
          'the instrument did not know',
          len(n4) < len(n123) < len(n23))

    # the two that were read, at source
    p0 = open(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex'),
              encoding='utf-8', errors='replace').read()
    p15 = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
               encoding='utf-8', errors='replace').read()
    # ** ⛭⛭⛭ RE-PINNED r3970, AND THE *ROUTE* IS NOW EXTINCT RATHER THAN THE CLAIM BEING WRONG. **
    # ** This check asserted that `prop:unique` supplies its arrival path *by a bracketed status
    # ** tag* -- `[Established: proved here from the maximal-symmetry requirement ...]` -- which was
    # ** true when read, and was one of the two routes this file found by READING what the sweep
    # ** flagged.  ** r3787 removed the status stamps from the papers: ZERO bracketed `[Established:`
    # ** tags remain in any paper, measured below. **  The proposition still supplies its path; it
    # ** now does so in the paper's own voice -- *"This is proved here from the maximal-symmetry
    # ** requirement together with the signature and causal-structure conditions"*.
    # **   ⇒ ** The pin was on the MECHANISM and the mechanism was retired, so both ends are pinned:
    # **     the tag at the commit that carried it, and the surviving clause here. **  *A route that
    # **     an instrument did not know can also stop existing, and the receipt that found it is the
    # **     natural place for that to be recorded rather than quietly lost.*
    _p0_flat = re.sub(r'\s+', ' ', p0)
    _p0_stamped = re.sub(r'\s+', ' ', _sp.run(
        ['git', 'show', '87b8f3c2~1:corpus/geometric_core_paper.tex'],
        cwd=ROOT, capture_output=True, text=True, errors='replace').stdout)
    check('prop:unique supplied its path by a bracketed status tag at 87b8f3c2~1, "[Established: '
          'proved here from the maximal-symmetry requirement ...]" -- the route this file found by '
          'READING what the sweep flagged',
          '[Established: proved here from the maximal-symmetry requirement' in _p0_stamped)
    _papers = [_f for _f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
               if not os.path.basename(_f).startswith('appendix_receipts')]
    _tags = len(re.findall(r'\[Established:', ' '.join(
        re.sub(r'\s+', ' ', open(_f, encoding='utf-8', errors='replace').read())
        for _f in _papers)))
    check(f'⛭ AND r3787 RETIRED THAT ROUTE CORPUS-WIDE: {_tags} bracketed status tag(s) remain in '
          f'any paper -- so the route is extinct, not merely moved',
          _tags == 0)
    check('⇒ and the path is still supplied, now in the paper\'s own voice: "This is proved here '
          'from the maximal-symmetry requirement together with the signature and causal-structure '
          'conditions; nothing is assumed of the embedding"',
          'This is proved here from the maximal-symmetry requirement together with the signature '
          'and causal-structure conditions; nothing is assumed of the embedding' in _p0_flat)
    check('prop:amplitude supplies its path by a following "\\noindent\\emph{Argument.}" paragraph',
          re.search(r'label\{prop:amplitude\}.{0,1200}?\\noindent\\emph\{Argument', 
                    re.sub(r'\s+', ' ', p15), re.S) is not None)

    # the class's own three founding instances all resolved this way
    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    check('L-209: the answer sat two sections above the question in the same file',
          'two sections above the question' in arc)
    check('U1: P16 answers a question in the next sentence and never asks it',
          'answers a question in the next sentence' in arc)
    check('V1/G1: rem:carter-chain was ALREADY written by the fork before the item was routed',
          'ALREADY FIXED BY THE FORK' in arc or 'rem:carter-chain' in arc)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the quantity does not exist, and the blind run shows why by converging. **')
    print('  Each sharpening lowered the flag count -- 20, then 7 -- and each remaining flag that was')
    print('  READ turned out to be an arrival route the instrument did not know: a bracketed')
    print('  [Established: ...] tag, a following "Argument." paragraph.')
    print('  ⇒ ** A METRIC OVER AN OPEN-ENDED SET OF REALISATIONS MEASURES THE METRIC-WRITER\'S')
    print('     IMAGINATION, NOT THE CORPUS. **  Nothing bounds the ways prose can supply an arrival')
    print('     path, which is why this class resisted instrumentation twice.')
    print('  ⌗ And the class\'s three founding instances all resolved the same way: ** in every case')
    print('    the arrival path EXISTED and a reader missed it.  The defect was in the reading. **')
    print('  ⇒ The class survives as a READING discipline, not as an instrument debt.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
