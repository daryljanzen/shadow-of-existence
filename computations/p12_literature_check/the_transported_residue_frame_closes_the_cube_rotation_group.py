"""The Schwarzschild-de Sitter horizon cubic P(r) = r^3 - r + c (alpha = 1, c = 2M) and the residue
pairing on functions over its three roots, diag(1/P'(r_i)).

What this computes.  The frame e_i / sqrt(P'(r_i)) that makes the pairing the identity is carried by
analytic continuation around loops in the complex c-plane about the two Nariai points c = +-2/(3 sqrt 3)
(the double roots).  Each loop returns the frame to itself up to a signed permutation; the group those
loops generate is computed directly rather than assumed from generators.

Results (asserted below):
  1. A loop about one Nariai point swaps the two merging roots and flips ONE sign: a four-fold rotation
     (order 4, det +1).  Its square is a pure sign change of two entries.  The quarter turn is the
     surface gravity vanishing like a square root at the Nariai point, so 1/sqrt(P') has a quarter-power
     branch there.
  2. The group the two loops generate has order 24 and every element is proper (det +1): profile
     1 identity, 9 half-turns, 8 three-fold, 6 four-fold rotations.  That is the rotation group O of the
     cube, isomorphic to S_4 = W(A_3), realised in the sign-twisted representation (signed permutations
     whose sign product equals the permutation's sign), NOT the reflection (Weyl) embedding T_d.
  3. Its elements with trivial permutation part are exactly the Klein four-group of even sign changes.
     No bare transposition is realised; the odd permutations come with an odd number of sign changes,
     so the uniform configuration (+,+,+) reaches (-,-,-).
  4. Adjoining the central inversion -I gives order 48, the full signed-permutation group O_h = W(B_3).
  5. Control: bare permutations plus even sign changes (the generators previously assumed) close T_d,
     with all six order-4 elements improper -- the test separates the two embeddings.
  6. Residue identities (Euler-Jacobi): sum 1/P'(r_i) = 0 and sum r_i/P'(r_i) = 0; since
     f'(r_i) = -P'(r_i)/r_i for f = 1 - 2M/r - r^2, the second is the vanishing sum of inverse
     surface gravities over all three horizons (cf. arXiv:2407.13079).
"""
import itertools
from collections import Counter
import numpy as np

cN = 2 / (3 * np.sqrt(3))

def roots(c):
    return np.roots([1, 0, -1, c])

def follow(prev, new):
    best = min(itertools.permutations(range(3)),
               key=lambda p: sum(abs(prev[i] - new[p[i]]) for i in range(3)))
    return np.array([new[best[i]] for i in range(3)])

def transport(center, c0=0.1, rad=0.15, n=6000):
    r0 = np.sort(roots(c0).real).astype(complex)
    a = center - rad * np.sign(center - c0)
    th0 = np.angle(a - center)
    path = list(np.linspace(c0, a, n))
    path += [center + rad * np.exp(1j * (th0 + t)) for t in np.linspace(0, 2 * np.pi, 4 * n)]
    path += list(np.linspace(a, c0, n))
    r = r0.copy()
    s = np.sqrt(1 / (3 * r**2 - 1) + 0j)
    for c in path:
        rn = follow(r, roots(c))
        sn = np.sqrt(1 / (3 * rn**2 - 1) + 0j)
        sn = np.where(abs(sn - s) < abs(sn + s), sn, -sn)
        r, s = rn, sn
    s0 = np.sqrt(1 / (3 * r0**2 - 1) + 0j)
    M = np.zeros((3, 3))
    for i in range(3):
        j = int(np.argmin(abs(r0 - r[i])))
        M[j, i] = np.real(s[i] / s0[j]).round(6)
    return M

def close(gens):
    key = lambda m: tuple(np.round(m, 6).flatten())
    G = {key(np.eye(3)): np.eye(3)}
    fr = [np.eye(3)]
    while fr:
        nf = []
        for g in fr:
            for h in gens:
                k = g @ h
                if key(k) not in G:
                    G[key(k)] = k
                    nf.append(k)
        fr = nf
    return list(G.values())

def order(m):
    p = m.copy()
    for k in range(1, 13):
        if np.allclose(p, np.eye(3)):
            return k
        p = p @ m
    return None

def profile(G):
    return Counter((order(m), int(round(np.linalg.det(m)))) for m in G)

A, B = transport(cN), transport(-cN)
print("loop about c = +cN:\n", A, "\nloop about c = -cN:\n", B)

# 1. each loop is a four-fold rotation whose square is a pure even sign change
for L in (A, B):
    assert order(L) == 4 and round(np.linalg.det(L)) == 1
    L2 = L @ L
    assert np.allclose(abs(L2), np.eye(3)) and sorted(np.diag(L2)) == [-1, -1, 1]

# 2. the realised group: order 24, all proper, the chiral octahedral profile
G = close([A, B])
prof = profile(G)
print("order", len(G), "profile (order, det):", dict(sorted(prof.items())))
assert len(G) == 24
assert dict(prof) == {(1, 1): 1, (2, 1): 9, (3, 1): 8, (4, 1): 6}

# 3. kernel of the permutation map is V_4; no bare transposition; (+,+,+) reaches (-,-,-)
pure = [m for m in G if np.allclose(abs(m), np.eye(3))]
assert len(pure) == 4 and all(round(np.prod(np.diag(m))) == 1 for m in pure)
bare = [m for m in G if (m >= 0).all()]
assert len(bare) == 3  # identity and the two three-cycles only
assert any(np.allclose(m @ np.ones(3), -np.ones(3)) for m in G)

# 4. with the central inversion: order 48, all signed permutations
G48 = close([A, B, -np.eye(3)])
assert len(G48) == 48

# 5. control: the assumed generators (bare permutations + even sign changes) give T_d instead
C3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)
T = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], float)
Td = close([C3, T, np.diag([1., -1, -1]), np.diag([-1., 1, -1])])
assert len(Td) == 24 and profile(Td)[(4, -1)] == 6 and profile(Td)[(4, 1)] == 0
print("control (assumed generators):", dict(sorted(profile(Td).items())))

# 6. Euler-Jacobi residue identities = vanishing sum of inverse surface gravities
for c in (0.1, 0.3, -0.25):
    r = roots(c)
    Pp = 3 * r**2 - 1
    assert abs(np.sum(1 / Pp)) < 1e-12 and abs(np.sum(r / Pp)) < 1e-12
    fprime = -Pp / r
    assert abs(np.sum(1 / fprime)) < 1e-12
print("ALL PASS")
