#!/usr/bin/env python3
"""r7345+cc66.5 -- SCORE half B ONCE against the rule frozen in DECLARATION.md (5d45a20e0).

Labels come from commit 7db5db61c, pushed before r7345 existed:
  PIN     = keep82.tsv minus the 2 residual keys READING.md ③ names
  NON-PIN = the 35 excluded (117 - 82) plus those 2 residual keys
Usage: python3 -I score.py <scratch-dir-with-extractor-copy> <repo-root>
"""
import hashlib, importlib.util, json, re, subprocess, sys

S, ROOT = sys.argv[1], sys.argv[2]
PRE = '7db5db61c'

def at(path):
    return subprocess.run(['git', '-C', ROOT, 'show', f'{PRE}:{path}'],
                          capture_output=True, text=True, check=True).stdout

BASE = 'computations/beyond_the_wall/r7343_cc66_the_container_read/'
all117 = {(q[0], json.loads(q[1])) for q in
          (ln.split('\t') for ln in at(BASE + 'new117.tsv').split('\n') if '\t' in ln)}
keep82 = {(q[0], json.loads(q[1])) for q in
          (ln.split('\t') for ln in at(BASE + 'keep82.tsv').split('\n') if '\t' in ln)}
# the 2 residual keys READING.md ③ names as still not pins
RESIDUAL_LITS = {'PO-',
                 'receipts/P15_CR_cosmology/P15_the_corpus_places_every_perturbation_source_before_'
                 'the_branch_point_and_everything_after_it_is_transfer_so_nothing_already_built_'
                 'supplies_anisotropic_content_on_the_expansion_leg.py'}
residual = {k for k in keep82 if k[1] in RESIDUAL_LITS}
assert len(residual) == 2, f'residual lits matched {len(residual)}, expected 2'
label = {k: ('PIN' if (k in keep82 and k not in residual) else 'NON-PIN') for k in all117}

# ---- the rule, transcribed from DECLARATION.md ② and not altered here ----
E1_READ = re.compile(r"\.splitlines\(|\.split\('\\n'\)|\.readlines\(|open\(|cat-file|git\('show'|git\('grep'")
E1_IMPORT = re.compile(r"ModuleType|exec_module|spec_from_file_location|importlib")
E1_KEYONLY = re.compile(r"\[\s*f?['\"][^'\"]*\.py['\"]\s*\]")
E2_STAMP = re.compile(r"r\d{4,5}\+(?:\d{2}|cc\d{2})(?:\.\d+)?")
E2_BARE = re.compile(r"^(?:\+\d+|cc\d+)$")
E3_DELIM = re.compile(r"^[-|=_\s]+$")

def verdict(lit, kinds, trace):
    cont = trace.split('\n')[0] if trace else ''
    if (kinds == {'py'} and E1_READ.search(trace) and not E1_IMPORT.search(trace)
            and not E1_KEYONLY.search(cont)):
        return 'E1'
    if ({'tsv', 'md'} & kinds) and (E2_STAMP.search(lit) or E2_BARE.match(lit)):
        return 'E2'
    if E3_DELIM.match(lit.strip()):
        return 'E3'
    return 'KEEP'

spec = importlib.util.spec_from_file_location('m', S + '/mutate_assertions.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
seen = {}
for r in m.quote(ROOT):
    k = (r['receipt'], r['lit'])
    if k not in all117:
        continue
    t = r.get('_trace') or ''
    v = verdict(r['lit'], set(m._EXT.findall(t)), t)
    if k not in seen or seen[k] == 'KEEP':      # any site's exclusion excludes the key
        seen[k] = v

def half(k):
    return 'A' if int(hashlib.sha256((k[0] + '\t' + k[1]).encode()).hexdigest()[0], 16) % 2 == 0 else 'B'

for H in ('A', 'B'):
    pop = [k for k in all117 if half(k) == H]
    forgone = [k for k in pop if label[k] == 'PIN' and seen.get(k, 'KEEP') != 'KEEP']
    missed = [k for k in pop if label[k] == 'NON-PIN' and seen.get(k, 'KEEP') == 'KEEP']
    excl = [k for k in pop if seen.get(k, 'KEEP') != 'KEEP']
    print(f'=== half {H}: {len(pop)} keys;  rule excludes {len(excl)};  '
          f'GENUINE FORGONE {len(forgone)};  NON-PINS KEPT (named) {len(missed)}')
    for tag, lst in (('FORGONE', forgone), ('KEPT-NON-PIN', missed)):
        for k in sorted(lst):
            print(f'    [{tag}] {seen.get(k, "KEEP"):4} {k[0].split("/")[-1][:40]} | {k[1][:48]}')
