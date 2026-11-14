"""Post-hoc sensitivity check (stated in RESULT.md as a deviation, written before its outcome was read): the hand-check gave
T7 'contaminates' kappa 0.26, the hand reading finding more contamination than the scorer.  All 160 T7 responses are
re-scored blind under the same question (SC_T7), in 4 shuffled batches of 40 with opaque ids; arms go to T7KEY.json."""
import glob, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); E7 = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, E7); import run_e7 as R  # noqa: E402
recs = sorted(glob.glob(os.path.join(E7, 'scores_main', 'T7', '*', 's*.json'))); rnd = random.Random(7780); rnd.shuffle(recs); key = {}
open(os.path.join(HERE, 'QUESTION.txt'), 'w').write(R.SC_T7 + '\n')
for i, f in enumerate(recs):
    b = i // 40 + 1; d = os.path.join(HERE, f'batch{b}'); os.makedirs(d, exist_ok=True); p = f'X{i + 1:03d}'
    open(os.path.join(d, p + '.txt'), 'w').write(json.load(open(f))['message'] + '\n')
    key[p] = dict(arm=f.split(os.sep)[-2], seat=os.path.basename(f)[:-5])
json.dump(key, open(os.path.join(HERE, 'T7KEY.json'), 'w'), indent=1); print(len(key))
