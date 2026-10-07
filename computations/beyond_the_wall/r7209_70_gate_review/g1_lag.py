"""G1: (a) replay check_order_acknowledged's lag over main's last 400 commits; (b) at HEAD, newest revision in a
reply HEADING against newest revision ANYWHERE in the reply file, per seat."""
import re, subprocess, sys
REV = re.compile(r'\br(\d{4,5})\b')
PAIRS = {'cc66': ('FOR_CC66.md', 'FOR_66.md'), '60': ('FOR_60.md', 'FOR_66_FROM_60.md'),
         '70': ('FOR_70.md', 'FOR_66_FROM_70.md'), '69': ('FOR_69.md', 'FOR_66_FROM_69.md')}
def show(rev, f):
    r = subprocess.run(['git', 'show', f'{rev}:{f}'], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None
def heads(t): return [int(m.group(1)) for l in t.split('\n') if l.startswith('## ') for m in REV.finditer(l)]
def anywhere(t): return [int(m.group(1)) for m in REV.finditer(t)]
revs = subprocess.run(['git', 'rev-list', '--first-parent', '-400', 'origin/main'], capture_output=True, text=True).stdout.split()
worst = {s: (None, None) for s in PAIRS}
for rv in revs:
    for s, (of, rf) in PAIRS.items():
        o, r = show(rv, of), show(rv, rf)
        if not o or not r or not heads(o) or not anywhere(r): continue
        lag = max(heads(o)) - max(anywhere(r))
        if worst[s][0] is None or lag > worst[s][0]: worst[s] = (lag, rv[:8])
print('(a) worst lag over', len(revs), 'first-parent commits of main:', {s: w for s, w in worst.items()})
print('(b) at HEAD -- newest revision in a reply HEADING vs ANYWHERE in the reply file:')
for s, (of, rf) in PAIRS.items():
    o, r = show('HEAD', of), show('HEAD', rf)
    if not r: print(f'   {s}: no reply file'); continue
    rh = [int(m.group(1)) for l in r.split('\n') if l.startswith('## ') for m in REV.finditer(l)]
    print(f'   {s}: order {max(heads(o))}; reply heading {max(rh) if rh else None}; anywhere {max(anywhere(r))}'
          + ('   <- closed by a MENTION, not a reply' if rh and max(anywhere(r)) > max(rh) else ''))
