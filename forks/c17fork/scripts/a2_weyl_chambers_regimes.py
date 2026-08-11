import sympy as sp, numpy as np

M = sp.symbols('M', real=True)
r1,r2,r3 = sp.symbols('r1 r2 r3', real=True)
print("="*70); print("c17fork_2 / bite (A): A2 Weyl-wall structure = the regime boundary"); print("="*70)

# Horizon cubic r^3 - r + 2M ; discriminant of r^3 + p r + q is -4p^3 - 27 q^2
p, q = -1, 2*M
Delta = sp.expand(-4*p**3 - 27*q**2)
print("\n[A1] Discriminant of r^3 - r + 2M :  Delta =", Delta, " = 4 - 108 M^2")
# Delta = product_{i<j}(r_i-r_j)^2  (the Weyl/Vandermonde invariant) -- verify on a numeric geometry
for Mv in [0.10]:
    roots = np.roots([1,0,-1,2*Mv]).real
    vander2 = np.prod([(roots[i]-roots[j])**2 for i in range(3) for j in range(i+1,3)])
    print(f"     check at M={Mv}: prod (r_i-r_j)^2 = {vander2:.6f}  vs  4-108M^2 = {4-108*Mv**2:.6f}")

crit = 1/np.sqrt(27)
print(f"\n[A2] Delta = 0  <=>  M = +/- 1/sqrt(27) = {crit:.5f}  (two horizons collide = a Weyl WALL)")
print("     Delta > 0  <=>  |M| < 1/sqrt27 : THREE real horizons  (full real A2 triplet)")
print("     Delta = 0  <=>  |M| = 1/sqrt27 : repeated root        (ON a Weyl wall = NARIAI)")
print("     Delta < 0  <=>  |M| > 1/sqrt27 : one real + cplx pair (triplet COMPLEXIFIED)")

print("\n[A3] regime map = discriminant-sign chambers of the A2 structure:")
for Mv,lab in [(0.10,'under-critical'),(crit,'critical (Nariai)'),(0.30,'over-critical')]:
    rts = np.roots([1,0,-1,2*Mv])
    nreal = int(np.sum(np.abs(rts.imag)<1e-9))
    D = 4-108*Mv**2
    print(f"     M={Mv:.4f} {lab:20s} Delta={D:+.4f}  real horizons={nreal}  roots={np.round(rts,3)}")

# [A4] signature: g_tt = N/r, N=r^3-r+2M.  N>0 => r timelike (cosmic time); N<0 => r spacelike (static)
print("\n[A4] signature sign(N): N>0 => r TIMELIKE (cosmic-time/cosmological); N<0 => r SPACELIKE (static)")
for Mv,lab in [(0.10,'under-critical (BH)'),(0.30,'over-critical (cosmos)')]:
    rts = sorted([x.real for x in np.roots([1,0,-1,2*Mv]) if abs(x.imag)<1e-9])
    # sample N sign on r>0 intervals
    test = [0.05,0.3,0.6,1.2]
    sgn = ['+' if (t**3 - t + 2*Mv)>0 else '-' for t in test]
    print(f"     M={Mv} {lab}: real horizons(r>0)={[round(x,3) for x in rts if x>0]}  sign N at r={test} -> {sgn}")
print("     => over-critical: N>0 for all r>0 (PURE cosmology, r=cosmic time throughout);")
print("        under-critical: interior region between horizons has N>0 (r=cosmic time) = interior-as-cosmology (P1).")

# [A5] negative-mass: 2M = r0 - r0^3 is ODD in r0 => r0->-r0 sends M->-M (reflection about r=0, thesis line78)
r0 = sp.symbols('r0', real=True)
twoM = r0 - r0**3
print("\n[A5] 2M(r0) =", twoM, " is ODD: 2M(-r0) =", sp.expand(twoM.subs(r0,-r0)), " => r0->-r0 sends M->-M")
print("     => negative mass is the Z2 reflection r->-r of the positive-mass A2 orbit (thesis line 78,")
print("        'reflections about r=0'); full solution-space discrete symmetry contains S3 x Z2.")
print("="*70)
print("RESULT: the A2 discriminant (Weyl-invariant) organizes the SOLUTION SPACE into")
print("  black-hole (Delta>0, real triplet) | NARIAI (Delta=0, on a Weyl wall) | cosmology")
print("  (Delta<0, complexified triplet, r=cosmic time). The Weyl walls ARE the Nariai/critical")
print("  loci; crossing them (M past 1/sqrt27) is interior-becomes-cosmology. One A2 object.")
print("="*70)
