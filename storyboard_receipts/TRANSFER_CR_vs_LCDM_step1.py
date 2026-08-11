"""TRANSFER_CR_vs_LCDM  (r2344 work, step 1 of the localisation done properly)

The question: the T(k) deficit at k~0.08 is 3.8-5.6% with a 1.7% log-slope error, and it is
transfer-era (r2344).  Is it a PHASE effect (the sound horizon differing) or an AMPLITUDE effect?

The CAMB-parameter proxy could not answer this, because every CAMB parameter moves several things
at once and none of them reproduces CR's rate change.  So: run ONE integrator on TWO backgrounds,
with a switch, so the differences can be turned on independently.

TWO differences between the backgrounds, and they are separable:
  (1) THE RATE     -- CR has NO radiation term in H; LambdaCDM does.
  (2) THE START    -- CR begins at eta_onset (the plasma's onset); LambdaCDM at eta -> 0.

This file builds the background halves and checks them against known numbers before any
perturbation is evolved.  Nothing is claimed from it yet.
"""
import numpy as np
from scipy.integrate import quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

c = 299792.458
H0 = 67.4                       # the directly measured value the corpus uses for the CR runs
Om = 0.3150
OL = 1 - Om
ombh2 = 0.02237
z_rec = 1089.9
a_rec = 1 / (1 + z_rec)
h = H0 / 100
Or = 4.15e-5 / h**2             # omega_r fixed by T_CMB
Rb_rec = 31500 * ombh2 / (2.7255 / 2.7) ** 4 / (1 + z_rec)


def background(with_radiation):
    """Return (a-grid, eta-grid, H(a), and the species fractions) for one background.

    with_radiation=False  -> CR: H^2 = H0^2 (Om a^-3 + OL), radiation is CONTENT not SOURCE
    with_radiation=True   -> LambdaCDM: the usual, radiation in the rate
    """
    if with_radiation:
        Hub = lambda a: H0 * np.sqrt(Or / a**4 + Om / a**3 + OL)
    else:
        Hub = lambda a: H0 * np.sqrt(Om / a**3 + OL)
    ag = np.logspace(-5, 0, 14000)
    eg = np.concatenate([[0.0], cumulative_trapezoid(c / (ag**2 * Hub(ag)), ag)])
    return ag, eg, Hub


def sound_horizon(Hub, z_from, z_to=z_rec):
    """r_s = int c_s / H  da/(a^2 H), from z_from down to recombination."""
    integrand = lambda a: c / (a**2 * Hub(a) * np.sqrt(3 * (1 + Rb_rec * a / a_rec)))
    return quad(integrand, 1 / (1 + z_from), a_rec, limit=250)[0]


print("=" * 78)
print("BACKGROUND HALVES, checked before any perturbation is evolved")
print("=" * 78)

for lab, wr in (("LambdaCDM (radiation in the rate)", True),
                ("CR        (radiation-free rate)  ", False)):
    ag, eg, Hub = background(wr)
    a_rec_eta = float(np.interp(a_rec, ag, eg))
    eta0 = eg[-1]
    DM = eta0 - a_rec_eta
    print()
    print("  %s" % lab)
    print("     conformal time to recombination : %.2f Mpc" % a_rec_eta)
    print("     comoving distance D_M           : %.1f Mpc" % DM)
    # matter-radiation equality, where it exists as a rate feature
    if wr:
        zeq = Om / Or - 1
        print("     z_eq (from the rate)            : %.0f" % zeq)
    else:
        print("     z_eq (from the rate)            : none -- radiation is not in the rate")

print()
print("=" * 78)
print("THE SOUND HORIZON, and where the two accounts part")
print("=" * 78)
ag_l, eg_l, Hub_l = background(True)
ag_c, eg_c, Hub_c = background(False)

# LambdaCDM: the integral converges from below, so z_from -> large
rs_lcdm = sound_horizon(Hub_l, 1e7)
print()
print("  LambdaCDM, integrated from z -> 1e7 :  r_s = %.2f Mpc" % rs_lcdm)

# CR: the integral needs a lower limit -- z_onset -- because the rate carries no radiation
print("  CR, needs a starting redshift (the rate carries no radiation):")
for z_on in (3000, 5000, 6797, 10000, 1e5):
    print("     z_onset = %-8.0f ->  r_s = %.2f Mpc" % (z_on, sound_horizon(Hub_c, z_on)))

print()
print("  ^ this is the one fitted parameter: z_onset is set by matching the acoustic ANGLE,")
print("    and the corpus's value is ~6797, giving r_s near the measured 144-147 Mpc.")
print()
print("NOTHING IS CLAIMED HERE.  The backgrounds are built and checked; the perturbation")
print("evolution on each, and the delta_c comparison, is the next step.")
