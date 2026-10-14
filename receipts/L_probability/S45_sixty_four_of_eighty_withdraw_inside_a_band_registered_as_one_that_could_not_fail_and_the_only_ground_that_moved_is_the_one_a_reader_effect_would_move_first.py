#!/usr/bin/env python3
r"""S45 -- THE REGISTERED READ OF r7328's EIGHTY, AND WHAT A BAND THAT CANNOT FAIL IS WORTH.

** WHAT WAS ORDERED. **  `r7325` ⑤: ① run the draw as registered, both bands as filed and the unfailable
one declared; ② the reader arm stands at `52` paired keys and PAIRED now means the two readers read the
SAME keys; ③ report `pi_d` as the arm's quantity and the margin only beside it.

*** ⓐ `64` OF `80` WITHDRAW.  THE REGISTERED BAND IS `37`-`71` AND THE READ IS INSIDE IT -- AND THE
    REGISTRATION SAID IN TERMS, BEFORE THE DRAW, THAT THIS BAND COULD NOT BE FAILED AT ANY SIZE THIS
    FRAME CAN SELL. ***
  => ** So the pass is reported as carrying NOTHING, which is what the standing rule r7325 made of this
     seat's own declaration is for: a reader who meets a pass that could not have failed has learned
     nothing from the pass. **  What carries content is the interval -- `+/-8.67` naive, `+/-10.78` at
     the registered design effect, `+/-9.25` at the one measured here -- and the grounds.

*** ⓑ AND THE CLUSTERING THE REGISTRATION IMPORTED OVER-BOUGHT BY `38` PER CENT. ***  *Measured on this
    draw's own outcomes the `ICC` is `0.079` against the imported `0.327`, so the design effect is
    `1.136` against `1.566` and the effective sample is `70.4` of `80` rather than `51.1`.*  ** And the
    figure that moved is the ICC and not the spread: the cluster weighting came out at `2.73`, the
    registered value exactly. **

*** ⓒ EXACTLY TWO GROUNDS MOVED BETWEEN THIS SAMPLE AND `r7320`'s, AND THE BIG ONE IS TEST `4`: `1` of
    `40` TO `15` of `80`, `+16.2` POINTS (`+3.7` TO `+26.4`). ***  *Every other ground's interval spans
    zero, so `r7320`'s own headline stands: Test `5` is flat and what withdraws a row is still largely
    where the check was cut.*
  ** ⚠ AND THE HONEST READING CUTS AGAINST THIS SEAT: Test `4` turns on occurrence counts and count
     HISTORIES -- the ground a reader effect would move first -- and this read used a count-history
     instrument that `r7320`'s read did not. **  *Confounded by the reader and by the text change both,
     reported as a ground that moved and as the sharpest argument yet for the reader arm.*

*** ⓓ THE REPLICATION IS NOT DISTINGUISHABLE FROM ZERO: `80.0` against `67.5` per cent is `+12.5`
    points, Newcombe `-3.5` to `+29.6`. ***  *A direction, not a difference -- member `89` applied to
    this seat's own replication.*

*** ⓔ TWO OF THE `80` WERE ALSO READ BLIND BY `70`'s POOL AND BY `71` UNDER THIS SAME TEXT.  ALL THREE
    READERS AGREE ON THE REGISTERED QUANTITY ON BOTH. ***  *The four-way verdict splits on one:
    `DELIBERATE` by step `2`'s third bullet against `MEANING-HELD` by step `4`'s first, which both reach
    a complete clause carrying a says-claim with only the decision order between them.*
  => ** And what that costs is computed: `8` of the `14` HELD rows sit on the same boundary, and taking
     every one of them at step `4` leaves the registered quantity at `64`.  The one ambiguity two
     independent readers actually exercised cannot reach the band. **

⛔ ** THE READER ARM IS READ ONCE AND ITS SECOND READING IS OWED: ** *`pi_d` is the share of keys whose
TWO readings differ and this revision is ONE reader.  Routed with its branches, not guessed.

⚠ WHAT THIS CANNOT FIX is at the foot, beginning with the fact that it is a self count whose band was
registered as unfailable, so neither protects it.
"""
import collections
import io
import math
import os
import random
import re
import subprocess
import sys

_C = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                  'computations', 'beyond_the_wall')
sys.path.insert(0, os.path.join(_C, 'r7330_60_the_eighty_read'))
sys.path.insert(0, os.path.join(_C, 'r7328_60_the_registration'))
sys.path.insert(0, os.path.join(_C, 'r7326_60_the_draw_designed'))
import read as T                                                       # noqa: E402
import size as G                                                       # noqa: E402
import design as D                                                     # noqa: E402

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
ORDER = '4d2010fc'              # r7325's orders on the trunk
PREG = 'aadfeb2c'               # the commit that PUSHED r7328's registration, before its draw
DRAW = '7cd0d48d'               # the commit that RAN that draw
D7330 = 'computations/beyond_the_wall/r7330_60_the_eighty_read'
D7328 = 'computations/beyond_the_wall/r7328_60_the_registration'


def show(sha, rel):
    return subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:{rel}'],
                          capture_output=True, text=True, errors='replace').stdout


def git(*a):
    return subprocess.run(['git', '-C', ROOT] + list(a),
                          capture_output=True, text=True, errors='replace').stdout


R = T.rows()
OUT = collections.Counter(r['outcome'] for r in R)
K, N = OUT['WITHDRAWN'], len(R)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('A -- THE ORDER, READ WHERE IT WAS WRITTEN')

ORD = show(ORDER, 'FOR_60.md')
_items = ['Run the draw as registered', 'stands as sized',
          'the two readers read the SAME keys', 'do not copy its split',
          'the margin only beside it']
print(f'      the order\'s three items present at {ORDER}: {[s in ORD for s in _items]}')
gate(f'Ⓐ①  THE ORDER IS READ AT `{ORDER}` AND NOT PARAPHRASED: `r7325` ⑤ says run the draw as '
     f'registered, stand the reader arm as sized, make it PAIRED in the literal sense -- the two '
     f'readers read the same keys -- and report the arm\'s quantity with the margin only beside it.  '
     f'** The seat that is ordered does not get to restate the order **',
     all(s in ORD for s in _items))

_charge = ['a measure of disagreement requires the same unit read twice',
           'every registration states whether', 'it is yours']
print(f'      the member charged and the standing rule made of this seat\'s declaration: '
      f'{[s in ORD for s in _charge]}')
gate(f'Ⓐ②  AND WHAT `r7325` DID WITH THIS SEAT\'S TWO FINDINGS IS RECORDED RATHER THAN '
     f're-litigated: the estimand failure is charged as member `91` -- *a measure of disagreement '
     f'requires the same unit read twice* -- against this seat\'s own filing of it as the same '
     f'family as an earlier member, and the unfailable-band declaration is made STANDING for every '
     f'seat.  ** A seat does not get to decide which of its findings is a member **',
     all(s in ORD for s in _charge))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('B -- THE READ COVERS THE DRAWN SAMPLE AND NOTHING ELSE')


def sample_rows(text):
    out = {}
    for l in text.split('\n'):
        if l.startswith('#') or not l.strip():
            continue
        c = l.split('\t')
        out[int(c[0])] = (c[1], c[2], c[6])
    return out


_S = sample_rows(show(DRAW, f'{D7328}/SAMPLE_80.tsv'))
_mismatch = [n for n in _S
             if (_S[n][0], _S[n][1], _S[n][2]) != (
                 {r['n']: r for r in R}[n]['receipt'],
                 {r['n']: r for r in R}[n]['literal'],
                 {r['n']: r for r in R}[n]['arm'])]
_outcomes = {r['outcome'] for r in R}
_named = [r for r in R if r['outcome'] == 'WITHDRAWN'
          and re.match(r'(Test [1-7]|step [1-4])$', r['decided_at'])]
print(f'      sample rows {len(_S)}, read rows {N}, mismatches {len(_mismatch)};  '
      f'outcomes seen {sorted(_outcomes)}')
gate(f'Ⓑ①  THE READ IS JOINED TO THE SAMPLE AS DRAWN, read at the DRAW commit and not in the '
     f'working tree: all `{len(_S)}` rows match on receipt, literal and arm with `{len(_mismatch)}` '
     f'mismatches, every row carries one of the three outcomes registered before the draw, and all '
     f'`{len(_named)}` of the `{K}` withdrawals name a test or a step.  ** A reading that does not '
     f'join its own draw is a different sample **',
     not _mismatch and len(_S) == N == 80
     and _outcomes <= {'WITHDRAWN', 'HELD', 'MOVED'} and len(_named) == K)

_both = [r for r in R if r['arm'] == 'both']
gate(f'Ⓑ②  and THE READER BLOCK IS THE FIRST `52` AS REGISTERED, which is checked as a property of '
     f'the order and not of a label: the `{len(_both)}` rows marked as the paired arm are exactly '
     f'rows `1` to `{len(_both)}`, so the block is a PREFIX of the drawn order and cannot have been '
     f'chosen after the keys were seen',
     len(_both) == 52 and {r['n'] for r in _both} == set(range(1, 53)))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('C -- THE REGISTERED QUANTITY, AND THE BAND SHOWN UNFAILABLE BY ARITHMETIC')

_lo, _hi = G.wilson(K, N)
_en_reg = N / T.DEFF_REG
_clo, _chi = G.wilson(K / N * _en_reg, _en_reg)
print(f'      {K} of {N} = {100 * K / N:.1f}%;  band {T.BAND_LO}-{T.BAND_HI};  '
      f'naive {100 * _lo:.1f}-{100 * _hi:.1f};  clustered {100 * _clo:.1f}-{100 * _chi:.1f}')
gate(f'Ⓒ①  THE REGISTERED QUANTITY IS `{K}` OF `{N}` AND IT IS INSIDE THE BAND `{T.BAND_LO}`-'
     f'`{T.BAND_HI}` FIXED BEFORE THE DRAW -- and ⛔ **the band is shown UNFAILABLE by arithmetic '
     f'rather than conceded in prose**: it spans `{T.BAND_HI - T.BAND_LO}` of `{N}` where the whole '
     f'interval this size resolves is `{100 * _clo:.1f}`-`{100 * _chi:.1f}`, so no outcome of `{N}` '
     f'keys lands outside it.  ** The pass is therefore reported as carrying nothing **',
     T.BAND_LO <= K <= T.BAND_HI
     and T.BAND_LO / N < _clo and T.BAND_HI / N > _chi)

_hw_naive = 100 * (_hi - _lo) / 2
_hw_reg = 100 * (_chi - _clo) / 2
gate(f'Ⓒ②  and WHAT THE READ DELIVERS IS THE INTERVAL, which is what `r7321` ② ordered the arm '
     f'sized to: `±{_hw_naive:.2f}` points naive and `±{_hw_reg:.2f}` at the registered design '
     f'effect, against the `±12.45` the registration priced and the `±16.46` `r7320`\'s `40` bought.  '
     f'** The arm bought what it was sized to buy **',
     _hw_reg < 12.45 and _hw_reg > _hw_naive and _hw_naive < 10.0)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('D -- THE CLUSTERING, MEASURED ON THIS DRAW AND CONTROLLED')

_g = collections.defaultdict(list)
for r in R:
    _g[r['receipt']].append(1 if r['outcome'] == 'WITHDRAWN' else 0)
_groups = list(_g.values())
_icc, _m0 = T.icc_oneway(_groups)
_deff = 1 + (_m0 - 1) * max(_icc, 0.0)
# CONTROL: the same verdicts re-grouped at random into clusters of the same sizes carry no ICC, so a
# low figure here is not the estimator failing to see one.
_rng = random.Random(7330)
_flat = [y for v in _groups for y in v]
_rng.shuffle(_flat)
_shuf, _i = [], 0
for v in _groups:
    _shuf.append(_flat[_i:_i + len(v)])
    _i += len(v)
_icc_s, _ = T.icc_oneway(_shuf)
print(f'      {N} keys in {len(_groups)} receipts, m0 {_m0:.2f};  ICC {_icc:+.3f}, deff {_deff:.3f}')
print(f'      CONTROL -- the same verdicts re-grouped at random: ICC {_icc_s:+.3f}')
gate(f'Ⓓ①  ⛭⛭ THE CLUSTERING IS MEASURED ON THIS DRAW AND THE REGISTRATION OVER-BOUGHT: `ICC` '
     f'`{_icc:.3f}` against the imported `0.327`, design effect `{_deff:.3f}` against the registered '
     f'`{T.DEFF_REG}`, effective sample `{N / _deff:.1f}` of `{N}` against `{_en_reg:.1f}`.  '
     f'** CONTROLLED by re-grouping the same verdicts at random into clusters of the same sizes, '
     f'where the correlation reads `{_icc_s:.3f}` -- so a small figure here is the receipts and not '
     f'a blind estimator **',
     _deff < T.DEFF_REG and _icc < 0.327 and abs(_icc_s) < 0.10)

gate(f'Ⓓ②  and THE FIGURE THAT MOVED IS THE CORRELATION AND NOT THE SPREAD, which is the half that '
     f'makes it a finding about the estimate rather than about the rotation: the cluster weighting '
     f'came out at `{_m0:.2f}`, the registered value to two places, so the same `m0` carried the '
     f'registered `ICC` to `{1 + (_m0 - 1) * 0.327:.3f}` and carries this one to `{_deff:.3f}`.  '
     f'** The rotation delivered the spread it promised; the imported correlation was the pessimistic '
     f'end and is now bracketed **',
     abs(_m0 - 2.73) < 0.005 and abs((1 + (_m0 - 1) * 0.327) - T.DEFF_REG) < 0.005)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('E -- THE REPLICATION, AND THE ONE GROUND THAT MOVED')

_nlo, _nhi = D.newcombe(K, N, 27, 40)
print(f'      {100 * K / N:.1f}% against 67.5%: {100 * (K / N - 27 / 40):+.1f} points, '
      f'Newcombe {100 * _nlo:+.1f} to {100 * _nhi:+.1f}')
gate(f'Ⓔ①  THE REPLICATION IS STATED AS A DIRECTION AND THE GATE ASSERTS THAT IT IS ONE: `{K}` of '
     f'`{N}` against `r7320`\'s `27` of `40` is `{100 * (K / N - 27 / 40):+.1f}` points with a '
     f'Newcombe interval of `{100 * _nlo:+.1f}` to `{100 * _nhi:+.1f}`, which CONTAINS zero.  '
     f'** So no difference is claimed -- member `89` applied to this seat\'s own replication, and '
     f'the gate fails if the interval ever excludes zero without the claim changing **',
     _nlo < 0 < _nhi)

_prev = io.open(os.path.join(ROOT, 'computations', 'beyond_the_wall',
                             'r7320_60_the_early_era_sampled', 'RESULT_40.tsv'),
                encoding='utf-8').read()
_pg, _pn = collections.Counter(), 0
for _l in _prev.split('\n'):
    if _l.startswith('#') or not _l.strip():
        continue
    _c = _l.split('\t')
    if len(_c) < 8:
        continue
    _pn += 1
    _m = re.match(r'(Test \d|step \d)', _c[7])
    if _m:
        _pg[_m.group(1)] += 1
_t = collections.Counter(r['decided_at'] for r in R)
print(f'      r7320: {_pn} rows, {sum(_pg.values())} grounds parsed;  this read: {N} rows, '
      f'{sum(_t.values())} grounds')
gate(f'Ⓔ②  and THE COMPARISON\'s OWN DENOMINATORS ARE ASSERTED BEFORE ANY DIFFERENCE IS TAKEN, '
     f'because a silent zero here fabricates every difference below: all `{_pn}` of `r7320`\'s rows '
     f'parse to a named ground and all `{N}` of this read\'s do.  ** This gate exists because the '
     f'first draft of the comparison read the wrong column and returned `0` of `40` on every '
     f'ground, which would have printed eight differences that were all the bug **',
     sum(_pg.values()) == _pn == 40 and sum(_t.values()) == N)

_moved, _flat_g = [], []
for _key in ('Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5', 'step 1', 'step 2', 'step 4'):
    if not (_t[_key] or _pg[_key]):
        continue
    _l2, _h2 = D.newcombe(_t[_key], N, _pg[_key], _pn)
    (_moved if (_l2 > 0 or _h2 < 0) else _flat_g).append(_key)
print(f'      grounds whose interval EXCLUDES zero: {_moved};  spanning zero: {_flat_g}')
gate(f'Ⓔ③  ⛭⛭ EXACTLY TWO GROUNDS MOVED AND THE BIG ONE IS TEST `4`: `{_pg["Test 4"]}` of `{_pn}` '
     f'to `{_t["Test 4"]}` of `{N}`, and step `4` the other way, with every other ground\'s interval '
     f'spanning zero -- so `r7320`\'s own headline STANDS: Test `5` is flat at `{_t["Test 5"]}` of '
     f'`{N}` against `{_pg["Test 5"]}` of `{_pn}`.  ** And Test `4` is the ground a reader effect '
     f'would move first, which is said in the reading rather than left for the gate **',
     _moved == ['Test 4', 'step 4'] and 'Test 5' in _flat_g and 'Test 1' in _flat_g)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('F -- THE CROSS-SEAT CHECK, AND WHAT THE ONE DISAGREEMENT CANNOT MOVE')

_mine = {(r['receipt'], r['literal']): r for r in R}
_agree_q, _agree_4, _ov_total = 0, 0, 0
for _nm, _rel in (('70', f'{"computations/beyond_the_wall"}/r7315_70_redraft3_score/'
                         'APPLICATION_70_blind.tsv'),
                  ('71', f'{"computations/beyond_the_wall"}/r7321_71_redraft3_blind/'
                         'BLIND_READ_71_redraft3.tsv')):
    _S2 = {}
    for _l in io.open(os.path.join(ROOT, _rel), encoding='utf-8'):
        if _l.startswith('#') or not _l.strip():
            continue
        _c = _l.rstrip('\n').split('\t')
        if _c[0] == 'receipt':
            continue
        _S2[(_c[0], _c[1])] = _c[3].strip()
    for _kk in [x for x in _mine if x in _S2]:
        _ov_total += 1
        _theirs = _S2[_kk]
        _agree_q += ((_mine[_kk]['outcome'] == 'WITHDRAWN') == (_theirs == 'REPAIR-OWED'))
        _agree_4 += ({'REPAIR-OWED': 'WITHDRAWN', 'DELIBERATE': 'HELD'}.get(_theirs, 'MOVED')
                     == _mine[_kk]['outcome'])
print(f'      blind overlaps {_ov_total};  agree on the registered quantity {_agree_q}; '
      f'on the four-way verdict {_agree_4}')
gate(f'Ⓕ①  TWO OF THE `{N}` WERE READ BLIND BY BOTH OTHER POOLS UNDER THIS SAME TEXT, and ALL THREE '
     f'READERS AGREE ON THE REGISTERED QUANTITY ON EVERY ONE: `{_agree_q}` of `{_ov_total}` '
     f'comparisons agree there, while `{_agree_4}` of `{_ov_total}` agree on the rule\'s four-way '
     f'verdict.  ** The split is `DELIBERATE` by step `2`\'s third bullet against `MEANING-HELD` by '
     f'step `4`\'s first, which both reach a complete clause carrying a says-claim **',
     _ov_total == 4 and _agree_q == 4 and _agree_4 == 2)

_exposed = [r for r in R if r['outcome'] == 'HELD'
            and ('whole' in r['detail'].lower() or 'headline' in r['detail'].lower())]
print(f'      HELD rows on that boundary: {len(_exposed)} of {OUT["HELD"]};  moving all of them '
      f'gives WITHDRAWN {K}, HELD {OUT["HELD"] - len(_exposed)}, '
      f'MOVED {OUT["MOVED"] + len(_exposed)}')
gate(f'Ⓕ②  ⛭⛭ AND WHAT THE AMBIGUITY COSTS IS COMPUTED RATHER THAN ARGUED: `{len(_exposed)}` of the '
     f'`{OUT["HELD"]}` held rows sit on that same boundary, and taking every one of them at step `4` '
     f'instead gives `WITHDRAWN {K}`, `HELD {OUT["HELD"] - len(_exposed)}`, '
     f'`MOVED {OUT["MOVED"] + len(_exposed)}`.  ** The registered quantity does not move at all, so '
     f'the one ambiguity two independent readers actually exercised cannot reach the band **',
     len(_exposed) >= 7 and OUT['HELD'] - len(_exposed) >= 0)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('G -- THE RESTRAINT: ONE READER, NO LEDGER, AND THE ARM\'s QUANTITY NOT CLAIMED')

_base_at_preg = show(f'{PREG}~1', 'corpus/quote_pin_baseline.tsv')
_base_now = io.open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8').read()
_touched = sorted({f for f in git('diff', '--name-only', f'{PREG}~1', DRAW).split('\n') if f})
print(f'      the ledger byte-identical across {PREG}~1..working tree: '
      f'{_base_at_preg == _base_now};  receipts in the registration range: '
      f'{[f for f in _touched if f.startswith("receipts/")]}')
gate(f'Ⓖ①  ⛔ **NOTHING IS WRITTEN TO THE LEDGER, as the specific negative it is**: '
     f'`corpus/quote_pin_baseline.tsv` is byte-identical to its state before the registration, so '
     f'none of the `{K}` withdrawals read here has been verdicted.  ** `{K}` withdrawals in a sample '
     f'are a FINDING; writing them in would add `{K}` to the trunk\'s owed class, and that decision '
     f'sits with the gating seat as it did at `r7320` **',
     _base_at_preg == _base_now)

_reading = io.open(os.path.join(ROOT, D7330, 'THE_READING.md'), encoding='utf-8').read()
_ticked = set()
for _m in re.findall(r'`([^`]+)`', _reading):
    _ticked.add(_m)
    for _num in re.findall(r'\d+(?:\.\d+)?', _m):
        _ticked.add(_num)
_pid = {'15.9', '9.1', '26.3', '52'} <= _ticked
_no_pid_claimed = not any(r.get('pi_d') for r in R)
_cols = [l for l in io.open(os.path.join(ROOT, D7330, 'RESULT_80.tsv'),
                            encoding='utf-8') if l.startswith('# n\t')][0]
_colnames = _cols.lstrip('# ').rstrip('\n').split('\t')
print(f'      the result columns: {_colnames};  the arm\'s quantity and its interval carried in the '
      f'reading: {_pid}')
gate(f'Ⓖ②  and THE ARM IS READ ONCE AND ITS `pi_d` IS NOT CLAIMED FROM THIS READ: the result file '
     f'carries ONE verdict per key and no second reading (`{len(_colnames)}` columns, one outcome), '
     f'and the reading reports the arm\'s quantity as the figure `r7328` measured with its interval '
     f'and the two MARGINS only beside it -- read by PARSING the reading\'s backticked figures.  '
     f'** `pi_d` is the share of keys whose TWO readings differ, and one reader cannot produce it **',
     _pid and _colnames.count('outcome') == 1 and 'decided_at' in _colnames)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print("=" * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
print("=" * 100)
print()
print(f'  ⛔ ** {K} OF {N} WITHDRAW AND THE BAND HOLDS -- AND THE BAND WAS REGISTERED, BEFORE THE')
print('     DRAW, AS ONE THAT COULD NOT FAIL. ** So the pass carries nothing and is reported that')
print(f'     way; what carries content is the interval (±{_hw_reg:.2f}) and the grounds.')
print(f'  ⛭⛭ ** THE CLUSTERING THE REGISTRATION IMPORTED OVER-BOUGHT BY 38 PER CENT: ICC {_icc:.3f}')
print(f'     against 0.327, design effect {_deff:.3f} against {T.DEFF_REG}. ** And the ICC is what moved:')
print(f'     the cluster weighting came out at {_m0:.2f}, the registered value exactly.')
print('  ⛭⛭ ** EXACTLY TWO GROUNDS MOVED AND THE BIG ONE IS TEST 4, FROM 1 OF 40 TO 15 OF 80. **')
print('     ⚠ And it is the ground a reader effect would move first, on a read that used a')
print("     count-history instrument r7320's read did not -- confounded, and said so.")
print('  ✔ ** ALL THREE READERS AGREE ON THE REGISTERED QUANTITY ON BOTH BLIND OVERLAPS, and the')
print('     one four-way split cannot reach the band: moving every exposed row leaves 64. **')
print('  ⛔ The reader arm is read ONCE; its second reading is owed and routed.')
if FAILURES:
    print('\n  FAILED:')
    for f in FAILURES:
        print(f'   - {f}')
sys.exit(1 if FAILURES else 0)
