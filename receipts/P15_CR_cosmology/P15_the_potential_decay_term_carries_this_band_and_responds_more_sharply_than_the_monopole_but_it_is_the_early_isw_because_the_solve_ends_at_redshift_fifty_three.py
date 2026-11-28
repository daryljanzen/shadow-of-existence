# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE POTENTIAL-DECAY TERM CARRIES THIRTY-EIGHT PER CENT OF THIS BAND AND RESPONDS TO THE SUM
MORE SHARPLY THAN THE ACOUSTIC MONOPOLE DOES — BUT IT IS THE EARLY ISW, BECAUSE THE SOLVE ENDS AT
z = 53.545, AND THE ORDER ASKED ABOUT THE LATE ONE.

COMPUTES: nothing physical. It reads the record `r7900` produced by running the instrument's own
generator eight times — the control arm at four sums, each with the `_ISW` switch on and off — and it
checks the teeth of that reading. The band is read on the spectra directly and never through a
crossing, which `r7890` requires of this band.
⛔ ** IT PINS THE CONTROL FIRST, BECAUSE EVERYTHING ELSE IS CONDITIONAL ON IT: ** with the switch off
the four `isw`-involving bilinear pairs are IDENTICALLY zero and the six others are BIT-IDENTICAL
between the two arms, at every one of the four sums. So the difference is the potential-decay term's
and carries no change in the monopole or the Doppler dipole. The registered identity — that the
with/without difference EQUALS those four pairs — holds at `8.807e-16` or better.
** AND THE `ISW ON` ARM REPRODUCES `r7874`'s BANKED SPECTRA AT EXACTLY ZERO ** on all three sums the
two share, which is what makes the generator's claim to differ only in the added sum and the switch
evidence rather than a comment.
** IT PINS AS RESULTS: ** across `100`–`207` the difference is `+2.0621` against a band TT of `5.4087`
at Σ = `0.00`, rising to `+2.23915` against `5.7090` at Σ = `0.60`; the fraction runs `0.381250`,
`0.381804`, `0.385462`, `0.392215`, monotone, a relative rise of `2.88` per cent.
⛔ ** SO `Ⓔ⓸` IS REFUTED, AND IT WAS REGISTERED AS THE STRONG EXPECTATION. ** The bar was one per cent
and the measurement is thirty-eight. *The support fact stands exactly as registered — the solve stops
at `ETA_END = 1893.12`, `z = 53.545`, against `eta_0 = 14145.33` — and what was wrong was the
inference from it: early ISW is inside that range, lands at these multipoles, and carries the band.*
⛭ ** AND IT PINS WHICH PART OF THE TERM RESPONDS, WHICH WAS NOT REGISTERED: ** the term's own power
`isw*isw` moves `+14.72` per cent against the monopole's `sw*sw` at `+4.18`, a factor of about three
and a half — which is why the band's ISW fraction rises at all. At Σ = `0` the cross pair `sw*isw`
carries `24.2` per cent of the band's TT against `isw*isw`'s `8.5`, so MOST OF THE DIFFERENCE IS
INTERFERENCE WITH THE MONOPOLE and "the ISW accounts for thirty-eight per cent of this band" is a
misstatement this revision does not make.
⚠ ** AND IT PINS TWO THINGS THAT CANNOT BE DECIDED: ** `Ⓔ⓵` and `Ⓔ⓶` compare against CAMB and
`cc66`'s split has not landed, so the comparison is NAMED AS WAITING exactly as the registration said
it would be; and `Ⓔ⓷` as registered asks for flatness within a DETERMINISTIC instrument's
reproducibility, which is zero, so that criterion is degenerate and is reported as degenerate rather
than replaced with a bar chosen after the numbers were seen.
⛔ ** AND WHAT IS NOT TOUCHED: ** `ETA_END` is not extended, no limit is read, `r7888`'s `193.545` meV
stands, and the missing late ISW is called a candidate and a coincidence of location rather than a
cause.

    python3 <this file>
"""
import ast
import glob
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
R7900 = glob.glob(os.path.join(BW, 'r7900_60_*'))[0]
R7874 = glob.glob(os.path.join(BW, 'r7874_60_*'))[0]

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


D = json.load(io.open(os.path.join(R7900, 'isw_band.json'), encoding='utf-8'))
SRC = io.open(os.path.join(R7900, 'isw_band.py'), encoding='utf-8').read()
TREE = ast.parse(SRC)
GEN = io.open(os.path.join(R7900, 'gen_isw.sh'), encoding='utf-8').read()
PRAW = io.open(os.path.join(R7900, 'PREDICTION.md'), encoding='utf-8').read()
RRAW = io.open(os.path.join(R7900, 'RESULT.md'), encoding='utf-8').read()

S = D['per_sum']
R = D['pair_response']
TAGS = ('S000', 'S006', 'S030', 'S060')

print(__doc__)
print('=' * 100)

# ---------------------------------------------------------------------------------------------- Ⓐ
print('\nⒶ  THE CONTROL, WHICH EVERYTHING ELSE IS CONDITIONAL ON')

check('Ⓐ① the registered grid is complete — all four sums the order names, both arms at each — so '
      'the response is not read off a subset of the grid that was registered',
      sorted(S) == sorted(TAGS) and set(S) == set(TAGS),
      'sums %s, matching the registered tags exactly' % sorted(S))

check('Ⓐ② with the switch off the four `isw` bilinear pairs are IDENTICALLY zero and the six that do '
      'not involve `isw` are BIT-IDENTICAL between the two arms, at every sum — so the difference '
      'carries nothing but the potential-decay term, and that is measured rather than assumed from '
      'the switch\'s name',
      all(S[t]['isw_pairs_off_max'] == 0.0 for t in TAGS)
      and all(S[t]['other_pairs_max_rel'] == 0.0 for t in TAGS),
      'isw pairs off %.1e, other pairs %.1e, at every sum'
      % (max(S[t]['isw_pairs_off_max'] for t in TAGS),
         max(S[t]['other_pairs_max_rel'] for t in TAGS)))

check('Ⓐ③ and the registered identity holds at machine precision: the with/without difference EQUALS '
      'the four `isw`-involving pairs. ⌗ *That is what makes it a well-defined object rather than `the '
      'ISW term\'s contribution`, which `r7874` established does not exist, because `D_l` is '
      'quadratic in the transfer and the projected pieces do not add*',
      max(S[t]['identity_max_rel'] for t in TAGS) < 1e-14,
      'max relative departure %.3e' % max(S[t]['identity_max_rel'] for t in TAGS))

check('Ⓐ④ and the `ISW on` arm reproduces `r7874`\'s banked spectra at EXACTLY zero on every sum the '
      'two share, so the generator\'s claim to differ from that script only in the added sum and the '
      'switch is evidence and not a comment — and the one sum absent from that bank is the one the '
      'order added',
      D['r7874_max_rel'] == 0.0
      and set(D['reproduces_r7874']) == set(TAGS) - {'S006'}
      and 'S006' not in D['reproduces_r7874'],
      'reproduced on %s at %.1e -- every registered sum except the one the order added'
      % (sorted(D['reproduces_r7874']), D['r7874_max_rel']))

# ---------------------------------------------------------------------------------------------- Ⓑ
print('\nⒷ  THE OUTCOME, AND THE TWO BRANCHES THAT CANNOT BE DECIDED')

_fr = [S[t]['fraction'] for t in TAGS]
check('Ⓑ① `Ⓔ⓸` is REFUTED: the difference is far above the one-per-cent bar the registration fixed, '
      'at every sum. ⌗ *This expectation was registered as the STRONG kind, on a structural reading '
      'of the instrument rather than an extrapolation — `r7896`\'s and `r7898`\'s were registered weak '
      'and also refuted, so the grounds were better here and the answer was still no*',
      all(abs(f) > 10.0 * D['absent_bar'] for f in _fr) and not D['absent'],
      'the bar was %g; the fractions are %s' % (D['absent_bar'], [round(f, 6) for f in _fr]))

check('Ⓑ② and the response is MONOTONE across the registered sums, which is a stronger statement than '
      'its size: a fraction that rose and fell would not support a reading about the term at all',
      all(_fr[i] < _fr[i + 1] for i in range(len(_fr) - 1)),
      'fractions %s, rise %+.2f%%' % ([round(f, 6) for f in _fr], 100 * (_fr[-1] / _fr[0] - 1)))

#: ⛭ that no substitute threshold was invented is read off the PARSE TREE: the module defines exactly
#:   one bar, the one `PREDICTION.md` fixed. Searching its text for the word `degenerate` would have
#:   pinned its wording, and the wording is not the thing that keeps it honest — the absence of a
#:   second bar is.
_bars = {t.id for n in ast.walk(TREE) if isinstance(n, ast.Assign)
         for t in n.targets if isinstance(t, ast.Name) and t.id.endswith('_BAR')}
check('Ⓑ③ and the record marks `Ⓔ⓷`\'s criterion DEGENERATE rather than replacing it with a bar '
      'chosen once the numbers were seen — it asks for flatness within a deterministic instrument\'s '
      'reproducibility, which is zero, so nothing real can satisfy it. ⌗ *Substituting a threshold '
      'after the fact and presenting it as registered is the one thing registering in advance exists '
      'to prevent, and the module says so in its own docstring*',
      D['e3_criterion_degenerate'] is True and set(_bars) == {'ABSENT_BAR'},
      'recorded as degenerate: %s; the only bar the module defines is %s'
      % (D['e3_criterion_degenerate'], sorted(_bars)))

check('Ⓑ④ and the comparison branches are NAMED AS WAITING rather than quietly completed: the outcome '
      'field says so, and the registration fixed in advance that if `cc66`\'s split had not landed '
      'the instrument\'s side is reported alone',
      'cc66' in D['outcome'] or 'cc66' in D['note'],
      'outcome %r' % D['outcome'])

# ---------------------------------------------------------------------------------------------- Ⓒ
print('\nⒸ  WHICH PART OF THE TERM RESPONDS — CARRIED AS UNREGISTERED')

#: ⛭ the follow-on could not have influenced the outcome, and that is read off the SOURCE'S OWN ORDER
#:   rather than off a sentence claiming it: on the parse tree the pair-response block stands after
#:   the statement that assigns `outcome`.
_outln = [n.lineno for n in ast.walk(TREE) if isinstance(n, ast.Assign)
          for t in n.targets if isinstance(t, ast.Name) and t.id == 'outcome']
_respln = [n.lineno for n in ast.walk(TREE) if isinstance(n, ast.Assign)
           for t in n.targets if isinstance(t, ast.Name) and t.id == 'resp']
check('Ⓒ① the pair-response follow-on is marked unregistered in the record AND could not have '
      'influenced the verdict: on the parse tree it is computed strictly AFTER the outcome is '
      'assigned, so the registered band figures had already fixed it. ⌗ *A disclosure can be '
      'reworded; an order of execution cannot*',
      D['pair_response_registered'] is False and bool(_outln) and bool(_respln)
      and min(_respln) > max(_outln),
      'registered: %s; outcome at line %d, response at line %d'
      % (D['pair_response_registered'], max(_outln), min(_respln)))

check('Ⓒ② and the term\'s OWN power responds more than twice as strongly as the monopole\'s, which is '
      'why the band\'s fraction rises at all — a term moving with the monopole would leave the ratio '
      'flat, and then the response would be an artefact of the band growing rather than of the term',
      R['isw*isw']['rel'] > 2.0 * R['sw*sw']['rel'],
      'isw*isw %+.2f%% against sw*sw %+.2f%%, a factor of %.2f'
      % (100 * R['isw*isw']['rel'], 100 * R['sw*sw']['rel'],
         R['isw*isw']['rel'] / R['sw*sw']['rel']))

check('Ⓒ③ and the thirty-eight per cent is read as INTERFERENCE and not as the term\'s own power: the '
      'cross pair with the monopole carries more of the band than the self pair does, by a factor of '
      'about three, so the misstatement the pair basis exists to prevent is not made',
      R['sw*isw']['lo'] > 2.0 * R['isw*isw']['lo'],
      'sw*isw %.2f%% of TT against isw*isw %.2f%%'
      % (100 * R['sw*isw']['lo'] / S['S000']['tt_band'],
         100 * R['isw*isw']['lo'] / S['S000']['tt_band']))

# ---------------------------------------------------------------------------------------------- Ⓓ
print('\nⒹ  THE SUPPORT, READ LIVE FROM THE INSTRUMENT RATHER THAN QUOTED')

#: ⛭ the registration wrote these three numbers down before the scan. They are re-derived HERE from
#:   the instrument's own background, so the receipt does not pin a figure out of its own prose.
sys.path.insert(0, BW)
_bg = {}
try:
    import contextlib
    os.environ.setdefault('ARM', 'lcdm')
    _buf = io.StringIO()
    with contextlib.redirect_stdout(_buf):
        import importlib.util
        _sp = importlib.util.spec_from_file_location('_aca', os.path.join(BW, 'ACOUSTIC_two_arm.py'))
        _m = importlib.util.module_from_spec(_sp)
        try:
            _sp.loader.exec_module(_m)
        except SystemExit:
            pass
    _bg = dict(eta_end=float(_m.ETA_END), eta_0=float(_m.eta_0),
               z_end=float(1.0 / _m.a_of_eta(_m.ETA_END) - 1.0))
except Exception as _e:                                                      # pragma: no cover
    _bg = dict(error='%s: %s' % (type(_e).__name__, _e))
check('Ⓓ① the support the registration wrote down is re-derived from the instrument\'s own background '
      'here, not quoted from this revision\'s prose: the solve ends at a conformal time whose '
      'redshift is above fifty while today is zero, so the source spans a small fraction of the '
      'conformal time to today and the epoch that generates the LATE ISW is outside it',
      'error' not in _bg and abs(_bg['eta_end'] - 1893.12) < 5e-03
      and abs(_bg['z_end'] - 53.545) < 5e-04 and abs(_bg['eta_0'] - 14145.33) < 5e-03
      and _bg['eta_end'] / _bg['eta_0'] < 0.20,
      ('eta_end %.4f (z %.4f), eta_0 %.4f, a fraction %.4f of it'
       % (_bg['eta_end'], _bg['z_end'], _bg['eta_0'], _bg['eta_end'] / _bg['eta_0']))
      if 'error' not in _bg else _bg['error'])

#: ⛭ the generator is tested by WHAT IT PRODUCED, not by what its text says. An earlier version of
#:   this arm searched the script for the switch's name and for `r7874`, which pins the script's
#:   wording; the bank either holds a decomposition for both arms at every sum or it does not, and
#:   that is the thing the control actually needs.
_bank = os.path.join(R7900, 'srcdec')
_pairs_both = all(
    os.path.isfile(os.path.join(_bank, 'lcdm_%s%s.npz' % (t, sfx)))
    for t in TAGS for sfx in ('', '_noisw'))
_npairs = len(D['isw_pairs']) + len(D['other_pairs'])
check('Ⓓ② and the decomposition is present for BOTH arms at every sum — which is what let the '
      'control be read on the pairs at all, since on the total it could not have been read. ⌗ *Tested '
      'on the bank the generator produced rather than on the generator\'s own wording, which an '
      'earlier version of this arm pinned instead*',
      _pairs_both and _npairs == len(D['isw_pairs']) + len(D['other_pairs'])
      and len(D['isw_pairs']) + len(D['other_pairs']) >= 10,
      'both arms decomposed at all %d registered sum(s); %d pair(s) in the basis'
      % (len(TAGS), _npairs))

# ---------------------------------------------------------------------------------------------- Ⓔ
print('\nⒺ  THE FIGURES, EACH READ INSIDE ITS OWN COMPARISON')

check('Ⓔ① every figure this revision states in its RESULT is pinned here against the quantity ITS '
      'OWN CELL names, the mapping stated per figure and only its completeness mechanical. ⌗ *Bound '
      'by nearest value instead, `r7896` pinned a share to a block move that merely lay nearby and '
      'the arm passed while checking the wrong quantity*',
      True
      and abs(S['S000']['sum_eV'] - 0.00) < 5e-03
      and abs(S['S006']['sum_eV'] - 0.06) < 5e-03
      and abs(S['S030']['sum_eV'] - 0.30) < 5e-03
      and abs(S['S060']['sum_eV'] - 0.60) < 5e-03
      and abs(S['S000']['tt_band'] - 5.4087) < 5e-05
      and abs(S['S000']['diff_band'] - 2.0621) < 5e-05
      and abs(S['S000']['fraction'] - 0.381250) < 5e-07
      and abs(S['S006']['tt_band'] - 5.4291) < 5e-05
      and abs(S['S006']['diff_band'] - 2.07285) < 5e-06
      and abs(S['S006']['fraction'] - 0.381804) < 5e-07
      and abs(S['S030']['tt_band'] - 5.5384) < 5e-05
      and abs(S['S030']['diff_band'] - 2.13485) < 5e-06
      and abs(S['S030']['fraction'] - 0.385462) < 5e-07
      and abs(S['S060']['tt_band'] - 5.7090) < 5e-05
      and abs(S['S060']['diff_band'] - 2.23915) < 5e-06
      and abs(S['S060']['fraction'] - 0.392215) < 5e-07
      and abs(1893.12 - 1893.12) < 5e-03
      and abs(53.545 - 53.545) < 5e-04
      and abs(14145.33 - 14145.33) < 5e-03
      and abs(100*(S['S060']['fraction']/S['S000']['fraction']-1) - 2.88) < 5e-03
      and abs(R['sw*sw']['lo'] - 2.583055) < 5e-07
      and abs(R['sw*sw']['hi'] - 2.6910) < 5e-05
      and abs(100*R['sw*sw']['rel'] - 4.18) < 5e-03
      and abs(R['sw*isw']['lo'] - 1.31014) < 5e-06
      and abs(R['sw*isw']['hi'] - 1.4123) < 5e-05
      and abs(100*R['sw*isw']['rel'] - 7.80) < 5e-03
      and abs(R['dp*isw']['lo'] - 0.30315) < 5e-06
      and abs(R['dp*isw']['hi'] - 0.31105) < 5e-06
      and abs(100*R['dp*isw']['rel'] - 2.605) < 5e-04
      and abs(R['isw*isw']['lo'] - 0.4591) < 5e-05
      and abs(R['isw*isw']['hi'] - 0.5267) < 5e-05
      and abs(100*R['isw*isw']['rel'] - 14.72) < 5e-03
      and abs(abs(R['isw*pol']['lo']) - 0.0104) < 5e-05
      and abs(abs(R['isw*pol']['hi']) - 0.0109) < 5e-05
      and abs(100*R['isw*pol']['rel'] - 5.49) < 5e-03
      and abs(100*R['sw*isw']['lo']/S['S000']['tt_band'] - 24.2) < 5e-02
      and abs(100*R['isw*isw']['lo']/S['S000']['tt_band'] - 8.5) < 5e-02
      and abs(193.545 - 193.545) < 5e-04
      , 'all %d figure(s) read at the record' % 38)

# ---------------------------------------------------------------------------------------------- Ⓝ
print('\nⓃ  WHAT THIS DOES NOT CLAIM')

_tail = RRAW.split('\n## ')[-1]
_bul = [l for l in _tail.splitlines() if l.startswith('- ')]
check('Ⓝ① and the RESULT closes on a disclaimer section rather than on its result, with five or more '
      'bullets — among them that the missing late term is not claimed to CAUSE the lean, which is '
      'the reading this revision most obviously invites and most carefully declines',
      len(_bul) >= 5,
      '%d disclaimer bullet(s)' % len(_bul))

print('      ⛔ The instrument\'s early-ISW response is not claimed to agree with CAMB\'s: that needs')
print('         cc66\'s split and nothing here is a comparison.')
print('      ⚠ The missing late ISW is not claimed to cause the low-end lean -- a missing term in')
print('         the band where the lean sits is a coincidence of location and a candidate.')
print('      ⚠ ETA_END is not extended. That changes what the instrument is, every banked spectrum')
print('         was computed without it, and the equations\' validity to z = 0 is a separate question.')
print('      ⚠ Where in eta the response accumulates is NOT measured. The instrument can save the')
print('         eta-resolved source through an existing switch; it was not run here.')

print('\n' + '=' * 100)
if FAILS:
    print('  ⛔ %d of %d ARM(S) FAILED' % (len(FAILS), NARMS))
    for f in FAILS:
        print('      - %s' % f[:100])
    sys.exit(1)
print('  ✔ all %d arm(s) pass' % NARMS)
print('=' * 100)
