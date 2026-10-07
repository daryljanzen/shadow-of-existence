"""Seeds for the rewritten check_order_acknowledged, each in a throwaway worktree carrying this tree's gate."""
import os, shutil, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
WT = '/tmp/claude-0/wt_r7209_g1'; GATE = 'corpus/check_order_acknowledged.py'
def fresh(rev):
    subprocess.run(['git', '-C', ROOT, 'worktree', 'remove', '--force', WT], capture_output=True)
    subprocess.run(['git', '-C', ROOT, 'worktree', 'add', '--detach', WT, rev], check=True, capture_output=True)
    shutil.copy(os.path.join(ROOT, GATE), os.path.join(WT, GATE))
def run():
    r = subprocess.run([sys.executable, GATE], cwd=WT, capture_output=True, text=True)
    return r.returncode, [l.strip() for l in r.stdout.splitlines() if '[FAIL]' in l or l.strip().startswith('⛔ 70') or l.strip().startswith('⛔ 69')]
def prepend(f, heads):
    p = os.path.join(WT, f); t = open(p).read(); i = t.index('\n## ')
    open(p, 'w').write(t[:i + 1] + ''.join(h + '\n\nbody\n\n---\n\n' for h in heads) + t[i + 1:])
res = {}
fresh('14ba3b93'); res['S1 the real defect, 14ba3b93'] = run()
fresh('HEAD'); res['S0 HEAD'] = run()
fresh('HEAD'); prepend('FOR_69.md', [f'## ⚑ r{n} — SEEDED ORDER TO 69 ALONE' for n in (7211, 7213, 7215, 7217)]); res['S2 four own sections to 69'] = run()
fresh('HEAD')
for f in ('FOR_CC66.md', 'FOR_60.md', 'FOR_70.md', 'FOR_69.md'):
    prepend(f, [f'## ⌗ r{n} — SEEDED BROADCAST, NOTHING ORDERED' for n in (7211, 7213, 7215, 7217)])
res['S3 four broadcasts to all four'] = run()
subprocess.run(['git', '-C', ROOT, 'worktree', 'remove', '--force', WT], capture_output=True)
for k, (rc, f) in res.items(): print(f'{k}: rc {rc}', f)
# ⌗ S1's first run read rc 1 with no [FAIL] line: at 14ba3b93 69's reply file did not exist, so the gate's
#   missing-pair check returns before the [FAIL] list.  The 70 row is marked, and that row is what S1 now reads.
ok = res['S1 the real defect, 14ba3b93'][0] == 1 and any(x.startswith('⛔ 70') for x in res['S1 the real defect, 14ba3b93'][1]) \
     and res['S0 HEAD'][0] == 0 and res['S2 four own sections to 69'][0] == 1 and res['S3 four broadcasts to all four'][0] == 0
print('SEEDS:', 'HELD' if ok else 'MISSED')
