#!/usr/bin/env python3
"""field_survey.py -- WHICH FIELDS DOES THE CORPUS USE THAT NO BAKE HAS EVER BEEN THROWN AT?

** ⛔⛭⛭ WHY THIS EXISTS.  THE LIST OF OUTSTANDING BAKES WAS SURVEYED ONCE, AT r1890, AND THE
CORPUS IS TWELVE HUNDRED REVISIONS PAST IT. **

  *`THE_MATHEMATICS_REACH` carries two questions and says which one paid:* **"The survey asked two
  things: which listed fields are unbaked, and which used fields are unlisted.  The second found
  more."**  *The second question is the one that found CATEGORY THEORY -- 363 uses and two papers
  named for its objects, absent from the reach list entirely because a groupoid filed under group
  theory gets baked with group theory's tools.*
  ⇒ ** And that question was asked ONCE. **  *Everything the corpus has grown since r1890 -- P11
    through P17, the whole c54 fork, the fermion sector -- has never been asked it.*
  ⇒ *** A SURVEY IS AN INSTRUMENT OR IT IS A MEMORY, and a memory twelve hundred revisions old is
      not evidence about this tree. ***

** ⌗ WHAT IT DOES. **  Each field is a VOCABULARY.  For every field, every term is counted across the
seventeen paper bodies -- comments and bibliography stripped, de-macroed, via `reach_baseline` -- and
the field's ledger is looked for on disk.  *A field with substantial usage and no ledger is a
candidate; a field with a ledger is a control.*

  ⛭ ** THE CONTROLS ARE THE POINT. **  *The already-baked fields are surveyed alongside the rest, and
    the instrument FAILS if it cannot re-find them.*  ⇒ *** A survey that reports a clean sheet
    because it cannot see anything is the failure mode this guards, and it is the same failure
    `check_theatre_currency` prints its population to avoid. ***
  ⚠ ** WHAT IT CANNOT DO. **  *A vocabulary is a proxy for a field.  A field the corpus uses under
    names not in its list is invisible here -- which is exactly the defect that hid category theory
    for ninety revisions, so the vocabularies are stated in full and are meant to be argued with.*
  ⚠ ** AND A COUNT IS NOT AN OPENING. **  *`reach_baseline`'s standing warning applies: the count
    says look, it does not say what is there.*

    python3 corpus/field_survey.py
    python3 corpus/field_survey.py --terms 'category theory'

Written r3162.  Stated for reversal.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE)
import reach_baseline as RB                                                # noqa: E402

#: ** THE VOCABULARIES, STATED IN FULL. **  Each entry: (field, ledger-file-or-None, terms).
#: *`ledger` is the file this field's bake wrote, or None if no bake has been thrown.  It is
#: CHECKED against the disk, not trusted -- a named ledger that does not exist is a failure.*
FIELDS = [
    # ---- controls: fields already thrown.  The instrument must re-find every one. ----
    ('projective geometry of quadrics', 'QUADRIC_GEOMETRY_LEDGER.md',
     ['quadric', 'projective', 'Cayley', 'Klein', 'polarity', 'absolute', 'cross-ratio']),
    ('conformal / Mobius geometry', 'CONFORMAL_GEOMETRY_LEDGER.md',
     ['conformal', 'inversive', 'stereographic', 'anharmonic', 'Weyl tensor']),
    ('complex analysis / monodromy', 'COMPLEX_ANALYSIS_LEDGER.md',
     ['monodromy', 'branch point', 'analytic continuation', 'Riemann surface', 'residue',
      'holomorphic', 'meromorphic']),
    ('category theory', 'CATEGORY_THEORY_LEDGER.md',
     ['groupoid', 'algebroid', 'morphism', 'category', 'functor', 'natural transformation']),
    ('variational / action', 'VARIATIONAL_LEDGER.md',
     ['Einstein--Hilbert', 'Einstein-Hilbert', 'action', 'Lagrangian', 'variational',
      'Euler--Lagrange', 'Hamiltonian']),
    ('combinatorics', 'COMBINATORICS_LEDGER.md',
     ['root system', 'weight', 'Weyl group', 'Dynkin', 'partition', 'multiplicity']),
    ('optics / lensing', 'OPTICS_LENSING_LEDGER.md',
     ['lensing', 'photon sphere', 'null geodesic', 'deflection', 'caustic', 'eikonal']),
    ('statistics / inference', 'STATISTICS_INFERENCE_LEDGER.md',
     ['likelihood', 'chi^2', 'base rate', 'reference class', 'covariance', 'residual']),
    # ---- candidates: no ledger on disk.  These are what the survey is FOR. ----
    ('number theory', None,
     ['integer', 'rational', 'irrational', 'transcendental', 'prime', 'Diophantine',
      'continued fraction', 'algebraic number', 'modular form', 'zeta']),
    ('representation theory', None,
     ['representation', 'irreducible', 'highest weight', 'Casimir', 'character',
      'branching', 'multiplet', 'triality']),
    ('differential topology / index theory', None,
     ['index theorem', 'Atiyah', 'Chern', 'characteristic class', 'cobordism', 'K-theory',
      'Euler characteristic', 'homotopy', 'homology', 'fundamental group']),
    ('spectral theory / harmonic analysis', None,
     ['spectrum', 'eigenvalue', 'self-adjoint', 'deficiency', 'Sturm', 'Fourier',
      'spherical harmonic', 'Laplacian', 'essentially self-adjoint', 'resolvent']),
    ('integrable systems', None,
     ['integrable', 'Lax pair', 'conserved quantity', 'first integral', 'separability',
      'Hamilton--Jacobi', 'Killing tensor', 'Carter constant', 'action-angle']),
    ('algebraic geometry', None,
     ['variety', 'scheme', 'divisor', 'genus', 'elliptic curve', 'singular point',
      'blow-up', 'discriminant', 'resultant', 'ideal']),
    ('catastrophe / singularity theory', None,
     ['catastrophe', 'fold', 'cusp', 'unfolding', 'codimension', 'versal', 'Morse',
      'degenerate critical point']),
    ('Cartan / differential geometry of connections', None,
     ['connection', 'curvature form', 'torsion', 'frame bundle', 'Cartan', 'moving frame',
      'principal bundle', 'holonomy', 'parallel transport', 'soldering']),
    ('numerical analysis', None,
     ['convergence', 'truncation error', 'discretisation', 'discretization', 'stiff',
      'step size', 'quadrature', 'interpolation', 'conditioning', 'round-off']),
    ('information theory', None,
     ['entropy', 'mutual information', 'channel capacity', 'Shannon', 'coarse-grain',
      'bit', 'compression']),
    ('probability / stochastic processes', None,
     ['stochastic', 'random walk', 'Brownian', 'Markov', 'ergodic', 'fluctuation',
      'noise', 'correlation function']),
    ('convexity / optimisation', None,
     ['convex', 'extremal', 'minimise', 'minimize', 'stationary point', 'constraint',
      'Lagrange multiplier', 'saddle']),
    ('functional analysis / operator theory', None,
     ['Hilbert space', 'Banach', 'bounded operator', 'unbounded', 'domain', 'closure',
      'dense', 'norm', 'inner product', 'unitary']),
]

#: ⛔⛭ ** AND A WORD-BOUNDED COUNT IS STILL NOT AN OPENING: FOUR OF THE TOP SEVEN WERE HOMONYMS. **
#:   *Read at r3162, term by term, the dominant word of four candidates is not the field's word:*
#:     * *`constraint` x138 of `convexity / optimisation`'s x140 is the HAMILTONIAN constraint --
#:       "the constraint deparametrizes to a true Hamiltonian", "it is the Hamiltonian constraint, a
#:       local functional of the cut's own bend".*  ⇒ ** Optimisation is not a field this corpus
#:       uses, and the entry is REFUSED rather than thrown. **
#:     * *`genus` x21 of `algebraic geometry`'s is the corpus's own species/genus TAXONOMY of metric
#:       singularities -- "two species of one genus" -- not the genus of a curve.*
#:     * *`closure` x100 of `functional analysis`'s x212 is a theorem closing and the Galois closure,
#:       not the closure of an operator.*
#:     * *`character` x67 of `representation theory`'s x231 is "causal character" and "analytic
#:       character"; only P14's "no character count on a finite group" is the group-theoretic word.*
#:   ⌗ ** AND TWO CANDIDATES ARE ALREADY DISCHARGED BY EARLIER BAKES, which the count cannot see: **
#:     *catastrophe theory by the ODE/dynamical-systems bake (r1911, `D4`) -- P07 states outright
#:     "The word fold is used here in its bifurcation-theoretic sense" -- and the operator half of
#:     spectral theory by `R-M` station Ⓗ (`L-264`, the Weyl limit-point test).*
#:   ⇒ *** SO THE INSTRUMENT ORDERS THE READING AND DOES NOT DO IT.  Three passes were needed before
#:       the list was trustworthy: substring to word, word to sense, and sense against the bakes
#:       already thrown -- and each pass reordered the top of the list. ***

#: a field with at least this many de-macroed uses is worth a look; stated, not tuned
NOTABLE = 40


#: ⛔⛭ ** THE FIRST FORM OF THIS SURVEY COUNTED SUBSTRINGS, AND ITS TOP CANDIDATE WAS AN ARTEFACT. **
#:   *`reach_baseline.counts` is deliberately a substring count -- right for its job, which is
#:   "does this phrase occur at all".  Used for a FIELD vocabulary it reports `bit` x253 by matching
#:   inside `orbit` and `arbitrary`, and `norm` x118 inside `normal` and `normalised`.*
#:   ⇒ *** So "information theory x285" led the candidate list on a word the corpus never uses in
#:       that sense, and the field with the largest number would have been thrown first. ***
#:   ⌷ *The r1890 survey this one re-runs said so in its own table header --* **"word-bounded and
#:     keys stripped"** *-- and the instrument rebuilt from it dropped the condition.*
#:   ⇒ ** A SURVEY THAT LOOSENS THE MATCH ITS PREDECESSOR TIGHTENED REPORTS A DIFFERENT CORPUS. **
#:     *Counted word-bounded below, on the de-macroed bodies, with the loose count kept beside it so
#:     the size of the correction is visible rather than quietly absorbed.*
#: ⌗ ** r3164: the word-bounded count now lives in `reach_baseline` and is IMPORTED. **
#:   *This file carried its own copy for two revisions.  A second implementation of the
#:   same rule is a second thing to keep in step, and the class of defect it guards
#:   against -- a gate restating the rule it guards -- is `L-272`'s own finding.*
word_counts = RB.word_counts


def field_total(terms):
    """{term: (word-bounded n, loose n)} de-macroed, and the field's word-bounded total"""
    per = {}
    for t in terms:
        loose = max(sum(RB.counts(t).values()), sum(RB.counts(t, tex=True).values()))
        tight = max(sum(word_counts(t, tex=False).values()),
                    sum(word_counts(t, tex=True).values()))
        per[t] = (tight, loose)
    return per, sum(v[0] for v in per.values())


def main():
    print()
    print('  field_survey -- which fields does the corpus USE that no bake has been thrown at?')
    print()
    ledgers = {os.path.basename(p) for p in glob.glob(os.path.join(ROOT, '*_LEDGER.md'))}
    print(f'    ledgers on disk: {len(ledgers)}')
    print()

    rows, missing_ledger = [], []
    for name, ledger, terms in FIELDS:
        per, tot = field_total(terms)
        have = ledger in ledgers if ledger else False
        if ledger and not have:
            missing_ledger.append((name, ledger))
        rows.append((name, ledger, have, tot, per))

    # ** THE CONTROL: every field declaring a ledger must be re-found by its own vocabulary. **
    controls = [r for r in rows if r[1]]
    dead = [r[0] for r in controls if r[3] < NOTABLE]
    print('  ' + '=' * 74)
    print('  CONTROLS -- fields already thrown.  The instrument must re-find every one.')
    print('  ==========================================================================')
    for name, ledger, have, tot, per in sorted(controls, key=lambda r: -r[3]):
        mark = 'ok ' if tot >= NOTABLE and have else '⛔ '
        print(f'    {mark} {name:44s} ×{tot:<6d} ledger {"present" if have else "MISSING"}')
    print()
    if missing_ledger:
        print(f'    ⛔ [FAIL] a field names a ledger that is not on disk: {missing_ledger}')
        print()
        return 1
    if dead:
        print(f'    ⛔ [FAIL] the survey cannot re-find {len(dead)} already-baked field(s): {dead}')
        print('       *A survey that reports a clean sheet because it cannot see anything is not')
        print('        measuring the corpus.  Fix the vocabulary before trusting any candidate.*')
        print()
        return 1
    print(f'    every one of the {len(controls)} thrown fields is re-found at ×{NOTABLE}+ '
          'by its own vocabulary — the instrument is reading the corpus.')

    print()
    print('  ' + '=' * 74)
    print('  CANDIDATES -- no ledger on disk, ordered by measured usage')
    print('  ==========================================================================')
    cands = sorted((r for r in rows if not r[1]), key=lambda r: -r[3])
    for name, _, _, tot, per in cands:
        flag = '★★' if tot >= 200 else ('★ ' if tot >= NOTABLE else '  ')
        top = ' · '.join(f'{t} ×{n}' + (f' (loose {ln})' if ln > n * 2 else '')
                         for t, (n, ln) in
                         sorted(per.items(), key=lambda kv: -kv[1][0])[:4] if n)
        print(f'    {flag} {name:44s} ×{tot:<6d} {top[:96]}')
    print()
    live = [r for r in cands if r[3] >= NOTABLE]
    print(f'    {len(live)} candidate field(s) at ×{NOTABLE} or more, and none of them has ever '
          'been thrown.')
    print()
    print('    ⌗ A COUNT IS NOT AN OPENING.  Read the context before calling anything a hole:')
    print("       python3 corpus/reach_baseline.py --context 'the term'")
    print()
    return 0


if __name__ == '__main__':
    if '--terms' in sys.argv:
        want = sys.argv[sys.argv.index('--terms') + 1]
        for name, ledger, terms in FIELDS:
            if want.lower() in name.lower():
                RB.survey(terms)
        sys.exit(0)
    sys.exit(main())
