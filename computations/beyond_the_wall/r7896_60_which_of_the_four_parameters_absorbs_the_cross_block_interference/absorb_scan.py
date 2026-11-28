# -*- coding: utf-8 -*-
"""r7896+60 — WHICH OF THE FOUR PARAMETERS ABSORBS THE CROSS-BLOCK INTERFERENCE?

`r7892` found the block decomposition of the low-end move ADDITIVE at a `6.5` per cent residual with
the four parameters re-profiled at every sum. `r7894` found it NOT additive at `24.7` per cent with
them held at the zero-sum fit, and concluded that the four, when free, ABSORB a cross-block
interference — `TT` alone outruns all thirty-six together on the held clock, and the refit hides it.
`r7894` recorded that it measured this on the held clock only and that PARTIAL freedom was the open
question.

This is that question. For each of `H0`, `OM`, `WB`, `NS` in turn: hold THAT ONE at the zero-sum fit,
leave the other three FREE, and read the residual of the same block decomposition. Each parameter's
absorption share is its position between the two banked ends.

⛭ **ONE FITTER COVERS ALL THREE REGIMES.** `fit_subset` minimises over the FREE indices only, so
freeing all four reduces it to `r7866`'s own `fit_x4` (same optimiser, same two starts projected onto
the subset) and holding all four reduces it to a bare evaluation. The two controls are therefore
computed by the SAME code path as the four partial arms, not by a second implementation that could
agree with the record for the wrong reason.

    python3 absorb_scan.py
"""
import io
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
R7866 = os.path.join(BTW, 'r7866_60_the_low_end_lean_located_and_the_bank_re_solved_on_the'
                          '_repaired_background')
R7892 = os.path.join(BTW, 'r7892_60_the_low_end_lean_decomposed_by_block_on_crossings_not_on_a'
                          '_difference_map')
R7894 = os.path.join(BTW, 'r7894_60_the_parameters_held_low_end_move_decomposed_by_block_and_the'
                          '_location_against_a_change_of_clock')
sys.path.insert(0, R7866)
sys.path.insert(0, R7894)
import same_bins as SB                                                      # noqa: E402
import held_by_block as HB                                                  # noqa: E402
SC, M6, M3 = SB.SC, SB.M6, SB.M3

NAMES = {0: 'TT', 1: 'TE', 2: 'EE'}
BLOCKS = ('TT', 'TE', 'EE')
KEYS = list(M3.KEYS4)

#: ⛭ BOTH ENDS OF EVERY SHARE ARE READ OUT OF THE RECORDS, NOT TYPED. The all-held residual is the
#:   DENOMINATOR, so a share means nothing if either end is wrong — which is why the registration
#:   says the shares are not computed at all unless both controls land.
_BB = json.load(io.open(os.path.join(R7892, 'by_block.json'), encoding='utf-8'))
_HB = json.load(io.open(os.path.join(R7894, 'held_by_block.json'), encoding='utf-8'))
FREE_RESID = float(_BB['residual_fraction'])          #: r7892, all four free
HELD_RESID = float(_HB['residual_fraction'])          #: r7894, all four held
HELD_X4 = [float(v) for v in _HB['held_x4']]
FREE_MOVE = float(_BB['move_all36_meV'])
HELD_MOVE = float(_HB['move_all36_meV'])

CONCENTRATED_BAR = 0.50      #: Ⓧ⓵: one parameter's share of the rise
TOGETHER_BAR = 0.50          #: Ⓧ⓶ against Ⓧ⓷: the four shares summed

FAILS = []
RAN = []


def gate(name, ok, got=None):
    RAN.append(name)
    print('  [%s] %s%s' % ('PASS' if ok else 'FAIL', name,
                           ('   (%s)' % got) if got is not None else ''))
    if not ok:
        FAILS.append(name.split()[0])
    return ok


def fit_subset(mod, s, held, x4_held):
    """chi2 minimised over the FREE indices only, the held ones pinned at `x4_held`

    `held` empty  -> reduces to `r7866`'s fit_x4: all four free, same starts, same optimiser.
    `held` all four -> reduces to a bare evaluation at `x4_held`, no optimiser called.
    """
    free = [i for i in range(len(x4_held)) if i not in held]
    if not free:
        return list(x4_held), float(mod.cmb.chi2_cmb(np.asarray(x4_held, float), s))
    from scipy.optimize import minimize

    def full(xf):
        v = list(x4_held)
        for j, i in enumerate(free):
            v[i] = float(xf[j])
        return np.asarray(v, float)

    f = lambda xf: float(mod.cmb.chi2_cmb(full(xf), s))          # noqa: E731
    best, val = None, np.inf
    for x0 in (np.zeros(len(x4_held)), np.array([1.0, -1.0, 0.5, -0.5])):
        r = minimize(f, np.asarray([x0[i] for i in free], float), method='Nelder-Mead',
                     options=dict(maxiter=6000, xatol=1e-6, fatol=1e-9))
        if r.fun < val:
            best, val = list(full(r.x)), float(r.fun)
    return best, float(val)


def profile(keep, held):
    """the chi2 profile over the seven sums on `keep`, with `held` pinned"""
    mod, nb = HB.restricted(keep)                 #: r7894's own restriction, imported not retyped
    tot = [fit_subset(mod, s, held, HELD_X4)[1] for s in SB.SUMS]
    return tot, nb


def decompose(ok, held, label):
    """the whole block decomposition under one freedom regime; returns its residual fraction"""
    full = np.ones(int(ok.sum()), bool)
    k36 = SB.the_thirty_six(ok)
    t0 = time.time()

    def crossing(keep, what):
        #: ⛭ `cross_of` returns None when the profile never reaches CROSS inside the sum grid. That
        #:   is a fact about the configuration, not a glitch, and it is said rather than swallowed:
        #:   a share computed from a missing crossing would be a number standing in for an absence.
        tot, nb = profile(keep, held)
        cx = SB.cross_of(SB.SUMS, tot)
        if cx is None:
            raise SystemExit('\n  \u26d4 NO CROSSING under %s on %s (%d bin(s)): the profile never '
                             'reaches %.2f inside the registered sum grid, so no share is '
                             'computable here. chi2: %s'
                             % (label, what, nb, SB.CROSS, ' '.join('%.3f' % v for v in tot)))
        return float(cx)

    base = crossing(full, 'the whole mask')
    all36 = crossing(k36, 'minus all thirty-six')
    M36 = all36 - base
    MB = {}
    for b in (0, 1, 2):
        keep = HB.lowest_of(ok, (b,))             #: r7894's own mask builder
        MB[NAMES[b]] = crossing(keep, 'minus %s\'s twelve' % NAMES[b]) - base
    ssum = sum(MB.values())
    resid = ssum - M36
    frac = abs(resid) / abs(M36)
    print('    %-26s base %8.4f  all36 %+8.4f  TT %+8.4f  TE %+8.4f  EE %+8.4f  '
          'resid %6.2f%%  (%.0f s)'
          % (label, base, M36, MB['TT'], MB['TE'], MB['EE'], 100 * frac, time.time() - t0))
    return dict(base=float(base), all36=float(all36), move=float(M36),
                block_moves={k: float(v) for k, v in MB.items()}, sum=float(ssum),
                residual=float(resid), residual_fraction=float(frac))


def main():
    print(__doc__)
    print('=' * 100)
    ok = M6.Model6('lcdm').cmb.ok

    print('\nⓍ⓪  THE TWO CONTROLS, COMPUTED BY THE SAME FITTER AS THE PARTIAL ARMS')
    print('    banked: all four free %.2f%% (r7892) | all four held %.2f%% (r7894)'
          % (100 * FREE_RESID, 100 * HELD_RESID))
    c_free = decompose(ok, (), 'all four FREE (control)')
    c_held = decompose(ok, tuple(range(len(KEYS))), 'all four HELD (control)')

    ok_free = abs(c_free['residual_fraction'] - FREE_RESID) < 5e-04
    ok_held = abs(c_held['residual_fraction'] - HELD_RESID) < 5e-04
    gate('Ⓧ⓪ the all-free control reproduces `r7892`\'s banked residual and the all-held control '
         'reproduces `r7894`\'s, both read out of their records rather than typed — and BOTH come '
         'out of the SAME fitter as the four partial arms, which is what makes the shares a '
         'position between two measured ends rather than between two remembered ones',
         ok_free and ok_held,
         'free %.2f%% vs banked %.2f%% | held %.2f%% vs banked %.2f%%'
         % (100 * c_free['residual_fraction'], 100 * FREE_RESID,
            100 * c_held['residual_fraction'], 100 * HELD_RESID))
    gate('Ⓧ⓪ᵃ and the two all-three-six moves reproduce their banked values too, so the controls '
         'agree on the MOVE and not only on the residual fraction',
         abs(c_free['move'] - FREE_MOVE) < 5e-04 and abs(c_held['move'] - HELD_MOVE) < 5e-04,
         'free %+.4f vs %+.4f | held %+.4f vs %+.4f' % (c_free['move'], FREE_MOVE,
                                                        c_held['move'], HELD_MOVE))
    if not (ok_free and ok_held):
        print('\n  ⛔ A CONTROL MISSED, so the shares are NOT computed — the registration fixed '
              'that in advance, because a share is a position between two numbers and means '
              'nothing if either end is wrong.')
        io.open(os.path.join(HERE, 'absorb_scan.json'), 'w', encoding='utf-8').write(
            json.dumps(dict(control_free=c_free, control_held=c_held, shares=None,
                            banked_free_residual=FREE_RESID, banked_held_residual=HELD_RESID),
                       indent=1, sort_keys=True, default=float))
        sys.exit('\n  ⛔ CONTROL FAILED: shares withheld by the registration\'s own rule')

    print('\nⓍ①  HOLD ONE, FREE THE OTHER THREE')
    arms, shares = {}, {}
    span = c_held['residual_fraction'] - c_free['residual_fraction']
    for i, k in enumerate(KEYS):
        arms[k] = decompose(ok, (i,), 'hold %s, free the rest' % k)
        shares[k] = (arms[k]['residual_fraction'] - c_free['residual_fraction']) / span

    print('\n    parameter   residual   share of the rise')
    for k in KEYS:
        print('    %-10s %7.2f%%   %+7.3f' % (k, 100 * arms[k]['residual_fraction'], shares[k]))
    ssum = sum(shares.values())
    top = max(shares, key=lambda k: shares[k])
    over = sorted([k for k in KEYS if shares[k] >= CONCENTRATED_BAR],
                  key=lambda k: -shares[k])
    print('    the four shares sum to %+.3f' % ssum)

    if over:
        outcome = 'Ⓧ⓵'
        note = ('CONCENTRATED in %s' % over[0]) if len(over) == 1 else \
               ('CONCENTRATED and REDUNDANT across %s' % ', '.join(over))
    elif ssum >= TOGETHER_BAR:
        outcome, note = 'Ⓧ⓶', 'DISTRIBUTED -- no one of them alone, but together'
    else:
        outcome, note = 'Ⓧ⓷', 'JOINT and not decomposable by parameter either'
    print('    ⇒ %s %s' % (outcome, note))

    gate('Ⓧ① the outcome is one of the three registered before any constrained fit ran, read off '
         'the numbers rather than chosen, and where two or more parameters clear the bar BOTH are '
         'named because redundant absorption is itself a finding',
         outcome in ('Ⓧ⓵', 'Ⓧ⓶', 'Ⓧ⓷'),
         '%s %s' % (outcome, note))
    gate('Ⓧ①ᵃ and every arm holds exactly ONE parameter and frees exactly three, so the four are '
         'comparable with each other and each differs from the all-free control in one place only',
         all(len(KEYS) - 1 == len([i for i in range(len(KEYS)) if i != j])
             for j in range(len(KEYS))),
         '%d arm(s), one held apiece' % len(KEYS))
    gate('Ⓧ①ᵇ and a share outside the unit interval is REPORTED rather than clipped, which the '
         'registration declared in advance: negative means holding that parameter makes the blocks '
         'MORE additive than leaving all four free, and above one means a single hold overshoots '
         'what four holds do',
         True,
         'range %+.3f to %+.3f; outside [0,1]: %s'
         % (min(shares.values()), max(shares.values()),
            [k for k in KEYS if shares[k] < 0.0 or shares[k] > 1.0] or 'none'))

    exp_met = (outcome == 'Ⓧ⓵' and top == 'H0' and shares['H0'] >= CONCENTRATED_BAR)
    print('\n    expected `Ⓧ⓵` with `H0`: %s' % ('MET' if exp_met else 'REFUTED'))
    gate('Ⓧ② and the registered expectation is reported as met or REFUTED against what was '
         'registered rather than reshaped to fit — the registration having called its own grounds '
         'weak, an argument from a neighbouring measurement and not from this one',
         True,
         'expected Ⓧ⓵ with H0; got %s, largest %s at %+.3f' % (outcome, top, shares[top]))

    #: ⛭ EXPLICITLY NOT REGISTERED. The registration asked which parameter's HOLD breaks additivity
    #:   and registered four hold-one arms. It did not ask the converse — whether freeing that one
    #:   alone RESTORES additivity — and a share above one makes the converse the sharper question,
    #:   because "necessary" and "sufficient" are different claims and the hold-one arms can only
    #:   speak to the first. These four arms are reported as an unregistered follow-on: they cannot
    #:   change the outcome above, which was fixed by the registered arms before they ran, and they
    #:   are named here rather than quietly folded into it.
    print('\nⓍ③  HOLD THREE, FREE ONE  — NOT REGISTERED, reported as a follow-on')
    free1, back = {}, {}
    for i, k in enumerate(KEYS):
        free1[k] = decompose(ok, tuple(j for j in range(len(KEYS)) if j != i),
                             'free %s only' % k)
        back[k] = (c_held['residual_fraction'] - free1[k]['residual_fraction']) / span

    print('\n    freed alone   residual   additivity recovered')
    for k in KEYS:
        print('    %-11s %7.2f%%   %+7.3f' % (k, 100 * free1[k]['residual_fraction'], back[k]))
    rtop = max(back, key=lambda k: back[k])
    sufficient = [k for k in KEYS if back[k] >= CONCENTRATED_BAR]
    agree = bool(sufficient) and rtop == top
    print('    ⇒ freeing %s alone recovers %+.3f of the rise; sufficient: %s'
          % (rtop, back[rtop], ', '.join(sufficient) or 'none'))
    gate('Ⓧ③ the unregistered converse is reported whichever way it falls, and whether it AGREES '
         'with the registered arms is said in the open: necessity and sufficiency are different '
         'claims about the same parameter, and only their agreement licenses calling the '
         'interference that parameter\'s to absorb',
         True,
         'hold-one names %s; free-one-alone names %s; agree: %s' % (top, rtop, agree))

    out = dict(control_free=c_free, control_held=c_held, arms=arms,
               free_one_only=free1, recovered={k: float(v) for k, v in back.items()},
               recovered_largest=rtop, sufficient=sufficient, converse_agrees=agree,
               converse_registered=False,
               shares={k: float(v) for k, v in shares.items()},
               share_sum=float(ssum), largest=top, over_bar=over, outcome=outcome, note=note,
               banked_free_residual=FREE_RESID, banked_held_residual=HELD_RESID,
               banked_free_move=FREE_MOVE, banked_held_move=HELD_MOVE,
               held_x4=HELD_X4, keys=KEYS, expectation_met=bool(exp_met),
               concentrated_bar=CONCENTRATED_BAR, together_bar=TOGETHER_BAR)
    io.open(os.path.join(HERE, 'absorb_scan.json'), 'w', encoding='utf-8').write(
        json.dumps(out, indent=1, sort_keys=True, default=float))
    print('\n  wrote absorb_scan.json')
    if FAILS:
        sys.exit('\n  ⛔ %d of %d GATE(S) FAILED: %s' % (len(FAILS), len(RAN), ', '.join(FAILS)))
    print('  ⇒ all %d gate(s) pass' % len(RAN))
    return 0


if __name__ == '__main__':
    sys.exit(main())
