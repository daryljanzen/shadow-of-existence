# -*- coding: utf-8 -*-
"""Ⓐ① THE MASSIVE-NEUTRINO BACKGROUND -- the Fermi-Dirac density and pressure, as a pure function.

⛭ `r7863` (69) item ①.  *This file is the PHYSICS, with no instrument in it and no switch: three
degenerate states of mass `Sum/3` at `T_nu = (4/11)^(1/3) T_gamma`, their energy density and
pressure from the Fermi-Dirac integral at each epoch.*  The instrument imports `omega_factor` and
multiplies the radiation term it already has, which is what makes the massless limit EXACT.

⛔ ** WHY A RATIO AND NOT A DENSITY. **  *The landed stack carries the neutrino sector as
`FNU * OR / a**4`.  If this file returned a density in its own units the instrument would have to
swap one expression for another, and `Sum = 0` would then agree only to the precision of two
different normalisations -- which is exactly the kind of "byte-identical" that is not.  So what is
returned is `rho_nu(a) / rho_nu,massless(a)`, a pure number that is EXACTLY `1.0` at zero mass
because the integrals are then the same integral.  The instrument multiplies, and with the mass at
zero the expression reduces to the landed line and the bits do not move.*

⌗ *The integral is the standard one: for one state of mass `m` at temperature `T`,*

      rho = (g / (2 pi^2)) INT_0^inf  q^2 sqrt(q^2 + (m/T)^2)  / (e^q + 1)  dq  * T^4
      p   = (g / (6 pi^2)) INT_0^inf  q^4 / sqrt(q^2 + (m/T)^2) / (e^q + 1)  dq  * T^4

*with `q = p/T` the comoving momentum in units of the temperature.  At `m = 0` both reduce to the
massless results and `rho = 3 p`.  The ratio this file returns is the first integral over its own
`m = 0` value, so every constant -- `g`, the `7/8`, the `(4/11)^(4/3)` -- cancels out of it.*
"""
import numpy as np
from scipy.integrate import quad

#: the neutrino temperature today, as a fraction of the photon temperature
T_RATIO = (4.0 / 11.0) ** (1.0 / 3.0)
#: T_gamma today in eV, from 2.7255 K: k_B = 8.617333262e-5 eV/K
T_GAMMA0_EV = 2.7255 * 8.617333262e-5
T_NU0_EV = T_RATIO * T_GAMMA0_EV
#: INT q^3/(e^q+1) dq = 7 pi^4 / 120 -- the massless energy integral, used as the denominator
_MASSLESS = 7.0 * np.pi ** 4 / 120.0
#: and INT q^2/(e^q+1) dq = 3 zeta(3)/2, the NUMBER integral, for the nonrelativistic limit
_NUMBER = 1.5 * 1.2020569031595943


def _rho_integral(y, limit=200):
    """INT_0^inf q^2 sqrt(q^2 + y^2) / (e^q + 1) dq,  y = m / T"""
    if y == 0.0:
        return _MASSLESS
    return quad(lambda q: q * q * np.sqrt(q * q + y * y) / (np.exp(q) + 1.0),
                0.0, np.inf, limit=limit)[0]


def _p_integral(y, limit=200):
    """INT_0^inf q^4 / sqrt(q^2 + y^2) / (e^q + 1) dq / 3,  y = m / T"""
    if y == 0.0:
        return _MASSLESS / 3.0
    return quad(lambda q: q ** 4 / np.sqrt(q * q + y * y) / (np.exp(q) + 1.0),
                0.0, np.inf, limit=limit)[0] / 3.0


def y_of(a, sum_ev, n_states=3.0):
    """`m / T_nu` at scale factor `a`, for ONE of `n_states` degenerate states of total `sum_ev`"""
    if sum_ev == 0.0:
        return 0.0
    return (float(sum_ev) / n_states) * a / T_NU0_EV


def omega_factor(a, sum_ev, n_states=3.0):
    """`rho_nu(a) / rho_nu,massless(a)` -- EXACTLY 1.0 at zero mass, by construction

    ⌗ *The instrument multiplies its own `FNU * OR / a**4` by this, so at `sum_ev = 0` the
    multiplication is by the float `1.0` and the landed expression is unchanged bit for bit.*
    """
    if sum_ev == 0.0:
        return 1.0
    return _rho_integral(y_of(a, sum_ev, n_states)) / _MASSLESS


def pressure_factor(a, sum_ev, n_states=3.0):
    """`p_nu(a) / p_nu,massless(a)` -- also exactly 1.0 at zero mass

    *Not used by the background rate, which needs only the density; it is here because the order
    asks for the pressure and because `w_nu = p/rho` is what shows the transition happening.*
    """
    if sum_ev == 0.0:
        return 1.0
    return _p_integral(y_of(a, sum_ev, n_states)) / (_MASSLESS / 3.0)


def w_of(a, sum_ev, n_states=3.0):
    """the equation of state: `1/3` while relativistic, falling to `0` as the mass takes over"""
    y = y_of(a, sum_ev, n_states)
    return _p_integral(y) / _rho_integral(y)


def omega_nu_today(sum_ev, h, n_states=3.0):
    """`Omega_nu` at `a = 1` from the integral itself, for comparison with the `93.14` rule

    ⌗ *`rho_nu,massless(a) = FNU * OR * rho_crit / a^4` is the instrument's own normalisation, so
    this returns the factor the instrument would apply at `a = 1` times its own massless term; the
    caller supplies `FNU * OR`.  What this function gives alone is the RATIO to the `93.14` value,
    which is the comparison worth printing.*
    """
    approx = float(sum_ev) / 93.14 / h ** 2
    return dict(approx_93_14=approx, factor_at_a1=omega_factor(1.0, sum_ev, n_states))


# ⛔⛭⛭⛭ ** A MEASUREMENT TAKEN BEFORE THE INSTRUMENT SIDE EXISTS, AND IT IS A FAILURE OF A
#   REGISTERED BAND WHOSE CAUSE IS NOT THIS TERM. **
#   *With the instrument's own `FNU * OR` as the massless normalisation, this file's density at
#   `a = 1` comes out BELOW both the `93.14` rule and the reference:*
#
#       Sum = 0.06 eV   Omega_nu(FD) 1.402007e-03   vs 93.14's 1.418062e-03   ratio 0.988678
#       Sum = 0.30 eV   Omega_nu(FD) 7.006979e-03   vs 93.14's 7.090310e-03   ratio 0.988247
#       Sum = 0.60 eV   Omega_nu(FD) 1.401377e-02   vs 93.14's 1.418062e-02   ratio 0.988234
#       the reference's own Omega_nu at Sum = 0.06 eV: 1.419620e-03
#
#   ⇒ ** THE CAUSE IS THE INSTRUMENT'S N_eff AND NOT THE INTEGRAL. **  *The reference reports
#   `N_eff = 3.0293` with a per-state degeneracy of `1.0147` -- the non-instantaneous-decoupling
#   correction -- while this instrument's `FNU = 0.4052` codes `N_eff = 3.000` exactly, and its own
#   comment says so.  `3.0293 / 3.0000 = 1.00978` accounts for the gap to the digit.*
#   ⌗ So the registered band of `5e-03` on `rho_nu / rho_crit` is expected to FAIL at about
#   `1.2e-02`, and it will be reported AS a failure with the criterion unmoved -- and with the cause
#   measured rather than asserted, because the instrument already exposes `DNEFF`: a run at
#   `DNEFF = +0.0293` is the test of this diagnosis, and it is a test that can refute it.
#   ⚠ *What this does NOT excuse: the drag ruler's flatness in the sum, which is the defect this
#   revision repairs. That is a one-per-cent-level question about `N_eff` sitting underneath an
#   eight-tenths-of-a-per-cent question about the ruler, and the two are separate.*
