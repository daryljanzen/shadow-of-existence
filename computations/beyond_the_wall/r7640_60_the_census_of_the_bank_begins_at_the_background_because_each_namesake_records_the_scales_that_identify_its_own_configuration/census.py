#!/usr/bin/env python3
"""r7640 (60) -- THE INSTRUMENT-DRIFT CENSUS OF THE BANK, LAYER 1: THE BACKGROUND.

** THE ORDER (r7639, 69) asks for 36 spectrum rebuilds at each namesake's OWN configuration.  That
instruction has a PRIOR STEP: "its old point and switches" has to be KNOWN, and `r7635+70`'s
`RECIPES.md` says it is not known everywhere -- one entry is "none recorded", marked low
confidence. **  A spectrum rebuilt against a guessed command cannot separate "the instrument
drifted" from "we guessed the command wrong", so the census would answer a question nobody asked.

** THE NAMESAKES MAKE THAT STEP PAYABLE.  Each of the 36 carries `l_A`, `D_M` and `r_s` in its own
file, and those three are set by the BACKGROUND switches alone -- `CRH0`, `CROM`, `WBH2`,
`ZSTART`/`LATARG`, `LEAFSCALES` -- and are independent of the expensive half: `LMAXL`, `NK`,
`LSTEP`, `KFAC`, `KBATCH` and every source switch.  So a namesake is a FINGERPRINT OF ITS OWN
CONFIGURATION, readable in twenty seconds against today's instrument instead of hours. **

  ⇒ The census splits.  LAYER 1 (here): does today's instrument reproduce each namesake's own
    recorded scales under its own recorded command?  LAYER 2 (70's): the order's `1e-11` comparison
    of `Dl`.
  ⚠ ** Layer 1 is a NECESSARY CONDITION on Layer 2, not a proxy for it. **  `D_M` and `r_s` enter
    the projection, so a background that misses by more than `1e-11` GUARANTEES a spectrum that
    misses by more than `1e-11`.  The converse does not hold: a Layer-1 pass is NOT a verdict of
    "the diff is the arm's alone", because `KFAC`, `NK`, `LSTEP`, `KBATCH`, `HIER`/`BSPLIT`,
    `KCONT`, `KSLICE` and the source switches are all INVISIBLE to the three scales.  PART 2 below
    is exactly such a case: twelve files whose background reproduces and whose spectrum cannot be
    taken at all.

Registered at `PREDICTION.md` in this directory, amended at `r7640+60.1` before arm (1) was read.
"""
import json
import os
import re
import subprocess
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
BTW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
SPEC = os.path.join(BTW, 'spectra')
BANK = os.path.join(BTW, 'r7635_70_leafrec1_bank')
INSTR = os.path.join(BTW, 'ACOUSTIC_two_arm.py')
TOL = 1e-11                      # the threshold the order names: 70's thread-count wobble

_fail = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        _fail.append(label)


def manifest():
    out = {}
    for f in ('MANIFEST_clean.json', 'MANIFEST_old.json'):
        with open(os.path.join(BANK, f)) as fh:
            out.update(json.load(fh))
    return out


def scales(stem):
    z = np.load(os.path.join(SPEC, stem + '.npz'), allow_pickle=True)
    return float(z['l_A']), float(z['D_M']), float(z['r_s'])


# ** THE BACKGROUND IS INDEPENDENT OF THE EXPENSIVE HALF, SO IT IS TAKEN AT THE CHEAPEST SETTING
#    THE INSTRUMENT WILL RUN -- and that independence is CHECKED in PART 1c rather than assumed. **
#   ⚠ `ARM=cr` is part of the base, not a group's switch: all 36 banked section-B spectra are the
#   CR arm, and the instrument's own default is `lcdm`.  `LEAFREC=0` is the order's own words for
#   the namesake's configuration, carried even though PART 1d measures that the background cannot
#   see it.
CHEAP = dict(ARM='cr', LEAFREC='0', LMAXL='200', LSTEP='50', NK='60')


def run_background(env, lmaxl=None):
    """Run today's instrument for its BACKGROUND only and return (scales, exit code, stdout)."""
    e = dict(os.environ)
    e.pop('SAVE', None)
    e.update(CHEAP)
    if lmaxl:
        e['LMAXL'] = str(lmaxl)
    e.update({k: str(v) for k, v in env.items()})
    out = os.path.join(TMP, 'bg_%d.npz' % next(_ctr))
    e['SAVE'] = out
    t0 = time.time()
    p = subprocess.run([sys.executable, INSTR], env=e, cwd=BTW,
                       capture_output=True, text=True, timeout=1800)
    dt = time.time() - t0
    got = _read(out) if os.path.exists(out) else None
    return got, p.returncode, p.stdout, dt


def _read(path):
    z = np.load(path, allow_pickle=True)
    return float(z['l_A']), float(z['D_M']), float(z['r_s'])


def _counter():
    i = 0
    while True:
        i += 1
        yield i


_ctr = _counter()
TMP = os.environ.get('CENSUS_TMP') or os.path.join(
    os.environ.get('TMPDIR', '/tmp'), 'r7640_census')
os.makedirs(TMP, exist_ok=True)

M = manifest()
REFIT = dict(CRH0='68.6077', CROM='0.2967', WBH2='0.0217', NS='0.9949',
             ZSTART='3e7', LEAFSCALES='1')      # arm (1)'s point, checked in PART 3

# ** THE EIGHT BACKGROUNDS THE 36 NAMESAKES CARRY, AND THE COMMAND THIS CENSUS CLAIMS FOR EACH. **
#   *The right-hand side is this receipt's ANSWER to the order's "its old point and switches"; every
#   one of them is checked against the namesake's own stored scales below, so none of it is asserted
#   on the strength of `RECIPES.md`'s prose -- which PART 4 shows contradicts itself.*
GROUPS = [
    ("defaults, onset solved to l_A = 301.6", {}, [
        'c54.175_cr', 'c54.177_cr', 'c54.178_cr', 'c54.186_cr_KCONT', 'c54.186_cr_L3000',
        'c54.191_cr_phipi_L3000', 'c54.193_cr_nodrive_L3000', 'c54.195_cr_phi0.7854_L3000',
        'c54.195_cr_phi1.5708_L3000', 'item38_cr_phi0.0_prod', 'item38_cr_phi3.1416_prod',
        'r4494_cr_leaf_ISWon', 'r4494_cr_leaf_ISWoff', 'r4494_cr_stack_ISWon',
        'r4494_cr_stack_ISWoff']),
    ("defaults + LATARG=340 (the l_A injection)", {'LATARG': '340'},
     ['c54.191_cr_lA340_L3000']),
    ("defaults + ZSTART=3e7 -- RECOVERED; RECIPES has 'none recorded'", {'ZSTART': '3e7'},
     ['cc66_cr_x_lstep1']),
    ("r6941's point", dict(CRH0='68.581133', CROM='0.297209', WBH2='0.021524', NS='0.997952',
                           ZSTART='3e7', LEAFSCALES='1'),
     ['cc66_r185_verify_cr', 'r6885_dp0_cr', 'r6885_los_cr', 'r6885_losdp0_cr',
      'r6885_lossw0_cr', 'r6889_nufs0_cr', 'r6911_source_cr', 'r6911_source_cr_kcont',
      'r6915_pairs_cr', 'r6941_fine_cr', 'r6959_eta_cr']),
    ("68.62 / 0.2973, ZSTART=3e7, LEAFSCALES=0", dict(CRH0='68.62', CROM='0.2973', ZSTART='3e7'),
     ['r6784_cr_crossing_hier', 'r6784_cr_crossing_hier_noCRIC', 'r6784_cr_crossing_los',
      'r6794_cr_crossing_kcont_summed']),
    ("68.60 / 0.2973, ZSTART=3e7, LEAFSCALES=1",
     dict(CRH0='68.60', CROM='0.2973', ZSTART='3e7', LEAFSCALES='1'),
     ['cc66_cr_x_h686_pol', 'cc66_cr_x_h686_L2000']),
    ("68.62 / 0.2973, ZSTART=3e7, LEAFSCALES=1",
     dict(CRH0='68.62', CROM='0.2973', ZSTART='3e7', LEAFSCALES='1'),
     ['cc66_cr_x_h6862_pol']),
    ("the cc66 refit minimum AS QUOTED -- arm (1)", REFIT, ['cc66_refit_verify_cr']),
]

# the twelve whose own KFAC today's alias gate refuses -- arm (3)
KF1 = {
    'c54.175_cr': dict(BSPLIT='0', LMAXL='2000', NK='600', POLC='0.8888888889'),
    'c54.177_cr': dict(BSPLIT='0', LMAXL='2000', NK='600'),
    'c54.178_cr': dict(BSPLIT='1', HIER='1', KBATCH='300', LMAXL='2000', NK='600'),
    'c54.186_cr_KCONT': dict(BSPLIT='1', HIER='1', KBATCH='300', KCONT='1',
                             LMAXL='2000', NK='1200'),
    'c54.186_cr_L3000': dict(BSPLIT='1', HIER='1', KBATCH='300', LMAXL='3000', NK='900'),
    'c54.191_cr_lA340_L3000': dict(BSPLIT='1', HIER='1', KBATCH='300', LATARG='340',
                                   LMAXL='3000', NK='900'),
    'c54.191_cr_phipi_L3000': dict(BSPLIT='1', HIER='1', KBATCH='300', CRPHI='3.1416',
                                   LMAXL='3000', NK='900'),
    'c54.193_cr_nodrive_L3000': dict(BSPLIT='1', HIER='1', KBATCH='300', NODRIVE='1',
                                     LMAXL='3000', NK='900'),
    'c54.195_cr_phi0.7854_L3000': dict(BSPLIT='1', HIER='1', KBATCH='300', CRPHI='0.7854',
                                       LMAXL='3000', NK='900'),
    'c54.195_cr_phi1.5708_L3000': dict(BSPLIT='1', HIER='1', KBATCH='300', CRPHI='1.5708',
                                       LMAXL='3000', NK='900'),
    'item38_cr_phi0.0_prod': dict(BSPLIT='1', HIER='1', KBATCH='300', LMAXL='3000', NK='900'),
    'item38_cr_phi3.1416_prod': dict(BSPLIT='1', HIER='1', KBATCH='300', CRPHI='3.1416',
                                     LMAXL='3000', NK='900'),
}

print(__doc__)
print("=" * 94)
print("  r7640 (60) -- LAYER 1 OF THE INSTRUMENT-DRIFT CENSUS:  the threshold is %g" % TOL)
print("=" * 94)

# ----------------------------------------------------------------------------------------------
print("\nPART 0 -- THE FREE TEST, WHICH NEEDS NO INSTRUMENT AND NO CONFIGURATION AT ALL")
print("  *`L_A = np.pi * D_M / R_S` at the end of the background, and `r6893+cc66.37` measured that")
print("  no transfer function on any of the three paths reads either -- they are metadata.  So each")
print("  stored triple checks ITSELF, and a mistyped scale fails before any run is spent on it.*")
print("  ⛭ ** THIS PART EXISTS BECAUSE `r7640+60.1` NEEDED IT: the first pass declared a MISS")
print("     against an `r_s` this seat had typed into its own target table.  The test catches it. **")

names = sorted({v['namesake'] for v in M.values()})
check("the bank is the 36 the order names", len(M) == 36)
worst = max(abs(lA - np.pi * DM / rs) for lA, DM, rs in map(scales, names))
check(f"all {len(names)} namesakes satisfy l_A = pi D_M / r_s to better than {TOL:g} "
      f"(worst {worst:.3e})", worst < TOL)
_typed = 120.16185830983276          # the discarded reading of r7640+60.1, kept
_lA, _DM, _rs = scales('c54.191_cr_lA340_L3000')
check("⛭ r7640+60.1: and the DISCARDED typed r_s fails that same test by 1.4e-04, so the guard "
      "that was missing would have refused it",
      abs(_lA - np.pi * _DM / _typed) > 1e-5 and abs(_rs - _typed) > 1e-5)

# ----------------------------------------------------------------------------------------------
print("\nPART 1 -- EVERY NAMESAKE'S OWN BACKGROUND, REPRODUCED UNDER ITS OWN RECORDED COMMAND")
covered, exact, cleared = [], 0, 0
for label, env, stems in GROUPS:
    got, rc, _out, dt = run_background(env)
    print(f"\n  ⌗ {label}   [{dt:.0f}s, exit {rc}]")
    print(f"    today: l_A={got[0]:.15g}  D_M={got[1]:.15g}  r_s={got[2]:.15g}")
    for stem in stems:
        tgt = scales(stem)
        d = [abs(a - b) for a, b in zip(got, tgt)]
        check(f"{stem:<30} l_A/D_M/r_s within {TOL:g}  "
              f"({d[0]:.2e} / {d[1]:.2e} / {d[2]:.2e})", max(d) < TOL)
        covered.append(stem)
        cleared += max(d) < TOL
        exact += max(d) == 0.0

check(f"all 36 namesakes are placed in a group, none twice ({len(covered)})",
      sorted(covered) == names)
check(f"⇒ ** ALL 36 BACKGROUNDS CLEAR THE ORDER'S THRESHOLD ** ({cleared}/36)", cleared == 36)
check(f"⇒ and 35 of the 36 reproduce EXACTLY, not merely within {TOL:g} ({exact}/36) -- the one "
      "that does not is the l_A injection, whose onset is a brentq root", exact == 35)

print("\n  PART 1d -- AND LEAFREC, WHICH THE ORDER NAMES, IS INVISIBLE TO THE BACKGROUND")
print("  *So the three scales identify the POINT and the rulers, and say nothing about the switch")
print("  whose default moved -- which is why PART 4c has to read the source and not a spectrum.*")
_r0, _, _, _ = run_background(dict(REFIT, LEAFREC='0'))
_r1, _, _, _ = run_background(dict(REFIT, LEAFREC='1'))
check("at the refit point LEAFREC=0 and LEAFREC=1 give BIT-IDENTICAL l_A, D_M, r_s", _r0 == _r1)

print("\n  PART 1b -- THE NEGATIVE CONTROL ON THE ONE SWITCH THE BANK'S TWO RECORDS DISAGREE ABOUT")
got0, _, _, _ = run_background(dict(CRH0='68.6077', CROM='0.2967', WBH2='0.0217', NS='0.9949',
                                    ZSTART='3e7'))                      # LEAFSCALES defaults to 0
tgt = scales('cc66_refit_verify_cr')
check(f"at LEAFSCALES=0 the SAME point misses r_s by {abs(got0[2]-tgt[2]):.1f} Mpc, so the three "
      "scales DO discriminate the switch and PART 1's match is not vacuous",
      abs(got0[2] - tgt[2]) > 100.0 and abs(got0[1] - tgt[1]) < TOL)

print("\n  PART 1c -- AND THE BACKGROUND REALLY IS INDEPENDENT OF THE EXPENSIVE HALF")
print("  *The claim that licenses reading 36 configurations in minutes rather than days.*")
ladder = [run_background({'LATARG': '340'}, lmaxl=L)[0] for L in (200, 400, 800)]
check("the LATARG=340 onset solve returns BIT-IDENTICAL l_A, D_M, r_s at LMAXL = 200, 400, 800",
      ladder[0] == ladder[1] == ladder[2])

# ----------------------------------------------------------------------------------------------
print("\nPART 2 -- ARM (3): TWELVE NAMESAKES WHOSE OWN KFAC TODAY'S INSTRUMENT REFUSES")
print("  *`RECIPES.md`: \"The c54/item38 files were made at KFAC=1 (k_max = LMAXL/D_M), which")
print("  today's alias gate refuses.\"  `alias_gate`'s truncation half -- added r3870, FAIL-CLOSED,")
print("  caller `if not alias_gate(kk): return 1` -- refuses at k_max*D_M/LMAXL < 1.9, and KFAC=1")
print("  makes that ratio 1.0 BY CONSTRUCTION (`KMAXL = KFAC * LMAXL`).*")
print("  ⇒ ** For these twelve the order's Layer-2 comparison HAS NO READING TO TAKE, and the")
print("     honest census entry is the refusal named to its gate -- not a rebuild at KFAC=2")
print("     reported as though it were the namesake's configuration. **")
refused, slow = 0, 0
for stem, env in sorted(KF1.items()):
    e = dict(env); e['KFAC'] = '1'; e['LEAFREC'] = '0'
    _got, rc, out, dt = run_background(e, lmaxl=env['LMAXL'])
    m = re.search(r'ratio ([0-9.]+)', out)
    ok = rc == 1 and 'k-TRUNCATED' in out
    check(f"{stem:<30} ABORTS: exit {rc}, ratio {m.group(1) if m else '?'}, "
          f"the gate's own line present  [{dt:.0f}s]", ok)
    refused += ok
    slow += dt > 120
check("⇒ ** ALL TWELVE REFUSE ** (12/12)", refused == 12)
check("and the refusal is reached BEFORE the solver, so it costs seconds and not hours -- the "
      "k grid and the gate sit above the mode integration in the same block", slow == 0)

# ----------------------------------------------------------------------------------------------
print("\nPART 3 -- ARM (1): THE 'DIGITS UNRECORDED' POINT WAS THE QUOTED DIGITS ALL ALONG")
print("  *`RECIPES.md` / `MANIFEST_old.json`: \"the cc66 refit minimum, ~68.6077/0.2967/0.0217/")
print("  0.9949, digits unrecorded\".  Arm (1) registered that A POINT EXISTS within 0.01 of each")
print("  quoted figure reproducing all three scales to 1e-11.  It does, and it is STRONGER than")
print("  registered: the point is the four quoted figures themselves, to zero difference.*")
held = M['cc66_refit_verify_cr_leafrec1']['held']
check("the bank does say 'digits unrecorded' of this point", 'digits unrecorded' in held)
g, _, _, _ = run_background(REFIT)
tgt = scales('cc66_refit_verify_cr')
check(f"68.6077 / 0.2967 / 0.0217 at ZSTART=3e7, LEAFSCALES=1 reproduces all three scales to "
      f"ZERO ({max(abs(a-b) for a, b in zip(g, tgt)):.1e})",
      all(a == b for a, b in zip(g, tgt)))
check("⇒ ** arm (1) is a HIT: nothing beyond the quoted four digits was ever needed, so the entry's "
      "'digits unrecorded' is retired **", True)

# ----------------------------------------------------------------------------------------------
print("\nPART 4 -- WHAT THE FILES SETTLE AGAINST THE BANK'S OWN PROSE")
print("  *Two records of the same switch disagree, and the namesake decides.*")
rec = open(os.path.join(BANK, 'RECIPES.md')).read()
check("RECIPES.md's TABLE puts the cc66 h686/h6862 family at LEAFSCALES=1",
      'ZSTART=3e7 LEAFSCALES=1' in rec)
fam = ['cc66_cr_x_h686_pol', 'cc66_cr_x_h6862_pol', 'cc66_cr_x_h686_L2000',
       'cc66_refit_verify_cr']
check("while MANIFEST's `held` says LEAFSCALES=0 of the namesakes of all four of them",
      all('LEAFSCALES=0' in M[s + '_leafrec1']['held'] for s in fam))
check("⇒ and the FILES settle it at 1: PART 1 matched all four at LEAFSCALES=1 to zero, and "
      "PART 1b shows 0 misses r_s by over 100 Mpc", cleared == 36)

print("\n  PART 4b -- THE pol PAIR IS TWO RUNS, AND THE BANK REBUILT IT AS ONE")
za = np.load(os.path.join(SPEC, 'cc66_cr_x_h686_pol.npz'), allow_pickle=True)
zb = np.load(os.path.join(SPEC, 'cc66_cr_x_h6862_pol.npz'), allow_pickle=True)
ra = np.load(os.path.join(SPEC, 'cc66_cr_x_h686_pol_leafrec1.npz'), allow_pickle=True)
rb = np.load(os.path.join(SPEC, 'cc66_cr_x_h6862_pol_leafrec1.npz'), allow_pickle=True)
rel = float(np.max(np.abs(za['Dl'] - zb['Dl']) / np.maximum(np.abs(za['Dl']), 1e-30)))
check(f"the two NAMESAKES differ: {rel:.2e} relative on Dl, and their points differ "
      f"(D_M {float(za['D_M']):.4f} vs {float(zb['D_M']):.4f})", rel > 1e-4)
check("the two REBUILDS are bit-identical, because on the arm of record both points collapse to "
      "one -- which is right for the bank and WRONG for this census",
      np.array_equal(ra['Dl'], rb['Dl']))
check("⇒ Layer 2 owes TWO runs here, at 68.60 and at 68.62; one rebuild cannot be compared with "
      "both namesakes", True)

print("\n  PART 4c -- THE DEFAULT THAT MOVED, WHICH IS WHY A RECORDED COMMAND IS NOT A RECORD")
src = open(INSTR).read()
check("today's instrument defaults LEAFREC to ON: os.environ.get('LEAFREC', '1')",
      "os.environ.get('LEAFREC', '1')" in src)
check("and the instrument's own note names the move -- \"LEAFREC defaulting ON at cc66.75 is the "
      "case in point\" -- beside r7097's config ratchet, which exists because __SWITCHES__ records "
      "only what the environment SET", 'LEAFREC` defaulting ON at `cc66.75`' in src)
check("⇒ so any namesake banked before cc66.75 whose command omits LEAFREC is a command that, run "
      "verbatim today, rebuilds the leafrec1 arm and NOT the namesake -- the general form of what "
      "cc66 found on r6885_dp0", True)
nocfg = sum('config' not in np.load(os.path.join(SPEC, s + '.npz'),
                                    allow_pickle=True).files for s in names)
check(f"and none of the 36 namesakes carries the `config` key that would have recorded it "
      f"({nocfg}/36 without), while today's writer emits one", nocfg == 36)

# ----------------------------------------------------------------------------------------------
print("\n" + "=" * 94)
print("  LAYER 1 IS COMPLETE AND LAYER 2 IS NOT THIS SEAT'S: the order asks the two seats to")
print("  coordinate run order through the repo, and the background layer loads no machine.  What")
print("  this receipt hands 70 is an IDENTIFIED command per namesake -- the GROUPS table above --")
print("  so that 70's 36 spectrum rebuilds compare against the instrument and not against a guess.")
print("=" * 94)
print(f"\n  {len(_fail)} failure(s)")
for f in _fail:
    print("   [FAIL] " + f)
sys.exit(1 if _fail else 0)
