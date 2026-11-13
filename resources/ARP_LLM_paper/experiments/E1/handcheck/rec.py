import json, sys, os
f = 'scores.json'; d = json.load(open(f)) if os.path.exists(f) else {}
for a in sys.argv[1:]:
    p, s = a.split('='); note = ''
    if ':' in s: s, note = s.split(':', 1)
    d[p] = {'scores': {str(i + 1): int(c) for i, c in enumerate(s)}, 'note': note}
json.dump(d, open(f, 'w'), indent=1, sort_keys=True); print(len(d), 'scored')
