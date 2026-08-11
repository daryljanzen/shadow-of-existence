#!/usr/bin/env python3
"""
`L-150`.  ** THE INHERITED DATA CANNOT BE INHERITED FROM THE COLLAPSE, BECAUSE THE COLLAPSE
GEOMETRY TRANSMITS ZERO PARAMETERS.  THE CORPUS PROVED THAT ITSELF AND DID NOT CASH IT. **

`L-170` closed the arc with: *deriving $n_s$ and characterising the progenitor are the same
problem.*  This asks the prior question — **what can the progenitor supply at all?** — by counting.

  PART 1  ** THE PROGENITOR'S GEOMETRY HAS EXACTLY ONE PARAMETER. **
  PART 2  ** AND c54.113 SHOWED THAT ONE PARAMETER DOES NOT SURVIVE THE APPROACH. **
  PART 3  ** WHAT THE CORPUS DRAWS FROM IT: at least four independent numbers. **
  PART 4  ** FOUR NUMBERS CANNOT COME FROM ZERO PARAMETERS.  So they come from the progenitor's
          MATTER CONTENT — which the construction's description does not carry. **
  PART 5  ** WHAT THE GEOMETRY *DOES* FIX, universally and parameter-free. **

Run: python3 L150b_the_progenitor_transmits_no_parameters.py      (sympy, numpy)
"""
import numpy as np
import sympy as sp

print(__doc__.split("Run:")[0])
r, M, al, tau = sp.symbols('r M alpha tau', positive=True)

# =====================================================================
print("=" * 78)
print("PART 1 — THE PROGENITOR'S GEOMETRY HAS ONE PARAMETER")
print("=" * 78)
print(f"  {'ingredient':>40} {'status':>34}")
for a, b in [("alpha = sqrt(3/Lambda)", "the ONE invariant, universal"),
             ("M, the progenitor mass", "a MODULUS: labels which member"),
             ("E = 1, marginally bound", "a CHOICE of geodesic, not a parameter"),
             ("the exterior", "exactly vacuum SdS -- no content in it"),
             ("the interior", "dust (Oppenheimer-Snyder), no composition")]:
    print(f"  {a:>40} {b:>34}")
print()
print("  ** So the progenitor family this construction describes is ONE-DIMENSIONAL: it is")
print("     parametrised by M and by nothing else. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — AND THAT ONE PARAMETER DOES NOT SURVIVE THE APPROACH")
print("=" * 78)
K = 48 * M**2 / r**6 + sp.Rational(8, 3) * (3 / al**2)**2
rb = (2 * M * al**2)**sp.Rational(1, 3) * sp.sinh(3 * tau / (2 * al))**sp.Rational(2, 3)
Kb = sp.simplify(sp.powsimp(K.subs(r, rb), force=True))
dK = sp.simplify(sp.diff(Kb, M))
print("  c54.113, re-run here rather than quoted.  Along the bead r(tau), the Kretschmann is")
print(f"     K(tau) = {Kb}")
print(f"     ** dK/dM = {dK}  ->  MASS-FREE **")
assert dK == 0
lead = sp.limit(tau**4 * Kb, tau, 0)
print(f"     and K -> (64/27)/tau^4 :  lim tau^4 K = {lead}")
assert sp.simplify(lead - sp.Rational(64, 27)) == 0
print()
for s in [
 "⇒⇒ ** SO THE CURVATURE HISTORY OF THE APPROACH IS THE SAME FOR EVERY PROGENITOR.  The corpus",
 "   states this itself: *'nothing about the parent survives in the approach to distinguish one",
 "   cosmogenesis from another'* (c54.113). **",
 "",
 "⌗ ***AND THAT IS A TRANSMISSION STATEMENT, NOT ONLY A UNIVERSALITY ONE.  A quantity that is the",
 "   same for every member carries no information about which member it was.  The geometry does not",
 "   transmit ONE parameter across the branch point.  It transmits ZERO.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT THE CORPUS DRAWS FROM IT")
print("=" * 78)
DRAWN = [
    ("A_s", "the scalar amplitude", "P15 sec:transmission"),
    ("n_s", "the spectral tilt", "P15 sec:transmission"),
    ("eta", "the baryon-to-photon ratio", "P15 sec:tensions"),
    ("z_onset (= rho_r/rho_m)", "the handover redshift", "P15 sec:tensions, c54.105"),
    ("the light-element composition", "He-4, D", "P16 / P15 sec:predictions"),
]
print(f"  {'datum':>28} {'what it is':>30} {'where':>28}")
for a, b, c in DRAWN:
    print(f"  {a:>28} {b:>30} {c:>28}")
print()
print("  c54.105 showed rho_r/rho_m at onset IS z_onset (one datum, not two), so the count of")
print("  INDEPENDENT numbers drawn from the progenitor is:")
indep = ["A_s", "n_s", "eta", "z_onset", "composition"]
print(f"     ** {len(indep) - 1} at least: {', '.join(indep[:3])}, {indep[3]} (= the ratio), plus the composition **")
assert len(indep) - 1 >= 4

# =====================================================================
print()
print("=" * 78)
print("PART 4 — FOUR NUMBERS CANNOT COME FROM ZERO PARAMETERS")
print("=" * 78)
print(f"  {'':>44} {'count':>8}")
for a, b in [("parameters of the progenitor GEOMETRY", 1),
             ("of those surviving the approach (c54.113)", 0),
             ("independent numbers the corpus draws from it", 4)]:
    print(f"  {a:>44} {b:>8}")
print()
for s in [
 "⛔⛔ ** SO 'INHERITED FROM THE PROGENITOR COLLAPSE' CANNOT MEAN INHERITED FROM THE COLLAPSE",
 "   GEOMETRY.  The geometry is a one-parameter family whose one parameter washes out of the",
 "   approach; it has nothing left to hand over. **",
 "",
 "✔ ** THE RESOLUTION IS NOT A CONTRADICTION AND IT IS WORTH STATING PRECISELY: what is inherited",
 "   is inherited from the progenitor's MATTER CONTENT — its composition, its entropy per baryon,",
 "   its perturbation spectrum — and NONE of that is carried by $M$. **  *The SdS exterior is",
 "   vacuum and the marginally-bound interior is dust without composition, so the construction's",
 "   own description of the progenitor is exactly the part that transmits nothing.*",
 "",
 "⇒⇒ ** WHICH RECLASSIFIES `L-150`.  It is not a DERIVATION problem — there is no quantity in the",
 "   construction to derive $\\eta$ FROM.  It is a MODELLING problem: it requires a progenitor",
 "   interior the construction does not currently write down. **",
 "",
 "⌗⌗ *And that is why the row has resisted: **every attempt to derive an inherited datum from the",
 "   collapse has been reaching into a vacuum solution for a number that only matter can carry.***",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT THE GEOMETRY DOES FIX")
print("=" * 78)
print("  The geometry is not empty-handed; it is empty-handed about the PROGENITOR.  What it fixes")
print("  it fixes universally, from alpha alone:")
alv = 1.0
Mv = alv / (3 * np.sqrt(3))
A = (2 * Mv * alv**2)**(1. / 3)
s_ = np.linspace(1e-9, np.pi * alv / 3.0, 400000)
a_ = A * np.abs(np.sin(1.5 * s_ / alv))**(2. / 3)
DETA = float(np.sum(np.diff(s_) / (0.5 * (a_[1:] + a_[:-1]))))
LAM = 1.1056e-52
alpha_m = np.sqrt(3.0 / LAM)
MPC = 3.0857e22
print(f"\n  {'quantity':>40} {'value':>22}")
for a, b in [("the segment's conformal length |Delta eta|", f"{DETA:.3f} alpha"),
             ("alpha itself", f"{alpha_m/MPC/1e3:.3f} Gpc"),
             ("so |Delta eta| in physical units", f"{DETA*alpha_m/MPC:.4g} Mpc")]:
    print(f"  {a:>40} {b:>22}")
assert abs(DETA - 3.32) < 0.02
assert 1.5e4 < DETA * alpha_m / MPC < 2.0e4
print()
for s in [
 "✔✔ ** THAT LENGTH IS PARAMETER-FREE: it is fixed by $\\Lambda$ and by nothing else, the same for",
 "   every progenitor, and it is the corpus's $1.8\\times10^4$ Mpc. **  *It sets the crossing's",
 "   filter scale $e^{-kc_s|\\Delta\\eta|}$ — so **what the geometry supplies is a CUTOFF, not a",
 "   CONTENT**: it says which modes survive, and says nothing about what their amplitude was.*",
 "",
 "⌗ ** AND THAT IS THE SAME SHAPE AS EVERY OTHER VERDICT THIS ARC HAS REACHED, three times now in",
 "   three different sectors: **",
 "   *`L-125` — the winding QUANTISES and does not measure a strength.*",
 "   *`L-164` — the flat bundle SELECTS and does not couple.*",
 "   *here    — the branch point FILTERS and does not supply.*",
 "   ⇒⇒ ***THE CONSTRUCTION IS A GEOMETRY OF SELECTION RULES.  It says which things are possible",
 "      and consistently declines to say how much.  That is a characterisation of the programme,",
 "      arrived at three independent ways, and it is worth more than any one of the three.***",
]:
    print("  " + s)
