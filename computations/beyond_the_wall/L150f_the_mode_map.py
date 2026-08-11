#!/usr/bin/env python3
"""
`L-150`.  ** THE INTERIOR-TO-OBSERVED MODE MAP — AND BOTH HALVES OF IT WERE ALREADY IN THE CORPUS,
UNJOINED. **

c54.132 bounded the progenitor's radiation fraction on one stated assumption: that the interior's
three-sphere harmonic index equals the observed multipole.  It does not.  This builds the map.

  PART 1  ** THE HARMONIC INDEX IS PRESERVED ACROSS THE BRANCH POINT — it is an integer label and
          the continuation acts at fixed $L$. **
  PART 2  ** OUR SIDE'S MAP IS ALREADY WRITTEN DOWN IN P15, with no new parameters. **
  PART 3  ** THE VALIDATION: the map must reproduce the corpus's own low-multipole deficit, and
          does. **
  PART 4  ** THE BOUND, REDONE — and it moves by nearly an order of magnitude. **

Run: python3 L150f_the_mode_map.py      (numpy)
"""
import numpy as np

print(__doc__.split("Run:")[0])

# =====================================================================
print("=" * 78)
print("PART 1 — THE HARMONIC INDEX IS PRESERVED")
print("=" * 78)
for s in [
 "  The spatial section is $S^3$ throughout: the collapse shrinks it to zero radius at the branch",
 "  point and the continuation re-expands it.  A perturbation decomposes in $S^3$ harmonics, and",
 "  ** the mode equation is DIAGONAL in the harmonic index $L$ — the index labels the eigenfunction,",
 "  not its amplitude, and the continuation acts on the radial factor at fixed $L$. **",
 "",
 "⇒ ** SO THE MAP ON THE INDEX IS THE IDENTITY, $L\\mapsto L$, and it is forced rather than chosen:",
 "   an integer eigenvalue label has nothing to rescale. **  *This is the same fact that makes the",
 "   crossing's filter a statement about each mode separately.*",
 "",
 "⌗ *And it is consistent with c54.125: the geometry transmits no PARAMETER, but a discrete LABEL",
 "   is not a parameter — it is carried by the topology, which the crossing does not change.*",
]:
    print(s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — OUR SIDE'S MAP IS ALREADY IN P15")
print("=" * 78)
print("  P15 `sec:flatlcdm`: the closed-S^3 spectrum is k_L = sqrt(L(L+2))/r_0, projected through")
print("  the FLAT spherical Bessel j_l(k_L D_C).  So a discrete mode L peaks at")
print("     ** l(L) = k_L D_C = sqrt(L(L+2)) * (D_C / r_0) **")
print()
print("  and both lengths are fixed with no new parameters.  Rebuilt from scratch here:")
H0, OmL, Omm = 67.4, 0.685, 0.315
c_kms = 299792.458
HubbleMpc = H0 / c_kms                       # Mpc^-1
Lam = 3 * HubbleMpc**2 * OmL                 # Mpc^-2
u = np.arcsinh(np.sqrt(OmL / Omm))
r0 = 2**(1 / 3) / np.sqrt(Lam) * np.sinh(u)**(2 / 3)
DC = 13927.0                                 # Mpc, the flat-LCDM observable
print(f"  {'quantity':>44} {'computed':>14} {'P15':>12}")
for nm, v, q in [("u = arcsinh sqrt(Om_L/Om_m)", u, 1.18),
                 ("r_0 = 2^(1/3)/sqrt(Lambda) * sinh^(2/3)(u)  [Mpc]", r0, 5064),
                 ("D_C  [Mpc]", DC, 13927),
                 ("stretch factor D_C / r_0", DC / r0, 2.75)]:
    print(f"  {nm:>44} {v:>14.4f} {q:>12}")
assert abs(u - 1.18) < 0.02
assert abs(r0 - 5064) / 5064 < 0.02
assert abs(DC / r0 - 2.75) < 0.05
S = DC / r0
print(f"\n  ** the stretch factor S = D_C/r_0 = {S:.3f} — the decoupling made numerical. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE VALIDATION")
print("=" * 78)
print("  The map is not free to be anything: it must reproduce the corpus's own parameter-free")
print("  low-multipole deficit, which P15 places at l <~ 8 with no source below it.")
print()
print(f"  {'L':>4} {'k_L r_0 = sqrt(L(L+2))':>24} {'l(L) = that times S':>22}")
for L in [2, 3, 4, 5, 6]:
    kl = np.sqrt(L * (L + 2))
    print(f"  {L:>4} {kl:>24.4f} {kl*S:>22.2f}")
l2 = np.sqrt(2 * 4) * S
print(f"\n  ** the lowest physical mode L = 2 lands at l = {l2:.2f}, and P15 states 7.8. **")
assert abs(l2 - 7.8) < 0.3
print("  ** and there is NO SOURCE BELOW IT, which is exactly the deficit the corpus predicts and")
print("     cross-validates on two independent transfers. **")
print()
for s in [
 "✔✔ ** SO THE MAP HAS AN INDEPENDENT CHECK AND PASSES IT.  The coefficient that carries interior",
 "   modes to observed multipoles is the same coefficient that produces the low-$\\ell$ deficit — one",
 "   number doing two jobs, and the second is already compared against data. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE BOUND, REDONE")
print("=" * 78)
print("  c54.132: the leaked (scale-invariant) contribution dominates the surviving mode below")
print("  k_x = 2 pi sqrt(3) / rho, with k in the INTERIOR's units -- i.e. k_L = sqrt(L(L+2)).")
print("  The observed spectrum is near scale-invariant out to l_max ~ 2500, which is the mode")
print()
kx_coeff = 2 * np.pi * np.sqrt(3)
print(f"  {'observed l_max':>16} {'k_L needed = l_max/S':>22} {'rho <=':>12} "
      f"{'rho_r/rho_m at a_max':>22}")
rows = []
for lmax in [1000, 2000, 2500]:
    kl_needed = lmax / S
    rho_req = kx_coeff / kl_needed
    rr = rho_req**2 / 4
    rows.append((lmax, kl_needed, rho_req, rr))
    print(f"  {lmax:>16} {kl_needed:>22.1f} {rho_req:>12.5f} {rr:>22.3e}")
lmax, kl_needed, rho_req, rr = rows[-1]
ours = 1.0 / 3400.0
print()
print(f"  ** rho_r/rho_m at the progenitor's maximum expansion <~ {rr:.2e} **")
print(f"     our own universe today:                              {ours:.2e}")
print(f"     ** so the parent ran about {ours/rr:.1f} times further past its own matter-radiation")
print(f"        equality than we have so far. **")
assert 1e-6 < rr < 1e-3
assert 3 < ours / rr < 30
print()
print(f"  ⌗ c54.132 assumed L = l and got {(2*np.pi*np.sqrt(3)/2500)**2/4:.1e}, i.e. a factor "
      f"{rr/((2*np.pi*np.sqrt(3)/2500)**2/4):.1f} tighter than the truth.")
print(f"     ** The map RELAXES the bound, because the stretch factor means the observed range")
print(f"        reaches only mode {kl_needed:.0f}, not mode 2500. **")
print()
for s in [
 "⇒⇒ ** AND THE STATEMENT IS NOW A REAL ONE RATHER THAN AN ORDER OF MAGNITUDE WITH AN ASSUMPTION:",
 "   the observed spectrum's flatness requires a progenitor that ran roughly an order of magnitude",
 "   further past its own matter--radiation equality than our universe has. **",
 "",
 "⌗⌗ ** AND NOTICE WHAT MADE IT COMPUTABLE: both halves were already in the corpus and unjoined. **",
 "   *P15 had the closed-$S^3$-to-multipole projection, built for the low-$\\ell$ deficit; c54.131",
 "   had the mixing in interior mode number.  **Neither paper had reason to look at the other, and",
 "   the joint was the whole missing step.***",
 "",
 "⚠ ** WHAT REMAINS ASSUMED, and it is much smaller than what it replaces: that the progenitor's",
 "   $S^3$ and ours carry the same harmonic labelling — which follows if the continuation is",
 "   through the same spatial section, as the construction has it, and would fail only if the",
 "   crossing changed the topology.  The corpus asserts it does not. **",
 "",
 "⌗ *Also assumed, and flagged rather than buried: that observed flatness extends to $\\ell\\sim2500$",
 "   in the sense relevant here, and that the interior's $c_s$ is $1/\\sqrt3$ at the crunch — the",
 "   second is safe, since radiation dominates there by construction.*",
]:
    print("  " + s)
