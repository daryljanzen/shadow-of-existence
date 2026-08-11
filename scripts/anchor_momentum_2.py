import sympy as sp

print("="*78)
print("ANCHOR — momentum sector, GENERAL COVARIANT level (Move 5).")
print("The shift enters as a CUT DATUM through the extrinsic curvature; the momentum")
print("density is the perp-i ADM constraint, the companion of the energy sector's")
print("perp-perp Hamiltonian constraint. j_i = the BEND IN THE SHIFT, exactly as")
print("rho = the bend in the leaf. Verified to reproduce anchor_momentum_1's direct")
print("G_{t phi} frame-drag (the spherical instance).")
print("="*78)

# ---- general statement (the construction's ADM framing: P5/P6 'leaf/lapse/shift/vantage' = ADM data)
# 3+1: ds^2 = -N^2 dt^2 + gamma_ij (dx^i + N^i dt)(dx^j + N^j dt)
# stationary leaf (d_t gamma = 0):  K_ij = (1/2N)(D_i N_j + D_j N_i)        [shift's symmetrized gradient]
# momentum constraint:  D_j(K^j_i - delta^j_i K) = 8 pi j_i   (= 0 in vacuum; the perp-i Einstein comp.)
# => j_i is a clean second-order functional of the SHIFT datum N^i alone. IT SEPARATES.

r, th, M, al, J, C0, eps = sp.symbols('r theta M alpha J C0 epsilon', positive=True)
w = sp.Function('w')(r)
f = 1 - 2*M/r - r**2/al**2
N = sp.sqrt(f)                                   # lapse (the locked SdS lapse)
X = [r, th, sp.Symbol('phi')]
gam = sp.diag(1/f, r**2, r**2*sp.sin(th)**2)     # the SdS spatial leaf
gaminv = gam.inv()

# shift: pure axial frame-drag, N^phi = eps*w(r) (eps = linearize bookkeeping)
Nup = sp.Matrix([0, 0, eps*w])
Nlow = sp.simplify(gam*Nup)                      # N_i = gamma_ij N^j  => N_phi = eps*w*r^2 sin^2 th

def christ3(g, ginv, X):
    n=3; Ga=[[[0]*n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                Ga[a][b][c]=sp.simplify(sum(ginv[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])
                                          -sp.diff(g[b,c],X[d])) for d in range(n))/2)
    return Ga
Ga = christ3(gam, gaminv, X)

# D_i N_j = d_i N_j - Ga^k_ij N_k
DN = sp.zeros(3,3)
for i in range(3):
    for j in range(3):
        DN[i,j] = sp.diff(Nlow[j], X[i]) - sum(Ga[k][i][j]*Nlow[k] for k in range(3))

# K_ij = (1/2N)(D_i N_j + D_j N_i)   (stationary)
K = sp.zeros(3,3)
for i in range(3):
    for j in range(3):
        K[i,j] = sp.simplify((DN[i,j]+DN[j,i])/(2*N))
Kmix = sp.simplify(gaminv*K)                     # K^i_j
Ktr  = sp.simplify(sum(Kmix[i,i] for i in range(3)))
print("\n[1] K (trace) =", Ktr, "  (0 => shift is divergence-free here; frame-drag is shear, traceless)")

# momentum constraint tensor T^j_i = K^j_i - delta^j_i K ; covariant divergence over j:
# D_j T^j_i = d_j T^j_i + Ga^j_jk T^k_i - Ga^k_ji T^j_k
T = sp.simplify(Kmix - sp.eye(3)*Ktr)
mom = sp.zeros(3,1)
for i in range(3):
    s = 0
    for j in range(3):
        s += sp.diff(T[j,i], X[j])
        for k in range(3):
            s += Ga[j][j][k]*T[k,i] - Ga[k][j][i]*T[j,k]
    mom[i] = sp.simplify(s)
# only the phi-component is nonzero (the angular-momentum density). Linearize in eps, strip angular factor.
mom_phi = sp.simplify(sp.diff(mom[2], eps).subs(eps,0))
ode_3p1 = sp.simplify(sp.numer(sp.together(mom_phi)))
ode_3p1 = sp.expand(sp.simplify(ode_3p1 / sp.gcd(ode_3p1, sp.sin(th))))
print("\n[2] ADM momentum constraint, phi-component (vacuum j_phi=0), numerator:")
print("   ", ode_3p1, "= 0")

print("\n[3] cross-check against anchor_momentum_1's DIRECT G_{t phi} frame-drag ODE:")
ode_direct = (-2*M*al**2*r*sp.diff(w,r,2) - 8*M*al**2*sp.diff(w,r) + al**2*r**2*sp.diff(w,r,2)
              + 4*al**2*r*sp.diff(w,r) - r**4*sp.diff(w,r,2) - 4*r**3*sp.diff(w,r))
ratio = sp.simplify(ode_3p1/ode_direct)
print("    (3+1 momentum ODE) / (direct G_{tphi} ODE) =", ratio,
      " (a constant => same equation, two derivations)")

print("\n[4] solutions on the vacuum momentum constraint:")
for trial,label in [(2*J/r**3,"w = 2J/r^3   (localized frame-drag, J the angular momentum)"),
                    (C0,"w = C0       (rigid co-rotation, homogeneous mode)"),
                    (C0+2*J/r**3,"w = C0 + 2J/r^3 (general)")]:
    print(f"    {label}:  residual = {sp.simplify(ode_3p1.subs(w,trial).doit())}")

print("\n"+"="*78)
print("READING (momentum sector, general covariant — completes the anchor's four data):")
print("="*78)
print("""
 - The shift is a CUT DATUM on the same footing as the leaf and the lapse. Through the
   extrinsic curvature K_ij = (1/2N)(D_i N_j + D_j N_i), it enters the perp-i ADM
   constraint D_j(K^j_i - delta^j_i K) = 8 pi j_i. So the momentum density j_i is a clean
   second-order functional of the shift ALONE -- IT SEPARATES (the plan's 'can-return'
   resolved: the momentum sector does separate cleanly at the representational level).
 - j_i = the BEND IN THE SHIFT, the exact perp-i companion of rho = the bend in the leaf
   (perp-perp). Vacuum is where the shift's bend vanishes: rigid co-rotation (w=const) and
   the localized 1/r^3 mode both give j=0 on the SdS substrate (Lambda cancels for 1/r^3).
 - The two derivations agree: the 3+1 momentum constraint (shift -> K -> j_i) reproduces
   the direct spacetime G_{t phi} of anchor_momentum_1 up to an overall constant -- the
   same frame-drag equation, confirming 'j_i = the shift's bend' is the construction's own
   ADM momentum constraint, not an imported model.
 - PHYSICAL CONTENT (P6, established at source, range_paper sec:rotation): the frame-drag
   amplitude J is NOT free -- it is the mass-offset times the twist, J = Ma/Xi^2. Offset
   alone (w=0) is SdS; twist alone (M=0) is de Sitter (maximally symmetric, not a new
   geometry); only the offset taken in a twisted slice carries J. The bare 'J' of
   anchor_momentum_1 is this Ma.
 - THE FOUR ADM CUT DATA NOW CLOSE as one functional of the cut:
       leaf   (3-geometry)   -> energy   rho = leaf bend     [Hamiltonian constraint, general]
       shift  (frame-drag)   -> momentum j_i = shift bend     [momentum constraint, THIS, general]
       lapse  (time-stacking)-> stress   S_ij= stacking bend  [ij evolution; anchor_stress_1]
       vantage(radial sig.)  -> signature (hole vs cosmos)    [operator sec:dictionary]
   Energy + momentum are the constraints (initial data on the leaf); stress is the
   evolution. HONEST SCOPE: verified on the spherical class (here + anchor_momentum_1/_2,
   recovering the direct computation); the general statement is the covariant ADM
   constraint with the CR bend-reading; the explicit non-spherical (homogeneous,
   axisymmetric/rotating-type-I) matter functionals remain (range sec:open item 2), and
   the dS5-slicing restriction (which cuts are admissible) remains.
""")
