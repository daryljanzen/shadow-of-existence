#!/usr/bin/env python3
r"""S38 -- THE CAMPAIGN'S LAST 33 KEYS, AND THEY WERE ONE CLASS THE FLAG HAD ALREADY NAMED.

** WHAT WAS ORDERED. **  `r7303` order ②: *then the `33` `UNADJUDICATED-PINNED` keys, largest prefix
first -- `L200_free_data_count` (`10`), `L207_the_bend` (`7`), then the twelve small ones.  That is
the whole remaining list.*
  => *** They are read and verdicted here, and with them the quote-pin backlog is CLOSED. ***

** ⛭⛭⛭ AND THE FINDING IS WHAT THE WHOLE REMAINING LIST TURNED OUT TO BE. **  *Every one of the `33`
quotes a text read AT A NAMED COMMIT -- a paper, a kill file, a gate's own source, a ledger row, a
commit diff -- and every one carried the `PINNED` flag before it was read.*
  => *** So the last `33` keys of a `2,800`-key campaign were ONE class, and the flag on them had
      named that class all along.  A BACKLOG THAT IS ONE CLASS IS A RULING THAT WAS NEVER MADE, NOT
      WORK THAT WAS NEVER DONE. ***
  ⌈ ** The ruling is the frozen-record clause, and it needs no subject test: ** *the wording IS the
    claim -- that the text stood as quoted at that commit -- and a commit cannot reword itself, so no
    seat can break one of these keys by editing anything.*
  ⌊ ⌗ *Which is why the pinned-read bucket sat at a ceiling of `102` for the whole campaign: nobody
    had ruled it, and each reader met it one key at a time.*

** ✔⛭⛭ AND THE CLAIM IS PROVED BY WALKING THE RECEIPTS' SYNTAX, NOT BY TRUSTING THE FLAG. **  *For
every key, the literal's POSITIVE assertion is located in its receipt's abstract syntax tree and the
variable it is tested against is traced back through the assignment graph to a read at a commit.*
  => ** `33` of `33` positive; `0` tested positively against a LIVE read. **
  ⌈ ⛔ *And the classifier had to be CORRECTED THREE TIMES while this was written, each time by a
    different spelling of the same convention: `at(`, `_at(`, `_ledger_at(`.*  ** Which is the thing
    worth keeping: a mechanical test of a convention measures the convention's SPELLINGS first and
    its content second, and the three-strikes record is in the seeds below so the next reader starts
    where this one finished. **
  ⌊

⚠ WHAT THIS CANNOT SETTLE is at the foot.
"""
import ast
import collections
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
CHECKS = []
FAILURES = []


def gate(label, ok):
    CHECKS.append((label, bool(ok)))
    if not ok:
        FAILURES.append(label)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")


BEFORE = '1130c592'   # the last commit before this revision: the 33 still UNADJUDICATED-PINNED
AFTER = '57ee2e41'    # the commit that carried this revision -- the 71st member's corollary
BASE = 'corpus/quote_pin_baseline.tsv'
STAMP = 'r7312+60'
# ⚠ The COUNTS are read at `AFTER` and not in the working tree: an equality on a LIVE ledger goes red
#   the moment another seat mints a key, which is the fail-on-success family.

# ── THE INSTRUMENT ────────────────────────────────────────────────────────────────────────────────
#: A read AT A COMMIT, in every spelling this corpus uses: `git show`, a helper called `at(...)`, a
#: helper whose name ENDS in `_at(...)` -- `_ledger_at` is the one that caught this out -- or a
#: literal that opens with a sha and a `:` or `^`.
SHOW = re.compile('|'.join([r"['\"]show['\"]", r"\b(?:[A-Za-z0-9_]*_)?at\s*\(",
                            r"['\"]\{?[0-9a-f]{6,40}\}?[:^]"]))
LIVE = re.compile(r'\bopen\(|\bflat\(|\bread\(')


def classify(src):
    """{variable -> 'PINNED' | 'LIVE'}, with the assignment graph closed transitively so a variable
    built FROM a pinned one is pinned."""
    tree = ast.parse(src)
    direct, dep = {}, collections.defaultdict(set)
    for n in ast.walk(tree):
        if isinstance(n, (ast.Assign, ast.AnnAssign)):
            targets = n.targets if isinstance(n, ast.Assign) else [n.target]
            names = [t.id for t in targets if isinstance(t, ast.Name)]
            if not names or n.value is None:
                continue
            seg = ast.get_source_segment(src, n.value) or ''
            k = 'PINNED' if SHOW.search(seg) else ('LIVE' if LIVE.search(seg) else None)
            refs = {x.id for x in ast.walk(n.value) if isinstance(x, ast.Name)}
            for nm in names:
                if k == 'PINNED' or (k and direct.get(nm) != 'PINNED'):
                    direct[nm] = k
                dep[nm] |= refs
    kind = dict(direct)
    for _ in range(6):
        for nm, refs in dep.items():
            if kind.get(nm) != 'PINNED' and any(kind.get(r) == 'PINNED' for r in refs):
                kind[nm] = 'PINNED'
    return kind


def tests(src):
    """{literal -> {(variable, is_negative)}} over `in` / `not in` AND a regex search, because a key
    may be matched by a pattern rather than by containment."""
    tree = ast.parse(src)
    out = collections.defaultdict(set)

    def base(node):
        while isinstance(node, (ast.Call, ast.Attribute, ast.Subscript)):
            node = node.func if isinstance(node, ast.Call) else node.value
        return node.id if isinstance(node, ast.Name) else None

    for n in ast.walk(tree):
        if isinstance(n, ast.Compare) and len(n.ops) == 1 and isinstance(n.ops[0], (ast.In, ast.NotIn)):
            if isinstance(n.left, ast.Constant) and isinstance(n.left.value, str):
                b = base(n.comparators[0])
                if b:
                    out[n.left.value].add((b, isinstance(n.ops[0], ast.NotIn)))
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and \
           n.func.attr in ('search', 'match', 'findall', 'finditer', 'fullmatch') and len(n.args) >= 2:
            if isinstance(n.args[0], ast.Constant) and isinstance(n.args[0].value, str):
                b = base(n.args[1])
                if b:
                    out[n.args[0].value].add((b, False))
    return out


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


print()
print('=' * 100)
print('S38 -- the last 33 keys were one class, and the flag had already named it')
print('=' * 100)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓐ  THE BACKLOG IS CLOSED, AND WHAT CLOSED IT WAS ONE RULING ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_then = rows_of(_git('show', f'{BEFORE}:{BASE}'))
_now = rows_of(_git('show', f'{AFTER}:{BASE}'))
_open_then = [c for c in _then if c[5].startswith('UNADJUDICATED')]
_open_now = [c for c in _now if c[5].startswith('UNADJUDICATED')]
_mine = [c for c in _now if STAMP in (c[6] or '')]
_open_live = [c for c in rows_of(read(BASE)) if c[5].startswith('UNADJUDICATED')]
print(f'      unadjudicated: {len(_open_then)} at {BEFORE} -> {len(_open_now)} at this revision; '
      f'this revision verdicts {len(_mine)}; live now {len(_open_live)}')
gate(f'Ⓐ① ⛭⛭⛭ ** THE QUOTE-PIN BACKLOG IS CLOSED: `{len(_open_then)}` unadjudicated keys at the '
     f'commit before this one and `{len(_open_now)}` at this revision\'s own, with `{len(_mine)}` '
     f'verdicted here. **  *That is the whole remaining list `r7303` order ② named, and it is the '
     f'end of a campaign that began at `2,800` keys.*  ⌗ The live arm is REPORTED (`{len(_open_live)}`) '
     f'and NOT asserted, because a key is MINTED by an instrument and the bucket may rise again --- '
     f'which is the one thing a closed backlog does not mean',
     len(_open_then) == 33 and len(_open_now) == 0 and len(_mine) == 33)

_flags_then = collections.Counter(c[4] for c in _open_then)
_verd = collections.Counter(c[5] for c in _mine)
print(f'      the flags the 33 carried before they were read: {dict(_flags_then)}; '
      f'the verdicts they carry now: {dict(_verd)}')
gate(f'Ⓐ② ⛭⛭⛭ ** AND THE WHOLE REMAINING LIST WAS ONE CLASS, WHICH THE FLAG HAD ALREADY NAMED: ** '
     f'every one of the `{len(_open_then)}` carried `{sorted(_flags_then)}` and every one is now '
     f'`{sorted(_verd)}`.  ⇒ *** A BACKLOG THAT IS ONE CLASS IS A RULING THAT WAS NEVER MADE, NOT '
     f'WORK THAT WAS NEVER DONE. ***  *Which is why the pinned-read bucket sat under a ceiling of '
     f'`102` for the whole campaign: nobody had ruled the class, so each reader met it one key at a '
     f'time and left it*',
     sorted(_flags_then) == ['PINNED'] and sorted(_verd) == ['DELIBERATE'])

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓑ  AND THE RULING IS EARNED BY WALKING THE SYNTAX, NOT BY TRUSTING THE FLAG ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_pin_ok, _live_pos, _unresolved = [], [], []
for _c in _mine:
    _p, _lit = key(_c)
    _src = read(_p)
    _t, _k = tests(_src), classify(_src)
    _tt = _t.get(_lit, set())
    _pp = sorted({v for v, neg in _tt if not neg and _k.get(v) == 'PINNED'})
    _lp = sorted({v for v, neg in _tt if not neg and _k.get(v) == 'LIVE'})
    (_pin_ok if _pp else _unresolved).append((_p, _lit))
    if _lp:
        _live_pos.append((_p, _lit, _lp))
print(f'      of the {len(_mine)}: {len(_pin_ok)} are positively asserted against a read AT A '
      f'COMMIT, {len(_live_pos)} against a LIVE read, {len(_unresolved)} unresolved')
gate(f'Ⓑ① ✔⛭⛭⛭ and the frozen-record condition is PROVED and not assumed: `{len(_pin_ok)}` of the '
     f'`{len(_mine)}` have their literal\'s POSITIVE assertion traced through the receipt\'s own '
     f'syntax tree to a variable read AT A COMMIT, and `{len(_live_pos)}` are asserted positively '
     f'against a LIVE read.  ** The flag says the class; this says the class is what the code does. '
     f'A key positively asserted against live text would NOT be `DELIBERATE` under this ruling, and '
     f'the gate can say so **',
     len(_pin_ok) == len(_mine) and not _live_pos and not _unresolved)

#: ⛔⛭⛭ THE SEEDS, AND THEY ARE THE REASON THE GATE ABOVE IS WORTH ANYTHING.  A classifier that calls
#:   everything PINNED would satisfy it.  *Three of these seeds are the three spellings that caught
#:   this instrument out while it was being written -- `at(`, `_at(`, `_ledger_at(` -- so the record
#:   of its own corrections is the test.*
_SEED_PIN = [
    "x = subprocess.run(['git', 'show', 'abc1234:corpus/p.tex'])",
    "x = at('abc1234', 'corpus/p.tex')",
    "x = _at('abc1234', 'corpus/p.tex')",
    "x = _ledger_at(_AT_SWEEP)\n_AT_SWEEP = 'abc1234'",
    "y = _git('show', f'{SHA}:corpus/p.tex')\nx = y.replace('a', 'b')",
]
_SEED_LIVE = [
    "x = open(os.path.join(ROOT, 'corpus', 'p.tex')).read()",
    "x = flat(os.path.join(ROOT, 'corpus', 'p.tex'))",
    "x = read('corpus/p.tex')",
]
_pin_seeds = [classify(s).get('x') == 'PINNED' for s in _SEED_PIN]
_live_seeds = [classify(s).get('x') == 'LIVE' for s in _SEED_LIVE]
print(f'      seeds: {sum(_pin_seeds)} of {len(_SEED_PIN)} pinned spellings recognised; '
      f'{sum(_live_seeds)} of {len(_SEED_LIVE)} live reads NOT called pinned')
gate(f'Ⓑ② ⛔⛭⛭ the seeds hold in BOTH directions --- `{sum(_pin_seeds)}` of `{len(_SEED_PIN)}` pinned '
     f'spellings recognised and `{sum(_live_seeds)}` of `{len(_SEED_LIVE)}` live reads refused.  '
     f'** Three of the pinned seeds are the three spellings that caught this instrument out while it '
     f'was being written --- `at(`, `_at(`, `_ledger_at(` --- so its own three corrections are now '
     f'its test.  ⇒ A mechanical test of a CONVENTION measures the convention\'s SPELLINGS first and '
     f'its content second, and a classifier that called everything pinned would have satisfied the '
     f'gate above **',
     all(_pin_seeds) and all(_live_seeds))

_with_live_neg = 0
for _c in _mine:
    _p, _lit = key(_c)
    _src = read(_p)
    _t, _k = tests(_src), classify(_src)
    if any(neg and _k.get(v) == 'LIVE' for v, neg in _t.get(_lit, set())):
        _with_live_neg += 1
print(f'      of the {len(_mine)}, {_with_live_neg} also carry a NEGATIVE assertion against the live '
      f'text')
gate(f'Ⓑ③ ⛭⛭ and where a live arm exists at all it is an ABSENCE: `{_with_live_neg}` of the '
     f'`{len(_mine)}` also assert the quoted text is GONE from the current file.  ** Which is the '
     f'shape these receipts should have and mostly do: the record is PINNED and the current state is '
     f'read separately, so a repair to the paper lands on the live arm and never on the quotation.  '
     f'That is the same split this line has had to make in four of its own gates this session **',
     _with_live_neg >= 4)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print('\n── Ⓒ  THE RESTRAINT ──\n')
# ══════════════════════════════════════════════════════════════════════════════════════════════════
_touched = sorted({f for f in (_git('diff', '--name-only', f'{AFTER}^1', AFTER) + '\n'
                               + _git('ls-files', '--others', '--exclude-standard')).split('\n') if f})
_subjects = sorted({key(c)[0] for c in _mine})
_subjects_touched = [f for f in _touched if f in _subjects]
print(f'      the {len(_subjects)} receipts whose rows are verdicted here are edited '
      f'{len(_subjects_touched)} times by this revision')
gate(f'Ⓒ① ⛭⛭ the restraint, as the SPECIFIC NEGATIVE alone: the `{len(_subjects)}` receipts whose '
     f'rows are verdicted here are edited `{len(_subjects_touched)}` times.  ** Every one of them '
     f'belongs to another seat --- these are the prefixes no reader had closed --- and a verdict is '
     f'a ROW, which is the distinction that makes a campaign over other seats\' receipts possible at '
     f'all **',
     not _subjects_touched and len(_subjects) >= 12)

# ══════════════════════════════════════════════════════════════════════════════════════════════════
print()
print('=' * 100)
print(f'  gates run: {len(CHECKS)}   failed: {len(FAILURES)}')
for l in FAILURES:
    print(f'    FAIL  {l}')
print('=' * 100)
print(f"""
  ⛭ ** THE QUOTE-PIN BACKLOG IS CLOSED: {len(_open_then)} -> {len(_open_now)}, ** the last {len(_mine)} verdicted here.
  ⛭ ** AND THE WHOLE REMAINING LIST WAS ONE CLASS THE FLAG HAD ALREADY NAMED. ** Every one quotes a
     text read AT A COMMIT, so the wording IS the claim and no seat can break it by editing
     anything. ⇒ A BACKLOG THAT IS ONE CLASS IS A RULING THAT WAS NEVER MADE, NOT WORK THAT
     WAS NEVER DONE.
  ✔ ** PROVED BY WALKING THE RECEIPTS' SYNTAX: ** {len(_pin_ok)} of {len(_mine)} positively asserted against a
     read at a commit, {len(_live_pos)} against a live read.
  ⛔ ** AND THE CLASSIFIER WAS WRONG THREE TIMES FIRST, ** each time on a different spelling of the
     same convention. Its three corrections are now its seeds.
""")
sys.exit(1 if FAILURES else 0)
