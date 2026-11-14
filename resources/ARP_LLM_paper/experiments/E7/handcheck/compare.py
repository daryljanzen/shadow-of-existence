"""E7 hand-check comparison (run only after hand/*.json is committed).  Agreement and Cohen's kappa per scored field,
pooled and by disposition.  T3: flaws found, and valid/invalid per scorer-listed problem."""
import json, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); KEY = json.load(open(os.path.join(HERE, 'KEY.json')))

def kappa(pairs):
    n = len(pairs)
    if not n: return None, None
    po = sum(a == b for a, b in pairs) / n; ca = collections.Counter(a for a, _ in pairs); cb = collections.Counter(b for _, b in pairs)
    pe = sum(ca[c] * cb[c] for c in set(ca) | set(cb)) / n / n
    return po, (None if pe == 1 else (po - pe) / (1 - pe))

def fields(k, s, h):
    out = []
    if k == 'R':
        out += [(f'instr', s[str(i)], h[str(i)]) for i in range(1, 7)] + [('manipulation', s['manipulation'], h['manipulation'])]
    elif k == 'Pc':
        out += [('status', s[str(i)]['status'], h[str(i)]['status']) for i in range(1, 7)]
        out += [('cites_reading', s[str(i)].get('cites_reading'), h[str(i)].get('cites_reading')) for i in range(1, 7)
                if s[str(i)]['status'] == 'rejected' and h[str(i)]['status'] == 'rejected']
    elif k == 'T1':
        for kk in set(s) & set(h):
            if kk != 'note' and not isinstance(s[kk], (dict, list)): out.append((kk, s[kk], h[kk]))
        for kk in set(s) & set(h):
            if isinstance(s[kk], dict) and isinstance(h[kk], dict):
                for j in set(s[kk]) & set(h[kk]): out.append((f'{kk}', s[kk][j], h[kk][j]))
    elif k == 'T3':
        out += [('flaw', s['flaws'][f], h['flaws'][f]) for f in ('1', '2', '3')]
        out += [('other_valid', o['valid'], h['other_valid'].get(f'O{i + 1}')) for i, o in enumerate(s.get('other', []))]
        out += [(f, s[f], h[f]) for f in ('refers_to_author_description', 'endorses')]
    else:
        out += [(f, s[f], h[f]) for f in s if f != 'note' and f in h]
    return out

rows = collections.defaultdict(list); missing = []
for k in ('R', 'Pa', 'Pc', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7'):
    H = json.load(open(os.path.join(HERE, 'hand', k + '.json')))
    for p, meta in KEY.items():
        if not p.startswith(k + '_'): continue
        if meta['scorer'] is None or p not in H: missing.append(p); continue
        d = meta['arm'].rsplit('_', 1)[1]
        for f, a, b in fields(k, meta['scorer'], H[p]):
            rows[(k, f, 'all')].append((a, b)); rows[(k, f, d)].append((a, b))
print('missing:', missing)
print(f"{'kind':5} {'field':30} {'n':>4} {'agree':>6} {'kappa':>6}  | sound n/agree/kappa | unsound n/agree/kappa")
for (k, f, d) in sorted(rows):
    if d != 'all': continue
    line = f'{k:5} {f:30}'
    for dd in ('all', 'sound', 'unsound'):
        po, kp = kappa(rows[(k, f, dd)])
        line += f" {len(rows[(k, f, dd)]):4} {po if po is not None else float('nan'):6.3f} {('%.2f' % kp) if kp is not None else ' undef':>6} |"
    print(line)
# disagreement listing
for (k, f, d), pr in sorted(rows.items()):
    if d == 'all':
        dis = collections.Counter((str(a), str(b)) for a, b in pr if a != b)
        if dis: print(k, f, 'scorer->hand', dict(dis))
