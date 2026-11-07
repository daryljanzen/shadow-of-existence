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

_f_own = DEP_C_own[J] / DEP_A[J]
_f_aor = DEP_C_aor[J] / DEP_A[J]
print(f"\n  ⇒ ARM ② SCORED ON THE COUNTERFACTUAL'S OWN LAW (A at rho*r_s*):")
print(f"      the departure at q = {x_a[J]:.2f}: {DEP_A[J]:+.4f} -> {DEP_C_own[J]:+.4f}, "
      f"a factor of {_f_own:.3f} ({100*(1-_f_own):+.1f} per cent of it gone)")
print(f"      registered: it falls by MORE THAN HALF  ⇒  "
      f"{'✔ CONFIRMED' if abs(_f_own) < 0.5 else '⛔ FALSIFIED'}")
print(f"  ⌗ and against the ARM OF RECORD's law, which is the WRONG comparison and is reported only "
      f"so it cannot be mistaken for the right one:")
print(f"      {DEP_A[J]:+.4f} -> {DEP_C_aor[J]:+.4f}, a factor of {_f_aor:.3f}")
print(f"  ⌗ the largest departure band of the COUNTERFACTUAL is q = {x_c[int(np.argmax(np.abs(DEP_C_own)))]:.2f} "
      f"({DEP_C_own[int(np.argmax(np.abs(DEP_C_own)))]:+.4f}) -- the same band as the arm of "
      f"record's: {int(np.argmax(np.abs(DEP_C_own))) == J}")
np.savez(os.path.join(HERE, 'gate3_and_bands.npz'), x=x_a, y_aor=y_a, y_cf=y_c,
         law_aor=LAW_AOR, law_cf=LAW_CF, dep_aor=DEP_A, dep_cf_own=DEP_C_own,
         dep_cf_aorlaw=DEP_C_aor, T_K=np.array([TKa, TKn, T_K_C]),
         T_L=np.array([TLa, TLn, T_L_C]), rho=RHO, J=J)
