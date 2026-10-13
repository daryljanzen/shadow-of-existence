#!/usr/bin/env python3
r"""S34 -- `r7295`'s order: the blind read scored, the primary `38` landed, and `L811` closed.

COMPUTES: nothing the papers quote.  This receipt reports a BLIND second read of one prefix, the
adjudication of `38` primary keys, and the closing of a prefix whose shares are reported rather than
registered.

** ✔⛭ THE MERGE CAME FIRST, WHICH IS THE ONE-LINE FIX `r7295` ORDERED. **  *`r7295` voided the
previous registration because its four prefixes were already verdicted on the trunk --- `UNREAD` is a
property of the COPY and not of the key --- and the fix is to fetch and merge BEFORE the
pre-registration push.  **The trunk's tip is an ancestor of this revision's registration commit, which
this receipt checks rather than asserts.***

** ⛔⛭⛭⛭ THE BLIND READ SCORES `1` OF `7`, BELOW THE REGISTERED `2`-`4`, SO THE BOTTOM REFUTATION
CONDITION FIRED: THE RULE IS ANTI-CORRELATED AND I MIS-STATED MY OWN BASE RATES. **  *With three
verdict classes in play, `1` of `7` is at or below chance.*
  ⌈ ⇒ ***AND THE DIRECTION IS THE FINDING, NOT THE SCORE: the SHORT keys were `DELIBERATE` and the
    MEDIUM ones `REPAIR-OWED` --- the opposite of my rule at BOTH ends.*** *A one-character span is the
    most `DELIBERATE` thing in the ledger, because the character IS the claim; a ten-character
    identifier is a PROXY, because it stands for a proposition it cannot carry.*
  ⌊ ⛔⛭⛭ ***AND THE REASON IS A BASE RATE TAKEN FROM THE WRONG POPULATION: mine came from a batch
    whose short tokens were COMMON WORDS AND STEMS, and I applied it to a batch whose short tokens are
    UNICODE CHARACTERS AND IDENTIFIERS.*** ⌗ *Which is `66`'s `80`th member --- an agreement figure
    from one batch is a sample and not a property --- with the same shape one step in: **a BASE RATE
    from one batch is a sample and not a property either.**  And it is the staleness defect once more:
    `r7295` had my registration describing my branch instead of the trunk; this has my base rate
    describing one population instead of the one in front of me.*

** ✔⛭ THE PRIMARY `38` LANDED, AND THE BANDS ARE NO LONGER ALL WRONG IN ONE DIRECTION. **  *`11` of
`14` held; `3` missed, **two BELOW and one ABOVE** --- against `r7296`'s four of eight where every miss
was above.* ⇒ *The cause is stated and was acted on: I raised the `MEANING-HELD` tops because that is
where `r7296` missed, and the misses now fall on both sides.*  ⌗ *And the one sharp registration --- the
subject rule's `SENTENCE`-tier reach per prefix --- is exact a THIRD time running.*

** ⛭ `L811` IS CLOSED with its shares reported and not registered, as ordered. **  *The backlog goes
`89` to `42` on this revision; it read `321` before the merge, which is the `242`-key staleness `r7295`
measured.*

⌗ *Sources: `r7295`'s order and its stride table; the registration read at the commit that pushed it;
the trunk's tip shown to be an ancestor of that commit; `BLIND_READ.tsv` in the four-column shape
ordered and NOT reconciled; and the ledger before and after, both at pinned commits.*
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

CHECKS = []
FAILURES = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


TRUNK = 'c33da8ff'    # origin/main's tip when this revision began
MERGE = '653cc50c'    # the merge of the trunk into this branch, BEFORE the registration
PREG = 'd07ee42b'     # the commit that PUSHED the registration, after the merge
AFTER = 'f5d6155d'    # the commit that carried this revision's verdicts -- the 71st member's corollary
# ⚠ The COUNTS below are read at `AFTER` and not in the working tree: an equality on a LIVE ledger
#   goes red the moment another seat lands a key, which is the fail-on-success family.  The ONE live
#   read kept is the backlog, and it is asserted MONOTONE rather than exact.
BASE = 'corpus/quote_pin_baseline.tsv'
PRED = 'computations/beyond_the_wall/r7300_60_the_blind_read/PREDICTION.md'
BLIND = 'computations/beyond_the_wall/r7300_60_the_blind_read/BLIND_READ.tsv'
PRIM = ['L256_the_band_taken', 'L801_nonlinear_shear_freedom',
        'L276_the_representation_theory_probe', 'L277_the_unclaimed_surface',
        'L809_one_loop_quartic', 'L551_register_integrity', 'L230_computes_convention']
def _git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True, text=True,
                          errors='replace').stdout


def read(rel):
    with io.open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        return fh.read()


def rows_of(text):
    return [c for c in (l.split('\t') for l in text.split('\n'))
            if len(c) >= 7 and c[0].startswith('receipts/')]


def anc(a, b):
    return subprocess.run(['git', 'merge-base', '--is-ancestor', a, b], cwd=ROOT,
                          capture_output=True).returncode == 0


print()
print('=' * 100)
print('S34 -- the blind read scored, the primary 38 landed, L811 closed')
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE MERGE CAME FIRST, WHICH IS THE FIX THE ORDER NAMED ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_trunk_in_merge = anc(TRUNK, MERGE)
_merge_before_preg = anc(MERGE, PREG)
_preg_in_head = anc(PREG, 'HEAD')
print(f'      trunk tip in the merge: {_trunk_in_merge}; merge before the registration: '
      f'{_merge_before_preg}; registration in HEAD: {_preg_in_head}')
gate(f'Ⓐ① ✔⛭⛭ the ordered fix is CHECKED and not asserted: the trunk\'s tip is an ancestor of the '
     f'merge (`{_trunk_in_merge}`), the merge is an ancestor of the registration commit '
     f'(`{_merge_before_preg}`), and the registration is in `HEAD` (`{_preg_in_head}`).  ** `r7295`: '
     f'a pre-registration is a claim about what is OPEN, and what is open is a TRUNK fact.  The '
     f'ordering is now a property of the history rather than a promise **',
     _trunk_in_merge and _merge_before_preg and _preg_in_head)

_pred = _git('show', f'{PREG}:{PRED}')
_rule_rows = re.findall(r'\|\s*`(SENTENCE|TOKEN)`\s*\|([^|]*?`(\d+)`[^|]*)\|\s*`([A-Z-]+)`\s*\|', _pred)
_rule = {(t, 'under' in cell.lower()): (int(n), v) for t, cell, n, v in _rule_rows}
_bands = {m[0]: ((int(m[2]), int(m[3])), (int(m[4]), int(m[5]))) for m in re.findall(
    r'\|\s*`(L\d+_[a-z0-9_]+)`\s*\|\s*`(\d+)`\s*\|[^|]*\|[^|]*\|'
    r'\s*`(\d+)`[\u2013-]`(\d+)`\s*\|\s*`(\d+)`[\u2013-]`(\d+)`\s*\|', _pred)}
_seven = re.findall(r'\|\s*`([1-7])`\s*\|\s*`(SENTENCE|TOKEN)`\s*\|\s*`(\d+)`\s*\|\s*\*\*`([A-Z-]+)`\*\*',
                    _pred)
_band = re.search(r'Registered: `(\d)` to `(\d)` of `7` agree', _pred)
_rule_tiers = sorted({t for t, _, _, _ in _rule_rows})
_rule_cuts = sorted({int(n) for _, _, n, _ in _rule_rows})
_rule_verdicts = {v for _, _, _, v in _rule_rows}
_seven_verdicts = {r[3] for r in _seven}
print(f'      the registration carries {len(_rule_rows)} rule rows over tiers {_rule_tiers} with '
      f'cut-offs {_rule_cuts}, {len(_seven)} fixed verdicts, and an agreement band of '
      f'{_band.group(1)}-{_band.group(2)}' if _band else '      no band found')
gate(f'Ⓐ② ⛔⛭⛭ and the blind read\'s RULE and its SEVEN VERDICTS are read out of that commit rather '
     f'than restated here: `{len(_rule_rows)}` rule rows --- two tiers `{_rule_tiers}` cut at '
     f'`{_rule_cuts}` characters, one arm each --- `{len(_seven)}` verdicts fixed by key, '
     f'`{len(_bands)}` prefix bands, and an agreement band of '
     f'`{_band.group(1)}`-`{_band.group(2)}` of `7`, with the rule\'s verdict classes and the seven '
     f'fixed ones the SAME set (`{sorted(_rule_verdicts) == sorted(_seven_verdicts)}`).  ** All of it '
     f'pushed before the first column of the other seat\'s read was looked at, which is what makes '
     f'the score below a measurement **',
     len(_rule_rows) == 4 and len(_rule_tiers) == 2 and len(_rule_cuts) == 2 and len(_rule) == 4
     and len(_seven) == 7 and _rule_verdicts == _seven_verdicts and len(_bands) == 7
     and _band is not None)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  THE BLIND READ: 1 OF 7, AND THE DIRECTION IS THE FINDING ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_bl = [l.split('\t') for l in read(BLIND).split('\n') if l.strip() and not l.startswith('#')]
_agree = [r for r in _bl if r[2] == r[3]]
_lo, _hi = int(_band.group(1)), int(_band.group(2))
print(f'      {len(_bl)} keys, agreement {len(_agree)}; registered band {_lo}-{_hi}')
gate(f'Ⓑ① ⛔⛭⛭⛭ ** THE BLIND READ SCORES `{len(_agree)}` OF `{len(_bl)}`, BELOW THE REGISTERED '
     f'`{_lo}`-`{_hi}`, SO THE BOTTOM REFUTATION CONDITION FIRED: ** the registration said `at or '
     f'below 1, the rule is anti-correlated and I have mis-stated my own base rates`.  ** With three '
     f'verdict classes in play, `{len(_agree)}` of `{len(_bl)}` is at or below chance --- a '
     f'length-only rule is not a weak discriminator, it is a wrong one **',
     len(_agree) <= 1 and len(_bl) == 7)

_short = [r for r in _bl if len(r[1]) < 6]
_mid = [r for r in _bl if 6 <= len(r[1]) < 20]
_short_del = [r for r in _short if r[2] == 'DELIBERATE']
_mid_ro = [r for r in _mid if r[2] == 'REPAIR-OWED']
print(f'      first-read verdicts by length: of {len(_short)} SHORTEST keys {len(_short_del)} are '
      f'DELIBERATE; of {len(_mid)} MEDIUM keys {len(_mid_ro)} are REPAIR-OWED')
gate(f'Ⓑ② ⛔⛭⛭⛭ and the DIRECTION is the finding, not the score: of the `{len(_short)}` shortest keys '
     f'`{len(_short_del)}` are `DELIBERATE` in the first read, and of the `{len(_mid)}` medium ones '
     f'`{len(_mid_ro)}` are `REPAIR-OWED` --- ** the opposite of my rule at BOTH ends. ** *A '
     f'one-character span is the most `DELIBERATE` thing in the ledger because the character IS the '
     f'claim; a ten-character identifier is a `PROXY` because it stands for a proposition it cannot '
     f'carry.*',
     len(_short_del) == len(_short) and len(_mid_ro) == len(_mid) and len(_short) >= 2)

_tier_of = {(c[0], c[1]): c[3] for c in rows_of(_git('show', f'{AFTER}:{BASE}'))}
_applied = []
for _r in _bl:
    _ge_arm = _rule[(_tier_of.get((_r[0], _r[1])), False)]
    _under_arm = _rule[(_tier_of.get((_r[0], _r[1])), True)]
    _applied.append(_ge_arm[1] if len(_r[1]) >= _ge_arm[0] else _under_arm[1])
_unmoved = sum(1 for _r, _v in zip(_bl, _applied) if _r[3] == _v)
_four_col = all(len(_r) == 4 for _r in _bl)
_disagree = sum(1 for _r in _bl if _r[2] != _r[3])
print(f'      four columns: {_four_col}; my column still the registered rule applied: {_unmoved} of '
      f'{len(_bl)}; the two columns disagree on {_disagree}')
gate(f'Ⓑ③ ✔⛭⛭ and NOT RECONCILING is asserted as the thing it is FOR rather than as the header line '
     f'that declares it: the file is the four-column shape ordered (`{_four_col}`), the two columns '
     f'disagree on `{_disagree}` of `{len(_bl)}`, and every one of `{_unmoved}` of `{len(_bl)}` second '
     f'verdicts is still EXACTLY the registered rule applied to that row\'s tier and length --- so '
     f'not one of them moved toward the other seat\'s after the columns were put side by side.  ** A '
     f'disagreement between seats is not a seat\'s to settle, and the check for that is that the '
     f'numbers did not move, not that a line says they did not **',
     _four_col and _unmoved == len(_bl) and _disagree == len(_bl) - 1)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  THE PRIMARY 38, AND THE BANDS ARE NO LONGER WRONG IN ONE DIRECTION ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_all = rows_of(_git('show', f'{AFTER}:{BASE}'))
_mine = [c for c in _all if 'r7300+60, the r7295 primary' in (c[6] or '')]
_by = collections.defaultdict(list)
for _c in _mine:
    _by[_c[0].split('/')[1]].append(_c)
print(f'      {len(_mine)} primary keys verdicted across {len(_by)} prefixes '
      f'(the order listed 37, the ledger carries 38)')
gate(f'Ⓒ① ⛭⛭ `{len(_mine)}` primary keys landed across `{len(_by)}` prefixes --- and the count is '
     f'`38` where the order lists `37`, because one prefix carries seven bare keys rather than six.  '
     f'** Reported in the registration rather than reconciled quietly, and it is one key **',
     len(_mine) == 38 and len(_by) == 7)

_score = []
for _p, (_rb, _mb) in _bands.items():
    _rs = _by[_p]
    _t = collections.Counter(c[5] for c in _rs)
    for _n, _v, _b in (('RO', 100.0 * _t['REPAIR-OWED'] / len(_rs), _rb),
                       ('MH', 100.0 * _t['MEANING-HELD'] / len(_rs), _mb)):
        _in = _b[0] <= _v <= _b[1]
        _score.append((_p, _n, _v, _b, _in))
        print(f'      {_p[:36]:36} {_n}  {_v:5.1f}%  band {_b[0]}-{_b[1]}  '
              f'{"in" if _in else ("ABOVE" if _v > _b[1] else "BELOW")}')
_missed = [s for s in _score if not s[4]]
_below = [s for s in _missed if s[2] < s[3][0]]
_above = [s for s in _missed if s[2] > s[3][1]]
gate(f'Ⓒ② ✔⛭⛭ `{len(_score) - len(_missed)}` of `{len(_score)}` bands HELD, and the `{len(_missed)}` '
     f'misses are NO LONGER ALL IN ONE DIRECTION: `{len(_below)}` below and `{len(_above)}` above, '
     f'against `r7296`\'s four of eight where every miss was ABOVE.  ** The cause was stated and acted '
     f'on --- the `MEANING-HELD` tops were raised because that is where the previous registration '
     f'missed --- so this is a correction with a measured reason rather than a new guess.  And the '
     f'bands scored are READ OUT of the registration commit, not retyped here **',
     len(_missed) <= 4 and _below and _above and len(_bands) == len(_by))

_ceil = True
for _p, _rs in _by.items():
    _sent = sum(1 for c in _rs if c[3] == 'SENTENCE')
    _sub = sum(1 for c in _rs if c[5] == 'REPAIR-OWED'
               and re.search(r'DANGLING|OBJECT-DANGLING|PRONOUN', c[6] or '', re.I))
    _ceil = _ceil and _sub <= _sent
gate(f'Ⓒ③ ✔⛭ and the one SHARP registration holds again --- the subject rule grounds no more '
     f'`REPAIR-OWED` rows than a prefix has `SENTENCE`-tier keys, in every one of the `{len(_by)}` '
     f'(`{_ceil}`).  ** Exact a THIRD time running, and it is on the file because `r7290`\'s tier '
     f'arithmetic was wrong by two in each direction **',
     _ceil)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓓ  L811 CLOSED, AND THE BACKLOG AGAINST THE STALE COPY ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_l811 = [c for c in _all if c[0].startswith('receipts/L811')]
_l811_open = [c for c in _l811 if c[5].startswith('UNADJUDICATED')]
_l811_mine = [c for c in _l811 if 'r7300+60, L811' in (c[6] or '')]
_l811_declared = bool(re.search(r'(?m)^#+ .*`L811`', _pred))
_l811_banded = [_p for _p in _bands if _p.startswith('L811')]
print(f'      L811: {len(_l811)} keys, {len(_l811_open)} still open, {len(_l811_mine)} closed here; '
      f'declared in a section of its own: {_l811_declared}; banded prefixes naming it: '
      f'{len(_l811_banded)}')
gate(f'Ⓓ① ⛭⛭ `L811` is CLOSED --- `{len(_l811_mine)}` keys verdicted here, `{len(_l811_open)}` left '
     f'open --- and its shares being REPORTED rather than registered is asserted as the ABSENCE it '
     f'is: the registration carries a section of its own for it (`{_l811_declared}`) and `0` of the '
     f'`{len(_bands)}` banded prefixes is `L811` (`{len(_l811_banded)}`).  ** `r7295` confirmed that '
     f'was the right call --- its literals were read while surveying the claim, and surveying what '
     f'you claimed is already reading it --- and the declaration belongs in the registration rather '
     f'than in a receipt, where it would read as an excuse **',
     len(_l811_open) == 0 and len(_l811_mine) == 9 and _l811_declared and not _l811_banded)

_un_merge = sum(1 for c in rows_of(_git('show', f'{MERGE}:{BASE}'))
                if c[5].startswith('UNADJUDICATED'))
_un_pre = sum(1 for c in rows_of(_git('show', f'{PREG}^:{BASE}'))
              if c[5].startswith('UNADJUDICATED'))
_un_now = sum(1 for c in rows_of(read(BASE)) if c[5].startswith('UNADJUDICATED'))
print(f'      backlog at the merge {_un_merge}; now {_un_now}')
gate(f'Ⓓ② ⛭⛭ `{_un_merge - _un_now}` landed this revision: the backlog goes `{_un_merge}` to '
     f'`{_un_now}`.  ** And the merge itself took it from `321` to `{_un_merge}` without a key being '
     f'read --- the `242`-key staleness `r7295` measured, which is the same defect as the base rate '
     f'above: a number true of the copy and not of the thing ** --- and this is the ONE live read '
     f'in the receipt, asserted MONOTONE rather than exact, because every other count here is an '
     f'equality on a set another seat can move and is pinned at `AFTER` instead',
     _un_now <= _un_merge and _un_now <= 45)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓔ  THE RESTRAINT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_subjects = sorted({c[0] for c in _mine} | {c[0] for c in _l811_mine}
                   | {c[0] for c in _all if c[0].startswith('receipts/L270')})
#: ⛔⛭⛭ r7314+60: THE RANGE WAS OPEN AND IT WENT RED THREE REVISIONS LATER.  `PREG` against the
#:   WORKING TREE is `PREG..whatever exists now`, so every later revision of this line enlarges the
#:   diff this gate reads, and one of the subject receipts eventually appears in it.  ** The claim is
#:   about what THIS revision edited, which is a closed range. **
#:   ⇒ *`66` repaired exactly this in `S31` at `r7295` (`PREG..AFTER`) and this line repaired it in
#:   `S32` at `r7304`.  This is the same shape a third time, in the gate that states the restraint
#:   against it -- and it is the fourth range in this line's own work to be closed for this reason.*
_touched = sorted({f for f in _git('diff', '--name-only', PREG, AFTER).split('\n') if f})
_touched_subjects = [f for f in _touched if f in _subjects]
print(f'      the rows verdicted here live in {len(_subjects)} receipts; this revision edited '
      f'{len(_touched_subjects)} of them')
gate(f'Ⓔ① ⛭⛭ the restraint, as the SPECIFIC NEGATIVE alone: the rows verdicted or double-read here '
     f'live in `{len(_subjects)}` receipts and this revision edited `{len(_touched_subjects)}` of '
     f'them, while the ledger IS in the diff --- because a verdict is a row and not an edit to the '
     f'gate it describes.  ** `L256`\'s receipt is on the do-not-edit list and is verdicted without '
     f'being touched, which is the distinction that list is for **',
     BASE in _touched and not _touched_subjects)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
for l in FAILURES:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ✔ ** THE MERGE CAME FIRST ** -- checked against the history, not promised: the trunk's tip is an
     ancestor of the merge, and the merge of the registration commit. That is r7295's one-line fix.
  ⛔ ** THE BLIND READ SCORES {len(_agree)} OF {len(_bl)}, BELOW THE REGISTERED {_lo}-{_hi}: the bottom refutation
     condition fired, and at or below chance with three classes in play. **
     And the DIRECTION is the finding: the shortest keys are DELIBERATE and the medium ones
     REPAIR-OWED -- the opposite of my rule at both ends.
  ⛔ ** A BASE RATE FROM ONE BATCH IS A SAMPLE AND NOT A PROPERTY. ** Mine came from a batch whose
     short tokens were common words and stems; I applied it where they are characters and
     identifiers. Same shape as the staleness that voided the last registration, one step in.
  ✔ ** {len(_score) - len(_missed)} of {len(_score)} bands held, and the {len(_missed)} misses are no longer all in one direction. **
     The MEANING-HELD tops were raised because that is where the last ones missed.
  ⛭ L811 closed. {_un_merge - _un_now} landed, {_un_now} remain.
""")
sys.exit(1 if FAILURES else 0)
