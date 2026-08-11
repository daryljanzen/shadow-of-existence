import sympy as sp
print("="*78)
print("ADM-6 (route a): does a quantized spectrum carry the standard-2d S3 rep?")
print("="*78)

# ---------------------------------------------------------------------------
# Part A. WHERE S3 would live on a quantum spectrum: L^2 of the sky-angle circle.
#   D3 = <tau: w -> w+2pi/3 ,  sigma: w -> pi/3 - w>  acting on functions psi(w).
#   Fourier basis e^{i n w}:  tau e^{inw}=zeta^n e^{inw} (zeta=e^{2pi i/3}); sigma e^{inw}=e^{i n pi/3} e^{-i n w}.
#   So sigma maps mode n <-> -n; for n != 0 the 2-dim space span{e^{inw},e^{-inw}} carries a D3 rep.
#   Decompose it by characters.  D3 classes: e ; 3-cycles (tau) ; transpositions (sigma).
# ---------------------------------------------------------------------------
print("\n(A) L^2(sky-angle circle) under D3 = <tau, sigma>: which modes carry the standard-2d irrep?")
print("    D3 character table (cols: e, 3-cycle, transposition):")
print("      trivial (1, 1, 1);  sign (1, 1, -1);  standard-2d (2, -1, 0)")
def decompose(chi):  # chi = (chi_e, chi_3cyc, chi_transp); class sizes 1,2,3
    irr={'trivial':(1,1,1),'sign':(1,1,-1),'standard2d':(2,-1,0)}
    sizes=(1,2,3)
    out={}
    for name,c in irr.items():
        m=sp.Rational(sum(s*a*b for s,a,b in zip(sizes,chi,c)),6)
        out[name]=m
    return out
for ncls,label in [(0,'n=0 (constant)'),(3,'n != 0, n = 0 mod 3'),(1,'n != 0, n = 1 mod 3'),(2,'n != 0, n = 2 mod 3')]:
    if ncls==0:
        chi=(1,1,1)  # 1-dim constant mode
    else:
        n=ncls
        chi_e=2
        chi_tau=sp.simplify(sp.exp(2*sp.I*sp.pi*n/3)+sp.exp(-2*sp.I*sp.pi*n/3))  # zeta^n+zeta^-n
        chi_tau=sp.nsimplify(sp.re(sp.simplify(chi_tau)))
        chi_sig=0  # sigma swaps e^{inw}<->e^{-inw}: zero diagonal
        chi=(chi_e,int(chi_tau),chi_sig)
    print(f"    {label:24s}: char={chi} -> {decompose(chi)}")
print("    => the STANDARD-2D irrep is carried by every mode n != 0 (mod 3); infinitely many copies.")
print("       (n=0 mod 3 modes give trivial+sign; the constant mode is trivial.)")

# ---------------------------------------------------------------------------
# Part B. The cosmological dust-time minisuperspace: what variable does it quantize?
# ---------------------------------------------------------------------------
print("\n(B) The cosmological dust-time H_phys quantizes the scale factor a(tau), NOT the sky-angle.")
print("    Flat FLRW, dust+Lambda, dust-time (N=1): single DOF = a, momentum p_a.")
print("    Friedmann constraint -> H_phys(a,p_a) generating tau-evolution; a in (0,inf), 1 DOF.")
print("    There is NO sky-angle w among its variables: the homogeneous reduction has FIXED the")
print("    member to Nariai = sigma's fixed point. So the S3 that lives on w is not in this Hilbert")
print("    space at all; the residual is at most the Z2 stabilizer of the fixed point, acting on the")
print("    (already-collapsed) root pair, not on the dynamical a. => quantizing it gives a standard")
print("    1-DOF quantum cosmology with NO standard-2d structure. SECTOR GAP, confirmed structurally.")
