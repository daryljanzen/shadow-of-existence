#!/usr/bin/env python3
"""dump --quote's full key set (receipt, literal, target, flags) as TSV, using the operator in scripts/ as it stands"""
import json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import mutate_assertions as M
rows = M.quote(ROOT)
seen = {}
for r in rows:
    seen.setdefault((r['receipt'], r['lit']), (r['target'], r['flags']))
for (rec, lit), (tg, fl) in sorted(seen.items()):
    print(f'{rec}\t{json.dumps(lit)}\t{tg}\t{fl}')
