"""convention_seed.py -- r7163+70.1 (70) ⓶: one planted receipt per NON-LITERAL reading convention the census
found, each pinning the same `CR_cosmology.tex` sentence and broken by the same edit, asked of every selector.
Pre-registered at PREDICTION.md beside this file.  Apparatus: r7161_70_lifecycle_seed/lifecycle_seed.py's.

  python3 convention_seed.py

THE REAL TREE IS NEVER TOUCHED: everything happens in `git worktree add --detach <tmp> HEAD`, removed at exit.
Selectors asked:
  run_touched_readers (main)     scripts/_touched_pin_readers.py as it stands on main (66's r7163 patch included)
  run_touched_readers (PROPOSED) proposed_touched_pin_readers.py beside this file, copied over it in the worktree
  receipt_scope --scope suite    and --scope reads
  TRACE (run and watch)          scripts/sweep_runner_reads.py --from <the seeds>, then: did the trace record the
                                 paper?  This is the run-and-watch instrument, measured on the same seeds.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SENT = 'to the first three gives the sky $\\phi/\\pi=-0.2404$'
EDIT = ('gives the sky $\\phi/\\pi=-0.2404$', 'gives the sky $\\phi/\\pi=-0.2406$')
DIR = 'receipts/L998_convention_seed'
LIT = json.dumps(SENT)
UP = "os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')"

HEAD = '''import os, sys
FAILED = []
def check(label, ok):
    print(f"  {'OK  ' if ok else 'FAIL'} {label}")
    if not ok:
        FAILED.append(label)
'''
TAIL = f'check("the sky phase sentence stands", {LIT} in SRC)\nsys.exit(1 if FAILED else 0)\n'

#: the planted receipts (registered) and their non-receipt support files (not registered)
SEEDS = {
    'K0a_NAME_control': f"SRC = open(os.path.join({UP}, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read()\n",
    'K0b_RB_IMPORT_control': f"sys.path.append(os.path.join({UP}, 'corpus'))\nimport reach_baseline as RB\n"
                             "SRC = RB.BODIES_TEX['P15']\n",
    'K1_GLOB': f"import glob\nSRC = ' '.join(open(f, encoding='utf-8').read() for f in sorted(glob.glob("
               f"os.path.join({UP}, 'corpus', '*.tex'))))\n",
    'K2_LISTDIR': f"C = os.path.join({UP}, 'corpus')\nSRC = ' '.join(open(os.path.join(C, f), encoding='utf-8').read() "
                  "for f in sorted(os.listdir(C)) if f.endswith('.tex'))\n",
    'K3_RB_PATHLOAD': f"import importlib.util\n_s = importlib.util.spec_from_file_location('rb', os.path.join({UP}, "
                      "'corpus', 'reach_baseline.py'))\nRB = importlib.util.module_from_spec(_s)\n_s.loader.exec_module(RB)\n"
                      "SRC = RB.BODIES_TEX['P15']\n",
    'K4_HELPER': f"sys.path.insert(0, os.path.join({UP}, 'corpus'))\nimport _seed_paper_text as H\nSRC = H.everything()\n",
    'K5_RECEIPT_IMPORT': "sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))\n"
                         "from _seed_sibling_reader import TEXT as SRC\n",
    'K6_CHILD_PROCESS': "import subprocess\nSRC = subprocess.run([sys.executable, '_seed_sibling_cat.py'], cwd="
                        "os.path.dirname(os.path.abspath(__file__)), capture_output=True, text=True).stdout\n",
    'K7_STEM': f"PAPER = 'CR_cosmology'\nSRC = open(os.path.join({UP}, 'corpus', PAPER + '.tex'), encoding='utf-8').read()\n",
    'K8_TABLE': "import json\n_d = os.path.dirname(os.path.abspath(__file__))\n"
                "_p = json.load(open(os.path.join(_d, '_seed_papers.json')))['P15']\n"
                "SRC = open(os.path.join(_d, '..', '..', _p[0], _p[1]), encoding='utf-8').read()\n",
}
SUPPORT = {
    'corpus/_seed_paper_text.py': "import glob, os\n\ndef everything():\n    d = os.path.dirname(os.path.abspath(__file__))\n"
                                  "    return ' '.join(open(f, encoding='utf-8').read() for f in sorted(glob.glob("
                                  "os.path.join(d, '*.tex'))))\n",
    f'{DIR}/_seed_sibling_reader.py': f"import os\nTEXT = open(os.path.join({UP}, 'corpus', 'CR_cosmology.tex'), "
                                      "encoding='utf-8').read()\n",
    f'{DIR}/_seed_sibling_cat.py': f"import glob, os\nfor f in sorted(glob.glob(os.path.join({UP}, 'corpus', '*.tex'))):\n"
                                   "    print(open(f, encoding='utf-8').read())\n",
    f'{DIR}/_seed_papers.json': json.dumps({'P15': ['corp' + 'us', 'CR_cosmo' + 'logy.t' + 'ex']}) + '\n',
}


def sh(cwd, *a, check=True, env=None):
    r = subprocess.run(list(a), cwd=cwd, capture_output=True, text=True, env=env)
    if check and r.returncode != 0:
        raise SystemExit(f'{a}: rc {r.returncode}\n{r.stdout[-2000:]}\n{r.stderr[-2000:]}')
    return r


def plant(wt):
    os.makedirs(os.path.join(wt, DIR), exist_ok=True)
    for name, body in SEEDS.items():
        open(os.path.join(wt, DIR, name + '.py'), 'w', encoding='utf-8').write(HEAD + body + TAIL)
    for p, body in SUPPORT.items():
        open(os.path.join(wt, p), 'w', encoding='utf-8').write(body)
    with open(os.path.join(wt, 'receipts', 'INDEX.md'), 'a', encoding='utf-8') as f:
        for name in SEEDS:
            f.write(f'| P15 | sec:intro | convention seed {name} | `L998_convention_seed/{name}.py` | ✔ | seed |  | r7163+70.1 |\n')


def main():
    wt = tempfile.mkdtemp(prefix='convseed_')
    os.rmdir(wt)
    sh(ROOT, 'git', 'worktree', 'add', '--detach', wt, 'HEAD')
    try:
        # ⛔ r7247+70.1: these two lines were `git config user.email/user.name` run in the WORKTREE -- and a linked
        #   worktree SHARES the main repository's `.git/config`, so they rewrote the identity of every later commit
        #   in the real checkout (this seat's own from r7245+70.0, and plausibly every seat that ran this script).
        #   The identity is now passed per command through the environment, which cannot outlive the process.
        os.environ.update(GIT_AUTHOR_NAME='convention seed', GIT_AUTHOR_EMAIL='seed@local',
                          GIT_COMMITTER_NAME='convention seed', GIT_COMMITTER_EMAIL='seed@local')
        plant(wt)
        # the source-literal audit: which seeds' OWN source names the paper (only the NAME control may)
        own = {n: 'CR_cosmology.tex' in open(os.path.join(wt, DIR, n + '.py')).read() for n in SEEDS}
        before = {}
        for name in SEEDS:
            before[name] = subprocess.run([sys.executable, '-W', 'ignore', name + '.py'], cwd=os.path.join(wt, DIR),
                                          capture_output=True, text=True).returncode
        # RUN AND WATCH: trace the seeds before the edit, write their entries into the worktree's READ_INDEX
        lst = os.path.join(wt, 'seeds.txt')
        open(lst, 'w').write('\n'.join(f'{DIR}/{n}.py' for n in SEEDS) + '\n')
        tdir = os.path.join(wt, '_trace')
        t0 = time.time()
        tr = sh(wt, sys.executable, 'scripts/sweep_runner_reads.py', '--out', tdir, '--from', lst, check=False)
        t_trace = time.time() - t0
        traced = {}
        for name in SEEDS:
            rec = None
            for fn in os.listdir(tdir) if os.path.isdir(tdir) else []:
                if name in fn and fn.endswith('.json'):
                    rec = json.load(open(os.path.join(tdir, fn)))
            reads = json.dumps(rec) if rec else ''
            traced[name] = ('corpus/CR_cosmology.tex' in reads) if rec else None
        sh(wt, 'git', 'add', '-A')
        sh(wt, 'git', 'commit', '-qm', 'seed: plant')
        a = sh(wt, 'git', 'rev-parse', 'HEAD').stdout.strip()
        p = os.path.join(wt, 'corpus', 'CR_cosmology.tex')
        s = open(p, encoding='utf-8').read()
        assert s.count(EDIT[0]) == 1, s.count(EDIT[0])
        open(p, 'w', encoding='utf-8').write(s.replace(*EDIT))
        after = {}
        for name in SEEDS:
            after[name] = subprocess.run([sys.executable, '-W', 'ignore', name + '.py'], cwd=os.path.join(wt, DIR),
                                         capture_output=True, text=True).returncode
        sel = {}
        r = sh(wt, sys.executable, 'scripts/_touched_pin_readers.py', a, check=False)
        sel['run_touched_readers (main, 66 patch in)'] = set(r.stdout.split())
        shutil.copy(os.path.join(HERE, 'proposed_touched_pin_readers.py'), os.path.join(wt, 'scripts', '_prop.py'))
        t0 = time.time()
        r = sh(wt, sys.executable, 'scripts/_prop.py', a, check=False)
        t_prop = time.time() - t0
        sel['run_touched_readers (PROPOSED)'] = set(r.stdout.split())
        if r.returncode:
            print(r.stderr[-1500:])
        sh(wt, 'git', 'add', '-A')
        sh(wt, 'git', 'commit', '-qm', 'seed: move the figure')
        b = sh(wt, 'git', 'rev-parse', 'HEAD').stdout.strip()
        for scope in ('suite', 'reads'):
            out = os.path.join(wt, f'scope_{scope}.txt')
            r = sh(wt, sys.executable, 'scripts/receipt_scope.py', '--range', f'{a}..{b}', '--scope', scope,
                   '--list', out, check=False)
            sel[f'receipt_scope --scope {scope}'] = set(open(out).read().split()) if os.path.exists(out) else set()
        print(f'\n  {"seed":<24} {"names paper":>11} {"rc before":>9} {"rc after":>8} {"TRACE sees":>10}   ' +
              '   '.join(f'{k}' for k in sel))
        for name in SEEDS:
            row = ['IN ' if any(g.endswith(name + '.py') for g in got) else 'out' for got in sel.values()]
            tv = {True: 'yes', False: 'NO', None: '—'}[traced[name]]
            print(f'  {name:<24} {str(own[name]):>11} {before[name]:>9} {after[name]:>8} {tv:>10}   ' +
                  '   '.join(f'{r:^{len(k)}}' for r, k in zip(row, sel)))
        print(f'\n  trace of the {len(SEEDS)} seeds: {t_trace:.1f}s wall (rc {tr.returncode});  PROPOSED selector: {t_prop:.1f}s')
        print(f'  PROPOSED selected {len(sel["run_touched_readers (PROPOSED)"])} receipt(s) in all; main selected '
              f'{len(sel["run_touched_readers (main, 66 patch in)"])}')
        for k in ('run_touched_readers (main, 66 patch in)', 'run_touched_readers (PROPOSED)'):
            extra = sorted(g for g in sel[k] if 'L998_convention_seed' not in g)
            print(f'    {k}: non-seed receipts selected: {len(extra)}  {[os.path.basename(x)[:50] for x in extra]}')
        return 0
    finally:
        sh(ROOT, 'git', 'worktree', 'remove', '--force', wt, check=False)
        shutil.rmtree(wt, ignore_errors=True)


if __name__ == '__main__':
    sys.exit(main())
