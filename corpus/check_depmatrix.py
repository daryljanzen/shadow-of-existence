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

ORDER = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12',
         'P13','P14','P15','P16','p0']

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
    # The LABEL, not the first mention: \ref{tab:dependency-matrix} occurs ~15k
    # characters earlier in the prose, and a backward window from THAT lands
    # nowhere near the table.  Found r3522 -- the gate had been reading an empty
    # slice and reporting "every row matches" over zero comparisons.
    i = t.find('\\label{tab:dependency-matrix}')
    if i < 0:
        return None
    j = t.rfind('\\begin{tabular}', 0, i)
    if j < 0:
        return None
    return {m.group(1): norm(m.group(2)) for m in ROW.finditer(t[j:i])}


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
    # A check that compares nothing must not return clean.  Before r3522 an empty
    # `shared` made `bad` empty and the gate printed "every row matches" -- a pass
    # that could not have been anything else.  Every recomputed row must be found.
    missing = [k for k in new if k not in old]
    if missing:
        print(f'  [FAIL] {len(missing)} of {len(new)} recomputed rows were not found in the table:')
        print(f'         {", ".join(missing)}')
        print('         The gate cannot compare what it cannot parse, and a check that')
        print('         compares nothing is not a check.  Repair the reader before trusting')
        print('         any verdict from this gate.')
        return 1
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

    # The figure is the THIRD place this claim is made, and the table's own
    # maintenance note already says to harmonise it.  Found stale in seven edge
    # labels at r3522 while the table was being refreshed -- so it is gated now
    # rather than left to a note.  Convention: dep/feed are `->`, so an edge
    # X --> Y is labelled M[Y][X], the number of times Y cites X.
    t = open(PAPER, encoding='utf-8', errors='replace').read()
    M = {a: dict(zip(ORDER, v.split('&'))) for a, v in new.items()}
    fig = []
    for m in re.finditer(r'\\draw\[(?:dep|feed)\][^;]*?\((P\d+)\)[^;]*?'
                         r'node\[wt[^\]]*\]\{(\d+)\}[^;]*?\((P\d+)\)|'
                         r'\\draw\[(?:dep|feed)\][^;]*?\((P\d+)\)\s*--\s*\((P\d+)\)\s*'
                         r'node\[wt[^\]]*\]\{(\d+)\}', t):
        g = m.groups()
        x, lab, y = (g[0], g[1], g[2]) if g[0] else (g[3], g[5], g[4])
        want = M.get(y, {}).get(x)
        if want is not None and want != lab:
            fig.append((x, y, lab, want))
    if fig:
        print()
        print(f'  [FAIL] the dependency FIGURE disagrees with the matrix in '
              f'{len(fig)} edge label(s):')
        for x, y, lab, want in fig:
            print(f'         {x} --> {y}: figure says {lab}, matrix says {want}')
        print('         A reader checks other things against a figure, not a figure')
        print('         against a script.  Harmonise fig:dependency-structure.')
        return 1
    print('  The dependency figure matches too.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
