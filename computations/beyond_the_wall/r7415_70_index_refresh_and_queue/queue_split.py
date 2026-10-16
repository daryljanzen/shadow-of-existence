"""r7415 ③: the r7383 queue.py measure, split at #463's merge (2026-10-16T01:07:54Z), plus the
queue-start time (run created -> fast job started) that separates waiting from running."""
import json, subprocess, statistics
from datetime import datetime
def api(p): return json.loads(subprocess.run(['gh','api',p],capture_output=True,text=True,check=True).stdout)
P = lambda s: datetime.fromisoformat(s.replace('Z','+00:00'))
CUT = P('2026-10-16T01:07:54Z')
wf = [w for w in api('repos/daryljanzen/shadow-of-existence/actions/workflows')['workflows'] if w['path'].endswith('gates.yml')][0]['id']
runs = api(f'repos/daryljanzen/shadow-of-existence/actions/workflows/{wf}/runs?branch=main&event=push&per_page=30')['workflow_runs']
rows = []
for r in runs:
    f = [j for j in api(f"repos/daryljanzen/shadow-of-existence/actions/runs/{r['id']}/jobs?per_page=30")['jobs'] if j['name'].startswith('fast')]
    c = P(r['created_at'])
    if not f or not f[0].get('completed_at'): rows.append((c, None, None, r['head_sha'][:8])); continue
    rows.append((c, (P(f[0]['started_at'])-c).total_seconds()/60, (P(f[0]['completed_at'])-c).total_seconds()/60, r['head_sha'][:8]))
for name, sel in (('before #463', [x for x in rows if x[0] < CUT]), ('after #463', [x for x in rows if x[0] >= CUT])):
    d = [x for x in sel if x[2] is not None]
    print(f'{name}: runs {len(sel)}, concluded {len(d)}')
    if d:
        print(f'  to fast complete: median {statistics.median(x[2] for x in d):.1f}, worst {max(x[2] for x in d):.1f}, best {min(x[2] for x in d):.1f}')
        print(f'  waiting (created -> fast started): median {statistics.median(x[1] for x in d):.1f}, worst {max(x[1] for x in d):.1f}')
    for x in sorted(sel): print('   ', x[0].strftime('%m-%d %H:%M'), x[3], 'wait', None if x[1] is None else round(x[1],1), 'done', None if x[2] is None else round(x[2],1))
