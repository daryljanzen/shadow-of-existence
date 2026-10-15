#!/usr/bin/env python3
r"""S27 -- `r7283`'s order: `L233` and `L557` verdicted, the mode called first, and the call is WRONG.

COMPUTES: nothing the papers quote.  This receipt measures the corpus's own quote-pin ledger over
seven prefixes, and the instrument is the ledger itself.

** ⛭⛭ THE BURDEN FIRST: `31` LANDED, `501` REMAIN. **  *`532` before, `501` after -- `L233_colour_
curvature` `17` and `L557_the_correction_stopped_at_the_sentence` `14`, complete.*

** ⛔⛭⛭⛭ AND MY MODE CALL IS REFUTED, WHICH `r7283` SAID WOULD BE WORTH MORE THAN A BAND THAT HOLDS.
**  *I called `L233` LOW and `L557` HIGH before reading a key. `L233` came back `0.0` per cent
`REPAIR-OWED`, which is the call.  **`L557` came back `14.3` per cent, and I called it `50` or
above.***
  ⇒ *** So `the papers were rewritten under this prefix` does NOT predict the high mode. A correction
      prefix -- the shape chosen because it is the hypothesis's own best case -- is not in the high
      mode at all. ***

** ⛔⛭⛭⛭ AND IT LANDED IN THE GAP MY OWN `r7280` CLAIM SAYS IS EMPTY, WHICH IMPLICATES BOTH CLAIMS AT
ONCE. **  *`r7280` asserted bimodality as the ABSENCE of any prefix between `5` and `50` per cent.
`L557` is at `14.3`.*
  ⇒ *** THE BIMODALITY IS NOT A STRICT TWO-MODE STRUCTURE.  It is a skewed distribution with a heavy
      low cluster, a high cluster, and now an intermediate case -- and `r7280`'s gate stays green
      only because it reads its own pinned state, which is the discipline working and not the claim
      surviving. ***
  ⌈ ⛔ ** AND THE PRE-REGISTRATION CONTAINED TWO CLAIMS THAT CANNOT BOTH BE TESTED BY ONE
    MEASUREMENT. **  *I wrote `refuted if `L557` lands at or below `5` per cent` while also holding
    that nothing lands between `5` and `50`.  **If the gap is empty, that refutation threshold
    describes an outcome my other claim says is impossible** -- so it was an escape hatch, and the
    measurement landed exactly in it.*
  ⌊ ⇒ *The honest reading: the CALL was `HIGH`, the measurement is `14.3`, the call is WRONG, and the
    threshold I wrote does not get to rescue it.  **A pre-registration whose refutation condition
    contradicts its own model is not a pre-registration of anything.***

** ⛭⛭ AND `MEANING-HELD` IS HIGHEST ON A PHYSICS PREFIX AND JUST SHORT OF TWO THIRDS. **  *`L233`
is `64.7` per cent -- `11` of `17` -- above every other prefix read and below the two-thirds line of
`66.7` by two points.*
  ⌈ ⛔ *This gate's first form said `crossed two thirds` and asserted `> 66.0`: **the rhetoric outran
    the number inside one label**, caught by running it.  The claim is the RANKING and the DISTANCE,
    both measured.*
  ⌊ ⇒ *So `r7280`'s split verdict sharpens without being overturned: the FREQUENCY claim generalises
    to a third kind of prefix, and two thirds remains the first pair's alone.*

⌗ *Sources: `r7283`'s order; `PREDICTION.md`, pushed with the mode calls before any site was read; the
ledger's own rows across seven prefixes; and `r7280`'s own bimodality gate, which this revision
refutes from outside rather than from its own pinned state.*
"""

import collections
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7260_60_land_and_verdict'))

import dangling_predicate_v2 as D          # noqa: E402  the ADOPTED arms, byte-for-byte

CHECKS = []
FAILURES = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


BEFORE = '4b554493'     # this revision's pre-registration, with the mode calls, before any key
AFTER = '6594bf32'      # the commit that carried this revision's 31 verdicts
BASE = 'corpus/quote_pin_baseline.tsv'
L233, L557 = 'L233_colour_curvature', 'L557_the_correction_stopped_at_the_sentence'


def _git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True, text=True,
                          errors='replace').stdout


def read(rel):
    with io.open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        return fh.read()


def rows_of(text):
    return [c for c in (l.split('\t') for l in text.split('\n'))
            if len(c) >= 6 and c[0].startswith('receipts/')]


print()
print('=' * 100)
print("S27 -- r7283's order: L233 and L557, the mode called first and the call refuted")
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  BOTH ENDS PINNED, WHICH IS WHAT r7280 LEARNED THE HARD WAY ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_resb = subprocess.run(['git', 'cat-file', '-e', BEFORE + '^{commit}'], cwd=ROOT,
                       capture_output=True).returncode == 0
_resa = subprocess.run(['git', 'cat-file', '-e', AFTER + '^{commit}'], cwd=ROOT,
                       capture_output=True).returncode == 0
_anc = subprocess.run(['git', 'merge-base', '--is-ancestor', BEFORE, 'HEAD'], cwd=ROOT,
                      capture_output=True).returncode == 0
_bb, _ba = _git('show', f'{BEFORE}:{BASE}'), _git('show', f'{AFTER}:{BASE}')
gate(f'Ⓐ① ⛔⛭⛭ both ends are LITERAL SHAS that resolve (`{_resb}`, `{_resa}`), the BEFORE is an '
     f'ancestor of `HEAD` (`{_anc}`), and the ledger differs between them --- so every count below is '
     f'a fact about two commits and not about whenever this is run',
     _resb and _resa and _anc and bool(_bb) and bool(_ba) and _bb != _ba)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  THE BURDEN, AND THE ONE MONOTONE LIVE READ ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_rb, _ra, _rn = rows_of(_bb), rows_of(_ba), rows_of(read(BASE))
_unb = [r for r in _rb if r[5] == 'UNADJUDICATED']
_una = [r for r in _ra if r[5] == 'UNADJUDICATED']
_unn = [r for r in _rn if r[5] == 'UNADJUDICATED']
_mine = [r for r in _ra if len(r) > 6 and 'r7284+60' in r[6]]
print(f'      UNADJUDICATED at {BEFORE}: {len(_unb)};  at {AFTER}: {len(_una)};  live: {len(_unn)};  '
      f'rows this revision wrote: {len(_mine)}')
gate(f'Ⓑ① ⛭⛭ ** `{len(_mine)}` LANDED AND `{len(_una)}` REMAIN ** --- `{len(_unb)}` before, and the '
     f'only live read is the MONOTONE one: the backlog has not risen since',
     len(_mine) == 31 and len(_unb) - len(_una) == 31 and len(_unn) <= len(_una))


def share(rows, pref):
    sub = [r for r in rows if '/' + pref + '/' in r[0] and len(r) > 6 and 'r7284+60' in r[6]]
    c = collections.Counter(r[5] for r in sub)
    return len(sub), c


_n233, _c233 = share(_ra, L233)
_n557, _c557 = share(_ra, L557)
_ro233 = 100.0 * _c233.get('REPAIR-OWED', 0) / max(_n233, 1)
_ro557 = 100.0 * _c557.get('REPAIR-OWED', 0) / max(_n557, 1)
_mh233 = 100.0 * _c233.get('MEANING-HELD', 0) / max(_n233, 1)
_mh557 = 100.0 * _c557.get('MEANING-HELD', 0) / max(_n557, 1)
print(f'      {L233:46} {_n233:3} keys  REPAIR-OWED {_ro233:5.1f}%  MEANING-HELD {_mh233:5.1f}%')
print(f'      {L557:46} {_n557:3} keys  REPAIR-OWED {_ro557:5.1f}%  MEANING-HELD {_mh557:5.1f}%')
gate(f'Ⓑ② ⛭ the two prefixes are complete and counted SEPARATELY, as the order requires --- '
     f'`{_n233}` and `{_n557}` --- and no key of either is left unadjudicated at `{AFTER}`',
     _n233 == 17 and _n557 == 14
     and not [r for r in _una if ('/' + L233 + '/') in r[0] or ('/' + L557 + '/') in r[0]])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  THE MODE CALL, READ OUT OF THE PRE-REGISTRATION AND SCORED ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_PRED = _git('show', f'{BEFORE}:computations/beyond_the_wall/r7284_60_the_crossed_test/PREDICTION.md')
_called_low = bool(re.search(r'`L233_colour_curvature`[^|]*\|[^|]*\|\s*\*\*LOW\*\*', _PRED))
_called_high = bool(re.search(r'`L557_the_correction_stopped_at_the_sentence`[^|]*\|[^|]*\|\s*'
                             r'\*\*HIGH\*\*', _PRED))
print(f'      the pre-registration called L233 LOW: {_called_low};  L557 HIGH: {_called_high}')
gate(f'Ⓒ① ⛔⛭⛭⛭ the calls are READ OUT OF THE PUSHED PRE-REGISTRATION rather than restated here, and '
     f'`L233` LOW is RIGHT at `{_ro233:.1f}` per cent while ** `L557` HIGH is WRONG at '
     f'`{_ro557:.1f}` ** --- so `the papers were rewritten under this prefix` does not predict the '
     f'high mode, and the correction prefix chosen as the hypothesis\'s own best case is not in it',
     _called_low and _called_high and _ro233 <= 5.0 and _ro557 < 50.0)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓓ  AND IT LANDED IN THE GAP r7280 ASSERTED WAS EMPTY ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════


def pfx_share(rows, pref):
    sub = [r for r in rows if '/' + pref + '/' in r[0]]
    c = collections.Counter(r[5] for r in sub)
    vd = sum(n for k, n in c.items() if not k.startswith('UNADJUDICATED'))
    return vd, c.get('REPAIR-OWED', 0), c.get('MEANING-HELD', 0)


_SEVEN = ('L165_defining_the_sum', 'L175_dimensional_descent', 'L202_phase_at_the_seam',
          'L211_closure_adjacency', 'L221_quark_lepton', 'L233_colour_curvature',
          'L269_the_second_theatre', 'P12_algebroid', L557)
_tab = {}
for _p in _SEVEN:
    # ⌗ r7339+70 (ported, for 60 to confirm or replace): the table is this revision's claim, so it
    #   is read at AFTER -- live, a later repair stride moved L202 and L221 under it (r7335's rule).
    _vd, _ro, _mh = pfx_share(_ra, _p)
    if _vd:
        _tab[_p] = (_vd, 100.0 * _ro / _vd, 100.0 * _mh / _vd)
for _p, (_vd, _r, _m) in sorted(_tab.items(), key=lambda kv: -kv[1][1]):
    print(f'      {_p:46} verdicted {_vd:3}  REPAIR-OWED {_r:5.1f}%  MEANING-HELD {_m:5.1f}%')
_between = {_p: _v[1] for _p, _v in _tab.items() if 5.0 < _v[1] <= 50.0}
_between_txt = ', '.join(f"{_p.split('_')[0]} {_v:.1f}%"
                        for _p, _v in sorted(_between.items()))
gate(f'Ⓓ① ⛔⛭⛭⛭ `r7280` asserted bimodality AS THE ABSENCE of any prefix between `5` and `50` per '
     f'cent, and this revision puts one there: `{len(_between)}` prefix(es) now in that band '
     f'(`{_between_txt}`).  ** So the '
     f'structure is a SKEWED DISTRIBUTION with a heavy low cluster and a high one, not a strict two '
     f'modes ** --- and `r7280`\'s gate stays green only because it reads its own PINNED state, '
     f'which is the discipline working rather than the claim surviving',
     len(_between) >= 1 and L557 in _between)

gate(f'Ⓓ② ⛔⛭⛭ and the pre-registration carried TWO CLAIMS THAT ONE MEASUREMENT CANNOT BOTH TEST: '
     f'its refutation threshold for the call was `at or below 5 per cent` while `r7280`\'s model says '
     f'nothing lands between `5` and `50`.  ** So the threshold described an outcome the model calls '
     f'impossible -- an escape hatch -- and the measurement landed in it **, which is why the call is '
     f'scored WRONG above rather than unrefuted',
     '`5` per cent' in _PRED and _ro557 > 5.0 and _ro557 < 50.0)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓔ  THE BANDS, AND THE TWO-THIRDS FIGURE ON A PHYSICS PREFIX ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_ROWRE = re.compile(r'^\|\s*([^|]*?)\s*\|\s*\*\*`(\d+)`\*\*\s*\|\s*`(\d+)`–`(\d+)`\s*\|', re.M)
_bands = [(m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)))
          for m in _ROWRE.finditer(_PRED)]
_meas = [_c233.get('REPAIR-OWED', 0), _c233.get('MEANING-HELD', 0),
         _c557.get('REPAIR-OWED', 0), _c557.get('MEANING-HELD', 0), 0]
_broke = []
for _i, (_name, _c, _lo, _hi) in enumerate(_bands):
    _m = _meas[_i] if _i < len(_meas) else None
    _in = _m is not None and _lo <= _m <= _hi
    if not _in:
        _broke.append(_i)
    print(f'      {"✔" if _in else "⛔"} {_name[:56]:56} {_c} in {_lo}-{_hi}, measured {_m}'
          f'{"" if _in else "   BREAKS"}')
gate(f'Ⓔ① ⛭⛭ the `{len(_bands)}` bands are parsed from the pre-registration and `{len(_broke)}` '
     f'break --- ** and that is the cheap half: the bands held while the CALL they were built around '
     f'was wrong **, which is the order\'s own point that a named mode is worth more than a band',
     len(_bands) == 5 and _broke == [])

# ⛔ *This gate's first form said `crossed two thirds` and asserted `> 66.0`.  It is `64.7`, which is
#   BELOW two thirds by two points -- the rhetoric outran the number inside one label, which is the
#   class this line keeps finding and now in its own summary line.  The claim is the RANKING plus the
#   distance, both measured.*
gate(f'Ⓔ② ⛭⛭ and `MEANING-HELD` is HIGHEST on a PHYSICS prefix and JUST SHORT of two thirds: `L233` '
     f'at `{_mh233:.1f}` per cent against a two-thirds line of `66.7`, above every other prefix '
     f'read.  ** So `r7280`\'s split verdict sharpens without being overturned: the FREQUENCY claim '
     f'generalises to a third kind of prefix, and two thirds is still only the first pair\'s **',
     64.0 <= _mh233 < 66.7 and all(_tab[_p][2] <= _mh233 for _p in _tab))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓕ  THE RESTRAINT, AND THE DANGLING TEST ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_touched = sorted(set(f for f in _git('diff', '--name-only', f'{BEFORE}..{AFTER}').split('\n') if f))
_rcpt = [f for f in _touched if f.startswith('receipts/') and f.endswith('.py')]
print(f'      {BEFORE}..{AFTER} touched {len(_touched)} file(s), {len(_rcpt)} of them receipts')
gate(f'Ⓕ① ⛭ the restraint over this revision\'s OWN RANGE: the ledger and nothing else --- '
     f'`{len(_rcpt)}` receipt file(s) --- so a verdict is a row and not an edit to the gate it '
     f'describes, and neither verdicted prefix is touched',
     BASE in _touched and not [f for f in _rcpt if (L233 in f or L557 in f)])

_KEYS = ['CONTESTED', 'the geometry quantises and does not couple',
         'EXACT for arbitrary $m(r)$', 'the three carry one mass parameter']
_dangling = [_k for _k in _KEYS if D.dangles(_k)]
print(f'      {len(_KEYS)} literal(s) pinned here, {len(_dangling)} dangle')
gate(f'Ⓕ② ✔⛭ the literals this receipt pins run through the ADOPTED dangling arms and '
     f'`{len(_dangling)}` dangle', not _dangling)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
_fail = FAILURES
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(_fail)}')
for l in _fail:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛭⛭ ** {len(_mine)} LANDED, {len(_una)} REMAIN. **  L233 and L557, complete.
  ⛔ ** MY MODE CALL IS REFUTED: ** L233 LOW is right at {_ro233:.1f} per cent; L557 was called HIGH and
     came back {_ro557:.1f}.  So "the papers were rewritten under this prefix" does not predict the mode.
  ⛔ ** AND IT LANDED IN THE GAP r7280 SAID WAS EMPTY, ** so the bimodality is a skewed distribution
     with two clusters and an intermediate case -- and the pre-registration's own refutation
     threshold described an outcome its model calls impossible, which is an escape hatch, not a test.
  ⛭ ** MEANING-HELD IS HIGHEST ON A PHYSICS PREFIX AND JUST SHORT OF TWO THIRDS: ** L233 at {_mh233:.1f}
     per cent against a line of 66.7 -- the frequency claim generalises to a third kind of prefix,
     and two thirds remains the first pair's.  The first form of that gate said "crossed", and 64.7
     is not 66.7: the rhetoric outran the number inside one label, caught by running it.
""")
sys.exit(1 if _fail else 0)
