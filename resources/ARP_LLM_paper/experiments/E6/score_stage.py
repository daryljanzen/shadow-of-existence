"""E6 stage measure (registered r7759, before any aggregate was read): blind scoring of the version output at steps 1, 3
and 5 of every main-run chain, with run_e6's scorer prompt and receipt stripping.  Records are written under opaque ids
(stage_main/<id>.json); the condition/task/rep/step for each id is in stage_key.json.  Usage: python3 score_stage.py"""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'harness'))
from run_e6 import SCORER, ctx, strip_receipt  # noqa: E402
from subject import Trial, run_batch  # noqa: E402
tasks = {t['id']: t for t in json.load(open(os.path.join(HERE, 'materials', 'tasks.json')))}
jobs = [(c, tid, k, j) for c in ('S', 'G-ARP', 'G-noR') for tid in sorted(tasks) for k in range(2) for j in (1, 3, 5)]
ids = random.Random(6756).sample(range(10000, 99999), len(jobs)); kf = os.path.join(HERE, 'stage_key.json')
key = {f's{i}': dict(cond=c, task=tid, rep=k, step=j) for i, (c, tid, k, j) in zip(ids, jobs)}
json.dump(key, open(kf, 'w'), indent=1, sort_keys=True)
T = []
for sid, m in key.items():
    t = tasks[m['task']]
    v = json.load(open(os.path.join(HERE, 'runs_main', m['cond'], f"{m['task']}__r{m['rep']}", f"step{m['step']}.json")))['response']
    fl = '\n'.join(f"{f['f']}. [{f['type']}] {f['description']} CORRECTION: {f['correction']}" for f in t['flaws'])
    ext = '\n'.join(f"- {e}" for e in t['open_extensions'])
    T.append(Trial('E6', 'stage', sid, SCORER, f"{ctx(t)}KNOWN FLAWS:\n{fl}\n\nEXTENSIONS:\n{ext}\n\nFINAL VERSION:\n{strip_receipt(v)}",
                   os.path.join(HERE, 'stage_main', f'{sid}.json'), role='scorer'))
run_batch(T, workers=4)
