import sympy as sp
G = sp.symbols('Gamma', real=True)
# Fiber -ψ'' + (G/x^2)ψ on L^2(0,∞): solutions ~ x^{s±}, s± = 1/2 ± (1/2)sqrt(1+4G).
# x^s in L^2 near 0  <=>  s > -1/2.  s_+ always L^2.  s_- L^2  <=>  G < 3/4.
# both L^2 near 0  <=> limit-circle (BC needed);  only one  <=> limit-point (ess. self-adjoint).
def classify(val):
    sm = sp.Rational(1,2) - sp.sqrt(1+4*val)/2
    Lc = sp.simplify(sm + sp.Rational(1,2)) > 0          # s_- > -1/2 ?
    return sp.nsimplify(sm), ("limit-circle (BC needed)" if Lc else "limit-point (ess. self-adj, no BC)")
print("threshold G = 3/4 :  s_- = -1/2  (marginal, limit-point onward)\n")
for v in [sp.Integer(0), sp.Rational(1,4), sp.Rational(3,4), sp.Integer(2)]:
    sm, cls = classify(v); print(f"  Γ={v}:  s_- = {sm}  ->  {cls}")
print("""
Decomposition (Γ̂ commutes with the radial part -> direct integral over spec(Γ̂)):
  spec(Γ̂) = [γ, ∞),  γ ≤ 1/4 < 3/4  (free scale factor) ... unbounded above (graviton momentum).
  -> ess. self-adjoint on the sector {Γ̂ ≥ 3/4};  limit-circle (BC) on {γ ≤ Γ̂ < 3/4}.
  -> the free single BC (deficiency (1,1), r363) is replaced by a self-adjoint condition
     supported on the sub-threshold graviton subspace {Γ̂ < 3/4}.
Cubic check (separately confirmed): cubic kinetic ~ π²φ/a³ enters at the SAME 1/x² order
  at the origin -> the full boundary coefficient Γ̂ is the INTERACTING graviton Hamiltonian's
  singular part; its spectrum + the UV definition of the tower sums is the open frontier.""")
