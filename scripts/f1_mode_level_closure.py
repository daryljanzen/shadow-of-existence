import sympy as sp
rho, th, ph, al = sp.symbols('rho theta phi alpha', positive=True)

print("="*74)
print("REACH step 4 — the MODE level: do coset-lapse HDA brackets reproduce the")
print("isotropy Killing vectors term-for-term?  {H_perp[X_a],H_perp[X_b]} =?= H(M_ab)")
print("="*74)

# dS4 static-patch SPATIAL LEAF (t=0, X5=0):  ds^2_3 = drho^2/f + rho^2 dOmega^2,  f=1-rho^2/al^2
f = 1 - rho**2/al**2
g = sp.diag(1/f, rho**2, rho**2*sp.sin(th)**2)          # leaf 3-metric (rho,theta,phi)
hinv = g.inv()                                          # h^{ab} = diag(f, 1/rho^2, 1/(rho^2 sin^2))
coords = [rho, th, ph]

# coset-lapse modes N_a = X_a|leaf  (de Sitter embedding coords on t=0,X5=0 slice):
# X1=rho sinth cosph, X2=rho sinth sinph, X3=rho costh, X4=sqrt(al^2-rho^2)  (X0=0 at t=0)
X = {1: rho*sp.sin(th)*sp.cos(ph),
     2: rho*sp.sin(th)*sp.sin(ph),
     3: rho*sp.cos(th),
     4: sp.sqrt(al**2 - rho**2)}

def hda_bracket_vector(Na, Nb):
    # xi^c = h^{cd}(Na d_d Nb - Nb d_d Na)   (the H_a produced by {H_perp[Na],H_perp[Nb]})
    xi = []
    for c in range(3):
        s = 0
        for d in range(3):
            s += hinv[c,d]*(Na*sp.diff(Nb, coords[d]) - Nb*sp.diff(Na, coords[d]))
        xi.append(sp.simplify(s))
    return xi   # contravariant xi^c on (rho,theta,phi)

def is_killing(xi):
    # Killing eqn: nabla_a xi_b + nabla_b xi_a = 0.  Compute L_xi g_{ab} directly.
    xil = [sp.simplify(sum(g[a,b]*xi[b] for b in range(3))) for a in range(3)]  # lower
    # Lie derivative of metric: (L_xi g)_{ab} = xi^c d_c g_ab + g_cb d_a xi^c + g_ac d_b xi^c
    L = sp.zeros(3,3)
    for a in range(3):
        for b in range(3):
            term = sum(xi[c]*sp.diff(g[a,b],coords[c]) for c in range(3))
            term += sum(g[c,b]*sp.diff(xi[c],coords[a]) for c in range(3))
            term += sum(g[a,c]*sp.diff(xi[c],coords[b]) for c in range(3))
            L[a,b] = sp.simplify(term)
    return L

# --- test 1: {X1,X2} should be M_12 = the azimuthal rotation d_phi (obvious leaf Killing vector) ---
xi12 = hda_bracket_vector(X[1], X[2])
print("\n[test 1]  xi = HDA{X1,X2}  (expect M_12 = d_phi, the phi-rotation):")
print("   xi^rho, xi^theta, xi^phi =", xi12)
L12 = is_killing(xi12)
print("   Killing? (L_xi g) =", "ZERO -> Killing vector" if L12 == sp.zeros(3,3) else L12)

# --- test 2: {X4,X1} should be M_41, a de Sitter 'translation' (less obvious tangential isometry) ---
xi41 = hda_bracket_vector(X[4], X[1])
print("\n[test 2]  xi = HDA{X4,X1}  (expect M_41, a de Sitter translation-isometry of the leaf):")
print("   xi^rho   =", xi41[0])
print("   xi^theta =", xi41[1])
print("   xi^phi   =", xi41[2])
L41 = is_killing(xi41)
print("   Killing? (L_xi g) =", "ZERO -> Killing vector" if L41 == sp.zeros(3,3) else "NONZERO:")
if L41 != sp.zeros(3,3): sp.pprint(L41)

# --- test 3: {X1,X3} another mixed one (expect M_13, a leaf rotation) ---
xi13 = hda_bracket_vector(X[1], X[3])
L13 = is_killing(xi13)
print("\n[test 3]  HDA{X1,X3} Killing? ", "ZERO -> Killing" if L13==sp.zeros(3,3) else "NONZERO")
