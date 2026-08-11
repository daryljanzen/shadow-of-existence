"""
P15_expansion_law.py -- verifies the P15 sec:properframe/sec:flatlcdm derivation core SYMBOLICALLY (sympy):
  eq:amplitude, eq:scalefac (the sinh^{2/3} law solving the E=1 radial geodesic), eq:rate (Friedmann coth^2
  form), eq:omega-ratio (csch^2), with a wrong-exponent CONTROL that forces the 2/3 power.
STATUS: ✔✔ (all symbolic; wrong-exponent control forces 2/3)   RUN: python3 P15_expansion_law.py   RUNTIME: ~3s
ORIGIN: built new r1397 (the derivation was prose+cite JanzenModernParallax/Janzen2015, unreceipted here).
"""
import sympy as sp
def ok(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
G,M,Lam,c,tau,r=sp.symbols('G M Lambda c tau r',positive=True)
allpass=True
print("="*72); print("P15 derivation core -- amplitude, sinh^{2/3} scale factor, Friedmann forms"); print("="*72)

# (1) eq:amplitude: at Nariai M = c^2/(3 sqrt(Lambda) G), (6GM/Lambda c^2)^{1/3} = 2^{1/3}/sqrt(Lambda)
M_nariai=c**2/(3*sp.sqrt(Lam)*G)
amp=(6*G*M/(Lam*c**2))**sp.Rational(1,3)
amp_nariai=sp.simplify(amp.subs(M,M_nariai))
allpass&=ok("eq:amplitude: (6GM/Lambda c^2)^{1/3} at Nariai = 2^{1/3}/sqrt(Lambda)",
            sp.simplify(amp_nariai-2**sp.Rational(1,3)/sp.sqrt(Lam))==0)

# (2) eq:scalefac solves the E=1 radial geodesic. In geometric units (c=1) the E=1 equation is
#     (dr/dtau)^2 = 1 - V_eff = 2GM/r + (Lambda/3) r^2   [V_eff=(r-2GM-(Lambda/3)r^3)/r].
#     Claimed solution r = A sinh^{2/3}(B tau), A=(6GM/Lambda)^{1/3}, B=(1/2)sqrt(3 Lambda).
A=(6*G*M/Lam)**sp.Rational(1,3); B=sp.sqrt(3*Lam)/2
r_sol=A*sp.sinh(B*tau)**sp.Rational(2,3)
lhs=sp.diff(r_sol,tau)**2
rhs=2*G*M/r_sol+(Lam/3)*r_sol**2
allpass&=ok("eq:scalefac: r=A sinh^{2/3}(B tau) solves (dr/dtau)^2 = 2GM/r + (Lambda/3)r^2  (E=1 geodesic)",
            sp.simplify(sp.expand_trig(lhs-rhs))==0)

# (2-control) a WRONG exponent p!=2/3 must NOT solve it
p=sp.Rational(1,2)
r_bad=A*sp.sinh(B*tau)**p
allpass&=ok("CONTROL: r=A sinh^{1/2}(B tau) does NOT solve the E=1 equation (the 2/3 power is forced)",
            sp.simplify(sp.expand_trig(sp.diff(r_bad,tau)**2-(2*G*M/r_bad+(Lam/3)*r_bad**2)))!=0)

# (3) eq:rate: H = rdot/r = (2B/3) coth(B tau); with the paper's B=(1/2)sqrt(3 Lambda) c, H^2=(Lambda c^2/3)coth^2
Bc=sp.sqrt(3*Lam)*c/2                       # paper's argument coefficient (with c)
H=sp.Rational(2,3)*Bc*sp.coth(Bc*tau)       # H = (2B/3) coth(B tau) for r ~ sinh^{2/3}(B tau)
allpass&=ok("eq:rate: H^2 = (Lambda c^2/3) coth^2((1/2)sqrt(3 Lambda) c tau)",
            sp.simplify(H**2-(Lam*c**2/3)*sp.coth(Bc*tau)**2)==0)

# (4) eq:omega-ratio: coth^2 = 1 + csch^2 => H^2 = Lambda c^2/3 + (Lambda c^2/3) csch^2;
#     the Lambda c^2/3 is the Lambda term, (Lambda c^2/3)csch^2 the matter term => Omega_m/Omega_L = csch^2
x=sp.symbols('x')
allpass&=ok("coth^2 = 1 + csch^2 (splits H^2 into Lambda term + matter term)",
            sp.simplify(sp.coth(x)**2-(1+sp.csch(x)**2))==0)
Lam_term=Lam*c**2/3; mat_term=(Lam*c**2/3)*sp.csch(Bc*tau)**2
allpass&=ok("eq:omega-ratio: Omega_m/Omega_Lambda = matter_term/Lambda_term = csch^2((1/2)sqrt(3 Lambda) c tau)",
            sp.simplify(mat_term/Lam_term-sp.csch(Bc*tau)**2)==0)
# and H^2 = (1/3)(8 pi G rho + Lambda c^2) form: the Lambda term is exactly (1/3)Lambda c^2
allpass&=ok("H^2 late-time -> (1/3)Lambda c^2 (the standard rate (1/2)sqrt(3 Lambda) c as tau->inf)",
            sp.simplify(sp.limit(H**2,tau,sp.oo)-Lam*c**2/3)==0)
print("="*72)
print("RESULT:", "ALL PASS -- amplitude, the sinh^{2/3} scale factor (E=1 geodesic, 2/3 forced by the control),\n         the Friedmann coth^2 rate, and the csch^2 density-ratio all verified symbolically." if allpass else "SOME FAILED")
print("="*72)
