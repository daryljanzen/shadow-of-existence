#!/usr/bin/env python3
"""r7345+cc66 ruling (b): what does the _SELF sibling drop from the EXISTING key set?
Scored on the BASE extractor (the hop is not landed), which is the thing the ratchet reads."""
import importlib.util, json, re, sys
S = sys.argv[1]
spec = importlib.util.spec_from_file_location('m', S + '/base_mutate.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
READ = re.compile(r"\.splitlines\(|\.split\('\\n'\)|\.readlines\(|open\(|cat-file|git\('show'|git\('grep'")
IMPORTED = re.compile(r"ModuleType|exec_module|spec_from_file_location|importlib")
KEYONLY = re.compile(r"\[\s*f?['\"][^'\"]*\.py['\"]\s*\]")
def other_source(trace):
    if set(m._EXT.findall(trace)) != {'py'}:
        return False
    if IMPORTED.search(trace):
        return False
    if KEYONLY.search(trace.split('\n')[0]):
        return False
    return bool(READ.search(trace))
drop, keep = {}, set()
for r in m.quote('/home/user/shadow-of-existence'):
    k = (r['receipt'], r['lit'])
    t = r.get('_trace') or ''
    if t and other_source(t):
        drop.setdefault(k, r)
    else:
        keep.add(k)
dropped = {k for k in drop if k not in keep}   # every SITE of the key must be dropped
print(f'existing keys: {len(keep | set(drop))};  keys ALL of whose sites the rule drops: {len(dropped)}')
with open(S + '/would_drop.tsv', 'w') as f:
    for k in sorted(dropped):
        r = drop[k]
        f.write('\t'.join([k[0], json.dumps(k[1]), r['target'], r['tier']]) + '\n')
for k in sorted(dropped):
    print('  ', drop[k]['target'], drop[k]['tier'], '|', k[0].split('/')[-1][:40], '|', k[1][:44])
