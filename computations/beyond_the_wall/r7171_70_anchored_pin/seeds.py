"""seeds.py -- r7171+70.1 (70) A2/A3: the new receipt against (A2) the five papers as they stood before r7168's
repair, and (A3) the anchor phrase rewritten out of every paper.  Throwaway worktree; the receipt is the working copy."""
import os, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
R = 'receipts/P01_BH_causality/P1_the_trapped_surface_theorem_is_cited_as_a_theorem_and_never_as_an_open_test.py'
CHANGED = ['CR_framework', 'CR_synthesis', 'canonical_time', 'geometric_core_paper', 'janzen_circle_v3']

wt = tempfile.mkdtemp(prefix='pinseed_'); os.rmdir(wt)
subprocess.run(['git', 'worktree', 'add', '--detach', wt, 'HEAD'], cwd=ROOT, capture_output=True)
try:
    os.makedirs(os.path.dirname(os.path.join(wt, R)), exist_ok=True)
    shutil.copy(os.path.join(ROOT, R), os.path.join(wt, R))

    def run(tag):
        d, b = os.path.split(os.path.join(wt, R))
        p = subprocess.run([sys.executable, b], cwd=d, capture_output=True, text=True)
        print(f'== {tag}: rc {p.returncode}')
        for l in p.stdout.splitlines():
            if l.strip().startswith(('OK', 'FAIL', 'anchored sites')):
                print('   ', l.strip()[:260])

    for s in CHANGED:   # A2: the pre-repair papers
        src = subprocess.run(['git', 'show', f'09161f5c^:corpus/{s}.tex'], cwd=ROOT, capture_output=True, text=True).stdout
        open(os.path.join(wt, 'corpus', s + '.tex'), 'w', encoding='utf-8').write(src)
    run('A2 the five papers before r7168')
    subprocess.run(['git', 'checkout', '-q', '--', 'corpus/'], cwd=wt)
    import glob, re   # A3: the anchor phrase rewritten out of every paper
    for p in glob.glob(os.path.join(wt, 'corpus', '*.tex')):
        t = open(p, encoding='utf-8').read()
        t2 = re.sub(r'trapped surface', 'marginal surface', t)
        t2 = re.sub(r'(collapse (?:does not|never|must not)?\s*)complete', r'\1finish', t2)
        t2 = re.sub(r'finite (exterior|cosmic) time', r'bounded \1 time', t2)
        t2 = re.sub(r'horizon completes', 'horizon closes', t2)
        if t2 != t:
            open(p, 'w', encoding='utf-8').write(t2)
    run('A3 the anchor phrase rewritten out of every paper')
finally:
    subprocess.run(['git', 'worktree', 'remove', '--force', wt], cwd=ROOT, capture_output=True)
    shutil.rmtree(wt, ignore_errors=True)
