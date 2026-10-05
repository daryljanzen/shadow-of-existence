"""A4: C1's headline marker set at HEAD, by r7043's own rule (trace_citations.section_of / is_conclusion)."""
import glob, os, re, sys
ROOT = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
def section_of(lines, ln):
    sec = 'preamble'
    for i in range(min(ln, len(lines))):
        l = lines[i]
        if '\\begin{abstract}' in l: sec = 'abstract'
        elif '\\end{abstract}' in l: sec = 'after-abstract'
        m = re.search(r'\\(?:sub)*section\*?\{([^}]*)\}', l)
        if m: sec = m.group(1)
    return sec
def is_conclusion(sec):
    return bool(re.search(r'conclu|summary|verdict|outlook|closing', sec, re.I))
out = []
for p in sorted(glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))):
    f = os.path.basename(p)
    if f.startswith('appendix_receipts'): continue
    lines = open(p, encoding='utf-8', errors='replace').read().split('\n')
    for ln, l in enumerate(lines):
        for m in re.finditer(r'\\rcpt\{([^}]*)\}', l):
            sec = section_of(lines, ln + 1)
            if sec == 'abstract' or is_conclusion(sec):
                out.append((f, sec, m.group(1)))
for r in out: print('\t'.join(r))
print(len(out), 'headline markers;', len(set(r[2] for r in out)), 'receipts', file=sys.stderr)
