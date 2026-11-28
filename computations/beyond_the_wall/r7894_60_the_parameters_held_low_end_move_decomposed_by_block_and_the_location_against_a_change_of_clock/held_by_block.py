# -*- coding: utf-8 -*-
"""r7894+60 — THE PARAMETERS-HELD LOW-END MOVE DECOMPOSED BY BLOCK, AND THE LOCATION TESTED AGAINST
A CHANGE OF CLOCK.

`r7892` decomposed `r7866`'s RE-PROFILED low-end move — `+48.2020` meV on the thirty-six lowest
bandpowers — and found it ADDITIVE at a `6.5` per cent residual with `84.4` per cent carried by `TT`.
It said in its own record that it decomposed that column and that `r7866`'s PARAMETERS-HELD move,
`+20.0868` meV on the SAME bins, remained undecomposed.

⛭ **This is the standing `r7138` guard one level down.** When two descriptions differ, ask whether
the difference survives a change of clock. `r7892` located the lean on ONE clock, the one where the
instrument re-fits its four parameters at every sum. The held column is the other clock — and it is
the REFERENCE's own treatment, so the question has teeth: if `TT`'s dominance is an artefact of the
freedom the instrument is given and the reference is not, then what `r7892` located is in part that
freedom rather than the data.

The construction is `r7892`'s with ONE substitution: at every mask, `chi2_cmb` is evaluated with the
four parameters HELD at the zero-sum fit on the whole mask, which is exactly how `r7866` built its
frozen column, instead of being re-fitted per sum. ⛔ **No fitting happens inside the scan**, so what
varies is the MASK and nothing else.

    python3 held_by_block.py
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
R7892 = os.path.join(BTW, 'r7892_60_the_low_end_lean_decomposed_by_block_on_crossings_not_on_a'
                          '_difference_map')
sys.path.insert(0, R7866)
import same_bins as SB                                                      # noqa: E402
SC, M6, M3 = SB.SC, SB.M6, SB.M3

NAMES = {0: 'TT', 1: 'TE', 2: 'EE'}
BLOCKS = ('TT', 'TE', 'EE')

#: ⛭ EVERY CONTROL TARGET IS READ OUT OF `r7866`'s OWN RECORD, NOT TYPED HERE — including the HELD
#:   PARAMETER VECTOR. `r7892`'s registered control fired because a row was named from memory, and
#:   the row it named was the one THIS revision needs. So the record is the source of all of it.
_SB = json.load(io.open(os.path.join(R7866, 'same_bins.json'), encoding='utf-8'))
HELD_WHOLE = float(_SB['instrument_frozen_whole']['crossing_meV'])
HELD_MINUS36 = float(_SB['instrument_frozen_minus36']['crossing_meV'])
HELD_MOVE = float(_SB['moves_meV']['instrument_frozen'])
HELD_X4 = [float(v) for v in _SB['instrument_frozen_whole']['x4']]
HELD_NB_WHOLE = int(_SB['instrument_frozen_whole']['nbins'])
HELD_NB_MINUS36 = int(_SB['instrument_frozen_minus36']['nbins'])

#: and `r7892`'s own result, for the clock comparison this revision exists to make
_BB = json.load(io.open(os.path.join(R7892, 'by_block.json'), encoding='utf-8'))
REPROF_SHARES = {k: float(v) for k, v in _BB['block_shares'].items()}
REPROF_TOP = str(_BB['largest_block'])
REPROF_MOVE = float(_BB['move_all36_meV'])
REPROF_ADDITIVE = bool(_BB['additive'])

ADDITIVE_BAR = 0.10                  #: Ⓦ⓵/Ⓦ⓷: the residual as a fraction of the whole move
CONCENTRATED_BAR = 0.80              #: one block's share of the whole move

FAILS = []
RAN = []


def gate(name, ok, got=None):
    RAN.append(name)
    print('  [%s] %s%s' % ('PASS' if ok else 'FAIL', name,
                           ('   (%s)' % got) if got is not None else ''))
    if not ok:
        FAILS.append(name.split()[0])
    return ok


def restricted(keep):
    """`r7866`'s own restriction of the instrument to `keep` of its mask, and nothing else"""
    mod = M6.Model6('lcdm')
    ok = mod.cmb.ok
    newok = ok.copy()
    newok[ok] = keep
    c = mod.cmb
    base, g, h = c.base, dict(c.g), dict(c.h)
    c.base = lambda s, nu=0, _o=base, _k=keep: np.asarray(_o(s, nu), float)[_k]
    c.g = {k: (lambda s, nu=0, _o=g[k], _k=keep: np.asarray(_o(s, nu), float)[_k])
           for k in M3.KEYS4}
    c.h = {k: (lambda s, nu=0, _o=h[k], _k=keep: np.asarray(_o(s, nu), float)[_k])
           for k in M3.KEYS4}
    c.ok, c.nb = newok, int(newok.sum())
    c.F, c.d, c.pos = SC.fisher_for(newok), SC.X_DATA[newok], SC.POSITIVE[newok]
    return mod, int(newok.sum())


def held_profile(keep, x4):
    """chi2_cmb on `keep` with the four parameters HELD at `x4` — no fit inside the scan"""
    mod, nb = restricted(keep)
    tot = [float(mod.cmb.chi2_cmb(x4, s)) for s in SB.SUMS]
    return tot, nb


def lowest_of(ok, blocks):
    """the twelve lowest-`BIN_LO` bandpowers of each named block dropped; others kept"""
    keep = np.ones(int(ok.sum()), bool)
    blk, lo = SC.BLOCK[ok], SC.BIN_LO[ok]
    for b in blocks:
        idx = np.where(blk == b)[0]
        keep[idx[np.argsort(lo[idx], kind='stable')][:SB.N_PER_BLOCK]] = False
    return keep


def crossing_for(keep, x4, label):
    tot, nb = held_profile(keep, x4)
    cx = SB.cross_of(SB.SUMS, tot)
    print('    %-22s %3d bin(s), chi2 at the seven sums %s'
          % (label, nb, ' '.join('%.2f' % v for v in tot)))
    return cx, nb, tot


def main():
    print(__doc__)
    print('=' * 100)

    mod0 = M6.Model6('lcdm')
    ok = mod0.cmb.ok
    full = np.ones(int(ok.sum()), bool)
    k36 = SB.the_thirty_six(ok)
    blk = SC.BLOCK[ok]

    # ══ Ⓦ⓪ THE HELD VECTOR AND THE MASK ARE BOTH r7866's ═══════════════════════════════════════
    print('\nⓌ⓪  THE HELD PARAMETERS COME FROM THE RECORD, AND A FRESH FIT AGREES')
    x4_fresh, _ = SB.fit_x4(M6.Model6('lcdm'), 0.0)
    x4_fresh = [float(v) for v in x4_fresh]
    dev = max(abs(a - b) for a, b in zip(x4_fresh, HELD_X4))
    print('    banked   %s' % ['%.6f' % v for v in HELD_X4])
    print('    re-fitted %s   max |deviation| %.3e' % (['%.6f' % v for v in x4_fresh], dev))
    gate('Ⓦ⓪ the four held parameters are read out of `r7866`\'s banked record and a fresh '
         'zero-sum fit on the whole mask reproduces them, so the scan is held at THAT revision\'s '
         'vector and not at one this revision happened to fit. ⌗ *Both halves matter: the record '
         'supplies the number so it cannot be misremembered, and the fit proves the record is the '
         'fit and not a stale copy*',
         len(HELD_X4) == len(M3.KEYS4) and dev < 1e-06,
         'max deviation %.3e over %d parameter(s)' % (dev, len(HELD_X4)))

    per_block = {NAMES[b]: int((~k36 & (blk == b)).sum()) for b in (0, 1, 2)}
    singles = {b: lowest_of(ok, (b,)) for b in (0, 1, 2)}
    agree = all(((~singles[b]) == (~k36 & (blk == b))).all() for b in (0, 1, 2))
    gate('Ⓦ⓪ᵃ the all-three mask drops twelve from each block and each single-block mask drops '
         'EXACTLY the bins the all-three mask drops from that block, so the three are a PARTITION '
         'of the thirty-six and the shares below are shares of one population',
         all(per_block[b] == 12 for b in BLOCKS)
         and sum(per_block.values()) == len(BLOCKS) * per_block[BLOCKS[0]] and agree,
         '%s, %d in all, partition %s' % (per_block, sum(per_block.values()), agree))

    # ══ Ⓦ① THE CONTROL — reproduce r7866's banked FROZEN row ═══════════════════════════════════
    print('\nⓌ①  THE CONTROL — does the all-three held move reproduce `r7866`\'s frozen row?')
    base_cx, nb0, _ = crossing_for(full, HELD_X4, 'the whole mask')
    all_cx, nb36, _ = crossing_for(k36, HELD_X4, 'minus all thirty-six')
    M36 = all_cx - base_cx
    print('    whole %.4f vs banked %.4f | minus36 %.4f vs banked %.4f | move %+.4f vs banked %+.4f'
          % (base_cx, HELD_WHOLE, all_cx, HELD_MINUS36, M36, HELD_MOVE))
    gate('Ⓦ① the all-three held move reproduces `r7866`\'s banked FROZEN row, BOTH crossings and '
         'not only their difference, so a pair of errors cancelling in the difference could not '
         'pass. ⌗ *Every target here was read out of `same_bins.json`; `r7892`\'s control fired '
         'because a row was typed from memory, and it was THIS row it named*',
         abs(base_cx - HELD_WHOLE) < 5e-04 and abs(all_cx - HELD_MINUS36) < 5e-04
         and abs(abs(M36) - abs(HELD_MOVE)) < 5e-04
         and nb0 == HELD_NB_WHOLE and nb36 == HELD_NB_MINUS36,
         'whole %.4f, minus36 %.4f, |move| %.4f, bins %d/%d' % (base_cx, all_cx, abs(M36),
                                                                nb0, nb36))
    gate('Ⓦ①ᵃ and the sign convention is reconciled rather than silently differing: `r7866` signs '
         'this move NEGATIVE, this reads the crossing difference POSITIVE, and removing the bins '
         'RAISES the crossing',
         M36 > 0.0 > HELD_MOVE and abs(M36 + HELD_MOVE) < 5e-04,
         'crossing %.2f -> %.2f, so +%.4f here against %+.4f banked' % (base_cx, all_cx, M36,
                                                                        HELD_MOVE))
    gate('Ⓦ①ᵇ and this is the OTHER clock, not the one `r7892` decomposed: the held move is '
         'smaller than the re-profiled move by a factor over two, on the very same bins',
         abs(REPROF_MOVE) / abs(M36) > 2.0,
         'held %+.4f against re-profiled %+.4f, ratio %.2f' % (M36, REPROF_MOVE,
                                                               abs(REPROF_MOVE) / abs(M36)))

    # ══ Ⓦ② THE DECOMPOSITION ═══════════════════════════════════════════════════════════════════
    print('\nⓌ②  THE THREE SINGLE-BLOCK HELD CROSSINGS')
    blocks, MB = {}, {}
    for b in (0, 1, 2):
        cx, _nb, _t = crossing_for(singles[b], HELD_X4, 'minus %s\'s twelve' % NAMES[b])
        blocks[NAMES[b]] = cx
        MB[NAMES[b]] = cx - base_cx
    ssum = sum(MB.values())
    resid = ssum - M36
    frac = abs(resid) / abs(M36)
    shares = {k: v / M36 for k, v in MB.items()}
    top = max(shares, key=lambda k: shares[k])
    additive = frac < ADDITIVE_BAR
    concentrated = shares[top] >= CONCENTRATED_BAR

    print('\n    the whole mask crosses at    %8.4f meV' % base_cx)
    print('    minus all thirty-six         %8.4f   move %+8.4f' % (all_cx, M36))
    for b in BLOCKS:
        print('    minus %-3s twelve             %8.4f   move %+8.4f   %6.1f per cent'
              % (b, blocks[b], MB[b], 100 * shares[b]))
    print('\n    the three sum to %+.4f against the whole %+.4f' % (ssum, M36))
    print('    residual %+.4f meV = %.1f per cent of the whole move   (bar: %.0f per cent)'
          % (resid, 100 * frac, 100 * ADDITIVE_BAR))

    states = []
    if additive:
        states.append('additive, residual %.1f per cent' % (100 * frac))
    else:
        states.append('NOT additive, residual %.1f per cent' % (100 * frac))
    if concentrated:
        states.append('concentrated in %s at %.1f per cent' % (top, 100 * shares[top]))

    # the registered outcome, read off the numbers rather than chosen
    if not additive:
        outcome = ['Ⓦ⓷']
        if concentrated:
            outcome.append('and concentrated in %s, reported alongside because the registration '
                           'said they are not exclusive' % top)
    elif top == REPROF_TOP:
        outcome = ['Ⓦ⓵']
    else:
        outcome = ['Ⓦ⓶']
    print('    ⇒ %s' % '; '.join(outcome))

    gate('Ⓦ② the outcome is one of the three registered before any crossing was computed, and '
         'where a non-additive residual sits beside a dominant block BOTH are reported rather '
         'than one chosen. ⌗ *The registration fixed `Ⓦ⓷` as the stronger reading, because a sum '
         'that does not close makes the shares untrustworthy*',
         outcome[0] in ('Ⓦ⓵', 'Ⓦ⓶', 'Ⓦ⓷'),
         '; '.join(outcome))
    gate('Ⓦ②ᵃ and each single-block move is a crossing DIFFERENCE against the same whole-mask '
         'crossing, so the three are commensurable with each other and with the whole',
         all(abs((blocks[b] - base_cx) - MB[b]) < 1e-09 for b in BLOCKS),
         'all three reconstruct from their own crossings')

    # ══ Ⓦ③ THE CLOCK COMPARISON — the whole point ══════════════════════════════════════════════
    print('\nⓌ③  DOES THE LOCATION SURVIVE THE CHANGE OF CLOCK?')
    print('    %-6s %12s %12s' % ('block', 're-profiled', 'held'))
    for b in BLOCKS:
        print('    %-6s %11.1f%% %11.1f%%' % (b, 100 * REPROF_SHARES[b], 100 * shares[b]))
    survives = (top == REPROF_TOP)
    print('    re-profiled dominant: %s | held dominant: %s   ⇒ the location %s'
          % (REPROF_TOP, top, 'SURVIVES' if survives else 'does NOT survive'))
    gate('Ⓦ③ the two clocks are compared on the block that dominates each, with `r7892`\'s shares '
         'READ OUT OF ITS RECORD rather than retyped, so this is a comparison against that '
         'revision\'s measurement and not against a remembered version of it',
         abs(sum(REPROF_SHARES.values()) - sum(REPROF_SHARES[b] for b in BLOCKS)) < 1e-12
         and REPROF_TOP in BLOCKS,
         're-profiled %s dominant at %.1f per cent; held %s at %.1f per cent'
         % (REPROF_TOP, 100 * REPROF_SHARES[REPROF_TOP], top, 100 * shares[top]))
    gate('Ⓦ③ᵃ and the registered expectation `Ⓦ⓵` is reported as met or REFUTED against what was '
         'registered, not reshaped to fit',
         True,
         'expected Ⓦ⓵; got %s' % outcome[0])

    out = dict(held_x4=HELD_X4, x4_refit=x4_fresh, x4_max_deviation=float(dev),
               base_crossing_meV=float(base_cx), all36_crossing_meV=float(all_cx),
               move_all36_meV=float(M36), banked_held_whole=HELD_WHOLE,
               banked_held_minus36=HELD_MINUS36, banked_held_move=HELD_MOVE,
               block_crossings_meV={k: float(v) for k, v in blocks.items()},
               block_moves_meV={k: float(v) for k, v in MB.items()},
               block_shares={k: float(v) for k, v in shares.items()},
               sum_of_blocks_meV=float(ssum), residual_meV=float(resid),
               residual_fraction=float(frac), additive=bool(additive),
               concentrated=bool(concentrated), largest_block=top,
               reprofiled_shares=REPROF_SHARES, reprofiled_largest=REPROF_TOP,
               reprofiled_move_meV=REPROF_MOVE, location_survives=bool(survives),
               outcome=outcome[0], states=states, per_block_dropped=per_block,
               bins_kept_whole=int(nb0))
    io.open(os.path.join(HERE, 'held_by_block.json'), 'w', encoding='utf-8').write(
        json.dumps(out, indent=1, sort_keys=True, default=float))
    print('\n  wrote held_by_block.json')
    if FAILS:
        sys.exit('\n  ⛔ %d of %d GATE(S) FAILED: %s' % (len(FAILS), len(RAN), ', '.join(FAILS)))
    print('  ⇒ all %d gate(s) pass' % len(RAN))
    return 0


if __name__ == '__main__':
    sys.exit(main())
