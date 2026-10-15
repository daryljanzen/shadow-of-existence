#!/usr/bin/env python3
"""gen_ef_tables.py -- campaign 15 (r7367+71.4/5): the literal tables for the ingoing Eddington-Finkelstein chart
  G = -F(r) dv^2 + 2 dv dr + P(r) (dth^2 + S(th) dph^2),   coordinates (v, r, th, ph) = indices 0..3,
at a point, with P = r^2 and S = sin^2 th near it.  Point values: F0, F1, F2 (F, F', F''), r, s = sin th, c = cos th.

Every table printed here is CHECKED entry by entry in Lean (probes/NonDiag.lean, section EFNariai) against the metric;
a wrong entry does not compile.  This script is the generator, committed with the measurement (cc66, r7365).

Conventions match the engine: Gam[i][j][k] = Gamma^k_ij;  R[i][j][k][l] = (R(e_i, e_j) e_k)^l
  = d_i Gam^l_jk - d_j Gam^l_ik + sum_m (Gam^m_jk Gam^l_im - Gam^m_ik Gam^l_jm);
RU[a][b][c][d] = R_a^{bcd} = sum_e G_ae sum_fgh Gi^bf Gi^cg Gi^dh R[f][g][h][e];
K = sum_abcd R[b][c][d][a] * RU[a][b][c][d]."""
import sympy as sp

v, r, th, ph = sp.symbols('v r theta phi')
X = [v, r, th, ph]
Ff = sp.Function('F')
F0, F1, F2, F3, s, c = sp.symbols('F0 F1 F2 F3 s c')
G = sp.zeros(4, 4)
G[0, 0] = -Ff(r); G[0, 1] = G[1, 0] = 1; G[2, 2] = r**2; G[3, 3] = r**2 * sp.sin(th)**2
Gi = G.inv()


def pt(e):
    e = e.subs(sp.Derivative(Ff(r), (r, 3)), F3).subs(sp.Derivative(Ff(r), (r, 2)), F2)
    e = e.subs(sp.Derivative(Ff(r), r), F1).subs(Ff(r), F0)
    e = e.subs(sp.sin(th), s).subs(sp.cos(th), c)
    return sp.factor(sp.cancel(e))


Gam = [[[sp.cancel(sum(Gi[k, l] * (sp.diff(G[j, l], X[i]) + sp.diff(G[l, i], X[j]) - sp.diff(G[i, j], X[l])) / 2
                         for l in range(4))) for k in range(4)] for j in range(4)] for i in range(4)]
R = [[[[sp.cancel(sp.diff(Gam[j][k][l], X[i]) - sp.diff(Gam[i][k][l], X[j])
                    + sum(Gam[j][k][m] * Gam[i][m][l] - Gam[i][k][m] * Gam[j][m][l] for m in range(4)))
        for l in range(4)] for k in range(4)] for j in range(4)] for i in range(4)]
RU = [[[[sp.cancel(sum(G[a, e] * Gi[b, f] * Gi[cc, g] * Gi[d, h] * R[f][g][h][e]
                         for e in range(4) for f in range(4) for g in range(4) for h in range(4)))
         for d in range(4)] for cc in range(4)] for b in range(4)] for a in range(4)]
K = sp.cancel(sum(R[b][cc][d][a] * RU[a][b][cc][d] for a in range(4) for b in range(4) for cc in range(4)
                    for d in range(4)))
Kc = Ff(r).diff(r, 2)**2 + 4 * Ff(r).diff(r)**2 / r**2 + 4 * (1 - Ff(r))**2 / r**4
assert sp.simplify(K - Kc) == 0, K
# ⌗ no trig simplification anywhere in the tables: sin, cos are only differentiated, never reduced by s^2 + c^2 = 1,
#   which is the same algebra Lean's check runs, so every entry closes by field_simp/ring alone


def lean(e):
    t = sp.sstr(pt(e)).replace('**', '^')
    return '(' + t + ')'


def nest(f, dims):
    if not dims:
        return lean(f(()))
    return '![' + ', '.join(nest(lambda rest, i=i: f((i,) + rest), dims[1:]) for i in range(dims[0])) + ']'


D1 = lambda ix: sp.diff(G[ix[0], ix[1]], X[ix[2]])
D2 = lambda ix: sp.diff(G[ix[0], ix[1]], X[ix[2]], X[ix[3]])
print('-- Gi'); print(nest(lambda ix: Gi[ix[0], ix[1]], [4, 4]))
print('-- D1'); print(nest(D1, [4, 4, 4]))
print('-- D2'); print(nest(D2, [4, 4, 4, 4]))
print('-- Gam'); print(nest(lambda ix: Gam[ix[0]][ix[1]][ix[2]], [4, 4, 4]))
print('-- R'); print(nest(lambda ix: R[ix[0]][ix[1]][ix[2]][ix[3]], [4, 4, 4, 4]))
print('-- RU'); print(nest(lambda ix: RU[ix[0]][ix[1]][ix[2]][ix[3]], [4, 4, 4, 4]))
print('-- K =', pt(K))
print('-- K closed form (simplified, s^2 + c^2 = 1 used):', pt(sp.simplify(K)))
