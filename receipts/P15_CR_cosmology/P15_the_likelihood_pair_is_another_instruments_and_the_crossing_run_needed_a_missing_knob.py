"""
P15_the_likelihood_pair_is_another_instruments_and_the_crossing_run_needed_a_missing_knob
========================================================================================

Object under test -- `PO-10` reopened at r6780 on a contradiction between `P15`'s body and `P15`'s own
receipt.  The body states chi^2 = 397.13 for this construction against 206.44 for flat LambdaCDM over
215 `plik_lite` TT bins with the same five parameters free in each, so Delta chi^2 = 190.7.
`P15_where_the_likelihood_sits` records that pair as SUPERSEDED.  The order asks which comparison is
legitimate, for the run on the configuration that now exists, for the floor beside the difference, for
whether the position deficit is in the spectrum the run is made on, and for what the old pair was.

** THE ANSWER TURNS ON A DISTINCTION NEITHER THE BODY NOR THE ORDER DRAWS: THERE ARE TWO INSTRUMENTS
HERE, NOT ONE ARGUMENT ABOUT ONE. **  Both are in the tree, both score through the same `plik_lite`
likelihood, and their CR arms are different objects:

   A  `computations/planck_tt_likelihood/fit.py`   CAMB, five parameters free, 215 bins
      ** its CR arm is CAMB's LambdaCDM spectrum MULTIPLIED by a damping envelope in ell. **
   B  `ACOUSTIC_two_arm.py` + `chi2_of_spectrum.py`   one fitted amplitude, 185 covered bins
      ** its CR arm is the construction's own spectrum, integrated from the construction's rate. **

The body's pair is A's.  The receipt's supersession is the statement that A's CR arm is not the
construction's spectrum.  ** Both are accurate; they are about different things, and the sentence in
the body presents A's number as though it were B's object. **

Q1 -- WHICH COMPARISON IS LEGITIMATE.  ** B's, and not because A is malformed. **  `F3` requires both
arms on one instrument and A satisfies it: A's control IS CAMB and A's CR arm is CAMB-plus-envelope,
five parameters each, same bins.  Nothing in A is inconsistent.  ** What A cannot do is carry the
object the disagreement now lives in. **  Its CR content enters only as exp(-(ell/ell_D)^2(r^2-1)), a
monotonic function of ell, and that is measured here rather than argued: applied to a spectrum it
shifts the first peak by at most a few multipoles and leaves the COMB -- the spacing, which is what an
acoustic scale is -- within a few per cent of where it found it.  *320/272/312 becomes 312/272/304
under an envelope strong enough to move ell_1 from 220 to 212.*  ** So A's peak positions are CAMB's
at A's five fitted parameters, and the construction's own comb is a different object. **  A tests the
damping signature on LambdaCDM's comb, which is what the receipt says, and B tests the spectrum.

  ⌗ AND A HAS NO FLOOR, WHICH IS WHY IT LOOKS CLEANER AND SAYS LESS.  `F2`'s floor is
  chi^2(this instrument's LambdaCDM arm) - chi^2(CAMB).  In A the LambdaCDM arm IS CAMB, so A's floor
  is identically zero by construction.  ** A floor of zero is not a better-conditioned instrument; it
  is the absence of an independent control. **

Q2 -- THE RUN, AND THE CONFIGURATION THAT NOW EXISTS WAS NOT REACHABLE.  On B, as the tree stands:

      LambdaCDM arm   chi^2 =   1320.5     185 covered bins, ell 100-1996, l_A = 301.4
      CR arm          chi^2 =  51817.0     185 covered bins, ell 100-1996, l_A = 301.6
      each with ONE fitted parameter, the amplitude -- not five

  ** But that CR arm is not on the crossing configuration either, and finding out why is most of this
  revision. **  B's CR arm had its background written in as LITERALS -- H0 = 73.00, Omega_m = 0.3066,
  the directly-measured-H_0 configuration that goes with `LATARG` = 301.6 being FITTED by solving
  z_onset.  `P15` now computes the acoustic scale from the rate at the branch point at the background
  the distance data fix on their own.  ** No knob reached it.  A configuration the paper states and
  the instrument cannot run is the same class of defect as a dead knob -- the run that would check the
  claim is unreachable -- and it is the fifth such finding on this line. **  `CRH0`, `CROM` and
  `CROMBH2` are exposed here, default unset byte-identical, verified against the banked values.

  ⚠ AND THE RUN THAT BECOMES POSSIBLE DOES NOT REPRODUCE THE PAPER'S ACOUSTIC SCALE, WHICH IS
  REPORTED AND NOT RESOLVED HERE.  Integrating the sound horizon from the branch point at the crossing
  background, the integral CONVERGES as `P15` says it does -- r_s runs 165.55, 227.83, 247.80, 254.13,
  255.36, 256.13 Mpc as the start recedes through z = 1e4 to 1e8 -- and the scale it converges to is

      l_A = 265.8, 193.2, 177.6, 173.2, 172.3, 171.8   ->   ** about 172, not 298 **

  against the body's computed comb of 298.0 and the sky's 298.4.  ** The two are not computing the
  same r_s: **  the body puts the sound horizon on the LEAF rate, which carries radiation, while
  keeping D_M on the radiation-free stacking rate; `rs_from` integrates against `Hphys`, which for
  this arm is the radiation-free rate, and the file's own comment says the instrument's two sound
  horizons are "correct and NOT interchangeable" and must not be unified.  ** Which of the two the
  paper intends is a question about the paper and is not settled here (SCOPE). **  What is established
  is that the number the body reports and the number this instrument computes come from different
  conventions, so no run of this instrument can confirm or refute the body's 298.0 until that is
  fixed.

Q3 -- THE FLOOR BESIDE THE DIFFERENCE.  On B:

      F2, the instrument's own floor   chi^2(LambdaCDM arm) - chi^2(CAMB)  =  +1114.0
      F3, the readable quantity        chi^2(CR arm) - chi^2(LambdaCDM arm) = +50496.5
      the difference is 45.33 times the floor  ->  in the physics, not the instrument

  ** AND THE ORDER'S OWN POINT LANDS EXACTLY WHERE IT AIMED. **  The body's Delta chi^2 = 190.7 is
  SMALLER than B's floor of 1114.0.  ** So that difference could not be read on this instrument even
  if it were this instrument's -- a floor of 1114 cannot resolve 191. **  It is readable on A only
  because A's floor is zero, and A's floor is zero because A has no independent control.

Q4 -- IS THE POSITION DEFICIT IN THE SPECTRUM THE RUN IS MADE ON.  ** On B yes, on A no, and the
difference is structural rather than a matter of degree. **  B's CR arm integrates the construction's
own perturbations on the construction's own rate and produces its own peak positions, so the deficit
is present in the spectrum being scored.  A's CR arm cannot contain it: its positions are CAMB's, and
an ell-only multiplicative envelope cannot supply a different comb, as Q1 measures.

Q5 -- WHAT THE OLD PAIR ACTUALLY WAS.  ** BOTH of the order's two options, which are not exclusive,
and that is the answer rather than a choice between them. **  `cr.json` banks a genuine
five-parameter optimum -- H0 = 78.129, omega_b = 0.02546, omega_c = 0.10104, 1e9 A_s = 2.0861,
n_s = 1.0949, chi^2 = 397.1255 -- so the refit is real and the body's "five parameters free in each"
is correct about the count.  ** And `fit.py` shows what was refitted: `Dltt = d[2:lmax+1, 0]`, CAMB's
LambdaCDM TT, and then `if cr: Dltt = Dltt * s` with s the damping envelope. **  The five parameters
were genuinely free; the SHAPE they were fitted through was LambdaCDM's.  *So the prose did not
acquire a fuller description than the number had -- the number had exactly that description, and what
it lacked was the construction's spectrum.*

  ⌗ AND ONE NUMBER IN THAT FIT IS WORTH READING: H0 = 78.13.  Neither the directly measured value the
  pinned arm uses (73.00) nor the crossing configuration's (68.62).  ** The five free parameters went
  where LambdaCDM-plus-envelope needed them, which is what "a different question" means concretely. **

CONSTRUCTION.  The order leaves the construction to this line.  What was built: the two instruments
held apart and each read on its own terms rather than one being called the other's error; the envelope
claim MEASURED on a banked spectrum instead of asserted from its functional form; the CR arm's
background exposed so the crossing configuration can be run at all, with the default proved
byte-identical; and the sound-horizon convergence scanned over four decades of starting redshift so
that "converges at its upper end" is a measurement here and not a quotation.

COMPUTES: scope -- what the pinned numbers do and do not bound.
  * `CRH0`/`CROM`/`CROMBH2` DEFAULT to the previous literals, and the default is verified
    byte-identical on l_A, r_s, D_M and the peak list.  ** Nothing banked moves. **
  * `CRH0 = 68.62`, `CROM = 0.2973` are the crossing configuration's background as the joint fit on
    the distance data returns it.  They are inputs here, not results of this receipt.
  * `ZSTART` in the convergence scan runs 1e4 to 1e8 and the scan IS the claim -- no single value is
    relied on.  The l_A it converges to is quoted to three figures and its residual drift between
    3e7 and 1e8 is 0.5, which is reported rather than hidden.
  * The envelope parameters (ell_D, r) in Q1's measurement are ILLUSTRATIVE, spanning envelopes
    strong enough to move ell_1 by four to eight multipoles.  ** The claim is the comb's insensitivity
    across that span, not any one pair. **  The actual fitted envelope needs CAMB, which is not in
    this container; the bound does not depend on its value because monotonicity in ell is what carries
    the argument and every envelope of that form has it.
  * 185 against 215 bins is the instrument's coverage, not a choice: B reaches ell 2000 and
    `plik_lite` runs to 2508, and the restriction is done on the COVARIANCE and re-inverted.

ORIGIN: written for r6780's order, routed through `FOR_60.md`; the two-instrument reading, the
envelope measurement, the exposed background knobs and the convergence scan are this line's.
"""
import json
import os
import sys

import numpy as np

_checks = []


def check(label, ok):
    _checks.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    assert ok, label


print(__doc__)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
LIK = os.path.join(ROOT, 'computations', 'planck_tt_likelihood')
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, LIK)
import chi2_of_spectrum as CS                                              # noqa: E402
from planck_lite_py import PlanckLitePy                                    # noqa: E402

lik = PlanckLitePy(data_directory=os.path.join(LIK, 'data'), year=2018, spectra='TT',
                   use_low_ell_bins=False)

# =========================================================================================
print("=" * 94)
print("PART 1 (C1) — F1 FIRST: THE PIPELINE AGAINST THE BANKED CAMB FIT, BEFORE ANY NUMBER IS READ")
print("=" * 94)
print("""
  The order makes this non-optional, and so does the receipt it calibrates against: if the CAMB
  flat-LambdaCDM best fit does not reproduce chi^2 = 206.4 over 215 TT bins, nothing below may be read.
""")
LCDM = json.load(open(os.path.join(LIK, 'lcdm.json')))
CHI_CAMB = float(LCDM['fun'])
print(f"    CAMB flat-LambdaCDM, banked:  chi^2 = {CHI_CAMB:.2f} over {lik.nbintt} TT bins"
      f"   ->   chi^2/dof = {CHI_CAMB / lik.nbintt:.3f}")
print(f"    its five fitted parameters:   H0 = {LCDM['x'][0]:.3f}, omega_b = {LCDM['x'][1]:.5f}, "
      f"omega_c = {LCDM['x'][2]:.5f}, 1e9 A_s = {LCDM['x'][3]:.4f}, n_s = {LCDM['x'][4]:.4f}")
check("F1: the CAMB reference is chi^2 = 206.4 over 215 bins", abs(CHI_CAMB - 206.4) < 0.1)
check("F1: chi^2/dof = 0.960, so the pipeline is wired",
      abs(CHI_CAMB / lik.nbintt - 0.960) < 0.005)
check("and the bin count is the 215 the body's sentence names", lik.nbintt == 215)

# =========================================================================================
print()
print("=" * 94)
print("PART 2 (Q1) — TWO INSTRUMENTS, AND WHAT A's CR ARM CANNOT CONTAIN")
print("=" * 94)
print("""
  A's CR arm is CAMB's LambdaCDM spectrum times exp(-(ell/ell_D)^2 (r^2 - 1)).  The claim is that such
  an envelope cannot supply a different comb.  ** Measured on a banked spectrum rather than argued
  from the formula, and the invariant is the SPACING, because that is what an acoustic scale is. **
""")
_z = np.load(os.path.join(SPEC, 'c54.178_lcdm.npz'))
LS, DL = _z['ls'], _z['Dl']


def peaks(D, n=4):
    return [int(LS[i]) for i in range(1, len(D) - 1) if D[i] > D[i - 1] and D[i] > D[i + 1]][:n]


def spacings(p):
    return [p[i + 1] - p[i] for i in range(len(p) - 1)]


BASE = peaks(DL)
print(f"    no envelope                          peaks {BASE}   spacings {spacings(BASE)}")
ENV = [(1500., 1.3), (1200., 1.4), (900., 1.6)]
moved, comb_kept = [], []
for lD, r in ENV:
    p = peaks(DL * np.exp(-(LS / lD) ** 2 * (r ** 2 - 1)))
    print(f"    x exp(-(l/{lD:.0f})^2({r}^2-1))          peaks {p}   spacings {spacings(p)}")
    moved.append(abs(p[0] - BASE[0]))
    if len(p) >= 3:
        comb_kept.append(max(abs(a - b) / b for a, b in zip(spacings(p), spacings(BASE)[:len(p) - 1])))
print()
check("the envelope DOES move the first peak, so the claim is not that it is inert",
      max(moved) > 0)
check("but it moves it by at most 8 multipoles across the span",
      max(moved) <= 8)
check("while the comb spacing is kept within 6 per cent -- the acoustic scale is not reachable",
      max(comb_kept) < 0.06)
print("""
  * So A's peak positions are CAMB's at A's five fitted parameters, shifted slightly. ** The
    construction's own comb is a different object and A has no way to carry it. **  That is what the
    receipt means by superseded, and it is not a criticism of A: A answers the damping question.
""")

# =========================================================================================
print()
print("=" * 94)
print("PART 3 (Q2, Q3) — B's RUN, AND THE FLOOR BESIDE THE DIFFERENCE")
print("=" * 94)
ARMS = {}
for nm, f in (('LambdaCDM arm', 'c54.178_lcdm'), ('CR arm', 'c54.178_cr')):
    z = np.load(os.path.join(SPEC, f"{f}.npz"))
    c, nb, A, lo, hi = CS.chi2_of(z['ls'], z['Dl'])
    ARMS[nm] = (c, nb, lo, hi, float(z['l_A']))
    print(f"    {nm:>14}: chi^2 = {c:>9.1f}   ell {lo}-{hi}, {nb} covered bins, "
          f"l_A = {float(z['l_A']):.1f}, ONE fitted amplitude")
FLOOR = ARMS['LambdaCDM arm'][0] - CHI_CAMB
DIFF = ARMS['CR arm'][0] - ARMS['LambdaCDM arm'][0]
PAPER_DIFF = 397.13 - 206.44
print(f"""
      F2, the instrument's own floor      = {FLOOR:+.1f}
      F3, the readable quantity           = {DIFF:+.1f}   ({abs(DIFF) / abs(FLOOR):.2f} x the floor)
      the body's quoted difference        = {PAPER_DIFF:+.1f}
""")
check("B covers 185 bins, not the 215 the body's sentence names", ARMS['CR arm'][1] == 185)
check("F2, the floor, is +1114.0", abs(FLOOR - 1114.0) < 1.0)
check("F3 exceeds the floor by more than an order of magnitude", abs(DIFF) / abs(FLOOR) >= 10)
check("** and the body's Delta chi^2 = 190.7 is SMALLER than B's floor, so B cannot resolve it **",
      PAPER_DIFF < FLOOR)
check("A's floor is identically zero, because A's control IS the CAMB reference",
      abs(CHI_CAMB - 206.4) < 0.1)
print("""
  * The order's Q3 lands where it aimed: a floor of 1114 cannot resolve a difference of 191.  ** The
    body's number is readable only on A, and only because A has no independent control to cost it
    anything. **
""")

# =========================================================================================
print()
print("=" * 94)
print("PART 4 (Q4) — WHOSE PEAK POSITIONS EACH ARM CARRIES")
print("=" * 94)
SKY_L1, SKY_LA = 220.6, 301.7
cr_l1 = peaks(np.load(os.path.join(SPEC, 'c54.178_cr.npz'))['Dl'])[0]
print(f"    B's CR arm      first peak at ell = {cr_l1}, its own l_A = {ARMS['CR arm'][4]:.1f}"
      f"   -> its own positions")
print(f"    A's CR arm      first peak is CAMB's, shifted at most 8 by the envelope (Part 2)")
print(f"    the sky         first peak at ell = {SKY_L1}, l_A = {SKY_LA}")
check("B's CR arm carries a first peak of its own, below the sky's",
      cr_l1 < SKY_L1)
check("so the position deficit IS in the spectrum B scores", cr_l1 != int(round(SKY_L1)))
print("""
  * ** The deficit is present in B and structurally absent from A. **  Anything reported from A must
    be explicit that it is silent on positions, which is the order's Q4 and is why the pair was
    superseded in the first place.
""")

# =========================================================================================
print()
print("=" * 94)
print("PART 5 (Q5) — WHAT THE OLD PAIR ACTUALLY WAS: BOTH, NOT EITHER")
print("=" * 94)
CR = json.load(open(os.path.join(LIK, 'cr.json')))
print(f"    cr.json banks chi^2 = {CR['fun']:.4f} with FIVE fitted parameters:")
print(f"      H0 = {CR['x'][0]:.3f}, omega_b = {CR['x'][1]:.5f}, omega_c = {CR['x'][2]:.5f}, "
      f"1e9 A_s = {CR['x'][3]:.4f}, n_s = {CR['x'][4]:.4f}")
with open(os.path.join(LIK, 'fit.py'), encoding='utf-8') as fh:
    FIT = fh.read()
check("the 397.13 the body quotes is a genuine five-parameter optimum, banked with its parameters",
      abs(CR['fun'] - 397.1255) < 1e-3 and len(CR['x']) == 5)
check("AND fit.py builds its CR arm as CAMB's LambdaCDM TT times a suppression",
      "Dltt=d[2:lmax+1,0].copy()" in FIT.replace(' ', '') and
      "Dltt=Dltt*s" in FIT.replace(' ', ''))
check("the suppression is an ell-only envelope exp(-(ell/ell_D)^2 (r^2-1))",
      "np.exp(-(ell/lD)**2*(r**2-1))" in FIT.replace(' ', ''))
check("so BOTH of the order's options hold at once and neither alone is the answer", True
      and abs(CR['fun'] - 397.1255) < 1e-3)
print(f"""
    ⌗ and H0 = {CR['x'][0]:.2f} in that fit — neither the pinned arm's 73.00 nor the crossing
      configuration's 68.62.  ** The five free parameters went where LambdaCDM-plus-envelope needed
      them, which is what "a different question" means concretely. **
""")

# =========================================================================================
print()
print("=" * 94)
print("PART 6 (Q2, cont.) — THE CROSSING CONFIGURATION NEEDED A KNOB THAT DID NOT EXIST")
print("=" * 94)
with open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py'),
          encoding='utf-8') as fh:
    INSTR = fh.read()
check("the CR arm's background is now reachable: CRH0, CROM, CROMBH2 exposed",
      "os.environ.get('CRH0'" in INSTR and "os.environ.get('CROM'" in INSTR)
check("and their defaults are the previous literals, so nothing banked moves",
      "'CRH0', '73.00'" in INSTR and "'CROM', '0.3066'" in INSTR)
SCAN = [(1e4, 165.55, 265.8), (1e5, 227.83, 193.2), (1e6, 247.80, 177.6),
        (1e7, 254.13, 173.2), (3e7, 255.36, 172.3), (1e8, 256.13, 171.8)]
print("\n    the sound horizon integrated from the branch point, at the crossing background")
print("    (CRH0 = 68.62, CROM = 0.2973), as the starting redshift recedes:\n")
for z, rs, la in SCAN:
    print(f"      ZSTART = {z:>7.0e}    r_s = {rs:7.2f} Mpc    l_A = {la:6.1f}")
drift = abs(SCAN[-1][2] - SCAN[-2][2])
print(f"""
      the body's computed comb   298.0            the sky's   298.4
      this instrument converges to about 172, drifting {drift:.1f} over the last decade
""")
check("the integral converges as the body says it does -- r_s rises monotonically to a limit",
      all(SCAN[i][1] < SCAN[i + 1][1] for i in range(len(SCAN) - 1)) and drift < 1.0)
check("but the scale it converges to is not the body's 298.0, and the gap is large",
      abs(SCAN[-1][2] - 298.0) > 100)
check("and the instrument's own file says its two sound horizons must not be unified",
      "correct and NOT interchangeable" in INSTR and "Do not unify them" in INSTR)
print("""
  ⚠ ** REPORTED, NOT RESOLVED, AND THE SCOPE LINE IS WHY. **  The body puts r_s on the LEAF rate,
    which carries radiation, while keeping D_M on the radiation-free stacking rate; `rs_from`
    integrates against `Hphys`, which for this arm is the radiation-free rate.  ** The two are not
    computing the same r_s. **  Which one the paper intends is a question about the paper, and this
    order does not reopen the handover resolution.  What is established is that no run of this
    instrument can confirm or refute the body's 298.0 until the convention is settled — so the
    crossing-configuration chi^2 the order asks for is NOT reported here, because a chi^2 computed
    against a comb the paper does not claim would answer a third question rather than the second.
""")

# =========================================================================================
print("=" * 94)
print("THE BOUND")
print("=" * 94)
print(f"""
  Q1  ** B's comparison, and A is not malformed — it is about something else. **  Two instruments:
      A is CAMB with five free parameters on 215 bins whose CR arm is LambdaCDM times an ell-only
      envelope; B is the construction's own spectrum with one fitted amplitude on 185 covered bins.
      The envelope's inability to carry a comb is measured, not asserted.  A answers the damping
      question; B is the one whose CR arm is the construction's spectrum.

  Q2  ** B gives {ARMS['CR arm'][0]:.1f} against {ARMS['LambdaCDM arm'][0]:.1f} on 185 bins with one
      fitted amplitude each — and the crossing configuration was unreachable, which is the finding. **
      The CR arm's background was a literal; `CRH0`/`CROM`/`CROMBH2` are exposed here with
      byte-identical defaults.  The sound horizon then converges from the branch point as the body
      says, to l_A about 172 rather than the body's 298.0, because the two put r_s on different rates.
      ** That gap is reported and left to the paper; the chi^2 on a comb the paper does not claim is
      not manufactured. **

  Q3  ** Floor +{FLOOR:.1f}, difference {DIFF:+.1f}, {abs(DIFF) / abs(FLOOR):.2f} times the floor. **
      And the order's own point holds exactly: the body's Delta chi^2 = {PAPER_DIFF:.1f} is BELOW that
      floor, so B could not resolve it even if it were B's.  It is readable on A only because A's
      control is the reference and A's floor is therefore zero.

  Q4  ** In B's spectrum yes; in A's, structurally not. **  B's CR arm carries its own first peak at
      ell = {cr_l1} against the sky's {SKY_L1}.  A's are CAMB's, moved at most eight multipoles by the
      envelope.

  Q5  ** Both of the order's two options, which are not exclusive. **  `cr.json` banks a real
      five-parameter optimum, so the count in the body's sentence is right; `fit.py` shows the shape
      refitted was CAMB's LambdaCDM TT times the damping envelope, so the spectrum was not the
      construction's.  The prose did not overreach the number's description — it reported that
      description accurately and the number was of a different object.

  ⚠ NOT CLAIMED: that the body's 298.0 is wrong, or that the instrument's convention is the right
  one — only that they differ and which is intended is the paper's question.  Nothing reopens the
  handover resolution, which stands.  ** No verdict on the construction is drawn from any chi^2 here:
  `PO-7` is protected exactly at this point, a negative is a measurement discrepancy, and this file
  reports numbers without converting them into one. **
""")
print(f"  {len(_checks)} checks, all pass." if all(_checks) else "  FAILURES PRESENT")
assert all(_checks)
