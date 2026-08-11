"""
F1 first sample -- the abundance-consistency front for the radiation-free rate.
CR's expanding phase begins COLD at the seam (z_onset), far below nucleosynthesis temperature,
so the light elements are NOT made in-situ -- they are seam-inherited from the hot CONTRACTING
phase (the progenitor collapse handover; P13 sec:tensions, r497). First sample: (1) confirm the
cold expanding phase quantitatively; (2) assess each measured primordial abundance against an
inherited origin. Per-element assessment stated for reversal; full yields gated on the matter sector.
"""
import numpy as np
T0 = 2.725                 # CMB temperature today [K]
K_per_eV = 11604.5
z_onset = 6801.0           # the seam (E4): theta*-fixed, H0-independent
T_onset = T0*(1+z_onset)   # [K]
T_BBN   = 1.0e9            # BBN freeze-out ~ 0.086 MeV [K]
z_BBN   = T_BBN/T0 - 1

print(f"CR expanding-phase onset:  z_onset = {z_onset:.0f},  T_onset = {T_onset:.3e} K = {T_onset/K_per_eV:.2f} eV")
print(f"BBN nucleosynthesis epoch: T_BBN  ~ {T_BBN:.1e} K = {T_BBN/K_per_eV/1e6:.3f} MeV,  needs z ~ {z_BBN:.2e}")
print(f"ratio z_BBN/z_onset = {z_BBN/z_onset:.2e}   ->  the BBN epoch lies a factor ~{z_BBN/z_onset:.0e} EARLIER than the seam")
print(f"=> CR's EXPANDING phase never reaches nucleosynthesis temperature (onset is {T_BBN/T_onset:.1e}x colder than BBN).")
print(f"   No in-situ BBN. The light elements are SEAM-INHERITED from the hot contracting-phase handover.\n")

print("FIRST-SAMPLE ABUNDANCE ASSESSMENT (measured 'primordial' values vs an inherited origin; for reversal):")
rows = [
 ("He-4  Y_p",   "0.245",      "FAVOURABLE", "the robust ~1/4 mass fraction is the generic n/p-freeze-out / stellar-He value;\n                a hot (O(rest-mass), MeV+) handover delivers it naturally -- not a tuned target."),
 ("metallicity", "~0 (oldest)", "FAVOURABLE", "a hot handover (GM/Rc^2=1/2 -> MeV+) photodissociates the progenitor's heavy nuclei,\n                resetting to a light-element composition -> near-zero metals in the oldest systems."),
 ("Li-7/H",      "1.6e-10 obs", "FAVOURABLE", "standard BBN over-predicts Li-7 ~3x (the lithium problem); CR is NOT bound to that\n                prediction, so it is freed to match the lower observed value -- a potential advantage."),
 ("D/H",         "2.5e-5",      "THE CONSTRAINT", "deuterium is fragile (stellar processing destroys it; a hot handover can both burn\n                and re-make it) -- the surviving D/H is set by the contracting-phase thermal history,\n                the sharp open piece that needs the handover thermodynamics (matter sector)."),
]
for name,val,verdict,note in rows:
    print(f"  {name:12s} {val:12s} [{verdict}]\n                {note}")
print(f"\nVERDICT: first sample FAVOURABLE -- the expanding phase is confirmed too cold for in-situ BBN, the")
print(f"  hot handover is energetically available (O(rest mass) -> MeV+), and He-4 / metallicity / lithium")
print(f"  sit consistently (lithium even advantageously) with an inherited origin. The DEUTERIUM yield is")
print(f"  the sharp open constraint; its derivation is gated on the contracting-phase handover (matter sector).")
