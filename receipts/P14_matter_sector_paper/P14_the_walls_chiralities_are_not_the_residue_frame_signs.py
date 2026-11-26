"""The walls' chiralities and the residue frame's signs are different objects.

P14 (Proposition prop:wall): each wall's chirality is a definite sigma_y eigenvalue whose sign is the sign of
the signed-radius flip, and R = gamma^5 is the orientation parity, which sends 2M -> -2M and reverses every
signed radius at once.  P14 (sec:family): a root transposition does not flip chirality -- the hinge S_3 sits
in D_6 as S_3 x 1, not as the twisted graph {(sigma, sgn sigma)}.  So the group acting on the three walls'
chiralities is D_6 = S_3 x <-I>.

The residue frame e_i/sqrt(f'(r_i)) of the horizon cubic, carried around the Nariai points (P12), closes the
cube rotation group O, in which every odd permutation carries an odd number of sign reversals.

Checked:
  1. In the realised frame holonomy O, no element is a bare transposition, and every element whose
     permutation is a transposition reverses exactly one or all three signs: O does not contain S_3 x 1.
     So the frame's signs cannot be the walls' chiralities without contradicting S_3 x 1.
  2. Read as chirality signs, O would carry the uniform (+,+,+) to mixed configurations; D_6 carries it only
     to (+,+,+) and (-,-,-).  Under D_6, dim ker_- is 0 or 3, never 1 or 2.
  3. A loop in the mass plane is closed: it returns to the same real 2M, hence the same geometry and the same
     signed-radius flips.  The chirality, a property of that geometry, is returned unchanged; the frame's
     sign is a branch of sqrt(f'(r_i)) along the loop and can change.  Checked here on the transported
     loop: the roots return as a set to their starting values while the frame entries change sign.

COMPUTES: the horizon cubic r^3 - r + 2M at alpha = 1; loops of radius 0.15 about each Nariai point from
2M = 0.1; group closure on signed permutations; orbits of (+,+,+) under O and under D_6.
"""
import itertools
import numpy as np

cN = 2 / (3 * np.sqrt(3))
c0 = 0.1

def roots(c):
    return np.roots([1, 0, -1, c])

def follow(prev, new):
    best = min(itertools.permutations(range(3)),
               key=lambda p: sum(abs(prev[i] - new[p[i]]) for i in range(3)))
    return np.array([new[best[i]] for i in range(3)])

def transport(center, rad=0.15, n=6000):
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
    return M, r0, r

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

def perm_and_signs(m):
    perm = tuple(int(np.argmax(abs(m[:, i]))) for i in range(3))
    signs = tuple(int(round(m[perm[i], i])) for i in range(3))
    return perm, signs

def parity(p):
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])
    return inv % 2

A, r0, rA = transport(cN)
B, _, _ = transport(-cN)
O = close([A, B])
assert len(O) == 24

# 1. no bare transposition; odd permutations carry an odd number of reversals
odd = [perm_and_signs(m) for m in O if parity(perm_and_signs(m)[0]) == 1]
assert len(odd) == 12
assert all(sum(1 for s in sg if s < 0) in (1, 3) for _, sg in odd)
bare_transpositions = [m for m in O if (m >= 0).all() and parity(perm_and_signs(m)[0]) == 1]
assert bare_transpositions == []
print("frame holonomy: 12 odd elements, each with 1 or 3 sign reversals; bare transpositions: 0")

# 2. orbits of the uniform configuration
plus = np.ones(3)
orbit_O = {tuple(int(x) for x in m @ plus) for m in O}
C3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)
T = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], float)
D6 = close([C3, T, -np.eye(3)])
assert len(D6) == 12
orbit_D6 = {tuple(int(x) for x in m @ plus) for m in D6}
print("orbit of (+,+,+) under O:", sorted(orbit_O))
print("orbit of (+,+,+) under D_6:", sorted(orbit_D6))
assert orbit_D6 == {(1, 1, 1), (-1, -1, -1)}
assert orbit_O == set(itertools.product((-1, 1), repeat=3))
assert {sum(1 for x in o if x < 0) for o in orbit_D6} == {0, 3}

# 3. the loop is closed on the geometry: the roots return as a set, the frame does not return as itself
assert np.allclose(np.sort(rA.real), np.sort(r0.real)) and np.allclose(rA.imag, 0, atol=1e-9)
assert not np.allclose(A, np.eye(3))
print("loop about +cN returns the root set to itself; frame returns as", A.astype(int).tolist())
assert np.array_equal(A, [[1, 0, 0], [0, 0, -1], [0, 1, 0]])
print("ALL PASS")
