#!/usr/bin/env python3
r"""A1 -- R-M station Ⓖ, thrown: the Atiyah sequence the theatre records as absent from P12 is not
absent.  It is P12's object, unnamed — and all four of its terms are already in the paper, under
four other words.

COMPUTES: the symmetric-space grading of so(5,1) on explicit 6×6 matrices, all three inclusions over
every basis pair; that [m,m] does not vanish; that the kernel of the anchor at the symmetric cut is
exactly h, by annihilating the cut direction; the rank arithmetic of the sequence; the symmetric-space
curvature −[[X,Y],Z] against the constant-curvature form on all 125 triples of m; and the Jacobi
identity over all 3375 basis triples.  No parameter is pinned and nothing is fitted.

** ⛭ ⓵ THE STATION, AS THE THEATRE STATES IT. **  *Ⓖ Lie algebroids — **BIT** — "P12 holds algebroid,
anchor and connection and **zero 'Atiyah sequence'**, which is exactly the structure relating those
three."*  ⌗ *With the caveat: "P12's algebroid is the constraint algebra's and not a bundle's."*

** ⛔⛭⛭ ⓶ THE CAVEAT IS RIGHT IN GENERAL AND WRONG HERE, AND THAT IS THE WHOLE FINDING. **  P12's
object is an **action** Lie algebroid `so(5,1) ⋉ C` over the space of cuts, and on the orbit the base
is the coset `dS₅ = SO(5,1)/SO(4,1)`.
  ⇒ *** The action algebroid of `G` on `G/H` IS the Atiyah algebroid of the principal `H`-bundle
      `G → G/H`.  So P12's algebroid is a bundle's after all — it is the one bundle the substrate
      already is. ***

** ⌗ ⓷ AND EVERY TERM OF THE SEQUENCE IS ALREADY IN THE PAPER, UNDER ANOTHER WORD. **

      *** 0 → ad(P) → A → T𝒞 → 0 ***

  * ** `ker(anchor)` = `h` = `so(4,1)` ** — *P12's own words for `h` are* **"the cut-fixing
    isotropy"**.  ⌗ *Checked here by annihilating the cut direction: exactly ten of the fifteen
    generators fix it, and they are exactly `h`.*  ⇒ ** So the kernel is named in the paper and never
    called a kernel: `kernel` occurs ZERO times in P12. **
  * ** `im(anchor)` ≅ `m` ** — *P12's* **"cut-deforming coset"**, *dimension five, the tangent space
    to the base.*
  * ** the splitting ** — *P12: "General relativity's constraint algebra has the structure-functions
    but has never been given the base they vary over, **nor a section of the bundle that would select
    a definite flow**.  This paper supplies both."*  ⇒ ** A section of the bundle that selects a flow
    IS a splitting of this sequence.  The paper supplies the splitting and does not say what it
    splits. **

** ⛭⛭ ⓸ AND P12'S CLOSURE TEST IS THE SPLITTING'S CURVATURE COMPUTATION. **  *The paper's defining
test is that the cut-deformation bracket closes: `[h,h]⊂h`, `[h,m]⊂m`, `[m,m]⊂h`, with `m` not a
subalgebra.*  ⇒ ** In the sequence's language a connection's curvature is `F(X,Y) = [σX,σY] − σ[X,Y]`,
valued in `ker ρ`.  For the canonical splitting `σ = m` the symmetric-space relation `[m,m] ⊂ h` IS
that statement: the curvature is valued in the isotropy, and it is nonzero. **
  ⇒ *** And it is the substrate's own curvature: `−[[X,Y],Z] = K(⟨Y,Z⟩X − ⟨X,Z⟩Y)` with `|K|=1`,
      verified on all 125 triples.  So "the bracket closes" and "the connection is curved, by exactly
      the Riemann tensor" are ONE computation, run once, read twice. ***

** ⌗ ⓹ AND THE SOURCE THAT CARRIES THE SEQUENCE IS ALREADY CITED. **  *P12 cites `Mackenzie2005` — the
standard reference for Lie algebroids and for the Atiyah sequence — and uses it for one sentence: that
the hypersurface-deformation algebra is a Lie algebroid rather than a Lie algebra.*
  ⇒ ** The structure the theatre records as missing is in the book the paper already cites. **

** ⓺ AND ONE ABSENCE IS A CONSEQUENCE RATHER THAN A GAP. **  *`Jacobi` occurs ZERO times in seventeen
papers, and the Jacobi identity is half of what makes a bracket a Lie bracket.*  ⇒ ** For an ACTION
algebroid it is inherited from the acting algebra, and `so(5,1)` satisfies it — checked over all 3375
basis triples. **  ⇒ *** So the axiom the corpus never states is automatic for the class of algebroid
it built, which is the Ⓘ pattern this theatre already banked: a field that reaches nothing can still
deliver a theorem. ***

WHAT IS NOT CLAIMED.  ** Not that P12 is wrong anywhere ** -- every ingredient used here is the
paper's, and the paper's own identification of the structure function with the coset metric is
untouched and is a different statement from this one (a metric, not a curvature).  ** Not that the
sequence splits as Lie algebroids ** -- that needs a FLAT connection, the canonical one is not flat by
⓸, and whether another is flat is a question about the bundle's topology that is not settled here and
is not needed for anything above.  ** Not that the full algebroid over the whole space of cuts is the
Atiyah algebroid ** -- the identification is on the ORBIT, where the base is the coset, which is the
symmetry-reducible sector P12 works on and states as its scope.  ** Not that `kernel`×0 in P12 is an
error ** -- the object is named, correctly, as the isotropy; what is absent is the sequence that makes
the four names one structure.

    python3 receipts/L265_station_G_the_sequence_is_the_object/A1_the_atiyah_sequence_is_not_missing_from_P12_it_is_P12s_object_unnamed.py

Written r3152, `L-265`.  Stated for reversal.
"""
import importlib.util
import itertools
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

spec = importlib.util.spec_from_file_location('_rb', os.path.join(ROOT, 'corpus',
                                                                  'reach_baseline.py'))
RB = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RB)
B = RB.BODIES

#: ** ⛭ THE BASELINE, READ AT THE COMMIT WHERE IT WAS MEASURED (r3970). **  `reach_baseline.counts`
#: ** reads the LIVE papers, which is right for a live claim and wrong for a baseline: a baseline is
#: ** a fact about the corpus BEFORE a throw, and this station's throw has since landed.  So the
#: ** same counting is done against a checkout of that commit, mirroring `reach_baseline.bodies()`
#: ** exactly -- `%` comments and the bibliography stripped, whitespace flattened -- because a
#: ** baseline compared under a DIFFERENT preprocessing is not a comparison.
#: **   ⇒ *Both ends of a measurement take a SHA, exactly as both ends of a quotation do: c54.226's
#: **     rule, applied to counts rather than to sentences.*
_AT_BUILD = '427babd3'          # r3152 -- this station's own throw
_AT_BUILD_CACHE = {}


def _at_build_counts(term):
    """`RB.counts(term)` as it read at this station's own throw commit."""
    import re as _re
    import subprocess as _sp
    if not _AT_BUILD_CACHE:
        for _tex, _key in RB.TEX2P.items():
            _raw = _sp.run(['git', 'show', f'{_AT_BUILD}:corpus/{_tex}'], cwd=ROOT,
                           capture_output=True, text=True, errors='replace').stdout
            _b = '\n'.join(l for l in _raw.split('\n') if not l.lstrip().startswith('%'))
            _j = _b.find('\\begin{thebibliography}')
            _AT_BUILD_CACHE[_key] = _re.sub(r'\s+', ' ', _b[:_j] if _j > 0 else _b)
        assert len(_AT_BUILD_CACHE) == len(RB.TEX2P), (
            'every paper must be readable at the throw commit, or the baseline is partial',
            sorted(set(RB.TEX2P.values()) - set(_AT_BUILD_CACHE)))
    return {k: len(_re.findall(_re.escape(term), v, _re.I))
            for k, v in _AT_BUILD_CACHE.items()}


ETA = np.diag([1., 1., 1., 1., 1., -1.])          # so(5,1) on R^{5,1}


def gen(a, b):
    X = np.zeros((6, 6))
    X[a, :] += ETA[b, :]
    X[b, :] -= ETA[a, :]
    return X


IDX = [(a, b) for a in range(6) for b in range(a + 1, 6)]
GENS = {ab: gen(*ab) for ab in IDX}
BASIS = np.stack([GENS[ab].flatten() for ab in IDX], axis=1)
#: the symmetric cut: h fixes it, m deforms it.  The cut direction is the 4-axis.
Hh = [ab for ab in IDX if 4 not in ab]
Mm = [ab for ab in IDX if 4 in ab]


def br(X, Y):
    return X @ Y - Y @ X


def expand(X):
    c, *_ = np.linalg.lstsq(BASIS, X.flatten(), rcond=None)
    assert np.allclose(BASIS @ c, X.flatten(), atol=1e-9), 'not in the span of the basis'
    return {ab: c[i] for i, ab in enumerate(IDX) if abs(c[i]) > 1e-9}


def lands_in(X, subset):
    return all(ab in subset for ab in expand(X))


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  A1 -- station Ⓖ thrown: where is the Atiyah sequence?')
    print()

    # ============================================================ (1) the baseline
    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ THE BASELINE, MEASURED BEFORE ANYTHING IS THROWN')
    print('  ' + '=' * 74)
    absent = {t: sum(RB.counts(t).values()) for t in
              ('Atiyah sequence', 'Atiyah algebroid', 'adjoint bundle', 'principal bundle',
               'exact sequence', 'Chevalley', 'Jacobi')}
    print(f'    absent corpus-wide: {absent}')
    # ** ⛭⛭⛭ RE-PINNED r3970, AND EVERY ZERO HERE ENDED BECAUSE THIS STATION ASKED FOR IT. **
    # ** Written r3152 (`427babd3`), this file's finding was that P12 HAS the Atiyah sequence as its
    # ** object and never names it.  *** r3251 wrote it in -- "the theatre results carried INTO the
    # ** papers, which is what a bake is for" -- and the vocabulary arrived with it: the sequence
    # ** twice, the Atiyah algebroid three times, the adjoint and principal bundles twice each, and
    # ** `kernel` in P12 where it read the isotropy alone. ***
    # **   ⇒ ** A BASELINE MEASURED BEFORE A THROW CANNOT BE ASSERTED AFTER THE THROW LANDS. **  It
    # **     is pinned at the commit where it was measured -- which is what makes it a baseline -- and
    # **     the DISCHARGE is asserted separately, so the receipt records the landing instead of
    # **     dying of it.  *Same shape as `L203/M3` and `L175/V1`, third and fourth in this debt.*
    _then = {t: sum(_at_build_counts(t).values()) for t in absent}
    check(f'⓵ the sequence and its vocabulary were absent from all seventeen papers at {_AT_BUILD}, '
          f'this file\'s own throw: {_then}',
          all(v == 0 for v in _then.values()))
    check(f'⛭⛭ AND THE THROW LANDED: they are present now -- {absent} -- carried into the papers at '
          f'r3251, "the theatre results carried INTO the papers, which is what a bake is for"',
          absent['Atiyah sequence'] >= 1 and absent['Atiyah algebroid'] >= 1
          and absent['adjoint bundle'] >= 1)
    present = {t: RB.counts(t)['P12'] for t in ('algebroid', 'anchor', 'bracket', 'connection',
                                                'isotropy', 'kernel')}
    print(f'    present in P12: {present}')
    _kernel_then = _at_build_counts('kernel')['P12']
    check(f'⓵ᵇ ⛔ while P12 held algebroid, anchor, bracket, connection and isotropy in quantity -- '
          f'and the word `kernel` {_kernel_then} times at {_AT_BUILD}, so the kernel of its own '
          f'anchor was named as the isotropy and never as a kernel',
          present['algebroid'] > 20 and present['anchor'] > 5 and present['isotropy'] > 10
          and _kernel_then == 0)
    check(f'⛭ AND P12 NAMES IT NOW: `kernel` {present["kernel"]} time(s) -- the object this file '
          f'computed in PART 3, ker(anchor) = the cut-fixing isotropy, is called by its name in the '
          f'paper rather than only in this receipt',
          present['kernel'] >= 1)
    check('⓵ᶜ and P12 already cites Mackenzie2005 -- the standard reference for Lie algebroids and '
          'for the Atiyah sequence -- for one sentence, that the hypersurface-deformation algebra '
          'is an algebroid rather than a Lie algebra',
          'Mackenzie2005' in B['P12']
          and 'not a Lie algebra but a Lie \\emph{algebroid}' in B['P12'])

    # ============================================================ (2) the object
    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛭⛭ THE OBJECT: AN ACTION ALGEBROID OVER A COSET')
    print('  ' + '=' * 74)
    check('⓶ P12 states the construction: an action Lie algebroid so(5,1) ⋉ 𝒞, the base the space '
          'of cuts, the acting algebra the substrate isometry, the anchor the cut-to-stress-energy '
          'map, and a SECTION that selects a definite flow',
          'action Lie algebroid' in B['P12']
          and 'nor a section of the bundle that would select a definite flow' in B['P12']
          and 'the acting algebra is the substrate\'s isometry $\\so(5,1)$' in B['P12'])
    check('⓶ᵇ and it names the two graded pieces in the paper\'s own words: h the CUT-FIXING '
          'ISOTROPY, m the CUT-DEFORMING coset',
          'the cut-fixing isotropy' in B['P12'] and 'cut-deforming coset' in B['P12'])
    check(f'⓶ᶜ dim so(5,1) = {len(IDX)}, dim h = {len(Hh)} = dim so(4,1), dim m = {len(Mm)} = '
          'dim dS₅ -- and the base of the orbit is the coset SO(5,1)/SO(4,1)',
          len(IDX) == 15 and len(Hh) == 10 and len(Mm) == 5)

    # ============================================================ (3) the sequence
    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⌗ THE SEQUENCE, TERM BY TERM')
    print('  ' + '=' * 74)
    v = np.zeros(6)
    v[4] = 1.0                                   # the cut direction
    ker = [ab for ab in IDX if np.linalg.norm(GENS[ab] @ v) < 1e-12]
    check(f'⓷ ker(anchor) computed by annihilating the cut direction: {len(ker)} generators, and '
          'they are EXACTLY h -- so the kernel is P12\'s "cut-fixing isotropy"',
          sorted(ker) == sorted(Hh))
    check(f'⓷ᵇ and the image has dimension {len(IDX) - len(ker)} = dim m = dim of the base, so the '
          'anchor is surjective on the orbit and the algebroid is TRANSITIVE there',
          len(IDX) - len(ker) == len(Mm))
    check(f'⓷ᶜ so the ranks close: rank ad(P) + rank T𝒞 = {len(Hh)} + {len(Mm)} = {len(IDX)} = '
          'rank A, which is the Atiyah sequence 0 → ad(P) → A → T𝒞 → 0',
          len(Hh) + len(Mm) == len(IDX))

    # ============================================================ (4) the curvature
    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⛭⛭ THE CLOSURE TEST IS THE CURVATURE COMPUTATION')
    print('  ' + '=' * 74)
    hh = all(lands_in(br(GENS[a], GENS[b]), Hh) for a in Hh for b in Hh)
    hm = all(lands_in(br(GENS[a], GENS[b]), Mm) for a in Hh for b in Mm)
    mm = all(lands_in(br(GENS[a], GENS[b]), Hh) for a in Mm for b in Mm)
    check(f'⓸ the three inclusions hold over every basis pair: [h,h]⊂h ({len(Hh)**2}), '
          f'[h,m]⊂m ({len(Hh)*len(Mm)}), [m,m]⊂h ({len(Mm)**2})', hh and hm and mm)
    nz = [(a, b) for a in Mm for b in Mm if np.linalg.norm(br(GENS[a], GENS[b])) > 1e-9]
    check(f'⓸ᵇ ⛔ and [m,m] does NOT vanish -- {len(nz)} nonvanishing pairs -- so the canonical '
          'splitting σ = m has curvature F(X,Y) = [σX,σY] valued in ker ρ = h, and it is nonzero',
          len(nz) > 0)
    # ** and the curvature is the substrate's own **
    MDIR = [0, 1, 2, 3, 5]

    def mv(a):
        return GENS[tuple(sorted((a, 4)))]

    bad = []
    for a in MDIR:
        for b in MDIR:
            for c in MDIR:
                R = -br(br(mv(a), mv(b)), mv(c))
                cand = ETA[b, b] * (c == b) * mv(a) - ETA[a, a] * (c == a) * mv(b)
                if np.linalg.norm(R) < 1e-9 and np.linalg.norm(cand) < 1e-9:
                    continue
                if np.linalg.norm(cand) < 1e-9:
                    bad.append((a, b, c))
                    continue
                K = np.sum(R * cand) / np.sum(cand * cand)
                if not np.allclose(R, K * cand, atol=1e-9) or abs(abs(K) - 1) > 1e-9:
                    bad.append((a, b, c))
    check(f'⛭ ⓸ᶜ *** and that curvature IS the substrate\'s Riemann tensor: −[[X,Y],Z] = '
          f'K(⟨Y,Z⟩X − ⟨X,Z⟩Y) with |K|=1, on all {len(MDIR)**3} triples of m, failures {bad or 0} '
          '-- so "the bracket closes" and "the connection is curved by exactly the Riemann tensor" '
          'are ONE computation, run once and read twice ***', bad == [])

    # ============================================================ (5) an absence that is a theorem
    print()
    print('  ' + '=' * 74)
    print('  PART 5 -- ⓺ AND ONE ABSENCE IS A CONSEQUENCE, NOT A GAP')
    print('  ' + '=' * 74)
    allg = [GENS[ab] for ab in IDX]
    viol = sum(1 for X, Y, Z in itertools.product(allg, allg, allg)
               if np.linalg.norm(br(br(X, Y), Z) + br(br(Y, Z), X) + br(br(Z, X), Y)) > 1e-9)
    # ⌗ same repair (r3970): the corpus now says `Jacobi` once, in P09 -- not in P12, so the point
    #   stands where this file makes it.  ** The computation is the load-bearing half and it is
    #   untouched: the identity HOLDS, checked on every basis triple. **  The corpus-wide zero is
    #   pinned at the throw and the live count reported.
    _jac_then = sum(_at_build_counts('Jacobi').values())
    _jac_now = RB.counts('Jacobi')
    check(f'⓺ `Jacobi` occurred {_jac_then} times in seventeen papers at {_AT_BUILD} and '
          f'{sum(_jac_now.values())} now ({dict((k, v) for k, v in _jac_now.items() if v)}, none in '
          f'P12), and so(5,1) satisfies it: {viol} violations over all {len(allg)**3} basis triples',
          viol == 0 and _jac_then == 0 and _jac_now['P12'] == 0)
    check('⓺ᵇ ⇒ for an ACTION algebroid the algebroid Jacobi identity is inherited from the acting '
          'algebra, so the axiom the corpus never states is AUTOMATIC for the class it built -- the '
          'Ⓘ pattern this theatre already banked, where a field that reaches nothing delivers a '
          'theorem',
          viol == 0 and 'a field that reaches nothing can still deliver a theorem'
          in open(os.path.join(ROOT, 'THE_MATHEMATICS_REACH.md'), encoding='utf-8').read())

    # ============================================================ (6) not a re-find
    print()
    print('  ' + '=' * 74)
    print('  PART 6 -- ⌗ AND THIS IS NOT A RE-FIND OF P12\'S OWN IDENTIFICATION')
    print('  ' + '=' * 74)
    check('⓻ P12 identifies the STRUCTURE FUNCTION with the coset METRIC -- a different object from '
          'a curvature, and untouched here',
          'The structure function is the substrate\'s metric' in B['P12']
          and 'identified with the coset metric of the symmetric space' in B['P12'])
    # ⌗ and this one too (r3970).  The load-bearing half is the FIRST clause -- the corpus calls
    #   nothing the curvature of a connection, which is what keeps PART 6's "not a re-find" claim
    #   true -- and it still holds at zero.  `splitting` and `horizontal` arrived in P12 with the
    #   r3251 landing, which is this station's own finding in the paper, so they are reported.
    check(f'⓻ᵇ and the corpus STILL calls nothing the curvature of a connection '
          f'({sum(RB.counts("curvature of the connection").values())} occurrences), so the '
          f'identification in PART 6 is untouched -- while `splitting` ({RB.counts("splitting")["P12"]}) '
          f'and `horizontal` ({RB.counts("horizontal")["P12"]}) did arrive in P12 with r3251, both '
          f'ZERO at {_AT_BUILD}',
          sum(RB.counts('curvature of the connection').values()) == 0
          and _at_build_counts('splitting')['P12'] == 0
          and _at_build_counts('horizontal')['P12'] == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:150]}')
        return 1
    print('  VERDICT: ** the Atiyah sequence is not missing from P12.  It is P12\'s object, unnamed,')
    print('  and all four of its terms are already in the paper under four other words. **')
    print('  ⌗ ** The caveat this station carried -- "P12\'s algebroid is the constraint algebra\'s')
    print('     and not a bundle\'s" -- is right in general and wrong here: ** the action algebroid')
    print('     of G on G/H IS the Atiyah algebroid of G → G/H, and the base on the orbit is the')
    print('     coset the substrate already is.')
    print('  ⌗ ** ker(anchor) = h = "the cut-fixing isotropy"; im = m = "the cut-deforming coset";')
    print('     and "a section of the bundle that would select a definite flow" is the splitting. **')
    print('     *The paper supplies the splitting and does not say what it splits.*')
    print('  ⛭ ** And P12\'s closure test IS the curvature computation: ** [m,m] ⊂ h says the')
    print('     splitting\'s curvature is valued in the isotropy, and −[[X,Y],Z] is the substrate\'s')
    print('     Riemann tensor on all 125 triples.  *One computation, run once, read twice.*')
    print('  ⌗ ** The structure that relates them is in the book the paper already cites. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
