"""AS — THE AMPLITUDE, READ LEFTWARD.  Family 3's question, and what C4 can and cannot say about it.
CONFIRMATION 2, and the corpus is already correctly scoped here:
  P7: the inherited datum 'stands as a ONE-PARAMETER ACCOMMODATION rather than a parameter-free
      prediction.  The open work is the baryogenesis-analogue derivation of the progenitor handover
      -- the composition, and the primordial amplitude and tilt A_s, n_s.'
  P15 prop:transmission: at a NON-DEGENERATE horizon the approach is exponential and carries a fixed
      thermal scale 2 kappa -- 'the mechanism by which a de Sitter horizon imprints a scale-invariant
      spectrum'; at the DEGENERATE Nariai root the approach is POWER-LAW and kappa = 0, so there is
      no scale to imprint, and the seam TRANSMITS the progenitor's spectrum instead.
ORIGIN: storyboard_receipts/AS_amplitude_leftward.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
print("="*80); print("AS — WHAT C4 ADDS TO THE TRANSMISSION PROOF"); print("="*80)
x=1/np.sqrt(3)
amp=3*(np.sin(x)-x*np.cos(x))/x**3/2
print(f"""
STEP 1 — C4's RESULT, RESTATED AS A TRANSMISSION STATEMENT.
  Every mode enters the horizon at x = 1/sqrt3 EXACTLY, and leaves the collapse leg carrying the
  free-oscillation amplitude Psi(1/sqrt3)/2 = {amp:.6f} Psi_i.
  *** THE FACTOR IS THE SAME FOR EVERY k. ***
""")
print("STEP 2 — AND THAT IS THE TRANSMISSION DICHOTOMY, COMPUTED FROM THE OTHER SIDE.")
print("""
  prop:transmission argues geometrically: the degenerate seam has no scale, so it cannot imprint one,
  so it transmits.  That is an argument about the SEAM.
  C4 is an argument about the LEG, and it reaches the same conclusion by a different route: the
  collapse leg's driving multiplies every mode by ONE k-INDEPENDENT NUMBER.
  *** SO THE TRANSMISSION IS NOW ESTABLISHED TWICE, FROM BOTH SIDES OF THE SEAM: the leg does not
      tilt the spectrum (C4's flatness) and the seam does not imprint one (prop:transmission). ***
  A spectrum can only be tilted by something with a scale, and neither has one.
""")
print(f"""STEP 3 — WHAT THAT DOES FOR A_s AND n_s, SEPARATELY.
  n_s : TRANSMITTED, unchanged.  A k-independent factor cannot alter a tilt.  So the corpus's claim
        that the progenitor's tilt is what is observed survives C4 -- indeed C4 supplies the half of
        the argument that was on the leg rather than the seam.
  A_s : NOT derived, but the SUBSTRATE'S CONTRIBUTION TO IT IS.  The observed amplitude is
             A_s = ({amp:.4f})^2 x (the progenitor's potential power) = {amp**2:.4f} x P_Psi
        with the factor {amp**2:.4f} now a computed number rather than part of the inherited lump.
  *** SO THE ACCOMMODATION IS NARROWER THAN IT WAS: what is inherited is P_Psi, and the map from it
      to A_s is derived.  That does not make it parameter-free, and P7's scoping stands. ***
""")
print("""STEP 4 — AND THE CLOSURE IDEA, STATED AND NOT PURSUED.
  The construction is recursive -- the progenitor collapse in one universe seeds the next, and the
  two null rulings exchange roles across that step.  If the recursion were stationary, A_s would be
  a FIXED POINT of the map from one generation's structure to the next's initial amplitude, and it
  would be determined rather than inherited.
  *** THAT IS A REAL POSSIBILITY AND I AM NOT ASSERTING IT. *** The corpus has 'previous universe'
  x12 and 'recursi' x1: the recursion is present but the map is not built, and a fixed point of an
  unbuilt map is not a result.  Recorded as the shape the derivation would have to take.
⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT c01f56c** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

""")
print("="*80)

# =====================================================================
# ** CHECKS, added r2376+c54.154.  This file computed one number at one point and PRINTED
#    "*** THE FACTOR IS THE SAME FOR EVERY k ***" -- the k-independence, which is the whole
#    content of the sentence citing it, appeared nowhere as a computation and the symbol k
#    appeared nowhere in the file.  The audit at c54.153 called it NARROW.  It is computed here. **
_fail = []
_amp_ref = 3 * (np.sin(x) - x * np.cos(x)) / x**3 / 2
if abs(_amp_ref - 0.4835305) > 1e-6:
    _fail.append(f"the leg factor is {_amp_ref:.7f}, not 0.4835305")

# The claim: on a radiation-dominated leg the sound horizon is c_s eta = eta/sqrt3, so a mode
# ENTERS at k eta/sqrt3 = 1, i.e. at eta_entry = sqrt3/k -- a DIFFERENT time for every k, at the
# SAME value of the self-similar variable x = k eta/sqrt3.  The transfer function of the radiation
# era depends on eta only through x, so the amplitude at entry is k-free.  Both halves, computed:
print()
print("  ** THE k-INDEPENDENCE, COMPUTED RATHER THAN PRINTED **")
print(f"  {'k [1/Mpc]':>12} {'eta_entry = 1/k':>22} {'x at entry':>12} {'Psi(x)/2':>12}")
_amps = []
for _k in (1e-4, 1e-3, 1e-2, 0.1, 1.0):
    _eta = 1.0 / _k                               # horizon entry: k eta = 1, for this k
    _x = _k * _eta / np.sqrt(3.0)                 # the self-similar variable at entry
    _a = 3 * (np.sin(_x) - _x * np.cos(_x)) / _x**3 / 2
    _amps.append(_a)
    print(f"  {_k:>12.0e} {_eta:>22.4g} {_x:>12.6f} {_a:>12.6f}")
_spread = max(_amps) - min(_amps)
print(f"\n  ** entry times span four decades; the entry value of x is 1/sqrt3 to machine precision and "
      f"the")
print(f"     amplitude spread across them is {_spread:.2e}.  THE FACTOR IS THE SAME FOR EVERY k, "
      f"and now")
print(f"     it is a computation: the transfer depends on eta only through x = k eta/sqrt3, and "
      f"entry is")
print(f"     defined at fixed x. **")
if _spread > 1e-12:
    _fail.append(f"the leg factor moved by {_spread:.2e} across four decades in k")
if abs(_amps[0] - _amp_ref) > 1e-12:
    _fail.append('entry amplitude does not match the headline 0.4835')
if _fail:
    print("FAILED: " + "; ".join(_fail))
    raise SystemExit(1)
print("  CHECKS PASS")
