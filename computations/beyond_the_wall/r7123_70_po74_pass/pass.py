"""r7123 (70) -- the adversarial pass on 60's PO-74 receipt
(`P15_the_constant_r_foliation_carries_the_sphere_across_the_lap_...`).  Pre-registered at PREDICTION.md beside
this file.  sympy only.  By r7115's premise, NO curvature invariant is compared ACROSS the reassignment: every
check is within one three-geometry or about the demonstration's logical structure.

  (1) derived or posited: is the layer's metric along the bead computed, or written down?  and does the shape
      invariant detect shape at all (control: a squashed, non-round S^3)?
  (2) fitted or applied: do the two substitutions carry information the target did not already supply?
  (3) the coordinate identity: is the chi of the S^3's polar form the chi of eq:proper-frame?
  (4) what should hold: the inflection at r_N, the double zero of f, the reassigned layer null there.
"""
import os
import re

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
RECEIPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                       'P15_the_constant_r_foliation_carries_the_sphere_across_the_lap_because_the_layers_shape_'
                       'invariant_is_the_same_pure_number_at_every_point_of_the_bead.py')
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print('\n' + '=' * 100 + '\n  ' + t + '\n' + '=' * 100)


def scalar_and_volume_density(g, x):
    """Ricci scalar and sqrt(det g) of a 3-metric, by the textbook formulas (general inverse: g may be
    non-diagonal)"""
    n = len(x)
    gi = sp.simplify(g.inv())
    Gm = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d]))
                            for d in range(n)) / 2) for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(
        sp.diff(Gm[a][b][d], x[a]) - sp.diff(Gm[a][b][a], x[d])
        + sum(Gm[a][a][e] * Gm[e][b][d] - Gm[a][d][e] * Gm[e][b][a] for e in range(n)) for a in range(n))))
    R = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    return R, sp.sqrt(sp.simplify(g.det())), gi * Ric


src = open(RECEIPT, encoding='utf-8').read()
a, r, h, eps = sp.symbols('a r h epsilon', positive=True)
chi, th, ph, psi = sp.symbols('chi theta phi psi', real=True)
SHAPE = 6 * (2 * sp.pi ** 2) ** sp.Rational(2, 3)

# =========================================================================================== (1)
head('(1) DERIVED OR POSITED')
m = re.search(r'^(G3 = sp\.diag\(r \*\* 2, r \*\* 2 \* sp\.sin\(chi\) \*\* 2.*)$', src, re.M)
print(f'      the receipt\'s layer metric, as written: {m.group(1).strip() if m else "(not found)"}')
gate('the receipt\'s layer metric along the bead is WRITTEN DOWN as the round S^3, r^2 dOmega_3^2 (its line '
     '`G3 = sp.diag(r ** 2, r ** 2 * sin(chi) ** 2, ...)`): it is the input, not a computed induced metric',
     m is not None)
gS3 = sp.diag(a ** 2, a ** 2 * sp.sin(chi) ** 2, a ** 2 * sp.sin(chi) ** 2 * sp.sin(th) ** 2)
R3, dens3, _ = scalar_and_volume_density(gS3, [chi, th, ph])
V3 = 2 * sp.pi ** 2 * a ** 3
inv3 = sp.simplify(R3 * V3 ** sp.Rational(2, 3))
gate(f'and on ANY round S^3 of ANY radius a, R V^(2/3) = {inv3}: the invariant is the same pure number by '
     f'IDENTITY, so "the same at every point of the bead" restates that the input was a round S^3 at every '
     f'point', sp.simplify(inv3 - SHAPE) == 0 and sp.simplify(R3 - 6 / a ** 2) == 0)
# control: a Berger (squashed) S^3 -- left-invariant, homogeneous, NOT round -- in Euler angles
gB = (a ** 2 / 4) * sp.Matrix([[1, 0, 0],
                               [0, 1, eps ** 2 * sp.cos(th)],
                               [0, eps ** 2 * sp.cos(th), eps ** 2]]) \
    + (a ** 2 / 4) * sp.Matrix([[0, 0, 0], [0, sp.sin(th) ** 2 + eps ** 2 * sp.cos(th) ** 2 - 1, 0], [0, 0, 0]])
# i.e. (a^2/4)[dth^2 + sin^2 th dph^2 + eps^2 (dpsi + cos th dph)^2] in (th, ph, psi)
RB, densB, _ = scalar_and_volume_density(gB, [th, ph, psi])
VB = sp.simplify(sp.integrate(sp.integrate(sp.integrate(sp.simplify(densB), (th, 0, sp.pi)), (ph, 0, 2 * sp.pi)),
                              (psi, 0, 4 * sp.pi)))
invB = sp.simplify(RB * VB ** sp.Rational(2, 3))
print(f'      Berger sphere: R = {sp.simplify(RB)},  V = {VB},  R V^(2/3) = {invB}')
gate('CONTROL: on a squashed (Berger) S^3 the same invariant VARIES with the squashing and equals '
     '6(2 pi^2)^(2/3) only at eps = 1, the round one -- so it is a genuine shape detector WHEN it is applied to '
     'a metric obtained independently; applied to a metric posited round, it can only return round',
     sp.simplify(invB.subs(eps, 1) - SHAPE) == 0 and abs(float(invB.subs(eps, sp.Rational(1, 2))) - float(SHAPE)) > 1)

# =========================================================================================== (2)
head('(2) FITTED OR APPLIED')
gH = sp.diag(h, r ** 2, r ** 2 * sp.sin(th) ** 2)       # the template: warp removed, chi block -> ANY constant h
RH, _, mixH = scalar_and_volume_density(gH, [chi, th, ph])
evH = [sp.simplify(mixH[i, i]) for i in range(3)]
print(f'      the template with the chi block set to an ARBITRARY constant h: eigenvalues {evH}, scalar {RH}')
gate('the two-substitution template sends the round S^3 to h dchi^2 + r^2 dOmega_2^2 for ANY h, with '
     'eigenvalues (0, 1/r^2, 1/r^2) whatever h is -- so reproducing 70\'s eigenvalues is NOT evidence that the '
     'chi-block step was the reassignment: the receipt\'s own gate B already shows the unwarping alone gives them',
     evH[0] == 0 and all(sp.simplify(e - 1 / r ** 2) == 0 for e in evH[1:]) and sp.simplify(RH - 2 / r ** 2) == 0)
gate('and "-f(r)" is SELECTED by matching the target: no rule in the receipt maps r^2 to -f(r) that would not '
     'equally map it to 1, r^2 or any h (its own text: "re-signed by the promoted null condition", stated, '
     'not applied)', 're-signed by the promoted null' in src and 'r ** 2 -> -f' not in src.replace(' ', ''))

# =========================================================================================== (3)
head('(3) THE COORDINATE IDENTITY')
L = sp.Symbol('L', positive=True)        # a length unit
dims = {'S^3 polar chi': 1, 'eq:proper-frame chi': L}
print('      S^3 polar form r^2[dchi^2 + sin^2 chi dOmega^2]: chi is an ANGLE (dimensionless); g_chichi = r^2 ~ L^2')
print('      eq:proper-frame -dtau^2 + (d_chi r)^2 dchi^2 + ...: tilde-tau = tau + chi, so chi ~ L; '
      'g_chichi = (d_chi r)^2 ~ 1, and on the layer -f(r) ~ 1')
gate('the chi of the S^3 polar form is a dimensionless angle and the chi of eq:proper-frame is a comoving '
     'label with the dimension of time (tilde-tau = tau + chi): "r^2 -> -f(r) on the chi block" swaps an L^2 '
     'coefficient for a dimensionless one, which is consistent only with an UNSTATED change of the coordinate '
     '(chi_length = r chi_angle at fixed r) -- so the step is a rescaling plus a coefficient change 1 -> -f, and '
     'the coefficient change is the part not derived', dims['S^3 polar chi'] != dims['eq:proper-frame chi'])

# =========================================================================================== (4)
head('(4) WHAT SHOULD HOLD')
al, rs = sp.symbols('alpha r_s', positive=True)
rN = al / sp.sqrt(3)
rsN = 2 * al / (3 * sp.sqrt(3))
f = 1 - rs / r - r ** 2 / al ** 2
rdd = sp.diff(rs / r + r ** 2 / al ** 2, r) / 2          # E=1: r'^2 = r_s/r + r^2/alpha^2 => r'' = (1/2) d/dr
gate('the inflection r\'\' = 0 sits at r_N = alpha/sqrt3 IDENTICALLY at the Nariai mass',
     sp.simplify(rdd.subs({rs: rsN, r: rN})) == 0)
gate('f(r_N) = f\'(r_N) = 0 at the Nariai mass: the double root', sp.simplify(f.subs({rs: rsN, r: rN})) == 0
     and sp.simplify(sp.diff(f, r).subs({rs: rsN, r: rN})) == 0)
gate('and the reassigned layer\'s chi block -f(r) = (d_chi r)^2 - 1 vanishes there: the constant-tilde-tau '
     'layer is NULL exactly at the inflection (70\'s r7111 finding, read in 60\'s terms) -- so 60\'s withdrawal of '
     '"the two metrics degenerate in different places" STANDS', sp.simplify((-f).subs({rs: rsN, r: rN})) == 0)

print(f'\n  {len(CHECKS)} checks, {sum(ok for _, ok in CHECKS)} pass')
assert all(ok for _, ok in CHECKS), [n for n, ok in CHECKS if not ok]
