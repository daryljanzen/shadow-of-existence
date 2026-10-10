#!/usr/bin/env python3
"""r7243+70.1 -- apply the EXTEND-LONG batch per PREDICTION.md, one receipt at a time, reverting any receipt whose
edit fails acceptance.  Writes ledger.json (one row per key: outcome and reason).  The baseline swap is a separate
step (swap_baseline.py) over the ledger's accepted keys, so the baseline is only touched once, consistently."""
import ast, io, json, os, re, subprocess, sys, tokenize
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import mutate_assertions as M

norm = lambda s: ' '.join(s.split())


def docstring_lines(src):
    t = ast.parse(src); out = set()
    for n in ast.walk(t):
        if isinstance(n, (ast.Module, ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)) and n.body:
            b = n.body[0]
            if isinstance(b, ast.Expr) and isinstance(b.value, ast.Constant) and isinstance(b.value.value, str):
                out.add((b.lineno, b.col_offset))
    return out


def render(tok, new):
    """write `new` in the quote style and prefix of the original token `tok`, or None if it cannot be"""
    m = re.match(r'(?i)^([rbuf]*)(\'\'\'|"""|\'|")', tok)
    pre, q = m.group(1), m.group(2)
    if 'f' in pre.lower() or 'b' in pre.lower():
        return None
    if 'r' in pre.lower():
        if q in new or new.endswith('\\') or ('\n' in new and len(q) == 1):
            pre = pre.replace('r', '').replace('R', '')
        else:
            return pre + q + new + q
    body = new.replace('\\', '\\\\').replace(q[0], '\\' + q[0])
    if len(q) == 1:
        body = body.replace('\n', '\\n')
    return pre + q + body + q


def edit(src, old, new):
    """replace every non-docstring STRING token whose value == old; return (new_src, n) or (None, 0)"""
    ds = docstring_lines(src)
    toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    lines = src.split('\n'); reps = []
    for tk in toks:
        if tk.type != tokenize.STRING or tk.start in ds:
            continue
        try:
            v = ast.literal_eval(tk.string)
        except Exception:
            continue
        if isinstance(v, str) and v == old:
            r = render(tk.string, new)
            if r is None:
                return None, 0
            reps.append((tk.start, tk.end, r))
    if not reps:
        return None, 0
    for (sl, sc), (el, ec), r in sorted(reps, reverse=True):
        assert sl == el
        L = lines[sl - 1]; lines[sl - 1] = L[:sc] + r + L[ec:]
    return '\n'.join(lines), len(reps)


def run(rec):
    p = subprocess.run([sys.executable, rec], cwd=ROOT, capture_output=True, text=True, timeout=900)
    return p.returncode


def keyed(rec, lit):
    rows = M.quote(ROOT, [os.path.join(ROOT, rec)])
    return any(r['lit'] == norm(lit) for r in rows)


def main(pre_ok):
    ext = json.load(open(os.path.join(HERE, 'extensions.json')))
    by = {}
    for o in ext:
        by.setdefault(o['receipt'], []).append(o)
    ledger = []
    for rec in sorted(by):
        keys = by[rec]
        todo = [o for o in keys if not o['divergent'] and o['b_verdict'] == 'DISCRIMINATING']
        for o in keys:
            if o['divergent']:
                ledger.append(dict(o, outcome='FAIL', reason='DIVERGENT: the sites need different extensions'))
            elif o['b_verdict'] != 'DISCRIMINATING':
                ledger.append(dict(o, outcome='FAIL', reason=f"NOT-DISCRIMINATING: acceptance (b), in the engine, read {o['b_verdict']}"))
        if not todo:
            continue
        if rec not in pre_ok:
            for o in todo:
                ledger.append(dict(o, outcome='FAIL', reason='PRE-RED: the receipt was not green before any edit'))
            continue
        path = os.path.join(ROOT, rec); orig = open(path, encoding='utf-8').read()
        # each key: try the collapsed extension, then the raw one if it differs; a key is kept only if the whole
        #   receipt still runs green with it and --quote keys it
        cur = orig
        for o in todo:
            got = None
            for cand in dict.fromkeys([norm(o['ext']), o['ext']]):
                if o['lit'] not in cand:
                    continue
                s2, n = edit(cur, o['lit'], cand)
                if s2 is None:
                    continue
                open(path, 'w', encoding='utf-8').write(s2)
                try:
                    rc = run(rec)
                except subprocess.TimeoutExpired:
                    rc = 'TIMEOUT'
                if rc == 0 and keyed(rec, cand):
                    got = (cand, n); cur = s2
                    break
                open(path, 'w', encoding='utf-8').write(cur)
            if got:
                ledger.append(dict(o, outcome='OK', new=got[0], n_tokens=got[1]))
            else:
                s2, _ = edit(cur, o['lit'], norm(o['ext']))
                reason = ('NO-TOKEN: no string token in the receipt equals the literal' if s2 is None and
                          edit(cur, o['lit'], o['lit'] + 'x')[0] is None else
                          'RED-AFTER: the receipt is not green with either form of the extension')
                ledger.append(dict(o, outcome='FAIL', reason=reason))
        open(path, 'w', encoding='utf-8').write(cur)
        json.dump(ledger, open(os.path.join(HERE, 'ledger.json'), 'w'), ensure_ascii=False, indent=1)
        print(f"  {sum(1 for x in ledger if x['receipt'] == rec and x['outcome'] == 'OK')}/{len(keys)}  {rec}", flush=True)
    json.dump(ledger, open(os.path.join(HERE, 'ledger.json'), 'w'), ensure_ascii=False, indent=1)
    import collections
    print('outcome:', dict(collections.Counter(x['outcome'] for x in ledger)))
    print('reasons:', dict(collections.Counter(x.get('reason', 'OK').split(':')[0] for x in ledger)))


if __name__ == '__main__':
    pre = [l.split() for l in open(sys.argv[1]) if l.strip() and l.strip() != 'DONE']
    main({p for rc, s, p in pre if rc == '0'})
