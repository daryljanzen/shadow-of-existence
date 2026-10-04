"""perturb.py -- r7164+70.1 (70): for each owed site with a DISTINCTIVE figure (a decimal, or an integer of two or
more digits), move every occurrence of that figure in corpus/*.tex and run the receipt.  PREDICTION.md beside this.

RED-ON-MOVE   the receipt fails with the paper's figure moved: it reads the figure somewhere (not a debt).
GREEN-ON-MOVE the receipt passes with the paper's figure moved: the site's debt is real.
Each receipt is first run unperturbed (it must pass), then perturbed; corpus/ is restored between sites.
Everything happens in a throwaway `git worktree` of HEAD.

  python3 perturb.py
"""
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import run_all_receipts as RA  # noqa: E402

LONG = getattr(RA, 'LONG', {})


def distinctive(x):
    return '.' in x or 'e' in x or len(x) >= 2


def moved(x):
    """a different value with the same digit count: bump the last digit (9 -> 8)"""
    d = x[-1]
    if not d.isdigit():
        return None
    return x[:-1] + ('8' if d == '9' else str(int(d) + 1))


def tok(x):
    return re.compile(r'(?<![\d.])' + re.escape(x) + r'(?![\d])')


def run(wt, rp):
    d, b = os.path.split(os.path.join(wt, rp))
    t = LONG.get(b, 900)
    try:
        p = subprocess.run([sys.executable, '-W', 'ignore', b], cwd=d, capture_output=True, text=True, timeout=t,
                           env=dict(os.environ, MPLBACKEND='Agg'))
        return p.returncode, (p.stdout + p.stderr)[-1500:]
    except subprocess.TimeoutExpired:
        return 'TIMEOUT', ''


def main():
    sites = json.load(open(os.path.join(HERE, 'sites.json')))
    wt = tempfile.mkdtemp(prefix='p43_')
    os.rmdir(wt)
    subprocess.run(['git', 'worktree', 'add', '--detach', wt, 'HEAD'], cwd=ROOT, capture_output=True)
    out = []
    base_rc = {}
    try:
        for i, s in enumerate(sites):
            figs = [f for f in s['figs'] if distinctive(f)]
            if not figs:
                out.append(dict(i=i, receipt=s['receipt'], site=s['site'], result='NOT-PERTURBABLE', figs=s['figs']))
                continue
            rp = s['receipt']
            if rp not in base_rc:
                base_rc[rp] = run(wt, rp)[0]
            touched = {}
            for f in sorted(glob.glob(os.path.join(wt, 'corpus', '*.tex'))):
                t = open(f, encoding='utf-8').read()
                n = 0
                for x in figs:
                    m = moved(x)
                    if m:
                        t, k = tok(x).subn(m, t)
                        n += k
                if n:
                    open(f, 'w', encoding='utf-8').write(t)
                    touched[os.path.basename(f)] = n
            if not touched:
                res, tail = 'NOT-IN-PAPER', ''
            else:
                rc, tail = run(wt, rp)
                res = 'RED-ON-MOVE' if rc not in (0, 'TIMEOUT') else ('GREEN-ON-MOVE' if rc == 0 else 'TIMEOUT')
            subprocess.run(['git', 'checkout', '-q', '--', 'corpus/'], cwd=wt)
            fails = [l.strip() for l in tail.splitlines() if 'FAIL' in l][:3]
            out.append(dict(i=i, receipt=rp, site=s['site'], figs=figs, base_rc=base_rc[rp], result=res,
                            touched=touched, fails=fails))
            print(f'{i:2d} base rc {base_rc[rp]}  {res:<16} {figs}  in {sum(touched.values())} place(s) of '
                  f'{len(touched)} paper(s)  {os.path.basename(rp)[:60]}', flush=True)
            for l in fails:
                print(f'       {l[:160]}', flush=True)
    finally:
        json.dump(out, open(os.path.join(HERE, 'perturb.json'), 'w'), indent=1, ensure_ascii=False)
        subprocess.run(['git', 'worktree', 'remove', '--force', wt], cwd=ROOT, capture_output=True)
        shutil.rmtree(wt, ignore_errors=True)


if __name__ == '__main__':
    main()
