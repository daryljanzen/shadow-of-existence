import json, sys, os
f = 'scores.json'; d = json.load(open(f)) if os.path.exists(f) else {}
for a in sys.argv[1:]:   # Q01=VVVIV/AANNA[:note]   V valid I invalid ; A anticipated N not
    p, s = a.split('='); note = ''
    if ':' in s: s, note = s.split(':', 1)
    v, an = s.split('/'); assert len(v) == len(an), p
    d[p] = {'valid': [c == 'V' for c in v], 'anticipated': [c == 'A' for c in an], 'note': note}
json.dump(d, open(f, 'w'), indent=1, sort_keys=True); print(len(d), 'scored')
