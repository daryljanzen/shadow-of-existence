"""
REACH step 5 -- the off-symmetric (vacuum-M) MODE level.

Question: as the cut moves off the symmetric (de Sitter, M=0) cut over the
M-modulus, does the symmetric-cut isometry-mode closure of step 4 LEAK, and is
the leak the algebroid connection?

Construction (grounded at slicing_operator.tex sec:ontology/kernel/bend):
the de Sitter manifold is the invariant substrate; SdS is a *slicing* of it;
a constant-M cut is a STRAIGHT cut (m'=0, VACUUM), not matter. So the substrate
modes are the de Sitter harmonics X_a, and an off-symmetric VACUUM cut (M!=0)
tests the connection across the M-modulus -- NOT matter (which is m'!=0).

Result: the retained SO(3) mode {X1,X2}->d_phi stays Killing for all M; the
broken dS-translation {X4,X1} (which closed as M_41 at M=0, step 4) leaks --
L_xi g != 0, every component carrying a factor M, all vanishing at M=0. The
leak enters solely through h^rr=f in xi^rho, whose M-variation d_M f = -2/rho is
the structure-function connection (steps 1-3). So the [m,m]->m leak IS that
connection, realized at the mode level.

Scope [reach]: vacuum M-modulus only; the MATTER bend (m'!=0) is a distinct rung.
No closed-form "leak = grad K_G" identity is claimed -- only that the leak is
driven by d_M f and vanishes at the symmetric stratum.
"""
import sympy as sp

rho, th, ph, al, M = sp.symbols('rho theta phi alpha M', positive=True)

# SdS spatial leaf (M symbolic, VACUUM straight cut m'=0)
f = 1 - 2*M/rho - rho**2/al**2
g = sp.diag(1/f, rho**2, rho**2*sp.sin(th)**2)
hinv = g.inv()                                  # h^{ab} = diag(f, 1/rho^2, 1/(rho^2 sin^2))
coords = [rho, th, ph]

# substrate reference modes = de Sitter harmonics (the M=0 coset-lapse modes)
X = {1: rho*sp.sin(th)*sp.cos(ph),
     2: rho*sp.sin(th)*sp.sin(ph),
     3: rho*sp.cos(th),
     4: sp.sqrt(al**2 - rho**2)}


def hda_vec(Na, Nb):
    """xi^c = h^{cd}(Na d_d Nb - Nb d_d Na): the H_a produced by {H_perp[Na],H_perp[Nb]}."""
    return [sp.simplify(sum(hinv[c, d]*(Na*sp.diff(Nb, coords[d]) - Nb*sp.diff(Na, coords[d]))
                            for d in range(3)))
            for c in range(3)]


def lie_g(xi):
    """(L_xi g)_{ab} = xi^c d_c g_ab + g_cb d_a xi^c + g_ac d_b xi^c."""
    L = sp.zeros(3, 3)
    for a in range(3):
        for b in range(3):
            t = sum(xi[c]*sp.diff(g[a, b], coords[c]) for c in range(3))
            t += sum(g[c, b]*sp.diff(xi[c], coords[a]) for c in range(3))
            t += sum(g[a, c]*sp.diff(xi[c], coords[b]) for c in range(3))
            L[a, b] = sp.simplify(t)
    return L


print("[A] retained SO(3): {X1,X2} on the SdS leaf")
xi12 = hda_vec(X[1], X[2])
L12 = lie_g(xi12)
print("    xi =", xi12, " ; L_xi g =",
      "ZERO -> Killing for all M (SO(3) retained)" if L12 == sp.zeros(3, 3) else L12)

print("\n[B] broken dS-translation: {X4,X1} on the SdS leaf -- the leak")
xi41 = hda_vec(X[4], X[1])
L41 = lie_g(xi41)
nz = [(a, b, L41[a, b]) for a in range(3) for b in range(3) if L41[a, b] != 0]
for a, b, val in nz:
    at0 = sp.simplify(val.subs(M, 0))
    print(f"    (L_xi g)[{coords[a]},{coords[b]}] : at M=0 ->", at0,
          "; carries factor M ->", sp.simplify(val.subs(M, 0)) == 0)

print("\n[C] the leak is driven by the structure-function connection")
print("    d_M(h^rr) = d_M f =", sp.simplify(sp.diff(f, M)), " (= -2/rho)")
print("    every leak component vanishes at M=0:",
      all(sp.simplify(val.subs(M, 0)) == 0 for _, _, val in nz),
      "-> recovers step-4 closure at the symmetric cut.")
