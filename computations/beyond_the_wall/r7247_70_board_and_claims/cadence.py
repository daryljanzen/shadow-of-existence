"""r7247+70.1 -- seat cadence on the quote-pin backlog: every commit reachable from HEAD that LOWERED the unverdicted
count of corpus/quote_pin_baseline.tsv, its seat and its trunk revision; then the gaps, in order cycles (two revision
numbers), between successive lowering commits of the same seat."""
import collections, json, os, re, subprocess
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
git = lambda *a: subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True, errors='replace').stdout
UNV = {'UNADJUDICATED', 'UNADJUDICATED-LIST', 'UNADJUDICATED-PINNED'}
def unverdicted(sha):
    n = 0
    for l in git('show', f'{sha}:corpus/quote_pin_baseline.tsv').split('\n'):
        if l.strip() and not l.startswith('#'):
            f = l.split('\t')
            if len(f) > 5 and f[5] in UNV: n += 1
    return n
def seat(subj):
    m = re.search(r'r\d{4}\+(cc66|70|60|69|66)\.', subj)
    if m: return m.group(1)
    m = re.match(r'\s*r(\d{4})', subj)
    if m: return '60' if int(m.group(1)) % 2 == 0 else '66'
    return '?'
def rev(subj):
    m = re.search(r'r(\d{4})', subj); return int(m.group(1)) if m else None
rows = []
for ln in git('log', '--no-merges', '--format=%H%x09%P%x09%s', '--', 'corpus/quote_pin_baseline.tsv').split('\n'):
    if not ln: continue
    h, parents, s = ln.split('\t', 2)
    par = parents.split()[0] if parents else None
    if not par: continue
    try:
        a, b = unverdicted(par), unverdicted(h)
    except Exception:
        continue
    if b < a:
        rows.append(dict(sha=h[:8], seat=seat(s), rev=rev(s), drop=a - b, subj=s[:90]))
rows.sort(key=lambda r: (r['rev'] or 0))
print('lowering commits', len(rows), dict(collections.Counter(r['seat'] for r in rows)))
for r in rows: print(f"  r{r['rev']} {r['seat']:5s} -{r['drop']:<4d} {r['subj'][:70]}")
gaps = {}
for s in {r['seat'] for r in rows}:
    rv = sorted({r['rev'] // 2 for r in rows if r['seat'] == s and r['rev']})
    gaps[s] = [b - a for a, b in zip(rv, rv[1:])]
print('gaps in order cycles, per seat:', gaps)
json.dump(dict(rows=rows, gaps=gaps), open(os.path.join(os.path.dirname(__file__), 'cadence.json'), 'w'), indent=1)
