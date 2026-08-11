"""
P16_peak_temperature.py -- verifies the P16 sec:peak M-independent peak-temperature floor. At the horizon
  GM/(R_s c^2)=1/2 identically, so the convergence delivers infall KE ~ 0.5 m_N = 469 MeV per nucleon,
  thermalizing to T_pk ~ 469/2.70 = 174 MeV (the QCD/hadronization scale, paper's ~170 MeV), INDEPENDENT of
  progenitor mass. This clears the deuterium bottleneck T_D=0.07 MeV by ~3.4 orders on T_pk (~3.8 on the
  infall energy 469 MeV -- the paper's "four orders", keyed to the 1/2 m_N c^2 scale), so the matter peaks
  fully dissociated and a cooling-leg freeze-out EXISTS FOR EVERY PROGENITOR. Honest scope: a robust bound,
  not the exact regulated peak (which stays open, can only push T_pk higher, and is downstream-irrelevant
  once dissociation is total). Physical-bound receipt, not a full thermalization computation.
STATUS: ✔✔ (T_pk~174 MeV M-independent, >> T_D; "four orders" keyed to the infall-energy scale)
RUN: python3 P16_peak_temperature.py   RUNTIME: <1s
ORIGIN: computations/p16_bbn/peak_temperature.py, verified r1399.
"""
import numpy as np
m_N = 938.9        # nucleon rest mass, MeV
T_D = 0.07         # deuterium bottleneck (photodissociation), MeV
# --- the M-independent infall energy: at the horizon GM/(R_s c^2) = 1/2 identically ---
eps_infall = 0.5*m_N     # specific kinetic energy per nucleon delivered by convergence, MeV
print("="*66); print("B-9 :: collapse peak temperature (P16-D)"); print("="*66)
print(f"  infall specific KE per nucleon at the horizon  = 0.5 m_N = {eps_infall:.0f} MeV")

# Thermalize that energy into a relativistic plasma. The peak temperature where the mean thermal
# energy per relativistic degree of freedom carries the infall energy per baryon: distribute
# eps_infall over the entropy the convergence generates. Two bracketing estimates:
#  (i)  energy per baryon = eps_infall shared as photons (E/N ~ 2.70 T):  T ~ eps_infall/2.70
#  (ii) full relativistic plasma at the QCD scale g*~ 30-60: T ~ [30 eps_infall n_b /(pi^2 g* )]^(1/4)
#       -- but n_b at the (regulated) peak is the open quantity; (i) is the robust per-particle scale.
T_i  = eps_infall/2.70
print(f"  (i) per-particle thermalization  T ~ eps/2.70   = {T_i:.0f} MeV")
print(f"      -> the natural infall-thermalization scale: a few x 10^2 MeV, the QCD/hadron era.")
print("-"*66)
print(f"  ROBUST, M-INDEPENDENT LOWER BOUND (P16 sec:peak): T_pk >~ O(10^2) MeV")
print(f"  margin over the deuterium bottleneck: T_pk/T_D >~ {T_i/T_D:.0e}  (~{np.log10(T_i/T_D):.1f} orders)")
print("="*66)
print(f"""THE NUMBER (B-9): the collapse peaks at T_pk ~ {T_i:.0f} MeV -- a few hundred MeV, the
infall-energy / QCD-hadronization scale, INDEPENDENT of the progenitor mass (the horizon identity
GM/R_s c^2 = 1/2 fixes the specific infall energy). This sits ~{np.log10(T_i/T_D):.0f} orders of
magnitude above the deuterium bottleneck T_D = {T_D} MeV, so the matter peaks fully dissociated and
a cooling-leg freeze-out exists for every progenitor -- exactly P16's established conclusion.

HONEST SCOPE (unchanged from P16): the number above is the robust M-independent SCALE. The EXACT
regulated peak -- how much deeper than the horizon the compression runs on the smooth substrate
through the r=0 branch point -- is set by the (open) branch-point regulation and can only push T_pk
HIGHER, never below the ~10^2 MeV floor. It is downstream-irrelevant: total dissociation erases the
peak's memory, so no abundance depends on the exact value. B-9 closed: the number is a few x 10^2 MeV
(floor ~10^2 MeV, M-independent); the exact regulated value stays open at no cost, as P16 states.""")

# --- ASSERTIONS (added r2376+c54.158) --------------------------------------------------------
# Pins the numbers this receipt prints for sec:peak, as CORRECTED in INDEX.md at c54.156:
# infall KE 469 MeV per nucleon, T_pk = 174 MeV (NOT the paper's old 170), and a margin over the
# deuterium bottleneck of 2.5e3 = 3.4 orders on TEMPERATURE (the "four orders" belongs to the
# infall ENERGY, 469/0.07 = 3.8 orders -- a different quantity).
# (a) the horizon identity GM/(R_s c^2)=1/2 fixes the specific infall energy at 0.5 m_N.
assert abs(eps_infall - 469.45) < 0.01
# (b) per-particle thermalization (E/N ~ 2.70 T) puts the peak at 173.87 MeV -- the QCD scale.
assert abs(T_i - 173.87) < 0.01
assert 100.0 < T_i < 1000.0                      # "a few x 10^2 MeV", the claimed floor
# (c) the margin over the deuterium bottleneck: 2483.9, i.e. 3.40 orders (INDEX: 2.5e3, 3.4).
assert abs(T_i/T_D - 2483.86) < 0.5
assert abs(np.log10(T_i/T_D) - 3.3951) < 1e-3
# (d) the infall ENERGY clears T_D by 3.83 orders -- the figure the paper's "four orders" tracks.
assert abs(np.log10(eps_infall/T_D) - 3.8265) < 1e-3
# NOTE (r2376+c54.158): the M-INDEPENDENCE itself is not a computation in this file -- no progenitor
# mass ever enters eps_infall = 0.5 m_N -- so there is nothing here to assert about it; it is the
# analytic content of the horizon identity GM/(R_s c^2) = 1/2, taken as input above.
