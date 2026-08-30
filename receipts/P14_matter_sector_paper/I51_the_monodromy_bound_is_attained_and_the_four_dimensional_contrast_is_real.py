#!/usr/bin/env python3
r"""I51 -- P14 AND ITS OWN RECEIPT BOTH STOP AT AN UPPER BOUND.  THE BOUND IS ATTAINED, AND THE
     FOUR-DIMENSIONAL CONTRAST THE PAPER DRAWS AGAINST IT IS REAL.

** WHAT THE PAPER SAYS.  ** `matter_sector_paper.tex` L642-645: *"The polynomial $r^{D-1}-r^{D-3}+2M$
has its two powers of one parity, so it is even in $r$ exactly at odd $D$; its root set is then stable
under a fixed-point-free involution, and the monodromy over the mass plane commutes with it.  At $D=5$
this **confines** the monodromy to the centraliser of $(0\,1)(2\,3)$ in $S_{4}$, of order eight against
twenty-four, so the monodromy group **cannot be** the full symmetric group on the roots and the
four-dimensional statement that it is has no odd-dimensional analogue."*

⛔ ** AND THAT IS AN UPPER BOUND, WHICH IS WHERE BOTH THE PAPER AND ITS RECEIPT STOP. **  *The existing
`P14_odd_D_is_pair_symmetric.py` asserts `len(S4) == 24 and len(cent) == 8` -- the SIZE OF THE
CENTRALISER, not the size of the monodromy group.*  ** "Contained in a group of order 8" is consistent
with the monodromy being trivial, and a trivial monodromy would mean the four roots never permute at
all -- which would make the `D=5` deck structure the paper reasons about empty rather than merely
smaller. **
  ⇒ *** So the claim as it stands cannot distinguish "smaller than $S_4$" from "nothing there", and
      that distinction is the whole content of the contrast it draws with $D=4$. ***

*** WHAT IS MEASURED HERE.  The monodromy group is COMPUTED, by continuing the roots around loops in
    the mass plane and recording the permutations they induce. ***
  * ** at $D=5$ the group has order EXACTLY 8 -- the bound is ATTAINED, not merely respected. **
    *So the monodromy is the full centraliser $D_4$, the imprimitive wreath-product symmetry of two
    $\pm$ pairs, and the structure is real rather than vacuous.*
  * ** at $D=4$ it is the full $S_3$, order 6. **  *Which is the four-dimensional statement the paper
    contrasts against, verified here rather than assumed -- and it is the CONTROL that makes the $D=5$
    number mean something: the same procedure returns "full symmetric group" where the paper says it
    should, and "order 8 of 24" where the paper says it should not.*

⌗ ** WHY THE COVER FACTORS, which is the reason the bound is attained. **  *$r^{4}-r^{2}+t$ is even, so
$u=r^{2}$ satisfies $u^{2}-u+t=0$: the degree-4 cover of the $t$-plane FACTORS as a degree-2 cover
($t\mapsto u$, branched at $t=\tfrac14$) beneath a degree-2 cover ($u\mapsto r=\pm\sqrt u$, branched
where $u=0$, i.e. $t=0$).*  ⇒ ** A loop about $t=\tfrac14$ exchanges the two pairs; a loop about $t=0$
exchanges the two roots within a pair.  Those two generate the order-8 wreath product, so the bound is
attained for a structural reason and not by accident. **

COMPUTES: scope -- what the pinned numbers do and do not bound.
  * `D = 4, 5` are the only dimensions measured.  ** The paper's claim is about odd $D$ generally; this
    receipt establishes it AT $D=5$ and does not generalise. **  *The evenness argument that bounds the
    group is already general and already receipted; what is added here is attainment at the one
    dimension the paper actually reasons about.*
  * `steps`, `radius` bound the CONTINUATION's accuracy only, and both are swept: the permutation must
    be stable under refining the step and under changing the loop radius, or it is an artefact of the
    tracking rather than a fact about the cover.
  * ** `t0 = 0.03` is a basepoint and must avoid the branch points $t=0$ and $t=\tfrac14$; any other
    interior basepoint gives a conjugate group and the same ORDER, which is the invariant claimed. **

Written r3662 by node 60, pass B on row 1 of the index-theory locator (`P14`).
"""
import itertools

import numpy as np

np.random.seed(11)


def poly_roots(D, t):
    r"""roots of $r^{D-1}-r^{D-3}+2M$ with $2M=t$, highest power first"""
    c = [0.0] * D
    c[0] = 1.0            # r^{D-1}
    c[2] = -1.0           # r^{D-3}
    c[-1] = t             # constant 2M
    return np.roots(c)


def track_loop(D, centre, radius, t0, steps):
    r"""continue the roots once around `centre` and return the permutation induced

    ** The tracking is nearest-neighbour matching between consecutive steps, which is correct only
    while the step is small enough that no two roots come closer than they move. **  *That is exactly
    what the step sweep below is checking, and it is why the sweep is part of the measurement rather
    than decoration.*
    """
    start = poly_roots(D, t0)
    cur = start.copy()
    order = list(range(len(start)))          # order[i] = which START root slot i now holds
    ang0 = np.angle(t0 - centre)
    for k in range(1, steps + 1):
        t = centre + radius * np.exp(1j * (ang0 + 2 * np.pi * k / steps))
        nxt = poly_roots(D, t)
        used, newcur, neworder = set(), [], []
        for i, z in enumerate(cur):
            j = min((jj for jj in range(len(nxt)) if jj not in used),
                    key=lambda jj: abs(nxt[jj] - z))
            used.add(j)
            newcur.append(nxt[j])
            neworder.append(order[i])
        cur, order = np.array(newcur), neworder
    # match the endpoint back onto the start set: slot i ended up holding start root perm[i]
    used, perm = set(), []
    for z in cur:
        j = min((jj for jj in range(len(start)) if jj not in used),
                key=lambda jj: abs(start[jj] - z))
        used.add(j)
        perm.append(j)
    return tuple(perm[order.index(i)] for i in range(len(start)))


def generated_order(perms):
    """order of the permutation group generated by `perms` -- closure under composition"""
    n = len(perms[0])
    ident = tuple(range(n))
    grp = {ident}
    frontier = [ident]
    while frontier:
        new = []
        for g in frontier:
            for h in perms:
                c = tuple(g[h[i]] for i in range(n))
                if c not in grp:
                    grp.add(c)
                    new.append(c)
        frontier = new
    return len(grp), grp


def branch_points(D):
    r"""values of $t$ at which two roots collide -- the discriminant's zeros

    *For $D=5$: $t=0$ and $t=\tfrac14$.  For $D=4$: $t=\pm 2/(3\sqrt3)$.*
    """
    if D == 5:
        return [0.0 + 0j, 0.25 + 0j]
    if D == 4:
        v = 2.0 / (3.0 * np.sqrt(3.0))
        return [v + 0j, -v + 0j]
    raise ValueError(D)


def monodromy_order(D, t0, steps=4000, shrink=1.0):
    pts = branch_points(D)
    perms = []
    for c in pts:
        others = [abs(c - o) for o in pts if abs(c - o) > 1e-12] + [abs(c - t0)]
        rad = shrink * 0.45 * min(others)
        perms.append(track_loop(D, c, rad, t0, steps))
    return generated_order(perms)[0], perms


if __name__ == '__main__':
    print(__doc__)
    print('=' * 78)
    print('THE MEASUREMENT — the monodromy group COMPUTED, not bounded')
    print('=' * 78)

    t0_5, t0_4 = 0.03 + 0.011j, 0.05 + 0.013j
    o5, p5 = monodromy_order(5, t0_5)
    o4, p4 = monodromy_order(4, t0_4)
    print(f'    D = 5 :  quartic r^4 - r^2 + t   monodromy order {o5}   '
          f'(centraliser bound 8, |S_4| = 24)')
    print(f'              generators (as images): {p5}')
    print(f'    D = 4 :  cubic   r^3 - r   + t   monodromy order {o4}   (|S_3| = 6)')
    print(f'              generators (as images): {p4}')
    print()
    print(f'    ⇒ ** AT D=5 THE BOUND IS ATTAINED: {o5} = 8, so the monodromy IS the full')
    print('       centraliser and the pair structure is real rather than vacuous. **')
    print(f'    ⇒ ** AT D=4 IT IS THE FULL SYMMETRIC GROUP: {o4} = |S_3|, which is the')
    print('       four-dimensional statement the paper contrasts against. **')

    print()
    print('=' * 78)
    print('THE CONTROLS — a permutation that moves with the tracking is an artefact')
    print('=' * 78)
    for st in (1000, 2000, 4000, 8000):
        a, _ = monodromy_order(5, t0_5, steps=st)
        b, _ = monodromy_order(4, t0_4, steps=st)
        print(f'    steps = {st:>5} :  D=5 order {a}    D=4 order {b}')
    print()
    for sh in (0.3, 0.6, 0.9):
        a, _ = monodromy_order(5, t0_5, shrink=sh)
        b, _ = monodromy_order(4, t0_4, shrink=sh)
        print(f'    loop radius x{sh} :  D=5 order {a}    D=4 order {b}')
    print()
    for t0 in (0.03 + 0.011j, -0.2 + 0.4j, 0.6 - 0.3j):
        a, _ = monodromy_order(5, t0)
        print(f'    basepoint {t0!s:>16} :  D=5 order {a}   *conjugate group, same order*')

    print()
    print('=' * 78)
    print('WHY — the cover factors, so the bound is attained structurally')
    print('=' * 78)
    print('    r^4 - r^2 + t is EVEN, so u = r^2 obeys u^2 - u + t = 0:')
    print('      t -> u   degree 2, branched at t = 1/4   (exchanges the two PAIRS)')
    print('      u -> r   degree 2, branched at u = 0 i.e. t = 0   (exchanges WITHIN a pair)')
    print('    Those two generate the order-8 wreath product Z2 wr Z2 = D_4.')

    # ⛔⛭ ** pinned to measured values, never to `expr == True` -- the habit THE_ARSENAL records
    #   against this line, caught once in a receipt of every one of its six fields. **
    assert o5 == 8, o5
    assert o4 == 6, o4
    for st in (1000, 2000, 4000, 8000):
        assert monodromy_order(5, t0_5, steps=st)[0] == 8
        assert monodromy_order(4, t0_4, steps=st)[0] == 6
    for sh in (0.3, 0.6, 0.9):
        assert monodromy_order(5, t0_5, shrink=sh)[0] == 8
    # the identity is not a monodromy: each loop must actually move the roots
    assert all(p != tuple(range(len(p))) for p in p5), p5
    assert all(p != tuple(range(len(p))) for p in p4), p4
    print()
    print('  ALL PASS')
