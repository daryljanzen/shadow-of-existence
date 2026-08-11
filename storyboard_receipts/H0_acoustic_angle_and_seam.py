"""H0 — THE ACOUSTIC SCALE AT THE DIRECTLY MEASURED H0.  The calculation I have been running backwards.
CORPUS CLAIM (P7, P15): 'There is no second Hubble rate to reconcile: THE DIRECTLY MEASURED H0 IS THE
GEOMETRY READ AT THE PRESENT EPOCH, while the lower value inferred from the microwave background rests
on a radiation-governed sound horizon the construction does not share... The acoustic scale is then met
at the directly measured rate by a single inherited datum, rho_r/rho_m ~ 2.'
SO: run at H0 = 73, and ASK WHAT SEAM REDSHIFT THE MEASURED ACOUSTIC ANGLE DEMANDS."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
c=299792.458
z_rec=1089.9; a_rec=1/(1+z_rec)
Om=0.31                       # the corpus's CMB-calibrated value, quoted in P15
print("="*80); print("H0 — THE ACOUSTIC SCALE, RUN AT THE MEASURED H0"); print("="*80)
def machinery(H0, z_onset, Om=Om, ombh2=0.0224):
    OL=1-Om
    a_s=1/(1+z_onset)
    Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
    Rbf=lambda a: Rb_rec*(a/a_rec)
    H=lambda a: H0*np.sqrt(Om/a**3+OL)                 # CR: matter + Lambda, no radiation term
    rs,_=quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rbf(a)))), a_s, a_rec, limit=300)
    DM,_=quad(lambda a: c/(a**2*H(a)), a_rec, 1.0, limit=300)
    return rs, DM, np.pi*DM/rs
# LambdaCDM reference at the CMB-inferred H0
def lcdm(H0=67.4, Om=0.307, ombh2=0.0224):
    OL=1-Om; z_eq=3403.6; Or=Om/(1+z_eq)
    Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
    Rbf=lambda a: Rb_rec*(a/a_rec)
    H=lambda a: H0*np.sqrt(Or/a**4+Om/a**3+OL)
    rs,_=quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rbf(a)))), 1e-9, a_rec, limit=300)
    DM,_=quad(lambda a: c/(a**2*H(a)), a_rec, 1.0, limit=300)
    return rs, DM, np.pi*DM/rs
rsL,DML,lL = lcdm()
print(f"\n  LambdaCDM at the CMB-inferred H0=67.4:  r_s={rsL:.2f}  D_M={DML:.0f}  l_*={lL:.1f}")
print(f"  *** the measured acoustic angle: l_* = {lL:.1f} (this is the FACT both must reproduce) ***")
# r2376+c54.160: the LambdaCDM anchor everything below is solved against.  The paper quotes the
# measured acoustic scale as l_A = pi/theta_* = 301.76; this receipt's reference reproduces it.
assert abs(lL - 301.6) < 0.3, f"LCDM l_* = {lL}"
assert abs(rsL - 145.93) < 0.05, f"LCDM r_s = {rsL}"
print(f"\n  Now CR at the DIRECTLY MEASURED H0, solving for the seam redshift l_* demands:\n")
print(f"  {'H0':>6s} {'z_onset needed':>14s} {'r_s (Mpc)':>11s} {'D_M (Mpc)':>11s} {'r_s vs LCDM':>13s}")
_c54160_seams = []   # r2376+c54.160: seam redshifts, one per H0, for the H0-independence assertion
for H0 in [67.4, 70.0, 73.0, 73.2, 74.0]:
    try:
        zs=brentq(lambda z: machinery(H0,z)[2]-lL, 1500., 60000.)
        rs,DM,l = machinery(H0,zs)
        print(f"  {H0:>6.1f} {zs:>14.0f} {rs:>11.2f} {DM:>11.0f} {100*(rs/rsL-1):>12.2f}%")
        _c54160_seams.append(zs)   # r2376+c54.160: collected for the assertion below (the assert
                                   # itself may not live inside this try, which swallows Exception)
    except Exception as e:
        print(f"  {H0:>6.1f}  no solution: {e}")
# r2376+c54.160: THE H0-INDEPENDENCE, ASSERTED.  STEP 2's claim -- and the paper's, in
# sec:refit-bound -- is that the acoustic angle fixes z_onset and NOT H0, so the SAME seam redshift
# must come back at every H0 in this table.  Pinned to the value it returns (6783), which is the
# paper's "the seam falls at z ~ 6.8e3".
assert len(_c54160_seams) == 5, f"the table lost a row: {_c54160_seams}"
assert max(_c54160_seams) - min(_c54160_seams) < 1.0, f"z_onset moved with H0: {_c54160_seams}"
assert abs(_c54160_seams[0] - 6783.0) < 3.0, f"seam redshift demanded = {_c54160_seams[0]}"
print("""
  *** READ IT.  AT THE DIRECTLY MEASURED H0 THE SOUND HORIZON MUST BE SMALLER, AND THE SEAM MUST BE
      LATER.  That is the corpus's claim made quantitative: the acoustic angle is met at the measured
      rate by ONE inherited datum, and the datum is the seam's radiation amplitude. ***
""")

print("="*80); print("THE MECHANISM, AND THEN THE CRUX"); print("="*80)
print("""
STEP 2 — WHY z_onset CAME OUT THE SAME FOR EVERY H0.  Because BOTH r_s and D_M scale as 1/H0 in a
  matter+Lambda cosmology, so l_* = pi D_M/r_s IS H0-INDEPENDENT.
  *** SO THE ACOUSTIC ANGLE DOES NOT DETERMINE H0 HERE.  IT DETERMINES z_onset. ***
  In LambdaCDM, r_s is fixed by omega_m and omega_b -- there is no free early datum -- so theta_*
  DOES determine H0, and that is where 67.4 comes from.  In CR the seam's radiation amplitude is one
  more inherited number, and it takes the constraint instead, leaving H0 free to be the directly
  measured value.
  *** THAT IS 'THERE IS NO SECOND H0 TO RECONCILE', DERIVED RATHER THAN ASSERTED -- and it is also
      exactly what 'a ONE-PARAMETER ACCOMMODATION' means.  The corpus's own scoping is correct. ***
""")
zs=brentq(lambda z: machinery(73.0,z)[2]-lL, 1500., 60000.)
print(f"   and the seam redshift the angle demands: {zs:.0f}  against the corpus's 6797 ({100*abs(zs-6797)/6797:.1f}% apart)")
# r2376+c54.160: the receipt's headline agreement -- the angle-demanded seam against the corpus's
# 6797 -- pinned as a number rather than left in a sentence.
assert abs(zs - 6783.0) < 3.0, f"seam demanded at H0=73: {zs}"
assert 100*abs(zs - 6797)/6797 < 0.4, f"seam vs corpus 6797: {100*abs(zs-6797)/6797}% apart"
print("""
STEP 3 — THE CRUX.  If z_onset absorbs the acoustic angle, DOES IT ALSO ABSORB THE DAMPING?
  If theta_D/theta_* is z_onset-independent the damping is a clean prediction; if it moves with
  z_onset, it is absorbable and there is no discriminator here at all.  COMPUTE IT.
""")
def damping(H0, z_onset, Om=Om, ombh2=0.0224):
    OL=1-Om; a_s=1/(1+z_onset)
    Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
    Rbf=lambda a: Rb_rec*(a/a_rec)
    g=lambda a: (Rbf(a)**2/(1+Rbf(a))+8/9)/(6*(1+Rbf(a)))
    H=lambda a: H0*np.sqrt(Om/a**3+OL)
    I,_=quad(lambda a: g(a)/H(a), a_s, a_rec, limit=300)
    rs,_=quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rbf(a)))), a_s, a_rec, limit=300)
    return np.sqrt(I), rs
# LCDM reference ratio
def damping_L(H0=67.4, Om=0.307, ombh2=0.0224):
    OL=1-Om; z_eq=3403.6; Or=Om/(1+z_eq)
    Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
    Rbf=lambda a: Rb_rec*(a/a_rec)
    g=lambda a: (Rbf(a)**2/(1+Rbf(a))+8/9)/(6*(1+Rbf(a)))
    H=lambda a: H0*np.sqrt(Or/a**4+Om/a**3+OL)
    I,_=quad(lambda a: g(a)/H(a), 1e-9, a_rec, limit=300)
    rs,_=quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rbf(a)))), 1e-9, a_rec, limit=300)
    return np.sqrt(I), rs
DL,rL = damping_L()
print(f"   {'z_onset':>8s} {'l_* (must be 301.6)':>20s} {'theta_D/theta_* vs LCDM':>26s}")
for zsv in [4000.,5500.,6783.,8000.,12000.]:
    D,rs = damping(73.0, zsv)
    _,_,l = machinery(73.0, zsv)
    ratio=(D/rs)/(DL/rL)
    print(f"   {zsv:>8.0f} {l:>20.1f} {100*(ratio-1):>25.2f}%")
    # r2376+c54.160: THE CRUX, PINNED AT ITS TWO ENDS.  STEP 3's claim -- and the paper's, in
    # sec:refit-bound -- is that theta_D/theta_* "varies from +43% to -3% across the onset
    # redshifts one might consider", so one datum cannot absorb both observables.  If the swing
    # ever collapsed, the damping would be absorbable and the discriminator would be gone.
    if zsv == 4000.:
        assert abs(100*(ratio-1) - 43.54) < 0.3, f"low-z_onset end = {100*(ratio-1)}%"
    if zsv == 12000.:
        assert abs(100*(ratio-1) + 3.09) < 0.3, f"high-z_onset end = {100*(ratio-1)}%"
    if zsv == 6783.:
        # at the seam the angle demands, l_* comes back to the measured value and the damping
        # residual is the +14% the error budget quotes.
        assert abs(l - 301.6) < 0.3, f"l_* at the demanded seam = {l}"
        assert abs(100*(ratio-1) - 14.15) < 0.3, f"damping residual at the seam = {100*(ratio-1)}%"
print("""
  *** AND THERE IT IS.  theta_D/theta_* MOVES STRONGLY WITH z_onset -- so the seam datum does NOT
      independently absorb both.  Fixing l_* to the sky FIXES z_onset, and the damping ratio is then
      DETERMINED. ***
  That is why the damping is the discriminator and the acoustic angle is not: one datum, two
  observables, and the first is spent.
""")
