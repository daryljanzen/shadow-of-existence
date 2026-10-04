"""perturb_manual.py -- r7164+70.1 (70): where the operator's figure is the receipt's OWN digits and the paper prints
fewer (site 30: `3.3387380236` vs the paper's `3.33874`), move the number the PAPER prints, by hand-named token.
Same worktree discipline as perturb.py.  Each move is far outside any tolerance."""
import os, re, shutil, subprocess, sys, tempfile, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
from perturb import run  # noqa: E402
S = json.load(open(os.path.join(HERE, 'sites.json')))
MOVES = {
    30: [('CR_cosmology.tex', '3.33874', '4.57407')],
    35: [(None, '43.8232', '60.0378')],
    39: [('CR_cosmology.tex', '1.53', '2.10')],
}
wt = tempfile.mkdtemp(prefix='p43m_'); os.rmdir(wt)
subprocess.run(['git', 'worktree', 'add', '--detach', wt, 'HEAD'], cwd=ROOT, capture_output=True)
try:
    for i, mv in MOVES.items():
        rp = S[i]['receipt']
        base = run(wt, rp)[0]
        n = 0
        for paper, old, new in mv:
            for f in ([os.path.join(wt, 'corpus', paper)] if paper else
                      [os.path.join(wt, 'corpus', x) for x in os.listdir(os.path.join(wt, 'corpus'))
                       if x.endswith('.tex') and not x.startswith('appendix_')]):
                t = open(f, encoding='utf-8').read()
                t2, k = re.subn(r'(?<![\d.])' + re.escape(old) + r'(?!\d)', new, t)
                if k:
                    open(f, 'w', encoding='utf-8').write(t2); n += k
        rc, tail = run(wt, rp)
        subprocess.run(['git', 'checkout', '-q', '--', 'corpus/'], cwd=wt)
        res = 'RED-ON-MOVE' if rc not in (0, 'TIMEOUT') else ('GREEN-ON-MOVE' if rc == 0 else 'TIMEOUT')
        print(f'{i:2d} base rc {base}  {res:<14} moved {mv} in {n} place(s)  {os.path.basename(rp)[:60]}')
        for l in [l.strip() for l in tail.splitlines() if 'FAIL' in l or 'Error' in l][:3]:
            print('      ', l[:170])
finally:
    subprocess.run(['git', 'worktree', 'remove', '--force', wt], cwd=ROOT, capture_output=True)
    shutil.rmtree(wt, ignore_errors=True)
