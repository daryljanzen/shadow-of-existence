#!/usr/bin/env python3
"""double_read_agreement.py -- POOL EVERY INDEPENDENT DOUBLE-READ OF THE QUOTE-PIN LEDGER AND PUBLISH THE AGREEMENT.

** r7293+70, on 66's r7293 ORDER. **  Two seats verdicting the same key without seeing each other is the only measurement
of how reader-dependent a verdict is.  `81.8` per cent from the first 22 keys halved to `53.6` at 56; this script pools
every double-read as it lands and publishes the figure per batch and cumulatively, with Cohen's kappa beside the raw share
(the verdict classes are unbalanced, and a raw share flatters), and says whether the pooled figure has yet reached the size
at which it stops moving (computations/beyond_the_wall/r7293_70_agreement/PREDICTION.md).

** THE INPUT CONVENTION -- a BATCH is one tracked file named `DOUBLE_READ*.tsv` or `BLIND_READ*.tsv` anywhere under
`computations/`, one row per key: **

    receipt <TAB> literal (JSON) <TAB> verdict (first reader) <TAB> verdict (second reader) [<TAB> anything]

`#` lines are comments; the first `# ...` line that names two readers is kept as the batch's label.  Agreement is
recomputed from the two verdicts (identical strings) -- a file's own AGREE column is checked against it and a mismatch is
reported, never trusted.  Batches are ordered by the commit that added the file.

** r7295+70: A DOUBLE-READ'S IDENTITY IS ITS KEY SET, NOT ITS FILE. **  66 re-presented 44 keys already inside the
pooled 56 as one more batch and the first version pooled them -- 100 keys from 56 distinct ones, no warning, and the
duplicate read as ordinary between-batch variance.  Every row is now keyed by (receipt, literal), and a key presented
twice -- across batches or inside one -- FAILS the run (exit 1, nothing written), naming both files.  Not a warning: a
warning is how a borrower inherits a defect silently.  A third reader of an already-double-read key is a different
measurement and needs a different key; it is refused here until that is designed.

    python3 scripts/double_read_agreement.py            # print the tables
    python3 scripts/double_read_agreement.py --seed     # the duplicate refusal, both ways, on built batches
    python3 scripts/double_read_agreement.py --write    # also write AGREEMENT.md beside the prediction
"""
import glob
import json
import math
import os
import subprocess
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7293_70_agreement', 'AGREEMENT.md')
N_STAR = None   # filled from PREDICTION.md's fixed rule by n_star(); see there


def batches():
    files = sorted(set(glob.glob(os.path.join(ROOT, 'computations', '**', 'DOUBLE_READ*.tsv'), recursive=True)
                       + glob.glob(os.path.join(ROOT, 'computations', '**', 'BLIND_READ*.tsv'), recursive=True)))
    out = []
    for f in files:
        rel = os.path.relpath(f, ROOT)
        # the oldest commit that touched the file (a file landed through a merge has no `--diff-filter=A` hit on main)
        when = (subprocess.run(['git', '-C', ROOT, 'log', '--reverse', '--format=%ct %h', '--', rel],
                               capture_output=True, text=True).stdout.split('\n')[0] or '').split()
        pairs, keys, mism, label = [], [], 0, ''
        for ln in open(f, encoding='utf-8', errors='replace'):
            ln = ln.rstrip('\n')
            if ln.startswith('#'):
                if not label and ('read' in ln.lower()) and len(ln) > 2:
                    label = ln.lstrip('# ').strip()[:90]
                continue
            c = ln.split('\t')
            if len(c) < 4 or not c[2].strip() or not c[3].strip():
                continue
            a, b = c[2].strip(), c[3].strip()
            pairs.append((a, b))
            keys.append((c[0].strip(), _lit(c[1])))
            if len(c) > 4 and c[4].strip() in ('AGREE', 'DISAGREE') and (c[4].strip() == 'AGREE') != (a == b):
                mism += 1
        out.append({'file': rel, 'when': int(when[0]) if when else 2 ** 62, 'sha': when[-1] if when else 'untracked',
                    'pairs': pairs, 'keys': keys, 'mismatch': mism, 'label': label})
    return sorted(out, key=lambda b: (b['when'], b['file']))


def _lit(cell):
    """the literal as the ledger means it: JSON-decoded when it is JSON, else the cell stripped"""
    cell = cell.strip()
    try:
        return json.loads(cell)
    except ValueError:
        return cell


def represented(bs):
    """[(receipt, literal, first file, second file)] for every key presented more than once"""
    seen, out = {}, []
    for x in bs:
        for k in x['keys']:
            if k in seen:
                out.append((*k, seen[k], x['file']))
            else:
                seen[k] = x['file']
    return out


def _seed():
    mk = lambda f, rows: {'file': f, 'keys': [r[:2] for r in rows], 'pairs': [r[2:] for r in rows]}
    a = mk('A.tsv', [('r/x.py', 'one', 'DELIBERATE', 'DELIBERATE'), ('r/x.py', 'two', 'REPAIR-OWED', 'DELIBERATE')])
    b = mk('B.tsv', [('r/y.py', 'one', 'MEANING-HELD', 'MEANING-HELD')])
    again = mk('C.tsv', [('r/x.py', 'two', 'REPAIR-OWED', 'REPAIR-OWED')])
    inner = mk('D.tsv', [('r/z.py', 'k', 'ALT-OK', 'ALT-OK'), ('r/z.py', 'k', 'ALT-OK', 'DELIBERATE')])
    cases = [('distinct keys in two batches pool', [a, b], False),
             ('the same literal under a different receipt is a different key', [a, b], False),
             ('a key re-presented in a later batch is refused', [a, b, again], True),
             ('a key presented twice inside one batch is refused', [inner], True)]
    bad = [f'{lab}: expected {"refused" if w else "pooled"}' for lab, bs, w in cases if bool(represented(bs)) != w]
    for b_ in bad:
        print(f'    [FAIL] {b_}')
    print(f'  seeds: {"hold" if not bad else "LOST"}')
    return 0 if not bad else 1


def kappa(pairs):
    n = len(pairs)
    if not n:
        return float('nan')
    po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return (po - pe) / (1 - pe) if pe < 1 else float('nan')


def wilson(k, n, z=1.96):
    if not n:
        return (float('nan'),) * 2
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


def tau2(bs):
    """DerSimonian-Laird between-batch variance of the agreement share"""
    ks = [(sum(a == b for a, b in x['pairs']), len(x['pairs'])) for x in bs if x['pairs']]
    if len(ks) < 2:
        return 0.0
    ps = [(k + 0.5) / (n + 1) for k, n in ks]
    vs = [p * (1 - p) / n for p, (_, n) in zip(ps, ks)]
    w = [1 / v for v in vs]
    pbar = sum(wi * pi for wi, pi in zip(w, ps)) / sum(w)
    q = sum(wi * (pi - pbar) ** 2 for wi, pi in zip(w, ps))
    c = sum(w) - sum(wi * wi for wi in w) / sum(w)
    return max(0.0, (q - (len(ks) - 1)) / c)


def n_star(p, t2, b=23, delta=0.05, z=1.96):
    """the pooled size at which adding one more batch of b keys moves the pooled share by more than `delta` with
    probability under 5 per cent: b/(n+b) * z * sqrt(t2 + p(1-p)/b) <= delta"""
    sd = math.sqrt(t2 + p * (1 - p) / b)
    return max(0, math.ceil(b * z * sd / delta - b))


def report(bs):
    lines = ['| # | batch (file, landed at) | keys | agree | raw | 95% (Wilson) | kappa |', '|---|---|---|---|---|---|---|']
    cum = []
    rows_cum = ['| after batch | pooled keys | pooled agree | pooled raw | moved by | pooled kappa |',
                '|---|---|---|---|---|---|']
    prev = None
    for i, x in enumerate(bs, 1):
        n = len(x['pairs'])
        k = sum(a == b for a, b in x['pairs'])
        lo, hi = wilson(k, n)
        lines.append(f"| {i} | `{x['file'].split('/')[-2]}/{x['file'].split('/')[-1]}` @ `{x['sha']}` | {n} | {k} | "
                     f"{100 * k / n:.1f}% | {100 * lo:.0f}–{100 * hi:.0f}% | {kappa(x['pairs']):+.2f} |"
                     + (f" ⚠ {x['mismatch']} AGREE-column mismatch(es)" if x['mismatch'] else ''))
        cum += x['pairs']
        K, N = sum(a == b for a, b in cum), len(cum)
        p = K / N
        mv = '' if prev is None else f"{100 * (p - prev):+.1f} pts"
        rows_cum.append(f"| {i} | {N} | {K} | {100 * p:.1f}% | {mv} | {kappa(cum):+.2f} |")
        prev = p
    N = len(cum)
    p = sum(a == b for a, b in cum) / N if N else float('nan')
    t2 = tau2(bs)
    ns = n_star(p, t2)
    return lines, rows_cum, N, p, t2, ns, kappa(cum)


def main():
    if '--seed' in sys.argv:
        return _seed()
    bs = batches()
    dup = represented(bs)
    if dup:
        print(f'  ⛔ {len(dup)} KEY(S) PRESENTED MORE THAN ONCE -- a double-read is its key set, and these keys are '
              f'already pooled.  Nothing is written.')
        for r, l, f1, f2 in dup[:40]:
            print(f'    {r}  {json.dumps(l, ensure_ascii=False)[:60]}  first in {f1}, again in {f2}')
        if len(dup) > 40:
            print(f'    ... and {len(dup) - 40} more')
        return 1
    # a file with no verdict pair yet -- a blind read filed before its other reader lands, or a reasons sidecar the glob
    # also matches -- is PENDING: left out of the pool and listed, never pooled and never fatal (r7295+70.5)
    pending = [x['file'] for x in bs if not x['pairs']]
    bs = [x for x in bs if x['pairs']]
    lines, rows_cum, N, p, t2, ns, kp = report(bs)
    head = (f'# The double-read agreement, pooled — generated by `scripts/double_read_agreement.py`\n\n'
            f'*{len(bs)} batch(es), {N} independently double-read keys.  Pooled raw agreement **{100 * p:.1f}%**, '
            f"pooled Cohen's kappa **{kp:+.2f}**.  Between-batch variance (DerSimonian–Laird) tau² = {t2:.4f}; "
            f'the size at which one more ~23-key batch moves the pooled share by more than 5 points with under 5% '
            f'probability is **n\\* = {ns}** keys (PREDICTION.md\'s rule, recomputed from the batches so far) — '
            f'{"REACHED" if N >= ns else f"NOT YET: {ns - N} keys to go"}.*\n')
    body = '\n'.join(['', '## Per batch', ''] + lines + ['', '## Cumulative', ''] + rows_cum) + '\n'
    if pending:
        body += ('\n## Pending -- filed, no verdict pair yet, not pooled\n\n'
                 + '\n'.join(f'- `{f}`' for f in pending) + '\n')
    print(head + body)
    if '--write' in sys.argv:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        open(OUT, 'w', encoding='utf-8').write(head + body)
        print(f'  written: {os.path.relpath(OUT, ROOT)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
