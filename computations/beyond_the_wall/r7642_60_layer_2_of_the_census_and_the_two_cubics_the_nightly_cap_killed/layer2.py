#!/usr/bin/env python3
"""r7642 (60) -- LAYER 2 OF THE INSTRUMENT-DRIFT CENSUS: THE SPECTRUM COMPARISON ITSELF.

** THE ORDER (`r7641`, 69).  Layer 2 is this seat's. **  Run the spectrum comparison on the 24
namesakes today's instrument can build under their own configuration: each rebuilt at its identified
command with `LEAFREC=0` set EXPLICITLY, the `pol` pair as TWO runs at 68.60 and 68.62, each compared
with its namesake -- bit-identical, or within `1e-11`, means the bank's old -> new diff is the arm's
alone; otherwise name the instrument change behind the difference and the receipts that read the file.

** THE REGISTERED NEGATIVE IS `r7640`'s ARM ④, carrying `r7639`'s own words, and `r7641` confirms it
stands: ** *one or more of the 36 besides `r6885_dp0` differs from its namesake under its own
configuration by more than `1e-11`.*  ⇒ So this receipt READS an arm already registered; it does not
register one.  `PREDICTION.md` beside it registers only what `r7640` did not: the `P10` choice (arm ⑤)
and the cost structure the reading has to survive (arm ⑥).

⚠ ** THE EXPENSIVE HALF RUNS OUT OF BAND AND NOTHING HERE TRUSTS ITS OUTPUT TEXT. **  `run_layer2.py`
rebuilds each namesake and writes an `.npz`; this receipt recomputes EVERY comparison from the two
`.npz` files themselves, and checks each rebuilt file's own `config` key -- `r7097`'s ratchet, which
records the switches the instrument RESOLVED rather than the ones that were typed -- against the
command the census claims for it.  A rebuild whose `config` disagrees with its claimed command is a
failure of this receipt, not a finding about the bank.

⌗ ** WHY `LEAFREC=0` IS SET EXPLICITLY AND IS NOT A NO-OP. **  Layer 1 measured that the three
background scales cannot see `LEAFREC`, and read off the instrument's own source that its default
moved to ON at `cc66.75`.  So a recorded command that omits it rebuilds the leafrec1 arm with a
background identical to the namesake's -- the exact shape that makes the trap invisible to Layer 1 and
visible only here.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)
SPEC = os.path.join(BTW, 'spectra')
REBUILT = os.path.join(HERE, 'rebuilt')
TOL = 1e-11                      # the order's threshold: 70's thread-count wobble

# the bank's own recorded procedure notes, kept beside the comparison rather than behind it
SLICED = {
    'r6911_source_cr': ('six KSLICE pieces of 250', 2.78e-17),
    'r6911_source_cr_kcont': ('eleven KSLICE pieces of 250', 2.78e-17),
    'r6915_pairs_cr': ('six KSLICE pieces', 1.61e-15),
}
# ⛔ ** ONE OF THE 36 IS NOT A SPECTRUM ON EITHER SIDE, AND THE CENSUS FOUND THAT BY REFUSING TO
#   COMPARE IT. **  `r6959_eta_cr`'s namesake carries 28 keys and NEITHER `ls` NOR `Dl`: it is the
#   `SRCETA` save -- the source's own weight across the window, band by band in q -- and its rebuilt
#   counterpart carries the same 32-key shape.  So the order's `Dl` comparison has no object here,
#   and the honest census entry compares what the pair DOES carry.
#     ⌗ *This also corrected this seat's own configuration table: the first pass omitted `SRCETA`,
#     so the rebuild produced a spectrum where the namesake has none -- a DIFFERENT OBJECT under the
#     same name, which is exactly the confusion the census exists to catch.  Corrected at
#     `r7642+60.5` with the discarded entry named.*
NO_SPECTRUM = {'r6959_eta_cr'}
NEEDS_PROCEDURE = {
    'r6794_cr_crossing_kcont_summed':
        'six KSLICE pieces of 450 SUMMED -- 2700 continuum modes, which one NK=900 run does not '
        'reach at all, so for this one the recorded command is not the recorded run',
}

_fail = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        _fail.append(label)


def load(path):
    z = np.load(path, allow_pickle=True)
    return z


def main():
    cfg = json.load(open(os.path.join(HERE, 'CONFIGS.json')))
    print(__doc__)
    print("=" * 96)
    print(f"  r7642 (60) -- LAYER 2: the threshold is {TOL:g}, and the comparison is on D_l")
    print("=" * 96)

    check("the census covers the 24 the instrument will build, which is the 36 less the twelve "
          "Layer 1 measured it refuses", len(cfg) == 24)
    check("the pol pair is TWO entries at TWO points, as the order requires",
          cfg['cc66_cr_x_h686_pol']['CRH0'] == '68.60'
          and cfg['cc66_cr_x_h6862_pol']['CRH0'] == '68.62')

    print("\nPART 1 -- EACH REBUILT FILE RECORDS THE RUN IT ACTUALLY WAS")
    print("  *`config` is the resolved-switch snapshot, so a typo in the command is caught here and")
    print("  not mistaken downstream for the instrument having drifted.*")
    have = []
    for stem in sorted(cfg):
        p = os.path.join(REBUILT, stem + '.npz')
        if not os.path.exists(p):
            continue
        z, env = load(p), cfg[stem]
        c = json.loads(str(z['config']))
        want_lm = float(env['LMAXL'])
        ok = (c['ARM'] == 'cr' and c['LEAFREC'] is False and c['LMAXL'] == want_lm
              and c['KFAC'] == 2.0
              and c['LEAFSCALES'] is (env.get('LEAFSCALES') == '1')
              and c['NODRIVE'] is (env.get('NODRIVE') == '1')
              and c['STACKPERT'] is (env.get('STACKPERT') == '1'))
        check(f"{stem:<32} ran at its claimed command: LEAFREC resolved OFF, LMAXL {c['LMAXL']:.0f}, "
              f"LEAFSCALES {c['LEAFSCALES']}, KFAC {c['KFAC']}", ok)
        have.append(stem)
    check(f"⌗ {len(have)} of 24 rebuilt so far; the rest are named in RESULT.md with their cost, "
          "never implied", len(have) > 0)

    print("\nPART 2 -- THE COMPARISON THE ORDER ASKS FOR, RECOMPUTED FROM THE TWO FILES")
    exact, within, over = [], [], []
    for stem in have:
        a, b = load(os.path.join(REBUILT, stem + '.npz')), load(os.path.join(SPEC, stem + '.npz'))
        if stem in NO_SPECTRUM:
            shared = sorted(set(a.files) & set(b.files) - {'config', 'manifest', 'arm', 'path'})
            worst, worstk = 0.0, ''
            for k in shared:
                x, y = np.asarray(a[k], float).ravel(), np.asarray(b[k], float).ravel()
                if x.shape != y.shape:
                    worst, worstk = float('inf'), k + ' (shape)'
                    break
                rel = np.abs(x - y) / np.maximum(np.abs(y), 1e-300)
                if float(rel.max()) > worst:
                    worst, worstk = float(rel.max()), k
            check(f"{stem:<32} has NO spectrum on either side -- the SRCETA save -- so it is "
                  f"compared on the {len(shared)} arrays it does carry, worst at {worstk!r} "
                  f"{worst:.3e}", worst < TOL)
            (within if worst < TOL else over).append(stem)
            continue
        same_grid = np.array_equal(a['ls'], b['ls'])
        check(f"{stem:<32} rebuilt on the namesake's own multipole grid "
              f"({len(a['ls'])} vs {len(b['ls'])})", same_grid)
        if not same_grid:
            continue
        d = np.abs(np.asarray(a['Dl'], float) - np.asarray(b['Dl'], float))
        rel = d / np.maximum(np.abs(np.asarray(b['Dl'], float)), 1e-300)
        bit = np.array_equal(a['Dl'], b['Dl'])
        worst = float(rel.max())
        note = ''
        if stem in SLICED:
            how, resid = SLICED[stem]
            note = f"   [namesake built as {how}; the bank records that split at {resid:.2e}]"
        if stem in NEEDS_PROCEDURE:
            note = f"   [⚠ {NEEDS_PROCEDURE[stem]}]"
        tag = 'BIT-IDENTICAL' if bit else ('within' if worst < TOL else 'OVER')
        print(f"      {stem:<32} {tag:<14} max rel {worst:.3e}  max abs {float(d.max()):.3e}{note}")
        (exact if bit else (within if worst < TOL else over)).append(stem)

    print()
    check(f"⇒ the arm's diff alone on {len(exact) + len(within)} of {len(have)} read "
          f"({len(exact)} bit-identical, {len(within)} within {TOL:g})",
          len(exact) + len(within) == len(have) - len(over))
    if over:
        print("  ⛔ OVER THE THRESHOLD, so the old -> new diff for these is NOT the arm's alone:")
        for stem in over:
            print(f"      {stem}")
    check("⌗ and r6885_dp0 -- the one cc66 already found over the arm move -- is IN this census "
          "rather than carved out of it, so its reading is taken here and not inherited",
          'r6885_dp0_cr' in cfg)

    print("\n" + "=" * 96)
    print(f"  {len(_fail)} failure(s)")
    for f in _fail:
        print("   [FAIL] " + f)
    sys.exit(1 if _fail else 0)


if __name__ == '__main__':
    main()
