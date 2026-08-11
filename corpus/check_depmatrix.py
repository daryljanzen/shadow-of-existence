#!/usr/bin/env python3
"""check_depmatrix.py -- the gate on the DEPENDENCY MATRIX, twelfth of the corpus's gates.

THE_PLAN's four-step state advance already says it: "Re-run scripts/depmatrix.py after ANY
citation change -- paste the LaTeX rows into P7's tab:dependency-matrix AND refresh
BOOK_INTRO_cosmiCave/assets/dependency_matrix.html."  ** Nothing failed when it was skipped. **

Found r2378, and the provenance was checked before it was claimed: run against the pristine
c54.108 tree AND the c54.134 tree, the recomputed rows mismatch the table 17 of 17 in BOTH.
Citations accumulated across a whole fork and the matrix was never refreshed, so the corpus's own
map of which paper leans on which had drifted -- P3's draw on P14 read 14 where it is 24, P7's on
P1 read 6 where it is 8.

** A stale dependency matrix is the same species as a stale grain, and worse in one respect: it
is a FIGURE.  A reader does not check a figure against a script; a figure is what they check other
things against. **

This gate FAILS rather than reports, because unlike RG-1 there is no judgement in it: the counts
are recomputed from the papers' own \\cite commands and either match or do not.

    python3 corpus/check_depmatrix.py

Written r2378.  Stated for reversal.
"""
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
PAPER = os.path.join(HERE, 'CR_framework.tex')
HTML = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'assets', 'dependency_matrix.html')
GEN = os.path.join(ROOT, 'scripts', 'depmatrix.py')
GENHTML = os.path.join(ROOT, 'scripts', 'gen_matrix_html_tbody.py')

ROW = re.compile(r'^(?:\\textbf\{)?([Pp]\d+|p0)(?: \\; [^}&]*)?\}?\s*&(.*?)\\\\\s*$', re.M)


def norm(s):
    return re.sub(r'\\textbf\{|\}|\s', '', s)


def recomputed():
    if not os.path.exists(GEN):
        return None
    out = subprocess.run([sys.executable, '-W', 'ignore', GEN], cwd=HERE,
                         capture_output=True, text=True)
    return {m.group(1): norm(m.group(2)) for m in ROW.finditer(out.stdout)}


def in_paper():
    t = open(PAPER, encoding='utf-8', errors='replace').read()
    i = t.find('tab:dependency-matrix')
    if i < 0:
        return None
    seg = t[max(0, i - 8000):i]
    return {m.group(1): norm(m.group(2)) for m in ROW.finditer(seg)}


def main():
    print()
    print('  DEPENDENCY MATRIX -- does P7\'s table still match the papers\' own citations?')
    print()
    new = recomputed()
    if not new:
        print('  [FAIL] cannot recompute: scripts/depmatrix.py did not return rows.')
        return 1
    old = in_paper()
    if old is None:
        print('  [FAIL] cannot find tab:dependency-matrix in CR_framework.tex.')
        return 1
    shared = [k for k in new if k in old]
    bad = [k for k in shared if new[k] != old[k]]
    print(f'  {len(new)} rows recomputed, {len(old)} rows in the table, {len(shared)} comparable.')
    print()
    if bad:
        print(f'  STALE ROWS: {len(bad)} of {len(shared)}')
        for k in bad[:20]:
            print(f'    [FAIL] {k}')
            print(f'        table: {old[k][:110]}')
            print(f'        now:   {new[k][:110]}')
        print()
        print('  ⛔ The matrix does not match the corpus it describes.')
        print('     Fix: run scripts/depmatrix.py from corpus/, paste the LaTeX rows into')
        print('     P7 tab:dependency-matrix, then refresh the HTML with')
        print('     scripts/gen_matrix_html_tbody.py.  This is step 2 of the state advance.')
        return 1
    print('  Every row matches the recomputed counts.')

    # the HTML companion is the same claim in a second place, so it is checked too
    if os.path.exists(HTML) and os.path.exists(GENHTML):
        gen = subprocess.run([sys.executable, '-W', 'ignore', GENHTML], cwd=HERE,
                             capture_output=True, text=True).stdout.strip()
        cur = open(HTML, encoding='utf-8', errors='replace').read()
        i, j = cur.find('<tbody>'), cur.find('</tbody>')
        if i >= 0 and j > i and gen:
            if cur[i:j + len('</tbody>')].strip() != gen:
                print()
                print('  [FAIL] the HTML companion (BOOK_INTRO_cosmiCave/assets/'
                      'dependency_matrix.html) does not match.')
                print('         The same claim in two places, and only one was refreshed --')
                print('         which is the correction-reaches-one-grain failure exactly.')
                return 1
            print('  The HTML companion matches too.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
