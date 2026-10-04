"""static.py -- r7163+70.1 (70) ⓵, the SOURCE half: every receipts/**/*.py classified by each convention its
source uses to reach a corpus paper, including the ones the trace cannot see (child processes, git show).
A receipt counts under every convention it uses.  Complements census.py (the trace half).

  python3 static.py
"""
import ast
import glob
import os
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
os.chdir(ROOT)
sys.path.insert(0, HERE)
import census as C  # noqa: E402

PAPERS = sorted(os.path.basename(f) for f in glob.glob('corpus/*.tex'))
TEXLIKE = tuple(os.path.basename(f) for f in glob.glob('corpus/*') if f.endswith(('.tex', '.tsv', '.txt')))
MODDIRS = ['corpus', 'scripts', 'computations', '.']


def reads_corpus(src):
    """does a source reach corpus papers: names one, globs corpus, or imports/loads reach_baseline"""
    return (any(p in src for p in PAPERS) or C.own_glob(src) or bool(C.RB_IMPORT.search(src))
            or bool(C.RB_PATH.search(src) and C.EXEC_LOAD.search(src)))


_mods = {}


def module_path(name, rdir):
    for d in [rdir] + MODDIRS:
        p = os.path.join(d, name.replace('.', '/') + '.py')
        if os.path.exists(p):
            return p
    return None


def imported(src):
    try:
        t = ast.parse(src)
    except SyntaxError:
        return []
    out = []
    for n in ast.walk(t):
        if isinstance(n, ast.Import):
            out += [a.name for a in n.names]
        elif isinstance(n, ast.ImportFrom) and n.module and n.level == 0:
            out.append(n.module)
    return out


def module_reads(p, depth=0, seen=None):
    """transitively, within the repo: does module p (or anything it imports) reach the papers?"""
    seen = seen or set()
    if p in seen or depth > 4:
        return False
    seen.add(p)
    if p not in _mods:
        _mods[p] = C.src_of(p)
    s = _mods[p]
    if reads_corpus(s):
        return True
    for m in imported(s):
        q = module_path(m, os.path.dirname(p))
        if q and module_reads(q, depth + 1, seen):
            return True
    return False


CHILD_SCRIPT = re.compile(r"""['"]([\w./-]+\.py)['"]""")


def main():
    conv = defaultdict(set)
    files = sorted(glob.glob('receipts/**/*.py', recursive=True))
    for f in files:
        s = C.src_of(f)
        rdir = os.path.dirname(f)
        if any(p in s for p in PAPERS):
            conv['NAME (a paper basename literally)'].add(f)
        if C.RB_IMPORT.search(s):
            conv['RB-IMPORT (import reach_baseline)'].add(f)
        if C.RB_PATH.search(s) and C.EXEC_LOAD.search(s):
            conv['RB-PATHLOAD (reach_baseline.py loaded by path)'].add(f)
        if C.own_glob(s):
            conv['GLOB/WALK (own glob/listdir/walk of corpus/)'].add(f)
        for m in imported(s):
            q = module_path(m, rdir)
            if not q or q == f or m == 'reach_baseline':
                continue
            if module_reads(q):
                key = ('RECEIPT-IMPORT (imports a receipt/sibling that reads)' if q.startswith('receipts/') or
                       os.path.dirname(q) == rdir else 'HELPER (imports a non-receipt module that reads)')
                conv[key].add(f)
                conv['  via ' + q].add(f)
        if re.search(r"git['\"],\s*['\"]show", s) or "'show'" in s:
            if re.search(r"""(HEAD|['"]):corpus/|['"]show['"],\s*f?['"][^'"]*:corpus/""", s):
                conv['GIT-SHOW (a committed corpus blob, not the working tree)'].add(f)
        if C.CHILD.search(s):
            for sc in CHILD_SCRIPT.findall(s):
                q = sc if os.path.exists(sc) else os.path.join(rdir, sc)
                if not os.path.exists(q):
                    q = next((os.path.join(d, sc) for d in MODDIRS if os.path.exists(os.path.join(d, sc))), None)
                if q and q != f and module_reads(q):
                    conv['CHILD-PROCESS (runs a python child that reads)'].add(f)
                    conv['  child ' + q].add(f)
                    break
        if re.search(r"""PAPER_OF|PAPERS\s*=\s*\{|\.tex['"]\s*%|f['"][^'"]*\{[^}]+\}\.tex""", s):
            conv['COMPUTED-NAME (a .tex path built from a variable)'].add(f)
    nonlit = set()
    for k, v in conv.items():
        if not k.startswith(('NAME', '  ', 'RB-IMPORT', 'GIT-SHOW')):
            nonlit |= v
    blind = {f for f in nonlit if not any(p in C.src_of(f) for p in PAPERS) and not C.RB_IMPORT.search(C.src_of(f))}
    print(f'  receipts/**/*.py: {len(files)}')
    print(f'  using any convention: {len(set().union(*[v for k, v in conv.items() if not k.startswith("  ")]))}\n')
    for k in sorted(conv, key=lambda k: (k.startswith('  '), -len(conv[k]))):
        if not k.startswith('  '):
            print(f'    {len(conv[k]):4d}  {k}')
    print('\n  the modules and children behind HELPER / RECEIPT-IMPORT / CHILD-PROCESS:')
    for k in sorted((k for k in conv if k.startswith('  ')), key=lambda k: -len(conv[k])):
        print(f'    {len(conv[k]):4d} {k}')
    print(f'\n  receipts with a non-literal convention: {len(nonlit)};  of them naming NO paper literally and not '
          f'importing reach_baseline (wholly invisible to the current name test): {len(blind)}')
    for f in sorted(blind):
        cs = [k.split(' (')[0] for k, v in conv.items() if f in v and not k.startswith('  ')]
        print(f'      {f}  [{", ".join(cs)}]')


if __name__ == '__main__':
    main()
