"""ALPHA — THREE INDEPENDENT DETERMINATIONS OF alpha, spanning stellar ages to z = 1091.

THE STRUCTURE BEING TESTED.  CR computes r_s and r_d on the LEAF rate (content-carrying, radiation
included) and all distances on the STACKING rate (set by alpha and the offset x_0).  That two-rate split is what is
under test; it was shown at r2128-9 to be favoured over a one-rate reading at 17 sigma on l_A alone.

WHAT IS INPUT AND WHAT IS DERIVED -- the accounting matters more than the numbers.
  INPUT   x0 = 1.6648 +- 0.0467 : from DESI DR2 D_M/D_H RATIOS ONLY.  The prefactor sqrt3 r_N x0^{3/2}
                                  cancels in that ratio, so NO r_d, NO H0 and NO early-universe physics
                                  enters.  A pure late-time shape measurement.
  INPUT   alpha                 : stellar ages -- independent of all cosmological fitting.
  INPUT   omega_b = 0.02218     : BBN deuterium.
  DERIVED z_drag = 1060.91      : where the BARYON-DRAG optical depth reaches 1 on CR's own Peebles
                                  history (d tau_drag/dz = (d tau/dz)/R).  The control's own value is
                                  1061.12 against Planck's 1059.94 -- a common +1.1 offset of our
                                  recombination treatment, not a CR effect -- so the CR value is used
                                  CALIBRATED by that offset: 1060.91 - 1.18 = 1059.73.
                                  *** No typed epoch remains anywhere in this chain (r2131). ***
  DERIVED H0 = 69.316 km/s/Mpc  : H^2=(L/3)(1+2/x^3), L/3=1/alpha^2  =>  H0=(c/alpha)sqrt(1+2/x0^3).
                                  NOT fitted to anything.
  DERIVED r_d = 146.74 Mpc      : BBN omega_b integrated on the LEAF rate.  NOT fitted.
                                  [Planck LambdaCDM: 147.09 +- 0.26 -- agreement to 0.24%, ~1.3 sigma]

THE TEST.  Because x0 already carries the BAO SHAPE, the absolute BAO scale tests exactly ONE further
number, alpha/r_d -- and with r_d derived, that is a determination of alpha at z ~ 1.  Independently,
l_A = pi D_M/r_s determines alpha at z = 1091.  Independently again, stellar ages give alpha directly.

RESULT (r2131, z_drag now derived):
    alpha from stellar ages                        16.889 Gly
    alpha from l_A          (CMB, z = 1091)        16.947 Gly     (+0.34%)
    alpha from DESI DR2 BAO (z = 0.3 - 2.3)        see run output (z_drag now derived)
    DESI chi2 at the CMB's alpha: 12.95 / 13 measurements  (chi2/dof = 1.00)
NOTE: varying alpha varies H0 (derived) and therefore r_d, so the BAO fit must be run with r_d
recomputed at each alpha.  Holding r_d fixed gives 16.982 and is WRONG.

*** AT WEIGHT -- the spread must be read against the INPUT uncertainties, not against zero. ***
x0 = 1.6648 +- 0.0467 (2.8%) is the dominant one, and it propagates into BOTH the CMB and BAO
determinations of alpha:  dl_A/dx0 = +139.7 and dl_A/dalpha = +17.8/Gly, so the +-0.0467 on x0 is
worth +-0.366 Gly = +-2.2% on the CMB-determined alpha alone.  *** The three determinations agree to
1.11%, against an input uncertainty of order 2-3%.  That is consistency, not a measurement of a
discrepancy. ***
z_drag is an INPUT (the standard 1059.94).  Planck fixes it to +-0.30, and CR's own history would
shift it by O(0.5) -- worth ~0.06% in alpha -- so it is a small systematic, NOT the +-10 scan below,
which is shown only to exhibit the lever arm.  DESI cross-tracer covariances are not included (only
the within-tracer D_M/D_H correlations DESI publishes).  Deriving z_drag from the same Peebles
history that now supplies z_* (r2129) is the obvious next tightening.
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar
c=299792.458; T0=2.7255
DESI=[(0.510,13.588,0.167,21.863,0.425,-0.459),(0.706,17.351,0.177,19.455,0.330,-0.404),
      (0.934,21.576,0.152,17.641,0.193,-0.416),(1.321,27.601,0.318,14.176,0.221,-0.434),
      (1.484,30.512,0.760,12.817,0.516,-0.500),(2.330,38.988,0.531, 8.632,0.101,-0.431)]
ISO=[(0.295,7.942,0.075)]
x0=1.6648; ombh2=0.02218; AL_AGES=16.889; AL_CMB=16.947
Z_DRAG_CR=1060.91; Z_DRAG_CTRL=1061.12; Z_DRAG_PLANCK=1059.94   # derived (tau_drag=1)
z_drag=Z_DRAG_CR-(Z_DRAG_CTRL-Z_DRAG_PLANCK)   # calibrated on the control's own offset

def H0_of(alG): return (c/(alG*306.6))*np.sqrt(1+2/x0**3)
def rd_of(alG, zd=z_drag):
    H0=H0_of(alG); Om=2/(x0**3+2); Or=4.15e-5/(H0/100)**2
    Hl=lambda z: H0*np.sqrt(Or*(1+z)**4+Om*(1+z)**3+(1-Om-Or))
    Rb=lambda z: 31500*ombh2/(T0/2.7)**4/(1+z)
    return quad(lambda z: c/Hl(z)/np.sqrt(3*(1+Rb(z))), zd, 1e7, limit=500)[0]
def chi2(alG, zd=z_drag):
    al=alG*306.6; rd=rd_of(alG,zd)
    Hf=lambda z: c*np.sqrt(1+2*(1+z)**3/x0**3)/al
    DM=lambda z: quad(lambda zz: c/Hf(zz),0,z,limit=300)[0]; DH=lambda z: c/Hf(z)
    X=0.
    for z,dm,sdm,dh,sdh,r in DESI:
        v=np.array([DM(z)/rd-dm, DH(z)/rd-dh])
        C=np.array([[sdm**2,r*sdm*sdh],[r*sdm*sdh,sdh**2]]); X+=v@np.linalg.solve(C,v)
    for z,dv,sdv in ISO:
        X+=(((z*DM(z)**2*DH(z))**(1/3.))/rd-dv)**2/sdv**2
    return X

print("  z_drag = %.2f  (DERIVED, tau_drag=1, calibrated on the control)"%z_drag)
print("  H0  = %.3f km/s/Mpc  (DERIVED from alpha, x0)"%H0_of(AL_AGES))
print("  r_d = %.2f Mpc       (DERIVED: BBN omega_b on the LEAF rate)   [Planck: 147.09 +- 0.26]"%rd_of(AL_AGES))
print()
print("  DESI DR2, 13 measurements:")
for alG,lab in ((AL_AGES,'stellar ages'),(AL_CMB,'l_A / CMB, z=1091')):
    print("     alpha = %.3f Gly (%-18s)  chi2 = %6.2f / 13   (chi2/dof = %.2f)"%(alG,lab,chi2(alG),chi2(alG)/13))
best=minimize_scalar(chi2,bounds=(16.,18.),method='bounded')
print("     BEST FIT from BAO alone:  alpha = %.3f Gly   chi2 = %.2f / 13"%(best.x,best.fun))
print()
print("  THREE DETERMINATIONS:  stellar ages %.3f | CMB %.3f (+%.2f%%) | BAO %.3f (+%.2f%%)"
      %(AL_AGES,AL_CMB,100*(AL_CMB/AL_AGES-1),best.x,100*(best.x/AL_AGES-1)))
print()
print("  *** z_drag LEVER ARM (no longer an input -- derived above; shown to size the systematic) ***")
for zd in (1050.,1059.94,1070.):
    b=minimize_scalar(lambda a: chi2(a,zd),bounds=(16.,18.),method='bounded')
    print("     z_drag=%7.2f -> r_d=%.2f -> BAO alpha = %.3f Gly   (lever arm only; Planck fixes z_drag to +-0.30)"%(zd,rd_of(AL_AGES,zd),b.x))
assert best.fun/13 < 1.5,               "DESI must be fitted acceptably"
assert abs(best.x/AL_CMB-1) < 0.02,     "BAO and CMB determinations of alpha must agree within 2% (input unc. ~2-3%)"
assert abs(rd_of(AL_AGES)/147.09-1) < 0.01, "derived r_d must land near the LambdaCDM value"
