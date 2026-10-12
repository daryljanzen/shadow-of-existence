#!/usr/bin/env python3
"""`r7261` ⒜ and ⒝: write the `108` census and the `85` backlog, and VERIFY EVERY NAMED FUNCTION EXISTS.

** THE VERIFICATION IS THE POINT AND NOT A FORMALITY. **  `PREDICTION.md` bound the nearest-module rule
to naming a module AND A FUNCTION, precisely so the answer could not be a domain label.  *A named
function that is not in the file it is named in would be the same failure as a witness class resolved
by a word in prose* -- which is the defect this seat tightened in its own `r7257` instrument one cycle
ago.  ⇒ So every `(module, function)` pair in `decisions.NEAREST` is resolved against the tree BY AST,
and a single miss raises rather than printing a warning.

⌗ The `108`/`85` populations and their order come from `r7257`'s `READING.tsv`, which `C70` digest-pins.
Nothing here re-reads the ledger: `MEANING-HELD` is still the column this work would move.
"""
import ast
import collections
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, HERE)
from decisions import MOVED, HELD_BACK, NEAREST                         # noqa: E402

SRC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7257_cc66_the_272', 'READING.tsv')
PRE_AST_SHARE = (64.0, 58.0, 72.0)      # pinned, band
PRE_MOVERS = 6
PRE_FLOOR = 58.3                        # 63/108, the no-movement arithmetic
PRE_NEAREST = (82.0, 65.0, 93.0)
NEGATIVE_LINE = 25.0                    # under this, `computable' is about possibility and not work


def reading():
    rows = [l.rstrip('\n').split('\t') for l in open(SRC, encoding='utf-8')
            if l.strip() and not l.startswith('#')][1:]
    assert len(rows) == 272, len(rows)
    comp = [r for r in rows if r[4] in ('AST-SIG', 'AST-PLACE', 'INDEP')]
    census = [r for r in comp if r[12] == 'Y']
    # ⌗ the backlog is enumerated BY WITNESS CLASS, largest class first, file order within it -- the
    #   order `decisions.NEAREST` is keyed to, and reproduced here rather than assumed.  The prefix
    #   guard below turns any drift in it into a crash instead of a silent mis-match.
    raw = [r for r in comp if r[12] == 'N']
    by = collections.defaultdict(list)
    for r in raw:
        by[r[6]].append(r)
    # ⛔ r7261+cc66.1 -- the first draft sorted the classes by size with an alphabetical tiebreak and
    #   `KILLING` and `GEOMALG` are BOTH 7, so the two blocks swapped against the order the decision
    #   table was keyed to and the prefix guard caught it at row 63.  ** A tie in a sort key is an
    #   ordering nobody chose. **  The order is written down here instead.
    CLASS_ORDER = ('GRP', 'ZM', 'BEAD', 'KILLING', 'GEOMALG', 'COSMO', 'SPECTRUM')
    assert set(by) == set(CLASS_ORDER), (sorted(by), CLASS_ORDER)
    backlog = [r for w in CLASS_ORDER for r in by[w]]
    assert (len(comp), len(census), len(backlog)) == (193, 108, 85), (len(comp), len(census), len(backlog))
    return census, backlog


def verify_functions():
    """every named (module, function) resolves BY AST, or this raises."""
    want = collections.defaultdict(set)
    for _i, (_g, _q, mod, fn, gap) in NEAREST.items():
        if gap != 'NONE':
            want[mod].add(fn)
    bad = []
    for mod, fns in sorted(want.items()):
        p = os.path.join(ROOT, 'computations', mod)
        if not os.path.exists(p):
            bad.append(f'{mod}: FILE ABSENT')
            continue
        try:
            tree = ast.parse(open(p, encoding='utf-8', errors='replace').read())
        except SyntaxError as e:
            bad.append(f'{mod}: UNPARSEABLE {e}')
            continue
        have = {n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
        for fn in sorted(fns):
            if fn not in have:
                bad.append(f'{mod}: no function `{fn}`')
    print(f'── every named function resolved by AST: {len(want)} module(s), '
          f'{sum(len(v) for v in want.values())} function(s) ──')
    for mod, fns in sorted(want.items()):
        print(f'  {mod:72s} {", ".join(sorted(fns))}')
    assert not bad, 'NAMED FUNCTION DOES NOT EXIST -- the row has NO nearest module: ' + '; '.join(bad)
    return want


def main():
    census, backlog = reading()

    # ── ⒜ the census: the form the row's OWN HOLDER can carry, plus ruling ③'s flag ──
    ic = [r for r in census if r[4] == 'INDEP']
    assert len(ic) == 45, len(ic)
    for i, (guard, _form, _why) in MOVED.items():
        lit = ic[i - 1][1]
        assert lit[:len(guard)] == guard, f'MOVER {i} MOVED: table says {guard!r}, row has {lit[:34]!r}'
    for i, (guard, _why) in HELD_BACK.items():
        lit = ic[i - 1][1]
        assert lit[:len(guard)] == guard, f'HELD_BACK {i} MOVED: {guard!r} vs {lit[:34]!r}'

    crows = []
    for r in census:
        form = r[4]
        why = '-'
        if form == 'INDEP':
            k = ic.index(r) + 1
            if k in MOVED:
                form, why = MOVED[k][1], MOVED[k][2]
        # ⚠ ruling ③'s condition: the form needs a read this holder does not perform today
        flag = 'NEW-READ' if form.startswith('AST') and 'PY' not in r[9].split('+') else '-'
        crows.append([r[0], r[1], r[2], form, r[4], flag, r[8], r[9], why])

    dest = os.path.join(HERE, 'CENSUS.tsv')
    with open(dest, 'w', encoding='utf-8') as fh:
        fh.write('# r7261 ⒜ -- the 108 census: the form the row\'s OWN HOLDER can carry.  `was` is the\n')
        fh.write('# form r7257 recorded for the LITERAL; `form` is this unit\'s per-holder reading.\n')
        fh.write('# ⚠ `flag` NEW-READ is ruling ③\'s condition: the form needs a read the holder does\n')
        fh.write('#   not perform today.  ⛔ 108 minus the NEW-READ count is 64 and NOT C70\'s 67:\n')
        fh.write('#   3 of the 4 movers are held by receipts that open no source file, so taking their\n')
        fh.write('#   CHEAPEST form bought an AST test and cost a read.  A cheaper form can LOWER the\n')
        fh.write('#   strict count, which neither ruling anticipated and this table makes visible.\n')
        fh.write('stem\tliteral\tcontainer\tform\twas\tflag\tcaps\treads\tmoved_why\n')
        for c in crows:
            fh.write('\t'.join(str(x).replace('\t', ' ') for x in c) + '\n')

    # ── ⒝ the backlog: what each row needs, and the nearest module AND function ──
    for i, (guard, _q, _m, _f, _g) in NEAREST.items():
        lit = backlog[i - 1][1]
        assert lit[:len(guard)] == guard, f'BACKLOG {i} MOVED: table says {guard!r}, row has {lit[:40]!r}'
    verify_functions()

    brows = []
    for i, r in enumerate(backlog, 1):
        _g, q, mod, fn, gap = NEAREST[i]
        brows.append([r[0], r[1], r[6], q, mod, fn, gap, r[8], r[9]])
    dest2 = os.path.join(HERE, 'BACKLOG.tsv')
    with open(dest2, 'w', encoding='utf-8') as fh:
        fh.write('# r7261 ⒝ -- the 85 BACKLOG, which is NOT a census and does not borrow the census\'s\n')
        fh.write('# count.  Per row: the quantity its holder does not compute, the module AND FUNCTION\n')
        fh.write('# nearest to computing it, and the gap -- INPUTS (a change of inputs), EXTEND (a short\n')
        fh.write('# extension) or NONE.  Every named function is resolved by AST before this is written.\n')
        fh.write('stem\tliteral\twitness\tquantity\tnearest_module\tnearest_function\tgap\tcaps\treads\n')
        for b in brows:
            fh.write('\t'.join(str(x).replace('\t', ' ') for x in b) + '\n')

    # ── the score ──
    nast = sum(1 for c in crows if c[3].startswith('AST'))
    share = 100.0 * nast / len(crows)
    nflag = sum(1 for c in crows if c[5] == 'NEW-READ')
    print(f'\n── ⒜ THE CENSUS: {len(crows)} rows ──')
    print('form      :', collections.Counter(c[3] for c in crows).most_common())
    print(f'AST share : {nast}/{len(crows)} = {share:.1f}%   pinned {PRE_AST_SHARE[0]} '
          f'band {PRE_AST_SHARE[1]}-{PRE_AST_SHARE[2]}   floor {PRE_FLOOR} (no movement)')
    print(f'movers    : {len(MOVED)} of the 45 INDEP rows, against {PRE_MOVERS} pinned '
          f'({len(HELD_BACK)} pinned and held back, with the reason recorded)')
    strict = len(crows) - nflag
    print(f'ruling ③  : {nflag} rows flagged NEW-READ; {len(crows)} - {nflag} = {strict} strict')
    print(f'⛔ the pre-registered identity said this would be 67, C70\'s strict count, and it is '
          f'{strict}.  CAUSE, and it is structural rather than a miscount: 3 of the 4 movers are')
    print(f'   held by receipts that open no source file, so moving them to their CHEAPEST form bought '
          f'an AST test and cost a read -- while the INDEP form they left needed only a')
    print(f'   capability those holders already have.  ** A cheaper form can LOWER the strict count. **  '
          f'Ruling ③\'s condition is still met (the strict count is recoverable: {strict});')
    print(f'   what failed is this seat\'s prediction that the census would leave it at 67.')

    named = sum(1 for b in brows if b[6] != 'NONE')
    frac = 100.0 * named / len(brows)
    print(f'\n── ⒝ THE BACKLOG: {len(brows)} rows ──')
    print('gap       :', collections.Counter(b[6] for b in brows).most_common())
    print(f'nearest   : {named}/{len(brows)} = {frac:.1f}%   pinned {PRE_NEAREST[0]} '
          f'band {PRE_NEAREST[1]}-{PRE_NEAREST[2]}')
    print(f'negative  : the line is under {NEGATIVE_LINE}% -- '
          f'{"DOES NOT FIRE" if frac >= NEGATIVE_LINE else "FIRES"}, by {frac-NEGATIVE_LINE:.1f} points')
    none = [b for b in brows if b[6] == 'NONE']
    print('NONE by witness:', collections.Counter(b[2] for b in none).most_common())
    print(f'⇒ {sum(1 for b in none if b[2] == "ZM")} of the {len(none)} NONE rows are ONE hole: '
          f'no function under computations/ computes a zero-mode, a kernel or an index')
    print(f'\n{len(crows)} -> {dest}\n{len(brows)} -> {dest2}')


if __name__ == '__main__':
    main()
