#!/usr/bin/env python3
"""Build the 34 baseline rows, with every field taken from the instrument that owns it.

⛔ r7367 ④'s remedy, applied: no key, target or tier is re-derived here.  The key comes from
`quote()`'s own record, the verdict's validity from `check_quote_pins`' OWN `held_check`.
"""
import importlib.util, json, os, subprocess, sys

spec = importlib.util.spec_from_file_location('m', 'scripts/mutate_assertions.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
gspec = importlib.util.spec_from_file_location('g', 'corpus/check_quote_pins.py')
g = importlib.util.module_from_spec(gspec); gspec.loader.exec_module(g)

recs = {}
for r in m.quote('.'):
    k = (r['receipt'], r['lit'])
    if k in m._MINTED and k not in recs:
        recs[k] = r
print(f'instrument records for the selector: {len(recs)} of {len(m._MINTED)}', file=sys.stderr)

rstar = {}
try:
    rstar = {(x[0], x[1]): x[2] for x in g.live_targets()} if hasattr(g, 'live_targets') else {}
except Exception:
    pass

rows, unheld = [], []
for k in sorted(recs):
    r = recs[k]
    receipt, lit = k
    tier = r['tier']
    # the target is the instrument's, via the gate's own filer where exposed; else the frozen label
    target = rstar.get(k) or r.get('target')
    if not target:
        for ln in open('computations/beyond_the_wall/r7367_cc66_pricing_the_thirty_four/'
                       'thirty_four.tsv', encoding='utf-8'):
            if '\t' in ln and not ln.startswith('#'):
                c = ln.split('\t')
                if c[0] == receipt and ' '.join(json.loads(c[1]).split()) == lit:
                    target = c[2]
                    break
    shas = subprocess.run(['git', 'log', '--format=%H', '--', receipt],
                          capture_output=True, text=True).stdout.split()
    got = None
    for sha in shas:                      # newest first: the latest commit that satisfies H1-H5
        why = f'r7367+cc66: held at {sha[:12]} -- the clause is the pin\'s MEANING, minted by the ' \
              f'r7367 targeted route over the committed list of 34'
        if g.held_check(receipt, lit, target, tier, why) == '':
            got = (sha, why)
            break
    if got:
        rows.append((receipt, json.dumps(lit, ensure_ascii=False), target, tier, '',
                     g.MEANING_HELD, got[1]))
    else:
        first = g.held_check(receipt, lit, target, tier,
                             f'held at {shas[0]}') if shas else 'no commit touches the receipt'
        unheld.append((receipt, lit, target, tier, first))

print(f'HELD and validated by the gate\'s own held_check : {len(rows)}', file=sys.stderr)
print(f'could NOT be held                               : {len(unheld)}', file=sys.stderr)
for u in unheld:
    print(f'   [UNHELD] {u[0].split("/")[-1][:44]} | {u[1][:40]!r} | {u[2]}/{u[3]} | {u[4]}',
          file=sys.stderr)
for row in rows:
    print('\t'.join(row))
