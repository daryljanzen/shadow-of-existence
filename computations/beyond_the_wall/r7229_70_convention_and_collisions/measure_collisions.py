"""r7229+70.1 -- collisions() before and after the first-parent repair, on HEAD and at N1's r3112 SHA."""
import os, sys, subprocess, tempfile, shutil, importlib
os.environ['NODE'] = 'ci'
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_revision_collisions as C
known = C.BASELINE | C.TESTIMONY

def old_rule(root=None):
    saved = C._same_line
    C._same_line = lambda a, b, r=None: C._anc(a, b, r) or C._anc(b, a, r)
    try:
        return C.collisions(root)
    finally:
        C._same_line = saved

def at(sha, fn):
    wt = tempfile.mkdtemp()
    subprocess.run(['git', 'worktree', 'add', '--detach', wt, sha], cwd=ROOT, capture_output=True)
    try:
        return fn(wt)
    finally:
        subprocess.run(['git', 'worktree', 'remove', '--force', wt], cwd=ROOT, capture_output=True)
        shutil.rmtree(wt, ignore_errors=True)

for label, root in [('HEAD', None)]:
    o, n = old_rule(root), C.collisions(root)
    print(f'{label}: ancestry rule {len(o)}  first-parent rule {len(n)}  new {len(set(n)-set(o))}  unbaselined {sorted(set(n)-known)}')
    for rev in sorted(set(n) - set(o)):
        print('  ', rev)
        for sha, w in n[rev]:
            sess = subprocess.run(['git', 'log', '-1', '--format=%an|%(trailers:key=Claude-Session,valueonly)', sha],
                                  cwd=ROOT, capture_output=True, text=True).stdout.strip().replace('\n', ' ')
            print('      ', sha, sess[-40:], '|', w[:70])
AT = '5af2a1da54'
o = at(AT, old_rule); n = at(AT, C.collisions)
print(f'AT {AT}: ancestry rule {len(o)}  first-parent rule {len(n)}  new {sorted(set(n)-set(o))}')
for cit in ['r6975', 'r6983', 'r7189', 'r7217', 'r7225']:
    print('citation', cit, 'fires' if cit in C.collisions() else 'does not fire')
