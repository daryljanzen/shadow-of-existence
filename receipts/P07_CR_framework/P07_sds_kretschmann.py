"""
P07_sds_kretschmann.py -- verifies P7's "Perspectival Singularity" Kretschmann claim, by COMPUTING the
  Kretschmann scalar of the SdS metric ds^2=-f dt^2+dr^2/f+r^2 dOmega^2, f=1-2M/r-Lambda r^2/3, from the
  metric (Christoffels -> Riemann R^a_bcd -> R_abcd -> R^abcd -> contraction), NOT asserting the value:
    [sec:null-boundary-correspondence rem "Perspectival Singularity" (L837); sec:sds-cosmology L682]
    (i)   K = R_abcd R^abcd = 48 M^2/r^6 + 8 Lambda^2/3 = 48 M^2/r^6 + 24/alpha^4  (alpha^2=3/Lambda);
          dimensionful  K = 48 G^2 M^2 / c^4 r^6 + 24/alpha^4;
    (ii)  the r=0 divergence is the M-term ALONE (48 M^2/r^6); the M->0 de Sitter remainder is the
          CONSTANT 24/alpha^4, regular everywhere including r=0;
    (iii) the metric function splits even/odd under the backward-radial reflection r -> -r:
          f_even = 1 - r^2/alpha^2 (the invariant de Sitter part), f_odd = -2M/r (the Schwarzschild part
          the reflection reverses) -- so the r=0 singularity rides the perspectival (odd, mass) reading.
  [P7 CR_framework -- the Kretschmann + its even/odd decomposition]
STATUS: ✔✔   RUN: python3 P07_sds_kretschmann.py   RUNTIME: ~12s
COMPUTES: the full Riemann tensor of SdS from the metric and contracts it to K; then reads off the M and
  Lambda pieces and the even/odd parts of f.
CONTROL: M=0 (pure de Sitter) => K collapses to the constant 24/alpha^4, FINITE at r=0 (no divergence);
  the divergence appears only when M!=0 and lives entirely in the 48M^2/r^6 term. (A Schwarzschild control
  Lambda=0 => K=48M^2/r^6, the pure r^-6 pole.)
BOUND: distinct from P2 `kretschmann_chain_rule`, which computes the SCHWARZSCHILD K=48M^2/r^6 (Lambda=0,
  the cycloid chart-artefact reading) -- NOT the SdS value, the 24/alpha^4 de Sitter remainder, or the
  even/odd split. This receipt is the SdS Kretschmann + its perspectival (even/odd) decomposition.
ORIGIN: built new (fork r1364e) -- P7's Perspectival-Singularity Kretschmann claim was unreceipted
  (COMPLETENESS_AUDIT.md, C6; adjudicated genuine-gap vs P2 at source).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
t,r,th,ph,M,Lam,alpha = sp.symbols('t r theta phi M Lambda alpha', positive=True)
f = 1 - 2*M/r - Lam*r**2/3
x=[t,r,th,ph]; n=4
g = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2)
gi = g.inv()
print("="*74); print("P07 SdS Kretschmann (Riemann computed from the metric, then contracted)"); print("="*74)

# Christoffel ^a_bc
Gam=[[[sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],x[cc])+sp.diff(g[d,cc],x[b])-sp.diff(g[b,cc],x[d])) for d in range(n))/2)
       for cc in range(n)] for b in range(n)] for a in range(n)]
# Riemann R^a_{bcd} = d_c Gam^a_bd - d_d Gam^a_bc + Gam^a_ce Gam^e_bd - Gam^a_de Gam^e_bc
def Riem(a,b,cc,d):
    return sp.simplify(sp.diff(Gam[a][b][d],x[cc]) - sp.diff(Gam[a][b][cc],x[d])
        + sum(Gam[a][cc][e]*Gam[e][b][d] for e in range(n))
        - sum(Gam[a][d][e]*Gam[e][b][cc] for e in range(n)))
R_ud = [[[[Riem(a,b,cc,d) for d in range(n)] for cc in range(n)] for b in range(n)] for a in range(n)]
# lower: R_{abcd} = g_ae R^e_{bcd}
R_dddd = [[[[sp.simplify(sum(g[a,e]*R_ud[e][b][cc][d] for e in range(n))) for d in range(n)] for cc in range(n)] for b in range(n)] for a in range(n)]
# raise all: R^{abcd}
R_uuuu = [[[[sp.simplify(sum(gi[a,ai]*gi[b,bi]*gi[cc,ci]*gi[d,di]*R_dddd[ai][bi][ci][di]
             for ai in range(n) for bi in range(n) for ci in range(n) for di in range(n)))
             for d in range(n)] for cc in range(n)] for b in range(n)] for a in range(n)]
K = sp.simplify(sum(R_dddd[a][b][cc][d]*R_uuuu[a][b][cc][d] for a in range(n) for b in range(n) for cc in range(n) for d in range(n)))
K = sp.simplify(K)

# (i) the value
K_claim = 48*M**2/r**6 + sp.Rational(8,3)*Lam**2
ok&=check("K = R_abcd R^abcd = 48 M^2/r^6 + 8 Lambda^2/3   (COMPUTED from the metric)",
          sp.simplify(K - K_claim)==0)
ok&=check("in terms of alpha (Lambda=3/alpha^2):  8 Lambda^2/3 = 24/alpha^4",
          sp.simplify(sp.Rational(8,3)*Lam**2 - 24/alpha**4).subs(Lam, 3/alpha**2)==0)
ok&=check("so  K = 48 M^2/r^6 + 24/alpha^4  (dimensionful 48 G^2M^2/c^4 r^6 + 24/alpha^4)",
          sp.simplify(K.subs(Lam,3/alpha**2) - (48*M**2/r**6 + 24/alpha**4))==0)

# (ii) the divergence is the M-term alone; the de Sitter remainder is regular
K_dS = sp.simplify(K.subs(M,0))                        # M->0 de Sitter
ok&=check("M->0 (pure de Sitter): K = 8 Lambda^2/3 = 24/alpha^4, a CONSTANT (no r-dependence)",
          sp.simplify(sp.diff(K_dS, r))==0 and sp.simplify(K_dS - sp.Rational(8,3)*Lam**2)==0)
ok&=check("de Sitter remainder is FINITE at r=0 (regular)", sp.limit(K_dS, r, 0) == sp.Rational(8,3)*Lam**2)
ok&=check("the r=0 divergence is the M-term ALONE (48 M^2/r^6 -> oo, the rest finite)",
          sp.limit(K - K_dS, r, 0) == sp.oo)
# CONTROL: Schwarzschild Lambda=0 => K = 48 M^2/r^6 (the pure pole, P2's object)
ok&=check("CONTROL: Lambda=0 (Schwarzschild) => K = 48 M^2/r^6 (pure r^-6 pole)",
          sp.simplify(K.subs(Lam,0) - 48*M**2/r**6)==0)
# CONTROL: break the coefficient -- 47 M^2/r^6 is NOT the Kretschmann
ok&=check("CONTROL: the coefficient is 48, not 47 (a wrong coeff fails)", sp.simplify(K - (47*M**2/r**6 + sp.Rational(8,3)*Lam**2))!=0)

# (iii) even/odd split of f under r -> -r
f_even = sp.simplify((f + f.subs(r,-r))/2)
f_odd  = sp.simplify((f - f.subs(r,-r))/2)
ok&=check("f_even (r->-r invariant) = 1 - r^2/alpha^2  (the de Sitter part)",
          sp.simplify(f_even - (1 - r**2/alpha**2)).subs(Lam,3/alpha**2)==0)
ok&=check("f_odd (r->-r reversed) = -2M/r  (the Schwarzschild part)", sp.simplify(f_odd - (-2*M/r))==0)
ok&=check("the singularity rides f_odd: the divergent K-term is carried by the odd (mass) part, "
          "the even (dS) part regular", sp.limit(48*M**2/r**6, r, 0)==sp.oo and sp.limit(K_dS,r,0)!=sp.oo)

print("="*74)
print("RESULT:", "ALL PASS -- K=48M^2/r^6+24/alpha^4 computed from the SdS metric; the r=0 divergence is the\n"
      "         mass term alone, the de Sitter remainder the regular constant 24/alpha^4; f splits even/odd\n"
      "         under r->-r into the invariant dS part and the perspectival (reversed) Schwarzschild part."
      if ok else "SOME FAILED")
print("="*74)

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS.  Every check above only PRINTED [PASS]/[FAIL] into `ok`, so the
# run exited 0 whatever the Riemann computation returned; `ok` is asserted here.  Added on top:
# the computed K evaluated NUMERICALLY at a point, K(M=1, alpha=1, r=2) = 48/64 + 24 = 24.75,
# so a wrong coefficient in either term is caught by a single number; the r^-6 rate of the
# divergence (r -> r/2 multiplies the mass term by 64); and the even/odd split checked as a
# function identity under r -> -r rather than only as a simplification to zero.
assert ok, "P07_sds_kretschmann: one of the printed checks FAILED"
assert abs(float(K.subs({M: 1, Lam: 3, r: 2})) - 24.75) < 1e-12
assert abs(float(K.subs({M: 1, Lam: 3, r: 1})) - 72.0) < 1e-12
assert abs(float((K - K_dS).subs({M: 1, Lam: 3, r: 1})/(K - K_dS).subs({M: 1, Lam: 3, r: 2})) - 64.0) < 1e-9
assert abs(float(K_dS.subs(Lam, 3)) - 24.0) < 1e-12                 # 24/alpha^4 at alpha = 1
assert sp.simplify(f - (f_even + f_odd)) == 0
assert sp.simplify(f_even.subs(r, -r) - f_even) == 0                # even under r -> -r
assert sp.simplify(f_odd.subs(r, -r) + f_odd) == 0                  # odd under r -> -r
assert sp.simplify(K.subs(r, -r) - K) == 0                          # so K itself is EVEN
print("  [r2376+c54.161] `ok` asserted; plus K(M=1, alpha=1, r=2) = 24.75 and K(r=1) = 72.0 as")
print("  numbers, the mass term's r^-6 rate (x64 from r=2 to r=1), and the even/odd split checked")
print("  as an identity under r -> -r.")
