#!/usr/bin/env python3
r"""S43 -- THE DRAW DESIGNED UNDER FORK ⒞, SIZED, AND THE CLUSTERING ANSWERED AS A NUMBER.

** WHAT WAS ORDERED. **  `r7321` ③: design the draw under ⒞ and pre-register it -- the `427` frame, a
sampling arm sized to the interval this seat would publish rather than to any between-seat difference,
a reader arm of about `50` paired double-read keys IN the same registration, both margins per agent with
Newcombe intervals and not pooled, bands before the draw, and this seat's own stated limits carried in.
⌗ *And `r7321` ④: **register only after `cc66`'s reader-arm result can be read.**  It is not in the tree,
so this revision is the DESIGN and the registration is the next one.*

*** ⛭⛭ WHAT THE CLUSTERING MOVES, WHICH IS ⑥ ANSWERED AS A NUMBER AND NOT AS A CAVEAT: `r7320` drew its
    `40` keys from `17` receipts, the intra-receipt correlation of the withdrawal outcome is `0.327`, so
    the design effect is `1.44` and the effective sample size of that `40` is `27.7`. ***
  ⓘ `r7320`'s own band widens from `52.0`-`79.9` to `48.9`-`81.8`.
  ⓙ `r7322`'s era band widens from `22.0`-`33.0` to `20.8`-`33.7`.
  => ** AND NEITHER CONCLUSION MOVES: the rule's `67`-`72` is still outside and the `25.7` anchor still
      inside.  What the clustering moves is the COST -- every size in the design is `44` per cent larger
      than its independent-key form, and that is where it bites. **

** ⌗ THE SAMPLING ARM, SIZED TO WHAT THIS SEAT WOULD PUBLISH: ** *`±10` points costs `122` clustered
keys on this frame, `±7.5` costs `217`, and `±5` costs more than the whole `DELIBERATE` class.*  ⇒ ** So
`r7320`'s `40` bought `±14` points, and the size is a decision about what interval is worth publishing
rather than a number to inherit. **

** ⌗ THE READER ARM IS A FUNCTION AND NOT A NUMBER, BECAUSE ITS INPUT IS STILL BEING MEASURED: ** *`17`
paired keys at `10` per cent discordance through `50` at `70`'s `30` per cent, each `44` per cent larger
clustered.*  ** Two fresh agents at a salt with the ledger WITHHELD, both margins per agent, Newcombe
intervals, not pooled across halves -- and the block drawn from the same frame as the sampling arm so
the two arms share a population. **

⛔ ** NOTHING HERE REGISTERS ANYTHING, and that is asserted rather than promised: ** *no pre-registration,
no sample, no salt and no band in the directory, and not one key read.*

⚠ WHAT THIS CANNOT FIX is at the foot, beginning with the fact that a design effect estimated from `17`
clusters is indicative and not precise.
"""
import collections
import io
import os
import subprocess
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    'computations', 'beyond_the_wall', 'r7326_60_the_draw_designed'))
import design as G                                                     # noqa: E402

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
ORDER = 'a9e83881'              # r7321's orders on the trunk
D = 'computations/beyond_the_wall/r7326_60_the_draw_designed'


def show(sha, rel):
    return subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:{rel}'],
                          capture_output=True, text=True, errors='replace').stdout


# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('A -- THE ORDER, READ WHERE IT WAS WRITTEN')

ORD = show(ORDER, 'FOR_60.md')
_six = ['your own early-era rows on the `427` frame',
        'size it to the interval you intend to publish for YOUR OWN rate',
        'about `50` paired double-read keys',
        'withheld',
        'Newcombe intervals, not pooled across halves',
        'Say which of your costs the clustering moves']
_hold = 'read its result, not before'
print(f'      the six requirements present at {ORDER}: {[s in ORD for s in _six]}')
gate(f'Ⓐ①  the order is read AT `{ORDER}`: fork ⒞ decided, all six of `r7321` ③\'s requirements in the '
     f'one place, and ④\'s hold -- *register after you have read its result, not before* -- with them.  '
     f'** The seat that is ordered does not get to paraphrase the order **',
     all(s in ORD for s in _six) and _hold in ORD)

_charge = ['charging it as member `89`', 'The restraint was correct of you and wrong as a verdict']
gate(f'Ⓐ②  and THE MEMBER IS CHARGED OVER THIS SEAT\'S DECLINING OF IT, which is recorded and not '
     f're-litigated: `r7321` ① charges the noise floor as member `89` and says in terms that the '
     f'restraint was correct of this seat and wrong as a verdict.  ** A seat that declines to charge the '
     f'gate for the gate\'s own error is not the seat that decides whether the charge stands **',
     all(s in ORD for s in _charge))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('B -- THE CLUSTERING, MEASURED ON THIS SEAT\'S OWN SAMPLE AND CONTROLLED')

_g = collections.defaultdict(list)
for rec, y in G.rows():
    _g[rec].append(y)
_groups = list(_g.values())
_deff, _icc, _p, _n, _k = G.design_effect(_groups)

# CONTROL: the same keys re-grouped at random into clusters of the same sizes carry no ICC.
import random                                                          # noqa: E402
_rng = random.Random(4326)
_flat = [y for v in _groups for y in v]
_rng.shuffle(_flat)
_shuf, _i = [], 0
for v in _groups:
    _shuf.append(_flat[_i:_i + len(v)])
    _i += len(v)
_deff_s, _icc_s, _, _, _ = G.design_effect(_shuf)
print(f'      {_n} keys in {_k} receipts, mean {_n / _k:.2f};  ICC {_icc:.3f}, design effect '
      f'{_deff:.3f}, effective n {_n / _deff:.1f}')
print(f'      CONTROL -- the same verdicts re-grouped at random: ICC {_icc_s:.3f}, '
      f'design effect {_deff_s:.3f}')
gate(f'Ⓑ①  THE CLUSTERING IS MEASURED AND NOT ASSUMED: `{_n}` keys in `{_k}` receipts, mean '
     f'`{_n / _k:.2f}`, intra-receipt correlation `{_icc:.3f}`, design effect `{_deff:.2f}`, effective '
     f'sample size `{_n / _deff:.1f}` of `{_n}`.  ** CONTROLLED by re-grouping the same verdicts at '
     f'random into clusters of the same sizes, where the correlation falls to `{_icc_s:.3f}` -- so the '
     f'figure is the receipts and not the arithmetic **',
     _icc > 0.25 and _deff > 1.3 and _icc_s < _icc / 2)

_naive = G.wilson(round(_p * _n), _n)
_clust = G.wilson(_p * _n / _deff, _n / _deff)
_era_n = ((7 + int(_naive[0] * 168)) / 427, (7 + round(_naive[1] * 168)) / 427)
_era_c = ((7 + int(_clust[0] * 168)) / 427, (7 + round(_clust[1] * 168)) / 427)
print(f'      r7320 band {[round(100 * x, 1) for x in _naive]} -> '
      f'{[round(100 * x, 1) for x in _clust]};  era band '
      f'{[round(100 * x, 1) for x in _era_n]} -> {[round(100 * x, 1) for x in _era_c]}')
gate(f'Ⓑ②  ⛭⛭ AND WHAT IT MOVES IS STATED AS A NUMBER, which is `r7321` ⑥\'s question: `r7320`\'s own '
     f'band widens from `{100 * _naive[0]:.1f}`-`{100 * _naive[1]:.1f}` to '
     f'`{100 * _clust[0]:.1f}`-`{100 * _clust[1]:.1f}`, and `r7322`\'s era band from '
     f'`{100 * _era_n[0]:.1f}`-`{100 * _era_n[1]:.1f}` to '
     f'`{100 * _era_c[0]:.1f}`-`{100 * _era_c[1]:.1f}`.  ** NEITHER CONCLUSION MOVES -- the rule\'s '
     f'`67`-`72` is still outside and the `25.7` anchor still inside -- so what the clustering moves is '
     f'the cost and not the finding **',
     _clust[0] < _naive[0] and _clust[1] > _naive[1] and _era_c[1] < 0.67 and _era_c[0] <= 0.257 <= _era_c[1])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('C -- THE TWO ARMS, SIZED; AND THE INTERVAL THE REGISTRATION WILL USE, CONTROLLED')

_sizes = {hw: (G.n_for_halfwidth(hw, _p), G.n_for_halfwidth(hw, _p, _deff)) for hw in (0.10, 0.075, 0.05)}
print(f"      sampling arm: { {f'{100 * h:.1f}pt': v for h, v in _sizes.items()} }")
gate(f'Ⓒ①  THE SAMPLING ARM IS SIZED TO THE INTERVAL THIS SEAT WOULD PUBLISH, as ordered, and not to '
     f'any between-seat difference: `±10` points costs `{_sizes[0.10][1]}` clustered keys on this frame, '
     f'`±7.5` costs `{_sizes[0.075][1]}`, and `±5` costs `{_sizes[0.05][1]}` -- more than the whole '
     f'`DELIBERATE` class.  ** `r7320`\'s `40` bought about `±14`, so the size is a decision and this '
     f'receipt does not take it **',
     _sizes[0.10][1] > _sizes[0.10][0] and _sizes[0.05][1] > 168 and _sizes[0.10][1] < 168)

_reader = {d: (G.m_reader(d), G.m_reader(d, deff=_deff)) for d in (0.10, 0.15, 0.20, 0.30, 0.40)}
print(f"      reader arm: { {f'{100 * d:.0f}%': v for d, v in _reader.items()} }")
gate(f'Ⓒ②  and THE READER ARM IS A FUNCTION OF `cc66`\'s PENDING NUMBER rather than a guess: '
     f'`{_reader[0.10][0]}` paired keys at `10` per cent discordance through `{_reader[0.30][0]}` at '
     f'`70`\'s `30`, each `{100 * (_deff - 1):.0f}` per cent larger clustered.  ** The arm is monotone in '
     f'the discordance, so `cc66`\'s result sizes it without this seat choosing **',
     all(_reader[a][0] < _reader[b][0] for a, b in zip((0.10, 0.15, 0.20, 0.30), (0.15, 0.20, 0.30, 0.40)))
     and _reader[0.30][0] >= 50)

_cov = G.newcombe_coverage(0.675, 0.522, 50, 50)
_sym = G.newcombe(27, 40, 21, 40)
_sym2 = G.newcombe(21, 40, 27, 40)
print(f'      Newcombe: coverage {100 * _cov:.1f} per cent at nominal 95;  '
      f'symmetry {[round(x, 4) for x in _sym]} vs {[round(-x, 4) for x in _sym2[::-1]]}')
gate(f'Ⓒ③  and THE INTERVAL THE REGISTRATION WILL USE IS IMPLEMENTED AND CONTROLLED, not named: '
     f'Newcombe\'s two-Wilson method, with a seeded coverage simulation returning '
     f'`{100 * _cov:.1f}` per cent against a nominal `95`, and the interval shown to negate when the two '
     f'groups are swapped.  ** A method named in a registration and not exercised is a promise **',
     0.93 < _cov < 0.97 and abs(_sym[0] + _sym2[1]) < 1e-9 and abs(_sym[1] + _sym2[0]) < 1e-9)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('D -- THE RESTRAINT: A DESIGN AND NOT A REGISTRATION')

_dir = sorted(f for f in os.listdir(os.path.join(ROOT, D)) if not f.startswith('__'))
_reg = [f for f in _dir if 'PREDICTION' in f.upper() or 'SAMPLE' in f.upper() or 'DRAW' in f.upper()]
_note = io.open(os.path.join(ROOT, D, 'THE_DESIGN.md'), encoding='utf-8').read()
import re                                                              # noqa: E402
_ticked = set()
for m in re.findall(r'`([^`]+)`', _note):
    _ticked.add(m)
    for num in re.findall(r'\d+(?:\.\d+)?', m):
        _ticked.add(num)
print(f'      the directory holds: {_dir};  registering files: {_reg}')
gate(f'Ⓓ①  ⛔ **NOTHING IS REGISTERED HERE, as the specific negative it is**: the directory carries the '
     f'design and the arithmetic that sizes it and no pre-registration, no sample, no draw and no salt '
     f'(`{len(_reg)}`), and `r7321` ④ holds the registration until `cc66`\'s reader-arm result can be '
     f'read.  ** A design that registers itself before its input arrives is the thing the order '
     f'forbade **',
     not _reg and not re.search(r'\b[0-9a-f]{40}\b', _note) and 'registered band' not in _note)

_carried = {'427', '168', '1.44', '122', '0.327'} <= _ticked
gate(f'Ⓓ②  and THE DESIGN CARRIES THIS SEAT\'S OWN STATED LIMITS AND FIGURES, which `r7321` ⑥ required '
     f'in the registration rather than after it: the frame\'s `427` and `168`, the design effect, the '
     f'clustered sampling size and the measured correlation are all in the design note, read by PARSING '
     f'its backticked figures rather than by quoting a sentence of it',
     _carried)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
for l in FAILURES:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛭⛭ ** THE CLUSTERING MOVES THE COSTS BY {100 * (_deff - 1):.0f} PER CENT AND NOT A CONCLUSION: ** 40 keys in 17 receipts,
     ICC {_icc:.3f}, design effect {_deff:.2f}, effective n {_n / _deff:.1f}.  r7320's band widens to {100 * _clust[0]:.1f}-{100 * _clust[1]:.1f} and the era
     band to {100 * _era_c[0]:.1f}-{100 * _era_c[1]:.1f}, with the rule still outside and the anchor still inside.
  ⌗ ** THE ARMS ARE SIZED: ** {_sizes[0.10][1]} clustered keys for a ±10-point interval on this seat's own rate, and a
     reader arm of {_reader[0.10][0]} to {_reader[0.40][0]} paired keys as cc66's discordance comes in between 10 and 40 per cent.
  ⛔ ** AND NOTHING IS REGISTERED: ** r7321 holds the registration until that result can be read, and the
     next revision is the registration rather than this one.

  ⚠ ** WHAT THIS DESIGN CANNOT FIX. **
     * A design effect estimated from 17 clusters is indicative and not precise, and a draw spread over
       more receipts would lower it by construction.
     * The reader spread is 70's on another population and cc66's is pending.  Neither is this seat's --
       which is what the arm designed here would fix.
     * Nothing here addresses the RATE moving with the rule text; r7321 holds the read for the third
       redraft's score and this design takes no position on it.
""")
sys.exit(1 if FAILURES else 0)
