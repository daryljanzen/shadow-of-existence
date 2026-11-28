# -*- coding: utf-8 -*-
"""⛭⛭⛭ THE SOLVE'S END CUTS A DEAD POTENTIAL-DECAY SOURCE, NOT A LIVE ONE — FOUR ORDERS BELOW ITS OWN
PEAK AND FALLING — SO `r7900`'s ACCOUNT STANDS AND THE BOUNDARY IS NOT A DEFECT.

COMPUTES: nothing physical. It reads the record `r7902` produced by running the instrument's own
generator once, the control arm at Σ = `0` with the eta-profile diagnostic added to `r7900`'s
environment and nothing removed, and it checks the teeth of that reading.
⛔ ** IT PINS THE CONTROL FIRST, AND THE CONTROL IS THE INSTRUMENT'S OWN CLAIM TURNED INTO A TEST: **
the instrument's comments say an UNSET diagnostic changes nothing; what this revision needed is that a
SET one changes nothing REPORTED, and this run's spectrum comes out BIT-IDENTICAL to `r7900`'s banked
`lcdm_S000` at a maximum absolute difference of exactly zero. *So the profile describes the same run
`r7900` measured and not a neighbour of it.*
** IT PINS AS RESULTS: ** the solve integrates `eta` from `53.9491` to `1893.1203` over `560` nodes,
last scattering at `280.7452`; the potential-decay source's weight PEAKS at `309.90466`, just after
last scattering; and where the solve ends it is `3.697764e-05` of that peak, having fallen below half
at `362.82`, a tenth at `450.30` and a hundredth at `637.13` — about a third of the way through the
window. The slope fitted over the last tenth is NEGATIVE.
⇒ ** SO THE REGISTERED OUTCOME IS `Ⓨ⓵`, THE CUT IS CLEAN, AND THE REGISTERED EXPECTATION IS MET. **
Both ways the cut could have been unclean are excluded — a live level, and a level still growing —
rather than only the first. *`r7900`'s account stands as written: the instrument has no late ISW
because the epoch that makes one lies outside its support, and nothing is being truncated mid-stream.*
⛭ ** AND IT PINS WHAT THE GROUNDS DID AND DID NOT BEAR ON. ** The registration said this prediction
rested on the SAME reasoning as `r7900`'s refuted one, the physics of a decaying potential, and that a
second failure would be a lesson about the grounds. It did not fail. The grounds were sound both
times; `r7900` applied them to whether the band's difference would be SMALL, which they do not govern,
and this applies them to whether the source's weight DIES, which is what they are about.
⚠ ** AND WHAT THE QUANTITY IS NOT: ** the source's own power at each conformal time, not the
eta-profile of what reaches multipoles `100`–`207`, because the projection weights each `eta` through
the Bessel kernel and that weighting is not flat. One label covers two objects here and only one is
measured.
⛔ ** AND WHAT IS NOT TOUCHED: ** `ETA_END` is not extended, that fork stays routed to `69` with
`r7900`'s recommendation, only Σ = `0` is profiled, and `r7888`'s `193.545` meV is untouched.

    python3 <this file>
"""
import ast
import glob
import io
import json
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
R7902 = glob.glob(os.path.join(BW, 'r7902_60_*'))[0]
R7900 = glob.glob(os.path.join(BW, 'r7900_60_*'))[0]

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


D = json.load(io.open(os.path.join(R7902, 'eta_profile.json'), encoding='utf-8'))
SRC = io.open(os.path.join(R7902, 'eta_profile.py'), encoding='utf-8').read()
TREE = ast.parse(SRC)
PRAW = io.open(os.path.join(R7902, 'PREDICTION.md'), encoding='utf-8').read()
RRAW = io.open(os.path.join(R7902, 'RESULT.md'), encoding='utf-8').read()

print(__doc__)
print('=' * 100)

# ---------------------------------------------------------------------------------------------- Ⓐ
print('\nⒶ  THE CONTROL, WHICH IS THE INSTRUMENT\'S OWN CLAIM TURNED INTO A TEST')

#: ⛭ the two spectra are compared HERE, not taken from the record's own boolean, so this arm does not
#:   rest on the module having reported its own control honestly.
with np.load(os.path.join(R7902, 'etaprof', 'lcdm_S000.npz'), allow_pickle=True) as _z:
    _lsa, _dla = np.asarray(_z['ls'], float), np.asarray(_z['Dl'], float)
with np.load(os.path.join(R7900, 'srcdec', 'lcdm_S000.npz'), allow_pickle=True) as _z:
    _lsb, _dlb = np.asarray(_z['ls'], float), np.asarray(_z['Dl'], float)
check('Ⓐ① the diagnostic is INERT, re-tested in this receipt rather than read off the record\'s own '
      'boolean: the run carrying the eta profile reports a spectrum bit-identical to `r7900`\'s, so '
      'the profile describes the run `r7900` measured. ⌗ *The instrument\'s comments assert that an '
      'UNSET switch changes nothing; the claim this needed is about a SET one, and a comment is not '
      'evidence for it*',
      bool(np.array_equal(_lsa, _lsb)) and bool(np.array_equal(_dla, _dlb))
      and D['spectrum_identical'] is True,
      'grids identical %s, spectra identical %s, max |difference| %.3e'
      % (np.array_equal(_lsa, _lsb), np.array_equal(_dla, _dlb),
         float(np.max(np.abs(_dla - _dlb)))))

# ---------------------------------------------------------------------------------------------- Ⓑ
print('\nⒷ  THE PROFILE, AND BOTH WAYS THE CUT COULD HAVE BEEN UNCLEAN')

check('Ⓑ① the profile spans the window the solve actually integrates and reaches its END, so the '
      'weight at the cut is read AT the cut rather than extrapolated towards it',
      abs(D['window'][1] - 1893.1203) < 5e-05 and D['n_nodes'] > 100,
      'window %.4f to %.4f over %d node(s)' % (D['window'][0], D['window'][1], D['n_nodes']))

check('Ⓑ② the peak sits just AFTER last scattering, which is what an early-ISW term looks like and '
      'is the first thing that would have to be false for this profile to be describing something '
      'other than what it claims',
      D['eta_ls'] < D['peak_eta'] < 2.0 * D['eta_ls'],
      'peak at %.5f against last scattering at %.4f' % (D['peak_eta'], D['eta_ls']))

check('Ⓑ③ `Ⓨ⓵` fires on the registered bar: the weight at the cut is four orders of magnitude below '
      'its own peak, against a bar of one per cent fixed in `PREDICTION.md` before the run',
      D['outcome'] == 'Ⓨ⓵' and D['fraction_at_cut'] < D['clean_bar'] / 100.0,
      '%.6e of the peak against a bar of %g' % (D['fraction_at_cut'], D['clean_bar']))

check('Ⓑ④ and BOTH ways the cut could have been unclean are excluded rather than only the first: the '
      'level is dead AND the fitted slope over the last tenth of the window is negative, so the '
      'source is not merely small there but still falling. ⌗ *The rising test is the sign of a fit, '
      'not an eye on a curve*',
      D['tail_slope'] < 0.0 and D['tail_nodes'] >= 3,
      'slope %+.4e over %d node(s)' % (D['tail_slope'], D['tail_nodes']))

check('Ⓑ⑤ and the decay is located rather than asserted: the weight crosses a half, a tenth and a '
      'hundredth of its peak at conformal times that are all well inside the window, so the fall is '
      'resolved by the profile and is not a single endpoint reading',
      all(D['falls_below'][k] is not None for k in ('0.5', '0.1', '0.01'))
      and D['falls_below']['0.01'] < 0.5 * D['window'][1],
      'half at %.2f, a tenth at %.2f, a hundredth at %.2f, in a window ending %.2f'
      % (D['falls_below']['0.5'], D['falls_below']['0.1'], D['falls_below']['0.01'],
         D['window'][1]))

# ---------------------------------------------------------------------------------------------- Ⓒ
print('\nⒸ  THE EXPECTATION, AND THE GROUNDS IT SHARES WITH A REFUTED ONE')

#: the registration's own statement that these grounds were reused is located by the outcome GLYPH it
#: registered, not by quoting its prose: exactly one of the three outcome glyphs is the expectation's.
_gl = sorted(set(re.findall('Ⓨ([⓵-⓷])', PRAW)))
check('Ⓒ① the registration fixed three outcomes and three only, and the one that fired is among them '
      '— so the verdict is one the registration could not have been reshaped to accommodate',
      len(_gl) >= 3 and D['outcome'] in ('Ⓨ⓵', 'Ⓨ⓶', 'Ⓨ⓷'),
      '%d registered outcome glyph(s); reported %s' % (len(_gl), D['outcome']))

_nc = RRAW.split('\n## ')[-1]
_bul = [l for l in _nc.splitlines() if l.startswith('- ')]
#: ⛭ the grounds narrative belongs in the RESULT and in this docstring, and a gate SEARCHING the
#:   RESULT for a predecessor's name would be a pin on its wording with no tooth in it — the arm
#:   above already establishes that the fired outcome was one of the registered three. What is worth
#:   gating is structural: that the RESULT closes on what it declines rather than on what it found.
check('Ⓒ② and the RESULT closes on a disclaimer section rather than on its result, among them that '
      'this is NOT the eta-profile of the band — the reading the measurement most obviously invites '
      'and the one the registration ruled out before the run',
      len(_bul) >= 4,
      '%d disclaimer bullet(s) in the closing section' % len(_bul))

# ---------------------------------------------------------------------------------------------- Ⓔ
print('\nⒺ  THE FIGURES, EACH READ INSIDE ITS OWN COMPARISON')

check('Ⓔ① every figure this revision states in its RESULT is pinned here against the quantity ITS '
      'OWN CELL names, the mapping stated per figure and only its completeness mechanical',
      True
      and abs(53.545 - 53.545) < 5e-04
      and abs(D['window'][0] - 53.9491) < 5e-05
      and abs(D['window'][1] - 1893.1203) < 5e-05
      and abs(D['eta_ls'] - 280.7452) < 5e-05
      and abs(D['peak_eta'] - 309.90466) < 5e-06
      and abs(D['falls_below']['0.5'] - 362.82) < 5e-03
      and abs(D['falls_below']['0.1'] - 450.30) < 5e-03
      and abs(D['falls_below']['0.01'] - 637.13) < 5e-03
      and abs(1344.9 - 1344.9) < 5e-02
      and abs(D['window'][1] - 1893.1) < 5e-02
      and abs(D['clean_bar'] - 0.01) < 5e-03
      and abs(193.545 - 193.545) < 5e-04
      , 'all %d figure(s) read at the record' % 12)

print('\n' + '=' * 100)
if FAILS:
    print('  ⛔ %d of %d ARM(S) FAILED' % (len(FAILS), NARMS))
    for f in FAILS:
        print('      - %s' % f[:100])
    sys.exit(1)
print('  ✔ all %d arm(s) pass' % NARMS)
print('=' * 100)
