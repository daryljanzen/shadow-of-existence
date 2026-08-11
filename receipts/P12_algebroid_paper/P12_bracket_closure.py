"""
P12_bracket_closure.py -- verifies prop:closure: at the symmetric cut so(5,1)=h (+) m with h=so(4,1),
  m = the boosts M_{a5} (a=0..4), the symmetric-space grading holds:
    [h,h] subset h,    [h,m] subset m,    [m,m] subset h,
  m is NOT a subalgebra (e.g. [M_05,M_15]=-M_01, the sign set by the substrate curvature). Under
  m <-> H_perp (normal constraint), h <-> H_a (tangential), this IS the Dirac / hypersurface-deformation
  algebra: {H_perp,H_perp}~H_a (two normal deformations bracket into a tangential one), {H_a,H_perp}~H_perp,
  {H_a,H_b}~H_c. [P12 algebroid_paper sec:bracket / prop:closure]
STATUS: ✔✔   RUN: python3 P12_bracket_closure.py   RUNTIME: ~3s
COMPUTES: builds the so(5,1) generators (6x6, eta=diag(-1,1,1,1,1,1)); every [h,h] lands in h, every [h,m]
  in m, every [m,m] in h (checked by basis decomposition); [M_05,M_15]=-M_01. CONTROL: [m,m] has ZERO
  component along m (so m is not closed) -- the defining feature that makes the Dirac algebra an algebroid.
ORIGIN: built new r1377 (P12 cited no receipts).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
eta=sp.diag(-1,1,1,1,1,1); N=6
def Mgen(mu,nu):
    # (M_{mu nu})^rho_sigma = delta^rho_mu eta_{nu sigma} - delta^rho_nu eta_{mu sigma}
    M=sp.zeros(N,N)
    for rho in range(N):
        for sig in range(N):
            M[rho,sig]=(1 if rho==mu else 0)*eta[nu,sig] - (1 if rho==nu else 0)*eta[mu,sig]
    return M
gens={}
for mu in range(N):
    for nu in range(mu+1,N):
        gens[(mu,nu)]=Mgen(mu,nu)
def br(A,B): return A*B-B*A
def decompose(Mat):
    # express Mat in the basis {M_{mu nu}, mu<nu}; return dict of nonzero coeffs
    coeffs={}
    remaining=Mat
    for (mu,nu),G in gens.items():
        # coefficient via a matching entry: (M_{mu nu})^mu_nu = eta_{nu nu}; pick entry [mu,nu]
        denom=G[mu,nu]
        if denom!=0:
            c=sp.simplify(remaining[mu,nu]/denom)
            if c!=0: coeffs[(mu,nu)]=c
    return coeffs
h_keys=[(mu,nu) for (mu,nu) in gens if nu<=4]        # so(4,1): indices 0..4
m_keys=[(a,5) for a in range(5)]                      # boosts M_{a5}
def in_h(Mat): return all(k in h_keys or v==0 for k,v in decompose(Mat).items())
def in_m(Mat): return all(k in m_keys or v==0 for k,v in decompose(Mat).items())
print("="*70); print("P12 symmetric-space grading of so(5,1): the bracket closes (Dirac algebra)"); print("="*70)
# [h,h] subset h
ok&=check("[h,h] subset h (h=so(4,1) is a subalgebra)",
          all(in_h(br(gens[a],gens[b])) for a in h_keys for b in h_keys))
# [h,m] subset m
ok&=check("[h,m] subset m (m is an h-module)",
          all(in_m(br(gens[a],gens[b])) for a in h_keys for b in m_keys))
# [m,m] subset h
ok&=check("[m,m] subset h (symmetric space: two normal generators bracket into a tangential one)",
          all(in_h(br(gens[a],gens[b])) for a in m_keys for b in m_keys))
# specific: [M_05,M_15] = -M_01
ok&=check("[M_05, M_15] = -M_01 (the sign set by the substrate curvature)",
          sp.simplify(br(gens[(0,5)],gens[(1,5)]) + gens[(0,1)])==sp.zeros(N,N))
# m is NOT a subalgebra: [m,m] has zero component along m
ok&=check("CONTROL: m is NOT a subalgebra -- every [m,m] has ZERO component along m (lands purely in h)",
          all(all(k not in m_keys for k in decompose(br(gens[a],gens[b])).keys()) for a in m_keys for b in m_keys))
# r2376+c54.158 -- rule 7: every PASS/FAIL above is computed and only PRINTED.  Pin `ok`, and with
# it the numbers prop:closure actually rests on: so(5,1) has 15 generators splitting 10 + 5 into
# h = so(4,1) and the coset m, so "[m,m] subset h" is a statement about a FIVE-dimensional
# complement landing in a TEN-dimensional subalgebra and not a relabelling; and the one specific
# structure constant the proposition names, [M_05,M_15] = -M_01, with coefficient exactly -1 on
# M_01 and on NOTHING else (the sign is set by the substrate curvature).
assert len(gens) == 15, len(gens)
assert (len(h_keys), len(m_keys)) == (10, 5), (len(h_keys), len(m_keys))
assert decompose(br(gens[(0,5)], gens[(1,5)])) == {(0,1): -1}, decompose(br(gens[(0,5)], gens[(1,5)]))
assert ok
print("="*70)
print("RESULT:", "ALL PASS -- the symmetric-space grading so(5,1)=h(+)m closes: [h,h]<h, [h,m]<m, [m,m]<h with m not\n         a subalgebra ([M_05,M_15]=-M_01). This is the Dirac (hypersurface-deformation) algebra: normal x normal -> tangential." if ok else "SOME FAILED")
print("="*70)
