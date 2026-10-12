#!/usr/bin/env python3
"""r7265+70.1 ②: N' = N plus deleting references (`~?\\cite{..}` and kin), measured as r7261 measured N."""
import glob, json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_quote_pins as Q
REF = re.compile(r'~?\\(?:cite|citep|citet|ref|eqref|S|rcpt|ldg)\b(?:\{[^}]*\})?')
def N2(t):
    return Q._flat(Q._unmark(REF.sub(' ', t))).strip()
base = Q.read_baseline()
held = [(k, v) for k, v in base.items() if v[3] == Q.MEANING_HELD]

def papers_at(sha):
    names = [n for n in Q._git('ls-tree', '--name-only', sha, 'corpus/').stdout.split()
             if n.endswith('.tex') and not os.path.basename(n).startswith('appendix_receipts')]
    return [Q._flat(Q._git('show', f'{sha}:{n}').stdout) for n in names]

# C-a: held PAPER rows whose H3 verdict changes under N'
ca, cache = [], {}
for (rc, lit), (t, tier, fl, v, why) in held:
    if t != 'PAPER':
        continue
    sha = Q._git('rev-parse', Q._HELD_AT.search(why).group(1)).stdout.strip()
    if sha not in cache:
        ps = papers_at(sha)
        cache[sha] = (ps, [N2(p) for p in ps])
    now = Q._present_at(sha, lit, t, rc)
    new = now or any(N2(lit) in x for x in cache[sha][1])
    if new != now:
        ca.append((rc, lit))
print('C-a held rows whose verdict changes under Nprime:', len(ca))

# C-b / C-c: PAPER keys gaining a match location under N' that N lacks (current papers)
tex = [Q._flat(open(p, encoding='utf-8', errors='replace').read()) for p in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
       if not os.path.basename(p).startswith('appendix_receipts')]
nt = [Q._unmark(x) for x in tex]
n2 = [N2(x) for x in tex]
gain = []
for (rc, lit), (t, *_r) in base.items():
    if t != 'PAPER':
        continue
    a = sum(x.count(Q._unmark(lit)) for x in nt) if Q._unmark(lit) else 0
    b = sum(x.count(N2(lit)) for x in n2) if N2(lit) else 0
    if b > a:
        gain.append((rc, lit, a, b))
print('C-b PAPER keys gaining a location under Nprime:', len(gain))
for rc, lit, a, b in gain:
    l2 = N2(lit)
    ctx = [x[max(0, m.start() - 70):m.end() + 50] for x in n2 for m in re.finditer(re.escape(l2), x)]
    print('GAIN', rc.split('/')[-1][:45], json.dumps(lit, ensure_ascii=False)[:70], f'N {a} -> Nprime {b}')
    for c in ctx[:4]:
        print('     ...', c)

# C-d: the burden recounted with references as non-markup
MARK = re.compile(r'\$|\\[A-Za-z]+')
burden = burden2 = 0
for (rc, lit), (t, tier, fl, v, why) in held:
    if t != 'PAPER':
        continue
    sha = Q._git('rev-parse', Q._HELD_AT.search(why).group(1)).stdout.strip()
    for p in cache[sha][0]:
        i = p.find(lit)
        if i < 0:
            continue
        a_ = max(p.rfind('. ', 0, i), p.rfind('\n\n', 0, i)) + 1
        b_ = p.find('. ', i + len(lit))
        rest = p[a_:b_ if b_ >= 0 else len(p)].replace(lit, ' ')
        burden += bool(MARK.search(rest))
        burden2 += bool(MARK.search(REF.sub(' ', rest)))
        break
print(f'C-d burden: {burden} as registered at r7261; {burden2} with references treated as non-markup '
      f'(a fall of {burden - burden2})')
