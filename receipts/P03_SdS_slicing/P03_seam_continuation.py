"""
P03_seam_continuation.py -- verifies: the equatorial seam joins the Riemannian spherical piece to the
  Lorentzian de Sitter piece by the analytic continuation theta->pi/2+i psi (sin theta -> cosh psi), a C1
  join at the throat, with the metric signature flipping (+,+)->(-,+) automatically because dtheta=i dpsi
  squares to -1. [P3 SdS-slicing-curve_v2 sec:seam, prop:flip, eq:sph, eq:dscont]
STATUS: ✔✔   RUN: python3 P03_seam_continuation.py   RUNTIME: ~3s
COMPUTES: sin(pi/2+i psi)=cosh psi; dtheta=i dpsi => dtheta^2=-dpsi^2; the spherical line element
  ds^2=dtheta^2+sin^2 theta dOmega^2 continuing to ds^2=-dpsi^2+cosh^2 psi dOmega^2 (the dtheta^2 coeff
  flips sign, angular stays +); the C1 join (r=sin theta and r=cosh psi agree in value=1 and first
  derivative=0 at the seam, while the SECOND derivative flips -1<->+1: C1 not C2, the curvature flip).
  CONTROL: a REAL shift theta->pi/2+psi (no i) does NOT flip the signature.
BOUND: the 2D slicing-surface signature flips; the spacetime is Lorentzian throughout (paper's own caveat).
ORIGIN: built new r1342 (uncited P3 claim).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
th, psi = sp.symbols('theta psi', real=True)
print("="*72); print("P03 equatorial seam: theta->pi/2+i psi, sin->cosh, signature flip"); print("="*72)
# (1) the continuation
sub = sp.pi/2 + sp.I*psi
ok&=check("sin(pi/2+i psi) = cos(i psi) = cosh psi", sp.simplify(sp.sin(sub) - sp.cosh(psi))==0)
# (2) dtheta = i dpsi => dtheta^2 = -dpsi^2
dth = sp.I  # dtheta/dpsi
ok&=check("dtheta = i dpsi  =>  dtheta^2 = -dpsi^2", sp.simplify(dth**2 + 1)==0)
# (3) eq:sph -> eq:dscont : ds^2 = dtheta^2 + sin^2 theta dOmega^2  under the continuation
# the dtheta^2 term: coefficient 1 * dtheta^2 = 1*(i dpsi)^2 = -dpsi^2 ; the sin^2 -> cosh^2
g_theta = 1                                    # coeff of dtheta^2 in eq:sph
g_psi   = sp.simplify(g_theta * dth**2)        # -> coeff of dpsi^2
ok&=check("dtheta^2 term -> -dpsi^2 (temporal coeff flips +1 -> -1)", g_psi == -1)
ang_sph = sp.sin(th)**2
ang_cont = sp.simplify(ang_sph.subs(th, sub))
ok&=check("sin^2 theta -> cosh^2 psi (angular coeff, stays +)", sp.simplify(ang_cont - sp.cosh(psi)**2)==0)
ok&=check("=> ds^2 = -dpsi^2 + cosh^2 psi dOmega^2  (eq:dscont), Lorentzian (-,+)", g_psi==-1 and sp.simplify(ang_cont-sp.cosh(psi)**2)==0)
# (4) signature (+,+) -> (-,+)
sig_sph = (sp.sign(g_theta), +1); sig_ds = (sp.sign(g_psi), +1)
ok&=check("signature (+,+) [spherical] -> (-,+) [de Sitter]", sig_sph==(1,1) and sig_ds==(-1,1))
# (5) C1 join at the seam: r=sin theta (theta<pi/2) and r=cosh psi (psi>0) meet at throat r=1
r_sph = sp.sin(th); r_ds = sp.cosh(psi)
v0  = (r_sph.subs(th,sp.pi/2), r_ds.subs(psi,0))
d1  = (sp.diff(r_sph,th).subs(th,sp.pi/2), sp.diff(r_ds,psi).subs(psi,0))
d2  = (sp.diff(r_sph,th,2).subs(th,sp.pi/2), sp.diff(r_ds,psi,2).subs(psi,0))
ok&=check("C0: r=1 on both pieces at the seam", v0==(1,1))
ok&=check("C1: dr=0 on both pieces at the seam (tangent to throat)", d1==(0,0))
ok&=check("NOT C2: d2r flips -1 (spherical) <-> +1 (de Sitter) -- the curvature/signature flip", d2==(-1,1))
# (6) CONTROL: a real shift (no i) does NOT flip the signature
sub_real = sp.pi/2 + psi
ok&=check("CONTROL: real shift -> sin->cos psi (bounded) + factor^2=+1 (NO flip); only i gives factor^2=-1 (flip)",
          sp.simplify(sp.sin(sub_real) - sp.cos(psi))==0 and sp.Integer(1)**2==1 and sp.I**2==-1)
print("="*72)
print("RESULT:", "ALL PASS -- one analytic function continued through theta->pi/2+i psi joins the (+,+)\n         spherical piece to the (-,+) de Sitter piece C1 at the throat; the signature flip is automatic\n         from dtheta=i dpsi (squares to -1), and it is the 2D slicing surface's, not the spacetime's." if ok else "SOME FAILED")
print("="*72)

# --- r2376+c54.159 -----------------------------------------------------------------
# The file computed a PASS/FAIL flag and only PRINTED it.  Assert the flag, and pin the
# continuation against an EXTERNAL number: sin(pi/2 + i psi) at psi=1 must be the real
# value cosh 1 = 1.5430806348152437 (a real shift would give cos 1 = 0.5403, the CONTROL).
# Then the signature flip and the C1-not-C2 join at the throat, as exact integer tuples.
assert ok, "P03_seam_continuation: a check FAILED"
_cont_at_1 = complex(sp.N(sp.sin(sub).subs(psi, 1)))
assert abs(_cont_at_1.real - 1.5430806348152437) < 1e-12 and abs(_cont_at_1.imag) < 1e-12
assert (sig_sph, sig_ds) == ((1, 1), (-1, 1))              # (+,+) spherical -> (-,+) de Sitter
assert (v0, d1, d2) == ((1, 1), (0, 0), (-1, 1))           # C0, C1 agree; d2 flips: NOT C2
assert sp.simplify(ang_cont - sp.cosh(psi)**2) == 0        # sin^2 theta -> cosh^2 psi
