"""AS — THE AMPLITUDE, READ LEFTWARD.  Family 3's question, and what C4 can and cannot say about it.
CONFIRMATION 2, and the corpus is already correctly scoped here:
  P7: the inherited datum 'stands as a ONE-PARAMETER ACCOMMODATION rather than a parameter-free
      prediction.  The open work is the baryogenesis-analogue derivation of the progenitor handover
      -- the composition, and the primordial amplitude and tilt A_s, n_s.'
  P15 prop:transmission: at a NON-DEGENERATE horizon the approach is exponential and carries a fixed
      thermal scale 2 kappa -- 'the mechanism by which a de Sitter horizon imprints a scale-invariant
      spectrum'; at the DEGENERATE Nariai root the approach is POWER-LAW and kappa = 0, so there is
      no scale to imprint, and the seam TRANSMITS the progenitor's spectrum instead."""
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
""")
print("="*80)
