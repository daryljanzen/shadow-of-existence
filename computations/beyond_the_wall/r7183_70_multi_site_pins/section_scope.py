"""Would section scoping disambiguate the MULTI-SITE pins?  For each, the sections its occurrences fall in.
SECTION-UNIQUE: every occurrence in a different section, so a section-scoped pin names exactly one site.
SECTION-SHARED: two or more occurrences share a section, so only a neighbourhood (sentence/paragraph) separates them."""
import csv, re, sys, os
D = os.path.dirname(os.path.abspath(__file__))
ROOT = sys.argv[1] if len(sys.argv) > 1 else '.'
rows = [r for r in csv.DictReader(open(os.path.join(D, 'head.tsv')), delimiter='\t', quoting=csv.QUOTE_NONE)
        if int(r['occurrences']) >= 2]
cache = {}
def secs_of(paper, lit):
    if paper not in cache:
        raw = re.sub(r'(?<!\\)%[^\n]*', '', open(os.path.join(ROOT, paper if '/' in paper else 'corpus/' + paper)).read())
        cache[paper] = ' '.join(raw.split())
    t = cache[paper]; lit = ' '.join(lit.split()); out = []; pos = 0
    heads = [(m.start(), m.group(0)) for m in re.finditer(r'\\(?:sub)*section\*?\{[^}]*\}|\\begin\{abstract\}', t)]
    while True:
        j = t.find(lit, pos)
        if j < 0: return out
        h = [s for p, s in heads if p < j]
        out.append(h[-1] if h else 'preamble'); pos = j + len(lit)
res = {}
for r in rows:
    s = secs_of(r['paper'], r['literal'])
    v = 'SECTION-UNIQUE' if len(set(s)) == len(s) else 'SECTION-SHARED'
    res.setdefault((r['kind'], v), []).append(r)
for k in sorted(res): print(k[0], k[1], len(res[k]))
