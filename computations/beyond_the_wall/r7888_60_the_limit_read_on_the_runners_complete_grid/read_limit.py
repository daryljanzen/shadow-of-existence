# -*- coding: utf-8 -*-
"""r7888+60 — THE LIMIT READ ON THE RUNNER'S COMPLETE GRID.

Order `r7885` (69) item ②.  `refs/ci/r7884_phiphi` carries all ten lensing points from `70`'s run.
This reads the control's limits on the closed envelope **as registered at `r7884`**, on that grid.

⛔ **NOTHING IS RETYPED.**  `r7884`'s `limits_nuhier.py` is imported whole and only its `NEW_PP`
source directory is redirected at the ref's points, before its assembly runs.  Its assembly, its five
plumbing gates `Ⓛ⓵`–`Ⓛ⓹`, its carried nodes and both envelope reads are untouched.  `r7886`'s
`verify_grid.py` closures are run as themselves, not reimplemented.

⛔ **AND THE TWO GRIDS ARE NOT MIXED.**  This checkout's own points are used ONLY as the cross-machine
control.  They are never an input to the limit.  Filling the ref's grid from the local bank, or the
local bank from the ref, would make a grid whose points came from two machines with nothing in the
record saying which came from where.

    python3 read_limit.py [--grid DIR] [--no-limit]

With no `--grid` the ten points are extracted from the ref, which is fetched if it is not present.
`--no-limit` runs this revision's own gates and stops before `r7884`'s read, which is how the gates
were checked without spending the read.
"""
import argparse
import io
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
#: ⛭ the repository root, ASKED FOR rather than counted up with `dirname`.  Counting levels got it
#:   wrong by one (it landed on `computations/`) and the archive came out empty a second time -- the
#:   guard below caught that too, but a path derived by arithmetic over a layout is a pin on the
#:   layout, and `git` already knows the answer.
ROOT = (subprocess.run(['git', 'rev-parse', '--show-toplevel'], cwd=HERE,
                       capture_output=True, text=True).stdout.strip()
        or os.path.dirname(os.path.dirname(BTW)))
R7884 = os.path.join(BTW, 'r7884_60_the_controls_limits_on_the_jointly_validated_sector')
R7886 = os.path.join(BTW, 'r7886_60_the_lensing_grid_launch_for_the_runner')
LOCAL = os.path.join(BTW, 'bank', 'phiphi_grid_eta4000_bvel1_primnorm1_nuhier')

REF = 'refs/ci/r7884_phiphi'
#: the ref, the run and the commit the ORDER pointed at.  A grid that is not these is not the grid.
REF_COMMIT = '133e612fe'
RUN_ID = '46016816497'
RUN_SHA = '46f824c2feba35951268316528e843d19c849200'
ARMS = ('lcdm', 'cr')
TAGS = ('S006', 'S015', 'S030', 'S045', 'S060')

FAILS = []


def gate(name, ok, got=None):
    print('  [%s] %s%s' % ('PASS' if ok else 'FAIL', name,
                           ('   (%s)' % got) if got is not None else ''))
    if not ok:
        FAILS.append(name.split()[0])
    return ok


def _git(*a):
    return subprocess.run(('git',) + a, cwd=BTW, capture_output=True, text=True)


def fetch_grid(dest):
    """extract the ref's points, fetching the ref if this checkout does not carry it"""
    local_ref = 'refs/remotes/ci/r7884_phiphi'
    if not _git('rev-parse', '--verify', '--quiet', local_ref).stdout.strip():
        print('  fetching %s ...' % REF)
        r = _git('fetch', 'origin', '%s:%s' % (REF, local_ref))
        if r.returncode:
            sys.exit('  ⛔ cannot fetch %s: %s' % (REF, r.stderr.strip()[:200]))
    os.path.isdir(dest) or os.makedirs(dest)
    #: ⛔ `git archive` RESOLVES THE TREE AT THE CURRENT DIRECTORY'S PATH INSIDE THE REPOSITORY, so
    #:   run from a subdirectory it archives that subdirectory of the tree -- and the ci ref's tree has
    #:   no such subdirectory, so the archive came out EMPTY (10240 bytes, pure tar padding) and this
    #:   directory extracted ZERO points.  Run from the repository ROOT.  ⌗ *The gates below caught it
    #:   and REFUSED rather than reading a limit off an empty grid, which is what they are for; but the
    #:   extraction itself has to be checked, because a silently empty source is the same shape of
    #:   defect as a gate that counts what is not there.*
    tar = subprocess.Popen(['git', 'archive', local_ref], cwd=ROOT, stdout=subprocess.PIPE)
    subprocess.run(['tar', '-x', '-C', dest], stdin=tar.stdout, check=True)
    tar.wait()
    if tar.returncode:
        sys.exit('  ⛔ git archive %s failed with %d' % (local_ref, tar.returncode))
    n = len([f for f in os.listdir(dest) if f.endswith('.json')])
    if n < 2 * len(TAGS):
        sys.exit('  ⛔ extracted only %d json file(s) from %s into %s -- the source is EMPTY or '
                 'partial, and no gate below should be asked to interpret that' % (n, local_ref, dest))
    print('  extracted %d json file(s) from %s' % (n, local_ref))
    return dest


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument('--grid', default=None)
    ap.add_argument('--no-limit', action='store_true')
    a = ap.parse_args(argv[1:])

    print(__doc__)
    print('=' * 100)
    grid = a.grid or fetch_grid(os.path.join(HERE, '_ref_grid'))
    print('  grid read   : %s' % grid)
    print('  control     : %s' % LOCAL)

    # ══ Ⓡ⓵ THE GRID IS THE RUNNER'S, AND THE ONE THE ORDER POINTED AT ═══════════════════════════
    print('\nⓇ⓵  THE GRID IS THE ONE THE ORDER POINTED AT, READ OFF THE POINTS\' OWN SIDECARS')
    runs, shas, bad1 = set(), set(), []
    for arm in ARMS:
        for tag in TAGS:
            p = os.path.join(grid, '%s_%s.timing.json' % (arm, tag))
            if not os.path.isfile(p):
                bad1.append('%s_%s has no timing sidecar' % (arm, tag))
                continue
            t = json.load(io.open(p, encoding='utf-8'))
            runs.add(str(t.get('run_id')))
            shas.add(str(t.get('sha')))
    gate('Ⓡ⓵ every one of the ten points records the SAME runner run and the SAME launch commit, and '
         'they are the run and commit the order named -- so this is not a grid assembled from '
         'several runs, and not a different grid wearing the right name',
         not bad1 and runs == {RUN_ID} and shas == {RUN_SHA},
         '; '.join(bad1[:3]) if bad1 else 'run %s, sha %s' % (sorted(runs), sorted(s[:12] for s in shas)))

    head = _git('rev-parse', '--short', 'refs/remotes/ci/r7884_phiphi').stdout.strip()
    gate('Ⓡ⓶ and the ref this checkout read is at the commit the order named',
         bool(head) and REF_COMMIT.startswith(head) or head.startswith(REF_COMMIT[:9]),
         'ref at %s, expected %s' % (head or None, REF_COMMIT))

    # ══ Ⓡ⓷ r7886's OWN CLOSURES, RUN AS THEMSELVES ══════════════════════════════════════════════
    print('\nⓇ⓷  r7886\'s FIVE CLOSURES, RUN AS THEMSELVES ON THIS GRID (not reimplemented here)')
    r = subprocess.run([sys.executable, os.path.join(R7886, 'verify_grid.py'), grid,
                        '--ref', LOCAL], capture_output=True, cwd=BTW)
    out = r.stdout.decode('utf-8', 'replace')
    for ln in out.splitlines():
        if '[PASS]' in ln or '[FAIL]' in ln or ln.strip().startswith('⚠'):
            print('   ', ln.strip()[:150])
    import re
    st = re.search(r'=> (Ⓒ⓸[^\n)]*)', out)
    worst = re.search(r'worst relative ([0-9.e+-]+)', out)
    gate('Ⓡ⓷ all five closures PASS on the runner\'s grid -- complete, provenanced, the right shape, '
         'inside the registered cross-machine bar, and the frozen list undrifted',
         r.returncode == 0, 'verify_grid rc=%d' % r.returncode)
    gate('Ⓡ⓸ ⛔ and the cross-machine control is reported in its REGISTERED state rather than as a '
         'pass -- the agreement is NOT zero, and a single refuse bar would have said it was',
         st is not None and worst is not None,
         '%s; worst %s' % (st.group(1).strip() if st else None, worst.group(1) if worst else None))

    if FAILS:
        sys.exit('\n  ⛔ %d GATE(S) FAILED: %s\n     ** NO LIMIT IS READ. The grid is not established '
                 'as the one the order pointed at, so a number read off it would not be the '
                 'ordered measurement. **' % (len(FAILS), ', '.join(FAILS)))
    print('\n  ⇒ all %d gate(s) pass, so the ordered grid is established and the read may proceed'
          % (4,))

    if a.no_limit:
        print('\n  ⌗ --no-limit: stopping BEFORE r7884\'s read, as registered.')
        return 0

    # ══ r7884's READ, IMPORTED WHOLE, WITH ONLY ITS SOURCE REDIRECTED ════════════════════════════
    print('\n' + '=' * 100)
    print('  r7884\'s limits_nuhier.py, imported whole; only NEW_PP is redirected at this grid.')
    print('=' * 100)
    sys.path.insert(0, R7884)
    import limits_nuhier as L
    assert os.path.realpath(L.NEW_PP) == os.path.realpath(LOCAL), (
        '⛔ r7884\'s NEW_PP is not the local bank any more; the redirect below would be silent')
    L.NEW_PP = grid                      #: ⛔ the ONLY change, and it is a source directory
    return L.main()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
