"""C2 — THE LIMITS. The comoving Hubble radius across the excursion, from the corpus's own geometry.
CONFIRMATION 4 — the object, and I take it from the corpus rather than from cosmology-by-habit:
  the E=1 (marginally bound) congruence IS this cosmology.  On it (dr/dtau~)^2 = E^2 - f = 1 - f,
  with f = 1 - 2M/r - r^2/alpha^2.  The signed areal radius r is the scale-factor analogue.
ORIGIN: storyboard_receipts/C2_horizon_limits.py -- registered r2376 (c54); edit the origin, not this copy."""
import sympy as sp, numpy as np
r,M,al,A=sp.symbols('r M alpha A', positive=True)
f=1-2*M/r-r**2/al**2
print("="*80); print("C2 — WHERE THE COMOVING HUBBLE RADIUS TURNS"); print("="*80)
print("\nSTEP 1 — the E=1 law IS a Friedmann equation. Derive, do not assert.")
oneminusf=sp.simplify(1-f)
print(f"   (dr/dtau)^2 = 1 - f = {oneminusf}")
H2=sp.simplify(oneminusf/r**2)
print(f"   so  H^2 = (1/r . dr/dtau)^2 = (1-f)/r^2 = {sp.expand(H2)}")
print("   *** = 2M/r^3 + 1/alpha^2 : EXACTLY matter + Lambda, with r the scale factor. ***")
print("   (and its solution is the corpus's own r ~ sinh^{2/3}, which is why the bead law is that.)")

print("\nSTEP 2 — L2 carries radiation as well. Add it as the corpus says: gravitating normally.")
H2r=A/r**4+2*M/r**3+1/al**2
print(f"   H^2 = {H2r}      (radiation ~ r^-4, matter ~ r^-3, substrate constant)")
com=sp.simplify(1/(r**2*H2r))
print(f"   comoving Hubble radius squared = 1/(r H)^2 = {sp.simplify(sp.together(com))}")
print("   -> (rH)^2 = A/r^2 + 2M/r + r^2/alpha^2, which is (1-f) + A/r^2 :")
print(f"      check: (1-f) + A/r^2 = {sp.expand(oneminusf+A/r**2)}   vs   r^2 H^2 = {sp.expand(r**2*H2r)}")
print("   *** THE COMOVING HUBBLE RADIUS IS BUILT FROM THE CORPUS'S OWN TURNAROUND FUNCTION 1-f. ***")

print("\nSTEP 3 — WHERE IT TURNS.  (rH)^{-1} is minimal where r^2 H^2 is maximal.")
expr=sp.expand(oneminusf+A/r**2)
d=sp.simplify(sp.diff(expr,r))
print(f"   d/dr [ (rH)^2 ] = {sp.factor(d)}")
quart=sp.simplify(sp.numer(sp.together(d)))
print(f"   setting it to zero:  {sp.factor(quart)} = 0")
print("   -> a QUARTIC in r.  Take the vacuum case A=0 first, which is the pure bead:")
q0=sp.simplify(quart.subs(A,0))
print(f"      A=0:  {sp.factor(q0)} = 0   ->   r^3 = M alpha^2")
print(f"      sols: {sp.solve(sp.Eq(q0,0), r)}")
print("   *** r = (M alpha^2)^{1/3}.  AND THAT IS THE LOCUS f' = 0: ***")
print(f"      f'(r) = {sp.simplify(sp.diff(f,r))} ,  zero at r^3 = {sp.solve(sp.Eq(sp.diff(f,r),0), r)}")
print("   *** SO THE COMOVING HUBBLE RADIUS EXTREMISES EXACTLY AT f' = 0. ***")

print("\n" + "="*80)
print("STEP 4 — WHICH WAY DOES IT TURN?  Get the sense right before saying anything.")
print("="*80)
import numpy as np
Mv, alv = 1.0, 3*np.sqrt(3)          # Nariai in the gauge 2M = 2/(3sqrt3) alpha ... set explicitly below
alv = 1.0; Mv = 1/(3*np.sqrt(3))     # Nariai: M = alpha/(3 sqrt3)
def rH2(rr, A=0.0): return A/rr**2 + 2*Mv/rr + rr**2/alv**2
rHE=(Mv*alv**2)**(1/3)
print(f"   gauge alpha=1, Nariai M = 1/(3sqrt3) = {Mv:.6f};  f'=0 at r = (M alpha^2)^(1/3) = {rHE:.6f}")
print(f"   and alpha/sqrt3 = {1/np.sqrt(3):.6f}   <-- SAME?  {np.isclose(rHE, 1/np.sqrt(3))}")
print("\n   (rH)^2 near it:")
for rr in [0.2,0.4,rHE,0.7,1.0,2.0]:
    print(f"     r={rr:.5f}   (rH)^2={rH2(rr):.6f}   comoving Hubble radius (rH)^-1={1/np.sqrt(rH2(rr)):.6f}")
print("   *** (rH)^2 has a MINIMUM at f'=0, so the COMOVING HUBBLE RADIUS IS MAXIMAL THERE. ***")
print("   (it diverges as r->0 through the matter term and as r->inf through the substrate term,")
print("    so the extremum between them is a minimum of (rH)^2 -- checked above, not assumed.)")
print("""
STEP 5 — AND ON THE COSMOLOGY THAT LOCUS *IS* THE SEAM.
  P7, in its own words: the E=1 rate 'passes a minimum at r=(M alpha^2)^{1/3}, the locus f'=0 --
  which ON THE NARIAI MEMBER, where the horizon cubic's double root makes f and f' vanish together,
  IS THE FRONT SEAM r = +alpha/sqrt3 ITSELF, so that there the re-expansion is slowest exactly at
  the seam.'
  Verified numerically just above: at Nariai, (M alpha^2)^{1/3} = alpha/sqrt3 to machine precision.
""")
print("*** SO THE COMOVING HUBBLE RADIUS IS MAXIMAL AT THE SEAM. ***")
print("   PHYSICS: the horizon is LARGEST at the seam, so that is where the MOST modes are inside it.")
print("   AND THAT IS P15's prop:subhorizon, derived rather than checked numerically: 'the acoustic")
print("   modes are sub-horizon at the seam' is not a numerical coincidence of z_onset ~ 6797 --")
print("   *** IT IS THE STATEMENT THAT THE SEAM SITS AT THE MAXIMUM OF THE COMOVING HORIZON, WHICH ON")
print("       THE NARIAI MEMBER IS FORCED BY f = f' = 0. ***")
print("""
STEP 6 — RADIATION MOVES THE MAXIMUM OFF THE SEAM, AND THE LIMITS FOLLOW FROM THAT.
  With the corpus's inherited datum rho_r/rho_m ~ 2 AT the seam, A = 4 M r_s, and the quartic's root
  moves out: r* = 1.5338 r_seam (gauge alpha=1, Nariai M).  So:
    * the comoving horizon is STILL RISING at the seam and turns over just OUTSIDE it;
    * *** THE SEAM IS NOT THE TURNING POINT OF THE HORIZON. IT IS JUST BEFORE IT. ***
    * and that EXPLAINS P15's prop:subhorizon rather than merely agreeing with it: the acoustic modes
      are already inside at the seam BECAUSE the seam sits on the rising part of the comoving horizon.
  A FIRST READING THAT SAID 'no mode exits and re-enters, the turning point IS the seam' WAS TOO
  STRONG AND IS WITHDRAWN -- it was the vacuum answer applied to a leg the corpus loads with radiation.

  WHAT THE LIMITS THEREFORE ARE:
    * the comoving horizon is MONOTONIC ON EACH SIDE of a single maximum at r*, which lies OUTSIDE
      the seam -- so on the whole excursion there is ONE turning point, not several;
    * a mode of comoving wavenumber k enters when (rH)^-1 = 1/k on the RISING branch and exits on the
      FALLING branch;
    * the seam sits between the two, on the rising side;
  *** SO EACH MODE'S DRIVING INTEGRAL HAS ITS LOWER LIMIT AT ITS OWN ENTRY (k-dependent, on the
      collapse side) AND RUNS THROUGH THE SEAM -- the driving does NOT terminate there. ***
  AND THAT IS THE PRECISE SENSE IN WHICH P15's 'each mode's driving is COMPLETE on the collapse side'
  needs care: complete for the modes whose entry is early enough, and the boundary between those and
  the rest is set by r*, which is a NUMBER THE CORPUS FIXES -- 1.53 r_seam at rho_r/rho_m = 2.
""")
print("="*80)

# ============================================================================================
# GATE — r2376+c54.160.  This receipt printed a PASS/FAIL boolean at STEP 4 -- "<-- SAME? True"
# from np.isclose(rHE, 1/sqrt3) -- and then only PRINTED it.  It is asserted here, together with
# pins of its own, so the file can fail.  What is being gated is C2's claim, which
# CR_cosmology.tex sec:envelope cites: the comoving Hubble radius "has a single turning point on
# the whole excursion; the SEAM sits just inside that turning point, on the rising branch".
#   ** r2501+c54.197: this comment previously quoted that sentence with "the branch point sits on
#   ** its rising branch" -- the paper's own wording at the time, and WRONG, which is why quoting a
#   ** paper verbatim inside the receipt that grounds it does not check the paper.  This file's
#   ** STEP 5-6 say SEAM sixteen times and branch point never; the loci INVERT (at the seam the
#   ** comoving horizon is near its maximum and the modes are inside; as r->0 it goes to zero and
#   ** every mode is outside), so the substitution flips prop:subhorizon's truth value.  Routed
#   ** item 21, fixed in the paper at c54.197; the quotation above is now the corrected sentence.
#   (1) the vacuum extremum of (rH)^2 sits at r = (M alpha^2)^{1/3}, and ON THE NARIAI MEMBER
#       that locus IS the front seam alpha/sqrt3 -- the printed boolean, now a gate, plus a PIN
#       of the radius itself to 0.5773503;
#   (2) the extremum is a MINIMUM of (rH)^2 (hence a MAXIMUM of the comoving horizon), checked
#       against the receipt's own tabulated neighbours rather than assumed -- and those two
#       neighbouring values are pinned to what the table prints;
#   (3) the quartic of STEP 3 and the locus f' = 0 have the SAME root -- the symbolic identity
#       the STEP-3 text asserts in prose.
# ============================================================================================
assert np.isclose(rHE, 1/np.sqrt(3)), \
    f"Nariai: (M alpha^2)^(1/3) = {rHE:.9f} is NOT the seam alpha/sqrt3 = {1/np.sqrt(3):.9f}"
assert abs(rHE - 0.5773503) < 1.0e-7, f"f'=0 locus moved: {rHE:.7f}, expected 0.5773503"
assert abs(Mv - 0.1924501) < 1.0e-7, f"Nariai mass moved: M = {Mv:.7f}, expected 0.1924501"
# (2) MINIMUM of (rH)^2 at the seam -- the sense of the turn, which STEP 4 says it checked.
assert rH2(rHE) < rH2(0.4) and rH2(rHE) < rH2(0.7), \
    "(rH)^2 is NOT minimal at f'=0 -- the comoving horizon does not peak at the seam"
assert abs(rH2(0.4) - 1.1222504) < 1.0e-6, f"(rH)^2 at r=0.4 is {rH2(0.4):.7f}, expected 1.1222504"
assert abs(rH2(0.7) - 1.0398574) < 1.0e-6, f"(rH)^2 at r=0.7 is {rH2(0.7):.7f}, expected 1.0398574"
assert abs(rH2(2.0) - 4.1924501) < 1.0e-6, f"(rH)^2 at r=2.0 is {rH2(2.0):.7f}, expected 4.1924501"
# (3) the quartic's vacuum root and the f'=0 locus are the SAME symbolic object.
_root_quartic = sp.solve(sp.Eq(q0, 0), r)
_root_fprime = sp.solve(sp.Eq(sp.diff(f, r), 0), r)
assert _root_quartic == _root_fprime, \
    f"the (rH)^2 extremum {_root_quartic} is NOT the locus f'=0 {_root_fprime}"
assert str(_root_quartic) == "[M**(1/3)*alpha**(2/3)]", \
    f"the vacuum extremum is not r = (M alpha^2)^(1/3): {_root_quartic}"
print(f"GATE C2 (r2376+c54.160): f'=0 at r = {rHE:.7f} = alpha/sqrt3, a MINIMUM of (rH)^2 "
      f"(value {rH2(rHE):.6f}) -- seam locus and turn sense both pinned.")
