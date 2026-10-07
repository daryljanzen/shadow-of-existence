"""G2: raw LaTeX control sequences and escaped-entity residue in the published pages' TEXT (outside <script>/<math>
and outside math spans).  G3: display-math blocks on each page against display environments in its source."""
import glob, html, os, re, sys
from collections import Counter
sys.path.insert(0, 'corpus')
B = 'BOOK_INTRO_cosmiCave'
LEAK = re.compile(r'\\(ref|eqref|cite|emph|begin|end|label|textbf|textit|section|rcpt)\{|amp;')
leaks = Counter(); sample = {}
for f in sorted(glob.glob(f'{B}/paper_P*.html')):
    t = open(f, encoding='utf-8', errors='replace').read()
    t = re.sub(r'<script.*?</script>|<style.*?</style>|<math.*?</math>', '', t, flags=re.S)
    t = re.sub(r'<span class="(?:math|katex)[^"]*".*?</span>', '', t, flags=re.S)
    text = re.sub(r'<[^>]+>', ' ', t)
    hits = [m.group(0) for m in LEAK.finditer(text)]
    if hits:
        leaks[os.path.basename(f)] = len(hits)
        m = LEAK.search(text); sample[os.path.basename(f)] = ' '.join(text[max(0, m.start()-60):m.end()+40].split())
print('G2 leaked control sequences / entity residue in page text:', sum(leaks.values()), 'in', len(leaks), 'page(s)')
for k, v in leaks.most_common(): print(f'   {k}: {v}   e.g. ...{sample[k][:130]}...')

# ---------------------------------------------------------------- G3
import importlib.util as u
spec = u.spec_from_file_location('_gph', 'scripts/gen_paper_html.py'); mod = u.module_from_spec(spec); spec.loader.exec_module(mod)
papers = {k: v[0] for k, v in mod.PAPERS.items()}
ENV = re.compile(r'\\begin\{(equation|align|gather|multline|eqnarray|displaymath)\*?\}|\\\[|\$\$')
short = []
for pid, stem in sorted(papers.items(), key=lambda kv: int(kv[0][1:])):
    sp, pp = f'corpus/{stem}.tex', f'{B}/paper_{pid}.html'
    if not (os.path.exists(sp) and os.path.exists(pp)): continue
    s = re.sub(r'(?<!\\)%[^\n]*', '', open(sp, encoding='utf-8').read())
    s = s.split('\\begin{document}', 1)[-1]
    n_src = len(ENV.findall(s)) - s.count('$$') // 2   # $$...$$ counted once, not twice
    pg = open(pp, encoding='utf-8').read()
    n_pg = len(re.findall(r'class="eq(?:wrap)?"', pg))
    n_pg_eq = len(re.findall(r'class="eq"', pg)); n_pg_wrap = len(re.findall(r'class="eqwrap"', pg))
    flag = n_pg_eq + 0 < n_src and max(n_pg_eq, n_pg_wrap) < n_src
    if flag: short.append(pid)
    print(f'G3 {pid:4} source display envs {n_src:4}   page .eq {n_pg_eq:4}  .eqwrap {n_pg_wrap:4}' + ('   <- page carries fewer' if flag else ''))
print('G3 papers whose page carries fewer display blocks than the source:', short)
