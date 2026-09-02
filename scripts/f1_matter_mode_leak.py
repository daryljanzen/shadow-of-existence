"""
REACH step 6 -- the MATTER mode level (m'(r) != 0).

Step 5 turned on the vacuum mass M (a straight cut, m'=0) and found the symmetric-cut
closure leaks, carried by M. This step turns on genuine matter: a slicing curve with
m'(r) != 0, i.e. density rho = m'/(4 pi r^2) (slicing_operator.tex, Prop "density is the
bend"). Question: does the symmetric-cut closure leak carry the matter density m' (the
bend), distinct from the enclosed mass m?

Construction-faithful (same as steps 4-5): the de Sitter manifold is the invariant
substrate, the matter leaf a bent slicing of it; the substrate modes are the de Sitter
harmonics X_a; the would-be coset-translation {X4,X1} closed as the isometry M_41 at the
symmetric (M=0) cut (step 4).

Result:
  [A] the retained SO(3) mode {X1,X2} -> d_phi stays Killing for ANY m(r).
  [B] the broken dS-translation {X4,X1} leaks, and the leak SPLITS by component:
        - angular (theta,theta),(phi,phi):  carry the ENCLOSED MASS m(r) only (no m').
        - radial   (r,r):                    carries the matter DENSITY m'(r).
  [C] the genuine-matter (density) piece of the radial leak is exactly linear in m',
      vanishes iff m'=0 (vacuum straight cut), and in terms of rho = m'/(4 pi r^2) reads
        8 pi alpha^2 r^2 rho sin(theta)cos(phi) / [ sqrt(alpha^2-r^2)(-alpha^2 r+2 alpha^2 m+r^3) ].
  [D] vacuum limit m(r)=M const (m'=0) recovers the step-5 vacuum-M leak.

So genuine matter (the density, the bend) DOES source the mode-level connection -- distinctly,
through the radial leak -- mirroring K_G's mass/matter split (-m/r^3 angular-like vs +4 pi rho).

Scope conjecture: the component structure (mass->angular, density->radial) is the finding; NO
closed-form "leak = grad K_G" identity is claimed.
"""
import sympy as sp

r, th, ph, al = sp.symbols('r theta phi alpha', positive=True)
M = sp.symbols('M', positive=True)
m = sp.Function('m')                       # mass function m(r); matter = bend m'(r) != 0

f = 1 - 2*m(r)/r - r**2/al**2              # matter slicing-curve leaf
g = sp.diag(1/f, r**2, r**2*sp.sin(th)**2)
hinv = g.inv()
coords = [r, th, ph]
X = {1: r*sp.sin(th)*sp.cos(ph), 2: r*sp.sin(th)*sp.sin(ph),
     3: r*sp.cos(th), 4: sp.sqrt(al**2 - r**2)}
mp = sp.Derivative(m(r), r)


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


# [A] retained SO(3)
xi12 = hda_vec(X[1], X[2])
L12 = lie_g(xi12)
print("[A] {X1,X2}: xi =", xi12, "; Killing for any m(r)?", L12 == sp.zeros(3, 3))

# [B] broken dS-translation: component split
xi41 = hda_vec(X[4], X[1])
L41 = lie_g(xi41)
print("\n[B] {X4,X1} leak -- which components carry the density m'(r):")
for a in range(3):
    if L41[a, a] != 0:
        print(f"    [{coords[a]},{coords[a]}] carries m'(r)?", L41[a, a].has(mp))

# [C] isolate the genuine-matter (density) piece of the radial leak
Lrr = L41[0, 0]
Lrr_mass = sp.simplify(Lrr.subs(mp, 0))                 # m'=0 piece (enclosed mass)
Lrr_density = sp.simplify(Lrr - Lrr_mass)               # the m' piece
print("\n[C] radial leak: genuine-matter (density m') piece")
print("    vanishes iff m'=0 (vacuum)?", sp.simplify(Lrr_density.subs(mp, 0)) == 0,
      "; linear in m'?", sp.simplify(Lrr_density - mp*sp.diff(Lrr_density, mp)) == 0)
rho_d = sp.symbols('rho_d', positive=True)
print("    in terms of rho=m'/(4 pi r^2):")
sp.pprint(sp.simplify(Lrr_density.subs(mp, 4*sp.pi*r**2*rho_d)))

# [D] vacuum limit recovers step 5
print("\n[D] vacuum m(r)=M (m'=0): angular leak")
print("    L[theta,theta]|_{m=M} =", sp.simplify(L41[1, 1].subs(m(r), M).doit()),
      "(= step-5 vacuum-M leak)")
