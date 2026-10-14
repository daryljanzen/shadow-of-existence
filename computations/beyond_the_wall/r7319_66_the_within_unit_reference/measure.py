#!/usr/bin/env python3
"""r7319, node 66 --- the two measurements this revision rules on, both from data already filed.

  (1) THE WITHIN-UNIT SPREAD ON THE OWEDNESS MARGIN.  70 split each of its two r7317 conditions
      between two fresh applier agents and reported the FLAG rate per agent.  It did not carry the
      split to the OWED verdict, which is the margin every ruling in this campaign lands on.  This
      does.  The agent split is recoverable from the files' own headers: `agent A keys 1-20 then
      agent B keys 21-40` on the crossover, `1-35 / 36-69` on the held set.

  (2) THE STRATUM MIX OF TWO DENOMINATORS.  cc66 (r7317+cc66) argues the rule's 67-72% sits above
      its own 60.7% because the appliers' denominator is construction-heavy and its own is whatever
      two colliding assignments overlapped on, and names the killing condition itself: same mix
      across the denominators and the explanation is dead.  The stratum label is the appliers'
      `judgement` column, so no re-read is needed for the two denominators that carry it.

Nothing here is joined to the ledger and nothing is written.  Read-only.
"""
import glob
import json
import math
import os
import sys

BTW = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(BTW))

# ── the two conditions 70 filed at r7317, with the agent cut its own header states ───────────────
CONDITIONS = [
    ('crossover / previous text 6bef6fd5',
     'r7315_70_redraft3_score/CROSSOVER_70_prev_text.tsv', 20, 40),
    ('held set  / third redraft 1a3c13a6',
     'r7315_70_redraft3_score/APPLICATION_70_blind.tsv', 35, 69),
]


def hdr_rows(path):
    """Header may be a bare row or the last `#` line whose first field is `receipt`."""
    hdr, data = None, []
    with open(path, encoding='utf-8') as fh:
        for ln in fh:
            ln = ln.rstrip('\n')
            if ln.startswith('#'):
                f = [x.strip() for x in ln.lstrip('#').strip().split('\t')]
                if f and f[0] == 'receipt':
                    hdr = f
                continue
            if not ln.strip():
                continue
            f = ln.split('\t')
            if hdr is None and f[0].strip() == 'receipt':
                hdr = [x.strip() for x in f]
                continue
            data.append(f)
    return hdr, data


def lit(s):
    try:
        return json.loads(s)
    except Exception:
        return s


def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d, (c + h) / d


def newcombe(k1, n1, k2, n2):
    """Newcombe's hybrid-score interval for a difference of two independent proportions."""
    l1, u1 = wilson(k1, n1)
    l2, u2 = wilson(k2, n2)
    p1, p2 = k1 / n1, k2 / n2
    lo = (p1 - p2) - math.sqrt((p1 - l1) ** 2 + (u2 - p2) ** 2)
    hi = (p1 - p2) + math.sqrt((u1 - p1) ** 2 + (p2 - l2) ** 2)
    return (p1 - p2) * 100, lo * 100, hi * 100


FLAG = lambda r: r['judgement'].strip().startswith('yes')
OWED = lambda r: r['verdict'] == 'REPAIR-OWED'

fail = []


def check(ok, label):
    print(('  [PASS] ' if ok else '  [FAIL] ') + label)
    if not ok:
        fail.append(label)


print('=' * 100)
print('  (1) THE WITHIN-UNIT SPREAD.  Two fresh agents under one instruction, keys split by hash.')
print('=' * 100)

spread = {}
for name, rel, cut, n in CONDITIONS:
    hdr, raw = hdr_rows(os.path.join(BTW, rel))
    rows = [dict(zip(hdr, r)) for r in raw]
    assert len(rows) == n, (rel, len(rows), n)
    dec = [r for r in rows if r['verdict'] != 'UNDECIDED']
    A = [r for r in rows[:cut] if r['verdict'] != 'UNDECIDED']
    B = [r for r in rows[cut:] if r['verdict'] != 'UNDECIDED']
    print(f'\n  {name}   n = {len(rows)}, decided = {len(dec)}, agents {len(A)} / {len(B)}')
    for lab, pred in (('FLAG', FLAG), ('OWED', OWED)):
        ka, kb = sum(1 for r in A if pred(r)), sum(1 for r in B if pred(r))
        kt = sum(1 for r in dec if pred(r))
        d, lo, hi = newcombe(ka, len(A), kb, len(B))
        excl = lo * hi > 0
        spread[(name, lab)] = (d, lo, hi, excl)
        print(f'    {lab}  pooled {kt}/{len(dec)} = {kt/len(dec)*100:5.1f}%   '
              f'A {ka}/{len(A)} = {ka/len(A)*100:5.1f}%   B {kb}/{len(B)} = {kb/len(B)*100:5.1f}%   '
              f'A-B = {d:+6.1f} ({lo:+.1f}, {hi:+.1f})  {"EXCLUDES 0" if excl else "includes 0"}')

print()
check(spread[(CONDITIONS[0][0], 'OWED')][3],
      "Ⓐ① the agent spread reaches the OWEDNESS margin: on the crossover the two agents' owed rates "
      'differ by 30.0 points and the interval excludes 0 --- so the spread 70 measured on the flag is '
      'not confined to the flag')
check(spread[(CONDITIONS[0][0], 'FLAG')][3] and spread[(CONDITIONS[1][0], 'FLAG')][3],
      'Ⓐ② 70\'s own FLAG finding reproduces: both conditions exclude 0 (-35.0 and +33.1)')
check(spread[(CONDITIONS[0][0], 'FLAG')][0] * spread[(CONDITIONS[1][0], 'FLAG')][0] < 0,
      'Ⓐ③ the FLAG gap FLIPS SIGN between conditions, which is what a fresh draw looks like and not a '
      'standing difference between two readers')
check(spread[(CONDITIONS[0][0], 'OWED')][0] * spread[(CONDITIONS[1][0], 'OWED')][0] > 0,
      'Ⓐ④ the OWED gap does NOT flip --- same sign both times (-30.0, -10.9), one interval excluding 0')

# the between-seat gap this is the reference for: r7299's per-seat owedness rates, pooled cells
R7299 = {'cc66': (74, 122), '70': (3, 6), '60': (40, 88), '69': (58, 128)}
cc = R7299['cc66'][0] / R7299['cc66'][1] * 100
g69 = cc - R7299['69'][0] / R7299['69'][1] * 100
g60 = cc - R7299['60'][0] / R7299['60'][1] * 100
print(f'\n  r7299, the ruling this is the reference for: cc66 {cc:.1f}% owed against '
      f"69 {R7299['69'][0]/R7299['69'][1]*100:.1f}% and 60 {R7299['60'][0]/R7299['60'][1]*100:.1f}% "
      f'--- gaps of {g69:.1f} and {g60:.1f} points, ruled "a threshold effect, and it is cc66\'s".')
check(abs(spread[(CONDITIONS[0][0], 'OWED')][0]) > max(g69, g60),
      f'Ⓐ⑤ THE REFERENCE WAS NEVER TAKEN: the within-seat owedness spread measured inside ONE seat '
      f'({abs(spread[(CONDITIONS[0][0], "OWED")][0]):.1f} points) EXCEEDS the between-seat gap '
      f'({max(g69, g60):.1f} points) that r7299 ruled a property of the seats')

# ── (2) the stratum mix ──────────────────────────────────────────────────────────────────────────
print()
print('=' * 100)
print("  (2) THE STRATUM MIX.  cc66's own killing condition, run on the two denominators that")
print('      carry the label.  No re-read.')
print('=' * 100)

# ⛔ A key read in several applier rounds carries several labels, so a dict keyed on the key alone
#   silently takes whichever file glob order put last.  That is the r7297 lesson --- the unit of a
#   double-read is the CELL and not the key --- arriving in my own hands on the stratum label.  So
#   cells are held per (key, round), and the disagreement among them is measured rather than hidden.
cells = {}        # (key, round) -> (stratum, owed)
for p in sorted(glob.glob(os.path.join(BTW, '*', 'APPLICATION_70*.tsv'))):
    hdr, raw = hdr_rows(p)
    if not hdr or 'judgement' not in hdr:
        continue
    rnd = os.path.basename(os.path.dirname(p)) + '/' + os.path.basename(p)
    ir, il, ij, iv = (hdr.index(c) for c in ('receipt', 'literal', 'judgement', 'verdict'))
    for r in raw:
        if len(r) <= max(ij, iv):
            continue
        k = (r[ir], lit(r[il]))
        cells[(k, rnd)] = ('judgement' if r[ij].strip().startswith('yes') else 'text',
                           r[iv] == 'REPAIR-OWED')

by_key = {}
for (k, _rnd), v in cells.items():
    by_key.setdefault(k, []).append(v)

# the label's OWN within-unit spread: keys read in more than one round, and how often the two
# rounds put the same key in different strata.
multi = {k: v for k, v in by_key.items() if len(v) > 1}
flip = sum(1 for v in multi.values() if len({s for s, _ in v}) > 1)
print(f'\n  the stratum label is itself a reader output.  {len(multi)} keys were labelled in more '
      f'than one applier round;\n  {flip} of them ({flip/max(len(multi),1)*100:.1f}%) were put in '
      f'DIFFERENT strata by different rounds.')

# a key counts once, by majority of its cells, ties broken to `judgement` (the conservative side
# for cc66's argument, since it is the low-owed stratum).
def collapse(vs):
    t = sum(1 for s, _ in vs if s == 'text')
    return ('text' if t * 2 > len(vs) else 'judgement',
            sum(1 for _, o in vs if o) * 2 > len(vs))

label = {k: collapse(v)[0] for k, v in by_key.items()}
owed_of = {k: collapse(v)[1] for k, v in by_key.items()}

double = set()
for p in sorted(glob.glob(os.path.join(BTW, '*', 'BLIND_READ*.tsv'))):
    hdr, raw = hdr_rows(p)
    if not hdr:
        continue
    ir, il = hdr.index('receipt'), hdr.index('literal')
    for r in raw:
        if len(r) <= il:
            continue
        if r[ir].startswith('receipts/'):
            double.add((r[ir], lit(r[il])))

n_app = len(label)
t_app = sum(1 for k in label if label[k] == 'text')
f_app = t_app / n_app
ov = double & set(label)
t_cc = sum(1 for k in ov if label[k] == 'text')
f_cc = t_cc / len(ov)

r_text = sum(owed_of[k] for k in label if label[k] == 'text') / t_app
r_jud = sum(owed_of[k] for k in label if label[k] == 'judgement') / (n_app - t_app)

print(f'\n  APPLIER denominator (the rule\'s 67-72%): n = {n_app:4d}   text-decides = {t_app:3d} = {f_app*100:.1f}%')
print(f"  DOUBLE-READ denominator (cc66's 60.7%):  n = {len(double):4d}   labelled = {len(ov)} "
      f'({len(ov)/len(double)*100:.1f}%)   text-decides = {t_cc} = {f_cc*100:.1f}%')
print(f'\n  owed rate BY STRATUM, on the applier keys:   text {r_text*100:.1f}%   '
      f'judgement {r_jud*100:.1f}%   spread {abs(r_text-r_jud)*100:.1f} points')

blend = lambda f: (f * r_text + (1 - f) * r_jud) * 100
f_worst = t_cc / len(double)          # every unlabelled double-read key is judgement: cc66's best case
f_best = (t_cc + (len(double) - len(ov))) / len(double)
print(f'\n  the blended rate a mix difference alone would produce:')
print(f'    at the applier mix      f = {f_app*100:.1f}%  ->  {blend(f_app):.1f}%   '
      f'(measured on those keys: {sum(owed_of.values())}/{n_app} = {sum(owed_of.values())/n_app*100:.1f}%)')
print(f"    at cc66's measured mix  f = {f_cc*100:.1f}%  ->  {blend(f_cc):.1f}%")
print(f"    at cc66's BEST CASE     f = {f_worst*100:.1f}%  ->  {blend(f_worst):.1f}%   "
      f'(every one of the {len(double)-len(ov)} unlabelled keys taken as judgement)')
bound = blend(f_app) - blend(f_worst)
gap = blend(f_app) - 60.7
print(f'\n  ⇒ MIX ACCOUNTS FOR AT MOST {bound:.1f} POINTS of the {gap:.1f}-point gap to cc66\'s 60.7%.')

check(abs(f_app - f_cc) < 5.0,
      f'Ⓑ① the two denominators carry the SAME MIX: {f_app*100:.1f}% against {f_cc*100:.1f}%, '
      f'{abs(f_app-f_cc)*100:.1f} points apart --- which is the condition cc66 named for its own '
      'explanation to be dead')
check(abs(r_text - r_jud) > 0.20,
      f'Ⓑ② and the strata are real, so the mix WOULD have mattered had it differed: {r_text*100:.1f}% '
      f'owed where the text decides against {r_jud*100:.1f}% where judgement enters')
check(bound < gap / 2,
      f'Ⓑ③ AT THE BOUND, not at the point estimate: even taking every unlabelled double-read key as '
      f'judgement --- the most favourable assignment the data allow cc66 --- mix moves the predicted '
      f'rate by {bound:.1f} points, under half the {gap:.1f}-point gap it is offered to explain')

print()
print('=' * 100)
print(f'  gates run: {len(fail) + 8}   failed: {len(fail)}')
print('=' * 100)
print("""
  ⛔ ** THE REFERENCE AGAINST WHICH A BETWEEN-UNIT DIFFERENCE IS A PROPERTY OF THE UNITS IS THE
     WITHIN-UNIT SPREAD, AND r7299 RULED WITHOUT IT. ** The spread inside one seat, on the very
     margin that was ruled on, is twice the between-seat gap that was called a threshold.
  ⌗ The A/B labels carry NO identity across the two conditions --- each drew two FRESH agents ---
     so the two splits are two independent measurements and are not pooled here.
  ✔ ** cc66's MIX EXPLANATION IS REFUTED ON THE CONDITION cc66 ITSELF NAMED **, from filed data,
     with no re-read: the denominators differ by 1.9 points, and at the bound mix accounts for at
     most 2.9 points of 12.9.  By cc66's own statement that leaves a LEVEL, and a drafting fact
     about the tests rather than a threshold held by any reader.
  ⛔ ** AND THE STRATUM LABEL CORROBORATES THE FIRST FINDING FROM A THIRD DIRECTION: ** of the 37
     keys one seat labelled in more than one round, 22 --- 59.5 per cent --- changed stratum between
     rounds.  Same seat, same instruction, same key, different draw.
  ⌗ Not measured: 60's 40 sampled era rows carry no applier label, so the third denominator's mix
     is unmeasured and the vintage leg of the gap is untouched by this.""")
sys.exit(1 if fail else 0)
