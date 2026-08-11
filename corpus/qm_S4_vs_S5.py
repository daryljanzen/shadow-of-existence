import numpy as np

print("="*70)
print("THE S4-vs-S5 FORK: where do gauge (su(3)) and hbar (Gibbons-Hawking) live?")
print("="*70)

# ---- Gell-Mann matrices: su(3) generators are i*lambda_a (anti-Hermitian, traceless) ----
l = [np.zeros((3,3),complex) for _ in range(8)]
l[0][[0,1],[1,0]] = 1
l[1][0,1]=-1j; l[1][1,0]=1j
l[2][0,0]=1; l[2][1,1]=-1
l[3][[0,2],[2,0]] = 1
l[4][0,2]=-1j; l[4][2,0]=1j
l[5][[1,2],[2,1]] = 1
l[6][1,2]=-1j; l[6][2,1]=1j
l[7]=np.diag([1,1,-2])/np.sqrt(3)
gen = [1j*L for L in l]   # su(3): anti-Hermitian, traceless

def realify(M):  # C^3 -> R^6 : z=x+iy -> (x,y); M=X+iY acts as [[X,-Y],[Y,X]]
    X,Y = M.real, M.imag
    return np.block([[X,-Y],[Y,X]])

print("\n[1] Does su(3) sit in so(6) (antisymmetric 6x6) and NOT in so(5)?")
maxasym=0; realdim_used=set()
for g in gen:
    R = realify(g)
    asym = np.abs(R+R.T).max()          # antisymmetric <=> R+R^T=0
    maxasym = max(maxasym, asym)
    # which of the 6 real coords does this generator move?
    moved = np.where(np.abs(R).sum(0)>1e-9)[0]
    realdim_used |= set(moved.tolist())
print(f"   max|R + R^T| over the 8 su(3) generators = {maxasym:.1e}  -> all antisymmetric => su(3) ⊂ so(6): {maxasym<1e-9}")
print(f"   real coordinates the su(3) action moves = {sorted(realdim_used)}  (needs all 6 => faithful on R^6)")
print(f"   => su(3) requires so(6)/S^5; it does NOT fit in so(5)/S^4 (only 5 real dims).")
print(f"      dims: dim su(3)=8, dim so(5)=10, dim so(6)=15; ranks 2,2,3.")
print(f"      minimal faithful REAL rep of su(3) is R^6 (the 3 ⊕ its conjugate), not R^5.")

print("\n[2] Gibbons-Hawking of dS_n: Euclidean section and temperature.")
print("   dS_n radius alpha: static-patch surface gravity kappa = 1/alpha (INDEPENDENT of n).")
print("   Euclidean time period beta = 2*pi/kappa = 2*pi*alpha (INDEPENDENT of n).")
print("   Euclidean continuation of dS_n is the round n-sphere S^n.")
for n in (4,5):
    kappa = 1.0  # in units alpha=1
    beta = 2*np.pi/kappa
    print(f"     dS_{n}:  Euclidean = S^{n},  kappa=1/alpha,  beta = {beta:.6f}*alpha = 2*pi*alpha")
print("   => beta=2*pi*alpha ALONE cannot tell S^4 (dS_4) from S^5 (dS_5): both give it.")

print("\n[3] The nesting.")
print("   S^4 ⊂ S^5 as the equator (x_5=0);  SO(5) ⊂ SO(6) as the stabilizer of an axis.")
print("   So the two candidate hbar-spheres are NOT disjoint from gauge's S^5:")
print("     - if hbar = substrate dS_5 GH  -> hbar-Euclid = S^5 = gauge's own sphere (EXACT co-location)")
print("     - if hbar = 4D-cosmology dS_4 GH-> hbar-Euclid = S^4 ⊂ S^5 (equator of gauge's sphere)")

print("\n[4] VERDICT")
print("   Gauge NEEDS the full S^5/SO(6) (su(3)⊄so(5)). Whichever de Sitter horizon sets hbar,")
print("   its Euclidean sphere is the global-Wick real form S^5/SO(6) OR its S^4 equator —")
print("   in BOTH readings the SAME real form as gauge, never a disjoint one.")
print("   => the fork does NOT split into 'same vs different real form'. It resolves to CLOSURE")
print("      at the real-form level; the only residue is full-S^5 vs S^4-equator, set by")
print("      whether hbar is the universal substrate GH (S^5) or the 4D observer GH (S^4⊂S^5).")
