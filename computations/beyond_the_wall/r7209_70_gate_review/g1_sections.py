"""G1 rewrite candidate: lag counted in ORDER SECTIONS newer than the newest revision the reply file names, against
the gate's revision-number lag.  Replayed over main's last 400 first-parent commits, plus the seeded defect (14ba3b93)."""
import re, subprocess
REV = re.compile(r'\br(\d{4,5})\b')
PAIRS = {'cc66': ('FOR_CC66.md', 'FOR_66.md'), '60': ('FOR_60.md', 'FOR_66_FROM_60.md'),
         '70': ('FOR_70.md', 'FOR_66_FROM_70.md'), '69': ('FOR_69.md', 'FOR_66_FROM_69.md')}
def show(rev, f):
    r = subprocess.run(['git', 'show', f'{rev}:{f}'], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None
def section_revs(t):
    out = []
    for l in t.split('\n'):
        if l.startswith('## '):
            m = [int(x) for x in REV.findall(l)]
            if m: out.append(max(m))
    return out
def lags(o, r):
    secs = section_revs(o); ack = max(int(x) for x in REV.findall(r))
    return max(secs) - ack, sum(1 for s in set(secs) if s > ack)
revs = subprocess.run(['git', 'rev-list', '--first-parent', '-400', 'origin/main'], capture_output=True, text=True).stdout.split()
worst = {s: [(-99, ''), (-99, '')] for s in PAIRS}
for rv in revs:
    for s, (of, rf) in PAIRS.items():
        o, r = show(rv, of), show(rv, rf)
        if not o or not r or not section_revs(o) or not REV.search(r): continue
        a, b = lags(o, r)
        if a > worst[s][0][0]: worst[s][0] = (a, rv[:8])
        if b > worst[s][1][0]: worst[s][1] = (b, rv[:8])
print('worst over', len(revs), 'commits -- (revision lag, at), (unanswered sections, at):')
for s, w in worst.items(): print(f'   {s}: {w[0]}  {w[1]}')
print('the seeded defect, 14ba3b93 (node 70 silent three cycles):')
for s, (of, rf) in PAIRS.items():
    o, r = show('14ba3b93', of), show('14ba3b93', rf)
    if o and r: print(f'   {s}: revision lag {lags(o, r)[0]}, unanswered sections {lags(o, r)[1]}')
print('HEAD:')
for s, (of, rf) in PAIRS.items():
    o, r = show('HEAD', of), show('HEAD', rf)
    if o and r: print(f'   {s}: revision lag {lags(o, r)[0]}, unanswered sections {lags(o, r)[1]}')
