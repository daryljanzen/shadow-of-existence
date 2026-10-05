#!/usr/bin/env python3
r"""
RECEIPT -- P15 / `sec:largescale`, `sec:intro`: ** THE BACKGROUND RETURNS $1.4011\times10^{4}$ Mpc
AT THIS ARM'S OWN PARAMETERS, SO $2.774$ IS THE CONSTRUCTION'S STRETCH -- AND `sec:largescale`'s
`1.395e4 / 2.76` IS A WHOLE CONFIGURATION AND NOT AN ARITHMETIC SLIP, THOUGH THE FIGURES NAME TWO
CANDIDATES AND DO NOT SEPARATE THEM. **

*** AND THE REASON IT SURVIVED: THE STRETCH IS A FUNCTION OF $\Omega_m$ ALONE, AND $r_0$ -- THE ONE
NUMBER THE SENTENCE CALLS FIXED PARAMETER-FREE -- IS $5051$ IN EVERY CANDIDATE. ***

`sec:largescale` prints `$D_C\approx1.395\times10^{4}$~Mpc`, `$r_0\approx5051$~Mpc` and
`the stretch $D_C/r_0\approx2.76$`.  `sec:intro` prints `the stretch $2.774$` twice and
`$D_C=1.4011\times10^{4}$` once.  *Both triples are internally consistent; they are not the same
configuration.*

** WHAT THE INSTRUMENT RETURNS, RUN RATHER THAN DIVIDED. **  `ACOUSTIC_two_arm` is imported at four
configurations and its own module-level `D_M` read off:

      ARM=cr   CRH0=68.60 CROM=0.2973   D_M = 14011.4567    r_0 = 5051.49    stretch 2.773728
      ARM=cr   (instrument default)      D_M = 13004.5552    r_0 = 4708.97    stretch 2.761656
      ARM=lcdm (control default)         D_M = 13864.6627    -- the control's rate
      ARM=lcdm LH0=68.60 LOM=0.2973      D_M = 13941.6290    -- the control's rate, refitted

*The refit pair $(68.60,\,0.2973)$ is the background `P15` fits and the one `sec:refit-bound` reports
on.*  ⇒ ** So the background returns the LARGER value, and `$2.774$` is the construction's stretch. **
*No configuration of THIS ARM above returns a $D_C$ that prints `1.395e4`.*

** AND IT IS NOT AN ARITHMETIC SLIP: `sec:largescale`'s TRIO IS ONE SELF-CONSISTENT CONFIGURATION. **
The stretch is EXACTLY a function of $\Omega_m$ -- $r_0$ and $D_C$ both scale as $c/H_0$, so $H_0$
cancels, measured identical to $10^{-12}$ across $H_0 = 65, 68.6, 73, 80$.  *The $\Omega_m$ window
that prints `2.76` is $[0.30402,\,0.31176]$: it CONTAINS the arm's pre-refit default $0.3066$, and
EXCLUDES both the refit's $0.2973$ and the control's $0.3150$.*  ⌈ *At $\Omega_m=0.3066$ with $H_0$
set so that $r_0 = 5051$ -- the paper's own $r_0$ -- the integral returns $13949.1$, which prints
`1.395e4` to the paper's own four figures.*

⛔⛔ ** AND THE STALE VALUE'S PROVENANCE IS NOT UNIQUE -- TWO CONFIGURATIONS PRINT IT, AND THE
FIGURES DO NOT SEPARATE THEM. **  *The arm at a pre-refit $\Omega_m$ returns $13949.1$; the CONTROL
at its own 185-bin refit minimum (`LH0=67.410309 LOM=0.309826`) returns $13954.3535$, and $27$
banked spectra carry it.*  **$5.2$ Mpc apart -- below the paper's own printed precision -- and both
give `2.76` against the arm's `5051`.**  ⇒ *So this receipt does not pick: the order's question is
answered the same either way, and it says instead that the second reading is the worse one, because
under it the printed stretch is THIS arm's $r_0$ over the CONTROL's distance -- one arm's discrete
source projected through the other arm's comoving distance.*

⛔ ** WHY NO GATE SAW IT, AND THIS IS THE PART A DIVISION CANNOT REACH. **  $r_0 = 5051$ is reachable
at BOTH $\Omega_m$ -- $H_0 = 68.6066$ at $0.2973$ and $H_0 = 68.0568$ at $0.3066$ -- so *the number
the sentence calls `fixed parameter-free` cannot discriminate the two configurations.  Only the
stretch can.*  ⇒ ** And FOUR receipts assert the computed value against the paper's printed literal
with tolerances of $\pm100$ Mpc and $\pm0.03$, which are $1.63\times$ and $2.19\times$ the
discrepancy they would have to catch ($61.5$ Mpc and $0.0137$).  Every one of them is green --- and
two more take the printed pair as their own INPUT, which is a different class and is counted
separately. **
*One of them prints `$1.401\times10^{4}$` and `$1.395\times10^{4}$` side by side in its own verdict
prose and calls them `four of the paper's parameter-free figures`.*

### ⌗ WHAT THE REPAIR COSTS, MEASURED AND NOT ASSUMED

- `$\ell_2$` goes $7.8111 \to 7.8453$: **both print the paper's `7.8`.**
- The third degree's modal multipole is `9` at both printed stretches and flips to `8` only below
  $2.741706$ -- so it is **not** at risk between them, with $0.032$ of margin at the construction's
  value.
- ⛔ *But the paper's printed displacement range `$1.70$ and $2.93$` becomes $1.7426$ to $3.0158$,
  so the printed ceiling is CROSSED* -- and `r7164`'s gate Ⓑ⑤ (`1.69 < e < 2.93` at every degree)
  **fails at the construction's stretch while passing at the stale one.**  ** So the repair has a
  consequence in print and a receipt that has to move with it. **

Built r7177+cc66.142 (node 66, code seat), answering the chat seat's `r7177` order -- *"establish
which $D_C$ this cosmology's background actually returns, and therefore which stretch is the
construction's ... not the division"* -- by running the instrument's own background rather than
dividing the paper's own numbers.

===================================================================================================
** WHAT IS READ RATHER THAN TYPED **
===================================================================================================

  ** THE PAPER'S SIX FIGURES ARE CAPTURED FROM THEIR OWN SENTENCES. **  Both triples are located in
  `corpus/CR_cosmology.tex` before anything is computed, so a drifted wording REFUSES rather than
  being replaced by this file's memory of it.

  ** AND $D_C$ IS THE INSTRUMENT'S OWN. **  `computations/beyond_the_wall/ACOUSTIC_two_arm.py` is
  imported at each configuration and its module-level `D_M` is read -- the same object the transfer
  is carried on and the same one the banked spectra record -- never re-implemented here.  `r_0` is
  the Nariai amplitude $2^{1/3}/\sqrt\Lambda$ formed from the instrument's own `alpha` and `x_0`.

  ** AND THE BANKS ARE COUNTED, NOT REMEMBERED. **  Every `.npz` in the three banks is opened and
  its stored `D_M` and `arm` read.

** PARAMETERS. **  $(H_0,\Omega_m) = (68.60, 0.2973)$, the refit background `P15` fits, and
$(73.00, 0.3066)$ / $(67.40, 0.3150)$, the instrument's own two defaults -- all four labelled with
which.  $z_{\rm rec} = 1089.9$ is the instrument's.  *Nothing is fitted here.*

** COMPUTES: which of the two printed comoving distances the background returns at this arm's own
   parameters; that the stretch is a function of Omega_m alone and therefore which Omega_m each
   printed triple is; that r_0 cannot tell them apart; that TWO configurations print the stale
   value and the figures do not separate them; what the banks carry; and what moves in print if the
   stale triple is repaired. ***

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~10 s)
"""
import contextlib
import importlib.util
import io
import os
import re
import sys

import numpy as np
from scipy.optimize import brentq
from scipy.special import spherical_jn

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEX = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
SRC = open(TEX, encoding='utf-8').read()
FLAT = re.sub(r'\s+', ' ', SRC)
INSTR = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')

# =================================================================================================
print(BAR)
print("  PART 1 -- ** THE SIX PRINTED FIGURES, CAPTURED OUT OF THE PAPER AS VALUES **")
print(BAR)

# ⛭ CAPTURED, NOT PINNED.  Every figure this receipt calls `the paper's` is READ here as a NUMBER
#   and its printed precision taken from the paper's own STRING, so a comparison is made at the
#   precision the paper claims and not at a float's repr (`cc66.140`'s over-claim, which this
#   seat's own instrument caught).  ** Nothing below types one of these values. **
PAT = {
    'stale_DC': (r"\$D_C\\approx([0-9.]+)\\times10\^\{4\}", 2),
    'stale_r0': (r"\$r_0\\approx([0-9]+)", 2),
    'stale_st': (r"the stretch \$D_C/r_0\\approx([0-9.]+)\$", 1),
    'live_st': (r"the stretch \$([0-9.]+)\$", 2),
    'live_DC': (r"\$D_C=([0-9.]+)\\times10\^\{4\}\$", 1),
}
GOT = {k: re.findall(p, FLAT) for k, (p, _) in PAT.items()}
for k, (p, want) in PAT.items():
    print(f"      {k:9s} wanted {want}, found {len(GOT[k])}: {GOT[k]}")

# the displacement clause, whose two numbers Part 5 compares a computed range against
DISP = r"\$([0-9.]+)\$ and \$([0-9.]+)\$, a displacement of order one mode"
GOT_DISP = re.findall(DISP, FLAT)
print(f"      disp      wanted 1, found {len(GOT_DISP)}: {GOT_DISP}")

ELL2 = r"carries the lowest mode to \$\\ell_2\\approx([0-9.]+)\$"
GOT_ELL2 = re.findall(ELL2, FLAT)
print(f"      ell_2     wanted 2, found {len(GOT_ELL2)}: {GOT_ELL2}")


def one(k):
    """the single distinct value printed under key k, or None if the paper does not print one"""
    v = set(GOT[k])
    return v.pop() if len(v) == 1 else None


# ⛭⛭ A THREE-WAY CLASSIFIER AND NOT A RELAPSE PAIR -- `PO-78`'s entry from `cc66.136`, applied where
#   the DEFECT is a collision between two sites rather than a defect in one.  The background half of
#   this receipt (Parts 2-6) is a fact about the construction and survives any repair of the prose,
#   so it runs unconditionally.  Only this part is contingent, and it has three states, which a
#   single refusal message cannot distinguish:
#     (i)   the collision is in print  -> this receipt's subject, and the figures are captured;
#     (ii)  the stale pair is GONE and the construction's stretch is still in print -> the order's
#           repair has landed; say so BY NAME, and keep going;
#     (iii) neither -> the wording has drifted, and a figure that cannot be located cannot be
#           checked.  REFUSE.
#   ⌗ The branch is the test (`r7141`: a scope statement is PRINTED, not asserted); what is
#     CHECKED below is arithmetic on the captured values, which can fail in either state.
COUNTS_OK = all(len(GOT[k]) == w for k, (_, w) in PAT.items())
DEFECT = COUNTS_OK and one('stale_DC') == '1.395' and one('stale_st') == '2.76' \
    and one('live_st') == '2.774' and one('live_DC') == '1.4011' and one('stale_r0') == '5051'
DISCHARGED = (not GOT['stale_DC']) and (not GOT['stale_st']) and len(GOT['live_st']) >= 1

if DEFECT:
    print("  ⛔ THE COLLISION IS IN PRINT: `sec:largescale` prints "
          "`$D_C\\approx1.395\\times10^{4}$` twice, `$r_0\\approx5051$` twice and "
          "`the stretch $D_C/r_0\\approx2.76$` once, while `sec:intro` prints "
          "`the stretch $2.774$` twice and `$D_C=1.4011\\times10^{4}$` once.  ** One paper, two "
          "stretches and two background lengths. **")
    PAPER_DC_STALE = float(one('stale_DC')) * 1e4
    PAPER_DC_LIVE = float(one('live_DC')) * 1e4
    PAPER_R0 = float(one('stale_r0'))
    PAPER_ST_STALE, PAPER_ST_LIVE = one('stale_st'), one('live_st')
elif DISCHARGED:
    print("  ✔ DISCHARGED -- ** `r7177`'s ORDER HAS BEEN ANSWERED IN PRINT: the stale pair "
          "`1.395e4 / 2.76` is gone from the paper and the stretch this receipt establishes as the "
          "construction's is what remains. **  *This is the discharge of this receipt's finding "
          "and NOT a drift: the defective literals are absent and the repaired one is present, "
          "which are two different measurements and are reported as two.*  The parts below are "
          "facts about the background rather than about the prose, and still assert.")
    PAPER_DC_STALE, PAPER_ST_STALE = None, None
    PAPER_DC_LIVE = float(one('live_DC')) * 1e4 if one('live_DC') else 1.4011e4
    PAPER_R0 = float(one('stale_r0')) if one('stale_r0') else 5051.0
    PAPER_ST_LIVE = one('live_st')
else:
    print("  ⛔ REFUSED -- ** THE WORDING THIS RECEIPT READS HAS DRIFTED INTO NEITHER STATE: "
          "the collision is not in print as this receipt located it, and the stale figures have "
          "not all gone. **  What was found: "
          + "; ".join(f"{k} {GOT[k]}" for k in PAT)
          + ".  A figure that cannot be located is not a figure that can be checked.  *Nothing is "
            "asserted.*")
    sys.exit(1)


def dps(s):
    """the number of decimals the paper PRINTS, read off its own string"""
    return len(s.split('.')[1]) if '.' in s else 0


if DEFECT:
    check("⛭ each printed stretch is the ratio of its OWN printed lengths at the paper's own "
          f"printed precision: {PAPER_DC_STALE:.0f}/{PAPER_R0:.0f} -> "
          f"{round(PAPER_DC_STALE / PAPER_R0, dps(PAPER_ST_STALE))} and "
          f"{PAPER_DC_LIVE:.0f}/{PAPER_R0:.0f} -> "
          f"{round(PAPER_DC_LIVE / PAPER_R0, dps(PAPER_ST_LIVE))} -- so neither site is internally "
          "wrong and that is why neither looks wrong alone",
          round(PAPER_DC_STALE / PAPER_R0, dps(PAPER_ST_STALE)) == float(PAPER_ST_STALE)
          and round(PAPER_DC_LIVE / PAPER_R0, dps(PAPER_ST_LIVE)) == float(PAPER_ST_LIVE))
    check("⛭ and the two printed stretches are NOT the same number at the coarser of the two "
          "printed precisions, so the collision is real and not a rounding of one value",
          round(float(PAPER_ST_LIVE), dps(PAPER_ST_STALE)) != float(PAPER_ST_STALE))
# ⌗ The displacement clause's two figures are NOT pinned on a count here: Part 5 INDEXES
#   `GOT_DISP[0]`, so an absent or drifted capture raises there rather than passing a count test.
#   *`check_prose_pins`' class, and `cc66.140`'s answer to it -- remove the pin, keep the number.*
print(f"      the displacement clause's two captured figures, read in Part 5: {GOT_DISP}")
# =================================================================================================
print()
print(BAR)
print("  PART 2 -- ** WHAT THE INSTRUMENT'S OWN BACKGROUND RETURNS, AT FOUR CONFIGURATIONS **")
print(BAR)

CFG = (('cr-refit', dict(ARM='cr', CRH0='68.60', CROM='0.2973')),
       ('cr-default', dict(ARM='cr')),
       ('lcdm-default', dict(ARM='lcdm')),
       ('lcdm-refit', dict(ARM='lcdm', LH0='68.60', LOM='0.2973')),
       ('cr-refit-LEAFGEOM', dict(ARM='cr', CRH0='68.60', CROM='0.2973', LEAFGEOM='1')),
       # the CONTROL's own 185-bin refit minimum, the configuration `verify_lcdm` is banked at
       ('lcdm-refit185', dict(ARM='lcdm', LH0='67.410309', LOM='0.309826')))
KNOBS = ('ARM', 'CRH0', 'CROM', 'LH0', 'LOM', 'LEAFGEOM', 'NK')
RUN = {}
_saved = {k: os.environ.get(k) for k in KNOBS}
for tag, env in CFG:
    for k in KNOBS:
        os.environ.pop(k, None)
    os.environ.update(env)
    os.environ['NK'] = '120'                       # the background is built before NK is used
    spec = importlib.util.spec_from_file_location(f"ACOUSTIC_two_arm_cc142_{tag}", INSTR)
    AT = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(AT)
    # r_0 is the Nariai amplitude carried to today, formed from the instrument's OWN parameters
    x03 = 2.0 / AT.OM - 2.0
    alpha = AT.C / AT.H0 * np.sqrt(1.0 + 2.0 / x03)
    r0 = x03 ** (1.0 / 3.0) * alpha / np.sqrt(3.0)
    RUN[tag] = dict(H0=AT.H0, OM=AT.OM, DM=float(AT.D_M), r0=float(r0), rad=bool(AT.RAD_IN_RATE))
    _tail = (f"  D_M = {AT.D_M:9.4f}  r_0 = {r0:8.2f}  stretch = {AT.D_M / r0:.6f}"
             if AT.ARM == 'cr' else
             f"  D_M = {AT.D_M:9.4f}  r_0 = --  (the areal radius is a `cr` construct and the "
             f"control does not carry one)")
    print(f"      {tag:20s} H0 = {AT.H0:6.2f}  Om = {AT.OM:.4f}  rate "
          f"{'radiation-INCLUDED' if AT.RAD_IN_RATE else 'GEOMETRIC (no radiation)':26s}" + _tail)
for k, v in _saved.items():
    os.environ.pop(k, None)
    if v is not None:
        os.environ[k] = v

cr = RUN['cr-refit']
check(f"⛭⛭ at THIS ARM'S OWN refit parameters the background returns `D_M = {cr['DM']:.4f}` Mpc, "
      f"which rounds to the LARGER of the paper's two captured lengths -- "
      f"`{PAPER_DC_LIVE / 1e4:.4f}e4`, not the stale `{(PAPER_DC_STALE or 0) / 1e4:.4f}e4` -- at "
      f"the paper's own printed precision",
      round(cr['DM'] / 1e4, dps(one('live_DC')))
      == round(PAPER_DC_LIVE / 1e4, dps(one('live_DC'))))
check(f"⛭ with `r_0 = {cr['r0']:.2f}` Mpc from Lambda parameter-free, which rounds to the captured "
      f"`{PAPER_R0:.0f}`", round(cr['r0']) == round(PAPER_R0))
check(f"⛭⛭ so the construction's stretch is `{cr['DM'] / cr['r0']:.6f}`, which prints the paper's "
      f"captured `{PAPER_ST_LIVE}` and NOT its captured `{PAPER_ST_STALE}`",
      round(cr['DM'] / cr['r0'], dps(PAPER_ST_LIVE)) == float(PAPER_ST_LIVE)
      and (PAPER_ST_STALE is None
           or round(cr['DM'] / cr['r0'], dps(PAPER_ST_STALE)) != float(PAPER_ST_STALE)))
check("⛭ and it is the larger value BECAUSE this arm's rate carries no radiation term by "
      "construction -- `RAD_IN_RATE` is False on `cr` and True on `lcdm`",
      cr['rad'] is False and RUN['lcdm-default']['rad'] is True)
check("⛭ the instrument's own CR default (73.00, 0.3066) returns `13004.56` with `r_0 = 4708.97`, "
      "which is NOT the paper's `r_0` -- so neither printed site is that configuration",
      abs(RUN['cr-default']['DM'] - 13004.5552) < 0.05
      and abs(RUN['cr-default']['r0'] - 4708.97) < 0.5)
check("⛭ and the CONTROL returns `13864.66` at its own default and `13941.63` refitted -- the "
      "radiation-included rate, and neither prints `1.395e4`",
      abs(RUN['lcdm-default']['DM'] - 13864.6627) < 0.05
      and abs(RUN['lcdm-refit']['DM'] - 13941.6290) < 0.05
      and round(RUN['lcdm-refit']['DM'] / 1e4, 4) == 1.3942)
check("⛔ and no configuration of THIS ARM run here returns a `D_C` that prints `1.395e4` "
      "(13945..13955) -- which is NOT the same as saying no configuration does, and Part 3 says "
      "which two do",
      not any(13945.0 <= v['DM'] <= 13955.0
              for k, v in RUN.items() if k.startswith('cr')))

# =================================================================================================
print()
print(BAR)
print("  PART 3 -- ** THE STRETCH IS A FUNCTION OF Omega_m ALONE, SO `r_0` CANNOT SEE THE "
      "DIFFERENCE **")
print(BAR)

C = 299792.458
Z_REC = 1089.9


def arm_bg(H0, OM):
    """the CR arm's own geometry: the matter+Lambda rate, radiation as content and not a source"""
    OL = 1.0 - OM
    x03 = 2.0 / OM - 2.0
    alpha = C / H0 * np.sqrt(1.0 + 2.0 / x03)
    r0 = x03 ** (1.0 / 3.0) * alpha / np.sqrt(3.0)
    zz = np.linspace(0.0, Z_REC, 400001)
    DC = np.trapezoid(C / (H0 * np.sqrt(OM * (1 + zz) ** 3 + OL)), zz)
    return r0, DC


check("⛭ this file's own background reproduces the INSTRUMENT's `D_M` at the refit to 1 part in "
      f"10^5, so what follows is the same object: {arm_bg(68.60, 0.2973)[1]:.3f} vs {cr['DM']:.3f}",
      abs(arm_bg(68.60, 0.2973)[1] / cr['DM'] - 1.0) < 1e-5)

SPREAD = {}
for OM in (0.2973, 0.3066, 0.3150):
    st = [arm_bg(H0, OM)[1] / arm_bg(H0, OM)[0] for H0 in (65.0, 68.6, 73.0, 80.0)]
    SPREAD[OM] = (min(st), max(st))
    print(f"      Om = {OM}:  stretch at H0 = 65, 68.6, 73, 80  ->  "
          + "  ".join(f"{s:.9f}" for s in st))
check("⛭⛭ the stretch is EXACTLY H_0-independent -- identical to 10^-12 across a 15 km/s/Mpc span "
      "at each Omega_m, because `r_0` and `D_C` both scale as c/H_0",
      all(hi - lo < 1e-12 for lo, hi in SPREAD.values()))

_st = lambda om: (lambda t: t[1] / t[0])(arm_bg(70.0, om))          # noqa: E731
om_lo = brentq(lambda om: _st(om) - 2.765, 0.20, 0.45)
om_hi = brentq(lambda om: _st(om) - 2.755, 0.20, 0.45)
om_lo, om_hi = min(om_lo, om_hi), max(om_lo, om_hi)
print(f"      the Omega_m window that PRINTS 2.76:  [{om_lo:.5f}, {om_hi:.5f}]")
check(f"⛭⛭ that window CONTAINS the arm's pre-refit default 0.3066 and EXCLUDES both the refit's "
      f"0.2973 and the control's 0.3150",
      om_lo <= 0.3066 <= om_hi and not (om_lo <= 0.2973 <= om_hi)
      and not (om_lo <= 0.3150 <= om_hi))

H0_a = brentq(lambda h: arm_bg(h, 0.3066)[0] - 5051.0, 50.0, 100.0)
H0_b = brentq(lambda h: arm_bg(h, 0.2973)[0] - 5051.0, 50.0, 100.0)
dc_a = arm_bg(H0_a, 0.3066)[1]
dc_b = arm_bg(H0_b, 0.2973)[1]
print(f"      r_0 = 5051 at Om = 0.3066 needs H0 = {H0_a:.4f}  ->  D_C = {dc_a:9.2f} "
      f"({dc_a / 1e4:.4f}e4)")
print(f"      r_0 = 5051 at Om = 0.2973 needs H0 = {H0_b:.4f}  ->  D_C = {dc_b:9.2f} "
      f"({dc_b / 1e4:.4f}e4)")
check("⛭⛭⛭ `r_0 = 5051` is reachable at BOTH Omega_m, 0.55 km/s/Mpc apart in H_0 -- so the one "
      "number the sentence calls `fixed parameter-free by Lambda` CANNOT discriminate the two "
      "configurations, and only the stretch can",
      abs(arm_bg(H0_a, 0.3066)[0] - 5051.0) < 0.01
      and abs(arm_bg(H0_b, 0.2973)[0] - 5051.0) < 0.01 and abs(H0_a - H0_b) > 0.4)
check(f"⛭⛭ and at the pre-refit Omega_m with `r_0` pinned at the paper's captured "
      f"`{PAPER_R0:.0f}` the integral returns `{dc_a:.2f}`, which prints the captured stale "
      f"`{(PAPER_DC_STALE or 0) / 1e4:.3f}e4` at the paper's own precision -- so that site is a "
      "SELF-CONSISTENT CONFIGURATION, the arm at an Omega_m the refit has moved, and not an "
      "arithmetic slip",
      PAPER_DC_STALE is None
      or round(dc_a / 1e4, dps(one('stale_DC')))
      == round(PAPER_DC_STALE / 1e4, dps(one('stale_DC'))))

# ⛔⛔ AND THE PROVENANCE IS NOT UNIQUE, WHICH IS THE PART I WOULD HAVE MISSED BY STOPPING AT THE
#   FIRST ACCOUNT THAT WORKED.  The CONTROL at its own 185-bin refit minimum returns 13954.3535,
#   which prints `1.395e4` TOO -- and 27 banked spectra carry it.  The two candidates are 5.2 Mpc
#   apart, BELOW the paper's own printed precision, and both give 2.76 against the arm's 5051.
#   ** So the printed triple does not say which configuration it is, and this receipt does not
#   pick.  It says the order's question is answered either way and that one of the two readings is
#   a CROSS-ARM ratio. **
CTRL_REFIT = RUN['lcdm-refit185']['DM']
print(f"      the CONTROL at its own 185-bin refit minimum returns D_M = {CTRL_REFIT:.4f} "
      f"({CTRL_REFIT / 1e4:.4f}e4)")
check("⛔⛭ a SECOND configuration prints the same `1.395e4`: the CONTROL at its own 185-bin refit "
      "minimum (`LH0=67.410309 LOM=0.309826`) returns 13954.3535, read off the instrument here "
      "and not typed",
      abs(CTRL_REFIT - 13954.3535) < 0.05 and round(CTRL_REFIT / 1e4, 4) == 1.3954)
check("⛔⛔ the two candidates are 5.2 Mpc apart -- BELOW the paper's own printed precision -- and "
      "both give `2.76` against the arm's `5051`, so the printed triple CANNOT say which it is, "
      "and the honest answer to `which configuration is the stale one` is `the figures do not "
      "separate them`",
      abs(CTRL_REFIT - dc_a) < 6.0
      and round(CTRL_REFIT / 5051.0, 2) == 2.76 and round(dc_a / 5051.0, 2) == 2.76)
check("⛔⛔⛭ and the second reading is worse than the first, because under it the printed stretch "
      "is THIS ARM's `r_0` over the CONTROL's comoving distance -- a cross-arm ratio, with one "
      "arm's source spectrum projected through the other arm's distance",
      abs(CTRL_REFIT / 5051.4882 - 2.762424) < 1e-5)
check("⛭ the one OTHER configuration that would print `2.76` -- the refit arm with `LEAFGEOM=1`, "
      "the geometry on the leaf rate -- returns `13941.6`, which prints `1.394e4` and not "
      "`1.395e4`; and `LEAFGEOM` is off, so it is not the background the transfer is carried on",
      round(RUN['cr-refit-LEAFGEOM']['DM'] / 1e4, 4) == 1.3942
      and round(RUN['cr-refit-LEAFGEOM']['DM'] / RUN['cr-refit-LEAFGEOM']['r0'], 2) == 2.76)

# =================================================================================================
print()
print(BAR)
print("  PART 4 -- ** WHAT THE BANKS CARRY: THE TRANSFER'S OWN RECORD OF ITS OWN DISTANCE **")
print(BAR)

BANKS = [os.path.join(ROOT, 'computations', 'beyond_the_wall', d)
         for d in ('spectra', 'refit_grid', 'refit_grid185')]
seen = []
for b in BANKS:
    if not os.path.isdir(b):
        continue
    for f in sorted(os.listdir(b)):
        if not f.endswith('.npz'):
            continue
        z = np.load(os.path.join(b, f), allow_pickle=True)
        if 'D_M' not in z.files:
            continue
        seen.append((float(np.atleast_1d(z['D_M'])[0]),
                     str(np.atleast_1d(z['arm'])[0]) if 'arm' in z.files else '?'))
n_refit = sum(1 for d, a in seen if a == 'cr' and abs(d - 14011.4567) < 1e-3)
prints_1395 = [(d, a) for d, a in seen if 13945.0 <= d <= 13955.0]
print(f"      {len(seen)} banked spectra carry a stored `D_M`;  {n_refit} of them are `cr` at "
      f"14011.4567;  {len(prints_1395)} carry a value that prints 1.395e4")
print("      the ones that do: " + ", ".join(f"{d:.2f} ({a})" for d, a in sorted(set(prints_1395))))
check("⛭ the banks carry a stored `D_M` at all, and enough of them to be a measurement",
      len(seen) > 150)
check("⛭⛭ sixteen banked `cr` spectra record `D_M = 14011.4567` -- the transfer's own record that "
      "this is the distance the arm's figures are taken on", n_refit == 16)
check("⛭⛭ and every banked value that prints `1.395e4` is on the `lcdm` CONTROL arm, not on this "
      "one -- so the paper's `1.395e4` is not any run of the arm whose `r_0` it is printed beside",
      len(prints_1395) > 0 and all(a == 'lcdm' for d, a in prints_1395))

# =================================================================================================
print()
print(BAR)
print("  PART 5 -- ** WHAT MOVES IN PRINT IF THE STALE TRIPLE IS REPAIRED **")
print(BAR)

NMAX = 220
LL = np.arange(NMAX)


def dist(L, stretch):
    x = np.sqrt(L * (L + 2)) * stretch
    W = (2 * LL + 1) * spherical_jn(LL, x) ** 2
    W = W / W.sum()
    return x, int(W.argmax()), float(np.sqrt((LL * LL * W).sum() - ((LL * W).sum()) ** 2))


S_STALE = 1.395e4 / 5051.0
S_LIVE = cr['DM'] / cr['r0']
for lab, s in (('stale 1.395e4/5051', S_STALE), ("the arm's own", S_LIVE)):
    d = [dist(L, s) for L in range(1, 9)]
    print(f"      {lab:20s} stretch {s:.6f}   ell_2 = {d[1][0]:.4f}   L=3 mode = {d[2][1]}   "
          f"displacement {min(x - m for x, m, _ in d):.4f} .. {max(x - m for x, m, _ in d):.4f}")
e_stale = [dist(L, S_STALE)[0] - dist(L, S_STALE)[1] for L in range(1, 9)]
e_live = [dist(L, S_LIVE)[0] - dist(L, S_LIVE)[1] for L in range(1, 9)]

check(f"⌗ `$\\ell_2$` goes {dist(2, S_STALE)[0]:.4f} -> {dist(2, S_LIVE)[0]:.4f}, and BOTH "
      f"round to EVERY figure the paper prints for it ({GOT_ELL2}) -- the floor's printed location "
      "does not move",
      bool(GOT_ELL2) and all(round(x, dps(v)) == float(v) for v in GOT_ELL2
                             for x in (dist(2, S_STALE)[0], dist(2, S_LIVE)[0])))
flip = 2.80
lo, hi = 2.70, 2.80
for _ in range(60):
    m = 0.5 * (lo + hi)
    if dist(3, m)[1] == 8:
        lo = m
    else:
        hi = m
flip = hi
print(f"      the third degree's modal multipole flips 8 -> 9 at stretch {flip:.6f}")
check(f"⌗ the third degree's modal multipole is 9 at BOTH printed stretches and flips to 8 only "
      f"below {flip:.4f}, so it is not at risk between them -- {S_LIVE - flip:.4f} of margin at the "
      f"construction's value",
      dist(3, S_STALE)[1] == 9 and dist(3, S_LIVE)[1] == 9 and flip < S_STALE < S_LIVE)
_slo, _shi = GOT_DISP[0]
_dlo, _dhi = float(_slo), float(_shi)
check(f"⛔⛔ but the paper's CAPTURED displacement range `{_slo}` to `{_shi}` becomes "
      f"{min(e_live):.4f} to {max(e_live):.4f}, so the printed CEILING IS CROSSED and that clause "
      "moves with the stretch -- while it accommodates the stale stretch, whose range is "
      f"{min(e_stale):.4f} to {max(e_stale):.4f}",
      max(e_stale) < _dhi < max(e_live) and min(e_stale) < _dlo < min(e_live))
check("⛔⛔ and `r7164`'s own gate Ⓑ⑤ -- `1.69 < e < 2.93` at EVERY degree -- passes on the stale "
      "stretch and FAILS on the construction's, so repairing the prose turns that receipt red "
      "unless its ceiling moves in the same pass",
      all(1.69 < e < 2.93 for e in e_stale) and not all(1.69 < e < 2.93 for e in e_live))

# ⌗ `r7164` ALSO takes the paper's printed pair as its own inputs, so its whole width table is on
#   the stale configuration.  *That is a reading of another seat's source and is recorded in the
#   `INDEX` row and in `FOR_66.md` rather than asserted here: a gate that pins another file's line
#   fails when that seat rewords, and the measurement that matters -- its Ⓑ⑤ bound -- is the check
#   immediately above, which is arithmetic.*

# =================================================================================================
print()
print(BAR)
print("  PART 6 -- ** WHY NO GATE CAUGHT IT: THE TOLERANCES ARE WIDER THAN THE DISCREPANCY **")
print(BAR)

GAP_DC = abs(cr['DM'] - 1.395e4)
GAP_ST = abs(S_LIVE - 2.76)
print(f"      the discrepancy a gate would have to catch:  D_C {GAP_DC:.3f} Mpc   stretch "
      f"{GAP_ST:.6f}")
print(f"      the tolerances that read them:               +-1.0e2 Mpc ({1.0e2 / GAP_DC:.3f}x)   "
      f"+-0.03 ({0.03 / GAP_ST:.3f}x)")
RDIR = os.path.join(ROOT, 'receipts')
slack = []
for d, _, fs in os.walk(RDIR):
    for f in fs:
        if not f.endswith('.py'):
            continue
        p = os.path.join(d, f)
        t = open(p, encoding='utf-8').read()
        if re.search(r"- *1\.395e4\) *< *1\.0e2", t) or re.search(r"- *2\.76\) *< *0\.03", t):
            slack.append(os.path.relpath(p, RDIR))
print(f"      receipts asserting the computed value against the printed literal with those "
      f"tolerances: {len(slack)}")
for s in sorted(slack):
    print(f"        - {s[:96]}")
check("⛔⛔ the two tolerances are 1.63x and 2.19x the discrepancy they would have to catch, so "
      "neither gate CAN fail on the quantity it names",
      1.0e2 / GAP_DC > 1.6 and 0.03 / GAP_ST > 2.1)
check("⛔ and FOUR receipts rest on those two tolerances, so this is a gate-design class and not "
      f"one loose number -- {len(slack)} found by walking `receipts/`", len(slack) == 4)
# ⛔⛔ AND ONE OF THE FOUR PRINTS BOTH VALUES IN ITS OWN VERDICT PROSE AND CALLS THEM `four of the
#   paper's parameter-free figures`, so the disagreement has been published inside a PASS -- in the
#   appendix, through that receipt's `INDEX` row.  *That is a reading of another seat's wording and
#   not a measurement, so it is in the `INDEX` row and in `FOR_66.md` and is NOT asserted here.*
#   ⌗ What IS asserted is the tolerance arithmetic above, which cannot be reworded away.

# =================================================================================================
print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED:")
    for f in fail:
        print(f"      - {f}")
    print(BAR)
    sys.exit(1)
print("  ✔ THE BACKGROUND RETURNS $1.4011\\times10^{4}$ Mpc AT THIS ARM'S OWN PARAMETERS, ON THIS")
print("    ARM'S OWN RATE, SO ** $2.774$ IS THE CONSTRUCTION'S STRETCH ** -- which is what the")
print("    order asked, settled by a run and not by a division.")
print("  ⛔ `sec:largescale`'s `1.395e4 / 2.76` is a self-consistent configuration and not an")
print("    arithmetic slip, but WHICH one the figures do not say: the arm at a pre-refit $\\Omega_m$")
print("    returns 13949.1 and the CONTROL at its own 185-bin refit returns 13954.35 -- 5.2 Mpc")
print("    apart, below the paper's own printed precision, and both printing `1.395e4` and `2.76`.")
print("    *The second reading is the worse one: under it the printed stretch is THIS arm's $r_0$")
print("    over the CONTROL's comoving distance.*")
print("  ⌗ *The stretch is a function of $\\Omega_m$ alone, and $r_0$ -- the one number the sentence")
print("    calls fixed parameter-free -- is 5051 in every candidate, which is why nothing saw it.*")
print("  ⛔ And the repair crosses the printed displacement ceiling `2.93`, turning `r7164`'s Ⓑ⑤")
print("    red unless that clause moves in the same pass.")
print(BAR)
print("  ALL CHECKS PASS")
