#!/usr/bin/env python3
r"""S35 -- THE `ENCODING-OK` GROUND, ORDERED AT `r7299` ON A COUNT, AND IT COSTS ITS AUTHOR 17 OF 27.

** WHAT WAS ORDERED. **  `69` filed `G1`-`G7` -- seven grounds for `REPAIR-OWED` written as tests over
the span and its check -- and left the `ENCODING-OK` border open in terms: *"I have made no call on
that border this campaign, so I have no ground to offer.  It needs the seats that did."*  `r7299`
counted who did: `ENCODING-OK` calls across the pooled set, `60` `12`, `69` `4`, `cc66` `0`, `70` `0`.
  => *** So the border is ordered to this seat, and the order names the four cells it must decide. ***

** WHAT IS FILED. **  `THE_ENCODING_GROUND.md` beside `notation_table.py`: the ground in `69`'s form,
and the table as CODE rather than as prose.  *A ground for a NOTATION class cannot be three readers
agreeing that two strings look like the same thing -- that is the judgement the ground exists to
remove.*  ** So two spellings are one spelling iff a CLOSED, ORDERED list of rewrites takes both to
the same string, and the verdict records the STEP it needed. **

** ⛔⛭⛭⛭ AND THE FINDING IS WHAT IT COSTS THE SEAT THAT WROTE IT. **  *Applied to every `ENCODING-OK`
row in the ledger carrying an `ALT` arm, the ground admits a MINORITY.*  ** Of this seat's own `27`:
`10` are notation, `11` are the substring family, `6` are word differences -- `17` of `27` fall
outside the class its author was ordered to define. **
  => *** The largest class outside it is the one the border was placed to exclude: an arm that is a
      PREFIX of another arm.  A pin accepting `exact for arbitrary` beside `EXACT for arbitrary
      $m(r)$` is not accepting two spellings; it is accepting one spelling and a prefix of it, and the
      prefix is the whole check. ***

** ⛔⛭⛭ AND THREE OF THE FOUR ORDERED CELLS GO THIS SEAT'S WAY AND THE FOURTH AGAINST IT. **  *The
three spellings of one subscript are `ENCODING-OK` at the `greek` and `braces` steps.  The three-way
alternation is NOT: no rewrite brings `analyticalindex`, `gradedindex` and `bulkindex` together, and
none should, because the difference between them is VOCABULARY.*  ** `69`'s `DELIBERATE` stands and
this seat's `ENCODING-OK` on that cell is withdrawn. **

** ⌗ AND NOTHING IS RE-VERDICTED ON THIS PUSH. **  *A ground and its re-verdicts in one revision is a
rule graded by its author on the keys it was derived from -- `66`'s own objection to `70` scoring a
rule before its score exists.*  ** The list is ROUTED with its per-seat split instead. **

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
from notation_table import norm, needed_step, STEPS          # noqa: E402  -- this revision's own table

CHECKS = []
FAILURES = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


BEFORE = '2fcc95a7'   # this branch's tip before this revision
AFTER = 'd9a899ca'   # the commit that carried this revision -- the 71st member's corollary
BASE = 'corpus/quote_pin_baseline.tsv'
GROUND = 'computations/beyond_the_wall/r7302_60_the_encoding_ground/THE_ENCODING_GROUND.md'
INSTRUMENT = os.path.join(ROOT, 'scripts', 'mutate_assertions.py')
# ⚠ The COUNTS below are read at `AFTER` and not in the working tree: an equality on a LIVE ledger
#   goes red the moment another seat lands a key, which is the fail-on-success family.


def _git(*a):
    return subprocess.run(['git'] + list(a), cwd=ROOT, capture_output=True, text=True,
                          errors='replace').stdout


def read(rel):
    with io.open(os.path.join(ROOT, rel), encoding='utf-8') as fh:
        return fh.read()


def rows_of(text):
    return [c for c in (l.split('\t') for l in text.split('\n'))
            if len(c) >= 7 and c[0].startswith('receipts/')]


_SITE = re.compile(r'\s*\[QUOTE-PIN\]\[(\w+)\]\[(\w+)\]\[([^\]]*)\]\s+(\S+?):(\d+):(\d+)\s+(".*")\s*$')


def alt_sites():
    # ⌗ r7339+70 (ported, for 60 to confirm or replace): the arms are read at AFTER, the tree whose
    #   verdicts they are joined to -- live, a later repair stride deletes arms (dead disjuncts) and
    #   the minority this receipt reported moves under it (r7335's three-way rule).
    import tempfile
    wt = tempfile.mkdtemp(prefix='S35_after_')
    subprocess.run(['git', 'worktree', 'add', '--detach', '-f', wt, AFTER], cwd=ROOT,
                   capture_output=True)
    try:
        r = subprocess.run([sys.executable, os.path.join(wt, 'scripts', 'mutate_assertions.py'),
                            '--quote'], cwd=wt, capture_output=True, text=True, timeout=900)
    finally:
        subprocess.run(['git', 'worktree', 'remove', '--force', wt], cwd=ROOT, capture_output=True)
    out = collections.defaultdict(list)
    for l in r.stdout.split('\n'):
        m = _SITE.match(l)
        if m and 'ALT' in m.group(3).split(','):
            out[(m.group(4), int(m.group(5)))].append(json.loads(m.group(7)))
    return out


def runs_of(alt):
    """a RUN is the arms on a maximal set of CONSECUTIVE lines: a boolean expression that wraps
    across lines is ONE check, and the line number alone does not say so."""
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
    return run_of, runs


print()
print('=' * 100)
print('S35 -- the ENCODING-OK ground, and it puts 17 of its author\'s own 27 calls outside the class')
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE TABLE IS CLOSED, ORDERED, AND A REFINEMENT CHAIN ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
#: ⛭⛭ The property that makes a STEP citable: once two arms agree at a step, every later step keeps
#:   them agreeing, because each step applies the same function to equal inputs.  So `needed_step`
#:   returns a FIRST step and not one of several, and two readers citing different steps for one pair
#:   is a contradiction rather than a matter of taste.
_PROBE = ['\\nu_R', 'nu_R', 'nu_{R}', 'M\\left(1+\\cos z\\right)', 'M(1+\\cos z)', '1+\\cos z',
          'ZSTART=3e7', 'ZSTART=3.0e7', "ZSTART', '3e7", 'analytical index', 'graded index',
          'bulk index', 'HALF ONE', 'HALF ①', 'decouple', 'decoupling', 'de Sitter', 'deSitter',
          '$A_{2}$', '$A_2$', 'exact for arbitrary', 'EXACT for arbitrary $m(r)$']
_mono = True
for _i, _a in enumerate(_PROBE):
    for _b in _PROBE[_i + 1:]:
        _agreed = False
        for _s in STEPS:
            if norm(_a, _s) == norm(_b, _s):
                _agreed = True
            elif _agreed:
                _mono = False
print(f'      {len(STEPS)} named steps; refinement holds over all '
      f'{len(_PROBE) * (len(_PROBE) - 1) // 2} probe pairs: {_mono}')
gate(f'Ⓐ① ✔⛭⛭ the table is CLOSED and ORDERED --- `{len(STEPS)}` named steps --- and it is a '
     f'REFINEMENT CHAIN (`{_mono}`): once two arms agree at a step, no later step separates them, '
     f'over every one of `{len(_PROBE) * (len(_PROBE) - 1) // 2}` probe pairs.  ** That is what makes '
     f'the STEP citable: `needed_step` returns a FIRST step and not one of several, so two readers '
     f'citing different steps for one pair contradict each other instead of differing in taste **',
     _mono and isinstance(STEPS, tuple) and len(STEPS) >= 10)

#: ⛭⛭ The four ordered cells are read OUT of the ground document rather than restated here -- the
#:   r7300 form: a receipt that retypes the thing it reports is scoring its own copy.
_ground = read(GROUND)
_cells = re.findall(r'\|\s*`([^`]+)`\s*\|\s*\*\*(?:`([A-Z-]+)`|NOT `([A-Z-]+)`)\*\*\s*\|\s*`?(\w+)`?',
                    _ground)
_cell_verdict = {c[0]: ('ENCODING-OK' if c[1] else 'NOT-ENCODING-OK', c[3]) for c in _cells}
print(f'      the ground answers {len(_cell_verdict)} ordered cells: '
      f'{[(k[:28], v[0]) for k, v in _cell_verdict.items()]}')
gate(f'Ⓐ② ⛭⛭ and the `{len(_cell_verdict)}` cells the order named are read OUT of the ground '
     f'document rather than restated in this receipt, each with the STEP it needed: '
     f'`{sorted({v[1] for v in _cell_verdict.values()})}`.  ** A receipt that retypes the thing it '
     f'reports is scoring its own copy, which is `r7300`\'s form carried forward **',
     len(_cell_verdict) == 4 and sum(1 for v in _cell_verdict.values()
                                     if v[0] == 'ENCODING-OK') == 3)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  THE FOUR ORDERED CELLS, ANSWERED BY RUNNING THE TABLE ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_nu = [r'\nu_R', 'nu_R', 'nu_{R}']
_nu_ok = all(norm(a) == norm(_nu[0]) for a in _nu)
_nu_steps = {a: needed_step(a, 'nu_R') for a in _nu if a != 'nu_R'}
_idx = ['analytical index', 'graded index', 'bulk index']
_idx_meet = len({norm(a) for a in _idx}) == 1
print(f'      the three spellings collapse: {_nu_ok}  steps {_nu_steps}')
print(f'      the three index branches collapse: {_idx_meet}  '
      f'{sorted({norm(a) for a in _idx})}')
gate(f'Ⓑ① ⛭⛭⛭ three of the four ordered cells go this seat\'s way, and they are DECIDED rather than '
     f'asserted: the three spellings of one subscript all normalise alike (`{_nu_ok}`), at the '
     f'`greek` and `braces` steps.  ** One symbol written as a command and as letters, and one '
     f'subscript in two brace styles --- the file\'s typography is not a fact about the corpus **',
     _nu_ok and set(_nu_steps.values()) == {'greek', 'braces'})

gate(f'Ⓑ② ⛔⛭⛭⛭ ** AND THE FOURTH GOES AGAINST IT: the three-way alternation is NOT `ENCODING-OK` '
     f'(`{_idx_meet}` --- the branches never meet), so `69`\'s `DELIBERATE` stands and this seat\'s '
     f'call on it is WITHDRAWN. ** *The three are NAMES the paper uses for one quantity, not '
     f'spellings of one name: no rewrite in the table brings `{norm(_idx[0])}`, `{norm(_idx[1])}` and '
     f'`{norm(_idx[2])}` together, and none should, because the difference between them is '
     f'VOCABULARY --- and a ground that decided it would be measuring the reader rather than the span*',
     not _idx_meet and len({norm(a) for a in _idx}) == 3)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  AND APPLIED TO THE LEDGER, THE GROUND ADMITS A MINORITY OF ITS AUTHOR\'S OWN CALLS ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_alt = alt_sites()
_run_of, _runs = runs_of(_alt)
_led = rows_of(_git('show', f'{AFTER}:{BASE}'))
_verdict = {}
_why = {}
for _c in _led:
    try:
        _verdict[(_c[0], json.loads(_c[1]))] = _c[5]
        _why[(_c[0], json.loads(_c[1]))] = _c[6]
    except Exception:
        pass


def _seat(p, a):
    w = _why.get((p, a), '')
    for s in ('+60', '+69', '+70', 'cc66', '+66'):
        if s in w:
            return s.lstrip('+')
    return '?'


_eo = [(p, ln, a) for (p, ln), arms in _alt.items() for a in arms
       if _verdict.get((p, a)) == 'ENCODING-OK']
_notation, _substring, _words = [], [], []
_stepuse = collections.Counter()
for _p, _ln, _a in _eo:
    _grp = _runs[_run_of[(_p, _ln)]]
    _na = norm(_a)
    _partner = [b for b in _grp if b != _a and norm(b) == _na]
    if _partner:
        _notation.append((_p, _ln, _a))
        _stepuse[needed_step(_a, _partner[0])] += 1
    elif any(b != _a and (_na in norm(b) or norm(b) in _na) for b in _grp):
        _substring.append((_p, _ln, _a))
    else:
        _words.append((_p, _ln, _a))
print(f'      {len(_eo)} ENCODING-OK rows carry an ALT arm: {len(_notation)} notation, '
      f'{len(_substring)} substring, {len(_words)} word differences')
gate(f'Ⓒ① ⛔⛭⛭⛭ ** THE GROUND ADMITS A MINORITY: of the `{len(_eo)}` `ENCODING-OK` rows carrying an '
     f'`ALT` arm, `{len(_notation)}` are notation, `{len(_substring)}` are the SUBSTRING family and '
     f'`{len(_words)}` differ by WORDS. ** *The largest class outside the border is the one the border '
     f'was placed to exclude --- an arm that is a PREFIX of another arm, where the prefix is the whole '
     f'check and the longer arm decides nothing*',
     len(_eo) >= 60 and len(_notation) < len(_substring) + len(_words)
     and len(_substring) > len(_words))

_mine = collections.Counter()
for _nm, _lst in (('notation', _notation), ('substring', _substring), ('words', _words)):
    for _p, _ln, _a in _lst:
        if _seat(_p, _a) == '60':
            _mine[_nm] += 1
_mine_total = sum(_mine.values())
print(f'      this seat\'s own: {dict(_mine)}  of {_mine_total}')
gate(f'Ⓒ② ⛔⛭⛭⛭ ** AND THE COST FALLS ON THE SEAT THAT WROTE IT: of this seat\'s own `{_mine_total}`, '
     f'`{_mine["notation"]}` are notation and `{_mine["substring"] + _mine["words"]}` fall OUTSIDE '
     f'the class its author was ordered to define. ** *That is the ground doing the one thing a ground '
     f'is for --- `r7299` ordered it to the seat that made the calls, and the first thing it does is '
     f'disqualify most of them.  A border drawn where it costs its author nothing is a border drawn '
     f'around what its author already did*',
     _mine_total >= 20 and _mine['substring'] + _mine['words'] > _mine['notation'])

print(f'      the step each notation pair needed: '
      f'{[(s, _stepuse[s]) for s in STEPS if _stepuse[s]]}')
gate(f'Ⓒ③ ⛭⛭ and the STEPS are themselves a measurement rather than a list: `braces` alone accounts '
     f'for `{_stepuse["braces"]}` of the `{len(_notation)}`, the largest single cause, and the widest '
     f'step in the table --- `binding`, which strips `=` and quotes --- accounts for only '
     f'`{_stepuse["binding"]}`.  ** So the table\'s riskiest rewrite is also its cheapest to drop, '
     f'and that is stated with its price rather than defended **',
     _stepuse['braces'] == max(_stepuse.values()) and _stepuse['binding'] <= 3)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓓ  THE SEEDS: A TABLE THAT COLLAPSES EVERYTHING WOULD PASS EVERY GATE ABOVE ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
#: ⛔⛭⛭ `69`'s rule records which test decided a row.  A NOTATION table needs the other half: pairs
#:   it MUST NOT bring together.  Without these, `norm` returning the empty string would satisfy
#:   every count above.
_MUST = [('\\nu_R', 'nu_{R}'), ('$A_2$', '$A_{2}$'), ('de Sitter', 'deSitter'),
         ('Y_p', 'Yp'), ('HALF ①', 'HALF ONE'), ('3e7', '3.0e7'),
         ('M\\left(1+\\cos z\\right)', 'M(1+\\cos z)'), ('(4/11)', '(4.0/11.0)')]
_MUSTNOT = [('analytical index', 'graded index'), ('decouple', 'decoupling'),
            ('DERIVED, C9', 'DERIVED in C9'), ('F=0', 'F^2'), ('1+\\cos z', 'M(1+\\cos z)'),
            ('exact for arbitrary', 'EXACT for arbitrary $m(r)$'),
            ('(4/11)', '(4.0/11.0)**(1.0/3.0)'),
            ('nu_R', 'nu_L'), ('ORDER 4', 'ORDER 5'), ('HALF ONE', 'HALF TWO')]
#: ⛔⛭ THE SEED THAT WAS WRONG, AND IT IS KEPT HERE AS THE CORRECTED PAIR.  The first form of this
#:   list asserted that `(4/11)` must NOT collapse with `(4.0/11.0)`, and the table collapses them at
#:   the `numeric` step -- correctly: those are two SPELLINGS of one number and the step is there to
#:   say so.  ** The real arm pair in that check is `(4/11)` against `(4.0/11.0)**(1.0/3.0)`, a cube
#:   root, which does not collapse and must not. **  The seed was measuring the wrong pair, which is
#:   this line's own recurring mistake one more time: the object under test was not the one the claim
#:   is about.
_must_ok = [p for p in _MUST if norm(p[0]) == norm(p[1])]
_mustnot_ok = [p for p in _MUSTNOT if norm(p[0]) != norm(p[1])]
print(f'      must collapse: {len(_must_ok)} of {len(_MUST)};  '
      f'must NOT collapse: {len(_mustnot_ok)} of {len(_MUSTNOT)}')
gate(f'Ⓓ① ✔⛭⛭ the seeds hold in BOTH directions: `{len(_must_ok)}` of `{len(_MUST)}` pairs that must '
     f'collapse do, and `{len(_mustnot_ok)}` of `{len(_MUSTNOT)}` that must not, do not.  ** The '
     f'second half is the one that matters: `norm` returning the empty string would satisfy every '
     f'count above, so a NOTATION ground is only as good as the pairs it REFUSES **',
     len(_must_ok) == len(_MUST) and len(_mustnot_ok) == len(_MUSTNOT))

_empty_would_pass = len({norm(a) for a in _PROBE}) > 1
gate(f'Ⓓ② ✔⛭ and the table is not the degenerate one: the `{len(_PROBE)}` probe arms map onto '
     f'`{len({norm(a) for a in _PROBE})}` distinct normal forms (`{_empty_would_pass}`), so the class '
     f'it defines is a class and not everything',
     _empty_would_pass and len({norm(a) for a in _PROBE}) >= 12)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓔ  THE RESTRAINT: A GROUND AND ITS RE-VERDICTS IN ONE REVISION IS A RULE GRADED BY ITS '
      'AUTHOR ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_touched = sorted({f for f in (_git('diff', '--name-only', BEFORE, AFTER) + '\n'
                               + _git('ls-files', '--others', '--exclude-standard')).split('\n') if f})
_ledger_touched = BASE in _touched
_others = sorted({_seat(p, a) for _l in (_substring, _words) for p, ln, a in _l} - {'60'})
print(f'      this revision touches {len(_touched)} files; the ledger among them: {_ledger_touched}; '
      f'seats other than this one carrying rows the ground disqualifies: {_others}')
gate(f'Ⓔ① ⛭⛭ the restraint, as the SPECIFIC NEGATIVE: the ledger is NOT in this revision\'s diff '
     f'(`{not _ledger_touched}`) and not one row is re-verdicted, this seat\'s own included.  ** A '
     f'ground and its re-verdicts in one revision is a rule graded by its author on the keys it was '
     f'derived from, which is `66`\'s own objection to a score drafted before it exists.  The '
     f'disqualified list is ROUTED with its per-seat split --- `{_others}` --- because another seat\'s '
     f'verdict is not this seat\'s to change **',
     not _ledger_touched and _others)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
for l in FAILURES:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛔ ** THE GROUND PUTS {_mine['substring'] + _mine['words']} OF ITS AUTHOR'S OWN {_mine_total} CALLS OUTSIDE THE CLASS. **
     {len(_notation)} of {len(_eo)} ENCODING-OK rows carrying an ALT arm are notation; {len(_substring)} are the substring
     family and {len(_words)} differ by words. The largest class outside the border is the one the
     border was placed to exclude: an arm that is a PREFIX of another arm.
  ⛔ ** AND THE FOURTH ORDERED CELL GOES AGAINST THIS SEAT: ** the three-way index alternation is
     three NAMES for one quantity and not three spellings of one name. 69's DELIBERATE stands.
  ✔ ** THE TABLE IS A REFINEMENT CHAIN, ** so the STEP a verdict cites is a first step and not one
     of several -- and `braces` alone accounts for {_stepuse['braces']} of the {len(_notation)}.
  ⛭ Nothing re-verdicted: the list is routed with its per-seat split.
""")
sys.exit(1 if FAILURES else 0)
