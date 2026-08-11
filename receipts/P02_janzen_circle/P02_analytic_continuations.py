"""
P02_analytic_continuations.py -- verifies: the cycloid arc continues analytically through BOTH critical
  points -- z=iρ at z=0 recovers the Schwarzschild exterior (Region I, r>2M), and z=π+iρ' at z=π is the
  back-seam continuation onto r<0. [P2 janzen_circle_v3 sec:continuation, prop:region_I_metric, prop:back_seam_metric]
STATUS: ✔✔   RUN: python3 P02_analytic_continuations.py   RUNTIME: ~4s
COMPUTES: the trig→hyperbolic substitution rules (cos z→cosh ρ, sin z→i sinh ρ, tan(z/2)→i tanh(ρ/2));
  r(iρ)=M(1+cosh ρ)∈(2M,∞) with r(0)=2M matching the interior endpoint; the interior metric coefficients
  mapping under η=iρ (dη²=−dρ²) to the exterior ones and AGREEING with Schwarzschild (1−2M/r=tanh²(ρ/2),
  dr²/(1−2M/r)=4M²cosh⁴(ρ/2)dρ², r²=M²(1+cosh ρ)²); and the back-seam z=π+iρ': r=M(1−cosh ρ')∈(−∞,0),
  r(0)=0. CONTROL: boundary values ρ=0/ρ'=0 recover the interior endpoints (continuation is seamless).
BOUND: verifies the metric identities of the two continuations; the Kruskal/four-region global structure
  (sec:four_regions) and the ontology (sec:ontology) are separate/analytic.
ORIGIN: built new r1335 (P2 cited no receipts).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
rho, rhop, M, t = sp.symbols('rho rhop M t', positive=True)
print("="*72); print("P02 analytic continuations: z=iρ (Region I) and z=π+iρ' (back-seam r<0)"); print("="*72)
# substitution rules
z=sp.I*rho
ok&=check("cos(iρ)=cosh ρ, sin(iρ)=i sinh ρ, tan(iρ/2)=i tanh(ρ/2)",
          sp.simplify(sp.cos(z)-sp.cosh(rho))==0 and sp.simplify(sp.sin(z)-sp.I*sp.sinh(rho))==0
          and sp.simplify(sp.tan(z/2)-sp.I*sp.tanh(rho/2))==0)
# --- Region I : z=iρ ---
r = M*(1+sp.cos(z))
ok&=check("r(iρ)=M(1+cosh ρ)  (r(0)=2M, r→∞)", sp.simplify(r-M*(1+sp.cosh(rho)))==0 and r.subs(rho,0)==2*M)
r_ext = M*(1+sp.cosh(rho))
ok&=check("1−2M/r = tanh²(ρ/2)  ⇒ g_tt = −(1−2M/r) = −tanh²(ρ/2) (Schwarzschild exterior)",
          sp.simplify((1-2*M/r_ext) - sp.tanh(rho/2)**2)==0)
dr = sp.diff(r_ext,rho)
ok&=check("dr²/(1−2M/r) = 4M²cosh⁴(ρ/2)dρ²  (radial coeff matches)",
          sp.simplify((dr**2/(1-2*M/r_ext) - 4*M**2*sp.cosh(rho/2)**4).rewrite(sp.exp))==0)
ok&=check("angular r² = M²(1+cosh ρ)²", sp.simplify(r_ext**2 - M**2*(1+sp.cosh(rho))**2)==0)
# interior coeffs -> exterior coeffs under eta=i rho (deta^2=-drho^2)
eta=sp.symbols('eta', positive=True)
ok&=check("interior −4M²cos⁴(η/2)dη² ↦ +4M²cosh⁴(ρ/2)dρ² (dη²=−dρ²)",
          sp.simplify((-4*M**2*sp.cos(eta/2)**4).subs(eta,sp.I*rho)*(-1) - 4*M**2*sp.cosh(rho/2)**4)==0)
ok&=check("interior +tan²(η/2)dt² ↦ −tanh²(ρ/2)dt²",
          sp.simplify((sp.tan(eta/2)**2).subs(eta,sp.I*rho) + sp.tanh(rho/2)**2)==0)
# --- back-seam : z=pi+i rho' ---
zb=sp.pi+sp.I*rhop
rb=M*(1+sp.cos(zb))
ok&=check("z=π+iρ': r=M(1−cosh ρ')∈(−∞,0), r(0)=0",
          sp.simplify(rb-M*(1-sp.cosh(rhop)))==0 and sp.simplify(rb.subs(rhop,0))==0)
ok&=check("  CONTROL: the back-seam sends r NEGATIVE for ρ'>0 (r=M(1−cosh 1)<0)", (M*(1-sp.cosh(1))).subs(M,1)<0)
print("="*72)
print("RESULT:", "ALL PASS -- z=iρ recovers the Schwarzschild exterior (metric identities all match), z=π+iρ'\n         continues onto r<0; both seamless at the boundary (ρ=0 → interior endpoints). The one cycloid\n         is hyperbola–circle–hyperbola: the Wick rotation converts the interior's trig to the exterior's hyperbolics." if ok else "SOME FAILED")
print("="*72)

# --- ASSERTIONS (added r2376+c54.158) --------------------------------------------------------
# This receipt's claim is a pair of EXACT symbolic identities (sec:continuation); the file prints
# no numeric figure, so these pin exact zeros rather than decimals.
# (a) the file's own PASS/FAIL boolean: every printed [PASS] above is now REQUIRED.
assert ok, "P02 continuation: at least one continuation identity FAILED"
# (b) Region I (z=iρ): 1−2M/r = tanh²(ρ/2) and dr²/(1−2M/r) = 4M²cosh⁴(ρ/2) dρ² with r=M(1+cosh ρ)
#     -- i.e. the continuation really lands on the Schwarzschild exterior metric.
_rI = M*(1 + sp.cosh(rho))
assert sp.simplify((1 - 2*M/_rI) - sp.tanh(rho/2)**2) == 0
assert sp.simplify((sp.diff(_rI, rho)**2/(1 - 2*M/_rI) - 4*M**2*sp.cosh(rho/2)**4).rewrite(sp.exp)) == 0
# (c) back-seam (z=π+iρ'): r=M(1−cosh ρ'), zero at ρ'=0 and STRICTLY NEGATIVE off it (the r<0 branch).
assert sp.simplify(M*(1 + sp.cos(sp.pi + sp.I*rhop)) - M*(1 - sp.cosh(rhop))) == 0
assert (M*(1 - sp.cosh(3))).subs(M, 1) < 0
