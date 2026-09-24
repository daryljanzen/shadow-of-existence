#!/usr/bin/env python3
"""
RECEIPT -- P16/P15: ** WITH THE HANDOVER AT THE CROSSING THE NUCLEOSYNTHESIS WINDOW IS CROSSED
TWICE -- UP THE COLLAPSE LEG AND DOWN THE EXPANDING ONE -- AND THE SECOND PASSAGE IS NOT A
CORRECTION TO THE ABUNDANCES.  ** IT IS WHERE THEY ARE MADE. **

** ⇒ AND THAT IS A SIMPLIFICATION, NOT A COMPLICATION. **  At the branch point the temperature
diverges, so every nucleus the collapse leg built is photodissociated back to free nucleons: D's
binding is 2.22 MeV and 4He's 28.3 MeV, against a temperature with no upper bound.  ** The
expanding leg then runs ordinary BBN from free nucleons on a rate the network cannot tell from
the standard one. **  *The old account put synthesis on the collapse's cooling leg below a 1.6 eV
onset; the new one puts it exactly where standard cosmology puts it, and the collapse leg's
products cannot survive to be counted.*

Built r6760+cc66.13 (node 66, code seat), on `PO-13`, at node 66 (chat seat)'s routed question in
`FOR_CC66` (`r6772+66.8`): "the temperature of the expanding leg at the handover on the adjudicated
configuration, and whether the window is crossed on that leg, on the collapse leg, or on both."

===================================================================================================
** THE DISTINCTION THE QUESTION TURNS ON, AND IT IS EASY TO MISS **
===================================================================================================

`ACOUSTIC_two_arm.py`'s `ZSTART` is a ** NUMERICAL ** start -- the depth at which the perturbation
answer has converged -- and is not the physical locus.  ** The physical locus is the branch point,
where a -> 0 and the temperature has no bound. **  So:

  * the question "what temperature is the handover at" has ** two answers **, and only one of them
    is about the construction;
  * and the answer about the construction is ** unbounded **, which is what makes the dissociation
    argument work at all.

  PART 1  ** THE WINDOW IN REDSHIFT, ** from the network's own T9 range.
  PART 2  ** WHERE `ZSTART` SITS IN IT, ** including the whole convergence scan.
  PART 3  ** WHICH LEG CROSSES IT. **
  PART 4  ** WHAT THE SECOND PASSAGE DOES: the dissociation thresholds. **
  PART 5  ** AND THE RATE THROUGH THE WINDOW, MEASURED RATHER THAN ASSERTED. **

** COMPUTES: T_0 = 2.7255 K; the network's own T9_start = 9.0 and T9_end = 0.08 read off
   `bbn_network.run`'s signature rather than typed; the adjudicated configuration H0 = 68.60,
   Om = 0.2973, wr = 4.15e-5; binding energies B(D) = 2.224573 MeV and B(4He) = 28.295673 MeV
   (AME2020).  *** Nothing here is fitted and no spectrum is read. *** **

rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~10 s)
"""
import inspect
import os
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'p16_bbn'))
import bbn_network as BBN                                                  # noqa: E402

T0_K = 2.7255
K_PER_MEV = 1.0 / 8.617333262e-11        # 1 MeV in kelvin
B_D, B_HE4 = 2.224573, 28.295673         # MeV, AME2020
H0, OM = 68.60, 0.2973
WR = 4.15e-5
C_KM = 299792.458
MPC_KM = 3.0856775814913673e19           # km in a Mpc


def z_of_T9(T9):
    return T9 * 1.0e9 / T0_K - 1.0


def T9_of_z(z):
    return (1.0 + z) * T0_K / 1.0e9


print("=" * 100)
print("  PART 1 -- ** THE WINDOW IN REDSHIFT **")
print("=" * 100)
sig = inspect.signature(BBN.run)
T9_HI = float(sig.parameters['T9_start'].default)
T9_LO = float(sig.parameters['T9_end'].default)
print(f"  read off `bbn_network.run`'s signature:  T9_start = {T9_HI}, T9_end = {T9_LO}")
print(f"  ⇒ the window is  z = {z_of_T9(T9_LO):.3e}  to  {z_of_T9(T9_HI):.3e}"
      f"   (T = {T9_LO * 1e9 / K_PER_MEV * 1e3:.1f} keV to {T9_HI * 1e9 / K_PER_MEV:.3f} MeV)")
if not (1e7 < z_of_T9(T9_LO) < 1e8 and 1e9 < z_of_T9(T9_HI) < 1e10):
    fail.append("the window's redshift bounds are not where T(z) = T_0 (1+z) puts them")

print()
print("=" * 100)
print("  PART 2 -- ** WHERE `ZSTART` SITS IN IT **")
print("=" * 100)
print(f"  {'ZSTART':>12} {'T9 there':>10} {'T':>12} {'vs the window':>28}")
for z in (3.0e6, 3.0e7, 3.0e8, 6.16e4):
    t9 = T9_of_z(z)
    where = ('BELOW it (cooler than T9_end)' if t9 < T9_LO else
             'ABOVE it (hotter than T9_start)' if t9 > T9_HI else 'INSIDE it')
    lab = f"{z:.3g}" + (" (the pin)" if z < 1e5 else "")
    print(f"  {lab:>12} {t9:>10.4f} {t9 * 1e9 / K_PER_MEV * 1e3:>9.2f} keV {where:>28}")
t9_default = T9_of_z(3.0e7)
print(f"""
  ** THE INSTRUMENT'S DEFAULT CROSSING START, ZSTART = 3e7, IS AT T9 = {t9_default:.4f} -- just
  INSIDE the window's cool edge, {(3.0e7 / z_of_T9(T9_LO) - 1) * 100:.0f}% above it. **  And the convergence scan
  r6760+cc66.1 ran, 3e6 to 3e8, spans from BELOW the window to well INSIDE it -- *and the peaks
  were identical across it.*  ⇒ ** So the spectrum is already known not to care where in this
  window the numerical start is put, which is worth saying before anything else: the question
  below is about the ABUNDANCES, not about the comb. **""")
if not (T9_LO < t9_default < T9_HI):
    fail.append(f"ZSTART = 3e7 gives T9 = {t9_default:.4f}, which is not inside the window")

print()
print("=" * 100)
print("  PART 3 -- ** WHICH LEG CROSSES IT **")
print("=" * 100)
print(f"""
  ** THE COLLAPSE LEG: YES. **  It runs from low temperature UP to the branch point, so it passes
  through [{T9_LO}, {T9_HI}] in the direction of increasing T.

  ** THE EXPANDING LEG: YES, AND NECESSARILY. **  It begins AT the branch point, where a -> 0 and
  T -> infinity without bound, and ends at the present.  *A continuous temperature history from
  unbounded to 2.7 K crosses every finite interval exactly once* -- so it crosses this one, and no
  choice of `ZSTART` can change that, `ZSTART` being a numerical convenience and not the locus.

  ⇒ *** BOTH.  THE WINDOW IS CROSSED TWICE. ***  That is the answer to the routed question, and it
  is forced by the handover's own definition rather than by any number computed here.""")

print()
print("=" * 100)
print("  PART 4 -- ** WHAT THE SECOND PASSAGE DOES **")
print("=" * 100)
# ** The dissociation temperature is NOT B/k -- the photon-to-baryon ratio is ~1e9, so the tail of
# the Planck distribution destroys a nucleus long before the mean photon energy reaches B.  The
# standard estimate is B/k divided by ln(1/eta) ~ 21, and the deuterium bottleneck is the textbook
# case: T_diss(D) ~ 0.07 MeV, not 2.2 MeV. **
ETA = 6.14e-10
LN = np.log(1.0 / ETA)
print(f"  {'nucleus':>10} {'B (MeV)':>9} {'B/k (T9)':>10} {'with the eta tail (T9)':>23}")
for nm, B in (('D', B_D), ('4He', B_HE4)):
    t9_naive = B * K_PER_MEV / 1.0e9
    t9_real = t9_naive / LN
    print(f"  {nm:>10} {B:>9.3f} {t9_naive:>10.1f} {t9_real:>22.2f}")
print(f"""
  *The dissociation temperature is NOT B/k: with eta = {ETA:.2e} there are ~10^9 photons per baryon,
  so the Planck tail destroys a nucleus well below that -- the standard estimate divides by
  ln(1/eta) = {LN:.1f}, and for D it gives the textbook deuterium bottleneck.*

  ** AND THE BRANCH POINT HAS NO UPPER BOUND ON T, so it exceeds BOTH thresholds by any margin
  asked for. **  ⇒ *** Every nucleus the collapse leg built is photodissociated back to free
  nucleons before the expanding leg begins.  The collapse leg's products cannot survive to be
  counted. ***

  ⇒ ** SO THE SECOND PASSAGE IS NOT A CORRECTION TO THE ABUNDANCES.  IT IS WHERE THEY ARE MADE. **
  *The expanding leg runs ordinary BBN from free nucleons, which is exactly what
  `bbn_network.py` integrates and exactly what standard cosmology does.*  ⌗ **That makes the new
  account SIMPLER than the old one**: `P15` and `P16` placed the synthesis on the collapse's
  cooling leg below a 1.6 eV onset, which required the leg to both build and preserve the nuclei;
  the crossing handover removes that requirement instead of adding one.""")
if B_D * K_PER_MEV / 1.0e9 / LN > T9_HI:
    fail.append("D's dissociation threshold is above the window -- the argument does not close")

print()
print("=" * 100)
print("  PART 5 -- ** THE RATE THROUGH THE WINDOW, MEASURED **")
print("=" * 100)
print("  The network integrates on H = sqrt(8 pi G rho_rad(T)/3) with its own g_*(T).  The leaf")
print("  rate is H0 sqrt(Om/a^3 + OL + Or/a^4).  ** If these disagree through the window, the")
print("  abundances are NOT the standard ones and the whole argument above is void. **")
Or = WR / (H0 / 100) ** 2
Ol = 1.0 - OM


def H_leaf_per_s(T9):
    a = T0_K / (T9 * 1.0e9)
    H_kms_mpc = H0 * np.sqrt(OM / a ** 3 + Ol + Or / a ** 4)
    return H_kms_mpc / MPC_KM


print(f"\n  {'T9':>8} {'H, network (1/s)':>18} {'H, leaf Omega_r (1/s)':>22} {'leaf/network':>13}")
hot, cold = [], []
for T9 in (9.0, 5.0, 3.0, 1.0, 0.3, 0.08):
    T_MeV = T9 / BBN.T9_per_MeV
    hn = BBN.Hubble(T_MeV)
    hl = H_leaf_per_s(T9)
    (hot if T9 > 1.5 else cold).append(abs(hl / hn - 1))
    print(f"  {T9:>8.2f} {hn:>18.4e} {hl:>22.4e} {hl / hn:>13.4f}")
print(f"""
  ⛔ ** THEY DO NOT AGREE ABOVE T9 ~ 1.5, AND THE DISAGREEMENT IS {max(hot) * 100:.0f}% -- WHICH IS NOT
  A ROUNDING. **  *A rate {max(hot) * 100:.0f}% slow through weak freeze-out would move Y_p, so this has to be
  said precisely rather than waved past.*  ⇒ ** The cause is the e+e- pairs. **  The network carries
  them in g_*(T); Omega_r = {WR}/h^2 is the POST-annihilation radiation density extrapolated back as
  a^-4, so it MISSES them, and they are the whole of the gap: it opens at T9 ~ 5 where the pairs
  annihilate and is closed to {max(cold) * 100:.1f}% below T9 = 1.5, where they are gone.

  ⇒ *** SO THE SENTENCE "a rate the network cannot tell from the standard one" IS TRUE OF THE
  PHYSICAL RATE AND FALSE OF `Omega_r/a^4` AS THIS INSTRUMENT PARAMETERISES IT. ***  The network does
  NOT run on the leaf parameterisation -- it builds rho_rad from g_*(T) -- so the abundances are
  computed on the right rate and nothing above is disturbed.  ** But nobody may compute BBN on the
  instrument's Omega_r and expect the table: it is a late-time parameterisation and the hot half of
  this window is before the epoch it is valid on. **
  ⌗ *That is a caveat about the INSTRUMENT'S background, not about the construction, and it is
  identical on the control -- flat LambdaCDM's Omega_r misses e+e- in exactly the same way.*""")
if max(cold) > 0.02:
    fail.append(f"the two rates differ by {max(cold) * 100:.1f}% BELOW T9 = 1.5, where the e+e- "
                "explanation does not apply -- the gap is not the pairs")
if max(hot) < 0.10:
    fail.append("the rates do not diverge above T9 = 1.5 -- PART 5's e+e- account has nothing "
                "to explain and its warning is unfounded")

print(f"""
=================================================================================================
  ** THE ANSWER TO THE ROUTED QUESTION, IN THREE LINES **
=================================================================================================

  1. ** The temperature of the expanding leg at the handover is UNBOUNDED ** -- the handover is the
     branch point, a -> 0.  `ZSTART = 3e7` is a numerical start at T9 = {t9_default:.4f} and is not
     the locus; the convergence scan already spans from below the window to inside it with no
     change in the spectrum.
  2. ** The window is crossed TWICE **, up the collapse leg and down the expanding one.
  3. ** The second passage is where the abundances are made. **  The branch point dissociates
     everything the first passage built, so the expanding leg runs ordinary BBN from free nucleons
     on the ordinary radiation-dominated Friedmann rate, which is what the network integrates.
     ⚠ *Said precisely, per PART 5: true of the PHYSICAL rate, and NOT of the instrument's
     `Omega_r/a^4`, which misses e+e- and is 44% slow above T9 ~ 1.5.*

  ⇒ ** So both papers can say it in the new terms and neither needs a correction to a number: the
  1.6 eV onset goes, the synthesis moves to the expanding leg, and the table stands. **
  ⚠ *What this does NOT say: that the collapse leg is unobservable, or that nothing else about it
  changes.  It says the ABUNDANCES do not, and only because the branch point erases the first
  passage.*
""")

print("=" * 100)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print("=" * 100)
