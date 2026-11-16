"""r7812+cc66 (a1): the re-pointed control at LSTEP=2, run in RESUMABLE k-SLICES and assembled.

⛭ ** NO INSTRUMENT EDIT IS NEEDED, AND THAT FALSIFIES MY OWN REGISTERED (5d). **  I registered that
this would require editing `ACOUSTIC_two_arm.py`, moving its blob and reddening the two
`instrument_blob` receipts as `r7807+cc66.4` did.  ** The facility already exists. **  `KSLICE=lo:hi`
was built by `60` at `r6794`, at this node's own request, for exactly this reason -- its comment says
*"a run too long for its node can be done in PIECES AND ADDED"* -- and `C_l` is accumulated as
`Cl += _project(kb, ...)` over disjoint batches, so slices add to the whole exactly.
  ⇒ *The lesson is mine: I predicted a change to an instrument I had not finished reading.*

⛔ ** THE AUTHOR'S OWN CAVEAT, AND WHY IT DOES NOT BITE HERE -- CHECKED TWICE OVER. **  The note warns
that slices add exactly ONLY ON A UNIFORM k-GRID, because `_project` takes its measure as
`dk = np.gradient(kb)` from the BATCH it is handed; on CR's physical ladder the end differences
differ from the centred ones and the batch boundaries move the weights.
  ⑴ This run is `ARM=lcdm`, whose grid is `np.linspace(12.0, KMAXL, NK*3) / D_M` -- uniform, and the
    instrument prints one constant `dk = 1.127e-04` for it.  The ladder warning is `ARM == 'cr'` only.
  ⑵ AND the slice boundaries are multiples of `KBATCH`, so each slice's internal batching reproduces
    the straight run's batches EXACTLY -- every array handed to `_project` is the same array it would
    have been handed unsliced.  So the sum is exact even if ⑴ were ever to stop holding.
  ⇒ *Belt and braces on purpose: ⑴ is a property of today's grid, ⑵ is a property of the arithmetic.*

⛔ ** AND THE MODE COUNT IS ASKED OF THE INSTRUMENT, NOT HARDCODED -- A LESSON FROM THIS FILE'S OWN
FIRST VERSION. **  It hardcoded `2547`, the `LMAXL=2000` count, and used it for the `LMAXL=400`
exactness check too.  But the short configuration has `780` modes, so the first slice `0:1250` took
ALL of them and the second was EMPTY: a "partition" of one piece, which would have passed the
exactness check **vacuously** and told me nothing.  *A check that cannot fail is worse than no check,
and this one was two minutes from reporting a false green.*  So `modes_of()` reads the count from the
instrument's own header, and the edges are built from it.

IDEMPOTENT: a finished slice is skipped; a running solver is found by reading /proc/*/environ for
ACOUSTIC_two_arm, never by a bare pgrep name test.

Run: python3 run_sliced.py [--short | --lmaxl N]
       --short     the LMAXL=400 exactness check's slices
       --lmaxl N   any other reported multipole ceiling (r7815 runs N=1300 for `cc66_lcdm`)
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
INSTR = os.path.join(BW, 'ACOUSTIC_two_arm.py')

#: r7815: (a1) named TWO banks -- `cc66_lcdm` and `cc66_lcdm_L2000` -- and only the second was run
#: here at r7813.  `cc66_lcdm.npz` is 600 samples on 100..1298 step 2, i.e. LMAXL=1300, and P15's
#: `2.10` per bin on the 133-bin unlensed configuration reads it.  So LMAXL becomes a PARAMETER
#: rather than a third hardcoded branch beside `--short`: a boolean that has to grow a third value
#: is the shape of a tool that stops being readable, and nothing else here depends on LMAXL --
#: `modes_of()` already asks the instrument for the mode count at whatever LMAXL is set.
SHORT = '--short' in sys.argv
if '--lmaxl' in sys.argv:
    LMAXL = str(int(sys.argv[sys.argv.index('--lmaxl') + 1]))
else:
    LMAXL = '400' if SHORT else '2000'
OUT = os.path.join(HERE, 'out_short' if SHORT else
                   'out' if LMAXL == '2000' else f'out_L{LMAXL}')
os.makedirs(OUT, exist_ok=True)

#: r7807's point verbatim.  KFAC is NOT set, so the corpus default 2.0 applies exactly as it did
#: there -- naming it here would be a second copy of a number the instrument already owns.
PLANCK = dict(ARM='lcdm', LH0='67.36', LOM='0.313773', WBH2='0.02237', NS='0.9649',
              HIER='1', LSTEP='2', LMAXL=LMAXL)
KBATCH = 250
STEM = ('r7812_control_step2_short' if SHORT
        else f'r7812_control_step2_L{LMAXL}')
PIECE = 250 if SHORT else 750          # a multiple of KBATCH -- see ⑵ in the docstring


def modes_of():
    """the instrument's OWN mode count for this configuration, parsed from its header"""
    env = dict(os.environ, KSLICE='0:1', SAVE='/dev/null', **PLANCK)
    r = subprocess.run([sys.executable, '-u', INSTR], env=env, cwd=BW,
                       capture_output=True, text=True, timeout=900)
    m = re.search(r'modes\s*=\s*(\d+)', r.stdout)
    if not m:
        raise SystemExit('could not read the mode count from the instrument:\n'
                         + r.stdout[-1500:] + r.stderr[-1500:])
    return int(m.group(1))


def edges_for(n):
    e = list(range(0, n, PIECE))
    if e[-1] != n:
        e.append(n)
    return e


def already_running():
    mine = {os.getpid(), os.getppid()}
    for d in os.listdir('/proc'):
        if not d.isdigit() or int(d) in mine:
            continue
        try:
            env = open(f'/proc/{d}/environ', 'rb').read().decode('utf-8', 'replace')
        except (OSError, PermissionError):
            continue
        if 'ACOUSTIC_two_arm' in env and STEM in env:
            return int(d)
    return None


def main():
    n = modes_of()
    edges = edges_for(n)
    slices = [(edges[i], edges[i + 1]) for i in range(len(edges) - 1)]
    assert all(lo % KBATCH == 0 for lo, _ in slices), 'a slice boundary is not a KBATCH multiple'
    assert len(slices) >= 2, (f'{len(slices)} slice(s) for {n} modes is not a partition -- the '
                              f'exactness check would be vacuous')
    assert sum(hi - lo for lo, hi in slices) == n, 'the slices do not cover the mode set exactly'
    print(f'  the instrument reports {n} modes; {len(slices)} slice(s), boundaries {edges}')
    pid = already_running()
    if pid:
        print(f'  skip: a slice of this stem is already in flight at pid {pid}')
        return 0
    for lo, hi in slices:
        out = os.path.join(OUT, f'{STEM}_k{lo}_{hi}.npz')
        if os.path.exists(out):
            print(f'  skip {lo}:{hi} -- already banked')
            continue
        env = dict(os.environ, SAVE=out, KSLICE=f'{lo}:{hi}', **PLANCK)
        print(f'\n  === slice {lo}:{hi} -> {os.path.basename(out)}')
        r = subprocess.run([sys.executable, '-u', INSTR], env=env, cwd=BW)
        if r.returncode != 0:
            print(f'  slice {lo}:{hi} rc={r.returncode} -- stopping; re-run to resume')
            return r.returncode
    print('\n  all slices banked')
    return 0


if __name__ == '__main__':
    sys.exit(main())
