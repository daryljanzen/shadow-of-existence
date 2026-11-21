#!/usr/bin/env python3
"""** THE CARRY, STARTED FROM THE INSTRUMENT'S OWN SOLVE INSTEAD OF FROM A CLOSED FORM. **

Order `r7847` ①, and registered arms `Ⓐ①` and `Ⓑ②`.

`r7848` left two measurements this file acts on.  Ⓐ① there found `growth_over_a()` -- a matter + Λ
closed form -- wrong by about half a per cent in `D` by `z = 0`, because it is evaluated on a
background that carries radiation.  `carry_validity.py` found that a matter-only growth equation
does not LINK two start times at all: the ratio it predicts between the instrument's own `Φ` at
`z = 188` and at `z = 12.8` is `k`-DEPENDENT, `0.9638` at the largest scales and `0.7362` at the
smallest.

** WHAT CHANGES HERE IS NOT THE EQUATION.  IT IS WHERE IT STARTS AND WHAT IT STARTS FROM. **  The
two-fluid equation already reads the instrument's own rate, so radiation is in its friction and in
its `Ω_m(a)` and the Meszaros suppression is carried rather than assumed:

    d2 d_cb/dN2  +  (2 + dlnH/dN) d d_cb/dN  =  1.5 Om_m(a) [ (1-f_nu) d_cb + f_nu d_nu ]

`r7848` started it at `z = 12.8` with initial conditions taken from the background quadrature's
growing mode.  **This file starts it at a handover and takes the initial conditions from the
instrument's own perturbation solve there** -- `delta_c`, `delta_b` and their `N`-derivative, read
off the solve rather than derived -- so the decaying mode that the residual radiation era leaves
behind is carried instead of discarded.

** THE COMPARISON NEEDS NO POISSON NORMALISATION, AND THAT IS DELIBERATE. **  At fixed `k`,
`Phi = -(3/2) (H0^2 Om / a) d_cb / k^2` in the Poisson limit, so every constant drops out of a
RATIO between two times:

    Phi(a2) / Phi(a1)  =  [ d_cb(a2) / a2 ] / [ d_cb(a1) / a1 ]

So Ⓐ① compares that quotient, computed from the carried ODE, against the instrument's OWN
`Phi(a2)/Phi(a1)` -- no units, no normalisation, nothing fitted, and the instrument is both the
source of the initial condition and the reference for the answer.  *That is the shape of test
`carry_validity.py` invented and failed; this file is the repair being judged by it.*

⚠ ** WHAT THE TEST IS REALLY TESTING, STATED BEFORE IT IS RUN. **  The quotient above assumes `Phi`
comes from the CLUSTERING matter alone at both times.  It does not: the radiation perturbations
contribute too, and they oscillate and decay.  On this background the radiation-to-matter density
ratio is `0.140` at `z = 482`, `0.0548` at `z = 188`, `0.0158` at `z = 53.6` and `0.0040` at
`z = 12.8`.  ** So an EARLIER handover carries more of the neutrino free-streaming that Ⓓ④ wants
and more of the radiation that Ⓐ① cannot describe, and the trade-off is a measurement rather than
a preference. **  That is why Ⓑ② measures the residual at three handovers instead of one.

State per mode in the instrument's solve, from `evolve`'s own docstring:
`dc tc dg tg dn tn Phi F2..F_LN db` -- so `0` is `delta_c`, `6` is `Phi`, and `db` is LAST.

Used as a module:  `PhiCarry(eta_h, targets).check()`
Run as a script:   the closed test at each handover, written to `phi_carry.json`.
"""
import io
import json
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
sys.path.insert(0, R7846)
sys.path.insert(0, _BTW)
import ACOUSTIC_two_arm as A                                               # noqa: E402
import growth_kdep as GK                                                  # noqa: E402

# the handovers to test, and the later time the instrument also covers that judges them
HANDOVERS = [float(v) for v in os.environ.get('HANDOVERS', '500,914,1400').split(',')]
JUDGE_AT = float(os.environ.get('JUDGE_AT', '1893'))
DELTA = float(os.environ.get('DELTA', '8.0'))        # the central-difference step in eta, Mpc
NKC = int(os.environ.get('NKC', '40'))
KMIN = float(os.environ.get('KMIN', '2e-4'))
KMAX = float(os.environ.get('KMAX', '1.0'))

# r7848's measured spread for the matter-only carry, which sets Ⓐ①'s criterion at one tenth of it
R7848_SPREAD = 0.9638386970854075 - 0.7362119180993076
CRITERION = 0.023


class PhiCarry:
    """the carry from one handover, with its initial conditions read off the instrument"""

    def __init__(self, eta_h, judge_at=JUDGE_AT, mnu_ev=0.0, n_species=3, kk=None, delta=DELTA):
        self.eta_h = float(eta_h)
        self.judge_at = float(judge_at)
        self.mnu = float(mnu_ev)
        self.n = int(n_species)
        self.m_each = self.mnu / self.n if self.mnu > 0 else 0.0
        self.onu = self.mnu / 93.14 / (float(A.H0) / 100.0) ** 2
        self.f_nu = self.onu / float(A.OM) if self.mnu > 0 else 0.0
        self.kk = (np.logspace(np.log10(KMIN), np.log10(KMAX), NKC) if kk is None
                   else np.asarray(kk, float))
        self.delta = float(delta)
        self._read_instrument()

    # ------------------------------------------------------------------ the instrument's own state
    def _read_instrument(self):
        """ONE solve, four output times: the handover, its two neighbours, and the judge"""
        te = np.array(sorted({self.eta_h - self.delta, self.eta_h, self.eta_h + self.delta,
                              self.judge_at}), float)
        sol, nk, NV = A.evolve(self.kk, t_eval=te, e_end=float(te[-1]))
        assert sol.status == 0, f'the instrument solve did not finish: {sol.message}'
        Y = sol.y.T.reshape(len(te), nk, NV)
        self.te, self.NV = te, NV
        self.i_h = int(np.argmin(np.abs(te - self.eta_h)))
        self.i_lo = int(np.argmin(np.abs(te - (self.eta_h - self.delta))))
        self.i_hi = int(np.argmin(np.abs(te - (self.eta_h + self.delta))))
        self.i_j = int(np.argmin(np.abs(te - self.judge_at)))
        assert len({self.i_lo, self.i_h, self.i_hi, self.i_j}) == 4, \
            'the four output times collapsed -- widen DELTA or move the judge'
        self.phi = Y[:, :, 6]
        wc = float(A.OCDM) / (float(A.OCDM) + float(A.OB))
        wb = 1.0 - wc
        # ** the two components are KEPT, not only their combination. **  carry_isolate needs
        # d_b/d_c to test whether the baryons have caught up, and re-solving the instrument to get
        # a column it already had would double the revision's cost for nothing.
        self.dc = Y[:, :, 0]
        self.db = Y[:, :, NV - 1]
        self.d_cb = wc * self.dc + wb * self.db
        self.a_of = np.array([float(A.a_of_eta(min(t, A.eta_0))) for t in te])
        self.N_of = np.log(self.a_of)
        self.weights = (wc, wb)

    # ------------------------------------------------------- the carry, cold matter and baryons
    # ** THIS WAS WRITTEN AS A REPAIR AND IT IS NOT ONE.  IT IS KEPT BECAUSE THE MEASUREMENT THAT
    # SHOWS IT IS NOT ONE IS WORTH MORE THAN THE FILE WOULD BE WITHOUT IT. **
    #
    # `carry_isolate` measured that at the handover the baryons have not caught up with the cold
    # matter at the scales that matter -- `d_b/d_c` is `1.0000` at `k = 2e-4` and `0.0101` at
    # `k = 1` at `eta = 500`, and NEGATIVE at the later handovers -- so a single `d_cb` that
    # averages a `d_c` with a `d_b` near zero looked like it must be starting from a state whose
    # next move a one-fluid equation cannot describe.  So the two clustering species are carried
    # separately here, sharing the source and the friction and coupled only through the total.
    #
    # ⇒ ** AND THE TWO CARRIES AGREE TO EVERY PRINTED DIGIT, WHICH IS NOT A COINCIDENCE: THEY ARE
    # THE SAME EQUATION. **  Both species obey `d2 d/dN2 + (2 + dlnH/dN) d d/dN = S(d_cb)`, with
    # the SAME `S` because the source depends only on the total.  Take `w_c` times the first plus
    # `w_b` times the second: the weighted sum `d_cb` obeys that one equation exactly, with initial
    # conditions `w_c d_c + w_b d_b` and `w_c d_c' + w_b d_b'` -- which are exactly the one-fluid
    # initial conditions, because a weighted sum of central differences IS the central difference of
    # the weighted sum.  *So splitting the species changes nothing, and the baryon shortfall
    # `carry_isolate` measured is NOT an error the carry can fix by splitting them.*
    #   ⌗ The guard this walks into is this seat's own: when a fork names two objects, check that
    #   the thing they are alternatives FOR has a slot for only one of them.  The source has one
    #   slot, for the total, so there was never a second object to carry.
    def _rhs2(self, N, y, k):
        a = np.exp(N)
        dc, dcp, db, dbp = y
        wc, wb = self.weights
        d_cb = wc * dc + wb * db
        kf = GK.k_fs(a, self.m_each)
        filt = 1.0 / (1.0 + (k / kf) ** 2) if np.isfinite(kf) else 1.0
        src = 1.5 * GK.om_tot(a) * d_cb * ((1.0 - self.f_nu) + self.f_nu * filt)
        fr = -(2.0 + GK._dlnh_dn(a))
        return [dcp, fr * dcp + src, dbp, fr * dbp + src]

    def ic2(self):
        """`d_c`, `d_b` and each one's `N`-derivative at the handover, read off the instrument"""
        dN = self.N_of[self.i_hi] - self.N_of[self.i_lo]
        return (self.dc[self.i_h], (self.dc[self.i_hi] - self.dc[self.i_lo]) / dN,
                self.db[self.i_h], (self.db[self.i_hi] - self.db[self.i_lo]) / dN)

    def carry_to2(self, N_end):
        """integrate both clustering species from the handover, returning `d_cb` at `N_end`"""
        c0, cp0, b0, bp0 = self.ic2()
        N_h = self.N_of[self.i_h]
        wc, wb = self.weights
        out = np.empty(len(self.kk))
        for i, k in enumerate(self.kk):
            s = solve_ivp(self._rhs2, (N_h, float(N_end)),
                          [float(c0[i]), float(cp0[i]), float(b0[i]), float(bp0[i])],
                          args=(float(k),), rtol=1e-11, atol=1e-16, method='Radau')
            assert s.success, f'the two-species carry failed at k = {k:.4g}: {s.message}'
            out[i] = wc * float(s.y[0, -1]) + wb * float(s.y[2, -1])
        return out

    # -------------------------------------------------------------------------------- the carry
    def _rhs(self, N, y, k):
        a = np.exp(N)
        d, dp = y
        kf = GK.k_fs(a, self.m_each)
        filt = 1.0 / (1.0 + (k / kf) ** 2) if np.isfinite(kf) else 1.0
        src = 1.5 * GK.om_tot(a) * d * ((1.0 - self.f_nu) + self.f_nu * filt)
        return [dp, -(2.0 + GK._dlnh_dn(a)) * dp + src]

    def ic(self):
        """`delta_cb` and `d delta_cb / dN` at the handover, READ OFF the instrument's own solve

        ** The derivative is a central difference of the instrument's own output and not a
        continuity equation written out here, so no gauge convention of this file's can be wrong
        about it. **
        """
        d0 = self.d_cb[self.i_h]
        dN = self.N_of[self.i_hi] - self.N_of[self.i_lo]
        dd0 = (self.d_cb[self.i_hi] - self.d_cb[self.i_lo]) / dN
        return d0, dd0

    def carry_to(self, N_end):
        """integrate each mode from the handover to `N_end`, returning `delta_cb` there"""
        d0, dd0 = self.ic()
        N_h = self.N_of[self.i_h]
        out = np.empty(len(self.kk))
        for i, k in enumerate(self.kk):
            s = solve_ivp(self._rhs, (N_h, float(N_end)), [float(d0[i]), float(dd0[i])],
                          args=(float(k),), rtol=1e-11, atol=1e-16, method='Radau')
            assert s.success, f'the carry failed at k = {k:.4g}: {s.message}'
            out[i] = float(s.y[0, -1])
        return out

    # ---------------------------------------------------------------------------------- the test
    def check(self):
        """Ⓐ①: the carried `Phi` quotient against the instrument's own, per `k`"""
        a_h, a_j = self.a_of[self.i_h], self.a_of[self.i_j]
        d_j = self.carry_to(self.N_of[self.i_j])
        d_h = self.d_cb[self.i_h]
        carried = (d_j / a_j) / (d_h / a_h)
        own = self.phi[self.i_j] / self.phi[self.i_h]
        rel = carried / own - 1.0
        d_j2 = self.carry_to2(self.N_of[self.i_j])
        carried2 = (d_j2 / a_j) / (d_h / a_h)
        rel2 = carried2 / own - 1.0
        rad_h = (float(A.OR) / a_h ** 4) / ((float(A.OM) - float(A.ONU)) / a_h ** 3)
        return dict(eta_h=self.eta_h, judge_at=self.judge_at, a_h=a_h, a_judge=a_j,
                    z_h=1.0 / a_h - 1.0, z_judge=1.0 / a_j - 1.0,
                    radiation_over_matter_at_handover=rad_h,
                    k=[float(v) for v in self.kk],
                    carried=[float(v) for v in carried], instrument=[float(v) for v in own],
                    rel=[float(v) for v in rel],
                    spread=float(rel.max() - rel.min()),
                    worst_abs=float(np.max(np.abs(rel))),
                    holds=bool((rel.max() - rel.min()) < CRITERION),
                    two_species=dict(
                        carried=[float(v) for v in carried2],
                        rel=[float(v) for v in rel2],
                        spread=float(rel2.max() - rel2.min()),
                        worst_abs=float(np.max(np.abs(rel2))),
                        holds=bool((rel2.max() - rel2.min()) < CRITERION),
                        identical_to_one_species=bool(
                            np.max(np.abs(carried2 / carried - 1.0)) < 1e-9),
                        worst_relative_difference_from_one_species=float(
                            np.max(np.abs(carried2 / carried - 1.0)))),
                    weights=dict(cdm=self.weights[0], baryon=self.weights[1]),
                    delta_eta=self.delta, n_k=int(len(self.kk)))


def main():
    print('\n  Ⓐ①/Ⓑ②: the carry judged CLOSED against the instrument\'s own Phi\n')
    print('  criterion: the spread of the residual across the band below %.3f, which is one tenth'
          % CRITERION)
    print('             of the %.4f spread r7848 measured for the matter-only carry' % R7848_SPREAD)
    print('  judge at eta = %.0f (z = %.2f); %d wavenumbers over %.1e..%.1e\n'
          % (JUDGE_AT, 1.0 / float(A.a_of_eta(JUDGE_AT)) - 1.0, NKC, KMIN, KMAX), flush=True)
    rows = []
    for eh in HANDOVERS:
        c = PhiCarry(eh).check()
        rows.append(c)
        print('  handover eta = %-6g (z = %7.2f, radiation/matter %.4f): spread %.4e, worst '
              '|residual| %.4e  -> %s'
              % (eh, c['z_h'], c['radiation_over_matter_at_handover'], c['spread'],
                 c['worst_abs'], 'HOLDS' if c['holds'] else 'FAILS'), flush=True)
        print('     residual at k = %.1e is %+.4e; at k = %.1e is %+.4e'
              % (c['k'][0], c['rel'][0], c['k'][-1], c['rel'][-1]), flush=True)
        t = c['two_species']
        print('     carrying the two clustering species SEPARATELY: spread %.4e, which differs '
              'from the one-species\n        carry by %.3e relative -- %s'
              % (t['spread'], t['worst_relative_difference_from_one_species'],
                 'THE SAME EQUATION, as the module\'s own note derives'
                 if t['identical_to_one_species'] else 'a real difference'), flush=True)
    best = min(rows, key=lambda r: r['spread'])
    spreads = [r['spread'] for r in rows]
    spreads2 = [r['two_species']['spread'] for r in rows]
    out = dict(criterion=CRITERION, r7848_matter_only_spread=R7848_SPREAD,
               judge_at=JUDGE_AT, handovers=rows,
               best_handover=best['eta_h'], best_spread=best['spread'],
               spread_range=[float(min(spreads)), float(max(spreads))],
               depends_on_handover=bool(max(spreads) > 3.0 * min(spreads)),
               any_holds=bool(any(r['holds'] for r in rows)),
               all_hold=bool(all(r['holds'] for r in rows)),
               two_species=dict(
                   spread_range=[float(min(spreads2)), float(max(spreads2))],
                   best_handover=float(min(rows, key=lambda r: r['two_species']['spread'])['eta_h']),
                   best_spread=float(min(spreads2)),
                   any_holds=bool(any(r['two_species']['holds'] for r in rows)),
                   identical_to_one_species=bool(
                       all(r['two_species']['identical_to_one_species'] for r in rows)),
                   worst_relative_difference=float(max(
                       r['two_species']['worst_relative_difference_from_one_species']
                       for r in rows))))
    print('\n  Ⓐ①: %s -- best spread %.4e at eta = %g, against the criterion %.3f and r7848\'s '
          '%.4f' % ('HOLDS' if out['any_holds'] else 'FAILS', out['best_spread'],
                    out['best_handover'], CRITERION, R7848_SPREAD))
    print('  Ⓑ②: the spread across the three handovers runs %.4e to %.4e, so the agreement %s '
          'on which handover is used'
          % (min(spreads), max(spreads),
             'DEPENDS' if out['depends_on_handover'] else 'does NOT depend strongly'))
    t = out['two_species']
    print('  ⌗ carrying the two clustering species SEPARATELY changes nothing: the worst relative '
          'difference\n     from the one-species carry is %.3e, because %s'
          % (t['worst_relative_difference'],
             'they are the same equation -- the source has ONE slot, for the total'
             if t['identical_to_one_species'] else 'they are not the same equation'))
    # ** THE RECORD IS KEYED BY ITS CONFIGURATION, which is this revision's own lesson about
    # r7848's cost table: a record that does not carry the configuration it was measured under
    # cannot be read later. **  `phi_carry.json` is the REGISTERED configuration -- the three
    # handovers judged at eta = 1893 -- and any other configuration writes beside it, never over
    # it.
    reg = (JUDGE_AT == 1893.0 and HANDOVERS == [500.0, 914.0, 1400.0])
    name = ('phi_carry.json' if reg
            else 'phi_carry_judge%g_from_%s.json' % (JUDGE_AT,
                                                     '_'.join('%g' % h for h in HANDOVERS)))
    out['is_the_registered_configuration'] = bool(reg)
    out['handovers_requested'] = [float(h) for h in HANDOVERS]
    with io.open(os.path.join(_HERE, name), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote %s%s\n' % (name, '' if reg else '   (NOT the registered configuration)'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
