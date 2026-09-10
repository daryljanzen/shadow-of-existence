#!/usr/bin/env python3
"""
gen_paper_html.py -- one paper's .tex -> a readable HTML chapter.

** WHAT THIS IS AND IS NOT. **  It is not a general LaTeX engine and does not try
to be.  It handles the environments this corpus actually uses, measured rather
than assumed: sections, theorem-like blocks, proofs, display equations, figures,
lists, and the two marker rails.  Anything it does not recognise is KEPT AS TEXT
rather than dropped -- the same rule the abstract converter runs on, and for the
same reason: a dropped macro silently changes the mathematics, a kept one is
visibly odd and gets fixed.

** THE NUMBERS COME FROM THE SAME PLACE THE PDF'S DO. **  Receipt and ledger
markers render `P3R7` and `L2` by reading the generated appendices, so a reader
moving between the PDF, this page and the web index sees one number for one
thing.  Nothing here assigns a number.

Usage:  python3 scripts/gen_paper_html.py P3
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave')
CDN = 'https://cdn.jsdelivr.net/gh/daryljanzen/shadow-of-existence@main'

# paper -> (tex stem, receipt appendix, ledger appendix)
PAPERS = {
    'P1': ('BH_causality_v2', 'P01', 'P1'), 'P2': ('janzen_circle_v3', 'P02', 'P2'),
    'P3': ('SdS-slicing-curve_v2', 'P03', 'P3'), 'P4': ('modern_parallax', 'P04', 'P4'),
    'P5': ('groupoid_paper', 'P05', 'P5'), 'P6': ('shadow_of_existence', 'P06', 'P6'),
    'P7': ('CR_framework', 'P07', 'P7'), 'P8': ('slicing_operator', 'P08', 'P8'),
    'P9': ('range_paper', 'P09', 'P9'), 'P10': ('canonical_time', 'P10', 'P10'),
    'P11': ('dynamics_paper', 'P11', 'P11'), 'P12': ('algebroid_paper', 'P12', 'P12'),
    'P13': ('boundary_paper', 'P13', 'P13'), 'P14': ('matter_sector_paper', 'P14', 'P14'),
    'P15': ('CR_cosmology', 'P15', 'P15'), 'P16': ('cosmogenesis_paper', 'P16', 'P16'),
    'P17': ('geometric_core_paper', 'P17', 'P17'), 'P18': ('CR_synthesis', None, 'SYN'),
}

THEOREMISH = ('theorem', 'proposition', 'lemma', 'corollary', 'definition',
              'remark', 'conjecture', 'example')

# The math converter is the live edition's, imported rather than copied: two
# converters gave two answers for one formula at r4597 and that must not recur.
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import importlib.util as _u
_sp = _u.spec_from_file_location('_gle', os.path.join(ROOT, 'scripts',
                                                      'gen_live_edition.py'))
_gle = _u.module_from_spec(_sp)
_sp.loader.exec_module(_gle)
mathspan = _gle.mathspan


def marker_numbers(paper):
    """key -> printed number, read from the GENERATED appendices, so the page
    cannot disagree with the PDF about what P3R7 is."""
    stem, rcpt_scope, ldg_scope = PAPERS[paper]
    nums = {}
    if rcpt_scope:
        fp = os.path.join(ROOT, 'corpus', f'appendix_receipts_{rcpt_scope}.tex')
        if os.path.exists(fp):
            nums.update(dict(re.findall(r'\\rcptlabel\{([^}]*)\}\{([^}]*)\}',
                                        open(fp, encoding='utf-8').read())))
    fp = os.path.join(ROOT, 'corpus', f'appendix_ledgers_{ldg_scope}.tex')
    if os.path.exists(fp):
        nums.update(dict(re.findall(r'\\ldglabel\{([^}]*)\}\{([^}]*)\}',
                                    open(fp, encoding='utf-8').read())))
    return nums


def inline(t, nums, labels):
    """Inline markup -> HTML.  Math first, so a formula is never split by a
    later rule operating on its innards."""
    t = re.sub(r'(?m)(?<!\\)%.*$', '', t)
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    t = re.sub(r'\$\\?([a-zA-Z]+)\$',
               lambda m: '<span class="m">' + mathspan('\\' + m.group(1))
               + '</span>', t)
    # A display equation can sit INSIDE a theorem or a proof, and those blocks
    # are handed here whole.  Without this, thirteen of P3's twenty-eight
    # equations reached the page as raw \begin{equation}.
    t = re.sub(r'\\begin\{(equation|align|gather)\*?\}(.*?)\\end\{\1\*?\}',
               lambda m: '<div class="eq">' +
               mathspan(re.sub(r'\\label\{[^}]*\}', '', m.group(2))) + '</div>',
               t, flags=re.S)
    t = re.sub(r'\$\$(.+?)\$\$|\\\[(.+?)\\\]',
               lambda m: '<div class="eq">' +
               mathspan(m.group(1) or m.group(2)) + '</div>', t, flags=re.S)
    t = re.sub(r'\\paragraph\*?\{([^{}]*)\}', r'<b class="para">\1</b> ', t)
    t = re.sub(r'\\begin\{(itemize|enumerate)\}(.*?)\\end\{\1\}',
               lambda m: ('<ul>' + ''.join(
                   '<li>' + x.strip() + '</li>' for x in
                   re.split(r'\\item\s*', m.group(2)) if x.strip()) + '</ul>'),
               t, flags=re.S)
    t = re.sub(r'\$([^$]+)\$',
               lambda m: '<span class="m">' + mathspan(m.group(1)) + '</span>', t)
    t = re.sub(r'\\rcpt\{([^}]*)\}',
               lambda m: '<sup class="mk r" title="' + m.group(1) + '">'
               + nums.get(m.group(1), 'R') + '</sup>', t)
    t = re.sub(r'\\ldg\{([^}]*)\}',
               lambda m: '<sup class="mk l" title="' + m.group(1) + '">'
               + nums.get(m.group(1), 'L') + '</sup>', t)
    # These run AFTER the reference and citation rules, so their argument may
    # already contain a tag with braces of its own -- a single-level pattern
    # left six emphases and three citations sitting raw on the page.  Repeated
    # so an inner wrapper is unwound before the outer one is tried.
    for _ in range(4):
        t2 = re.sub(r'\\(?:emph|textit)\{([^{}]*)\}', r'<em>\1</em>', t)
        t2 = re.sub(r'\\(?:textbf|strong)\{([^{}]*)\}', r'<strong>\1</strong>', t2)
        if t2 == t:
            break
        t = t2
    # Anything still wrapped has a tag inside it: take the widest span that
    # ends before the next macro, rather than leaving the macro visible.
    t = re.sub(r'\\(?:emph|textit)\{([^\\]*?)\}', r'<em>\1</em>', t)
    t = re.sub(r'\\(?:textbf|strong)\{([^\\]*?)\}', r'<strong>\1</strong>', t)
    t = re.sub(r'\\texttt\{([^{}]*)\}', r'<code>\1</code>', t)
    t = re.sub(r'\\footnote\{([^{}]*)\}', r' <span class="fn">(\1)</span>', t)
    t = re.sub(r'\\paragraph\*?\{([^{}]*)\}', r'<b class="para">\1</b> ', t)
    t = re.sub(r'\\(?:eqref|ref)\{([^}]*)\}',
               lambda m: '<a class="xr" href="#' + m.group(1) + '">'
               + labels.get(m.group(1), '\u00a7') + '</a>', t)
    t = re.sub(r'\\cite[tp]?\[([^\]]*)\]\{([^}]*)\}',
               lambda m: '<span class="cite">[' + m.group(2) + ', '
               + m.group(1) + ']</span>', t)
    t = re.sub(r'\\cite[tp]?\{([^}]*)\}',
               lambda m: '<span class="cite">[' +
               ', '.join(x.strip() for x in m.group(1).split(',')) + ']</span>', t)
    t = re.sub(r'\\(?:label|index|vspace|hspace|noindent|clearpage|newpage)'
               r'\*?\{?[^}\n]*\}?', '', t)
    # Last sweep: anything still carrying a macro name has braces a pattern
    # could not pair.  Unwrap it rather than print it -- a reader must never
    # meet a backslash, and the argument is the content.
    t = re.sub(r'\\(?:emph|textit|textbf|strong|texttt|footnote)\s*\{', '', t)
    t = re.sub(r'\\cite[tp]?\s*\{([^}]*)\}?',
               lambda m: '<span class="cite">[' + m.group(1) + ']</span>', t)
    t = re.sub(r'\\(?:maketitle|tableofcontents|bigskip|medskip|smallskip)\b', '', t)
    t = re.sub(r'\\(sin|cos|tan|log|ln|exp|sinh|cosh|tanh)\b', r'\1', t)
    t = t.replace('---', '\u2014').replace('--', '\u2013').replace('~', ' ')
    t = t.replace("``", '\u201c').replace("''", '\u201d')
    return re.sub(r'[ \t]+', ' ', t)


def convert(paper):
    stem, _r, _l = PAPERS[paper]
    src = os.path.join(ROOT, 'corpus', stem + '.tex')
    s = open(src, encoding='utf-8', errors='replace').read()
    i = s.find(r'\begin{document}')
    body = s[i + len(r'\begin{document}'):]
    body = body.split(r'\end{document}')[0]
    body = re.sub(r'\\(?:ldg|rcpt)appendix\{[^}]*\}|\\input\{[^}]*\}', '', body)
    body = re.sub(r'\\begin\{thebibliography\}.*?\\end\{thebibliography\}', '',
                  body, flags=re.S)

    nums = marker_numbers(paper)

    # Pass one: number the theorem-like blocks and the equations, so a cross
    # reference can resolve to what the reader will actually see.
    labels, counts = {}, {}
    for m in re.finditer(r'\\begin\{(' + '|'.join(THEOREMISH) +
                         r')\}(?:\[[^\]]*\])?\s*\\label\{([^}]*)\}', body):
        kind = m.group(1)
        counts[kind] = counts.get(kind, 0) + 1
        labels[m.group(2)] = f'{kind.capitalize()} {counts[kind]}'
    eqn = 0
    for m in re.finditer(r'\\begin\{equation\}(.*?)\\end\{equation\}', body, re.S):
        eqn += 1
        lb = re.search(r'\\label\{([^}]*)\}', m.group(1))
        if lb:
            labels[lb.group(1)] = f'({eqn})'
    secn = 0
    for m in re.finditer(r'\\section\{[^}]*\}\s*\\label\{([^}]*)\}', body):
        secn += 1
        labels[m.group(1)] = f'\u00a7{secn}'

    out, eqn, counts = [], 0, {}

    def flush(buf):
        txt = ' '.join(buf).strip()
        if txt:
            out.append('<p>' + inline(txt, nums, labels) + '</p>')
        buf.clear()

    buf, i = [], 0
    lines = body.split('\n')
    while i < len(lines):
        ln = lines[i]
        st = ln.strip()

        m = re.match(r'\\(sub)?(sub)?section\*?\{(.*)\}', st)
        if m:
            flush(buf)
            lvl = 2 + (1 if m.group(1) else 0) + (1 if m.group(2) else 0)
            aid = ''
            nx = lines[i + 1] if i + 1 < len(lines) else ''
            lb = re.search(r'\\label\{([^}]*)\}', ln + nx)
            if lb:
                aid = f' id="{lb.group(1)}"'
            out.append(f'<h{lvl}{aid}>' + inline(m.group(3), nums, labels)
                       + f'</h{lvl}>')
            i += 1
            continue

        m = re.match(r'\\begin\{(' + '|'.join(THEOREMISH) + r')\}(\[[^\]]*\])?', st)
        if m:
            flush(buf)
            kind = m.group(1)
            counts[kind] = counts.get(kind, 0) + 1
            note = (' \u2014 ' + m.group(2)[1:-1]) if m.group(2) else ''
            blk, i = [], i + 1
            while i < len(lines) and rf'\end{{{kind}}}' not in lines[i]:
                blk.append(lines[i])
                i += 1
            i += 1
            txt = '\n'.join(blk)
            lb = re.search(r'\\label\{([^}]*)\}', txt)
            aid = f' id="{lb.group(1)}"' if lb else ''
            out.append(f'<div class="thm {kind}"{aid}>'
                       f'<span class="thmhead">{kind.capitalize()} '
                       f'{counts[kind]}{note}.</span> '
                       + inline(txt, nums, labels) + '</div>')
            continue

        if st.startswith(r'\begin{proof}'):
            flush(buf)
            blk, i = [], i + 1
            while i < len(lines) and r'\end{proof}' not in lines[i]:
                blk.append(lines[i])
                i += 1
            i += 1
            out.append('<div class="proof"><span class="thmhead">Proof.</span> '
                       + inline('\n'.join(blk), nums, labels)
                       + ' <span class="qed">\u25a1</span></div>')
            continue

        if st.startswith(r'\begin{equation}'):
            flush(buf)
            blk, i = [], i + 1
            while i < len(lines) and r'\end{equation}' not in lines[i]:
                blk.append(lines[i])
                i += 1
            i += 1
            eqn += 1
            txt = '\n'.join(blk)
            lb = re.search(r'\\label\{([^}]*)\}', txt)
            aid = f' id="{lb.group(1)}"' if lb else ''
            txt = re.sub(r'\\label\{[^}]*\}', '', txt)
            out.append(f'<div class="eqwrap"{aid}><div class="eq">'
                       + mathspan(txt) + f'</div><span class="eqno">({eqn})</span></div>')
            continue

        if st.startswith(r'\begin{figure}'):
            flush(buf)
            blk, i = [], i + 1
            while i < len(lines) and r'\end{figure}' not in lines[i]:
                blk.append(lines[i])
                i += 1
            i += 1
            txt = '\n'.join(blk)
            g = re.search(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}', txt)
            cap = re.search(r'\\caption\{(.*)\}', txt, re.S)
            lb = re.search(r'\\label\{([^}]*)\}', txt)
            aid = f' id="{lb.group(1)}"' if lb else ''
            src_f = g.group(1) if g else ''
            # A PDF figure cannot be an <img>; it is linked rather than shown,
            # and said so rather than rendered as a broken image.
            if src_f.lower().endswith('.pdf'):
                media = (f'<p class="figalt"><a href="{CDN}/corpus/{src_f}">'
                         'Open this figure (PDF)</a></p>')
            elif src_f:
                media = f'<img src="{CDN}/corpus/{src_f}" alt="">'
            else:
                media = ''
            out.append(f'<figure{aid}>{media}'
                       + (f'<figcaption>{inline(cap.group(1), nums, labels)}'
                          '</figcaption>' if cap else '') + '</figure>')
            continue

        if st.startswith(r'\begin{itemize}') or st.startswith(r'\begin{enumerate}'):
            flush(buf)
            tag = 'ul' if 'itemize' in st else 'ol'
            end = r'\end{itemize}' if tag == 'ul' else r'\end{enumerate}'
            blk, i = [], i + 1
            while i < len(lines) and end not in lines[i]:
                blk.append(lines[i])
                i += 1
            i += 1
            items = [x.strip() for x in
                     re.split(r'\\item\s*', '\n'.join(blk)) if x.strip()]
            out.append(f'<{tag}>' + ''.join(
                '<li>' + inline(x, nums, labels) + '</li>' for x in items)
                + f'</{tag}>')
            continue

        if st.startswith(r'\begin{abstract}'):
            flush(buf)
            blk, i = [], i + 1
            while i < len(lines) and r'\end{abstract}' not in lines[i]:
                blk.append(lines[i])
                i += 1
            i += 1
            paras = [x for x in re.split(r'\n\s*\n', '\n'.join(blk)) if x.strip()]
            out.append('<div class="abstract"><h2>Abstract</h2>' + ''.join(
                '<p>' + inline(x, nums, labels) + '</p>' for x in paras) + '</div>')
            continue

        if not st:
            flush(buf)
        elif st.startswith('%'):
            pass
        else:
            buf.append(ln)
        i += 1
    flush(buf)
    return '\n'.join(out), labels, nums


def main():
    paper = sys.argv[1] if len(sys.argv) > 1 else 'P3'
    if paper not in PAPERS:
        raise SystemExit(f'unknown paper {paper}')
    stem = PAPERS[paper][0]
    html_body, labels, nums = convert(paper)

    src = open(os.path.join(ROOT, 'corpus', stem + '.tex'),
               encoding='utf-8', errors='replace').read()
    m = re.search(r'\\title\{(.+?)\}\s*\n\s*\\author', src, re.S)
    title = _gle.title_of(stem) or paper
    head, _, sub = title.partition(':')

    base = open(os.path.join(OUT_DIR, 'live_edition.html'),
                encoding='utf-8').read()
    css = re.search(r'<style>(.*?)</style>', base, re.S).group(1)
    extra = """
  .paper {{ max-width:46rem; }}
  .paper p {{ margin:0 0 1rem; }}
  .paper h2 {{ font-size:1.25rem; margin:2.4rem 0 .7rem; }}
  .paper h3 {{ font-size:1.06rem; margin:1.8rem 0 .5rem; }}
  .abstract {{ background:#f4f7fa; border-left:3px solid var(--line);
               padding:1rem 1.2rem; margin:1.5rem 0 2rem; font-size:.95rem; }}
  .abstract h2 {{ font-size:.8rem; letter-spacing:.09em; text-transform:uppercase;
                  margin:0 0 .6rem; color:var(--faint); }}
  .thm {{ margin:1.2rem 0; padding:.1rem 0 .1rem 1rem;
          border-left:2px solid var(--line); }}
  .thmhead {{ font-weight:600; }}
  .thm.remark {{ border-left-style:dotted; }}
  .proof {{ margin:1rem 0 1.4rem; font-size:.96rem; color:#3b4753; }}
  .qed {{ float:right; color:var(--faint); }}
  .eqwrap {{ display:flex; align-items:center; gap:1rem; margin:1.1rem 0; }}
  .eq {{ flex:1 1 auto; text-align:center; font-style:italic; }}
  .eqno {{ flex:0 0 auto; color:var(--faint); font-size:.85rem; }}
  figure {{ margin:1.6rem 0; text-align:center; }}
  figure img {{ max-width:100%; border:1px solid var(--line); }}
  figcaption {{ color:var(--faint); font-size:.86rem; margin-top:.5rem;
                text-align:left; line-height:1.5; }}
  .figalt a {{ font-size:.9rem; }}
  sup.mk {{ font-size:.62rem; font-family:'Iowan Old Style',Georgia,serif;
            letter-spacing:.02em; padding-left:.1em; }}
  sup.mk.r {{ color:var(--pole); }}
  sup.mk.l {{ color:#4a7a8c; }}
  .cite {{ color:var(--faint); font-size:.9em; }}
  .xr {{ text-decoration:none; }}
  .fn {{ color:var(--faint); font-size:.9em; }}
""".replace('{{', '{').replace('}}', '}')

    page = (f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1">'
            f'\n<title>{head} \u2014 The Shadow of Existence</title>\n<style>'
            + css + extra + '</style>\n</head>\n<body>\n<div class="wrap paper">\n'
            '<p class="note"><a href="./live_edition.html">\u2190 The Shadow of '
            f'Existence</a></p>\n<p class="pn">{paper}</p>\n<h1>{head}</h1>\n'
            + (f'<p class="lede">{sub.strip()}</p>\n' if sub.strip() else '')
            + f'<p class="note"><a href="{CDN}/corpus/{stem}.pdf">'
            'Open the typeset PDF</a></p>\n'
            + html_body +
            '\n<footer>Generated from the paper\u2019s own source. '
            '<a href="https://github.com/daryljanzen/shadow-of-existence">'
            'Source.</a></footer>\n</div>\n</body>\n</html>\n')

    out = os.path.join(OUT_DIR, f'paper_{paper}.html')
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write(page)
    print(f'  paper_{paper}.html: {len(page)} bytes, {len(labels)} labels, '
          f'{len(nums)} markers resolvable.')


if __name__ == '__main__':
    main()
