"""E8 item draw (seed 8): 24 task items in three blocks of 8. Blocks X and Z each hold E1 x3, E2 x3 (one correct-contested,
one wrong-confident, one open) and E3 x2; block Y holds E1 x2, E2 x2 (one of each non-open kind) and E3 x4. Order A
is X,Y,Z and order B is Z,Y,X, alternating by session index, so every item in X and Z is early (turns 1-8) in half the
sessions and late (turns 17-24) in the other half; Y is always turns 9-16. Writes sessions.json."""
import json, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.dirname(os.path.dirname(HERE))
rnd = random.Random(8)
e1 = [i['id'] for i in json.load(open(os.path.join(EXP, 'E1/materials/items.json'))) if i['id'] != 'E1-09']
e2 = json.load(open(os.path.join(EXP, 'E2/materials/items.json')))
e3 = [i['id'] for i in json.load(open(os.path.join(EXP, 'E3/materials/items.json')))]
kind = lambda k: [i['id'] for i in e2 if i['kind'] == k]
E1 = rnd.sample(e1, 8); CC = rnd.sample(kind('correct_contested'), 3); WC = rnd.sample(kind('wrong_confident'), 3)
OP = rnd.sample(kind('open'), 2); E3 = rnd.sample(e3, 8)
X = E1[0:3] + [CC[0], WC[0], OP[0]] + E3[0:2]
Z = E1[3:6] + [CC[1], WC[1], OP[1]] + E3[2:4]
Y = E1[6:8] + [CC[2], WC[2]] + E3[4:8]
for b in (X, Y, Z):
    rnd.shuffle(b)
out = dict(seed=8, blocks=dict(X=X, Y=Y, Z=Z), order_A=X + Y + Z, order_B=Z + Y + X,
           spin_up=['arp_standalone.tex', 'E7/materials/evidence/01_halden_pilot.md', 'E7/materials/evidence/02_varden_trial.md',
                    'E7/materials/evidence/03_reexamination_critique.md', 'E7/materials/evidence/04_meta_analysis.md',
                    'E7/materials/evidence/05_two_year_followup.md', 'E7/materials/evidence/06_synthesis.md',
                    'E7/materials/disposition_sound.md'])
json.dump(out, open(os.path.join(HERE, 'sessions.json'), 'w'), indent=1); print(out['order_A'])
