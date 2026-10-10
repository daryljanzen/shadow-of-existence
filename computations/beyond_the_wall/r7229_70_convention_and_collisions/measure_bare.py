"""r7229+70.1 -- the widened BARE (head form, 78 pre-convention citations named) over every ref: what it newly
catches against the dash form, and how many of those are citations by r7227+70.1's classification or, for subjects
written since that classification, by reading each one."""
import os, sys, csv, subprocess
os.environ['NODE'] = 'ci'
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_revision_collisions as C
cls = {r['sha']: r['bucket'] for r in csv.DictReader(open(os.path.join(
    ROOT, 'computations/beyond_the_wall/r7227_70_bare_widening/newly_caught.tsv')), delimiter='\t')}
out = subprocess.run(['git', 'log', '--all', '--format=%h%x09%s'], cwd=ROOT, capture_output=True, text=True).stdout
pop, new = 0, []
for ln in out.split('\n'):
    if '\t' not in ln: continue
    pop += 1
    sha, s = ln.split('\t', 1); s = s.strip()
    if C.claim_of(s) and not C.BARE_DASH.match(s):
        new.append((sha[:8], cls.get(sha[:8], 'UNCLASSIFIED (written after r7227+70.1)'), s))
from collections import Counter
print('population', pop, ' newly caught by the widened BARE', len(new))
print(Counter(b for _, b, _ in new))
for sha, b, s in new:
    if b.startswith('UNCLASSIFIED') or b == 'REFERENCE':
        print('  ', sha, b[:12], s[:100])
