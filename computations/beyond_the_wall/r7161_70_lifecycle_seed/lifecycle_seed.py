"""lifecycle_seed.py -- r7161+70.1 (70): plant one defect of a scoped gate's own class at each lifecycle stage and ask
whether the gate's SCOPE SELECTOR includes it.  Pre-registered at PREDICTION.md beside this file.

  python3 lifecycle_seed.py            # builds a throwaway worktree of HEAD, measures, removes it

THE REAL TREE IS NEVER TOUCHED.  Everything happens in `git worktree add --detach <tmp> HEAD`, removed at exit.

The planted receipts all pin one sentence of `corpus/CR_cosmology.tex` -- "to the first three gives the sky
$\\phi/\\pi=-0.2404$" -- and the paper edit moves that figure.  So each of them is a receipt the edit can break, and
each selector SHOULD put each of them in scope.  The variants are the lifecycle stages:
  S1  names CR_cosmology.tex, opens it, pins the sentence; in no baseline       (written, not adjudicated)
  S2  the same pin, read through corpus/reach_baseline.py (RB.BODIES_TEX['P15'])  (the H1 read path)
  S3  as S1, with its literal recorded in quote_pin_baseline.tsv                  (adjudicated)
  S4  the figure asserted in a LABEL only, reading nothing                        (the unread-figure class)
Run twice: the planted receipts UNREGISTERED, then REGISTERED (an INDEX.md row each, in the worktree).
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
SENT = 'to the first three gives the sky $\\phi/\\pi=-0.2404$'
EDIT = ('gives the sky $\\phi/\\pi=-0.2404$', 'gives the sky $\\phi/\\pi=-0.2406$')
DIR = 'receipts/L999_lifecycle_seed'
LIT = json.dumps(SENT)          # the literal as Python source writes it

HEAD = '''import os, sys
FAILED = []
def check(label, ok):
    print(f"  {'OK  ' if ok else 'FAIL'} {label}")
    if not ok:
        FAILED.append(label)
'''
SEEDS = {
    'S1_names_the_paper': HEAD + f'''SRC = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read()
check("the sky phase sentence stands", {LIT} in SRC)
sys.exit(1 if FAILED else 0)
''',
    'S2_reads_through_reach_baseline': HEAD + f'''sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'corpus'))
import reach_baseline as RB
SRC = RB.BODIES_TEX['P15']
check("the sky phase sentence stands", {LIT} in SRC)
sys.exit(1 if FAILED else 0)
''',
    'S3_adjudicated': HEAD + f'''SRC = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read()
check("the sky phase sentence stands (adjudicated)", {LIT} in SRC)
sys.exit(1 if FAILED else 0)
''',
    'S4_label_only': HEAD + '''x = -0.24041
check(f"the fit returns {x:.4f}, the paper's -0.2404", abs(x - (-0.2404)) < 1e-3)
sys.exit(1 if FAILED else 0)
''',
}


def sh(cwd, *a, check=True):
    r = subprocess.run(list(a), cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise SystemExit(f'{a}: rc {r.returncode}\n{r.stdout[-2000:]}\n{r.stderr[-2000:]}')
    return r


def plant(wt, register):
    os.makedirs(os.path.join(wt, DIR), exist_ok=True)
    for name, src in SEEDS.items():
        open(os.path.join(wt, DIR, name + '.py'), 'w', encoding='utf-8').write(src)
    bl = os.path.join(wt, 'corpus', 'quote_pin_baseline.tsv')
    with open(bl, 'a', encoding='utf-8') as f:
        f.write(f'{DIR}/S3_adjudicated.py\t{LIT}\tPAPER\tSENTENCE\t\tDELIBERATE\tr7161+70.1 lifecycle seed S3\n')
    if register:
        with open(os.path.join(wt, 'receipts', 'INDEX.md'), 'a', encoding='utf-8') as f:
            for name in SEEDS:
                f.write(f'| P15 | sec:intro | lifecycle seed {name} | `L999_lifecycle_seed/{name}.py` | ✔ | seed |  | r7161+70.1 |\n')


#: ⛭ the proposed one-line repair to `_touched_pin_readers.py`, applied ONLY inside the throwaway worktree: a receipt
#:   that IMPORTS reach_baseline reads every `corpus/*.tex` (its `bodies()` globs them), so it counts as naming any
#:   changed paper.  The literal / number intersection after it is unchanged, so the cost is the 21 such receipts
#:   being string-scanned, not run.
PATCH = (("any(nm in src for nm in names)",
          "(any(nm in src for nm in names) or (any(nm.endswith('.tex') for nm in names) and "
          "re.search(r'^\\s*(?:import reach_baseline|from reach_baseline )', src, re.M)))"),)


def measure(register, patched=False):
    wt = tempfile.mkdtemp(prefix='lcseed_')
    os.rmdir(wt)
    sh(ROOT, 'git', 'worktree', 'add', '--detach', wt, 'HEAD')
    try:
        # ⛔ r7247+70.1: these were `git config user.email/user.name` in a linked WORKTREE, which shares the main
        #   repository's `.git/config` -- so they rewrote the identity of every later commit in the real checkout.
        #   Passed through the environment instead, which ends with the process.
        os.environ.update(GIT_AUTHOR_NAME='lifecycle seed', GIT_AUTHOR_EMAIL='seed@local',
                          GIT_COMMITTER_NAME='lifecycle seed', GIT_COMMITTER_EMAIL='seed@local')
        plant(wt, register)
        if patched:
            tp = os.path.join(wt, 'scripts', '_touched_pin_readers.py')
            t = open(tp, encoding='utf-8').read()
            for old, new in PATCH:
                assert t.count(old) == 2, t.count(old)
                t = t.replace(old, new)
            open(tp, 'w', encoding='utf-8').write(t)
        sh(wt, 'git', 'add', '-A')
        sh(wt, 'git', 'commit', '-qm', 'seed: plant')
        a = sh(wt, 'git', 'rev-parse', 'HEAD').stdout.strip()
        p = os.path.join(wt, 'corpus', 'CR_cosmology.tex')
        s = open(p, encoding='utf-8').read()
        assert s.count(EDIT[0]) == 1, s.count(EDIT[0])
        open(p, 'w', encoding='utf-8').write(s.replace(*EDIT))
        # the edit really breaks S1-S3: run them on the edited paper
        broken = {}
        for name in SEEDS:
            r = subprocess.run([sys.executable, '-W', 'ignore', name + '.py'], cwd=os.path.join(wt, DIR),
                               capture_output=True, text=True)
            broken[name] = r.returncode
        tpr = sh(wt, sys.executable, 'scripts/_touched_pin_readers.py', a, check=False)
        sel = {'run_touched_readers (_touched_pin_readers)': set(tpr.stdout.split())}
        sh(wt, 'git', 'add', '-A')
        sh(wt, 'git', 'commit', '-qm', 'seed: move the figure')
        b = sh(wt, 'git', 'rev-parse', 'HEAD').stdout.strip()
        for scope in ('suite', 'reads'):
            lst = os.path.join(wt, f'scope_{scope}.txt')
            r = sh(wt, sys.executable, 'scripts/receipt_scope.py', '--range', f'{a}..{b}', '--scope', scope,
                   '--list', lst, check=False)
            got = set(open(lst).read().split()) if os.path.exists(lst) else set()
            sel[f'receipt_scope --scope {scope}'] = got
            if r.returncode not in (0,):
                sel[f'receipt_scope --scope {scope}'] = got | {f'(rc {r.returncode}: {r.stderr.strip().splitlines()[-1][:120] if r.stderr.strip() else ""})'}
        return broken, sel
    finally:
        sh(ROOT, 'git', 'worktree', 'remove', '--force', wt, check=False)
        shutil.rmtree(wt, ignore_errors=True)


def main():
    for register, patched in ((False, False), (True, False), (True, True)):
        broken, sel = measure(register, patched)
        print(f'\n  == planted receipts {"REGISTERED in INDEX.md" if register else "UNREGISTERED"}'
              + ('  -- WITH THE PROPOSED _touched_pin_readers PATCH (worktree only)' if patched else ''))
        print('     does the paper edit break each seed?  ' +
              ', '.join(f'{n.split("_")[0]}: {"FAILS" if rc else "passes"}' for n, rc in broken.items()))
        for who, got in sel.items():
            extra = [g for g in got if g.startswith('(rc')]
            row = ['IN ' if any(g.endswith(n + '.py') for g in got) else 'out' for n in SEEDS]
            print(f'     {who:<45} ' + '  '.join(f'{n.split("_")[0]}:{r}' for n, r in zip(SEEDS, row))
                  + (f'   {extra[0]}' if extra else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
