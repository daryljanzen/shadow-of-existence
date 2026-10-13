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

** r7297+70: THE UNIT IS THE (key, reader-pair) CELL. **  The r7295 key was one dimension short: 60 read 47 keys that 69
and cc66 had already double-read, and the pooler refused 44 of them as duplicates when they are a NEW reader pair on an old
key set -- the more informative kind, since only a new pair separates a reader effect from a key effect.  Every batch now
declares its readers on a comment line

    # readers: 69 | 60

(order-free: `69 | 60` and `60 | 69` are one pair), and a row is keyed by (receipt, literal, reader pair).  The same pair
presenting a key twice is still refused; a new pair on the same key pools.  A globbed file with no `# readers:` line, or
naming one reader twice, FAILS the run by name: the line is also what tells a batch from commentary the glob happens to
match (a reasons sidecar), so a file without it is never pooled by default.  The pooled share is now over CELLS, and a
key read by three seats contributes three; the per-pair table says how the figure divides.

** r7299+70: A BATCH IS RECOGNISED BY ITS CONTENT, NOT ONLY ITS NAME (69's suggestion, routed by 66). **  A reasons sidecar
that the glob matches has prose where a verdict belongs.  A file whose first-verdict column holds no verdict on any row
is NOT A BATCH (a verdict cell may be EMPTY -- a pending side -- but not prose): it is excluded and listed by name, and cannot pool at zero per cent as 69's GROUNDS file once did.  A
file whose verdict columns hold a verdict on some rows and something else on others is a MALFORMED batch and fails the
run, because there the content is a batch and a cell of it is wrong.

** r7307+70: THE COLUMN RULE IS ASSERTED, NOT ASSUMED (66's r7307). **  Column 3 holds the FIRST reader named on the
`# readers:` line and column 4 the second.  An inverted file pools to the same agreement -- a pair is order-free -- but
every per-seat rate comes out backwards, and a joiner that fills the empty column labels the blind seat's verdicts as the
primary's.  Where a batch's own comment lines name the verdict columns by seat, the LAST such line (a later correction
governs) must name them in the `# readers:` order; if it names them the other way the batch is MALFORMED and the run fails.
A batch whose comments name no column by seat is not checked, and says nothing either way.

    python3 scripts/double_read_agreement.py            # print the tables
    python3 scripts/double_read_agreement.py --seed     # the duplicate refusal, both ways, on built batches
    python3 scripts/double_read_agreement.py --write    # also write AGREEMENT.md beside the prediction
"""
import glob
import json
import re
import math
import os
import subprocess
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7293_70_agreement', 'AGREEMENT.md')
N_STAR = None   # filled from PREDICTION.md's fixed rule by n_star(); see there
VERDICTS = {'DELIBERATE', 'ALT-OK', 'REPAIR-OWED', 'NOT-A-PIN', 'ENCODING-OK', 'MEANING-HELD', 'EXTENDED',
            'UNADJUDICATED', 'UNADJUDICATED-PINNED'}   # the ledger's verdict classes (corpus/quote_pin_baseline.tsv)


def batches():
    files = sorted(set(glob.glob(os.path.join(ROOT, 'computations', '**', 'DOUBLE_READ*.tsv'), recursive=True)
                       + glob.glob(os.path.join(ROOT, 'computations', '**', 'BLIND_READ*.tsv'), recursive=True)))
    out = []
    for f in files:
        rel = os.path.relpath(f, ROOT)
        # the oldest commit that touched the file (a file landed through a merge has no `--diff-filter=A` hit on main)
        when = (subprocess.run(['git', '-C', ROOT, 'log', '--reverse', '--format=%ct %h', '--', rel],
                               capture_output=True, text=True).stdout.split('\n')[0] or '').split()
        pairs, keys, mism, label, readers = [], [], 0, '', None
        rows, vcells, hdr = [], [], []
        for ln in open(f, encoding='utf-8', errors='replace'):
            ln = ln.rstrip('\n')
            if ln.startswith('#'):
                if not rows:
                    hdr.append(ln)
                if readers is None and ln.lstrip('# ').lower().startswith('readers:'):
                    readers = tuple(r.strip() for r in ln.split(':', 1)[1].split('|'))
                    continue
                if not label and ('read' in ln.lower()) and len(ln) > 2:
                    label = ln.lstrip('# ').strip()[:90]
                continue
            c = ln.split('\t')
            if len(c) >= 3 and ln.strip():
                vcells.append((c[2].strip(), c[3].strip() if len(c) > 3 else ''))
            if len(c) < 4 or not c[2].strip() or not c[3].strip():
                continue
            a, b = c[2].strip(), c[3].strip()
            pairs.append((a, b))
            rows.append((c[0].strip(), _lit(c[1])))
            if len(c) > 4 and c[4].strip() in ('AGREE', 'DISAGREE') and (c[4].strip() == 'AGREE') != (a == b):
                mism += 1
        pair = _pair(readers)
        keys = [(*k, pair) for k in rows]
        out.append({'file': rel, 'when': int(when[0]) if when else 2 ** 62, 'sha': when[-1] if when else 'untracked',
                    'pairs': pairs, 'keys': keys, 'mismatch': mism, 'label': label, 'readers': readers, 'pair': pair,
                    'shape': _shape(vcells), 'columns': _column_order(hdr, readers)})
    return sorted(out, key=lambda b: (b['when'], b['file']))


def _shape(vcells):
    """'batch', 'sidecar' (no row verdict-shaped) or 'malformed' (some rows not): a row is verdict-shaped when both
    verdict cells are a verdict or EMPTY (a pending side) and at least one is a verdict"""
    ok = [all(x in VERDICTS | {''} for x in v) and any(v) for v in vcells]
    return 'sidecar' if ok and not any(ok) else 'malformed' if not all(ok) else 'batch'


def _column_order(header_lines, readers):
    """'ok', 'inverted' or None: the LAST comment line that names the verdict columns and both readers decides"""
    if not readers or len(readers) != 2:
        return None
    a, b = readers
    pos = lambda name, l: [m.start() for m in re.finditer(rf'(?<![\w.]){re.escape(name)}(?![\w.])', l)]
    last = None
    for l in header_lines:
        if l.lower().lstrip('# ').startswith('readers:') or not re.search(r'verdict|column|receipt\s', l, re.I):
            continue
        ia, ib = pos(a, l), pos(b, l)
        if ia and ib:
            last = 'ok' if ia[0] < ib[0] else 'inverted'
    return last


def _lit(cell):
    """the literal as the ledger means it: JSON-decoded when it is JSON, else the cell stripped"""
    cell = cell.strip()
    try:
        return json.loads(cell)
    except ValueError:
        return cell


def _pair(readers):
    """the order-free reader pair, or None when the declaration is missing, not two names, or one name twice"""
    if not readers or len(readers) != 2 or not all(readers) or readers[0] == readers[1]:
        return None
    return tuple(sorted(readers))


def unlabelled(bs):
    """[file] for every batch that does not declare two distinct readers"""
    return [x['file'] for x in bs if x.get('pair') is None]


def represented(bs):
    """[(receipt, literal, reader pair, first file, second file)] for every (key, pair) cell presented more than once"""
    seen, out = {}, []
    for x in bs:
        for k in x['keys']:
            if k in seen:
                out.append((*k, seen[k], x['file']))
            else:
                seen[k] = x['file']
    return out


def _seed():
    def mk(f, rows, readers=('69', 'cc66')):
        pair = _pair(readers)
        return {'file': f, 'keys': [(*r[:2], pair) for r in rows], 'pairs': [r[2:] for r in rows], 'pair': pair}
    a = mk('A.tsv', [('r/x.py', 'one', 'DELIBERATE', 'DELIBERATE'), ('r/x.py', 'two', 'REPAIR-OWED', 'DELIBERATE')])
    b = mk('B.tsv', [('r/y.py', 'one', 'MEANING-HELD', 'MEANING-HELD')])
    again = mk('C.tsv', [('r/x.py', 'two', 'REPAIR-OWED', 'REPAIR-OWED')])
    inner = mk('D.tsv', [('r/z.py', 'k', 'ALT-OK', 'ALT-OK'), ('r/z.py', 'k', 'ALT-OK', 'DELIBERATE')])
    newpair = mk('E.tsv', [('r/x.py', 'two', 'REPAIR-OWED', 'DELIBERATE')], ('69', '60'))
    flipped = mk('F.tsv', [('r/x.py', 'two', 'DELIBERATE', 'REPAIR-OWED')], ('cc66', '69'))
    bare = mk('G.tsv', [('r/w.py', 'k', 'ALT-OK', 'ALT-OK')], None)
    self_ = mk('H.tsv', [('r/w.py', 'k', 'ALT-OK', 'ALT-OK')], ('69', '69'))
    refused = lambda bs: bool(represented(bs)) or bool(unlabelled(bs))
    cases = [('distinct keys in two batches pool', [a, b], False),
             ('the same literal under a different receipt is a different key', [a, b], False),
             ('a key re-presented in a later batch is refused', [a, b, again], True),
             ('a key presented twice inside one batch is refused', [inner], True),
             ('r7297: the same key under a NEW reader pair pools', [a, b, newpair], False),
             ('r7297: the same pair in the other order is the same pair, refused', [a, flipped], True),
             ('r7297: a batch declaring no readers is refused', [a, bare], True),
             ('r7297: a batch naming one reader twice is refused', [a, self_], True)]
    bad = [f'{lab}: expected {"refused" if w else "pooled"}' for lab, bs, w in cases if refused(bs) != w]
    shapes = [('r7299: a four-column batch is a batch', [('DELIBERATE', 'REPAIR-OWED')], 'batch'),
              ('r7299: a pending blind read (one side empty) is a batch', [('', 'REPAIR-OWED')], 'batch'),
              ('r7299: a reasons sidecar (prose in the verdict column) is not a batch',
               [('(a) PROXY on a PARTIAL CODE LINE', ''), ('(b) the token is the claim', '')], 'sidecar'),
              ('r7299: a GROUNDS file shaped verdict, prose is not a batch', [('REPAIR-OWED', 'G4: short token')], 'sidecar'),
              ('r7299: verdicts with one prose cell is a malformed batch',
               [('DELIBERATE', 'DELIBERATE'), ('DELIBERATE', 'see note')], 'malformed')]
    bad += [f'{lab}: expected {w}, got {_shape(v)}' for lab, v, w in shapes if _shape(v) != w]
    cols = [('r7307: columns named in the readers order', ['# receipt\tliteral\tverdict (60, primary)\tverdict (69, blind)'],
             ('60', '69'), 'ok'),
            ('r7307: columns named against the readers order', ['# receipt\tliteral\tfirst verdict (cc66, blind)\tsecond '
             'verdict (69, primary)'], ('69', 'cc66'), 'inverted'),
            ('r7307: a later correction line governs', ['# receipt\tliteral\tfirst verdict (cc66)\tsecond verdict (60)',
             '#: moved: column 3 is now 60, column 4 cc66'], ('60', 'cc66'), 'ok'),
            ('r7307: a seat id inside a revision id is not a seat', ['# receipt\tliteral\tverdict (69, r7260)\tverdict (60)'],
             ('69', '60'), 'ok'),
            ('r7307: no column named by seat is not checked', ['# an accidental double-read'], ('69', 'cc66'), None)]
    bad += [f'{lab}: expected {w}, got {_column_order(h, r)}' for lab, h, r, w in cols if _column_order(h, r) != w]
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
    rows_cum = ['| after batch | pooled cells | pooled agree | pooled raw | moved by | pooled kappa |',
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
    sidecars = [x['file'] for x in bs if x['shape'] == 'sidecar']
    malformed = [x['file'] for x in bs if x['shape'] == 'malformed']
    inverted = [x['file'] for x in bs if x['shape'] == 'batch' and x.get('columns') == 'inverted']
    if inverted:
        print(f'  ⛔ {len(inverted)} BATCH(ES) WHOSE COMMENTS NAME THE VERDICT COLUMNS AGAINST THE `# readers:` ORDER -- '
              f'column 3 is the first-named reader.  Nothing is written.')
        for f in inverted:
            print(f'    {f}')
        return 1
    bs = [x for x in bs if x['shape'] != 'sidecar']
    if sidecars:
        print(f'  ⌗ {len(sidecars)} FILE(S) MATCH THE BATCH GLOB AND HOLD NO VERDICT IN THE VERDICT COLUMN -- not a batch '
              f'(a reasons sidecar), excluded and listed:')
        for f in sidecars:
            print(f'    {f}')
        print()
    if malformed:
        print(f'  ⛔ {len(malformed)} BATCH(ES) WITH A NON-VERDICT IN A VERDICT CELL ON SOME ROWS -- a malformed batch, '
              f'not a sidecar.  Nothing is written.')
        for f in malformed:
            print(f'    {f}')
        return 1
    bare = unlabelled(bs)
    if bare:
        print(f'  ⛔ {len(bare)} FILE(S) MATCH THE BATCH GLOB AND DECLARE NO TWO READERS -- every batch carries '
              f'`# readers: A | B`, and a file without it is not pooled by default.  Nothing is written.')
        for f in bare:
            print(f'    {f}')
        return 1
    dup = represented(bs)
    if dup:
        print(f'  ⛔ {len(dup)} (KEY, READER-PAIR) CELL(S) PRESENTED MORE THAN ONCE -- the same two readers on the same '
              f'key are one measurement, already pooled.  Nothing is written.')
        for r, l, pr, f1, f2 in dup[:40]:
            print(f'    {r}  {json.dumps(l, ensure_ascii=False)[:60]}  [{" | ".join(pr)}]  first in {f1}, again in {f2}')
        if len(dup) > 40:
            print(f'    ... and {len(dup) - 40} more')
        return 1
    # ⌗ r7297+66: a one-sided batch is PENDING, not an error, and this was a hard failure.
    #   The blind read lands in the cycle it is ordered; the PRIMARY it pairs with may not.  `69`'s
    #   blind read of `L801` is correct and complete and has no second column because `60` spent its
    #   cycle on four prefixes it believed unread, so the primary never landed.  Failing there stops
    #   the instrument whenever the protocol is mid-stride, which is most of the time.  Listed and
    #   excluded from the pool instead, so the figure is computed from the batches that ARE paired
    #   and the pending ones stay visible.  ** The pool must not silently drop them: a pending batch
    #   that nobody can see is a blind read that never gets paired. **
    pending = [x['file'] for x in bs if not x['pairs']]
    bs = [x for x in bs if x['pairs']]
    if pending:
        print(f'  ⌗ {len(pending)} BATCH(ES) PENDING -- blind read landed, primary has not, so there is no verdict '
              f'pair yet.  Excluded from the pool and NOT discarded:')
        for f in pending:
            print(f'    {f}')
        print()
    if not bs:
        print('  ⛔ NO PAIRED BATCH -- nothing to pool.')
        return 1
    lines, rows_cum, N, p, t2, ns, kp = report(bs)
    distinct = len({k[:2] for x in bs for k in x['keys']})
    by_pair = {}
    for x in bs:
        by_pair.setdefault(x['pair'], []).extend(x['pairs'])
    pair_rows = ['| reader pair | cells | agree | raw | kappa |', '|---|---|---|---|---|']
    for pr, ps in sorted(by_pair.items()):
        k_ = sum(a == b for a, b in ps)
        pair_rows.append(f'| `{" | ".join(pr)}` | {len(ps)} | {k_} | {100 * k_ / len(ps):.1f}% | {kappa(ps):+.2f} |')
    head = (f'# The double-read agreement, pooled — generated by `scripts/double_read_agreement.py`\n\n'
            f'*{len(bs)} batch(es), {N} independently double-read (key, reader-pair) cells over {distinct} distinct '
            f'keys and {len(by_pair)} reader pair(s).  Pooled raw agreement **{100 * p:.1f}%**, '
            f"pooled Cohen's kappa **{kp:+.2f}**.  Between-batch variance (DerSimonian–Laird) tau² = {t2:.4f}; "
            f'the size at which one more ~23-key batch moves the pooled share by more than 5 points with under 5% '
            f'probability is **n\\* = {ns}** keys (PREDICTION.md\'s rule, recomputed from the batches so far) — '
            f'{"REACHED" if distinct >= ns else f"NOT YET: {ns - distinct} keys to go"}, counted in DISTINCT keys and not '
            f'in cells -- the rule was registered in keys, and three readings of one key are not three independent '
            f'samples when the disagreement is a property of the key (r7297).*\n')
    body = '\n'.join(['', '## Per batch', ''] + lines + ['', '## Per reader pair', ''] + pair_rows
                     + ['', '## Cumulative', ''] + rows_cum) + '\n'
    if pending:
        body += ('\n## Pending -- filed, no verdict pair yet, not pooled\n\n'
                 + '\n'.join(f'- `{f}`' for f in pending) + '\n')
    if sidecars:
        body += ('\n## Not a batch -- matches the glob, holds no verdict in the verdict column (r7299)\n\n'
                 + '\n'.join(f'- `{f}`' for f in sidecars) + '\n')
    print(head + body)
    if '--write' in sys.argv:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        open(OUT, 'w', encoding='utf-8').write(head + body)
        print(f'  written: {os.path.relpath(OUT, ROOT)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
