"""Record hand scores: python3 rec.py Q01=110/VVIV[:note]  (flaws 1-3 found; then V/I per listed other problem, in order)"""
import json, os, sys
f = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scores.json'); d = json.load(open(f)) if os.path.exists(f) else {}
for a in sys.argv[1:]:
    p, s = a.split('=', 1); note = ''
    if ':' in s: s, note = s.split(':', 1)
    fl, ot = s.split('/')
    d[p] = {'flaws': [int(x) for x in fl], 'other_valid': [x == 'V' for x in ot], 'note': note}
json.dump(d, open(f, 'w'), indent=1, sort_keys=True); print(len(d), 'scored')
