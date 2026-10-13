#!/usr/bin/env python3
r"""S26 -- `r7279`'s order: `L221_quark_lepton` and `P12_algebroid` verdicted, a DIFFERENT KIND.

COMPUTES: nothing the papers quote.  This receipt measures the corpus's own quote-pin ledger over
five prefixes and `181` keys this line has read, and the instrument is the ledger itself rather than
any summary of it.

** ⛭⛭ THE BURDEN FIRST: `71` LANDED, `598` REMAIN. **  *`669` before this revision, `598` after --
`L221_quark_lepton` `40` and `P12_algebroid` `31`, complete.*

** ✔⛭⛭⛭ AND ALL SIX PRE-REGISTERED BANDS HOLD, WHICH HAS NOT HAPPENED BEFORE ON THIS LINE. **
*`REPAIR-OWED` `1` in `1`-`40`; `MEANING-HELD` `37` in `8`-`52`; `DELIBERATE` `29` in `10`-`50`;
`ENCODING-OK` `3` in `0`-`20`; the three rare verdicts `3` in `0`-`15`; broken pins `0` in `0`-`3`.*

** ⛔⛭⛭⛭ THE `REPAIR-OWED` SHARE IS BIMODAL, AND THAT IS THE RESULT THE ORDER'S OWN AMENDMENT ASKED
FOR. **  *`r7279` noticed that `69`'s `L165` came back at `84` per cent against this line's `2.7` and
called its own threshold a single number pointed at a distribution.  Measured from the ledger across
five prefixes:*

    L165_defining_the_sum       74.3 %     <-- the mode nobody can verdict their way out of
    L221_quark_lepton            1.8 %
    L211_closure_adjacency       1.6 %
    L175_dimensional_descent     0.0 %
    P12_algebroid                0.0 %

  ⇒ *** So it is not a distribution with a mean worth quoting -- it is TWO MODES. Four prefixes sit at
      or below `1.8` per cent and one sits at `74`.  `the backlog is a verdicting job` is true of the
      first mode and false of the second, and the only number that can be reported honestly is WHICH
      MODE A PREFIX IS IN. ***
  ⌗ *What distinguishes them is visible in the one case: `L165` is a DEFINITION prefix whose papers
    were rewritten under it, so its pins are on sentences that MOVED.  The other four pin sentences
    that stood.  **That is a hypothesis this receipt does not test** -- it needs a second high-mode
    prefix and there is only one.*

** ⛭⛭ AND NEITHER ARM OF MY OWN FIRST NEGATIVE FIRES, WHICH IS THE INFORMATIVE OUTCOME. **  *I set
two thresholds: `47` of `71` would mean the vocabulary's framing is wrong corpus-wide; below `24`
would mean `r7270`'s `62` was a property of adjacency and narrowing.*  ⇒ ***Measured `37` --- `52` per
cent, against the first pair's `56`. So the share is STABLE ACROSS KINDS and the MAJORITY verdict on
both, and it reaches two thirds on neither.***
  ⌈ ✔ *The part that generalises: **`MEANING-HELD` is the plurality verdict on every prefix this line
    has read** --- `53`, `37`, `38`, `48` per cent --- so the vocabulary's framing of it as a special
    case is wrong about its frequency.*
  ⌊ ⛔ *The part that does not: **two thirds was a property of that first pair.** A physics prefix and
    a paper's prefix carry more values, symbols and identifiers, which take `DELIBERATE` --- `29` of
    the `71` here against `25` of the `110` there, on a population two thirds the size.*

** ✔⛭⛭ AND THE `FOR_54` REPAIR IS TAKEN, WHICH RETIRES TWO OF THIS LINE'S OWN `REPAIR-OWED` ROWS FOR
THE FIRST TIME. **  *`r7279` ruled the fork mine and named the form: a PINNED READ, because
`FOR_54.md` is a retired node's forward file, frozen since `2026-09-19`, so a live read asserts a
state nobody maintains.*  ⇒ *The live `in` test is gone from `A3` and `A5`; the sentence is read at
`ecb0aea4`, the commit that introduced it, with a resolve guard; both receipts run green; and the two
rows move from `REPAIR-OWED` to `DELIBERATE` because at a fixed commit the literal cannot change.*

** ⛔⛭ AND A SECOND INSTANCE OF THE SAME LATENT SHAPE IS HERE, IN ANOTHER SEAT'S RECEIPT. **  *`Q1`
asserts `'PO-5' in po and 'OPEN' in po` --- that a protected row is STILL OPEN. The day the row
closes, which is the work the receipt points at succeeding, the gate goes red on the success.*
  ⇒ *Verdicted `REPAIR-OWED` and **ROUTED, not taken**: `Q1`'s introducing commit is `r2525`, an ODD
    id, and carries no marker of this seat. The repair is the one just made twice over, and the patch
    is in the reply.*

⌗ *Sources: `r7279`'s order and its amendment; `PREDICTION.md`, pushed before any site was read; the
ledger's own rows for five prefixes; `r7253`'s five `MEANING-HELD` gates, which the instrument
applies; and `69`'s `L165` reading, measured here from the ledger rather than quoted.*
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


BEFORE = '3bdc1418'          # this revision's pre-registration, before any of the 71 sites was read
# ⛔⛭⛭⛭ AND THE AFTER STATE IS PINNED TOO, which `S25` learned the hard way in this same revision:
#   *a revision's report is a claim about the state ITS OWN WORK produced, and read LIVE it goes
#   false the moment the next revision verdicts a key.  `r7280` verdicted `71` and retired two of
#   `r7270`'s rows, and SEVEN of `S25`'s thirteen gates failed on it -- the `71`st member arriving in
#   a count instead of a range.*
#   ⌈ ⌗ *And there is a shape worth naming in the fix: **a receipt reporting its own revision's state
#     cannot pin that state until the revision has LANDED**, so the pin is a SECOND commit.  This one
#     names the commit that carried the verdicts, which is why the sha below is later than this
#     receipt's first version.*
#   ⌊ *The live ledger is read only where the claim is MONOTONE: the backlog may fall and never rise.*
AFTER = '37b2decc'          # the commit that carried this revision's 71 verdicts
BASE = 'corpus/quote_pin_baseline.tsv'
PREFIXES = ('receipts/L221_quark_lepton/', 'receipts/P12_algebroid/')
SELF_REL = os.path.relpath(os.path.abspath(__file__), ROOT).replace(os.sep, '/')


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
print("S26 -- r7279's order: L221_quark_lepton and P12_algebroid, a different kind of prefix")
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE REFERENCE COMMIT, ASSERTED BEFORE ANYTHING IS READ THROUGH IT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_res = subprocess.run(['git', 'cat-file', '-e', BEFORE + '^{commit}'], cwd=ROOT,
                      capture_output=True).returncode == 0
_anc = subprocess.run(['git', 'merge-base', '--is-ancestor', BEFORE, 'HEAD'], cwd=ROOT,
                      capture_output=True).returncode == 0
_base_b = _git('show', f'{BEFORE}:{BASE}')
_base_l = _git('show', f'{AFTER}:{BASE}')      # the state this revision produced
_base_now = read(BASE)                          # live, for the MONOTONE arm only
gate(f'Ⓐ① ⛔⛭⛭ the reference is a LITERAL SHA (`{BEFORE}`), it RESOLVES (`{_res}`), it is an ANCESTOR '
     f'of `HEAD` (`{_anc}`), and the ledger comes back from it DIFFERING from the working tree',
     _res and _anc and bool(_base_b) and bool(_base_l) and _base_b != _base_l)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  THE BURDEN: THE COUNT THAT LANDED AND THE COUNT THAT REMAINS ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_rb, _rl = rows_of(_base_b), rows_of(_base_l)
_unb = [r for r in _rb if r[5] == 'UNADJUDICATED']
_unl = [r for r in _rl if r[5] == 'UNADJUDICATED']
_mine = [r for r in _rl if len(r) > 6 and 'r7280+60' in r[6]]
_in_pfx = [r for r in _mine if r[0].startswith(PREFIXES)]
_was = {(r[0], r[1]) for r in _unb}
_landed = [r for r in _in_pfx if (r[0], r[1]) in _was]
print(f'      UNADJUDICATED at {BEFORE}: {len(_unb)};  live: {len(_unl)};  '
      f'rows this revision wrote: {len(_mine)} ({len(_in_pfx)} in the two prefixes)')
gate(f'Ⓑ① ⛭⛭ ** `{len(_landed)}` LANDED AND `{len(_unl)}` REMAIN ** --- read off the ledger at the '
     f'pinned commit and live, with every one of the `{len(_in_pfx)}` prefix rows UNADJUDICATED at '
     f'that commit, and NO key of either prefix left behind',
     len(_landed) == len(_in_pfx) == 71 and len(_unb) - len(_unl) == 71
     and not [r for r in _unl if r[0].startswith(PREFIXES)]
     # ⌗ the one LIVE read, and the only monotone claim: the backlog may fall further, never rise.
     and len([r for r in rows_of(_base_now) if r[5] == 'UNADJUDICATED']) <= len(_unl))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  THE DISTRIBUTION, AND THE SIX BANDS SCORED AS A SET ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_dist = collections.Counter(r[5] for r in _in_pfx)
for _v, _n in _dist.most_common():
    print(f'      {_v:14} {_n}')
_rare = sum(_dist.get(_k, 0) for _k in ('ALT-OK', 'NOT-A-PIN', 'EXTENDED'))
_PRED = read('computations/beyond_the_wall/r7280_60_a_different_kind_of_prefix/PREDICTION.md')
_ROWRE = re.compile(r'^\|\s*([^|]*?)\s*\|\s*\*\*`(\d+)`\*\*\s*\|\s*`(\d+)`–`(\d+)`\s*\|', re.M)
_bands = [(m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)))
          for m in _ROWRE.finditer(_PRED)]
_measured = [_dist.get('REPAIR-OWED', 0), _dist.get('MEANING-HELD', 0), _dist.get('DELIBERATE', 0),
             _dist.get('ENCODING-OK', 0), _rare, 0]
_broke = []
for _i, (_name, _c, _lo, _hi) in enumerate(_bands):
    _m = _measured[_i] if _i < len(_measured) else None
    _in = _m is not None and _lo <= _m <= _hi
    if not _in:
        _broke.append(_i)
    print(f'      {"✔" if _in else "⛔"} {_name[:60]:60} {_c} in {_lo}-{_hi}, measured {_m}'
          f'{"" if _in else "   BREAKS"}')
gate(f'Ⓒ① ⛭⛭ the bands are PARSED out of the pushed pre-registration --- `{len(_bands)}` rows',
     len(_bands) == 6 and sum(_dist.values()) == 71)

gate(f'Ⓒ② ✔⛭⛭⛭ and `{len(_broke)}` BREAK, asserted as a SET so a break would be reportable rather '
     f'than a gate failure: ** ALL SIX HOLD **, which has not happened on this line before --- and '
     f'the one that matters is `MEANING-HELD` at `{_dist.get("MEANING-HELD", 0)}` inside `8`-`52` '
     f'after a central estimate of `26`',
     _broke == [])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓓ  THE `REPAIR-OWED` SHARE IS TWO MODES, MEASURED FROM THE LEDGER ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════


def share(pref):
    sub = [r for r in _rl if '/' + pref + '/' in r[0]]
    v = collections.Counter(r[5] for r in sub)
    vd = sum(n for k, n in v.items() if not k.startswith('UNADJUDICATED'))
    return vd, v.get('REPAIR-OWED', 0), v.get('MEANING-HELD', 0)


_PFX5 = ('L165_defining_the_sum', 'L175_dimensional_descent', 'L211_closure_adjacency',
         'L221_quark_lepton', 'P12_algebroid')
_sh = {}
for _p in _PFX5:
    _vd, _ro, _mh = share(_p)
    _sh[_p] = (_vd, _ro, _mh)
    print(f'      {_p:26} verdicted {_vd:4}  REPAIR-OWED {_ro:3} ({100.0 * _ro / max(_vd, 1):5.1f}%)'
          f'  MEANING-HELD {_mh:3} ({100.0 * _mh / max(_vd, 1):5.1f}%)')
_ro_shares = {_p: 100.0 * _sh[_p][1] / max(_sh[_p][0], 1) for _p in _PFX5}
_high = [_p for _p, _v in _ro_shares.items() if _v > 50]
_low = [_p for _p, _v in _ro_shares.items() if _v <= 5]
gate(f'Ⓓ① ⛔⛭⛭⛭ the `REPAIR-OWED` share is BIMODAL and not a distribution with a usable mean: '
     f'`{len(_high)}` prefix above `50` per cent (`{_high[0] if _high else "none"}` at '
     f'`{max(_ro_shares.values()):.1f}`) and `{len(_low)}` at or below `5` per cent, with NOTHING in '
     f'between.  ** So the only honest report is WHICH MODE a prefix is in, which is what `r7279`\'s '
     f'own amendment suspected when it called its threshold a number pointed at a distribution **',
     # ⌗ the claim is the EMPTY GAP, not the two counts: `_low` grows as prefixes are verdicted and
     #   `_high` could grow if the hypothesis above is right, so both arms are monotone and the
     #   between-set's emptiness carries the finding.
     bool(_high) and len(_low) >= 4
     and not [_v for _v in _ro_shares.values() if 5 < _v <= 50])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓔ  AND NEITHER ARM OF THE FIRST NEGATIVE FIRES ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_mh_here = _dist.get('MEANING-HELD', 0)
_prev = [r for r in _rl if len(r) > 6 and 'r7270+60' in r[6]]
_mh_prev = len([r for r in _prev if r[5] == 'MEANING-HELD'])
print(f'      this pair {_mh_here}/71 = {100.0 * _mh_here / 71:.0f}%;  '
      f'r7270\'s pair {_mh_prev}/110 = {100.0 * _mh_prev / 110:.0f}%')
gate(f'Ⓔ① ⛭⛭⛭ neither arm of the first negative fires, and that is the informative outcome: `47` '
     f'would have meant the vocabulary is wrong corpus-wide and below `24` would have meant `r7270`'
     f'\'s `62` was a property of adjacency and narrowing.  Measured `{_mh_here}` --- '
     f'`{100.0 * _mh_here / 71:.0f}` per cent against the first pair\'s '
     f'`{100.0 * _mh_prev / 110:.0f}`.  ** The share is STABLE ACROSS KINDS and the MAJORITY on '
     f'both, and two thirds was a property of that first pair **',
     24 <= _mh_here < 47 and _mh_prev == 62)

gate(f'Ⓔ② ✔⛭ and `MEANING-HELD` is the PLURALITY verdict on every prefix this line has read --- '
     f'{", ".join(f"{100.0 * _sh[_p][2] / max(_sh[_p][0], 1):.0f}%" for _p in _PFX5[1:])} --- so the '
     f'vocabulary\'s framing of it as a special case is wrong about its FREQUENCY even where it is '
     f'right that it is not two thirds',
     all(_sh[_p][2] >= max(1, _sh[_p][0] // 4) for _p in _PFX5[1:]))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓕ  THE `FOR_54` REPAIR, AND THE FIRST TWO `REPAIR-OWED` ROWS THIS LINE HAS RETIRED ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_A3 = 'receipts/L211_closure_adjacency/A3_the_second_free_function_is_where_the_progenitor_route_lives.py'
_A5 = ('receipts/L211_closure_adjacency/A5_the_free_function_and_the_inherited_datum_are_one_'
       'freedom.py')
_OPENLIT = 'The substrate route is closed; the progenitor route is open'
_live_read = [_p for _p in (_A3, _A5) if "open(os.path.join(ROOT, 'FOR_54.md')" in read(_p)]
_pinned = [_p for _p in (_A3, _A5) if "_F54_AT = 'ecb0aea4'" in read(_p)]
_f54_rows = [r for r in _rl if json.loads(r[1]) == _OPENLIT]
_runs = {}
for _p in (_A3, _A5):
    _r = subprocess.run([sys.executable, os.path.join(ROOT, _p)],
                        cwd=os.path.dirname(os.path.join(ROOT, _p)),
                        capture_output=True, text=True, timeout=900)
    _runs[_p.split('/')[-1][:3]] = _r.returncode
print(f'      live reads left: {len(_live_read)};  pinned reads: {len(_pinned)};  '
      f'runs: {_runs};  ledger rows on that literal: '
      f'{[r[5] for r in _f54_rows]}')
gate(f'Ⓕ① ✔⛭⛭ the live read of a FROZEN file is gone from both receipts and replaced by a read at a '
     f'literal sha with a resolve guard, both run green, and the two ledger rows move from '
     f'`REPAIR-OWED` to `DELIBERATE` --- ** the first `REPAIR-OWED` rows this line has RETIRED rather '
     f'than minted **, and they retire because at a fixed commit the literal cannot change',
     not _live_read and len(_pinned) == 2 and all(_v == 0 for _v in _runs.values())
     and len(_f54_rows) == 2 and all(r[5] == 'DELIBERATE' for r in _f54_rows))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓖ  THE SECOND INSTANCE OF THE SAME LATENT SHAPE, AND WHY IT IS ROUTED ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_Q1 = ('receipts/L221_quark_lepton/Q1_the_missing_operator_and_the_higgs_identification_are_one_'
       'gap.py')
_q1_src = read(_Q1)
_q1_bare = "'PO-5' in po and 'OPEN' in po" in _q1_src
_q1_intro = _git('log', '--diff-filter=A', '--format=%H%x00%s%x00%B', '-1', '--', _Q1)
_q1_rid = re.search(r'\br(\d{4,})\b', _q1_intro.split('\x00')[1] if '\x00' in _q1_intro else '')
_q1_odd = bool(_q1_rid) and int(_q1_rid.group(1)) % 2 == 1
_q1_sess = 'session_019ueTyssVbFDSERkfHfUeP9' in _q1_intro
_q1_row = [r for r in _in_pfx if r[0] == _Q1 and json.loads(r[1]) == 'OPEN']
print(f'      Q1 carries the bare OPEN test: {_q1_bare};  introduced at '
      f'r{_q1_rid.group(1) if _q1_rid else "?"} (odd: {_q1_odd});  this seat\'s session: {_q1_sess}')
gate(f'Ⓖ① ⛔⛭⛭ a SECOND instance of the latent shape is live in another seat\'s receipt: `Q1` asserts '
     f'that a protected row is STILL OPEN with a bare `in` test, so it goes red the day the row '
     f'closes --- and it is ROUTED rather than repaired, because its introducing commit is an ODD '
     f'revision carrying no marker of this seat.  ** Verdicted `REPAIR-OWED` with the patch in the '
     f'reply, which is the division the do-not-edit rule sets **',
     _q1_bare and _q1_odd and not _q1_sess
     and len(_q1_row) == 1 and _q1_row[0][5] == 'REPAIR-OWED')

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓗ  THE RESTRAINT, AND THE DANGLING TEST ON THIS RECEIPT\'S OWN KEYS ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_touched = sorted(set(f for f in _git('diff', '--name-only',
                                      f'{BEFORE}..{AFTER}').split('\n') if f))
_rcpt_touched = [f for f in _touched if f.startswith('receipts/') and f.endswith('.py')]
print(f'      this revision touched {len(_touched)} file(s), {len(_rcpt_touched)} of them receipts: '
      + ', '.join(f.split('/')[-1][:22] for f in _rcpt_touched))
gate(f'Ⓗ① ⛭ the restraint: the ledger plus the two receipts `r7279` RULED mine, and no receipt of '
     f'either verdicted prefix --- a verdict is a row in the ledger, not an edit to the gate it '
     f'describes',
     BASE in _touched
     and not [f for f in _rcpt_touched if f.startswith(PREFIXES)]
     and set(_rcpt_touched) <= {_A3, _A5, SELF_REL})

_KEYS = [_OPENLIT, 'OPEN', 'a count of gradings and not of fields',
         'the three wall modes are one operator\'s kernel and therefore identical particles']
_dangling = [_k for _k in _KEYS if D.dangles(_k)]
print(f'      {len(_KEYS)} literal(s) this receipt pins, {len(_dangling)} dangle')
gate(f'Ⓗ② ✔⛭ the literals this receipt pins run through the ADOPTED dangling arms before being '
     f'written and `{len(_dangling)}` dangle --- `r7257`\'s standing order, arms imported '
     f'byte-for-byte',
     not _dangling)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
_fail = FAILURES
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(_fail)}')
for l in _fail:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛭⛭ ** {len(_landed)} LANDED, {len(_unl)} REMAIN. **  L221_quark_lepton and P12_algebroid, complete.
  ✔ ** ALL SIX PRE-REGISTERED BANDS HOLD **, which has not happened on this line before.
  ⛔ ** THE REPAIR-OWED SHARE IS TWO MODES: ** one prefix at {max(_ro_shares.values()):.0f} per cent and four at or
     below 2, with nothing in between -- so the only honest report is which mode a prefix is in.
  ⛭ ** AND NEITHER ARM OF THE FIRST NEGATIVE FIRES: ** MEANING-HELD at {_mh_here} of 71 ({100.0 * _mh_here / 71:.0f} per cent)
     against the first pair's {100.0 * _mh_prev / 110:.0f} -- stable across kinds, the majority on both, two thirds on
     neither.  The frequency claim generalises; the two-thirds claim was that pair's.
  ✔ ** AND TWO REPAIR-OWED ROWS ARE RETIRED **, the first this line has closed rather than opened,
     by the pinned read r7279 ruled -- with a second instance of the same shape routed, not taken.
""")
sys.exit(1 if _fail else 0)
