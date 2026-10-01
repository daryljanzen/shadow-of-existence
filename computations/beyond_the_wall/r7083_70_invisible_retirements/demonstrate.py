"""r7083 (70) -- the count, and the hazard shown on a scratch copy.  The ledger itself is never edited.

1. COUNT: every comment line of corpus/open_ledger.txt carrying a ledger row (`<id> | <paper> | <VERDICT> |`),
   id-first (`# <id> | ...`, which the parsers read) against prefixed (`# ⌗ RETIRED (...): <id> | ...`, which
   they do not); plus ids that comment prose names as retired and that have no row line anywhere.
2. HAZARD: in a scratch copy of corpus/, one prefixed retired id is put back LIVE.  check_open_ledger's
   ⓸ ("none both live and retired") is run as the retirement stands (prefixed), then with that one line
   converted to id-first.  Both runs print what ⓸ says about that id.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
LED = os.path.join(ROOT, 'corpus', 'open_ledger.txt')
ROW = re.compile(r'\b([0-9a-f]{10})\s*\|\s*[^|]+\|\s*[A-Z][A-Z-]+\s*\|')
FIRST = re.compile(r'#\s*([0-9a-f]{10})\s*\|')        # the parsers' own regex

L = open(LED, encoding='utf-8').read().splitlines()
first, pref, live = {}, {}, set()
for i, l in enumerate(L, 1):
    m = ROW.search(l)
    if not m:
        continue
    if not l.startswith('#'):
        live.add(m.group(1))
    elif FIRST.match(l):
        first.setdefault(m.group(1), []).append(i)
    else:
        pref.setdefault(m.group(1), []).append(i)
rows = set(first) | set(pref) | live
prose = set()
for l in L:
    if l.startswith('#') and not ROW.search(l):
        prose |= set(re.findall(r'(?<![0-9a-f])([0-9a-f]{10})(?![0-9a-f])', l))
prose_only = sorted(prose - rows)
noncomm = sum(1 for l in L if l.startswith('#') and not FIRST.match(l))

print('COUNT')
print(f'  comment lines not id-first (all prose included): {noncomm}')
print(f'  retired ROW lines, id-first (visible to the parsers): {sum(map(len, first.values()))} over {len(first)} ids')
print(f'  retired ROW lines, prefixed (invisible):              {sum(map(len, pref.values()))} over {len(pref)} ids')
print(f'  ids named retired in prose with NO row line at all:   {len(prose_only)}  {prose_only}')
print(f'  TRUE retired ids: {len(set(first) | set(pref) | set(prose_only))}  '
      f'(check_open_ledger prints {len(first)})')
print(f'  prefixed ids also live: {sorted(set(pref) & live) or "none"};  also id-first: {sorted(set(pref) & set(first)) or "none"};'
      f'  repeated: {sorted(k for k, v in pref.items() if len(v) > 1) or "none"}')
shapes = {}
for k, v in pref.items():
    s = re.sub(r'\(.*?\)', '(…)', L[v[0] - 1].split(k)[0])
    shapes[s] = shapes.get(s, 0) + 1
print(f'  prefix shapes: {shapes}')


def gate_on(ledger_lines):
    with tempfile.TemporaryDirectory() as t:
        shutil.copytree(os.path.join(ROOT, 'corpus'), os.path.join(t, 'corpus'), symlinks=True)
        for d in os.listdir(ROOT):           # the papers the scan reads sit beside corpus/ only via ROOT
            if d not in ('corpus', '.git') and not os.path.exists(os.path.join(t, d)):
                os.symlink(os.path.join(ROOT, d), os.path.join(t, d))
        open(os.path.join(t, 'corpus', 'open_ledger.txt'), 'w', encoding='utf-8').write('\n'.join(ledger_lines) + '\n')
        r = subprocess.run([sys.executable, 'corpus/check_open_ledger.py'], cwd=t, capture_output=True, text=True)
        return r.returncode, r.stdout


k = sorted(pref)[0]
ln = pref[k][0] - 1
row = L[ln][L[ln].index(k):]
base = L + [row]                                          # the same row, put back LIVE
conv = list(base)
conv[ln] = '# ' + row                                     # that one retirement in id-first form
print(f'\nHAZARD, on scratch copies: id {k} (ledger line {ln + 1}) put back LIVE')
for lab, lines in (('retirement as it stands (prefixed)', base), ('that one line converted to id-first', conv)):
    rc, out = gate_on(lines)
    said = [l.strip() for l in out.splitlines() if k in l and ('BOTH' in l or 'FAIL' in l)]
    print(f'  {lab:38s} rc={rc}  ⓸ on {k}: {said[0] if said else "SILENT"}')
