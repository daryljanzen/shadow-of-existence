import json, sys, os
f = 'scores.json'; d = json.load(open(f)) if os.path.exists(f) else {}
V = {'A': 'ACCEPT', 'R': 'REJECT', 'O': 'OPEN', 'H': 'HEDGE'}
for a in sys.argv[1:]:   # V001=RN  (verdict letter, settled S/N)[:note]
    p, s = a.split('='); note = ''
    if ':' in s: s, note = s.split(':', 1)
    d[p] = {'verdict': V[s[0]], 'settled': s[1] == 'S', 'note': note}
json.dump(d, open(f, 'w'), indent=1, sort_keys=True); print(len(d), 'scored')
