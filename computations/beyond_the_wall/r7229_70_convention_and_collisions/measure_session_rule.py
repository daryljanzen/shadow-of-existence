"""r7229+70.1 -- AMENDMENT after C1 missed: two commits on one id are one line's span only when they share a
Claude-Session; a pair whose sessions both exist and differ is a reuse.  A commit with no trailer falls back to
ancestry (the old rule), since nothing else says whose it is.  Measured here, every new collision listed."""
import os, sys, subprocess, collections
os.environ['NODE'] = 'ci'
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_revision_collisions as C
out = subprocess.run(['git', 'log', '--format=%h%x09%(trailers:key=Claude-Session,valueonly,separator=%x20)%x09%an%x09%s'],
                     cwd=ROOT, capture_output=True, text=True).stdout
by = collections.defaultdict(list)
for ln in out.split('\n'):
    p = ln.split('\t')
    if len(p) < 4: continue
    m = C.claim_of(p[3].strip())
    if m: by[m.group(1)].append((p[0], p[1].strip(), p[2], p[3]))
anc_pairs, sess_bad = 0, {}
for rev, es in by.items():
    for i, a in enumerate(es):
        for b in es[i + 1:]:
            if not (C._anc(a[0], b[0]) or C._anc(b[0], a[0])):
                continue
            anc_pairs += 1
            if a[1] and b[1] and a[1] != b[1]:
                sess_bad.setdefault(rev, set()).update([a, b])
old = set(C.collisions())
print('ancestor-related pairs on one id:', anc_pairs)
print('ids with an ancestor-related pair from two different sessions:', len(sess_bad),
      ' of which not already collisions:', len(set(sess_bad) - old))
for rev in sorted(set(sess_bad) - old):
    print(' ', rev)
    for sha, sess, an, s in sorted(sess_bad[rev]):
        print('     ', sha, sess[-12:], an[:16].ljust(16), s[:80])
