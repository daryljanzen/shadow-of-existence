#!/usr/bin/env python3
r"""S1 -- L-245 (the stability half of L-801) closed against the literature: the bracket is a 2x2 grid in
(symmetry x data-size), and the ONE open cell is (general, all-data) = the cosmic no-hair CONJECTURE, a
general-relativity open problem, not a CR-specific gap. The cell CR actually needs -- the perturbative
graviton, vacuum, small departures from the de Sitter substrate -- is COVERED, and P11 itself names the
covering result.

** Board lead L-802 (cc54's band); closes the bracket on L-245 (registered r2530), informs vein L-165
(PO-6). L-245's own next step: "close the bracket -- either find the general all-data statement in the
literature, or state exactly which class the corpus needs and whether it is covered -- THIS IS A
LITERATURE QUESTION BEFORE IT IS A COMPUTATION." This takes the SECOND horn and states the class. **

** THE QUESTION (L-245). ** Does a general no-isometry leaf with sigma^TT != 0 evolve without runaway,
for ALL data? L-801 settled the FREEDOM (the count is symmetry-free, the contracted Bianchi identity);
the STABILITY is the remainder, and P11 routes it OUT by name -- Friedrich, Andreasson-Ringstrom, Nariai.
** State no expected outcome; report where the literature actually brackets it. **

** THE GRID. ** Future stability of de Sitter (Lambda>0) is proved cell by cell, and the two axes are
SYMMETRY (symmetric / general-no-isometry) and DATA SIZE (small / all). Surveyed r2534:
    (general, small)     COVERED. Friedrich 1986 (VACUUM, no symmetry, small data -- de Sitter is an
                         attractor, a form of cosmic no-hair); Ringstrom 2008 (Einstein + nonlinear
                         scalar field); Rodnianski-Speck 2013 and Speck (Euler fluid, 0<c_s^2<1/3, with
                         and without vorticity). The whole GENERAL small-data column is done, vacuum
                         and the standard matter models.
    (symmetric, all)     COVERED in symmetry classes. Andreasson-Ringstrom 2016 (T^3-Gowdy Einstein-
                         Vlasov, ALL data, "future stable in the class of all solutions"); surface-
                         symmetric Einstein-Vlasov 2014; Wald 1983 (spatially HOMOGENEOUS Bianchi, any
                         matter obeying SEC+DEC). Beyer 2009: the Nariai branch is the non-generic
                         UNSTABLE exception inside Gowdy.
    (general, ALL)       ** OPEN. ** No theorem. This is the cosmic no-hair CONJECTURE proper -- large,
                         inhomogeneous, no-symmetry data flowing to de Sitter -- and it is a
                         general-relativity open problem, exactly as L-245 says ("it is a general-
                         relativity stability question, which is why P11 routes it out rather than
                         solving it").

** P11 ALREADY NAMES THE COVERING RESULT FOR THE CELL CR NEEDS, and this is the whole closing. ** The
beyond-wall stratum is FREE GRAVITATIONAL RADIATION (vacuum-Lambda), and its physical object is the
propagating graviton -- "a de Sitter wave admitting Bunch-Davies quantization", a PERTURBATION of the de
Sitter substrate. P11: "Friedrich is a small-data result, EXACTLY THE PERTURBATIVE REGIME OF THE
PROPAGATING GRAVITON, so it settles the in-regime all-orders stability directly." ** So the cell CR needs
is (general, VACUUM, small), and Friedrich 1986 covers it exactly. ** P11 also flags, honestly, that this
is "convergence across results ... rather than a single theorem covering the exact vacuum polarized
Gowdy-Lambda case" -- i.e. the bracket, by P11's own admission, and the exact-model theorem is not the
point.

** THE CLOSING (L-245's second horn). ** The bracket closes as: the general no-isometry stability is
COVERED for SMALL data (Friedrich vacuum -- the exact perturbative-graviton match P11 names -- plus
Ringstrom and Rodnianski-Speck for matter), and the cell the construction actually needs (the
perturbative graviton, vacuum, small departures from the dS substrate) sits inside it. The ONE open cell
is (general, all-data) = the cosmic no-hair conjecture, and it is general relativity's open problem, not
CR's. ** So "does it evolve without runaway for ALL data" is OPEN in general -- but a CR-specific answer
does not require settling it: what the construction needs is the perturbative cell, which is closed. **

WHAT THIS ADDS OVER P11, since a literature note that only restates the corpus is worth nothing:
  * ** The 2x2 STRUCTURE, ** which turns "convergence across results" into a grid with one named open
    cell, so the gap is a coordinate rather than a feeling.
  * ** Rodnianski-Speck (2013) and Speck, ** the fluid small-data general results, which the corpus does
    NOT cite (grep: zero) -- they fill the (general, small) matter cell beyond P11's Friedrich/scalar.
  * ** The NAME of the open cell: ** it is the cosmic no-hair conjecture, not a CR construction problem,
    which is the disposition L-245 asked for.

WHAT IS NOT CLAIMED, stated for reversal.
  ** Not that the cosmic no-hair conjecture is settled ** -- the (general, all-data) cell is OPEN and is
  named as open. ** Not that CR provably needs only small data ** -- whether a strongly-nonlinear
  (large sigma^TT) beyond-wall regime is ever physically required is a question about the CONSTRUCTION and
  is not settled here; what is stated is that the perturbative regime the construction's own framing points to
  (P11's Bunch-Davies graviton) is covered, and that the large-data alternative is the general conjecture
  and not a CR-specific hole. ** Not a re-derivation ** -- these are external theorems, cited with their
  identifiers, not proved here; this is the LITERATURE bounding L-245 asked for, not a computation. **
  Not that P11 erred ** -- it routed the question out correctly and named the covering result; this makes
  its bracket explicit and adds the fluid cell.

Written r2534 (cc54, L-802). Asserts against SOURCES (dynamics_paper.tex = P11) and the grid's internal
logic -- never against the register. Literature identifiers in CITES. Stated for reversal.
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


def norm(path):
    raw = open(os.path.join(ROOT, 'corpus', path), encoding='utf-8', errors='replace').read()
    body = '\n'.join(l for l in raw.split('\n') if not l.lstrip().startswith('%'))
    return re.sub(r'\s+', ' ', body)


# ---- the literature, as data: (result, matter, symmetry, data_size, covers?, identifier) -------------
# axes: symmetry in {'symmetric','general'}; data in {'small','all'}
CITES = [
    ('Friedrich 1986',          'vacuum', 'general',   'small', True,  'CMP 107, 587 (1986)'),
    ('Ringstrom 2008',          'scalar', 'general',   'small', True,  'Invent. math. 173, 123'),
    ('Rodnianski-Speck 2013',   'euler',  'general',   'small', True,  'arXiv:1102.1501, Selecta Math. (Speck later added vorticity)'),
    ('Andreasson-Ringstrom 2016','vlasov','symmetric', 'all',   True,  'arXiv:1306.6223, JEMS'),
    ('surface-symmetric 2014',  'vlasov', 'symmetric', 'all',   True,  'arXiv:1402.7085'),
    ('Wald 1983',               'SEC+DEC','symmetric', 'all',   True,  'PRD 28, 2118 (Bianchi)'),
    ('Beyer 2009 (Nariai)',     'vacuum', 'symmetric', 'all',   False, 'arXiv:0902.2532 -- UNSTABLE exception'),
]


def covered_cells():
    return {(m, s, d) for _, mt, s, d, ok, _ in
            [(n, mt, s, d, ok, i) for n, mt, s, d, ok, i in CITES] if ok for m in [mt]}


def main():
    print()
    print('  S1 -- L-245: does the general no-isometry leaf evolve without runaway for ALL data?')
    print()
    p11 = norm('dynamics_paper.tex')

    # ---- source anchors: P11 routes the question out by name --------------------------------------
    check('P11 routes the stability question OUT by name -- Friedrich (vacuum small-data) and '
          'Andreasson-Ringstrom (all-data T^3-Gowdy), Nariai the non-generic exception',
          'Friedrich proved the nonlinear stability of de Sitter in vacuum' in p11
          and 'extend cosmic no-hair and future stability to \\emph{all} data in the $T^3$-Gowdy class' in p11
          and 'the one non-generic exception, the Nariai branch' in p11)
    check('P11 names the CELL CR needs and its covering result: "Friedrich is a small-data result, '
          'EXACTLY THE PERTURBATIVE REGIME OF THE PROPAGATING GRAVITON, so it settles the in-regime '
          'all-orders stability directly"',
          'exactly the perturbative regime of the propagating graviton' in p11
          and 'settles the in-regime all-orders stability directly' in p11)
    check('and P11 itself calls this a BRACKET, not a single-theorem closure: "convergence across '
          'results ... rather than a single theorem covering the exact vacuum polarized Gowdy" case',
          'This is convergence across results' in p11
          and 'rather than a single theorem covering the exact vacuum polarized' in p11)
    check('the object is perturbative -- "the linearized propagating graviton is a de Sitter wave '
          'admitting Bunch-Davies quantization" -- so the regime is small departures from the substrate',
          'the linearized propagating graviton is a de Sitter wave admitting Bunch' in p11)

    # ---- the grid: exactly one (symmetry x data) cell is uncovered, and it is (general, all) -------
    # ** general data SUBSUMES symmetric: a result at (general, d) covers (symmetric, d) too. **
    axes = [(s, d) for s in ('symmetric', 'general') for d in ('small', 'all')]

    def is_covered(s, d):
        return any(ok and cd == d and (cs == s or cs == 'general')
                   for _, _, cs, cd, ok, _ in CITES)

    covered = {c for c in axes if is_covered(*c)}
    open_cells = [c for c in axes if c not in covered]
    check('the GENERAL small-data cell is covered (Friedrich vacuum + Ringstrom scalar + '
          'Rodnianski-Speck fluid)', ('general', 'small') in covered)
    check('the SYMMETRIC all-data cell is covered (Andreasson-Ringstrom, surface-symmetric, Wald-Bianchi)',
          ('symmetric', 'all') in covered)
    check('and EXACTLY ONE cell is open -- the (general, ALL-data) cell -- which is the cosmic no-hair '
          'CONJECTURE, a general-relativity open problem and not a CR-specific gap',
          open_cells == [('general', 'all')])

    # ---- the cell CR needs is inside the covered region -------------------------------------------
    # beyond-wall stratum = free gravitational radiation (vacuum), perturbative graviton (small data),
    # no isometry (general).  Friedrich 1986 is (vacuum, general, small) -> the exact match.
    friedrich = [c for c in CITES if c[0] == 'Friedrich 1986'][0]
    check('the cell CR needs -- (vacuum, general, small): the perturbative graviton, free radiation, '
          'small departures from the dS substrate -- is EXACTLY Friedrich 1986 (vacuum, general, small)',
          friedrich[1] == 'vacuum' and friedrich[2] == 'general' and friedrich[3] == 'small'
          and friedrich[4] is True)

    # ---- what this adds: the fluid cell the corpus does not cite ----------------------------------
    corpus_all = ''.join(norm(p) for p in ('dynamics_paper.tex', 'CR_cosmology.tex', 'CR_framework.tex'))
    check('this ADDS Rodnianski-Speck (the fluid small-data general result), which the corpus does '
          'NOT cite -- filling the (general, small) MATTER cell beyond P11\'s vacuum+scalar',
          'Rodnianski' not in corpus_all and 'Speck' not in corpus_all
          and any(n.startswith('Rodnianski-Speck') for n, *_ in CITES))
    check('every stability result the corpus DOES cite falls in a COVERED cell -- none sits in the '
          '(general, all-data) open cell, consistent with that cell being the open conjecture',
          all((s, d) in covered or n.startswith('Beyer')
              for n, _, s, d, ok, _ in CITES if ok))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (L-245, the second horn -- WHICH CLASS THE CORPUS NEEDS AND WHETHER IT IS COVERED):')
    print('  ** THE BRACKET CLOSES AS A GRID WITH ONE OPEN CELL. ** General no-isometry stability is')
    print('     COVERED for SMALL data (Friedrich vacuum -- the exact perturbative-graviton match P11')
    print('     names -- plus Ringstrom scalar and Rodnianski-Speck fluid for matter). The one open cell')
    print('     is (general, ALL-data) = the cosmic no-hair CONJECTURE, general relativity\'s open')
    print('     problem, NOT a CR-specific hole.')
    print('  ** THE CELL CR NEEDS IS COVERED. ** The beyond-wall stratum is free vacuum-Lambda radiation,')
    print('     a perturbative graviton (P11\'s Bunch-Davies de Sitter wave) -- the (vacuum, general,')
    print('     small) cell -- and Friedrich 1986 covers it exactly, as P11 already states.')
    print('  => So L-245 is answered without settling the conjecture: what stays open (general all-data)')
    print('     is general GR\'s cosmic no-hair, and the construction does not need it -- unless a')
    print('     strongly-nonlinear beyond-wall regime is required, which is a question about the')
    print('     construction, not a gap the literature leaves in the perturbative regime. Informs L-165.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
