"""Seeds for the MULTI-SITE ratchet, in a throwaway worktree carrying this tree's uncommitted operator and gate."""
import json, os, re, shutil, subprocess, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
WT = '/tmp/claude-0/wt_r7201_seed'
FILES = ['scripts/mutate_assertions.py', 'corpus/check_quote_pins.py', 'corpus/quote_pin_baseline.tsv']
def fresh():
    subprocess.run(['git', '-C', ROOT, 'worktree', 'remove', '--force', WT], capture_output=True)
    subprocess.run(['git', '-C', ROOT, 'worktree', 'add', '--detach', WT, 'HEAD'], check=True, capture_output=True)
    for f in FILES: shutil.copy(os.path.join(ROOT, f), os.path.join(WT, f))
def gate():
    r = subprocess.run([sys.executable, 'corpus/check_quote_pins.py'], cwd=WT, capture_output=True, text=True)
    m = re.search(r'MULTI-SITE: (\d+) pinned', r.stdout)
    return r.returncode, int(m.group(1)) if m else None, [l.strip() for l in r.stdout.splitlines() if 'MULTI-SITE COUNT ROSE' in l]
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_quote_pins as G
live = G.measure()
single = next((k, v) for k, v in sorted(live.items()) if v[0] == 'PAPER' and v[1] == 'SENTENCE' and 'MULTI' not in v[2]
              and 'P15_CR_cosmology' in k[0] and len(k[1]) > 30 and k[1] in open(os.path.join(ROOT, 'corpus/CR_cosmology.tex')).read())
multi = next((k, v) for k, v in sorted(live.items()) if 'MULTI' in v[2] and 'P15_CR_cosmology' in k[0]
             and open(os.path.join(ROOT, 'corpus/CR_cosmology.tex')).read().count(k[1]) == 2)
res = {}
fresh(); res['S0 HEAD'] = gate()
fresh()
p = os.path.join(WT, 'corpus/CR_cosmology.tex'); t = open(p).read()
open(p, 'w').write(t.replace('\\end{document}', single[0][1] + '\n\n\\end{document}', 1)); res['S1 a single-site literal duplicated'] = gate()
fresh()
t = open(p).read(); open(p, 'w').write(t.replace(multi[0][1], 'REMOVED-BY-SEED', 1)); res['S2 one copy of a two-copy MULTI literal removed'] = gate()
subprocess.run(['git', '-C', ROOT, 'worktree', 'remove', '--force', WT], capture_output=True)
print('single-site key used:', single[0][0].split('/')[-1][:60], json.dumps(single[0][1])[:80])
print('multi-site key used: ', multi[0][0].split('/')[-1][:60], json.dumps(multi[0][1])[:80])
for k, (rc, n, msg) in res.items(): print(f'{k}: rc {rc}, MULTI {n}', msg[:1])
ok = res['S0 HEAD'][0] == 0 and res['S1 a single-site literal duplicated'][0] == 1 and res['S1 a single-site literal duplicated'][1] == 250 \
     and res['S2 one copy of a two-copy MULTI literal removed'][0] == 0 \
     and res['S2 one copy of a two-copy MULTI literal removed'][1] < 249
# ⌗ The first run expected S2 to read exactly 248 and read 247: the literal `10.8` is pinned by TWO receipts, so one
#   copy removed takes two keys off the backlog.  The expectation was wrong, not the ratchet; S2 now asserts the
#   count FELL and the gate stayed green, which is what the ratchet promises.
print('RATCHET SEEDS:', 'HELD' if ok else 'MISSED')
