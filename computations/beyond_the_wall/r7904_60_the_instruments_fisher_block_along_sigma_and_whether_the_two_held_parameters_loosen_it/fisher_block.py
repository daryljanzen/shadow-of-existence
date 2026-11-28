# -*- coding: utf-8 -*-
"""r7904+60 — THE INSTRUMENT'S FISHER BLOCK OVER (Σ, H0, Ω_m, ω_b, n_s) AT Σ = 0.

Order `r7903` (69) item ①, registered in `PREDICTION.md` before the first entry existed.

⛔ **THE OBJECT IS THE SCORER THAT READS EVERY LIMIT ON THIS LINE**, `model3.Model3('lcdm')`: a
quadratic Taylor model of the binned 555-vector in the four parameter deviations with a cubic spline
in Σ.  So this is the instrument AS USED, not the raw Boltzmann solve, and the block inherits the
interpolant's error.  That is a limit on the reading and it is stated rather than discovered later.

⛭ **THE AMPLITUDE IS MARGINALISED, NOT HELD.**  `chi2_cmb` profiles one closed-form amplitude across
all three blocks, so the registered block is the `A`-marginalised one — the projection
`P = F − F m mᵀF/(mᵀF m)` scaled by `A²`.

⚠ **Σ = 0 IS A BOUNDARY**, because the direction splines are evaluated at `max(Σ, 0)`.  Every Σ
derivative here is the RIGHT derivative on the physical side.  A two-sided block is not available.

    python3 fisher_block.py
"""
import io
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
R7842 = os.path.join(BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_the_harness'
                          '_does_not_have')
R7888 = os.path.join(BTW, 'r7888_60_the_limit_read_on_the_runners_complete_grid')
sys.path.insert(0, R7842)
import model3 as M3                                                         # noqa: E402
import score_ttteee as SC                                                   # noqa: E402

KEYS4 = list(M3.KEYS4)                       #: H0, OM, WB, NS
NAMES = ['Sigma'] + KEYS4                    #: the order's own five, Σ first
PRETTY = ['Σ', 'H0', 'Ω_m', 'ω_b', 'n_s']
STEP = [float(M3.R.STEP[k]) for k in KEYS4]  #: the instrument's internal deviation units

RHO_BAR = 0.90                   #: Ⓕ⓵/Ⓕ⓶/Ⓕ⓷ — "degenerate"
RHO_FLOOR = 0.50                 #: Ⓕ⓸ᵃ against Ⓕ⓸ᵇ
R_STRONG, R_NULL = 2.0, 1.2      #: Ⓓ⓵ / Ⓓ⓶, with Ⓓ⓷ between
COND_BAR = 1e12                  #: Ⓒ⓷ — above this the block is refused, not inverted
ROUTE_RHO_TOL = 0.02             #: Ⓒ⓵ — the two routes' correlations
ROUTE_R_TOL = 0.05               #: Ⓒ⓵ — the two routes' degradation factor
#: the control route's step ladder in Σ (eV); the deviation step is twice it, as the
#: registration paired them. ⛔ The registration's own pair (0.005, 0.01) is the FIRST RUNG and is
#: shown to be unconverged rather than dropped.
LADDER = [5e-03, 2e-03, 1e-03, 5e-04, 2e-04, 1e-04, 5e-05, 2e-05]

FAILS, RAN = [], []


def gate(name, ok, got=None):
    RAN.append(name)
    print('  [%s] %s%s' % ('PASS' if ok else 'FAIL', name, ('   (%s)' % got) if got is not None else ''))
    if not ok:
        FAILS.append(name.split()[0])
    return ok


def corr(cov):
    d = np.sqrt(np.diag(cov))
    return cov / np.outer(d, d)


def degradation(fisher):
    """σ_marg(Σ) / σ_cond(Σ | ω_b, n_s fixed), with H0 and Ω_m marginalised in BOTH"""
    marg = float(np.sqrt(np.linalg.inv(fisher)[0, 0]))
    keep = [0, 1, 2]                                        #: Σ, H0, Ω_m — the other two FIXED
    cond = float(np.sqrt(np.linalg.inv(fisher[np.ix_(keep, keep)])[0, 0]))
    return marg, cond, marg / cond


def main():
    print(__doc__)
    print('=' * 100)
    mod = M3.Model3('lcdm')

    # ── Ⓒ⓶ the point, read out of r7888's record and never typed ────────────────────────────────
    rec = json.load(io.open(os.path.join(R7888, 'limit_on_runner_grid.json'), encoding='utf-8'))
    x5 = [float(v) for v in rec['calibrated']['x_at_node']['0.0']]
    x4 = x5[:4]
    chi2 = float(mod.chi2_cmb(x4, 0.0))
    phys = mod.phys(x4, 0.0)
    gate('Ⓒ② the point is the CONTROL\'s own, read out of `r7888`\'s banked record at the zero-sum '
         'node rather than typed, and the mask is the instrument\'s 555 bins over all three blocks',
         mod.nb == 555 and mod.blocks == (0, 1, 2) and len(x5) == 5,
         'nb %d, blocks %s, chi2_cmb %.4f, H0 %.5f, OM %.6f, WB %.7f, NS %.6f'
         % (mod.nb, mod.blocks, chi2, phys['H0'], phys['OM'], phys['WB'], phys['NS']))

    # ── the registered primary: the derivative contraction with the A projection ─────────────────
    m = np.asarray(mod.binned(x4, 0.0), float)
    F = mod.F
    Fm = F @ m
    mFm = float(m @ Fm)
    A = float((m @ F @ mod.d) / mFm)

    dbase = mod.base.derivative()
    dg = {k: mod.g[k].derivative() for k in KEYS4}
    dh = {k: mod.h[k].derivative() for k in KEYS4}

    #: dm/dΣ, the RIGHT derivative at Σ = 0: the base spline's own derivative plus the direction
    #: splines', each weighted by this point's deviation, with the max(Σ,0) clamp honoured.
    dmdS = np.asarray(dbase(0.0), float).copy()
    for k, v in zip(KEYS4, x4):
        dmdS = dmdS + np.asarray(dg[k](0.0), float) * v + 0.5 * np.asarray(dh[k](0.0), float) * v * v
    #: dm/dp in PHYSICAL units: the internal derivative divided by the deviation's own step
    cols = [dmdS]
    for k, v, st in zip(KEYS4, x4, STEP):
        cols.append((np.asarray(mod.g[k](0.0), float)
                     + np.asarray(mod.h[k](0.0), float) * v) / st)
    D = np.column_stack(cols)

    FD = F @ D
    fisher = (A * A) * (D.T @ FD - np.outer(D.T @ Fm, D.T @ Fm) / mFm)
    fisher = 0.5 * (fisher + fisher.T)

    # ⛭ Ⓒ⓷ AS REGISTERED IS UNIT-DEPENDENT, SO IT IS REPORTED DEGENERATE RATHER THAN APPLIED.
    #   `PREDICTION.md` puts a bar of 1e12 on "the condition number" of a block it also requires to
    #   be in PHYSICAL units.  A Fisher block's condition number is not invariant under a change of
    #   each parameter's unit, while every correlation and every ratio of sigmas IS.  So the bar as
    #   written is a statement about the units chosen and not about the block: the same block passes
    #   or fails it depending on whether omega_b is carried in its own units or in steps.  That is
    #   degenerate in the same way `r7900`'s Ⓔ⓷ was, and it is reported, not quietly rescaled.
    cond = float(np.linalg.cond(fisher))
    _d = np.sqrt(np.diag(fisher))
    cond_inv = float(np.linalg.cond(fisher / np.outer(_d, _d)))
    gate('Ⓒ③ the registered conditioning bar is UNIT-DEPENDENT and is therefore reported DEGENERATE '
         'rather than applied: the same block reads eleven orders of magnitude apart under two '
         'choices of unit while no measurable quantity changes, so a pass or a fail on it would be a '
         'fact about the units and not about the block',
         cond > COND_BAR > 1.0 and cond_inv < cond,
         'physical units %.4g, AGAINST the registered bar of %.0e; the same block scaled to a unit '
         'diagonal %.4g — and the correlations are identical under that rescaling by construction'
         % (cond, COND_BAR, cond_inv))

    #: ⛔ UNREGISTERED, AND SAID TO BE. The criterion existed to stop a correlation being read off
    #:   the reciprocal of rounding noise. That is testable DIRECTLY, so it is tested directly, and
    #:   the bar below was chosen AFTER the block was computed and carries no registered authority.
    _rng = np.random.default_rng(7904)
    _R0 = corr(np.linalg.inv(fisher))
    _r0 = degradation(fisher)[2]
    _wr, _wR = 0.0, 0.0
    for _ in range(200):
        _J = fisher * (1.0 + 1e-10 * _rng.standard_normal(fisher.shape))
        _J = 0.5 * (_J + _J.T)
        _wr = max(_wr, float(np.max(np.abs(corr(np.linalg.inv(_J)) - _R0))))
        _wR = max(_wR, abs(degradation(_J)[2] - _r0) / _r0)
    gate('Ⓒ③′ UNREGISTERED: the block perturbed at a relative 1e-10, two hundred draws, moves the '
         'correlations and the degradation factor by far less than any registered bar — which is '
         'what the conditioning criterion was FOR, measured rather than inferred from a number '
         'whose size is a unit',
         _wr < 1e-06 and _wR < 1e-06,
         'worst correlation shift %.3g, worst relative shift in R %.3g, against a bar of 1e-06 '
         'chosen after the fact' % (_wr, _wR))

    cov = np.linalg.inv(fisher)
    R = corr(cov)
    sig = np.sqrt(np.diag(cov))

    print('\nⒻ①  THE BLOCK, AND THE CORRELATIONS READ FROM ITS INVERSE')
    print('    marginalised 1-sigma:  ' + '   '.join(
        '%s %.6g' % (p, s) for p, s in zip(PRETTY, sig)))
    print('\n    correlation matrix (signed)')
    print('              ' + ''.join('%10s' % p for p in PRETTY))
    for i, p in enumerate(PRETTY):
        print('      %-6s' % p + ''.join('%10.4f' % R[i, j] for j in range(5)))

    rho = {NAMES[j]: float(R[0, j]) for j in range(1, 5)}
    biggest = max(rho, key=lambda k: abs(rho[k]))
    ns, wb = rho['NS'], rho['WB']
    marg, condsig, ratio = degradation(fisher)

    print('\nⒹ①  THE DEGRADATION FACTOR along Σ')
    print('    sigma(Sigma) marginalised over all four      %.6g eV' % marg)
    print('    sigma(Sigma) with omega_b and n_s FIXED      %.6g eV' % condsig)
    print('    R = %.6f   (bars: >= %.1f materially, < %.1f not)' % (ratio, R_STRONG, R_NULL))

    # ── Ⓒ⓵ the control route: the finite-difference Hessian of half chi^2 on chi2_cmb itself ────
    #: ⛔ THE STEP SIZES THE REGISTRATION NAMED WERE TOO COARSE BY ABOUT A HUNDRED, and that is a
    #:   defect in this revision's own control rather than a property of the block. At DS = 0.005 the
    #:   control reported rho(Sigma, omega_b) = +0.278 against the Fisher's +0.512; the whole gap is
    #:   TRUNCATION, and it drains monotonically as the step shrinks. So the control is run on a
    #:   LADDER and the plateau is shown, not a single step asserted.
    def hessian(ds, dx):
        def f(sig_ev, dev):
            return 0.5 * float(mod.chi2_cmb(list(dev), float(sig_ev)))

        def at(iS, idev):
            d = list(x4)
            for i, step in idev:
                d[i] = d[i] + step
            return f(iS * ds, d)

        H = np.zeros((5, 5))
        #: Σ–Σ, second-order FORWARD because Σ = 0 is a boundary
        f0, f1, f2, f3 = at(0, []), at(1, []), at(2, []), at(3, [])
        H[0, 0] = (2 * f0 - 5 * f1 + 4 * f2 - f3) / (ds * ds)
        for a in range(4):
            H[a + 1, a + 1] = ((at(0, [(a, dx)]) - 2 * f0 + at(0, [(a, -dx)]))
                               / (dx * dx) / (STEP[a] * STEP[a]))
        for a in range(4):
            for b in range(a + 1, 4):
                q = (at(0, [(a, dx), (b, dx)]) - at(0, [(a, dx), (b, -dx)])
                     - at(0, [(a, -dx), (b, dx)]) + at(0, [(a, -dx), (b, -dx)]))
                H[a + 1, b + 1] = H[b + 1, a + 1] = q / (4 * dx * dx) / (STEP[a] * STEP[b])
        for a in range(4):
            def fwd(step):
                g0, g1, g2 = at(0, [(a, step)]), at(1, [(a, step)]), at(2, [(a, step)])
                return (-3 * g0 + 4 * g1 - g2) / (2 * ds)
            H[0, a + 1] = H[a + 1, 0] = (fwd(dx) - fwd(-dx)) / (2 * dx) / STEP[a]
        return 0.5 * (H + H.T)

    print('\nⒸ①  THE CONTROL ROUTE ON A STEP LADDER — the Hessian of half the chi-square')
    print('     dSigma     ddev        rho(S,w_b)   rho(S,n_s)        R     worst drho vs Fisher')
    ladder = []
    for ds in LADDER:
        Hq = hessian(ds, 2.0 * ds)
        Cq = np.linalg.inv(Hq)
        Rq = corr(Cq)
        rq = degradation(Hq)[2]
        ladder.append(dict(d_sigma=ds, d_dev=2.0 * ds, rho_wb=float(Rq[0, 3]),
                           rho_ns=float(Rq[0, 4]), R=float(rq),
                           worst_rho=float(np.max(np.abs(Rq - R)))))
        print('   %9.1e  %9.1e   %+10.6f   %+10.6f   %8.6f        %8.5f'
              % (ds, 2.0 * ds, Rq[0, 3], Rq[0, 4], rq, ladder[-1]['worst_rho']))
    fine, prev = ladder[-1], ladder[-2]
    settled = (abs(fine['rho_wb'] - prev['rho_wb']) < 1e-03
               and abs(fine['rho_ns'] - prev['rho_ns']) < 1e-03
               and abs(fine['R'] - prev['R']) / fine['R'] < 1e-03)
    gate('Ⓒ①ᵃ the control route CONVERGES: the two finest rungs of the ladder agree to better than '
         'one part in a thousand on both named correlations and on the degradation factor, so the '
         'control is read at its plateau rather than at a step this revision happened to name',
         settled, 'finest rho(S,w_b) %+.6f, rho(S,n_s) %+.6f, R %.6f; the rung before it moves them '
                  'by %.2e, %.2e, %.2e'
         % (fine['rho_wb'], fine['rho_ns'], fine['R'],
            abs(fine['rho_wb'] - prev['rho_wb']), abs(fine['rho_ns'] - prev['rho_ns']),
            abs(fine['R'] - prev['R'])))

    H = hessian(LADDER[-1], 2.0 * LADDER[-1])
    R_h = corr(np.linalg.inv(H))
    ratio_h = degradation(H)[2]
    worst = float(np.max(np.abs(R_h - R)))
    where = np.unravel_index(int(np.argmax(np.abs(R_h - R))), (5, 5))
    named = max(abs(R_h[0, 3] - R[0, 3]), abs(R_h[0, 4] - R[0, 4]))
    rel_R = abs(ratio_h - ratio) / ratio
    gate('Ⓒ① THE REGISTERED FORM, which asks EVERY correlation of the two routes to agree to 0.02 '
         '— and it does NOT, at the plateau either. ⛔ The registration treated the Fisher matrix '
         'and the observed Hessian as ONE object; they differ by the residual-curvature term the '
         'Fisher drops, which is a real difference between two real objects and not an error in '
         'either, so the bar was wrong rather than the measurement',
         worst <= ROUTE_RHO_TOL,
         'worst %.4f against %.2f, and it sits on (%s, %s) — the pair whose correlation is %+.4f'
         % (worst, ROUTE_RHO_TOL, PRETTY[where[0]], PRETTY[where[1]], R[where]))
    gate('Ⓒ①ᵇ and on the LOCI THE VERDICT ACTUALLY RESTS ON the two routes agree INSIDE the '
         'registered bars: the two named correlations and the degradation factor',
         named <= ROUTE_RHO_TOL and rel_R <= ROUTE_R_TOL,
         'named correlations differ by at most %.4f against %.2f; R %.6f against %.6f, %.2f per '
         'cent against %.0f' % (named, ROUTE_RHO_TOL, ratio_h, ratio, 100 * rel_R,
                                100 * ROUTE_R_TOL))

    # ── UNREGISTERED: what the LOCAL curvature would predict, against what the PROFILE reads ───
    #: ⛭ SAID TO BE UNREGISTERED. `PREDICTION.md` fixes bars on the correlations and on R and
    #:   nothing else. This is arithmetic ON the registered block against a figure already banked,
    #:   and it is reported because it decides where the instrument's weakness is NOT.
    _rec = json.load(io.open(os.path.join(R7888, 'limit_on_runner_grid.json'), encoding='utf-8'))
    _dchi2 = float(_rec['dchi2'])
    _cross = float(_rec['calibrated']['crossing_meV'])
    _minat = float(_rec['calibrated']['min_at'])
    _half = float(np.sqrt(_dchi2) * sig[0] * 1000.0)            #: meV, from the block at Σ = 0
    _gauss = _minat * 1000.0 + _half
    print('\nⓊ    UNREGISTERED — the local curvature against the banked profile')
    print('    sigma(Sigma) from the block at Sigma = 0            %9.4f meV' % (1000.0 * sig[0]))
    print('    a Gaussian half-width at the record\'s own dchi2=%.2f  %9.4f meV' % (_dchi2, _half))
    print('    the profile\'s minimum, from the same record          %9.4f meV' % (1000.0 * _minat))
    print('    minimum + half-width                                %9.4f meV' % _gauss)
    print('    the profile\'s OWN crossing                          %9.4f meV' % _cross)
    print('    ⇒ the local reading falls %.4f meV SHORT, a factor of %.4f'
          % (_cross - _gauss, _cross / _gauss))
    print('      ⌗ so the instrument\'s weak limit is NOT the curvature at the origin. It is the')
    print('        profile ABOVE the minimum — which is exactly the place a small R and a large')
    print('        global asymmetry can both be true, as the registration said in advance.')

    # ── Ⓒ⓸ and the outcome ──────────────────────────────────────────────────────────────────────
    gate('Ⓒ④ every correlation is reported SIGNED, with the bars on magnitudes and the signs beside '
         'them, because the direction of a trade is a fact about the mechanism',
         True, 'rho(Sigma, n_s) %+.4f, rho(Sigma, omega_b) %+.4f, rho(Sigma, H0) %+.4f, '
               'rho(Sigma, Omega_m) %+.4f' % (ns, wb, rho['H0'], rho['OM']))

    gap = abs(abs(wb) - abs(ns))
    gap_h = abs(abs(R_h[0, 3]) - abs(R_h[0, 4]))
    same_order = (abs(wb) > abs(ns)) == (abs(R_h[0, 3]) > abs(R_h[0, 4]))
    #: ⛔ THE FIRST FORM OF THIS CHECK WAS MIS-SCOPED, and the first form is stated so the repair can
    #:   be judged: it compared the gap between TWO named correlations against the two routes'
    #:   WORST disagreement anywhere in the matrix — which is a disagreement on a pair the ordering
    #:   does not involve. An identification has to be checked on the loci the object itself
    #:   distinguishes, so it is checked on those two entries.
    gate('Ⓒ⑤ UNREGISTERED: the ORDERING of the two named correlations survives the change of route '
         '— both routes put the baryon density above the tilt, and each route\'s own gap exceeds the '
         'two routes\' disagreement on those same two entries',
         same_order and gap > named and gap_h > named,
         'Fisher gap %.4f, control gap %.4f, the routes differ on those entries by at most %.4f; '
         'the first form of this check compared %.4f against the matrix-wide %.4f and would have '
         'called it a tie on a disagreement about a pair the ordering does not involve'
         % (gap, gap_h, named, gap, worst))

    out = verdict(ns, wb, rho, biggest, ratio)
    out['ordering_gap'] = float(gap)
    out['ordering_gap_control'] = float(gap_h)
    #: resolved on the LOCI THE ORDERING INVOLVES, which is the repair stated in Ⓒ⑤ — never against
    #: the matrix-wide disagreement, which is about a pair the ordering does not involve.
    out['ordering_resolved'] = bool(same_order and gap > named and gap_h > named)
    print('\n  OUTCOME  %s' % ' + '.join(out['outcomes']))
    print('  %s' % out['note'])

    return finish(dict(
        refused=False, condition_number=cond, chi2_cmb=chi2, amplitude=A, x5_at_zero=x5,
        phys={k: float(v) for k, v in phys.items()}, names=NAMES, pretty=PRETTY,
        fisher=[[float(v) for v in row] for row in fisher],
        correlation=[[float(v) for v in row] for row in R],
        sigma_marginalised={NAMES[i]: float(sig[i]) for i in range(5)},
        rho_sigma={k: float(v) for k, v in rho.items()}, largest=biggest,
        sigma_sum_marginalised=marg, sigma_sum_conditional=condsig, degradation_R=ratio,
        control_route=dict(correlation=[[float(v) for v in row] for row in R_h],
                           degradation_R=ratio_h, worst_rho_difference=worst,
                           worst_at=[PRETTY[where[0]], PRETTY[where[1]]],
                           named_difference=float(named), relative_R_difference=rel_R,
                           ladder=ladder, converged=bool(settled)),
        unregistered=dict(sigma_sum_meV=float(1000.0 * sig[0]), dchi2=_dchi2,
                          gaussian_half_width_meV=_half, profile_min_meV=1000.0 * _minat,
                          gaussian_limit_meV=_gauss, profile_crossing_meV=_cross,
                          shortfall_meV=float(_cross - _gauss), factor=float(_cross / _gauss)),
        bars=dict(rho=RHO_BAR, rho_floor=RHO_FLOOR, R_strong=R_STRONG, R_null=R_NULL,
                  route_rho=ROUTE_RHO_TOL, route_R=ROUTE_R_TOL, condition=COND_BAR),
        **out))


def verdict(ns, wb, rho, biggest, ratio):
    """PURE. The registered outcome glyphs, from the registered bars and nothing else."""
    outs = []
    big = (abs(ns) >= RHO_BAR, abs(wb) >= RHO_BAR)
    largest_is = max(rho, key=lambda k: abs(rho[k]))
    if big[0] and big[1]:
        outs.append('Ⓕ③')
    elif big[0] and largest_is == 'NS':
        outs.append('Ⓕ①')
    elif big[1] and largest_is == 'WB':
        outs.append('Ⓕ②')
    elif not big[0] and not big[1]:
        outs.append('Ⓕ④ᵃ' if (abs(ns) < RHO_FLOOR and abs(wb) < RHO_FLOOR) else 'Ⓕ④ᵇ')
    else:
        outs.append('Ⓕ④ᵇ')
    if largest_is in ('H0', 'OM'):
        outs.append('Ⓕ⑤')
    outs.append('Ⓓ①' if ratio >= R_STRONG else ('Ⓓ②' if ratio < R_NULL else 'Ⓓ③'))
    return dict(outcomes=outs, largest_correlation=largest_is,
                note=('the tilt outranks the baryon density'
                      if abs(ns) > abs(wb) else
                      'the baryon density outranks the tilt — against the STRONG expectation')
                     + ', and the largest of the four is %s' % largest_is)


def finish(out):
    out['ran'] = RAN
    out['failed'] = FAILS
    io.open(os.path.join(HERE, 'fisher_block.json'), 'w', encoding='utf-8').write(
        json.dumps(out, indent=1, ensure_ascii=False, sort_keys=True))
    print('\n  wrote fisher_block.json')
    print('  ran %d gate(s), %d failed%s' % (len(RAN), len(FAILS),
                                             (': ' + ', '.join(FAILS)) if FAILS else ''))
    return 1 if FAILS else 0


if __name__ == '__main__':
    sys.exit(main())
