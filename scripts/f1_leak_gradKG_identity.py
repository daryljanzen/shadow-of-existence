"""
GRIND r267 -- resolves the named-open internal caveat of F1 (f1_homomorphism_consolidation §4a):

  Is the mode-level connection-leak equal to grad K_G in closed form?

Steps 5-6 established only that the leak is *driven by* d_M f / the density and splits
mass->angular, density->radial -- explicitly "weaker than an identity," the leak = grad K_G
identity left UNCLAIMED. This script settles it, in the same construction (matter leaf, de
Sitter harmonic modes, the broken dS-translation {X4,X1} whose Killing-failure is the leak).

VERDICT (computed, symbolic, general m(r)):
  The identity does NOT hold, and the obstruction is structural, not a missing simplification:
    * K_G = 1/alpha^2 - m/r^3 + 4*pi*rho  contains the density term 4*pi*rho = m'/r^2, so
      grad K_G = d_r K_G = (r^2 m'' - 3 r m' + 3 m)/r^4  carries m'' (the Hessian carries m''').
    * the mode-level leak L_xi g is a function of (m, m') ONLY -- it never contains m''.
    A tensor of derivative order (m,m') cannot equal one of order m'' for general m(r).

POSITIVE CHARACTERIZATION (the closed form the caveat lacked):
    The leak IS the transverse-modulus data in closed form -- the angular components are
    EXACTLY linear in the enclosed mass m (L[theta,theta]/m = -4 alpha^2 sin th cos ph /
    sqrt(alpha^2 - r^2), independent of m and m'), and the radial component carries the
    density m'. So the connection is the modulus data (mass->angular, density->radial), the
    "bend" itself -- a transverse-modulus (d_M) object, NOT the spatial gradient of K_G.

CONSEQUENCE [reach -- for the one-clock test, Entry 8]:
    The connection's TRANSVERSE face is thereby pinned in closed form as the modulus data
    (m, m'); grad K_G is ruled out as that face. This sharpens, but does not resolve, the
    one-clock test (whether the connection's along-orbit trivialization equals its transverse
    restriction at the seam) -- only its transverse term is now in closed form.

Receipts it builds on: f1_offsymmetric_mode_leak.py (step 5), f1_matter_mode_leak.py (step 6),
f1_grading_through_KG.py (K_G), f1_homomorphism_consolidation.md §4a.
"""
import sympy as sp

r, th, ph, al = sp.symbols('r theta phi alpha', positive=True)
m = sp.Function('m')

# matter leaf (3-leaf), exactly as steps 5-6
f = 1 - 2*m(r)/r - r**2/al**2
g = sp.diag(1/f, r**2, r**2*sp.sin(th)**2)
hinv = g.inv()
coords = [r, th, ph]
X = {1: r*sp.sin(th)*sp.cos(ph), 4: sp.sqrt(al**2 - r**2)}


def hda_vec(Na, Nb):
    return [sp.simplify(sum(hinv[c, d]*(Na*sp.diff(Nb, coords[d]) - Nb*sp.diff(Na, coords[d]))
                            for d in range(3))) for c in range(3)]


def lie_g(xi):
    L = sp.zeros(3, 3)
    for a in range(3):
        for b in range(3):
            t = sum(xi[c]*sp.diff(g[a, b], coords[c]) for c in range(3))
            t += sum(g[c, b]*sp.diff(xi[c], coords[a]) for c in range(3))
            t += sum(g[a, c]*sp.diff(xi[c], coords[b]) for c in range(3))
            L[a, b] = sp.simplify(t)
    return L


L = lie_g(hda_vec(X[4], X[1]))                       # the leak
m2 = sp.Derivative(m(r), (r, 2))
m3 = sp.Derivative(m(r), (r, 3))

KG = 1/al**2 - m(r)/r**3 + sp.diff(m(r), r)/r**2     # intrinsic Gaussian curvature (4 pi rho = m'/r^2)
dKG = sp.simplify(sp.diff(KG, r))                    # grad K_G (radial)
HessKG = sp.simplify(sp.diff(KG, r, 2))              # Hessian K_G (radial)

leak_has_m2 = any(L[a, b].has(m2) for a in range(3) for b in range(3))
print("leak L_xi g contains m''(r)? ", leak_has_m2, "  (function of (m, m') only)")
print("grad K_G contains m''?        ", dKG.has(m2))
print("Hess K_G contains m'''?       ", HessKG.has(m3))
assert not leak_has_m2 and dKG.has(m2) and HessKG.has(m3)
print(">>> VERDICT: leak =/= grad K_G (derivative-order mismatch; identity ruled out).")

ang = sp.simplify(L[1, 1] / m(r))
print("\nL[theta,theta]/m(r) =", ang, " (no m, m' -> exactly linear in enclosed mass)")
print("radial leak carries density m'? ", sp.simplify(L[0, 0]).has(sp.Derivative(m(r), r)))
print(">>> POSITIVE: leak = transverse-modulus data (mass->angular, density->radial), closed form;")
print("    the connection is a d_M object, not the spatial gradient of K_G.")
