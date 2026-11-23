"""
P15, r7857+cc66.3, on 69's order r7857: items ① and ②.

** ① MY SPREAD DISAGREEMENT IS WITHDRAWN -- WE WERE NOT BINNING THE SAME OBJECT.  ② AND `FOURPI`
MOVES NOT ONE OF THE SIX RECEIPTS 60's SWEEP ROUTED HERE -- BUT IT BREAKS A CLOSURE THEIR SWEEP WAS
NOT LOOKING FOR, IN FOUR RECEIPTS, SEVEN ARMS, ONE OF THEM 70's. **

===================================================================================================
** ① THE SPREAD, RECONCILED -- AND THE CONFIGURATION CARRIES NONE OF IT **
===================================================================================================

  configuration                                  spread    arith mean
  r7855 as published: lmax 2196, lensed_scalar   0.056634   0.503313
  lmax 2600 only, lensed_scalar                  0.056613   0.503336
  60's exact pair: lmax 2600, total              0.056613   0.503336
  60's pair plus lens_potential_accuracy 2       0.056721   0.503359

⌗ *The middle two rows are BIT-IDENTICAL, in every digit of every entry, and that is not a copying
slip: with no tensors CAMB's `total` IS the lensed scalar spectrum, so `lensed_scalar` against
`total` was never a difference at all -- which disposes of half my hypothesis before the numbers do.*

⛔ ** BANDS Ⓐ AND Ⓑ ARE REFUTED.  My hypothesis was that my `lmax` and my `lensed_scalar` made the
spread; it is false, and four lines say so: matching 60's configuration exactly moves the spread by
`0.00002`, which is four parts in ten thousand of the disagreement. **

⇒ ** THE CAUSE IS THAT THE TWO SIDES BINNED DIFFERENT OBJECTS. **  60's `cmb_side.py` takes its bank
side from `mod.cmb.binned(x4, SUM_REF)` -- `model6`'s RECONSTRUCTED binned model, interpolated and
re-binned off the sum-dependence grid.  This seat binned the RAW INSTRUMENT SPECTRUM straight out of
`POLSAVE`.  A reconstruction through a grid is smooth in `ell` by construction; the raw spectrum is
not.  ⌗ *That the difference is SUFFICIENT is an inference and is labelled one: `mod.cmb.binned`
needs `POL_DIR`, which this container has lost, so the two objects cannot be differenced here.*

⛔ ** SO THE r7855 HEADLINE IS WITHDRAWN: "five times less flat than reported" compared this seat's
raw-spectrum scatter against their model-reconstruction scatter, and that is not like for like. **
*What stands from r7855: the factor itself (`0.503313` against their `0.504672`, `0.27` per cent) and
that it is in EE too (`0.497180`).  What is withdrawn: the flatness comparison, and the claim to have
DERIVED their convention -- theirs is `(4/9) A_s k_pivot^(1-ns) e^(-2 tau)` and mine `A_s (3/5)^2`,
two different expressions agreeing to `0.213` per cent.*

** AND THE OSCILLATION THE ORDER ASKS FOR, AT THE FIRST THREE PEAKS. **  Departure of the ratio from
its own mean: `-0.34` per cent at `ell = 220`, `+0.43` at `540`, `+2.53` at `812`, worst `-6.35` at
`1920`, r.m.s. `2.31`.  ⇒ It GROWS with multipole, so it is a damping-tail difference and not an
acoustic-scale one; an `l_A` error would alternate at fixed amplitude instead.

===================================================================================================
** ② THE SIX ABSOLUTE STATEMENTS: ZERO OF SIX MOVE, AND THE SWEEP'S CLASSIFIER IS WHY **
===================================================================================================

Each receipt was run TWICE, in its own process, once with every instrument TT `Dl` the bank hands it
DOUBLED -- which is what `FOURPI` does to them exactly (`Cl *= 4 pi`, then `Dl = Cl l(l+1) / 2 pi`,
so `Dl -> 2 Dl`; 60 measured `2.000000000000`, worst departure `8.9e-16`, and said a regenerated
bank is bit-for-bit predictable from the existing one).

  receipt                          npz    doubled   FAIL base -> doubled   what moves
  model difference / contrast       48       19           0 -> 0           the fitted amplitude
  monopole zero point              15        3            0 -> 0           printed peak HEIGHTS
  no-fit confrontation              5        4            0 -> 0           NOTHING AT ALL
  period-difference null            1        0           (unreachable)     see the figure probe
  projection's conformal time       0        0           (reads no bank)   nothing it states
  two channels, multiplicative      8        6            0 -> 0           NOTHING AT ALL

⇒ ** NOT ONE ASSERTION IN THE SIX CHANGES VERDICT, AND TWO OF THEM DO NOT MOVE A SINGLE PRINTED
DIGIT. **  What moves is three things, all of them the invariance working rather than failing:
  * the model-difference receipt's PRINTED fitted amplitude, `13583.4831 -> 6791.7415`, exactly a
    half -- the amplitude absorbing the factor is what keeps `chi^2` at `286.8941240254` both ways;
  * the monopole receipt's three printed lines of absolute peak HEIGHTS, exactly doubled, with the
    `P1/P2` and `P1/P3` beside them unchanged -- the heights are printed, the ratios are asserted;
  * four of the `66` keys `fig:acoustic-nofit` banks, which are its four fitted amplitudes, each
    halving; the other `62` are invariant to `1e-12`, and NO receipt in the tree reads a `_A` key.

⛔ ** AND MY OWN EXPECTATION WAS WRONG, WHICH IS THE PART WORTH KEEPING. **  `PREDICTION.md` Ⓕ named
the no-fit confrontation as *"the one I most expect to move, because no fit is precisely the
condition under which an amplitude error cannot be absorbed"*.  It is the receipt where not one
number moves.  ⇒ ** "Nothing fitted" in these receipts means no COSMOLOGICAL PARAMETERS fitted to
the microwave data -- the background comes from the distance data -- and the amplitude is fitted in
closed form at the covariance-weighted optimum regardless.  60's heuristic matched the phrase and
read it as the amplitude being held. **  Band Ⓕ registered *at most three of the six*; the answer is
zero, so Ⓕ holds and its reasoning limb does not.

===================================================================================================
** ⛔ AND THE EXPOSURE IS SOMEWHERE THE SWEEP DID NOT LOOK: `Dl_pairs` **
===================================================================================================

`FOURPI` is not "TT-only" even inside TT.  `out[j] = np.sum(P * _tr**2) * _FP_ACC` carries the
accumulation factor; `_dec[j, _c] = ... np.sum(P * _Dl[_a] * _Dl[_b])`, the bilinear decomposition
accumulated BESIDE it, carries neither factor, and the save line writes `Dl = Cl l(l+1) / _FP_DL`
next to a bare `Dl_pairs = _dc`.  ⇒ ** So the ten pairs would stop closing on the `D_l` saved beside
them, by exactly a factor two: the closure goes from `1.6e-15` to `0.500000` on all four banked
`SRCDEC` files, and the instrument's own `SRCDEC` print -- which divides by the `4 pi`-scaled `Cl` --
would read `0.920423` instead of `1e-15`. **

  receipt                                         owner   FAIL base -> doubled
  the cross term is not the channel               cc66         0 -> 2
  the bank already existed (Doppler minority)     cc66         0 -> 2
  the step survives a differential estimator      cc66         0 -> 2
  the three instruments with no noise model       70           0 -> 1
  the step is the excess's own                    cc66         0 -> 0  (survives)

⇒ ** Four receipts, seven arms, and one of them is NOT THIS SEAT'S. **  Every one is a CLOSURE or a
SHARE -- `sum of pairs == D_l`, or `pair / D_l` -- so 60's sweep could not have found them: it was
looking for absolute amplitudes and these are identities.  *This is the `r7615` coupling class: a
receipt coupled to a switch by an arithmetic relation over the tree, naming neither the switch nor
the file that will change.*  ⌗ Routed to 69, NOT patched: the order says not to patch until the
defaults are on, and the repair here belongs on 60's side -- `_dec` wants `_FP_ACC` and the save
wants `/_FP_DL`, after which the closure holds again and nothing below needs touching.

-------------------------------------------------------------------------------
COMPUTES: the amplitude-fit invariance on the banked spectra directly (chi^2 and the fitted
  amplitude, before and after doubling); the `Dl_pairs` closure on all four banked `SRCDEC` files as
  it stands and under the doubling; the asymmetry READ OFF THE PARSED INSTRUMENT SOURCE rather than
  its text; and the three banked audit records -- the six receipts, the five `Dl_pairs` readers, and
  the figure generator -- including each one's own positive control.
  ** IT PINS NO COSMOLOGICAL PARAMETER AND RUNS NO INSTRUMENT. **  Item ① is read from the two
  records committed with the computation; item ② is read from the audit records and re-derived here
  where it can be re-derived without a subprocess.
STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy; under a second -- it runs no
  instrument and calls no `camb`)
"""
import ast
import json
import os
import sys

import numpy as np

print(__doc__.split("STATUS:")[0])
BAR = "=" * 100
fail = []


RAN = []


def check(label, ok, got=None):
    RAN.append(label)
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}" + (f"   (got {got})" if got is not None else ""))
    if not ok:
        fail.append(label)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), f'ROOT is wrong: {ROOT}'
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
CD = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                  'r7857_cc66_the_spread_reconciled_and_the_absolute_statements_read')
INST = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py')
PAIRS = ['r6915_pairs_lcdm.npz', 'r6915_pairs_cr.npz', 'r6915_pairs_cr_leafrec1.npz',
         'r7695_pairs_cr_combrho.npz']
FOURPI_RATIO = 2.0

# =================================================================================================
print(BAR)
print("  Ⓐ -- ** ① THE SPREAD: FOUR CONFIGURATIONS, AND THE CONFIGURATION CARRIES NONE OF IT **")
print(BAR)
SPR = json.load(open(os.path.join(CD, 'spread_reconciled.json')))
_k = list(SPR)
for k in _k:
    print(f"      {k.strip():45s} spread {SPR[k]['spread']:.6f}   arith {SPR[k]['arith']:.6f}"
          f"   {SPR[k]['n']} bins")
_mine, _theirs = SPR[_k[0]], SPR[_k[2]]
check("Ⓐ① the configuration this seat published and 60's EXACT configuration give the same spread to "
      "`0.00003` -- `0.056634` against `0.056613`, which is `0.4` per cent of the `0.046` "
      "disagreement with their `0.010542`, so ⛔ BANDS Ⓐ AND Ⓑ ARE REFUTED",
      abs(_mine['spread'] - 0.056634) < 5e-6 and abs(_theirs['spread'] - 0.056613) < 5e-6
      and abs(_mine['spread'] - _theirs['spread']) < 3e-5,
      f"{_mine['spread']:.6f} vs {_theirs['spread']:.6f}")
check("Ⓐ② and every one of the four configurations lands in the same place -- `lens_potential_"
      "accuracy 2` is the widest excursion at `0.056721` and the means span `0.503313` to "
      "`0.503359` -- so no switch on this side produces a spread near `0.010542`",
      all(abs(SPR[k]['spread'] - 0.0566) < 0.0002 for k in _k)
      and abs(max(SPR[k]['spread'] for k in _k) - 0.056721) < 5e-6
      and abs(min(SPR[k]['arith'] for k in _k) - 0.503313) < 5e-6
      and abs(max(SPR[k]['arith'] for k in _k) - 0.503359) < 5e-6
      and all(SPR[k]['n'] == 185 for k in _k))
check("Ⓐ③ all four read the SAME bin count, so the spreads are comparable at all -- `185` bins, "
      "which is 60's own count",
      len({SPR[k]['n'] for k in _k}) == 1 and SPR[_k[0]]['n'] == 185)

OSC = json.load(open(os.path.join(CD, 'oscillation_at_peaks.json')))
print(f"      peaks: {OSC['peak_220']['departure_per_cent']:+.2f}% at ell "
      f"{OSC['peak_220']['ell']:.0f}, {OSC['peak_540']['departure_per_cent']:+.2f}% at "
      f"{OSC['peak_540']['ell']:.0f}, {OSC['peak_812']['departure_per_cent']:+.2f}% at "
      f"{OSC['peak_812']['ell']:.0f};  worst {OSC['worst']['departure_per_cent']:+.2f}% at "
      f"{OSC['worst']['ell']:.0f};  r.m.s. {OSC['rms_per_cent']:.2f}%")
check("Ⓐ④ ** the oscillation at the first three peaks is `-0.34`, `+0.43` and `+2.53` per cent, "
      "worst `-6.35` at `ell = 1920` and `2.31` r.m.s. ** -- and it GROWS with multipole, which is a "
      "damping-tail difference and not the fixed-amplitude alternation an acoustic-scale error gives",
      abs(OSC['peak_220']['departure_per_cent'] + 0.335) < 0.005
      and abs(OSC['peak_540']['departure_per_cent'] - 0.427) < 0.005
      and abs(OSC['peak_812']['departure_per_cent'] - 2.535) < 0.005
      and abs(OSC['worst']['departure_per_cent'] + 6.347) < 0.005
      and abs(OSC['rms_per_cent'] - 2.310) < 0.005
      and abs(OSC['peak_812']['departure_per_cent']) > abs(OSC['peak_220']['departure_per_cent']))

# =================================================================================================
print()
print(BAR)
print("  Ⓑ -- ** ② THE MECHANISM, RE-DERIVED HERE: ONE FITTED AMPLITUDE ABSORBS THE FACTOR EXACTLY **")
print(BAR)
_z = np.load(os.path.join(SP, 'cc66_r185_verify_lcdm.npz'), allow_pickle=True)
_ls, _dl = np.asarray(_z['ls'], float), np.asarray(_z['Dl'], float)
# ** a FIXED linear map and a FIXED positive-definite weight, so what is shown is a property of the
#   FIT and not of this sector's particular operator or covariance. **
_rng = np.random.default_rng(7857)
_W = _rng.normal(size=(60, len(_ls)))
_M = _W @ np.diag(1.0 + 0.1 * np.cos(_ls / 97.0))                      # the fixed linear map
_L = _rng.normal(size=(60, 60))
_FI = _L @ _L.T + 60.0 * np.eye(60)                                    # the fixed weight
_d = _M @ _dl * 0.47 + _rng.normal(scale=1e-3, size=60)


def scored(dl):
    m = _M @ dl
    A = float(m @ _FI @ _d / (m @ _FI @ m))
    r = A * m - _d
    return A, float(r @ _FI @ r), r


_A1, _C1, _r1 = scored(_dl)
_A2, _C2, _r2 = scored(_dl * FOURPI_RATIO)
print(f"      chi2 {_C1:.10f} -> {_C2:.10f}      fitted amplitude {_A1:.6e} -> {_A2:.6e}"
      f"   (ratio {_A2 / _A1:.15f})")
check("Ⓑ⑤ ** the fitted amplitude halves EXACTLY and the residual does not move at all **, so every "
      "chi^2, every whitened residual and every statistic built on one is invariant under the `2` "
      "`FOURPI` applies -- the ratio is `0.5` to `1e-15` and the residual to `1e-12` of its scale",
      abs(_A2 / _A1 - 0.5) < 1e-15
      and float(np.max(np.abs(_r1 - _r2))) < 1e-12 * float(np.max(np.abs(_r1)))
      and abs(_C2 - _C1) < 1e-9 * max(1.0, _C1),
      f"amplitude ratio {_A2 / _A1:.15f}, dchi2 {_C2 - _C1:+.2e}")

# =================================================================================================
print()
print(BAR)
print("  Ⓒ -- ** ② THE SIX, RUN BOTH WAYS -- AND EACH ONE'S OWN POSITIVE CONTROL **")
print(BAR)
SIX = json.load(open(os.path.join(CD, 'fourpi_audit_six.json')))
for f, v in SIX.items():
    print(f"      {f[4:52]:50s} npz {v['archives_opened']:3d}  doubled {v['arrays_doubled']:3d}"
          f"  FAIL {len(v['fails_base'])} -> {len(v['fails_doubled'])}  rc {v['rc_base']} -> "
          f"{v['rc_doubled']}  moved {len(v['moved'])}")
_reach = {f: v for f, v in SIX.items() if v['arrays_doubled'] > 0}
check("Ⓒ⑥ ** ZERO OF THE SIX MOVE: not one assertion changes verdict and not one exit code changes **"
      " -- four of the six are REACHED by the doubling, between `3` and `19` arrays each, and all "
      "four come back `0` FAIL both ways",
      len(SIX) == 6 and len(_reach) == 4
      and all(v['fails_doubled'] == [] and v['fails_base'] == [] and v['rc_base'] == 0
              and v['rc_doubled'] == 0 for v in _reach.values())
      and min(v['arrays_doubled'] for v in _reach.values()) == 3
      and max(v['arrays_doubled'] for v in _reach.values()) == 19,
      f"{len(_reach)} of {len(SIX)} reached, "
      f"{sum(len(v['fails_doubled']) for v in SIX.values())} FAIL in all")
# ⛭ ** NAMED, NOT COUNTED -- and `check_prose_pins` is what made me write it this way. **  *The
#   first form of this arm asserted `.count(1) == 1` and `.count(0) == 1` over the unreachable
#   receipts, and the gate flagged both as pins on a COUNT OF MATCHES: two receipts swapping which
#   one opens an archive would have left them both true.  Keyed by receipt instead, it says which
#   receipt opens what, and it is strictly the stronger statement.*
_unreach = {f[4:30]: v['archives_opened'] for f, v in SIX.items() if v['arrays_doubled'] == 0}
print(f"      unreached by the doubling, with the archives each one opens: {_unreach}")
check("Ⓒ⑦ ⛔ and the POSITIVE CONTROL is what makes that readable: the two receipts the probe does "
      "NOT reach are declared rather than counted as clean -- the period-difference null opens a "
      "single archive and it holds no instrument spectrum, and the projection receipt opens none at "
      "all, each named here rather than counted",
      _unreach == {'the_period_difference_null': 1, 'the_projection_read_recomb': 0},
      f"{_unreach}")
_nofit = [v for f, v in SIX.items() if 'no_fit_confrontation' in f][0]
_two = [v for f, v in SIX.items() if 'two_channels' in f][0]
check("Ⓒ⑧ ⛔ ** AND THE ONE Ⓕ NAMED AS MOST LIKELY TO MOVE IS ONE OF THE TWO THAT MOVE NO DIGIT AT "
      "ALL ** -- the no-fit confrontation and the two-channels receipt each come back with an "
      "IDENTICAL run, because `nothing fitted` names the parameters and not the amplitude",
      _nofit['moved'] == [] and _two['moved'] == []
      and _nofit['arrays_doubled'] == 4 and _two['arrays_doubled'] == 6)
_md = [v for f, v in SIX.items() if 'model_difference' in f][0]
check("Ⓒ⑨ and the ONE line the model-difference receipt moves is its printed fitted amplitude, which "
      "halves while the `chi^2` printed on the same line does not move a digit -- so the only "
      "absolute amplitude any of the six prints moves by exactly the factor, and nothing asserted "
      "does.  ⌗ *The ratio reads `0.4999999963` and not `0.5` because it is taken off the four "
      "decimals the line PRINTS; the exact half is Ⓑ⑤'s, measured on the arrays*",
      len(_md['moved']) == 1 and abs(_md['moved'][0][2] - 0.5) < 5e-8
      and '13583.4831' in _md['moved'][0][0] and '6791.7415' in _md['moved'][0][1]
      and '286.8941240254' in _md['moved'][0][0] and '286.8941240254' in _md['moved'][0][1])
_mono = [v for f, v in SIX.items() if 'monopole_zero_point' in f][0]
check("Ⓒ⑩ and the monopole receipt moves three lines, all of them printed absolute peak HEIGHTS "
      "doubling, with the `P1/P2` and `P1/P3` printed beside them unchanged in the same line",
      len(_mono['moved']) == 3
      and all(abs(m[2] - 2.0) < 0.001 for m in _mono['moved'])
      and all('P1/P2 = 2.1' in m[0] and m[0].split('P1/P2')[1] == m[1].split('P1/P2')[1]
              for m in _mono['moved']))

# =================================================================================================
print()
print(BAR)
print("  Ⓓ -- ** ② THE ONE RECEIPT THE PROBE CANNOT REACH, CLOSED ONE LAYER OUT **")
print(BAR)
FIG = json.load(open(os.path.join(CD, 'fourpi_figure_probe.json')))
print(f"      the figure generator: {FIG['keys']} banked keys, {FIG['hits_doubled']} arrays doubled,"
      f" worst relative move {FIG['worst']:.6f}, live bank untouched = {FIG['live_unchanged']}")
for k, d in FIG['moved']:
    print(f"        {k} moves by {d:.6f}")
check("Ⓓ⑪ ** of the `66` keys `fig:acoustic-nofit` banks, exactly `4` move and all four are its "
      "FITTED AMPLITUDES, each halving ** -- so the receipt that reads this bank reads only "
      "amplitude-fitted quantities and cannot move, which is now a measurement and not an inference",
      FIG['keys'] == 66 and len(FIG['moved']) == 4
      and all(k.endswith('_A') and abs(d - 0.5) < 1e-9 for k, d in FIG['moved'])
      and abs(FIG['worst'] - 0.5) < 1e-9 and FIG['hits_doubled'] == 4 and FIG['hits_base'] == 0)
check("Ⓓ⑫ and the probe wrote NOTHING inside the repository while measuring that -- the live bank's "
      "own hash is unchanged, asserted by the probe rather than assumed, and no receipt anywhere in "
      "the tree reads a banked `_A` key",
      FIG['live_unchanged'] is True)

# =================================================================================================
print()
print(BAR)
print("  Ⓔ -- ** ⛔ THE CLOSURE THE SWEEP DID NOT LOOK FOR: `Dl_pairs` AGAINST ITS OWN `Dl` **")
print(BAR)
_now, _under = [], []
for f in PAIRS:
    z = np.load(os.path.join(SP, f), allow_pickle=True)
    d, p = np.asarray(z['Dl'], float), np.asarray(z['Dl_pairs'], float)
    _now.append(float(np.max(np.abs(p.sum(axis=1) - d) / np.abs(d))))
    _under.append(float(np.max(np.abs(p.sum(axis=1) - FOURPI_RATIO * d)
                               / np.abs(FOURPI_RATIO * d))))
    print(f"      {f:32s} closure now {_now[-1]:.3e}   under FOURPI {_under[-1]:.6f}")
_print_would = 1.0 - 1.0 / (4.0 * np.pi)
print(f"      and the instrument's own SRCDEC print, which divides by the 4pi-scaled Cl, would read"
      f" {_print_would:.6f}")
SRC = open(INST).read()
TREE = ast.parse(SRC)


def _names(node):
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}




# ** the TT accumulation is the one `out[...]` assignment that sums the squared transfer over the
#   mode power -- picked by its own expression's names, because the instrument has 34 `out[...]`
#   assignments and a positional guess would have read one of the other 33. **
_acc = [n for n in ast.walk(TREE) if isinstance(n, ast.Assign) and len(n.targets) == 1
        and isinstance(n.targets[0], ast.Subscript)
        and isinstance(n.targets[0].value, ast.Name) and n.targets[0].value.id == 'out'
        and {'P', '_tr'} <= _names(n.value)]
_dec = [n for n in ast.walk(TREE) if isinstance(n, ast.Assign) and len(n.targets) == 1
        and isinstance(n.targets[0], ast.Subscript)
        and isinstance(n.targets[0].value, ast.Name) and n.targets[0].value.id == '_dec']
_savez = [n for n in ast.walk(TREE) if isinstance(n, ast.Call)
          and isinstance(n.func, ast.Attribute) and n.func.attr == 'savez'
          and {k.arg for k in n.keywords} >= {'Dl', 'Dl_pairs'}]
assert len(_acc) == 1 and len(_dec) == 1 and len(_savez) == 1, \
    f'the instrument must carry one accumulation, one decomposition and one pairs save -- ' \
    f'{len(_acc)}, {len(_dec)}, {len(_savez)}'
_kw = {k.arg: k.value for k in _savez[0].keywords}


def _unit_factor_names(tree):
    """the module-level names whose OWN assignment is `<something> if <a name> else 1.0`

    ** 60's own inert-unit-factor class, read STRUCTURALLY. **  *This arm therefore pins no name of
    theirs: rename the factors or the switch and it still reads, which is the difference between
    depending on another seat's STRUCTURE and depending on its SPELLING.*
    """
    out = {}
    for n in tree.body:
        if not (isinstance(n, ast.Assign) and len(n.targets) == 1
                and isinstance(n.targets[0], ast.Name) and isinstance(n.value, ast.IfExp)):
            continue
        v = n.value
        if (isinstance(v.test, ast.Name) and isinstance(v.orelse, ast.Constant)
                and v.orelse.value == 1.0):
            out[n.targets[0].id] = v.test.id
    return out


_UF = _unit_factor_names(TREE)
_U = set(_UF)
_accN, _decN = _names(_acc[0].value) & _U, _names(_dec[0].value) & _U
_dlN, _prN = _names(_kw['Dl']) & _U, _names(_kw['Dl_pairs']) & _U
# ⛭ r7861 (69): 60's repair applies `/ _FP_DL` where `_dc` is FORMED, one line above the save, and saves the name
#   bare; so a bare name in the save is followed to its own assignment, which is where the factor now lives.
if isinstance(_kw['Dl_pairs'], ast.Name):
    _prA = [n for n in ast.walk(TREE) if isinstance(n, ast.Assign) and len(n.targets) == 1
            and isinstance(n.targets[0], ast.Name) and n.targets[0].id == _kw['Dl_pairs'].id]
    for _n in _prA:
        _prN |= _names(_n.value) & _U
_gap = (not _decN) or (not _prN)
print(f"      the instrument's unit-factor class, read structurally: {sorted(_UF)} on switch(es) "
      f"{sorted(set(_UF.values()))}")
print(f"      reaching the TT accumulation {sorted(_accN)};  the decomposition beside it "
      f"{sorted(_decN)};  the `Dl` save {sorted(_dlN)};  the `Dl_pairs` save {sorted(_prN)}")
check("Ⓔ⑬ the ten pairs close on their own `D_l` AS THE TREE STANDS, on all four banked `SRCDEC` "
      "files -- below `2e-15` relative, so the identity is real and the gate that reads it is sound",
      len(_now) == 4 and max(_now) < 2e-15, f"worst {max(_now):.3e}")
check("Ⓔ⑭ ⛔ ** AND IT WOULD STOP CLOSING BY EXACTLY A FACTOR TWO IF THE DEFAULTS WENT ON WHILE THE "
      "GAP IS OPEN: `0.500000` on all four banks, against `1.6e-15` now ** -- asserted as the "
      "IMPLICATION of the gap read off the parsed source, so that 60 putting a unit factor into the "
      "decomposition makes the antecedent false and this arm passes on the other limb instead of "
      "needing an edit",
      (not _gap) or (abs(max(_under) - 0.5) < 1e-12 and abs(min(_under) - 0.5) < 1e-12),
      f"gap open = {_gap}, closure under the doubling {min(_under):.6f}-{max(_under):.6f}")
check("Ⓔ⑮ ⛭ RE-READ r7861 (69) AS THE RECORD OF THE REPAIR, AS DESIGNED: 60's r7860 put the unit "
      "factors into the decomposition and the pairs save, so the decomposition now carries the SAME "
      "unit factor as the accumulation and the `Dl_pairs` save the same as the `Dl` save.  As first "
      "landed this arm stated the gap: the accumulation DID carry a unit factor while the decomposition beside it carried "
      "none, which is where the asymmetry lived -- found by walking the instrument's own inert-"
      "unit-factor CLASS, the one 60 defined for their ratchet, so this arm depends on their "
      "structure and not on the spelling of either factor -- and the two that DO reach TT are gated "
      "by ONE switch, which is what makes them one repair rather than two.  ⌗ *This arm is a WATCH and is MEANT to "
      "redden when 60 repairs it: it states what the tree holds now, so putting a unit factor into "
      "the decomposition turns it red and it is then re-read as a record of the repair.  Ⓔ⑭'s "
      "implication arm is written the other way round and passes across that same repair, which was "
      "verified by making the edit*",
      len(_UF) >= 2 and len(_accN) == 1 and len(_dlN) == 1
      and {_UF[n] for n in _accN} == {_UF[n] for n in _dlN}
      and _decN == _accN and _prN == _dlN,
      f"accumulation {sorted(_accN)}, decomposition {sorted(_decN)}, "
      f"`Dl` {sorted(_dlN)}, `Dl_pairs` {sorted(_prN)}")
check("Ⓔ⑯ and the instrument's own `SRCDEC` closure print would read `0.920423`, not the `1e-15` it "
      "prints now, because that line divides by the `4 pi`-scaled `Cl` rather than by the saved "
      "`D_l` -- so the run's own log would contradict itself",
      abs(_print_would - 0.920423) < 5e-7)

# =================================================================================================
print()
print(BAR)
print("  Ⓕ -- ** ⛔ FOUR RECEIPTS GO RED ON IT, SEVEN ARMS, AND ONE OF THEM IS 70's **")
print(BAR)
PRS = json.load(open(os.path.join(CD, 'fourpi_audit_pairs.json')))
for f, v in PRS.items():
    print(f"      {f[4:52]:50s} doubled {v['arrays_doubled']:3d}  FAIL {len(v['fails_base'])} -> "
          f"{len(v['fails_doubled'])}  rc {v['rc_base']} -> {v['rc_doubled']}")
_red = {f: v for f, v in PRS.items() if v['fails_doubled']}
check("Ⓕ⑰ ** four of the five `Dl_pairs` readers go RED and they carry `7` arms between them, "
       "against `0` as the tree stands ** -- and the fifth survives, so this is a measurement over "
       "the readers and not a blanket statement about them",
      len(PRS) == 5 and len(_red) == 4
      and sum(len(v['fails_doubled']) for v in PRS.values()) == 7
      and sum(len(v['fails_base']) for v in PRS.values()) == 0
      and all(v['rc_base'] == 0 for v in PRS.values())
      and sum(1 for v in PRS.values() if v['rc_doubled'] == 1) == 4,
      f"{len(_red)} red, {sum(len(v['fails_doubled']) for v in PRS.values())} arms")
check("Ⓕ⑱ and the closure gate is among them on BOTH arms -- the cross-term receipt's own order says "
      "to gate the closure first and read nothing below it if it fails, so this is not a cosmetic arm",
      [f for f in _red if 'cross_term' in f] != []
      and len(_red[[f for f in _red if 'cross_term' in f][0]]['fails_doubled']) == 2
      and all('CLOSE ON `D_l` EXACTLY' in s
              for s in _red[[f for f in _red if 'cross_term' in f][0]]['fails_doubled']))
_mine_red = [f for f in _red if 'three_instruments' not in f]
check("Ⓕ⑲ ⛭ and one of the four is NOT this seat's -- the three-instruments receipt is `70`'s, found "
      "by a census over `receipts/` for the key rather than by reading this seat's own list, which "
      "is the only way a receipt belonging to another seat could have been found at all",
      len(_mine_red) == 3 and [f for f in _red if 'three_instruments' in f] != []
      and len(_red[[f for f in _red if 'three_instruments' in f][0]]['fails_doubled']) == 1)
check("Ⓕ⑳ and every one of the seven is a CLOSURE or a SHARE and not an absolute amplitude, which is "
      "why 60's sweep could not have found them: it searched for amplitude-held statements",
      all(('CLOSE ON' in s) or ('sum' in s.lower()) or ('share' in s.lower())
          or ('carries' in s.lower()) or ('bilinear' in s.lower()) or ('pair' in s.lower())
          for v in _red.values() for s in v['fails_doubled']))

# =================================================================================================
print()
print(BAR)
print("  Ⓖ -- ** THE COUNT, COUNTED **")
print(BAR)
# ⛔ ** THE COUNT IS READ OFF THE ARMS THAT RAN, not typed beside them: `RAN` is appended by
#   `check` itself, so adding, removing or renaming an arm reddens this one.  *A count asserted
#   against its own literal is the hollow shape this corpus lints for, and it would pass whatever
#   the file did.* **
_before = len(RAN)
_uniq = len(set(RAN))
print(f"      {_before} arms ran before this one, {_uniq} of them distinct")
check(f"Ⓖ㉑ ** twenty arms ran before this one and every one of them was adjudicated, and the "
      f"count is read off the list `check` itself appends ** -- so an arm added or dropped reddens "
      f"this arm rather than leaving a stale count in the prose",
      _before == 20 and _uniq == _before,
      f"{_before} arms, {_uniq} distinct")

print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED:")
    for f in fail:
        print(f"      - {f}")
    print(BAR)
    sys.exit(1)
print("  ✔ ** ① THE SPREAD DISAGREEMENT IS WITHDRAWN: the configuration carries NONE of it and the")
print("    two sides binned different objects.  The oscillation is -0.34 / +0.43 / +2.53 per cent at")
print("    the first three peaks, worst -6.35 at 1920, growing with ell. **")
print("  ✔ ** ② ZERO OF THE SIX MOVE under FOURPI, two of them not by a single digit, because every")
print("    scoring path fits one amplitude in closed form.  `nothing fitted` names the PARAMETERS. **")
print("  ⛔ ** AND THE EXPOSURE IS ELSEWHERE: `Dl_pairs` carries neither factor, so the ten pairs")
print("    would stop closing on their own `D_l` by exactly two -- four receipts, seven arms, one of")
print("    them 70's.  ROUTED TO 69, NOT PATCHED. **")
print(BAR)
print("  ALL CHECKS PASS")
