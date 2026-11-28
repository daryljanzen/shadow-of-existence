# -*- coding: utf-8 -*-
"""r7908+60 — THE SAME FISHER BLOCK AT THE PROFILE'S MINIMUM AND ABOVE IT.

This seat's own item on the fork `r7904` routed to `69`, registered in `PREDICTION.md` and pushed
before the first interior entry existed.

⛭ **ONE FUNCTION READS ALL THREE POINTS.**  `block_at` is called at Σ = `0`, `0.06` and `0.30`, and
the Σ = `0` call must reproduce `r7904`'s recorded block ENTRY FOR ENTRY -- which is what makes the
three points one measurement rather than three.  The amplitude is projected out exactly as there.

⛔ **AND BOTH NEW POINTS ARE INTERIOR, WHICH IS WHY THEY WERE CHOSEN.**  `model3.binned` evaluates the
direction splines at `max(Σ, 0)`, so at Σ = `0` a central difference crosses a KINK and `r7904` had to
take the right derivative.  At Σ > `0` the clamp is inactive and the analytic derivative IS the
two-sided one.  This module MEASURES that on the function rather than asserting it from the source.

⌗ **TWO OF `r7904`'s LESSONS ARE APPLIED HERE RATHER THAN REPEATED.**  No conditioning bar is
registered, because a condition number on a Fisher block is unit-dependent and so degenerate as a
criterion.  And the finite-difference Hessian is a CONVERGENCE CHECK at the loci the verdict rests on
only -- the two named correlations and the degradation factor -- with no bar on the rest of the
matrix, because the Fisher matrix and the observed Hessian are two objects.

    python3 interior_block.py
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
R7904 = os.path.join(BTW, 'r7904_60_the_instruments_fisher_block_along_sigma_and_whether_the_two'
                          '_held_parameters_loosen_it')
sys.path.insert(0, R7842)
import model3 as M3                                                         # noqa: E402

KEYS4 = list(M3.KEYS4)
NAMES = ['Sigma'] + KEYS4
PRETTY = ['Σ', 'H0', 'Ω_m', 'ω_b', 'n_s']
STEP = [float(M3.R.STEP[k]) for k in KEYS4]

POINTS = [('Ⓞ', 0.00, '0.0'), ('Ⓐ', 0.06, '0.06'), ('Ⓑ', 0.30, '0.3')]
GROW_BAR, FLAT_BAR = 0.10, 0.05        #: Ⓟ⓵ / Ⓟ⓶ / Ⓟ⓸
R_STRONG, R_NULL = 2.0, 1.2            #: Ⓝ⓵ / Ⓝ⓶
LADDER = [1e-03, 5e-04, 2e-04, 1e-04, 5e-05, 2e-05]
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
    marg = float(np.sqrt(np.linalg.inv(fisher)[0, 0]))
    cond = float(np.sqrt(np.linalg.inv(fisher[np.ix_([0, 1, 2], [0, 1, 2])])[0, 0]))
    return marg, cond, marg / cond


def block_at(mod, x4, sum_ev):
    """the A-marginalised Fisher block in physical units, by the same arithmetic at every Σ"""
    s = float(sum_ev)
    m = np.asarray(mod.binned(x4, s), float)
    F = mod.F
    Fm = F @ m
    mFm = float(m @ Fm)
    A = float((m @ F @ mod.d) / mFm)
    dbase = mod.base.derivative()
    dg = {k: mod.g[k].derivative() for k in KEYS4}
    dh = {k: mod.h[k].derivative() for k in KEYS4}
    g0 = max(s, 0.0)                     #: the clamp model3 itself applies
    dmdS = np.asarray(dbase(s), float).copy()
    for k, v in zip(KEYS4, x4):
        dmdS = dmdS + np.asarray(dg[k](g0), float) * v + 0.5 * np.asarray(dh[k](g0), float) * v * v
    cols = [dmdS]
    for k, v, st in zip(KEYS4, x4, STEP):
        cols.append((np.asarray(mod.g[k](g0), float)
                     + np.asarray(mod.h[k](g0), float) * v) / st)
    D = np.column_stack(cols)
    fisher = (A * A) * (D.T @ (F @ D) - np.outer(D.T @ Fm, D.T @ Fm) / mFm)
    return 0.5 * (fisher + fisher.T), A, float(mod.chi2_cmb(x4, s))


def hessian(mod, x4, sum_ev, ds, dx):
    """the observed Hessian of half the chi-square, CENTRAL in Σ at an interior point"""
    def f(i, idev):
        d = list(x4)
        for j, st in idev:
            d[j] = d[j] + st
        return 0.5 * float(mod.chi2_cmb(d, float(sum_ev) + i * ds))
    H = np.zeros((5, 5))
    f0 = f(0, [])
    H[0, 0] = (f(1, []) - 2 * f0 + f(-1, [])) / (ds * ds)
    for a in range(4):
        H[a + 1, a + 1] = ((f(0, [(a, dx)]) - 2 * f0 + f(0, [(a, -dx)]))
                           / (dx * dx) / (STEP[a] * STEP[a]))
    for a in range(4):
        for b in range(a + 1, 4):
            q = (f(0, [(a, dx), (b, dx)]) - f(0, [(a, dx), (b, -dx)])
                 - f(0, [(a, -dx), (b, dx)]) + f(0, [(a, -dx), (b, -dx)]))
            H[a + 1, b + 1] = H[b + 1, a + 1] = q / (4 * dx * dx) / (STEP[a] * STEP[b])
    for a in range(4):
        q = (f(1, [(a, dx)]) - f(1, [(a, -dx)]) - f(-1, [(a, dx)]) + f(-1, [(a, -dx)]))
        H[0, a + 1] = H[a + 1, 0] = q / (4 * ds * dx) / STEP[a]
    return 0.5 * (H + H.T)


def main():
    print(__doc__)
    print('=' * 100)
    mod = M3.Model3('lcdm')
    L = json.load(io.open(os.path.join(R7888, 'limit_on_runner_grid.json'), encoding='utf-8'))
    P4 = json.load(io.open(os.path.join(R7904, 'fisher_block.json'), encoding='utf-8'))

    rec = {}
    for tag, s, node in POINTS:
        x5 = [float(v) for v in L['calibrated']['x_at_node'][node]]
        fisher, A, chi2 = block_at(mod, x5[:4], s)
        cov = np.linalg.inv(fisher)
        R = corr(cov)
        sig = np.sqrt(np.diag(cov))
        marg, condsig, ratio = degradation(fisher)
        rec[tag] = dict(sum_ev=s, node=node, x5=x5, amplitude=A, chi2_cmb=chi2,
                        phys={k: float(v) for k, v in mod.phys(x5[:4], s).items()},
                        fisher=[[float(v) for v in row] for row in fisher],
                        correlation=[[float(v) for v in row] for row in R],
                        sigma={NAMES[i]: float(sig[i]) for i in range(5)},
                        rho_sigma={NAMES[j]: float(R[0, j]) for j in range(1, 5)},
                        sigma_sum_marginalised=marg, sigma_sum_conditional=condsig,
                        degradation_R=ratio,
                        posdef=bool(np.min(np.linalg.eigvalsh(fisher)) > 0.0))

    # ── Ⓒ⓵ the Σ = 0 block reproduced ENTRY FOR ENTRY through this module's own path ─────────────
    mine = np.asarray(rec['Ⓞ']['fisher'], float)
    theirs = np.asarray(P4['fisher'], float)
    worst = float(np.max(np.abs(mine - theirs)))
    rel = worst / float(np.max(np.abs(theirs)))
    gate('Ⓒ⓵ the Σ = 0 block is REPRODUCED through THIS module\'s own code path, entry for entry '
         'against `r7904`\'s record — which is what makes the three points one measurement rather '
         'than three, so a difference between them cannot be a difference between implementations',
         worst == 0.0,
         'worst absolute difference %.3e over %d entries (relative %.3e)'
         % (worst, mine.size, rel))

    # ── Ⓒ⓶ the clamp, MEASURED on the function — as its PRESENCE, which is exact ────────────────
    #: ⛔ THE FIRST FORM OF THIS GATE WAS MIS-SCOPED, and the first form is stated so the repair can
    #:   be judged. It compared the SIZE of the one-sided-derivative disagreement at the origin
    #:   against the interior points and asked for a factor of a hundred; it measured 4.638e-05
    #:   against 2.194e-06 and 2.136e-06, a factor of about twenty-one, and FAILED. But most of what
    #:   a one-sided difference measures is the function's own curvature, not a kink — so the bar sat
    #:   on a quantity that mixes the two, and the factor of a hundred was invented.
    #: ⛭ AND THE SECOND FORM ASKED FOR EXACT ZERO, WHICH CANNOT HOLD EITHER — reported rather than
    #:   quietly relaxed. The identity is exact in exact arithmetic, but `binned` must ADD the frozen
    #:   direction terms and this test subtracts the base spline again, so the cancellation leaves
    #:   rounding: `3.488e-14` relative. ⇒ *What the measurement shows is the RATIO — ten orders of
    #:   magnitude between the two sides of zero — and that is what the gate reads.*
    #: THE CLAMP'S PRESENCE IS EXACT IN EXACT ARITHMETIC. Below Σ = 0 the direction splines
    #:   are FROZEN at zero, so the whole Σ-dependence of `binned` there is the base spline's: the
    #:   difference of `binned` at two negative sums must EQUAL the difference of `base` at them, to
    #:   the last bit. Between two positive sums it must NOT, because the frozen terms move again.
    print('\nⒸ⓶  THE CLAMP, AS ITS PRESENCE — an identity exact below zero and broken above')
    x4o = [float(v) for v in rec['Ⓞ']['x5'][:4]]

    def frozen_gap(aa, bb):
        """max departure from `binned(a) - binned(b) == base(a) - base(b)`, scaled"""
        db = (np.asarray(mod.base(aa), float) - np.asarray(mod.base(bb), float))
        d = (np.asarray(mod.binned(x4o, aa), float)
             - np.asarray(mod.binned(x4o, bb), float) - db)
        return float(np.max(np.abs(d))) / float(np.max(np.abs(db)))

    gb, ga = frozen_gap(-0.04, -0.02), frozen_gap(0.20, 0.30)
    print('    below zero, Σ = -0.04 against -0.02:  departure from the base-only identity  %.3e' % gb)
    print('    above zero, Σ =  0.20 against  0.30:  departure from the base-only identity  %.3e' % ga)
    gate('Ⓒ⓶ the clamp is ACTIVE below Σ = 0 and INACTIVE above it, measured as an EXACT identity on '
         'the function rather than as the size of a one-sided disagreement: below zero the direction '
         'splines are frozen, so the whole Σ-dependence there is the base spline\'s and the identity '
         'holds there at the FLOOR OF DOUBLE PRECISION while above zero it is broken by ten orders '
         'of magnitude more',
         ga > 1e+08 * gb and gb < 1e-12,
         'below %.3e, which is cancellation; above %.3e, a factor of %.3g' % (gb, ga, ga / gb))

    h = 1e-05
    kink = {}
    for tag, s_, _n in POINTS:
        x4 = [float(v) for v in rec[tag]['x5'][:4]]
        b0 = np.asarray(mod.binned(x4, s_), float)
        right = (np.asarray(mod.binned(x4, s_ + h), float) - b0) / h
        left = (b0 - np.asarray(mod.binned(x4, s_ - h), float)) / h
        kink[tag] = float(np.max(np.abs(right - left)) / float(np.max(np.abs(right))))
    print('    ⌗ and the one-sided disagreement itself, reported with NO bar on it: Σ = 0  %.3e;  '
          'Σ = 0.06  %.3e;  Σ = 0.30  %.3e' % (kink['Ⓞ'], kink['Ⓐ'], kink['Ⓑ']))

    gate('Ⓒ⓷ each point\'s four parameters are READ OUT of `r7888`\'s record at that node and never '
         'typed, and the score at each is reported so the point is identified by what it is',
         all(rec[t]['x5'] == [float(v) for v in L['calibrated']['x_at_node'][n]]
             for t, _s, n in POINTS),
         '; '.join('%s chi2 %.4f, H0 %.5f, NS %.6f'
                   % (t, rec[t]['chi2_cmb'], rec[t]['phys']['H0'], rec[t]['phys']['NS'])
                   for t, _s, _n in POINTS))

    gate('Ⓒ⓸ every block is a symmetric POSITIVE-DEFINITE matrix before any correlation is read '
         'from its inverse, and every correlation below is reported SIGNED. ⌗ *No conditioning bar '
         'is registered: `r7904` established that one on a Fisher block is unit-dependent*',
         all(rec[t]['posdef'] for t, _s, _n in POINTS),
         'smallest eigenvalues %s'
         % ['%.4e' % float(np.min(np.linalg.eigvalsh(np.asarray(rec[t]['fisher'], float))))
            for t, _s, _n in POINTS])

    # ── the reading ─────────────────────────────────────────────────────────────────────────────
    print('\nⓅ⓵  THE THREE POINTS')
    print('      Σ (eV)   rho(Σ,H0)  rho(Σ,Ω_m)  rho(Σ,ω_b)  rho(Σ,n_s)    sigma(Σ) eV        R')
    for tag, s, _n in POINTS:
        r = rec[tag]['rho_sigma']
        print('   %s  %5.2f    %+9.6f   %+9.6f   %+9.6f   %+9.6f    %11.7f  %9.6f'
              % (tag, s, r['H0'], r['OM'], r['WB'], r['NS'],
                 rec[tag]['sigma_sum_marginalised'], rec[tag]['degradation_R']))

    d_wb = abs(rec['Ⓑ']['rho_sigma']['WB']) - abs(rec['Ⓞ']['rho_sigma']['WB'])
    d_ns = abs(rec['Ⓑ']['rho_sigma']['NS']) - abs(rec['Ⓞ']['rho_sigma']['NS'])
    sig_grew = (rec['Ⓑ']['sigma_sum_marginalised'] > rec['Ⓞ']['sigma_sum_marginalised'])
    print('\n    Δrho from Σ = 0 to Σ = 0.30:   omega_b %+.6f    n_s %+.6f' % (d_wb, d_ns))
    print('    sigma(Σ) %.7f → %.7f eV, a factor of %.6f%s'
          % (rec['Ⓞ']['sigma_sum_marginalised'], rec['Ⓑ']['sigma_sum_marginalised'],
             rec['Ⓑ']['sigma_sum_marginalised'] / rec['Ⓞ']['sigma_sum_marginalised'],
             '  (GREW, as registered)' if sig_grew else '  (did NOT grow — the STRONG expectation)'))

    # ── Ⓒ⓹ the Hessian as a convergence check at the loci only ──────────────────────────────────
    print('\nⒸ⓹  THE OBSERVED HESSIAN as a convergence check, at the two interior points, on the '
          'loci the verdict rests on only')
    lad = {}
    for tag, s, _n in POINTS[1:]:
        x4 = [float(v) for v in rec[tag]['x5'][:4]]
        rows = []
        for ds in LADDER:
            H = hessian(mod, x4, s, ds, 2.0 * ds)
            Rh = corr(np.linalg.inv(H))
            rows.append(dict(d_sigma=ds, rho_wb=float(Rh[0, 3]), rho_ns=float(Rh[0, 4]),
                             R=float(degradation(H)[2])))
        lad[tag] = rows
        print('    %s  Σ = %.2f' % (tag, s))
        for r in rows:
            print('        dΣ %8.1e   rho(Σ,ω_b) %+.6f   rho(Σ,n_s) %+.6f   R %.6f'
                  % (r['d_sigma'], r['rho_wb'], r['rho_ns'], r['R']))
    ok = True
    for tag in lad:
        a, b = lad[tag][-1], lad[tag][-2]
        ok = (ok and abs(a['rho_wb'] - b['rho_wb']) < 1e-03
              and abs(a['rho_ns'] - b['rho_ns']) < 1e-03
              and abs(a['R'] - b['R']) / a['R'] < 1e-03)
    gate('Ⓒ⓹ the control route CONVERGES at both interior points on the quantities the verdict uses '
         '— the two named correlations and the degradation factor — and NO bar is placed on the rest '
         'of the matrix, because the Fisher matrix and the observed Hessian are two objects and '
         '`r7904`\'s bar failed for treating them as one',
         ok, '; '.join('%s: the finest two rungs differ by %.1e, %.1e, %.1e'
                       % (t, abs(lad[t][-1]['rho_wb'] - lad[t][-2]['rho_wb']),
                          abs(lad[t][-1]['rho_ns'] - lad[t][-2]['rho_ns']),
                          abs(lad[t][-1]['R'] - lad[t][-2]['R'])) for t in lad))
    for tag in lad:
        fine = lad[tag][-1]
        print('    %s  the two routes at the plateau:  ω_b %+.6f against %+.6f;  n_s %+.6f against '
              '%+.6f;  R %.6f against %.6f'
              % (tag, fine['rho_wb'], rec[tag]['rho_sigma']['WB'],
                 fine['rho_ns'], rec[tag]['rho_sigma']['NS'], fine['R'],
                 rec[tag]['degradation_R']))

    # ── UNREGISTERED: every node the record banked, because reading one costs no solve ──────────
    #: ⛭ SAID TO BE UNREGISTERED. `PREDICTION.md` named two interior points and the verdict is fixed
    #:   by them alone; these nodes cannot change it. They are read because the three registered
    #:   points turn out NOT to locate where the profile is shallow, and saying so while leaving a
    #:   free measurement untaken would be the worse report.
    print('\nⓊ    UNREGISTERED — the same block at EVERY node `r7888` banked')
    print('        Σ (eV)      sigma(Σ) eV    rho(Σ,w_b)   rho(Σ,n_s)         R    a Gaussian from here')
    scan = []
    _dchi = float(L['dchi2'])
    _cross = float(L['calibrated']['crossing_meV'])
    for node in sorted(L['calibrated']['x_at_node'], key=float):
        sv = float(node)
        x5n = [float(v) for v in L['calibrated']['x_at_node'][node]]
        fsh, _A, _c2 = block_at(mod, x5n[:4], sv)
        cv = np.linalg.inv(fsh)
        Rr = corr(cv)
        sg = float(np.sqrt(cv[0, 0]))
        gx = 1000.0 * (sv + float(np.sqrt(_dchi)) * sg)
        scan.append(dict(sum_ev=sv, sigma_sum=sg, rho_wb=float(Rr[0, 3]),
                         rho_ns=float(Rr[0, 4]), R=float(degradation(fsh)[2]),
                         gaussian_from_here_meV=gx))
        print('      %7.3f   %13.7f    %+9.6f    %+9.6f   %9.6f   %14.4f meV'
              % (sv, sg, Rr[0, 3], Rr[0, 4], degradation(fsh)[2], gx))
    _sg = [r['sigma_sum'] for r in scan]
    _mono = bool(np.all(np.diff(_sg) < 0.0)) or bool(np.all(np.diff(_sg) > 0.0))
    _at = float(scan[int(np.argmax(_sg))]['sum_ev'])
    _reach = [r['sum_ev'] for r in scan if r['gaussian_from_here_meV'] >= _cross]
    print('    ⇒ sigma(Σ) is %s in Σ over these nodes, and is LARGEST at Σ = %.3f'
          % ('MONOTONE' if _mono else 'NOT monotone', _at))
    print('      the profile\'s own crossing is %.4f meV; a Gaussian read from a node reaches it '
          'only from Σ >= %s' % (_cross, ('%.3f' % min(_reach)) if _reach else 'no node measured'))
    print('      ⌗ *So the local curvature never accounts for the crossing from below it: that is '
          'the same')
    print('        shortfall `r7904` measured, now shown to persist at every node under the '
          'crossing rather')
    print('        than only at the origin.*')

    # ── UNREGISTERED, AND IT CORRECTS `r7904`: THE SHORTFALL WAS TWO LIKELIHOODS, NOT ONE SHAPE ──
    #: ⛔ `r7904` reported, unregistered, that the local reading of the limit falls 43.67255 meV short
    #:   of the profile's own crossing, and read that as the profile being wider above its minimum
    #:   than its curvature allows. ** THAT COMPARISON CROSSED TWO LIKELIHOODS. ** This block is
    #:   `chi2_cmb`: 555 CMB bandpowers, five parameters, no more. `r7888`'s crossing is read on
    #:   `Model6.chi2`, which is `Model3.chi2(..., bao=True)` PLUS a lensing likelihood PLUS a tau
    #:   prior, over SIX parameters — tau being the sixth, which is the fifth entry of every
    #:   `x_at_node` and sits near 0.054 at every node.
    #: ⇒ *So the right test is INSIDE ONE OBJECT: read the profile's own curvature from the profile's
    #:   OWN delta-chi-square values and see whether it accounts for its own crossing.* No Fisher is
    #:   needed and nothing is re-solved; the record already carries the numbers.
    print('\nⓋ    UNREGISTERED — A CORRECTION TO `r7904`: the profile\'s own curvature, from its own values')
    _ss = np.asarray(L['calibrated']['sums'], float)
    _dd = np.asarray(L['calibrated']['delta'], float)
    _k = int(np.argmin(_dd))
    own = []
    for n in (3, 5, 6):
        sel = list(range(max(0, _k - (n // 2)), min(len(_ss), _k + (n // 2) + 1)))
        aa, bb, _cc = np.polyfit(_ss[sel], _dd[sel], 2)
        v = -bb / (2.0 * aa)
        sg = 1.0 / float(np.sqrt(aa))
        gx = 1000.0 * (v + float(np.sqrt(_dchi)) * sg)
        own.append(dict(nodes=len(sel), vertex=float(v), sigma=sg, crossing_meV=float(gx)))
        print('    a parabola on %d node(s) about the minimum:  vertex %.6f eV,  sigma %.6f eV,  '
              'crossing %.4f meV' % (len(sel), v, sg, gx))
    print('    the profile\'s OWN crossing:                                                      '
          '      %.4f meV' % _cross)
    print('    the CMB-only block\'s sigma at the same node, for contrast:  %.7f eV  ->  %.4f meV'
          % (rec['Ⓐ']['sigma_sum_marginalised'],
             1000.0 * (0.06 + float(np.sqrt(_dchi)) * rec['Ⓐ']['sigma_sum_marginalised'])))
    _span = (min(o['crossing_meV'] for o in own), max(o['crossing_meV'] for o in own))
    _accounted = _span[0] <= _cross <= _span[1]
    print('    ⇒ the profile\'s own curvature puts its crossing in [%.4f, %.4f] meV across those '
          'three fits,' % _span)
    print('      and the actual crossing is %.4f — %s.'
          % (_cross, 'INSIDE that range' if _accounted else 'OUTSIDE it'))
    print('      ⛔ *So `r7904`\'s shortfall was NOT the profile\'s shape. It was a CMB-only')
    print('        five-parameter sigma extrapolated against a crossing read on CMB plus BAO plus')
    print('        lensing plus a tau prior over six parameters: one label, two likelihoods. The')
    print('        profile is accounted for by its own curvature, and that sentence of `r7904` is')
    print('        withdrawn here rather than left standing.*')

    out = verdict(d_wb, d_ns, rec['Ⓐ']['degradation_R'], rec['Ⓑ']['degradation_R'])
    print('\n  OUTCOME  %s' % ' + '.join(out['outcomes']))
    print('  %s' % out['note'])

    io.open(os.path.join(HERE, 'interior_block.json'), 'w', encoding='utf-8').write(
        json.dumps(dict(points=rec, delta_rho=dict(WB=float(d_wb), NS=float(d_ns)),
                        sigma_grew=bool(sig_grew), clamp=kink, ladder=lad,
                        reproduced_r7904_worst=worst, names=NAMES, pretty=PRETTY,
                        correction_to_r7904=dict(own_curvature=own, span_meV=list(_span),
                                                 crossing_meV=_cross, accounted=bool(_accounted),
                                                 cmb_only_sigma_at_min=rec['Ⓐ']['sigma_sum_marginalised']),
                        unregistered=dict(scan=scan, sigma_monotone=_mono,
                                          sigma_largest_at=_at,
                                          gaussian_reaches_from=(min(_reach) if _reach else None),
                                          clamp_identity_below=gb,
                                          clamp_identity_above=ga, clamp_onesided=kink),
                        bars=dict(grow=GROW_BAR, flat=FLAT_BAR, R_strong=R_STRONG, R_null=R_NULL),
                        ran=RAN, failed=FAILS, **out),
                   indent=1, ensure_ascii=False, sort_keys=True))
    print('\n  wrote interior_block.json')
    print('  ran %d gate(s), %d failed%s' % (len(RAN), len(FAILS),
                                             (': ' + ', '.join(FAILS)) if FAILS else ''))
    return 1 if FAILS else 0


def verdict(d_wb, d_ns, r_a, r_b):
    """PURE. The registered outcome glyphs, from the registered bars and the measured numbers only."""
    outs = []
    if d_wb >= GROW_BAR or d_ns >= GROW_BAR:
        outs.append('Ⓟ⓵')
    if d_wb <= -FLAT_BAR or d_ns <= -FLAT_BAR:
        outs.append('Ⓟ⓸')
    if not outs:
        outs.append('Ⓟ⓶' if (abs(d_wb) < FLAT_BAR and abs(d_ns) < FLAT_BAR) else 'Ⓟ⓷')
    outs.append('Ⓝ⓵' if max(r_a, r_b) >= R_STRONG
                else ('Ⓝ⓶' if max(r_a, r_b) < R_NULL else 'Ⓝ⓷'))
    return dict(outcomes=outs, note='omega_b %+.6f and n_s %+.6f against a grow bar of %.2f and a '
                                    'flat bar of %.2f; R %.6f and %.6f'
                                    % (d_wb, d_ns, GROW_BAR, FLAT_BAR, r_a, r_b))


if __name__ == '__main__':
    sys.exit(main())
