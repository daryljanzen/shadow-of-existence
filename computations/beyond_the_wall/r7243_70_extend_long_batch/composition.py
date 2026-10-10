"""composition only: how many of the 295 keys have more than one wrap-tolerant site.  No extension is computed."""
import json, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'r7223_70_detector_blindnesses'))
import r1_wrap as W
W.paper_half(); W.source_half()
batch = json.load(open(os.path.join(HERE, 'batch_inputs.json')))
c = collections.Counter(); miss = 0
for half, rec, lit, D in batch:
    key = ('P' if half == 'PAPER' else 'S', rec, lit)
    if key not in W.SITES:
        miss += 1; continue
    n = len(W.SITES[key][1]); c[(half, 'multi' if n > 1 else 'single')] += 1
print(dict(c), 'not found in SITES', miss)
