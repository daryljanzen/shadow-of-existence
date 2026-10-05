"""A6 seeds for the PROPOSED UNRUNNABLE check: the gate's function run against HEAD and two seeded worktrees.
The patch is applied only inside throwaway worktrees; the gate in the committed tree is untouched."""
import glob, os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
WT = '/tmp/claude-0/wt_r7177_unrun'
PATCH = os.path.join(HERE, 'proposed_check_receipts_run.diff')
PROBE = ("import sys,time; sys.argv=['x']; sys.path.insert(0,'corpus'); import check_receipts_run as G; "
         "t=time.time(); m=G.unrunnable_still_needs(); print('MOVED', m); print('SECONDS %.2f' % (time.time()-t))")

def run(label, edit):
    subprocess.run(['git', '-C', ROOT, 'worktree', 'remove', '--force', WT], capture_output=True)
    subprocess.run(['git', '-C', ROOT, 'worktree', 'add', '--detach', WT, 'HEAD'], check=True, capture_output=True)
    subprocess.run(['git', 'apply', PATCH], cwd=WT, check=True)
    if edit:
        edit(WT)
    r = subprocess.run([sys.executable, '-c', PROBE], cwd=WT, capture_output=True, text=True)
    print(f'{label}:\n    {r.stdout.strip()}{r.stderr.strip()[-300:]}')
    subprocess.run(['git', '-C', ROOT, 'worktree', 'remove', '--force', WT], capture_output=True)
    return r.stdout

def drop_camb(wt):
    p = glob.glob(os.path.join(wt, 'receipts', '**', 'C47_the_neutrinos_were_missing.py'), recursive=True)[0]
    t = open(p).read()
    import re
    t2 = re.sub(r'^(\s*)(import camb|from camb)', r'\1pass  # seeded: \2', t, flags=re.M)
    assert t2 != t
    open(p, 'w').write(t2)

def delete_listed(wt):
    p = glob.glob(os.path.join(wt, 'receipts', '**', 'P15_damping_reabsorption.py'), recursive=True)[0]
    os.remove(p)

s0 = run('S0 HEAD (patch applied)', None)
s1 = run('S1 C47_the_neutrinos_were_missing stops importing camb', drop_camb)
s2 = run('S2 P15_damping_reabsorption deleted', delete_listed)
ok = ("MOVED []" in s0 and "LIFTED C47_the_neutrinos_were_missing.py" in s1
      and "STALE P15_damping_reabsorption.py" in s2)
print('A6 (UNRUNNABLE):', 'HELD' if ok else 'MISSED')
