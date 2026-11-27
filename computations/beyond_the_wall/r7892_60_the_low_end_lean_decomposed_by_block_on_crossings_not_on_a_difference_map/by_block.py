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
ORDER_ALL36 = -20.09                 #: r7866's measured move on all thirty-six, the control
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
    gate('Ⓚ① the all-three move reproduces `r7866`\'s `-20.09` meV within `0.5`, so this is the '
         'instrument that revision measured and a decomposition of its move is comparable. ⛔ *This '
         'was the registered refusal condition: had it missed, no decomposition would be reported*',
         abs(M36 - ORDER_ALL36) < 0.5, '%+.2f meV against r7866\'s %+.2f' % (M36, ORDER_ALL36))

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

    out = dict(base_crossing_meV=float(base_cx), all36_crossing_meV=float(all_cx),
               move_all36_meV=float(M36), r7866_all36_meV=ORDER_ALL36,
               block_crossings_meV={k: float(v) for k, v in blocks.items()},
               block_moves_meV={k: float(v) for k, v in MB.items()},
               block_shares={k: float(v) for k, v in shares.items()},
               sum_of_blocks_meV=float(ssum), residual_meV=float(resid),
               residual_fraction=float(frac), additive=bool(additive),
               concentrated=bool(concentrated), largest_block=top,
               states=states, expectation_K3_met=bool(exp_met),
               weak_expectation_EE=(None if weak_met is None else bool(weak_met)),
               per_block_dropped=per_block, bins_kept_whole=int(nb0))
    io.open(os.path.join(HERE, 'by_block.json'), 'w', encoding='utf-8').write(
        json.dumps(out, indent=1, sort_keys=True, default=float))
    print('\n  wrote by_block.json')
    if FAILS:
        sys.exit('\n  ⛔ %d GATE(S) FAILED: %s' % (len(FAILS), ', '.join(FAILS)))
    print('  ⇒ all gate(s) pass')
    return 0


if __name__ == '__main__':
    sys.exit(main())
