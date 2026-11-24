# -*- coding: utf-8 -*-
"""Ⓐ① THE THIRTY-SIX LOW BANDPOWERS THIS LINE'S MATCHED-COUNT CUT DROPS, NAMED BY BLOCK AND
MULTIPOLE -- and the same for the forty-nine the reference's rule drops, so the two low ends are
compared as SETS and not by their costs.

⌗ *`r7862`'s `tail_control.narrow_low` drops `total // 3` bandpowers from EACH block, ordered by
`BIN_LO` within the block.  cc66's `cut_rescore._masked(..., 'bot')` drops the `n_cut` GLOBALLY
lowest covered bins, with no per-block split.  Those are two different rules, and this file
establishes whether they pick the same bins before anything is read into what each cut cost.*

    NODE=60 python3 low_bins.py
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
sys.path.insert(0, os.path.join(_BTW, 'r7862_60_the_calibrated_case_on_the_references_terms_and_'
                                      'the_damping_tails_share_of_the_gap'))
import tail_share as TS                                                     # noqa: E402,F401
import tail_control as TC                                                   # noqa: E402
import score_ttteee as SC                                                   # noqa: E402
import model3 as M3                                                         # noqa: E402
import model6 as M6                                                         # noqa: E402

NAMES = {0: 'TT', 1: 'TE', 2: 'EE'}
TOTAL = 36                       # the matched-count leg: the ell>1800 high cut dropped 36


def rows_for(idx):
    """(block, lo, hi) for each bandpower index, sorted as a reader would want them"""
    return sorted((int(SC.BLOCK[i]), int(SC.BIN_LO[i]), int(SC.BIN_HI[i]), int(i)) for i in idx)


def bands(rows):
    """one line per block: count and the ell span the dropped bins cover"""
    out = {}
    for b in (0, 1, 2):
        mine = [r for r in rows if r[0] == b]
        out[NAMES[b]] = dict(n=len(mine),
                             ell_lo=(min(r[1] for r in mine) if mine else None),
                             ell_hi=(max(r[2] for r in mine) if mine else None))
    return out


def main():
    print(__doc__)
    print('=' * 100)
    mod = M6.Model6('lcdm')
    ok = mod.cmb.ok
    okidx = np.where(ok)[0]
    print('\n  THE INSTRUMENT\'S MASK:  %d bandpower(s) of %d in the score'
          % (int(ok.sum()), SC.BLOCK.size))
    for b in (0, 1, 2):
        m = okidx[SC.BLOCK[okidx] == b]
        print('    %s  %4d bin(s), ell %d..%d'
              % (NAMES[b], m.size, int(SC.BIN_LO[m].min()), int(SC.BIN_HI[m].max())))

    # ── Ⓐ①ᵃ the thirty-six, by this line's own rule, reproduced from tail_control itself ──
    n_per = TOTAL // 3
    keep = np.ones(int(ok.sum()), bool)
    blk, lo = SC.BLOCK[ok], SC.BIN_LO[ok]
    dropped_local = []
    for b in (0, 1, 2):
        idx = np.where(blk == b)[0]
        order = idx[np.argsort(lo[idx], kind='stable')]
        keep[order[:n_per]] = False
        dropped_local.extend(order[:n_per].tolist())
    mine = okidx[np.array(sorted(dropped_local))]
    rows_mine = rows_for(mine)
    newok = ok.copy()
    newok[ok] = keep

    print('\n  Ⓐ①ᵃ THE THIRTY-SIX, by `r7862`\'s rule (%d per block, ordered by BIN_LO):' % n_per)
    for b in (0, 1, 2):
        these = [r for r in rows_mine if r[0] == b]
        print('    %s  %s' % (NAMES[b], ', '.join('%d-%d' % (r[1], r[2]) for r in these)))
    print('    ⇒ per block: %s' % json.dumps(bands(rows_mine)))
    print('    the mask after the cut spans ell %d..%d over %d bin(s)'
          % (int(SC.BIN_LO[newok].min()), int(SC.BIN_HI[newok].max()), int(newok.sum())))

    # the landed cut's own record, as the check on the naming
    landed = TC.narrow_low(M6.Model6('lcdm'), SC, M3, n_per)
    agree = (landed['dropped'] == len(mine) == TOTAL
             and landed['bins_after'] == int(newok.sum())
             and landed['ell_lo_after'] == int(SC.BIN_LO[newok].min()))
    print('    ⇒ against `tail_control.narrow_low` itself: dropped %d, bins_after %d, '
          'ell_lo_after %d  %s'
          % (landed['dropped'], landed['bins_after'], landed['ell_lo_after'],
             'AGREES' if agree else 'DISAGREES -- the naming is wrong'))

    # ── Ⓐ①ᵇ the reference's forty-nine, by cc66's own rule on its own covered mask ──
    # cc66's `covered` is `isfinite(mb) & isin(BLOCK, (0,1,2))` on the REFERENCE's spectra, and
    # its record says 613 -- the whole score.  So the rule is reproducible from `SC` alone, and
    # the reproduction of its own `n_cut = 49` is the check that it is the same rule.
    cov = np.ones(SC.BLOCK.size, bool)
    n_cut = int((cov & (SC.BIN_LO > 1800)).sum())
    covidx = np.where(cov)[0]
    theirs = covidx[np.argsort(SC.BIN_LO[covidx], kind='stable')][:n_cut]
    rows_theirs = rows_for(theirs)
    print('\n  Ⓐ①ᵇ THE REFERENCE\'S FORTY-NINE, by cc66\'s rule (the %d globally lowest of %d):'
          % (n_cut, int(cov.sum())))
    for b in (0, 1, 2):
        these = [r for r in rows_theirs if r[0] == b]
        if these:
            print('    %s  %d bin(s), ell %d..%d'
                  % (NAMES[b], len(these), these[0][1], these[-1][2]))
    print('    ⇒ per block: %s' % json.dumps(bands(rows_theirs)))
    print('    ⇒ cc66\'s own record says it removed 49 of 613 leaving 564; this rule gives '
          '%d of %d leaving %d  %s'
          % (n_cut, int(cov.sum()), int(cov.sum()) - n_cut,
             'AGREES' if (n_cut == 49 and int(cov.sum()) == 613) else 'DISAGREES'))

    set_mine, set_theirs = set(int(i) for i in mine), set(int(i) for i in theirs)
    inter = sorted(set_mine & set_theirs)
    only_mine = sorted(set_mine - set_theirs)
    only_theirs = sorted(set_theirs - set_mine)
    print('\n    ** THE TWO LOW ENDS AS SETS **')
    print('      in both:            %2d  %s'
          % (len(inter), ', '.join('%s %d-%d' % (NAMES[r[0]], r[1], r[2])
                                   for r in rows_for(inter)) or '(none)'))
    print('      this line\'s only:   %2d  (ell %s)'
          % (len(only_mine),
             '%d..%d' % (min(SC.BIN_LO[only_mine]), max(SC.BIN_HI[only_mine]))
             if only_mine else 'none'))
    print('      the reference\'s only: %d  (ell %s)'
          % (len(only_theirs),
             '%d..%d' % (min(SC.BIN_LO[only_theirs]), max(SC.BIN_HI[only_theirs]))
             if only_theirs else 'none'))
    nblocks_theirs = sum(1 for b in (0, 1, 2) if bands(rows_theirs)[NAMES[b]]['n'] > 0)
    print('      ⇒ the REGISTERED EXPECTATION was that cc66\'s forty-nine come from FEWER than '
          'three blocks.  They come from %d, split %s.'
          % (nblocks_theirs,
             '/'.join(str(bands(rows_theirs)[NAMES[b]]['n']) for b in (0, 1, 2))))
    print('      ⛔ ** SO THAT EXPECTATION IS REFUTED, and is reported as refuted. **  The sets '
          'differ for a DIFFERENT reason, measured below.')

    # ── Ⓐ①ᶜ the bins the reference covers and the instrument does not ──
    notok = np.where(~ok)[0]
    rows_gap = rows_for(notok)
    print('\n  Ⓐ①ᶜ THE %d BINS THE REFERENCE COVERS AND THE INSTRUMENT DOES NOT:' % notok.size)
    for b in (0, 1, 2):
        m = notok[SC.BLOCK[notok] == b]
        if m.size:
            print('    %s  %2d bin(s), ell %d..%d'
                  % (NAMES[b], m.size, int(SC.BIN_LO[m].min()), int(SC.BIN_HI[m].max())))
    below = notok[SC.BIN_HI[notok] < 100]
    print('    ⇒ %d of the %d sit BELOW ell = 100, which is where the instrument\'s score starts'
          % (below.size, notok.size))
    overlap_of_theirs = len(set_theirs & set(int(i) for i in np.where(ok)[0]))
    print('    ⇒ and of cc66\'s forty-nine, only %d are bins the instrument covers at all'
          % overlap_of_theirs)

    out = dict(instrument=dict(n_covered=int(ok.sum()), n_per_block=n_per, total=TOTAL,
                               rows=[[NAMES[r[0]], r[1], r[2]] for r in rows_mine],
                               per_block=bands(rows_mine),
                               ell_lo_after=int(SC.BIN_LO[newok].min()),
                               ell_hi_after=int(SC.BIN_HI[newok].max()),
                               bins_after=int(newok.sum()),
                               landed=landed, agrees_with_landed=bool(agree)),
               reference=dict(n_covered=int(cov.sum()), n_cut=n_cut,
                              rows=[[NAMES[r[0]], r[1], r[2]] for r in rows_theirs],
                              per_block=bands(rows_theirs),
                              reproduces_cc66_record=bool(n_cut == 49
                                                          and int(cov.sum()) == 613),
                              n_blocks=nblocks_theirs),
               sets=dict(in_both=[[NAMES[r[0]], r[1], r[2]] for r in rows_for(inter)],
                         n_in_both=len(inter), n_only_instrument=len(only_mine),
                         n_only_reference=len(only_theirs),
                         expectation_three_blocks_refuted=bool(nblocks_theirs == 3),
                         reference_bins_the_instrument_covers=overlap_of_theirs),
               uncovered=dict(n=int(notok.size),
                              rows=[[NAMES[r[0]], r[1], r[2]] for r in rows_gap],
                              n_below_100=int(below.size)))
    io.open(os.path.join(_HERE, 'low_bins.json'), 'w', encoding='utf-8').write(
        json.dumps(out, indent=1, sort_keys=True))
    print('\n  wrote low_bins.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
