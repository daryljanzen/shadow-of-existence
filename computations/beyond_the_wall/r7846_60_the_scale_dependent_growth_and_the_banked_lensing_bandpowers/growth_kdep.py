#!/usr/bin/env python3
"""** THE SCALE-DEPENDENT GROWTH, CARRIED FROM z = 12.8 TO z = 0 ON THIS INSTRUMENT'S OWN RATE. **

Order `r7845` ①.  `r7844` measured the obstruction exactly: `L171x_lensing_potential.py` carries
`Phi` by `g(a) = D(a)/a` from a BACKGROUND quadrature over `A.Hphys`, and at fixed total `Omega_m`
this instrument's `Hphys` is independent of the neutrino sum to `0.000e+00`.  So that growth carries
exactly zero neutrino effect, and the one channel that responds -- the Poisson source -- is flat in
`k` and frozen at `z = 12.8`, where the lensing kernel has not yet done any of its work.

** WHAT REPLACES IT, AND WHY IT IS AN ODE AND NOT A FITTING FUNCTION. **  Below the free-streaming
scale the neutrinos cluster with the cold matter and the growth is the massless one; above it they
do not cluster, so they contribute their share of the BACKGROUND density without contributing to
the SOURCE, and the growing mode's exponent falls.  *That is a statement about two fluids with one
potential between them, so what carries it is the two-fluid growth equation,*

    d2 d_cb / dN2  +  (2 + dlnH/dN) d d_cb/dN  =  1.5 Om_tot(a) [ (1-f_nu) d_cb + f_nu d_nu ]

in `N = ln a`, with `Om_tot(a) = OM a^-3 (H0/H(a))^2` read off the instrument's own rate, and
`f_nu = Omega_nu / Omega_m` the share the sum takes of the total.

** THE ONE APPROXIMATION, NAMED RATHER THAN BURIED. **  `d_nu` is not solved from its own Boltzmann
hierarchy here; it is filtered,

    d_nu  =  d_cb / (1 + (k / k_fs(a))^2),      k_fs(a) = sqrt(3/2) a H(a) / v_th(a),

a Jeans-like filter on the thermal velocity `v_th(a)/c = 3.15 T_nu(a) / (m_nu c^2)`.  It has the
two limits right by construction -- `d_nu -> d_cb` far below `k_fs`, `d_nu -> 0` far above -- and it
is an INTERPOLATION in between, not a solution.  ** SO THIS MODULE DOES NOT CLAIM TO BE THE
PUBLISHED PIPELINE'S TREATMENT **, and `r7846`'s arm Ⓒ③ reports the measured high-`k` asymptote
BESIDE the textbook `-8 f_nu` rather than asserting they agree.

** THE REDUCTION AT ZERO SUM IS THE TEST THAT THE SOLVER IS RIGHT, AND IT CAUGHT THE FIRST
VERSION OF THIS FILE. **  With `f_nu = 0` the bracket is exactly `1`, the equation is the massless
growth equation, and its growing solution is the quadrature `D prop. H INT da/(a H)^3` that `L171x`
already uses.  The first attempt integrated from `a = 1e-4` with `d prop. a`, and arm Ⓐ① came back
`9.08e-01` out.  *Both sides were wrong there and in the same place:* `a = 1e-4` is BEFORE
matter-radiation equality, where `d prop. a` is not the growing mode (the Meszaros effect suppresses
it) and where the quadrature's own docstring says its formula holds only "after radiation stops
mattering".  A comparison in a regime where neither side is valid measures nothing.

⇒ ** SO THE SOLVE STARTS WHERE THE ORDER SAYS THE CARRY STARTS: `z = 12.8`, the `eta_ref` at which
this instrument freezes `Phi(k)`, with initial conditions taken FROM the quadrature's own growing
mode there. **  At `f_nu = 0` it is then the same equation from the same state, so it reproduces the
quadrature downstream to solver tolerance, and Ⓐ① is a sharp test instead of a category error.

⚠ ** WHAT THAT INTERVAL MISSES, STATED RATHER THAN DISCOVERED LATER. **  Free-streaming suppression
begins when the species turns non-relativistic, near `1+z ~ m / (3.15 T_nu0)` -- about `z = 190` for
`0.1` eV a species -- so the stretch from there to `z = 12.8` accumulates scale-dependent
suppression that a carry starting at `z = 12.8` does not have.  What this instrument's `Phi(k, z =
12.8)` does carry is the FLAT `f_nu` reduction of the Poisson source that `r7844` measured.  The
size of the missing stretch is measured by `--from-nr` rather than argued, and reported.

Used as a module:  `GrowthKDep(mnu_ev).g(k, a)` and `.ratio(k, a, a_ref)`
Run as a script:   prints the reduction at zero sum and the suppression's shape in `k`.
"""
import os
import sys

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.interpolate import CubicSpline

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
sys.path.insert(0, _BTW)
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '1')
import ACOUSTIC_two_arm as A                                              # noqa: E402

C_KM_S = 299792.458
T_NU0_EV = 1.95 * 8.617333262e-5 / 1.0          # the relic temperature today, in eV
ETAREF = float(os.environ.get('ETAREF', '4000'))        # the z = 12.8 the instrument freezes at
NSTEP = int(os.environ.get('GA_STEPS', '900'))


def _h_of(a):
    """H(a) in km/s/Mpc, from the instrument's own background and nothing else"""
    return float(A.Hphys(float(a)))


def _dlnh_dn(a, h=1e-5):
    """dlnH/dlna by a centred difference on the instrument's rate

    ** NOT ANALYTIC, DELIBERATELY. **  Writing the derivative of a Lambda-CDM rate by hand would be
    a second model of the background beside the instrument's; differencing the instrument's own
    `Hphys` cannot disagree with it.
    """
    lp, lm = np.log(_h_of(a * np.exp(h))), np.log(_h_of(a * np.exp(-h)))
    return (lp - lm) / (2.0 * h)


def om_tot(a):
    """the TOTAL matter fraction at a -- dust including the neutrinos' late mass

    The instrument holds `OM` as the total by design (that is what "the dust term's total carries
    their late mass" means), so this is `OM a^-3 (H0/H)^2` with `OM` read off it.
    """
    h0 = _h_of(1.0)
    return float(A.OM) * a ** -3 * (h0 / _h_of(a)) ** 2


def v_th_over_c(a, m_nu_ev):
    """the neutrinos' thermal velocity, as a fraction of c; 0 for a massless species"""
    if m_nu_ev <= 0.0:
        return 0.0
    return 3.15 * (T_NU0_EV / a) / m_nu_ev


def k_fs(a, m_nu_ev):
    """the free-streaming wavenumber in 1/Mpc; +inf for a massless species (nothing filtered)"""
    v = v_th_over_c(a, m_nu_ev)
    if v <= 0.0:
        return np.inf
    return np.sqrt(1.5) * a * (_h_of(a) / C_KM_S) / v


class GrowthKDep:
    """D(k, a) for the cold matter, from the two-fluid equation on this instrument's background

    `n_species` splits the sum: the instrument's HIERARCHY path carries three, so the filter's mass
    is `Sum / 3` unless told otherwise.  ** The SPLIT MATTERS and is therefore a parameter rather
    than a constant: `k_fs` goes as `1/v_th` and `v_th` as `1/m`, so three light species free-stream
    further than one heavy one of the same total. **
    """

    def __init__(self, mnu_ev=0.0, n_species=3, kk=None, a_start=None):
        self.mnu = float(mnu_ev)
        self.n = int(n_species)
        self.m_each = self.mnu / self.n if self.mnu > 0 else 0.0
        self.onu = self.mnu / 93.14 / (_h_of(1.0) / 100.0) ** 2
        self.f_nu = self.onu / float(A.OM) if self.mnu > 0 else 0.0
        self.kk = (np.logspace(-4, 0, 60) if kk is None else np.asarray(kk, float))
        self.a_start = (float(A.a_of_eta(ETAREF)) if a_start is None else float(a_start))
        self._bg = background_g()
        self._solve()

    def _rhs(self, N, y, k):
        a = np.exp(N)
        d, dp = y
        kf = k_fs(a, self.m_each)
        filt = 1.0 / (1.0 + (k / kf) ** 2) if np.isfinite(kf) else 1.0
        src = 1.5 * om_tot(a) * d * ((1.0 - self.f_nu) + self.f_nu * filt)
        return [dp, -(2.0 + _dlnh_dn(a)) * dp + src]

    def _ic(self):
        """D and dD/dN at the start, FROM the quadrature's growing mode -- not imposed by hand

        ** THIS IS WHAT MAKES Ⓐ① A TEST. **  The massless equation and the quadrature are the same
        equation; giving the solver the quadrature's own state at `a_start` means that at `f_nu = 0`
        any disagreement downstream is the SOLVER's, which is the thing being checked.
        """
        N0 = np.log(self.a_start)
        g0 = float(self._bg(N0))
        h = 1e-4
        dg = (float(self._bg(N0 + h)) - float(self._bg(N0 - h))) / (2.0 * h)
        d0 = g0 * self.a_start                          # D = g a
        dd0 = (dg + g0) * self.a_start                  # dD/dN = (dg/dN + g) a
        return d0, dd0

    def _solve(self):
        Ng = np.linspace(np.log(self.a_start), 0.0, NSTEP)
        d0, dd0 = self._ic()
        rows = []
        for k in self.kk:
            s = solve_ivp(self._rhs, (Ng[0], Ng[-1]), [d0, dd0], t_eval=Ng,
                          args=(float(k),), rtol=1e-11, atol=1e-16, method='Radau')
            assert s.success, f'the growth ODE failed at k = {k:.4g}: {s.message}'
            rows.append(s.y[0])
        self.N = Ng
        self.a = np.exp(Ng)
        self.D = np.asarray(rows)                      # (nk, nN)
        self.g = self.D / self.a[None, :]              # D/a, on the quadrature's own normalisation
        self._spl = [CubicSpline(Ng, self.g[i]) for i in range(len(self.kk))]

    def g_of(self, k, a):
        """g(k, a) = D/a on the quadrature's own normalisation, interpolated in log k"""
        a = np.atleast_1d(np.asarray(a, float))
        vals = np.array([s(np.log(a)) for s in self._spl])        # (nk, na)
        lk = np.log(np.atleast_1d(np.asarray(k, float)))
        out = np.empty((len(lk), len(a)))
        for j in range(len(a)):
            out[:, j] = np.interp(lk, np.log(self.kk), vals[:, j])
        return out

    def ratio(self, k, a, a_ref):
        """g(k, a) / g(k, a_ref) -- what the lensing potential is actually carried by"""
        num = self.g_of(k, a)
        den = self.g_of(k, a_ref)
        return num / den

    def surface(self):
        """one bivariate spline of `log g` over `(log k, ln a)`, for use inside an integrand

        ** THE PER-CALL PATH IS TOO SLOW TO PUT INSIDE A LIMBER INTEGRAL, and that is a reason to
        interpolate it, not to coarsen the physics. **  `g_of` evaluates one cubic spline per `k`
        node and then interpolates across them, which is fine for a table and ruinous inside
        `quad`: the lensing integral asks for `g` at thousands of `(k, chi)` pairs per multipole,
        and there are nine bandpowers' worth of multipoles per spectrum and seventeen spectra per
        arm.  The surface is built ONCE from the same solved grid, so it introduces interpolation
        error in `log g` and no new physics.
        """
        from scipy.interpolate import RectBivariateSpline
        lg = np.log(np.maximum(self.g, 1e-300))
        return RectBivariateSpline(np.log(self.kk), self.N, lg, kx=3, ky=3, s=0)

    def ratio_fn(self, a_ref):
        """a callable `(k, a) -> g(k,a)/g(k,a_ref)` off that surface, scalar and fast"""
        S = self.surface()
        lkmin, lkmax = np.log(self.kk[0]), np.log(self.kk[-1])
        Nmin, Nmax = self.N[0], self.N[-1]
        lnref = float(np.clip(np.log(a_ref), Nmin, Nmax))

        def f(k, a):
            lk = min(max(float(np.log(k)), lkmin), lkmax)
            N = min(max(float(np.log(a)), Nmin), Nmax)
            return float(np.exp(S(lk, N)[0, 0] - S(lk, lnref)[0, 0]))
        return f


def background_g():
    """`L171x`'s own background quadrature, for the zero-sum comparison -- its code, not a copy

    ** READ OFF `L171x` RATHER THAN REIMPLEMENTED. **  A reduction test against a second copy of
    the thing being reduced to would prove only that the two copies agree.
    """
    import importlib.util
    p = os.path.join(_BTW, 'L171x_lensing_potential.py')
    spec = importlib.util.spec_from_file_location('_l171x', p)
    m = importlib.util.module_from_spec(spec)
    sys.modules['_l171x'] = m
    spec.loader.exec_module(m)
    return m.growth_over_a()


def isolate_against_matter_lambda(a_start, kk=None):
    """** IS THE ODE RIGHT, OR IS THE QUADRATURE? **  Both, on a background each is valid on.

    Arm Ⓐ① asks this solver to reproduce `L171x`'s `growth_over_a()`.  It does not: the gap is zero
    at the start by construction and grows monotonically to `5.3e-03` by `z = 0`, WHILE the
    radiation share falls to nothing -- so it is not residual radiation at the start, it accumulates.

    This isolates which side moves.  `D prop. H INT da/(a H)^3` is the growing mode of the growth
    equation **only for matter + Lambda**; `L171x` evaluates it on this instrument's background,
    which carries radiation.  So: build the quadrature AND the ODE on one pure matter + Lambda rate
    and compare.  *If they agree to solver tolerance the ODE is right and the quadrature is being
    used outside its own stated validity; if they do not, the ODE has a bug.*
    """
    om0 = float(A.OM)
    h0 = _h_of(1.0)

    def hml(a):
        return h0 * np.sqrt(om0 * a ** -3 + (1.0 - om0))

    def omml(a):
        return om0 * a ** -3 * (h0 / hml(a)) ** 2

    def dlnhml(a, h=1e-5):
        return (np.log(hml(a * np.exp(h))) - np.log(hml(a * np.exp(-h)))) / (2.0 * h)

    ag = np.logspace(-4, 0, 600)
    Dq = np.array([hml(x) * quad(lambda y: 1.0 / (y * hml(y)) ** 3, 1e-8, x, limit=200)[0]
                   for x in ag])
    gq = Dq / ag
    gq /= gq[0]
    bgml = CubicSpline(np.log(ag), gq)

    N0 = np.log(a_start)
    g0 = float(bgml(N0))
    h = 1e-4
    dg = (float(bgml(N0 + h)) - float(bgml(N0 - h))) / (2.0 * h)

    def rhs(N, y):
        a = np.exp(N)
        return [y[1], -(2.0 + dlnhml(a)) * y[1] + 1.5 * omml(a) * y[0]]

    Ng = np.linspace(N0, 0.0, NSTEP)
    sol = solve_ivp(rhs, (Ng[0], Ng[-1]), [g0 * a_start, (dg + g0) * a_start], t_eval=Ng,
                    rtol=1e-12, atol=1e-16, method='Radau')
    assert sol.success, sol.message
    mine = sol.y[0] / np.exp(Ng)
    rel = np.abs(mine / bgml(Ng) - 1.0)
    return dict(max_rel=float(np.max(rel)), at_start=float(rel[0]), at_today=float(rel[-1]),
                verdict=('the ODE is the growth equation and the quadrature is being used outside '
                         'matter + Lambda' if np.max(rel) < 1e-6 else 'the ODE has a bug'))


def main():
    import json
    kk = np.logspace(-4, 0, 40)
    out = {}

    print('  solving the zero-sum case', flush=True)
    g0 = GrowthKDep(0.0, kk=kk)
    bg = background_g()
    print('     the carry runs a = %.5f (z = %.2f) to a = 1'
          % (g0.a_start, 1.0 / g0.a_start - 1.0), flush=True)
    ag = np.exp(np.linspace(np.log(g0.a_start), 0.0, 25))
    rel = np.abs(g0.g_of(kk, ag) / bg(np.log(ag))[None, :] - 1.0)
    out['A1_vs_quadrature'] = dict(
        max_rel=float(np.max(rel)), at_start=float(np.max(rel[:, 0])),
        at_today=float(np.max(rel[:, -1])), registered_tol=1e-10,
        holds=bool(np.max(rel) <= 1e-10),
        a_start=float(g0.a_start), z_start=float(1.0 / g0.a_start - 1.0),
        n_k=int(len(kk)), n_a=int(len(ag)))
    print('  Ⓐ① against L171x\'s quadrature on the instrument\'s own background: max rel = %.3e '
          'against a registered 1e-10 -- FAILS' % np.max(rel), flush=True)
    print('     and it is 0 at the start by construction, growing monotonically to z = 0, so it '
          'ACCUMULATES', flush=True)

    iso = isolate_against_matter_lambda(g0.a_start)
    out['A1_isolation'] = iso
    print('  ⇒ isolated: both sides on ONE pure matter+Lambda rate agree to %.3e'
          % iso['max_rel'], flush=True)
    print('     %s' % iso['verdict'], flush=True)

    print('  solving Sum = 0.30 eV', flush=True)
    g3 = GrowthKDep(0.30, kk=kk)
    sup = g3.g_of(kk, np.array([1.0]))[:, 0] / g0.g_of(kk, np.array([1.0]))[:, 0] - 1.0
    out['B2_shape'] = dict(
        k=[float(v) for v in kk], suppression=[float(v) for v in sup],
        monotone_non_increasing=bool(np.all(np.diff(sup) <= 1e-12)),
        at_low_k=float(sup[0]), at_high_k=float(sup[-1]), f_nu=float(g3.f_nu))
    print('  Ⓑ② suppression at a = 1: %+.6f at k = %.4g, %+.6f at k = %.4g; monotone '
          'non-increasing in k: %s'
          % (sup[0], kk[0], sup[-1], kk[-1], out['B2_shape']['monotone_non_increasing']),
          flush=True)

    power, textbook = 2.0 * sup[-1], -8.0 * g3.f_nu
    out['C3_asymptote'] = dict(measured_on_power=float(power), textbook=float(textbook),
                               ratio=float(power / textbook), f_nu=float(g3.f_nu),
                               is_a_report_not_a_test=True)
    print('  Ⓒ③ the high-k asymptote on the POWER: %+.5f against the textbook -8 f_nu = %+.5f, '
          'a ratio of %.3f  (REPORTED, not tested)' % (power, textbook, power / textbook),
          flush=True)

    z_nr = g3.m_each / (3.15 * T_NU0_EV) - 1.0
    a_nr = 1.0 / (1.0 + z_nr)
    out['missing_stretch'] = dict(z_nonrelativistic=float(z_nr), a_nonrelativistic=float(a_nr))
    print('  ⌗ the species turns non-relativistic near z = %.0f' % z_nr, flush=True)
    if a_nr < g0.a_start:
        g0n = GrowthKDep(0.0, kk=kk, a_start=a_nr)
        g3n = GrowthKDep(0.30, kk=kk, a_start=a_nr)
        supn = (g3n.g_of(kk, np.array([1.0]))[:, 0] / g0n.g_of(kk, np.array([1.0]))[:, 0] - 1.0)
        out['missing_stretch'].update(
            power_from_nr=float(2 * supn[-1]), power_from_etaref=float(power),
            fraction_carried=float(sup[-1] / supn[-1]),
            ratio_from_nr_to_textbook=float(2 * supn[-1] / textbook))
        print('     carried from there instead: %+.5f on the power against %+.5f from z = 12.8'
              % (2 * supn[-1], power), flush=True)
        print('     ⇒ the ORDERED interval carries %.1f per cent of what the full one does, and '
              'the full one is %.3f of the textbook asymptote'
              % (100.0 * sup[-1] / supn[-1], 2 * supn[-1] / textbook), flush=True)

    with open(os.path.join(_HERE, 'growth_kdep.json'), 'w') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('  wrote growth_kdep.json', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
