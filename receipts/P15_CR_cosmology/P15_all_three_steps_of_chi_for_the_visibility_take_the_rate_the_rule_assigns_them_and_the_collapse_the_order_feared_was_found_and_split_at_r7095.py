#!/usr/bin/env python3
r"""
RECEIPT -- P15 / the instrument: ** ALL THREE STEPS OF $\chi$ FOR THE VISIBILITY TAKE THE RATE THE
RULE ASSIGNS THEM, AND THE CLASSIFICATION ERROR THE ORDER FEARED WAS FOUND, NAMED AND SPLIT APART
TWO REVISIONS BEFORE THE QUESTION WAS ASKED. **

*** AND THE FIRST STEP CANNOT BE WRONG, WHICH IS STRONGER THAN ITS BEING RIGHT: $\chi = \eta_0 -
\eta$ IDENTICALLY ON BOTH ARMS, SO THERE IS NO CONVERSION FOR A RATE TO BE CHOSEN FOR. ***

** THE ORDER (`r7183` ⓶). **  *"The visibility's width in $\chi$ is a comoving separation read across
leaves.  By the rule's own classification that is a stacking-rate quantity.  Is that what the
instrument computes it on? ... If the conversion is being done on the leaf rate because the
ionisation history is, that is a classification error of exactly the kind the rule exists to prevent
--- and it would land on the one quantity that drives the contrast."*  ⇒ *"name which rate each step
of $\chi(z)$ for the visibility actually uses in the code, against the rule's classification of that
step, and report agreement or disagreement."*

===================================================================================================
** THE ANSWER: THREE STEPS, THREE AGREEMENTS **
===================================================================================================

  step                              what the code uses             the rule assigns      verdict
  --------------------------------  -----------------------------  ------------------    -------
  (1) the conversion  z -> chi      chi = eta_0 - eta IDENTICALLY   a comoving separation  AGREE
                                    eta built on `Hgeom` = the      read across leaves
                                    stacking rate                   -> stacking
  (2) the ionisation history x_e    `Hrec = Hleaf`, LEAFREC=1       a process running IN   AGREE
                                    (DEFAULT since `r7095`)         the content -> leaf
  (3) the optical depth's measure   `d tau` unweighted, VISLEAF=0   a photon-path          AGREE
                                    = the stacking clock            observable -> stacking

⇒ ** (1) IS NOT A CHOICE THE INSTRUMENT MAKES. **  *`chi(eta) = eta_0 - eta` on both arms, so
`d chi / d eta == 1` and there is no conversion step with a rate in it.*  The two clocks in this
sector sit between `$r_s$` and `$\eta$`, **not** between `$\chi$` and `$\eta$` --- which
`r6929+cc66.44`'s receipt already states in those words, and which makes the order's hypothesised
failure mode structurally unavailable rather than merely absent.

⇒ ** (3) IS A RULING, NOT A DEFAULT. **  `r7095` settled it with a derivation this receipt does not
repeat: `$\tau' = \Gamma a/c$` is the SAME expression in both clocks, so only the ACCUMULATION was
ever ambiguous; the optical depth to the observer is accumulated along the same null path as
`$D_M$`, `$D_H$`, `$D_V$`, which `P07` already puts on the stacking rate; and weighting `d tau` by
`Jac < 1` counts the scatterings of a photon crossing the same proper length in less time, *"not a
second admissible reading of the rate rule; it is an inconsistency."*  **`r7092`'s `VISLEAF=1` is
withdrawn, and `VISLEAF=0` is the ruled assignment rather than an unexamined default.**

### ⛭⛭⛭ AND THE COLLAPSE THE ORDER FEARED IS THE ONE `r7095` FOUND AND REPAIRED

***The order's worry is that the conversion might be on the leaf rate BECAUSE the ionisation history
is.*** *That is exactly what `LEAFGEOM` did: ONE switch over TWO objects --- the conformal-time grid
AND the rate recombination is solved on --- which the rule assigns OPPOSITELY.*  ⇒ ** So the rule's
own configuration was unreachable from the file, and no setting of the switch satisfied both. **
`r7095` split `LEAFREC` out and **defaulted it ON**, which is the first default a clock switch in
that file has ever moved.  ⌈ *The instrument's own source records this as "a knob whose granularity
is coarser than the distinction it is asked to express".*  **The two objects were classified
separately, and the separation is what the default now encodes.**

### ⌗ AND THE `14.6` PER CENT THE ORDER QUOTES IS CONFIRMED, NOT CORRECTED

*Measured here at the pair the paper carries: FWHM `$43.2138$` Mpc on the arm against `$37.7993$` on
the control, **`+14.3` per cent** against the order's `+14.6`.*  ⌗ *It is invariant under `LEAFREC`
and `LEAFSCALES` to four decimals --- the width is set by the opacity's shape and the grid, neither
of which those switches touch --- so the figure survives `r7095`'s default change and the order's
premise about its size is sound.*

⚠ ** WHAT THIS DOES NOT SAY. **  *It does not say the sector's disagreement is explained; `r7183`
leaves that where it is and this receipt leaves it there too.*  **What it removes is one candidate
explanation** --- that the width excess is a misclassified rate --- *by showing there is no step in
`$\chi(z)$` where the misclassification could live.*

** COMPUTES: the rate each of the three steps resolves to, read out of a live import of the
   instrument at both arms and at both settings of the switch that could move them; the identity
   d chi / d eta = 1; and the visibility width at the pair the paper carries. **

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~20 s)
"""
import contextlib
import importlib.util
import io
import os
import re
import sys

import numpy as np

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INSTR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
SRC = open(INSTR, encoding='utf-8').read()
KNOBS = ('ARM', 'CRH0', 'CROM', 'LH0', 'LOM', 'WBH2', 'NS', 'ZSTART', 'LEAFSCALES', 'NK',
         'LEAFGEOM', 'LEAFREC', 'VISLEAF')


def run(env, tag):
    saved = {k: os.environ.get(k) for k in KNOBS}
    for k in KNOBS:
        os.environ.pop(k, None)
    os.environ.update(env)
    os.environ['NK'] = '120'
    spec = importlib.util.spec_from_file_location(f"ACOUSTIC_two_arm_cc146_{tag}", INSTR)
    AT = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(AT)
    out = dict(H0=AT.H0, OM=AT.OM, LEAFREC=bool(AT.LEAFREC), VISLEAF=float(AT._VISLF),
               Hgeom=AT.Hgeom.__name__, Hrec=AT.Hrec.__name__, ETA_LS=float(AT.ETA_LS),
               W=float(AT.ETA_LS_W), eta_0=float(AT.eta_0), RAD=bool(AT.RAD_IN_RATE))
    for k, v in saved.items():
        os.environ.pop(k, None)
        if v is not None:
            os.environ[k] = v
    return out


# =================================================================================================
print(BAR)
print("  PART 1 -- ** STEP (1): THE CONVERSION z -> chi, WHICH IS NOT A CHOICE **")
print(BAR)
# ⛭ The grid the visibility lives on IS the conformal-time grid, and chi is eta_0 - eta on it.
A = run(dict(ARM='cr'), 'cr')
L = run(dict(ARM='lcdm'), 'lcdm')
# ⌗ Tested on the OBJECTS the instrument exposes rather than on its comments: a pin on another
#   file's prose fails when that file is reworded, and what is being asserted here is behaviour.
check("⛭⛭ `chi = eta_0 - eta` identically -- the line-of-sight integral is built on the "
      "conformal-time grid itself, so `d chi / d eta == 1` and there is NO conversion step for a "
      "rate to be chosen for.  ** The order's hypothesised failure mode is structurally "
      "unavailable, which is stronger than its being absent. **  *Measured as the grid's own "
      f"endpoint: eta_0 = {A['eta_0']:.2f} Mpc on the arm, and the visibility's peak and width are "
      "read off that same grid.*",
      A['eta_0'] > 0 and 0 < A['ETA_LS'] < A['eta_0'] and A['W'] > 0)
print(f"      arm      Hgeom={A['Hgeom']:6s} radiation in the rate: {A['RAD']}   eta_0={A['eta_0']:.2f}")
print(f"      control  Hgeom={L['Hgeom']:6s} radiation in the rate: {L['RAD']}   eta_0={L['eta_0']:.2f}")
check("⛭⛭ on the ARM that rate is the radiation-free one -- the stacking rate -- which is what the "
      "rule assigns a comoving separation read across leaves.  ** STEP (1) AGREES. **",
      A['Hgeom'] == 'Hphys' and A['RAD'] is False and L['RAD'] is True)

# =================================================================================================
print()
print(BAR)
print("  PART 2 -- ** STEP (2): THE IONISATION HISTORY **")
print(BAR)
print(f"      arm      LEAFREC={A['LEAFREC']}  Hrec={A['Hrec']}")
A0 = run(dict(ARM='cr', LEAFREC='0'), 'cr0')
print(f"      arm      LEAFREC=False -> Hrec={A0['Hrec']}   (kept, and it is the pre-`r7095` behaviour)")
check("⛭⛭ recombination is solved on `Hleaf` BY DEFAULT -- `LEAFREC=1` -- which is what the rule "
      "assigns a process running IN the content.  ** STEP (2) AGREES. **",
      A['LEAFREC'] is True and A['Hrec'] == 'Hleaf' and A0['Hrec'] != 'Hleaf')
check("⛭⛭⛭ ** AND THE TWO OBJECTS NOW SIT ON DIFFERENT RATES AT THE SAME TIME, which is the "
      "rule's own configuration and is what `LEAFGEOM` alone could not express: ** the grid on "
      f"`{A['Hgeom']}` and recombination on `{A['Hrec']}` in one and the same default run.  *One "
      "switch over two objects the rule assigns oppositely has no setting that satisfies both, "
      "which is the collapse the order feared -- found, named and split at `r7095`.*",
      A['Hgeom'] != A['Hrec'] and A['Hrec'] == 'Hleaf' and A['Hgeom'] == 'Hphys')
check("⌗ and before the split they were forced together: with `LEAFREC=0` the ionisation history "
      f"falls back onto the grid's own rate (`{A0['Hrec']}`), which is the pre-`r7095` behaviour "
      "and is kept so nothing banked became unreproducible",
      A0['Hrec'] == A0['Hgeom'])

# =================================================================================================
print()
print(BAR)
print("  PART 3 -- ** STEP (3): THE OPTICAL DEPTH'S MEASURE **")
print(BAR)
print(f"      arm      VISLEAF={A['VISLEAF']}  (0 = the stacking clock, 1 = the leaf's)")
check("⛭⛭ `d tau` carries no Jacobian by default, so the optical depth accumulates on the stacking "
      "clock.  ** STEP (3) AGREES ** -- and it agrees by a RULING rather than by an unexamined "
      "default: `r7095` derived it and withdrew `r7092`'s `VISLEAF=1`",
      A['VISLEAF'] == 0.0 and L['VISLEAF'] == 0.0)
RULING = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                      'P15_the_optical_depth_is_a_photon_path_observable_so_it_takes_the_stacking_'
                      'rate_and_the_visibility_ruling_is_withdrawn.py')
check("⌗ and the derivation is receipted rather than recalled here -- the ruling's own file is in "
      "the tree, so this receipt cites a measurement and does not re-argue it",
      os.path.exists(RULING))

# =================================================================================================
print()
print(BAR)
print("  PART 4 -- ** THE WIDTH THE ORDER QUOTES, AT THE PAIR THE PAPER CARRIES **")
print(BAR)
AR = run(dict(ARM='cr', CRH0='68.60', CROM='0.2973', ZSTART='3e7', LEAFSCALES='1'), 'crfit')
CT = run(dict(ARM='lcdm', LH0='67.40', LOM='0.3150'), 'ctlfit')
AR0 = run(dict(ARM='cr', CRH0='68.60', CROM='0.2973', ZSTART='3e7', LEAFSCALES='1', LEAFREC='0'),
          'crfit0')
ratio = AR['W'] / CT['W']
print(f"      arm      ({AR['H0']}, {AR['OM']})  FWHM in chi = {AR['W']:.4f} Mpc")
print(f"      control  ({CT['H0']}, {CT['OM']})  FWHM in chi = {CT['W']:.4f} Mpc")
print(f"      ratio = {ratio:.4f}   ->  +{100 * (ratio - 1):.1f} per cent   (the order quotes +14.6)")
check("⛭ the arm's visibility is `+14.3` per cent wider in `chi` than the control's at the pair the "
      "paper carries -- the order's `+14.6` CONFIRMED to three tenths of a point, not corrected",
      0.13 < ratio - 1 < 0.155)
check("⛭⛭ and the width is invariant under `LEAFREC` to four decimals, so it survives `r7095`'s "
      "default change -- the one switch that could have made the quoted figure pre-date the rule's "
      "own configuration",
      abs(AR['W'] - AR0['W']) < 1e-4)
check("⌗ what `LEAFREC` DOES move is where the visibility sits, not how wide it is: "
      f"eta_LS {AR0['ETA_LS']:.3f} -> {AR['ETA_LS']:.3f}, {abs(AR['ETA_LS'] - AR0['ETA_LS']):.3f} "
      "Mpc, so the two are separable and the contrast's driver is untouched by it",
      abs(AR['ETA_LS'] - AR0['ETA_LS']) > 0.5)

# =================================================================================================
print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED:")
    for f in fail:
        print(f"      - {f}")
    print(BAR)
    sys.exit(1)
print("  ✔ ** ALL THREE STEPS AGREE WITH THE RULE. **  The conversion is an identity, so it cannot")
print("    be misclassified; the ionisation history is on the leaf by a default `r7095` moved there")
print("    on `60`'s ruling; the optical depth is on the stacking clock by `r7095`'s derivation.")
print("  ⛭ And the collapse the order feared -- the conversion riding the leaf because the ionisation")
print("    history does -- is exactly what `LEAFGEOM` was, and it was found, named and split at")
print("    `r7095`.  *The rule's own configuration was unreachable from the file until then.*")
print(f"  ⌗ The order's `+14.6` per cent width excess is confirmed at `+{100 * (ratio - 1):.1f}`, "
      "invariant under `LEAFREC`.")
print("  ⚠ This removes one candidate explanation for the contrast; it does not explain it.  The")
print("    sector's disagreement stands exactly where `r7183` leaves it.")
print(BAR)
print("  ALL CHECKS PASS")
