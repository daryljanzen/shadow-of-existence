"""r7137+70.1 (70): the SOURCE/ALT sample -- my reading (fixed before the rule was written) against a mechanical rule.
Reads corpus/quote_pin_baseline.tsv and the receipts; edits nothing."""
import ast, json, os, random, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(ROOT, 'corpus', 'quote_pin_baseline.tsv'), encoding='utf-8')
        if l.strip() and not l.startswith('#')]
keys = sorted((r[0], json.loads(r[1])) for r in rows if r[2] == 'SOURCE' and 'ALT' in r[4] and r[5] == 'UNADJUDICATED')
random.seed(7137)
samp = random.sample(keys, 30)
# my reading, written down from the sites BEFORE the rule below existed (sample order)
READ = ['SPELLING', 'SPELLING', 'SPELLING', 'SPELLING', 'SPELLING', 'SPELLING', 'SPELLING', 'SPELLING', 'VACUOUS',
        'SPELLING', 'SPELLING', 'VACUOUS', 'SPELLING', 'STATE-ENUM', 'STATE-ENUM', 'SPELLING', 'VACUOUS', 'VACUOUS',
        'SPELLING', 'SPELLING', 'SPELLING', 'SPELLING', 'VACUOUS', 'SPELLING', 'SPELLING', 'SPELLING', 'SPELLING',
        'SPELLING', 'SPELLING', 'SPELLING']


def norm(s):
    return re.sub(r'[\s*_{}\\$]+', '', s.lower())


def arms_of(path, lit):
    """the string-literal arms of the innermost `or` holding `lit in X`"""
    tree = ast.parse(open(os.path.join(ROOT, path), encoding='utf-8').read())
    best = None
    for n in ast.walk(tree):
        if isinstance(n, ast.BoolOp) and isinstance(n.op, ast.Or):
            lits = [m.value for m in ast.walk(n) if isinstance(m, ast.Constant) and isinstance(m.value, str)
                    and any(isinstance(p, ast.Compare) and p.left is m for p in ast.walk(n))]
            if lit in lits and (best is None or len(lits) < len(best)):
                best = lits
    return best or [lit]


def rule(arms):
    """VACUOUS: an arm a short generic token (<= 7 chars, one word, or a bare number) beside a longer arm it does not
    contain.  SPELLING: every arm shares a normalised core with another (containment either way).  else STATE-ENUM."""
    ns = [norm(a) for a in arms]
    for a, n in zip(arms, ns):
        short = (len(a) <= 7 and len(a.split()) == 1) or re.fullmatch(r'[\d.]+', a)
        if short and any(len(b) > len(a) and n not in m and m not in n for b, m in zip(arms, ns) if b != a):
            return 'VACUOUS'
    if all(any(i != j and (ns[i] in ns[j] or ns[j] in ns[i]) for j in range(len(ns))) for i in range(len(ns))):
        return 'SPELLING'
    if any(re.search(r'\b(r\d{3,5}|c54\.\d+)\b|\b(open|owed|closed|struck|withdrawn)\b|~~', a, re.I) for a in arms):
        return 'STATE-ENUM'
    return 'SPELLING?'      # different words for one fact, which overlap cannot see


agree = 0
for (p, lit), want in zip(samp, READ):
    arms = arms_of(p, lit)
    got = rule(arms)
    ok = got == want or (got == 'SPELLING?' and want == 'SPELLING')
    agree += ok
    print(f"  {'=' if ok else 'X'} read {want:10s} rule {got:10s} {os.path.basename(p)[:44]:44s} {[a[:28] for a in arms]}")
from collections import Counter
print(f"\n  my reading: {dict(Counter(READ))}")
print(f"  rule agrees on {agree} of {len(READ)} ({100*agree/len(READ):.0f} %)")
