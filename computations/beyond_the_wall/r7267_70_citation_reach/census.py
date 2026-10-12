#!/usr/bin/env python3
"""r7267+70.1: the citation-reach census.  PROSE: every \\rcpt{X} in a non-appendix paper, the claim being its sentence.
APPENDIX: every receipts/INDEX.md row, the claim being its `claim (one line)` cell.  Two proxies, as pre-registered:
SCOPE (a universal operator whose governed noun the receipt's source never names) and NUMBER (a decimal figure the
receipt's source never contains).  Writes census.tsv (every site, its flags) and prints the counts and the seeds."""
import ast, glob, json, os, random, re, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_quote_pins as Q
HERE = os.path.dirname(os.path.abspath(__file__))
FILES = {os.path.basename(p)[:-3]: p for p in glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'), recursive=True)}
SCOPE = re.compile(r"\b(every|all|any|each|whole|entire|general|generic|always|never|uniquely|only|for all|at every)\s+"
                   r"((?:the|a|an|its|their|of|such|other|single|possible|one|two|three|those|these)\s+){0,3}"
                   r"([A-Za-z][A-Za-z\-]{2,})", re.I)
NUM = re.compile(r'(?<![\w.])(\d+\.\d{2,}|\d{2,}\.\d+)(?![\w.])')
STOP = {'the', 'and', 'that', 'this', 'which', 'with', 'from', 'than', 'such', 'other', 'case', 'cases', 'time', 'way',
        'ways', 'part', 'parts', 'one', 'ones', 'thing', 'things', 'point', 'points'}
_SRC = {}
_AT = {}          # receipt name -> source text to use instead of the working tree's (for a seed read at its own commit)

def reach(src):
    """REVISED after the S+1 seed failed (results.md): what a receipt's CHECKS can reach, read by PARSING, as 66 read
    I55 -- every string literal that is not a docstring, and every identifier and attribute name.  Comments and
    docstrings are excluded: they describe the receipt, they are not what it tests."""
    try:
        t = ast.parse(src)
    except SyntaxError:
        return src.lower()
    doc = set()
    for n in ast.walk(t):
        if isinstance(n, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and n.body \
                and isinstance(n.body[0], ast.Expr) and isinstance(getattr(n.body[0], 'value', None), ast.Constant) \
                and isinstance(n.body[0].value.value, str):
            doc.add(id(n.body[0].value))
    parts = []
    for n in ast.walk(t):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in doc:
            parts.append(n.value)
        elif isinstance(n, ast.Name):
            parts.append(n.id)
        elif isinstance(n, ast.Attribute):
            parts.append(n.attr)
    return ' '.join(parts).lower()

def src_text(name):
    """(the parsed reach, lower-cased; the raw source) of the receipt"""
    key = (name, name in _AT)
    if key not in _SRC:
        s = _AT.get(name) or open(FILES[name], encoding='utf-8', errors='replace').read()
        _SRC[key] = (reach(s), s)
    return _SRC[key]

def stem(w):
    w = w.lower()
    for suf in ('ations', 'ation', 'ings', 'ing', 'ies', 'es', 's'):
        if w.endswith(suf) and len(w) - len(suf) >= 4:
            return w[:-len(suf)]
    return w

def scope_flags(claim, name):
    low, _ = src_text(name)
    out = []
    for m in SCOPE.finditer(claim):
        noun = m.group(3)
        if noun.lower() in STOP:
            continue
        if stem(noun) not in low:
            out.append(f'{m.group(1).lower()} … {noun}')
    return out

def number_flags(claim, name):
    _, raw = src_text(name)
    return [n for n in NUM.findall(claim) if n not in raw and n.rstrip('0') not in raw]

def sentence(text, i):
    a = max(text.rfind('. ', 0, i), text.rfind('\n\n', 0, i)) + 1
    b = text.find('. ', i)
    return text[a:b + 1 if b >= 0 else len(text)]

def prose(texts=None):
    rows = []
    texts = texts or {os.path.basename(t): open(t, encoding='utf-8', errors='replace').read()
                      for t in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
                      if not os.path.basename(t).startswith('appendix')}
    for paper, t in sorted(texts.items()):
        flat = Q._flat(t)
        for m in re.finditer(r'\\rcpt\{([^}]+)\}', flat):
            name = m.group(1).split(',')[0].strip()
            if name not in FILES:
                rows.append(('PROSE', paper, name, None, [], [])); continue
            claim = Q._unmark(re.sub(r'\\(?:rcpt|ldg)\{[^}]*\}', ' ', sentence(flat, m.start())))
            rows.append(('PROSE', paper, name, claim, scope_flags(claim, name), number_flags(claim, name)))
    return rows

def appendix(index_text=None):
    rows = []
    text = index_text or open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8', errors='replace').read()
    for ln in text.split('\n'):
        c = [x.strip() for x in re.split(r'(?<!\\)\|', ln)]
        if len(c) < 6 or not c[4].startswith('`'):
            continue
        name = os.path.basename(c[4].strip('`'))[:-3]
        if name not in FILES:
            continue
        claim = c[3]
        rows.append(('APPENDIX', c[1], name, claim, scope_flags(claim, name), number_flags(claim, name)))
    return rows

def git(*a):
    return subprocess.run(['git', '-C', ROOT, *a], capture_output=True, text=True, errors='replace').stdout

if __name__ == '__main__':
    P, A = prose(), appendix()
    with open(os.path.join(HERE, 'census.tsv'), 'w', encoding='utf-8') as f:
        f.write('# population\tpaper\treceipt\tSCOPE flags\tNUMBER flags\tclaim\n')
        for pop, paper, name, claim, s, n in P + A:
            f.write('\t'.join([pop, paper, name, '; '.join(s), ' '.join(n), (claim or '')[:400]]) + '\n')
    for lab, rows in (('PROSE', P), ('APPENDIX', A)):
        k = len(rows); s = sum(bool(r[4]) for r in rows); n = sum(bool(r[5]) for r in rows)
        print(f'{lab}: {k} sites; SCOPE-flagged {s} ({100*s/k:.1f}%); NUMBER-flagged {n} ({100*n/k:.1f}%); '
              f'either {sum(bool(r[4] or r[5]) for r in rows)}')
    # seeds
    i55 = 'I55_the_atiyah_sequence_is_exact_and_a_characteristic_class_is_not_available'
    pre = git('log', '-1', '--format=%H', '-S', 'over that orbit', '--', 'corpus/algebroid_paper.tex').strip()
    old = git('show', f'{pre}^:corpus/algebroid_paper.tex')
    _AT[i55] = git('show', f'{pre}^:' + os.path.relpath(FILES[i55], ROOT))
    s1 = [r for r in prose({'algebroid_paper.tex': old}) if r[2] == i55]
    del _AT[i55]
    print('S+1 I55, sentence before the repair, SCOPE flags:', [r[4] for r in s1])
    pre2 = git('log', '-1', '--format=%H', '-S', 'in its OWN endpoint', '--', 'receipts/INDEX.md').strip()
    _AT['P15_damping_ratio_clean'] = git('show', f'{pre2}^:' + os.path.relpath(FILES['P15_damping_ratio_clean'], ROOT))
    s2 = [r for r in appendix(git('show', f'{pre2}^:receipts/INDEX.md')) if r[2] == 'P15_damping_ratio_clean']
    del _AT['P15_damping_ratio_clean']
    print('S+2 P15R22, INDEX row before the repair, NUMBER flags:', [r[5] for r in s2])
    idx = open(os.path.join(ROOT, 'receipts', 'INDEX.md'), encoding='utf-8').read()
    for name in (i55, 'P15_damping_ratio_clean'):
        row = next(ln for ln in idx.split('\n') if name in ln)
        computes = [x.strip() for x in re.split(r'(?<!\\)\|', row)][6]
        print(f'S- {name[:30]}: its own `what it computes` as the claim -> SCOPE {scope_flags(computes, name)} '
              f'NUMBER {number_flags(computes, name)}')
