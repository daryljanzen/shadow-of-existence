"""Candidate fix: an order section whose heading appears VERBATIM in another seat's order file is a broadcast, not an
order to this seat, and is not counted.  Lag = this seat's own (non-broadcast) sections newer than the newest revision
its reply file names.  Evaluated on the seeded defect, at HEAD, and over main's last 400 first-parent commits."""
import re, subprocess
REV = re.compile(r'\br(\d{4,5})\b')
PAIRS = {'cc66': ('FOR_CC66.md', 'FOR_66.md'), '60': ('FOR_60.md', 'FOR_66_FROM_60.md'),
         '70': ('FOR_70.md', 'FOR_66_FROM_70.md'), '69': ('FOR_69.md', 'FOR_66_FROM_69.md')}
def show(rev, f):
    r = subprocess.run(['git', 'show', f'{rev}:{f}'], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None
def heads(t): return [l.strip() for l in t.split('\n') if l.startswith('## ') and REV.search(l)]
def own_lag(rev):
    orders = {s: show(rev, p[0]) for s, p in PAIRS.items()}
    out = {}
    for s, (of, rf) in PAIRS.items():
        o, r = orders[s], show(rev, rf)
        if not o or not r or not REV.search(r): continue
        others = set(h for t, x in orders.items() if t != s and x for h in heads(x))
        ack = max(int(x) for x in REV.findall(r))
        own = [h for h in heads(o) if h not in others]
        out[s] = sum(1 for h in own if max(int(x) for x in REV.findall(h)) > ack)
    return out
print('seeded defect 14ba3b93:', own_lag('14ba3b93'))
print('HEAD:', own_lag('HEAD'))
revs = subprocess.run(['git', 'rev-list', '--first-parent', '-400', 'origin/main'], capture_output=True, text=True).stdout.split()
worst = {}
for rv in revs:
    for s, n in own_lag(rv).items():
        if n > worst.get(s, (-1, ''))[0]: worst[s] = (n, rv[:8])
print('worst own-section lag over', len(revs), 'commits:', worst)
