#!/usr/bin/env python3
"""
RECEIPT — P15 `sec:transmission`: ** THE INHERITED DATA ARE NOT INHERITED FROM THE COLLAPSE
GEOMETRY, BECAUSE THAT GEOMETRY TRANSMITS ZERO PARAMETERS.  A COUNT. **

  PART 1  the progenitor geometry is a ONE-parameter family (M; alpha is universal, E=1 a choice)
  PART 2  ** and c54.113's mass-free approach means that one parameter does not survive it **
  PART 3  the corpus draws FOUR independent numbers from it
  PART 4  ** what the geometry DOES fix: |Delta eta| = 3.32 alpha, parameter-free **

rc=0 on success.  Run: python3 P15_the_geometry_transmits_no_parameters.py   (sympy, numpy)
"""
import sys

import numpy as np
import sympy as sp

print(__doc__.split("rc=0")[0])
r, M, al, tau = sp.symbols('r M alpha tau', positive=True)

print("=" * 78)
print("PART 1 & 2 — ONE PARAMETER, AND IT DOES NOT SURVIVE")
print("=" * 78)
print("  the SdS progenitor family is parametrised by M alone: alpha is the one invariant and")
print("  E = 1 is a choice of geodesic.  Along the bead:")
K = 48 * M**2 / r**6 + sp.Rational(8, 3) * (3 / al**2)**2
rb = (2 * M * al**2)**sp.Rational(1, 3) * sp.sinh(3 * tau / (2 * al))**sp.Rational(2, 3)
Kb = sp.simplify(sp.powsimp(K.subs(r, rb), force=True))
print(f"     K(tau) = {Kb}")
assert sp.diff(Kb, M) == 0
assert sp.simplify(sp.limit(tau**4 * Kb, tau, 0) - sp.Rational(64, 27)) == 0
print("     dK/dM = 0, asserted, and K -> (64/27)/tau^4, asserted.")
print("  ** A quantity identical for every member carries no information about which member it")
print("     was.  The approach transmits ZERO parameters, not one. **")

print()
print("=" * 78)
print("PART 3 — WHAT IS DRAWN FROM IT")
print("=" * 78)
drawn = ["A_s", "n_s", "eta", "z_onset (= rho_r/rho_m, one datum by c54.105)", "the composition"]
for d in drawn:
    print(f"     - {d}")
print(f"  ** at least four independent numbers drawn from zero transmitted parameters. **")
assert len(drawn) - 1 >= 4
print("  => 'inherited from the progenitor collapse' cannot mean inherited from the collapse")
print("     GEOMETRY.  It means inherited from the progenitor's MATTER CONTENT -- composition,")
print("     entropy per baryon, perturbation spectrum -- none of which M carries, the exterior")
print("     being exactly vacuum and the interior dust without composition.")

print()
print("=" * 78)
print("PART 4 — WHAT THE GEOMETRY DOES FIX")
print("=" * 78)
alv = 1.0
Mv = alv / (3 * np.sqrt(3))
A = (2 * Mv * alv ** 2) ** (1. / 3)
s_ = np.linspace(1e-9, np.pi * alv / 3.0, 400000)
a_ = A * np.abs(np.sin(1.5 * s_ / alv)) ** (2. / 3)
DETA = float(np.sum(np.diff(s_) / (0.5 * (a_[1:] + a_[:-1]))))
alpha_m = np.sqrt(3.0 / 1.1056e-52)
MPC = 3.0857e22
print(f"  |Delta eta| = {DETA:.3f} alpha  =  {DETA*alpha_m/MPC:.4g} Mpc,  fixed by Lambda alone")
assert abs(DETA - 3.32) < 0.02
assert 1.5e4 < DETA * alpha_m / MPC < 2.0e4
print("  ** so the geometry supplies a CUTOFF, not a CONTENT: which modes survive, not how large")
print("     they were. **")
print()
print("  BOUND: this is a counting argument about what the construction's own description of the")
print("  progenitor can carry.  It does not show that no model supplies eta -- it shows that no")
print("  model of the VACUUM EXTERIOR can, and that the row therefore needs an interior.")
print()
print("ALL PASS")
sys.exit(0)
