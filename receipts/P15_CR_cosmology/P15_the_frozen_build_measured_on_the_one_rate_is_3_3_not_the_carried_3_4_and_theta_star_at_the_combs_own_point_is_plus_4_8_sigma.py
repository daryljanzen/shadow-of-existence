#!/usr/bin/env python3
r"""`r7801` ** THE FROZEN BUILD MEASURED ON THE ONE RATE IS `3.339` PER CENT, NOT THE CARRIED `3.4` --
AND θ\* AT THE BUILD THE COMB's `298.5` COMES FROM IS `+4.84` SIGMA, NOT THE `+2.3` IN PRINT. **

Discharging orders ① and ② of the chat seat's `r7801`.  Registered before either computation existed
in `computations/beyond_the_wall/r7801_cc66_the_frozen_run_and_theta_star/PREDICTION.md`.

===================================================================================================
** COMPUTES: ** ⒜ the FROZEN arm-B build at the distances' point with `SPLITCLOCK` UNSET, at
   `NS3 = 1800` and `2400` and their h² extrapolation, through `r7703+70`'s own producer with one
   `POINTS` entry added -- the leg that did not exist -- and its agreement with the exact transfer
   and with the decoupled build; ⒝ `theta_*` on the corpus's own definition, re-solved by running
   `70`'s `theta_corpus.py`, at the point the `298.5` comb build actually sits at.
   No refit; no new minimum sought; `theta_obs` inherited.
===================================================================================================

** ① THE MEASURED FIGURES, AND WHAT THEY DO TO THE CARRY THEY REPLACE. **

      one-rate frozen, distances' point   vs exact transfer   vs decoupled
      MEASURED (h², this run)                  3.339 %            1.837 %
      carried at `r7799` (additive)            3.395 %            1.767 %
      carried at `r7799` (multiplicative)      3.351 %            1.740 %
      the (L) baseline the paper had           3.167 %            1.809 %

⇒ ** THE CARRY HELD, TO `0.056` AND `0.070` PERCENTAGE POINTS -- INSIDE THE `±0.3` I REGISTERED. **
*So the clock- and point-stability argument under it was sound, and that is worth saying because the
row was registered to be able to say the opposite.*  ⛔ ** BUT IT WAS JUST ENOUGH TO MOVE THE PRINTED
DIGIT: the carried `3.395` rounds to `3.4`, which is what `P15` prints today, and the measured
`3.339` rounds to `3.3`. **  The decoupled figure rounds to `1.8` either way.

⛭ ** WHY THE LEG HAD TO BE RUN AT ALL. **  `r7703+70` banked `distances__armB_frozen__L__*` and
`control__armB_frozen__one_clock__*` -- so the one combination this order needs,
`distances__armB_frozen__one_clock__*`, was the hole in the lattice.  ① asserts it is still absent
from the bank, which is what makes this receipt's run the measurement rather than a re-reading.

⛔ ** THE TWO GUARDS ARE INHERITED, NOT INVENTED. **  `max|Phi|` is read per rung because `r7703`
item 1 found that a ** finite ** blow-up passes the harness's `isfinite` test and silently returns
`r = 1`; both rungs print `0.926779`, inside the `<= 0.93` every banked rung holds to.  And
`NS3 >= ~3000` is NOT used: at `3600` the mode at the `HKCAP` edge (`h*k = 0.079998`) blows up at
`k*eta ~ 250`.  ② asserts both.

** ② θ\*, AND THE ORDER'S PREMISE CORRECTED BEFORE THE FIGURE IS GIVEN. **

The order says the `+2.3` sigma figure is *"from the early leaf-rate refit (r7753)"*, and asks for it
re-solved *"on the build the comb's 298.5 comes from"* -- as though it were one quantity at a stale
revision.  ** It is not.  It is a different POINT. **

      point                                            100θ\*  on the leaf rate   pull
      distances' (68.60, 0.2973, 0.02237)  <- the 298.5 build      1.04235       +4.84 σ
      arm-of-record refit (68.5707, 0.29125, 0.021643)             1.04215       +4.18 σ
      leaf-rate refit minimum (68.5857, 0.29446, 0.022181)         1.04157       +2.33 σ   <- the `+2.3`

`spectra/r7749_leafgeom_nofit_L2000_cr.npz`'s own `__SWITCHES__` read
`ARM=cr CRH0=68.60 CROM=0.2973 HIER=1 LEAFGEOM=1 LEAFREC=1 LEAFSCALES=1`, and its manifest records
`point: {CRH0: 68.60, CROM: 0.2973}`.  ⇒ ** So the figure `P15` can cite for that build is `+4.8`
sigma, and it is WORSE than the `+2.3` now in print by about a factor of two in the pull. **  ⑥
asserts the identification from the bank's own switches rather than from the order's description.

⛭ *And the onset is reported with the pull, because a pull alone does not say whether an onset
reaching `theta_obs` exists: at this point one does, at `1.231e6`, with `rho_r/rho_m = 365.25`.*

⛔ ** WHAT IS NOT ADJUDICATED HERE. **  Which point `P15` should quote, and whether `+4.8` sigma is
acceptable, are `69`'s.  Nothing is refitted, no minimum is sought, and the measured frozen depths are
left in this computation's own `frozen_one_clock.json` rather than written into a shared `spectra`
bank -- banking them is `69`'s or `70`'s call, and ⑧ asserts this receipt writes no bank.
"""
import ast as _ast
import json
import os
import re
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
RUN = os.path.join(BW, 'r7801_cc66_the_frozen_run_and_theta_star', 'frozen_one_clock.json')
THETA = os.path.join(BW, 'r7749_70_leafgeom_refit', 'theta_corpus.py')
THETA_J = os.path.join(BW, 'r7749_70_leafgeom_refit', 'theta_corpus.json')
ELLS = [2, 3, 4, 5, 6, 7, 8]
CHECKS = []


def check(name, ok, witness=''):
    CHECKS.append((name, bool(ok)))
    print(f"    [{'PASS' if ok else 'FAIL'}] {name}")
    if witness:
        print(f'             {witness}')


def bank(stem):
    p = os.path.join(SPEC, stem + '.npz')
    if not os.path.exists(p):
        sys.exit(f'FATAL: {p} is not where this reads it from; the bank has moved.')
    out = {}
    with np.load(p, allow_pickle=True) as z:
        for k in z.files:
            v = z[k]
            try:
                out[k] = np.asarray(v, float)          # a numeric row
            except (ValueError, TypeError):
                out[k] = str(v.item() if v.shape == () else v)   # a config/switches/arm string
    return out


AA = bank('p15_lowell_depths_armA_leafpert_leafrec1')
OC = bank('p15_lowell_depths_distances_oneclock_leafrec1')
LP = bank('p15_lowell_depths_leafpert_leafrec1')
FC = bank('p15_lowell_depths_frozen_converged_leafrec1')
COMB = bank('r7749_leafgeom_nofit_L2000_cr')
A_1, D_1, F_1def = AA['distances__armA__one_clock_gate'], OC['armB_decoupled'], OC['armB_frozen']
F_Ld, F_Lh2 = LP['distances__armB_frozen__L'], FC['distances__armB_frozen__L__h2']
A_L, D_L = AA['distances__armA__L'], LP['distances__armB_decoupled__L']

runs = json.load(open(RUN, encoding='utf-8'))
print('=' * 100)
print(__doc__)
print('=' * 100)


def spread(a, b_):
    r = [100.0 * abs(1.0 - float(y) / float(x)) for x, y in zip(a, b_)]
    i = int(np.argmax(r))
    return max(r), ELLS[i]


def h2(a, b_, n1=1800, n2=2400):
    """70's own extrapolation, copied from r7703's bank_frozen.py rather than re-derived."""
    return (n2 ** 2 * np.asarray(b_, float) - n1 ** 2 * np.asarray(a, float)) / (n2 ** 2 - n1 ** 2)


D1800 = np.asarray(runs['distances_one_clock__NS3_1800']['depths'], float)
D2400 = np.asarray(runs['distances_one_clock__NS3_2400']['depths'], float)
H2 = np.round(h2(D1800, D2400), 4)
M_TR, M_TRL = spread(A_1, H2)
M_DE, M_DEL = spread(D_1, H2)

# ------------------------------------------------------------------ ① the leg was the hole
_absent = not any(k.startswith('distances__armB_frozen__one_clock') for k in FC)
_has_L = 'distances__armB_frozen__L__h2' in FC
_has_ctl = 'control__armB_frozen__one_clock__h2' in FC
check("⛭⛭⛭ `r7801` ** ① THE LEG THIS ORDER NEEDS WAS THE HOLE IN THE LATTICE, AND STILL IS IN THE "
      "BANK: `r7703+70` HAS `distances__armB_frozen__L__*` AND `control__armB_frozen__one_clock__*`, "
      "BUT NO `distances__armB_frozen__one_clock__*` ** ⇒ *which is what makes this receipt's two "
      "rungs a MEASUREMENT and not a re-reading of someone's bank -- and is why `r7799` had to carry "
      "the figure instead of measuring it*",
      _absent and _has_L and _has_ctl
      and sorted(runs) == ['distances_one_clock__NS3_1800', 'distances_one_clock__NS3_2400'],
      f"bank has the (L) distances leg {_has_L}, the one-clock CONTROL leg {_has_ctl}, and a "
      f"one-clock DISTANCES leg {not _absent}; this run banked {sorted(runs)}")

# ------------------------------------------------------------------ ② the inherited guards
_phis = [runs[k]['phimax'] for k in runs]
_ns3 = sorted(int(k.rsplit('_', 1)[1]) for k in runs)
_src = open(os.path.join(BW, 'r7801_cc66_the_frozen_run_and_theta_star',
                         'run_frozen_one_clock.py'), encoding='utf-8').read()
_no_split = "assert 'SPLITCLOCK' not in env" in _src
check("⛭⛭ `r7801` ** ② AND BOTH GUARDS HOLD, BOTH OF THEM INHERITED RATHER THAN INVENTED: `max|Phi| = "
      "0.926779` ON EACH RUNG, INSIDE THE `<= 0.93` EVERY BANKED RUNG KEEPS, AND `NS3` STAYS AT "
      "`1800 / 2400` ** ⇒ *`r7703` item 1 found that a **finite** blow-up passes the harness's "
      "`isfinite` test and silently returns `r = 1`, so the rung that looks converged is the one to "
      "distrust; and `NS3 >= ~3000` is unusable because at `3600` the mode at the `HKCAP` edge "
      "(`h*k = 0.079998`) blows up at `k*eta ~ 250`.  ⌗ The launcher also ASSERTS `SPLITCLOCK` is "
      "absent from the child's environment, because 'one rate' here IS the absence of that switch*",
      all(p is not None and p <= 0.93 for p in _phis)
      and all(abs(p - 0.926779) < 5e-7 for p in _phis)
      and _ns3 == [1800, 2400] and max(_ns3) < 3000 and _no_split,
      f"max|Phi| per rung {_phis}; NS3 rungs {_ns3}; the launcher asserts SPLITCLOCK absent "
      f"{_no_split}")

# ------------------------------------------------------------------ ③ the measured figures
check("⛭⛭⛭ `r7801` ** ③ AND THE MEASURED FIGURES ARE `3.339` PER CENT AGAINST THE EXACT TRANSFER AND "
      "`1.837` AGAINST THE DECOUPLED BUILD ** ⇒ *the h² extrapolation is `70`'s own, "
      "`(n2²b - n1²a)/(n2² - n1²)`, copied from `r7703`'s `bank_frozen.py` rather than re-derived.  "
      "⌗ The two maxima sit at DIFFERENT multipoles, `l = 4` against the transfer and `l = 3` against "
      "the decoupled build, which is the same split the (L) leg shows*",
      abs(M_TR - 3.339) < 0.001 and abs(M_DE - 1.837) < 0.0005
      and M_TRL == 4 and M_DEL == 3
      and round(M_TR, 1) == 3.3 and round(M_DE, 1) == 1.8,
      f"h² leg {[round(float(v), 4) for v in H2]}; vs exact transfer {M_TR:.3f}% at l={M_TRL}, "
      f"vs decoupled {M_DE:.3f}% at l={M_DEL}; rungs {[round(float(v), 4) for v in D1800]} and "
      f"{[round(float(v), 4) for v in D2400]}")

# ------------------------------------------------------------------ ④ the carry, checked
_add = np.array([float(F_Lh2[i]) - float(F_Ld[i]) for i in range(7)])
_mul = np.array([float(F_Lh2[i]) / float(F_Ld[i]) for i in range(7)])
C_a = np.array([float(F_1def[i]) + _add[i] for i in range(7)])
C_m = np.array([float(F_1def[i]) * _mul[i] for i in range(7)])
CA_TR, _ = spread(A_1, C_a)
CA_DE, _ = spread(D_1, C_a)
CM_TR, _ = spread(A_1, C_m)
CM_DE, _ = spread(D_1, C_m)
_d_tr, _d_de = M_TR - CA_TR, M_DE - CA_DE
check("⛭⛭⛭⛔ `r7801` ** ④ AND THE CARRY `r7799` REPORTED **HELD**, TO `0.056` AND `0.070` PERCENTAGE "
      "POINTS -- INSIDE THE `±0.3` REGISTERED -- SO THE CLOCK- AND POINT-STABILITY ARGUMENT UNDER IT "
      "WAS SOUND. BUT IT WAS JUST ENOUGH TO MOVE THE PRINTED DIGIT: THE CARRIED `3.395` ROUNDS TO "
      "`3.4`, WHICH `P15` PRINTS, AND THE MEASURED `3.339` ROUNDS TO `3.3` ** ⇒ *** this row was "
      "registered to be able to say the carry was WRONG, and it says the opposite -- which is only "
      "worth something because the other answer was available. ** The decoupled figure rounds to "
      "`1.8` either way, so `P15` has ONE digit to change and not two. ** *** ⌗ *The largest "
      "per-multipole depth disagreement between measured and carried is `0.0033`*",
      abs(CA_TR - 3.395) < 0.001 and abs(CA_DE - 1.767) < 0.001
      and abs(CM_TR - 3.351) < 0.001 and abs(CM_DE - 1.740) < 0.001
      and abs(_d_tr - (-0.056)) < 0.0005 and abs(_d_de - 0.070) < 0.0005
      and max(abs(_d_tr), abs(_d_de)) < 0.3
      and round(CA_TR, 1) == 3.4 and round(M_TR, 1) == 3.3
      and round(CA_DE, 1) == round(M_DE, 1) == 1.8
      and abs(float(np.max(np.abs(H2 - C_a))) - 0.0033) < 0.00005,
      f"carried additive {CA_TR:.3f}/{CA_DE:.3f}, multiplicative {CM_TR:.3f}/{CM_DE:.3f}; measured "
      f"{M_TR:.3f}/{M_DE:.3f}; deltas {_d_tr:+.3f}/{_d_de:+.3f} pp, both inside ±0.3; rounded "
      f"{round(CA_TR, 1)} -> {round(M_TR, 1)} and {round(CA_DE, 1)} -> {round(M_DE, 1)}; max depth "
      f"disagreement {float(np.max(np.abs(H2 - C_a))):.4f}")

# ------------------------------------------------------------------ θ*: re-solved, not quoted
_before = json.load(open(THETA_J, encoding='utf-8'))
_pr = subprocess.run([sys.executable, '-I', THETA], capture_output=True, text=True, timeout=1800,
                     cwd=os.path.dirname(THETA))
_after = json.load(open(THETA_J, encoding='utf-8'))


def _flat(d):
    return {(p, g, k): v for p, row in d.items() for g, gv in row.items() for k, v in gv.items()}


_fb, _fa = _flat(_before), _flat(_after)
_moved = [k for k in _fb if not ((_fb[k] is None and _fa.get(k) is None)
                                 or (_fb[k] is not None and _fa.get(k) is not None
                                     and abs(float(_fb[k]) - float(_fa[k])) < 1e-9))]
_DIST = "distances' point (68.60, 0.2973), omega_b built-in 0.02237"
_LEAF = 'leaf-rate assignment (D_M on leaf rate)'
_STACK = 'arm of record (D_M on stacking rate)'
_MIN = 'leaf-rate refit minimum (68.5857, 0.29446, 0.022181)'
_d_leaf = _after[_DIST][_LEAF]
_m_leaf = _after[_MIN][_LEAF]

check("⛭⛭⛭ `r7801` ** ⑤ AND θ\\* IS RE-SOLVED HERE, NOT QUOTED: `70`'s `theta_corpus.py` IS RUN AND ALL "
      "SIX STORED ROWS REPRODUCE, `0` MOVED ** ⇒ *so the figure below is a measurement in this receipt "
      "rather than a reading of `theta_corpus.json`, which is what the registration required*",
      _pr.returncode == 0 and not _moved and len(_fb) == len(_fa) and len(_fb) >= 12,
      f"theta_corpus rc={_pr.returncode}; {len(_fb)} stored value(s), {len(_moved)} moved")

# ------------------------------------------------------------------ ⑥ the premise, corrected
_sw = COMB['switches']
_m_h0 = re.search(r'CRH0=([\d.]+)', _sw)
_m_om = re.search(r'CROM=([\d.]+)', _sw)
_leafgeom = 'LEAFGEOM=1' in _sw
_at_dist = (_m_h0 and abs(float(_m_h0.group(1)) - 68.60) < 0.005
            and _m_om and abs(float(_m_om.group(1)) - 0.2973) < 0.00005)
_not_at_min = not (_m_h0 and abs(float(_m_h0.group(1)) - 68.585672) < 0.005
                   and _m_om and abs(float(_m_om.group(1)) - 0.294463) < 0.00005)
check("⛭⛭⛭⛔ `r7801` ** ⑥ AND THE ORDER'S PREMISE IS WRONG, WHICH ⑥ SETTLES FROM THE BANK'S OWN "
      "SWITCHES: THE `298.5` COMB BUILD SITS AT THE **DISTANCES' POINT** `(68.60, 0.2973)` WITH "
      "`LEAFGEOM=1`, NOT AT THE LEAF-RATE REFIT MINIMUM `(68.5857, 0.29446)` THE `+2.3` SIGMA BELONGS "
      "TO ** ⇒ *** so re-solving θ\\* *\"on the build the comb's `298.5` comes from\"* does not refresh "
      "`+2.3` sigma -- it REPLACES it with `+4.84`, which is worse by about a factor of two in the "
      "pull. *** ⌗ *Read from `r7749_leafgeom_nofit_L2000_cr`'s own `__SWITCHES__` string, not from "
      "the order's description of it, which is the whole reason the two came apart*",
      _at_dist and _not_at_min and _leafgeom
      and abs(100 * _d_leaf['theta_zstart'] - 1.04235) < 0.000005
      and abs(_d_leaf['pull_zstart'] - 4.84) < 0.005
      and abs(100 * _m_leaf['theta_zstart'] - 1.04157) < 0.000005
      and abs(_m_leaf['pull_zstart'] - 2.33) < 0.005
      and _d_leaf['pull_zstart'] > 2 * _m_leaf['pull_zstart'] * 0.9,
      f"the comb build's switches: CRH0={_m_h0.group(1) if _m_h0 else None}, "
      f"CROM={_m_om.group(1) if _m_om else None}, LEAFGEOM=1 {_leafgeom}; at the distances' point "
      f"{_at_dist}, at the refit minimum {not _not_at_min}; 100theta* "
      f"{100 * _d_leaf['theta_zstart']:.5f} ({_d_leaf['pull_zstart']:+.2f} sigma) against the "
      f"minimum's {100 * _m_leaf['theta_zstart']:.5f} ({_m_leaf['pull_zstart']:+.2f})")

# ------------------------------------------------------------------ ⑦ the onset beside the pull
check("⛭⛭ `r7801` ** ⑦ AND THE ONSET IS REPORTED WITH THE PULL: AT THE `298.5` BUILD'S POINT AN ONSET "
      "REACHING `theta_obs` **EXISTS**, AT `1.231e6`, WITH `rho_r/rho_m = 365.25` -- WHILE ON THE ARM "
      "OF RECORD AT THE SAME POINT THERE IS **NONE** IN `[1.2e3, 1e9]` ** ⇒ *a pull on its own does "
      "not say whether the construction can reach the observed scale at all, and the two answers "
      "differ at the same point by which rate carries `D_M` -- so the onset is the half of the result "
      "that says the leaf-rate assignment is not merely closer but reachable*",
      abs(_d_leaf['onset_matching'] - 1231355.5) < 1.0
      and abs(_d_leaf['rho_r_over_rho_m_at_onset'] - 365.25) < 0.005
      and _after[_DIST][_STACK]['onset_matching'] is None,
      f"leaf rate at the distances' point: onset {_d_leaf['onset_matching']:.1f}, "
      f"rho_r/rho_m {_d_leaf['rho_r_over_rho_m_at_onset']:.2f}; arm of record at the same point: "
      f"onset {_after[_DIST][_STACK]['onset_matching']}")

# ------------------------------------------------------------------ ⑧ every figure pinned; scope
_pins = dict(
    m_tr=abs(M_TR - 3.339) < 0.001, m_de=abs(M_DE - 1.837) < 0.0005,
    c_tr=abs(CA_TR - 3.395) < 0.001, c_de=abs(CA_DE - 1.767) < 0.001,
    cm_tr=abs(CM_TR - 3.351) < 0.001, cm_de=abs(CM_DE - 1.740) < 0.001,
    l_tr=abs(spread(A_L, F_Lh2)[0] - 3.167) < 0.001,
    l_de=abs(spread(D_L, F_Lh2)[0] - 1.809) < 0.0005,
    phimax=all(abs(p - 0.926779) < 5e-7 for p in _phis),
    maxdep=abs(float(np.max(np.abs(H2 - C_a))) - 0.0033) < 0.00005,
    th_dist=abs(100 * _d_leaf['theta_zstart'] - 1.04235) < 0.000005,
    th_min=abs(100 * _m_leaf['theta_zstart'] - 1.04157) < 0.000005,
    th_stack=abs(100 * _after[_DIST][_STACK]['theta_zstart'] - 1.03715) < 0.000005,
    pull_dist=abs(_d_leaf['pull_zstart'] - 4.84) < 0.005,
    pull_min=abs(_m_leaf['pull_zstart'] - 2.33) < 0.005,
    pull_stack=abs(_after[_DIST][_STACK]['pull_zstart'] - (-11.92)) < 0.005,
    onset=abs(_d_leaf['onset_matching'] - 1231355.5) < 1.0,
    # the INDEX row prints the onset as 1.231e6 and the deltas to three decimals, so each is pinned
    # in the UNITS IT IS PRINTED IN -- check_figures_pinned reads the printed figure, not mine
    onset_e6=abs(_d_leaf['onset_matching'] / 1e6 - 1.231) < 0.0005,
    d_tr=abs(_d_tr - (-0.056)) < 0.0005, d_de=abs(_d_de - 0.070) < 0.0005,
    rho=abs(_d_leaf['rho_r_over_rho_m_at_onset'] - 365.25) < 0.005,
)
check("⛭⛭ `r7801` ** ⑧ AND EVERY FIGURE THE `INDEX` ROW PUBLISHES IS PINNED HERE BY A COMPARISON -- "
      "THE MEASURED PAIR, BOTH CARRY FORMS, THE (L) BASELINE, `max|Phi|`, THE CARRY'S OWN ERROR, AND "
      "ALL SIX θ\\* NUMBERS WITH THE ONSET ** ⇒ *`check_figures_pinned` PARSES rather than runs, and a "
      "tolerance looser than its own allowance does not count as a pin -- which is what caught "
      "`1.809` at `r7799`, so that one is pinned at `0.0005` here*",
      all(_pins.values()),
      f"{sum(_pins.values())} of {len(_pins)} pinned; NOT pinned: "
      f"{sorted(k for k, v in _pins.items() if not v) or 'none'}")

_FORBIDDEN = {'curve_fit', 'minimize', 'minimize_scalar', 'lstsq', 'polyfit', 'savez',
              'savez_compressed', 'nsigma'}
_names = set()
for _n in _ast.walk(_ast.parse(open(__file__, encoding='utf-8').read())):
    if isinstance(_n, _ast.Name):
        _names.add(_n.id)
    elif isinstance(_n, _ast.Attribute):
        _names.add(_n.attr)
_hits = sorted(_names & _FORBIDDEN)
check("⛭⛭ `r7801` ** ⑨ AND THE SCOPE LIMIT IS ASSERTED RATHER THAN PROMISED: NOTHING IS REFITTED, NO "
      "MINIMUM IS SOUGHT, `theta_obs` IS INHERITED, AND THIS RECEIPT WRITES NO BANK ** ⇒ *the measured "
      "depths stay in the computation's own `frozen_one_clock.json`; writing them into a shared "
      "`spectra` bank is `69`'s or `70`'s call, and the AST walk below asserts no `savez` here.  Which "
      "point `P15` should quote, and whether `+4.8` sigma is acceptable, are `69`'s rulings*",
      not _hits,
      f"fitting, minimisation and banking names in this file's AST: {_hits or 'none'}")

print()
bad = [n for n, ok in CHECKS if not ok]
print(f"  {len(CHECKS) - len(bad)} of {len(CHECKS)} gates pass")
if bad:
    for n in bad:
        print(f"  FAILED: {n}")
    sys.exit(1)
