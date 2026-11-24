#!/usr/bin/env python3
"""P15, r7863+cc66, on 69's order r7863 items ① and ②.

COMPUTES: nothing.  Every cosmological parameter read here is `r7853`'s like-for-like profile's or
this revision's re-scored legs', and every limit is the `2.71` crossing of a `Delta chi^2` this
receipt READS from `cuts_and_node.json` rather than deriving.  No parameter is pinned as this
receipt's own; the only quantities it owns are the comparisons below.

** ⛔ BOTH ELL CUTS COST THIS REFERENCE ALMOST NOTHING, AND THE LOW END COSTS LESS THAN THE TOP IN
THREE OF FOUR COMPARISONS -- SO 60's ASYMMETRY DOES NOT REPRODUCE.  AND THE PROFILE IS ONE BRANCH
ALL THE WAY TO 0.60 eV ON BOTH RULERS, WITH NO COLD START LANDING LOWER AT ANY SUM. **

Bands Ⓐ-Ⓖ were registered at `r7863+cc66.1` (`00d6dd181`) BEFORE either computation existed; item
③'s block was measured and reported as waiting on 60's own `r7863` item ①.  Six bands hold and one
is refuted; the refutation is the result that matters and it inverts the inference 60's cut test
invites.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT     # r7861: asserted, not counted
WORK = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                    'r7863_cc66_the_ell_cuts_and_the_top_node_on_the_reference')
R = json.load(open(os.path.join(WORK, 'cuts_and_node.json')))
LFL = json.load(open(os.path.join(
    ROOT, 'computations', 'beyond_the_wall',
    'r7853_cc66_the_repaired_transfer_and_the_like_for_like_reference', 'likeforlike.json')))

C, RATIO, NODE = R['cuts'], R['bot_over_top'], R['node']
RAN = []


def check(label, ok, got=''):
    RAN.append(label)
    print('    %-5s %s%s' % ('OK' if ok else 'FAIL', label, ('   (got %s)' % got) if got else ''))
    if not ok:
        FAILED.append(label)


FAILED = []
print(__doc__)

print('=' * 99)
print('** ① THE EIGHT CUT LEGS, AGAINST BANDS FIXED BEFORE ANY OF THEM RAN **')
print('=' * 99)
print()
print('  arm        leg       removed (cut, covered, kept)   limit95 meV    move vs uncut')
for k in sorted(C):
    c = C[k]
    print('  %-9s %-9s %-29s %10.2f      %+7.2f'
          % (c['mode'], c['leg'], str(tuple(c['removed'])), c['limit95_meV'], c['move_meV']))
print()

# -- Ⓐ: the method first, then the band ------------------------------------------------------------
_land = {'rd_camb': 30.56, 'rd_min': 54.00}
check('Ⓐ① ** the limits are read by the SAME crossing r7853 used, checked against its own landed '
      'figures rather than assumed ** -- the reference arms it re-scores still report `30.56` and '
      '`54.00` meV in the record this receipt reads, so the method is the arm of record and not a '
      'second one',
      abs(LFL['rd_camb']['limit95_meV'] - 30.56) < 5e-3
      and abs(LFL['rd_min']['limit95_meV'] - 54.00) < 5e-3,
      '%.5f and %.5f' % (LFL['rd_camb']['limit95_meV'], LFL['rd_min']['limit95_meV']))

_moves = {k: C[k]['move_meV'] for k in C}
_least = min(_moves.values())
check('Ⓐ② ** Ⓐ HOLDS ON ALL EIGHT LEGS: every cut LOOSENS its limit and none tightens one ** -- the '
      'smallest move is `+0.770` meV against a band refuted by any tightening beyond `0.5`, so no '
      'removed bin anywhere was pulling the fit toward high mass',
      all(v > 0 for v in _moves.values()) and abs(_least - 0.770) < 5e-4,
      'least %+.4f meV over %d legs' % (_least, len(_moves)))

check('Ⓐ③ ⌗ and every one of the eight legs is INTERIOR to the box at every point, so no limit here '
      'is a boundary artefact',
      all(C[k]['interior'] for k in C), '%d of %d interior' % (sum(C[k]['interior'] for k in C),
                                                               len(C)))

# -- Ⓑ: the tail's share ---------------------------------------------------------------------------
_t18 = C['rd_min|top1800']['move_meV']
_t15 = C['rd_min|top1500']['move_meV']
check('Ⓑ④ ** Ⓑ HOLDS ON ITS FIRST LIMB: cutting every bin above `1800` moves the minimised limit '
      '`+1.24` meV, where the band allowed `5` ** -- so the damping tail carries almost none of '
      'THIS reference\'s limit either, which is the one place the two pipelines agree',
      abs(_t18 - 1.24) < 5e-3 and _t18 < 5.0, '%+.4f meV' % _t18)

check('Ⓑ⑤ ** and on its second: the `1500` cut, removing twice as many bins, moves it `+8.40` meV '
      'against a band of `12` ** -- the cost grows with the bins removed and stays inside, so the '
      'first limb is not a one-cut accident',
      abs(_t15 - 8.40) < 5e-3 and _t15 < 12.0, '%+.4f meV' % _t15)

# -- Ⓒ: the refutation, and the one case that goes the other way ------------------------------------
print()
print('  the band Ⓒ ratios -- low-end move divided by top move, at matched bin count:')
for k in sorted(RATIO):
    print('    %-16s %8.3f' % (k, RATIO[k]))
print()

check('Ⓒ⑥ ⛔ ** Ⓒ IS REFUTED AT ITS REGISTERED CUT: the matched low-end removal moves the minimised '
      'limit `0.835` times what the top removal does, where the band said MORE THAN TEN ** -- so '
      'the low end is not merely less costly than registered, it is CHEAPER than the top',
      abs(RATIO['rd_min|1800'] - 0.835) < 5e-4 and RATIO['rd_min|1800'] < 10.0,
      '%.4f' % RATIO['rd_min|1800'])

check('Ⓒ⑦ ⛔ ** and the second cut refutes it far harder: `0.216`, the low end costing four and a '
      'half times LESS than the top ** -- twice as many bins removed from each end, and the gap '
      'between the ends widens instead of closing',
      abs(RATIO['rd_min|1500'] - 0.216) < 5e-4 and RATIO['rd_min|1500'] < 10.0,
      '%.4f' % RATIO['rd_min|1500'])

_above = {k: v for k, v in RATIO.items() if v > 1.0}
check('Ⓒ⑧ ⌗ AND THE ONE COMPARISON THAT GOES THE OTHER WAY IS NAMED RATHER THAN AVERAGED AWAY: on '
      'the calibrated arm at the first cut the ratio is above one, so "the low end is cheaper in '
      'every comparison" is FALSE and is not claimed -- three of the four are below one and this '
      'one is not',
      list(_above) == ['rd_camb|1800'] and abs(RATIO['rd_camb|1800'] - 1.281) < 5e-4,
      '%s at %.4f' % (list(_above), RATIO['rd_camb|1800']))

check('Ⓒ⑨ ⇒ ** AND EVERY ONE OF THE FOUR IS ORDERS BELOW WHAT THE OTHER PIPELINE MEASURES ** -- 60 '
      'report the low end costing one hundred and sixty-six times the top on their own harness; the '
      'largest ratio anywhere on this reference is under `1.3`, so the two pipelines agree the tail '
      'carries almost nothing and disagree about the low end by more than two orders',
      max(RATIO.values()) < 1.3 and all(v < 10.0 for v in RATIO.values()),
      'max %.4f over %d comparisons' % (max(RATIO.values()), len(RATIO)))

# -- Ⓓ: the limb written to fall -------------------------------------------------------------------
_d18 = C['rd_camb|top1800']['move_meV'] < C['rd_min|top1800']['move_meV']
_d15 = C['rd_camb|top1500']['move_meV'] < C['rd_min|top1500']['move_meV']
check('Ⓓ⑩ ** Ⓓ HOLDS ON BOTH CUTS, AND IT WAS REGISTERED AS THE LIMB MOST LIKELY TO FALL ** -- the '
      'calibrated arm moves less in absolute terms than the minimised one under the same top cut, '
      '`+0.77` against `+1.24` and `+5.66` against `+8.40`, so tying the ruler to the drag epoch '
      'really does leave one fewer freedom with which to absorb lost information',
      _d18 and _d15,
      '%+.2f<%+.2f and %+.2f<%+.2f' % (C['rd_camb|top1800']['move_meV'],
                                       C['rd_min|top1800']['move_meV'],
                                       C['rd_camb|top1500']['move_meV'],
                                       C['rd_min|top1500']['move_meV']))

check('Ⓓ⑪ ⌗ and the effect is visible at BOTH cuts rather than at one, which is what makes it a '
      'property of the ruler\'s treatment and not of a single bin selection',
      _d18 and _d15, 'both True')

# -- Ⓔ Ⓕ Ⓖ: the top node ---------------------------------------------------------------------------
print()
print('=' * 99)
print('** ② THE TOP NODE: SIXTEEN POINTS, WARM AND COLD AT EVERY SUM ON BOTH RULERS **')
print('=' * 99)
print()
for mode in ('rd_camb', 'rd_min'):
    n = NODE[mode]
    print('  %s' % mode)
    for r in n['rows']:
        print('    Sum %.2f   warm %10.3f   cold %10.3f   cold-warm %+9.6f   H0 %7.3f   step %+.4f'
              % (r['sum'], r['warm_total'], r['cold_total'], r['cold_minus_warm'],
                 r['H0_best'], r['step']))
    print('    all steps down %s   max %.4f vs bound %.4f   H0 at 0.60 %.3f   any cold lower %s'
          % (n['all_steps_down'], n['max_step'], n['bound_3x_mean'], n['H0_at_060'],
             n['any_cold_lower']))
print()

_worst = min(NODE[m]['worst_cold_minus_warm'] for m in NODE)
check('Ⓔ⑫ ** NO COLD START LANDS LOWER AT ANY OF THE EIGHT SUMS, ON EITHER RULER ** -- the worst '
      'cold-minus-warm anywhere is `-0.000057`, which is agreement and not a lower basin, so the '
      'warm chain was never following the basin it came from.  ⌗ *This is the arm that earns the '
      'one-branch answer: without it a smooth warm sequence and a warm path stuck in its own basin '
      'are indistinguishable*',
      not any(NODE[m]['any_cold_lower'] for m in NODE) and abs(_worst + 0.000057) < 5e-7,
      'worst %+.6f' % _worst)

check('Ⓔ⑬ ** Ⓔ HOLDS ON BOTH RULERS: H0 falls at every step to 0.60 eV and no step reaches the '
      'registered three-times-the-mean bound ** -- the largest step is `0.2246` against `0.6280` on '
      'the calibrated arm and `0.3847` against `1.1180` on the minimised one, and every one of the '
      'sixteen points is interior to the box',
      all(NODE[m]['all_steps_down'] and NODE[m]['max_within_bound'] and NODE[m]['all_interior']
          for m in NODE)
      and abs(NODE['rd_camb']['bound_3x_mean'] - 0.6280) < 5e-5
      and abs(NODE['rd_min']['bound_3x_mean'] - 1.1180) < 5e-5
      and abs(NODE['rd_camb']['max_step'] - 0.2246) < 5e-5
      and abs(NODE['rd_min']['max_step'] - 0.3847) < 5e-5
      and max(r['sum'] for m in NODE for r in NODE[m]['rows']) == 0.60,
      'max/bound %.4f/%.4f and %.4f/%.4f' % (NODE['rd_camb']['max_step'],
                                             NODE['rd_camb']['bound_3x_mean'],
                                             NODE['rd_min']['max_step'],
                                             NODE['rd_min']['bound_3x_mean']))

_h0c, _h0m = NODE['rd_camb']['H0_at_060'], NODE['rd_min']['H0_at_060']
check('Ⓕ⑭ ** Ⓕ HOLDS ON BOTH RULERS: the landing points are `65.967` and `63.480`, inside the '
      'registered intervals `65.0`-`66.8` and `62.0`-`64.5` ** -- the intervals were a linear '
      'continuation of the measured steps plus about one either way, and both land inside without '
      'needing the margin',
      65.0 < _h0c < 66.8 and 62.0 < _h0m < 64.5
      and abs(_h0c - 65.967) < 5e-4 and abs(_h0m - 63.480) < 5e-4,
      '%.4f and %.4f' % (_h0c, _h0m))

_gap = abs(_h0m - R['sixty_second_branch_H0'])
check('Ⓖ⑮ ⛭ ** Ⓖ HOLDS, AND IT IS THE SHARP ONE: this reference\'s own minimised point at 0.60 eV '
      'sits `2.26` away from the value 60 report for their second branch there, far outside the '
      '`0.5` window the band set for its own refutation ** -- so the two pipelines do NOT land on '
      'the same place at the top of the range',
      2.0 < _gap < 2.5 and _gap > 0.5 and abs(_gap - 2.2596) < 5e-4,
      '%.4f apart' % _gap)

_near = abs(R['my_rd_min_H0_at_030'] - R['sixty_second_branch_H0'])
check('Ⓖ⑯ ⇒ ** and the value they read as a SECOND branch at the top of the range is this '
      'reference\'s ONE-branch value near the middle of it ** -- the minimised arm passes within '
      '`0.03` of it around a third of an electronvolt, where this profile is smooth, monotone and '
      'cold-start confirmed, so on these terms that number locates a sum rather than a basin',
      _near < 0.05 and abs(_near - 0.0270) < 5e-5, '%.5f apart' % _near)

# -- Ⓗ: the registration's own defect --------------------------------------------------------------
print()
_cov = {tuple(C[k]['removed']) for k in C}
check('Ⓗ⑰ ⛔ ** AND THE REGISTRATION\'S OWN HEDGE IS FALSE, RECORDED RATHER THAN DROPPED ** -- it '
      'said the counts removed come from a covered set smaller than the instrument\'s full one; '
      'every leg reports the covered figure EQUAL to it, because this reference reaches every bin '
      'the instrument has, so the hedge guarded against a restriction that does not exist here',
      all(r[1] == 613 for r in _cov), 'covered %s on all legs' % sorted({r[1] for r in _cov}))

check('Ⓗ⑱ ⌗ and the counts actually removed are `49` and `103`, not the thirty-six the other '
      'pipeline removed -- the difference the registration predicted, for a different reason than '
      'it gave, which is why the comparison is of SHARES and never of bin counts',
      sorted({r[0] for r in _cov}) == [49, 103], '%s' % sorted({r[0] for r in _cov}))

print()
check('Ⓘ⑲ ** eighteen arms ran before this one and every one was adjudicated **, the count read off '
      'the list the check function itself appends rather than typed beside them',
      len(RAN) == 18 and len(set(RAN)) == 18, '%d arms, %d distinct' % (len(RAN), len(set(RAN))))

print()
print('=' * 99)
print('  ✔ ** SIX OF SEVEN BANDS HOLD: Ⓐ on all eight legs, Ⓑ on both limbs, Ⓓ where it was')
print('    written to fall, and Ⓔ Ⓕ Ⓖ on both rulers with no cold start landing lower anywhere. **')
print('  ⛔ ** AND Ⓒ IS REFUTED ON ALL FOUR COMPARISONS -- the low end is CHEAPER than the top on')
print('    the minimised arm at both cuts, 0.835 and 0.216, where the band said more than ten and')
print('    the other pipeline measures 166 the other way.  The tail is agreed; the low end is not. **')
print('=' * 99)
if FAILED:
    print('  %d FAILED: %s' % (len(FAILED), FAILED))
    raise SystemExit(1)
print('  ALL CHECKS PASS')
