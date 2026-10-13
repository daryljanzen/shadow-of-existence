#!/usr/bin/env python3
"""r7287+70.2, EXPLORATORY and run AFTER the registered negative fired (results.md): the same never-moved test, with a
key located only in the files its OWN receipt names (string constants in the receipt that are tracked paths or their
basenames), instead of _present_at's any-file-holding-the-literal rule.  Reference set only.  Writes keys_named.tsv."""
import ast, json, os, sys, time
from concurrent.futures import ThreadPoolExecutor
import never_moved as N

TRACKED = N.git(N.ROOT, 'ls-files').split('\n')
BYBASE = {}
for t in TRACKED:
    BYBASE.setdefault(os.path.basename(t), []).append(t)


def named(receipt):
    try:
        tree = ast.parse(open(os.path.join(N.ROOT, receipt), encoding='utf-8', errors='replace').read())
    except (SyntaxError, OSError):
        return []
    out = set()
    tracked = set(TRACKED)
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and len(n.value) < 200:
            s = n.value.strip().lstrip('./')
            if s in tracked:
                out.add(s)
            elif '/' not in s and s in BYBASE and len(BYBASE[s]) == 1:
                out.add(BYBASE[s][0])
    return sorted(p for p in out if p != receipt)


def classify(key):
    receipt, lit, target = key
    det = []
    for n in named(receipt):
        try:
            t = open(os.path.join(N.ROOT, n), encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        flat = N.Q._flat(t)
        if not (lit in t or lit in flat):
            continue
        nd = N.needle(lit, t)
        det.append((n, nd, N.moved_in(N.ROOT, n, nd) if len(nd) >= 3 else -1))
    cs = [c for _, _, c in det if c > 0]
    if not cs:
        return 'UNLOCATED', det
    return ('MOVED' if any(c >= 2 for c in cs) else 'NEVER'), det


rows = [l.rstrip('\n').split('\t') for l in open('keys.tsv', encoding='utf-8') if not l.startswith('#')]
keys = [(r[1], json.loads(r[2]), r[3], r[4]) for r in rows if r[0] == 'REF']
t0 = time.time()
with ThreadPoolExecutor(4) as ex:
    res = list(ex.map(lambda k: classify(k[:3]), keys))
with open('keys_named.tsv', 'w', encoding='utf-8') as fh:
    fh.write('# receipt\tliteral\ttarget\tverdict\tclass\tfiles\n')
    for k, (c, det) in zip(keys, res):
        fh.write('\t'.join([k[0], json.dumps(k[1], ensure_ascii=False), k[2], k[3], c,
                            ' | '.join(f'{n}:{c2}' for n, _, c2 in det)]) + '\n')
print(f'{len(keys)} keys in {time.time() - t0:.0f} s')
