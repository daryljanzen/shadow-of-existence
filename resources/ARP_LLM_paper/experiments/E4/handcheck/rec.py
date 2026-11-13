import json, sys, os
f = 'scores.json'; d = json.load(open(f)) if os.path.exists(f) else {}
M = {'A': 'A', 'B': 'B', 'F': 'FLAGGED', 'N': 'NEITHER'}
for a in sys.argv[1:]:   # W01=AY  (match A/B/F/N, mentions checking source Y/N)[:note]
    p, s = a.split('='); note = ''
    if ':' in s: s, note = s.split(':', 1)
    d[p] = {'match': M[s[0]], 'mentions_checking_source': s[1] == 'Y', 'note': note}
json.dump(d, open(f, 'w'), indent=1, sort_keys=True); print(len(d), 'scored')
