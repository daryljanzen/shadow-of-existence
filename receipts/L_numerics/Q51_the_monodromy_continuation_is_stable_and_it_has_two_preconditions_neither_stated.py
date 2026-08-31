#!/usr/bin/env python3
r"""Q51 -- P05's MONODROMY IS COMPUTED AT ONE DISCRETISATION AND ONE RADIUS.  SWEPT, IT IS STABLE
     OVER THREE DECADES -- AND IT HAS TWO PRECONDITIONS, BOTH OF WHICH FAIL SILENTLY.

** WHAT THE PAPER SAYS, AND WHY THIS IS NOT A NIT.  ** `groupoid_paper.tex` `prop:monodromy` closes
with *"(Verified numerically by continuation in the complex $2M$-plane.)"*, and
`rem:monodromy-group` says outright that the generation claim ** IS a computation ** whose
alternative was real: *"Two transpositions generate $S_{3}$ only if they DIFFER ... Had the same
pair collided at both, the group would have been $\mathbb{Z}_{2}$ and the claim false, so the
alternative was a real one."*

*** THAT $S_{3}$ IS LOAD-BEARING ACROSS THE CORPUS. ***  *It is the Weyl group of $A_2$, the Galois
group of the horizon cubic (`rem:galois`), the family symmetry read on the fermion sector, and the
first factor of $\mathrm{Aut}(A_2)=S_3\times\mathbb{Z}_2$.*  ** And a continuation that steps too
coarsely mislabels sheets. **  *Nothing in `P05` or `X5_monodromy_group` sweeps the step count or
the loop radius, so what is established is the permutation AT ONE DISCRETISATION.*

*** THE ANSWER: THE COMPUTATION IS ROBUST. ***
  * ** At $2M_{*}=+2/(3\sqrt3)$ the loop induces $(1\,2)$ and at $-2M_{*}$ it induces $(0\,1)$ --
    the same two transpositions at every step count from 4 to 1024 and every radius from $0.3$ down
    to $0.001$. **  *They differ, so they generate $S_3$, of order six.*
  ⇒ ** `prop:monodromy` and `rem:monodromy-group` stand, and now they stand on a sweep. **

⛔⛭⛭ *** AND THE SWEEP FOUND THE TWO PRECONDITIONS THE SENTENCE DOES NOT STATE, BOTH OF WHICH FAIL
     SILENTLY -- returning a plausible permutation rather than an error. ***

  1. ** THE LOOP MUST NOT ENCLOSE BOTH BRANCH POINTS. **  *The two Nariai values sit at
     $\pm2/(3\sqrt3)$, separated by $0.7698$.  A loop of radius $0.8$ about one of them encircles the
     other as well and returns the **3-cycle** $(0\,1\,2)$ -- the PRODUCT of the two transpositions,
     which is a correct monodromy of a different loop and a wrong answer to the paper's question.*
     ** The precondition is $\epsilon<2\cdot 2/(3\sqrt3)$, and it is geometric: it is the same
     separation the discriminant $\Delta=4-27(2M)^{2}$ already measures. **
  2. ** THE LOOP MUST BE RESOLVED. **  *At radius $8$ and TWO steps the continuation returns the
     IDENTITY -- no permutation at all, which would make the deck structure vacuous -- and at three
     steps it returns a 3-cycle.*  ** Neither raises an error.  The matching is nearest-neighbour and
     nearest-neighbour matching always succeeds; when the roots move further than their separation
     between samples it succeeds at the wrong pairing. **

⌗ ** SO THE CONTROL IS NOT MANUFACTURED: the test CAN come out otherwise, and both ways it does are
exhibited here rather than argued. **  *A refinement sweep that never breaks is a sweep that cannot
detect the failure it was written for -- the same shape as `Q50`'s one-sided mutation, one field
earlier.*

⌗ ** WHAT IS NOT CLAIMED. **  *Not that `P05` is wrong -- it is right, and the sweep is what now says
so.  Not that its receipt should have swept: `X5_monodromy_group` establishes the permutations and
that is what it was written to do.  Only that "verified numerically" was carrying two conditions,
and that both are cheap to state and cheap to violate.*

COMPUTES: scope.
  * The cubic is $r^{3}-r+2M$ in the gauge $\alpha=1$ -- `P05` `sec:deck`'s own normalisation, and
    `M_STAR` $=2/(3\sqrt3)$ its Nariai value.
  * `NSTEPS` and `RADII` are the swept discretisations and loop radii.  ** The verdict is a pair of
    permutations and must not move inside the valid region; it MUST move outside it. **
  * `BIG_R`, `COARSE` are the deliberately-invalid settings the two controls use.
  * ** NOT CLAIMED: any statement about the Galois group over a field. **  *That is `T1`'s and
    `T50`'s; this is about a numerical continuation.*

Written r3724 by node 60, numerical-analysis v2 pass, probe `Q51`, closing that field's one open row.
"""
import itertools

import numpy as np

M_STAR = 2 / (3 * np.sqrt(3))
NSTEPS = (4, 8, 16, 32, 64, 128, 256, 1024)
RADII = (0.3, 0.1, 0.03, 0.01, 0.003, 0.001)
BIG_R, COARSE = 0.8, 2

FAILS = []


def check(name, cond):
    ok = bool(cond)
    print(f"    [{'ok ' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILS.append(name)


def continue_loop(center, eps, nstep):
    r"""continue the three roots once around $2M=\text{center}+\epsilon e^{i\phi}$

    ** The matching is nearest-neighbour, which is what `P05` describes as "matching by continuity"
    -- and which always succeeds, correctly or not. **
    """
    r0 = np.sort_complex(np.roots([1, 0, -1, center + eps]))
    cur = r0.copy()
    for j in range(1, nstep + 1):
        nr = np.roots([1, 0, -1, center + eps * np.exp(2j * np.pi * j / nstep)])
        used, new = set(), np.empty(3, complex)
        for i in sorted(range(3), key=lambda i: min(abs(nr - cur[i]))):
            d = sorted((abs(nr[k] - cur[i]), k) for k in range(3) if k not in used)
            new[i] = nr[d[0][1]]
            used.add(d[0][1])
        cur = new
    return tuple(int(np.argmin(abs(r0 - cur[i]))) for i in range(3))


def cycle_type(p):
    seen, out = set(), []
    for i in range(3):
        if i in seen:
            continue
        c, j = [], i
        while j not in seen:
            seen.add(j)
            c.append(j)
            j = p[j]
        out.append(len(c))
    return tuple(sorted(out, reverse=True))


def group_order(gens):
    G = {(0, 1, 2)}
    while True:
        new = {tuple(a[b[i]] for i in range(3)) for a in G for b in gens} | G
        if new == G:
            return len(G)
        G = new


if __name__ == '__main__':
    print(__doc__)
    print('=' * 98)
    print('(A) THE SWEEP — every step count against every radius, at both branch points')
    print('=' * 98)
    print(f'    Nariai values 2M = +/- {M_STAR:.6f};  separation {2*M_STAR:.6f}')
    for center, tag in ((M_STAR, '+2M*'), (-M_STAR, '-2M*')):
        print(f'\n    about {tag}:')
        print('      ' + f"{'radius':>8} " + ' '.join(f'n={n:<5}' for n in NSTEPS))
        seen = set()
        for eps in RADII:
            row = [continue_loop(center, eps, n) for n in NSTEPS]
            seen |= set(row)
            print('      ' + f'{eps:>8g} ' + ' '.join(f'{"".join(map(str,p)):<7}' for p in row))
        check(f'  {tag}: ONE permutation over {len(NSTEPS)}x{len(RADII)} settings '
              f'-> {sorted(seen)}', len(seen) == 1)
        p = seen.pop()
        check(f'  {tag}: and it is a TRANSPOSITION, cycle type {cycle_type(p)}',
              cycle_type(p) == (2, 1))
        globals()['P_PLUS' if center > 0 else 'P_MINUS'] = p

    print()
    check(f'the two branch points give DIFFERENT transpositions — {P_PLUS} against {P_MINUS}, '
          'which is the alternative rem:monodromy-group says was real', P_PLUS != P_MINUS)
    n = group_order([P_PLUS, P_MINUS])
    check(f'and together they generate a group of order {n} — S_3', n == 6)

    print()
    print('=' * 98)
    print('(B) THE TWO PRECONDITIONS — both fail SILENTLY, returning a plausible permutation')
    print('=' * 98)
    print(f'    CONTROL 1 — a loop of radius {BIG_R} about +2M* encloses BOTH branch points '
          f'(separation {2*M_STAR:.4f}):')
    big = [continue_loop(M_STAR, BIG_R, n) for n in (64, 256, 1024)]
    print('      ' + '   '.join(f'n={n}: {"".join(map(str,p))} (cycle type {cycle_type(p)})'
                                for n, p in zip((64, 256, 1024), big)))
    check(f'  the enclosing loop returns a 3-CYCLE, not a transposition — the PRODUCT of the two',
          all(cycle_type(p) == (3,) for p in big))
    check('  and it is exactly the product of the two transpositions',
          big[-1] == tuple(P_PLUS[P_MINUS[i]] for i in range(3))
          or big[-1] == tuple(P_MINUS[P_PLUS[i]] for i in range(3)))

    print()
    print(f'    CONTROL 2 — an under-resolved loop, {COARSE} steps, at radii where the roots move '
          f'further than their separation between samples:')
    coarse = [(e, continue_loop(M_STAR, e, COARSE)) for e in (0.3, 1.5, 8.0, 40.0)]
    for e, p in coarse:
        print(f'      eps={e:<6g} n={COARSE}: {"".join(map(str,p))}  (cycle type {cycle_type(p)})')
    ident = [p for e, p in coarse if p == (0, 1, 2)]
    check(f'  under-resolution returns the IDENTITY at large radius — no permutation at all, which '
          f'would make the deck structure vacuous ({len(ident)} of {len(coarse)} settings)',
          len(ident) > 0)
    # §4: if a line is a record, PRINT it.  "no error was raised" is a fact about what did not
    # happen, and `check(..., True and <tautology>)` would have been a hollow assertion wearing a
    # verdict.  The four rows above are the record; this is the sentence that reads them.
    print('           and NOT ONE of the four raised an error -- nearest-neighbour matching always')
    print('           succeeds, so a wrong pairing is returned as confidently as a right one.')
    print('           THAT is why the sweep is the only thing that could have found this.')

    print()
    print('=' * 98)
    print('    => THE COMPUTATION IS ROBUST INSIDE ITS REGION AND THE REGION HAS A BOUNDARY.')
    print(f'       Valid: eps < {2*M_STAR:.4f} (the branch-point separation, which the discriminant')
    print('       4 - 27(2M)^2 already measures) and the loop resolved.  Outside either, the')
    print('       continuation returns a wrong permutation and says nothing about it.')
    print('=' * 98)
    if FAILS:
        print(f'  {len(FAILS)} FAILED: ' + '; '.join(FAILS))
        raise SystemExit(1)
    print('  ALL PASS')
