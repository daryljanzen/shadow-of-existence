#!/usr/bin/env python3
"""check_pages_current.py -- A SERVED PAGE MUST BE THE ONE ITS SOURCE GENERATES.

** WHY THIS EXISTS. **  Editing a paper's `.tex` does not regenerate the chapter the book
serves.  At r6477 four of seven served pages were behind their sources -- every one of them
a paper edited that day -- and `paper_P17.html` was still publishing a claim the corpus had
WITHDRAWN at r6465, because the correction landed in the `.tex` and the page was never
rebuilt.  ** A withdrawn claim on a served page is not a stale note; it is the book telling
a reader something the corpus has retracted. **

** THE SHAPE IS THE ONE `check_appendix_current` ALREADY PROVED. **  Regenerate into a
temporary file, compare to what is committed, report a divergence.  Not an mtime check:
mtimes are reset by any checkout and would report a clean tree as dirty and a stale page as
fresh.

⚠ AND THE SAME WARNING THAT GATE CARRIES APPLIES HERE.  ** This reports that the rails
diverge; it does not tell you which side is right. **  Read the diff before regenerating --
a page can differ because its source moved, which wants a rebuild, or because the generator
moved, which may want neither.
"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
GEN = os.path.join(ROOT, 'scripts', 'gen_paper_html.py')
PAGES = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave')


def served_pages():
    if not os.path.isdir(PAGES):
        return []
    out = []
    for f in sorted(os.listdir(PAGES)):
        if f.startswith('paper_') and f.endswith('.html'):
            out.append((f[len('paper_'):-len('.html')], os.path.join(PAGES, f)))
    return out


def main():
    if not os.path.exists(GEN):
        print('  [FAIL] scripts/gen_paper_html.py missing')
        return 1
    pages = served_pages()
    print()
    print(f'  SERVED PAGES -- is each the one its source generates?  ({len(pages)} page(s))')
    print()
    stale, failed = [], []
    for pid, path in pages:
        before = open(path, 'rb').read()
        r = subprocess.run([sys.executable, GEN, pid], cwd=ROOT,
                           capture_output=True, text=True)
        if r.returncode != 0:
            failed.append((pid, (r.stderr or '').strip().split('\n')[-1][:70]))
            continue
        after = open(path, 'rb').read()
        if after != before:
            stale.append((pid, len(after) - len(before)))
        if after != before:
            open(path, 'wb').write(before)      # leave the tree as found
        print(f'    {pid:<6} {"REGENERATES DIFFERENTLY" if after != before else "current"}')
    print()
    if failed:
        print(f'  ⛔ {len(failed)} page(s) whose generator failed:')
        for pid, err in failed:
            print(f'    [FAIL] {pid}: {err}')
    if stale:
        print(f'  ⛔ {len(stale)} SERVED PAGE(S) BEHIND THEIR SOURCE:')
        for pid, d in stale:
            print(f'    [FAIL] paper_{pid}.html differs by {d:+d} bytes from what its .tex generates')
        print('     Run: python3 scripts/gen_paper_html.py <id>   -- after reading the diff.')
        print('     ⌗ The tree is left as found; this gate reports, it does not rebuild.')
        print()
        return 1
    if failed:
        return 1
    print('  every served page is the one its source generates.')
    print('  ⌗ A withdrawn claim reaching a served page is the case this was built for:')
    print('    the correction landed in the .tex and the book kept publishing the claim.')
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
