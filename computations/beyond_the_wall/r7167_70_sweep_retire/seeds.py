"""seeds.py -- r7167+70.1 (70) T2 and T4: the window control, and the retirement rule against seeded papers.

  python3 seeds.py

T2: every RETIRED-CITED row's closing distance, and how a FIXED 300-character window would have classified it.
T4: in a throwaway worktree, (a) delete every `\\rcpt{P04_redshift_isotropy_floor}` from modern_parallax.tex -- the
    0.285 row must go LIVE and its property test must run and pass; (b) restore, then print 0.290 where the paper
    prints 0.285 -- the row must go RETIRED-DRIFTED.  C1 is run whole each time.
"""
import os, re, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
C1 = 'receipts/L_probability/C1_the_citation_sweep_finds_no_headline_mis_cited_and_thirteen_below_it_that_cite_the_wrong_receipt_or_none.py'


def run_c1(root):
    d, b = os.path.split(os.path.join(root, C1))
    p = subprocess.run([sys.executable, '-W', 'ignore', b], cwd=d, capture_output=True, text=True, timeout=900)
    return p.returncode, p.stdout + p.stderr


def rows(out):
    return [l.strip() for l in out.splitlines() if re.match(r'\s*\[(RETIRED-\w+|PASS|FAIL)\] \(ii+\)', l)]


rc, out = run_c1(ROOT)
print(f'== T2 on the live tree (rc {rc}) -- closing distance, and a fixed 300-character window\'s reading')
opened = 0
for l in rows(out):
    m = re.search(r'\((ii+)\) (.*?): (\[.*?\]).*?at (\+[\d, +]+) chars', l)
    if m:
        ds = [int(x) for x in re.findall(r'\d+', m.group(4))]
        w = 'OPEN under a 300-char window' if max(ds) > 300 else 'retired under it too'
        opened += max(ds) > 300
        print(f'    {m.group(2)[:45]:<45} {m.group(3)[:28]:<28} +{max(ds):>5}  {w}')
print(f'    => a fixed 300-character window would have called {opened} of these rows open\n')

wt = tempfile.mkdtemp(prefix='c1seed_'); os.rmdir(wt)
subprocess.run(['git', 'worktree', 'add', '--detach', wt, 'HEAD'], cwd=ROOT, capture_output=True)
try:
    shutil.copy(os.path.join(ROOT, C1), os.path.join(wt, C1))           # the working copy under test
    mp = os.path.join(wt, 'corpus', 'modern_parallax.tex')
    orig = open(mp, encoding='utf-8').read()
    for tag, text in (('(a) every \\rcpt{P04_redshift_isotropy_floor} deleted', orig.replace('\\rcpt{P04_redshift_isotropy_floor}', '')),
                      ('(b) 0.285 printed as 0.290', re.sub(r'(?<![\d.])0\.285(?![\d])', '0.290', orig))):
        open(mp, 'w', encoding='utf-8').write(text)
        rc, out = run_c1(wt)
        row = [l for l in rows(out) if 'modern_parallax' in l]
        ran = [l.strip() for l in out.splitlines() if l.strip().startswith('ran ')]
        print(f'== T4 {tag}: C1 rc {rc}')
        for l in row:
            print('    ', l[:200])
        print(f'     runs: {ran or "none"}')
    open(mp, 'w', encoding='utf-8').write(orig)
finally:
    subprocess.run(['git', 'worktree', 'remove', '--force', wt], cwd=ROOT, capture_output=True)
    shutil.rmtree(wt, ignore_errors=True)
