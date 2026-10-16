#!/usr/bin/env python3
"""r7402 (60) -- THE GATE THAT COUNTED THE REPAIRS IT ORDERED.  Four arms, all registered in
`PREDICTION.md` at `FRAME` before this ran.

⛔ THE BANDS ARE IN `PREDICTION.md`, COMMITTED AT `FRAME` BEFORE THIS RAN: ⒜ 11 (5-17), ⒝ 4 (0-25),
⒞ 2 (0-10), ⒟ exact 0.

⛭ `S37`'s `Ⓑ②` reads its ROWS at a pinned commit and its ARMS from a live mint, and all seventeen of the
pinned literals are absent from the live map because sixteen were `REPAIR-OWED` and the repairs landed.
⇒ The pinned form runs the mint over the tree at `AFTER` with the instrument AS IT STOOD at `AFTER`, in a
detached worktree, so both ends of the clause are historical.

⛭⛭ AND THE DETECTOR NEEDS THE SPLITS `r7386` PAID FOR: a clause is `gate(label, cond)` and only
`args[1:]` is the claim (LABEL vs CONDITION), a live read asserted as a DIRECTION or a CEILING is sound
(`r7368` ②'s carve-out, FIGURE vs DIRECTION), and a name is counted for what the clause CONSUMES rather
than for appearing in the file (SHAPE vs USE).

    python3 -I cost.py            # everything
    python3 -I cost.py --no-pinned   # skip the worktree mint, for the census alone
"""
import argparse
import ast
import collections
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

FRAME = '78c87575'
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))

# `S37`'s own constants, read from the receipt rather than retyped
S37 = ('receipts/L_probability/S37_the_ground_disqualified_seventeen_of_its_authors_own_calls_and_'
       'sixteen_of_them_are_repairs.py')
BASE = 'corpus/quote_pin_baseline.tsv'
INSTRUMENT = 'scripts/mutate_assertions.py'
SITE = re.compile(r'\s*\[QUOTE-PIN\]\[(\w+)\]\[(\w+)\]\[([^\]]*)\]\s+(\S+?):(\d+):(\d+)\s+(".*")\s*$')
_SHA = re.compile(r'\b[0-9a-f]{8,40}\b')
# the asserting call forms this corpus uses, and the index at which the CLAIM starts
ASSERTERS = {'gate': 1, 'check': 1, 'assert_': 1}


def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True, errors='replace').stdout


def consts():
    """`AFTER`, `BEFORE` and `STAMP` taken from `S37`'s own module tree, never retyped here"""
    tree = ast.parse(open(os.path.join(ROOT, S37), encoding='utf-8').read())
    out = {}
    for n in ast.walk(tree):
        if (isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)
                and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str)):
            out[n.targets[0].id] = n.value.value
    return out


C37 = consts()
AFTER, BEFORE, STAMP = C37['AFTER'], C37['BEFORE'], C37['STAMP']


def rows_of(text):
    return [c for c in (l.split('\t') for l in text.split('\n'))
            if len(c) >= 7 and c[0].startswith('receipts/')]


def mine_rows():
    return [c for c in rows_of(git('show', f'{AFTER}:{BASE}')) if STAMP in (c[6] or '')]


def parse_alt(out):
    """(alt, run_of, runs) exactly as `S37`'s `alt_runs` groups them: maximal consecutive-line runs"""
    alt = collections.defaultdict(list)
    for l in out.split('\n'):
        m = SITE.match(l)
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


def live_alt():
    r = subprocess.run([sys.executable, os.path.join(ROOT, INSTRUMENT), '--quote'], cwd=ROOT,
                       capture_output=True, text=True, timeout=1800)
    return parse_alt(r.stdout)


def pinned_alt(sha=None):
    """the mint over the tree at `sha` with the INSTRUMENT AS IT STOOD THERE -- a detached worktree, so
    neither end of the measurement is this tree's"""
    sha = sha or AFTER
    tmp = tempfile.mkdtemp(prefix='r7402_')
    d = os.path.join(tmp, 'tree')
    subprocess.run(['git', '-C', ROOT, 'worktree', 'add', '-q', '--detach', d, sha], check=True)
    try:
        r = subprocess.run([sys.executable, os.path.join(d, INSTRUMENT), '--quote'], cwd=d,
                           capture_output=True, text=True, timeout=1800)
        return parse_alt(r.stdout)
    finally:
        subprocess.run(['git', '-C', ROOT, 'worktree', 'remove', '--force', d],
                       capture_output=True, text=True)
        shutil.rmtree(tmp, ignore_errors=True)


# ⛭ `S37`'s own normaliser, IMPORTED and not retyped: `r7302`'s notation table decides what counts as
#   the same notation, and a guess at it would move every containment verdict.  The receipt reaches it
#   the same way -- `from notation_table import norm`.
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7302_60_the_encoding_ground'))
from notation_table import norm                                   # noqa: E402


def pairs(mine, alt, run_of, runs):
    """`Ⓑ②`'s own count: of `mine`, how many stand in a containment relation with another arm of their
    own run.  Returns (count, reached) -- `reached` is how many of `mine` are present as an arm at all,
    which is the figure that separates a real zero from a structural one."""
    n, reached = 0, 0
    for c in mine:
        p, a = c[0], json.loads(c[1]) if c[1].startswith('"') else c[1]
        ln = next((l for (pp, l), arms in alt.items() if pp == p and a in arms), None)
        if ln is None:
            continue
        reached += 1
        grp = runs[run_of[(p, ln)]]
        if any(b != a and (norm(a) in norm(b) or norm(b) in norm(a)) for b in grp):
            n += 1
    return n, reached


# ============================================================== the census: MIXED-PROVENANCE CLAUSES
_PIN_READ = re.compile(r"""['"]show['"]|\bgit\s*\(\s*['"]show['"]|git\s+show\b""")
_LIVE_READ = re.compile(r'\bopen\s*\(|\bread\s*\(|\bread_text\s*\(|subprocess\.(run|check_output)|'
                        r'\bls-files\b|\bglob\b|\blive_|__file__')
_DIRECTIONAL = (ast.Lt, ast.Gt, ast.LtE, ast.GtE)


def seat_receipts():
    """every receipt whose source carries a `+60` revision stamp -- the scope, stated mechanically"""
    out = []
    for f in git('ls-files', 'receipts').split('\n'):
        if not f.endswith('.py'):
            continue
        try:
            src = open(os.path.join(ROOT, f), encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        if re.search(r'r\d{4}\+60\b', src):
            out.append((f, src))
    return out


def _targets(n):
    """every NAME a statement writes -- including a TUPLE target, which is what the first form missed:
    `_alt, _run_of, _runs = alt_runs()` binds three names and none of them is a bare `Name` target."""
    tg = []
    if isinstance(n, ast.Assign):
        tg = n.targets
    elif isinstance(n, (ast.AnnAssign, ast.AugAssign)):
        tg = [n.target]
    elif isinstance(n, (ast.For, ast.comprehension)):
        tg = [n.target]
    return [x.id for t in tg for x in ast.walk(t) if isinstance(x, ast.Name)]


def _bindings(tree, src, wide=False):
    """name -> {PINNED, LIVE, ''} from the source segment of what writes it.
    `wide=False` is FORM 1, kept for the record: single `Name` targets only, which is how the first
    detector was written and why it missed its own subject.  `wide=True` is FORM 2: every target shape,
    every writing statement, and the names each statement CONSUMES, so a kind can propagate."""
    out, consumes = {}, {}
    for n in ast.walk(tree):
        if not isinstance(n, (ast.Assign, ast.AnnAssign, ast.AugAssign, ast.For)):
            continue
        if not wide:
            if not (isinstance(n, ast.Assign) and len(n.targets) == 1
                    and isinstance(n.targets[0], ast.Name)) and not (
                    isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name)):
                continue
        names = _targets(n)
        if not names:
            continue
        val = n.value if not isinstance(n, ast.For) else n.iter
        if val is None:
            continue
        seg = ast.get_source_segment(src, val) or ''
        if wide and isinstance(n, ast.For):
            seg += '\n'.join(ast.get_source_segment(src, b) or '' for b in n.body)
        pin = bool(_PIN_READ.search(seg)) or bool(_SHA.search(seg))
        live = bool(_LIVE_READ.search(seg)) and not pin
        kind = 'PINNED' if pin else ('LIVE' if live else '')
        eaten = {x.id for x in ast.walk(val) if isinstance(x, ast.Name)}
        if wide and isinstance(n, ast.For):
            eaten |= {x.id for b in n.body for x in ast.walk(b) if isinstance(x, ast.Name)}
        for nm in names:
            out.setdefault(nm, set()).add(kind)
            consumes.setdefault(nm, set()).update(eaten - {nm})
    return out, consumes


def _reach(names, binds, consumes=None, depth=4):
    """the kinds a CONDITION consumes.  FORM 1 looks one hop; FORM 2 follows what each written name was
    built from, which is the hop `Ⓑ②` needs: its condition names only `_pairs`, a counter filled inside
    a loop over the live map."""
    kinds, seen, front = set(), set(), set(names)
    for _ in range(depth if consumes is not None else 1):
        nxt = set()
        for nm in front:
            if nm in seen:
                continue
            seen.add(nm)
            kinds |= binds.get(nm, set())
            if consumes is not None:
                nxt |= consumes.get(nm, set())
        front = nxt - seen
        if not front:
            break
    return kinds


def _writers(tree, src):
    """name -> (its own kinds, the names its WRITING statements consume).  A `for` contributes its
    `iter` and only the statements inside it that WRITE the name, never the whole body -- which is
    where FORM 2 over-reached, absorbing every name a loop mentions."""
    kinds, inputs = {}, {}

    def add(nm, seg, eaten):
        pin = bool(_PIN_READ.search(seg)) or bool(_SHA.search(seg))
        live = bool(_LIVE_READ.search(seg)) and not pin
        kinds.setdefault(nm, set()).add('PINNED' if pin else ('LIVE' if live else ''))
        inputs.setdefault(nm, set()).update(eaten - {nm})

    for n in ast.walk(tree):
        if isinstance(n, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            if n.value is None:
                continue
            seg = ast.get_source_segment(src, n.value) or ''
            eaten = {x.id for x in ast.walk(n.value) if isinstance(x, ast.Name)}
            for nm in _targets(n):
                add(nm, seg, eaten)
        elif isinstance(n, ast.For):
            it = ast.get_source_segment(src, n.iter) or ''
            iteaten = {x.id for x in ast.walk(n.iter) if isinstance(x, ast.Name)}
            for nm in _targets(n):
                add(nm, it, iteaten)
            # only the statements INSIDE that write a name carry the loop's iterable into that name --
            # ⛭ AND THE GUARD COUNTS: an increment inside `if any(... for b in _grp)` was BUILT FROM
            #   `_grp`, and a form that reads only the right-hand side `1` misses exactly that, which
            #   is how the first narrowing missed its own subject for the third time in this phase.
            guards = {}
            for b in n.body:
                for w in ast.walk(b):
                    if isinstance(w, ast.If):
                        gnames = {x.id for x in ast.walk(w.test) if isinstance(x, ast.Name)}
                        gseg = ast.get_source_segment(src, w.test) or ''
                        for inner in w.body + w.orelse:
                            for q in ast.walk(inner):
                                guards.setdefault(id(q), (set(), ''))
                                g0, s0 = guards[id(q)]
                                guards[id(q)] = (g0 | gnames, s0 + gseg)
            for b in n.body:
                for w in ast.walk(b):
                    if isinstance(w, (ast.Assign, ast.AugAssign, ast.AnnAssign)) and w.value is not None:
                        seg = ast.get_source_segment(src, w.value) or ''
                        eaten = {x.id for x in ast.walk(w.value) if isinstance(x, ast.Name)} | iteaten
                        g, gs = guards.get(id(w), (set(), ''))
                        eaten |= g
                        seg += gs
                        for nm in _targets(w):
                            add(nm, seg, eaten)
                    elif isinstance(w, ast.Call) and isinstance(w.func, ast.Attribute) \
                            and isinstance(w.func.value, ast.Name) and w.func.attr in ('append', 'add',
                                                                                       'extend', 'update'):
                        seg = ast.get_source_segment(src, w) or ''
                        eaten = {x.id for x in ast.walk(w) if isinstance(x, ast.Name)} | iteaten
                        add(w.func.value.id, seg, eaten)
    return kinds, inputs


def _mixes(nm, kinds, inputs, depth=2):
    """the kinds ONE derived name was built from -- its own writing statements plus, to `depth`, the
    names those consume.  The clause is flagged on a SINGLE name mixing, never on the union over every
    name the condition mentions, which is a shape counted where a use was meant."""
    seen, front, got = set(), {nm}, set()
    for _ in range(depth + 1):
        nxt = set()
        for x in front:
            if x in seen:
                continue
            seen.add(x)
            got |= kinds.get(x, set())
            nxt |= inputs.get(x, set())
        front = nxt - seen
        if not front:
            break
    return got


def census3():
    """FORM 3: a clause is mixed iff ONE name its condition consumes was itself built from both a
    pinned and a live source, within two hops of its own writing statements."""
    mixed, floors = [], []
    for f, src in seat_receipts():
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        kinds, inputs = _writers(tree, src)
        for n in ast.walk(tree):
            if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                    and n.func.id in ASSERTERS):
                continue
            claim = n.args[ASSERTERS[n.func.id]:]
            if not claim:
                continue
            names = {x.id for a in claim for x in ast.walk(a) if isinstance(x, ast.Name)}
            hits = sorted(nm for nm in names if {'PINNED', 'LIVE'} <= _mixes(nm, kinds, inputs))
            if not hits:
                continue
            cmps = [x for a in claim for x in ast.walk(a) if isinstance(x, ast.Compare)]
            floorish = []
            for cp in cmps:
                for op, rhs in zip(cp.ops, cp.comparators):
                    if isinstance(op, (ast.GtE, ast.Eq)) and isinstance(rhs, ast.Constant) \
                            and isinstance(rhs.value, int) and rhs.value >= 1:
                        floorish.append('FLOOR' if isinstance(op, ast.GtE) else 'EQUALITY')
            directional = any(isinstance(op, _DIRECTIONAL) for cp in cmps for op in cp.ops)
            rec = (f, n.lineno, hits, sorted(set(floorish)), directional)
            mixed.append(rec)
            if floorish:
                floors.append(rec)
    return mixed, floors


def census(wide=True):
    """(mixed, floors) -- asserting clauses whose CONDITION consumes both a pinned and a live binding,
    and the subset asserting a FLOOR or an EQUALITY on a count rather than a direction.  `wide=False`
    reproduces FORM 1, which is kept so the improvement is demonstrated rather than narrated."""
    mixed, floors = [], []
    for f, src in seat_receipts():
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        binds, consumes = _bindings(tree, src, wide=wide)
        for n in ast.walk(tree):
            if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                    and n.func.id in ASSERTERS):
                continue
            claim = n.args[ASSERTERS[n.func.id]:]          # LABEL vs CONDITION
            if not claim:
                continue
            names = {x.id for a in claim for x in ast.walk(a) if isinstance(x, ast.Name)}
            kinds = _reach(names, binds, consumes if wide else None)
            if not ({'PINNED', 'LIVE'} <= kinds):
                continue
            # FIGURE vs DIRECTION: a live read asserted as a direction or a ceiling is sound
            cmps = [x for a in claim for x in ast.walk(a) if isinstance(x, ast.Compare)]
            floorish = []
            for cp in cmps:
                for op, rhs in zip(cp.ops, cp.comparators):
                    if isinstance(op, ast.GtE) and isinstance(rhs, ast.Constant) \
                            and isinstance(rhs.value, int) and rhs.value >= 1:
                        floorish.append('FLOOR')
                    elif isinstance(op, ast.Eq) and isinstance(rhs, ast.Constant) \
                            and isinstance(rhs.value, int) and rhs.value >= 1:
                        floorish.append('EQUALITY')
            directional = any(isinstance(op, _DIRECTIONAL) for cp in cmps for op in cp.ops)
            rec = (f, n.lineno, sorted(names & set(binds)), sorted(set(floorish)), directional)
            mixed.append(rec)
            if floorish:
                floors.append(rec)
    return mixed, floors


# ⛭ FORM 4, the narrowing the registered ⒞ actually meant: the live end must be a DEFECT CENSUS -- the
#   output of an instrument run -- because "a count the work they watch drives to zero" is a count of
#   defects and not any live figure.  A live read of a paper or a ledger is not that.
_CENSUS_READ = re.compile(r'mutate_assertions|--quote|--prose|--cannot-fail|sweep_\w+|'
                          r'check_\w+\.py|alt_runs\s*\(')


def census4():
    """clauses asserting a FLOOR or an EQUALITY on a count ONE of whose inputs is an instrument run
    (a defect census, live) and another a pinned read -- the fail-on-success shape, mechanically"""
    out = []
    for f, src in seat_receipts():
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        kinds, inputs = _writers(tree, src)
        censusy = set()
        for n in ast.walk(tree):
            if isinstance(n, (ast.Assign, ast.AugAssign, ast.AnnAssign)) and n.value is not None:
                seg = ast.get_source_segment(src, n.value) or ''
                if _CENSUS_READ.search(seg):
                    censusy.update(_targets(n))
            elif isinstance(n, ast.For):
                seg = ast.get_source_segment(src, n.iter) or ''
                if _CENSUS_READ.search(seg):
                    censusy.update(_targets(n))
        if not censusy:
            continue
        for n in ast.walk(tree):
            if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
                    and n.func.id in ASSERTERS):
                continue
            claim = n.args[ASSERTERS[n.func.id]:]
            if not claim:
                continue
            names = {x.id for a in claim for x in ast.walk(a) if isinstance(x, ast.Name)}
            hit = []
            for nm in names:
                seen, front = set(), {nm}
                reach = set()
                for _ in range(3):
                    nxt = set()
                    for x in front:
                        if x in seen:
                            continue
                        seen.add(x)
                        reach.add(x)
                        nxt |= inputs.get(x, set())
                    front = nxt - seen
                if (reach & censusy) and 'PINNED' in _mixes(nm, kinds, inputs):
                    hit.append(nm)
            if not hit:
                continue
            cmps = [x for a in claim for x in ast.walk(a) if isinstance(x, ast.Compare)]
            fl = [('FLOOR' if isinstance(op, ast.GtE) else 'EQUALITY')
                  for cp in cmps for op, rhs in zip(cp.ops, cp.comparators)
                  if isinstance(op, (ast.GtE, ast.Eq)) and isinstance(rhs, ast.Constant)
                  and isinstance(rhs.value, int) and rhs.value >= 1]
            if fl:
                out.append((f, n.lineno, sorted(set(hit)), sorted(set(fl))))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--no-pinned', action='store_true')
    a = ap.parse_args()
    print(f'# r7402 (60) -- the gate that counted the repairs it ordered, at FRAME {FRAME}')
    print(f"# S37's own constants, read from its module tree: AFTER={AFTER} BEFORE={BEFORE} "
          f'STAMP={STAMP}')
    mine = mine_rows()
    print(f'# {len(mine)} rows carry that stamp in the baseline AT {AFTER}')

    t0 = time.time()
    la = live_alt()
    live_n, live_reached = pairs(mine, *la)
    t_live = time.time() - t0
    print()
    print(f'# LIVE  (the form the gate has now): pairs {live_n}, of which present as an arm at all '
          f'{live_reached} of {len(mine)}   [{t_live:.1f}s]')
    print('#   ⇒ a zero that is STRUCTURAL and not a measurement: if no pinned literal is a live arm,')
    print('#     every iteration continues and the count cannot be anything but zero.')

    if not a.no_pinned:
        t0 = time.time()
        pa = pinned_alt()
        pin_n, pin_reached = pairs(mine, *pa)
        t_pin = time.time() - t0
        print()
        print(f'# ⒜ PINNED (tree AND instrument at {AFTER}): pairs {pin_n}, present as an arm '
              f'{pin_reached} of {len(mine)}   (band 5-17, central 11)   [{t_pin:.1f}s]')
        print(f'#   the clause asserts >= 10, so at its own revision it is '
              f'{"SATISFIED" if pin_n >= 10 else "⛔ NOT SATISFIED"}')

    t0 = time.time()
    mixed, floors = census3()
    narrow, narrow_f = census(wide=False)
    wide2, wide2_f = census(wide=True)
    t_c = time.time() - t0
    print()
    print(f'# ⛔ FORM 1, kept for the record -- single `Name` targets, one hop: {len(narrow)} clause(s), '
          f'{len([m for m in narrow if m[0] == S37])} of them in S37 itself.')
    print('#   ⇒ THE FIRST FORM MISSED ITS OWN SUBJECT: `Ⓑ②`\'s live end arrives through a TUPLE target')
    print('#     (`_alt, _run_of, _runs = alt_runs()`) and its condition names only the counter those')
    print('#     three fill, so neither the target shape nor the one hop could reach it.')
    print(f'# ⛔ FORM 2 -- every target shape, four hops, a loop body absorbed whole: {len(wide2)} '
          f'clause(s).  OVER-COUNTS: a four-hop closure over a long receipt reaches some pinned read '
          f'and some live read from almost any name, which is a shape counted where a use was meant.')
    print(f'# ⒝ FORM 3, the measured one -- ONE name built from both provenances within two hops of '
          f'its own writing statements: {len(mixed)}   '
          f'(band 0-25, central 4)   [{t_c:.1f}s over {len(seat_receipts())} receipt(s)]')
    print(f'#   of those, asserting a FLOOR or an EQUALITY on a count: {len(floors)}')
    f4 = census4()
    print(f'# ⒞ FORM 4, the narrowing ⒞ actually meant -- a FLOOR or EQUALITY on a count one of whose '
          f'inputs is an INSTRUMENT RUN (a defect census, live) and another a pinned read: {len(f4)}   '
          f'(band 0-10, central 2)')
    for x in sorted(f4):
        print(f'#     {x[0].split("/")[-1][:58]}:{x[1]}  {",".join(x[2])}  {",".join(x[3])}')
    print(f'# ⒟ remaining in S37 itself: '
          f'{len([m for m in mixed if m[0] == S37])}   (point prediction 0 AFTER the repair)')
    print()
    print('# every mixed clause: receipt, line, the bindings its condition consumes, floor/equality, '
          'any directional comparison')
    for m in sorted(mixed):
        print('\t'.join((m[0], str(m[1]), ','.join(m[2]), ','.join(m[3]) or '-', str(m[4]))))


if __name__ == '__main__':
    main()
