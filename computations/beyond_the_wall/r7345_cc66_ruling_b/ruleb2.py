#!/usr/bin/env python3
"""r7345+cc66 ruling (b), second pass: the exclusion is a CONJUNCTION of mechanism tests, each
stated, scored against the hand-judged 14."""
import importlib.util, json, re, sys
S = sys.argv[1]
spec = importlib.util.spec_from_file_location('m', S + '/mutate_assertions.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
hand = {(a, json.loads(b)) for a, b in
        (x.split('\t') for x in open(S + '/want14.txt').read().split('\n') if '\t' in x)}
new = {(q[0], json.loads(q[1])) for q in
       (ln.rstrip('\n').split('\t') for ln in open(S + '/k_new2.keys')) if len(q) == 2}

# ⓐ the trace READS a .py as TEXT: a line-wise split, a whole-file read, or a git blob read.
READ_PY = re.compile(r"\.splitlines\(|\.split\('\\n'\)|\.readlines\(|open\(|cat-file|git\('show'|git\('grep'")
# ⓑ ...but a path used as a dict KEY is not a file this container reads.
KEY_ONLY = re.compile(r"\[\s*(?:f?'[^']*\.py'|f?\"[^\"]*\.py\")\s*\]")
# ⓒ ...and a module IMPORTED from source is a namespace, not source text.
IMPORTED = re.compile(r"ModuleType|exec_module|spec_from_file_location|importlib")

def excl(kinds, trace, cont_text):
    if kinds != {'py'}:          # tex (or any other kind) beside it is _rstar's UNDECIDED shape
        return False
    if not READ_PY.search(trace):
        return False
    if IMPORTED.search(trace):
        return False
    if KEY_ONLY.search(cont_text):
        return False
    return True

got = set()
for r in m.quote('/home/user/shadow-of-existence'):
    key = (r['receipt'], r['lit'])
    if key not in new:
        continue
    t = r.get('_trace') or ''
    cont_text = t.split('\n')[0] if t else ''
    deep = r.get('_deep') or t
    if excl(set(m._EXT.findall(deep)), deep, cont_text):
        got.add(key)
tp, fp, fn = len(got & hand), len(got - hand), len(hand - got)
print(f'caught={len(got)}  hit={tp}  over={fp}  missed={fn}   (hand class = {len(hand)})')
print('--- over ---')
for k in sorted(got - hand):
    print('  ', k[0].split('/')[-1][:44], '|', k[1][:46])
print('--- missed ---')
for k in sorted(hand - got):
    print('  ', k[0].split('/')[-1][:44], '|', k[1][:46])
