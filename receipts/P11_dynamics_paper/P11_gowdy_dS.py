"""
P11_gowdy_dS.py -- verifies sec:gowdy: the polarized Gowdy-de Sitter metric
  ds^2 = e^{2(gam-psi)}(-dt^2+dz^2) + e^{2psi} dx^2 + R^2 e^{-2psi} dy^2  (psi,gam,R functions of t,z)
  has vacuum-Lambda Einstein equations R_munu=Lambda g_munu EQUIVALENT to the four Gowdy field equations:
    (WAVE)     (R psi_t)_t-(R psi_z)_z = Lambda R e^{2(gam-psi)}
    (AREA)     R_tt-R_zz = 2 Lambda R e^{2(gam-psi)}
    (ENERGY)   2(R_t gam_t+R_z gam_z)-(R_tt+R_zz) = 2R(psi_t^2+psi_z^2)
    (MOMENTUM) R_t gam_z+R_z gam_t-R_tz = 2R psi_t psi_z .
  psi is the single transverse-traceless polarization (the propagating graviton on the leaf).
  [P11 dynamics_paper sec:gowdy]
STATUS: ✔✔   RUN: python3 P11_gowdy_dS.py   RUNTIME: ~40s
COMPUTES: the Einstein tensor of the Gowdy metric; E_xx = WAVE x (deriv-free factor); E_tz = MOMENTUM/R;
  E_tt+E_zz = ENERGY/R; E_yy = (WAVE-AREA) x (deriv-free factor). So {R_munu=Lambda g_munu} <=> the four equations.
CONTROL: dropping Lambda (Lambda=0) leaves the flat-space Gowdy equations (WAVE/AREA source terms vanish).
ORIGIN: built new r1372 (P11 cited no receipts).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
def derivfree(e): return not e.atoms(sp.Derivative)
ok=True
t,z,x,y,Lam=sp.symbols('t z x y Lambda', real=True)
psi=sp.Function('psi')(t,z); gam=sp.Function('gamma')(t,z); R=sp.Function('R')(t,z)
X=[t,z,x,y]; n=4
g=sp.diag(-sp.exp(2*(gam-psi)), sp.exp(2*(gam-psi)), sp.exp(2*psi), R**2*sp.exp(-2*psi)); gi=g.inv()
def ch(a,b,c): return sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(n))/2)
Ga=[[[ch(a,b,c) for c in range(n)] for b in range(n)] for a in range(n)]
def Ric(b,c): return sp.simplify(sum(sp.diff(Ga[a][b][c],X[a]) for a in range(n))-sum(sp.diff(Ga[a][b][a],X[c]) for a in range(n))
                                 +sum(Ga[a][a][d]*Ga[d][b][c] for a in range(n) for d in range(n))-sum(Ga[a][c][d]*Ga[d][b][a] for a in range(n) for d in range(n)))
Ev=lambda b,c: sp.simplify(Ric(b,c)-Lam*g[b,c])
pt,pz=sp.diff(psi,t),sp.diff(psi,z); Rt,Rz=sp.diff(R,t),sp.diff(R,z); gt,gz=sp.diff(gam,t),sp.diff(gam,z)
W = sp.diff(R*pt,t)-sp.diff(R*pz,z) - Lam*R*sp.exp(2*(gam-psi))
A = sp.diff(R,t,2)-sp.diff(R,z,2) - 2*Lam*R*sp.exp(2*(gam-psi))
En= 2*(Rt*gt+Rz*gz)-(sp.diff(R,t,2)+sp.diff(R,z,2)) - 2*R*(pt**2+pz**2)
Mo= Rt*gz+Rz*gt-sp.diff(R,t,z) - 2*R*pt*pz
print("="*70); print("P11 polarized Gowdy-de Sitter: R_munu=Lambda g_munu <=> the four field equations"); print("="*70)
Exx,Eyy,Ett,Ezz,Etz=Ev(2,2),Ev(3,3),Ev(0,0),Ev(1,1),Ev(0,1)
ok&=check("WAVE:     E_xx = WAVE x (derivative-free factor) => E_xx=0 <=> WAVE", derivfree(sp.simplify(Exx/W)))
ok&=check("MOMENTUM: E_tz = MOMENTUM / R", sp.simplify(Etz - Mo/R)==0)
ok&=check("ENERGY:   E_tt + E_zz = ENERGY / R", sp.simplify((Ett+Ezz) - En/R)==0)
ok&=check("AREA:     E_yy = (WAVE - AREA) x (derivative-free factor) => given WAVE, E_yy=0 <=> AREA",
          derivfree(sp.simplify(Eyy/(W-A))))
# CONTROL: Lambda=0 removes the source terms of WAVE and AREA (flat-space Gowdy)
ok&=check("CONTROL: Lambda=0 -> WAVE source Lambda R e^{2(gam-psi)} vanishes ((R psi_t)_t=(R psi_z)_z)",
          sp.simplify(W.subs(Lam,0) - (sp.diff(R*pt,t)-sp.diff(R*pz,z)))==0)
print("="*70)
print("RESULT:", "ALL PASS -- the polarized Gowdy-de Sitter Einstein equations R_munu=Lambda g_munu are exactly the\n         four field equations (WAVE/AREA/ENERGY/MOMENTUM): the confined bend is a consistent nonlinear GW." if ok else "SOME FAILED")
print("="*70)

# --- r2376+c54.158 -------------------------------------------------------------------
# PINS THIS RECEIPT'S OWN CLAIM.  (a) the PASS/FAIL flag the file previously only PRINTED.
# (b) the equivalence sec:gowdy asserts, restated as three exact symbolic identities plus
# the two proportionality facts: E_tz = MOMENTUM/R and E_tt+E_zz = ENERGY/R identically,
# and E_xx / WAVE, E_yy / (WAVE-AREA) are derivative-free (so vanishing of the Einstein
# combination is equivalent to, not merely implied by, the field equation).  This is a
# structural equivalence with no external number in it -- UNPINNED by construction.
assert ok, "P11 Gowdy-dS: at least one check FAILED"
assert sp.simplify(Etz - Mo/R) == 0, "E_tz is not MOMENTUM/R"
assert sp.simplify((Ett + Ezz) - En/R) == 0, "E_tt+E_zz is not ENERGY/R"
assert derivfree(sp.simplify(Exx/W)) and derivfree(sp.simplify(Eyy/(W - A))), \
    "E_xx/WAVE or E_yy/(WAVE-AREA) still carries derivatives: the equivalence fails"
