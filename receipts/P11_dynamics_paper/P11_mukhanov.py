"""
P11_mukhanov.py -- verifies sec:nonlinear's mode analysis: the linear tensor perturbation delta-psi on the
  de Sitter background obeys deltapsi'' + 3H deltapsi' + (k^2/a^2) deltapsi + m^2 deltapsi = 0 (cosmic time),
  and passing to the Mukhanov variable W=a deltapsi (conformal time eta) gives
     W'' + (k^2 + m^2 a^2 - a''/a) W = 0.
  On de Sitter a=-1/(H eta), a''/a = 2/eta^2, so for the PHYSICAL (massless) mode m^2=0 this is
     W'' + (k^2 - 2/eta^2) W = 0   (eq:mukhanov),
  the standard massless-field equation: the effective mass is exactly zero. The naive m^2=2Lambda=6H^2
  would instead give +4/eta^2 -- the "6H^2 -> 4H^2" apparent shift the paper flags as a gauge/truncation
  artifact. [P11 dynamics_paper sec:nonlinear]
STATUS: ✔✔   RUN: python3 P11_mukhanov.py   RUNTIME: ~3s
COMPUTES: the exact Mukhanov transformation W=a deltapsi (symbolic); a''/a=2/eta^2 on de Sitter; the massless
  reduction W''+(k^2-2/eta^2)W=0. CONTROL: a nonzero m^2 leaves a residual m^2 a^2 term (not massless).
ORIGIN: built new r1375 (P11 cited no receipts).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
eta,k,m,H=sp.symbols('eta k m H', real=True)
a=sp.Function('a')(eta); W=sp.Function('W')(eta)
print("="*70); print("P11 Mukhanov reduction: massless de Sitter mode"); print("="*70)
# (1) the exact transformation: substitute deltapsi=W/a into the conformal-time equation
dpsi=W/a
eom = sp.diff(dpsi,eta,2) + 2*(sp.diff(a,eta)/a)*sp.diff(dpsi,eta) + (k**2 + m**2*a**2)*dpsi
eom_times_a = sp.simplify(eom*a)
target = sp.diff(W,eta,2) + (k**2 + m**2*a**2 - sp.diff(a,eta,2)/a)*W
ok&=check("Mukhanov W=a deltapsi: conformal eqn => W'' + (k^2 + m^2 a^2 - a''/a) W = 0",
          sp.simplify(eom_times_a - target)==0)
# (2) de Sitter scale factor a=-1/(H eta): a''/a = 2/eta^2
a_dS=-1/(H*eta)
app_over_a = sp.simplify(sp.diff(a_dS,eta,2)/a_dS)
ok&=check("de Sitter a=-1/(H eta): a''/a = 2/eta^2", sp.simplify(app_over_a - 2/eta**2)==0)
# (3) massless (m^2=0) on de Sitter: W'' + (k^2 - 2/eta^2) W = 0  (eq:mukhanov)
pot_massless = sp.simplify((k**2 + 0*a_dS**2 - app_over_a))
ok&=check("PHYSICAL massless mode (m^2=0): W'' + (k^2 - 2/eta^2) W = 0  (eq:mukhanov, effective mass zero)",
          sp.simplify(pot_massless - (k**2 - 2/eta**2))==0)
# (4) the naive m^2=2Lambda=6H^2 would give +4/eta^2 (the flagged 6H^2->4H^2 artifact)
m2_naive=6*H**2
pot_naive = sp.simplify(k**2 + m2_naive*a_dS**2 - app_over_a)
ok&=check("naive m^2=6H^2 would give k^2 + 4/eta^2 (the '6H^2->4H^2' shift the paper flags as a gauge artifact)",
          sp.simplify(pot_naive - (k**2 + 4/eta**2))==0)
# CONTROL: a generic nonzero m^2 leaves a residual m^2 a^2 term (mode is NOT massless)
ok&=check("CONTROL: nonzero m^2 leaves a residual m^2 a^2 = m^2/(H^2 eta^2) term (not the massless form)",
          sp.simplify((k**2 + m**2*a_dS**2 - app_over_a) - (k**2 - 2/eta**2)) == sp.simplify(m**2/(H**2*eta**2)))
print("="*70)
print("RESULT:", "ALL PASS -- the Mukhanov variable reduces the de Sitter tensor mode to W''+(k^2-2/eta^2)W=0, a\n         MASSLESS field: the physical effective mass is exactly zero (the 6H^2->4H^2 shift is a gauge/truncation artifact)." if ok else "SOME FAILED")
print("="*70)

# --- r2376+c54.158 -------------------------------------------------------------------
# PINS THIS RECEIPT'S OWN CLAIM.  (a) the PASS/FAIL flag the file previously only PRINTED.
# (b) the two figures sec:nonlinear turns on: the PHYSICAL mode gives W''+(k^2-2/eta^2)W=0
# (effective mass exactly zero), while the naive m^2=6H^2 would give k^2+4/eta^2 -- the
# "6H^2 -> 4H^2" apparent shift the paper flags as a gauge/truncation artifact.  The 4 is
# the pinned figure; if the naive potential were anything else the flagged artifact moves.
assert ok, "P11 Mukhanov: at least one check FAILED"
assert sp.simplify(pot_naive - (k**2 + 4/eta**2)) == 0, "naive m^2=6H^2 potential is %s, not k^2+4/eta^2" % pot_naive
assert sp.simplify(pot_massless - (k**2 - 2/eta**2)) == 0, "massless potential is %s, not k^2-2/eta^2" % pot_massless
