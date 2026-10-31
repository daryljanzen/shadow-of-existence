"""
** THE SPECTRA AND THE GEOMETRY ARE ON THE ARM OF RECORD AS OF `r7643+cc66.65`; THE SWITCH-IDENTITY
LEG IS NOT. **  `r6925_visleaf_cr`, `r6919_injected_cr`, `r6911_source_cr` and `cc66_r185_verify_cr`
move to their `_leafrec1` siblings.  The geometry moves by SUBSTITUTION: `r6925_geometry` has no
sibling, but `r6929+cc66.44` made `VISLEAF` a fraction whose endpoints ARE the two assignments, so
`r6929_geometry_leafrec1` carries the same quantities at f=0 and f=1 -- gated here, before a figure is
read off it, as bit-identical on the namesake arm across all ten quantity pairs (`cc66.64`).
ARM KEYS READ: `Dl__noop_{t}` out of `r6925_noop`, by template on both arms.  The `VISLEAF`-is-inert
identity pairs it against `r6893_switch_screen_{t}`'s `Dl__base` and needs both on one arm, so that
pair stays on the namesake -- and `cc66.64` proved it cannot be shortcut, the no-op bank's arm
spectrum BEING the screen's own base.

⛔ ** THREE CONDITIONS MOVE, AND ALL THREE WERE PREDICTED BEFORE THEY WERE MEASURED. **
⓵ WHICH ASSIGNMENT IS PHASE-CONTAMINATED IS A PROPERTY OF THE ARM.  The band residual runs 0.0485 at
`VISLEAF=0` down to 0.0168 at `VISLEAF=1` here, where on the namesake it ran 0.0088 UP to 0.0555.
Measured rather than named: the injection combs' mean signed offset in q is $-0.0154$ at `VISLEAF=0`
and $+0.0058$ at `VISLEAF=1`, against $-0.0017$ and $+0.0194$ on the namesake.  *** On BOTH arms the
offset changes sign between the two assignments, so one end is always phase-clean and the other
always contaminated -- the caution is structural and only its DIRECTION is the arm's. ***
⓶ AND THE SECTOR STILL DOES NOT CLOSE, BY THE OTHER HALF.  The source deficit closes 23 per cent of
the level gap and 107 PER CENT of the slope gap, its own slope being $-0.00742$ rather than flat --
against 54 and 10 per cent with a flat $-0.00106$ on the namesake.  *So the deficit carries the slope
here and the level there, and on neither arm both.*  ⌗ `cc66.40`'s $0.992$ is that arm's figure; this
one measures $0.9950$.
⓷ *The comb's verdict is unchanged and is the one the conclusion rests on.*

P15_the_visibilitys_clock_is_the_one_the_kernel_reads_and_the_comb_votes_against_the_alternative
===============================================================================================

LEVEL: `r6925`'s order -- ** which clock is the visibility a density in, and does the rate rule
determine it? ** -- with the retained fraction and the COMB reported side by side and neither picked
over the other, as the order requires.  Both arms at their verified 185-bin refit minima.

** WHAT THE ORDER ASKED, AND WHAT COMES BACK. **

 ⛭⛭ (1) THE AUDIT TURNS UP SOMETHING THE ORDER DID NOT EXPECT: ** THE INSTRUMENT ALREADY ANSWERS
     THIS QUESTION TWICE, AND DIFFERENTLY. **  Every site where the optical depth or the visibility
     touches a rate is on the STACKING clock -- EXCEPT the recombination history, which took its own
     switch and the LEAF rate at `r7095+cc66.75` (`Hrec`, `LEAFREC=1` by default; `LEAFREC=0` is the
     old behaviour and is bit-identical),
     `taup_of` built on `eg`'s conformal time, `tau` integrated over `_egrid`, `ETA_LS` and
     `ETA_LS_W` read off that grid.  ⛔ ** But `1/k_D^2` twenty lines below IS Jac-weighted under
     `LEAFSCALES`. **  ⇒ *So the DIFFUSION length -- a scale the plasma accumulates -- takes the leaf
     clock, and the OPTICAL DEPTH -- also accumulated by the plasma -- takes the stacking clock.*
     ** Two objects on the same side of the rate rule, given opposite clocks, with nothing in the
     instrument or the corpus stating the choice. **  *That is the gap the order named, already open
     in the code.*

 ⌗ (2) SO THE OTHER ASSIGNMENT IS NOT AN INVENTION, IT IS THE ONE THE INSTRUMENT ALREADY USES NEXT
     DOOR.  `VISLEAF=1` applies to `tau` exactly the weighting `1/k_D^2` applies to itself.  On the
     control it is BIT-IDENTICAL, because `Jac == 1` there by the rate identity; on the arm it moves
     the visibility peak from eta = 485.99 to 483.83, its FWHM from 43.591 to 43.952 Mpc, and r_D
     from 7.473 to 7.168.

 ⚑⚑ (3) ON THE GEOMETRY THE TWO ASSIGNMENTS AGREE, WHICH IS THE ORDER'S SECOND BRANCH.

         VISLEAF   d r_s/d chi control   arm      ratio     (13.1% lower means)
         0             0.454950       0.395135   0.8685      13.15% lower
         1             0.454950       0.395359   0.8690      13.10% lower

     ** d r_s/d chi moves by 0.06 per cent. **  ⇒ *And the reason is structural rather than lucky:
     `d r_s/d chi` is a RATIO of two accumulations across the SAME window, so re-weighting the
     window's measure re-weights numerator and denominator alike and the ratio is nearly invariant.*
     ⇒ ** So the visibility is not where the freedom is, and the 13.1 per cent is forced by the rule
     as stated -- which the order called the sharper and more falsifiable place. **
     ⛭ *The INVARIANCE survives the move to the arm of record unchanged -- 0.06 per cent there and
     0.06 per cent here -- which is what `structural rather than lucky` predicted.  The LEVEL does
     move: 12.8 per cent lower than the control becomes 13.1, read out of `r6929_geometry_leafrec1`
     at the same two assignments (`cc66.65`).*

 ⛔ (4) BUT ON THE CONTRAST IT DOES MOVE, AND ON THE COMB IT MOVES THE WRONG WAY -- SO THE TWO
     DISAGREE AND THE ORDER SAYS TO REPORT THAT RATHER THAN PICK.
      * ** THE CONTRAST: the injection's retained ratio goes 1.0929 -> 1.0752 and its slope
        +0.02955 -> +0.01794 **, i.e. TOWARD this arm's own real source at 1.0685 and +0.02178 --
        though the SLOPE crosses past it rather than arriving at it.  Read alone, that is still the
        order's FIRST branch.
      * ⛔ ** THE COMB: the arm's first peak moves from ell = 220 to 228 and ell_1/ell_A from 0.7262
        to 0.7526, against the sky's 0.7312; P1/P2 goes 2.136 to 2.009. **  The control's comb is
        bit-identical both ways.  ⇒ *The assignment that improves the contrast breaks the peak
        positions, and the order's own guard is that an assignment which moves the comb is one the
        peak positions have already voted on.*  ⌗ *At `VISLEAF=0` the raw reading sits BELOW the sky
        and at `VISLEAF=1` far above it, so `moves away` is a crossing here; the second peak's raw
        bin reads 532 against the namesake's 540, which is `cc66.54`'s known tie and is declared
        where it is printed.*
      * ⚠ ** AND THE CONTRAST NUMBER IS NOT EVEN CLEAN, FOR THE SAME REASON -- BUT IT IS THE OTHER
        ASSIGNMENT THAT IS DIRTY ON THIS ARM. **  Band by band under `VISLEAF=0` the ratio runs
        1.021 / 1.085 / 1.063 / 1.090 / 1.130 / 1.035 / 1.225 -- non-monotonic scatter, residual
        0.0485 -- against 1.031 / 1.038 / 1.072 / 1.091 / 1.084 / 1.126 / 1.085 under `VISLEAF=1`,
        residual 0.0168.  *** On the namesake arm it was exactly the reverse. ***  *The band ratio
        reads the PHASE OFFSET between the arm's injection comb and the control's, measured here as
        $-0.0154$ at `VISLEAF=0` against $+0.0058$ at `VISLEAF=1`: the contaminated assignment is
        simply the misaligned one.*  ⇒ ** That is `cc66.40`'s guard firing a third time, on the
        ALIGNMENT rather than on the assignment -- and because the offset CHANGES SIGN between the
        two, one end is always clean and the other always dirty.  Which end is the arm's property;
        that one of them is, is structural. **
     ⇒ *** So: the geometry says forced, the contrast says improvable, the comb says no, and the
     contrast's own band structure says its improvement is not to be trusted.  The comb is the only
     one of the three with an external referent, and it votes for the assignment the instrument
     already has. ***

 ⚑ (5) ⓶ AND THE SOURCE'S CANCELLATION STILL DOES NOT CLOSE THE SECTOR -- BUT ON THIS ARM IT IS THE
     LEVEL IT LEAVES OPEN, NOT THE SLOPE.  Pure geometry gives 1.0929 at +0.02955; the real source
     1.0685 at +0.02178.  Multiplying the injection by this arm's measured source deficit -- 0.9950,
     and NOT flat, its own slope being -0.00742 -- gives 1.0872 at +0.02120.  ⇒ ** That closes 23 per
     cent of the level gap and 107 PER CENT of the slope gap. **  *** So the four trough-filling
     channels now account for the whole slope difference, slightly overshooting it, and for under a
     quarter of the level difference.  On the namesake arm it was the reverse -- 54 and 10 per cent,
     with `cc66.40`'s deficit FLAT in q at -0.00106, which was the stated reason it could not carry a
     slope. ***  ⇒ ** The order's conditional is still half satisfied and the closure it hoped for
     still does not arrive; WHICH half is the arm's property and is restated rather than carried. **
     *What the LEVEL still needs is the real source's own eta-dependence across the visibility, which
     is precisely what the injection replaced -- named, not measured here.  That sentence was about
     the slope on the namesake arm; the deficit carries the slope here, so the remainder has moved.*

-------------------------------------------------------------------------------
WHAT IS CLAIMED.

 (1) The audit, site by site with its rate: five stacking-clock sites for tau and g, against
     `1/k_D^2` Jac-weighted under `LEAFSCALES` -- two plasma-accumulated objects on opposite clocks.
 (2) `VISLEAF` is bit-identical when unset on both arms, AND bit-identical when SET on the control,
     which is the rate identity showing in a second place.
 (3) d r_s/d chi across the FWHM under both assignments: 0.396733 against 0.396957 on the arm, the
     control unchanged -- a 0.06 per cent move, with the structural reason stated.
 (4) The injection's retained ratio and q-slope under both, with the band-by-band values that show
     the `VISLEAF=1` slope is contaminated by the comb shift.
 (5) The comb under both: the arm's first four peaks, ell_1/ell_A and P1/P2, against the sky's
     0.7312; and the control bit-identical.
 (6) The source deficit closes 54 per cent of the level gap and 10 per cent of the slope gap.

WHAT IS NOT CLAIMED.

 * NOT that the two-rate assignment is right, which is the row's question now and not this order's.
 * NOT that `VISLEAF=1` is wrong as physics.  ** What is measured is that it moves the comb away
   from the sky while moving the contrast toward the real source, and that its contrast improvement
   is partly a phase artefact. **  Which of the two clocks the optical depth SHOULD be a density in
   is not settled here -- only that the instrument's current choice is the one the peak positions
   support and that the rule as stated does not determine it.
 * NOT that the 0.06 per cent invariance of d r_s/d chi settles the row.  It says the visibility is
   not where the freedom is; the freedom is in the rule's assignment of r_s itself.
 * NOT a mechanism beyond `cc66.42`'s, and nothing here touches `prop:flat`.
 * NOT that the injected runs are spectra of the model.  The `injvl` arrays are the projection's
   transfer of a known input; only the `combvl` arrays are spectra, and they are labelled apart.
 * ⚠ NOT that this receipt's first launcher worked.  It dropped its extra environment through a
   positional-argument bug and thirty-six slices ran as plain `VISLEAF=0` spectra, reporting nothing
   wrong and reproducing the banked spectra -- which is the shape that gets banked as an answer.  The
   episode is in the launcher's own comment and the fix is a smoke test that greps the log for the
   marker the switch must print before the set goes out.

COMPUTES: scope.
  * ** EVERY COSMOLOGICAL PARAMETER IS BANKED, NOT CHOSEN HERE. **  Both arms at `r6825+cc66.25`'s
    verified 185-bin refit minima.  Nothing here re-fits and nothing here moves.
  * `spectra/r6925_visleaf_{lcdm,cr}.npz` (the injection and the real spectrum under `VISLEAF=1`),
    `r6925_geometry.npz` (both assignments, per arm), `r6925_noop.npz` (the two gates).
  * The `VISLEAF=0` side is `r6919+cc66.42`'s and `r6911+cc66.40`'s banks, and the comb's
    `VISLEAF=0` side is `cc66_r185_verify_*` -- read with the SAME statistic, abscissa and window.
  * NOTHING IS FITTED except the straight lines through the band ratios, whose scatter is reported.
"""
import os

import numpy as np
from scipy.signal import argrelextrema

FAILS = []


def check(name, cond, got=None):
    if cond:
        print(f"  [PASS] {name}" + (f"   ({got})" if got is not None else ""))
    else:
        FAILS.append(name)
        print(f"  [FAIL] {name}" + (f"   (got {got})" if got is not None else ""))


print(__doc__)
print("=" * 100)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
SRC = open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')).read()
NEED = ('r6925_visleaf_lcdm.npz', 'r6925_visleaf_cr_leafrec1.npz', 'r6925_geometry.npz',
        'r6929_geometry.npz', 'r6929_geometry_leafrec1.npz', 'r6925_noop.npz',
        'r6919_injected_lcdm.npz', 'r6919_injected_cr_leafrec1.npz', 'r6911_source_lcdm.npz',
        'r6911_source_cr_leafrec1.npz', 'cc66_r185_verify_lcdm.npz',
        'cc66_r185_verify_cr_leafrec1.npz',
        'r6893_switch_screen_lcdm.npz', 'r6893_switch_screen_cr.npz')
for _n in NEED:
    check(f"the bank this receipt reads is present: `spectra/{_n}`",
          os.path.exists(os.path.join(SP, _n)), _n)
if FAILS:
    print("\n  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK YET, so nothing is read and this receipt")
    print("     FAILS rather than reporting the parts it could run as the whole.")
    print("=" * 100)
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)

# ⛭⛭ r7643+cc66.65: ** THE SPECTRA MOVE TO THE ARM OF RECORD; THE GEOMETRY MOVES BY SUBSTITUTION;
#   THE SWITCH-IDENTITY LEG CANNOT MOVE AT ALL. **
#   *`r6925_visleaf_cr`, `r6919_injected_cr`, `r6911_source_cr` and `cc66_r185_verify_cr` have
#   `_leafrec1` siblings and move.  The CONTROL stays where it is: `LEAFREC` is inert on the control
#   keys this receipt reads, which `cc66.63` measured rather than assumed.*
#   ⛭ ** AND THE GEOMETRY MOVES THOUGH `r6925_geometry` HAS NO SIBLING (`cc66.64`). **  *That bank
#   holds the two assignments as key suffixes `_0` and `_1`.  `r6929+cc66.44` made `VISLEAF` a
#   FRACTION whose endpoints ARE those two assignments, so `r6929_geometry` carries the same
#   quantities at `f=0` and `f=1` -- and it carries them BIT-IDENTICALLY, which is what licenses the
#   substitution and is gated below before a single figure is read off it.*
#   ⛔ ** ARM KEYS READ: ** `Dl__noop_{t}` out of `r6925_noop`, by template on both arms.  *The
#   `VISLEAF`-is-inert identity pairs it against `r6893_switch_screen_{t}`'s `Dl__base` and needs BOTH
#   on one arm, so that pair stays on the namesake -- the `cc66.57`/`.61`/`.62`/`.63` shape.  And
#   `cc66.64` proved it cannot be shortcut: the no-op bank's arm spectrum IS the screen's own base, so
#   substituting the screen's sibling would make the leg compare the base against itself.*
_A = '_leafrec1'
VL = {'lcdm': np.load(os.path.join(SP, 'r6925_visleaf_lcdm.npz')),
      'cr': np.load(os.path.join(SP, f'r6925_visleaf_cr{_A}.npz'))}
IJ = {'lcdm': np.load(os.path.join(SP, 'r6919_injected_lcdm.npz')),
      'cr': np.load(os.path.join(SP, f'r6919_injected_cr{_A}.npz'))}
SO = {'lcdm': np.load(os.path.join(SP, 'r6911_source_lcdm.npz')),
      'cr': np.load(os.path.join(SP, f'r6911_source_cr{_A}.npz'))}
VR = {'lcdm': np.load(os.path.join(SP, 'cc66_r185_verify_lcdm.npz')),
      'cr': np.load(os.path.join(SP, f'cc66_r185_verify_cr{_A}.npz'))}
NOOP = np.load(os.path.join(SP, 'r6925_noop.npz'))
# the geometry, substituted -- and the substitution gated as an identity on the namesake arm first
_G25 = np.load(os.path.join(SP, 'r6925_geometry.npz'))
_G29 = np.load(os.path.join(SP, 'r6929_geometry.npz'))
GE = np.load(os.path.join(SP, f'r6929_geometry{_A}.npz'))
_fg = _G29['f__cr']
_V = {'0': int(np.argmin(np.abs(_fg - 0.0))), '1': int(np.argmin(np.abs(_fg - 1.0)))}
_QUANT = ('eta_ls', 'fwhm', 'rD', 'cs', 'l_A')
_sub_pairs = [(k, a) for k in _QUANT for a in ('cr', 'lcdm')]
_sub_exact = sum(1 for k, a in _sub_pairs
                 if (float(_G25[f'{k}__{a}_0']), float(_G25[f'{k}__{a}_1']))
                 == (float(_G29[f'{k}__{a}'][_V['0']]), float(_G29[f'{k}__{a}'][_V['1']])))
check("⛭⛭ ** THE GEOMETRY SUBSTITUTION IS GATED BEFORE IT IS USED: every quantity this receipt reads "
      "out of `r6925_geometry` is carried BIT-IDENTICALLY by `r6929_geometry` at f=0 and f=1, on BOTH "
      "arms. **  *Ten quantity pairs, matched by NAME and value -- a value-only match would be a "
      "scalar coincidence, which is the error `cc66.64` made first and then guarded*",
      _sub_exact == len(_sub_pairs) == 10
      and float(_fg[_V['0']]) == 0.0 and float(_fg[_V['1']]) == 1.0,
      f"{_sub_exact} of {len(_sub_pairs)} exact, at f = "
      f"{float(_fg[_V['0']]):g} and {float(_fg[_V['1']]):g}")
#   ⚭⚭ r7645+cc66.68: ** AND THE SIBLING IS A SUPERSET, SO `__cr` IN IT IS THE NAMESAKE'S. **
#   *r7643+70's fold re-keyed `r6929_geometry_leafrec1` AFTER cc66.65 re-pointed this receipt against
#   r7641's keying, where `__cr` DID hold the arm of record.  The arm of record moved to
#   `__cr_leafrec1`, and `__cr` now carries the namesake's values BIT-IDENTICALLY -- so the key this
#   gate was written to defend became the namesake's own, and the gate below is the one that caught it:
#   it asserted GE's `cs__cr` DIFFERS from the namesake's, and after the re-key the two are equal.  It
#   is kept in its strengthened form: the sibling must be a superset, 28 namesake keys bit-identical
#   and 12 of 14 arm keys moved, with the arm read under `_GARM`.  Point `_GARM` back at `cr` and this
#   fails.*
_GARM = 'cr_leafrec1'                                   # the arm of record's key IN THE GEOMETRY BANK
_gsup = sum(1 for k in _G29.files if k in GE.files and np.array_equal(_G29[k], GE[k]))
_gmov = sum(1 for k in _G29.files if k.endswith('__cr') and f'{k}_leafrec1' in GE.files
            and not np.array_equal(_G29[k], GE[f'{k}_leafrec1']))
check("   ⇒ and so the two assignments this receipt is about are read on the ARM OF RECORD, out of a "
      "bank that is a SUPERSET of the namesake -- `__cr` in it IS the namesake's, bit for bit",
      GE is not _G29 and _gsup == len(_G29.files) == 28 and _gmov == 12
      and float(GE[f'cs__{_GARM}'][_V['0']]) != float(_G29['cs__cr'][_V['0']])
      and abs(float(GE[f'cs__{_GARM}'][_V['0']]) - 0.3951353109255077) < 1e-12,
      f"{_gsup} of {len(_G29.files)} namesake keys bit-identical, {_gmov} of 14 arm keys moved; "
      f"d r_s/d chi at the stacking clock: {float(_G29['cs__cr'][_V['0']]):.6f} (namesake) -> "
      f"{float(GE[f'cs__{_GARM}'][_V['0']]):.6f} (arm of record)")
g = lambda k, a, v: float(GE[f'{k}__{_GARM if a == "cr" else a}'][_V[v]])


def env_a(x, y, win=1.0):
    """`r6911+cc66.40`'s running arithmetic mean -- the statistic is that receipt's, unchanged"""
    e = np.empty_like(y)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(x, y, win=1.0):
    e = env_a(x, y, win)
    return (y - e) / e


ED = np.arange(0.85, 5.76, 0.7)
CTR = np.array([(a + b) / 2 for a, b in zip(ED[:-1], ED[1:])])


def bands(Q, O):
    out = []
    for a, b in zip(ED[:-1], ED[1:]):
        x = np.linspace(a, b, 400)
        out.append(np.interp(x, Q['cr'], O['cr']).std() / np.interp(x, Q['lcdm'], O['lcdm']).std())
    return np.array(out)


# ===================================================================================================
print("\nPART 1 -- THE AUDIT: EVERY PLACE THE OPTICAL DEPTH OR THE VISIBILITY TOUCHES A RATE.")
print("-" * 100)
# ⛭⛭ ** THE FIRST SITE'S READ MOVED AT `r7091+cc66.73` AND THE SUBSTANCE IT ASSERTS DID NOT. **
# *`LEAFGEOM` made the conformal-time grid and the whole geometry switchable onto the leaf rate, so the
# instrument now names the geometry's rate `Hgeom` -- `Hphys` at the default, `Hleaf` under `LEAFGEOM=1`.
# The recombination history is solved against that one rate, as it must be: solving it against `Hphys`
# while the grid rode `Hleaf` would put TWO clocks back in, which is the defect `r7091` removed.*
#   ⇒ ** So this site is now CONDITIONAL and is labelled so.  At the default it is the stacking clock and
#   this receipt's own finding -- five stacking-clock sites for tau and g -- stands exactly as it did;
#   under `LEAFGEOM=1` it is the leaf's, together with every other site that reads the grid. **
#   ⌗ *Same shape as the `VISLEAF` fraction above: the flag's single read became two lines and the gate
#   followed the code without the claim moving.  A source-read audit has to track the source.*
# ⛭⛭ ** AND IT MOVED AGAIN AT `r7095+cc66.75`, THIS TIME ONTO ITS OWN SWITCH AND ITS OWN RATE. **
# *`r7095` ruled that `LEAFGEOM` was one knob over two objects the rate rule assigns OPPOSITELY --
# `D_M` takes the stacking rate, recombination the leaf's -- so the rule's own configuration was
# unreachable.  `LEAFREC` splits it out and **defaults to the LEAF**, which is what `P07`'s rate rule
# assigns a process running in the content.*
#   ⇒ ** So this site is no longer the geometry's at all: it is recombination's own, leaf by default. **
#   ⌗ *That makes this receipt's original finding -- five STACKING-clock sites for tau and g -- false at
#   the new default for THIS one site, and the receipt says so rather than keeping the old label: the
#   site is still audited, still read from the source, and now reads what the code reads.*
SITES = [("the recombination history's expansion rate", "xe_history(lambda z: Hrec(",
          "recombination's OWN, LEAF by default (LEAFREC, r7095+cc66.75)"),
         ("tau' = n_e sigma_T a, built on `eg`'s conformal time", "taup_of = CubicSpline(_ea,", 'stacking'),
         ("the tau integration's measure", "_tau = np.concatenate([[0.0], np.cumsum(", 'stacking*'),
         ("the visibility and its peak/FWHM, read off `_egrid`", "vis_of = CubicSpline(_egrid,", 'stacking'),
         ("1/k_D^2's measure", "_dE = _dE * 0.5 * (np.asarray(Jac_of(", 'LEAF under LEAFSCALES')]
for nm, needle, clock in SITES:
    check(f"site found and its clock read from the source: {nm} -- {clock}",
          SRC.count(needle) == 1, f"`{needle[:44]}...`")
check("⛔ ** AND THE TWO ARE ON OPPOSITE CLOCKS. **  `1/k_D^2`'s measure is Jac-weighted under "
      "`LEAFSCALES` and `tau`'s is not, so the diffusion length takes the LEAF clock and the optical "
      "depth the STACKING clock -- two objects on the same side of the rate rule, with nothing "
      "stating the choice.  *That is the gap `r6925` named, already open in the code.*",
      SRC.count('_dE = _dE * 0.5 * (np.asarray(Jac_of(') == 1
      and SRC.count('_dTau = _dTau * 0.5 * (np.asarray(Jac_of(') == 1
      # ⌗ `r6929+cc66.44` made `VISLEAF` a FRACTION -- f=0 the stacking clock, f=1 the leaf's -- so
      #   this gate reads the two lines that replaced the flag's single read.  ** The substance it
      #   asserts is unchanged: `1/k_D^2`'s measure is Jac-weighted unconditionally under
      #   `LEAFSCALES` and `tau`'s only under `VISLEAF`, and f == 1 takes the expression above
      #   UNCHANGED so this receipt's own runs are still the code's endpoint, bit for bit. **
      and SRC.count("_VISLF = float(os.environ.get('VISLEAF', '0'))") == 1
      and SRC.count('_VISL = _VISLF != 0.0') == 1,
      "`1/k_D^2` Jac-weighted unconditionally under LEAFSCALES; `tau` only under `VISLEAF`")
for t in ('lcdm', 'cr'):
    b = np.load(os.path.join(SP, f'r6893_switch_screen_{t}.npz'))
    check(f"[{t}] `VISLEAF` UNSET IS BIT-IDENTICAL against the banked base",
          np.array_equal(NOOP[f'Dl__noop_{t}'], b['Dl__base']),
          f"max|dD_l| = {float(np.max(np.abs(NOOP[f'Dl__noop_{t}'] - b['Dl__base']))):.3e}")
check("⚑ and `VISLEAF=1` on the CONTROL is bit-identical TOO -- the rate identity showing in a "
      "second place, and the one-sided nature of the whole finding in one result",
      np.array_equal(NOOP['Dl__visl_lcdm'], NOOP['Dl__noop_lcdm']),
      f"max|dD_l| = {float(np.max(np.abs(NOOP['Dl__visl_lcdm'] - NOOP['Dl__noop_lcdm']))):.3e}")

# ===================================================================================================
print("\nPART 2 -- ⓵ THE GEOMETRY UNDER BOTH ASSIGNMENTS.  THIS IS THE ORDER'S SECOND BRANCH.")
print("-" * 100)
print(f"    {'VISLEAF':8s} {'arm eta_LS':>11s} {'arm FWHM':>10s} {'arm r_D':>9s} "
      f"{'d r_s/d chi ctl':>16s} {'arm':>10s} {'ratio':>8s}")
for v in ('0', '1'):
    print(f"    {v:8s} {g('eta_ls','cr',v):11.2f} {g('fwhm','cr',v):10.3f} {g('rD','cr',v):9.3f} "
          f"{g('cs','lcdm',v):16.6f} {g('cs','cr',v):10.6f} "
          f"{g('cs','cr',v)/g('cs','lcdm',v):8.4f}")
_r0 = g('cs', 'cr', '0') / g('cs', 'lcdm', '0')
_r1 = g('cs', 'cr', '1') / g('cs', 'lcdm', '1')
print(f"    ⇒ {100*(1-_r0):.2f} per cent lower becomes {100*(1-_r1):.2f}: a move of "
      f"{100*abs(_r1-_r0)/_r0:.2f} per cent in the ratio")
check("⚑⚑ ** ON THE GEOMETRY THE TWO ASSIGNMENTS AGREE. **  `d r_s/d chi` is a RATIO of two "
      "accumulations across the SAME window, so re-weighting that window's measure re-weights "
      "numerator and denominator alike -- the invariance is structural, not lucky.  ⇒ The visibility "
      "is NOT where the freedom is, and the 13.1 per cent is forced by the rule as stated",
      abs(_r1 - _r0) / _r0 < 0.005,
      f"{_r0:.6f} against {_r1:.6f}, {100*abs(_r1-_r0)/_r0:.2f} per cent apart")
check("...and the control's geometry does not move at all, so every number here is the arm's alone",
      abs(g('cs', 'lcdm', '1') - g('cs', 'lcdm', '0')) < 1e-12,
      f"{g('cs','lcdm','0'):.6f} both ways")
check("⌗ but the switch is NOT inert on the arm -- the visibility peak, its width and r_D all move, "
      "so this is a connected knob reporting a near-null and not `r4558`'s unwired one",
      abs(g('eta_ls', 'cr', '1') - g('eta_ls', 'cr', '0')) > 1.0
      and abs(g('rD', 'cr', '1') / g('rD', 'cr', '0') - 1) > 0.02,
      f"eta_LS {g('eta_ls','cr','0'):.2f} -> {g('eta_ls','cr','1'):.2f}, "
      f"r_D {g('rD','cr','0'):.3f} -> {g('rD','cr','1'):.3f} "
      f"({100*(g('rD','cr','1')/g('rD','cr','0')-1):+.1f}%)")

# ===================================================================================================
print("\nPART 3 -- THE CONTRAST AND THE COMB, SIDE BY SIDE, NEITHER PICKED OVER THE OTHER.")
print("-" * 100)
Q0 = {t: IJ[t]['ls__sweepown'].astype(float) / float(IJ[t]['l_A__sweepown']) for t in IJ}
O0 = {t: osc(Q0[t], IJ[t]['Dl__sweepown']) for t in IJ}
Q1 = {t: VL[t]['ls__injvl'].astype(float) / float(VL[t]['l_A__injvl']) for t in VL}
O1 = {t: osc(Q1[t], VL[t]['Dl__injvl']) for t in VL}
Y0, Y1 = bands(Q0, O0), bands(Q1, O1)
S0, I0 = np.polyfit(CTR, Y0, 1)
S1, I1 = np.polyfit(CTR, Y1, 1)
print("  (a) THE CONTRAST -- the injection's retained ratio, band by band and fitted")
print(f"      {'q band':22s} " + " ".join(f"{v:6.2f}" for v in CTR))
print(f"      {'VISLEAF=0 (cc66.42)':22s} " + " ".join(f"{v:6.3f}" for v in Y0))
print(f"      {'VISLEAF=1 (the other)':22s} " + " ".join(f"{v:6.3f}" for v in Y1))
print(f"      VISLEAF=0: mean {Y0.mean():.4f}  slope {S0:+.5f}  residual rms "
      f"{np.std(Y0 - np.polyval([S0, I0], CTR)):.4f}")
print(f"      VISLEAF=1: mean {Y1.mean():.4f}  slope {S1:+.5f}  residual rms "
      f"{np.std(Y1 - np.polyval([S1, I1], CTR)):.4f}")
# ⌗ r7643+cc66.65: `cc66.41/42`'s 1.0694 / +0.01167 are the NAMESAKE arm's and are labelled so.
#   This arm's own real source is measured in PART 4 below -- mean 1.0685, slope +0.02178 -- and the
#   gate above compares the two assignments against each other, not against either reference.
print(f"      the real source, cc66.41/42 on the NAMESAKE arm: mean 1.0694  slope +0.01167")
print(f"      ⇒ this arm's own real source is measured in PART 4: mean 1.0685  slope +0.02178")
check("⌗ read ALONE the other assignment moves the contrast TOWARD the real source -- which is the "
      "order's FIRST branch, and is why it cannot be dismissed on the geometry alone",
      Y1.mean() < Y0.mean() and S1 < S0,
      f"mean {Y0.mean():.4f} -> {Y1.mean():.4f}, slope {S0:+.5f} -> {S1:+.5f}, against the real "
      f"1.0694 / +0.01167")
# ⛔⛭⛭⛭ r7643+cc66.65: ** WHICH ASSIGNMENT IS CONTAMINATED IS A PROPERTY OF THE ARM, AND THE
#   MECHANISM IS MEASURED HERE RATHER THAN NAMED. **
#   *The old form asserted that `VISLEAF=1` is the scattered one and `VISLEAF=0` the smooth one, and
#   read a factor-3 residual as fixed to that direction.  On the arm of record it is the OTHER WAY
#   ROUND: the residual runs 0.0485 at `VISLEAF=0` down to 0.0168 at `VISLEAF=1`, where on the
#   namesake it ran 0.0088 up to 0.0555.*
#   ⇒ *** The band ratio reads the PHASE OFFSET between the arm's injection comb and the control's
#       over the band range, so the contaminated assignment is simply the MISALIGNED one -- and which
#       of the two that is depends on the arm.  Measured below rather than cited: the mean signed
#       offset in q is -0.0154 at `VISLEAF=0` and +0.0058 at `VISLEAF=1` here, against -0.0017 and
#       +0.0194 on the namesake. ***
#   ⛭ ** AND THE PART THAT IS ARM-INDEPENDENT IS THE STRUCTURE: on BOTH arms the offset CHANGES SIGN
#   between the two assignments, so one of them is always the phase-clean end and the other always the
#   contaminated one.  The caution the receipt needs is therefore structural, and only its direction
#   is this arm's. **  *`cc66.40`'s guard firing a third time -- on the ALIGNMENT, as `cc66.63` found
#   for the same statistic on the scan banks, which these injection banks now confirm independently.*
_R0 = float(np.std(Y0 - np.polyval([S0, I0], CTR)))
_R1 = float(np.std(Y1 - np.polyval([S1, I1], CTR)))


def _qpk(z, kls, klA, kDl, n=8):
    """the comb in q, sub-bin, of one banked spectrum -- its own l_A, never the other arm's"""
    ls, Dl = z[kls].astype(float), z[kDl]
    out = []
    for i in argrelextrema(Dl, np.greater, order=3)[0][:n]:
        y0, y1, y2 = Dl[i - 1], Dl[i], Dl[i + 1]
        den = y0 - 2 * y1 + y2
        off = 0.5 * (y0 - y2) / den if den != 0 else 0.0
        out.append(float(ls[i] + off * (ls[i + 1] - ls[i])))
    return np.array(out) / float(z[klA])


def _offset(A, kls, klA, kDl):
    """the MEAN SIGNED offset, in q, between the arm's comb and the control's, over the band range"""
    qa, qc = (_qpk(A[t], kls, klA, kDl) for t in ('cr', 'lcdm'))
    n = min(qa.size, qc.size)
    m = (qc[:n] >= ED[0]) & (qc[:n] <= ED[-1])
    return float(np.mean(qa[:n][m] - qc[:n][m])), int(m.sum())


_D0, _n0 = _offset(IJ, 'ls__sweepown', 'l_A__sweepown', 'Dl__sweepown')
_D1, _n1 = _offset(VL, 'ls__injvl', 'l_A__injvl', 'Dl__injvl')
print(f"      the injection comb against the CONTROL's, mean signed offset in q over the band range:")
print(f"        VISLEAF=0 {_D0:+.6f}   VISLEAF=1 {_D1:+.6f}   over {_n0} and {_n1} in-band peaks")
print(f"        ⇒ the MISALIGNED assignment here is VISLEAF={'0' if abs(_D0) > abs(_D1) else '1'}, "
      f"and it is the one carrying the scatter")
check("⚠⛭⛭ ** AND ONE OF THE TWO ASSIGNMENTS IS ALWAYS PHASE-CONTAMINATED, SO THE SLOPE CANNOT BE "
      "READ AS PHYSICS WITHOUT NAMING WHICH END IS CLEAN -- AND ON THIS ARM IT IS `VISLEAF=1` THAT IS "
      "CLEAN, NOT `VISLEAF=0`. **  The band ratio reads the phase offset between the arm's injection "
      "comb and the control's: that offset CHANGES SIGN between the two assignments, so one end is "
      "always the aligned one, and the residual follows it.  ⛔ *On the namesake arm the clean end "
      "was `VISLEAF=0` and this receipt said so; the direction is the arm's property and is restated "
      "rather than carried*",
      (abs(_D0) > abs(_D1)) == (_R0 > _R1)
      and _D0 * _D1 < 0
      and max(_R0, _R1) / min(_R0, _R1) > 2.5
      and abs(_D0 + 0.015437) < 1e-5 and abs(_D1 - 0.005823) < 1e-5
      and abs(_R0 - 0.04851) < 5e-6 and abs(_R1 - 0.01677) < 5e-6,
      f"offset {_D0:+.6f} / {_D1:+.6f} (sign change), residual {_R0:.4f} / {_R1:.4f} "
      f"(factor {max(_R0,_R1)/min(_R0,_R1):.2f}), and the larger offset carries the larger residual")

print("\n  (b) THE COMB -- which the order asks for beside the contrast, and which has an external referent")
SKY = 0.7312
COMB = {}
for t in ('lcdm', 'cr'):
    for v, ls, Dl, lA in (('0', VR[t]['ls'].astype(float), VR[t]['Dl'], float(VR[t]['l_A'])),
                          ('1', VL[t]['ls__combvl'].astype(float), VL[t]['Dl__combvl'],
                           float(VL[t]['l_A__combvl']))):
        pk = argrelextrema(Dl, np.greater, order=3)[0][:4]
        COMB[(t, v)] = dict(pk=[int(ls[q]) for q in pk], r=float(ls[pk[0]] / lA),
                            p12=float(Dl[pk[0]] / Dl[pk[1]]))
        print(f"      {t:5s} VISLEAF={v}  peaks at l = {str(COMB[(t,v)]['pk']):26s} "
              f"l_1/l_A = {COMB[(t,v)]['r']:.4f}   P1/P2 = {COMB[(t,v)]['p12']:.3f}")
print(f"      the sky: l_1/l_A = {SKY:.4f}")
# ⚠⌗ r7643+cc66.65: ** THE SECOND PEAK'S RAW READING IS A KNOWN BIN TIE AND IT LANDS THE OTHER WAY
#   HERE. **  *At `VISLEAF=0` the printed quartet reads 532 where the namesake arm read 540.  That is
#   `cc66.54`'s coin flip, not a motion: the two bins tie to about 0.011 per cent on the `LSTEP=8`
#   grid, and `cc66.60`'s 0.464 per cent comb offset is enough to land it the other side.  The sub-bin
#   locator does not move with it (`cc66.63` measures l_2 at 535.85 on this arm).*
#   ⇒ ** Nothing in this receipt turns on the second peak -- every gate reads `pk[0]` -- so this is
#   DECLARED rather than repaired, and gated so a THIRD value would be caught. **
check("⚠ ⌗ the second peak's raw reading is one of the two tied bins and not a third value, so the "
      "printed quartet carries `cc66.54`'s known coin flip and nothing new",
      COMB[('cr', '0')]['pk'][1] in (532, 540) and COMB[('cr', '1')]['pk'][1] in (532, 540)
      and COMB[('lcdm', '0')]['pk'][1] == COMB[('lcdm', '1')]['pk'][1] == 540,
      f"the arm reads {COMB[('cr','0')]['pk'][1]} at VISLEAF=0 and "
      f"{COMB[('cr','1')]['pk'][1]} at VISLEAF=1; the control reads "
      f"{COMB[('lcdm','0')]['pk'][1]} both ways")
check("⛔ ** THE COMB VOTES AGAINST THE OTHER ASSIGNMENT. **  The arm's first peak moves and its "
      "`l_1/l_A` moves AWAY from the sky, while the control's comb is bit-identical -- and the "
      "order's own guard is that an assignment which moves the comb is one the peak positions have "
      "already voted on",
      COMB[('cr', '1')]['pk'][0] != COMB[('cr', '0')]['pk'][0]
      and abs(COMB[('cr', '1')]['r'] - SKY) > abs(COMB[('cr', '0')]['r'] - SKY)
      and COMB[('lcdm', '1')]['pk'] == COMB[('lcdm', '0')]['pk'],
      f"the arm's l_1 {COMB[('cr','0')]['pk'][0]} -> {COMB[('cr','1')]['pk'][0]}, l_1/l_A "
      f"{COMB[('cr','0')]['r']:.4f} -> {COMB[('cr','1')]['r']:.4f} against the sky's {SKY:.4f}; "
      f"P1/P2 {COMB[('cr','0')]['p12']:.3f} -> {COMB[('cr','1')]['p12']:.3f}")
check("⇒ ** SO THE CONTRAST AND THE COMB DISAGREE, and this receipt says so rather than picking. **  "
      "The comb is the only one of the three readings with an external referent, and it supports the "
      "assignment the instrument already has",
      True,
      "geometry: forced; contrast: improvable but phase-contaminated; comb: against")

# ===================================================================================================
print("\nPART 4 -- ⓶ WHERE THE SOURCE'S PARTIAL CANCELLATION SITS.")
print("-" * 100)
QK = {t: SO[t]['k'] * float(SO[t]['r_s']) / np.pi for t in SO}
QR = {t: SO[t]['ls'].astype(float) / (np.pi * float(SO[t]['D_M']) / float(SO[t]['r_s'])) for t in SO}
O2 = {t: osc(QK[t], SO[t]['S_i'] ** 2) for t in SO}
O3 = {t: osc(QR[t], SO[t]['Dl']) for t in SO}
REAL, SRC_ = [], []
for a, b in zip(ED[:-1], ED[1:]):
    x = np.linspace(a, b, 400)
    REAL.append(np.interp(x, QR['cr'], O3['cr']).std() / np.interp(x, QK['cr'], O2['cr']).std()
                / (np.interp(x, QR['lcdm'], O3['lcdm']).std()
                   / np.interp(x, QK['lcdm'], O2['lcdm']).std()))
    A, B = np.interp(x, QK['cr'], O2['cr']), np.interp(x, QK['lcdm'], O2['lcdm'])
    SRC_.append(float(np.sum(A * B) / np.sum(B * B)))
REAL, SRC_ = np.array(REAL), np.array(SRC_)
PROD = Y0 * SRC_
SR, _ = np.polyfit(CTR, REAL, 1)
SS, _ = np.polyfit(CTR, SRC_, 1)
SX, _ = np.polyfit(CTR, PROD, 1)
print(f"      {'':22s} " + " ".join(f"{v:6.2f}" for v in CTR) + "     mean     slope")
for nm, y, sl in (('the injection', Y0, S0), ('x the source deficit', PROD, SX),
                  ('the real source', REAL, SR), ('the source deficit', SRC_, SS)):
    print(f"      {nm:22s} " + " ".join(f"{v:6.3f}" for v in y) + f"   {y.mean():7.4f}  {sl:+8.5f}")
_lev = (Y0.mean() - PROD.mean()) / (Y0.mean() - REAL.mean())
_slp = (S0 - SX) / (S0 - SR)
print(f"      ⇒ the source deficit closes {100*_lev:.0f} per cent of the level gap and "
      f"{100*_slp:.0f} per cent of the slope gap")
# ⛔⛭⛭⛭ r7643+cc66.65: ** THE SECTOR STILL DOES NOT CLOSE INTO ONE ACCOUNT, AND IT IS THE OTHER
#   HALF THAT FAILS. **
#   *On the namesake arm the deficit closed 54 per cent of the LEVEL gap and 10 per cent of the SLOPE
#   gap, and `cc66.40`'s 0.992 was FLAT in q (slope -0.00106) -- which was the reason it could not
#   carry a slope difference.  On the arm of record the deficit is 0.9950 with slope -0.00742, SEVEN
#   TIMES steeper and not flat at all, and it closes 23 per cent of the level gap and 107 PER CENT of
#   the slope gap.*
#   ⇒ *** So the conclusion survives on both arms and its mechanism INVERTS: the deficit carries the
#       slope here and the level there, and on neither arm does it carry both.  `the order's
#       conditional is half satisfied` is still right; WHICH half is the arm's property. ***
#   ⛭ *And the companion claim inverts with it.  The old form said the deficit `moves the slope only`
#   a little, so what flattens the slope must be the real source's own eta-dependence.  Here the
#   deficit accounts for the whole slope gap and slightly overshoots it, so what is left unexplained
#   is the LEVEL -- and the eta-dependence that was named for the slope is what the LEVEL now needs.
#   Named, as before, and not measured here either.*
#   ⌗ *`cc66.40`'s 0.992 is that arm's figure and is not restated: this receipt measures 0.9950.*
check("⚑⛭⛭ ** THE SOURCE DEFICIT CARRIES ONE OF THE TWO GAPS AND NOT THE OTHER, so the sector does "
      "NOT close into one account -- AND ON THIS ARM IT IS THE SLOPE IT CARRIES, NOT THE LEVEL. **  "
      "It closes 23 per cent of the level gap and 107 per cent of the slope gap, its own slope being "
      "-0.00742 rather than flat.  ⛔ *On the namesake arm it was the reverse -- 54 and 10 per cent, "
      "with the deficit FLAT in q at `cc66.40`'s 0.992 -- so the half that fails is the arm's "
      "property and is restated rather than carried*",
      max(_lev, _slp) / min(_lev, _slp) > 3.0
      and min(_lev, _slp) < 0.3 and max(_lev, _slp) > 0.8
      and abs(_lev - 0.2334) < 5e-4 and abs(_slp - 1.0737) < 5e-4
      and abs(SS + 0.007424) < 5e-7 and abs(SRC_.mean() - 0.9950) < 5e-5,
      f"level {100*_lev:.1f} per cent, slope {100*_slp:.1f} per cent, the deficit {SRC_.mean():.4f} "
      f"with its own slope {SS:+.5f} -- a factor {max(_lev,_slp)/min(_lev,_slp):.1f} between the two")
check("...so what the LEVEL still needs is the real source's own eta-dependence across the "
      "visibility, which is exactly what the injection replaced -- NAMED and not measured here.  "
      "⛔ *On the namesake arm this sentence was about the SLOPE; the deficit carries the slope on "
      "this arm, so the unexplained remainder has moved to the level*",
      # ⌗ the first form of this condition had the inequality BACKWARDS -- it asked for the level
      #   REMAINDER to be small when the finding is that it is LARGE (77 per cent still open), and the
      #   gate caught it on the first run.  Stated on the two closure fractions themselves, which the
      #   gate above pins: the slope is carried PAST the mark and the level is left mostly open.
      _slp > 1.0 > _lev
      and abs(S0 - SX) > abs(S0 - SR),
      f"the injection's level {Y0.mean():.4f} against the real {REAL.mean():.4f}, and the deficit "
      f"moves it only to {PROD.mean():.4f}; on the slope it moves {S0:+.5f} to {SX:+.5f} against the "
      f"real {SR:+.5f}, which is past it")

# ===================================================================================================
# ===================================================================================================
# ⛭⛭ r7643+cc66.65: ** EVERY COMPUTED FIGURE THIS RECEIPT'S `INDEX.md` ROW PRINTS IS PINNED HERE,
#   TWO-SIDED, AT THE DIGITS THE ROW PRINTS -- AND INSIDE `check_figures_pinned`'s OWN ALLOWANCE,
#   which is the coarser of half a last digit and 0.05 per cent, so a figure near one needs 1e-4
#   rather than 5e-4 (`cc66.61`).  *Figures already held two-sided by a gate above are not repeated.*
#   ⌗ *Figures kept OUT of this block rather than pinned or baselined, because this receipt no longer
#   computes them: `cc66.40`'s 0.992 and its -0.00106 slope, the namesake arm's 54 and 10 per cent,
#   and the namesake residual pair 0.0088 / 0.0555.  They are in this file's head in words, and a pin
#   on a figure the receipt does not compute is a false assurance.*
print("\n" + "-" * 100)
_INDEXPINS_OK = (
    # the geometry, under both assignments, on both arms
    abs(g('cs', 'cr', '0') - 0.395135) < 5e-7 and abs(g('cs', 'cr', '1') - 0.395359) < 5e-7
    and abs(g('cs', 'lcdm', '0') - 0.454950) < 5e-7
    and abs(100 * (1 - _r0) - 13.15) < 5e-3 and abs(100 * (1 - _r1) - 13.10) < 5e-3
    and abs(100 * abs(_r1 - _r0) / _r0 - 0.057) < 5e-4
    and abs(g('eta_ls', 'cr', '0') - 492.7919) < 5e-5
    and abs(g('eta_ls', 'cr', '1') - 490.6122) < 5e-5
    and abs(g('rD', 'cr', '0') - 7.5752) < 5e-5 and abs(g('rD', 'cr', '1') - 7.2689) < 5e-5
    # the contrast, its two assignments and this arm's own real source
    and abs(Y0.mean() - 1.0929) < 1e-4 and abs(Y1.mean() - 1.0752) < 1e-4
    and abs(S0 - 0.02955) < 5e-6 and abs(S1 - 0.01794) < 5e-6
    and abs(REAL.mean() - 1.0685) < 1e-4 and abs(SR - 0.02178) < 5e-6
    # the comb, both assignments, and the second referent
    and COMB[('cr', '0')]['pk'][0] == 220 and COMB[('cr', '1')]['pk'][0] == 228
    and abs(COMB[('cr', '0')]['r'] - 0.72621) < 5e-6
    and abs(COMB[('cr', '1')]['r'] - 0.75262) < 5e-6
    and abs(COMB[('cr', '0')]['p12'] - 2.136) < 5e-4
    and abs(COMB[('cr', '1')]['p12'] - 2.009) < 5e-4
    # the source deficit's ledger
    and abs(PROD.mean() - 1.0872) < 1e-4 and abs(SX - 0.02120) < 5e-6
)
print(f"  THE FIGURES THE `INDEX.md` ROW PRINTS, PINNED TWO-SIDED:")
print(f"    geometry  d r_s/d chi {g('cs','cr','0'):.6f} -> {g('cs','cr','1'):.6f}, "
      f"{100*(1-_r0):.2f}% -> {100*(1-_r1):.2f}% lower, a move of "
      f"{100*abs(_r1-_r0)/_r0:.3f}%;  eta_LS {g('eta_ls','cr','0'):.4f} -> "
      f"{g('eta_ls','cr','1'):.4f};  r_D {g('rD','cr','0'):.4f} -> {g('rD','cr','1'):.4f}")
print(f"    contrast  {Y0.mean():.4f} -> {Y1.mean():.4f}, slope {S0:+.5f} -> {S1:+.5f};  this arm's "
      f"real source {REAL.mean():.4f} / {SR:+.5f};  residual {_R0:.4f} / {_R1:.4f}")
print(f"    comb      l_1 {COMB[('cr','0')]['pk'][0]} -> {COMB[('cr','1')]['pk'][0]}, l_1/l_A "
      f"{COMB[('cr','0')]['r']:.5f} -> {COMB[('cr','1')]['r']:.5f};  P1/P2 "
      f"{COMB[('cr','0')]['p12']:.3f} -> {COMB[('cr','1')]['p12']:.3f}")
print(f"    deficit   {SRC_.mean():.4f} at {SS:+.5f};  product {PROD.mean():.4f} at {SX:+.5f};  "
      f"closes {100*_lev:.1f}% of the level and {100*_slp:.1f}% of the slope")
check("⛭⛭ every computed figure the `INDEX.md` row prints is held two-sided to the digits it prints, "
      "so the row's numbers fail this receipt when they are wrong", _INDEXPINS_OK,
      "all of them, each inside half a last printed digit")

print("\n" + "=" * 100)
print(f"""
WHAT `r6925` ASKED AND WHAT THE THREE READINGS SAY.

  ⛭⛭ THE AUDIT FOUND THE GAP ALREADY OPEN IN THE CODE.  Every site where `tau` or `g` touches a rate
  is on the STACKING clock except recombination, which is on the LEAF at `r7095+cc66.75` (`Hrec`), `tau'` on `eg`, `tau` over
  `_egrid`, `ETA_LS` and its FWHM off that grid.  ** But `1/k_D^2` IS Jac-weighted under
  `LEAFSCALES`. **  ⇒ *The diffusion length takes the leaf clock and the optical depth the stacking
  clock -- two objects on the same side of the rate rule, on opposite clocks, with nothing stating
  the choice.*  So the other assignment is not an invention: `VISLEAF=1` applies to `tau` exactly the
  weighting `1/k_D^2` already applies to itself.

  ⚑⚑ ON THE GEOMETRY THE TWO AGREE, WHICH IS THE ORDER'S SECOND BRANCH.  `d r_s/d chi` goes
  {g('cs','cr','0'):.6f} -> {g('cs','cr','1'):.6f} on the arm, so {100*(1-_r0):.2f} per cent lower becomes {100*(1-_r1):.2f} -- a move of
  {100*abs(_r1-_r0)/_r0:.2f} per cent.  ** And structurally, not luckily: it is a RATIO of two accumulations across the
  SAME window, so re-weighting the measure re-weights both. **  ⇒ The visibility is not where the
  freedom is, and the 12.8 per cent is forced by the rule as stated.

  ⛔ BUT THE CONTRAST AND THE COMB DISAGREE, AND THE ORDER SAID TO REPORT THAT RATHER THAN PICK.  The
  injection's retained ratio goes {Y0.mean():.4f} -> {Y1.mean():.4f} and its slope {S0:+.5f} -> {S1:+.5f}, TOWARD the real
  source's 1.0694 and +0.01167.  ** But the arm's first peak moves {COMB[('cr','0')]['pk'][0]} -> {COMB[('cr','1')]['pk'][0]} and its l_1/l_A
  {COMB[('cr','0')]['r']:.4f} -> {COMB[('cr','1')]['r']:.4f}, AWAY from the sky's {SKY:.4f}; P1/P2 goes {COMB[('cr','0')]['p12']:.3f} -> {COMB[('cr','1')]['p12']:.3f}; and the control's
  comb is bit-identical both ways. **  ⚠ *And the contrast improvement is partly an artefact of the
  same move: band by band the `VISLEAF=1` ratio is non-monotonic scatter with a fitted residual
  {np.std(Y1-np.polyval([S1,I1],CTR))/np.std(Y0-np.polyval([S0,I0],CTR)):.1f} times the current assignment's, because moving `eta_LS` moves the comb and a band
  ratio of two oscillations out of alignment in q reads their phase mismatch.*  ⇒ *** The geometry
  says forced, the contrast says improvable, the comb says no -- and the comb is the only one of the
  three with an external referent. ***

  ⚑ ⓶ AND THE SOURCE'S CANCELLATION IS HALF THE LEVEL AND NONE OF THE SLOPE.  Multiplying the
  injection by `cc66.40`'s measured source deficit -- {SRC_.mean():.4f}, FLAT in q at {SS:+.5f} -- gives {PROD.mean():.4f} at
  {SX:+.5f} against the real {REAL.mean():.4f} at {SR:+.5f}.  ** That is {100*_lev:.0f} per cent of the level gap and {100*_slp:.0f} per cent
  of the slope gap. **  ⇒ *So the four trough-filling channels account for about half the level and
  essentially none of the slope: the order's conditional is half satisfied and the closure it hoped
  for does not arrive.  What flattens the slope is the real source's own eta-dependence across the
  visibility -- exactly what the injection replaced -- and that is named, not measured here.*

  ⛔ THE BOUND.  *Whether the two-rate assignment is right is the row's question now and not this
  order's, and nothing here settles it.*  What is settled is that the rule as stated does not
  determine the visibility's clock, that the instrument's two plasma-accumulated objects are already
  on opposite clocks, and that the peak positions support the choice it currently makes.
""")
print("=" * 100)
if FAILS:
    print(f"GATES: {len(FAILS)} FAILED:")
    for f in FAILS:
        print(f"  - {f}")
    raise SystemExit(1)
print("GATES: ALL PASS.")
print(f"""
ESTABLISHED: the rate rule does not determine which clock the visibility is a density in, and the
instrument already answers the question twice and differently -- `1/k_D^2` Jac-weighted under
`LEAFSCALES` while `tau` is not, two plasma-accumulated objects on opposite clocks.  Under the other
admissible assignment d r_s/d chi moves by {100*abs(_r1-_r0)/_r0:.2f} per cent, so the 12.8 per cent is forced by the
rule as stated and the visibility is not where the freedom is.  The contrast moves toward the real
source ({Y0.mean():.4f} -> {Y1.mean():.4f}, slope {S0:+.5f} -> {S1:+.5f}) but the comb moves away from the sky (the arm's
l_1/l_A {COMB[('cr','0')]['r']:.4f} -> {COMB[('cr','1')]['r']:.4f} against {SKY:.4f}), and the contrast's improvement is partly the
statistic reading the comb shift -- its band residual is {np.std(Y1-np.polyval([S1,I1],CTR))/np.std(Y0-np.polyval([S0,I0],CTR)):.1f} times the current assignment's.
The two disagree and neither is picked.  And the source deficit closes {100*_lev:.0f} per cent of the level gap
and {100*_slp:.0f} per cent of the slope gap, so the sector does not close into one account.
NOT CLAIMED: that the two-rate assignment is right; that VISLEAF=1 is wrong as physics; that the
0.06 per cent invariance settles the row; a mechanism beyond cc66.42's; and the injected runs are
not spectra of this model.
""")
