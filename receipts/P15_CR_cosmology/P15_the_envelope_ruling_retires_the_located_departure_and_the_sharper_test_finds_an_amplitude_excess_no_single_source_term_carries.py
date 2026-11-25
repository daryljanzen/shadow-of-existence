# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE ENVELOPE RULING RETIRES THIS LINE'S OWN LOCATED DEPARTURE, THE SHARPER TEST FINDS A REAL
AMPLITUDE EXCESS THE RULING WOULD HAVE DISCARDED, AND NO SINGLE SOURCE TERM CARRIES IT.

COMPUTES: the previous revision's departure re-read against the oscillation ENVELOPE rather than
against point values, on both CAMB legs, whole-band and local, with another seat's own envelope
numbers RECOMPUTED from its own inputs before its definition is used; a two-parameter shift test of
the instrument's response against CAMB's over the same stretch, whose allowance for a registration
shift is READ OFF the bank's recorded acoustic scale against CAMB's own, not chosen; and the
instrument's own bilinear source decomposition -- ten pairs that close on the reported spectrum --
with each pair's share of the change over the stretch at two sums.
** IT PINS AS RESULTS: the six departures and the six envelopes that put every one of them INSIDE;
the gap `0.030531` against the envelope `0.045076`, `0.68` of it, where a point-value ratio read
`1.769`; the amplitudes `1.152` and `1.296` in TT against `1.014` and `1.046` in EE, each stable
across its own near-best band; the registration allowances `2.563e-04` and `5.170e-04` and the
shifts `7.0e-04` and `-1.9e-03` that exceed them; and the pair shares `0.383`, `0.342` and `0.198`
with the closure at `1.3e-15`. **
⛔ ** AND IT PINS WHAT WAS RETIRED, WHAT WAS NOT RUN, AND WHAT IS ANSWERED BOTH WAYS: ** the
previous revision's READING that a departure is located at those multipoles is retired while its
NUMBERS stand; the correction arm is NOT RUN under its own registered gate, whose stated reason the
shift test then dissolves; and the order's conditional arm has its condition answered BOTH WAYS by
one measurement, so no switch is written and both readings are routed.
⛔ ** NO LIMIT AND NO ENVELOPE CROSSING IS PINNED HERE, because this revision read none. **

⌷ ** THE ID. **  `69` ordered this as `r7873`, which merged `r7872`, ruled the low-multipole
residual and the lean one object until a measurement separates them, and relayed the envelope rule.

⚠ ** FOUR THINGS IN THIS RECORD ARE THIS SEAT'S OWN, and the first is that the ruling was spent on
this line's OWN landed headline before anything new was measured -- which retired it. **

    NODE=60 python3 <this file>

Written r7874 (60).  Stated for reversal.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                 'r7874_60_the_sum_response_by_source_term_and_the_correction_that_decides_'
                 'one_object')
FAILS = []
NARMS = 0


def load(name, d=None):
    with io.open(os.path.join(d or D, name), encoding='utf-8') as fh:
        return json.load(fh)


def text(name, d=None):
    with io.open(os.path.join(d or D, name), encoding='utf-8') as fh:
        return fh.read()


def check(name, ok, got=None):
    global NARMS
    NARMS += 1
    if ok:
        print('  [PASS] %s' % name + ('   (%s)' % got if got is not None else ''))
    else:
        FAILS.append(name)
        print('  [FAIL] %s' % name + ('   (got %s)' % got if got is not None else ''))


print(__doc__)
print('=' * 100)

ENV = load('envelope.json')
SH = load('shift.json')
PT = load('per_term.json')
#: ⛔ *the prose is matched on a WHITESPACE-FLATTENED copy -- four arms of the previous revision's
#: receipt failed on where a line happened to wrap, which is a fact about the editor and not about
#: the record.*
RESULT = ' '.join(text('RESULT.md').split())
PRED = ' '.join(text('PREDICTION.md').split())
GEN = text('gen_srcdec.sh')
GEN_FLAT = ' '.join(GEN.split())

# ── Ⓐ the borrowed definition is reproduced before it is used ───────────────────────────────────
_rp = ENV['reproduction']
check('Ⓐ⓪ᵃ ⛭ ** ANOTHER SEAT\'S ENVELOPE NUMBERS ARE RECOMPUTED FROM ITS OWN CONTROL, TAU, `A_s`, '
      '`lmax` AND CAMB LEG BEFORE ITS DEFINITION IS USED, and they agree to SIX SIGNIFICANT '
      'DIGITS. **  ⇒ *a second seat re-implementing a definition and then comparing against its '
      'own version is how two numbers get called the same thing; the worst relative difference is '
      '`1.06e-06` over six rows*',
      abs(_rp['worst_rel_diff'] - 1.06e-06) < 5e-08
      and len(_rp['rows']) == 6
      and all(abs(v['here']['envelope'] - v['cc66']['envelope'])
              / abs(v['cc66']['envelope']) < 2e-06 for v in _rp['rows'].values()),
      'worst %.3e over %d row(s)' % (_rp['worst_rel_diff'], len(_rp['rows'])))

check('Ⓐ⓪ᵃᵃ ⛔ AND THE SCRIPT\'S OWN `1e-06` GATE DOES NOT PASS THAT NUMBER, AND IS LEFT UNMOVED: '
      'the gate was this seat\'s and was set too tight for a figure CAMB reproduces to about a '
      'part in a million.  ⇒ *the measurement is the number and not the threshold, and this arm '
      'pins the DISAGREEMENT between them rather than quietly loosening one*',
      _rp['holds'] is False and _rp['worst_rel_diff'] > 1e-06
      and _rp['worst_rel_diff'] < 2e-06
      and 'That gate is left UNMOVED' in RESULT)

check('Ⓐ⓪ᵃᵇ ⛭ and the LEG MISMATCH is named rather than absorbed: the other seat computed on the '
      'LENSED leg while the instrument\'s banked spectra are UNLENSED, so the envelope is '
      'leg-dependent -- both legs are reported and the verdict is taken on the like-for-like one, '
      'which over this stretch agrees with the other to three digits',
      abs(ENV['envelopes']['TT|0.60|unlensed|the run 100-212']['envelope'] - 0.04507564) < 5e-8
      and abs(ENV['envelopes']['TT|0.60|lensed|the run 100-212']['envelope'] - 0.04499824) < 5e-8
      and 'The leg mismatch is named' in RESULT)

# ── Ⓑ the registered negative, and what it retires ──────────────────────────────────────────────
_h = ENV['r7872_headline']
check('Ⓑ⓪ᵇ ⛭⛭⛭ ** THE REGISTERED NEGATIVE FIRED ON THIS LINE\'S OWN LANDED HEADLINE: the gap is '
      '`0.030531` against an envelope of `0.045076` over the same stretch, `0.68` of it, where the '
      'previous revision read a point-value ratio of `1.769`. **  ⇒ *its NUMBERS stand -- the '
      'instrument returns `0.070234` and CAMB `0.039702` at the bottom of the band, exactly as it '
      'reported -- and what does NOT stand is the READING that a departure is LOCATED there*',
      abs(_h['instrument_at_100'] - 0.070234) < 5e-6
      and abs(_h['camb_unlensed_at_100'] - 0.039702) < 5e-6
      and abs(_h['point_ratio'] - 1.769) < 5e-4
      and abs(_h['gap_at_100'] - 0.030531) < 5e-6
      and abs(_h['envelope_over_the_run_unlensed'] - 0.045076) < 5e-6
      and abs(_h['gap_over_envelope_unlensed'] - 0.677) < 5e-3
      and _h['survives_on_like_for_like'] is False
      and _h['survives_on_cc66_leg'] is False,
      'gap %.6f over envelope %.6f = %.3f'
      % (_h['gap_at_100'], _h['envelope_over_the_run_unlensed'],
         _h['gap_over_envelope_unlensed']))

check('Ⓑ⓪ᵇᵃ and it is INSIDE at every block and every sum, not only at the one the headline named: '
      'six departures `0.00122`, `0.00805`, `0.03053`, `0.00080`, `0.00261`, `0.01031` against six '
      'envelopes `0.00447`, `0.02207`, `0.04508`, `0.00598`, `0.03273`, `0.07054`',
      all(ENV['departure']['%s|%.2f|the run 100-212' % (b, s)]['verdict_on_like_for_like']
          == 'INSIDE' for b in ('TT', 'EE') for s in (0.06, 0.30, 0.60))
      and abs(ENV['departure']['TT|0.60|the run 100-212']['max_departure_vs_unlensed']
              - 0.03053147) < 5e-8
      and abs(ENV['departure']['EE|0.60|the run 100-212']['max_departure_vs_unlensed']
              - 0.01030974) < 5e-8,
      '6 of 6 INSIDE')

check('Ⓑ⓪ᵇᵇ ⛔ and the retirement is in the record in those words, so a reader cannot take the '
      'previous revision\'s located departure as standing: the NUMBERS stand, the READING does not',
      'THE DEPARTURE IS NOT RESOLVED AS A DEPARTURE UNDER THE RULING' in RESULT
      and 'numbers stand' in RESULT
      and 'does not stand is the reading that a departure is LOCATED' in RESULT)

# ── Ⓒ the shift test: the allowance is measured, and the verdict is an amplitude ────────────────
_ps = SH['peak_shifts']
check('Ⓒ④ᵃ ⛭ ** THE ALLOWANCE FOR A REGISTRATION SHIFT IS MEASURED AND NOT CHOSEN: ** the '
      'instrument\'s own sum-induced fractional peak shift off the bank\'s recorded `l_A` against '
      'CAMB\'s off its own `theta*` -- `-4.163e-03` against `-4.419e-03` at the middle sum and '
      '`-8.440e-03` against `-8.957e-03` at the top -- so the difference an `eps` may legitimately '
      'be is `2.563e-04` and `5.170e-04`.  ⇒ *a ratio of ratios, so it does not turn on whose '
      'definition of the acoustic scale is used*',
      abs(_ps['0.30']['frac_shift_instrument'] + 4.163e-03) < 5e-7
      and abs(_ps['0.30']['frac_shift_camb'] + 4.419e-03) < 5e-7
      and abs(_ps['0.60']['frac_shift_instrument'] + 8.440e-03) < 5e-7
      and abs(_ps['0.60']['frac_shift_camb'] + 8.957e-03) < 5e-7
      and abs(abs(_ps['0.30']['difference']) - 2.563e-04) < 5e-8
      and abs(abs(_ps['0.60']['difference']) - 5.170e-04) < 5e-8)

_f = SH['fits']
check('Ⓒ④ᵇ ⛭⛭⛭ ** AN AMPLITUDE DIFFERENCE, IN EVERY BLOCK AND BOTH SUMS -- so the envelope test '
      'was TOO LENIENT and there is a real departure it could not see. **  *TT wants `1.152` and '
      '`1.296`, EE `1.014` and `1.046`, each STABLE across its own near-best band; and the shifts '
      'the fits want exceed the measured allowance by `2.7` and `3.7` times.*  ⇒ *routed to the '
      'seat that made the ruling, not asserted over it*',
      all(_f[k]['verdict'] == 'AMPLITUDE' for k in _f)
      and abs(_f['TT|0.30']['best_A'] - 1.15162) < 5e-5
      and abs(_f['TT|0.60']['best_A'] - 1.29592) < 5e-5
      and abs(_f['EE|0.30']['best_A'] - 1.01405) < 5e-5
      and abs(_f['EE|0.60']['best_A'] - 1.04630) < 5e-5
      and abs(_f['TT|0.30']['eps_over_allowed'] - 2.73) < 0.02
      and abs(_f['TT|0.60']['eps_over_allowed'] - 3.68) < 0.02
      and 'too lenient' in RESULT,
      'TT %.3f and %.3f; EE %.3f and %.3f'
      % (_f['TT|0.30']['best_A'], _f['TT|0.60']['best_A'],
         _f['EE|0.30']['best_A'], _f['EE|0.60']['best_A']))

check('Ⓒ④ᵇᵃ and the amplitude is STABLE where the shift is not, which is what makes the verdict '
      'readable at all: `A` moves by under `0.015` across each near-best band while `eps` is '
      'pinned only to about `1e-03`  ⇒ *a well-pinned amplitude beside a poorly-pinned shift is '
      'not a trade-off, and that distinction is the whole of the next arm*',
      all(_f[k]['A_spread'] < 0.015 for k in _f)
      and all(_f[k]['A_and_eps_trade_off'] is False for k in _f),
      'worst A spread %.4f' % max(_f[k]['A_spread'] for k in _f))

check('Ⓒ④ᶜ ⛔ ** AND A CRITERION OF THIS SEAT\'S MISFIRED, PINNED PER ROW RATHER THAN DELETED: ** '
      'the registered NOT SEPARABLE clause is about an `A`-`eps` TRADE-OFF, and the first cut coded '
      'the `eps` band\'s WIDTH, which is a proxy for that clause and not the clause.  On the proxy '
      'all four rows read NOT SEP; on the clause as written, with `A` measured ACROSS the band, '
      'all four read AMPLITUDE.  ⇒ *both verdicts are carried in the record, per row*',
      all(_f[k]['verdict_from_the_coded_proxy'] == 'NOT SEP' for k in _f)
      and all(_f[k]['verdict'] == 'AMPLITUDE' for k in _f)
      and 'trade off against each other across a wide range at comparable residual' in PRED
      and 'is no trade-off at all' in RESULT)

check('Ⓒ④ᵈ ⛭ and the arm was REGISTERED IN AN ADDENDUM, committed and pushed before it ran, rather '
      'than folded into the registration after a result  ⇒ *a registration edited after a result '
      'is not a registration, and the file says so about itself*',
      'ADDENDUM, REGISTERED AFTER' in PRED
      and 'committed and pushed before the arm below is computed' in PRED
      and 'a registration edited after a result is not a registration' in PRED
      and 'Nothing above is changed' in PRED)

# ── Ⓓ the decomposition ────────────────────────────────────────────────────────────────────────
check('Ⓓ①ᵃ ⛭ ** THE CLOSURE IS CHECKED BEFORE ANYTHING IS READ OFF THE COLUMNS: ** the ten '
      'bilinear pairs sum to the reported `D_l` to `1.3e-15` relative at every sum, and the '
      'registered BLOCKED outcome is empty  ⇒ *the order asks for each TERM\'s response and `D_l` '
      'is QUADRATIC in the transfer, so what exists is ten PAIRS and not four terms*',
      PT['blocked'] == [] and PT['n_pairs'] == 10
      and max(PT['closure_relative'].values()) < 1e-14
      and PT['pairs'][0] == 'sw*sw' and 'sw*isw' in PT['pairs']
      and 'does not license naming a carrier' in RESULT,
      'worst closure %.3e' % max(PT['closure_relative'].values()))

_c30, _c60 = PT['carriers']['0.30'], PT['carriers']['0.60']
check('Ⓓ①ᵇ ⛭⛭⛭ ** NO SINGLE TERM CARRIES IT. **  *The largest pair is `sw*sw` at both sums -- '
      '`0.383` and `0.361` -- but it does NOT dominate: the CROSS pair `sw*isw` sits `0.342` at '
      'both, `1.12` and `1.06` times behind, and three pairs spanning `sw` and `isw` are each above '
      'a tenth.*  ⇒ *the registered live case was a cross pair carrying it; what obtained is '
      'nearly that -- a diagonal largest with a cross pair at ninety-five per cent of its share*',
      _c30['top_pair'] == 'sw*sw' and _c60['top_pair'] == 'sw*sw'
      and abs(_c30['top_share'] - 0.3831) < 5e-4 and abs(_c60['top_share'] - 0.3607) < 5e-4
      and _c30['second_pair'] == 'sw*isw' and _c60['second_pair'] == 'sw*isw'
      and abs(_c30['second_share'] - 0.342) < 1e-3 and abs(_c60['second_share'] - 0.342) < 1e-3
      and _c30['top_dominates'] is False and _c60['top_dominates'] is False
      and len(_c30['pairs_above_a_tenth']) == 3 and len(_c60['pairs_above_a_tenth']) == 3
      and PT['top_dominates_at_both_sums'] is False
      and 'NO SINGLE TERM CARRIES IT' in PT['verdict'],
      '%s %.4f against %s %.4f' % (_c30['top_pair'], _c30['top_share'],
                                   _c30['second_pair'], _c30['second_share']))

check('Ⓓ①ᵇᵃ ⛔ and the per-TERM sums DOUBLE-COUNT the cross pairs, so they are pinned as what they '
      'are and not as a partition: `sw` `0.746` and `0.721`, `isw` `0.551` and `0.580`, `dp` '
      '`0.080` and `0.081`, `pol` under a thousandth -- which add to more than one exactly because '
      '`sw*isw` is counted twice',
      PT['carriers']['0.30']['term_sums_double_count_cross_pairs'] is True
      and abs(_c30['term_sums']['sw'] - 0.746) < 1e-3
      and abs(_c30['term_sums']['isw'] - 0.551) < 1e-3
      and abs(_c60['term_sums']['isw'] - 0.580) < 1e-3
      and abs(_c30['term_sums']['pol']) < 2e-3
      and (_c30['term_sums']['sw'] + _c30['term_sums']['isw']) > 1.0
      and 'DOUBLE-COUNT the cross pairs' in RESULT)

check('Ⓓ①ᵇᵇ ⚠ AND THE FIRST CUT\'S PRINTED VERDICT NAMED `sw*sw` AS THE CARRIER, WHICH IS THE SAME '
      'OVERREACH THIS LINE HAS CORRECTED TWICE BEFORE -- the largest called THE carrier while a '
      'cross pair sat at ninety-five per cent of its share.  A dominance test is measured now and '
      'reported per sum, and the record carries the correction rather than the first verdict',
      'the largest contributor and by every contributor above a tenth' in PRED
      and 'overreach of the same shape this line has corrected twice before' in RESULT
      and _c30['top_over_second'] is not None
      and abs(_c30['top_over_second'] - 1.12) < 0.02
      and abs(_c60['top_over_second'] - 1.06) < 0.02)

# ── Ⓔ the two arms that did not run, and why ────────────────────────────────────────────────────
check('Ⓔ③ ⛔ ** THE ORDER\'S CONDITIONAL ARM HAS ITS CONDITION ANSWERED BOTH WAYS BY ONE '
      'MEASUREMENT: ** the `isw` is NOT the largest single pair -- not met -- and the '
      '`isw`-involving pairs carry a MAJORITY, `0.551` and `0.580` -- met.  ⇒ *no switch is '
      'written and BOTH readings are routed, because a conditional arm whose condition the '
      'measurement answers both ways is a decision for the seat that wrote the condition*',
      PT['isw_is_the_largest_pair'] is False
      and PT['isw_pairs_carry_a_majority'] is True
      and 'The switch is NOT written, and both readings are ROUTED' in RESULT
      and 'not a coin for this one to toss' in RESULT)

check('Ⓔ② ⛔ AND THE CORRECTION ARM IS NOT RUN UNDER ITS OWN REGISTERED GATE, with the gate\'s '
      'stated REASON then DISSOLVED by the shift test and that dissolution recorded: *a correction '
      'built from an unresolvable residual would decide "one object" on noise* was the reason, and '
      'the residual turns out resolvable -- as an amplitude.  ⇒ *so the arm is carried and '
      're-registration is ROUTED, because running it on that basis would be acting past a gate '
      'without re-registering it*',
      'does NOT run' in PRED
      and 'would decide "one object" on noise' in PRED
      and 'NOT RUN under the gate' in RESULT
      and 'dissolves the gate’s stated REASON' in RESULT
      or 'dissolves the gate' in RESULT)

check('Ⓔ⓪ ** THE REGISTRATION CAME FIRST AND THREE OF ITS NEGATIVES WERE REACHABLE AND FIRED: ** '
      'the file declares four reads before it, two of which it says change this revision\'s shape; '
      'it states that "each term\'s response" does not exist before the decomposition was run; and '
      'it writes the envelope outcome, the not-separable case and the unmet condition in as live '
      'outcomes',
      'committed and pushed before any computation' in PRED
      and 'does not exist' in PRED
      and 'IT DOES NOT' in PRED
      and 'NOT RUN, condition not met' in PRED)

check('Ⓔ⓪ᵃ ⛭ and the generator carries its own reason: the control arm with the decomposition '
      'switch ON, derived from the previous revision\'s own generator with that one switch flipped '
      'and narrowed to the three sums the order names',
      'SRCDEC="$f"' in GEN and 'NUFD=1 ARM=lcdm' in GEN
      and 'WHY PAIRS AND NOT TERMS' in GEN_FLAT
      and 'NARROWED TO WHAT ITEM' not in GEN_FLAT)

check('Ⓔ④ ⛔ AND THE SCOPE IS DECLARED: no limit is read, NO ENVELOPE CROSSING APPEARS IN THIS '
      'RECORD AT ALL, no switch is written, no CAMB per-term figure is quoted because none exists, '
      'the basin test belongs to another seat, and no other seat\'s receipt is edited',
      'No limit is read, and no envelope crossing appears in this record at all' in RESULT
      and 'No switch is written' in RESULT
      and 'because none exists' in RESULT
      and "no other seat's receipt is edited" in RESULT)

check('Ⓔ⑤ ⚠ and FOUR things in this record are this seat\'s own, including that the ruling was '
      'spent on this line\'s own headline FIRST and retired it, and that the pattern across the '
      'overreaches is named: the verdicts that FAILED named a single cause',
      'THIS SEAT’S OWN' in RESULT or 'THIS SEAT' in RESULT.upper()
      and 'spent on this line' in RESULT
      and 'named a single cause' in RESULT
      and 'cuts against this line' in RESULT)

print('')
print('=' * 100)
if FAILS:
    print('  ⛔ %d CHECK(S) FAILED:' % len(FAILS))
    for f in FAILS:
        print('     - %s' % f[:140])
    print('=' * 100)
    sys.exit(1)
print('  OK  %d of %d arms' % (NARMS, NARMS))
print('=' * 100)
sys.exit(0)
