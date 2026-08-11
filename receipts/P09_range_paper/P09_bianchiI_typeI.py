"""
P09_bianchiI_typeI.py -- verifies prop:typeI: the generic vacuum-Lambda Bianchi-I (anisotropic flat)
  cosmology ds^2=-dt^2+sum_i a_i(t)^2 dx_i^2 with a_i=sinh(3t)^{1/3} tanh(3t/2)^{C_i/3}, sum C_i=0,
  sum C_i^2=6, is vacuum-Lambda (Lambda=3, alpha=1) and Petrov TYPE I when the C_i are DISTINCT -- its
  electric Weyl tensor has three DISTINCT eigenvalues (discriminant != 0), so I^3 != 27 J^2. So algebraic
  type is no constraint on the operator's range: it reaches the generic (Type I) sector, not just the
  separable Type-D corner. [P9 range_paper sec:petrov / prop:typeI]
STATUS: ✔✔   RUN: python3 P09_bianchiI_typeI.py   RUNTIME: ~6s
COMPUTES: full curvature by the numeric GR pipeline (Christoffel->Riemann->Ricci->Weyl); R^mu_nu=3 delta
  (vacuum-Lambda); the electric Weyl E_ij=C_{titj}/(a_i a_j) is traceless with 3 distinct eigenvalues (Type I),
  and the speciality (discriminant) VARIES with t. CONTROL: two equal C_i (axisymmetric, e.g. (2,-1,-1)) is
  Type D -- two equal Weyl eigenvalues, discriminant = 0.
ORIGIN: built new r1365 (P9 cited no receipts).
"""
import sympy as sp, numpy as np
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
def weyl_eigs(Cvals, tt):
    t=sp.symbols('t', positive=True)
    a=[(sp.sinh(3*t))**sp.Rational(1,3)*(sp.tanh(3*t/2))**(sp.nsimplify(Cvals[i])/3) for i in range(3)]
    gsym=sp.diag(-1, a[0]**2, a[1]**2, a[2]**2)
    g_f=sp.lambdify(t, gsym,'numpy'); dg_f=sp.lambdify(t, sp.diff(gsym,t),'numpy')
    def christ(x):
        g=np.array(g_f(x),float); dg=np.array(dg_f(x),float); gi=np.linalg.inv(g); Ga=np.zeros((4,4,4))
        for A in range(4):
         for b in range(4):
          for c in range(4):
            Ga[A,b,c]=0.5*sum(gi[A,d]*((dg[d,c] if b==0 else 0)+(dg[d,b] if c==0 else 0)-(dg[b,c] if d==0 else 0)) for d in range(4))
        return Ga
    Ga=christ(tt); dGa=(christ(tt+1e-6)-christ(tt-1e-6))/2e-6; R=np.zeros((4,4,4,4))
    for A in range(4):
     for b in range(4):
      for c in range(4):
       for d in range(4):
        R[A,b,c,d]=(dGa[A,b,d] if c==0 else 0)-(dGa[A,b,c] if d==0 else 0)+sum(Ga[A,e,c]*Ga[e,b,d]-Ga[A,e,d]*Ga[e,b,c] for e in range(4))
    g=np.array(g_f(tt),float); gi=np.linalg.inv(g); Ric=np.einsum('abad->bd',R); Ricmix=gi@Ric
    Rl=np.einsum('ae,ebcd->abcd',g,R); Rs=float(np.einsum('bd,bd->',gi,Ric))
    Cw=np.zeros((4,4,4,4))
    for A in range(4):
     for b in range(4):
      for c in range(4):
       for d in range(4):
        Cw[A,b,c,d]=Rl[A,b,c,d]-0.5*(g[A,c]*Ric[b,d]-g[A,d]*Ric[b,c]-g[b,c]*Ric[A,d]+g[b,d]*Ric[A,c])+Rs/6*(g[A,c]*g[b,d]-g[A,d]*g[b,c])
    av=[np.sqrt(g[i,i]) for i in [1,2,3]]
    E=np.array([[Cw[0,i+1,0,j+1]/(av[i]*av[j]) for j in range(3)] for i in range(3)])
    eig=np.sort(np.linalg.eigvals(E).real)
    disc=float(np.prod([(eig[i]-eig[j])**2 for i in range(3) for j in range(i+1,3)]))
    return Ricmix, E, eig, disc
print("="*70); print("P09 Bianchi-I -> Petrov Type I (algebraic type is no constraint)"); print("="*70)
# (1) vacuum-Lambda for the DISTINCT-C_i (generic) case
Ric1,E1,eig1,disc1=weyl_eigs([sp.sqrt(3),0,-sp.sqrt(3)], 0.4)
ok&=check("distinct C_i=(sqrt3,0,-sqrt3): vacuum-Lambda R^mu_nu = 3 delta^mu_nu (Lambda=3)", np.allclose(Ric1, 3*np.eye(4), atol=1e-5))
# (2) electric Weyl traceless, 3 DISTINCT eigenvalues -> Type I
ok&=check(f"electric Weyl traceless (tr={np.trace(E1):.1e}) with 3 DISTINCT eigenvalues {np.round(eig1,4)} -> TYPE I",
          abs(np.trace(E1))<1e-6 and len(set(np.round(eig1,4)))==3 and disc1>1e-9)
# (3) speciality (discriminant) VARIES with t -> not fixed on the special locus
_,_,_,disc_a=weyl_eigs([sp.sqrt(3),0,-sp.sqrt(3)], 0.25)
_,_,_,disc_b=weyl_eigs([sp.sqrt(3),0,-sp.sqrt(3)], 0.8)
ok&=check(f"speciality varies with t (discriminant: {disc_a:.4f} @0.25, {disc1:.4f} @0.4, {disc_b:.4f} @0.8; all !=0 -> Type I throughout)",
          disc_a>1e-9 and disc1>1e-9 and disc_b>1e-9 and abs(disc_a-disc_b)>1e-3)
# (4) CONTROL: two equal C_i (axisymmetric) is Type D -- two equal Weyl eigenvalues, discriminant 0
Ric2,E2,eig2,disc2=weyl_eigs([2,-1,-1], 0.4)
ok&=check("CONTROL: axisymmetric C_i=(2,-1,-1) is vacuum-Lambda and TYPE D -- two equal Weyl eigenvalues, discriminant=0",
          np.allclose(Ric2,3*np.eye(4),atol=1e-5) and disc2<1e-9 and len(set(np.round(eig2,4)))==2)
print("="*70)
print("RESULT:", f"ALL PASS -- generic (distinct-C) Bianchi-I is vacuum-Lambda Petrov TYPE I (3 distinct Weyl\n         eigenvalues, I^3!=27J^2); the axisymmetric case is Type D. Algebraic type is no constraint on the range." if ok else "SOME FAILED")
print("="*70)

# ** r2376+c54.161 -- THE VERDICT, ASSERTED, PLUS PINS OF ITS OWN. **  Every check above printed
#   PASS or FAIL and nothing read the result: `ok` could go False with the receipt still exiting 0.
assert ok, "a check above printed FAIL -- see the transcript"
#   THE EXPONENT CONSTRAINT, PINNED: the a_i = sinh(3t)^{1/3} tanh(3t/2)^{C_i/3} family is
#   vacuum-Lambda only for sum C_i = 0 and sum C_i^2 = SIX -- the Kasner-like condition -- and
#   both the generic triple and the axisymmetric control satisfy it.
for _C in ([float(sp.sqrt(3)), 0.0, -float(sp.sqrt(3))], [2.0, -1.0, -1.0]):
    assert abs(sum(_C)) < 1e-12, _C
    assert abs(sum(c*c for c in _C) - 6.0) < 1e-12, _C
#   THE COSMOLOGICAL CONSTANT, PINNED: R^mu_nu = 3 delta^mu_nu means Lambda = 3 (alpha = 1), so
#   the Ricci scalar is 4 Lambda = 12 in both the Type-I and the Type-D case.
assert abs(float(np.trace(Ric1)) - 12.0) < 1e-4, np.trace(Ric1)
assert abs(float(np.trace(Ric2)) - 12.0) < 1e-4, np.trace(Ric2)
#   THE ALGEBRAIC TYPE, PINNED OFF THE ELECTRIC WEYL: traceless (three eigenvalues summing to
#   zero); THREE distinct in the generic case (Type I) and exactly TWO distinct in the
#   axisymmetric one (Type D), with the Type-D discriminant vanishing.
assert abs(float(np.trace(E1))) < 1e-6 and abs(float(np.trace(E2))) < 1e-6
assert abs(float(sum(eig1))) < 1e-6 and abs(float(sum(eig2))) < 1e-6
assert len(set(np.round(eig1, 4))) == 3 and len(set(np.round(eig2, 4))) == 2
assert disc1 > 1e-9 and abs(disc2) < 1e-9, (disc1, disc2)
#   and the Type-D pattern is the 2:-1:-1 one: the repeated eigenvalue is minus half the lone one.
_lone = [e for e in np.round(eig2, 6) if list(np.round(eig2, 6)).count(e) == 1][0]
_rep = [e for e in np.round(eig2, 6) if list(np.round(eig2, 6)).count(e) == 2][0]
assert abs(_rep/_lone - (-0.5)) < 1e-4, (_lone, _rep)
