"""Record hand scores: python3 rec.py H01=1101/110/0[:note]  (flaws 1-4 corrected, extensions, introduced errors)"""
import json, os, sys
f = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scores.json'); d = json.load(open(f)) if os.path.exists(f) else {}
for a in sys.argv[1:]:
    p, s = a.split('=', 1); note = ''
    if ':' in s: s, note = s.split(':', 1)
    c, e, i = s.split('/')
    d[p] = {'corrected': [int(x) for x in c], 'extensions': [int(x) for x in e], 'introduced_errors': int(i), 'note': note}
json.dump(d, open(f, 'w'), indent=1, sort_keys=True); print(len(d), 'scored')
