#!/usr/bin/env python3
"""r7642 (60) -- THE LAYER-2 RUNNER: rebuild each namesake at ITS OWN configuration, one at a time.

** This is the out-of-band half, and only the expensive half. **  It runs today's instrument once per
namesake at the command `r7640` identified for it, with `LEAFREC=0` set EXPLICITLY -- which is the
point, because the default moved at `cc66.75` and a recorded command that omits it rebuilds the other
arm.  Each run writes its own `.npz`, and every one carries the `config` key `r7097`'s ratchet writes,
so the artefact records what the run DID rather than what was typed.

⚠ ** THE COMPARISON IS NOT MADE HERE. **  `layer2.py` recomputes every diff from the two `.npz` files
themselves, so nothing downstream trusts a number this script printed.

⌗ Cost order, cheapest first, as `r7642`'s arm ⑥ registers: `LMAXL` 1300 before 2000, and inside each
  the coarser `LSTEP` first.  ** MEASURED: the cheapest family takes 639 s standing alone **, so the
  24 do not fit in one serial pass and `JOBS` runs several at once.
⚠ ** EVERY RUN IS PINNED TO ONE THREAD (`OMP`/`OPENBLAS`/`MKL` = 1) WHETHER OR NOT `JOBS` > 1, and
  that is what makes the parallelism safe here: ** the census threshold is `1e-11`, which is the
  thread-count wobble `70` gated, so a run whose thread count changed under contention would be
  measuring the wobble rather than the instrument.  Pinned, the arithmetic is the same at `JOBS` 1 and
  4 and only the wall time moves.  *The order asks the two seats to coordinate machine load: this
  claims one container and no runner.*
"""
import concurrent.futures as cf
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
INSTR = os.path.join(BTW, 'ACOUSTIC_two_arm.py')
OUT = os.path.join(HERE, 'rebuilt')
LOG = os.path.join(HERE, 'runs')
CFG = json.load(open(os.path.join(HERE, 'CONFIGS.json')))

# the recorded per-file procedure notes that bear on whether ONE run reproduces the namesake
SLICED = {
    'r6911_source_cr': 'six KSLICE pieces of 250; the bank records the split residual at 2.78e-17',
    'r6911_source_cr_kcont': 'eleven KSLICE pieces of 250; split residual 2.78e-17',
    'r6915_pairs_cr': 'six KSLICE pieces; the bank records the pairs closing on D_l to 1.61e-15',
    'r6794_cr_crossing_kcont_summed': 'SIX KSLICE PIECES OF 450 SUMMED -- 2700 continuum modes, which '
                                      'one NK=900 run does NOT reach, so this one needs the procedure '
                                      'and not the command',
}


def cost_key(item):
    stem, env = item
    return (int(float(env['LMAXL'])), -int(env.get('LSTEP', '99')), int(env.get('NK', '0')), stem)


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(LOG, exist_ok=True)
    budget = float(os.environ.get('RUN_BUDGET', '5400'))     # per run, seconds
    only = os.environ.get('ONLY', '')
    jobs = int(os.environ.get('JOBS', '1'))
    order = sorted(CFG.items(), key=cost_key)
    todo = [(s, e) for s, e in order
            if (not only or only in s) and not os.path.exists(os.path.join(OUT, s + '.npz'))]
    print(f"  LAYER-2 RUNNER -- {len(todo)} of {len(order)} namesake(s) left, cheapest first, "
          f"{budget:.0f}s each, {jobs} at a time, ONE THREAD each\n", flush=True)
    if jobs > 1:
        with cf.ThreadPoolExecutor(max_workers=jobs) as pool:
            for line in pool.map(lambda it: one(it[0], it[1], budget), todo):
                print(line, flush=True)
        return
    for stem, env in todo:
        print(one(stem, env, budget), flush=True)


def one(stem, env, budget):
    """Run ONE namesake at its identified command and return the report line."""
    npz = os.path.join(OUT, stem + '.npz')
    e = dict(os.environ)
    for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
        e[k] = '1'
    e.update({'ARM': 'cr', 'LEAFREC': '0'})
    e.update(env)
    e['SAVE'] = npz
    for k in ('ONLY', 'RUN_BUDGET', 'JOBS'):
        e.pop(k, None)
    note = SLICED.get(stem)
    t0 = time.time()
    with open(os.path.join(LOG, stem + '.log'), 'w') as fh:
        try:
            rc = subprocess.run([sys.executable, INSTR], env=e, cwd=BTW,
                                stdout=fh, stderr=subprocess.STDOUT,
                                timeout=budget).returncode
        except subprocess.TimeoutExpired:
            rc = 'TIMEOUT'
    dt = time.time() - t0
    return (f"  [{stem}]  LMAXL={env['LMAXL']} LSTEP={env.get('LSTEP', '-')} "
            f"NK={env.get('NK', 'auto')}  ->  rc={rc}  {dt:.0f}s  "
            f"{'saved' if os.path.exists(npz) else 'NO FILE'}"
            + (f"\n       ⚠ {note}" if note else ""))


if __name__ == '__main__':
    main()
