#!/usr/bin/env python3
"""per-SITE container kinds for every quote-pin row, r7345+cc66."""
import importlib.util, json, sys
path, root = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location('m', path)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for r in m.quote(root):
    narrow = sorted(set(m._EXT.findall(r.get('_trace') or '')))
    print("\t".join([r["receipt"], json.dumps(r["lit"]), r["site"], r['target'], r['tier'],
                     r['flags'], ','.join(narrow) or '-', ','.join(r['_kinds']) or '-',
                     ' '.join((r.get('_trace') or '').split('\n')[0].split())[:90]]))
