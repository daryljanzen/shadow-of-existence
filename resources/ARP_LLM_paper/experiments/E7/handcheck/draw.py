"""E7 hand-check draw (registered r7779, before any main-run score was read): 4 seats per arm (32 of 160, 20%), seed 7779.
For each drawn seat, every scorer judgment feeding a reported measure (R, Pa, Pc, T1-T7; Pb is non-informative by
construction) becomes one packet holding exactly what the scorer saw, under an opaque id, grouped by kind and shuffled.
T3 packets also list the scorer's other problems with the valid marks removed.  Arm, seat and scorer verdict go to
KEY.json, opened only after scores.json is committed."""
import glob, json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); E7 = os.path.dirname(HERE); sys.path.insert(0, E7)
import run_e7 as R  # noqa: E402
KINDS = ('R', 'Pa', 'Pc', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7')
PROMPT = {'R': R.SC_R, 'Pa': R.SC_A, 'Pc': R.SC_C, 'T1': R.R1.SCORER, 'T2': R.SC_T2, 'T3': R.R3.SCORER,
          'T4': R.SC_T4, 'T5': R.SC_T5, 'T6': R.SC_T6, 'T7': R.SC_T7}
rnd = random.Random(7779); seats = []
for arm in R.ARMS:
    done = sorted(os.path.basename(d) for d in glob.glob(os.path.join(E7, 'runs_main', arm, 's*'))
                  if os.path.exists(os.path.join(d, f'turn{R.NFINAL}.json')))
    seats += [(arm, s) for s in rnd.sample(done, 4)]
key = {}
for k in KINDS:
    items = seats[:]; rnd.shuffle(items); d = os.path.join(HERE, 'packets', k); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'QUESTION.txt'), 'w').write(PROMPT[k] + '\n')
    for n, (arm, s) in enumerate(items, 1):
        f = os.path.join(E7, 'scores_main', k, arm, s + '.json'); r = json.load(open(f)); p = f'{k}_{n:02d}'
        m = re.search(r'\{.*\}', r['response'].replace('"{"issue"', '{"issue"'), re.S); sc = json.loads(m.group(0)) if m else None
        body = r['message']
        if k == 'T3' and sc:
            body += '\n\nOTHER PROBLEMS LISTED BY THE SCORER (mark each valid or invalid):\n' + '\n'.join(
                f'  O{i + 1}. {o["issue"]}' for i, o in enumerate(sc.get('other', [])))
        open(os.path.join(d, p + '.txt'), 'w').write(body + '\n')
        key[p] = dict(arm=arm, seat=s, record=os.path.relpath(f, E7), scorer=sc)
json.dump(key, open(os.path.join(HERE, 'KEY.json'), 'w'), indent=1); print(len(key), 'packets')
