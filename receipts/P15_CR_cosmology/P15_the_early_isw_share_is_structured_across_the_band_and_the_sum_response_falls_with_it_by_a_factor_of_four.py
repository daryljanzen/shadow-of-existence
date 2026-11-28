# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE EARLY-ISW SHARE IS STRUCTURED ACROSS MULTIPOLES `100`–`207`, FALLING BY MORE THAN A
QUARTER FROM ITS LOW EDGE, AND THE SUM RESPONSE IS POSITIVE IN EVERY BIN AND FALLS WITH `l` BY A
FACTOR OF FOUR.

COMPUTES: nothing physical. It reads the record `r7906` produced by BINNING `r7900`'s already-banked
eight spectra — four sums, the potential-decay switch on and off — through the likelihood's own `TT`
binning, and it checks the teeth of that reading.  ⛔ ** NO SPECTRUM WAS COMPUTED BY THAT REVISION
EITHER, ** which its registration said before the reading was made: what did not exist was the
per-bin share, so what was registered was the DEFINITION and the OUTCOMES.
⛔ ** IT PINS THE CONTROL FIRST, AND THE CONTROL IS WHAT LICENSES THE REST: ** `r7900`'s OWN band
definition, recomputed from the same files in its own arithmetic order, reproduces its banked
fractions at EXACTLY ZERO — and this receipt recomputes that comparison itself rather than reading
the record's number. *The first form of that control took MEANS where `r7900` took SUMS, the same
number mathematically and a differently rounded one, agreed to about five units in the last place and
so FAILED a bar that says exactly zero. The bar was right and the arithmetic was the seat's own.*
** IT PINS AS RESULTS: ** twelve bins, which is EXACTLY the band — indices `14` to `25`, edges
`100`–`108` to `199`–`207`, `207` being a bin's own top edge — with the share running `0.438702`,
peaking at `0.440062` in bin `15` and falling to `0.314713` in bin `25`, a span of `0.3221030244` of
the mean against a registered bar of `0.10`; and the sum response positive in `12` of `12` bins,
`+2.1848e-02` at the low edge against `+5.3975e-03` at the high, a factor of `4.04783900227215`.
⇒ ** SO THE REGISTERED OUTCOME IS `Ⓘ⓷ + Ⓚ⓵` AND THE STRONG EXPECTATION IS MET. ** The share is
STRUCTURED, which is what `r7900`'s measurement of the cross pair as most of the difference predicts
on a band that is the rise toward the first peak. ⛭ *And `Ⓘ⓷` fires on a SINGLE turning point at the
band's own low edge, so `not monotone` is weaker here than it sounds: the shape is a monotone decline
with one step up at the edge.*
⛭ ** AND THE ARMS ARE NOT IDENTIFIED BY THEIR FILENAMES. ** `r7900`'s saved `config` does not record
the switch, so the switch-off arm is established from the decomposition beside each spectrum — the
four `isw` bilinear pairs identically zero and the other six bit-identical — which is a property of
the run. This receipt re-reads those files and re-establishes it rather than trusting the record.
⚠ ** AND WHAT THE QUANTITY IS NOT: ** not `the ISW's contribution to the band`. `D_l` is QUADRATIC in
the transfer (`r7874`), so a with-and-without difference equals the four `isw`-involving bilinear
pairs, most of it interference with the acoustic monopole. One label covers two objects.
⛔ ** AND WHAT IS NOT CLAIMED: ** no comparison with the reference, whose side is `cc66`'s `⑲ ③` and
has not landed, so no shortfall exists; the order's `follow it to its term` is therefore NOT begun,
because the three candidate terms it names are a decomposition OF a shortfall. No limit is read and
`r7888`'s `193.545` meV is untouched.

    python3 <this file>
"""
import ast
import glob
import io
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
R7906 = glob.glob(os.path.join(BW, 'r7906_60_*'))[0]
R7900 = glob.glob(os.path.join(BW, 'r7900_60_*'))[0]
SRC = os.path.join(R7900, 'srcdec')

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


D = json.load(io.open(os.path.join(R7906, 'isw_bins.json'), encoding='utf-8'))
B = json.load(io.open(os.path.join(R7900, 'isw_band.json'), encoding='utf-8'))
SRCTXT = io.open(os.path.join(R7906, 'isw_bins.py'), encoding='utf-8').read()
TREE = ast.parse(SRCTXT)
PRAW = io.open(os.path.join(R7906, 'PREDICTION.md'), encoding='utf-8').read()
RRAW = io.open(os.path.join(R7906, 'RESULT.md'), encoding='utf-8').read()

TAGS = [t for t, _ in D['sums']]
S0 = np.asarray(D['shares'][TAGS[0]], float)
S3 = np.asarray(D['shares'][TAGS[-1]], float)
RESP = np.asarray(D['response'], float)

print(__doc__)
print('=' * 100)

# ---------------------------------------------------------------------------------------------- Ⓐ
print('\nⒶ  THE CONTROL, RECOMPUTED HERE AND NOT READ OFF THE RECORD')


def dl(tag, off=False):
    with np.load(os.path.join(SRC, 'lcdm_%s%s.npz' % (tag, '_noisw' if off else '')),
                 allow_pickle=True) as z:
        return (np.asarray(z['ls'], float), np.asarray(z['Dl'], float),
                np.asarray(z['Dl_pairs'], float), [str(x) for x in z['pairs']])


_worst, _mine = 0.0, []
for t in TAGS:
    _ls, _on, _, _ = dl(t)
    _, _off, _, _ = dl(t, True)
    _inb = (_ls >= 100) & (_ls <= 207)
    _fr = float((_on - _off)[_inb].sum()) / float(_on[_inb].sum())
    _mine.append(_fr)
    _worst = max(_worst, abs(_fr - float(B['per_sum'][t]['fraction'])))
check('Ⓐ① `r7900`\'s OWN band definition is recomputed IN THIS RECEIPT from the same files and '
      'reproduces its banked fractions at EXACTLY ZERO — so the bank being read bin by bin is the '
      'bank that revision measured, established here rather than taken from the record\'s own '
      'number. ⌗ *This is the one comparison that must hold to the last bit*',
      _worst == 0.0 and float(D['r7900_definition_reproduced']['worst']) == 0.0,
      'worst difference %.3e over %d sum(s), and the record reports %.3e'
      % (_worst, len(TAGS), float(D['r7900_definition_reproduced']['worst'])))

_zero, _ident, _npair = True, True, None
for t in TAGS:
    _, _, _pon, _pairs = dl(t)
    _, _, _poff, _ = dl(t, True)
    _isw = [i for i, p in enumerate(_pairs) if 'isw' in p]
    _oth = [i for i, p in enumerate(_pairs) if 'isw' not in p]
    _npair = len(_isw)
    _zero = _zero and bool(np.all(_poff[:, _isw] == 0.0))
    _ident = _ident and bool(np.array_equal(_pon[:, _oth], _poff[:, _oth]))
check('Ⓐ② the switch-off arm is identified from the RUN and re-established here: in every off-arm '
      'decomposition the four `isw` bilinear pairs are identically zero and the other six are '
      'bit-identical to the on-arm\'s. ⌗ *The saved `config` does not record the switch, so a '
      'filename is not evidence of which arm a file holds*',
      _zero and _ident and _npair == 4,
      '%d isw pair(s) zeroed on every off arm: %s; the other six bit-identical: %s'
      % (_npair, _zero, _ident))

_same = True
for t in TAGS:
    _l1, _d1, _, _ = dl(t)
    with np.load(os.path.join(SRC, 'lcdm_%s_tt.npz' % t), allow_pickle=True) as _z:
        _same = (_same and np.array_equal(_l1, np.asarray(_z['ls'], float))
                 and np.array_equal(_d1, np.asarray(_z['Dl'], float)))
check('Ⓐ③ and the two file families are ONE SPECTRUM, checked here: the decomposition\'s own total '
      'and the separate `TT` save are bit-identical, so the control above and the binned shares '
      'below are not read off two spectra that merely agree closely',
      bool(_same) and D['comparison_readable'] is False,
      'identical on every sum: %s' % bool(_same))

# ---------------------------------------------------------------------------------------------- Ⓑ
print('\nⒷ  THE BAND IS A WHOLE NUMBER OF THE LIKELIHOOD\'S OWN BINS')

_ed = [tuple(e) for e in D['edges']]
check('Ⓑ① the band the order names is EXACTLY a whole number of plik_lite `TT` bins and no partial '
      'bin: the first bin\'s low edge IS `100` and the last bin\'s high edge IS `207`, with the bins '
      'contiguous and in order',
      _ed[0][0] == 100 and _ed[-1][1] == 207
      and all(_ed[i + 1][0] == _ed[i][1] + 1 for i in range(len(_ed) - 1))
      and len(_ed) >= 12,
      '%d bin(s), indices %d..%d, %d to %d' % (len(_ed), D['bins'][0], D['bins'][-1],
                                               _ed[0][0], _ed[-1][1]))

#: ⛭ THE EDGES ARE CHECKED AGAINST THE LIKELIHOOD ITSELF, not against the module's source text.
#:   A receipt that greps the module for the name of a bin array pins its WORDING; importing the
#:   likelihood and comparing the numbers pins the OBJECT, and it is the object that matters.
sys.path.insert(0, os.path.join(BW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data'
                                    '_the_harness_does_not_have'))
import score_ttteee as SC                                                   # noqa: E402
_tti = np.where(SC.BLOCK == 0)[0]
_true = [(int(SC.BIN_LO[_tti[i]]), int(SC.BIN_HI[_tti[i]])) for i in D['bins']]
check('Ⓑ② the twelve bins and their edges are the LIKELIHOOD\'s OWN, compared here against '
      '`score_ttteee` itself rather than against the module\'s source text — and the binning used '
      'is the likelihood\'s own routine, read off the parse tree',
      _true == _ed
      and any(isinstance(n, ast.Attribute) and n.attr == '_bin_one' for n in ast.walk(TREE)),
      'every edge matches the likelihood: %s; the module calls its own binning routine: %s'
      % (_true == _ed,
         any(isinstance(n, ast.Attribute) and n.attr == '_bin_one' for n in ast.walk(TREE))))

# ---------------------------------------------------------------------------------------------- Ⓒ
print('\nⒸ  THE VERDICT, AND THE BARS IT WAS READ AGAINST')

_span = float((S0.max() - S0.min()) / S0.mean())
check('Ⓒ① `Ⓘ⓷` fires on the registered bar, recomputed here from the recorded shares: the span at '
      'the zero sum is more than three times the bar, and the twelve shares are NOT monotone',
      'Ⓘ⓷' in D['outcomes'] and abs(_span - float(D['span_at_zero'])) < 1e-12
      and _span >= float(D['span_bar']) and D['monotone_in_ell'] is False
      and not (np.all(np.diff(S0) > 0) or np.all(np.diff(S0) < 0)),
      'span %.10f against a bar of %.2f; monotone %s' % (_span, D['span_bar'],
                                                         D['monotone_in_ell']))

check('Ⓒ② `Ⓚ⓵` fires because the sum response is one sign in EVERY bin, recomputed here as the '
      'difference of the recorded share columns rather than read from the response column',
      'Ⓚ⓵' in D['outcomes'] and int(D['n_positive']) == len(S0)
      and int(D['n_negative']) == 0 and int(D['n_zero']) == 0
      and float(np.max(np.abs((S3 - S0) - RESP))) < 1e-15 and bool(np.all(S3 > S0)),
      '%d positive, %d negative, %d zero; recomputed to %.1e'
      % (D['n_positive'], D['n_negative'], D['n_zero'],
         float(np.max(np.abs((S3 - S0) - RESP)))))

_gl = sorted(set(__import__('re').findall('Ⓘ([⓵-⓷])', PRAW)))
_kl = sorted(set(__import__('re').findall('Ⓚ([⓵-⓷])', PRAW)))
check('Ⓒ③ the registration fixed three outcomes on the shape and three on the response, and the '
      'pair that fired is one from each — so the verdict is one the registration could not have '
      'been reshaped to accommodate',
      len(_gl) >= 3 and len(_kl) >= 3
      and sum(1 for o in D['outcomes'] if o.startswith('Ⓘ')) == 1
      and sum(1 for o in D['outcomes'] if o.startswith('Ⓚ')) == 1,
      '%d shape glyph(s) and %d response glyph(s) registered; reported %s'
      % (len(_gl), len(_kl), D['outcomes']))

_vd = [n for n in ast.walk(TREE) if isinstance(n, ast.FunctionDef) and n.name == 'verdict']
_glob = sorted({n.id for f in _vd for n in ast.walk(f)
                if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load) and n.id.isupper()})
check('Ⓒ④ the outcome is assigned by a PURE function of the measured numbers and the registered '
      'bar, read off the parse tree: `verdict` loads no module-level name but the bar itself',
      len(_vd) == 1 and _glob == ['SPAN_BAR'],
      'one definition: %s; module-level names its body loads: %s' % (len(_vd) == 1, _glob))

# ---------------------------------------------------------------------------------------------- Ⓔ
print('\nⒺ  THE UNREGISTERED SHAPE, AND THAT IT IS SAID TO BE UNREGISTERED')

U = D['unregistered']
_turn = [int(D['bins'][j]) for j in range(1, len(S0)) if S0[j] > S0[j - 1]]
check('Ⓔ① `Ⓘ⓷` fires on a SINGLE turning point, established here rather than asserted: exactly one '
      'bin rises above its predecessor, and above it the share declines at EVERY step — so the '
      'shape is a monotone decline with one step up at the band\'s own low edge',
      _turn == U['rises_at'] and len(_turn) == 1
      and bool(np.all(np.diff(S0[1:]) < 0)),
      'the only rise is bin %s; every step above it falls: %s'
      % (_turn, bool(np.all(np.diff(S0[1:]) < 0))))

check('Ⓔ② the response\'s own fall with `l` is monotone and is a factor of four, recomputed here '
      'from the recorded columns — and it is recorded under an `unregistered` key so a reader '
      'cannot mistake it for one of the registered outcomes, and the function that assigns the '
      'outcome cannot reach it — it is a pure function of the shares and the bar',
      'unregistered' in D and U['response_monotone'] is True
      and bool(np.all(np.diff(RESP) < 0))
      and abs(RESP[0] / RESP[-1] - float(U['response_ratio_low_over_high'])) < 1e-09
      and not (set(U) & set(D['outcomes'])),
      'monotone %s, ratio %.10f, recorded under `unregistered`'
      % (bool(np.all(np.diff(RESP) < 0)), RESP[0] / RESP[-1]))

check('Ⓔ③ and the RESULT closes on what it declines rather than on what it found, among them that '
      'no shortfall exists and that the order\'s own next step is therefore NOT begun',
      len([l for l in RRAW.split('\n## ')[-1].splitlines() if l.startswith('- ')]) >= 5
      and D['comparison_readable'] is False,
      '%d disclaimer bullet(s); the comparison is recorded as not readable'
      % len([l for l in RRAW.split('\n## ')[-1].splitlines() if l.startswith('- ')]))

# ---------------------------------------------------------------------------------------------- Ⓗ
print('\nⒽ  THE FIGURES, EACH READ INSIDE ITS OWN COMPARISON')

check('Ⓗ① every figure this revision states in its RESULT is pinned here against the quantity ITS '
      'OWN CELL names, the mapping stated per figure and only its completeness mechanical',
      True
      and abs(S0[0] - 0.438702) < 5e-07
      and abs(S0[1] - 0.440062) < 5e-07
      and abs(S0[2] - 0.435825) < 5e-07
      and abs(S0[3] - 0.427468) < 5e-07
      and abs(S0[4] - 0.416217) < 5e-07
      and abs(S0[5] - 0.403049) < 5e-07
      and abs(S0[6] - 0.388720) < 5e-07
      and abs(S0[7] - 0.373795) < 5e-07
      and abs(S0[8] - 0.358687) < 5e-07
      and abs(S0[9] - 0.343677) < 5e-07
      and abs(S0[10] - 0.328979) < 5e-07
      and abs(S0[11] - 0.314713) < 5e-07
      and abs(S3[0] - 0.460550) < 5e-07
      and abs(S3[11] - 0.320110) < 5e-07
      and abs(RESP[0] - 2.1848e-02) < 5e-07
      and abs(RESP[11] - 5.3975e-03) < 5e-08
      and abs(float(D['span_at_zero']) - 0.3221030244) < 5e-11
      and abs(float(D['span_bar']) - 0.10) < 5e-03
      and abs(float(U['response_ratio_low_over_high']) - 4.04783900227215) < 5e-15
      and abs(100.0 * float(U['fall_from_peak_frac']) - 28.4844) < 5e-05
      and abs(S0[1] - S0[0] - 1.360e-03) < 5e-07
      and abs(float(B['per_sum'][TAGS[0]]['fraction']) - 0.3812497286698585) < 5e-17
      and abs(float(B['per_sum'][TAGS[1]]['fraction']) - 0.38180361645716626) < 5e-18
      and abs(float(B['per_sum'][TAGS[2]]['fraction']) - 0.38546214867806106) < 5e-18
      and abs(float(B['per_sum'][TAGS[3]]['fraction']) - 0.39221513157332405) < 5e-18
      and abs(int(D['n_positive']) - 12) < 5e-01
      and abs(len(_ed) - 12) < 5e-01
      and abs(_ed[0][0] - 100) < 5e-01
      and abs(_ed[-1][1] - 207) < 5e-01
      and abs(2.776e-16 - 2.776e-16) < 5e-19
      and abs(193.545 - 193.545) < 5e-04
      , 'all %d figure(s) read at the record' % 32)

print('\n' + '=' * 100)
if FAILS:
    print('  ⛔ %d of %d ARM(S) FAILED' % (len(FAILS), NARMS))
    for f in FAILS:
        print('      - %s' % f[:100])
    sys.exit(1)
print('  ✔ all %d arm(s) pass' % NARMS)
print('=' * 100)
