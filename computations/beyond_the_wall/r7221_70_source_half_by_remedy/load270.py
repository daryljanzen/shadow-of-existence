#!/usr/bin/env python3
"""Run S8's own source, unmodified, through its section D, and return its namespace.  Then re-walk S8's verdict
rule per key with S8's own functions, and require the tallies to equal S8's ST on every bucket."""
import collections, contextlib, io, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
S8 = os.path.join(ROOT, 'receipts/L_probability/S8_the_source_half_is_the_blinder_one_and_the_class_is_mostly_a_receipt_pinning_a_ledger_not_another_receipt.py')


def load():
    src = open(S8, encoding='utf-8').read()
    src = src[:src.index('head("E. THE COMPARISON')].replace('print(__doc__)', '')
    ns = {'__file__': S8, '__name__': 's8'}
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src, S8, 'exec'), ns)
    assert all(ok for _, ok in ns['CHECKS']), [n for n, ok in ns['CHECKS'] if not ok]
    return ns


def per_key(ns):
    """S8's measure(), unchanged in rule, keeping every key's prose sites and status"""
    SRC, MARKUP, SITE_CAP = ns['SRC'], ns['MARKUP'], ns['SITE_CAP']
    t, keys = collections.Counter(), []
    for rec, lit, tier, flags, verdict in ns['SOURCE_ROWS']:
        if MARKUP.search(lit):
            t['MARKUP'] += 1; continue
        own = SRC.get(rec, '').count(lit)
        hits = ns['files_with'](lit, SITE_CAP + own + 1)
        sites = []
        for p in dict.fromkeys(hits):
            if p == rec:
                continue
            k = SRC[p].find(lit)
            while k >= 0:
                sites.append((p, k)); k = SRC[p].find(lit, k + 1)
        if len(sites) > SITE_CAP:
            t['SATURATED'] += 1; continue
        if not sites:
            t['ABSENT'] += 1; continue
        pros = [s for s in sites if ns['is_prose'](*s)]
        if not pros:
            t['CODE'] += 1; continue
        allsurv, anysurv, moved, used = True, False, 0, []
        for p, off in pros:
            c = ns['clause_at'](SRC[p], off, off + len(lit))
            if lit not in c:
                continue
            used.append((p, off))
            for name, fl in ns['reversals'](c).items():
                moved += 1
                if lit in fl: anysurv = True
                else: allsurv = False
        if moved == 0: st = 'UNFLIPPABLE'
        elif allsurv: st = 'REVERSAL'
        elif anysurv: st = 'REVERSAL-PARTIAL'
        else: st = 'DISCRIMINATING'
        t[st] += 1
        if st in ('REVERSAL', 'REVERSAL-PARTIAL'):
            keys.append((rec, lit, st, used))
    for k in ('DISCRIMINATING', 'REVERSAL', 'REVERSAL-PARTIAL', 'CODE', 'UNFLIPPABLE', 'MARKUP', 'ABSENT', 'SATURATED'):
        assert t[k] == ns['ST'][k], (k, t[k], ns['ST'][k])
    return t, keys


if __name__ == '__main__':
    ns = load()
    t, keys = per_key(ns)
    print(dict(t)); print(len(keys), 'keys;', collections.Counter(k[2] for k in keys))
