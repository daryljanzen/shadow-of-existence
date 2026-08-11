"""C7 — THE STEP THE TRAP WAS GUARDING.
full_transfer_verdict.py ASSUMED the high-ell peaks equal LambdaCDM's and applied the extra damping,
getting a large deficit -- and P15 disowns it because 'that assumption IS the unbuilt part.'
C4 built it.  So the same calculation can now be done with a DERIVED envelope.
FIRST, though, one number that decides everything and that I have not yet checked.
ORIGIN: storyboard_receipts/C7_equality_and_deficit.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np
print("="*80); print("C7 — WHERE IS EQUALITY IN THIS COSMOLOGY?"); print("="*80)
z_onset=6797.0; ratio_seam=2.0
print(f"""
  The boost is not flat forever: in LambdaCDM the modes that get it are those entering BEFORE
  matter-radiation EQUALITY, and the turnover of the envelope sits at the equality scale.  So the
  envelope's shape is fixed by WHERE EQUALITY IS -- and I have not checked that against LambdaCDM's.

  The corpus's inherited datum: rho_r/rho_m = {ratio_seam} AT THE SEAM, z_onset = {z_onset:.0f}.
  rho_r/rho_m ~ (1+z), so equality (ratio = 1) is at
""")
z_eq_CR=(1+z_onset)/ratio_seam - 1
print(f"     1+z_eq = (1+z_onset)/{ratio_seam:.0f} = {1+z_eq_CR:.1f}   ->   z_eq(CR) = {z_eq_CR:.0f}")
print(f"     LambdaCDM's:  z_eq ~ 3400")
print(f"     *** RATIO: {(1+z_eq_CR)/3401:.4f} ***")
print("""
  *** THE INHERITED DATUM PUTS EQUALITY AT ESSENTIALLY LambdaCDM's REDSHIFT. ***
  That is not a fit -- rho_r/rho_m ~ 2 at the seam is the corpus's single inherited number, measured
  from the acoustic scale, and z_eq falls out of it.  So the mode that divides boosted from unboosted
  is the SAME mode in both cosmologies.
  => C4's flat envelope turns over at the SAME k as LambdaCDM's.  The peaks track, and they track for
     a structural reason and not by assumption.
""")
print("="*80); print("SO NOW THE STEP THE TRAP GUARDED, DONE HONESTLY"); print("="*80)
print("""
  The two inputs are now BOTH derived rather than one derived and one assumed:
    * the driving envelope -- flat, saturating, turning over at LambdaCDM's equality scale (C4 + above);
    * the diffusion length -- ~9% longer, CR-specific, non-reabsorbable (P15 damping_ratio_clean).
  Damping enters as exp[-(k/k_D)^2] with k_D ~ 1/r_D, so a 9% longer r_D is a 9% SMALLER k_D:
""")
f=1.09
for l in [500,800,1000,1500,2000,2500]:
    # ratio of suppressions at fixed k: exp[-(k/k_D,CR)^2] / exp[-(k/k_D,LCDM)^2]
    # k/k_D scales with l/l_D ; take l_D ~ 1400 for LambdaCDM
    lD=1400.0
    supp_L=np.exp(-(l/lD)**2)
    supp_C=np.exp(-(l*f/lD)**2)
    print(f"     ell={l:>5d}:  LambdaCDM exp[-(l/l_D)^2] = {supp_L:.4f}   CR = {supp_C:.4f}   ratio = {supp_C/supp_L:.4f}")
print("""
  *** THE DEFICIT IS REAL AND IT DOES NOT CANCEL. ***
  With the envelope now DERIVED and found to track, there is nothing left to offset the extra
  damping: CR predicts LESS high-ell power than flat LambdaCDM, by a factor that grows as
  exp[-(l/l_D)^2 (f^2 - 1)] with f = 1.09.
  This is the honest outcome, and it is the OPPOSITE of a rescue.
""")
print("="*80)

# ============================================================================================
# GATE — r2376+c54.160.  This receipt printed its equality redshift and its deficit table and
# asserted nothing.  What is gated is C7's own claim, which CR_cosmology.tex sec:envelope cites:
# "Its turnover sits at equality, and the inherited datum places equality at
#  1+z_eq = (1+z_onset)/2 = 3399, essentially flat LambdaCDM's -- so the envelope turns over at
#  the same wavenumber, for a structural reason and not by assumption."
#   (1) the equality redshift the inherited datum produces, pinned to 3399 exactly as the paper
#       prints it -- if z_onset or rho_r/rho_m at the seam is retuned, this fails first;
#   (2) "essentially flat LambdaCDM's" made a gate: the ratio to 3401 is within a tenth of a
#       per cent, and it is pinned to the 0.9994 the receipt prints;
#   (3) the deficit itself -- the last row of the receipt's own table, and the closed form
#       exp[-(l/l_D)^2 (f^2-1)] it says the table realises, both pinned at ell = 2500.
# ============================================================================================
assert abs(z_eq_CR - 3398.0) < 0.05, f"z_eq(CR) = {z_eq_CR:.1f}, expected 3398"
assert abs((1 + z_eq_CR) - 3399.0) < 0.05, \
    f"1+z_eq = (1+z_onset)/{ratio_seam:.0f} = {1+z_eq_CR:.1f}, CR_cosmology.tex says 3399"
assert abs((1 + z_eq_CR)/3401 - 0.9994) < 1.0e-4, \
    f"ratio to LambdaCDM equality = {(1+z_eq_CR)/3401:.4f}, expected 0.9994"
assert abs((1 + z_eq_CR)/3401 - 1) < 0.001, \
    "equality is no longer 'essentially flat LambdaCDM's' -- the structural coincidence has drifted"
# (3) the deficit.  supp_L, supp_C are the last table row (ell = 2500); f = 1.09, l_D = 1400.
assert abs(supp_L - 0.041222) < 1.0e-6, f"LambdaCDM suppression at ell=2500 is {supp_L:.6f}"
assert abs(supp_C - 0.022628) < 1.0e-6, f"CR suppression at ell=2500 is {supp_C:.6f}"
assert abs(supp_C/supp_L - 0.548917) < 1.0e-6, \
    f"deficit ratio at ell=2500 is {supp_C/supp_L:.6f}, expected 0.548917"
assert abs(supp_C/supp_L - np.exp(-(2500/lD)**2*(f**2 - 1))) < 1.0e-12, \
    "the tabulated ratio is not exp[-(l/l_D)^2 (f^2-1)] -- the closed form C7 states does not hold"
assert supp_C < supp_L, "the deficit has changed sign: CR no longer predicts LESS high-ell power"
print(f"GATE C7 (r2376+c54.160): 1+z_eq = {1+z_eq_CR:.1f} ({(1+z_eq_CR)/3401:.4f} of LambdaCDM's), "
      f"deficit at ell=2500 = {supp_C/supp_L:.4f} -- equality and deficit pinned.")
