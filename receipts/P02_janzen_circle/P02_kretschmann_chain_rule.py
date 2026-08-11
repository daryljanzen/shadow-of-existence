"""
P02_kretschmann_chain_rule.py -- verifies: the Kretschmann divergence at r=0 is a chain-rule / chart-
  labelling artefact -- K(z)=48/(M⁴(1+cos z)⁶) has a 12th-order pole at z=π (r=0) but is finite at z=0
  (r=2M), the pole order = (2nd-order vanishing of r) × (r⁻⁶ in K), and under the opposite labelling the
  pole lands at the horizon instead. [P2 janzen_circle_v3 sec:kretschmann, prop:Kretschmann, cor + remark]
STATUS: ✔✔   RUN: python3 P02_kretschmann_chain_rule.py   RUNTIME: ~4s
COMPUTES: K(z) from K=48M²/r⁶ with r=M(1+cos z); K(0)=3/(4M⁴) finite; the Laurent series of K about z=π
  (leading 3072/(M⁴ε¹²), pole order 12); the pole-order arithmetic 6×(vanishing order of r); and a
  RELABEL r̃=M(1−cos z) (horizon↔r=0 swapped) under which K̃ instead has the 12th-order pole at z=0.
BOUND: verifies the divergence is label-tracking (a fact about the composition), NOT the ontological reading
  of the real, coordinate-independent divergence (sec:ontology, explicitly left open by the paper).
ORIGIN: built new r1334 (P2 cited no receipts).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
z, M, eps = sp.symbols('z M epsilon', positive=True)
r = M*(1+sp.cos(z))
K = sp.simplify(48*M**2/r**6)
print("="*72); print("P02 Kretschmann as a chain-rule / labelling artefact"); print("="*72)
ok&=check("K(z) = 48/(M⁴(1+cos z)⁶)", sp.simplify(K - 48/(M**4*(1+sp.cos(z))**6))==0)
ok&=check("K(0) = 3/(4M⁴)  finite at r=2M", sp.simplify(K.subs(z,0) - sp.Rational(3,4)/M**4)==0)
# Laurent series about z=pi : substitute z = pi - eps, expand in eps
Keps = K.subs(z, sp.pi - eps)
# leading coefficient and order
leadterm = sp.simplify(sp.limit(Keps*eps**12, eps, 0))
ok&=check("K has a 12th-order pole at z=π: lim K·ε¹² = 3072/M⁴", sp.simplify(leadterm - 3072/M**4)==0)
ok&=check("  (and K·ε¹⁰ → ∞, K·ε¹⁴ → 0 : order is exactly 12)",
          sp.limit(Keps*eps**14, eps,0)==0 and sp.limit(sp.Abs(Keps)*eps**10, eps,0)==sp.oo)
# chain-rule arithmetic: r vanishes to 2nd order at z=pi, K ~ r^-6 => pole order 6*2=12
r_eps = sp.series(r.subs(z,sp.pi-eps), eps,0,4).removeO()
ok&=check("chain rule: r ~ M ε²/2 at z=π (2nd-order zero), K∝r⁻⁶ ⇒ pole 6×2 = 12",
          sp.simplify(r_eps - M*eps**2/2)==0)
# the label swap: r~ = M(1-cos z) (horizon<->r=0 swapped). Now r~=0 at z=0, r~=2M at z=pi.
r_swap = M*(1-sp.cos(z)); K_swap = 48*M**2/r_swap**6
ok&=check("RELABEL r̃=M(1−cos z): now r̃=0 at z=0, r̃=2M at z=π (labels swapped)",
          sp.simplify(r_swap.subs(z,0))==0 and sp.simplify(r_swap.subs(z,sp.pi)-2*M)==0)
ok&=check("  under the swap the 12th-order pole lands at z=0 (the horizon), K̃(π) finite",
          sp.simplify(sp.limit(K_swap*z**12, z, 0) - 3072/M**4)==0 and sp.simplify(K_swap.subs(z,sp.pi)-sp.Rational(3,4)/M**4)==0)
print("="*72)
print("RESULT:", "ALL PASS -- the r⁻⁶ divergence is a 12th-order pole = (2nd-order zero of r)×(r⁻⁶), landing\n         wherever the chart labels the critical point r=0; the label swap moves it to the horizon. The\n         divergence tracks the LABEL, not an intrinsic difference between the two critical points." if ok else "SOME FAILED")
print("="*72)

# --- ASSERTIONS (added r2376+c54.158) --------------------------------------------------------
# Pins the figures this receipt prints (sec:kretschmann, INDEX row): K(0)=3/(4M^4) finite at r=2M,
# a pole at z=pi of order EXACTLY 12 with leading coefficient 3072/M^4, and the same 12th-order
# pole at z=0 under the relabelling r~=M(1-cos z).
# (a) the file's own PASS/FAIL boolean.
assert ok, "P02 Kretschmann: at least one pole-order/labelling check FAILED"
# (b) the finite end and the pole coefficient, as exact rationals in M.
assert sp.simplify(K.subs(z, 0)*M**4 - sp.Rational(3, 4)) == 0
assert sp.simplify(leadterm*M**4 - 3072) == 0
# (c) the order is exactly 12: eps^14 kills it, eps^10 does not.
assert sp.limit(Keps*eps**14, eps, 0) == 0 and sp.limit(sp.Abs(Keps)*eps**10, eps, 0) == sp.oo
# (d) the chain-rule arithmetic 12 = 2 (order of the zero of r) x 6 (the r^-6 in K).
assert sp.simplify(r_eps - M*eps**2/2) == 0
# (e) the label swap moves the SAME 3072/M^4 12th-order pole onto the horizon z=0.
assert sp.simplify(sp.limit(K_swap*z**12, z, 0)*M**4 - 3072) == 0
assert sp.simplify(K_swap.subs(z, sp.pi)*M**4 - sp.Rational(3, 4)) == 0
