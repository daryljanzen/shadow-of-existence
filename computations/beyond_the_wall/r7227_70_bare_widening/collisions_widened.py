"""r7227+70.1 -- what `collisions()` reports on this branch's HEAD under the old BARE and under the HEAD form."""
import os, re, sys
os.environ['NODE'] = 'ci'
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'corpus'))
import check_revision_collisions as c
known = c.BASELINE | c.TESTIMONY
old = c.collisions()
c.BARE = re.compile(r'^(r\d{3,5})(?![\w+.])\s*(?:[—-]\s*)?(.*)$')
new = c.collisions()
print('old BARE :', len(old), 'collisions;', 'unbaselined', sorted(set(old) - known))
print('HEAD form:', len(new), 'collisions;', 'unbaselined', sorted(set(new) - known))
for rev in sorted(set(new) - set(old)):
    print(' ', rev)
    for sha, w in new[rev]:
        print('     ', sha, w[:90])
