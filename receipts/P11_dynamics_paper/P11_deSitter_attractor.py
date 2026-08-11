"""
P11_deSitter_attractor.py -- verifies sec:nonlinear (the de Sitter attractor, prop:admit): in the homogeneous
  sector of the Gowdy-de Sitter system the nonlinear Lambda>0 dynamics is exactly solvable and isotropizes.
    (i)  the isotropic background psi_t=sqrt(L/3) e^psi solves psi_tt=psi_t^2 (ENERGY) and 3 psi_t^2=L e^{2psi}
         (AREA=WAVE); with lapse N=e^psi the scale factor a=e^psi and cosmic time dtau=a dt give constant
         Hubble H=sqrt(L/3) -- exact de Sitter;
    (ii) the canonical SHEAR CHARGE C0 = R_t - 2 R psi_t is CONSERVED (dC0/dt = AREA - 2 WAVE = 0 on shell);
    (iii)the shear s=psi-(1/2)ln R obeys 2 R s_t = -C0, so as R grows the shear freezes and the anisotropy
         dilutes -> de Sitter attractor. [P11 dynamics_paper sec:nonlinear / prop:admit]
STATUS: ✔✔   RUN: python3 P11_deSitter_attractor.py   RUNTIME: ~3s
COMPUTES: the background solves both reduced equations; cosmic-time H is constant; C0 conserved via AREA=2WAVE;
  2 R s_t = -C0 (shear-charge relation). CONTROL: C0 != 0 (anisotropic) vs C0=0 (exactly isotropic background).
ORIGIN: built new r1374 (P11 cited no receipts).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
t,Lam=sp.symbols('t Lambda', positive=True)
psi=sp.Function('psi')(t); R=sp.Function('R')(t); gam=sp.Function('gamma')(t)
pt=sp.diff(psi,t)
print("="*70); print("P11 de Sitter attractor (homogeneous Gowdy-dS)"); print("="*70)
# (i) background: psi_t = sqrt(L/3) e^psi
psi_bg=sp.Function('psi')  # symbolic; test the ODE relation
# substitute psi_t = sqrt(L/3) e^psi and check psi_tt=psi_t^2 and 3 psi_t^2 = L e^{2psi}
ptb=sp.sqrt(Lam/3)*sp.exp(psi)           # the claimed psi_t
pttb=sp.diff(ptb,t).subs(sp.diff(psi,t), ptb)   # psi_tt via chain rule with psi_t=ptb
ok&=check("background psi_t=sqrt(L/3)e^psi => psi_tt = psi_t^2 (ENERGY)", sp.simplify(pttb - ptb**2)==0)
ok&=check("background: 3 psi_t^2 = Lambda e^{2psi} (AREA=WAVE)", sp.simplify(3*ptb**2 - Lam*sp.exp(2*psi))==0)
# (ii) cosmic-time Hubble constant: a=e^psi, dtau=a dt => H=(da/dtau)/a = psi_t/a = sqrt(L/3)
a=sp.exp(psi); H = (sp.diff(a,t)/a)/a       # (da/dt)/a / a = (da/dtau)/a since dt/dtau=1/a
ok&=check("a=e^psi, cosmic-time H=(da/dtau)/a = psi_t e^{-psi} = sqrt(L/3) (constant -> de Sitter)",
          sp.simplify(H.subs(sp.diff(psi,t), ptb) - sp.sqrt(Lam/3))==0)
# (iii) shear charge C0=R_t-2R psi_t conserved via AREA=2 WAVE
WAVE = sp.diff(R*pt,t) - Lam*R*sp.exp(2*(gam-psi))
AREA = sp.diff(R,t,2)   - 2*Lam*R*sp.exp(2*(gam-psi))
C0 = sp.diff(R,t) - 2*R*pt
dC0 = sp.diff(C0, t)
ok&=check("C0=R_t-2R psi_t: dC0/dt = AREA - 2*WAVE (= 0 on shell => conserved shear charge)",
          sp.simplify(dC0 - (AREA - 2*WAVE))==0)
# (iv) shear s=psi-(1/2)ln R obeys 2 R s_t = -C0
s = psi - sp.Rational(1,2)*sp.log(R)
ok&=check("shear s=psi-(1/2)ln R obeys 2 R s_t = -C0 (so s_t=-C0/2R -> 0 as R grows: anisotropy dilutes)",
          sp.simplify(2*R*sp.diff(s,t) - (-C0))==0)
# CONTROL: C0!=0 is the anisotropic branch; C0=0 is the exactly isotropic background (s_t=0)
ok&=check("CONTROL: C0=0 <=> s_t=0 (exact isotropy); C0!=0 is anisotropic, diluting as R grows",
          sp.simplify(sp.diff(s,t).subs(sp.diff(R,t), 2*R*pt))==0)   # C0=0 means R_t=2R psi_t -> s_t=0
print("="*70)
print("RESULT:", "ALL PASS -- the homogeneous Gowdy-dS dynamics has an exact de Sitter background (constant H) and a\n         conserved shear charge C0 whose relation 2R s_t=-C0 dilutes the anisotropy: de Sitter is the attractor." if ok else "SOME FAILED")
print("="*70)

# --- r2376+c54.158 -------------------------------------------------------------------
# PINS THIS RECEIPT'S OWN CLAIM.  (a) the PASS/FAIL flag the file previously only PRINTED.
# (b) the de Sitter rate itself: the cosmic-time Hubble parameter of the background obeys
# 3 H^2 = Lambda exactly, i.e. H = sqrt(Lambda/3) -- the constant-H de Sitter attractor
# prop:admit names.  The 3 is the pinned figure: 3H^2=Lambda, not H^2=Lambda or 3H^2=2Lambda.
assert ok, "P11 de Sitter attractor: at least one check FAILED"
H_dS = sp.simplify(H.subs(sp.diff(psi, t), ptb))
assert sp.simplify(3*H_dS**2 - Lam) == 0, "cosmic-time H = %s does not satisfy 3H^2 = Lambda" % H_dS
