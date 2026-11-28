"""⑱④ — the 12-of-13 overlap, recomputed from the bin counts rather than taken on report.

Order `r7895` (69) item ⑱④: *"Say whether you read it as 60 does (an overlap that removes
'unreadable' as a reason to set the candidate aside, and not evidence for the ISW) or as
over-reading."*

`PREDICTION.md` Ⓕ⑥ registered that this would be answered *"with the overlap recomputed from the
bin lists rather than taken on report"*.  `r7892`'s own record carries the counts, so the recompute
is of the ARITHMETIC that makes the overlap what it is — and that arithmetic turns out to settle the
question in a way neither the order nor `r7892`'s record states.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
R7892 = os.path.join(os.path.dirname(HERE),
                     'r7892_60_the_low_end_lean_decomposed_by_block_on_crossings_not_on_a_difference_map')


def main():
    d = json.load(open(os.path.join(R7892, 'by_block.json'), encoding='utf-8'))

    subpeak = int(d['subpeak_tt_bins'])             # 13
    dropped = int(d['carrying_block_dropped'])      # 12, TT's lowest twelve bandpowers
    both = int(d['subpeak_and_dropped'])            # 12
    kept = int(d['subpeak_kept'])                   # 1
    outside = int(d['dropped_outside_subpeak'])     # 0
    peak = d['first_peak']                          # 220

    #: ⛭ THE INCLUSION, NOT AN INTERSECTION.  `dropped_outside_subpeak == 0` says every carrying bin
    #:   is a sub-peak bin, so the carrying set is a SUBSET of the sub-peak set rather than a set
    #:   that happens to meet it.  Stated as a check so it fails if either count moves.
    inclusion = (outside == 0 and both == dropped)
    accounted = (both + kept == subpeak)

    #: ⛔ AND THE INCLUSION IS FORCED BY THE TWO DEFINITIONS.  The carrying set IS "the twelve
    #:   LOWEST TT bandpowers" (`r7866`, carried by `r7892`); the sub-peak set IS "the TT bins below
    #:   the first peak".  The twelve lowest bins must lie below the peak whenever at least twelve
    #:   bins do, and `subpeak_tt_bins` says thirteen do.  So the overlap could not have come out
    #:   any other way, and a count that cannot come out otherwise measures nothing.
    forced = subpeak >= dropped

    out = {
        'source': 'r7892 by_block.json, counts read not re-derived',
        'subpeak_tt_bins': subpeak, 'carrying_block_dropped': dropped,
        'subpeak_and_dropped': both, 'subpeak_kept': kept,
        'dropped_outside_subpeak': outside, 'first_peak': peak,
        'overlap_registered_by_60': d.get('overlap_registered'),
        'bins_kept_whole_60': d.get('bins_kept_whole'),
        'tt_share_of_move': d.get('block_shares', {}).get('TT'),
        'move_all36_meV': d.get('move_all36_meV'),
        'is_inclusion_not_intersection': inclusion,
        'subpeak_fully_accounted': accounted,
        'inclusion_forced_by_definitions': forced,
        'reading': ('agree with 60 on the conclusion, and for a reason 60 does not state: the '
                    'overlap is forced by the two definitions, so it is not evidence of anything, '
                    'and that is exactly why it cannot be used to DISMISS the candidate either'),
    }
    json.dump(out, open(os.path.join(HERE, 'overlap_read.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)

    print('\n  ⑱④ THE OVERLAP, RECOMPUTED FROM THE COUNTS\n')
    print('    sub-peak TT bins (l < %s):            %d' % (peak, subpeak))
    print('    TT bins carrying the low-end move:    %d   (%.1f%% of the %.3f meV move)'
          % (dropped, 100.0 * (out['tt_share_of_move'] or 0), out['move_all36_meV'] or 0))
    print('    in both:                              %d' % both)
    print('    sub-peak but kept:                    %d' % kept)
    print('    carrying but NOT sub-peak:            %d' % outside)
    print()
    print('    ⇒ inclusion, not intersection:        %s' % inclusion)
    print('    ⇒ sub-peak fully accounted (12+1=13): %s' % accounted)
    print('    ⇒ inclusion FORCED by definitions:    %s   (13 sub-peak >= 12 lowest)' % forced)
    print('    ⌗ 60 registered the overlap in advance: %s' % out['overlap_registered_by_60'])
    print()
    assert inclusion and accounted and forced, 'the counts do not support the stated reading'
    print('    ' + out['reading'] + '\n')


if __name__ == '__main__':
    main()
