#!/usr/bin/env python3
"""
RECEIPT — P16 / P15: ** THE INTERIOR-TO-OBSERVED MODE MAP.  BOTH HALVES WERE ALREADY IN THE CORPUS
AND UNJOINED, AND THE JOINED MAP VALIDATES AGAINST THE LOW-MULTIPOLE DEFICIT. **

  PART 1  the harmonic index is preserved across the branch point: the equation is diagonal in L
  PART 2  ** our side's map is P15's own: l(L) = sqrt(L(L+2)) * D_C/r_0, no new parameters **
  PART 3  ** VALIDATION: it must send the lowest physical mode to P15's stated l = 7.8, and does **
  PART 4  ** the bound on the progenitor, redone with the map **

rc=0 on success.  Run: python3 P16_the_interior_to_observed_mode_map.py     (numpy)
"""
import sys

import numpy as np

print(__doc__.split("rc=0")[0])

print("=" * 78)
print("PART 1 — THE INDEX IS PRESERVED")
print("=" * 78)
print("  The spatial section is S^3 throughout; a perturbation decomposes in its harmonics; the")
print("  mode equation is DIAGONAL in the harmonic index L, which labels the eigenfunction and not")
print("  its amplitude, and the continuation acts on the radial factor at fixed L.")
print("  ** So the map on the index is the identity, L -> L, and it is forced: an integer")
print("     eigenvalue label has nothing to rescale.  Consistent with the geometry transmitting no")
print("     PARAMETER -- a discrete LABEL is carried by the topology, not by a parameter. **")

print()
print("=" * 78)
print("PART 2 — OUR SIDE'S MAP, REBUILT FROM SCRATCH")
print("=" * 78)
H0, OmL, Omm, c_kms, DC = 67.4, 0.685, 0.315, 299792.458, 13927.0
Lam = 3 * (H0 / c_kms)**2 * OmL
u = np.arcsinh(np.sqrt(OmL / Omm))
r0 = 2**(1 / 3) / np.sqrt(Lam) * np.sinh(u)**(2 / 3)
S = DC / r0
print("  P15 sec:flatlcdm: k_L = sqrt(L(L+2))/r_0 projected through the FLAT j_l(k_L D_C), so")
print("     l(L) = sqrt(L(L+2)) * (D_C / r_0)")
print(f"  {'u = arcsinh sqrt(Om_L/Om_m)':>44} {u:>12.4f}   (P15: 1.18)")
print(f"  {'r_0 = 2^(1/3) Lambda^(-1/2) sinh^(2/3) u  [Mpc]':>44} {r0:>12.1f}   (P15: 5064)")
print(f"  {'stretch factor S = D_C/r_0':>44} {S:>12.4f}   (P15: 2.75)")
assert abs(u - 1.18) < 0.02 and abs(r0 - 5064) / 5064 < 0.02 and abs(S - 2.75) < 0.05

print()
print("=" * 78)
print("PART 3 — VALIDATION AGAINST THE LOW-MULTIPOLE DEFICIT")
print("=" * 78)
l2 = np.sqrt(2 * 4) * S
print(f"  lowest physical mode L = 2  ->  l = sqrt(8) * S = {l2:.2f}      (P15 states 7.8)")
assert abs(l2 - 7.8) < 0.3
print("  ** and no source below it -- which IS the corpus's parameter-free deficit at l <~ 8,")
print("     already cross-validated on two independent transfers. **")
print("  ** So the coefficient carrying interior modes to observed multipoles is the same number")
print("     that produces the deficit: one coefficient doing two jobs, the second already")
print("     compared against data. **")

print()
print("=" * 78)
print("PART 4 — THE BOUND, REDONE")
print("=" * 78)
kx = 2 * np.pi * np.sqrt(3)
print("  The leaked (scale-invariant) contribution dominates below k_x = 2 pi sqrt(3)/rho, with k")
print("  in INTERIOR units, k_L = sqrt(L(L+2)).  Observed flatness to l_max maps to k_L = l_max/S.")
print(f"\n  {'l_max':>10} {'k_L = l_max/S':>16} {'rho <=':>12} {'rho_r/rho_m at a_max':>22}")
for lm in [1000, 2000, 2500]:
    kl = lm / S
    rho = kx / kl
    print(f"  {lm:>10} {kl:>16.1f} {rho:>12.5f} {rho**2/4:>22.3e}")
rr = (kx / (2500 / S))**2 / 4
ours = 1 / 3400.0
print(f"\n  ** rho_r/rho_m at maximum expansion <~ {rr:.2e}, against our own {ours:.2e} today **")
print(f"     -- a parent that ran about {ours/rr:.1f} times further past its own equality scale.")
assert 1e-6 < rr < 1e-3 and 3 < ours / rr < 30
naive = (kx / 2500)**2 / 4
print(f"\n  and the map RELAXES the previous bound: assuming L = l gave {naive:.1e}, a factor")
print(f"  {rr/naive:.1f} tighter than the truth, because the observed range reaches mode")
print(f"  {2500/S:.0f} and not mode 2500.")
print()
print("  BOUND: what remains assumed is that the progenitor's S^3 and ours carry the same harmonic")
print("  labelling -- which follows if the continuation is through the same spatial section, as the")
print("  construction has it, and would fail only if the crossing changed the topology.  ** Much")
print("  smaller than the assumption it replaces. **")
print()
print("ALL PASS")
sys.exit(0)
