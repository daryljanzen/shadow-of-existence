"""perturb_pins.py -- r7164+70.1 (70): for a FORMULA/FIGURE site whose file carries a quote-pin of the ATTRIBUTED
expression (hand-picked below, each read), mutate that printed expression in the papers and run the receipt.
RED-ON-MOVE means the paper's expression IS pinned by the file, so the site's hard-coded copy is not a debt."""
import os, re, shutil, subprocess, sys, tempfile, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
from perturb import run  # noqa: E402
S = json.load(open(os.path.join(HERE, 'sites.json')))
PINS = {int(k): v for k, v in {
    26: ['$c_{0}B(\\tfrac16,\\tfrac12)/2=3.33874$'],
    27: ['$\\ell\\simeq28$', '$\\ell\\simeq2475$'],
    29: ['$T(k)\\to2^{7/3}k^2e^{-k\\,s_{\\rm tot}}$'],
}.items()} if __import__('sys').argv[1:] == ['second'] else {
    3: ['Every $\\mathbb{Z}_2$ grading splits those four $2+2$'],
    12: ['attaining $\\gamma=\\tfrac14$ across the natural ordering family'],
    16: ["the tower's frequencies are $\\mu_n^2=n(n+2)$", 'the degeneracy is $2(n-1)(n+3)$'],
    28: ['so $L(L+2)$ is its $\\varepsilon=1$ member'],
    31: ['ds^2=-d\\tau^2+(\\partial_\\chi r)^2\\,d\\chi^2+r^2 d\\Omega^2'],
    32: ['the phase $\\varphi=2\\pi r/\\sqrt3\\alpha$'],
    34: ['ds^2=-d\\tau^2+(\\partial_\\chi r)^2\\,d\\chi^2+r^2 d\\Omega^2'],
    38: ["$f(r_{N})=f'(r_{N})=0$ and $f''(r_{N})=-2\\Lambda$"],
    42: ['3\\pi/(\\Lambda\\ell_P^2)', '3\\pi/(\\Lambda\\ell_P^{2})'],
}


def mutate(p):
    m = re.search(r'\d', p)
    if m:
        d = p[m.start()]
        return p[:m.start()] + ('8' if d == '9' else str(int(d) + 1)) + p[m.end():]
    return p[:1] + 'Q' + p[1:]


wt = tempfile.mkdtemp(prefix='p43p_'); os.rmdir(wt)
subprocess.run(['git', 'worktree', 'add', '--detach', wt, 'HEAD'], cwd=ROOT, capture_output=True)
try:
    for i, pins in PINS.items():
        rp = S[i]['receipt']
        base = run(wt, rp)[0]
        n = 0
        for f in os.listdir(os.path.join(wt, 'corpus')):
            if not f.endswith('.tex') or f.startswith('appendix_'):
                continue
            path = os.path.join(wt, 'corpus', f)
            t = open(path, encoding='utf-8').read()
            t2 = t
            for p in pins:
                n += t2.count(p)
                t2 = t2.replace(p, mutate(p))
            if t2 != t:
                open(path, 'w', encoding='utf-8').write(t2)
        rc, tail = run(wt, rp)
        subprocess.run(['git', 'checkout', '-q', '--', 'corpus/'], cwd=wt)
        res = 'RED-ON-MOVE' if rc not in (0, 'TIMEOUT') else ('GREEN-ON-MOVE' if rc == 0 else 'TIMEOUT')
        print(f'{i:2d} base rc {base}  {res:<14} {n} printed occurrence(s) mutated  {os.path.basename(rp)[:60]}', flush=True)
        for l in [l.strip() for l in tail.splitlines() if 'FAIL' in l][:2]:
            print('      ', l[:170], flush=True)
finally:
    subprocess.run(['git', 'worktree', 'remove', '--force', wt], cwd=ROOT, capture_output=True)
    shutil.rmtree(wt, ignore_errors=True)
