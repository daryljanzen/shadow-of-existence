"""seeds.py -- r7169+70.1 (70) D2-D5: the four states of one finding, seeded in a throwaway worktree, C1 run whole.

The finding: `modern_parallax` sec:floor's 0.285, mis-cited at r7043 to R2 and computed by P04, repaired by citing P04.
  repair kept      the tree as it is                                  -> RETIRED-CITED
  defect returns   every \\rcpt{P04_redshift_isotropy_floor} -> \\rcpt{R2_...}  -> LIVE-DEFECT (property runs, rc 0)
  rewrite          every \\rcpt{P04_redshift_isotropy_floor} -> \\rcpt{R50_...} -> LIVE-UNRECOGNISED (rc 1, runs nothing)
  figure moved     0.285 printed as 0.290                             -> RETIRED-DRIFTED
"""
import os, re, shutil, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
C1 = 'receipts/L_probability/C1_the_citation_sweep_finds_no_headline_mis_cited_and_thirteen_below_it_that_cite_the_wrong_receipt_or_none.py'
P04 = '\\rcpt{P04_redshift_isotropy_floor}'
R2 = '\\rcpt{R2_the_papers_correlation_figures_are_the_ones_nothing_checked}'
R50 = '\\rcpt{R50_the_long_wavelength_bullet_reverses_for_the_observable_and_the_corner_is_three_parts_per_million}'

wt = tempfile.mkdtemp(prefix='c1def_'); os.rmdir(wt)
subprocess.run(['git', 'worktree', 'add', '--detach', wt, 'HEAD'], cwd=ROOT, capture_output=True)
try:
    shutil.copy(os.path.join(ROOT, C1), os.path.join(wt, C1))
    mp = os.path.join(wt, 'corpus', 'modern_parallax.tex')
    orig = open(mp, encoding='utf-8').read()
    firsts = []
    for tag, text in (('repair kept', orig), ('defect returns', orig.replace(P04, R2)),
                      ('rewrite (a third receipt)', orig.replace(P04, R50)),
                      ('figure moved', re.sub(r'(?<![\d.])0\.285(?![\d])', '0.290', orig)),
                      # ⌗ ADDED AFTER THE PRE-REGISTERED RUN: the pre-registered rewrite seed swapped P04 alone, but
                      #   the closing group is P04+R2 jointly, so R2 -- the ORIGINALLY cited receipt -- still closed
                      #   the figure, and LIVE-DEFECT was the correct reading.  This seed replaces the WHOLE group.
                      ('rewrite (the whole closing group -> a third receipt)', orig.replace(P04 + R2, R50))):
        open(mp, 'w', encoding='utf-8').write(text)
        d, b = os.path.split(os.path.join(wt, C1))
        p = subprocess.run([sys.executable, '-W', 'ignore', b], cwd=d, capture_output=True, text=True, timeout=900)
        out = p.stdout + p.stderr
        row = [l.strip() for l in out.splitlines() if 'modern_parallax' in l and re.search(r'\[(RETIRED-\w+|PASS|FAIL)\]', l)]
        ran = [l.strip()[:90] for l in out.splitlines() if l.strip().startswith('ran ')]
        print(f'== {tag}: C1 rc {p.returncode}')
        for l in row:
            print('    ', l[:260])
        print(f'     runs: {ran or "none"}')
        firsts.append(row[0][:40] if row else '')
    print(f'\n== D5: distinct first lines across the {len(firsts)} seeds: {len(set(firsts))}')
    open(mp, 'w', encoding='utf-8').write(orig)
finally:
    subprocess.run(['git', 'worktree', 'remove', '--force', wt], cwd=ROOT, capture_output=True)
    shutil.rmtree(wt, ignore_errors=True)
