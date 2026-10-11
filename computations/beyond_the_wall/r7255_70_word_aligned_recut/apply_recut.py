#!/usr/bin/env python3
"""r7255+70.1 -- apply the word-aligned re-cuts: per receipt, token-edit every clipped literal to its re-cut (r7243's
`edit`, non-docstring string tokens only), run the receipt, require it green AND the new literal keyed by the
operator; otherwise revert that receipt.  Writes ledger.json.  The baseline re-key is swap.py's, over accepted keys."""
import importlib.util, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
spec = importlib.util.spec_from_file_location('ab', os.path.join(HERE, '..', 'r7243_70_extend_long_batch', 'apply_batch.py'))
AB = importlib.util.module_from_spec(spec); spec.loader.exec_module(AB)
cuts = json.load(open(os.path.join(HERE, 'recut.json')))
by = {}
for o in cuts:
    by.setdefault(o['receipt'], []).append(o)
ledger = []
for rec, keys in sorted(by.items()):
    path = os.path.join(ROOT, rec)
    src0 = open(path, encoding='utf-8').read()
    pre = AB.run(rec)
    src, notes = src0, []
    for o in keys:
        new, n = AB.edit(src, o['lit'], o['recut'])
        if new is None:
            notes.append((o, 'NOT-EDITABLE: no plain string token equals the literal'))
            continue
        src = new
        notes.append((o, f'edited {n} token(s)'))
    if src == src0:
        for o, why in notes:
            ledger.append(dict(receipt=rec, lit=o['lit'], recut=o['recut'], outcome='SKIPPED', why=why, pre=pre))
        continue
    open(path, 'w', encoding='utf-8').write(src)
    post = AB.run(rec)
    ok = post == 0 and all(AB.keyed(rec, o['recut']) for o, w in notes if w.startswith('edited'))
    if not ok:
        open(path, 'w', encoding='utf-8').write(src0)
    for o, why in notes:
        ledger.append(dict(receipt=rec, lit=o['lit'], recut=o['recut'], pre=pre, post=post,
                           outcome=('APPLIED' if ok and why.startswith('edited') else 'REVERTED' if why.startswith('edited') else 'SKIPPED'),
                           why=why if ok or not why.startswith('edited') else f'{why}; receipt rc={post} or new literal not keyed -- reverted'))
json.dump(ledger, open(os.path.join(HERE, 'ledger.json'), 'w'), ensure_ascii=False, indent=1)
import collections
print(collections.Counter(x['outcome'] for x in ledger), ' pre-red receipts:', sorted({os.path.basename(x['receipt'])[:40] for x in ledger if x['pre']}))
for x in ledger:
    if x['outcome'] != 'APPLIED':
        print('  ', x['outcome'], os.path.basename(x['receipt'])[:45], json.dumps(x['lit'])[:50], x['why'][:90])
