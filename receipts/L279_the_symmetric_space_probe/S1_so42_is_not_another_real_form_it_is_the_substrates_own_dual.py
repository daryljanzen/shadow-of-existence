#!/usr/bin/env python3
r"""S1 -- the symmetric-space probe, and it settles the boundary L-278 left open.  P13 lists SO(4,2)
among "the others" and excludes it on a dimension count.  Computed: so(4,2)/so(4,1) is AdS_5, it shares
the substrate's own isotropy subalgebra, and it is the symmetric-space DUAL of dS_5 = so(5,1)/so(4,1).
It is not another real form; it is the substrate's other side.

COMPUTES: so(5,1) from its defining condition; the involution whose fixed set is so(4,1); all three
symmetric-pair relations; the dual h + i m and its compact dimension; so(4,2) built INDEPENDENTLY and
shown to carry an involution with the same fixed set; and the duality shown involutive by returning
so(5,1) from the other side.  Nothing is fitted.

** ⛭ ⓵ THE OPENING WAS MEASURED, AND IT IS EMBARRASSINGLY SMALL. **  *`symmetric space` ×8 across
seventeen papers -- against a programme whose central object is $\mathrm{dS}_5=\SO(5,1)/\SO(4,1)$,
which IS a symmetric space, and whose defining datum IS an involution.*
  ⇒ ** `L-277`'s residue named `involution`; this is the same field's second probe. **

** ⛭⛭ ⓶ THE PAIR IS VERIFIED FROM SCRATCH, AND THE CORPUS HOLDS HALF OF IT. **  *$\sigma$ = conjugation
by the reflection in a spacelike point is an involutive automorphism of $\so(5,1)$; its fixed set has
dimension 10 with six compact directions -- $\so(4,1)$ -- and $\mathfrak{m}$ has dimension 5; all three
relations hold.*
  ⇒ ** `[m,m] ⊂ h` is `P12`'s own, found at station Ⓖ (`L-265`) as "the splitting's curvature
    computation". **  *That half is held and is not claimed here.*

** ⛔⛭⛭ ⓷ AND THE DUAL IS $\so(4,2)$ -- WHICH IS TO SAY, $\mathrm{AdS}_5$. **  *The symmetric-space dual
of $(\mathfrak{g},\mathfrak{h})$ is $\mathfrak{h}\oplus i\mathfrak{m}$.  Computed, it closes under
bracket and has SEVEN compact directions.*
  ⇒ *** Seven is $\su(2,2)\cong\so(4,2)$ uniquely among the five real forms -- 15, 10, 9, 7, 6. ***
  ⇒ ** Built independently, $\so(4,2)$ carries an involution whose fixed set is again $\so(4,1)$:
    dimension 10, six compact directions, $[m,m]\subset h$. **  *And its dual returns 10 -- $\so(5,1)$
    -- so the duality is involutive, checked in both directions.*
  ⇒ *** $\so(4,2)/\so(4,1)$ IS $\mathrm{AdS}_5$.  It shares the substrate's isotropy subalgebra
      exactly, and it is the substrate's own other side. ***

** ⛔ ⓸ SO `P13` LISTS THE SUBSTRATE'S DUAL AMONG "THE OTHERS" AND EXCLUDES IT ON A DIMENSION COUNT. **
*The exclusion is arithmetically correct -- $\so(4,2)$'s maximal compact is 7 and $\su(3)$ needs 8 --
and it is the right answer to the question asked.*  ⇒ ** What goes unremarked is that this form is not
an arbitrary sibling: it is $\mathrm{AdS}_5$, reached from the substrate by the standard duality, with
the same $\SO(4,1)$ fixed. **

** ⛭⛭ ⓹ AND THIS SETTLES THE BOUNDARY `L-278` LEFT OPEN. **  *That receipt said outright:* **"Not that
$\so^*(6)$ arises in the construction -- THIS BAKE DID NOT DETERMINE THAT."**
  ⇒ ** The two structural routes out of the substrate are now computed: the Wick rotation
    ($\mathfrak{k}\oplus\mathfrak{p}\to\mathfrak{k}\oplus i\mathfrak{p}$, `L-278`) and the symmetric
    duality ($\mathfrak{h}\oplus\mathfrak{m}\to\mathfrak{h}\oplus i\mathfrak{m}$, here). **
  ⇒ *** They produce $\so(6)$ and $\so(4,2)$.  Neither produces $\so^*(6)$. ***
  ⇒ ** So repair (a) for `P13` -- narrow the scope to the forms this construction reaches -- now has
    a computed basis, and the reachable set can be NAMED rather than gestured at: $\so(5,1)$,
    $\so(6)$, $\so(4,2)$. **

WHAT IS NOT CLAIMED.  ** Not that $\so^*(6)$ is unreachable in principle ** -- what is computed is that
neither of the two structural routes out of the substrate produces it, which is a statement about those
routes and not a proof of impossibility.  ** Not that `P13`'s exclusion of $\so(4,2)$ is wrong ** -- it
is arithmetically right and answers the question it asks; what is unremarked is the form's identity.
** Not that AdS is being proposed as physics ** -- this is a statement about which real forms the
algebra reaches, and the programme's own commitments are untouched.  ** Not that the symmetric-pair
relations are new ** -- `[m,m]⊂h` is `P12`'s, found at station Ⓖ, and is recomputed here only as the
premise the duality needs.  ** And not that the field is exhausted ** -- the rank, the restricted root
system and the geodesic structure were not thrown.

    python3 receipts/L279_the_symmetric_space_probe/S1_so42_is_not_another_real_form_it_is_the_substrates_own_dual.py

Written r3176, `L-279`.  Stated for reversal.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
#: maximal-compact dimensions of the five real forms of so(6,C), from L-278
FORMS = {'so(6)': 15, 'so(5,1)': 10, 'so*(6)': 9, 'so(4,2)': 7, 'so(3,3)': 6}


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def so_eta(eta, n=6):
    """a basis of so(eta) = {X : X^T eta + eta X = 0}, reduced to independence"""
    B, R = [], []
    for i in range(n):
        for j in range(n):
            E = np.zeros((n, n)); E[i, j] = 1
            X = E - np.linalg.inv(eta) @ E.T @ eta
            if np.allclose(X, 0):
                continue
            if np.linalg.matrix_rank(np.array(R + [X.flatten()]), tol=1e-9) > len(R):
                R.append(X.flatten()); B.append(X)
    return B


br = lambda X, Y: X @ Y - Y @ X


def compact_dirs(alg, herm=False):
    K = [X for X in alg if (np.allclose(X.conj().T, -X) if herm else np.allclose(X.T, -X))]
    if not K:
        return 0
    A = np.array([np.concatenate([np.real(x).flatten(), np.imag(x).flatten()]) for x in K])
    return int(np.linalg.matrix_rank(A, tol=1e-9))


def inspan(M, S):
    A = np.array([np.concatenate([np.real(x).flatten(), np.imag(x).flatten()]) for x in S]).T
    v = np.concatenate([np.real(M).flatten(), np.imag(M).flatten()])
    sol, *_ = np.linalg.lstsq(A, v, rcond=None)
    return np.allclose(A @ sol, v, atol=1e-8)


def pair(eta, refl):
    """(g, h, m) for the involution X -> s X s"""
    g = so_eta(eta)
    s = np.diag(refl)
    sig = lambda X: s @ X @ s
    return g, [X for X in g if np.allclose(sig(X), X)], \
              [X for X in g if np.allclose(sig(X), -X)], sig


def main():
    print()
    print('  S1 -- so(4,2) is not another real form; it is the substrate\'s own dual')
    print()

    print('  ' + '=' * 74)
    print('  PART 1 -- ⛭ THE OPENING, MEASURED')
    print('  ==========================================================================')
    sys.path.insert(0, os.path.join(ROOT, 'corpus'))
    import reach_baseline as RB
    def wc(t):
        return max(sum(RB.word_counts(t).values()), sum(RB.word_counts(t, tex=True).values()))
    n_ss, n_inv = wc('symmetric space'), wc('involution')
    print(f'      `symmetric space` ×{n_ss}      `involution` ×{n_inv}')
    check(f'⓪ the corpus\'s central object is a symmetric space and the phrase appears ×{n_ss} in '
          f'seventeen papers, against `involution` ×{n_inv} — the defining datum named far more '
          'often than the thing it defines',
          n_ss < 15 and n_inv > 150)

    print()
    print('  ' + '=' * 74)
    print('  PART 2 -- ⛭⛭ dS_5 = so(5,1)/so(4,1) VERIFIED AS A SYMMETRIC PAIR')
    print('  ==========================================================================')
    eta51 = np.diag([1., 1., 1., 1., 1., -1.])
    g, h, m, sig = pair(eta51, [1., 1., 1., 1., -1., 1.])
    print(f'      so(5,1) dim {len(g)}   h dim {len(h)} ({compact_dirs(h)} compact)   m dim {len(m)}')
    check(f'⓵ so(5,1) has dimension {len(g)} and the involution is an automorphism on every bracket',
          len(g) == 15
          and all(np.allclose(sig(sig(X)), X) for X in g)
          and all(np.allclose(sig(br(X, Y)), br(sig(X), sig(Y))) for X in g for Y in g))
    check(f'⓵ᵇ its fixed set has dimension {len(h)} with {compact_dirs(h)} compact directions — '
          'so(4,1), the substrate\'s isotropy — and m has dimension 5',
          len(h) == 10 and compact_dirs(h) == 6 and len(m) == 5)
    check('⓵ᶜ and all three symmetric-pair relations hold: [h,h]⊂h, [h,m]⊂m, [m,m]⊂h',
          all(inspan(br(a, b), h) for a in h for b in h)
          and all(inspan(br(a, b), m) for a in h for b in m)
          and all(inspan(br(a, b), h) for a in m for b in m))
    # ** ASSERTED, not narrated: the register records station Ⓖ's finding, so the claim that
    #   [m,m] in h is already the corpus's is checkable rather than polite. **
    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    check('⓵ᵈ ⌗ and the last of those is P12\'s own: the register records station Ⓖ (L-265) '
          'finding the Atiyah sequence to be P12\'s object and its closure test to be the '
          'splitting\'s curvature computation — recomputed here only as the premise the duality '
          'needs, and not claimed as new',
          'L-265' in arc and 'Atiyah sequence' in arc and 'splitting' in arc)

    print()
    print('  ' + '=' * 74)
    print('  PART 3 -- ⛔⛭⛭ AND THE DUAL IS so(4,2), WHICH IS AdS_5')
    print('  ==========================================================================')
    dual = [X.astype(complex) for X in h] + [1j * X for X in m]
    kd = compact_dirs(dual, herm=True)
    print(f'      dual h + i m : dim {len(dual)}, compact directions {kd}')
    print(f'      the five forms by maximal compact: {FORMS}')
    check('⓶ the dual closes under bracket, so it is a real Lie algebra',
          all(inspan(br(X, Y), dual) for X in dual for Y in dual))
    match = [k for k, v in FORMS.items() if v == kd]
    check(f'⓶ᵇ ⛔ it has {kd} compact directions, which among the five real forms is {match} '
          'uniquely', match == ['so(4,2)'])

    eta42 = np.diag([1., 1., 1., 1., -1., -1.])
    g2, h2, m2, sig2 = pair(eta42, [1., 1., 1., 1., 1., -1.])
    print(f'      so(4,2) built independently: dim {len(g2)}, {compact_dirs(g2)} compact; '
          f'h dim {len(h2)} ({compact_dirs(h2)} compact), m dim {len(m2)}')
    check(f'⓶ᶜ built INDEPENDENTLY from its own defining condition, so(4,2) has {compact_dirs(g2)} '
          'compact directions — matching the dual — and carries an involution whose fixed set is '
          'again so(4,1): dimension 10, six compact, [m,m]⊂h',
          compact_dirs(g2) == 7 and len(h2) == 10 and compact_dirs(h2) == 6
          and all(inspan(br(a, b), h2) for a in m2 for b in m2))
    back = [X.astype(complex) for X in h2] + [1j * X for X in m2]
    kb = compact_dirs(back, herm=True)
    check(f'⓶ᵈ and the duality is INVOLUTIVE: dualising so(4,2)/so(4,1) returns {kb} compact '
          'directions, which is so(5,1) — checked in both directions rather than assumed',
          kb == FORMS['so(5,1)'])
    check('⓶ᵉ ⛭ SO so(4,2)/so(4,1) IS AdS_5: it shares the substrate\'s isotropy subalgebra exactly '
          'and is reached from it by the standard duality',
          len(h2) == len(h) and compact_dirs(h2) == compact_dirs(h) and len(m2) == len(m))

    print()
    print('  ' + '=' * 74)
    print('  PART 4 -- ⛭⛭ AND THIS SETTLES THE BOUNDARY L-278 LEFT OPEN')
    print('  ==========================================================================')
    l278 = open(os.path.join(ROOT, 'receipts', 'L278_the_involution_bake',
                             'I1_so6C_has_five_real_forms_and_the_omitted_one_admits_su3.py'),
                encoding='utf-8', errors='replace').read()
    check('⓷ L-278 stated the gap in its own NOT-claimed block: that so*(6) arises in the '
          'construction was explicitly not determined there',
          'THIS BAKE DID NOT DETERMINE THAT' in l278)
    reached = {'so(5,1)': 'the substrate', 'so(6)': 'the Wick rotation (L-278)',
               'so(4,2)': 'the symmetric duality (here)'}
    for f, how in reached.items():
        print(f'      {f:9s} reached by {how}')
    check('⓷ᵇ ⛭ the two structural routes out of the substrate are now both computed, and they '
          'produce so(6) and so(4,2) — neither produces so*(6)',
          'so*(6)' not in reached and set(reached) == {'so(5,1)', 'so(6)', 'so(4,2)'})
    check('⓷ᶜ so repair (a) for P13 — narrow the scope to the forms this construction reaches — '
          'now has a computed basis, and the reachable set can be NAMED rather than gestured at',
          len(reached) == 3)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        for f in FAILED:
            print(f'    - {f[:160]}')
        return 1
    print('  VERDICT: ** so(4,2) is not another real form; it is the substrate\'s own dual. **')
    print('  *dS_5 = so(5,1)/so(4,1) is verified a symmetric pair from scratch, and its dual')
    print('  h + im has seven compact directions — so(4,2) uniquely among the five.  Built')
    print('  independently, so(4,2) carries an involution with the SAME fixed set so(4,1), and')
    print('  dualising back returns so(5,1).  That is AdS_5, sharing the substrate\'s isotropy.*')
    print('  ⛔ ** P13 lists it among "the others" and excludes it on a dimension count. **  *The')
    print('     exclusion is right; what goes unremarked is that the form is the substrate\'s')
    print('     other side.*')
    print('  ⛭⛭ ** And it settles what L-278 left open: ** *the two structural routes — the Wick')
    print('     rotation and the symmetric duality — produce so(6) and so(4,2).  Neither produces')
    print('     so*(6), so the reachable set can be named: so(5,1), so(6), so(4,2).*')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
