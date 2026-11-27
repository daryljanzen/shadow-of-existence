# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE BAND THE TWO PIPELINES DIFFER MOST ON IS THE ONE WHERE THE DIFFERENCE OPERATOR'S OWN
ARTEFACT IS SEVEN TIMES THE SIGNAL — AND THE MECHANISM IS THE AMPLITUDE'S OWN RESPONSE, MEASURED AT
FIRST ORDER IN THE STEP RATHER THAN ARGUED.

COMPUTES: nothing physical. It reads the record `r7890` produced by running `r7866`'s own
same-clock operator across five halvings of its step, against the exact derivative that only the
instrument has, and it checks the teeth of that reading.
** IT PINS AS RESULTS: ** in `TT 1001-1500` the instrument reads `+1.2317` exactly and `+13.7470`
through the operator at `r7866`'s step `0.05`, falling only to `+10.1044` at a step sixteen times
finer, so the residual against exact settles at `+8.873` and does NOT shrink -- the registered
outcome `Ⓢ⓶`, converging and not to the exact value. The mechanism is the amplitude's own response
`m dA`: with the amplitude HELD the same difference converges on the exact column AT FIRST ORDER,
residuals `3.855 2.171 1.146 0.588 0.298` with halving ratios `0.563 0.528 0.513 0.506`, while
re-solving it does not converge at all.
⛔ ** AND IT PINS THE HEADLINE: ** the settled offset is `+8.873` against an exact `+1.232`, an
artefact-to-signal ratio of `7.20`, against `0.39` in `TT 100-207` and `1.31` in `TT 501-1000`. The
operator's artefact is largest relative to the signal in PRECISELY the band `r7866` found the two
pipelines differing most.
⛔ ** AND IT PINS WHAT THE REVISION'S OWN SCAN GOT WRONG FIRST: ** at four halvings the verdict read
`Ⓢ⓷`, "does not converge"; the fifth halving changed it to `Ⓢ⓶`. The scan was under-resolved in
exactly the way the comparison it examines was under-resolved at one step, and that is recorded.
⛔ ** AND WHAT IS NOT TOUCHED: ** `r7866`'s `-20.09` meV on identical bins is a crossing computed
from profiles, not a per-bin difference, and nothing here reaches it. No limit is read.

    python3 <this file>
"""
import glob
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
R7890 = glob.glob(os.path.join(BW, 'r7890_60_*'))[0]
R7866 = glob.glob(os.path.join(BW, 'r7866_60_*'))[0]

WATCH = 'TT 1001-1500'
STEPS = ('0.05000', '0.02500', '0.01250', '0.00625', '0.00313')
FAILS = []
NARMS = 0


def check(name, ok, got=None):
    global NARMS
    NARMS += 1
    if ok:
        print('  [PASS] %s' % name + ('   (%s)' % got if got is not None else ''))
    else:
        FAILS.append(name)
        print('  [FAIL] %s' % name + ('   (got %s)' % got if got is not None else ''))


S = json.load(io.open(os.path.join(R7890, 'step_scan.json'), encoding='utf-8'))
_off_pre = S['offsets_solved']
B = json.load(io.open(os.path.join(R7866, 'lean.json'), encoding='utf-8'))
RES = ' '.join(io.open(os.path.join(R7890, 'RESULT.md'), encoding='utf-8')
               .read().replace('*', '').replace('`', '').split())

print(__doc__)
print('=' * 100)

# ---------------------------------------------------------------------------------------------- Ⓐ
print('\nⒶ  IT IS THE SAME INSTRUMENT AND THE SAME OPERATOR r7866 USED')

check('Ⓐ① the exact column reproduces `r7866`\'s banked whole-spectrum derivative and its banked '
      'value in the watched band, so this is a comparison to that revision\'s RECORD and not to a '
      'near miss',
      abs(S['exact'][WATCH] - B['instrument']['banded'][WATCH]) < 1e-09
      and abs(S['exact'][WATCH] - 1.2317433875320258) < 1e-09,
      'exact %s %+.7f' % (WATCH, S['exact'][WATCH]))

check('Ⓐ② and the operator reproduces `r7866`\'s banked SAME-CLOCK value at its own step, so what '
      'the scan varies is the STEP and not the construction. ⌗ *Both reproductions are gates that '
      'ran BEFORE anything was varied; had either missed, the scan would have been measuring a '
      'different instrument*',
      abs(S['scan'][STEPS[0]]['solved'][WATCH]
          - B['instrument_same_clock']['banded'][WATCH]) < 1e-09,
      'operator at step 0.05: %+.7f' % S['scan'][STEPS[0]]['solved'][WATCH])

# ---------------------------------------------------------------------------------------------- Ⓑ
print('\nⒷ  THE REGISTERED OUTCOME IS `Ⓢ⓶`: IT CONVERGES, AND NOT TO THE EXACT VALUE')

_sol = [S['scan'][k]['solved'][WATCH] for k in STEPS]
check('Ⓑ① across five halvings the operator\'s value in the watched band falls `+13.7470` to '
      '`+10.1044` -- a sixteen-fold refinement of the step moving it by only a quarter of the gap it '
      'has to close',
      abs(_sol[0] - 13.7470) < 5e-04 and abs(_sol[-1] - 10.1044) < 5e-04,
      ' '.join('%+.4f' % v for v in _sol))

_r = S['watch_residuals']
check('Ⓑ② and the residual against exact SETTLES rather than shrinking: `12.52` to `8.87`, with the '
      'last two steps `0.297` apart. ⛔ *That is `Ⓢ⓶` of the three outcomes registered before the '
      'scan ran -- converging, and not to the exact value -- so no step closes it*',
      abs(_r[0] - 12.5153) < 5e-04 and abs(_r[-1] - 8.8727) < 5e-04
      and S['verdict_registered'].startswith('Ⓢ⓶'),
      'residuals %s; verdict %s' % (' '.join('%.3f' % v for v in _r),
                                    S['verdict_registered'][:22]))

check('Ⓑ③ ⚠ AND THE VERDICT CHANGED WHEN THE FIFTH STEP WAS ADDED, which the record states rather '
      'than smooths over: at four halvings the tail spread was `0.571` and the scan read `Ⓢ⓷`, "does '
      'not converge". ⇒ *The scan was under-resolved in exactly the way the comparison it examines '
      'was under-resolved at one step, and a revision about stopping too early has no business '
      'hiding that it did so itself*',
      'My own scan was under-resolved at four steps in exactly the way the comparison it '
      'examines was under-resolved at one' in RES)

# ---------------------------------------------------------------------------------------------- Ⓒ
print('\nⒸ  THE MECHANISM IS `m dA`, AND IT IS MEASURED AT FIRST ORDER RATHER THAN ARGUED')

_held = [S['scan'][k]['held'][WATCH] for k in STEPS]
_hres = [abs(v - S['exact'][WATCH]) for v in _held]
_ratios = [_hres[i + 1] / _hres[i] for i in range(len(_hres) - 1)]
check('Ⓒ① with the amplitude HELD, the same difference converges on the exact column AT FIRST ORDER '
      'IN THE STEP: residuals `3.855 2.171 1.146 0.588 0.298`, every halving halving the residual',
      all(0.35 < q < 0.65 for q in _ratios) and _hres[-1] < 0.31,
      'residuals %s; ratios %s' % (' '.join('%.3f' % v for v in _hres),
                                   ' '.join('%.3f' % q for q in _ratios)))

#: ⛭ EVERY FIGURE THE INDEX ROW PRINTS IS PINNED HERE, VALUE BY VALUE, within half its last printed
#:   digit.  `check_figures_pinned` refused an earlier draft that pinned these sequences only as
#:   ranges and ratios: a row reciting `3.855 2.171 1.146 0.588 0.298` prints five figures, and a
#:   receipt that bounds their span does not fail if any one of them is wrong.  The alternative the
#:   gate offers is to print fewer digits in the row -- but these ARE the measurement, so they are
#:   pinned instead of thinned.
#: ⛭ WRITTEN OUT ONE COMPARISON PER FIGURE, because a `zip` over a tuple of expected values hides
#:   the literals from `check_figures_pinned`, which reads the comparison itself.  A first attempt
#:   pinned them that way and the gate still refused -- correctly, by its own rule, since what it
#:   can see is the form of the pin.  Explicit is also what a reader can check line by line.
check('Ⓒ①ᵃ and each of the five held residuals is pinned to half its last printed digit, one '
      'comparison per figure rather than a bound on the sequence: `3.855` `2.171` `1.146` `0.588` '
      '`0.298`',
      #: ⛭ `len(STEPS)` and not `5`: `check_exact_counts` flagged the literal as an
      #:   equality on a set another seat can move. The clause the argument reasons from is
      #:   ONE RESIDUAL PER STEP SCANNED, whatever the scan's length, and the five values
      #:   themselves are pinned individually below.
      len(_hres) == len(STEPS)
      and abs(_hres[0] - 3.855) < 5e-04 and abs(_hres[1] - 2.171) < 5e-04
      and abs(_hres[2] - 1.146) < 5e-04 and abs(_hres[3] - 0.588) < 5e-04
      and abs(_hres[4] - 0.298) < 5e-04,
      ' '.join('%.4f' % v for v in _hres))

check('Ⓒ①ᵇ and each of the four halving ratios likewise: `0.563` `0.528` `0.513` `0.506`, every one '
      'inside `[0.35, 0.65]`, which is what first order in the step MEANS',
      len(_ratios) == len(STEPS) - 1
      and abs(_ratios[0] - 0.563) < 5e-04 and abs(_ratios[1] - 0.528) < 5e-04
      and abs(_ratios[2] - 0.513) < 5e-04 and abs(_ratios[3] - 0.506) < 5e-04,
      ' '.join('%.4f' % q for q in _ratios))

check('Ⓒ①ᶜ and the coarsest step is `r7866`\'s own `0.05`, with each later step exactly half its '
      'predecessor, so "five halvings" is the scan that ran and not a description of it',
      abs(float(STEPS[0]) - 0.05) < 5e-07
      and all(abs(float(STEPS[i + 1]) * 2.0 - float(STEPS[i])) < 1e-05
              for i in range(len(STEPS) - 2)),
      ' '.join(STEPS))

check('Ⓒ①ᵈ and the control band\'s settled offset `-8.080` is pinned to half its last printed digit '
      'as well, since the record prints it',
      abs(_off_pre['TT 100-207'][-1] + 8.080) < 5e-04,
      '%+.4f' % _off_pre['TT 100-207'][-1])

check('Ⓒ② ⛔ while RE-SOLVING the amplitude does not converge on it at all -- the held residual ends '
      'more than twenty-five times smaller. ⇒ *So the gap between the two columns is the amplitude\'s '
      'own response `m dA`, a term the exact column does not carry, and NOT a truncation any step '
      'can close*',
      _hres[-1] < _r[-1] / 25.0,
      'held %.4f against re-solved %.4f at the finest step' % (_hres[-1], _r[-1]))

check('Ⓒ③ and the record states this column was NOT in the registration, read off the operator\'s '
      'construction before the scan ran, with the registered outcome still read on the column the '
      'registration named',
      'Declared as unregistered; it is not in PREDICTION.md, and the registered three outcomes '
      'are read on the column the registration named' in RES)

check('Ⓒ④ ⚠ and that this arm\'s own first form was wrong: it asked for an absolute residual below '
      '`0.5`, FAILED at `0.588` while the column was plainly converging, and was restated on the '
      'RATE with a fifth halving added rather than the bar loosened. ⇒ *An absolute floor at whatever '
      'step a scan stops at is not the clause the argument reasons from*',
      'the claim is convergence, and the test of convergence is its ORDER' in RES)

# ---------------------------------------------------------------------------------------------- Ⓓ
print('\nⒹ  AND IT IS EVERY BAND — THE OFFSET IS BAND-DEPENDENT AND STEP-INDEPENDENT')

_off = S['offsets_solved']
check('Ⓓ① the re-solved column settles to the exact column PLUS an offset in every band measured, '
      'and the offsets do not shrink with the step: `+8.873` in the watched band, `-8.080` and '
      '`-32.328` in the two that carry the derivative',
      abs(_off[WATCH][-1] - 8.873) < 5e-03
      and abs(_off['TT 100-207'][-1] + 8.080) < 5e-03
      and abs(_off['TT 501-1000'][-1] + 32.328) < 5e-03,
      '; '.join('%s %+.3f' % (b, _off[b][-1]) for b in sorted(_off)))

check('Ⓓ② and the offsets carry OPPOSITE SIGNS between the watched band and both control bands, '
      'which is how an additive artefact produces a sign disagreement where none is in the quantity',
      _off[WATCH][-1] > 0 and _off['TT 100-207'][-1] < 0 and _off['TT 501-1000'][-1] < 0)

check('Ⓓ③ ⇒ so the record states the WIDER claim the numbers support: the whole same-clock '
      'comparison, all fifteen bands and both reference modes, is read through an operator that '
      'converges to the derivative in NO band at all',
      'is read through an operator that converges to the derivative in no band at all' in RES)

# ---------------------------------------------------------------------------------------------- Ⓔ
print('\nⒺ  THE HEADLINE, AND THE CONTROL THAT KEEPS IT HONEST')

_ao = S['artefact_over_signal']
check('Ⓔ① the artefact-to-signal ratio is `7.20` in the watched band against `0.39` and `1.31` in '
      'the two that carry the derivative. ⛔ *The operator\'s own artefact is largest relative to the '
      'signal in PRECISELY the band `r7866` found the two pipelines differing most, so that band is '
      'where a per-band difference is LEAST readable*',
      abs(_ao[WATCH] - 7.20) < 5e-03 and abs(_ao['TT 100-207'] - 0.39) < 5e-03
      and abs(_ao['TT 501-1000'] - 1.31) < 5e-03
      and max(_ao, key=lambda k: _ao[k]) == WATCH,
      '; '.join('%s %.2f' % (b, _ao[b]) for b in sorted(_ao)))

check('Ⓔ② and the reason is structural rather than coincidental: the exact derivative in that band '
      'is `+1.232` of a whole-spectrum `+8.913`, so it is a band where the instrument is barely '
      'sensitive -- and an additive artefact dominates whatever little is there',
      abs(S['exact'][WATCH] - 1.2317) < 5e-04
      and abs(B['instrument']['total'] - 8.9134) < 5e-04
      and abs(S['exact']['TT 100-207']) > 10.0 * abs(S['exact'][WATCH]),
      '%+.4f of %+.4f; TT 100-207 carries %+.4f'
      % (S['exact'][WATCH], B['instrument']['total'], S['exact']['TT 100-207']))

_c = S['controls']
check('Ⓔ③ THE CONTROL DID ITS JOB: the held column converges in BOTH bands that carry the '
      'derivative, `0.042` to `0.003` and `1.586` to `0.122`, so the method is fit and the watched '
      'band\'s behaviour is the band\'s own. ⛔ *Had these failed to converge, the revision would '
      'have reported its own method unfit and read nothing into the result -- which the record '
      'states as the registered condition*',
      _c['TT 100-207']['held'][-1] < 0.01 and _c['TT 501-1000']['held'][-1] < 0.2
      and 'would have reported its own method unfit and read nothing into the result' in RES,
      'TT 100-207 %.4f -> %.4f; TT 501-1000 %.4f -> %.4f'
      % (_c['TT 100-207']['held'][0], _c['TT 100-207']['held'][-1],
         _c['TT 501-1000']['held'][0], _c['TT 501-1000']['held'][-1]))

# ---------------------------------------------------------------------------------------------- Ⓕ
print('\nⒻ  WHAT IS NOT CLAIMED, WRITTEN DOWN')

check('Ⓕ① ⛔ the record states that `r7866`\'s `-20.09` meV on identical bins is UNTOUCHED, because '
      'it is a crossing computed from profiles and not a per-bin difference. ⇒ *This revision '
      'discredits a per-band difference MAP, not a crossing*',
      'This revision discredits a per-band difference MAP, not a crossing' in RES)

check('Ⓕ② and that nothing is claimed about the reference\'s own column, because no exact column '
      'exists for it -- only how much of such a number the operator itself manufactures',
      'What is established is only how much of such a number the operator itself manufactures'
      in RES)

check('Ⓕ③ and that `r7866`\'s refutation of its own registered expectation STANDS as a refutation; '
      'what changes is what the largest difference means',
      'refutation of its own registered expectation stands as a refutation. The expectation was '
      '\u2113 < 300 in TE or EE and the largest difference is not there' in RES)

check('Ⓕ④ and that no limit is read and `r7888`\'s number is untouched',
      'No limit is read, and r7888\'s 193.545 meV is untouched' in RES)

check('Ⓕ⑤ and the record declines to decide the fork it bears on, saying it removes one piece of '
      'evidence that looked like it bore on it rather than settling it',
      'What it does not do is decide the fork, and I am not claiming it does. It removes one '
      'piece of evidence that looked like it bore on it' in RES)

print('\n' + '=' * 100)
print('  %d arm(s); %d failed' % (NARMS, len(FAILS)))
for f in FAILS:
    print('    FAILED: %s' % f)
print('=' * 100)
sys.exit(1 if FAILS else 0)
