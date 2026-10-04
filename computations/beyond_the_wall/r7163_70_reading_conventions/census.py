"""census.py -- r7163+70.1 (70) ⓵: every way a receipt in this tree reaches a corpus file's bytes, counted.

Ground truth is receipts/READ_INDEX.json (what each receipt OPENED under the trace).  For every traced
receipt whose blob still matches its traced sha, each (receipt, corpus file) read pair is classified by
the first convention its source explains it with (PREDICTION.md).  Edited / untraced receipts are
classified from source only and reported apart.

  python3 census.py            # summary + every non-NAME pair
"""
import fnmatch
import glob
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
os.chdir(ROOT)
D = json.load(open('receipts/READ_INDEX.json'))['receipts']
EXT = ('.tex', '.tsv', '.txt')
CORPUS = sorted(f for f in glob.glob('corpus/*') if f.endswith(EXT))
RB_IMPORT = re.compile(r'^\s*(?:import reach_baseline|from reach_baseline )', re.M)
RB_PATH = re.compile(r"reach_baseline\.py['\"]")
EXEC_LOAD = re.compile(r'spec_from_file_location|SourceFileLoader|exec\(|runpy\.|import_module')
GLOBWALK = re.compile(r"(glob\.glob|glob\(|iglob|os\.listdir|os\.walk|scandir|Path\([^)]*\)\.(?:glob|rglob|iterdir))")
CORPUS_REF = re.compile(r"""['"]corpus['"/]|corpus/""")
SUBPROC = re.compile(r"subprocess|os\.system|check_output|git['\"],\s*['\"]show")


def src_of(p):
    try:
        return open(p, encoding='utf-8', errors='replace').read()
    except OSError:
        return ''


def blob(p):
    return subprocess.run(['git', 'hash-object', p], capture_output=True, text=True).stdout.strip()


_mod_cache = {}


def module_explains(mod, base):
    """does an imported module's source name `base` or glob/walk corpus/?  (one level; recursion below)"""
    k = (mod, base)
    if k not in _mod_cache:
        s = src_of(mod)
        _mod_cache[k] = (base in s) or bool(GLOBWALK.search(s) and CORPUS_REF.search(s)) or \
            bool(RB_IMPORT.search(s))
    return _mod_cache[k]


def _cover(pats):
    out = set()
    for pat in pats:
        out |= set(f for f in CORPUS if fnmatch.fnmatchcase(f, pat) and (pat.count('/') == f.count('/')
                                                                         or '**' in pat))
    return out


def reads_of(e):
    """(CONTENT reads: r + d coverage, MEMBERSHIP-only: g coverage not also read).  receipt_scope's own
    semantics: a glob returns names, so only a content read is affected by a paper edit."""
    opened = set(f for f in e.get('r', []) if f.startswith('corpus/') and f.endswith(EXT))
    content = opened | _cover(e.get('d', []))
    return content, opened, _cover(e.get('g', [])) - content


def own_glob(src):
    """the receipt's OWN source globs / lists / walks corpus: a glob-ish call within 3 lines of a corpus ref"""
    L = src.splitlines()
    for i, ln in enumerate(L):
        if GLOBWALK.search(ln) and not ln.lstrip().startswith('#'):
            win = '\n'.join(L[max(0, i - 1):i + 3])
            if re.search(r"""['"]corpus['"/]|corpus/|\bCORPUS\b|\bPAPERS?_DIR\b""", win):
                return True
    return False


CHILD = re.compile(r"""subprocess\.(?:run|check_output|Popen|call)\(\s*\[\s*sys\.executable|['"]python3?['"]\s*,""")


def classify(rp, src, f, e, opened):
    base = os.path.basename(f)
    stem = base.rsplit('.', 1)[0]
    if base in src:
        return 'NAME'
    if RB_IMPORT.search(src):
        return 'RB-IMPORT'
    if RB_PATH.search(src) and EXEC_LOAD.search(src):
        return 'RB-PATHLOAD'
    if f not in opened and not any(o.endswith(os.path.splitext(f)[1]) for o in opened):
        # only a `d` superset covers f, and the receipt opened no corpus file of f's kind at all: the
        # directory it read whole was corpus/*.py (gates, generators), not the papers
        return 'D-SUPERSET'
    if own_glob(src):
        return 'GLOB/WALK'
    mods = [m for m in e.get('r', []) if m.endswith('.py') and m != rp and not m.startswith('scripts/sweep_runner')]
    for m in mods:
        if module_explains(m, base):
            return ('RECEIPT-IMPORT:' if m.startswith('receipts/') else 'HELPER:') + m
    if CHILD.search(src):
        return 'CHILD-PROCESS'
    if re.search(r'(?<![\w])' + re.escape(stem) + r'(?![\w.])', src):
        return 'STEM'
    return 'UNEXPLAINED'


def per_conv_all(pc):
    return set().union(*pc.values()) if pc else set()


def main():
    pairs = Counter()
    per_conv = defaultdict(set)
    rec_blind = defaultdict(set)
    clean = edited = 0
    readers = set()
    detail = []
    superset = Counter()
    for rp, e in sorted(D.items()):
        if not rp.startswith('receipts/') or not os.path.exists(rp):
            continue
        if not blob(rp).startswith(e.get('sha', '')):
            edited += 1
            continue
        clean += 1
        src = src_of(rp)
        allr, opened, memb = reads_of(e)
        for f in memb:
            pairs['(membership only)'] += 1
            per_conv['(membership only)'].add(rp)
        if not allr:
            continue
        readers.add(rp)
        for f in sorted(allr):
            c = classify(rp, src, f, e, opened)
            key = c.split(':')[0]
            if key == 'D-SUPERSET':
                superset[rp] += 1
                continue
            pairs[key] += 1
            per_conv[key].add(rp)
            if key not in ('NAME',):
                rec_blind[rp].add(c)
                detail.append((key, rp, f, c))
    readers = {rp for rp in readers if rp in per_conv_all(per_conv)}
    print(f'  d-SUPERSET artefacts (corpus/* read whole, but only corpus/*.py opened -- not paper readers): '
          f'{len(superset)} receipts, {sum(superset.values())} pairs: '
          f'{sorted(os.path.basename(r)[:40] for r in superset)}')
    tex_readers = {rp for rp in readers if any(f.endswith('.tex') for f in reads_of(D[rp])[0])}
    memb_pairs = pairs.pop('(membership only)', 0); memb_recs = per_conv.pop('(membership only)', set())
    print(f'  traced receipts present: {clean + edited};  blob unchanged since trace: {clean};  edited: {edited}')
    print(f'  clean receipts whose trace reads a corpus .tex/.tsv/.txt: {len(readers)}  (.tex: {len(tex_readers)})')
    print(f'  glob-MEMBERSHIP-only pairs (names listed, content not read; not a paper-edit dependency): '
          f'{memb_pairs} in {len(memb_recs)} receipts')
    tot = sum(pairs.values())
    print(f'\n  (receipt, corpus file) read pairs: {tot}')
    for k, n in pairs.most_common():
        print(f'    {k:<16} {n:6d} pairs  {100 * n / tot:5.1f} %   in {len(per_conv[k])} receipts')
    blind = {rp for rp, cs in rec_blind.items() if any(c.split(":")[0] not in ('NAME', 'RB-IMPORT') for c in cs)}
    print(f'\n  receipts by convention (a receipt counts under each convention it uses):')
    for k in pairs:
        print(f'    {k:<16} {len(per_conv[k]):4d} receipts')
    print(f'\n  receipts with >=1 pair the current gate cannot see (not NAME, not RB-IMPORT): {len(blind)}')
    hel = Counter(c.split(':', 1)[1] for k, rp, f, c in detail if ':' in c)
    print('\n  modules carrying HELPER / RECEIPT-IMPORT reads (pairs):')
    for m, n in hel.most_common():
        print(f'    {n:5d}  {m}')
    print('\n  per receipt, non-NAME conventions (excluding RB-IMPORT-only):')
    for rp in sorted(blind):
        cs = sorted(rec_blind[rp])
        print(f'    {rp}\n        {"; ".join(cs)}')
    # static-only: subprocess/git-show readers among all receipts
    allpy = glob.glob('receipts/**/*.py', recursive=True)
    st = Counter()
    for p in allpy:
        s = src_of(p)
        if not s:
            continue
        if re.search(r"git['\"],\s*['\"]show", s) and 'corpus' in s:
            st['GIT-SHOW of corpus (static)'] += 1
        if SUBPROC.search(s) and CORPUS_REF.search(s):
            st['subprocess + corpus ref (static)'] += 1
        if RB_IMPORT.search(s):
            st['RB-IMPORT (static, all .py)'] += 1
        if RB_PATH.search(s):
            st['reach_baseline.py by path (static)'] += 1
        if GLOBWALK.search(s) and CORPUS_REF.search(s):
            st['glob/walk + corpus ref (static)'] += 1
    print(f'\n  static, over all {len(allpy)} receipts/**/*.py:')
    for k, n in st.most_common():
        print(f'    {n:5d}  {k}')
    json.dump(dict(detail=detail, blind=sorted(blind)), open(os.path.join(HERE, 'census.json'), 'w'), indent=0)


if __name__ == '__main__':
    main()
