"""r7805+cc66 item ①: classify every item on today's PO-87 census as re-derived, re-grounded or
still standing.

The census (`r7667/census.py`) is re-run unmodified; this reads its output and applies the three
verdicts registered in PREDICTION.md.  The discriminator it adds is the one the census does not
make: WHOSE spectrum each item reads.

  * a spectrum whose stem carries `lcdm` is the LAMBDA-CDM CONTROL's.  A control has no leaf rate --
    there is no such thing as LCDM on the leaf rate -- so a control spectrum is "off the leaf rate"
    by construction, and every receipt that compares the arm against the control must read one.
  * a spectrum whose banked `config` says `LEAFGEOM: true` IS the one-rate build: the configuration
    PO-87 wants figures derived on.  The census misreads these as namesakes because its suffix test
    looks for `_leafrec1` and the corpus's newer banks are named descriptively.
  * anything else read on the arm side is a candidate for genuinely standing.

Run: python3 computations/.../r7667_cc66_po87_the_unfiltered_list/census.py | python3 classify.py
     python3 classify.py <census stdout file>        (a path also works)
"""
import glob
import os
import re
import sys

import numpy as np

# The census text comes from STDIN unless a readable path is given.  ⛔ It used to default to a path
# under /tmp, which existed on the authoring machine and NOT on the runner -- so this script crashed
# in CI, the receipt's gate 6 parsed nothing, its counts fell back to -1, and the receipt went red
# there while passing here.  A default that only resolves on one machine is not a default.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
    txt = open(sys.argv[1]).read()
else:
    txt = sys.stdin.read()
    if not txt.strip():
        raise SystemExit('no census text: pass a path as argv[1] or pipe census.py\'s stdout in')
block = txt[txt.index('THE UNFILTERED LIST'):]

ITEM = re.compile(
    r'^  \[(\d+)\] \[(\w+)\] (receipts/\S+)\n'
    r'       spectra read \(namesake/superseded\): \[([^\]]*)\]\n'
    r'       re-derivable by repointing: ([^\n]*)\n'
    r'((?:       \S[^\n]*\n)*)', re.M)

_cfg_cache = {}


def leafgeom(stem):
    """True if the bank's own config says LEAFGEOM, None if the bank records no config at all."""
    if stem in _cfg_cache:
        return _cfg_cache[stem]
    hits = glob.glob(os.path.join(ROOT, 'computations', 'beyond_the_wall', '**', stem + '.npz'),
                     recursive=True)
    out = 'missing'
    if hits:
        out = 'no-config'
        try:
            with np.load(hits[0], allow_pickle=True) as z:
                for k in ('config', 'switches', '__SWITCHES__'):
                    if k in z.files:
                        v = z[k]
                        s = str(v.item() if v.shape == () else v)
                        out = ('LEAFGEOM' if re.search(r'"?LEAFGEOM"?\s*[:=]\s*(true|1)', s, re.I)
                               else 'arm-no-leafgeom')
                        break
        except Exception as e:                                                      # noqa: BLE001
            out = f'unreadable ({type(e).__name__})'
    _cfg_cache[stem] = out
    return out


rows = []
for n, tag, path, spectra, rederiv, sents in ITEM.findall(block):
    stems = [s.strip().strip("'\"")[:-4] for s in spectra.split(',') if s.strip()]
    kinds = {}
    for st in stems:
        kinds[st] = 'CONTROL' if 'lcdm' in st.lower() else leafgeom(st)
    arm_side = [s for s, k in kinds.items() if k not in ('CONTROL', 'LEAFGEOM')]
    if not stems:
        verdict, why = 'UNDECIDED (needs a read)', 'reads no namesake; on the list only because every load site is undecidable'
    elif all(k == 'CONTROL' for k in kinds.values()):
        verdict, why = 'NOT A DEFECT (control)', 'every spectrum it reads is the control\'s own, and a control has no leaf rate'
    elif all(k in ('CONTROL', 'LEAFGEOM') for k in kinds.values()):
        verdict, why = 'RE-DERIVED', 'the arm-side spectrum it reads IS the one-rate build (config says LEAFGEOM)'
    else:
        verdict, why = 'STANDS (candidate)', f'reads arm-side spectra that are not the one-rate build: {sorted(arm_side)}'
    first = ''
    m = re.search(r'corpus/\S+\.tex: "(.{0,240})', sents)
    if m:
        first = m.group(1)
    rows.append((int(n), path.split('/')[-1], kinds, verdict, why, first))

print(f'  PO-87 CENSUS ON TODAY\'S TREE -- {len(rows)} items, classified\n')
by = {}
for r in rows:
    by.setdefault(r[3], []).append(r)
for v in ('STANDS (candidate)', 'NOT A DEFECT (control)', 'RE-DERIVED', 'UNDECIDED (needs a read)'):
    got = by.get(v, [])
    print(f'  {"=" * 96}\n  {v}: {len(got)}\n  {"=" * 96}')
    for n, name, kinds, verdict, why, first in got:
        print(f'   [{n:02d}] {name[:92]}')
        print(f'        {why}')
        if kinds:
            print(f'        spectra: ' + '; '.join(f'{s}={k}' for s, k in sorted(kinds.items())))
        if first and v in ('STANDS (candidate)', 'RE-DERIVED'):
            print(f'        sentence: "{first[:200]}..."')
    print()
print('  ' + '-' * 96)
print(f'  TOTAL {len(rows)}:  ' + ',  '.join(f'{k} {len(v)}' for k, v in sorted(by.items())))
