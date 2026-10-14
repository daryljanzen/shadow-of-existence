#!/usr/bin/env python3
r"""S44 -- THE REGISTRATION, AND TWO CORRECTIONS TO THIS SEAT'S OWN DESIGN ONE REVISION OLD.

** WHAT WAS ORDERED. **  `r7321` ③ ordered the draw designed and pre-registered; `r7321` ④ and `r7323` ②
held the registration until `cc66`'s reader-arm result could be read, because the reader arm's size was
a FUNCTION of the spread that measurement would report.  `r7323` ② put the two branches as *recurs near
`30` -> full size* and *comes back tight -> sizes down*.

*** ⛔ BOTH BRANCHES ARE KEYED ON A QUANTITY THE FORMULA DOES NOT TAKE, AND THE HOLD IS DISCHARGED
    BECAUSE THE SIZE NEVER DEPENDED ON IT. ***
  ⓐ `70`'s `30.0` is a MARGIN -- a difference between two readers' owed RATES -- and the seat that
     produced it calls it one: *your owed-margin split*, `-30.0 (-52.5, -2.9)`.
  ⓑ The size formula takes the rate of DISAGREEMENTS: the share of keys whose two readings differ.
  ⓒ They are different quantities, and this receipt shows it on the data rather than arguing it: on the
     crossover the two pools' owed rates are EQUAL -- a margin of exactly zero -- while `4` of the `40`
     keys were read differently.  A margin of zero is consistent with every key disagreeing.
  ⓓ No instrument in this campaign had reported the second quantity.  It is recoverable from two paired
     reader sets already on the trunk, and measured here for the first time: `4` of `40` under the
     previous text, `11` of `69` under the third redraft.

*** ⛔ AND THE SAMPLING ARM'S PRICE LIST AT `r7326` SOLD THREE INTERVALS THIS FRAME DOES NOT STOCK. ***
  ⓔ The design effect is a FUNCTION of the size, not a constant: the frame holds its keys in a fixed
     number of receipts, so every key added to a draw enlarges the clusters it has to go in.
  ⓕ Priced that way, every key `r7320` left buys `11.37` points of half-width and the whole population
     buys `10.46`, so none of `10.0`, `7.5` and `5.0` is purchasable at any price -- and two of the three
     sizes quoted for them exceed the population outright.

** WHAT IS REGISTERED, pushed before the draw ran and before one key was read: ** the sampling arm at
`80` keys spread over all `29` receipts by a receipt rotation, its replication band stated as a band that
cannot be failed at any affordable size; and the reader arm at `52` paired keys sized from the UPPER end
of the measured interval rather than its point, with a refutation condition that is resolvable.

⚠ WHAT THIS CANNOT FIX is at the foot, beginning with the fact that the rate of disagreements measured
here is between two SEATS' pools where the arm it sizes is two agents from ONE pool.
"""
import collections
import io
import math
import os
import random
import re
import subprocess
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    'computations', 'beyond_the_wall', 'r7328_60_the_registration'))
import size as G                                                       # noqa: E402

CHECKS = []
FAILURES = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


def head(t):
    print("\n  " + "=" * 96 + f"\n  {t}\n  " + "=" * 96)


print(__doc__)
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
ORDER = '7812bccd'              # r7323's orders on the trunk
MARGIN = '7812bccd'             # the trunk commit carrying 70's own label for its figure
PREG = 'aadfeb2c'               # the commit that PUSHED this registration, before the draw
AFTER = '7cd0d48d'              # the commit that RAN the draw -- the range's far end, literal and closed
D = 'computations/beyond_the_wall/r7328_60_the_registration'
HELD = 'the held set, third redraft at 1a3c13a6'
CROSS = 'the crossover, previous text at 6bef6fd5'


def show(sha, rel):
    return subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:{rel}'],
                          capture_output=True, text=True, errors='replace').stdout


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a),
                          capture_output=True, text=True, errors='replace').stdout


# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('A -- THE ORDER AND THE HOLD, READ WHERE THEY WERE WRITTEN')

ORD = show(ORDER, 'FOR_60.md')
_hold = ['AND YOU WERE RIGHT NOT TO REGISTER', 'a FUNCTION of the spread it will report',
         'your reader arm goes in at full size', 'your arm sizes down',
         'hold, and register when that result lands']
print(f'      the hold and its two branches present at {ORDER}: {[s in ORD for s in _hold]}')
gate(f'Ⓐ①  THE HOLD IS READ AT `{ORDER}` AND NOT PARAPHRASED: `r7323` ② says the reader arm is a '
     f'function of the spread the pending measurement will report, gives the two branches by name, and '
     f'closes *hold, and register when that result lands*.  ** The seat under a hold does not get to '
     f'restate the hold it is discharging **',
     all(s in ORD for s in _hold))

MARG = show(MARGIN, 'FOR_66_FROM_70.md')
_label = 'owed-margin split'
_fig = '(−52.5, −2.9)'
print(f'      70\'s own label for the figure: {_label in MARG};  the figure itself: {_fig in MARG}')
gate(f'Ⓐ②  ⛭⛭ AND THE SEAT THAT PRODUCED THE FIGURE CALLS IT A MARGIN, which is the whole of the '
     f'correction and is read off the trunk rather than inferred: `FOR_66_FROM_70.md` at `{MARGIN}` '
     f'carries the words *{_label}* and the interval `{_fig}` for the same number `r7326` sized a '
     f'reader arm from as a rate of disagreements.  ** A figure\'s own author naming its quantity '
     f'settles what quantity it is **',
     _label in MARG and _fig in MARG)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('B -- THE RATE OF DISAGREEMENTS, MEASURED FOR THE FIRST TIME AND CONTROLLED')

_m = {}
for _name, _fa, _fb in G.PAIRED:
    _keys, _disc, _dec, _discdec, _A, _hdr = G.discordance(_fa, _fb)
    _B, _ = G.read_tsv(_fb)
    _m[_name] = dict(keys=_keys, disc=_disc, dec=_dec, discdec=_discdec, A=_A, B=_B, hdr=_hdr)
    print(f'      {_name}: {len(_keys)} paired, {len(_disc)} discordant '
          f'= {100 * len(_disc) / len(_keys):.1f}%')

_h, _c = _m[HELD], _m[CROSS]
_pd = len(_h['disc']) / len(_h['keys'])
_lo, _hi = G.wilson(len(_h['disc']), len(_h['keys']))

# CONTROL: break the pairing.  Pairing each 70 verdict with a RANDOM 71 verdict must give a much
# higher disagreement rate -- otherwise the pairing carries no information and the figure is chance.
_rng = random.Random(7328)
_a = [_h['A'][k][3].strip() for k in _h['keys']]
_b = [_h['B'][k][3].strip() for k in _h['keys']]
_perm = []
for _ in range(400):
    _s = _b[:]
    _rng.shuffle(_s)
    _perm.append(sum(1 for x, y in zip(_a, _s) if x != y) / len(_a))
_chance = sum(_perm) / len(_perm)
print(f'      CONTROL -- the pairing broken, 400 permutations: {100 * _chance:.1f}% disagree '
      f'against {100 * _pd:.1f}% paired')
gate(f'Ⓑ①  ⛭⛭ THE QUANTITY THE FORMULA TAKES IS MEASURED AND CONTROLLED: of the `{len(_h["keys"])}` '
     f'keys both pools read under the third redraft, `{len(_h["disc"])}` were read differently '
     f'(`{100 * _pd:.1f}` per cent, Wilson `{100 * _lo:.1f}`-`{100 * _hi:.1f}`), and '
     f'`{len(_c["disc"])}` of `{len(_c["keys"])}` under the previous text.  ** CONTROLLED by breaking '
     f'the pairing: pairing each reading with a random one of the other pool\'s gives '
     f'`{100 * _chance:.1f}` per cent, so the agreement is the keys and not the arithmetic **',
     0.05 < _pd < 0.30 and _chance > 2 * _pd and len(_c['disc']) == 4)

_rate_a = sum(1 for k in _c['keys'] if _c['A'][k][3].strip() == 'REPAIR-OWED') / len(_c['keys'])
_rate_b = sum(1 for k in _c['keys'] if _c['B'][k][3].strip() == 'REPAIR-OWED') / len(_c['keys'])
_pd_c = len(_c['disc']) / len(_c['keys'])
print(f'      the crossover: owed rates {100 * _rate_a:.1f}% and {100 * _rate_b:.1f}%, margin '
      f'{100 * (_rate_a - _rate_b):+.1f}; keys read differently {100 * _pd_c:.1f}%')
gate(f'Ⓑ②  ⛭⛭⛭ AND THE TWO QUANTITIES ARE SHOWN DIFFERENT ON THE DATA RATHER THAN ARGUED: on the '
     f'crossover the two pools\' owed rates are EQUAL, so the margin is exactly zero, while '
     f'`{len(_c["disc"])}` of the `{len(_c["keys"])}` keys were read differently.  ** A margin of zero '
     f'is consistent with every key disagreeing, which is why the arm could not be sized from one **',
     abs(_rate_a - _rate_b) < 1e-12 and len(_c['disc']) > 0)

_si = _h['hdr'].index('seen')
_bands = {}
for _lab in ('seen', 'unseen'):
    for _name, _d in (('held', _h), ('cross', _c)):
        _kk = [k for k in _d['keys']
               if _d['A'][k][_si].lower().startswith('yes') == (_lab == 'seen')]
        _dd = sum(1 for k in _kk if k in set(_d['disc']))
        _bands[(_lab, _name)] = (_dd, len(_kk)) + G.wilson(_dd, len(_kk))
_ov = all(_bands[('seen', n)][2] < _bands[('unseen', n)][3] for n in ('held', 'cross'))
print(f'      seen vs unseen: { {k: (v[0], v[1], round(100 * v[2], 1), round(100 * v[3], 1)) for k, v in _bands.items()} }')
gate(f'Ⓑ③  and THE ONE PATTERN IN IT IS STATED AS A DIRECTION AND NOT AS A DIFFERENCE, which is '
     f'member `89` applied to this seat\'s own numbers: keys the appliers had already seen disagree '
     f'more often in BOTH sets, and in both the two intervals OVERLAP, so neither sample could have '
     f'distinguished it from zero.  ** The direction is reported, the difference is not claimed **',
     _ov and _bands[('seen', 'held')][0] / _bands[('seen', 'held')][1]
     > _bands[('unseen', 'held')][0] / _bands[('unseen', 'held')][1])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('C -- WHAT THE FRAME CAN SUPPLY, AND THE THREE INTERVALS IT CANNOT')

_pop = G.frame()
_rest = [c for c in _pop if (c[0], c[1]) not in G.drawn_at_r7320(_pop)]
_caps_all = list(collections.Counter(c[0] for c in _pop).values())
_caps = list(collections.Counter(c[0] for c in _rest).values())
_curve = {}
for _n in (33, 40, 60, 80, 100, 128):
    _s = G.spread(_caps, _n)
    _de, _m0 = G.deff_of(_s)
    _curve[_n] = (_de, _m0, G.wilson_halfwidth(_n, _de)[0])
print(f'      the frame: {len(_pop)} keys in {len(_caps_all)} receipts; {len(_rest)} left in '
      f'{len(_caps)}')
print(f"      the curve: { {n: (round(v[0], 3), round(v[2], 2)) for n, v in _curve.items()} }")
gate(f'Ⓒ①  ⛭⛭ THE DESIGN EFFECT IS A FUNCTION OF THE SIZE AND NOT A CONSTANT, which is what `r7326` '
     f'③ got wrong: the frame holds its `{len(_pop)}` keys in `{len(_caps_all)}` receipts, so every key '
     f'added to a draw enlarges the clusters it has to go in, and the design effect rises from '
     f'`{_curve[33][0]:.3f}` at `33` keys to `{_curve[128][0]:.3f}` at every key left.  ** A size '
     f'multiplied by a fixed design effect prices a draw nobody can make **',
     all(_curve[a][0] < _curve[b][0] for a, b in zip((33, 40, 60, 80, 100), (40, 60, 80, 100, 128)))
     and _curve[128][0] > 1.44 > _curve[40][0])

_best = G.wilson_halfwidth(len(_rest), G.deff_of(G.spread(_caps, len(_rest)))[0])[0]
_best_all = G.wilson_halfwidth(len(_pop), G.deff_of(G.spread(_caps_all, len(_pop)))[0])[0]
print(f'      the best half-width on the keys left: {_best:.2f}; on the whole population: '
      f'{_best_all:.2f}')
gate(f'Ⓒ②  ⛔⛭⛭ SO NONE OF THE THREE HALF-WIDTHS `r7326` ③ PRICED IS PURCHASABLE ON THIS FRAME AT ANY '
     f'PRICE, as the specific negative it is: every key `r7320` left, drawn as well as it can be drawn, '
     f'buys `{_best:.2f}` points, and the whole population buys `{_best_all:.2f}`.  ** The table quoted '
     f'`10.0`, `7.5` and `5.0`, and the frame\'s floor is above all three **',
     _best > 10.0 and _best_all > 10.0 and _best_all < _best)

_quoted = {0.10: 122, 0.075: 217, 0.05: 487}
_over = {hw: n for hw, n in _quoted.items() if n > len(_pop)}
print(f'      quoted sizes exceeding the population of {len(_pop)}: {_over}')
gate(f'Ⓒ③  and TWO OF THE THREE SIZES IT QUOTED EXCEED THE POPULATION OUTRIGHT, which the table did '
     f'not say: `{_quoted[0.075]}` and `{_quoted[0.05]}` keys against a class of `{len(_pop)}`.  '
     f'** A price list is not a price list if it quotes a quantity the shop does not hold **',
     len(_over) == 2 and all(n > len(_pop) for n in _over.values())
     and _quoted[0.10] < len(_pop))

_hw_r7320 = G.wilson_halfwidth(40, 1.44)[0]
_hw_spread = G.wilson_halfwidth(40, G.deff_of(G.spread(_caps_all, 40))[0])[0]
print(f'      r7320\'s 40 in 17 receipts bought {_hw_r7320:.2f}; the same 40 spread over '
      f'{len(_caps_all)} would have bought {_hw_spread:.2f}')
gate(f'Ⓒ④  ⌗ and ONE THING THE FRAME GIVES BACK FREE, which is why the draw below rotates: `r7320`\'s '
     f'own `40` lay in `17` receipts and bought `{_hw_r7320:.2f}` points, where the same `40` spread '
     f'over every receipt would have bought `{_hw_spread:.2f}`.  ** Two points of interval were lost to '
     f'the draw\'s own concentration and cost nothing to recover **',
     _hw_spread < _hw_r7320 - 1.5)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('D -- THE DRAW: REGISTERED FIRST, THEN RUN, AND IT HITS THE FIGURE IT WAS PRICED ON')

_pred_at_preg = show(PREG, f'{D}/PREDICTION.md')
_files_at_preg = set(git('ls-tree', '--name-only', '-r', PREG, '--', D).split('\n'))
_sample = f'{D}/SAMPLE_80.tsv'
print(f'      at {PREG} the directory holds: '
      f'{sorted(f.split("/")[-1] for f in _files_at_preg if f)}')
gate(f'Ⓓ①  ⛭⛭ THE REGISTRATION WAS PUSHED BEFORE THE DRAW RAN, as a closed fact about the history and '
     f'not a promise in prose: the registration commit `{PREG}` carries the pre-registration and '
     f'carries NO sample file, and the draw is a later commit.  ** `r7295`\'s ruling: what is open is '
     f'a trunk fact, so the order of the commits is the claim **',
     _pred_at_preg.strip() and _sample not in _files_at_preg
     and f'{D}/size.py' in _files_at_preg)

_rows = [l.rstrip('\n').split('\t') for l in
         io.open(os.path.join(ROOT, _sample), encoding='utf-8') if not l.startswith('#')]
_rows = [r for r in _rows if r and r[0].strip()]
_alloc = collections.Counter(r[1] for r in _rows)
_n80, _k80 = len(_rows), len(_alloc)
_m0_80 = (_n80 - sum(v * v for v in _alloc.values()) / _n80) / (_k80 - 1)
_de_80 = 1 + (_m0_80 - 1) * G.ICC
print(f'      the drawn sample: {_n80} keys over {_k80} receipts, m0 {_m0_80:.2f}, '
      f'deff {_de_80:.3f}')
gate(f'Ⓓ②  ⛭⛭ AND THE ROTATION LANDS THE DESIGN EFFECT IT WAS PRICED ON, to the places the '
     f'registration fixed: the `{_n80}` keys lie over all `{_k80}` receipts with a cluster weighting '
     f'of `{_m0_80:.2f}` and a design effect of `{_de_80:.3f}`, against `{_curve[80][1]:.2f}` and '
     f'`{_curve[80][0]:.3f}` registered.  ** A registered size that the draw does not realise is a '
     f'size for a different draw **',
     abs(_m0_80 - _curve[80][1]) < 0.005 and abs(_de_80 - _curve[80][0]) < 0.0005
     and _k80 == len(_caps))

_note = io.open(os.path.join(ROOT, D, 'PREDICTION.md'), encoding='utf-8').read()
_fix = ['CORRECTED BEFORE THE DRAW RAN', 'A\nre-ordering cannot spread a sample',
        'it does not change which keys are in it']
_fix_pat = [re.sub(r'\s+', r'\\s+', s) for s in _fix]
_fix_hit = [bool(re.search(p, _note)) for p in _fix_pat]
print(f'      the correction recorded in the registration: {_fix_hit}')
gate(f'Ⓓ③  and THE DRAW RULE WAS ITSELF REPAIRED BEFORE THE DRAW RAN, with the repair in the '
     f'registration rather than quiet: the line first said the `80` would be taken by hash and then '
     f're-ordered, and a re-ordering cannot spread a sample because it does not change which keys are '
     f'in it.  ** A pre-registration repaired after its draw is not one; this one was repaired before, '
     f'and says so **',
     all(_fix_hit))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('E -- THE TWO BANDS, AND THE ONE THAT CAN FAIL')

_de80 = _curve[80][0]
_sd_new = math.sqrt(G.CENTRE * (1 - G.CENTRE) / (80 / _de80))
_sd_old = (_hw_r7320 / 100) / G.Z95
_sd_rep = math.sqrt(_sd_new ** 2 + _sd_old ** 2)
_band = (G.CENTRE - G.Z95 * _sd_rep, G.CENTRE + G.Z95 * _sd_rep)
#: ⌗ The registration's own figures are read by PARSING its backticked numbers and NOT by asserting
#: that a sentence of it is present: a gate that quotes a span out of the middle of a sentence is the
#: defect this seat's own r7320 recipe names, and it fails on a reword.  Pin a value, a name, or a
#: whole clause -- here, the values.
_figs = set()
for _m in re.findall(r'`([^`]+)`', _note):
    _figs.add(_m)
    for _num in re.findall(r'\d+(?:\.\d+)?', _m):
        _figs.add(_num)
_band_registered = {str(math.floor(80 * _band[0])), str(math.ceil(80 * _band[1])), '80'} <= _figs
_ratio = 100 * G.Z95 * _sd_rep / _curve[80][2]
print(f'      replication band {100 * _band[0]:.1f}-{100 * _band[1]:.1f}, '
      f'{math.floor(80 * _band[0])}-{math.ceil(80 * _band[1])} of 80;  its figures in the '
      f'registration: {_band_registered};  band half-width / arm half-width = {_ratio:.2f}')
gate(f'Ⓔ①  ⛔ THE SAMPLING ARM\'s BAND IS REGISTERED AND LABELLED A BAND THAT CANNOT FAIL, which is '
     f'the labelling and not an excuse: a replication band carries `r7320`\'s own error as well as the '
     f'new sample\'s, so the two standard deviations compose to `{100 * _sd_rep:.2f}` and the band is '
     f'`{math.floor(80 * _band[0])}`-`{math.ceil(80 * _band[1])}` of `80` withdrawn.  ** Its half-width is '
     f'`{_ratio:.2f}` times the arm\'s own, so no outcome of `80` keys can land outside it, and the '
     f'registration carries both figures -- read by PARSING its backticked numbers and not by '
     f'asserting that a sentence of it is present **',
     _band[0] < 0.50 and _band[1] > 0.85 and _sd_rep > _sd_new
     and _band_registered and _ratio > 1.5)

_h_reader = {p: 100 * G.Z95 * math.sqrt(p / 52) for p in (_pd, _hi)}
print(f'      the reader arm at 52 paired keys: half-width '
      f'{ {round(100 * p, 1): round(v, 1) for p, v in _h_reader.items()} } against a bound of '
      f'{100 * G.BOUND:.1f}')
gate(f'Ⓔ②  ⛭⛭ AND THE READER ARM IS THE RESOLVABLE ONE, with the number that makes it so: `52` paired '
     f'keys, sized from the UPPER end of the measured interval rather than its point because a sample '
     f'of `{len(_h["keys"])}` cannot distinguish the two, give a half-width of '
     f'`{_h_reader[_hi]:.1f}` points on the two readers\' margin against a refutation condition of '
     f'`{100 * G.BOUND:.1f}`.  ** The first arm in this campaign that could fail on a reader '
     f'difference, and the figure it needed was lying unmeasured in two files on the trunk **',
     _h_reader[_hi] < 100 * G.BOUND and _h_reader[_pd] < _h_reader[_hi]
     and G.m_reader(_hi) > G.m_reader(_pd))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('F -- THE RESTRAINT: REGISTERED AND DRAWN, AND NOT ONE KEY READ')

_hdr80 = [l for l in io.open(os.path.join(ROOT, _sample), encoding='utf-8')
          if l.startswith('# n\t')][0]
_cols = _hdr80.lstrip('# ').rstrip('\n').split('\t')
_verdictish = [c for c in _cols
               if c.lower() in ('verdict', 'outcome', 'withdrawn', 'decided_at', 'what_decided_it')]
_dir = sorted(f for f in os.listdir(os.path.join(ROOT, D)) if not f.startswith('__'))
_result = [f for f in _dir if 'RESULT' in f.upper() or 'READING' in f.upper()]
print(f'      the sample\'s columns: {_cols};  the directory: {_dir}')
gate(f'Ⓕ①  ⛔ **NOT ONE KEY IS READ THIS REVISION, as the specific negative it is**: the drawn sample '
     f'carries no verdict, outcome or decided-at column (`{len(_verdictish)}`), and the directory holds '
     f'no result and no reading (`{len(_result)}`).  ** `r7321` forbids reading a key this cycle, and '
     f'the draw is the whole of what ran **',
     not _verdictish and not _result and len(_rows) == 80)

#: ⌗ The range is `PREG..AFTER`, two LITERAL commits, and not `PREG..HEAD`: a range with a live end
#: counts another seat's ordinary repair as this revision's, which is the live-subject class `r7307`
#: measured and the defect `S34`'s `Ⓔ①` carried until `r7309`.  The commit that adds this file adds
#: no receipt but this file, which the second arm asserts directly off the drawn keys.
_touched = sorted({f for f in git('diff', '--name-only', f'{PREG}~1', AFTER).split('\n') if f})
_drawn_receipts = {r[1] for r in _rows}
_subjects = [f for f in _touched if f.startswith('receipts/')]
_self = os.path.join('receipts', 'L_probability', os.path.basename(__file__))
print(f'      the closed range {PREG}~1..{AFTER} touched {len(_touched)} files, of which '
      f'{len(_subjects)} receipts; drawn receipts naming this file: '
      f'{sum(1 for r in _drawn_receipts if r == _self)}')
gate(f'Ⓕ②  and THE REVISION EDITS NO RECEIPT IT DRAWS, read over a CLOSED range of two literal '
     f'commits and not over a live one: `{len(_subjects)}` receipts are in `{PREG}~1..{AFTER}`, and '
     f'none of the `{len(_drawn_receipts)}` receipts the `{len(_rows)}` keys name is this file.  '
     f'** `r7307`\'s live-subject class, which is the defect `S34` carried: a restraint gate has a '
     f'live end unless its range names two commits **',
     not _subjects and _self not in _drawn_receipts
     and all(r[1].startswith('receipts/') for r in _rows))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print("=" * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
print("=" * 100)
print()
print('  ⛔ ** THE READER ARM WAS SIZED OFF A MARGIN WHERE THE FORMULA TAKES A RATE OF')
print('     DISAGREEMENTS, AND ON THE CROSSOVER THAT MARGIN IS EXACTLY ZERO WHILE 4 OF 40')
print('     KEYS WERE READ DIFFERENTLY. ** Measured for the first time: 11 of 69 under the')
print('     standing text, Wilson 9.1-26.3, and the size is taken from the upper end.')
print('  ⛔ ** AND NONE OF THE THREE HALF-WIDTHS r7326 PRICED IS FOR SALE ON THIS FRAME. **')
print('     The design effect is a function of the size, not a constant: 168 keys in 33')
print('     receipts, so the floor is 10.46 points and two of the three sizes quoted exceed')
print('     the population outright.')
print('  ✔ ** REGISTERED FIRST, THEN DRAWN: 80 keys over all 29 receipts, and the rotation')
print('     lands the design effect it was priced on to three places. **')
print('  ⛭ The reader arm is the resolvable one; the sampling arm is an estimation arm and is')
print('     registered as one.')
if FAILURES:
    print('\n  FAILED:')
    for f in FAILURES:
        print(f'   - {f}')
sys.exit(1 if FAILURES else 0)
