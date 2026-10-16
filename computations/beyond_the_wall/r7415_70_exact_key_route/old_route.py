#!/usr/bin/env python3
"""r7415+70 ④ -- THE REFERENCE: `check_quote_pins._present_at` per row, as cc66's census calls it, one verdict a
row written out so the new route is compared row by row.   python3 -I old_route.py OUT.tsv [--target T]"""
import importlib.util, json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rows import rows  # noqa: E402
spec = importlib.util.spec_from_file_location('g', 'corpus/check_quote_pins.py')
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
out = sys.argv[1]
tgt = sys.argv[sys.argv.index('--target') + 1] if '--target' in sys.argv else ''
R = [r for r in rows() if not tgt or r[2] == tgt]
head = g._git('rev-parse', os.environ.get('SHA', 'HEAD')).stdout.strip()   # pinned, so a commit mid-run moves nothing
t0 = time.time(); per = {}
with open(out, 'w', encoding='utf-8') as f:
    f.write(f'# old route at {head} over {len(R)} row(s)\n')
    for i, (rc, lit, target, tier, verdict) in enumerate(R):
        t = time.time()
        p = g._present_at(head, lit, target, rc)
        per[target] = per.get(target, 0.0) + time.time() - t
        f.write(f'{i}\t{target}\t{int(p)}\t{rc}\t{json.dumps(lit, ensure_ascii=False)}\n'); f.flush()
    f.write(f'# WALL {time.time() - t0:.1f}s ' + ' '.join(f'{k}={v:.1f}s' for k, v in sorted(per.items())) + '\n')
