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
        if stem in NO_SPECTRUM:
            # ⌗ The SRCETA writer has its OWN key set and does not carry `config`; what it DOES carry
            #   is the same information under its own names, so that is what is checked here.
            ok = (str(z['path']) == 'HIER' and int(z['leafscales']) == 1
                  and float(z['taper']) == 0.0 and not bool(z['sliced']))
            check(f"{stem:<32} is the SRCETA save and records its own resolved switches instead of "
                  f"a config key: path {str(z['path'])}, leafscales {int(z['leafscales'])}, "
                  f"taper {float(z['taper']):g}, sliced {bool(z['sliced'])}", ok)
            have.append(stem)
            continue
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
            reads = []
            for k in shared:
                x, y = np.asarray(a[k], float).ravel(), np.asarray(b[k], float).ravel()
                if x.shape != y.shape:
                    reads.append((float('inf'), k + ' (shape)'))
                    continue
                reads.append((float((np.abs(x - y) / np.maximum(np.abs(y), 1e-300)).max()), k))
            worst, worstk = max(reads) if reads else (float('inf'), '(nothing compared)')
            nbit = sum(1 for r, _ in reads if r == 0.0)
            check(f"{stem:<32} has NO spectrum on either side -- the SRCETA save -- so it is "
                  f"compared on the {len(reads)} arrays it does carry: {nbit} bit-identical, "
                  f"worst at {worstk!r} {worst:.3e}",
                  worst < TOL and len(reads) >= 20)
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

    part3(cfg, have)

    print("\n" + "=" * 96)
    print(f"  {len(_fail)} failure(s)")
    for f in _fail:
        print("   [FAIL] " + f)
    sys.exit(1 if _fail else 0)


DIAG = os.path.join(HERE, 'diagnostics')


def rel_of(pa, pb):
    """max |a-b|/|b| on D_l, and whether the two are bit-identical."""
    a, b = load(pa), load(pb)
    if not np.array_equal(a['ls'], b['ls']):
        return float('inf'), False
    x, y = np.asarray(a['Dl'], float), np.asarray(b['Dl'], float)
    return float((np.abs(x - y) / np.maximum(np.abs(y), 1e-300)).max()), np.array_equal(x, y)


def part3(cfg, have):
    """** THE ORDER'S SECOND BRANCH: name the instrument change behind each difference. **

    Both answers have the SAME SHAPE, and it is the shape the instrument's own source already names
    for another switch: *a switch reached one path of three.*  A switch that was inert on the path a
    file was banked on, and is live there now, makes the banked file a run of the command WITHOUT it
    -- so the file's NAME claims a switch its contents do not carry, and the old -> new diff carries
    the switch's whole effect on top of the arm's.
    """
    S, R = SPEC, REBUILT
    print("\nPART 3 -- NAMING THE CHANGE BEHIND EACH DIFFERENCE, WHICH IS THE ORDER'S SECOND BRANCH")

    print("\n  ⓐ r6885_dp0_cr -- THE DOPPLER-DIPOLE SWITCH DID NOT REACH THE HIERARCHY PATH.")
    plain = 'cc66_r185_verify_cr'          # the identical command WITHOUT the switch
    if plain in have and 'r6885_dp0_cr' in have:
        r1, b1 = rel_of(os.path.join(S, 'r6885_dp0_cr.npz'), os.path.join(S, plain + '.npz'))
        r2, b2 = rel_of(os.path.join(S, 'r6885_dp0_cr.npz'), os.path.join(R, plain + '.npz'))
        r3, _ = rel_of(os.path.join(R, 'r6885_dp0_cr.npz'), os.path.join(R, plain + '.npz'))
        check("the namesake is BIT-IDENTICAL to the namesake of the same command WITHOUT the "
              "switch, so the switch did nothing at its build", b1)
        check(f"and BIT-IDENTICAL to TODAY's run of that switch-free command, so what moved is the "
              f"switch and not the rest of the instrument", b2)
        check(f"while TODAY the switch changes that spectrum by {r3:.3e} -- the whole of the "
              f"difference the census measured", r3 > 1e-3)
        lo, _ = rel_of(os.path.join(S, 'r6885_losdp0_cr.npz'), os.path.join(S, 'r6885_los_cr.npz'))
        ln, _ = rel_of(os.path.join(R, 'r6885_losdp0_cr.npz'), os.path.join(R, 'r6885_los_cr.npz'))
        check(f"⛭ AND THE CONTROL SAYS IT IS THE PATH AND NOT THE SWITCH: on the LINE-OF-SIGHT path "
              f"the same switch was already live at the build and is live now, to the same figure "
              f"({lo:.3e} then, {ln:.3e} now)", abs(lo - ln) < 1e-6 and lo > 1e-3)
    src = open(os.path.join(BTW, 'ACOUSTIC_two_arm.py')).read()
    check("⇒ and the instrument's own source NAMES the commit: `_SWSRC` and `_DPSRC` wired on the "
          "hierarchy path at r6889+cc66.36", '`_SWSRC` AND `_DPSRC` WIRED HERE AT r6889+cc66.36' in src)
    check("⇒ and names the measurement this census just reproduced: DPSRC=0 on that path "
          "'returned a BIT-IDENTICAL spectrum on both arms (r6885+cc66.35)'",
          'returned a BIT-IDENTICAL spectrum on both arms (r6885+cc66.35)' in src)

    print("\n  ⓑ r6784_cr_crossing_los -- THE INITIAL-CONDITION SWITCH DID NOT REACH THE "
          "LINE-OF-SIGHT PATH.")
    nd = os.path.join(DIAG, 'r6784_cr_crossing_los__noCRIC.npz')
    if os.path.exists(nd) and 'r6784_cr_crossing_los' in have:
        r1, b1 = rel_of(nd, os.path.join(S, 'r6784_cr_crossing_los.npz'))
        r2, _ = rel_of(os.path.join(R, 'r6784_cr_crossing_los.npz'),
                       os.path.join(S, 'r6784_cr_crossing_los.npz'))
        check("the namesake is BIT-IDENTICAL to TODAY's run of its own command WITH THE SWITCH "
              "REMOVED, so the switch did nothing on this path at its build", b1)
        check(f"while its command WITH the switch misses the namesake by {r2:.3e}", r2 > 1e-3)
        rh, _ = rel_of(os.path.join(R, 'r6784_cr_crossing_hier.npz'),
                       os.path.join(S, 'r6784_cr_crossing_hier.npz'))
        check(f"⛭ AND THE CONTROL IS THE SAME GROUP'S HIERARCHY MEMBER, which carries the SAME "
              f"switch and reproduces at {rh:.3e}: so the switch was live THERE at the build",
              rh < TOL)
        ca, _ = rel_of(os.path.join(S, 'r6784_cr_crossing_hier.npz'),
                       os.path.join(S, 'r6784_cr_crossing_hier_noCRIC.npz'))
        cb, _ = rel_of(os.path.join(R, 'r6784_cr_crossing_hier.npz'),
                       os.path.join(R, 'r6784_cr_crossing_hier_noCRIC.npz'))
        check(f"⇒ and the switch's own ACTION did not change -- with against without, on the path "
              f"that had it, is {ca:.3e} then and {cb:.3e} now. ** What changed is its REACH. **",
              abs(ca - cb) < 1e-9 and ca > 1e-3)

    print("\n  ⓒ WHAT IS MEASURED AND NOT NAMED, SAID RATHER THAN LEFT OUT")
    print("  *Two differences remain, both on the hierarchy path, both small, and neither is named")
    print("  to a commit here.  The search: the three switches the two named findings implicate were")
    print("  each tested against their own controls above; the instrument's source carries no note")
    print("  with a revision after r6784 describing a change to the hierarchy's CR handover; and the")
    print("  clone is shallow, so history cannot be asked.  Reported as unlocated, with the files")
    print("  and the figures, rather than attributed to the nearest story.*")
    for stem in ('r6784_cr_crossing_hier_noCRIC', 'r6794_cr_crossing_kcont_summed'):
        if stem in have:
            r, _ = rel_of(os.path.join(R, stem + '.npz'), os.path.join(S, stem + '.npz'))
            extra = NEEDS_PROCEDURE.get(stem, '')
            print(f"      {stem:<32} {r:.3e}" + (f"\n        ⚠ {extra}" if extra else ""))
    check("⌗ and both are on the hierarchy path with the initial-condition switch UNSET, which is "
          "the one combination the two named findings do not cover",
          cfg['r6784_cr_crossing_hier_noCRIC'].get('CRIC') is None
          and cfg['r6794_cr_crossing_kcont_summed'].get('CRIC') is None
          and cfg['r6784_cr_crossing_hier_noCRIC'].get('HIER') == '1')


if __name__ == '__main__':
    main()
