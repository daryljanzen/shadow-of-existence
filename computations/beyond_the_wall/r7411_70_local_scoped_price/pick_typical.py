"""r7411+70: suite/reads/tolerance scope sizes for the last 20 revision commits on main; pick the median."""
import subprocess, sys, statistics, time
sys.path.insert(0, 'scripts'); import receipt_scope as rs
t0 = time.time()
log = subprocess.run(['git', 'log', '--first-parent', '--format=%h %s', '-300', 'origin/main'], capture_output=True, text=True).stdout.split('\n')
revs = [l.split(' ', 1)[0] for l in log if l and l.split(' ', 1)[1:] and l.split(' ', 1)[1][:1] == 'r' and l.split(' ', 1)[1][1:2].isdigit()][:20]
idx = rs.load('.')[0]
rows = []
for c in revs:
    out = subprocess.run(['git', 'diff', '--name-status', '-M', f'{c}~1', c], capture_output=True, text=True).stdout
    changed, gone, added = set(), set(), set()
    for l in out.split('\n'):
        if not l: continue
        p = l.split('\t')
        st = p[0][0]
        if st == 'M': changed.add(p[1])
        elif st == 'A': added.add(p[1]); changed.add(p[1])
        elif st == 'D': gone.add(p[1])
        elif st == 'R': gone.add(p[1]); added.add(p[2]); changed.add(p[2])
    sz = {w: len(rs.scope(idx, set(changed), set(gone), set(added), w)) for w in ('suite', 'reads', 'tolerance')}
    rows.append((sz['suite'], c, sz))
    print(c, sz)
rows.sort()
med = rows[len(rows) // 2]
print('median suite scope', statistics.median(r[0] for r in rows), '-> typical revision', med[1], med[2])
print('wall', round(time.time() - t0, 1), 's')
