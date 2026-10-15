#!/usr/bin/env python3
"""dump every quote-pin key with the FILE KINDS its narrow and wide traces name.
r7345+cc66, step one of the container-gated hop: read what the containers actually are."""
import importlib.util, json, sys

path, root = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location('m', path)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
rows = m.quote(root)
seen = {}
for r in rows:
    k = (r['receipt'], r['lit'])
    narrow = sorted(set(m._EXT.findall(r.get('_trace') or '')))
    if k in seen:                      # a key's sites union, as _rstar does
        seen[k][0].update(narrow); seen[k][1].update(r['_kinds'])
    else:
        seen[k] = [set(narrow), set(r['_kinds']), r['target'], r['tier'], r['flags']]
for (rc, lit), (nk, wk, tg, tr, fl) in sorted(seen.items()):
    print('\t'.join([rc, json.dumps(lit), tg, tr, fl,
                     ','.join(sorted(nk)) or '-', ','.join(sorted(wk)) or '-']))
