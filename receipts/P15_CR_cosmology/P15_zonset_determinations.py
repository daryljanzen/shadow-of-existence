"""P15_zonset_determinations.py -- what each determination of z_onset actually returns, and which of
   them are H0-independent.  Backs the sec:tensions 'second check' paragraph.
   (1) Pinning the MEASURED acoustic angle 100theta_*=1.04109 (l_A=pi/theta_*=301.76) returns
       z_onset=6797, IDENTICALLY at H0=67.4/70.0/73.0 -- the same H0-independence that carries the
       acoustic scale out of the Hubble tension, recovered from the onset side.
   (2) The superseded form pinned the ROUNDED l_*=301, which is 0.25% off the measured angle, and
       returned ~6844 -- agreeing with the 6850 then in use ONLY because 6850 itself produces
       l_*=300.90.  A discriminator pinned to a value the quantity under test already returns could
       not have returned otherwise; the agreement was an artefact of the rounding.
   (3) The inherited datum taken ALONE (rho_r/rho_m=2 exactly at onset) fixes 1+z=2*om_m/om_r and is
       NOT H0-independent: 6840/7378/8024 at H0=67.4/70.0/73.0 (Omega_m held, omega_r fixed by T_CMB).
       It coincides with the angle-fixed value only near H0=67.4.
STATUS: OK (all three determinations computed; H0-independence of (1) exact to 5 digits)
RUN: python3 P15_zonset_determinations.py   RUNTIME: ~3s
ORIGIN: built r2376 (c54) on the conventions of storyboard_receipts/RATE_assignment_map.py."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
c=299792.458; z_rec=1089.9; a_rec=1/(1+z_rec); ombh2=0.02237; wr=4.1833e-5; Om=0.3150
MEAS_TH=1.04109                      # measured 100 theta_*
Rb=lambda a: 31500*ombh2/(2.7255/2.7)**4*a
Hstack=lambda H0:(lambda a: H0*np.sqrt(Om/a**3+(1-Om)))
rs=lambda H,zf: quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rb(a)))),1/(1+zf),a_rec,limit=300)[0]
DM=lambda H: quad(lambda a: c/(a**2*H(a)),a_rec,1.0,limit=400)[0]
th100=lambda zf,H0: 100*rs(Hstack(H0),zf)/DM(Hstack(H0))
lstar=lambda zf,H0: np.pi*DM(Hstack(H0))/rs(Hstack(H0),zf)
MEAS_L=np.pi/(MEAS_TH/100)
print("  measured 100theta_* = %.5f  ->  l_A = %.2f ; rounded l_*=301 is %.2f%% off"%(MEAS_TH,MEAS_L,100*(301/MEAS_L-1)))
z_meas=brentq(lambda z: lstar(z,67.4)-MEAS_L,4000,12000,xtol=0.5)
z_round=brentq(lambda z: lstar(z,67.4)-301.0,4000,12000,xtol=0.5)
print("  (1) pinning the MEASURED angle      -> z_onset = %.0f"%z_meas)
print("      H0-independence:  "+"  ".join("%.5f@%.1f"%(th100(z_meas,H) ,H) for H in (67.4,70.,73.)))
print("  (2) pinning the ROUNDED l_*=301     -> z_onset = %.0f   (l_* at 6850 = %.2f)"%(z_round,lstar(6850.,67.4)))
print("      => the old agreement with 6850 is the rounding, not a recovery")
print("  (3) inherited datum alone (rho_r/rho_m=2 at onset), Omega_m held:")
for h in (0.674,0.700,0.730):
    print("      H0=%.1f : z_onset = %.0f   (rho_r/rho_m at z=%.0f is %.3f)"%(
        h*100, 2*Om*h*h/wr-1, z_meas, wr*(1+z_meas)/(Om*h*h)))
ok = abs(z_meas-6797)<2 and max(abs(th100(z_meas,H)-MEAS_TH) for H in (67.4,70.,73.))<2e-5
print("\n  RESULT: %s -- (1) returns 6797 and is H0-independent; (2) is rigged by the rounding;"%("PASS" if ok else "FAIL"))
print("          (3) is H0-DEPENDENT and agrees with (1) only near H0=67.4.")

# --- ASSERTIONS r2376+c54.160 -------------------------------------------------------------
# `ok` was computed and only printed as PASS/FAIL, so a failure exited 0 all the same.  It is
# asserted here, and the rest of the paragraph P15 sec:tensions draws from this receipt is
# pinned alongside it: z_onset=6797 from the measured angle, l_A=301.76, the rounded-l_* run,
# the l_* that 6850 itself returns (300.90 -- the whole rigging argument), the H0-DEPENDENT
# inherited-datum triple 6840/7378/8024, and rho_r/rho_m=1.69 at the directly measured H0.
assert ok, "the receipt's own PASS/FAIL verdict came out FAIL"
assert abs(z_meas - 6797.0) < 1.0, f"angle-fixed z_onset = {z_meas}, paper says 6797"
assert abs(MEAS_L - 301.76) < 0.01, f"l_A = {MEAS_L}, paper says 301.76"
# H0-independence of determination (1), the point of the paragraph -- 5 digits, three rates
for _H in (67.4, 70.0, 73.0):
    assert abs(th100(z_meas, _H) - 1.04109) < 1e-5, f"100theta_* at H0={_H} is {th100(z_meas,_H)}"
# determination (2): the superseded rounded-l_* pinning, and the l_* that 6850 returns.
# NOTE r2376+c54.160: the paper's sentence reports the earlier form as having recovered 6873;
# this receipt recomputes that same pinning and returns 6844.  Pinned to what it computes.
assert abs(z_round - 6844.0) < 1.0, f"rounded-l_* z_onset = {z_round}, receipt prints 6844"
assert abs(lstar(6850., 67.4) - 300.90) < 0.02, "6850 must itself return l_*=300.90 or the rigging argument fails"
assert z_round != z_meas and abs(z_round - z_meas) > 30.0, "the two pinnings must actually differ"
# determination (3): NOT H0-independent -- the spread is the claim
_inh = [2 * Om * h * h / wr - 1 for h in (0.674, 0.700, 0.730)]
assert abs(_inh[0] - 6840.0) < 1.0 and abs(_inh[1] - 7378.0) < 1.0 and abs(_inh[2] - 8024.0) < 1.0
assert _inh[2] - _inh[0] > 1000.0, "determination (3) must be H0-DEPENDENT -- that is the whole point"
assert abs(_inh[0] - z_meas) < 50.0, "(3) coincides with (1) only near H0=67.4"
assert abs(wr * (1 + z_meas) / (Om * 0.730**2) - 1.694) < 0.002, "rho_r/rho_m at the measured H0; paper says 1.69"
print("\n[assertions r2376+c54.160] 6797 (H0-independent to 1e-5), 6844, l_*(6850)=300.90, 6840/7378/8024, 1.694: pinned.")
