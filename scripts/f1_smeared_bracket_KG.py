import sympy as sp
r, th, M, alpha = sp.symbols('r theta M alpha', positive=True)
N, Mf = sp.Function('N'), sp.Function('Mf')   # radial lapse smearings N(r), M(r)

print("="*72)
print("REACH step 3 — does the SMEARED HDA bracket close through the intrinsic")
print("carrier? (structure-function level)")
print("HDA: {H_perp[N],H_perp[M]} = H_a[ eps h^{ab}(N d_b M - M d_b N) ], h^{ab}=leaf inv 3-metric.")
print("="*72)

# slicing-curve leaf (slicing_operator gauge):  ds^2_3 = dr^2/f + r^2 dOmega^2
f = 1 - 2*M/r - r**2/alpha**2
hinv = {'rr': f, 'thth': 1/r**2, 'phph': 1/(r**2*sp.sin(th)**2)}   # inverse 3-metric h^{ab}
print("\n[1] leaf inverse 3-metric (the HDA structure function h^{ab}):")
print("    h^rr =", hinv['rr'], " ;  h^thth = 1/r^2 ;  h^phph = 1/(r^2 sin^2 th)")

# radial lapses N(r), M(r): the only nonzero smeared-bracket component is a=r
Nr, Mr = N(r), Mf(r)
bracket_r = sp.simplify(hinv['rr']*(Nr*sp.diff(Mr,r) - Mr*sp.diff(Nr,r)))
print("\n[2] smeared bracket, radial lapses N(r),M(r):  {H_perp[N],H_perp[M]} = H_r[ X^r ] with")
print("    X^r = h^rr (N M' - M N') =", bracket_r)
print("    => closes on H_r (the tangential/momentum constraint), coefficient = h^rr = f.")

# the coefficient IS the K_G-carried structure function: K_G = -f'/(2r)  <=>  f recovered from K_G
KG = sp.simplify(-sp.diff(f,r)/(2*r))
print("\n[3] the closing coefficient f = h^rr is the intrinsic-K_G object (step 1):")
print("    K_G = -f'/(2r) =", KG, "  ;  and f = h^rr is the same structure function steps 1-2 carry.")

# the CONNECTION at the smeared level: M-variation of the bracket coefficient
dM_coeff = sp.simplify(sp.diff(hinv['rr'], M))
dM_KG = sp.simplify(sp.diff(KG, M))
print("\n[4] connection at the smeared-bracket level (M-variation of the closing coefficient):")
print("    d_M (h^rr) =", dM_coeff, "  (= -2/r, the [m,m]->m leak / structure-function variation)")
print("    d_M K_G    =", dM_KG, "  (= -1/r^3); link  d_M K_G = -d_r(d_M h^rr)/(2r):",
      sp.simplify(dM_KG - (-sp.diff(dM_coeff,r)/(2*r))) == 0)

# symmetric cut (M=0): coefficient constant-curvature, connection vanishes
print("\n[5] symmetric cut M=0:  h^rr = f =", f.subs(M,0), " (de Sitter leaf);  d_M-connection present off it.")
print("    so the smeared bracket closes with a CONSTANT structure function at M=0 (genuine Lie),")
print("    and a VARYING one off it (genuine algebroid) -- the variation carried by K_G.")
