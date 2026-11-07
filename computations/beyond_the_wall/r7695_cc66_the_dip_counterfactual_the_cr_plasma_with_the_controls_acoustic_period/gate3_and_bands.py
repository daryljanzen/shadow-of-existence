"""r7695+cc66 -- GATE 3, THE REGISTERED D_l-SIDE PREDICTION, AND THE SEVEN BANDS OF THE COUNTERFACTUAL.

Everything here was registered before the rebuild was launched (`GATE_3_REGISTERED.md`) or before a
band was read (`BEFORE_READING_IT.md`).  Nothing below chooses its own criterion.

  GATE 3    T_K of the rebuilt CR source == the control's 1.017000, tolerance 5e-4 = two steps of
            `fit_period`'s own grid (linspace(0.90, 1.20, 1201)).  NOTHING is read off the bands
            until this passes.
  GATE 3b   the rebuilt bank's r_s, D_M, l_A unchanged from the arm of record's -- a re-combed
            plasma and not a different cosmology.
  PREDICT   T_L comes out at the control's too, within the same two steps.  Registered
            low-to-moderate; the licence is in GATE_3_REGISTERED.md and it is the interesting limb.
  ARM ②     the q ~ 1.9 departure falls by more than half -- scored against the COUNTERFACTUAL'S OWN
            law, A at rho*r_s*, with the arm-of-record law reported beside it and named as the wrong
            comparison.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.abspath(os.path.join(HERE, '..'))
SP = os.path.join(BW, 'spectra')
sys.path.insert(0, os.path.join(BW, 'r7637_70_own_comb_statistic'))
import own_comb as OC                                                              # noqa: E402

RHO = 0.9945919371
TOL = 5e-4
T_K_C, T_L_C = 1.017000, 1.009250          # the control's, measured at r7699+cc66.0 (comb_target.py)
FAIL = []


def banks(cr_pairs, cr_source):
    PR = {t: dict(np.load(os.path.join(SP, n), allow_pickle=True)) for t, n in
          (('lcdm', 'r6915_pairs_lcdm.npz'), ('cr', cr_pairs))}
    SO = {t: dict(np.load(os.path.join(SP, n), allow_pickle=True)) for t, n in
          (('lcdm', 'r6911_source_lcdm_leafrec1.npz'), ('cr', cr_source))}
    return {t: dict(QL=PR[t]['ls'].astype(float) / float(PR[t]['l_A']),
                    QK=SO[t]['k'] * float(SO[t]['r_s']) / np.pi,
                    Dl=np.asarray(PR[t]['Dl'], float),
                    S2=np.asarray(SO[t]['S_i'], float) ** 2) for t in PR}, PR, SO


for _n in ('r7695_pairs_cr_combrho.npz', 'r7695_source_cr_combrho.npz'):
    if not os.path.exists(os.path.join(SP, _n)):
        raise SystemExit(f'  ⛔ spectra/{_n} is not on disk -- run launch_combrho.sh then '
                         f'bank_combrho.py')

AOR, _, SO_A = banks('r6915_pairs_cr_leafrec1.npz', 'r6911_source_cr_leafrec1.npz')
CF, _, SO_C = banks('r7695_pairs_cr_combrho.npz', 'r7695_source_cr_combrho.npz')
C_A, C_C = OC.retention_combs(AOR), OC.retention_combs(CF)

# ── GATE 3b first: the background, because a moved background invalidates QK itself ─────────────
print("  ⛭ GATE 3b -- THE BACKGROUND, arm of record vs the counterfactual")
for _q in ('r_s', 'D_M', 'l_A', 'ns'):
    _a, _n = float(SO_A['cr'][_q]), float(SO_C['cr'][_q])
    print(f"      {_q:5s} {_a:.9f}  {_n:.9f}   {'same' if _a == _n else '⛔ MOVED'}")
    if _a != _n:
        FAIL.append(f'GATE 3b: {_q} moved {_a} -> {_n}')
_same_k = np.array_equal(np.asarray(SO_A['cr']['k'], float), np.asarray(SO_C['cr']['k'], float))
print(f"      the saved k grid is the PROJECTION's, unchanged: {_same_k}")
if not _same_k:
    FAIL.append('GATE 3b: the saved k grid moved -- QK is not comparable')

# ── GATE 3: the source comb's period ────────────────────────────────────────────────────────────
TKa, TKn = C_A['cr']['K'][0], C_C['cr']['K'][0]
TLa, TLn = C_A['cr']['L'][0], C_C['cr']['L'][0]
print(f"\n  ⛭ GATE 3 -- THE SOURCE COMB'S FITTED PERIOD, control {T_K_C:.6f}")
print(f"      arm of record  {TKa:.6f}   ({TKa - T_K_C:+.6f} from the control)")
print(f"      counterfactual {TKn:.6f}   ({TKn - T_K_C:+.6f} from the control)")
_g3 = abs(TKn - T_K_C) <= TOL
print(f"      ⇒ {'✔ GATE 3 PASSES' if _g3 else '⛔ [FAIL] GATE 3'}: |{TKn:.6f} - {T_K_C:.6f}| = "
      f"{abs(TKn - T_K_C):.6f} against the fitter's two grid steps {TOL:.5f}")
if not _g3:
    FAIL.append(f'GATE 3: T_K came out {TKn:.6f}, not {T_K_C:.6f}')

print(f"\n  ⚑ THE REGISTERED D_l-SIDE PREDICTION, control {T_L_C:.6f}")
print(f"      arm of record  {TLa:.6f}   ({TLa - T_L_C:+.6f});  counterfactual {TLn:.6f}   "
      f"({TLn - T_L_C:+.6f})")
_pL = abs(TLn - T_L_C) <= TOL
print(f"      ⇒ registered that it ALSO lands at the control's within two steps: "
      f"{'✔ CONFIRMED' if _pL else '⛔ FALSIFIED'}")
print("      ⌗ " + ("the D_l comb's period difference is INHERITED FROM THE PLASMA and the "
                    "projection adds none of its own" if _pL else
                    "part of the D_l comb's period difference is the PROJECTION's geometry and not "
                    "the plasma's -- so the own-comb statistic's L-side remap corrects two things "
                    "at once, which is a finding about the statistic"))

if FAIL:
    print()
    for f in FAIL:
        print(f'  ⛔ [FAIL] {f}')
    print("  ⇒ NOTHING is read off the seven bands until gate 3 and 3b pass, as registered.")
    raise SystemExit(1)

# ── the seven bands, and the departure against BOTH laws ────────────────────────────────────────
_L = np.load(os.path.join(HERE, 'law_at_rho_cache.npz'))
assert abs(float(_L['rho']) - RHO) < 1e-12, 'the law cache is at a different rho'
assert float(_L['leg1_maxdiff']) < 1e-12 and float(_L['leg2_maxdiff']) > 1e-6, \
    'the law recomputation s own two legs did not pass -- rerun law_at_rho.py'
_AQ = {'cr': np.asarray(_L['ls'], float) / float(_L['l_A'])}
_AL = np.load(os.path.join(SP, 'r7041_accept_lcdm.npz'), allow_pickle=True)
_AQ['lcdm'] = np.asarray(_AL['ls__fixed'], float) / float(_AL['l_A__fixed'])
_AA_l = np.asarray(_AL['A'], float)


def lawband(_a, _b, A_cr):
    """the law's arm/control ratio over one band by its band MEAN -- r7689 arm 5, unchanged"""
    _g = np.linspace(_a, _b, 400)
    return np.interp(_g, _AQ['cr'], A_cr).mean() / np.interp(_g, _AQ['lcdm'], _AA_l).mean()


ED7 = np.linspace(0.35 + 0.5 + 1e-9, 5.75, 8)
LAW_AOR = np.array([lawband(a, b, np.asarray(_L['A_bank'], float)) for a, b in zip(ED7[:-1], ED7[1:])])
LAW_CF = np.array([lawband(a, b, np.asarray(_L['A_rho'], float)) for a, b in zip(ED7[:-1], ED7[1:])])
x_a, y_a = OC.retained_own(AOR, 1.0, 7, 5.75, C=C_A)
x_c, y_c = OC.retained_own(CF, 1.0, 7, 5.75, C=C_C)
DEP_A = y_a - LAW_AOR
J = int(np.argmax(np.abs(DEP_A)))
DEP_C_own = y_c - LAW_CF
DEP_C_aor = y_c - LAW_AOR

print(f"\n  ⛭ THE SEVEN BANDS -- the departure is read at q = {x_a[J]:.2f}, where the arm of "
      f"record's is largest")
print("      q      measured(AOR)  law(AOR)   dep(AOR)  |  measured(CF)  law(CF)   dep(CF)   "
      "dep(CF vs AOR law)")
for i in range(7):
    print(f"    {x_a[i]:5.2f}   {y_a[i]:11.4f}  {LAW_AOR[i]:8.4f}  {DEP_A[i]:+8.4f}  |  "
          f"{y_c[i]:11.4f}  {LAW_CF[i]:8.4f}  {DEP_C_own[i]:+8.4f}   {DEP_C_aor[i]:+8.4f}")

# ⛔⛔⛔ ** THE RAW DEPARTURE IS NOT THE STATISTIC, AND READING IT AS ONE GIVES A FALSE POSITIVE
#   HERE -- WHICH THE FIRST FORM OF THIS SCRIPT PRINTED AS `CONFIRMED`. **
#   *The raw `dep` at `q = 1.9` goes `+0.0192 -> +0.0000`: 99.9 per cent gone, arm ② apparently
#   confirmed on its own words.  But EVERY OTHER BAND acquires about `-0.021` at the same time.  The
#   LEVEL of the whole set moved and `q = 1.9` is simply where the new level crosses the law.*
#   ⇒ ** The departure at `q ~ 1.9` is a BAND-TO-BAND SHAPE claim by construction** -- `r7689`'s
#     finding is that the law carries the offset and the rise and NOT the band-to-band shape, and
#     `r7693`'s dip test detrends (`_detr`) for exactly that reason.  *The shape statistic is the one
#     established BEFORE this measurement, so it is the one that scores the arm; choosing it here is
#     not choosing the statistic that gives the answer I prefer.*
#   ⌗ *`BEFORE_READING_IT.md` guarded the LAW against moving under the counterfactual and did not
#     guard the LEVEL.  One level up, the same mistake: a number that falls for the wrong reason.*
def _detr(_y):
    """r7693's own detrending, lifted in form: the departure's band-to-band shape, level removed"""
    return _y - np.polyval(np.polyfit(x_a, _y, 1), x_a)


_SA, _SC = _detr(DEP_A), _detr(DEP_C_own)
_f_raw = DEP_C_own[J] / DEP_A[J]
_f_shape = _SC[J] / _SA[J]
_shift = float(DEP_C_own.mean() - DEP_A.mean())
print(f"\n  ⛔ THE LEVEL MOVED, SO THE RAW DEPARTURE AND THE SHAPE DISAGREE -- both are given")
print(f"      the mean departure over the seven bands: {DEP_A.mean():+.5f} -> "
      f"{DEP_C_own.mean():+.5f}, a UNIFORM shift of {_shift:+.5f}")
print(f"      q      dep(AOR)  dep(CF)  |  shape(AOR)  shape(CF)")
for i in range(7):
    print(f"    {x_a[i]:5.2f}   {DEP_A[i]:+8.4f} {DEP_C_own[i]:+8.4f}  |  {_SA[i]:+9.4f}  "
          f"{_SC[i]:+9.4f}")
print(f"\n  ⇒ ARM ② SCORED ON THE SHAPE, against the counterfactual's OWN law:")
print(f"      at q = {x_a[J]:.2f}: {_SA[J]:+.4f} -> {_SC[J]:+.4f}, a factor of {_f_shape:+.3f}")
print(f"      and q = {x_a[J]:.2f} is STILL the largest |shape| of the seven: "
      f"{int(np.argmax(np.abs(_SC))) == J}")
print(f"      registered: it falls by MORE THAN HALF  ⇒  "
      f"{'✔ CONFIRMED' if abs(_f_shape) < 0.5 else '⛔ FALSIFIED'}")
print(f"\n  ⌗ THE RAW READING, reported so it cannot be mistaken for the answer: "
      f"{DEP_A[J]:+.4f} -> {DEP_C_own[J]:+.4f}, a factor of {_f_raw:.3f} "
      f"({100*(1-_f_raw):+.1f} per cent) -- which is the LEVEL's shift and not the feature's.")
print(f"  ⌗ and against the ARM OF RECORD's law, the wrong law as registered: "
      f"{DEP_A[J]:+.4f} -> {DEP_C_aor[J]:+.4f}, a factor of {DEP_C_aor[J]/DEP_A[J]:.3f}")
print(f"\n  ⚠ ARM ③'s CONFOUND IS NOW MEASURED AND NOT FEARED: the uniform {_shift:+.4f} is what a "
      f"resample that carries an envelope stretch does to a RATIO of RMS values, and this test "
      f"cannot separate it from the period change.  ⇒ **The result is reported as UNSEPARATED on "
      f"the level**, exactly as arm ③ registered, and the SHAPE is what the arm is scored on.")
np.savez(os.path.join(HERE, 'gate3_and_bands.npz'), x=x_a, y_aor=y_a, y_cf=y_c,
         law_aor=LAW_AOR, law_cf=LAW_CF, dep_aor=DEP_A, dep_cf_own=DEP_C_own,
         dep_cf_aorlaw=DEP_C_aor, shape_aor=_SA, shape_cf=_SC,
         level_shift=np.array(_shift), T_K=np.array([TKa, TKn, T_K_C]),
         T_L=np.array([TLa, TLn, T_L_C]), rho=RHO, J=J)
