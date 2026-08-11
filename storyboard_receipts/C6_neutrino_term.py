"""C6 — THE ANISOTROPIC-STRESS TERM.  The second of C4's two named terms.
FINDING ZERO, before any physics: the corpus's TEXT says 'neutrino' ZERO times, and
'anisotropic stress' zero, and 'free-streaming' zero -- while its BBN CODE carries them explicitly
(bbn_network.py: 'neutrinos share the plasma T until ~ e+- annihilation, then decouple to (4/11)^1/3').
*** SO THE CORPUS COMMITS TO A NEUTRINO BACKGROUND IN ITS COMPUTATIONS AND NEVER SAYS SO IN ITS
    PAPERS.  That is an implicit commitment, and it is load-bearing for what follows. ***"""
import numpy as np
print("="*80); print("C6 — THE NEUTRINO TERM"); print("="*80)
print("""
STEP 1 — THE ESCAPE THAT WOULD HAVE BEEN CONVENIENT, AND FAILS.
  If the driving happened above ~1 MeV the neutrinos would still be COUPLED, carrying no anisotropic
  stress, and Phi = Psi would be EXACT.  Checked against the corpus's own seam temperature (1.6 eV,
  P16) with T ~ 1/r: coupling needs k/k_s > 6.25e5.  The modes of interest are k/k_s ~ 1 to 1e3.
  *** THE ESCAPE FAILS BY FIVE ORDERS OF MAGNITUDE.  Phi != Psi on the driving leg. ***

STEP 2 — SO THE TERM IS REAL.  WHAT DOES IT DO, AND IS IT SHARED?
  Two things must be separated, and they have different answers.
  (a) IS THE PHYSICS THE SAME ON A CONTRACTING LEG?
      Free-streaming is collisionless geodesic transport, and the collisionless Boltzmann equation is
      TIME-REVERSAL INVARIANT.  So the neutrino sector time-reverses with the rest of the leg, exactly
      as P15's driving argument requires of the photon sector.  *** No new physics is needed. ***
  (b) IS THE FRACTION THE SAME?
      The effect is governed by f_nu = rho_nu/rho_rad, fixed by N_eff and the temperature ratio.
      *** BOTH ARE SHARED WITH LambdaCDM, because the cooling leg IS a standard BBN -- which is the
          corpus's own claim and is what the network code implements. ***
""")
fnu=0.4052
print(f"STEP 3 — THE MAGNITUDE, quoted as standard and not derived here.")
print(f"   f_nu = rho_nu/rho_rad = {fnu:.4f} for three species with the (4/11)^(4/3) ratio:")
r_nu=(4/11)**(4/3); N=3.046
print(f"      check: 3.046 x (7/8) x (4/11)^(4/3) / [1 + 3.046 x (7/8) x (4/11)^(4/3)] = "
      f"{(N*(7/8)*r_nu)/(1+N*(7/8)*r_nu):.4f}")
print("   Bashinsky & Seljak (2004): free-streaming neutrinos produce, for modes well INSIDE the")
print("   horizon, a CONSTANT phase shift and a CONSTANT amplitude suppression -- both k-INDEPENDENT")
print("   in that limit.  This is standard radiation-era physics, cited not re-derived.")
print("""
  *** AND THAT IS THE LOAD-BEARING POINT FOR THIS BUILD: ***
  C4's result is that the driving ENVELOPE is FLAT above ~10 k_s.  A k-INDEPENDENT rescaling and a
  k-INDEPENDENT phase shift leave a flat envelope FLAT.
  *** SO THE NEUTRINO TERM CHANGES THE ENVELOPE'S NORMALISATION AND PHASE AND NOT ITS SHAPE -- and
      the shape is what P15 named uncomputed. ***
""")
print("STEP 4 — WHAT BREAKS, HONESTLY.")
print("   The exact potential is no longer 3(sin x - x cos x)/x^3: with free-streaming neutrinos the")
print("   equation is integro-differential and its solution is NOT elementary.  So:")
print("     * the CLOSED FORM for Psi(x) holds for the photon-baryon fluid alone;")
print("     * with neutrinos it is a correction whose deep sub-horizon limit is k-independent;")
print("     * *** the closure is therefore a property of the SKELETON, not of the full system, and")
print("         C4's flat envelope survives the correction while C1's exact Psi does not. ***")
print("   Both statements are kept. Neither is softened into the other.")
print("="*80)
