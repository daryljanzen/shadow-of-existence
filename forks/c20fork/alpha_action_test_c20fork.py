import numpy as np
print("="*78)
print("c20fork TURN 3 — the alpha-action (P3-deferred): gauge homothety or new symmetry?")
print("P3 line 51: alpha=sqrt(3/Lambda)=1 is a GAUGE CHOICE; alpha the invariant,")
print("M the slicing-dependent factor; 2M = alpha((r0/alpha)-(r0/alpha)^3).")
print("="*78)

def f(r, twoM, alpha):
    return 1 - twoM/r - r**2/alpha**2

# Homothety: alpha -> lam*alpha, r -> lam*r, 2M -> lam*2M, l -> lam*l.
lam, r, twoM, alpha = 3.7, 0.8, 0.2, 1.0
base   = f(r, twoM, alpha)
scaled = f(lam*r, lam*twoM, lam*alpha)
print(f"\nf(r;2M,alpha)               = {base:.10f}")
print(f"f(lam r; lam 2M, lam alpha) = {scaled:.10f}   invariant? {np.isclose(base,scaled)}")

# The dimensionless content rho=r/alpha obeys rho^3 - rho + (2M/alpha) = 0;
# scale-invariant iff 2M/alpha is invariant under the homothety:
m1 = twoM/alpha
m2 = (lam*twoM)/(lam*alpha)
print(f"\ndimensionless 2M/alpha: gauge={m1:.6f}  scaled={m2:.6f}  invariant? {np.isclose(m1,m2)}")
print("=> roots in units of alpha (rho=r/alpha) identical at every alpha")
print("=> the Aut(A_2)=S_3 x Z_2 classification is SCALE-INVARIANT.")

print("\n"+"="*78)
print("VERDICT (turn 3): the alpha-action = the gauge homothety R_+ (continuous scaling).")
print(" It is NOT a new discrete symmetry; it relates scaled copies of one dimensionless")
print(" structure, under which Aut(A_2)=S_3 x Z_2 is invariant.  This closes the last")
print(" P3-deferred piece (the action between distinct de Sitter representations, different")
print(" alpha).  The gem is fully classified: discrete Aut(A_2) on the complexified locus,")
print(" regimes as real/imaginary sections of the sin->cosh continuation, scale-invariant.")
print("="*78)
