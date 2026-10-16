"""r7413+70: is the reads scope's 0-of-20 design or breakage?"""
import json, os, subprocess, sys
sys.path.insert(0, 'scripts'); import receipt_scope as rs
idx = rs.load('.')[0]
raw = json.load(open(rs.INDEX))['receipts']
traced = set()
for r, e in raw.items():
    traced |= {os.path.relpath(x) if os.path.isabs(x) else x for x in e.get('r', [])}
# R-a: deletes/renames in the same 20 revisions
log = subprocess.run(['git', 'log', '--first-parent', '--format=%h %s', '-300', 'origin/main'], capture_output=True, text=True).stdout.split('\n')
revs = [l.split(' ', 1)[0] for l in log if l and len(l.split(' ', 1)) > 1 and l.split(' ', 1)[1][:1] == 'r' and l.split(' ', 1)[1][1:2].isdigit()][:20]
dr = []
for c in revs:
    for l in subprocess.run(['git', 'diff', '--name-status', '-M', f'{c}~1', c], capture_output=True, text=True).stdout.split('\n'):
        if l[:1] in ('D', 'R'): dr.append((c, l))
print('R-a deletes/renames in 20 revisions:', len(dr), '; of those read by an index entry:',
      sum(1 for c, l in dr if l.split('\t')[1] in traced))
for c, l in dr[:6]: print('   ', c, l[:120])
# R-b: delete a traced read
rec_b, e_b = next((r, e) for r, e in raw.items() if e.get('r'))
f_b = sorted(e_b['r'])[0]; f_b = os.path.relpath(f_b) if os.path.isabs(f_b) else f_b
sc = rs.scope(idx, set(), {f_b}, set(), 'reads')
print('R-b delete', f_b, '->', len(sc), 'in reads scope; source receipt in it:', rec_b in sc)
# R-c: a glob member added (membership change)
rec_c, e_c = next(((r, e) for r, e in raw.items() if e.get('g')), (None, None))
if rec_c:
    pat = e_c['g'][0]; pat = os.path.relpath(pat) if os.path.isabs(pat) else pat
    import fnmatch
    member = pat.replace('*', 'zz_probe')
    sc = rs.scope(idx, set(), set(), {member}, 'reads')
    print('R-c add glob member', member, 'of', pat, '->', len(sc), '; source in it:', rec_c in sc)
# R-d: control
sc = rs.scope(idx, set(), {'no/such/file_read_by_nobody.txt'}, set(), 'reads')
print('R-d control ->', len(sc))
