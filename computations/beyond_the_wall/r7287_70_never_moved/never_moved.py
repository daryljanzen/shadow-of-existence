#!/usr/bin/env python3
"""r7287+70.1: for every quote-pin key in scope, has its literal's line ever moved?  (PREDICTION.md, 6daf24a9.)

    python3 never_moved.py --seed            # the built seeds, in a scratch repository
    python3 never_moved.py [--jobs 4]        # writes keys.tsv (one row per key) and prints the per-prefix table

A key is located at HEAD by check_quote_pins._present_at's own file rule; per file, the needle is the longest run of
the literal found verbatim on one line; `git log -S needle --max-count=2 -- file` gives 1 (NEVER MOVED), 2 (MOVED),
or 0 (UNLOCATED).  A key in several files is NEVER MOVED only if it is never moved in every one."""
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_quote_pins as Q  # noqa: E402

REFERENCE = ['L175_dimensional_descent', 'L211_closure_adjacency', 'L221_quark_lepton', 'L200_free_data_count',
             'L165_defining_the_sum', 'P12_algebroid', 'L147_two_arm', 'L269_the_second_theatre',
             'L202_phase_at_the_seam', 'L257_the_label_did_double_duty', 'L281_the_prior_art_hole',
             'L802_stability_bracket', 'L207_the_bend']
STAMP = re.compile(r'r(72[6-9]\d)')


def git(root, *a):
    return subprocess.run(['git', '-C', root, *a], capture_output=True, text=True, errors='replace').stdout


def prefix(receipt):
    return receipt.split('/')[1] if receipt.count('/') >= 2 else receipt


def campaign(row):
    note = row[6] if len(row) > 6 else ''
    m = [int(x) for x in STAMP.findall(note)]
    return bool(m) and max(m) >= 7269 and not row[5].startswith('UNADJ')


def files_for(root, lit, target, receipt):
    """the files at HEAD holding the literal, by _present_at's rule"""
    if target == 'PAPER':
        names = [n for n in git(root, 'ls-files', 'corpus').split()
                 if n.endswith('.tex') and not os.path.basename(n).startswith('appendix_receipts')]
    else:
        w = (lit.replace('\\', '').split() or [lit])[0]
        names = [n for n in git(root, 'grep', '-l', '-F', '-e', w, 'HEAD', '--').split('\n') if ':' in n]
        names = [n.split(':', 1)[1] for n in names]
        names = [n for n in names if n != receipt]
    out = []
    for n in names:
        p = os.path.join(root, n)
        try:
            t = open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        flat = Q._flat(t)
        if lit in t or lit in flat or (Q._unmark(lit) and Q._unmark(lit) in Q._unmark_text(flat)):
            out.append((n, t))
    return out


def needle(lit, text):
    """the longest run of the literal's words found verbatim on one line of `text`"""
    words = lit.split()
    best = ''
    for i in range(len(words)):
        for j in range(len(words), i, -1):
            cand = ' '.join(words[i:j])
            if len(cand) <= len(best):
                break
            if cand in text:                    # no newline in `cand`, so a hit is on one line
                best = cand
                break
    if not best and lit.strip() and '\n' not in lit.strip() and lit.strip() in text:
        best = lit.strip()
    return best


def moved_in(root, path, nd):
    out = git(root, 'log', '-S', nd, '--max-count=2', '--format=%H', '--', path).split()
    return len(out)


def classify(root, key):
    receipt, lit, target = key
    fs = files_for(root, lit, target, receipt)
    if not fs:
        return 'UNLOCATED', []
    detail = []
    for n, t in fs:
        nd = needle(lit, t)
        if len(nd) < 6:
            detail.append((n, nd, -1))
            continue
        detail.append((n, nd, moved_in(root, n, nd)))
    counts = [c for _, _, c in detail if c >= 0]
    if not counts or all(c == 0 for c in counts):
        return 'UNLOCATED', detail
    return ('MOVED' if any(c >= 2 for c in counts) else 'NEVER'), detail


def spearman(xs, ys):
    def ranks(v):
        o = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(o):
            j = i
            while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]:
                j += 1
            for k in range(i, j + 1):
                r[o[k]] = (i + j) / 2 + 1
            i = j + 1
        return r
    a, b = ranks(xs), ranks(ys)
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    cov = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    va = sum((x - ma) ** 2 for x in a) ** 0.5
    vb = sum((y - mb) ** 2 for y in b) ** 0.5
    return cov / (va * vb) if va and vb else float('nan')


def seed():
    tmp = tempfile.mkdtemp(prefix='nm_seed_')
    r = lambda *a: subprocess.run(['git', '-C', tmp, *a], capture_output=True, text=True)
    r('init', '-q')
    r('config', 'user.email', 's@x')
    r('config', 'user.name', 's')
    f = os.path.join(tmp, 'p.tex')

    def commit(text, m):
        open(f, 'w').write(text)
        r('add', '.')
        r('commit', '-qm', m)
    commit('alpha line\nthe frozen sentence stays\nthe moving sentence once\n', 'a')
    commit('alpha line edited\nthe frozen sentence stays\n', 'b')                     # moving removed
    commit('alpha line edited\nthe frozen sentence stays\nthe moving sentence once\n', 'c')   # and re-added
    commit('alpha line edited\nthe frozen sentence stays\nthe moving sentence once\na wrapped\nsentence here\n', 'd')
    t = open(f).read()
    res = {
        'introduced once reads NEVER': moved_in(tmp, 'p.tex', needle('the frozen sentence stays', t)) == 1,
        'added, removed, re-added reads MOVED': moved_in(tmp, 'p.tex', needle('the moving sentence once', t)) == 2,
        'a wrapped literal is located by its longest one-line run': needle('a wrapped sentence here', t) == 'sentence here'
        or needle('a wrapped sentence here', t) == 'a wrapped',
    }
    for k, v in res.items():
        print(f'    [{"ok" if v else "FAIL"}] {k}')
    return all(res.values())


def main():
    if '--seed' in sys.argv:
        return 0 if seed() else 1
    jobs = int(sys.argv[sys.argv.index('--jobs') + 1]) if '--jobs' in sys.argv else 4
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'),
                                                     encoding='utf-8') if not l.startswith('#')]
    rows = [r for r in rows if len(r) >= 6]
    keys = {}
    for r in rows:
        unadj = r[5].startswith('UNADJ')
        ref = prefix(r[0]) in REFERENCE and campaign(r)
        if unadj or ref:
            keys[(r[0], json.loads(r[1]), r[2])] = (r[5], 'UNADJ' if unadj else 'REF')
    t0 = time.time()
    with ThreadPoolExecutor(jobs) as ex:
        res = dict(zip(keys, ex.map(lambda k: classify(ROOT, k), keys)))
    wall = time.time() - t0
    with open(os.path.join(HERE, 'keys.tsv'), 'w', encoding='utf-8') as fh:
        fh.write('# set\treceipt\tliteral\ttarget\tverdict\tclass\tfiles (path:needle:commits)\n')
        for k, (cls, det) in res.items():
            v, s = keys[k]
            fh.write('\t'.join([s, k[0], json.dumps(k[1], ensure_ascii=False), k[2], v, cls,
                                ' | '.join(f'{n}:{json.dumps(nd, ensure_ascii=False)[:60]}:{c}' for n, nd, c in det)])
                     + '\n')
    print(f'  {len(keys)} key(s) classified in {wall:.0f} s wall at {jobs} job(s)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
