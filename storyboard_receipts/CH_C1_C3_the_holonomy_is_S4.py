#!/usr/bin/env python3
"""RECEIPT — Cartan/holonomy bake `C1`–`C3`: ** THE RESIDUE PAIRING'S HOLONOMY IS S_4 = W(so(6,C)),
COMPUTED BY CONTINUATION AND NOT ASSUMED — AND THE GROUP IS GENERIC TO DEPRESSED CUBICS, SO THE
SURPRISE BELONGS ON THE OTHER SIDE OF THE MATCH. **

LEVEL: NO RATE — analytic continuation of an algebraic function and finite group theory.

WHY THIS RECEIPT EXISTS.  The Cartan/holonomy ledger (r3164) carries a real numerical computation --
  the monodromy of the three roots of r^3 - r + 2M together with the three branches of
  sqrt(f'(r_i)) = sqrt(3 r_i^2 - 1), continued around each Nariai point and around infinity -- and
  reports order 24, root image S_3, a Klein four-group kernel, and the element-order profile
  {1:1, 2:9, 3:8, 4:6}.  ** It receipts none of it, and every conclusion in the ledger turns on those
  numbers. **  Closed here.

C1 — THE GENERATORS, BY CONTINUATION.  gamma_+ and gamma_- are TRANSPOSITIONS OF DIFFERENT PAIRS, and
  gamma_inf is a 3-CYCLE.  That "different pairs" is not decoration: P05's rem:monodromy-group states
  the condition a naive version misses -- "two transpositions generate S_3 only if they differ" -- and
  this computation is what supplies it.  A control loop enclosing no branch point returns the
  identity, so the method can tell a small group from a large one.

C2 — THE GROUP.  Generated: order 24, root image S_3 (order 6), kernel of order 4 and equal to
  {(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)} -- exactly P05's Klein four-group, the even-sign
  patterns, arrived at by continuation rather than by unimodularity.  Element-order profile
  {1:1, 2:9, 3:8, 4:6}, which is S_4's and no other order-24 group's.

C3 — WHAT 24 SELECTS.  Among all classical Weyl groups of rank 2 to 6 and all five exceptionals, the
  only ones of order 24 are W(A_3) and W(D_3) -- and those coincide because so(6,C) = sl(4,C).  ** So
  the match is a RANK-THREE fact: it holds where it holds and fails immediately on either side. **

AND THE BAKE'S OWN BITE, which this receipt supports: the group is GENERIC to one-parameter depressed
  cubic families taken with their per-root square root.  So "substrate-derived rather than assumed" is
  sound about the DERIVATION -- the Klein four-group really does come from the residue pairing and is
  not put in by hand -- and misplaces the surprise.  What is not forced is that the substrate's Weyl
  group is the SAME group.

VERDICTS ARE ASSERTS.
"""
import numpy as np
import math
from collections import Counter

print("=" * 78)
print("  C1 / C2 / C3 — the holonomy of the residue pairing")
print("=" * 78)


def make_roots(a1):
    """roots of r^3 + a1 r + m, as a function of m.  ** f'(r) = 3 r^2 + a1, and the a1 term is
    load-bearing: dropping it changes the branch structure and collapses the group from 24 to 6.
    Caught by this receipt's own assert while it was being written. **"""
    return lambda m: np.roots([1, 0, a1, m]), (lambda r: 3 * r**2 + a1)


def track(pair, path, n=4000):
    rootfn, fp = pair
    ms = np.concatenate([np.linspace(path[i], path[i + 1], n) for i in range(len(path) - 1)])
    r = rootfn(ms[0])
    s = np.sqrt(fp(r) + 0j)             # branch of sqrt(f'(r))
    for m in ms[1:]:
        nr = rootfn(m)
        nr = nr[[int(np.argmin(np.abs(nr - x))) for x in r]]
        ns = np.sqrt(fp(nr) + 0j)
        ns = np.where(np.abs(ns - s) > np.abs(-ns - s), -ns, ns)
        r, s = nr, ns
    return r, s


def element(pair, base, path):
    rootfn, fp = pair
    r0 = rootfn(base)
    s0 = np.sqrt(fp(r0) + 0j)
    r, s = track(pair, path)
    p = tuple(int(np.argmin(np.abs(r0 - x))) for x in r)
    sg = tuple(1 if abs(s[k] - s0[j]) < abs(s[k] + s0[j]) else -1 for k, j in enumerate(p))
    return p, sg


def lasso(base, c, rad=0.12):
    return [base, c + rad] + [c + rad * np.exp(1j * t) for t in np.linspace(0, 2 * np.pi, 25)] + [c + rad, base]


# ---------------------------------------------------------------- C1
rf = make_roots(-1.0)
base = 0.0 + 0.35j
bp = 2 / (3 * np.sqrt(3))
gp = element(rf, base, lasso(base, bp))
gm = element(rf, base, lasso(base, -bp))
big = [base] + [2.0 * np.exp(1j * t) for t in np.linspace(np.angle(base), np.angle(base) + 2 * np.pi, 60)] + [base]
gi = element(rf, base, big)
ctl = element(rf, base, [base] + [base + 0.05 * np.exp(1j * t) for t in np.linspace(0, 2 * np.pi, 40)] + [base])

print(f"\n  C1  gamma_+   root permutation {gp[0]}   signs {gp[1]}")
print(f"      gamma_-   root permutation {gm[0]}   signs {gm[1]}")
print(f"      gamma_inf root permutation {gi[0]}   signs {gi[1]}")
print(f"      control (encloses nothing) {ctl[0]}   signs {ctl[1]}")
assert ctl[0] == (0, 1, 2) and ctl[1] == (1, 1, 1), "a null loop must return the identity"


def cyc_type(p):
    seen, t = set(), []
    for i in range(3):
        if i in seen:
            continue
        c, j = 0, i
        while j not in seen:
            seen.add(j); j = p[j]; c += 1
        t.append(c)
    return tuple(sorted(t))


assert cyc_type(gp[0]) == (1, 2), "gamma_+ must be a transposition"
assert cyc_type(gm[0]) == (1, 2), "gamma_- must be a transposition"
assert gp[0] != gm[0], "and they must transpose DIFFERENT pairs -- P05's stated condition"
assert cyc_type(gi[0]) == (3,), "gamma_inf must be a 3-cycle"
print("  ** VERDICT C1: two transpositions of DIFFERENT pairs and a 3-cycle at infinity;")
print("     the null loop returns the identity.  This is what supplies P05's condition that")
print("     'two transpositions generate S_3 only if they differ'. **")

# ---------------------------------------------------------------- C2
ID = ((0, 1, 2), (1, 1, 1))


def mul(a, b):
    pa, sa = a; pb, sb = b
    return tuple(pa[pb[i]] for i in range(3)), tuple(sa[pb[i]] * sb[i] for i in range(3))


def generate(gens):
    G, frontier = {ID}, [ID]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = mul(g, x)
                if y not in G:
                    G.add(y); nxt.append(y)
        frontier = nxt
    return G


G = generate([gp, gm])
kern = {s for p, s in G if p == (0, 1, 2)}


def order(x):
    y, n = x, 1
    while y != ID:
        y = mul(x, y); n += 1
    return n


prof = dict(sorted(Counter(order(x) for x in G).items()))
print(f"\n  C2  |G| = {len(G)}   root image {len({p for p,_ in G})}   kernel {len(kern)}")
print(f"      kernel = {sorted(kern)}")
print(f"      element-order profile = {prof}")
assert len(G) == 24 and len({p for p, _ in G}) == 6 and len(kern) == 4
assert kern == {(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)}, "must be P05's Klein four-group"
assert prof == {1: 1, 2: 9, 3: 8, 4: 6}, "must be S_4's profile"
print("  ** VERDICT C2: order 24, root image S_3, kernel exactly P05's Klein four-group,")
print("     and the profile is S_4's and no other order-24 group's. **")

# ---------------------------------------------------------------- C3
print("\n  C3  Weyl group orders:")
for n in range(2, 7):
    A, B, D = math.factorial(n + 1), 2**n * math.factorial(n), 2**(n - 1) * math.factorial(n)
    print(f"      rank {n}: |W(A_{n})|={A:<8} |W(B_{n})|={B:<8} |W(D_{n})|={D:<8}"
          f"{'   <-- 24' if 24 in (A, B, D) else ''}")
    if n != 3:
        assert 24 not in (A, B, D), f"only rank 3 may hit 24 (rank {n} did)"
assert 24 not in (12, 1152, 51840, 2903040, 696729600), "no exceptional is 24"
print("      exceptionals: 12, 1152, 51840, 2903040, 696729600  -- none is 24")
print("  ** VERDICT C3: 24 selects W(A_3) = W(D_3) and nothing else, and those coincide")
print("     because so(6,C) = sl(4,C).  A RANK-THREE fact. **")

# ---------------------------------------------------------------- genericity
print("\n  and the bake's bite: the group is GENERIC to depressed cubic families")
print("      (for r^3 + p r + q the discriminant vanishes at q = +/- 2 (-p/3)^{3/2},")
print("       which is IMAGINARY when p > 0 -- the branch points leave the real axis")
print("       but the monodromy group does not change.)")
for p_, lbl in [(-1.0, "r^3 - r + q   (the horizon cubic)"), (-4.0, "r^3 - 4r + q"),
                (1.0, "r^3 + r + q   (no real merger)"), (-7.0, "r^3 - 7r + q")]:
    pair = make_roots(p_)
    q_b = 2 * ((-p_ / 3.0) + 0j) ** 1.5          # complex-safe
    b2 = 0.0 + (abs(q_b) * 0.9 + 0.3) * 1j
    rad = max(0.08, 0.15 * abs(q_b))
    g1 = element(pair, b2, lasso(b2, q_b, rad))
    g2 = element(pair, b2, lasso(b2, -q_b, rad))
    n = len(generate([g1, g2]))
    print(f"      {lbl:34s} branch points +/-{q_b:.4f}   |G| = {n}")
    assert n == 24, f"every depressed cubic family must give 24 (got {n} for {lbl})"
print("  ** So the Klein four-group is FORCED BY THE CUBIC.  'Substrate-derived rather than")
print("     assumed' is sound about the derivation and misplaces the surprise: what is NOT")
print("     forced is that the substrate's Weyl group is the same group. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
