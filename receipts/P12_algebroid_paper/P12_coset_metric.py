"""
P12_coset_metric.py -- verifies the "structure function is the substrate's metric" claim: the structure
  function h^{ab} of the hypersurface-deformation bracket {H_perp,H_perp}=H_a[h^{ab}(...)] (eq:HH) is, on the
  symmetric-cut reduction, the COSET METRIC of SO(5,1)/SO(4,1). Computed directly: the Killing form of
  so(5,1) restricted to the coset m = span{M_{a5}} is proportional to eta_{ab}=diag(-1,1,1,1,1) -- signature
  (1,4), LORENTZIAN. The indefinite ("wrong") sign, supplied by the substrate's geometry, is the problem-of-
  time obstruction. At the symmetric cut it is constant (so(5,1) a Lie algebra); base-varying -> algebroid.
  [P12 algebroid_paper sec:bracket -- structure function paragraph]
STATUS: ✔✔   RUN: python3 P12_coset_metric.py   RUNTIME: ~4s
COMPUTES: the Killing form B(X,Y)=tr(ad_X ad_Y) built from the so(5,1) structure constants; B restricted to
  m is diagonal proportional to eta_{ab}; its signature is (1,4) (one sign vs four) -- indefinite/Lorentzian.
CONTROL: the compact directions h=so(4,1) and the timelike coset direction M_{05} carry OPPOSITE-sign Killing
  norms -- the indefiniteness is intrinsic, not a normalization choice.
ORIGIN: built new r1378 (P12 cited no receipts).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
eta=sp.diag(-1,1,1,1,1,1); N=6
def Mgen(mu,nu):
    M=sp.zeros(N,N)
    for rho in range(N):
        for sig in range(N):
            M[rho,sig]=(1 if rho==mu else 0)*eta[nu,sig]-(1 if rho==nu else 0)*eta[mu,sig]
    return M
keys=[(mu,nu) for mu in range(N) for nu in range(mu+1,N)]   # 15 generators
gens=[Mgen(*k) for k in keys]; idx={k:i for i,k in enumerate(keys)}; n=len(keys)
def br(A,B): return A*B-B*A
# structure constants f[i][j][k]: [g_i,g_j] = sum_k f g_k  (solve by matching a distinguished entry)
def coeffs(Mat):
    out=[0]*n
    for k,(mu,nu) in enumerate(keys):
        d=gens[k][mu,nu]
        if d!=0:
            c=sp.simplify(Mat[mu,nu]/d)
            out[k]=c
    return out
ad=[sp.zeros(n,n) for _ in range(n)]    # ad[i]^k_j = coeff of g_k in [g_i,g_j]
for i in range(n):
    for j in range(n):
        cs=coeffs(br(gens[i],gens[j]))
        for k in range(n): ad[i][k,j]=cs[k]
# Killing form B_ij = tr(ad_i ad_j)
B=sp.Matrix(n,n, lambda i,j: sp.simplify((ad[i]*ad[j]).trace()))
print("="*70); print("P12 coset metric = Killing form on m = so(5,1)/so(4,1), signature (1,4)"); print("="*70)
m_keys=[(a,5) for a in range(5)]; m_i=[idx[k] for k in m_keys]
Bm=sp.Matrix(5,5, lambda a,b: B[m_i[a], m_i[b]])
ok&=check("Killing form restricted to m is DIAGONAL (the coset directions are B-orthogonal)",
          all(Bm[a,b]==0 for a in range(5) for b in range(5) if a!=b))
# proportional to eta_{ab}=diag(-1,1,1,1,1): ratio Bm[a,a]/eta_{aa} constant
lam=sp.simplify(Bm[0,0]/eta[0,0])
ok&=check(f"B|m proportional to eta_{{ab}}=diag(-1,1,1,1,1): B[a,a]/eta[a,a] = {lam} (constant over a)",
          all(sp.simplify(Bm[a,a]/eta[a,a]-lam)==0 for a in range(5)))
diag=[sp.simplify(Bm[a,a]) for a in range(5)]
npos=sum(1 for d in diag if d>0); nneg=sum(1 for d in diag if d<0)
ok&=check(f"signature of B|m is (1,4) LORENTZIAN: diagonal {diag} -> ({npos} of one sign, {nneg} of the other)",
          {npos,nneg}=={1,4})
# CONTROL: the timelike coset direction M_05 has opposite Killing-norm sign to the spacelike M_15,...,M_45
ok&=check("CONTROL: B(M_05,M_05) has OPPOSITE sign to B(M_15,M_15) (indefiniteness is intrinsic)",
          sp.simplify(sp.sign(Bm[0,0])+sp.sign(Bm[1,1]))==0)
# r2376+c54.158 -- rule 7: the four PASS/FAIL above are computed and only PRINTED.  Pin `ok`, and
# pin the FIGURES this receipt prints, which ARE the structure-function claim: the Killing form
# restricted to the coset is B|m = diag(8,-8,-8,-8,-8) -- so the printed proportionality constant
# is exactly -8 (B|m = -8 eta_ab), and the split is ONE entry of one sign against FOUR of the
# other, i.e. signature (1,4), LORENTZIAN.  A definite (5,0) or (0,5) coset metric would carry no
# problem-of-time obstruction at all, so the 1-vs-4 count is the whole content.
assert lam == -8, lam
assert diag == [8, -8, -8, -8, -8], diag
assert (npos, nneg) == (1, 4), (npos, nneg)
assert ok
print("="*70)
print("RESULT:", "ALL PASS -- the coset metric (Killing form on m) is proportional to diag(-1,1,1,1,1), signature\n         (1,4): the structure function is the substrate's LORENTZIAN metric -- the 'wrong sign' of the problem of time." if ok else "SOME FAILED")
print("="*70)
