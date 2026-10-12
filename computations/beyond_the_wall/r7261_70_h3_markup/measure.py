#!/usr/bin/env python3
"""r7261+70.1: H-a..H-d of PREDICTION.md, on the 270 MEANING-HELD rows and on every PAPER key of the baseline."""
import glob, json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_quote_pins as Q

MARK = re.compile(r'\$|\\[A-Za-z]+')
rows = [(k, v) for k, v in Q.read_baseline().items()]
held = [(k, v) for k, v in rows if v[3] == Q.MEANING_HELD]
out = {'held': len(held), 'raw_fail': [], 'norm_fail': [], 'burden': 0, 'paper_held': 0}

def papers_at(sha):
    names = [n for n in Q._git('ls-tree', '--name-only', sha, 'corpus/').stdout.split()
             if n.endswith('.tex') and not os.path.basename(n).startswith('appendix_receipts')]
    return [Q._flat(Q._git('show', f'{sha}:{n}').stdout) for n in names]

for (rc, lit), (t, tier, fl, v, why) in held:
    t = 'PAPER' if rc.endswith('B57_the_rules_are_centre_data_the_force_is_root_vectors.py') and \
        lit == 'baryon 1, diquark 0, meson 1' else t
    sha = Q._git('rev-parse', Q._HELD_AT.search(why).group(1)).stdout.strip()
    raw = Q._present_at(sha, lit, t, rc, normalise=False)
    if not raw:
        out['raw_fail'].append(rc.split('/')[-1][:40] + ' ' + lit[:40])
    if not Q._present_at(sha, lit, t, rc):
        out['norm_fail'].append(rc.split('/')[-1][:40] + ' ' + lit[:40])
    if t == 'PAPER':
        out['paper_held'] += 1
        if raw:
            for p in papers_at(sha):
                i = p.find(lit)
                if i < 0:
                    continue
                a = max(p.rfind('. ', 0, i), p.rfind('\n\n', 0, i)) + 1
                b = p.find('. ', i + len(lit))
                sent = p[a:b if b >= 0 else len(p)]
                out['burden'] += bool(MARK.search(sent.replace(lit, '')))
                break

# H-d: PAPER keys whose literal carries markup and gains a match location under N
tex = [Q._flat(open(p, encoding='utf-8', errors='replace').read()) for p in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
       if not os.path.basename(p).startswith('appendix_receipts')]
ntex = [Q._unmark(x) for x in tex]
coll = []
for (rc, lit), (t, *_r) in rows:
    if t != 'PAPER' or not MARK.search(lit):
        continue
    r = sum(x.count(lit) for x in tex)
    n = sum(x.count(Q._unmark(lit)) for x in ntex)
    if n > r:
        coll.append((rc, lit, r, n))
out['collisions'] = len(coll)
print(json.dumps({k: v for k, v in out.items()}, indent=1, ensure_ascii=False))
for c in coll:
    print('COLLISION', c[0].split('/')[-1][:50], json.dumps(c[1], ensure_ascii=False), 'raw', c[2], 'N', c[3])

# H-c, broken down (NOT scored; the registered H-c counts any `\command`, which includes `\cite` and `\ref`)
import collections
kinds = collections.Counter()
for (rc, lit), (t, tier, fl, v, why) in held:
    if t != 'PAPER':
        continue
    sha = Q._git('rev-parse', Q._HELD_AT.search(why).group(1)).stdout.strip()
    for p in papers_at(sha):
        i = p.find(lit)
        if i < 0:
            continue
        a = max(p.rfind('. ', 0, i), p.rfind('\n\n', 0, i)) + 1
        b = p.find('. ', i + len(lit))
        rest = p[a:b if b >= 0 else len(p)].replace(lit, ' ')
        m = '$' in rest
        e = bool(Q._EMPH.search(rest))
        r = bool(re.search(r'\\(?:cite|ref|eqref|rcpt|ldg|S)\b', rest))
        kinds['math' if m else 'emphasis' if e else 'reference-only' if r else
              'other-command' if MARK.search(rest) else 'none'] += 1
        kinds['literal carries markup itself'] += bool(MARK.search(lit))
        break
print('H-c by kind (first match wins: math, emphasis, reference-only, other-command, none):', dict(kinds))
