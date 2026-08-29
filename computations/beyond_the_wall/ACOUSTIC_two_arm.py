#!/usr/bin/env python3
"""ACOUSTIC_two_arm.py -- ** ONE MACHINERY, TWO ARMS, AND A GUARD THAT CAN FAIL. **

Built r2376+c54.168, front #5 / front #18.

** WHY IT EXISTS. **  This fork has never had a LIVE control.  `ROBUST_p1p2_scan` quotes one from
r1975 in a comment and runs none, so every absolute ell_1 it has ever produced was unreadable --
c54.164 showed its figures move over ell_1 in {150,165,315} under four readings of its own stated
initial condition, and there was nothing to measure that against.  ** Without a control an absolute
peak position is not a number, and without an undriven guard a comb deficit is not a finding. **

THREE THINGS ON ONE SET OF EQUATIONS, so that nothing is a difference of machinery:

  ARM=lcdm   the radiation-included rate with adiabatic super-horizon initial data, started deep in
             radiation domination.  ** This must land near the sky's 220.6 or the instrument is not
             an arbiter of anything, and that is the first thing the receipt asserts. **
  ARM=cr     the L1 rate -- radiation is CONTENT, not a source -- started at the onset.  The density
             fractions are normalised to the STACK while the rate is radiation-free: both at once,
             which is the assignment the corpus's own decision rule forces.
  NODRIVE=1  ** every coupling to the potential removed, at every site: the 4 Phi' in the photon,
             neutrino and CDM continuity equations AND the k^2 Psi in the photon/baryon and neutrino
             Euler equations, in BOTH the tight-coupled and post-switch branches. **  Undriven, the
             source comb must land on the integers n pi/r_s.  A switch that removes a coupling must
             remove ALL of it -- a half-applied NODRIVE is a documented way to report a false null.

** THE COMB IS MEASURED ON SOURCE EXTREMA IN k, NEVER IN ell. **  In ell-space the projection kernel
and the visibility width distort spacing independently, so a comb measured there cannot distinguish
"the oscillator is not free" from "the projection is not uniform".

Usage:
    ARM=lcdm python3 ACOUSTIC_two_arm.py            # the control
    ARM=cr   python3 ACOUSTIC_two_arm.py            # the CR arm
    ARM=lcdm NODRIVE=1 python3 ACOUSTIC_two_arm.py  # the guard on the control
    ARM=cr   NODRIVE=1 python3 ACOUSTIC_two_arm.py  # the guard on the CR arm
Env: NK (modes, default 260), LMAXL (default 1300), RTOL, NOPROJ=1 (comb only, no projection).
"""
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
from scipy.signal import argrelextrema
from scipy.special import spherical_jn

C = 299792.458
ARM = os.environ.get('ARM', 'lcdm')
NODRIVE = os.environ.get('NODRIVE', '0') == '1'
DR = 0.0 if NODRIVE else 1.0                  # the driving switch, multiplying EVERY coupling
# ** THE DRIVING SPLIT INTO ITS TWO TERMS (r2376+c54.170), so the k-dependence can be attributed. **
#   DRC  the 4 Phi' in the photon, neutrino and CDM CONTINUITY equations -- the potential's RATE OF
#        CHANGE feeding the density, which is what "the potential decays" means dynamically.
#   DRE  the k^2 Psi in the photon/baryon and neutrino EULER equations -- the potential's GRADIENT
#        driving the velocity, which is the restoring force the oscillator swings against.
# Phi's OWN evolution is never switched: it is the potential's dynamics, not a coupling into the
# fluid, and removing it would change the background rather than the driving.
DRC = float(os.environ.get('DRC', DR))
DRE = float(os.environ.get('DRE', DR))
NK = int(os.environ.get('NK', '260'))
LMAXL = float(os.environ.get('LMAXL', '1300'))
RTOL = float(os.environ.get('RTOL', '1e-7'))
LN = 12                                        # neutrino hierarchy depth
BSPLIT = os.environ.get('BSPLIT', '1') != '0'  # baryons at their OWN contrast (c54.178)

# ---- the two backgrounds -----------------------------------------------------------------------
if ARM == 'lcdm':
    H0, OM, OMBH2 = 67.40, 0.3150, 0.0224
    FNU, Z_REC = 0.4052, 1089.9
    OR = 4.15e-5 / (H0 / 100) ** 2
    RAD_IN_RATE = True
    Z_START = None                             # set below, deep in radiation domination
else:
    H0, OM, OMBH2 = 73.00, 0.3066, 0.0224
    FNU, Z_REC = 0.4052, 1089.9
    OR = 4.15e-5 / (H0 / 100) ** 2
    RAD_IN_RATE = False                        # ** radiation is content, not a source **
    Z_START = None                             # the onset, solved for the pinned acoustic scale

OL = 1.0 - OM
A_REC = 1.0 / (1.0 + Z_REC)
RB_REC = 31500 * OMBH2 / (2.7255 / 2.7) ** 4 / (1 + Z_REC)
# ** RBFAC scales the baryon loading R consistently (sound speed AND baryon Euler inertia, via
# Rb_of and rs_from).  Default 1.0 = byte-identical.  RBFAC=0 removes loading (c_s=1/sqrt3, no
# compression/rarefaction asymmetry) -- the diagnostic for whether the second-gap contraction
# (the odd-even alternation) is loading-driven.  A diagnostic lever, not a physics change. **
RB_REC = float(os.environ.get('RBFAC', '1.0')) * RB_REC


def Hphys(a):
    """H(a) in km/s/Mpc -- the ONLY place the two arms' rates differ"""
    t = OM / a ** 3 + OL
    if RAD_IN_RATE:
        t = t + OR / a ** 4
    return H0 * np.sqrt(t)


ag = np.logspace(-9, 0, 40000)
_seed = float(quad(lambda a: C / (a ** 2 * Hphys(a)), 1e-16, ag[0], limit=200)[0])
eg = np.concatenate([[_seed], _seed + cumulative_trapezoid(C / (ag ** 2 * Hphys(ag)), ag)])
Hc_of = CubicSpline(eg, ag * Hphys(ag) / C)                       # comoving Hubble, 1/Mpc
# ** LEAFPERT=1: THE PERTURBATION SECTOR ON THE LEAF'S RATE (option (b)).  P15 sec:properframe and
# P7's rate-rule remark both assign THE PERTURBATIONS to the leaf: "a process running in the content
# -- rs, r_D, recombination, the perturbations -- takes the leaf's".  The file carries ONE rate, and
# in the CR arm it is the stacking rate, so the perturbations run on L1 where the framework says L2.
# The fix is not a rescaled source but the leaf's own rate in the perturbation equations.  Since both
# conformal times are monotone in a, the change is an exact chain rule:
#     dY/deta_stack = (H_stack/H_leaf) * F(Y, Hcal_leaf)
# so every spline and grid is untouched, rs, D_M and the projection keep the stacking rate (L1, and
# what sec:tensions assigns them), and in the lcdm arm H_leaf == H_stack identically, making this a
# NO-OP THERE -- which is the self-check. **
def Hleaf(a):
    return H0 * np.sqrt(OM / a ** 3 + OL + OR / a ** 4)            # radiation gravitates: L2
# ** DEFAULT ON (r3409).  The perturbation sector runs on the LEAF congruence, which is what the
# framework assigns it: P15 sec:properframe and P7's rate-rule remark both read "a process running
# in the content --- rs, r_D, recombination, THE PERTURBATIONS --- takes the leaf's".  Validated two
# ways before the default was inverted: the lcdm arm's two rate expressions are character-identical,
# so Jac == 1 and this is provably a no-op there; and that no-op was confirmed numerically at 2700
# modes, l_1 = 220 against the validated control's 220 and the sky's 220.6.  Set STACKPERT=1 to
# recover the pre-r3409 behaviour, which ran the perturbations on the stacking rate -- kept only so
# the earlier results in PO13_WORKING_STATE can be reproduced. **
LEAFPERT = os.environ.get('STACKPERT', '0') != '1'
Hl_of  = CubicSpline(eg, ag * Hleaf(ag) / C)                       # comoving leaf Hubble, 1/Mpc
Jac_of = CubicSpline(eg, Hphys(ag) / Hleaf(ag))                    # d eta_leaf / d eta_stack
# ** PHASEONLY=1: reckon ONLY the oscillator's phase in leaf conformal time, nothing else -- the
# PURE-CLOCK operation, isolated from LEAFPERT's full leaf dynamics.  Scaling the photon PRESSURE
# (restoring) term by phi^2=(H_stack/H_leaf)^2 makes the sound frequency k c_s -> k c_s
# (d eta_leaf/d eta_stack) while friction, source and diffusion stay on the stacking clock.  Distinct
# from LEAFPERT (which moves the whole equation to the leaf); the two are alternative operations and
# should not both be set.  Identically 1 in the lcdm arm, a provable no-op. **
PHASEONLY = os.environ.get('PHASEONLY', '0') == '1'
# ** PHASEPOW: the POWER of the clock factor phi = H_stack/H_leaf carried by the restoring term.
# The default 2 is the frequency reading -- the pressure term goes as k^2 c_s^2, so a clock on the
# frequency enters squared.  PHASEPOW=1 is the SOUND-SPEED reading: the clock enters c_s once, not
# k c_s twice.  Added r3511 (58) as a DIAGNOSTIC to bracket the two readings, after PHASEONLY=1 (phi^2)
# was found to OVERSHOOT the sky (l_1/l_A = 0.8090 against 0.7312) where LEAFPERT undershoots
# (0.6764) -- so the sky lies BETWEEN the two operations and the physical question is which power
# the restoring term carries.  Identically 1 in the lcdm arm for any power, so still a no-op there. **
PHASEPOW = float(os.environ.get('PHASEPOW', '2'))
Phi2_of = CubicSpline(eg, (Hphys(ag) / Hleaf(ag)) ** PHASEPOW if PHASEONLY else np.ones_like(ag))
# ** SRCSTACK (diagnostic, requires LEAFPERT): the layered-ontology division of the ONE perturbation
# equation between the two clocks.  L1 (stacking/geometry) is the gravitational potential Phi; L2
# (leaf/content) is the plasma.  LEAFPERT puts the WHOLE equation on the leaf and undershoots the
# position (source drags the phase); PHASEONLY puts ONLY the frequency on the leaf and overshoots
# (source+friction on stack under-damp).  SRCSTACK keeps the GEOMETRIC POTENTIAL sector on the stack
# clock while frequency/friction/diffusion (the content) stay on the leaf:
#   SRCSTACK=phi  -- only Phi's own evolution (out[:,6]=Php) on the stack (cleanest L1/L2 split).
#   SRCSTACK=src  -- Phi's evolution AND every potential coupling (the Php/Ps source terms) on stack.
# Identically LEAFPERT in the lcdm arm (Jac==1), a provable no-op.  A DIAGNOSTIC to let position and
# amplitude pin which terms are L1; NOT a committed frame. **
SRCSTACK = os.environ.get('SRCSTACK', '')
# ** PROJMAP (58's r3527 layer reading): the two-horizon ratio r_stack/r_leaf applied ONCE at the
# PROJECTION -- the content sound-horizon mapped onto the phenomenological ruler (the layer
# diffeomorphism's Jacobian), NOT a post-hoc relabel of the output peaks.  It multiplies the distance
# x0 in the k->l Bessel relation, so a source feature at k appears at l = k*x0*PROJMAP.  A single
# factor on the k->l relation is UNIFORM in l (comb and damping, both baked into S(kb), stretch
# together), so this is expected to move POSITION and leave HEIGHT ratios fixed -- run to MEASURE
# that, not assume it.  Default 1.0 = no-op. **
PROJMAP = float(os.environ.get('PROJMAP', '1'))
_rt = OR / ag ** 4 + OM / ag ** 3 + OL                            # ** the STACK, both arms **
# ** GSRC=1: THE CONSTRAINT FACTOR.  The G^0_0 equation is k^2 Phi + 3H(Phi'+H Psi) = -4 pi G a^2
# drho.  Writing the source as (3/2) H^2 sum(Om_i d_i) uses H^2 = (8 pi G/3) a^2 rho_tot -- the
# FRIEDMANN CONSTRAINT, which in CR is the L2 leaf readout "with radiation gravitating normally"
# (P15 sec:properframe).  The CR arm's Hc is the L1 rate, built from rho_tot WITHOUT radiation,
# while the Om_i are normalised to the full stack.  The two are not the same rho_tot, so the
# source is short by rho_tot(full)/rho_tot(free).  This factor supplies it.  Identically 1 in the
# lcdm arm, where the rate already carries radiation. **
_free = OM / ag ** 3 + OL
GSRC = os.environ.get('GSRC', '0') == '1' and not RAD_IN_RATE
Gf_of = CubicSpline(eg, (_rt / _free) if GSRC else np.ones_like(_rt))
# ** GSRCRAD=1 (58's r3530 diagnosis of the GSRC overshoot): apply the constraint factor _rt/_free to
# the RADIATION source terms ONLY (Ogv*dg + Onv*dn), leaving matter/baryons at plain normalisation --
# i.e. radiation enters Phi's source additively at full strength while the matter sector is NOT
# rescaled.  Requires GSRC=1 (else Gf==1, no-op).  ** CAVEAT (cc54): every Omega is normalised to
# _rt, so the matter coefficient is rho_m/rho_tot and its source is SHORT by rho_free/rho_tot too --
# the shortfall is the Hc^2-vs-Omega mismatch, not radiation-specific.  So this UNDER-counts matter by
# standard EFE; it lands the sky only if CR's constraint puts matter's local gravity on rho_free. **
GSRCRAD = os.environ.get('GSRCRAD', '0') == '1'
Og_of = CubicSpline(eg, (1 - FNU) * (OR / ag ** 4) / _rt)
On_of = CubicSpline(eg, FNU * (OR / ag ** 4) / _rt)
# ** THE MATTER SECTOR IS SPLIT INTO BARYONS AND CDM AT c54.178. **  Until now it was ONE fluid
# with one density contrast, which meant the baryon density was carried at the CDM's value -- and
# before recombination those are not the same: delta_b is dragged by the photons while delta_c grows.
# It is 16% of the matter and it enters the potential, so it is not free.  The split is also
# REQUIRED by the photon hierarchy that follows: once the baryons have their own velocity they must
# have their own density, or the continuity equation they satisfy is not theirs.
OB = OMBH2 / (H0 / 100) ** 2
OCDM = OM - OB
Ob_of = CubicSpline(eg, (OB / ag ** 3) / _rt)
Oc_of = CubicSpline(eg, (OCDM / ag ** 3) / _rt)
Om_of = CubicSpline(eg, (OM / ag ** 3) / _rt)
Rb_of = CubicSpline(eg, RB_REC * (ag / A_REC))
a_of_eta = CubicSpline(eg, ag)
eta_rec = float(np.interp(A_REC, ag, eg))
eta_0 = eg[-1]
D_M = eta_0 - eta_rec
# ** FREEZEJAC (diagnostic, 58's height-by-subtraction reference): freeze the clock ratio
# phi = Jac = H_stack/H_leaf at its RECOMBINATION value, removing the RUNNING of phi while keeping
# its level.  Paired with a running-phi run under SRCSTACK=vel, the per-peak HEIGHT ratio isolates
# the boost the RUNNING clock supplies -- CR's structural analogue of radiation driving.  phi == 1
# for all eta on the control arm (H_leaf == H_stack), so this is a provable no-op there. **
if os.environ.get('FREEZEJAC', '0') == '1':
    _phi_rec = float(Jac_of(eta_rec))
    Jac_of = (lambda v: (lambda e: v))(_phi_rec)
    print(f"  FREEZEJAC: clock ratio phi frozen at its recombination value phi_rec = {_phi_rec:.5f}")


def rs_from(z_lo):
    # r_s on the STACKING clock -- the COMOVING RULER for l_A = pi D_M / r_s, theta_* and the
    # projection (L1).  This is the OTHER of the instrument's two sound horizons; the PHASE
    # ACCUMULATOR for the oscillator and Q is r_s,leaf in `sound_phase`.  See that docstring: the two
    # are correct and NOT interchangeable (ratio 1.286 at the physical onset).  Do not unify them.
    return quad(lambda a: C / (a ** 2 * Hphys(a) * np.sqrt(3 * (1 + RB_REC * a / A_REC))),
                1.0 / (1.0 + z_lo), A_REC, limit=250)[0]


if ARM == 'lcdm':
    Z_START = 3.0e7                                      # deep in radiation domination
    R_S = rs_from(1e8)                                   # from a ~ 0, the standard sound horizon
else:
    # ** LATARG IS THE CORPUS'S ONE FITTED NUMBER, MADE VISIBLE, AND r2441+c54.189 IS WHY. **
    # `z_onset` is solved so that l_A = pi D_M / r_s hits a TARGET rather than coming out as an
    # output -- which is not a hidden fudge: P15 sec:acoustic states it in those words, *"the
    # measured acoustic scale is reproduced at the directly measured H_0 by a single z_onset"*, and
    # calls z_onset *"the one fitted number"*.  ** But it was a literal buried in a brentq call,
    # so nothing downstream could vary it and nothing had. **  Exposing it asks the question the
    # front actually needs: GIVEN that l_A is fitted, is the peak SPACING deficit -- the only
    # acoustic content left after c54.187 and c54.188 -- an artefact of where the pin was put?
    # *LATARG = 301.6 is the value as coded and is the default; nothing moves unless it is set.*
    _latarg = float(os.environ.get('LATARG', '301.6'))
    # ** ZSTART forces the onset redshift instead of solving it from LATARG.  Default unset =
    # byte-identical.  The closing counterfactual (58): push z_onset UP past the acoustic re-entry
    # redshifts (n=1 ~2.9e4, n=2 ~1.2e5, n=3 ~2.7e5) so the modes cross the horizon DURING the plasma
    # era, and read g2/g1 (scale-free, so it survives the acoustic-scale fit breaking).  If the
    # alternation appears as z_onset rises past re-entry, the residual IS the absence of
    # crossing-during-plasma and follows from the onset being on the branch point's cooling leg. **
    _zstart_env = os.environ.get('ZSTART')
    Z_START = float(_zstart_env) if _zstart_env else \
        brentq(lambda z: np.pi * D_M / rs_from(z) - _latarg, 1500., 60000.)
    R_S = rs_from(Z_START)
A_START = 1.0 / (1.0 + Z_START)
ETA_S = float(np.interp(A_START, ag, eg))
ETA_END = float(os.environ.get('ETAEND', 0)) or float(np.interp(min(20 * A_REC, 1.0), ag, eg))
L_A = np.pi * D_M / R_S

# ---- Thomson opacity, identical for both arms (a function of the scale factor alone) ------------
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), 'storyboard_receipts'))
from RD_diffusion_direct import xe_history, n_H0_of, sigT, Mpc_m, xe_total       # noqa: E402

_YP = 0.2454
_zg, _xeg = xe_history(lambda z: Hphys(1 / (1 + z)) * 1e3 / Mpc_m, OMBH2, _YP,
                       z_hi=3000.0, z_lo=80.0, n=6000)
_nH0 = n_H0_of(OMBH2, _YP)


def _xe(a):
    z = 1.0 / a - 1.0
    xH = (float(np.interp(z, _zg[::-1], _xeg[::-1])) if (_zg[-1] <= z <= _zg[0])
          else (1.0 if z > _zg[0] else float(_xeg[-1])))
    return xe_total(z, xH, _nH0, _YP, helium=True)


_aa = np.logspace(np.log10(1 / (1 + 3e4)), 0.0, 4000)
_ea = np.array([float(np.interp(x, ag, eg)) for x in _aa])
taup_of = CubicSpline(_ea, np.array([_xe(x) * _nH0 / x ** 3 * sigT * x * Mpc_m for x in _aa]))
VISC = 16.0 / 45.0
TPGATE = 0.6

# ---- the optical depth and the VISIBILITY, for the line-of-sight transfer (c54.173) --------------
# ** Until c54.173 this instrument evaluated the source at a SINGLE eta_rec -- a delta-function last
# scattering.  Real last scattering has a finite width, and treating it as instantaneous is the
# dominant error in the PEAK HEIGHTS: it was 13-26% at c54.168 against positions good to 1.5%.
# tau(eta) = INT_eta^eta0 tau' d(eta'),  g = tau' exp(-tau),  and the source is integrated against g. **
_egrid = np.linspace(float(_ea[0]), eta_0, 40000)
_tp = np.maximum(taup_of(_egrid), 0.0)
_tau = np.concatenate([[0.0], np.cumsum(0.5 * (_tp[1:] + _tp[:-1]) * np.diff(_egrid))])
_tau = _tau[-1] - _tau                                      # tau(eta), zero today
tau_of = CubicSpline(_egrid, _tau)
vis_of = CubicSpline(_egrid, _tp * np.exp(-_tau))           # g = tau' e^-tau
_gi = int(np.argmax(_tp * np.exp(-_tau)))
ETA_LS = float(_egrid[_gi])                                 # the visibility peak -- true last scattering
_gv = _tp * np.exp(-_tau)
_half = _gv > 0.5 * _gv[_gi]
ETA_LS_W = float(_egrid[_half][-1] - _egrid[_half][0])      # its FWHM in conformal time

# ---- THE DIFFUSION SCALE, DERIVED FROM THIS ARM'S OWN OPACITY AND RATE (c54.175) ----------------
# ** The tight-coupling closure in the hierarchy switches off at tau' = 0.6/Mpc.  The visibility
# peaks where tau' ~ 0.03/Mpc -- twenty times lower -- so the photon quadrupole and the slip are
# absent through the whole of last scattering and the line-of-sight transfer carried NO Silk
# damping at all.  That is the height error: at c54.173 P1/P2 and P1/P3 were both LOW, meaning the
# second and third peaks were too HIGH, which is what under-damping looks like. **
#
# The standard tight-coupling (WKB) result is a photon damping factor exp(-k^2/k_D^2) with
#     1/k_D^2(eta) = INT_0^eta [ R^2/(1+R) + 8/9 ] / [ 6 (1+R) tau' ] d(eta'),
# and it is DERIVED on this arm's own rate and opacity rather than imported or fitted -- which is
# what the pre-line-of-sight path did with a hardcoded r_D.
_Rg = Rb_of(_egrid)
# ** THE SHEAR COEFFICIENT IS 16/15, AND AT c54.177 IT IS DERIVED RATHER THAN REMEMBERED. **
# `L171w_hierarchy_damping_coefficient.py` measures it from the photon Boltzmann hierarchy with the
# polarisation multipoles carried alongside, on this instrument's own background and opacity, by
# ratio against the perfect tight-coupled fluid on the same equations.  Extrapolated to zero
# k/tau' it returns C = 1.0609 against 16/15 = 1.0667 with polarisation and C = 0.8844 against
# 8/9 = 0.8889 without -- ** and the POLARISATION CORRECTION, which is the thing actually in
# dispute, comes out as a factor 1.1996 against 6/5.  To three parts in ten thousand. **
#
# ** THE HISTORY MATTERS BECAUSE IT IS THE POINT. **  At c54.176 this was set to 16/15 on my
# recollection, then put back to 8/9 -- correctly, because a remembered number is not a derivation.
# In the same revision chi^2 through plik_lite was found to prefer 8/9 over 16/15 by 1123 units,
# and that preference was recorded and refused.  ** It is refused again here: 16/15 is adopted
# because it is DERIVED, and the 1123 is now a sharpened measurement of what the instrument is
# missing rather than an argument about a coefficient. **  What it is missing is named: the
# polarisation SOURCE terms.  Taking the polarisation's contribution to the DAMPING without its
# contribution to the SOURCE -- g*Pi/4 and (3/4k^2) d^2(g*Pi)/deta^2 -- is half of one physical
# effect, and the half taken is the half that removes power.
_POLC = float(os.environ.get('POLC', 16.0 / 15.0))
_int = (_Rg ** 2 / (1 + _Rg) + _POLC) / (6.0 * (1 + _Rg) * np.maximum(_tp, 1e-30))
# ** DAMPX IS A DIAGNOSTIC AND IS NEVER A PHYSICS CHOICE (c54.176). **  It multiplies 1/k_D^2 by a
# constant, so it slides the damping SCALE without touching the ENVELOPE'S SHAPE.  Its only use is
# to ask whether ONE scale can match BOTH P1/P2 and P1/P3 at once: if the two ratios select
# different DAMPX, no coefficient -- 8/9, 16/15 or any other -- can fix the heights, and the residual
# is the shape of the envelope rather than its scale.  Default 1.0; any run that reports physics
# must leave it there.
_DAMPX = float(os.environ.get('DAMPX', 1.0))
# ** DIFFLEAF (LGF, pairs with SRCSTACK=vel): Silk diffusion is a CONTENT process on a layer, so by the
# LGF axiom it keeps the LEAF clock -- like c_s and recombination -- not the stacking clock the setup
# integral above uses.  The random walk accumulates over eta_leaf with opacity tau'_leaf = tau'_stack/Jac:
#   r_D^2_leaf = INT (A/tau'_stack) Jac^2 d(eta_stack),  i.e. the integrand gains a factor phi^2 = Jac^2.
# Since phi<1 early (radiation era), this REDUCES the damping at high k -- exactly where vel over-damps.
# It is the same axiom that fixed the position, applied to the one remaining content term; NOT a knob.
# phi==1 on the control, so this is a provable no-op there (byte-identical). **
if os.environ.get('DIFFLEAF', '0') == '1':
    _int = _int * np.asarray(Jac_of(_egrid), dtype=float) ** 2
    print("  DIFFLEAF: k_D integral moved to the LEAF clock (integrand x phi^2); diffusion is content (LGF)")
_kD2inv = np.concatenate([[0.0], np.cumsum(0.5 * (_int[1:] + _int[:-1]) * np.diff(_egrid))])
kD2inv_of = CubicSpline(_egrid, _kD2inv)
_rD = float(np.sqrt(_kD2inv[_gi]))
print(f"  diffusion: r_D at the visibility peak = {_rD:.2f} Mpc  ->  l_D = {(eta_0-ETA_LS)/_rD:.0f}")


def evolve(kk, t_eval=None, e_end=None, y_init=None):
    """the hierarchy, vectorised over k.  State per mode: dc tc dg tg dn tn Phi F2..F_LN db

    ** db IS APPENDED AT THE END AND NOT INSERTED (c54.178), so that every index the line-of-sight
    transfer and the comb reader already use is untouched.  A re-layout of the state vector is a
    silent-failure machine: nothing raises, the spectrum just changes. **

    ** t_eval given => NO dense_output. **  Storing an interpolant for every adaptive step over
    2100 modes and eta = 0.02-4000 exhausts memory and the process is killed with no traceback
    (c54.173, and it took a `ps` to notice rather than an error).  The line-of-sight transfer knows
    its sample points in advance, so it asks for them.
    """
    nk = len(kk)
    NV = 7 + (LN - 1) + 1
    I_DB = NV - 1
    e_end = ETA_END if e_end is None else float(e_end)
    y0 = np.zeros((nk, NV))

    if ARM == 'lcdm':
        # ** ADIABATIC SUPER-HORIZON DATA, derived from this code's OWN constraint rather than
        #    quoted.  With Phi' = 0, k^2 Phi/(3H) negligible and Om_r -> 1, the Phi equation
        #    0 = -H Psi - (H/2)(Og dg + On dn + Oc dc) with adiabaticity dc = (3/4) dg gives
        #    dg = dn = -2 Phi.  theta follows from the Euler equation at leading order in k eta. **
        Ph0 = -np.ones(nk)
        dg0 = -2.0 * Ph0
        dc0 = 0.75 * dg0
        th0 = 0.5 * kk ** 2 * ETA_S * Ph0
        y0[:, 0], y0[:, 1] = dc0, th0
        y0[:, 2], y0[:, 3] = dg0, th0
        y0[:, 4], y0[:, 5] = dg0, th0
        y0[:, 6] = Ph0
        y0[:, I_DB] = dc0                        # adiabatic: delta_b = delta_c = (3/4) delta_gamma
    else:
        # ** THE CR ARM'S HANDOVER.  Theta-hat flat in k (sec:envelope's deep sub-horizon limit),
        #    the phase common, AND THE VELOCITIES ZERO -- which is what the corpus's own text says
        #    and what c54.164 found ROBUST_p1p2_scan does not impose.  Stated as a choice, and it
        #    is the choice the paper describes. **
        # ** CRPHI OPENS THE ONE THING "A COMMON PHASE" LEAVES UNSPECIFIED, AND r2441+c54.186 IS
        # WHY. **  The corpus's datum is "ONE datum per mode and a COMMON phase"; this block picks
        # the phase at a DENSITY extremum, which is a choice inside that phrase and not the phrase
        # itself.  ** c54.164 already measured that ell_1 is NOT stable under readings of this same
        # stated initial condition -- ell_1 in {150, 165, 315} -- while the source comb's SPACING is,
        # at 0.72-0.79 of pi/r_s under every one. **  Eight instrument states have varied the
        # TRANSFER and none has varied the DATUM, so an invariance of ell_1/ell_A across them is an
        # invariance of the transfer and says nothing about the datum.  *CRPHI = 0 is the choice as
        # coded and is the default; nothing moves unless it is set.*
        #
        # For a mode already sub-horizon at the seam, delta_g = D cos(k c_s (eta - eta_S) + phi),
        # and the code's own continuity equation d(delta_g)/deta = -(4/3) theta_g gives
        # theta_g = (3/4) D k c_s sin(phi).  phi = 0 is a density extremum with theta = 0.
        # ** CRPHI=entry -- THE FROZEN-MODE CONDITION CARRIED FORWARD, r3369 (node 57). **
        #   P15 argues sin(phi) = 0 from "what crosses is FROZEN": a frozen mode has
        #   d(delta_g)/deta = 0, hence theta_g = 0.  *That is a condition at the BRANCH POINT.*  The
        #   instrument imposes it at the ONSET -- which is not a locus of the construction at all but
        #   the redshift solved so that l_A hits LATARG.  Between the two, a mode with k/H > 1 has
        #   ENTERED THE HORIZON AND OSCILLATED: measured r3359, entry at z = 15,700 for the
        #   first-peak mode against an onset at z = 6,761, with 0.186 pi of acoustic phase accumulated
        #   in between, rising to 0.636 pi at l = 400 and 1.639 pi at l = 800, and ZERO below l ~ 150
        #   where the modes really are still frozen and the condition is CORRECT as coded.
        #   ** So this reading carries the SAME condition to the onset instead of re-imposing it there:
        #   phi(k) = k * int_entry^onset c_s d eta, and phi = 0 for any mode that has not entered. **
        #   *It is a HYPOTHESIS about the construction and not a derivation from it -- no source states
        #   what the datum should be at the onset (checked across all three source classes, r3363).*
        #   The neglected phase is SUPERLINEAR in k, since entry itself moves with k, so this is a
        #   SPACING correction and not only an offset.  ** Default unchanged; nothing moves unless set. **
        _phi_mode = os.environ.get('CRPHI', '0.0')
        if _phi_mode in ('entry', 'entryleaf'):
            # ** entryleaf: the seam IC reckoned on the LEAF clock (58's start-time test).  Horizon
            # entry is detected with the leaf comoving Hubble, and the pre-onset acoustic phase is
            # integrated in eta_leaf (d eta_leaf = Jac * d eta_stack).  'entry' keeps the stack clock
            # (node 57 r3369).  Diagnostic of whether the under-produced odd-even alternation is the
            # late plasma start (missing oscillation history) rather than the driving. **
            _leaf = (_phi_mode == 'entryleaf')
            _Hrate = Hleaf if _leaf else Hphys
            _Hc_g = ag * _Hrate(ag) / C
            _phi = np.zeros(nk)
            for _j, _k in enumerate(kk):
                _in = np.nonzero(_k / _Hc_g > 1.0)[0]
                if len(_in) == 0 or ag[_in[0]] >= A_START:
                    continue                          # never entered before the onset: still frozen
                _e_in = float(np.interp(ag[_in[0]], ag, eg))
                _phi[_j] = _k * quad(
                    lambda e: (float(Jac_of(e)) if _leaf else 1.0)
                    / np.sqrt(3.0 * (1.0 + float(Rb_of(e)))), _e_in, ETA_S, limit=200)[0]
            print(f"    CRPHI={_phi_mode}: phi(k) spans {_phi.min():.4f} to {_phi.max():.4f} rad "
                  f"({_phi.max()/np.pi:.3f} pi); {int((_phi == 0).sum())} of {nk} modes still frozen")
        else:
            _phi = float(_phi_mode)
        xe = float(os.environ.get('CRXE', str(1.0 / np.sqrt(3))))

        def _T(x):
            """the corpus's own transfer shape 3(sin x - x cos x)/x^3, the C4 form"""
            x = np.asarray(x, float)
            return np.where(x < 1e-6, 1.0 - x ** 2 / 10.0,
                            3 * (np.sin(x) - x * np.cos(np.where(x < 1e-6, 1.0, x)))
                            / np.where(x < 1e-6, 1.0, x) ** 3)

        # ** CRAMP OPENS THE SECOND DATUM FREEDOM: WHAT "FLAT IN k" IS FLAT AT.  c54.187 scanned the
        # PHASE and named this one as the remaining one.  The coded reading evaluates the C4 transfer
        # at a SINGLE argument xe = 1/sqrt(3) for every mode -- which is that shape read at each
        # mode's OWN horizon crossing (x = k c_s eta with k eta = 1), a self-similar reading and a
        # defensible one.  ** The alternative reading evaluates the SAME shape at each mode's own
        # phase AT THE SEAM, x = k c_s eta_S, so modes that crossed earlier get a smaller amplitude.
        # Both are readings of "one datum per mode"; neither is invented here. **
        #   CRAMP=flat  Theta-hat = T(xe), k-independent          [the instrument as coded, default]
        #   CRAMP=seam  Theta-hat = T(k c_s eta_S), k-dependent
        # *A scan that moves the SPACING is the one that would matter -- the phase moved only the
        # position.  This knob is a no-op at its default and nothing moves unless it is set.*
        _cs = 1.0 / np.sqrt(3.0 * (1.0 + float(Rb_of(ETA_S))))
        _amp = os.environ.get('CRAMP', 'flat')
        if _amp == 'seam':
            _That0 = -_T(kk * _cs * ETA_S) / 2.0
        elif _amp == 'flat':
            _That0 = (-_T(xe) / 2.0) * np.ones(nk)
        else:
            raise SystemExit(f"CRAMP={_amp} is not a reading this instrument knows (flat|seam)")
        A_flat = -(3 * (np.sin(xe) - xe * np.cos(xe)) / xe ** 3) / 2
        Ph0 = -np.ones(nk)
        That = _That0
        dg0 = 4.0 * (That - Ph0) * np.cos(_phi)
        th0 = 0.75 * (4.0 * (That + 1.0)) * kk * _cs * np.sin(_phi)
        y0[:, 0], y0[:, 1] = 0.75 * dg0, th0
        y0[:, 2], y0[:, 3] = dg0, th0
        y0[:, 4], y0[:, 5] = dg0, th0
        y0[:, 6] = Ph0
        y0[:, I_DB] = 0.75 * dg0

    def rhs(e, Y):
        y = Y.reshape(nk, NV)
        dc, tc, dg, tg, dn, tn, Ph = (y[:, j] for j in range(7))
        db = y[:, I_DB]
        F = y[:, 7:I_DB]
        Hc, Rb = float(Hl_of(e) if LEAFPERT else Hc_of(e)), float(Rb_of(e))
        PH2 = float(Phi2_of(e))                      # PHASEONLY clock factor (1 unless PHASEONLY)
        Ogv, Onv = float(Og_of(e)), float(On_of(e))
        Ocv, Obv = float(Oc_of(e)), float(Ob_of(e))
        sig = F[:, 0] / 2
        tp = float(taup_of(e))
        # ** NOTC=1 removes the in-hierarchy tight-coupling damping (the photon quadrupole closure
        # and the baryon slip) so that the DERIVED exp(-k^2/k_D^2) factor is the only place
        # diffusion acts.  Otherwise the two double-count over tau' > TPGATE, which is exactly the
        # region the k_D integral also covers -- and at c54.175 the control came out OVER-damped
        # (+6.7% and +17% on the height ratios) where before it was under-damped. **
        on = (tp > TPGATE) and os.environ.get('NOTC', '1') != '1'
        sgg = (VISC * tg / tp) if on else np.zeros(nk)
        slip = (kk ** 2 * Rb ** 2 / (3.0 * (1 + Rb) ** 2 * tp)) if on else np.zeros(nk)
        Ps = Ph - 6 * Hc ** 2 * (Onv * sig + Ogv * sgg) / kk ** 2
        # ** THE BARYONS ENTER THE POTENTIAL AT THEIR OWN CONTRAST (c54.178). **  Before this they
        # were carried at the CDM's, which over-weights them: delta_b is dragged by the photons and
        # oscillates while delta_c grows.  It is 16% of the matter and it is not free.
        # BSPLIT=0 restores the pre-c54.178 behaviour -- the whole matter sector at delta_c -- so
        # that the change can be MEASURED on this instrument rather than asserted.
        _mat = (Ocv * dc + Obv * db) if BSPLIT else ((Ocv + Obv) * dc)
        _gf = float(Gf_of(e))
        _dsrc = (_gf * (Ogv * dg + Onv * dn) + _mat) if GSRCRAD else _gf * (Ogv * dg + Onv * dn + _mat)
        Php = -Hc * Ps - kk ** 2 * Ph / (3 * Hc) - (Hc / 2) * _dsrc
        # ** DR multiplies EVERY coupling to the potential, at EVERY site. **
        out = np.empty_like(y)
        out[:, 0] = -tc + DRC * 3 * Php
        out[:, 1] = -Hc * tc + DRE * kk ** 2 * Ps
        out[:, 2] = -(4 / 3) * tg + DRC * 4 * Php
        out[:, 3] = (-(Hc * Rb / (1 + Rb)) * tg + PH2 * (kk ** 2 / (1 + Rb)) * dg / 4
                     + DRE * kk ** 2 * Ps - kk ** 2 * sgg / (1 + Rb) - slip * tg)
        out[:, 4] = -(4 / 3) * tn + DRC * 4 * Php
        out[:, 5] = kk ** 2 * (dn / 4 - sig) + DRE * kk ** 2 * Ps
        out[:, 6] = Php
        out[:, 7] = (8 / 15) * tn - (3 / 5) * kk * F[:, 1]
        for i in range(1, LN - 2):
            l = i + 2
            out[:, 7 + i] = kk / (2 * l + 1) * (l * F[:, i - 1] - (l + 1) * F[:, i + 1])
        out[:, 7 + LN - 2] = kk * F[:, LN - 3] - (LN + 1) / e * F[:, LN - 2]
        # ** the baryon continuity equation, on the baryon velocity.  In this branch the baryons are
        # tightly coupled and tg IS their velocity; the hierarchy branch gives them their own. **
        out[:, I_DB] = -tg + DRC * 3 * Php
        jac = float(Jac_of(e)) if LEAFPERT else 1.0
        if SRCSTACK and LEAFPERT:
            # split the GEOMETRIC POTENTIAL sector back onto the stack clock (x1); content stays on leaf
            src = np.zeros_like(out)
            if SRCSTACK in ('phi', 'src'):
                src[:, 6] = Php                               # Phi's own evolution (L1)
            if SRCSTACK in ('src', 'cpl'):                    # the potential's couplings INTO the plasma
                src[:, 0] = DRC * 3 * Php
                src[:, 1] = DRE * kk ** 2 * Ps
                src[:, 2] = DRC * 4 * Php
                src[:, 3] = DRE * kk ** 2 * Ps
                src[:, 4] = DRC * 4 * Php
                src[:, 5] = DRE * kk ** 2 * Ps
                src[:, I_DB] = DRC * 3 * Php
            if SRCSTACK == 'vel':                             # ONLY the velocity-source Ps (the phase driver)
                src[:, 1] = DRE * kk ** 2 * Ps
                src[:, 3] = DRE * kk ** 2 * Ps
                src[:, 5] = DRE * kk ** 2 * Ps
            return ((out - src) * jac + src).ravel()
        return out.ravel() * jac

    if y_init is not None:
        y0 = y_init
    sol = solve_ivp(rhs, [ETA_S, e_end], y0.ravel(), method='RK45', rtol=RTOL, atol=1e-12,
                    dense_output=(t_eval is None), t_eval=t_eval,
                    max_step=(e_end - ETA_S) / 200)
    return sol, nk, NV


def sound_phase(e_lo, e_hi):
    """r_s on the LEAF clock -- the PHASE ACCUMULATOR for the oscillator and for Q(k).

    ** THE INSTRUMENT CARRIES TWO SOUND HORIZONS BY DESIGN, AND THEY ARE NOT INTERCHANGEABLE. **
      - r_s,leaf  (THIS function): int c_s d(eta_leaf) = int c_s Jac d(eta_stack).  The oscillator
        turns over on the leaf clock (LEAFPERT), so the accumulated sound phase Q -- a turnover
        expressed in half-periods -- MUST be reckoned here.  A phase accumulator is reckoned in the
        clock the phase accumulates in.
      - r_s,stack (`rs_from`): int c_s d(eta_stack).  The COMOVING RULER, used by l_A = pi D_M / r_s,
        theta_* and the line-of-sight projection (L1, what sec:tensions assigns them).
    Both are correct.  The ratio r_s,stack / r_s,leaf = 1.286 at the physical onset (rs_stack 135.46,
    rs_leaf 105.36 Mpc).  ** Do NOT unify them: that reads the oscillator's phase on the ruler's clock
    and undoes the leaf-rate correction. **  The gate is the undriven Q column, which must return
    1.0000 AND be k-independent on BOTH arms; a stack-clock numerator here made CR's undriven Q come
    out at 1.33-1.57 (the stack/leaf ratio, k-dependent because the turnover moves with k). """
    return quad(lambda e: (float(Jac_of(e)) if LEAFPERT else 1.0)
                / np.sqrt(3.0 * (1.0 + float(Rb_of(e)))), e_lo, e_hi, limit=200)[0]


def qscan():
    """** THE DRIVING SHIFT, MEASURED BY SUBTRACTION AGAINST AN UNDRIVEN REFERENCE. **

    For each k, evolve TWICE on the same equations -- driven and undriven -- and report Q, the
    accumulated sound phase in half-periods at the FIRST extremum of Theta-hat = Theta_0 + Psi:

        Q(k) = k * INT c_s d(eta) / pi,  from eta_start to that extremum.

    ** Undriven, a free oscillator turns over at Q = 1 by construction, so the undriven column IS
    the calibration and it is measured rather than assumed. **  The difference

        Delta(k) = Q_undriven(k) - Q_driven(k)

    is the driving shift in half-periods, with NO model of the driving anywhere in it: the two runs
    differ in one multiplicative switch and in nothing else.
    """
    global DR, DRC, DRE
    KS = np.array([float(x) for x in os.environ.get(
        'QK', '0.012,0.020,0.030,0.045,0.065,0.090,0.120,0.160').split(',')])
    # ** FOUR CONFIGURATIONS, and the middle two are the attribution. **
    CONFIGS = [('undriven', 0.0, 0.0), ('continuity only', 1.0, 0.0),
               ('Euler only', 0.0, 1.0), ('driven', 1.0, 1.0)]
    print()
    print("=" * 78)
    print(f"  Q1(k) — THE DRIVING SHIFT BY SUBTRACTION   ARM={ARM}")
    print("=" * 78)
    print("  Q = k INT c_s d(eta)/pi at the first extremum of Theta-hat, from eta_start.")
    print("  ** Undriven is the calibration and is MEASURED, not assumed. **\n")
    res = {}
    for tag, dc, de in CONFIGS:
        DRC, DRE = dc, de
        sol, nk, NV = evolve(KS)
        ee = np.linspace(ETA_S + 1e-6, eta_rec, 4000)
        Y = np.array([sol.sol(e).reshape(nk, NV) for e in ee])
        # ** Theta_0 = delta_gamma/4, THE SAME VARIABLE IN BOTH COLUMNS. **  The first draft used
        # Theta-hat = Theta_0 + Psi, and Psi is NOT switched off by DR -- only its couplings INTO
        # the fluid are -- so the undriven column carried a non-oscillating piece that produced a
        # spurious turning point at the start and the calibration came out 0.0003 instead of 1.
        # ** The undriven calibration is what caught it, which is the whole reason for measuring
        # rather than assuming it. **  Theta_0 is also the variable the c54.168 guard validated.
        That = Y[:, :, 2] / 4
        Tvel = Y[:, :, 3]                                 # photon velocity theta_gamma (index 3)
        # ** QTURN=vel defines the turnover as the first ZERO-CROSSING OF THE PHOTON VELOCITY, not the
        # extremum of Theta_0.  Under driving dTheta_0/deta = -(4/3)theta_g + DRC*4*Phi', so the density
        # extremum is NOT the velocity zero when the potential drives -- and for the CR arm's frozen
        # sub-horizon IC the k eta>1 cut removes nothing, so the Theta_0 extremum catches an early
        # driving transient.  The velocity zero is the physical acoustic turnover and is transient-free. **
        _turn_vel = os.environ.get('QTURN', '') == 'vel'
        q = []
        for i in range(nk):
            if _turn_vel:
                v = Tvel[:, i]
                turn = np.where(np.sign(v[1:]) != np.sign(v[:-1]))[0]
            else:
                d = np.diff(That[:, i])
                turn = np.where(np.sign(d[1:]) != np.sign(d[:-1]))[0]
            # ** THE ACOUSTIC TURNOVER IS BY DEFINITION AFTER HORIZON ENTRY, so extrema at k eta < 1
            # are excluded.  This is not a tuned threshold: it is the definition of the quantity.
            # Without it the DRIVEN LambdaCDM column returned Q ~ 0.001 -- a decaying-mode transient
            # in the initial data, sitting two grid points from the start, and the undriven column
            # (Q = 1.000) is what exposed it. **  For the CR arm the modes are already sub-horizon
            # at the onset, so this cut removes nothing there and the two arms stay like-for-like.
            turn = [t for t in turn if KS[i] * ee[t + 1] > 1.0]
            # ** QMIN skips a frozen-IC DRIVING TRANSIENT: on the CR arm the driven mode's first
            # velocity zero-crossing sits at Q ~ 0.08 (the potential's initial kick to a mode already
            # deep sub-horizon), and the real acoustic turnover is the next crossing at Q ~ 1.2, with
            # subsequent crossings spaced ~1 half-period (the undriven period).  Requiring Q > QMIN
            # takes the acoustic turnover, not the transient.  Default 0 = unchanged; the undriven
            # column (no transient) is unaffected at any QMIN < 1. **
            _qmin = float(os.environ.get('QMIN', '0'))
            _cand = [(t, KS[i] * sound_phase(ETA_S, ee[t + 1]) / np.pi) for t in turn]
            _cand = [(t, qv) for t, qv in _cand if qv > _qmin]
            if not _cand:
                q.append(np.nan); continue
            q.append(_cand[0][1])
        res[tag] = np.array(q)
    hdr = ('k [1/Mpc]', 'undriven', 'continuity', 'Euler only', 'driven')
    print(f"  {hdr[0]:>11} {hdr[1]:>11} {hdr[2]:>12} {hdr[3]:>12} {hdr[4]:>10}")
    fmt = lambda x: ('%.4f' % x) if np.isfinite(x) else '—'                       # noqa: E731
    for i, k in enumerate(KS):
        print(f"  {k:>11.4f} {fmt(res['undriven'][i]):>11} {fmt(res['continuity only'][i]):>12} "
              f"{fmt(res['Euler only'][i]):>12} {fmt(res['driven'][i]):>10}")
    u = res['undriven'][np.isfinite(res['undriven'])]
    print(f"\n  ** CALIBRATION: undriven spans {u.min():.4f}-{u.max():.4f} against the exact 1. **")
    print(f"\n  {'configuration':>16} {'Q range':>20} {'variation':>11} {'fitted exponent':>17}")
    for tag, _, _ in CONFIGS:
        q = res[tag]
        m = np.isfinite(q)
        if m.sum() < 3:
            continue
        sl = np.polyfit(np.log(KS[m]), np.log(q[m]), 1)[0]
        print(f"  {tag:>16} {('%.4f - %.4f' % (q[m].min(), q[m].max())):>20} "
              f"{q[m].max()/q[m].min():>10.2f}x {('k^%+.2f' % sl):>17}")
    print("\n  ** THE ATTRIBUTION: whichever single term reproduces the driven column's variation")
    print("     is the term the k-dependence lives in.  If neither does, it is their interference. **")
    return 0


def los_spectrum(kk, ee, Y, L_A, D_M, R_S):
    """** Delta_l(k) = INT S(k,eta) j_l(k(eta_0 - eta)) d(eta), with

           S = g (Theta_0 + Psi)  +  e^-tau (Phi' + Psi')  +  (1/k^2) d/d(eta) [ g theta_b ].

    ** THE DOPPLER TERM CARRIES 1/k^2 AND NOT 1/k, and the difference is a derivation rather than a
    tuning. **  The line-of-sight term is (g v_b)'/k with v_b the VELOCITY; this hierarchy evolves
    theta = i k . v, so v_b = theta_b/k and the term is (g theta_b)'/k^2.  Written with 1/k the
    Doppler contribution is over-weighted in proportion to k, which fills the troughs at high
    multipole and corrupts the height ratios while leaving the FIRST peak's position almost alone --
    which is exactly the signature the first line-of-sight run showed.

    The first term is the monopole seen through a visibility of FINITE WIDTH; the second is the
    integrated Sachs-Wolfe; the third is the Doppler term, differentiated as a whole rather than
    evaluated at a point. **  What this replaces is a source evaluated at a SINGLE eta_rec -- a
    delta-function last scattering, whose true width here is 37.8 Mpc FWHM.
    """
    nk = len(kk)
    sg = Y[:, :, 7] / 2
    Hcv = np.array([Hc_of(e) for e in ee])[:, None]
    Onv = np.array([On_of(e) for e in ee])[:, None]
    Ph = Y[:, :, 6]
    Ps = Ph - 6 * Hcv ** 2 * Onv * sg / kk[None, :] ** 2
    g_ = vis_of(ee)[:, None]
    et = np.exp(-tau_of(ee))[:, None]
    # ** the damping multiplies the PHOTON perturbations and not the potentials. **  Theta_0 and the
    # baryon velocity diffuse; Psi and the ISW do not.
    print(f"  line-of-sight: visibility peak eta = {ETA_LS:.2f}, FWHM = {ETA_LS_W:.1f} Mpc, "
          f"{len(ee)} samples over eta = {ee[0]:.0f}-{ee[-1]:.0f}")
    dk = np.gradient(kk)
    P = kk ** (0.965 - 1) / kk * dk
    x0 = eta_0 - ee
    ls = np.arange(100, int(LMAXL), int(os.environ.get('LSTEP', '8')))

    # ** POLSRC (consistency repair, both arms): the instrument already takes polarisation's contribution
    # to the DAMPING (the 16/15 coefficient in k_D) but drops its contribution to the SOURCE -- half of
    # one physical effect, the half that removes power (the recorded 1123-chi^2 debt on the control).
    # Restore the two polarisation source terms  g*Pi/4  and  (3/4k^2) d^2(g*Pi)/deta^2.  In the polarised
    # tight-coupling limit of the L171w hierarchy (F_2'=(8/15)tg-tau'(F_2-Pi/10), G_0=Pi/2, G_2=Pi/10):
    #   Pi = (5/2) F_2,  F_2 = (32/45)(tg/tau'),  so  Pi = (16/9)(tg/tau')  -- tg = photon velocity Y[:,3].
    # NOT a CR knob: symmetric across arms, no free parameter, completion of a half-present term. **
    _POLSRC = os.environ.get('POLSRC', '0') == '1'

    def source(dampx):
        # ** the damping multiplies the PHOTON perturbations and not the potentials. **  Theta_0 and
        # the baryon velocity diffuse; Psi and the ISW do not.
        Dmp = np.exp(-dampx * (kk[None, :] ** 2) * kD2inv_of(ee)[:, None])
        S = (g_ * (Y[:, :, 2] / 4 * Dmp + Ps)
             + et * (np.gradient(Ph, ee, axis=0) + np.gradient(Ps, ee, axis=0))
             + np.gradient(g_ * Y[:, :, 3] * Dmp, ee, axis=0) / kk[None, :] ** 2)
        if _POLSRC:
            # g*Pi = (tau' e^-tau)(16/9 tg/tau') = (16/9) e^-tau tg -- the tau' CANCELS, so g*Pi is finite
            # through last scattering (the tight-coupling Pi diverges but g vanishes at the same rate).
            gPi = (16.0 / 9.0) * et * Y[:, :, 3] * Dmp                   # a photon perturbation: it diffuses
            S = S + gPi / 4.0 + (3.0 / (4.0 * kk[None, :] ** 2)) * \
                np.gradient(np.gradient(gPi, ee, axis=0), ee, axis=0)
        return S

    def spectra(dampx_list):
        """** THE BESSEL PROJECTION IS PAID ONCE FOR THE WHOLE SCAN, NOT ONCE PER POINT. **

        j_l(k(eta_0-eta)) does not depend on the damping, and evaluating it over 560 x 1800 points
        for every multipole is the entire cost of the transfer.  Looping ell OUTSIDE and the damping
        INSIDE turns an N-point scan from N projections into one.  The sources are held for all N
        (~20 MB per point) rather than the Bessel bank (~2 GB), which is the affordable half.
        """
        Ss = [source(x) for x in dampx_list]
        Cl = np.zeros((len(dampx_list), len(ls)))
        for j_, l in enumerate(ls):
            J = spherical_jn(int(l), kk[None, :] * x0[:, None] * PROJMAP)
            for i_, S in enumerate(Ss):
                Cl[i_, j_] = np.sum(P * np.trapezoid(S * J, ee, axis=0) ** 2)
        return Cl * (ls * (ls + 1))[None, :]

    # ** DSCAN SLIDES THE DAMPING SCALE AND NOTHING ELSE (c54.176). **  If P1/P2 and P1/P3 select
    # DIFFERENT multipliers, then no coefficient in the k_D integral -- 8/9, 16/15, or any other --
    # can match both, and the residual is the SHAPE of the damping envelope, not its scale.
    _scan = os.environ.get('DSCAN')
    if _scan:
        _xs = [float(v) for v in _scan.split(',')]
        _all = spectra(_xs)
        print("  " + "-" * 74)
        print("  DAMPING-SCALE SCAN — one multiplier on 1/k_D^2, everything else held fixed")
        print("  " + "-" * 74)
        print(f"    {'DAMPX':>8} {'l_1':>6} {'P1/P2':>9} {'vs sky':>9} {'P1/P3':>9} {'vs sky':>9}")
        for _x, _Dl in zip(_xs, _all):
            if os.environ.get('DSAVE'):
                np.savez(f"{os.environ['DSAVE']}_{_x:.3f}.npz", ls=ls, Dl=_Dl, l_A=L_A, D_M=D_M,
                         r_s=R_S, arm=ARM, dampx=_x)
            _pk = [q for q in argrelextrema(_Dl, np.greater, order=3)[0]]
            if len(_pk) < 3:
                print(f"    {_x:>8.3f}   fewer than three peaks")
                continue
            _r2, _r3 = _Dl[_pk[0]] / _Dl[_pk[1]], _Dl[_pk[0]] / _Dl[_pk[2]]
            print(f"    {_x:>8.3f} {int(ls[_pk[0]]):>6} {_r2:>9.4f} {(_r2-2.256)/2.256:>8.2%} "
                  f"{_r3:>9.4f} {(_r3-2.280)/2.280:>8.2%}")
        print(f"    {'sky':>8} {221.1:>6.1f} {2.256:>9.4f} {'+-3.4%':>9} {2.280:>9.4f} "
              f"{'+-3.2%':>9}")
        print("    *the sky's own peak-height ratios carry 3.2-3.4% from the plik_lite covariance,")
        print("     read on the peak bandpower bins -- so this column resolves nothing finer.*")
        return 0
    Dl = spectra([_DAMPX])[0]
    if os.environ.get('SAVE'):
        np.savez(os.environ['SAVE'], ls=ls, Dl=Dl, l_A=L_A, D_M=D_M, r_s=R_S, arm=ARM)
        print(f"  saved {len(ls)} multipoles to {os.environ['SAVE']}")
    pk = [q for q in argrelextrema(Dl, np.greater, order=3)[0]]
    print("  " + "-" * 74)
    print(f"  PEAKS (line-of-sight)   l_A = {L_A:.1f}")
    print("  " + "-" * 74)
    print(f"    peaks at l = {[int(ls[q]) for q in pk[:4]]}")
    if len(pk) >= 3:
        print(f"    l_1/l_A = {ls[pk[0]]/L_A:.4f}   P1/P2 = {Dl[pk[0]]/Dl[pk[1]]:.3f}   "
              f"P1/P3 = {Dl[pk[0]]/Dl[pk[2]]:.3f}")
    print(f"    sky: 220.6 / 538.1 / 809.8,  l_1/l_A = {220.6/301.7:.4f},  P1/P2 = 2.217,  "
          f"P1/P3 = 2.277")
    return 0



def alias_gate(kk):
    """** THE PROJECTION MUST RESOLVE THE BESSEL OSCILLATION IN k, WHICH HAS PERIOD 2 pi / D_M. **

    ** THIS GATE EXISTED ONLY ON THE DELTA-FUNCTION PATH UNTIL c54.178, AND THE LINE-OF-SIGHT PATH
    -- the default since c54.173 -- HAD NONE. **  It cost a run immediately: a development
    configuration at 300 modes put the first peak at ell = 196 instead of 220 and nothing said so.
    *The failure is silent by construction, which is why it needs a gate and not care: the SOURCE
    comb stays correct to a per cent while the PROJECTED spectrum combs at a spacing set by the
    sampling.*  Returns True if the sampling is adequate.
    """
    dk_need = 2.0 * np.pi / D_M
    dk_have = float(np.median(np.diff(kk)))
    print(f"  projection sampling: dk = {dk_have:.3e}, Bessel period 2pi/D = {dk_need:.3e}, "
          f"points per period = {dk_need/dk_have:.1f}")
    if dk_need / dk_have >= 4.0:
        return True
    if ARM == 'cr' and os.environ.get('KCONT', '0') != '1':
        print("  ⌗ CR's ladder is DISCRETE and physical, so this is not aliasing — but it is only")
        print("    not aliasing if the answer does not depend on it. Run KCONT=1 to check.")
        return True
    print("  ⛔ UNDER-SAMPLED — raise NK; the projected peaks would be aliasing, and the source")
    print("     comb would stay correct while they did it.")
    return False


# =================================================================================================
# THE PHOTON BOLTZMANN HIERARCHY WITH POLARISATION (r2376+c54.178, front #2)
# =================================================================================================
# ** WHAT THIS REPLACES AND WHY. **  Until now the photons were a two-moment FLUID and the diffusion
# damping was applied to the source as a derived envelope exp(-k^2/k_D^2).  c54.177 derived the
# coefficient in that envelope from the hierarchy -- and in doing so named what the envelope cannot
# do: polarisation enters the transfer TWICE, raising the damping AND contributing to the SOURCE
# through g*Pi/4 and (3/4k^2) d^2(g*Pi)/deta^2 with Pi = Theta_2 + Theta^P_0 + Theta^P_2.  ** An
# envelope has the half that removes power and not the half that returns it. **  The only way to get
# both is to carry the multipoles.
#
# ** THE SWITCH IS PLACED WHERE THE ENVELOPE IS STILL RIGHT AND THE HIERARCHY IS STILL CHEAP. **
# Deep in tight coupling the hierarchy is stiff -- tau' ~ 1e5/Mpc at eta ~ 1 -- and integrating it
# there costs everything and buys nothing.  ** At tau' = 3/Mpc (eta = 128) only 3.3% of the total
# 1/k_D^2 has accumulated, so 97% of the damping is done DYNAMICALLY by the hierarchy and the
# envelope carries only the deep tail where it is most accurate. **  That number is printed, and it
# is the justification for the split rather than a hope about it.
#
#   segment 1   the fluid, exactly as before, from ETA_S to eta_sw
#   segment 2   the hierarchy from eta_sw, initialised on the TIGHT-COUPLING values of F_2, G_0, G_2
#               so that no relaxation transient is charged to the physics
#
# and the source multiplies by exp(-k^2 * kD2inv(min(eta, eta_sw))) -- FROZEN at the switch, so the
# envelope covers [start, eta_sw] and the hierarchy covers [eta_sw, end] and neither covers the
# other's interval.  ** That is what makes a double count impossible here rather than merely absent:
# the two mechanisms are supported on disjoint intervals by construction. **
LG = int(os.environ.get('LG', '24'))            # photon + polarisation hierarchy depth
TCSW = float(os.environ.get('TCSW', '3.0'))     # tau' at which the fluid hands over, 1/Mpc
NVF = 7 + (LN - 1) + 1                          # the fluid layout, unchanged
I_DB_ = NVF - 1
I_TB = NVF                                      # the baryon velocity, its own from here
I_FG = I_TB + 1                                 # F_2 .. F_LG          (LG-1 entries)
I_GG = I_FG + (LG - 1)                          # G_0 .. G_LG          (LG+1 entries)
NVH = I_GG + (LG + 1)


def eta_switch():
    """the conformal time at which tau' falls to TCSW -- one time for every mode

    ** A PER-MODE SWITCH WOULD BUY NOTHING HERE AND COST CORRECTNESS. **  The largest wavenumber this
    instrument carries is k_max = LMAXL/D_M ~ 0.14/Mpc, so at tau' = 3 every mode has k/tau' < 0.05
    and the tight-coupling expansion is good to a part in a thousand for all of them at once.
    """
    _e = np.linspace(float(_ea[0]), eta_rec, 20000)
    _t = taup_of(_e)
    i = int(np.argmin(np.abs(_t - TCSW)))
    return float(_e[i])


def evolve_hier(kk, t_eval, e_sw, yF):
    """segment 2: the photon hierarchy with polarisation, from the fluid state at the switch"""
    nk = len(kk)
    y0 = np.zeros((nk, NVH))
    y0[:, :NVF] = yF
    tp_sw = float(taup_of(e_sw))
    # ** THE TIGHT-COUPLING VALUES, DERIVED FROM THE HIERARCHY'S OWN QUASI-STATIC LIMIT AND NOT
    # QUOTED. **  Setting the time derivatives and the k-terms to zero in the l = 2 and polarisation
    # equations gives G_0 = Pi/2, G_2 = Pi/10, hence Pi = F_2/(1 - 3/5) = (5/2)F_2, and then
    # 0 = (8/15)theta - tau'(F_2 - Pi/10) = (8/15)theta - (3/4)tau' F_2, so F_2 = (32/45)theta/tau'.
    # *That is sigma_gamma = (16/45)theta/tau', which is the VISC this file has always carried --
    # and 16/45 over the unpolarised 8/27 is 6/5, the same ratio c54.177 measured.*
    F2 = (32.0 / 45.0) * yF[:, 3] / tp_sw
    y0[:, I_TB] = yF[:, 3]
    y0[:, I_FG] = F2
    y0[:, I_GG] = 1.25 * F2
    y0[:, I_GG + 2] = 0.25 * F2

    def rhs(e, Y):
        y = Y.reshape(nk, NVH)
        dc, tc, dg, tg, dn, tn, Ph = (y[:, j] for j in range(7))
        db, tb = y[:, I_DB_], y[:, I_TB]
        Fn = y[:, 7:I_DB_]
        F = y[:, I_FG:I_GG]
        G = y[:, I_GG:]
        Hc, Rb = float(Hl_of(e) if LEAFPERT else Hc_of(e)), float(Rb_of(e))
        PH2 = float(Phi2_of(e))                      # PHASEONLY clock factor (1 unless PHASEONLY)
        Ogv, Onv = float(Og_of(e)), float(On_of(e))
        Ocv, Obv = float(Oc_of(e)), float(Ob_of(e))
        tp = float(taup_of(e))
        sig = Fn[:, 0] / 2
        sgg = F[:, 0] / 2
        Pi = F[:, 0] + G[:, 0] + G[:, 2]
        Ps = Ph - 6 * Hc ** 2 * (Onv * sig + Ogv * sgg) / kk ** 2
        _mat = (Ocv * dc + Obv * db) if BSPLIT else ((Ocv + Obv) * dc)
        _gf = float(Gf_of(e))
        _dsrc = (_gf * (Ogv * dg + Onv * dn) + _mat) if GSRCRAD else _gf * (Ogv * dg + Onv * dn + _mat)
        Php = -Hc * Ps - kk ** 2 * Ph / (3 * Hc) - (Hc / 2) * _dsrc
        out = np.zeros_like(y)
        out[:, 0] = -tc + DRC * 3 * Php
        out[:, 1] = -Hc * tc + DRE * kk ** 2 * Ps
        out[:, 2] = -(4 / 3) * tg + DRC * 4 * Php
        # ** the photon Euler equation now exchanges momentum with the baryons instead of sharing
        # their velocity, and the quadrupole is a STATE and no longer a closure. **
        out[:, 3] = kk ** 2 * (PH2 * dg / 4 - sgg) + DRE * kk ** 2 * Ps + tp * (tb - tg)
        out[:, 4] = -(4 / 3) * tn + DRC * 4 * Php
        out[:, 5] = kk ** 2 * (dn / 4 - sig) + DRE * kk ** 2 * Ps
        out[:, 6] = Php
        out[:, 7] = (8 / 15) * tn - (3 / 5) * kk * Fn[:, 1]
        for i in range(1, LN - 2):
            l = i + 2
            out[:, 7 + i] = kk / (2 * l + 1) * (l * Fn[:, i - 1] - (l + 1) * Fn[:, i + 1])
        out[:, 7 + LN - 2] = kk * Fn[:, LN - 3] - (LN + 1) / e * Fn[:, LN - 2]
        out[:, I_DB_] = -tb + DRC * 3 * Php
        out[:, I_TB] = -Hc * tb + DRE * kk ** 2 * Ps + tp * (tg - tb) / Rb
        # photons: F_2 .. F_LG
        out[:, I_FG] = (8 / 15) * tg - (3 / 5) * kk * F[:, 1] - tp * (F[:, 0] - Pi / 10)
        for i in range(1, LG - 2):
            l = i + 2
            out[:, I_FG + i] = (kk / (2 * l + 1) * (l * F[:, i - 1] - (l + 1) * F[:, i + 1])
                                - tp * F[:, i])
        out[:, I_FG + LG - 2] = kk * F[:, LG - 3] - (LG + 1) / e * F[:, LG - 2] - tp * F[:, LG - 2]
        # polarisation: G_0 .. G_LG
        out[:, I_GG] = -kk * G[:, 1] + tp * (-G[:, 0] + Pi / 2)
        out[:, I_GG + 1] = (kk / 3) * (G[:, 0] - 2 * G[:, 2]) - tp * G[:, 1]
        out[:, I_GG + 2] = (kk / 5) * (2 * G[:, 1] - 3 * G[:, 3]) + tp * (-G[:, 2] + Pi / 10)
        for l in range(3, LG):
            out[:, I_GG + l] = (kk / (2 * l + 1) * (l * G[:, l - 1] - (l + 1) * G[:, l + 1])
                                - tp * G[:, l])
        out[:, I_GG + LG] = kk * G[:, LG - 1] - (LG + 1) / e * G[:, LG] - tp * G[:, LG]
        jac = float(Jac_of(e)) if LEAFPERT else 1.0
        if SRCSTACK in ('vel', 'src') and LEAFPERT:
            # the gravity velocity-source (DRE k^2 Ps, = grad Phi) on the STACK clock; content on leaf
            src = np.zeros_like(out)
            src[:, 1] = DRE * kk ** 2 * Ps
            src[:, 3] = DRE * kk ** 2 * Ps
            src[:, 5] = DRE * kk ** 2 * Ps
            src[:, I_TB] = DRE * kk ** 2 * Ps
            if SRCSTACK == 'src':                       # the whole geometry sector on stack: + Phi's own evolution
                src[:, 6] = Php
                src[:, 0] = DRC * 3 * Php
                src[:, 2] = DRC * 4 * Php
                src[:, 4] = DRC * 4 * Php
                src[:, I_DB_] = DRC * 3 * Php
            return ((out - src) * jac + src).ravel()
        return out.ravel() * jac

    sol = solve_ivp(rhs, [e_sw, ETA_END], y0.ravel(), method='RK45', rtol=RTOL, atol=1e-12,
                    t_eval=t_eval, max_step=(ETA_END - e_sw) / 200)
    if not sol.success:
        raise RuntimeError(f"hierarchy segment failed: {sol.message}")
    return sol


def hier_run(kk, EE, L_A_, D_M_, R_S_):
    """** THE WHOLE HIERARCHY PATH, BATCHED OVER k SO THAT MEMORY IS BOUNDED BY CHOICE. **

    The state is NVH ~ 70 wide instead of the fluid's 20, and storing it for every mode at every
    line-of-sight sample is what would kill this -- 1800 modes x 560 samples x 70 doubles is half a
    gigabyte, and c54.173 already lost a run to exactly this failure with no traceback.  ** C_l is a
    SUM over k, so it batches exactly: each chunk is evolved, projected and discarded. **
    """
    e_sw = eta_switch()
    frac = float(kD2inv_of(e_sw)) / float(kD2inv_of(ETA_LS))
    print(f"  hierarchy: LG = {LG}, handover at tau' = {TCSW}/Mpc (eta = {e_sw:.1f}), where "
          f"{frac:.1%} of 1/k_D^2 has accumulated")
    print(f"  so the envelope carries {frac:.1%} of the damping and the multipoles carry "
          f"{1-frac:.1%} of it")
    # ** PHIHIER=1 (with PHISAVE + PHIQ): the full-range potential Phi(eta) on the HIER COMPOSITION for
    # the selected q-modes -- fluid from ETA_S to the switch (identical to the fluid path there), then
    # the hierarchy from the switch to recombination (the refinement the fluid path lacks).  Closes
    # node 59's fluid-vs-HIER path split for the Phi-decay measurement.  Returns early. **
    if os.environ.get('PHIHIER') == '1' and os.environ.get('PHISAVE'):
        _qt = [float(x) for x in os.environ.get('PHIQ', '1,2,3').split(',')]
        _sk = np.array([kk[int(np.argmin(np.abs(kk * R_S_ / np.pi - q)))] for q in _qt])
        _g1 = np.linspace(ETA_S, e_sw, 300)
        _s1, _, _NVf = evolve(_sk, t_eval=_g1, e_end=e_sw)
        _Y1 = _s1.y.T.reshape(len(_g1), len(_sk), _NVf)
        _g2 = np.linspace(e_sw, eta_rec, 300)
        _Y2 = evolve_hier(_sk, _g2, e_sw, _Y1[-1]).y.T.reshape(len(_g2), len(_sk), NVH)
        _eta = np.concatenate([_g1, _g2[1:]])
        _phi = np.concatenate([_Y1[:, :, 6], _Y2[1:, :, 6]], axis=0).T   # (nsel, neta)
        _a = np.interp(_eta, eg, ag)
        np.savez(os.environ['PHISAVE'], eta=_eta, a=_a, phi=_phi,
                 qpk=_sk * R_S_ / np.pi, kpk=_sk, arm=ARM, eta_rec=eta_rec, eta_s=ETA_S)
        print(f"  PHISAVE-HIER (full range): q={[round(float(k*R_S_/np.pi),2) for k in _sk]} "
              f"-> {os.environ['PHISAVE']}")
        return np.array([100.0]), np.array([0.0])
    ls = np.arange(100, int(LMAXL), int(os.environ.get('LSTEP', '8')))
    x0 = eta_0 - EE
    Cl = np.zeros(len(ls))
    nb = int(os.environ.get('KBATCH', '250'))
    E1 = EE[EE <= e_sw]
    E2 = EE[EE > e_sw]
    for i0 in range(0, len(kk), nb):
        kb = kk[i0:i0 + nb]
        nk = len(kb)
        t1 = np.concatenate([E1, [e_sw]])
        s1, _, NVf = evolve(kb, t_eval=t1, e_end=e_sw)
        Y1 = s1.y.T.reshape(len(t1), nk, NVf)
        s2 = evolve_hier(kb, E2, e_sw, Y1[-1])
        Y2 = s2.y.T.reshape(len(E2), nk, NVH)
        Y = np.zeros((len(EE), nk, NVH))
        Y[:len(E1), :, :NVf] = Y1[:-1]
        Y[:len(E1), :, I_TB] = Y1[:-1, :, 3]            # tightly coupled before the switch
        Y[len(E1):] = Y2
        Cl += _project(kb, EE, Y, ls, x0, e_sw)
        print(f"    modes {i0}-{i0+nk} done", flush=True)
    Dl = Cl * ls * (ls + 1)
    return ls, Dl


def _project(kb, ee, Y, ls, x0, e_sw):
    """the line-of-sight integral with the POLARISATION SOURCE TERMS carried

        S = g (Theta_0 + Psi + Pi/4) + e^-tau (Phi' + Psi')
            + (1/k^2) d/deta [ g theta_b ]  +  (3/4k^2) d^2/deta^2 [ g Pi ]

    with Pi = Theta_2 + Theta^P_0 + Theta^P_2 in the Theta normalisation, i.e. (F_2+G_0+G_2)/4.
    ** The last two terms are what an exp(-k^2/k_D^2) envelope cannot supply at any coefficient. **
    """
    Hcv = np.array([Hc_of(e) for e in ee])[:, None]
    Onv = np.array([On_of(e) for e in ee])[:, None]
    Ogv = np.array([Og_of(e) for e in ee])[:, None]
    sgn = Y[:, :, 7] / 2
    sgg = Y[:, :, I_FG] / 2
    Ph = Y[:, :, 6]
    Ps = Ph - 6 * Hcv ** 2 * (Onv * sgn + Ogv * sgg) / kb[None, :] ** 2
    g_ = vis_of(ee)[:, None]
    et = np.exp(-tau_of(ee))[:, None]
    # ** the envelope, FROZEN AT THE SWITCH. **  It covers [start, eta_sw] and nothing after, and
    # the hierarchy covers [eta_sw, end] and nothing before.  Disjoint supports, so the double count
    # that cost c54.175 a revision cannot occur here even in principle.
    D = np.exp(-(kb[None, :] ** 2) * kD2inv_of(np.minimum(ee, e_sw))[:, None])
    Th0 = Y[:, :, 2] / 4 * D
    Pi = (Y[:, :, I_FG] + Y[:, :, I_GG] + Y[:, :, I_GG + 2]) / 4 * D
    tb = Y[:, :, I_TB] * D
    # ** PISRC=0 KEEPS THE HIERARCHY AND DROPS ONLY THE POLARISATION SOURCE TERMS. **  That is the
    # control for c54.177's claim that an envelope has "the half that removes power and not the half
    # that returns it": with PISRC=0 this transfer has exactly the half an envelope has, computed
    # dynamically, so the difference between the two runs IS the returned half and nothing else.
    _PI = float(os.environ.get('PISRC', '1'))
    S = (g_ * (Th0 + Ps + _PI * Pi / 4)
         + et * (np.gradient(Ph, ee, axis=0) + np.gradient(Ps, ee, axis=0))
         + np.gradient(g_ * tb, ee, axis=0) / kb[None, :] ** 2
         + _PI * 0.75 * np.gradient(np.gradient(g_ * Pi, ee, axis=0), ee, axis=0)
         / kb[None, :] ** 2)
    dk = np.gradient(kb)
    P = kb ** (0.965 - 1) / kb * dk
    out = np.empty(len(ls))
    for j, l in enumerate(ls):
        J = spherical_jn(int(l), kb[None, :] * x0[:, None] * PROJMAP)
        out[j] = np.sum(P * np.trapezoid(S * J, ee, axis=0) ** 2)
    return out


def main():
    if os.environ.get('QSCAN', '0') == '1':
        return qscan()
    stretch = 2.750
    # ** KCONT=1 replaces the CR arm's DISCRETE ladder with a dense continuum sampling. **  For CR
    # the ladder k_L = sqrt(L(L+2))/r_0 is PHYSICAL -- the sum is the object, not an approximation
    # to an integral -- so its coarseness is not aliasing.  But that is a claim, and running the
    # same arm both ways is what turns it into a measurement: if the peak position is the same,
    # discreteness is not what sets it, and the driving is.
    if ARM == 'cr' and os.environ.get('KCONT', '0') != '1':
        Ls = np.arange(2, int((LMAXL + 400) / stretch) + 2)
        lL = np.sqrt(Ls * (Ls + 2)) * stretch
    else:
        lL = np.linspace(12.0, LMAXL, NK * 3)
    lL = lL[lL <= LMAXL]
    if len(lL) > NK * 3:
        lL = lL[:: max(1, len(lL) // (NK * 3))]
    kk = lL / D_M

    print()
    print("=" * 78)
    print(f"  ACOUSTIC TWO-ARM INSTRUMENT — ARM={ARM}   DRIVING={'OFF (guard)' if NODRIVE else 'ON'}")
    print("=" * 78)
    print(f"  rate: {'radiation-INCLUDED' if RAD_IN_RATE else 'radiation-FREE (L1)'}   "
          f"H0={H0}  Om={OM}")
    print(f"  z_start = {Z_START:.4g}   eta_start = {ETA_S:.3f}   eta_rec = {eta_rec:.1f}   "
          f"eta_end = {ETA_END:.0f}")
    print(f"  D_M = {D_M:.0f} Mpc   r_s = {R_S:.2f} Mpc   l_A = pi D/r_s = {L_A:.1f}   "
          f"modes = {len(kk)}")
    print()

    if os.environ.get('LOS', '1') == '1':
        # the line-of-sight grid is known in advance, so ask the integrator for exactly it
        # ** two-scale sampling: the visibility window carries all the fast structure and gets the
        # points; past it only the ISW survives and it is smooth. **  A single uniform grid over
        # eta = 54-4000 spent most of its samples where the source is identically zero.
        n_los = int(os.environ.get('NLOS', '560'))
        e_lo = max(ETA_S + 1e-6, ETA_LS - 6.0 * ETA_LS_W)
        e_hi = ETA_LS + 6.0 * ETA_LS_W
        EE = np.concatenate([np.linspace(e_lo, e_hi, int(0.75 * n_los), endpoint=False),
                             np.linspace(e_hi, ETA_END, n_los - int(0.75 * n_los))])
        if not alias_gate(kk):
            return 1
        if os.environ.get('HIER', '0') == '1':
            ls, Dl = hier_run(kk, EE, L_A, D_M, R_S)
            if os.environ.get('SAVE'):
                np.savez(os.environ['SAVE'], ls=ls, Dl=Dl, l_A=L_A, D_M=D_M, r_s=R_S, arm=ARM)
                print(f"  saved {len(ls)} multipoles to {os.environ['SAVE']}")
            pk = [q for q in argrelextrema(Dl, np.greater, order=3)[0]]
            print("  " + "-" * 74)
            print(f"  PEAKS (line-of-sight, HIERARCHY)   l_A = {L_A:.1f}")
            print("  " + "-" * 74)
            print(f"    peaks at l = {[int(ls[q]) for q in pk[:4]]}")
            if len(pk) >= 3:
                print(f"    l_1/l_A = {ls[pk[0]]/L_A:.4f}   P1/P2 = {Dl[pk[0]]/Dl[pk[1]]:.3f}   "
                      f"P1/P3 = {Dl[pk[0]]/Dl[pk[2]]:.3f}")
            print(f"    sky: 220.6 / 538.1 / 809.8,  l_1/l_A = {220.6/301.7:.4f},  "
                  f"P1/P2 = 2.217,  P1/P3 = 2.277")
            return 0
        sol, nk, NV = evolve(kk, t_eval=EE)
        Yl = sol.y.T.reshape(len(EE), nk, NV)
        return los_spectrum(kk, EE, Yl, L_A, D_M, R_S)
    sol, nk, NV = evolve(kk)
    yr = sol.sol(eta_rec).reshape(nk, NV)
    sig = yr[:, 7] / 2
    Psr = yr[:, 6] - 6 * Hc_of(eta_rec) ** 2 * On_of(eta_rec) * sig / kk ** 2
    SW = yr[:, 2] / 4 + Psr
    TH0 = yr[:, 2] / 4                                   # the oscillator alone

    # ** PHISAVE: the potential Phi(eta) for the first three acoustic-peak modes (58's envelope test
    # of branch C).  Does the potential decay with the k-dependent phase that produces the odd-even
    # alternation, or smoothly?  A field the ODE already carries (state index 6), no new run. **
    if os.environ.get('PHISAVE'):
        # ** PHIQ=1,2,3 selects modes at FIXED acoustic phase q = k r_s/pi (same number of
        # half-periods by recombination on BOTH arms) so Phi's decay-per-half-period is a MATCHED
        # comparison; without it, the arm's own peak modes are used (which differ in k between arms). **
        _phiq = os.environ.get('PHIQ')
        if _phiq:
            _qt = [float(x) for x in _phiq.split(',')]
            _pk = np.array([int(np.argmin(np.abs(kk * R_S / np.pi - q))) for q in _qt])
        else:
            _pk = argrelextrema(np.abs(TH0), np.greater, order=4)[0]
            _pk = _pk[(kk[_pk] * R_S / np.pi < 5)][:4]    # first four peak modes
        _etg = np.linspace(ETA_S, eta_rec, 500)
        _Yg = sol.sol(_etg).reshape(nk, NV, len(_etg))    # (nk, NV, neta)
        _clock = np.asarray(Jac_of(_etg), dtype=float) + np.zeros_like(_etg)  # phi(eta)=Jac (const if frozen)
        _ag = np.interp(_etg, eg, ag)                     # scale factor a(eta) -- common variable across arms
        np.savez(os.environ['PHISAVE'], eta=_etg, a=_ag, phi=_Yg[_pk, 6, :], dg=_Yg[_pk, 2, :],
                 tg=_Yg[_pk, 3, :], clock=_clock,
                 qpk=kk[_pk] * R_S / np.pi, kpk=kk[_pk], arm=ARM, eta_rec=eta_rec, eta_s=ETA_S)
        print(f"  PHISAVE: Phi(eta) for peak modes q={[round(float(kk[j]*R_S/np.pi),2) for j in _pk]} "
              f"-> {os.environ['PHISAVE']}")

    # ---- THE COMB, ON SOURCE EXTREMA IN k -------------------------------------------------------
    print("  " + "-" * 74)
    print("  THE COMB — source extrema in k, at recombination.  NEVER measured in ell-space.")
    print("  " + "-" * 74)
    for label, S in (("SW = dg/4 + Psi", SW), ("Theta_0 = dg/4", TH0)):
        idx = argrelextrema(np.abs(S), np.greater, order=4)[0]
        q = kk[idx] * R_S / np.pi
        q = q[q < 6]
        print(f"    {label:>16}: " + "  ".join(f"{x:.4f}" for x in q[:6]))
        if len(q) >= 3:
            d = np.diff(q)
            print(f"    {'spacing':>16}: " + "  ".join(f"{x:.4f}" for x in d[:5])
                  + f"      mean {np.mean(d):.4f}")
    print()
    if NODRIVE:
        idx = argrelextrema(np.abs(TH0), np.greater, order=4)[0]
        q = kk[idx] * R_S / np.pi
        q = q[q < 6]
        print("  ** THE GUARD: undriven, these must be the integers. **")
        print(f"     got {[round(float(x), 4) for x in q[:5]]}")
        if len(q):
            dev = max(abs(float(x) - round(float(x))) for x in q[:5])
            print(f"     worst departure from an integer: {dev:.4f}")
        return 0

    # ---- projection --------------------------------------------------------------------------
    if os.environ.get('NOPROJ', '0') == '1':
        return 0
    DP = yr[:, 3] / kk



    # ** THE PROJECTION MUST RESOLVE THE BESSEL OSCILLATION IN k, WHICH HAS PERIOD 2 pi / D. **
    #    The first run of this file sampled k more coarsely than that and the projected spectrum
    #    aliased into a comb of spacing ~40 in ell while the SOURCE comb was correct to 1.5%.
    #    ** That is exactly why the comb is measured on source extrema and not in ell-space. **
    dk_need = 2.0 * np.pi / D_M
    dk_have = float(np.median(np.diff(kk)))
    print(f"  projection sampling: dk = {dk_have:.3e}, Bessel period 2pi/D = {dk_need:.3e}, "
          f"points per period = {dk_need/dk_have:.1f}")
    if dk_need / dk_have < 4.0:
        if ARM == 'cr' and os.environ.get('KCONT', '0') != '1':
            print("  ⌗ CR's ladder is DISCRETE and physical, so this is not aliasing — but it is")
            print("    only not aliasing if the answer does not depend on it. Run KCONT=1 to check.")
        else:
            print("  ⛔ UNDER-SAMPLED — raise NK; the projected peaks below would be aliasing.")
            return 1
    ee = np.linspace(eta_rec, ETA_END, 24)
    Yg = np.array([sol.sol(e).reshape(nk, NV) for e in ee])
    Phg, sgg = Yg[:, :, 6], Yg[:, :, 7] / 2
    Hcv = np.array([Hc_of(e) for e in ee])[:, None]
    Onv = np.array([On_of(e) for e in ee])[:, None]
    Psg = Phg + 6 * Hcv ** 2 * Onv * sgg / kk[None, :] ** 2
    IS = np.gradient(Phg, ee, axis=0) + np.gradient(Psg, ee, axis=0)        # (n_ee, nk)
    rD = float(os.environ.get('RD', '5.5' if ARM == 'lcdm' else '10.88'))
    damp = np.exp(-(kk * rD) ** 2)
    SWd, DPd = SW * damp, DP * damp
    dk = np.gradient(kk)
    P = kk ** (0.965 - 1) / kk * dk
    x = kk * D_M
    xi = kk[None, :] * (eta_0 - ee)[:, None]                               # (n_ee, nk)
    ls = np.arange(100, int(LMAXL), 4)
    Cl = np.empty(len(ls))
    DO_ISW = os.environ.get('NOISW', '0') != '1'
    for j, l in enumerate(ls):
        Dt = SWd * spherical_jn(int(l), x) + DPd * spherical_jn(int(l), x, derivative=True)
        if DO_ISW:
            Dt = Dt + np.trapezoid(IS * spherical_jn(int(l), xi), ee, axis=0)
        Cl[j] = np.sum(P * Dt ** 2)
    Dl = Cl * ls * (ls + 1)
    # ** SAVE for the likelihood (c54.172).  The normalisation is arbitrary here -- the amplitude is
    # one fitted parameter downstream, exactly as A_s is -- so what is banked is the SHAPE. **
    if os.environ.get('SAVE'):
        np.savez(os.environ['SAVE'], ls=ls, Dl=Dl, l_A=L_A, D_M=D_M, r_s=R_S, arm=ARM)
        print(f"  saved {len(ls)} multipoles to {os.environ['SAVE']}")
    pk = [q for q in argrelextrema(Dl, np.greater, order=3)[0]]
    print("  " + "-" * 74)
    print(f"  PEAKS   l_A = {L_A:.1f}")
    print("  " + "-" * 74)
    print(f"    peaks at l = {[int(ls[q]) for q in pk[:4]]}")
    if len(pk) >= 3:
        print(f"    l_1/l_A = {ls[pk[0]]/L_A:.4f}   P1/P2 = {Dl[pk[0]]/Dl[pk[1]]:.3f}   "
              f"P1/P3 = {Dl[pk[0]]/Dl[pk[2]]:.3f}")
    print(f"    sky: 220.6 / 538.1 / 809.8,  l_1/l_A = {220.6/301.7:.4f},  "
          f"P1/P2 = 2.217,  P1/P3 = 2.277")
    return 0


if __name__ == '__main__':
    sys.exit(main())
