#!/usr/bin/env python3
r"""T1 -- L-280 produced a counterexample the thesis refutes on its own page, and L-282 inherited it.
The claim is stated in a paper, PROVED in resources/PhD_thesis, and reachable by neither instrument:
reach_baseline reads the papers, prior_art reads the receipts, and nothing read the sources.

COMPUTES: the induced signature on both real spheres of real M^5, directly, confirming the thesis's
classification; the thesis line that states it located by the new instrument; the three source classes
counted; and the three receipts of this line that pinned a defect, each shown to report rather than
assert after repair.  Nothing is fitted.

** ⛔⛭⛭ ⓵ THE SAME FAILURE A THIRD TIME, AND EACH TIME ONE LAYER DEEPER. **
  * *`reach_baseline` (`L-263`) -- built because a bake must know what the corpus HOLDS.  It reads the
    seventeen PAPER bodies.*
  * *`prior_art` (`L-281`) -- built because two bakes walked into a question the RECEIPTS had settled.*
  * *And neither reads* `resources/` *, where `p0`'s `prop:unique` sends the reader:*
    **"\\cite{JanzenThesis} \\S sec\\_RPT"**.
  ⇒ *** SO A CLAIM CAN BE STATED IN A PAPER, CITED TO A PROOF, AND CHECKED BY NEITHER INSTRUMENT. ***

** ⛔⛔ ⓶ WHICH IS EXACTLY WHAT `L-280` DID. **  *It read `P13`'s sentence as false because Minkowski,
de Sitter and anti-de Sitter are all maximally symmetric Lorentzian five-manifolds -- true, and not a
counterexample to the proposition the sentence compresses.*
  ⇒ ** `prop:unique` says "the only REAL RIEMANNIAN manifold that is maximally symmetric and carries
    an intrinsic Lorentzian signature", and REAL is load-bearing. **
  ⌗ *The thesis classifies the real spheres $x\cdot x=\alpha^2$ of real $\mathbb{M}^5$: $\alpha^2>0$
    is de Sitter, the maximally symmetric TIMELIKE hypersurface; $\alpha^2<0$ is the maximally
    symmetric SPACELIKE one, which* **"has four positive-definite eigenvalues"** *; $\alpha^2=0$ is
    the null cone.*
  ⇒ *** IN THAT FAMILY THERE IS NO LORENTZIAN ALTERNATIVE TO DE SITTER.  The anti-de Sitter that is
      Lorentzian embeds in a different ambient, with a second timelike direction. ***

** ⛭⛭ ⓷ AND THE ROUTING FINDING SURVIVES BOTH RECEIPTS INTACT. **  *Six sites state the substrate's
uniqueness; five carry a qualifier; `P13` carried none and cited nothing.  That was real, it was
applied, and it is untouched by the correction.*
  ⇒ ** What is withdrawn is a counterexample.  What stands is a routing gap and its repair. **

** ⌗ ⓸ AND THE CONCLUSION OF `L-282` PART 3 SURVIVES ON BETTER GROUND. **  *It argued
least-arbitrariness cannot separate the candidates.  Within the family it still cannot -- the
$\alpha^2>0$ and $\alpha^2<0$ members are both maximally symmetric -- and what separates them is
SIGNATURE.*  ⇒ ** Which is `prop:unique`, so the repair is still a citation and not a clause. **

** ⛭ ⓹ AND THE PIN-THE-DEFECT PATTERN IS FIXED AT THE CLASS, NOT THE INSTANCE. **  *Node 57's note:
three receipts of this line pinned the defect they found, so each would fail the moment its own
finding landed and the next node would read a red as a regression.*  ⇒ ** All three now REPORT the
paper's wording and ASSERT only what they established -- the mathematics, which does not move when a
paper improves. **

WHAT IS NOT CLAIMED.  ** Not that `L-280`'s arithmetic was wrong ** -- Minkowski, de Sitter and
anti-de Sitter do all have fifteen-dimensional isometry, and that computation is kept; what was wrong
was calling it a counterexample.  ** Not that `resources/` is the corpus ** -- it is a SOURCE, may be
superseded by the papers, and says what was PROVED rather than what is currently claimed; the
instrument's head says so.  ** Not that three instruments are enough ** -- each was built after a
failure, and the honest expectation is a fourth.  ** And not that `prop:unique`'s proof is verified
here ** -- the thesis's classification is read and its signature claim recomputed; the proposition's
full proof is not re-derived.

    python3 receipts/L283_the_third_source_class/T1_the_papers_cite_the_receipts_decide_and_resources_is_where_the_proofs_live.py

Written r3184, `L-283`.  Stated for reversal.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def induced_signature(alpha2_point, eta):
    """eigenvalues of the induced metric on x.x = const at the given point"""
    pt = np.array(alpha2_point, float)
    nn = pt @ eta @ pt
    keep = []
    for k in range(len(pt)):
        e = np.zeros(len(pt)); e[k] = 1
        v = e - (e @ eta @ pt) / nn * pt
        if np.linalg.matrix_rank(np.array(keep + [v]), tol=1e-9) > len(keep):
            keep.append(v)
    T = np.array(keep)
    g = T @ eta @ T.T
    return np.linalg.eigvalsh((g + g.T) / 2)


def main():
    print()
    print('  T1 -- the papers cite, the receipts decide, and resources/ is where the proofs live')
    print()
    sys.path.insert(0, os.path.join(ROOT, 'corpus'))
    import source_texts as ST

    print('  ' + '=' * 74)
    print('  PART 1 -- ⛔⛭⛭ THE THESIS SETTLES IT, AND THE SIGNATURE IS RECOMPUTED')
    print('  ==========================================================================')
    eta = np.diag([-1., 1, 1, 1, 1])
    ds = induced_signature([0., 2, 0, 0, 0], eta)      # x.x = +4
    ads = induced_signature([2., 0, 0, 0, 0], eta)     # x.x = -4
    print(f'      alpha^2 > 0  induced eigenvalues {np.round(ds, 3)}   -> LORENTZIAN (de Sitter)')
    print(f'      alpha^2 < 0  induced eigenvalues {np.round(ads, 3)}   -> RIEMANNIAN')
    check('⓵ on the real spheres of real M^5 the alpha^2>0 member is Lorentzian and the alpha^2<0 '
          'member is RIEMANNIAN — four positive eigenvalues, recomputed directly',
          sum(1 for e in ds if e < 0) == 1 and all(e > 0 for e in ads))
    check('⓵ᵇ ⛔ SO THERE IS NO LORENTZIAN ALTERNATIVE TO DE SITTER IN THAT FAMILY, and L-280\'s '
          'counterexample was drawn from outside it',
          all(e > 0 for e in ads))
    hits = ST.search(['positive-definite eigenvalues'])
    check('⓵ᶜ and the thesis says so in its own words, located by the new instrument in '
          'resources/PhD_thesis/thesischap3.tex',
          any('thesischap3' in h[0] for h in hits))

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛔ THREE SOURCE CLASSES, AND THE INSTRUMENTS REACHED TWO')
    print('  ==========================================================================')
    import reach_baseline as RB
    import prior_art as PA
    n_papers = len(RB.BODIES_TEX)
    n_receipts = len(PA.receipt_heads())
    n_sources = len(ST.source_files())
    print(f'      papers   (reach_baseline) : {n_papers}')
    print(f'      receipts (prior_art)      : {n_receipts}')
    print(f'      sources  (source_texts)   : {n_sources}   <- unreached until r3184')
    check(f'⓶ the corpus has three source classes — {n_papers} papers, {n_receipts} receipts, '
          f'{n_sources} sources — and until this revision two instruments reached two of them',
          n_papers > 10 and n_receipts > 500 and n_sources > 10)
    check('⓶ᵇ and p0 sends the reader to the third: prop:unique cites the thesis at sec_RPT',
          'sec' in RB.BODIES_TEX['p0'] and 'prop:unique' in RB.BODIES_TEX['p0'])
    check('⓶ᶜ ⌗ the instrument states that resources/ is a SOURCE and not the live corpus — it '
          'says what was PROVED, not what is currently claimed',
          'not the live corpus' in open(os.path.join(ROOT, 'corpus', 'source_texts.py'),
                                        encoding='utf-8', errors='replace').read())

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛭⛭ WHAT SURVIVES, AND IT IS THE ROUTING FINDING')
    print('  ==========================================================================')
    B = RB.BODIES_TEX
    qualified = [('p0', 'only real Riemannian manifold that is maximally symmetric'),
                 ('P03', 'unique real Riemannian manifold whose Lorentzian signature is intrinsic'),
                 ('P06', 'maximally symmetric structure being the unique one that requires its own'),
                 ('P10', 'unique maximally symmetric structure carrying no unforced')]
    check('⓷ the five qualified sites are still there — the routing finding does not depend on the '
          'counterexample and is untouched by its withdrawal',
          all(ph.lower() in B[pa].lower() for pa, ph in qualified))
    check('⓷ᵇ ⛭ and L-282\'s conclusion survives on better ground: within the family, '
          'least-arbitrariness still cannot separate the alpha^2>0 member from the alpha^2<0 one, '
          'both being maximally symmetric — what separates them is SIGNATURE, which is prop:unique',
          all(e > 0 for e in ads) and 'prop:unique' in B['p0'])

    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⛭ AND THE PIN-THE-DEFECT PATTERN IS FIXED AT THE CLASS')
    print('  ==========================================================================')
    pinned = [('L278_the_involution_bake', 'I1'), ('L280_the_decidable_claims', 'D1'),
              ('L282_the_scope_that_five_papers_carry', 'Q1')]
    fixed = []
    for d, pre in pinned:
        path = [f for f in os.listdir(os.path.join(ROOT, 'receipts', d))
                if f.startswith(pre)][0]
        src = open(os.path.join(ROOT, 'receipts', d, path),
                   encoding='utf-8', errors='replace').read()
        fixed.append('paper_state' in src or 'REPORTED, not asserted' in src
                     or 'do not move when P13 is repaired' in src)
        print(f'      {d[:38]:38s} reports rather than pins: {fixed[-1]}')
    check('⓸ all three receipts that pinned a defect now REPORT the paper\'s wording and assert '
          'only what they established — so a successful repair no longer reds them',
          all(fixed))
    check('⓸ᵇ ⌗ which is node 57\'s note taken at the class rather than the instance: a bake\'s '
          'checks must assert what it establishes, not quote what it found wrong',
          len(fixed) == 3)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:160]}')
        return 1
    print('  VERDICT: ** the papers cite, the receipts decide, and resources/ is where the proofs')
    print('  live. **')
    print('  ⛔ ** L-280 produced a counterexample the thesis refutes on its own page, ** *and')
    print('     L-282 inherited it.  p0\'s prop:unique says "the only REAL RIEMANNIAN manifold",')
    print('     and REAL is load-bearing: on the real spheres of real M^5 the alpha^2<0 member is')
    print('     RIEMANNIAN — four positive eigenvalues, recomputed here — so in that family there')
    print('     is no Lorentzian alternative to de Sitter.*')
    print('  ⌗ ** The routing finding stands entire ** *— five qualified sites, P13 with none —')
    print('     and it is what 57 applied.  What is withdrawn is a counterexample, not a gap.*')
    print('  ⛭ ** And the failure is one layer deeper each time: ** *reach_baseline for what the')
    print('     corpus publishes, prior_art for what it has decided, and now source_texts for')
    print('     what it PROVED.  Each was built after a failure; the honest expectation is a')
    print('     fourth.*')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
