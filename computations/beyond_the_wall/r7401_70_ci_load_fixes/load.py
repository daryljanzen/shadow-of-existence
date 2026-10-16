"""r7401+70: 24 h of gates.yml runs -- job-minutes by event and job class, and branch pushes superseded."""
import json, subprocess, time
from datetime import datetime, timezone, timedelta
t0 = time.time()
R = 'repos/daryljanzen/shadow-of-existence'
def api(p): return json.loads(subprocess.run(['gh', 'api', p], capture_output=True, text=True, check=True).stdout)
P = lambda s: datetime.fromisoformat(s.replace('Z', '+00:00')) if s else None
wf = [w for w in api(f'{R}/actions/workflows')['workflows'] if w['path'].endswith('gates.yml')][0]['id']
now = datetime.now(timezone.utc); since = now - timedelta(hours=24)
runs, page = [], 1
while True:
    b = api(f'{R}/actions/workflows/{wf}/runs?per_page=100&page={page}&created=>={since:%Y-%m-%dT%H:%M:%SZ}')['workflow_runs']
    runs += b; page += 1
    if len(b) < 100: break
mins = {}            # (event, cls) -> job-minutes
per_run = {}
for r in runs:
    tot = 0.0
    for j in api(f"{R}/actions/runs/{r['id']}/jobs?per_page=30")['jobs']:
        s, c = P(j.get('started_at')), P(j.get('completed_at'))
        if not s or j.get('conclusion') == 'skipped': continue
        m = ((c or now) - s).total_seconds() / 60
        cls = 'scoped' if j['name'].startswith('scoped') else j['name'].split(' ')[0]
        mins[(r['event'], cls)] = mins.get((r['event'], cls), 0) + m
        if cls == 'scoped': tot += m
    per_run[r['id']] = tot
total = sum(mins.values())
pr_scoped = mins.get(('pull_request', 'scoped'), 0)
print(f'runs {len(runs)}  job-minutes {total:.0f}')
for k in sorted(mins): print(f'  {k[0]:13s} {k[1]:9s} {mins[k]:7.0f}')
print(f'P-a pull_request scoped share: {100*pr_scoped/total:.1f} %')
# branch push runs superseded: a later push run on the same ref was created before this run completed
br = [r for r in runs if r['event'] == 'push' and r['head_branch'] != 'main']
sup, saving = 0, 0.0
for r in br:
    later = [x for x in br if x['head_branch'] == r['head_branch'] and P(x['created_at']) > P(r['created_at'])]
    if not later: continue
    nxt = min(P(x['created_at']) for x in later)
    end = P(r['updated_at']) if r['status'] == 'completed' else now
    if nxt < end:
        sup += 1
        # minutes this run's scoped jobs spent after the superseding push: approximate by the run's share after nxt
        start = P(r['run_started_at'] or r['created_at'])
        frac = max(0.0, (end - max(nxt, start)).total_seconds()) / max(1.0, (end - start).total_seconds())
        saving += per_run[r['id']] * frac
print(f'P-b branch push runs superseded: {sup} of {len(br)} = {100*sup/max(1,len(br)):.1f} %')
post = total - pr_scoped
print(f'P-c (2) saving after (1): {saving:.0f} of {post:.0f} job-min = {100*saving/max(1,post):.1f} %')
print(f'P-d wall {time.time()-t0:.1f} s')
