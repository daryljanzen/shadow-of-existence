# *** CORRECTED (r962): CR depth is 0.47/0.41 (genuine Boltzmann, verify_lowell_boltzmann.py), NOT
# 0.22/0.20. The 'striking quadrupole match' does NOT survive (CR 0.47 sits above observed ~0.2), the
# octopole over-suppression softens (0.41 vs ~0.6-1.0), and the low-ell likelihood is a WASH
# (Delta(-2lnL)~+1.8, verify_lowell_likelihood_v2.py). The verdict below is superseded by that wash. ***
"""
THE CONFRONTATION WITH THE DATA -- CR's low-ell prediction vs the observed CMB low multipoles.
The correspondence test (the outward edge). Reported straight, at weight, no manufactured coherence:
CR matches the quadrupole strikingly and is in TENSION at the octopole.

CR PREDICTION (verify_lowell_full_radiative.py), as CR/LCDM ratio of ell(ell+1)C_ell (full radiative
order: SW + early + late ISW, continuum-validated):
   ell=2: 0.22   ell=3: 0.20   ell=4: 0.31   ell=5: 0.70   ell=6: 0.93   ell>=8: ~1.0
i.e. a parameter-free deficit, ell=2 AND ell=3 both ~0.2, recovering by ell~6-8. The mechanism (flat
projection of the discrete closed-S^3 source, lowest mode k_2 -> ell~8) starves ell=2 and ell=3 ALIKE.

OBSERVED low multipoles (literature; estimator- and mask-dependent, cosmic-variance-limited):
 - Quadrupole D_2 = ell(ell+1)C_2/2pi:  ~176-250 uK^2 (Efstathiou max-likelihood, astro-ph/0310207),
   WMAP-team pseudo-C_l 123 uK^2.  LCDM expectation ~1000-1250 uK^2.  => observed/LCDM ~ 0.15-0.25.
 - Octopole D_3:  ~794-1183 uK^2 (Efstathiou), WMAP-team 611 uK^2.  LCDM ~1000-1100 uK^2.
   => observed/LCDM ~ 0.6-1.1 (estimator-dependent; Efstathiou's mid/high end is ~LCDM-normal).
 - The deficit is "coherently low" over 2<=ell<=30 but dominated by the quadrupole; overall <3 sigma
   (cosmic variance), "especially ell=2" robustly, ell=3 ambiguous (A&A 2021; Planck 2013 XXIII;
   Bennett 2011).  The quadrupole-octopole ALIGNMENT is a SEPARATE anomaly (orientation, not power);
   CR predicts power, not alignment, and does not address it.

THE HONEST VERDICT:
 - QUADRUPOLE: STRIKING MATCH. CR predicts 0.22; observed ~0.2. A parameter-free number, set by
   Lambda through r_0 and D_C, landing on the single most robust large-angle anomaly. Not retrofitted.
 - OCTOPOLE: TENSION. CR predicts 0.20 (octopole as suppressed as the quadrupole); the observed
   octopole is mostly higher (~0.6-1.0 of LCDM), only "low" under the more aggressive estimators.
   CR's mechanism over-predicts the octopole suppression: it cannot make ell=2 low without making
   ell=3 low by nearly the same factor, because the single floor k_2 starves them together. The
   observed sky has a sharp quadrupole-only suppression that CR's smooth ell<~7 deficit does not
   reproduce.
 - SIGNIFICANCE CEILING: the data are cosmic-variance-limited (<3 sigma over 2<=ell<=30), so neither
   the quadrupole match nor the octopole tension can be made decisive at the lowest multipoles. The
   confrontation is real but the instrument is blunt here.

PIVOT (for the programme, not asserted into the corpus as resolved):
 - The quadrupole match is a genuine, parameter-free correspondence success -- worth stating exactly,
   not inflated into "CR explains the low-ell anomaly" (it does not explain the octopole).
 - The octopole tension is the falsification edge the mechanism actually exposes: does the full
   transfer (Doppler, the exact discrete measure, a genuine Boltzmann solve) differentiate ell=2 from
   ell=3, or is the smooth ell<~7 deficit a firm CR prediction in tension with the data? That is the
   live question this test hands back -- a real next move, not a verdict.
 - Coherence shown is not correspondence earned: this is the outward edge, and it reads as a partial
   match with a real tension, held at exactly that weight.

(Sources: arXiv:astro-ph/0310207 Efstathiou; A&A 2021 aa41251-21; Planck 2013 XXIII arXiv:1303.5083;
arXiv:1501.02647. LCDM low-ell D_ell ~1000-1250 uK^2 is the standard SW-plateau+ISW expectation.)
"""
import numpy as np
# CR prediction (from verify_lowell_full_radiative.py), CR/LCDM ratio:
ell   = np.array([2,    3,    4,    5,    6,    8])
CR    = np.array([0.22, 0.20, 0.31, 0.70, 0.93, 1.00])
# observed/LCDM, central estimate and rough range (cosmic-variance-limited):
obs_lo= np.array([0.15, 0.58, 0.55, 0.70, 0.85, 0.95])
obs_hi= np.array([0.25, 1.10, 1.05, 1.10, 1.05, 1.05])
obs_c = 0.5*(obs_lo+obs_hi)
print(" ell   CR    obs(range)        verdict")
for i,l in enumerate(ell):
    inside = obs_lo[i] <= CR[i] <= obs_hi[i]
    v = "MATCH" if inside else ("CR LOW (tension)" if CR[i] < obs_lo[i] else "CR HIGH")
    print(f"  {l}   {CR[i]:.2f}   {obs_lo[i]:.2f}-{obs_hi[i]:.2f}   {v}")
print("\n quadrupole: CR 0.22 vs obs ~0.2  -> STRIKING MATCH (parameter-free)")
print(" octopole:   CR 0.20 vs obs ~0.6-1.0 -> TENSION (CR over-predicts suppression)")
print(" data <3sigma, cosmic-variance-limited: confrontation real, instrument blunt at lowest ell")
