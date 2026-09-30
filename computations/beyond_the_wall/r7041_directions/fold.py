"""ONE definition of "is this configuration complete", shared by every reader of r7041's runs.

** WHY THIS IS A MODULE AND NOT A COPIED SNIPPET. **  The runs exist in two forms: five configurations
finished UNSLICED before this container's restarts made that scheme unworkable, and the rest are sliced on
`KSLICE` at width 250.  *A reader that knows about only one form silently reports a configuration as absent;
a reader that re-implements the completeness test disagrees with the launcher about what "done" means.*
⇒ Both live here, once.

⛔ ** AND COMPLETENESS IS CHECKED, NOT INFERRED FROM A FILE COUNT. **  A slice's mode count comes from its
own slice-0 log (`modes = N`, the instrument's own print), and every slice from 0 to N in steps of 250 must
be present AND carry `__DONE__`.  *A count of files cannot tell a complete set from one missing its middle,
which is exactly the failure `r6911`'s bank guarded against and the reason this is not a glob.*

⌗ ** An out-of-range slice contributes exactly zero **, verified at r7041+cc66.70 (`max|Dl| = 0.0`), so the
sum over a complete set is exact whether or not the last slice is full.
"""
import glob
import os
import re

import numpy as np

W = 250


def _done(log):
    try:
        with open(log, encoding='utf-8', errors='replace') as f:
            return '__DONE__' in f.read()
    except OSError:
        return False


def modes_from_log(log):
    """the instrument's OWN count, read rather than re-derived from KFAC and NK"""
    try:
        with open(log, encoding='utf-8', errors='replace') as f:
            m = re.search(r'modes = (\d+)', f.read())
        return int(m.group(1)) if m else None
    except OSError:
        return None


def load(outdir, tag):
    """(ls, Dl, l_A, form) for a COMPLETE configuration, or None -- with `form` naming which scheme"""
    un = os.path.join(outdir, f'{tag}.npz')
    if os.path.exists(un) and _done(os.path.join(outdir, f'{tag}.log')):
        d = np.load(un)
        return d['ls'].astype(float), np.asarray(d['Dl'], float), float(d['l_A']), 'unsliced'
    k0log = os.path.join(outdir, f'{tag}_k0.log')
    n = modes_from_log(k0log)
    if n is None or not _done(k0log):
        return None
    want = list(range(0, n, W))
    parts = []
    for i in want:
        f = os.path.join(outdir, f'{tag}_k{i}.npz')
        if not (os.path.exists(f) and _done(os.path.join(outdir, f'{tag}_k{i}.log'))):
            return None
        parts.append(np.load(f))
    ls = parts[0]['ls']
    for p in parts:
        if not np.array_equal(p['ls'], ls):
            raise SystemExit(f'{tag}: slices disagree on the multipoles')
    Dl = sum(np.asarray(p['Dl'], float) for p in parts)
    return ls.astype(float), Dl, float(parts[0]['l_A']), f'sliced({len(parts)})'


def status(outdir, tag):
    """how far a configuration has got, for a partial read to LABEL itself honestly"""
    k0log = os.path.join(outdir, f'{tag}_k0.log')
    n = modes_from_log(k0log)
    if os.path.exists(os.path.join(outdir, f'{tag}.npz')) and _done(os.path.join(outdir, f'{tag}.log')):
        return 'complete (unsliced)'
    if n is None:
        return 'not started'
    want = list(range(0, n, W))
    have = sum(1 for i in want
               if os.path.exists(os.path.join(outdir, f'{tag}_k{i}.npz'))
               and _done(os.path.join(outdir, f'{tag}_k{i}.log')))
    return f'{have}/{len(want)} slices'


if __name__ == '__main__':
    D = '/tmp/n66/r7041'
    # ⌗ ** BOTH FORMS, or the report understates its own progress. **  A scan for `*_k0.log` alone misses
    # the five configurations that finished UNSLICED and have no slice-0 log at all -- so it would print
    # them as absent while `load()` folds them happily.  *A status view that disagrees with the loader is
    # worse than no status view.*
    rows = []
    for o in ('inj', 'real'):
        d = os.path.join(D, o)
        for f in sorted(glob.glob(os.path.join(d, '*_k0.log'))):
            rows.append((d, os.path.basename(f)[:-7]))
        for f in sorted(glob.glob(os.path.join(d, '*.log'))):
            b = os.path.basename(f)[:-4]
            if not re.search(r'_k\d+$', b) and not b.endswith('_src'):
                rows.append((d, b))
    seen = set()
    done = 0
    for o, t in rows:
        if (o, t) in seen:
            continue
        seen.add((o, t))
        st = status(o, t)
        if st.startswith('complete') or st.split('/')[0] == st.split('/')[-1].split()[0]:
            pass
        r = load(o, t)
        done += r is not None
        print(f'  {t:42s} {st:22s} {"FOLDS" if r is not None else "-"}')
    print(f'\n  {done} of {len(seen)} started configuration(s) fold to a complete spectrum')
