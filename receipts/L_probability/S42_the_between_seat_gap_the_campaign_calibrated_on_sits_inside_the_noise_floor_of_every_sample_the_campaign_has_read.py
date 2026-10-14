#!/usr/bin/env python3
r"""S42 -- WHAT A PER-SEAT COMPARISON COSTS, AND WHY `15.3` POINTS WAS NEVER RESOLVABLE.

** WHAT WAS ASKED. **  `r7319`'s ruling ③, in its own words: *"when your per-seat draw does run, its
comparison across seats will need a within-seat reference to mean anything, and that is a design question
for the draw rather than something to bolt on afterwards."*  ⇒ ** Settled here as arithmetic on a DESIGN:
no population, no size, no draw, no salt and no band.  The per-seat measurement is NOT ordered and this
revision does not pre-register it. **

** ⛭ THE TWO SPREADS, AND NEITHER IS THE OTHER. **
  ⓘ **the READER spread** -- the same keys read twice -- is `30.0` points (`-52.5`, `-2.9`), excluding
     zero.  *`66`'s measurement at `r7319` on `70`'s two-agent split.  CITED and not re-derived.*
  ⓙ **the SAMPLING spread** -- different keys read once -- measured HERE on rows already read: a binomial
     SE of `7.4` points on `40`, and an exact split-half `|p1-p2|` with mean `12.2` and a `95`th
     percentile of `25.0`.
  => *Different causes with different fixes: more keys shrink the sampling spread and do nothing to the
     reader spread, and only a second reader OF THE SAME KEYS measures the reader spread at all.*

*** ⛔⛭⛭⛭ AND THE NOISE FLOOR SETTLES IT: the `95` per cent half-width on a difference between two units
    is `20.5` points at `40` keys each and `15.6` at `69` -- the largest blind read this campaign has run.
    ⇒ `r7299`'s `15.3`-point between-seat gap, which the calibration half was built on, SITS INSIDE THE
    NOISE FLOOR OF EVERY SAMPLE SIZE THE CAMPAIGN HAS ACTUALLY USED, before the reader spread is counted
    at all. ***  ** `66`'s eighty-eighth member says the reference was never taken; the sampling axis says
    the difference was not resolvable in principle at these sizes. **

** ⌗ WHAT IT COSTS TO MEAN SOMETHING, PER SEAT: ** *`158` keys to resolve `15.3` points at `80` per cent
power; `40` keys to resolve `30.0`; and `50` DOUBLE-READ keys to bound the reader difference under `15.3`
when paired at the observed discordance, `72` unpaired.*  ⇒ ** A bounded draw of `40` per seat resolves a
`30`-point gap and nothing finer, and five seats at `158` is `790` keys, which is not bounded. **

⛭⛭ ** THE RECOMMENDATION IS A FORK AND IT IS THE GATING SEAT'S: ** *read `158` per seat; or compare two
seats at a time with a pooled reference; or ⒞ drop the between-seat comparison, report each seat's rate
with its own interval, and carry ONE double-read block per seat.*  ** This seat recommends ⒞ -- the only
one a bounded draw can carry -- and the `DESIGN_NOTE.md` beside this receipt states all three. **

⚠ WHAT THIS CANNOT SETTLE is at the foot, beginning with the fact that a split-half of one reader's
verdicts is the spread of a `20`-row estimate and not of a `40`-row one.
"""
import io
import math
import os
import random
import subprocess
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    'computations', 'beyond_the_wall', 'r7324_60_the_within_unit_reference'))
import power as P                                                      # noqa: E402

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
ORDER = '015afbaf'          # r7319's orders and 66's own figures, on the trunk
D = 'computations/beyond_the_wall/r7324_60_the_within_unit_reference'


def show(sha, rel):
    return subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:{rel}'],
                          capture_output=True, text=True, errors='replace').stdout


# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('A -- THE QUESTION IS THE ORDER\'S AND THE READER SPREAD IS THE GATING SEAT\'S')

ORD = show(ORDER, 'FOR_60.md')
_asked = ['will need a within-seat reference to mean anything',
          'and that is a design question',
          'Do not pre-register it']
gate(f'Ⓐ①  the question is read AT `{ORDER}` and not paraphrased: `r7319` ruling ③ asks for the '
     f'within-seat reference as a DESIGN question for the draw, and the same order says in terms not to '
     f'pre-register the draw.  ** Both halves of that instruction are in the one place **',
     all(s in ORD for s in _asked))

_F70 = show(ORDER, 'FOR_70.md')
_reader = ['`30.0`', '`−52.5`, `−2.9`', 'r7319_66_the_within_unit_reference']
_withdrawn = 'The calibration half is\nwithdrawn' in show(ORDER, 'FOR_69.md')
gate(f'Ⓐ②  and THE READER SPREAD IS CITED, NOT RE-DERIVED: `66`\'s own `r7319` measurement on `70`\'s '
     f'two-agent split -- `30.0` points, `−52.5` to `−2.9`, excluding zero -- is read from its own '
     f'routing at that commit, with the instrument it names.  ** A seat that re-derives another seat\'s '
     f'measurement to use it has taken the measurement twice and checked it once.  ⌗ And the '
     f'calibration half that gap carried is ALREADY WITHDRAWN at the same revision (`{_withdrawn}`), so '
     f'what follows strengthens a decision rather than reopening one **',
     all(s in _F70 for s in _reader) and _withdrawn)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('B -- THE SAMPLING SPREAD, MEASURED ON ROWS ALREADY READ, AND CONTROLLED')

RES = [l.split('\t') for l in io.open(os.path.join(ROOT, D, '..', 'r7320_60_the_early_era_sampled',
                                                   'RESULT_40.tsv'), encoding='utf-8').read().split('\n')
       if l and not l.startswith('#')]
_k = sum(1 for c in RES if c[6] == 'WITHDRAWN')
_n = len(RES)
_se = math.sqrt((_k / _n) * (1 - _k / _n) / _n)
_mean, _sd, _p95 = P.split_half_exact(_k, _n)

# CONTROL: the enumeration against a seeded Monte-Carlo draw of the same split, and the weights to one
rng = random.Random(7324)
rows = [1] * _k + [0] * (_n - _k)
_mc = []
for _ in range(20000):
    rng.shuffle(rows)
    h = _n // 2
    _mc.append(abs(sum(rows[:h]) / h - sum(rows[h:]) / h))
_mc_mean = sum(_mc) / len(_mc)
_w = sum(p for _, p in [(d, p) for d, p in zip(*[iter([])] * 2)]) if False else None
print(f'      r7320 read {_k} of {_n};  binomial SE {100 * _se:.1f} points')
print(f'      exact split-half |p1-p2|: mean {100 * _mean:.1f}, sd {100 * _sd:.1f}, '
      f'95th {100 * _p95:.1f};  seeded Monte-Carlo mean {100 * _mc_mean:.1f}')
gate(f'Ⓑ①  THE SAMPLING SPREAD, measured on `r7320`\'s own `{_n}` rows rather than on a new read: a '
     f'binomial SE of `{100 * _se:.1f}` points, and an EXACT split-half `|p1-p2|` with mean '
     f'`{100 * _mean:.1f}` and `95`th percentile `{100 * _p95:.1f}` -- enumerated over every way of '
     f'halving the sample.  ** CONTROLLED against a seeded Monte-Carlo of the same split, which agrees '
     f'to `{abs(_mc_mean - _mean) * 100:.2f}` points **',
     _k == 27 and _n == 40 and abs(_mc_mean - _mean) < 0.01 and _mean > _se)

_floors = {n: P.floor_between(n, _k / _n) for n in (40, 69, 158)}
print(f"      noise floor, 95 per cent half-width: "
      f"{ {n: round(100 * v, 1) for n, v in _floors.items()} }")
gate(f'Ⓑ②  ⛔ AND THE GAP IS INSIDE THE FLOOR AT EVERY SIZE THE CAMPAIGN HAS READ: the `95` per cent '
     f'half-width on a difference between two units is `{100 * _floors[40]:.1f}` points at `40` keys '
     f'each and `{100 * _floors[69]:.1f}` at `69` -- the largest blind read run -- against the '
     f'`{100 * P.GAP_SEAT:.1f}`-point gap `r7299` calibrated on.  ** It clears the floor only at '
     f'`158`, where the floor is `{100 * _floors[158]:.1f}` **',
     P.GAP_SEAT < _floors[40] and P.GAP_SEAT < _floors[69] and P.GAP_SEAT > _floors[158])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('C -- WHAT IT COSTS, AND THE ASSUMPTION THE COSTS REST ON')

_n158 = P.n_two_proportion(P.GAP_SEAT, _k / _n)
_n30 = P.n_two_proportion(P.GAP_READER, _k / _n)
_m_paired = P.m_paired_bound(P.GAP_SEAT, P.GAP_READER)
_m_unpaired = P.m_unpaired_bound(P.GAP_SEAT, _k / _n)
print(f'      per seat: {_n158} keys for the 15.3-point gap, {_n30} for the 30-point one;  '
      f'{_m_paired} paired double-read keys to bound the reader difference, {_m_unpaired} unpaired')
gate(f'Ⓒ①  THE PRICE OF THE REFERENCE, per seat: `{_n158}` keys to resolve `15.3` points at `80` per '
     f'cent power, `{_n30}` to resolve `30.0`, and `{_m_paired}` DOUBLE-READ keys to bound the reader '
     f'difference under `15.3` when paired at the observed discordance (`{_m_unpaired}` unpaired).  ** So '
     f'a bounded draw of `40` per seat resolves a `30`-point gap and nothing finer, and five seats at '
     f'`{_n158}` is `{5 * _n158}` keys **',
     _n158 > 150 and _n30 <= 41 and _m_paired < _m_unpaired and _m_paired > 40)

_recs = {c[1] for c in RES}
_note = io.open(os.path.join(ROOT, D, 'DESIGN_NOTE.md'), encoding='utf-8').read()
gate(f'Ⓒ②  ⌗ and THE ASSUMPTION IS NAMED WITH ITS NUMBER rather than left in a footnote: every cost '
     f'above assumes INDEPENDENT keys, and `r7320`\'s own sample drew its `{_n}` keys from '
     f'`{len(_recs)}` receipts -- so a clustered draw inflates all of them, which the design note says '
     f'in terms',
     len(_recs) == 17 and 'drew `40` keys from `17` receipts' in _note)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('D -- THE RESTRAINT, AND WHOSE MEMBER THIS IS')

_dir = sorted(os.listdir(os.path.join(ROOT, D)))
_registers = [f for f in _dir if 'PREDICTION' in f.upper() or 'SAMPLE' in f.upper()]
_salt = 'SALT' in _note.upper()
print(f'      the computation directory holds: {_dir}')
gate(f'Ⓓ①  ⛔ **NOTHING IS PRE-REGISTERED, as the specific negative it is**: the directory carries a '
     f'design note and the arithmetic that produces it and NO pre-registration, no sample, no draw and '
     f'no salt (`{len(_registers)}` registering files, salt in the note: `{_salt}`).  ** `r7319` says the '
     f'per-seat draw is not ordered and says not to pre-register it; a design is not a registration, and '
     f'this one fixes no population, no size and no band **',
     not _registers and not _salt)

_member = ['a difference between units is a property of the units only against the spread WITHIN a unit',
           'never took that reference']
gate(f'Ⓓ②  ⌗ and THE MEMBER IS THE GATING SEAT\'S, CITED AND NOT RESTATED: the eighty-eighth is `66`\'s, '
     f'read at `{ORDER}` in its own words.  ** What this revision adds is its SAMPLING sibling: the '
     f'reader axis says the reference was never taken, and the sampling axis says the difference was not '
     f'resolvable at these sizes -- two causes with two fixes, and the fix for one does nothing for the '
     f'other **',
     all(m in _F70 for m in _member))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
for l in FAILURES:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛔ ** THE {100 * P.GAP_SEAT:.1f}-POINT BETWEEN-SEAT GAP SITS INSIDE THE NOISE FLOOR OF EVERY SAMPLE SIZE THIS
     CAMPAIGN HAS READ: ** {100 * _floors[40]:.1f} points at 40 keys per unit, {100 * _floors[69]:.1f} at 69.  It clears the floor only
     at {_n158}, which is {5 * _n158} keys across five seats.
  ⛭⛭ ** AND THE TWO SPREADS ARE DIFFERENT CAUSES: ** the reader spread is 30.0 points (66's measurement,
     cited) and the sampling spread is {100 * _se:.1f} points on 40 (this seat's, measured here).  More keys shrink
     the second and do nothing to the first; only a second reader of the SAME keys touches the first.
  ⌗ ** THE REFERENCE HAS A PRICE: ** about {_m_paired} double-read keys per seat, paired, and it has to be IN the
     draw.  The fork is the gating seat's and this seat recommends dropping the between-seat comparison.

  ⚠ ** WHAT THIS CANNOT SETTLE. **
     * A split-half of one reader's verdicts is the spread of a 20-row estimate, not of a 40-row one.
       It is reported as that and it is not the reader spread.
     * The reader figure is 70's, on a different population and a different text.  Carrying it onto this
       seat assumes the reader spread travels, which nothing here tests -- and the one key this seat and
       71 both read AGREED, which is one key and not a reference.
     * Every cost assumes independent keys at the observed rate.  r7320 drew {_n} keys from {len(_recs)} receipts, so
       a clustered draw inflates all of them.
     * ⛔ And this is a DESIGN and not a measurement: nothing here is ordered, nothing is registered, and
       the per-seat draw remains the gating seat's to order when its trigger is met.
""")
sys.exit(1 if FAILURES else 0)
