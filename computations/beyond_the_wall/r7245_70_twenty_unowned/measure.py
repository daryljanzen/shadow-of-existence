"""r7245+70.1 -- S12's unowned bucket recomputed at HEAD, and for each site: its partition, its last writer (kind),
and its introducer (the first commit whose diff adds the comparison text)."""
import collections, json, os, re, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_exact_counts as E
git = lambda *a: subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True, errors='replace').stdout
parity = lambda s: 'no-rev' if re.match(r'\s*r(\d{4})', s) is None else ('EVEN' if int(re.match(r'\s*r(\d{4})', s).group(1)) % 2 == 0 else 'ODD')
rels = [p for p in git('ls-files', 'receipts/').split('\n') if p.endswith('.py')]
sites = []
for rel in rels:
    src = open(os.path.join(ROOT, rel), encoding='utf-8').read()
    for seg, part, line in E.sites_of(src):
        sites.append((rel, line, seg, part))
info = {}
for rel in {s[0] for s in sites}:
    sha = ln = None
    for row in git('blame', '--line-porcelain', '--', rel).split('\n'):
        p = row.split()
        if len(p) >= 3 and len(p[0]) == 40 and all(c in '0123456789abcdef' for c in p[0]):
            sha, ln = p[0], int(p[2])
        elif row.startswith('summary ') and ln is not None:
            info[(rel, ln)] = (sha, row[8:])
def kind(sha, subj):
    par = git('log', '-1', '--format=%P', sha).split()
    if len(par) > 1 or subj.lower().startswith('merge'): return 'MERGE'
    if re.match(r'\s*r\d{4}', subj): return 'REVISION'
    if re.search(r'\br\d{3,4}\b|c\d+\.\d+|cc?\d+\.\d+', subj): return 'REVISION-NO-HEAD-ID'
    return 'APPARATUS/OTHER'
out = []
for rel, line, seg, part in sites:
    sha, subj = info.get((rel, line), ('?', '?'))
    if parity(subj) != 'no-rev':
        continue
    date = git('log', '-1', '--format=%ad', '--date=short', sha).strip()
    # introducer: oldest commit whose patch adds a line containing the comparison's first 40 characters
    needle = seg[:40]
    intro = git('log', '--reverse', '--format=%h|%ad|%s', '--date=short', '-S', needle, '--', rel).split('\n')[0]
    ih, idate, isubj = (intro.split('|', 2) + ['', '', ''])[:3]
    out.append(dict(receipt=rel, line=line, comparison=seg, partition=part, last_sha=sha[:8], last_date=date,
                    last_subject=subj[:120], last_kind=kind(sha, subj), intro_sha=ih, intro_date=idate,
                    intro_subject=isubj[:120], intro_parity=parity(isubj) if isubj else '?'))
json.dump(out, open(os.path.join(os.path.dirname(__file__), 'unowned.json'), 'w'), indent=1, ensure_ascii=False)
print('claim-sites', len(sites), ' unowned', len(out))
print('partition', dict(collections.Counter(o['partition'] for o in out)))
print('last-writer kind', dict(collections.Counter(o['last_kind'] for o in out)))
print('introducer parity', dict(collections.Counter(o['intro_parity'] for o in out)))
print('last-writer dates', sorted({o['last_date'] for o in out}))
