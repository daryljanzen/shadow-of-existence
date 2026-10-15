import json, subprocess, time, statistics
from datetime import datetime, timezone
t0 = time.time()
def api(p): return json.loads(subprocess.run(['gh','api',p],capture_output=True,text=True,check=True).stdout)
wf = [w for w in api('repos/daryljanzen/shadow-of-existence/actions/workflows')['workflows'] if w['path'].endswith('gates.yml')][0]['id']
runs = api(f'repos/daryljanzen/shadow-of-existence/actions/workflows/{wf}/runs?branch=main&event=push&per_page=30')['workflow_runs']
now = datetime.now(timezone.utc)
P = lambda s: datetime.fromisoformat(s.replace('Z','+00:00'))
done, never = [], []
for r in runs:
    jobs = api(f"repos/daryljanzen/shadow-of-existence/actions/runs/{r['id']}/jobs?per_page=30")['jobs']
    f = [j for j in jobs if j['name'].startswith('fast')]
    c = P(r['created_at'])
    if f and f[0].get('completed_at'):
        done.append(((P(f[0]['completed_at'])-c).total_seconds()/60, r['head_sha'][:8], r['created_at'], f[0]['conclusion']))
    else:
        never.append((r['head_sha'][:8], r['created_at'], r['status'], round((now-c).total_seconds()/60)))
d = sorted(x[0] for x in done)
print('runs', len(runs), 'concluded', len(done), 'never', len(never))
print('median min', round(statistics.median(d),1), 'worst', round(max(d),1), 'best', round(min(d),1))
print('window', runs[-1]['created_at'], '->', runs[0]['created_at'])
for x in sorted(done, key=lambda x:-x[0])[:5]: print('  slow', round(x[0],1), x[1:])
for x in never: print('  never', x)
print('wall s', round(time.time()-t0,1))
