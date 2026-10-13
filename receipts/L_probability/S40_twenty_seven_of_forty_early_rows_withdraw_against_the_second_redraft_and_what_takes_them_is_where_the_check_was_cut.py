#!/usr/bin/env python3
r"""S40 -- THE BOUNDED SAMPLE `r7313` ORDERED: `27` OF `40` WITHDRAW, AND THE BAND IS REFUTED.

** WHAT WAS ORDERED. **  `r7313`: *"a BOUNDED sample of pre-`r7260` rows, re-read WITH the rule,
counting how many of their `DELIBERATE`s their own authors withdraw"* -- the sample size, the draw and
the band registered BEFORE the read, against the SECOND redraft (`6bef6fd5`) and not the first.

** THE THREE COMMITS, IN THIS ORDER. **  `848a1db2` the pre-registration (population `168`, SIZE `40`,
the draw, the three outcomes, the band `8`-`16`, centre `11`, and the two refutation conditions);
`c9322295` the draw, run from the published salt; and this one, the reading.

*** ⛔⛭⛭⛭ THE RESULT: `27` WITHDRAWN, `11` HELD, `2` MOVED.  THE BAND FAILED, ABOVE IT, AND THE
    REGISTERED REFUTATION AT OR ABOVE `25` IS MET. ***  *The claim I made at `r7318` -- that the early
    era's shortfall is substantially a matter of WHEN it was read, so re-reading early rows with the
    instruments should bring them to about the post-instrument era's `25.7` per cent -- is refuted in
    the direction the pre-registration named.*  ** Re-read with the rule, my own early `DELIBERATE`s
    withdraw at `67.5` per cent, which is where the rule's own aggregate rate already sat. **

** ⛭⛭ AND WHAT TAKES THEM IS NOT THE ERA.  IT IS WHERE THE CHECK WAS CUT. **
  ⓘ **Test 1 takes `11`**: the span is cut INSIDE its own sentence, so its subject or its condition
     stays outside -- and in one case (`item 10`) the condition left outside is the very distinction
     that receipt was written to make.
  ⓙ **Test 5 takes `11`**: one compound label over several arms, each found independently in the
     file, with nothing joining them.
  ⓚ Test 3 takes `4` (a code string standing in for what a tool does, in a check that never runs it)
     and Test 4 takes `1` (a bare `243` occurring three times in the block the check reads).
  => *** `22` of the `27` fall to two grounds, and NEITHER IS A PROPERTY OF THE ERA: both are
      properties of HOW I CUT A GATE.  Reading the rows earlier or later would not have moved either.
      ⇒ WHAT WITHDRAWS A ROW IS WHERE THE CHECK WAS CUT, AND NOT WHAT THE QUOTED WORDS SAY. ***
  ⌗ *And the clause the redraft added for this era took NOTHING: step 4's third bullet decided `0` of
    the `40`, because every fragment that could have fallen there fell at Test 1 first.*

** ✔ WHAT HOLDS IS THE REPAIR RECIPE. **  *All `11` `HELD` rows are a value, a formula or a NAME used
as data (`6`, two of them read by PARSING the other receipt); a WHOLE clause where the claim is that
the file states it (`3`); or a single unchanged line whose TEXT IS THE FACT (`2`).*  ⇒ ** Pin a value,
a name, or a whole clause -- never a span out of the middle of a sentence, and never several arms
under one label. **

** ⛭⛭ AND THE ONE CHECK ON A SELF COUNT THAT DOES NOT RUN THROUGH ME. **  *`71`'s blind application of
the same redraft landed on the trunk while this was being read.  **One key is in both samples, and we
agree on the verdict, the step and the reason.**  Its `50` owed keys are decided Test `1` `21` and Test
`5` `12` ahead of everything else -- the same two grounds in the same order as these `27`, on a
different population, read blind -- and it records the same cause for the second: the joint-piece
paragraph sends a claim about pieces TOGETHER to Test `5` instead of step 2.*

⛔ ** THIS REVISION VERDICTS NOTHING. **  *`27` withdrawals read in a sample are a FINDING.  Writing
them into the ledger adds `27` rows to the `366` `REPAIR-OWED` the trunk already carries -- the
VERDICTING campaign is the one that closed, and `r7315` repaired that very framing in `PO-78`'s
standing state -- and it binds the campaign that has not; `r7313` and the pre-registration both put
that decision with the gating seat.  **Routed with the table.**

⚠ WHAT THIS CANNOT SETTLE is at the foot -- beginning with the fact that it is a SELF count whose one
protection, the band, is the thing that failed.
"""
import ast
import hashlib
import io
import os
import re
import subprocess
import sys

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

# the three commits this revision stands on, as literal shas.  EVERY read below is at one of them:
# the reading was performed on one tree, and a gate that re-read the live tree would go red the next
# time another seat reworded a paper -- which is this line's own recurring finding.
RULE = '6bef6fd5acf0692299f306c96e2ee630542dac14'      # the SECOND redraft, and the draw's salt
PREG = '848a1db2'                                       # the pre-registration, pushed before the draw
DRAW = 'c9322295'                                       # the draw, and the tree the reading is of
D = 'computations/beyond_the_wall/r7320_60_the_early_era_sampled'


def show(sha, rel):
    r = subprocess.run(['git', '-C', ROOT, 'show', f'{sha}:{rel}'],
                       capture_output=True, text=True, errors='replace')
    return r.stdout


def rows_of(text):
    out = []
    for l in text.split('\n'):
        if l.startswith('#') or not l.strip():
            continue
        out.append(l.split('\t'))
    return out


RULETEXT = show(RULE, 'computations/beyond_the_wall/r7299_69_the_rule/THE_RULE.md')
PRE = show(PREG, f'{D}/PREDICTION.md')
SAMPLE = rows_of(show(DRAW, f'{D}/SAMPLE_40.tsv'))
RESULT = rows_of(io.open(os.path.join(ROOT, D, 'RESULT_40.tsv'), encoding='utf-8').read())

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('A -- THE RULE, THE PRE-REGISTRATION AND THE DRAW, EACH READ WHERE IT CANNOT BE EDITED')

_changes = ['step 2 reaches the quotation only when it is the whole of that statement',
            'the number of times\n  it occurs in the file has changed once',
            'Nothing else outside the quotation makes the repair owed under this test',
            'recorded as decided at step 4',
            'It takes only the\nspelling arms']
gate(f'Ⓐ①  the rule applied here is the SECOND redraft at `{RULE[:8]}`, read AT that commit, and the '
     f'five changes the pre-registration named in advance are all in it -- so none of them can be '
     f'claimed afterwards as a discovery',
     len(RULETEXT) > 6000 and all(c in RULETEXT for c in _changes))

_anc = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', PREG, DRAW]).returncode == 0
_anc2 = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', DRAW, 'HEAD']).returncode == 0
_band = '`8`–`16` of `40` WITHDRAWN' in PRE and '`11` of `40` (`27.5` per cent)' in PRE
_refut = 'At or above `25` of `40`' in PRE and 'At or below `5` of `40`' in PRE
gate('Ⓐ②  and the pre-registration is PRIOR to the draw and the draw prior to this reading -- '
     'ancestry, not assertion -- with the band, the centre and BOTH refutation conditions fixed in '
     'it before one row was read',
     _anc and _anc2 and _band and _refut)


def seat(w):
    for s in ('+60', '+69', '+70', 'cc66', '+66', '+71'):
        if s in (w or ''):
            return s.lstrip('+')
    return '?'


def rev(w):
    m = re.match(r'r(\d{4})', w or '')
    return int(m.group(1)) if m else None


_led = [c for c in rows_of(show(PREG, 'corpus/quote_pin_baseline.tsv')) if c[0].startswith('receipts/')]
_pop = [c for c in _led if c[5] == 'DELIBERATE' and seat(c[6]) == '60' and (rev(c[6]) or 99999) < 7260]
_redrawn = sorted(_pop, key=lambda c: hashlib.sha256(
    (RULE + c[0] + '\t' + c[1]).encode('utf-8')).hexdigest())[:40]
_same = [(c[0], c[1]) for c in _redrawn] == [(c[0], c[1]) for c in SAMPLE]
gate(f'Ⓐ③  and THE DRAW REPRODUCES: the population read AT the pre-registration commit is `{len(_pop)}` '
     f'rows, and re-running the published hash over it returns the same `{len(SAMPLE)}` keys in the same '
     f'order as `SAMPLE_40.tsv`.  ** Deterministic from a salt published before the draw, so nobody '
     f'has to take the sample on my word **',
     len(_pop) == 168 and len(SAMPLE) == 40 and _same)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('B -- THE READING COVERS THE SAMPLE, AND EVERY WITHDRAWAL NAMES ITS TEST')

_keys_match = [(c[1], c[2]) for c in RESULT] == [(c[0], c[1]) for c in SAMPLE]
gate(f'Ⓑ①  the reading is OF THE DRAWN SAMPLE and of nothing else: `{len(RESULT)}` rows, the same keys '
     f'in the same order as the draw, one line each',
     len(RESULT) == 40 and _keys_match and [c[0] for c in RESULT] == [str(i) for i in range(1, 41)])

_OUT = {'WITHDRAWN', 'HELD', 'MOVED'}
_named = all(re.match(r'Test [1-7]\b', c[7]) for c in RESULT if c[6] == 'WITHDRAWN') or \
    all(re.match(r'Test [1-7]\b|step 4 -- third bullet', c[7]) for c in RESULT if c[6] == 'WITHDRAWN')
_detail = all(len(c[8].strip()) > 40 for c in RESULT)
gate('Ⓑ②  and every row carries one of the three outcomes the pre-registration fixed, every '
     'WITHDRAWN row names the test that decided it, and every row says what the site detail was -- '
     'which is the redraft\'s own closing instruction: *a verdict without its test cannot be checked '
     'by the next reader*',
     all(c[6] in _OUT for c in RESULT) and _named and _detail)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('C -- THE COUNT, AND THE SCORE AGAINST THE BAND REGISTERED BEFORE THE DRAW')

W = [c for c in RESULT if c[6] == 'WITHDRAWN']
H = [c for c in RESULT if c[6] == 'HELD']
M = [c for c in RESULT if c[6] == 'MOVED']
print(f'      WITHDRAWN {len(W)}   HELD {len(H)}   MOVED {len(M)}   of {len(RESULT)}')
gate(f'Ⓒ①  THE COUNT: `{len(W)}` WITHDRAWN, `{len(H)}` HELD, `{len(M)}` MOVED of `{len(RESULT)}`.  ** The '
     f'registered quantity is the `{len(W)}` alone: a MOVED row is a changed reading and not a '
     f'withdrawal, and counting the two of them in would have made the figure `{len(W) + len(M)}` **',
     len(W) + len(H) + len(M) == 40 and len(W) == 27 and len(H) == 11 and len(M) == 2)

_pct = 100.0 * len(W) / 40
gate(f'Ⓒ②  ⛔ AND THE BAND FAILED, ABOVE IT: `{len(W)}` of `40` is `{_pct:.1f}` per cent against a '
     f'registered band of `8`-`16` and a central guess of `11`, and it is at or above the `25` the '
     f'pre-registration fixed as the SECOND refutation condition.  ** So the `r7318` claim is '
     f'refuted in the registered direction and not in the flattering one -- the early era does not '
     f'come to the post-instrument era\'s `25.7` per cent when it is read with the instruments, it '
     f'comes to the rule\'s own rate **',
     len(W) > 16 and len(W) >= 25)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('D -- THE THREE GROUNDS, CORROBORATED MECHANICALLY AT THE PINNED TREE')


def checks_requiring(src, lit):
    """every check/gate call in `src` that carries `lit` in one of its own STRING CONSTANTS.

    Read off the parsed constants and not off the source text: a receipt writes a long span as
    adjacent literals over two lines, which the parser folds and a text search misses."""
    out = []
    for n in ast.walk(ast.parse(src)):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in ('check', 'gate'):
            for c in ast.walk(n):
                if isinstance(c, ast.Constant) and isinstance(c.value, str) and lit in c.value:
                    out.append(n)
                    break
    return out


def required_pieces(src, node):
    """{container source: [string literals the check requires PRESENT in it]}"""
    d = {}
    for c in ast.walk(node):
        if isinstance(c, ast.Compare) and len(c.ops) == 1 and isinstance(c.ops[0], ast.In) \
                and isinstance(c.left, ast.Constant) and isinstance(c.left.value, str):
            d.setdefault(ast.get_source_segment(src, c.comparators[0]) or '?', []).append(c.left.value)
    return d


def ground(c):
    return c[7].split(' -- ')[0].strip()


_t5 = [c for c in RESULT if ground(c) == 'Test 5']
_t5_ok, _t5_worst = [], 99
for c in _t5:
    src = show(DRAW, c[1])
    best = 0
    for node in checks_requiring(src, ast.literal_eval(c[2])):
        pieces = required_pieces(src, node)
        best = max([best] + [len(v) for v in pieces.values()])
    _t5_ok.append(best >= 2)
    _t5_worst = min(_t5_worst, best)
print(f'      Test 5 rows: {len(_t5)};  smallest number of pieces one container is asked for: {_t5_worst}')
gate(f'Ⓓ①  **Test 5 corroborated by PARSING and not by my reading**: for each of the `{len(_t5)}` rows '
     f'decided there, a check requiring that literal at `{DRAW}` requires at least `2` string pieces '
     f'PRESENT IN ONE CONTAINER -- the smallest is `{_t5_worst}` -- so each piece carries a claim half '
     f'of a joint requirement cannot reach',
     len(_t5) == 11 and all(_t5_ok))


def ws(t):
    return re.sub(r'\s+', ' ', t)


# the site of each Test 1 row, at the pinned tree, with the normaliser the check itself reads through
_SITE = {
    '2': ('corpus/CR_cosmology.tex', 'raw'), '5': ('corpus/CR_framework.tex', 'raw'),
    '8': ('scripts/run_all_receipts.py', 'raw'), '10': ('corpus/CR_cosmology.tex', 'raw'),
    '11': ('scripts/run_all_receipts.py', 'raw'), '14': (f'{D}/../r7186_60_third_transport/PREDICTION.md', 'ws'),
    '22': ('corpus/matter_sector_paper.tex', 'raw'), '28': ('FOR_60.md', 'raw'),
    '31': (f'{D}/../r7186_60_third_transport/PREDICTION.md', 'ws'),
    '35': (f'{D}/../r7192_60_the_two_floors/PREDICTION.md', 'ws'),
    '38': ('corpus/CR_cosmology.tex', 'raw'),
}


def before_in_sentence(text, lit):
    i = text.find(lit)
    if i < 0:
        return None
    pre = text[:i]
    cut = max(pre.rfind('. '), pre.rfind('\n'), pre.rfind('! '), pre.rfind('? '), pre.rfind('; '))
    return pre[cut + 1:].strip()


_t1 = [c for c in RESULT if ground(c) == 'Test 1']
_t1_ok, _t1_min = [], 10 ** 6
for c in _t1:
    rel, mode = _SITE[c[0]]
    t = show(DRAW, os.path.normpath(rel))
    if mode == 'ws':
        t = ws(t)
    frag = before_in_sentence(t, ast.literal_eval(c[2]))
    _t1_ok.append(bool(frag) and len(frag) >= 10)
    _t1_min = min(_t1_min, len(frag or ''))
print(f'      Test 1 rows: {len(_t1)};  shortest run of the same sentence standing BEFORE the span: '
      f'{_t1_min} characters')
gate(f'Ⓓ②  **Test 1 corroborated at the site**: each of the `{len(_t1)}` rows decided there is cut '
     f'INSIDE its own sentence at `{DRAW}` -- at least `10` characters of that sentence stand before '
     f'the quotation, the shortest being `{_t1_min}` -- which is where a subject or a condition is '
     f'left.  ** The words left outside are named row by row in the table, and the test is closed to '
     f'exactly those three things **',
     len(_t1) == 11 and all(_t1_ok))

_t3 = [c for c in RESULT if ground(c) == 'Test 3']
_t3_ok = []
for c in _t3:
    src = show(DRAW, c[1])
    nodes = checks_requiring(src, ast.literal_eval(c[2]))
    runs = [any(isinstance(x, ast.Call) for x in ast.walk(n.args[1])) for n in nodes if len(n.args) > 1]
    _t3_ok.append(bool(runs) and not all(runs))
gate(f'Ⓓ③  **Test 3 corroborated by parsing the condition**: for each of the `{len(_t3)}` rows decided '
     f'there, the deciding check\'s CONDITION contains no call at all at `{DRAW}` -- it finds strings '
     f'in a tool\'s source and cannot have exercised the behaviour the claim names',
     len(_t3) == 4 and all(_t3_ok))

_run = show(DRAW, 'scripts/run_all_receipts.py')
_T = ('P15_the_four_dimensional_treatment_keeps_the_economy_and_keeps_more_of_it_but_in_the_'
      'sphere_label_so_the_bridge_exists_only_on_the_squashing_free_sector.py')
_blk = _run[_run.find('⛭ ADDED r7188 (60)'):_run.find(f"'{_T}': ")]
_t4 = [c for c in RESULT if ground(c) == 'Test 4']
print(f"      Test 4: '243' occurs {_blk.count('243')} times in the block that check reads")
gate(f'Ⓓ④  **Test 4\'s one row corroborated by counting**: the block that check actually reads carries '
     f'`{_blk.count("243")}` occurrences of `243` at `{DRAW}`, and the claim concerns ONE of them -- the '
     f'fifth-slowest figure of one run',
     len(_t4) == 1 and _blk.count('243') == 3 and 0 < len(_blk) < 6000)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('E -- WHAT THAT MEANS: THE TWO GROUNDS, THE SHAPE THAT HOLDS, AND THE BORDER')

_by = {}
for c in W:
    _by[ground(c)] = _by.get(ground(c), 0) + 1
_step4_third = [c for c in RESULT if 'third bullet' in c[7]]
print(f'      grounds: {_by};  decided at step 4\'s third bullet: {len(_step4_third)}')
gate(f'Ⓔ①  ⛭⛭ **TWO GROUNDS TAKE `{_by.get("Test 1", 0) + _by.get("Test 5", 0)}` OF THE `{len(W)}`, AND '
     f'NEITHER IS A PROPERTY OF THE ERA**: Test 1 `{_by.get("Test 1", 0)}` and Test 5 '
     f'`{_by.get("Test 5", 0)}` -- a span cut inside its sentence, and a compound label over arms '
     f'found independently.  ** Both are properties of HOW I CUT A GATE, and reading the rows earlier '
     f'or later would not have moved either.  ⇒ What withdraws a row is where the check was cut, not '
     f'what the quoted words say **',
     _by.get('Test 1', 0) == 11 and _by.get('Test 5', 0) == 11 and sum(_by.values()) == 27)

gate(f'Ⓔ②  ⌗ and THE CLAUSE THE REDRAFT ADDED FOR THIS ERA TOOK NOTHING: step 4\'s third bullet -- a '
     f'fragment that is neither a clause nor a name, on a line that has changed -- decided '
     f'`{len(_step4_third)}` of the `40`, because every fragment that could have fallen there fell at '
     f'Test 1 first, one step earlier and with the words left outside named',
     len(_step4_third) == 0)

_shapes = {'value': 0, 'formula': 0, 'name': 0, 'whole clause': 0, 'unchanged line': 0}
for c in H:
    k = c[7].split(' -- ')[-1].strip()
    _shapes[k] = _shapes.get(k, 0) + 1
_data = _shapes['value'] + _shapes['formula'] + _shapes['name']
gate(f'Ⓔ③  ✔ and WHAT HOLDS IS THE REPAIR RECIPE: all `{len(H)}` HELD rows are a value, a formula or a '
     f'NAME used as data (`{_data}`, two of them read by PARSING the other receipt rather than by '
     f'quoting it), a WHOLE clause where the claim is that the file states it '
     f'(`{_shapes["whole clause"]}`), or a single unchanged line whose text IS the fact '
     f'(`{_shapes["unchanged line"]}`).  ** Pin a value, a name, or a whole clause -- never a span out '
     f'of the middle of a sentence, and never several arms under one label **',
     _data == 6 and _shapes['whole clause'] == 3 and _shapes['unchanged line'] == 2
     and _data + _shapes['whole clause'] + _shapes['unchanged line'] == len(H))

sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7302_60_the_encoding_ground'))
import notation_table as NT                                            # noqa: E402

_KEY = 'the Weyl $S_3$ is the relation among the three hinges'
_AS_WRITTEN = 'the Weyl $S_3$ \\emph{is} the relation among the three hinges'
_step = NT.needed_step(_AS_WRITTEN, _KEY)
_border = [c for c in RESULT if 'spelling border' in c[8]]
gate(f'Ⓔ④  ⌗ and THE SPELLING BORDER LEFT NOTHING UNDECIDED EITHER: `{len(_border)}` row of the `40` '
     f'reads its target through a markup normaliser, and this seat\'s own `ENCODING-OK` ground takes '
     f'the paper\'s `\\emph{{is}}` and the read\'s `is` to ONE string -- needing the `{_step}` step, '
     f'the `emphasis` step alone leaving `{{is}}`.  ** The row is HELD on its content and ENCODING-OK '
     f'on its spelling arm, and the verdict records the step it needed **',
     len(_border) == 1 and _step == 'braces' and _AS_WRITTEN in show(DRAW, 'corpus/matter_sector_paper.tex'))

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('F -- THE RESTRAINT, AND THE LIMIT OF A SEAT SCORING ITS OWN ROWS')

_led_pre = show(PREG, 'corpus/quote_pin_baseline.tsv')
_led_draw = show(DRAW, 'corpus/quote_pin_baseline.tsv')
_live = io.open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8').read()
_keys = {(c[1], c[2]) for c in RESULT}
_stamped = [c for c in rows_of(_live)
            if c[0].startswith('receipts/') and (c[0], c[1]) in _keys and 'r7320' in (c[6] if len(c) > 6 else '')]
gate(f'Ⓕ①  ⛔ **THIS REVISION VERDICTS NOTHING, asserted as the specific negative it is**: the ledger '
     f'is byte-identical across the pre-registration and the draw commits, and not one of the `40` '
     f'drawn rows carries a `r7320` verdict in the live file (`{len(_stamped)}`).  ** `27` withdrawals '
     f'read in a sample are a FINDING; writing them in re-opens a backlog this line closed and binds '
     f'the campaign, and `r7313` and the pre-registration both put that decision with the gating '
     f'seat **',
     _led_pre == _led_draw and len(_stamped) == 0)

_self = 'This is a SELF-withdrawal count and not a blind read' in PRE
_prot = 'The band above is the only protection against that and it is registered before\n  the draw' in PRE
gate('Ⓕ②  ⚠ and THE LIMIT IS THE ONE DECLARED BEFORE THE DRAW: this is a SELF count, the figure is '
     'not independent of me, and the band was named there as *the only protection* against a seat '
     'that had just argued the early era is weak finding that it withdraws.  ** That protection is '
     'the thing that failed -- so what can be checked without trusting me is the draw\'s '
     'reproduction and the three grounds above, each read at a commit and not at the live tree **',
     _self and _prot)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
head('G -- THE ONE CHECK ON A SELF COUNT THAT DOES NOT RUN THROUGH ME: 71 READ ONE OF THESE KEYS BLIND')

# 71's blind application of the SAME redraft, landed on the trunk at r7315's merge and read AT that
# commit.  A different population, a different seat, and no sight of any verdict -- which is the only
# thing available that can corroborate a count its own author made.
TRUNK = '619a4753'
_G71 = rows_of(show(TRUNK, 'computations/beyond_the_wall/r7313_71_redraft2_blind/GROUNDS_71_redraft2.tsv'))
_owed71 = [r for r in _G71 if r[2] == 'REPAIR-OWED']
_t71 = {}
for r in _owed71:
    _t71[r[4]] = _t71.get(r[4], 0) + 1
_mine_keys = {(c[1], c[2]): c for c in RESULT}
_shared = [(r, _mine_keys[(r[0], r[1])]) for r in _G71 if (r[0], r[1]) in _mine_keys]
_agree = [(r, c) for r, c in _shared
          if (r[2] == 'DELIBERATE') == (c[6] == 'HELD') and r[3] == '2' and c[7].startswith('step 2')]
print(f'      71 blind: {len(_owed71)} owed of {len(_G71)};  deciding test over owed: {_t71}')
print(f'      keys both of us read: {len(_shared)};  agreeing on verdict AND step: {len(_agree)}')
gate(f'Ⓖ①  ⛭⛭ **ONE KEY OF THE `40` WAS ALSO READ BLIND BY `71`, AND WE AGREE ON THE VERDICT, THE STEP '
     f'AND THE REASON**: `$D_M=D_C$` -- `71` `DELIBERATE` at step 2\'s second bullet because the claim '
     f'lists the four pieces as each present, which says something about each piece ON ITS OWN; this '
     f'seat `HELD` at step 2 for the same reason.  ** On the one key where a blind reader overlaps a '
     f'self count, the self count does not move **',
     len(_shared) == 1 and len(_agree) == 1)

_top = sorted(_t71.items(), key=lambda kv: -kv[1])[:2]
gate(f'Ⓖ②  ⛭ and THE TWO GROUNDS ARE THE SAME TWO ON A DIFFERENT POPULATION READ BLIND: `71`\'s `50` '
     f'owed keys are decided `Test {_top[0][0]}` `{_top[0][1]}` and `Test {_top[1][0]}` `{_top[1][1]}` '
     f'ahead of everything else, where this seat\'s `27` are Test 1 `11` and Test 5 `11` -- and `71` '
     f'records the same cause for the second, that the redraft\'s joint-piece paragraph sends a claim '
     f'about pieces TOGETHER to Test 5 instead of step 2.  ** Test 1\'s share is `{100.0 * _top[0][1] / len(_owed71):.0f}` '
     f'per cent there against `{100.0 * 11 / len(W):.0f}` here **',
     {_top[0][0], _top[1][0]} == {'1', '5'} and len(_owed71) == 50)


def quoting_checks(src, lit):
    n = 0
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in ('check', 'gate'):
            for c in ast.walk(node):
                if isinstance(c, ast.Constant) and isinstance(c.value, str) and lit in c.value:
                    n += 1
                    break
    return n


SITE_GROUNDS = {'Test 1', 'Test 2', 'Test 4'}
_multi = [c for c in RESULT if quoting_checks(show(DRAW, c[1]), ast.literal_eval(c[2])) > 1]
_immune = [c for c in _multi if ground(c) in SITE_GROUNDS]
print(f'      rows quoted by MORE THAN ONE check: {len(_multi)} of 40;  '
      f'decided by a SITE ground and so check-independent: {len(_immune)}')
gate(f'Ⓖ③  ⌗ and `71`\'s NEW OPEN PLACE -- *a row several checks quote with different results* -- '
     f'MEASURED on this population rather than discussed: `{len(_multi)}` of the `40` are quoted by '
     f'more than one check, `{len(_immune)}` of those are decided by a ground that is a property of the '
     f'SITE (Tests 1, 2, 4) and so cannot differ between checks.  ** By this seat\'s reading none of the '
     f'`{len(_multi)}` had checks that disagreed -- the `{len(_immune)}` cannot, and in the other four the '
     f'claim is joint or several alike in both checks; that half is a reading and is marked as one. **  ** The discriminator follows from the rule\'s own text: Tests 1, 2 and '
     f'4 are properties of the SITE, step 2 and Tests 3, 5, 6, 7 of the CHECK -- so the question only '
     f'arises when no site ground is met.  ⇒ Offered with a proposed tie-break for that case, OWED IF '
     f'ANY CHECK OWES IT, which is `69`\'s to write and `66`\'s to order **',
     len(_multi) == 8 and len(_immune) == 4)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
for l in FAILURES:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛔ ** {len(W)} OF 40 WITHDRAW, {len(H)} HOLD, {len(M)} MOVE. **  The registered band was 8-16 with a centre of 11,
     and the registered refutation at or above 25 is MET: the r7318 claim is refuted in the direction
     the pre-registration named rather than in the flattering one.
  ⛭⛭ ** AND WHAT TAKES THEM IS WHERE THE CHECK WAS CUT, NOT WHAT THE QUOTED WORDS SAY: ** Test 1 and
     Test 5 take 11 each -- a span cut inside its own sentence, and one label over arms found
     independently -- and the clause the redraft added for this era took none.
  ✔ ** The repair recipe is what held: ** a value, a name, or a WHOLE clause.  Nothing else held.

  ⚠ ** WHAT THIS CANNOT SETTLE. **
     * It is a SELF count.  The band was the one protection and it failed, so the figure is worth
       exactly what its machinery is worth: the draw reproduces from a salt published before it ran,
       and each ground is corroborated by parsing or counting at a pinned commit.
     * 40 of 168 rows of ONE seat in ONE era.  It says nothing about another seat's early rows, and
       cc66's rate moves the other way across r7260.
     * DELIBERATE rows only, as ordered.  A re-read of the era's MEANING-HELD rows is a different
       measurement, and the two MOVED rows here are the only hint of its size.
     * ⛔ And r7313 is explicit: if the sample says the early rows mostly withdraw, that is a finding
       and NOT an order to re-read 1,665 rows.  Nothing here proposes that.
""")
sys.exit(1 if FAILURES else 0)
