"""The level below the substrate's: general relativity's own de Sitter spacetime, isometry so(4,1).

At a slice of global de Sitter the Killing data split so(4,1) = so(4) + m4, with so(4) the slice's own
isometries (tangential deformations) and m4 the four boosts normal to it (normal deformations).
Checked on explicit matrices:
  1. the split is direct, dimensions 6 + 4 = 10;
  2. [so(4), so(4)] in so(4), [so(4), m4] in m4, [m4, m4] in so(4): a symmetric pair, so two normal
     deformations bracket into a tangential one, the same shape as the substrate's so(5,1)/so(4,1);
  3. the Killing form restricted to m4 is DEFINITE (all four eigenvalues of one sign);
  4. the substrate's coset so(5,1)/so(4,1) has a Killing form on its m of signature (1,4), indefinite.
So the indefinite coset metric belongs to the substrate's level, not to the level below.
"""
import itertools
import numpy as np

def gens(eta):
    n = len(eta)
    E = {}
    for m, v in itertools.combinations(range(n), 2):
        M = np.zeros((n, n))
        for r in range(n):
            for s in range(n):
                M[r, s] = (r == m) * eta[v] * (v == s) - (r == v) * eta[m] * (m == s)
        E[(m, v)] = M
    return E

def in_span(X, basis):
    A = np.array([b.flatten() for b in basis]).T
    c = np.linalg.lstsq(A, X.flatten(), rcond=None)[0]
    return np.allclose(A @ c, X.flatten(), atol=1e-12)

def check(eta, normal):
    E = gens(eta)
    h = [M for (a, b), M in E.items() if normal not in (a, b)]
    m = [M for (a, b), M in E.items() if normal in (a, b)]
    allg = h + m
    assert np.linalg.matrix_rank(np.array([g.flatten() for g in allg])) == len(allg)
    for X, Y in itertools.product(h, h):
        assert in_span(X @ Y - Y @ X, h)
    for X, Y in itertools.product(h, m):
        assert in_span(X @ Y - Y @ X, m)
    for X, Y in itertools.product(m, m):
        assert in_span(X @ Y - Y @ X, h)
    n = len(allg)
    def ad(X):
        cols = []
        A = np.array([g.flatten() for g in allg]).T
        for Y in allg:
            Z = X @ Y - Y @ X
            cols.append(np.linalg.lstsq(A, Z.flatten(), rcond=None)[0])
        return np.array(cols).T
    K = np.array([[np.trace(ad(X) @ ad(Y)) for Y in m] for X in m])
    ev = np.linalg.eigvalsh(K)
    return len(h), len(m), int((ev > 1e-9).sum()), int((ev < -1e-9).sum())

# level below: so(4,1) on M^5 with eta = diag(-1,1,1,1,1); the slice's normal is the time direction 0
below = check([-1, 1, 1, 1, 1], normal=0)
print("so(4,1) = so(4) + m4:", below[:2], " Killing form on m4 (+,-):", below[2:])
assert below == (6, 4, 4, 0)

# the substrate: so(5,1) on M^6 with eta = diag(-1,1,1,1,1,1); the cut-normal direction is 5
sub = check([-1, 1, 1, 1, 1, 1], normal=5)
print("so(5,1) = so(4,1) + m :", sub[:2], " Killing form on m (+,-):", sub[2:])
assert sub == (10, 5, 1, 4)
print("ALL PASS")
