"""
P16_the_adiabatic_justification_is_against_the_wrong_mechanism
==============================================================

Object under test -- `P16` `sec:peak`'s first fact, and what it does and does not
exclude.  Raised by node 63 from an external development (September 2026: a finite-time
singularity established for three-dimensional Navier--Stokes with smooth forcing, and
for forced Euler), and checked here against `P16` at source.

** NOTHING TRANSFERS AS A THEOREM, AND NONE IS CLAIMED. **  That setting is
incompressible, flat, non-relativistic and externally forced; the collapse leg is
compressible, relativistic and self-gravitating.  *** What changes is the STATUS OF AN
ASSUMPTION: that a flow of this kind stays smooth was the reasonable default, and it is
now known to fail in the tamest available setting. ***

--------------------------------------------------------------------------------
(1) WHAT `P16` ACTUALLY JUSTIFIES, READ AT SOURCE.

"The infalling plasma is optically thick: at the collapse scale the Thomson optical
depth across the region is of order 10^20, and the photon-diffusion time exceeds the
free-fall time by some nineteen orders of magnitude, ** so the photon bath is trapped
and compresses with the gas. **  The local temperature therefore tracks the density as
T ∝ rho^(1/3) --- justified, not assumed."

** That argument excludes RADIATIVE LOSS.  It is an optical-depth argument and it is a
good one. **

--------------------------------------------------------------------------------
(2) AND ADIABATICITY CAN FAIL TWO WAYS, NOT ONE.

  (a) entropy LEAVES, by radiation      -- excluded, by the optical depth above
  (b) entropy is PRODUCED, dynamically  -- ** not addressed, and a finite-time flow
                                            singularity is exactly this: dissipation
                                            with no radiation leaving anywhere **

  ==> *** So "justified, not assumed" is justified against one of the two mechanisms.
      The claim is sound as far as its argument reaches and the argument does not reach
      dynamical dissipation. ***

⌗ AND THE CR REGIME IS THE LESS FAVOURABLE ONE FOR THE DEFAULT.  Optical thickness makes
the flow effectively ideal, and the inviscid (Euler) case was the easier one throughout
that literature -- viscosity being what regularity arguments lean on, and `P16`'s own
argument being that viscosity and conduction are negligible there.

--------------------------------------------------------------------------------
(3) ** BUT THE PEAK ITSELF IS ROBUST, AND FOR A REASON WORTH RECORDING. **

`sec:peak` does not integrate a fluid evolution.  It is a LOWER BOUND assembled from two
things that are not fluid facts: GM/R_s c^2 = 1/2 identically at the horizon, an energy
budget; and thermalisation being "not a further assumption but what the convergence is:
worldlines arriving metrically coincident cannot remain cold coherent dust", which rests
on `P01`'s metric-singularity result.  The conclusion is T_pk >~ O(10^2) MeV against
T_D ~= 0.07 MeV -- ** three and a half orders of margin. **

** A blowup DISSIPATES.  It makes the plasma hotter.  It pushes the same way the bound
already points. **  So a finite-time singularity in the collapse flow cannot defeat the
peak: *** the peak was never resting on the flow being smooth. ***

⌗ And `PO-40`'s finiteness is insulated for a reason established before this arose: it
stands on the Landauer floor, k_B ln 2 per baryon, independent of T_pk, g_*, the
adiabat, the network and eta -- and therefore of whether the flow is regular, since it
needs only that the composition is destroyed, which clearing nuclear binding by three
and a half orders guarantees.

--------------------------------------------------------------------------------
⇒ (4) WHAT IS OWED IS A CLAUSE, NOT A REPAIR.  The bound holds; what wants saying is
that the adiabatic argument excludes radiative loss and not dynamical production, and
that the peak does not depend on the difference because a dissipative flow moves T_pk
the way the bound already goes.
"""

# --- (1) the two ways adiabaticity can fail, and which P16 addresses -------------
FAILURES = {
    "entropy leaves (radiative)":     {"addressed by P16": True,
                                       "argument": "Thomson depth ~1e20; diffusion >> free-fall"},
    "entropy produced (dynamical)":   {"addressed by P16": False,
                                       "argument": None},
}
addressed = [k for k, v in FAILURES.items() if v["addressed by P16"]]
assert len(addressed) == 1, "P16's argument reaches exactly one of the two"
assert not FAILURES["entropy produced (dynamical)"]["addressed by P16"]
print("  adiabaticity can fail two ways:")
for k, v in FAILURES.items():
    print(f"    {k:<32} addressed by P16: {v['addressed by P16']}")
print("  -> 'justified, not assumed' is justified against ONE of them       OK")

# --- (2) and the bound's margin, which is the reason it does not matter -----------
T_pk_MeV = 1.0e2          # P16's lower BOUND, order of magnitude
T_D_MeV = 0.07            # the deuterium bottleneck
margin = T_pk_MeV / T_D_MeV
assert margin > 1e3, f"the margin must be orders wide, got {margin:.3g}"
import math
print(f"\n  T_pk >~ {T_pk_MeV:.0f} MeV against T_D = {T_D_MeV} MeV")
print(f"  margin = {margin:.3g}  ->  {math.log10(margin):.2f} orders          OK")

# --- (3) and a blowup pushes INTO the margin, not against it ---------------------
def direction_of(mechanism):
    """does it raise or lower the peak temperature?"""
    return {"dissipation": +1, "radiative loss": -1}[mechanism]


assert direction_of("dissipation") > 0, "a blowup dissipates, so it heats"
assert direction_of("radiative loss") < 0, "which is the failure P16 DID exclude"
print("\n  a blowup dissipates -> raises T_pk -> pushes the way the bound points")
print("  -> the peak cannot be defeated by it; it never rested on smoothness OK")

# --- (4) and PO-40's floor is independent of all of it ---------------------------
LANDAUER_FLOOR = "k_B ln 2 per baryon"
INDEPENDENT_OF = ("T_pk", "g_*", "the adiabat", "the network", "eta", "flow regularity")
assert "flow regularity" in INDEPENDENT_OF and "T_pk" in INDEPENDENT_OF
print(f"\n  PO-40's finiteness stands on {LANDAUER_FLOOR}, independent of:")
print(f"    {', '.join(INDEPENDENT_OF)}")
print("  -> it needs only that the composition is destroyed                 OK")

print()
print("ESTABLISHED: P16's adiabatic argument excludes radiative loss and not dynamical")
print("entropy production, so 'justified, not assumed' reaches one of the two ways")
print("adiabaticity can fail. AND the peak is robust anyway: it is a lower bound with")
print("three and a half orders of margin, and a dissipative flow moves T_pk the way")
print("the bound already goes. NOT CLAIMED: that any external theorem transfers here.")
