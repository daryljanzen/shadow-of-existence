"""r7807+cc66 item ①: resolve every bank the 23 PO-87 items load to its PRODUCING SWITCHES.

The banks mostly carry no `config` (that is why 16 items are undecidable), so each is traced to the
shell line that produced it and the three rate switches are read off that line:

    LEAFSCALES  the acoustic scales on the leaf rate
    LEAFREC     recombination read on the leaf rate   <- the census's `_leafrec1` marker
    LEAFGEOM    the PROJECTION DISTANCE on the leaf rate

⛔ THE DISTINCTION THIS ROUND HAS TO MAKE AND THE CENSUS DOES NOT.  Its marker is the `_leafrec1`
suffix, i.e. LEAFREC alone.  But after r7749/r7801 "the leaf rate" for a FIGURE means the projection
too -- the sentence P15 now carries is "the perturbations and the projection alike on the rate the
universe has".  So a bank splits three ways, not two:

    LEAFREC=0                 plainly off the leaf rate
    LEAFREC=1, LEAFGEOM=0     on it for the scales and recombination, OFF it for the projection
    LEAFGEOM=1                the one-rate build

Run: python3 trace_banks.py
"""
import glob
import json
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(BW))
FLAGS = ('LEAFSCALES', 'LEAFREC', 'LEAFGEOM')
_sh = {p: open(p, errors='replace').read() for p in
       glob.glob(os.path.join(BW, '**', '*.sh'), recursive=True)}
_py = {p: open(p, errors='replace').read() for p in
       glob.glob(os.path.join(BW, '**', '*.py'), recursive=True)}


def bank_path(stem):
    hits = glob.glob(os.path.join(BW, '**', stem + '.npz'), recursive=True)
    return hits[0] if hits else None


def from_config(stem):
    p = bank_path(stem)
    if not p:
        return None
    try:
        with np.load(p, allow_pickle=True) as z:
            for k in ('config', 'switches', '__SWITCHES__'):
                if k in z.files:
                    v = z[k]
                    s = str(v.item() if v.shape == () else v)
                    try:
                        c = json.loads(s)
                        return {f: bool(c.get(f)) for f in FLAGS}, 'config'
                    except (ValueError, TypeError):
                        return ({f: bool(re.search(rf'{f}=1|"{f}":\s*true', s, re.I)) for f in FLAGS},
                                'switches-string')
    except Exception:                                                        # noqa: BLE001
        return None
    return None


def _expand(line, text, depth=0):
    """Substitute shell variable definitions from the same file, recursively.

    ⛔ Without this the tracer missed almost every bank: the dominant recipe shape is a TAG plus a
    shared variable -- `c54.178_cr $CR $F178` -- so the rate switches are never on the stem's own
    line.  A tracer that reads only that line reports UNTRACED and looks like an absence of
    evidence when it is an absence of substitution.
    """
    if depth > 4:
        return line
    for var in set(re.findall(r'\$\{?([A-Za-z_][A-Za-z0-9_]*)\}?', line)):
        m = re.search(rf'^{var}=(?:"([^"]*)"|\'([^\']*)\'|(\S+))', text, re.M)
        if m:
            val = next(g for g in m.groups() if g is not None)
            line = re.sub(rf'\$\{{?{var}\}}?(?![A-Za-z0-9_])', _expand(val, text, depth + 1), line)
    return line


def from_producer(stem):
    """The recipe line that names this stem, with its shared variables expanded.

    A line is a RECIPE only if, once expanded, it carries `ARM=` -- which excludes reader scripts
    that merely open the bank.  That mattered: `cc66_r185_verify_cr` first traced to a READER
    (`contrast_two_models.py`) and took its flags from a line that produced nothing.
    """
    pat = re.compile(re.escape(stem) + r'(?![A-Za-z0-9_])')
    best = None
    for src in (_sh, _py):
        for path, text in src.items():
            for line in text.split('\n'):
                if not pat.search(line):
                    continue
                full = _expand(line, text)
                if 'ARM=' not in full:
                    continue
                flags = {f: bool(re.search(rf'\b{f}=1\b', full)) for f in FLAGS}
                cand = (flags, os.path.relpath(path, ROOT), full.strip()[:170])
                # prefer a .sh recipe over a .py one, and any recipe over none
                if best is None or (path.endswith('.sh') and not best[1].endswith('.sh')):
                    best = cand
    return best


def verdict(stem):
    if 'lcdm' in stem.lower():
        return 'CONTROL', 'the bank is the control\'s own', None
    c = from_config(stem)
    if c:
        flags, how = c
        src = f'its own banked `{how}`'
    else:
        p = from_producer(stem)
        if not p:
            return 'UNTRACED', 'no config and no producing line names this stem', None
        flags, path, line = p
        src = f'its producer `{path}`'
    if flags['LEAFGEOM']:
        return 'ON THE LEAF RATE', f'LEAFGEOM=1 per {src}', flags
    if flags['LEAFREC']:
        return 'SPLIT (projection off)', f'LEAFREC=1 but LEAFGEOM=0 per {src}', flags
    return 'OFF THE LEAF RATE', f'no leaf-rate switch per {src}', flags


if __name__ == '__main__':
    import sys
    stems = sys.argv[1:]
    if not stems:
        raise SystemExit('give bank stems as arguments')
    for s in stems:
        v, why, flags = verdict(s)
        print(f'  {s:34} {v:24} {why}')
        if flags:
            print(f'  {"":34} flags: ' + ', '.join(f'{k}={int(v2)}' for k, v2 in flags.items()))
