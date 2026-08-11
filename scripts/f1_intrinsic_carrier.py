import sympy as sp
r, M, alpha = sp.symbols('r M alpha', positive=True)
m = sp.Function('m')

print("="*70)
print("REACH step 1 — is the matter/bend face carried INTRINSICALLY by the")
print("slicing curve? (K_G of the slicing surface, Theorema-Egregium-intrinsic)")
print("="*70)

# slicing_operator matter curve: f = 1 - 2 m(r)/r - r^2/alpha^2  (Lambda=3/alpha^2)
f = 1 - 2*m(r)/r - r**2/alpha**2
# P3 slicing-surface Gaussian curvature (surface of revolution ds^2=dl^2+r^2 dphi^2):
KG = sp.simplify(-sp.diff(f, r)/(2*r))
print("\n[1] K_G = -f'/(2r) for the matter curve f=1-2m/r-r^2/alpha^2:")
print("    K_G =", KG)

# matter density (slicing_operator prop:bend): rho = m'(r)/(4 pi r^2)
rho = sp.diff(m(r), r)/(4*sp.pi*r**2)
KG_in_terms = sp.simplify(KG - (1/alpha**2 - m(r)/r**3 + 4*sp.pi*rho))
print("\n[2] claim  K_G = 1/alpha^2 - m/r^3 + 4*pi*rho   (matter = +4*pi*rho in K_G):")
print("    K_G - (1/alpha^2 - m/r^3 + 4*pi*rho) =", KG_in_terms, " (expect 0)")

# vacuum reduction m=M const -> matches the paper K_G = 1/alpha^2 - M/r^3
fvac = 1 - 2*M/r - r**2/alpha**2
KGvac = sp.simplify(-sp.diff(fvac, r)/(2*r))
print("\n[3] vacuum (m=M const): K_G =", KGvac, " (paper: 1/alpha^2 - M/r^3)")

# the CONNECTION (structure-function M-variation) read in leaf vs in K_G
dM_hrr = sp.simplify(sp.diff(fvac, M))           # leaf radial structure function h^rr=f
dM_KG  = sp.simplify(sp.diff(KGvac, M))          # intrinsic surface curvature
link   = sp.simplify(dM_KG - (-sp.diff(dM_hrr, r)/(2*r)))
print("\n[4] connection, two readings of the same f-bend:")
print("    d_M h^rr = d_M f =", dM_hrr, "   (the HDA connection, vision/consolidation)")
print("    d_M K_G        =", dM_KG, "   (intrinsic surface curvature variation)")
print("    d_M K_G - (-d_r(d_M h^rr)/(2r)) =", link, " (expect 0: same bend, leaf & surface)")

# link to the 3D leaf Hamiltonian constraint: ^3R = (2/r^2)(1-f) + 4 K_G ?
R3 = sp.simplify((2/r**2)*(1 - fvac - r*sp.diff(fvac, r)))   # adm1 3-Ricci scalar
check3R = sp.simplify(R3 - ((2/r**2)*(1-fvac) + 4*KGvac))
print("\n[5] 3D leaf Ricci (adm1) vs 2D K_G:  ^3R = (2/r^2)(1-f) + 4 K_G ?")
print("    ^3R =", R3, " ;  residual =", check3R, " (expect 0)")
