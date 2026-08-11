"""
P15_confront_lowell_data.py -- confronts CR's low-ell prediction with the observed CMB low multipoles, using
  the CORRECTED genuine-Boltzmann depths (0.47/0.41...; the original body's old 0.22/0.20 "striking quadrupole
  match" is SUPERSEDED, per that file's own r962 banner, and is corrected here). Observed/LCDM (literature,
  cosmic-variance-limited): quadrupole ~0.15-0.25 (robustly low), octopole ~0.58-1.10 (estimator-dependent).
  RESULT: CR 0.47 sits ABOVE the sharp observed quadrupole (~0.2) and CR 0.41 mildly below the near-LCDM
  octopole (~0.6-1.0) -- matching neither, a WASH; the likelihood Delta(-2lnL)~+1.8 is verify_lowell_likelihood_v2.py.
STATUS: ✔✔ (data confrontation with corrected depths; wash, matches paper; body brought in line with the r962 correction)
RUN: python3 P15_confront_lowell_data.py   RUNTIME: <1s
ORIGIN: computations/perturbation_verify/confront_lowell_data.py, corrected+verified r1395 (old body superseded per its own banner).
ORIGIN-DIVERGENCE: origin retains the pre-r962 body under its own correction banner; this copy carries the corrected genuine-Boltzmann depths (0.47/0.41, a wash). Adjudicated r2376 (c54.3): THIS COPY AUTHORITATIVE, origin kept as historical record.
"""

import numpy as np
# CR prediction: the CORRECTED genuine-Boltzmann depths (verify_lowell_boltzmann.py, r962),
# superseding the old SW-analytic 0.22/0.20 -- CR/LCDM ratio of ell(ell+1)C_ell:
ell   = np.array([2,    3,    4,    5,    6,    8])
CR    = np.array([0.47, 0.41, 0.36, 0.68, 0.92, 1.00])   # 0.473/0.410/0.356/0.676/0.916/0.998
# observed/LCDM, central estimate and rough range (literature, cosmic-variance-limited):
obs_lo= np.array([0.15, 0.58, 0.55, 0.70, 0.85, 0.95])
obs_hi= np.array([0.25, 1.10, 1.05, 1.10, 1.05, 1.05])
print(" ell   CR    obs(range)        verdict")
for i,l in enumerate(ell):
    inside = obs_lo[i] <= CR[i] <= obs_hi[i]
    v = "MATCH" if inside else ("CR LOW (mild over-suppression)" if CR[i] < obs_lo[i] else "CR HIGH (over-predicts power)")
    print(f"  {l}   {CR[i]:.2f}   {obs_lo[i]:.2f}-{obs_hi[i]:.2f}   {v}")
print("\n quadrupole: CR 0.47 vs obs ~0.2  -> CR sits ABOVE the sharp observed quadrupole dip")
print(" octopole:   CR 0.41 vs obs ~0.6-1.0 -> mild over-suppression, not severe")
print(" NET: a WASH -- CR's smooth ~0.4-0.5 deficit matches neither the sharp quadrupole nor the")
print("      near-LCDM octopole, sitting between them. Likelihood Delta(-2lnL)~+1.8 (verify_lowell_likelihood_v2.py),")
print("      well inside cosmic variance (<3 sigma over 2<=ell<=30). Neither a correspondence success nor a")
print("      sharp falsification risk. The quadrupole-octopole ALIGNMENT anomaly is separate; CR predicts power, not orientation.")

# =====================================================================
# ** CHECKS, added r2376+c54.154.  Print-only until now.  The claim P15 draws from this file is a
#    DIRECTION PAIR -- CR above the observed quadrupole and below the observed octopole, matching
#    neither -- so that pair is what is asserted. **
_fail = []
if not CR[0] > obs_hi[0]:
    _fail.append(f"CR {CR[0]} is not above the observed quadrupole band {obs_lo[0]}-{obs_hi[0]}")
if not CR[1] < obs_lo[1]:
    _fail.append(f"CR {CR[1]} is not below the observed octopole band {obs_lo[1]}-{obs_hi[1]}")
if not (min(CR[:4]) == CR[2]):
    _fail.append("CR's own minimum over ell = 2..5 is not at ell = 4")
# ** the 'matches neither' is a claim about the DEFICIT REGION, ell <= 5.  Above it CR has
#    essentially no deficit and does match (ell = 6 and 8 sit inside their bands), which is not a
#    counterexample but is worth having asserted rather than assumed -- the first draft of this
#    check tested every ell and fired, which is how the distinction got written down. **
_lo_region = [i for i, l in enumerate(ell) if l <= 5]
if any(obs_lo[i] <= CR[i] <= obs_hi[i] for i in _lo_region):
    _fail.append("a multipole in the deficit region ell <= 5 MATCHES; the verdict is not 'a wash'")
if not all(obs_lo[i] <= CR[i] <= obs_hi[i] for i, l in enumerate(ell) if l >= 6):
    _fail.append("CR fails to match ABOVE the deficit region, which would be a different problem")
print()
print("  ** CHECKS (c54.154): CR asserted ABOVE the observed quadrupole band and BELOW the "
      "observed")
print("     octopole band, its own minimum asserted at ell = 4, and NO multipole asserted inside "
      "its")
print("     band FOR ell <= 5 -- which is the 'matches neither' the paper reads off this file --")
print("     while ell >= 6 is asserted to match, since that is where CR carries no deficit. **")
if _fail:
    print("FAILED: " + "; ".join(_fail))
    raise SystemExit(1)
print("  CHECKS PASS")
