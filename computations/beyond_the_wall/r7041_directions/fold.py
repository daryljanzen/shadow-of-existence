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

W = 250                     # the DEFAULT width, and the width every slice banked before r7051 used

# ⛭ THE WIDTH POLICY LIVES HERE from this revision, because `next_slices` imports this module and not the
#   other way round, and because the count below needs it.  `W` above stays exactly what it says it is: the
#   fallback for a slice that declared no range, which is history and does not move.
GRID = '/tmp/n66/r7041/grid'
BASE_W = 100                # was 250: a slice must finish inside a container window or it is redone from nothing
BASE_NLOS = 560
MIN_W = 40
LSTEP_ELL = {'lstep4': 475}      # tag -> reported l count; everything else runs the base LSTEP=8
BASE_ELL = 238


def arm_cfg(tag):
    """`inj_sweepown_lcdm_nlosf90` -> ('lcdm', 'nlosf90'); None when the tag carries no arm"""
    parts = tag.split('_')
    for i, p in enumerate(parts):
        if p in ('cr', 'lcdm') and i + 1 < len(parts):
            return p, '_'.join(parts[i + 1:])
    return None, None


def width_for(arm, tag):
    """equal-cost width for this configuration, or the default when no grid was banked for it"""
    w = BASE_W * BASE_ELL / LSTEP_ELL.get(tag, BASE_ELL)
    g = os.path.join(GRID, f'g_{arm}_{tag}.npz')
    if not os.path.exists(g):
        return max(MIN_W, int(round(w)))
    try:
        nlos = int(np.load(g)['nlos'])
    except Exception:
        return max(MIN_W, int(round(w)))
    return max(MIN_W, int(round(w * BASE_NLOS / nlos)))


def slice_range(log, lo):
    """a slice's OWN declared k-range, read from its log -- `W` is only the fallback.

    ⛔ ** THE FIRST VERSION ASSUMED THE TILING INSTEAD OF READING IT. **  It built the expected offsets as
    `range(0, n, W)` from a single module-level `W`, so a configuration sliced at any other width read as
    incomplete forever -- and a configuration whose width CHANGED between runs would have read as complete
    off a set that does not tile.  *That is this stretch's own common thread for the fourth time: a claim
    about a set made without reading the set.*
      ⇒ The launcher now writes `__SLICE__ lo:hi` into each slice's log, so a slice states its own extent
      and the fold CHECKS the union rather than predicting it.  Slices banked before that line existed
      report no range, and for those -- and only those -- the historical 250 is assumed, which is what they
      were actually run at.
    """
    try:
        with open(log, encoding='utf-8', errors='replace') as f:
            m = re.search(r'__SLICE__ (\d+):(\d+)', f.read())
        if m:
            return int(m.group(1)), int(m.group(2))
    except OSError:
        pass
    return lo, lo + W


def covered_to(outdir, tag):
    """the first k-index NOT yet covered by a banked, done slice -- walking abutting ranges from 0.

    ⛭ ** THIS IS WHAT LETS A CONFIGURATION CHANGE SLICE WIDTH WITHOUT DISCARDING ANYTHING. **  Because the
    fold checks the UNION of declared ranges rather than a uniform width, new narrower slices may simply
    ABUT the ones already banked: `0:250`, `250:500`, then `500:562`, `562:624`, ... still tiles `[0, n)`
    exactly, with no gap and no overlap.  *Without the range-reading fold this would have meant re-running
    every banked slice of the configuration at the new width.*
    """
    got = []
    for f in sorted(glob.glob(os.path.join(outdir, f'{tag}_k*.npz'))):
        m = re.search(r'_k(\d+)\.npz$', os.path.basename(f))
        if not m:
            continue
        lo = int(m.group(1))
        if _done(os.path.join(outdir, f'{tag}_k{lo}.log')):
            got.append(slice_range(os.path.join(outdir, f'{tag}_k{lo}.log'), lo))
    end = 0
    for lo, hi in sorted(got):
        if lo == end:
            end = hi
        elif lo > end:
            break                        # a gap: everything past it must still be run
    return end


def tiling(outdir, tag, n):
    """the slices present, and whether their declared ranges cover [0, n) exactly -- or None"""
    got = []
    for f in sorted(glob.glob(os.path.join(outdir, f'{tag}_k*.npz'))):
        m = re.search(r'_k(\d+)\.npz$', os.path.basename(f))
        if not m:
            continue
        lo = int(m.group(1))
        log = os.path.join(outdir, f'{tag}_k{lo}.log')
        if not _done(log):
            continue
        got.append(slice_range(log, lo) + (f,))
    got.sort()
    if not got or got[0][0] != 0:
        return None
    # ⛔ ** THIS IS A SEARCH, NOT A WALK, AND IT IS EXACT. **  *A configuration that changed width carries
    #   strays from the old scheme, and a greedy scan over them was defeated twice.*  r7051 refused every
    #   non-abutting slice, so one `2500:2750` banked before a width change made `inj_fixed_lcdm_nlos2240`
    #   unfoldable forever.  Skipping a stray fixed that, and then `inj_fixed_cr_nlos2240` -- tiled exactly by
    #   `0:62 ... 1426:1488` over n=1452, plus a legacy undeclared slice falling back to `250:500` -- still read
    #   as incomplete, because that stray sorts BETWEEN `248:310` and `310:372`.
    #     ⌷ And no scan order fixes it.  Preferring the SHORTER range at a given `lo` strands
    #     `{0:62, 62:124, 0:250, 250:500}`, whose valid tiling is `{0:250, 250:500}`; preferring the LONGER one
    #     strands `{0:50, 50:80, 80:150, 0:100}`, whose valid tiling is the three short ones.  *Greedy is simply
    #     the wrong shape: whether a slice belongs depends on what can follow it.*
    #   ⇒ ** So the reachable ends are searched, breadth-first, and a tiling is returned only when one
    #   ABUTS exactly from 0 to at least `n`. **  Overlaps are never summed, because only `lo == end` can
    #   extend a partial tiling -- so the safety r7051 wanted is structural here rather than conservative, and
    #   "safe and stuck" is gone with it.  *Slices number tens per configuration, so the search is free.*
    nxt = {}
    for lo, hi, f in got:
        nxt.setdefault(lo, []).append((hi, f))
    seen, frontier = {0: None}, [0]
    goal = None
    while frontier and goal is None:
        nf = []
        for e in frontier:
            for hi, f in nxt.get(e, ()):
                if hi <= e or hi in seen:
                    continue             # no progress, or this end is already reachable more cheaply
                seen[hi] = (e, hi, f)
                if hi >= n:
                    goal = hi
                    break
                nf.append(hi)
            if goal is not None:
                break
        frontier = nf
    if goal is None:
        return None                      # no set of declared ranges abuts from 0 to n: a real gap
    used, at = [], goal
    while seen[at] is not None:
        prev, hi, f = seen[at]
        used.append((prev, hi, f))
        at = prev
    used.reverse()
    return used


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
    got = tiling(outdir, tag, n)
    if got is None:
        return None
    parts = [np.load(f) for _lo, _hi, f in got]
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
    # ⛭ THE DENOMINATOR USED TO BE PREDICTED FROM `W`, the default width, while the widths have been
    # per-configuration since r7051.  The comment here said so -- and then this seat summed the column and
    # reported it as progress anyway, which made `inj_fixed_cr_nlos2240` read `25/6` and made every total
    # quoted from it wrong.  ** A documented approximation is still wrong when it is read as a count. **
    # So it now predicts at the configuration's OWN width, the same `width_for` the launcher queues from.
    # *The NUMERATOR still counts what is banked and done, and `load()` remains the authority on coverage.*
    done = [r for r in (tiling(outdir, tag, n) or [])]
    have = len(done) if done else sum(
        1 for f in glob.glob(os.path.join(outdir, f'{tag}_k*.npz'))
        if _done(f[:-4] + '.log'))
    # ⛔ AND THE FRACTION IS REPORTED IN MODES, NOT SLICES.  Counting banked slices against a slice count
    # is incommensurable the moment a width changes: 250-wide slices measured against a 100-wide denominator
    # made a COMPLETE configuration read `6/30`, and against the old fixed denominator made another read
    # `25/6`.  ** Modes are width-independent, so they are what a progress fraction can honestly be made of **
    # -- and `covered_to` already measures exactly that, by the same walk `tiling` verifies.
    covered = min(covered_to(outdir, tag), n)   # the last slice may overhang `n`; that is not extra coverage
    return f'{covered}/{n} modes, {have} slice(s)'


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
        # ⛭ the arm's `nk15` / `nk20` are the same computation as its `base` -- byte-identical `k` and
        # `eta` from `GRIDSAVE`, `max|Dl| = 0.0` on the banked slices -- so they are NOT QUEUED and their
        # slice 0 must not read as a configuration stalled at 1 of 6.  *`report_c.py` substitutes `base`
        # for them under a gate; here they are labelled for what they are.*
        if re.search(r'_cr_nk(15|20)$', t):
            print(f'  {t:42s} {"inert: = _cr_base":22s} NOT QUEUED')
            continue
        st = status(o, t)
        if st.startswith('complete') or st.split('/')[0] == st.split('/')[-1].split()[0]:
            pass
        r = load(o, t)
        done += r is not None
        print(f'  {t:42s} {st:22s} {"FOLDS" if r is not None else "-"}')
    print(f'\n  {done} of {len(seen)} started configuration(s) fold to a complete spectrum')
