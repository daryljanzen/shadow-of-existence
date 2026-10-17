#!/usr/bin/env python3
"""r7435+70 ④: run named_files.py's OWN definitions (its source up to the line where the run starts), at the tree
it ran on, and count what line 27 drops.  python3 measure.py WORKTREE_AT_r7287+70.2"""
import ast, json, os, sys
from concurrent.futures import ThreadPoolExecutor
W = sys.argv[1]
D = os.path.join(W, 'computations', 'beyond_the_wall', 'r7287_70_never_moved')
os.chdir(D); sys.path.insert(0, D)
src = open('named_files.py', encoding='utf-8').read()
head = src.split('\nrows = ', 1)[0]                     # the definitions; the run itself starts at `rows =`
ns = {'__name__': 'named_files_defs'}
exec(compile(head, 'named_files.py', 'exec'), ns)
BYBASE, TRACKED, N = ns['BYBASE'], ns['TRACKED'], ns['N']
tracked = set(TRACKED)


def bare(receipt):
    """every bare-basename string constant in the receipt: (constant, n tracked files with that basename)"""
    try:
        tree = ast.parse(open(os.path.join(N.ROOT, receipt), encoding='utf-8', errors='replace').read())
    except (SyntaxError, OSError):
        return {}
    out = {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) < 200:
            s = n.value.strip().lstrip('./')
            if s and s not in tracked and '/' not in s and '.' in s:
                out[s] = len(BYBASE.get(s, []))
    return out


def named_wide(receipt):
    """named() with line 27 widened: an ambiguous basename resolves to ALL its candidates"""
    base = set(ns['_orig_named'](receipt))
    for s, k in bare(receipt).items():
        if k >= 2:
            base.update(p for p in BYBASE[s] if p != receipt)
    return sorted(base)


ns['_orig_named'] = ns['named']
rows = [l.rstrip('\n').split('\t') for l in open('keys.tsv', encoding='utf-8') if not l.startswith('#')]
keys = [(r[1], json.loads(r[2]), r[3], r[4]) for r in rows if r[0] == 'REF']
recorded = {}
for l in open('keys_named.tsv', encoding='utf-8'):
    if l.startswith('#'):
        continue
    c = l.rstrip('\n').split('\t')
    recorded[(c[0], c[1])] = c[4]
consts = {}
touched = []
for k in keys:
    b = bare(k[0])
    consts.update({s: v for s, v in b.items()})
    if any(v >= 2 for v in b.values()):
        touched.append(k)
amb = sorted(s for s, v in consts.items() if v >= 2)
none = sorted(s for s, v in consts.items() if v == 0)
uniq = sorted(s for s, v in consts.items() if v == 1)
print(f'REF keys: {len(keys)}; distinct bare-basename constants in their receipts: {len(consts)} '
      f'(unique {len(uniq)}, AMBIGUOUS {len(amb)}, absent {len(none)})')
nonuniq = len(amb) + len(none)
print(f'N-a  ambiguous share of the not-unique: {len(amb)} of {nonuniq} = {100 * len(amb) / max(1, nonuniq):.1f} %'
      f'   (of ALL bare constants: {100 * len(amb) / max(1, len(consts)):.1f} %)')
print(f'N-b  REF keys whose receipt has >= 1 ambiguous bare constant: {len(touched)} of {len(keys)} = '
      f'{100 * len(touched) / max(1, len(keys)):.1f} %')
ns['named'] = named_wide                                 # classify() looks `named` up in its own globals
with ThreadPoolExecutor(4) as ex:
    wide = list(ex.map(lambda k: ns['classify'](k[:3])[0], touched))
changed = [(k, recorded.get((k[0], json.dumps(k[1], ensure_ascii=False))), w) for k, w in zip(touched, wide)
           if recorded.get((k[0], json.dumps(k[1], ensure_ascii=False))) != w]
print(f'N-c  of those {len(touched)}, keys whose class CHANGES when ambiguous names resolve to all candidates: {len(changed)}')
for k, was, now in changed:
    print(f'       {was} -> {now}   {k[0].split("/")[-1][:60]}   {json.dumps(k[1])[:50]}')
print('ambiguous constants (n files):', ', '.join(f'{s}({consts[s]})' for s in amb[:40]))
