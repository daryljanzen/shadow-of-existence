"""A5 seeds for C1's announcing limit, each in a throwaway worktree of the working tree's C1 receipt at HEAD."""
import glob, os, re, shutil, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
C1 = glob.glob(os.path.join(ROOT, 'receipts/L_probability/C1_*.py'))[0]
WT = '/tmp/claude-0/wt_r7177_c1'

def run(label, edit):
    subprocess.run(['git', '-C', ROOT, 'worktree', 'remove', '--force', WT], capture_output=True)
    subprocess.run(['git', '-C', ROOT, 'worktree', 'add', '--detach', WT, 'HEAD'], check=True, capture_output=True)
    shutil.copy(C1, os.path.join(WT, os.path.relpath(C1, ROOT)))     # the receipt under test, uncommitted
    if edit:
        edit(WT)
    r = subprocess.run([sys.executable, os.path.relpath(C1, ROOT)], cwd=WT, capture_output=True, text=True)
    line = [l for l in r.stdout.split('\n') if 'STATED LIMIT still holds' in l]
    print(f'{label}: rc {r.returncode}')
    for l in line:
        print('   ', l.strip()[:400])
    subprocess.run(['git', '-C', ROOT, 'worktree', 'remove', '--force', WT], capture_output=True)
    return r.returncode, ' '.join(line)

def add_abstract_marker(wt):
    p = os.path.join(wt, 'corpus', 'BH_causality_v2.tex')
    t = open(p, encoding='utf-8').read()
    i = t.index('\\end{abstract}')
    open(p, 'w', encoding='utf-8').write(t[:i] + ' A seeded headline claim.\\rcpt{P1_the_trapped_surface_theorem_is_cited_as_a_theorem_and_never_as_an_open_test}\n' + t[i:])

def drop_headline_marker(wt):
    p = os.path.join(wt, 'corpus', 'geometric_core_paper.tex')
    t = open(p, encoding='utf-8').read()
    n = t.count('\\rcpt{Q3_cayley_klein}')
    open(p, 'w', encoding='utf-8').write(t.replace('\\rcpt{Q3_cayley_klein}', '', 1))
    print(f'    (Q3_cayley_klein markers in the paper before the seed: {n}; the first removed)')

res = {}
res['S0'] = run('S0 HEAD', None)
res['S1'] = run('S1 a \\rcpt added to BH_causality_v2\'s abstract', add_abstract_marker)
res['S2'] = run('S2 the first Q3_cayley_klein marker removed from geometric_core_paper', drop_headline_marker)
ok = (res['S0'][0] == 0 and res['S1'][0] == 1 and 'WIDENED BH_causality_v2.tex' in res['S1'][1]
      and res['S2'][0] == 1 and 'STALE geometric_core_paper.tex: Q3_cayley_klein' in res['S2'][1])
print('A5:', 'HELD' if ok else 'MISSED')
