# -*- coding: utf-8 -*-
"""r7892+60 — THE LOW-END LEAN DECOMPOSED BY BLOCK, ON CROSSINGS AND NOT ON A DIFFERENCE MAP.

`r7866` located the lean: removing the same thirty-six bins moves the instrument's crossing by
`-20.09` meV against the reference's `-0.12`, a factor of `162` on identical bins. Two thirds of that
move has no named mechanism -- `tau` is out structurally, the late ISW is unreadable on this mask, and
the lensing amplitude carries `33` per cent.

⛔ **AND `r7890` RULED OUT THE OBVIOUS NEXT INSTRUMENT.** The per-band difference map cannot localise
anything: the same-clock operator converges to the exact derivative in NO band, settling to a
band-dependent signed offset that is SEVEN TIMES the signal in the band `r7866` picked out. But
`-20.09` meV is a CROSSING computed from profiles, which `r7890` left untouched. **So this
decomposition is built out of crossings.**

The thirty-six are the twelve lowest bandpowers of EACH of three blocks, so the move splits by block:
all thirty-six as the control, then TT only, TE only, EE only. `r7866`'s `same_bins.py` is IMPORTED
and its mask builder, profiler and crossing reader reused; nothing is retyped.

    python3 by_block.py
"""
import io
import ast
import re
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
R7866 = os.path.join(BTW, 'r7866_60_the_low_end_lean_located_and_the_bank_re_solved_on_the'
                          '_repaired_background')
sys.path.insert(0, R7866)
import same_bins as SB                                                      # noqa: E402
SC, M6 = SB.SC, SB.M6

NAMES = {0: 'TT', 1: 'TE', 2: 'EE'}

#: ⛭ THE CONTROL TARGET IS READ OUT OF `r7866`'s OWN RECORD, NOT TYPED HERE.
#:   `PREDICTION.md` named `-20.09` meV, and the registered refusal FIRED on `+48.20`. The gate was
#:   right and the registration was wrong: `r7866` banks TWO moves on these same thirty-six bins --
#:   `moves_meV.instrument_frozen = -20.0868` with the four parameters HELD as the reference's are,
#:   and `moves_meV.instrument = -48.2020` with its own four RE-PROFILED at every sum. `inst_profile`
#:   re-profiles, so it computes the SECOND row, and the registration named the first.
#:   ⇒ *Reading the target out of `same_bins.json` instead of typing it ties the comparison to the
#:   machinery: whichever row the profiler computes, the control is that row's banked value, and the
#:   row cannot be mis-named again. This is a MIS-SPECIFIED CONTROL CORRECTED, not a bar loosened --
#:   the bar is still `0.5` meV and both crossings are now checked too, which is stricter than the
#:   single move comparison the registration asked for.*
_SB = json.load(io.open(os.path.join(R7866, 'same_bins.json'), encoding='utf-8'))
R7866_WHOLE = float(_SB['instrument_whole']['crossing_meV'])
R7866_MINUS36 = float(_SB['instrument_minus36']['crossing_meV'])
R7866_MOVE = float(_SB['moves_meV']['instrument'])
R7866_FROZEN_MOVE = float(_SB['moves_meV']['instrument_frozen'])
ADDITIVE_BAR = 0.10                  #: Ⓚ⓵: the residual, as a fraction of the whole move
CONCENTRATED_BAR = 0.80              #: Ⓚ⓶: one block's share of the whole move

FAILS = []


def gate(name, ok, got=None):
    print('  [%s] %s%s' % ('PASS' if ok else 'FAIL', name,
                           ('   (%s)' % got) if got is not None else ''))
    if not ok:
        FAILS.append(name.split()[0])
    return ok


def lowest_of(ok, blocks):
    """the twelve lowest-`BIN_LO` bandpowers of each named block dropped; others kept"""
    keep = np.ones(int(ok.sum()), bool)
    blk, lo = SC.BLOCK[ok], SC.BIN_LO[ok]
    for b in blocks:
        idx = np.where(blk == b)[0]
        keep[idx[np.argsort(lo[idx], kind='stable')][:SB.N_PER_BLOCK]] = False
    return keep


def move_for(keep, label):
    """the crossing with `keep`, against the crossing on the whole mask, in meV"""
    prof, nb = SB.inst_profile(keep)
    cx = SB.cross_of(SB.SUMS, prof)
    print('    %-22s %d bin(s) kept, chi2 at the seven sums %s'
          % (label, nb, ' '.join('%.2f' % v for v in prof)))
    return cx, nb, prof


def main():
    print(__doc__)
    print('=' * 100)

    mod = M6.Model6('lcdm')
    ok = mod.cmb.ok
    full = np.ones(int(ok.sum()), bool)

    # ══ Ⓚ⓪ THE MASK IS THE ONE r7866 NAMED ═════════════════════════════════════════════════════
    print('\nⓀ⓪  THE THIRTY-SIX ARE TWELVE PER BLOCK, READ OFF THE MASK')
    k36 = SB.the_thirty_six(ok)
    blk = SC.BLOCK[ok]
    per_block = {NAMES[b]: int((~k36 & (blk == b)).sum()) for b in (0, 1, 2)}
    gate('Ⓚ⓪ the all-three mask drops exactly twelve bandpowers from each of the three blocks, '
         'thirty-six in all -- read off the mask rather than assumed',
         sum(per_block.values()) == 36 and set(per_block.values()) == {SB.N_PER_BLOCK},
         '%s' % per_block)
    #: and the single-block masks agree with it where they overlap
    singles = {b: lowest_of(ok, (b,)) for b in (0, 1, 2)}
    agree = all(((~singles[b]) == (~k36 & (blk == b))).all() for b in (0, 1, 2))
    gate('Ⓚ⓪ᵃ and each single-block mask drops EXACTLY the bins the all-three mask drops from that '
         'block, so the three are a partition of the thirty-six and not three differently-chosen '
         'twelves', agree,
         '; '.join('%s %d' % (NAMES[b], int((~singles[b]).sum())) for b in (0, 1, 2)))

    # ══ THE CROSSINGS ══════════════════════════════════════════════════════════════════════════
    print('\n  THE PROFILES — four parameters re-fit at each of the seven banked sums, per mask')
    print('  ' + '-' * 98)
    base_cx, nb0, _ = move_for(full, 'the whole mask')
    all_cx, _, _ = move_for(k36, 'minus all thirty-six')
    blocks = {}
    for b in (0, 1, 2):
        cx, nb, _ = move_for(singles[b], 'minus %s\'s twelve' % NAMES[b])
        blocks[NAMES[b]] = cx

    if base_cx is None or all_cx is None or any(v is None for v in blocks.values()):
        sys.exit('\n  ⛔ A PROFILE PRODUCED NO CROSSING on the seven banked sums. ** A missing '
                 'crossing is NOT a zero move and is not read as one. ** No decomposition is '
                 'reported: base %s, all-36 %s, blocks %s'
                 % (base_cx, all_cx, {k: v for k, v in blocks.items()}))

    M36 = all_cx - base_cx
    MB = {k: v - base_cx for k, v in blocks.items()}
    print('\n  THE MOVES, each a crossing difference against the whole mask')
    print('    the whole mask crosses at      %8.2f meV' % base_cx)
    print('    minus all thirty-six           %8.2f meV   move %+8.2f' % (all_cx, M36))
    for k in ('TT', 'TE', 'EE'):
        print('    minus %s\'s twelve             %8.2f meV   move %+8.2f'
              % (k, blocks[k], MB[k]))

    # ══ Ⓚ① THE CONTROL ════════════════════════════════════════════════════════════════════════
    print('\nⓀ①  THE CONTROL — does the all-three move reproduce r7866?')
    gate('Ⓚ① ⛔ THE REGISTERED CONTROL FIRED, AND IT WAS RIGHT: `PREDICTION.md` named `-20.09` meV, '
         'which is `r7866`\'s PARAMETERS-HELD row, while this profiler RE-PROFILES the four at every '
         'sum and so computes its other row. The control is now read out of `r7866`\'s own record '
         'rather than typed, so the row cannot be mis-named again -- and BOTH crossings are checked, '
         'not just the move, which is stricter than the registration asked for',
         abs(abs(M36) - abs(R7866_MOVE)) < 0.5
         and abs(base_cx - R7866_WHOLE) < 0.01 and abs(all_cx - R7866_MINUS36) < 0.01,
         'whole %.4f vs banked %.4f; minus36 %.4f vs banked %.4f; |move| %.4f vs banked |%.4f| '
         '(the frozen row, which the registration named, is %.4f)'
         % (base_cx, R7866_WHOLE, all_cx, R7866_MINUS36, abs(M36), abs(R7866_MOVE),
            R7866_FROZEN_MOVE))

    gate('Ⓚ①ᵃ and the sign convention is reconciled rather than silently differing: `r7866` reports '
         'these moves NEGATIVE, this reads the crossing difference POSITIVE, and the crossing rises '
         'when the bins are removed. ⇒ *Same quantity, opposite sign convention, stated*',
         M36 > 0 and R7866_MOVE < 0 and all_cx > base_cx,
         'crossing %.2f -> %.2f, so removing the bins RAISES it by %+.2f; r7866 signs that %.2f'
         % (base_cx, all_cx, M36, R7866_MOVE))

    # ══ Ⓚ② THE REGISTERED OUTCOMES, READ OFF THE NUMBERS ══════════════════════════════════════
    print('\nⓀ②  THE REGISTERED OUTCOMES, read off the numbers rather than chosen')
    ssum = sum(MB.values())
    resid = abs(ssum - M36)
    frac = resid / max(abs(M36), 1e-30)
    shares = {k: v / M36 for k, v in MB.items()}
    top = max(shares, key=lambda k: shares[k])
    additive = frac < ADDITIVE_BAR
    concentrated = shares[top] >= CONCENTRATED_BAR
    print('    the three single-block moves sum to %+8.2f against the whole %+8.2f' % (ssum, M36))
    print('    residual %8.2f meV = %.1f per cent of the whole move   (Ⓚ⓵ bar: %.0f per cent)'
          % (resid, 100.0 * frac, 100.0 * ADDITIVE_BAR))
    for k in ('TT', 'TE', 'EE'):
        print('    %s carries %+7.1f per cent of the whole move' % (k, 100.0 * shares[k]))
    states = []
    if additive:
        states.append('Ⓚ⓵ ADDITIVE -- the blocks act independently and `%s` is the largest' % top)
    if concentrated:
        states.append('Ⓚ⓶ CONCENTRATED -- `%s` alone carries %.0f per cent'
                      % (top, 100.0 * shares[top]))
    if not states:
        states.append('Ⓚ⓷ NON-ADDITIVE -- the blocks interact through the shared four-parameter '
                      'profile, so no per-block attribution is available; the next instrument must '
                      'break the PARAMETERS rather than the bins')
    for st in states:
        print('    ⇒ %s' % st)
    gate('Ⓚ② the outcome is one of the three registered before any profile ran, and where two fire '
         'BOTH are reported rather than one chosen. ⌗ *The registration said they are not exclusive '
         'by construction and that choosing between them after the numbers are seen is what is '
         'excluded*', bool(states), ' + '.join(s.split(' --')[0] for s in states))

    # ══ Ⓚ③ THE REGISTERED EXPECTATION, AND WHETHER IT SURVIVED ════════════════════════════════
    print('\nⓀ③  THE REGISTERED EXPECTATION — `Ⓚ⓷` non-additive, and weakly EE if one dominates')
    exp_met = (not additive) and (not concentrated)
    weak_met = (top == 'EE') if concentrated or additive else None
    print('    expected `Ⓚ⓷`: %s' % ('MET' if exp_met else 'REFUTED -- it is %s'
                                     % ' + '.join(s.split(' --')[0] for s in states)))
    print('    the weak expectation that EE dominates if one block does: %s'
          % ('MET' if weak_met else ('REFUTED -- it is %s' % top) if weak_met is False
             else 'not reached, no single block dominates'))
    gate('Ⓚ③ the expectation is reported as met or REFUTED against what was registered, not '
         'reshaped to fit. ⌗ *The registration said a refutation here is the BETTER outcome, because '
         'it hands the next step a named block instead of a harder instrument*', True,
         'Ⓚ⓷ %s; weak EE %s' % ('met' if exp_met else 'refuted', weak_met))

    # ══ Ⓚ④ WHERE THE CARRYING BLOCK'S TWELVE SIT -- NOT REGISTERED, MEASURED AFTER THE OUTCOME ══
    print('\nⓀ④  THE TWELVE THE CARRYING BLOCK DROPS, AGAINST r7866\'S OWN SUB-PEAK COUNT')
    _csrc = io.open(os.path.join(R7866, 'candidates.py'), encoding='utf-8').read()
    _fp = [n.value.value for n in ast.walk(ast.parse(_csrc))
           if isinstance(n, ast.Assign) and any(getattr(t, 'id', None) == 'FIRST_PEAK' for t in n.targets)
           and isinstance(n.value, ast.Constant)]
    FIRST_PEAK = int(_fp[0]) if _fp else -1
    _rmd = re.sub(r'\s+', ' ', io.open(os.path.join(R7866, 'RESULT.md'), encoding='utf-8').read())
    _m = re.search(r'only `(\d+)` TT bins below the first peak', _rmd)
    R7866_SUBPEAK = int(_m.group(1)) if _m else -1

    TOPB = {v: k for k, v in NAMES.items()}[top]
    _blk, _lo, _hi = SC.BLOCK[ok], SC.BIN_LO[ok], SC.BIN_HI[ok]
    _tt = (_blk == TOPB)
    _sub = _tt & (_hi < FIRST_PEAK)                 # r7866's own criterion: the bin lies WHOLLY below
    _drop = (~k36) & _tt                            # the twelve this revision's carrying block drops
    n_sub, n_drop = int(_sub.sum()), int(_drop.sum())
    n_both = int((_sub & _drop).sum())
    n_sub_only = int((_sub & ~_drop).sum())
    n_drop_only = int((_drop & ~_sub).sum())
    print('    the criterion is `BIN_HI < %d`, read out of r7866\'s own source' % FIRST_PEAK)
    print('    TT bins wholly below the first peak   %3d   (r7866\'s record says %d)' % (n_sub, R7866_SUBPEAK))
    print('    the carrying block `%s` drops          %3d' % (NAMES[TOPB], n_drop))
    print('    in both                               %3d' % n_both)
    print('    below the peak and KEPT               %3d   -> %s'
          % (n_sub_only, [(int(a), int(b)) for a, b in zip(_lo[_sub & ~_drop], _hi[_sub & ~_drop])]))
    print('    dropped and NOT wholly below          %3d' % n_drop_only)

    gate('Ⓚ④ the sub-peak criterion is r7866\'s own, parsed from its source and its record rather than '
         'retyped here, and the recount reproduces the number that record carries. ⌗ *The sub-peak set is '
         '`TT`\'s by construction, so this comparison is only about the carrying block because the carrying '
         'block IS `TT` -- asserted here rather than assumed, so a re-measure that moved the lean to another '
         'block fires this gate instead of silently comparing two different blocks*',
         FIRST_PEAK == 220 and R7866_SUBPEAK > 0 and n_sub == R7866_SUBPEAK and NAMES[TOPB] == 'TT',
         'FIRST_PEAK=%d, recount %d, record %d, carrying block %s'
         % (FIRST_PEAK, n_sub, R7866_SUBPEAK, NAMES[TOPB]))
    gate('Ⓚ④ᵃ the twelve the carrying block drops lie inside the sub-peak set rather than straddling it: '
         'every one of them is wholly below the first peak, and they are all but one of that set',
         n_drop_only == 0 and n_both == n_drop and n_sub_only == n_sub - n_drop,
         '%d of %d in both, %d kept, %d outside' % (n_both, n_sub, n_sub_only, n_drop_only))
    gate('Ⓚ④ᵇ ⌗ *NOT REGISTERED -- measured after the outcome was read, and reported as an '
         'observation, not as a test.* It cannot confirm the late-ISW candidate, which is UNREADABLE on exactly '
         'these bins by r7866\'s own finding; it says only that the block carrying most of the move is where the '
         'one candidate r7866 could neither confirm nor refute lives', True,
         'overlap %d/%d, not a test of the candidate' % (n_both, n_sub))

    out = dict(base_crossing_meV=float(base_cx), all36_crossing_meV=float(all_cx),
               move_all36_meV=float(M36), r7866_move_banked=R7866_MOVE,
               r7866_frozen_move_banked=R7866_FROZEN_MOVE,
               r7866_whole_banked=R7866_WHOLE, r7866_minus36_banked=R7866_MINUS36,
               block_crossings_meV={k: float(v) for k, v in blocks.items()},
               block_moves_meV={k: float(v) for k, v in MB.items()},
               block_shares={k: float(v) for k, v in shares.items()},
               sum_of_blocks_meV=float(ssum), residual_meV=float(resid),
               residual_fraction=float(frac), additive=bool(additive),
               concentrated=bool(concentrated), largest_block=top,
               states=states, expectation_K3_met=bool(exp_met),
               weak_expectation_EE=(None if weak_met is None else bool(weak_met)),
               per_block_dropped=per_block, bins_kept_whole=int(nb0),
               first_peak=FIRST_PEAK, r7866_subpeak_record=R7866_SUBPEAK,
               subpeak_tt_bins=n_sub, carrying_block_dropped=n_drop,
               subpeak_and_dropped=n_both, subpeak_kept=n_sub_only,
               dropped_outside_subpeak=n_drop_only, overlap_registered=False)
    io.open(os.path.join(HERE, 'by_block.json'), 'w', encoding='utf-8').write(
        json.dumps(out, indent=1, sort_keys=True, default=float))
    print('\n  wrote by_block.json')
    if FAILS:
        sys.exit('\n  ⛔ %d GATE(S) FAILED: %s' % (len(FAILS), ', '.join(FAILS)))
    print('  ⇒ all gate(s) pass')
    return 0


if __name__ == '__main__':
    sys.exit(main())
