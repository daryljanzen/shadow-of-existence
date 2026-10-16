#!/usr/bin/env python3
"""r7415+70 ④ -- THE CHEAPER EXACT ROUTE to the dead-pin census (r7371+70.2 ④, built and priced here).

`check_quote_pins._present_at` is CALLED, not reimplemented: `hit`, `_flat`, `_unmark` and the PAPER/SOURCE file
selection are the gate's.  Only its I/O is replaced, three ways:
  * every blob at the commit is read ONCE through one `git cat-file --batch` and pre-loaded into the gate's own
    `_SHOW_CACHE` as `_flat(text)`, exactly what its `git show` branch would have stored;
  * its `git grep -l -F -e WORD SHA --` is answered from that same text (one `find` pass over the concatenated
    blobs, memoised per WORD), and its `git ls-tree --name-only SHA corpus/` from the tree listing;
  * `_unmark_text`, an LRU of 512 that thrashes across the SOURCE half's thousands of files, is made unbounded.
Every other git call falls through to the real `_git`.

    SHA=<commit> python3 -I new_route.py OUT.tsv [--target T]
"""
import bisect, functools, threading, importlib.util, json, os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rows import rows  # noqa: E402

t_all = time.time()
spec = importlib.util.spec_from_file_location('g', 'corpus/check_quote_pins.py')
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
out = sys.argv[1]
tgt = sys.argv[sys.argv.index('--target') + 1] if '--target' in sys.argv else ''
R = [r for r in rows() if not tgt or r[2] == tgt]
sha = g._git('rev-parse', os.environ.get('SHA', 'HEAD')).stdout.strip()

# ── one read of the tree ────────────────────────────────────────────────────────────────────────────────────
t0 = time.time()
ls = subprocess.run(['git', '-C', g.ROOT, 'ls-tree', '-r', '-z', sha], capture_output=True).stdout.split(b'\0')
blobs = []                                   # (path, oid) for blobs only: a gitlink is not searched by git grep
for e in ls:
    if not e:
        continue
    meta, path = e.split(b'\t', 1)
    mode, typ, oid = meta.split()
    if typ == b'blob':
        blobs.append((path.decode('utf-8', 'surrogateescape'), oid))
p = subprocess.Popen(['git', '-C', g.ROOT, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
def _feed():                                 # a writer thread, or the two pipes fill and deadlock each other
    p.stdin.write(b''.join(oid + b'\n' for _, oid in blobs)); p.stdin.close()


threading.Thread(target=_feed, daemon=True).start()
TEXT = {}
for path, oid in blobs:
    hdr = p.stdout.readline().split()
    n = int(hdr[2])
    raw = p.stdout.read(n); p.stdout.read(1)
    TEXT[path] = raw.decode('utf-8', 'replace')    # what `_git(..., text=True, errors='replace')` decodes to
p.wait()
names = list(TEXT)
for n_ in names:
    g._SHOW_CACHE[(sha, n_)] = g._flat(TEXT[n_])
SEP = '\0'
BIG = SEP.join(TEXT[n_] for n_ in names)
STARTS, o = [], 0
for n_ in names:
    STARTS.append(o); o += len(TEXT[n_]) + 1
t_read = time.time() - t0


@functools.lru_cache(maxsize=None)
def files_with(word):
    """the files `git grep -l -F -e word` lists: every blob whose text contains `word`"""
    hits, i = [], BIG.find(word)
    while i != -1:
        k = bisect.bisect_right(STARTS, i) - 1
        hits.append(names[k])
        nxt = STARTS[k + 1] if k + 1 < len(STARTS) else len(BIG)
        i = BIG.find(word, nxt)
    return hits


class _R:
    def __init__(self, out):
        self.stdout, self.stderr, self.returncode = out, '', 0


real = g._git
PAPER_LS = '\n'.join(n_ for n_ in names if n_.startswith('corpus/') and '/' not in n_[len('corpus/'):])
GREP_FALLBACK = [0]


def fake(*a):
    if a[:2] == ('ls-tree', '--name-only') and a[2] == sha and a[3:] == ('corpus/',):
        return _R(PAPER_LS)
    if a[:4] == ('grep', '-l', '-F', '-e') and a[5:] == (sha, '--') and '\n' not in a[4] and a[4]:
        return _R('\n'.join(f'{sha}:{n_}' for n_ in files_with(a[4])))
    if a and a[0] == 'grep':
        GREP_FALLBACK[0] += 1                       # a shape this route does not model goes to real git, counted
    return real(*a)


g._git = fake
g._unmark_text = functools.lru_cache(maxsize=None)(g._unmark)

t1 = time.time(); per = {}
with open(out, 'w', encoding='utf-8') as f:
    f.write(f'# new route at {sha} over {len(R)} row(s)\n')
    for i, (rc, lit, target, tier, verdict) in enumerate(R):
        t = time.time()
        pr = g._present_at(sha, lit, target, rc)
        per[target] = per.get(target, 0.0) + time.time() - t
        f.write(f'{i}\t{target}\t{int(pr)}\t{rc}\t{json.dumps(lit, ensure_ascii=False)}\n')
    f.write(f'# READ {t_read:.1f}s ({len(blobs)} blobs, {len(BIG)/1e6:.1f} M chars); KEYS {time.time() - t1:.1f}s '
            + ' '.join(f'{k}={v:.1f}s' for k, v in sorted(per.items()))
            + f'; WALL {time.time() - t_all:.1f}s; grep fallbacks {GREP_FALLBACK[0]}\n')
