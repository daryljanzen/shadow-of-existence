#!/usr/bin/env python3
"""r7355+cc66 ④ -- RE-MEASURE the three r7351 limit figures on the merged trunk.

`r7355` ④: *"You closed that revision with: 80 genuine pins stay invisible to the ratchet, and the
price of making them visible is 13 keys no stated container rule excludes, 11 of them because the
instrument's own trace names nothing to test.  Those three numbers were measured before 157 rows
were repaired across three seats.  Re-measure all three on the merged trunk."*

POPULATION: the `117` hop-minted keys whose hand labels are frozen at `7db5db61c` -- `new117.tsv`
and `keep82.tsv`, both pushed before `r7345` was written, so the labels cannot be revised to fit.
The `2` residual keys `READING.md` ③ names are re-classed NON-PIN exactly as `score.py` did, giving
`80` PIN / `37` NON-PIN.

RULE: `E1`/`E2`/`E3` transcribed from `r7345_cc66_the_one_test/DECLARATION.md` ② and NOT altered.

    python3 -I relimit.py <scratch-dir-with-patched-extractor-copy> <repo-root>
"""
import importlib.util, json, re, subprocess, sys

S, ROOT = sys.argv[1], sys.argv[2]
PRE = '7db5db61c'
BASE = 'computations/beyond_the_wall/r7343_cc66_the_container_read/'


def at(p):
    return subprocess.run(['git', '-C', ROOT, 'show', f'{PRE}:{p}'],
                          capture_output=True, text=True, check=True).stdout


all117 = [(q[0], json.loads(q[1])) for q in
          (ln.split('\t') for ln in at(BASE + 'new117.tsv').split('\n') if '\t' in ln)]
keep82 = {(q[0], json.loads(q[1])) for q in
          (ln.split('\t') for ln in at(BASE + 'keep82.tsv').split('\n') if '\t' in ln)}
RES = {'PO-',
       'receipts/P15_CR_cosmology/P15_the_corpus_places_every_perturbation_source_before_the_branch'
       '_point_and_everything_after_it_is_transfer_so_nothing_already_built_supplies_anisotropic_'
       'content_on_the_expansion_leg.py'}
residual = {k for k in keep82 if k[1] in RES}
assert len(residual) == 2, f'residual lits matched {len(residual)}, expected 2'
label = {k: ('PIN' if (k in keep82 and k not in residual) else 'NON-PIN') for k in all117}
S117 = set(all117)

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
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
seen, kindsof = {}, {}
for r in m.quote(ROOT):
    k = (r['receipt'], r['lit'])
    if k not in S117:
        continue
    t = r.get('_trace') or ''
    kn = set(m._EXT.findall(t))
    v = verdict(r['lit'], kn, t)
    if k not in seen or seen[k] == 'KEEP':      # any site's exclusion excludes the key
        seen[k], kindsof[k] = v, kn
    elif k not in kindsof:
        kindsof[k] = kn

found = [k for k in all117 if k in seen]
excl = [k for k in found if seen[k] != 'KEEP']
forgone = [k for k in found if label[k] == 'PIN' and seen[k] != 'KEEP']
kept_non = [k for k in found if label[k] == 'NON-PIN' and seen[k] == 'KEEP']
kept_pin = [k for k in found if label[k] == 'PIN' and seen[k] == 'KEEP']
empty = [k for k in kept_non if not kindsof.get(k)]

print(f'frozen population        : {len(all117)} keys, PIN {sum(1 for k in all117 if label[k]=="PIN")} '
      f'/ NON-PIN {sum(1 for k in all117 if label[k]=="NON-PIN")}')
print(f'surfaced by the follow   : {len(found):3d}   <-- must be 117 or the follow is not faithful')
print(f'rule excludes            : {len(excl):3d}   (r7351: 24)')
print(f'GENUINE FORGONE          : {len(forgone):3d}   (r7351: 0)')
print(f'genuine pins still KEPT  : {len(kept_pin):3d}   (r7351: 80)   <-- figure 1')
print(f'non-pins the rule KEEPS  : {len(kept_non):3d}   (r7351: 13)   <-- figure 2')
print(f'  of those EMPTY narrow  : {len(empty):3d}   (r7351: 11)   <-- figure 3')
print()
for k in sorted(kept_non):
    print(f'  [KEPT NON-PIN] kinds={",".join(sorted(kindsof.get(k) or [])) or "-":10} '
          f'{k[0].split("/")[-1][:38]} | {k[1][:50]!r}')
for k in sorted(forgone):
    print(f'  [FORGONE] {seen[k]} {k[0].split("/")[-1][:38]} | {k[1][:50]!r}')
