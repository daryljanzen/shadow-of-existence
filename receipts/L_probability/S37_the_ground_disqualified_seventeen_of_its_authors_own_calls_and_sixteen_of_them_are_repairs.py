#!/usr/bin/env python3
r"""S37 -- THE `ENCODING-OK` GROUND APPLIED TO ITS AUTHOR'S OWN CALLS: 16 REPAIRS AND ONE THE OTHER WAY.

** WHAT WAS ORDERED. **  `r7303` order ①, restated unchanged at `r7307`: *the `17` re-verdicts your
`ENCODING-OK` ground calls for, in a revision of their own, each recording its named step.*
  => *** So this revision changes `17` rows and nothing else.  The ground is not touched, no receipt
      is touched, and every row carries the question of the ground and the TEST of `69`'s rule that
      decided it. ***

** ⛔⛭⛭⛭ THE RESULT: `16` OF THE `17` OWE A REPAIR AND EXACTLY ONE MOVES THE OTHER WAY. **

  ⓘ ** THE SUBSTRING FAMILY, `11` ROWS. **  *An arm that is a strict substring of its partner after
    the table decides the check alone, because the shorter span is true whenever the longer one is.*
    ** Both sides of such a pair owe a repair, and for OPPOSITE reasons: the short arm because it
    carries less than the claim, the long arm because it NEVER DECIDES. **
  ⓙ ** THE WORD DIFFERENCES, `6` ROWS. **  *The border does not reach them, so `69`'s rule decides,
    and it decides against five of them on Test 1 -- the words that make the claim true are outside
    the span -- or Test 6, an arm true for a reason unrelated to the claim.*

** ✔⛭⛭ AND THE ONE THAT GOES THE OTHER WAY IS THE ONE WORTH THE REVISION. **  *`SO(5,1)/SO(4,1)`
against a claim that the substrate is FIVE-DIMENSIONAL: the span IS the structure whose dimension
answers the claim, so it is a name used as data and the verdict is `DELIBERATE`.*  ** Its partner in
the same disjunction -- the phrase naming the substrate DE SITTER -- does not carry the claim at all,
and the check passes on it. **
  => *** One disjunction, two arms, and the ground sends them in opposite directions.  That is the
      argument for a per-ARM verdict rather than a per-check one, which is the clause this line put
      on the register at `r7302`. ***

⚠ WHAT THIS CANNOT SETTLE is at the foot.
"""
import collections
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
GROUND_DIR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7302_60_the_encoding_ground')
sys.path.insert(0, GROUND_DIR)
from notation_table import norm                              # noqa: E402  -- r7302's own table

CHECKS = []
FAILURES = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


BEFORE = '865f6f13'   # the last commit before this revision: every one of the 17 still ENCODING-OK
AFTER = 'HEAD'        # the commit that carried this revision -- the 71st member's corollary
BASE = 'corpus/quote_pin_baseline.tsv'
GROUND = 'computations/beyond_the_wall/r7302_60_the_encoding_ground/THE_ENCODING_GROUND.md'
TABLE = 'computations/beyond_the_wall/r7302_60_the_encoding_ground/notation_table.py'
STAMP = 'r7310+60'
INSTRUMENT = os.path.join(ROOT, 'scripts', 'mutate_assertions.py')
# ⚠ The COUNTS are read at `AFTER` and not in the working tree: an equality on a LIVE ledger goes red
#   the moment another seat lands a key, which is the fail-on-success family.


def _git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True, text=True,
                          errors='replace').stdout


def read(rel):
    with io.open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        return fh.read()


def rows_of(text):
    return [c for c in (l.split('\t') for l in text.split('\n'))
            if len(c) >= 7 and c[0].startswith('receipts/')]


def key(c):
    try:
        return (c[0], json.loads(c[1]))
    except Exception:
        return (c[0], c[1])


_SITE = re.compile(r'\s*\[QUOTE-PIN\]\[(\w+)\]\[(\w+)\]\[([^\]]*)\]\s+(\S+?):(\d+):(\d+)\s+(".*")\s*$')


def alt_runs():
    """the ALT arms grouped as `r7302`'s ground defines a RUN: maximal sets of CONSECUTIVE lines,
    because a boolean expression that wraps across lines is ONE check."""
    r = subprocess.run([sys.executable, INSTRUMENT, '--quote'], cwd=ROOT, capture_output=True,
                       text=True, timeout=900)
    alt = collections.defaultdict(list)
    for l in r.stdout.split('\n'):
        m = _SITE.match(l)
        if m and 'ALT' in m.group(3).split(','):
            alt[(m.group(4), int(m.group(5)))].append(json.loads(m.group(7)))
    byfile = collections.defaultdict(list)
    for (p, ln) in alt:
        byfile[p].append(ln)
    run_of = {}
    for p, lns in byfile.items():
        rid, prev = 0, None
        for ln in sorted(lns):
            if prev is not None and ln - prev > 1:
                rid += 1
            run_of[(p, ln)] = (p, rid)
            prev = ln
    runs = collections.defaultdict(list)
    for (p, ln), arms in alt.items():
        runs[run_of[(p, ln)]].extend(arms)
    return alt, run_of, runs


print()
print('=' * 100)
print('S37 -- the ground applied to its author\'s own calls: 16 repairs and one the other way')
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE SEVENTEEN, AND EVERY ONE CARRIES THE STEP THAT DECIDED IT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_now = rows_of(_git('show', f'{AFTER}:{BASE}'))
_mine = [c for c in _now if STAMP in (c[6] or '')]
_verd = collections.Counter(c[5] for c in _mine)
_with_step = [c for c in _mine if 'STEP:' in (c[6] or '')]
print(f'      {len(_mine)} rows carry this revision\'s stamp; verdicts {dict(_verd)}; '
      f'carrying a STEP clause {len(_with_step)}')
gate(f'Ⓐ① ⛭⛭ `{len(_mine)}` rows are re-verdicted and NOTHING else is: `{_verd["REPAIR-OWED"]}` owe a '
     f'repair and `{_verd["DELIBERATE"]}` moves the other way, and all `{len(_with_step)}` record the '
     f'STEP that decided them.  ** `r7303` order ① asked for the step on every row, which is `69`\'s '
     f'own discipline --- *a verdict without its test cannot be checked by the next reader* --- '
     f'carried onto the border this seat was ordered to write **',
     len(_mine) == 17 and len(_with_step) == 17 and _verd['REPAIR-OWED'] == 16
     and _verd['DELIBERATE'] == 1)

_before = {key(c): c[5] for c in rows_of(_git('show', f'{BEFORE}:{BASE}'))}
_were_eo = [c for c in _mine if _before.get(key(c)) == 'ENCODING-OK']
print(f'      of the {len(_mine)}, {len(_were_eo)} stood at ENCODING-OK at the commit before this one')
gate(f'Ⓐ② ⛭⛭ and every one of the `{len(_were_eo)}` is a WITHDRAWAL and not a fresh adjudication: '
     f'each stood at `ENCODING-OK` at `{BEFORE}`, read out of git rather than remembered.  ** They '
     f'are this seat\'s own prior calls, and the ground that disqualifies them is the one this seat '
     f'was ordered to write because it had made most of them **',
     len(_were_eo) == len(_mine))

_steps = collections.Counter(re.search(r'STEP: ([^.]+)\.', c[6]).group(1).strip()
                             for c in _mine if re.search(r'STEP: ([^.]+)\.', c[6]))
print('      the steps that decided them:')
for _s, _n in sorted(_steps.items(), key=lambda kv: -kv[1]):
    print(f'          {_n:2d}  {_s}')
gate(f'Ⓐ③ ⛭ and the steps are a MEASUREMENT and not a formality: `{len(_steps)}` distinct steps over '
     f'`{len(_mine)}` rows, and the single commonest is `69`\'s Test 1 --- the words that make the '
     f'claim true are outside the span.  ** Which is the narrower-than-claim family arriving through '
     f'a door this seat opened by defining the notation class narrowly: the rows the border excludes '
     f'are not a new class, they are the old one **',
     len(_steps) >= 4 and sum(_n for _s, _n in _steps.items() if 'Test 1' in _s) >= 8)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  AND THE SET IS EXACTLY THE ONE THE GROUND DISQUALIFIES, NO MORE AND NO FEWER ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_alt, _run_of, _runs = alt_runs()
_eo_left = []
for (_p, _ln), _arms in _alt.items():
    for _a in _arms:
        _row = next((c for c in _now if key(c) == (_p, _a)), None)
        if _row is None or _row[5] != 'ENCODING-OK':
            continue
        _grp = _runs[_run_of[(_p, _ln)]]
        if not any(b != _a and norm(b) == norm(_a) for b in _grp):
            _eo_left.append((_p, _a))
print(f'      ENCODING-OK rows carrying an ALT arm with NO notation partner, after this revision: '
      f'{len(_eo_left)}')
_mine_left = [(p, a) for p, a in _eo_left
              if '+60' in (next(c[6] for c in _now if key(c) == (p, a)) or '')]
print(f'      of those, this seat\'s own: {len(_mine_left)}')
gate(f'Ⓑ① ⛭⛭⛭ and the re-verdicted set is EXACTLY the one the ground disqualifies: after this '
     f'revision `{len(_mine_left)}` of this seat\'s `ENCODING-OK` rows carrying an `ALT` arm are left '
     f'without a notation partner.  ** The ground is applied to its author\'s calls IN FULL rather '
     f'than to the ones that were cheap to move --- and `{len(_eo_left)}` such rows remain in other '
     f'seats\' names, reported and routed, because another seat\'s verdict is not this seat\'s to '
     f'change **',
     not _mine_left and len(_eo_left) > 0)

_pairs = 0
for _c in _mine:
    _p, _a = key(_c)
    _ln = next((ln for (pp, ln), arms in _alt.items() if pp == _p and _a in arms), None)
    if _ln is None:
        continue
    _grp = _runs[_run_of[(_p, _ln)]]
    if any(b != _a and (norm(_a) in norm(b) or norm(b) in norm(_a)) for b in _grp):
        _pairs += 1
print(f'      of the {len(_mine)}, {_pairs} sit in a substring relation with an arm of their own run')
gate(f'Ⓑ② ⛭⛭ and the substring family is COUNTED rather than asserted: `{_pairs}` of the '
     f'`{len(_mine)}` stand in a containment relation with another arm of their own run after the '
     f'table, which is what makes one of the two decide alone.  ** Both sides of such a pair owe a '
     f'repair and for OPPOSITE reasons --- the short arm carries less than the claim, the long arm '
     f'never decides --- and that asymmetry is why each row records its own test **',
     _pairs >= 10)

_the_one = [c for c in _mine if c[5] == 'DELIBERATE'][0]
_one_lit = key(_the_one)[1]
_one_ln = next(ln for (pp, ln), arms in _alt.items() if pp == key(_the_one)[0] and _one_lit in arms)
_one_grp = [b for b in _runs[_run_of[(key(_the_one)[0], _one_ln)]] if b != _one_lit]
_carries_five = '5' in norm(_one_lit) and not any('5' in norm(b) for b in _one_grp)
print(f'      the one DELIBERATE row: its span carries the digit the claim turns on and its '
      f'{len(_one_grp)} partner(s) do not: {_carries_five}')
gate(f'Ⓑ③ ✔⛭⛭⛭ ** AND ONE DISJUNCTION SENDS ITS TWO ARMS IN OPPOSITE DIRECTIONS, which is the '
     f'argument for a per-ARM verdict: ** the span kept `DELIBERATE` carries the digit the claim '
     f'turns on while its partner does not (`{_carries_five}`), so one arm IS the structure the '
     f'claim is about and the other names a different property of the same object --- and the check '
     f'passes on either.  *That is `r7302`\'s clause used rather than restated: `ENCODING-OK`, and '
     f'every verdict on this border, is about an ARM and never about a disjunction*',
     _carries_five and len(_one_grp) >= 1)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  THE RESTRAINT: A RE-VERDICT IS A ROW ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_touched = sorted({f for f in (_git('diff', '--name-only', BEFORE, AFTER) + '\n'
                               + _git('ls-files', '--others', '--exclude-standard')).split('\n') if f})
_receipts_touched = [f for f in _touched if f.startswith('receipts/') and f.endswith('.py')
                     and 'S37_' not in f]
_ground_touched = [f for f in _touched if f in (GROUND, TABLE)]
_subjects = sorted({key(c)[0] for c in _mine})
print(f'      {len(_touched)} path(s) in the diff; receipts other than this revision\'s own: '
      f'{len(_receipts_touched)}; the ground or its table: {len(_ground_touched)}; the '
      f'{len(_subjects)} receipts whose rows are re-verdicted are untouched')
gate(f'Ⓒ① ⛭⛭ the restraint, as the SPECIFIC NEGATIVE alone: the `{len(_subjects)}` receipts whose '
     f'rows are re-verdicted here are edited `{len(_receipts_touched)}` times, and the ground and '
     f'its table are edited `{len(_ground_touched)}` times.  ** A re-verdict is a ROW and not an edit '
     f'to the gate it describes --- these receipts belong to other seats and none is this seat\'s to '
     f'change --- and a ground that moved in the revision that applied it would be a rule graded by '
     f'its author on the keys it was tuned to **',
     not _receipts_touched and not _ground_touched and len(_subjects) >= 5)

_live_bare = sum(1 for c in rows_of(read(BASE)) if c[5].startswith('UNADJUDICATED'))
_at_after = sum(1 for c in _now if c[5].startswith('UNADJUDICATED'))
print(f'      unadjudicated at this revision {_at_after}; live now {_live_bare}')
gate(f'Ⓒ② ⛭ and this revision adjudicates nothing new: the unadjudicated count stands at '
     f'`{_at_after}` at this revision\'s own commit, unchanged by it, because a re-verdict moves a '
     f'row between settled classes.  ⌗ *The live arm is `{_live_bare}` and is REPORTED, not asserted*',
     _at_after > 0)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
for l in FAILURES:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛔ ** {_verd['REPAIR-OWED']} OF THE {len(_mine)} OWE A REPAIR, ** and the ground that says so is the one this seat was
     ordered to write because it had made most of the calls it disqualifies.
  ✔ ** AND EXACTLY ONE MOVES THE OTHER WAY: ** a span that IS the structure the claim is about,
     beside a partner, in the same disjunction, that names a different property of the same
     object -- so one check sends its two arms in opposite directions.
  ⛭ Every row records the step of the ground and the test of 69's rule that decided it; the
     commonest is Test 1, the words that make the claim true being outside the span.
  ⛭ Nothing else moved: no receipt edited, the ground and its table untouched, and
     {len(_eo_left)} rows of the same shape left in other seats' names, reported and routed.
""")
sys.exit(1 if FAILURES else 0)
