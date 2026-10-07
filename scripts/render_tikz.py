#!/usr/bin/env python3
"""render_tikz.py -- A FIGURE DRAWN IN TIKZ IS STILL A FIGURE.

** WHY THIS EXISTS. **  `gen_paper_html.py` renders a figure by carrying its
`\\includegraphics` across.  A figure whose picture is a `tikzpicture` has no
`\\includegraphics`, so the generator emitted the caption and dropped the drawing --
leaving a page that says "Figure 3." and then describes, at length, a diagram that is
not there.  Measured at r7207: four such figures, two in `P7` and two in `P15`, every
one of them a caption with nothing above it.

** THE FIX IS TO RENDER THEM, not to teach the page to apologise. **  Each
`tikzpicture` inside a `figure` with a `\\label` is compiled standalone against the same
packages its paper loads, cropped to the drawing, and written to
`BOOK_INTRO_cosmiCave/fig/tikz_<label>.svg`.  SVG rather than a raster because these are
line diagrams with text in them: it scales, it stays small, and the labels stay
selectable.

⌗ ONE SOURCE, so the page cannot drift from the PDF.  The drawing on the page is compiled
from the same `tikzpicture` the paper typesets, not a hand-made copy of it -- a hand-made
copy is a second source that agrees until someone edits one of them.

⌗ Idempotent: a drawing whose source has not changed is not recompiled.  The hash of the
`tikzpicture` body plus the preamble is kept beside the SVG.
"""
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
CORPUS = os.path.join(ROOT, 'corpus')
OUT = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'fig')

#: Packages that break a `standalone` document or cannot resolve outside the corpus
#: directory.  Everything ELSE in the paper's preamble is carried across.
#:
#: ⌗ r7207: this was first written as a WHITELIST of package names, and it dropped
#: `\usepackage{amsmath, amssymb, amsthm}` because that line names three packages in one
#: set of braces.  `\boldsymbol` was then undefined and the drawing failed to compile.
#: * A whitelist has to anticipate how the preamble is written; a blocklist only has to
#: name the handful of things that are known to break. *
DROP = re.compile(r'^\\(?:documentclass|usepackage(?:\[[^\]]*\])?\{(?:geometry|hyperref|'
                  r'receipts|ledgers|caption|fancyhdr|titlesec|natbib|biblatex)\}|'
                  r'(?:input|include)\b|bibliographystyle|pagestyle|geometry)', re.M)


#: Commands that belong to a dropped package and span several lines, so a line filter
#: cannot see where they end.  `\\hypersetup{...}` is the one that bit: hyperref is
#: dropped and its configuration block then sat there undefined.
BLOCKS = ('hypersetup', 'geometry', 'captionsetup', 'lstset')


def _strip_blocks(text):
    for name in BLOCKS:
        while True:
            i = text.find('\\' + name + '{')
            if i < 0:
                break
            j = text.index('{', i)
            depth = 0
            for k in range(j, len(text)):
                if text[k] == '{':
                    depth += 1
                elif text[k] == '}':
                    depth -= 1
                    if depth == 0:
                        break
            else:
                break
            text = text[:i] + text[k + 1:]
    return text


def preamble(src):
    head = _strip_blocks(src.split('\\begin{document}')[0])
    keep = [ln for ln in head.split('\n')
            if ln.strip() and not ln.lstrip().startswith('%')
            and not DROP.match(ln.strip())]
    return '\n'.join(keep)


def figures(src):
    """(label, tikz body) for each figure that has a tikzpicture and no includegraphics."""
    out = []
    for m in re.finditer(r'\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}', src, re.S):
        body = m.group(1)
        if '\\includegraphics' in body:
            continue
        tz = re.search(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', body, re.S)
        lb = re.search(r'\\label\{([^}]*)\}', body)
        if tz and lb:
            out.append((lb.group(1), tz.group(0)))
    return out


def slug(label):
    return 'tikz_' + re.sub(r'[^A-Za-z0-9]+', '_', label).strip('_')


def render(label, tikz, pre, force=False):
    name = slug(label)
    svg = os.path.join(OUT, name + '.svg')
    stamp = os.path.join(OUT, name + '.hash')
    h = hashlib.sha256((pre + tikz).encode('utf-8')).hexdigest()[:16]
    if not force and os.path.exists(svg) and os.path.exists(stamp) \
            and io.open(stamp).read().strip() == h:
        return 'cached'

    doc = ('\\documentclass[border=4pt]{standalone}\n' + pre
           + '\n\\begin{document}\n' + tikz + '\n\\end{document}\n')
    with tempfile.TemporaryDirectory() as d:
        tex = os.path.join(d, 'f.tex')
        io.open(tex, 'w', encoding='utf-8').write(doc)
        for _ in range(2):
            r = subprocess.run(['pdflatex', '-interaction=nonstopmode',
                                '-halt-on-error', '-output-directory', d, tex],
                               capture_output=True, text=True)
        pdf = os.path.join(d, 'f.pdf')
        if not os.path.exists(pdf):
            tail = '\n'.join(r.stdout.strip().split('\n')[-12:])
            return 'FAILED\n' + tail
        os.makedirs(OUT, exist_ok=True)
        c = subprocess.run(['pdftocairo', '-svg', pdf, svg], capture_output=True, text=True)
        if c.returncode != 0 or not os.path.exists(svg):
            return 'FAILED at pdftocairo: ' + c.stderr.strip()[:300]
    io.open(stamp, 'w').write(h + '\n')
    return 'rendered'


def main(argv):
    force = '--force' in argv
    only = [a for a in argv if not a.startswith('-')]
    if not shutil.which('pdflatex') or not shutil.which('pdftocairo'):
        print('  ⛔ pdflatex and pdftocairo are both required')
        return 1
    print()
    print('  TIKZ FIGURES -- a figure drawn in TikZ is still a figure')
    bad = n = 0
    for fn in sorted(os.listdir(CORPUS)):
        if not fn.endswith('.tex') or fn.startswith('appendix_'):
            continue
        if only and not any(o in fn for o in only):
            continue
        src = io.open(os.path.join(CORPUS, fn), encoding='utf-8').read()
        figs = figures(src)
        if not figs:
            continue
        pre = preamble(src)
        for label, tikz in figs:
            v = render(label, tikz, pre, force)
            n += 1
            if v.startswith('FAILED'):
                bad += 1
                print(f'    ⛔ {fn}  {label}\n       {v}')
            else:
                print(f'    {"·" if v == "cached" else "✓"} {fn}  {label} -> '
                      f'fig/{slug(label)}.svg  ({v})')
    print(f'\n  {n} tikz figure(s); {bad} failed.')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
