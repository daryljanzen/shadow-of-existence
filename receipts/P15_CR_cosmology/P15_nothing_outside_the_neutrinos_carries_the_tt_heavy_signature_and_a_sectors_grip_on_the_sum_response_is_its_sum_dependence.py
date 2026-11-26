# -*- coding: utf-8 -*-
"""⛭⛭⛭ NOTHING OUTSIDE THE NEUTRINOS CARRIES THE TT-HEAVY SIGNATURE, SO THE DIAGNOSTIC BRANCH IS
CLOSED; THE RADIATION-DENSITY CORRECTION IS EE-HEAVY AND PULLS THE OTHER WAY; AND A SECTOR'S GRIP ON
THE SUM RESPONSE IS ITS SUM DEPENDENCE AND NOTHING ELSE.

COMPUTES: the sum-response amplitude leverage of every sector the existing banks hold at more than
one sum -- the radiation-density correction at both of its banked step sizes, the Fermi-Dirac
background on against off, and the baryon-velocity term on against off -- each fitted against CAMB
by the fit of record, executed and not re-implemented, with its reproduction leg required to return
that fit's four headline amplitudes first; the leverage the arm of record REQUIRES, re-measured by
the same run rather than carried over; the step control that separates a property of a sector from a
property of a step; and the readability floor that keeps a ratio of two roundings from being read as
a leverage.
** IT PINS AS RESULTS: the required leverage `10.790` at `0.30` eV and `6.392` at `0.60`, from TT's
`0.15162` and `0.29592` against EE's `0.01405` and `0.04630`; the radiation-density correction's
leverage `0.498` and `0.530` at the smaller step and `0.422` and `0.523` at the larger, which are
`0.046`, `0.083`, `0.039` and `0.082` of what is required -- EE-heavy, and the WRONG SIGN of
asymmetry rather than a weak version of the right one; the step control's `1.179` and `1.013`, which
put that leverage in the sector and not in the step; the Fermi-Dirac background's `275.037` and
`10.212`, which are `25.490` and `1.598` of required; and the baryon-velocity term's move of
`1.733e-05` and `1.523e-07` in the two blocks, below the fit's own last printed digit. **
⛔ ** AND IT PINS A GAP IN THIS SEAT'S OWN REGISTRATION: ** the registration put "has no readable
move" in one verdict row and never said what readable means. The threshold is taken from the FIT --
five decimals in `A`, so `1e-05` -- and not from this measurement, and the verdict row is the same
whether the gap is filled that way or the candidate is dropped, which is pinned here because a
repair that could have changed the answer would need more than a footnote.
⛔ ** AND IT PINS THAT EXACTLY ONE REGISTERED ROW FIRES, ** which the previous revision's own item
could not say.
⛔ ** NO LIMIT IS PINNED HERE AND NONE WAS READ. ** The order puts the limit behind the next item's
joint validation, and nothing in this revision reaches it. ** AND THE FOUR COSMOLOGICAL PARAMETERS
ARE NOT ANSWERED: ** every offset leg in the banks is at zero sum, which the registration declared
in advance as a limit of the banks rather than a finding about the parameters.

⌷ ** THE ID. **  `69` ordered this as `r7879`, which merged `r7878`, refined its EE ruling to joint
agreement for a closure-respecting sector, took this line's unregistered leverage read as the frame,
and ruled branch `(b)` first and bounded to ONE revision with `(a)` as the repair.

⚠ ** TWO THINGS IN THIS RECORD ARE THIS SEAT'S OWN: ** the registration gap above, and the fact
that the only TT-heavy sector in the banks is the neutrino background itself -- which is not a
sector outside the neutrinos and so cannot answer the branch whatever its number.

    NODE=60 python3 <this file>

Written r7880 (60).  Stated for reversal.
"""
import io
import json
import os
import sys

import numpy

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
D = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                 'r7880_60_what_sets_the_tt_ee_leverage')
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
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

LV = load('leverage.json')
#: ⛔ *the prose is matched on a WHITESPACE-FLATTENED copy -- four arms of an earlier revision's
#: receipt failed on where a line happened to wrap, which is a fact about the editor and not about
#: the record.*
RESULT = ' '.join(text('RESULT.md').split())
PRED = ' '.join(text('PREDICTION.md').split())
SRC = text('leverage.py')
REQ = LV['required']
A = LV['arms']
S = ('0.30', '0.60')
DN1, DN2 = '⓵ DNEFF = 0.0293', '⓶ DNEFF = 0.044'
NUFD, BVEL = '⓷ NUFD off', '⓸ BVEL off'

# ══ Ⓐ THE FIT IS THE ONE OF RECORD, AND IT REPRODUCED ═══════════════════════════════════════════

check('Ⓐ①ᵃ ⛭ ** THE REPRODUCTION LEG REPRODUCED: ** the fit of record returns `1.15162`, `1.29592`, '
      '`1.01405` and `1.04630` on the landed bank, so the leverages below are read through the fit '
      'the arm of record was judged on',
      LV['reproduced'] is True
      and abs(LV['landed']['TT|0.30'] - 1.15162) < 5e-06
      and abs(LV['landed']['TT|0.60'] - 1.29592) < 5e-06
      and abs(LV['landed']['EE|0.30'] - 1.01405) < 5e-06
      and abs(LV['landed']['EE|0.60'] - 1.04630) < 5e-06)

check('Ⓐ①ᵇ ⛭ ** AND NEITHER THE FIT NOR ITS REBINDING IS COPIED: ** the fit is executed from the '
      'file of record and the rebinding function is IMPORTED from the revision that wrote it.  ⇒ '
      '*so there is no second copy of either, and the comparison is not between two instruments*',
      'from refit import the_two_rebindings' in SRC
      and 'the_two_rebindings(io.open(SHIFT, encoding=' in SRC
      and SRC.count('def the_two_rebindings') == 0)

check('Ⓐ①ᶜ ⛭⛭ ** THE REQUIRED LEVERAGE IS RE-MEASURED BY THIS RUN AND NOT CARRIED OVER: ** `10.790` '
      'at `0.30` eV and `6.392` at `0.60`, from TT\'s `0.15162` and `0.29592` against EE\'s '
      '`0.01405` and `0.04630`.  ⇒ *and it agrees with the previous revision\'s figure to the last '
      'digit, which is what makes the two tables comparable*',
      abs(REQ['0.30']['leverage'] - 10.790) < 0.0005
      and abs(REQ['0.60']['leverage'] - 6.392) < 0.0005
      and abs(REQ['0.30']['tt'] - 0.15162) < 5e-06
      and abs(REQ['0.60']['tt'] - 0.29592) < 5e-06
      and abs(REQ['0.30']['ee'] - 0.01405) < 5e-06
      and abs(REQ['0.60']['ee'] - 0.04630) < 5e-06)

# ══ Ⓑ THE RADIATION-DENSITY CORRECTION IS EE-HEAVY ══════════════════════════════════════════════

#: ⌘ ** AND THE TWO SUMS ARE PINNED FROM THE BANKS' OWN RECORDED PROVENANCE, ** not printed beside
#:   a receipt that would not notice if they were wrong: the landed bank's config records the sum
#:   each of its legs ran at.
_MNU = {}
for _tag, _rel in (('0.30', 'lcdm_S030.npz'), ('0.60', 'lcdm_S060.npz')):
    _z = numpy.load(os.path.join(BW, 'bank', 'pol_grid_bvel1_nufd_only', _rel), allow_pickle=True)
    _MNU[_tag] = json.loads(str(_z['config']))['MNU']

check('Ⓐ①ᵈ ⛭ ** THE TWO SUMS THE WHOLE TABLE IS READ AT ARE `0.30` AND `0.60` eV, read off the '
      'landed bank\'s own recorded configuration: ** so a mislabelled column would fail here rather '
      'than pass as a figure nothing checks',
      abs(_MNU['0.30'] - 0.30) < 5e-09 and abs(_MNU['0.60'] - 0.60) < 5e-09
      and sorted(LV['required']) == ['0.30', '0.60'],
      'MNU = %s' % _MNU)

check('Ⓑ②ᵃ ⛭⛭ ** THE RADIATION-DENSITY CORRECTION IS EE-HEAVY, WHICH IS THE WRONG SIGN OF ASYMMETRY '
      'AND NOT A WEAK VERSION OF THE RIGHT ONE: ** leverage `0.498` and `0.530` at the smaller step '
      'and `0.422` and `0.523` at the larger, against a required `10.790` and `6.392`.  ⇒ *it moves '
      'about twice as much of EE as of TT, where what is wanted is six to eleven times as much TT '
      'as EE*',
      abs(A[DN1]['sums']['0.30']['leverage'] - 0.498) < 0.0005
      and abs(A[DN1]['sums']['0.60']['leverage'] - 0.530) < 0.0005
      and abs(A[DN2]['sums']['0.30']['leverage'] - 0.422) < 0.0005
      and abs(A[DN2]['sums']['0.60']['leverage'] - 0.523) < 0.0005
      and all(A[k]['sums'][s]['leverage'] < 1.0 for k in (DN1, DN2) for s in S))

check('Ⓑ②ᵇ ⛭ and as a fraction of what is required that is `0.046`, `0.083`, `0.039` and `0.082` -- '
      'four to eight per cent, and in the wrong direction',
      abs(A[DN1]['sums']['0.30']['of_required'] - 0.046) < 0.0005
      and abs(A[DN1]['sums']['0.60']['of_required'] - 0.083) < 0.0005
      and abs(A[DN2]['sums']['0.30']['of_required'] - 0.039) < 0.0005
      and abs(A[DN2]['sums']['0.60']['of_required'] - 0.082) < 0.0005)

check('Ⓑ②ᶜ ⛭⛭ ** AND THAT LEVERAGE IS A PROPERTY OF THE SECTOR AND NOT OF THE STEP, which is the '
      'control the registration fixed for exactly this: ** the two banked step sizes agree to '
      '`1.179` and `1.013`, inside the same `4/3` band.  ⇒ *a leverage that differed between two '
      'steps of one sector would have been a property of the step, and would have been reported '
      'UNREADABLE rather than as an answer either way*',
      abs(LV['step_control']['0.30']['ratio'] - 1.179) < 0.0005
      and abs(LV['step_control']['0.60']['ratio'] - 1.013) < 0.0005
      and all(LV['step_control'][s]['agrees'] is True for s in S)
      #: ⚠ *the literal is read off the record's bytes: the sentence begins after an emphasis
      #:   mark, so its first word is capitalised, and the leading article is left out of the pin
      #:   rather than guessed at.*
      and 'leverage that differs between the `+` and the `−` offset is not a property of the '
          'sector' in PRED)

# ══ Ⓒ THE ONLY TT-HEAVY SECTOR IS THE NEUTRINO BACKGROUND ITSELF ════════════════════════════════

check('Ⓒ③ᵃ ⛭⛭⛭ ** THE ONLY CANDIDATE WITH A TT-HEAVY SIGNATURE AT ALL IS THE NEUTRINO BACKGROUND '
      'ITSELF: ** `275.037` at `0.30` eV and `10.212` at `0.60`, which are `25.490` and `1.598` of '
      'required.  ⇒ *and it is not a sector OUTSIDE the neutrinos, so it cannot answer the branch '
      'whatever its number -- which is the finding and not a technicality*',
      abs(A[NUFD]['sums']['0.30']['leverage'] - 275.037) < 0.0005
      and abs(A[NUFD]['sums']['0.60']['leverage'] - 10.212) < 0.0005
      and abs(A[NUFD]['sums']['0.30']['of_required'] - 25.490) < 0.0005
      and abs(A[NUFD]['sums']['0.60']['of_required'] - 1.598) < 0.0005
      and all(A[NUFD]['sums'][s]['leverage'] > REQ[s]['leverage'] for s in S))

check('Ⓒ③ᵇ ⛭ ** AND THE NEAR THING IS SAID OUT LOUD AND THE BAND IS NOT MOVED: ** at `0.60` eV it '
      'is `1.598` of required against a band edge of `1.333`.  ⌗ *At `0.30` it is `25` times '
      'required, so the pair is not in band at both sums under any reading, and the leverage is '
      'nowhere near constant in the sum*',
      A[NUFD]['sums']['0.60']['in_band'] is False
      and A[NUFD]['sums']['0.30']['in_band'] is False
      and abs(LV['band'] - 4.0 / 3.0) < 1e-12
      and A[NUFD]['sums']['0.30']['leverage'] / A[NUFD]['sums']['0.60']['leverage'] > 20)

# ══ Ⓓ THE BARYON-VELOCITY TERM DOES NOT MOVE THE SUM RESPONSE ═══════════════════════════════════

check('Ⓓ④ᵃ ⛭ ** THE BARYON-VELOCITY TERM\'S SUM RESPONSE IS UNMOVED AT THE FIT\'S OWN PRECISION: ** '
      '`1.733e-05` in TT and `1.523e-07` in EE, against the `0.15162` and `0.29592` that would have '
      'to be removed',
      abs(A[BVEL]['sums']['0.30']['d_tt'] - 1.733e-05) < 5e-09
      and abs(A[BVEL]['sums']['0.30']['d_ee'] - 1.523e-07) < 5e-11
      and A[BVEL]['sums']['0.30']['readable'] is False
      and A[BVEL]['sums']['0.60']['readable'] is False
      and A[BVEL]['sums']['0.30']['leverage'] is None)

check('Ⓓ④ᵇ ⛔⛭⛭ ** AND THE READABILITY FLOOR IS A GAP IN THIS SEAT\'S OWN REGISTRATION, NAMED RATHER '
      'THAN QUIETLY FILLED: ** the registration put "has no readable move" in a verdict row and '
      'never said what readable means.  The threshold is taken from the FIT -- five decimals in '
      '`A`, so `1e-05` -- and not from this measurement.  ⇒ *and the verdict row is the same whether '
      'the gap is filled that way or the candidate is dropped, which is said because a repair that '
      'could have changed the answer would need more than a footnote*',
      'has no readable move' in PRED
      and 'A GAP IN THIS SEAT\'S OWN REGISTRATION, NAMED RATHER THAN QUIETLY FILLED' in RESULT
      and 'the verdict row is the same either way' in RESULT
      and 'READABLE = 1e-05' in SRC)

# ══ Ⓔ THE REGISTERED ARGUMENT, CONFIRMED BY SIZE ════════════════════════════════════════════════

check('Ⓔ⑤ᵃ ⛭⛭ ** THE ARGUMENT REGISTERED BEFORE THE MEASUREMENT IS CONFIRMED BY SIZE ON ALL THREE '
      'READABLE CANDIDATES: ** a sector\'s grip on the sum response is its SUM DEPENDENCE and '
      'nothing else.  The term that is the same at every sum moves `A` by parts in a million; the '
      'density the sum interacts with, by parts in a thousand; the sum\'s own background, by a third '
      'to a half',
      max(abs(A[BVEL]['sums'][s][k]) for s in S for k in ('d_tt', 'd_ee')) < 1e-04
      and 1e-03 < max(abs(A[DN2]['sums'][s][k]) for s in S for k in ('d_tt', 'd_ee')) < 1e-01
      and min(abs(A[NUFD]['sums'][s]['d_tt']) for s in S) > 0.3
      #: ⚠ *and this one spans a block-quote marker, which the whitespace flattening keeps, so
      #:   the pin is on the clause and not on the sentence that carries the `>` in its middle.*
      and 'effect on `D_ℓ` is **sum-dependent**' in PRED)

check('Ⓔ⑤ᵇ ⛭ and it was registered AS AN ARGUMENT TO BE CHECKED and not asserted, with the '
      'consequence for the existing banks stated in advance rather than discovered: every parameter '
      'offset leg is at zero sum, so the banks cannot show a parameter\'s sum dependence',
      'This is an argument, not a measurement' in PRED
      and 'a limit of the banks' in PRED
      and 'the four parameter offsets are banked **only at `Σ = 0`**' in PRED)

# ══ Ⓕ THE VERDICT, AND THAT EXACTLY ONE ROW FIRES ═══════════════════════════════════════════════

check('Ⓕ⑥ᵃ ⛭⛭ ** THE VERDICT IS `Ⓒ` -- NOTHING OUTSIDE THE NEUTRINOS CARRIES IT, AND THE BRANCH IS '
      'CLOSED -- AND EXACTLY ONE REGISTERED ROW FIRES, ** which the previous revision\'s own item '
      'could not say',
      LV['verdict'] == 'C'
      and LV['exactly_one_fires'] is True
      and LV['rows'] == {'A': False, 'B': False, 'C': True, 'D': False},
      'verdict %s, rows %s' % (LV['verdict'], LV['rows']))

check('Ⓕ⑥ᵇ ⛭ ** AND THE TWO NULLS WERE REGISTERED AS DIFFERENT ANSWERS AND ARE NOT COLLAPSED: ** '
      'the row that fired closes the branch; the row that did not would have left it open because '
      'the banks could not answer it.  ⇒ *one candidate IS unreadable, and that is why the '
      'distinction had to be registered rather than invented here*',
      'are different answers and are not to be collapsed' in PRED
      and LV['rows']['D'] is False
      and sum(1 for s in S if A[BVEL]['sums'][s]['readable']) == 0
      and sum(1 for k in A for s in S if A[k]['sums'][s]['readable']) == 6)

check('Ⓕ⑥ᶜ ⛭ ** AND NO LIMIT IS READ: ** the order puts the limit behind the next item\'s joint '
      'validation, and the record says so',
      'NO LIMIT IS READ IN THIS REVISION, under any outcome' in PRED
      and 'No limit is read**, under any outcome' in RESULT)

check('Ⓕ⑥ᵈ ⌗ and the candidate set was CLOSED in the registration before any of it was measured, '
      'with four candidates and no fifth added after a number was seen',
      len(LV['arms']) == 4
      and 'Closed here so that no candidate can be added after its number is seen' in PRED
      and sorted(LV['arms']) == sorted([DN1, DN2, NUFD, BVEL]))

check('Ⓕ⑥ᵉ ⌗ and the one candidate whose provenance rests on a directory name is marked as such in '
      'the record, which was declared in the registration before it was read',
      A[BVEL]['provenance_recorded'] is False
      and all(A[k]['provenance_recorded'] for k in (DN1, DN2, NUFD))
      and 'the only evidence of what they ran with is the **directory name**' in PRED
      #: ⚠ *`'directory name only'` was the first pin here and it is three words that could turn
      #:   up anywhere; a weak key is better REPLACED than adjudicated, so the pin is on the
      #:   record's own sentence about this candidate instead.*
      and "**`BVEL`'s provenance rests on a directory name.**" in RESULT)

print('=' * 100)
print('  %d arm(s), %d failed' % (NARMS, len(FAILS)))
for f in FAILS:
    print('   FAILED: %s' % f)
sys.exit(1 if FAILS else 0)
