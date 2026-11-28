"""P3 sec:slicing / sec:hinge-geometry -- THE THREE HORIZON ROOTS ARE THE OFFSETS OF THREE PARALLEL PLANES,
ONE THROUGH EACH HINGE.

The equatorial section (gauge alpha = 1): the throat is the unit circle about the axis O, and the three hinges
stand at transverse distance 2, 120 degrees apart, H_k = 2 (cos 2 pi k/3, sin 2 pi k/3), H_0 being the hinge
whose plane swings.  The cut is the plane through H_0 at swing angle w measured from the line H_0 -> O, the
plane swinging toward +X_2 (the section viewed from the north pole); its unit normal is n = (sin w, cos w) and
its signed offset from the axis is d_0 = n . H_0 = 2 sin w.  The parallel planes through the other two hinges
have offsets d_k = n . H_k.  Claims checked:

  (1) d_k = 2 sin(w + 2 pi k / 3), and the three values d_k / sqrt3 are EXACTLY the three roots of the horizon
      cubic x^3 - x + 2M = 0 at 2M = x_0 - x_0^3, x_0 = d_0/sqrt3 = (2/sqrt3) sin w (symbolic, every w).
  (2) the offsets sum to zero (the depressed cubic's vanishing trace), because the hinges sit symmetrically about
      the axis.
  (3) at every swing angle away from the six Nariai marks exactly one of the three planes cuts the throat
      (|d| < 1), and it is the plane carrying the root of least magnitude; at w = pi/6 two planes have offset 1 and are ONE line, the
      side H_0 H_1 of the hinge triangle, tangent to the throat at its midpoint, and the third is the parallel
      through H_2 at offset -2, the lone root -2/sqrt3; at w = 0 the offsets are 0 and -+sqrt3, the roots 0
      and -+1.
  (4) the two points where the cutting plane crosses the throat do NOT carry the horizon values: on the throat
      the signed areal radius of the point at angle u from the back point (-1, 0) is sin u (its distance from
      the back--hinge axis, which is the areal radius in the de Sitter static frame centred at the back point),
      and across the undercritical arc the crossing points' values meet a horizon value only at three isolated
      angles, each a transversal crossing of two different functions of w, the far crossing point's equalling
      the black-hole root only at w = 0, where it is the back point.
  (5) reversing the common normal, n -> -n, leaves every plane in place and negates every offset (the
      mass-reflection R, 2M -> -2M); reflecting the swing in the hinge's own axis, w -> -w, carries the
      tangent from the hinge at +30 degrees to the one at -30 degrees (the two rulings through it) and negates
      the root triple; relabelling the hinges permutes the offsets; negation commutes with every relabelling,
      so the symmetry generated on the root triples is a direct product S_3 x Z_2.

COMPUTES: scope.
  * `alpha = 1` sets the unit of length (gauge); offsets, roots and areal radii are in units of alpha.
  * the hinge distance 2 is P3's forced placement (prop:twoalpha), not a free choice here; the sweep in (3) is
    12001 swing angles over the full turn, in (4) 4001 on the undercritical arc; the identity in (1) holds at
    every w.
"""
import itertools
import numpy as np
import sympy as sp

w = sp.symbols('w', real=True)
n = sp.Matrix([sp.sin(w), sp.cos(w)])
H = [2*sp.Matrix([sp.cos(2*sp.pi*k/3), sp.sin(2*sp.pi*k/3)]) for k in range(3)]
d = [sp.simplify((n.T*h)[0]) for h in H]

# (1) closed form and the roots of the cubic
for k in range(3):
    assert sp.simplify(sp.expand_trig(d[k] - 2*sp.sin(w + 2*sp.pi*k/3))) == 0, k
x0 = d[0]/sp.sqrt(3)
twoM = x0 - x0**3
for k in range(3):
    xk = d[k]/sp.sqrt(3)
    assert sp.simplify(sp.expand_trig(sp.expand(xk**3 - xk + twoM))) == 0, f"offset {k} is not a root"
print("(1) d_k = 2 sin(w + 2 pi k/3); each d_k/sqrt3 is a root of x^3 - x + 2M at 2M = x0 - x0^3     OK")

# (2) the trace vanishes
assert sp.simplify(sp.expand_trig(sum(d))) == 0
print("(2) the three offsets sum to zero                                                          OK")

# (3) which plane cuts the throat
fd = sp.lambdify(w, d, 'numpy')
nariai = np.pi/6 + np.arange(6)*np.pi/3
for wv in np.linspace(0, 2*np.pi, 12001):
    if np.min(np.abs((wv - nariai + np.pi) % (2*np.pi) - np.pi)) < 1e-3:
        continue
    dv = np.array(fd(wv), dtype=float)
    cutting = np.where(np.abs(dv) < 1)[0]
    assert len(cutting) == 1, (wv, dv)
    assert cutting[0] == np.argmin(np.abs(dv)), (wv, dv)
dN = np.array(fd(np.pi/6), dtype=float)
assert np.allclose(sorted(dN), [-2, 1, 1]) and np.isclose(dN[0], 1) and np.isclose(dN[1], 1)
# at Nariai the planes through H0 and H1 are one line: H1 lies on the plane through H0
Hn = [np.array([float(c) for c in h]) for h in H]
nN = np.array([np.sin(np.pi/6), np.cos(np.pi/6)])
assert np.isclose(nN @ (Hn[1] - Hn[0]), 0.0)
tN = (Hn[0] + Hn[1])/2                       # the side's midpoint is the tangency point
assert np.isclose(np.linalg.norm(tN), 1.0)
d0 = np.array(fd(0.0), dtype=float)
assert np.allclose(sorted(d0), [-np.sqrt(3), 0, np.sqrt(3)])
print("(3) away from the Nariai marks one plane cuts, the least-magnitude root; Nariai: one side, tangent at its")
print("    midpoint, offsets (1, 1, -2); w = 0: offsets (0, +-sqrt3)                              OK")

# (4) the crossing points do not carry the horizon values
def crossings(wv):
    h = Hn[0]; t = np.array([-np.cos(wv), np.sin(wv)])
    b = 2*h @ t; c = h @ h - 1; disc = b*b - 4*c
    return [h + s*t for s in ((-b + np.sqrt(disc))/2, (-b - np.sqrt(disc))/2)]
def areal(p):                                # signed distance from the back--hinge axis (the X_1 axis)
    return p[1]
from scipy.optimize import brentq
def gaps(wv):
    roots = np.sort(np.array(fd(wv), dtype=float))/np.sqrt(3)
    far, near = crossings(wv)
    return abs(areal(far)) - roots[1], abs(areal(near)) - roots[2], abs(areal(far)) - roots[2], abs(areal(near)) - roots[1]
grid = np.linspace(1e-4, np.pi/6 - 1e-4, 4001)
G = np.array([gaps(wv) for wv in grid])
zeros = []
for j in range(4):
    sgn = np.sign(G[:, j])
    for i in np.where(sgn[:-1]*sgn[1:] < 0)[0]:
        zeros.append((j, brentq(lambda x: gaps(x)[j], grid[i], grid[i+1])))
# the far point carries the black-hole root only at w = 0; the only interior coincidence is ONE isolated angle
assert G[0, 0] > 0 and np.all(G[:, 0] > 0)
assert len(zeros) == 3 and sorted(j for j, _ in zeros) == [1, 2, 3], zeros
for j, wx in zeros:                          # each coincidence is a transversal crossing, not an interval
    assert np.sign(gaps(wx - 1e-3)[j]) != np.sign(gaps(wx + 1e-3)[j])
far0, _ = crossings(0.0)
assert np.allclose(far0, [-1, 0]) and np.isclose(areal(far0), 0.0)
print("(4) across the undercritical arc the crossing points' areal radii meet a horizon value only at")
print("    the isolated angles " + ", ".join(f"{np.degrees(x):.1f}" for _, x in sorted(zeros, key=lambda z: z[1])) + " deg, each a transversal crossing; the far point")
print("    carries the black-hole root only at w = 0, where it is the back point r = 0             OK")

# (5) R and the hinge relabellings commute: a direct product on the root triples
wv = 0.31
dv = np.array(fd(wv), dtype=float)
R = lambda v: -v
for perm in itertools.permutations(range(3)):
    P = lambda v, perm=perm: v[list(perm)]
    assert np.allclose(R(P(dv)), P(R(dv)))
# reflecting the swing in the hinge's own axis, w -> -w, carries the tangent at +30 deg to the one at -30 deg
# and negates the root triple (as a multiset; it also exchanges hinges 1 and 2)
for wv2 in np.linspace(0.0, 2*np.pi, 97):
    assert np.allclose(np.sort(np.array(fd(-wv2), dtype=float)), np.sort(-np.array(fd(wv2), dtype=float)))
tp, tm = (np.array([-np.cos(x), np.sin(x)]) for x in (np.pi/6, -np.pi/6))
for t in (tp, tm):                           # both are tangent lines from H_0: offset 1 from the axis
    nn = np.array([t[1], -t[0]])
    assert np.isclose(abs(nn @ Hn[0]), 1.0)
signs = {tuple(np.round(np.sort(e*dv), 12)) for e in (1, -1)}
assert len(signs) == 2                       # R is not a relabelling: it is the outer factor
print("(5) reversing the normal negates every offset and commutes with every hinge relabelling;")
print("    it is not itself a relabelling, so the generated symmetry is S_3 x Z_2                  OK")
