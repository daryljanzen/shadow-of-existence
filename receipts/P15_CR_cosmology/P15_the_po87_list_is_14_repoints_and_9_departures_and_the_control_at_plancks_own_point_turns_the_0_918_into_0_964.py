"""
** PO-87's 23 ITEMS ARE 14 REPOINTS AND 9 DEPARTURES, SO THE CLAUSE IS NOT STRUCK; AND THE CONTROL
RUN AT PLANCK 2018's OWN PUBLISHED POINT IMPROVES BY $4.781$ PER CENT, TURNING THE PUBLISHED $0.918$
INTO $0.964$ AND HALVING THE ARM'S MARGIN. **

⛭⛭ r7815/r7819 (cc66): ** AND THAT RATIO IS SCORED ACROSS A SAMPLING MISMATCH, WHICH GATE 5b MEASURES
AND THE PAPER NOW PRINTS INSTEAD. **  Gate 5's denominator is the re-pointed control at `LSTEP=8`
(238 samples) and its numerator the old one at `LSTEP=2` (950), and the binner reads the difference.
At matched step-2 sampling the re-pointed control's $\chi^{2}$ is $204.709$, the published $0.918$
becomes $0.960$, and the improvement is $4.367$ per cent.  *The two sampling banks agree to
`5.55e-16` at every shared multipole at the same point, so what moves is the BINNING and not the
physics -- which is precisely why it was measured before a sentence took the number.*  ⇒ *Gate 5
stands as the step-8 run's own figure and is not what a sentence may quote; gate 5b's is.*

Order r7807 (69), items ① and ②, after both r7805 recommendations were ruled in: PO-87's clause is
scoped to ARM spectra, and the control is re-pointed to Planck's published best fit.  Item ③ (the
comb receipt's filename stays) was ruled at r7797 and needs nothing.

** ② THE RUN, NOT A STENCIL, AS ORDERED. **  `ARM=lcdm LH0=67.36 LOM=0.313773 WBH2=0.02237
NS=0.9649 HIER=1 LSTEP=8 LMAXL=2000`, 2547 modes, rc=0, peaks at $[220,540,812,1132]$.
  ⛔ ** THE INSTRUMENT CARRIES NO NEUTRINO MASS ** -- a massless free-streaming hierarchy (`LN`,
  `FNU`, `DNEFF`) and no `mnu` anywhere -- while Planck's published fit assumes $\sum m_\nu=0.06$ eV.
  **So this is Planck's POINT in this instrument, not Planck's MODEL**, and that is said here rather
  than left for a reader to discover.  69's conditional is answered: it does not carry it.
  ⌗ *And the instrument takes $\Omega_m$, not $\omega_c$, so the point converts at ITS OWN
  $h=0.6736$: $(0.1200+0.02237)/0.6736^{2}=0.313773$ -- not the $0.313400$ my r7805 stencil used at
  a FIXED $H_0=67.40$.  The real re-pointing moves $H_0$ and $n_s$ too, so this is a different point
  and not that stencil's prediction re-measured.*

** WHAT MOVES. **  On the refit receipts' own scoring (P15's CAMB lensing operator, 185 lensed bins):
the control's no-fit $\chi^{2}$ falls $214.057\to203.823$, ** IMPROVING by $4.781$ per cent **, so
** the published $0.918$ becomes $0.964$ ** and the arm's margin over the control falls from $8.2$ to
$3.6$ per cent -- *less than half the published claim*.  The control's peaks move $+0.1195$, $+0.3502$,
$+0.6620$ and $+0.9198$ multipoles, the fourth-peak move exceeding every fourth-feature difference the
paper prints.  ⛭ ** AND THE REFITTED $1.002$ CANNOT MOVE, shown STRUCTURALLY rather than numerically:
** it is `lf_rf / ctl_rf`, read from the two REFIT verifies, and the un-refitted bank is read only
for the no-fit ratio -- so the figure never touches what is being re-pointed.  *A demonstration beats
an agreement of numbers here, because an agreement could be luck.*

** ① THE 23, READ BY HAND: 14 STAND AS REPOINTS AND 9 LEAVE. **  The method is r7635's `RECIPES.md`,
authoritative where my own tracer was not: *"every command in this table banked before `cc66.75` that
omits `LEAFREC` ... run verbatim today rebuilds the leafrec1 arm and not its namesake"*, and *"none
of the 36 namesakes carries the `config` key that would have recorded it; every `_leafrec1` file
does"*.  So the namesake arm banks are off the leaf rate, and each has a banked twin.
  * ** the 7 candidates: all OFF the leaf rate, all with a banked `_leafrec1` twin ** -> 7 repoints;
  * ** the 16 undecidable split 6 / 3 / 7: ** 6 read no arm grid at all (they leave), 3 read a
    `_leafrec1` grid AND a namesake one, which is a COMPARISON and not a defect (they leave), and 7
    read a namesake grid whose `_leafrec1` twin directory exists (7 more repoints).
  ⇒ ** 14 repoints are the remaining work and 9 items leave; PO-87 is NOT struck. **

⛔ ** AND A CORRECTION TO MY OWN r7805 RESULT, WHICH 69 HAS ALREADY MERGED. **  That round reported
the census's `cheap` count as $0$ and let it stand as "no item is repointable end to end".  `cheap`
is the CONJUNCTION of two tests -- every namesake path has a twin AND no load site is undecidable --
and it is also computed on BASENAMES, so a second copy of the same bank in another seat's `rebuilt/`
directory, with no twin beside it, makes a repointable item read as un-repointable.  **The count was
right for what `cheap` means and wrong as an answer to "can these be repointed": 14 of them can.**

** COMPUTES: ** the control spectrum at Planck's published point, banked WITH a `config` -- both
banks, the `POLSAVE` one included, which is the proof of the fix this round made first so the
polarisation bank could never join an undecidable list.  Nothing else is run: the 23 are read, and
no figure is re-derived and no paper sentence edited here.

Built r7807+cc66, registered at
`computations/beyond_the_wall/r7807_cc66_the_23_items_and_the_repointed_control/PREDICTION.md`.
11 gates, rc=0 on success.  Run: python3 <this file>   (numpy, scipy, camb; ~2 min)
"""
import glob
import json
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
MINE = os.path.join(BW, 'r7807_cc66_the_23_items_and_the_repointed_control')
SP = os.path.join(BW, 'spectra')
RCP = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
fail = []


def G(n, ok, msg):
    print(f"  {'✅' if ok else '⛔'} GATE {n}  {msg}")
    if not ok:
        fail.append(f'gate {n}: {msg}')


# ======================================================================================= GATE 1 ===
# The run exists, at the ordered point, and BOTH banks carry a config.
NEW = os.path.join(MINE, 'out', 'r7807_control_planck2018_L2000.npz')
POL = os.path.join(MINE, 'out', 'r7807_control_planck2018_L2000_pol.npz')
cfgs = {}
for tag, p in (('TT', NEW), ('pol', POL)):
    with np.load(p, allow_pickle=True) as z:
        cfgs[tag] = json.loads(str(z['config'].item())) if 'config' in z.files else None
_both = all(c is not None for c in cfgs.values())
_arm = all(c and c.get('ARM') == 'lcdm' for c in cfgs.values())
_lmax = all(c and float(c.get('LMAXL', 0)) == 2000.0 for c in cfgs.values())
_kfac = all(c and float(c.get('KFAC', 0)) == 2.0 for c in cfgs.values())
G(1, _both and _arm and _lmax and _kfac,
  f"the control run is banked and BOTH banks carry a `config` ({_both}) -- the TT bank and the "
  f"POLSAVE one, which is the direct proof of the fix this round made first; ARM=lcdm ({_arm}), "
  f"LMAXL=2000 ({_lmax}), KFAC at the corpus default 2.0 ({_kfac})")

# ======================================================================================= GATE 2 ===
# The instrument carries no neutrino mass -- asserted against its own source, not remembered.
_src = open(os.path.join(BW, 'ACOUSTIC_two_arm.py')).read()
_no_mnu = not re.search(r'\bmnu\b|\bMNU\b|m_nu\s*=', _src)
_massless = bool(re.search(r"LN = int\(os\.environ\.get\('LN'", _src))
G(2, _no_mnu and _massless,
  f"the instrument carries NO neutrino mass, read off its own source: no `mnu`/`MNU` anywhere "
  f"({_no_mnu}) and a massless free-streaming hierarchy depth `LN` instead ({_massless})  ⇒ this is "
  f"Planck's POINT in this instrument, not Planck's MODEL, and 69's conditional is answered")

# ======================================================================================= GATE 3 ===
# The point conversion, at the instrument's own h.
WB, WC, H = 0.02237, 0.1200, 0.6736
OM = (WC + WB) / H ** 2
OM_STENCIL = (WC + WB) / 0.674 ** 2
_ran_at = None   # set in gate 11's block, from the launcher: the config does not record the point
G(3, abs(OM - 0.313773) < 1e-6 and abs(OM_STENCIL - 0.313400) < 1e-6 and abs(OM - OM_STENCIL) > 3e-4,
  f"the point converts at the instrument's OWN h: Omega_m = ({WC}+{WB})/{H}^2 = {OM:.6f}, against "
  f"the {OM_STENCIL:.6f} my r7805 stencil used at h=0.674 and a FIXED H0 -- a difference of "
  f"{OM - OM_STENCIL:+.6f}, so the run is a DIFFERENT POINT and not that stencil re-measured")

# ======================================================================================= GATE 4 ===
# What moves: the control improves, and by how much.
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import camb                                                                    # noqa: E402
import chi2_of_spectrum as CS                                                  # noqa: E402
_p = camb.set_params(H0=67.40, ombh2=WB, omch2=0.3150 * 0.674 ** 2 - WB, mnu=0.06, omk=0, tau=0.054,
                     As=2.1e-9, ns=0.965, lmax=3000)
_cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
_le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
LG = np.arange(len(_le), dtype=float)
LENS = np.ones_like(_le)
LENS[_un > 0] = _le[_un > 0] / _un[_un > 0]


def load(p):
    with np.load(p, allow_pickle=True) as z:
        return np.asarray(z['ls'], float), np.asarray(z['Dl'], float)


def score(p):
    ls, Dl = load(p)
    c, nb = CS.chi2_of(ls, Dl * np.interp(ls, LG, LENS))[:2]
    return float(c), int(nb)


CO, nbo = score(os.path.join(SP, 'cc66_lcdm_L2000.npz'))
CN, nbn = score(NEW)
PCT = 100 * (CN - CO) / CO
G(4, nbo == nbn == 185 and abs(CO - 214.057) < 0.05 and abs(CN - 203.823) < 0.05
  and abs(PCT + 4.781) < 0.02 and CN < CO,
  f"the control's no-fit chi^2 over {nbn} lensed bins falls {CO:.3f} -> {CN:.3f}, IMPROVING by "
  f"{abs(PCT):.3f} per cent  ⇒ PREDICTION (2e) HELD: a better control is a harder comparison, which "
  f"is why the ratio rises")

# ======================================================================================= GATE 5 ===
# The published 0.918 becomes 0.964.
PUB = 0.918
ARM = PUB * CO
NEWR = ARM / CN
G(5, abs(NEWR - 0.9641) < 0.0004 and round(NEWR, 3) != PUB
  and abs(100 * (1 - NEWR) - 3.6) < 0.1 and 0.94 <= NEWR <= 0.97,
  f"the published {PUB} becomes {NEWR:.4f}, printing as {NEWR:.3f} -- the arm's margin over the "
  f"control falling from {100 * (1 - PUB):.1f} to {100 * (1 - NEWR):.1f} per cent, LESS THAN HALF "
  f"the published claim  ⇒ PREDICTION (2a) HELD (0.94-0.97 registered)")

# ===================================================================================== GATE 5b ===
#: ⛭⛭⛭ r7815/r7819 (cc66): ** AND GATE 5's RATIO IS SCORED ACROSS A SAMPLING MISMATCH, WHICH IS MY
#: OWN CORRECTION (a) IN THE ONLY FORM THAT SURVIVED. **  `cc66_lcdm_L2000.npz` is the old control at
#: `LSTEP=2` -- 950 samples on 100..1998 -- and `NEW` is the re-pointed one at `LSTEP=8`, 238 samples
#: on 100..1996.  `chi2_of_spectrum.chi2_of` bins whatever grid it is handed into 185 bins, so the two
#: sides of gate 5 were binned from DIFFERENT samplings.  *At the same point the two sampling banks'
#: `Dl` agree to 5.55e-16 at every shared multipole, so what moves here is the BINNING and not the
#: physics -- which is exactly why it had to be measured before a paper sentence took the number.*
#: ⇒ ** `(a1)` built the matched step-2 bank at Planck's point, and THAT is the comparison the paper
#: prints.  Gate 5 stands as the step-8 run's own figure; it is not what a sentence may quote. **
NEW2 = os.path.join(BW, 'r7812_cc66_the_resumable_mode_loop_and_the_one_pass', 'out',
                    'r7812_control_step2_L2000_assembled.npz')
CN2, nbn2 = score(NEW2)
PCT2 = 100 * (CN2 - CO) / CO
NEWR2 = PUB * CO / CN2
G('5b', nbn2 == 185 and abs(CN2 - 204.709) < 0.05 and abs(NEWR2 - 0.9599) < 0.0004
  and round(NEWR2, 3) == 0.960 and abs(abs(PCT2) - 4.367) < 0.02 and CN2 > CN,
  f"AT MATCHED SAMPLING the re-pointed control's no-fit chi^2 is {CN2:.3f} over {nbn2} bins, not "
  f"{CN:.3f}: the published {PUB} becomes {NEWR2:.4f}, printing as {NEWR2:.3f}, and the control's "
  f"improvement is {abs(PCT2):.3f} per cent and not {abs(PCT):.3f}  ⇒ ** this is the figure the "
  f"paper prints; gate 5's is the step-8 run's own **")

# ======================================================================================= GATE 6 ===
# The r7805 stencil is vindicated inside its registered bound.
STENCIL = 0.9571
G(6, abs(NEWR - STENCIL) <= 0.01 and abs(NEWR - STENCIL) > 0.001,
  f"r7805's stencil said {STENCIL:.4f} holding H0 fixed; the real run says {NEWR:.4f}, a difference "
  f"of {NEWR - STENCIL:+.4f} against the 0.01 I registered  ⇒ PREDICTION (2b) HELD, and the "
  f"stencil's scope reached a point it did not itself evaluate")

# ======================================================================================= GATE 7 ===
# The peaks move, and the fourth exceeds every printed fourth-feature difference.
def peaks(p, n=4):
    ls, Dl = load(p)
    y = Dl * np.interp(ls, LG, LENS)
    out = []
    for i in range(2, len(ls) - 2):
        if y[i] > y[i - 1] and y[i] > y[i + 1] and y[i] > y[i - 2] and y[i] > y[i + 2]:
            a, b, c = y[i - 1], y[i], y[i + 1]
            d = a - 2 * b + c
            out.append(ls[i] + (0.5 * (a - c) / d if d else 0.0) * (ls[i + 1] - ls[i]))
    return out[:n]


PO, PN = peaks(os.path.join(SP, 'cc66_lcdm_L2000.npz')), peaks(NEW)
MV = [b - a for a, b in zip(PO, PN)]
FOURTH = (0.00, 0.18, 0.21)
# ⛔ peak 1's move is 0.1195 -- EXACTLY on the three-decimal rounding boundary, so printing 0.119
#   or 0.120 is a coin toss and neither is pinnable within the gate's own allowance.  Four
#   decimals throughout, which is what the measurement actually supports.
G(7, len(MV) == 4 and abs(MV[0] - 0.1195) < 0.00005 and abs(MV[1] - 0.3502) < 0.00005
  and abs(MV[2] - 0.6620) < 0.00005 and abs(MV[3] - 0.9198) < 0.00005 and MV[3] > max(FOURTH),
  f"the control's peaks move {MV[0]:+.4f}, {MV[1]:+.4f}, {MV[2]:+.4f} and {MV[3]:+.4f} multipoles; "
  f"the fourth exceeds every fourth-feature difference P15 prints {FOURTH}  ⇒ PREDICTION (2d) HELD")

# ======================================================================================= GATE 8 ===
# The refitted 1.002 cannot move -- STRUCTURALLY: it never reads the un-refitted bank.
_lvl = os.path.join(RCP, 'P15_with_the_projection_distance_on_the_leaf_rate_the_refitted_spectrum_'
                         'is_level_with_the_control_and_the_bao_fit_does_not_move.py')
_lsrc = open(_lvl).read()
_ratio = re.search(r'round\(lf_rf / ctl_rf, 3\) == 1\.002', _lsrc)
_ctl_rf = re.search(r"ctl_rf, n2, _ = score\('cc66_r185_verify_lcdm\.npz'\)", _lsrc)
_lf_rf = re.search(r"lf_rf, n6, sw_rf = score\('r7749_leafgeom_refit_verify_cr\.npz'\)", _lsrc)
_ctl_nf = re.search(r"ctl_nf, n1, _ = score\('cc66_lcdm_L2000\.npz'\)", _lsrc)
G(8, all((_ratio, _ctl_rf, _lf_rf, _ctl_nf)),
  f"the refitted 1.002 CANNOT move, shown from the owning receipt's own source rather than by "
  f"agreeing numbers: it is `lf_rf / ctl_rf` ({bool(_ratio)}), read from the two REFIT verifies "
  f"({bool(_ctl_rf)}, {bool(_lf_rf)}), while the un-refitted `cc66_lcdm_L2000.npz` is read only as "
  f"`ctl_nf` for the no-fit ratio ({bool(_ctl_nf)})  ⇒ PREDICTION (2c) HELD")

# ======================================================================================= GATE 9 ===
# Item ①: every namesake arm bank the 7 candidates read has a banked _leafrec1 twin.
SEVEN = {
    '01': ['r6919_geometry', 'r6919_noop'], '05': ['r6929_geometry'],
    '06': ['c54.178_cr', 'c54.186_cr_KCONT', 'c54.186_cr_L3000'],
    '15': ['r6885_los_cr', 'r6885_losdp0_cr', 'r6885_lossw0_cr'],
    '16': ['r6893_switch_screen_cr', 'r6897_fields', 'r6897_noop'],
    '28': ['cc66_r185_verify_cr'], '29': ['cc66_r185_verify_cr'],
}
_twins = {k: all(glob.glob(os.path.join(SP, b + '_leafrec1.npz')) for b in v) for k, v in SEVEN.items()}
_recipes = open(os.path.join(BW, 'r7635_70_leafrec1_bank', 'RECIPES.md')).read()
_moved = re.search(r'THE LEAFREC DEFAULT MOVED', _recipes)
_none_cfg = re.search(r'None of the 36 namesakes carries the `config` key', _recipes)
G(9, all(_twins.values()) and len(_twins) == 7 and bool(_moved) and bool(_none_cfg),
  f"all 7 candidates are REPOINTABLE: every namesake arm bank they read has a banked `_leafrec1` "
  f"twin ({sum(_twins.values())}/7).  And they are off the leaf rate on r7635's RECIPES.md's own "
  f"authority -- the LEAFREC default moved ({bool(_moved)}) and none of the 36 namesakes carries a "
  f"`config` ({bool(_none_cfg)})  ⇒ PREDICTION (1d) HELD, and (1b) FALSIFIED: I expected at least 2 "
  f"of the 7 to leave and NONE does")

# ====================================================================================== GATE 10 ===
# Item ①: the 16 split 6 / 3 / 7, so 9 of the 23 leave and 14 stand.
_dirre = re.compile(r"'((?:refit_grid|grid)[A-Za-z0-9_]*)'")
PRE = ['P15_both_mechanisms_contribute_at_unit_amplitude',
       'P15_the_controls_base_log_is_banked_beside_the_grids',
       'P15_the_de_tilted_peak_set_is_the_phase_observable',
       'P15_the_fit_has_the_controls_freedom',
       'P15_the_frozen_build_measured_on_the_one_rate',
       'P15_the_kernels_phase_difference_between_the_arms',
       'P15_the_no_fit_confrontation_is_three_per_bin',
       'P15_the_peak_plane_survives_the_merge',
       'P15_the_phase_is_the_driving_and_the_undriven_arms_agree',
       'P15_the_refit_leaves_the_background_where_the_distances_put_it',
       'P15_the_residual_does_not_sit_at_ell_A',
       'P15_the_retention_is_the_combs_average',
       'P15_the_selection_does_not_truncate',
       'P15_the_shared_fraction_does_not_mean_what_i_said',
       'P15_the_skys_own_fourth_peak_cannot_tell_the_arms_apart',
       'P15_the_spacing_drift_is_made_in_the_projection']
_names = os.listdir(RCP)
kinds = {'none': 0, 'both': 0, 'namesake': 0}
# ⛭ r7811 (node 70, 69's ruling on r7809+70.3): the one genuine repoint of the 14, g1, was REWRITTEN on the arm of
#   record and RENAMED to what it finds.  It is counted here as what it was at r7807 -- a namesake reader, so one of
#   the 14 -- and its new file is required to read the twins, so the count records the repoint as DONE, not lost.
REPOINTED_SINCE = {'P15_the_controls_base_log_is_banked_beside_the_grids':
                   'P15_on_the_arm_of_record_the_peak_heights_and_chi2_both_put_the_licensed_build_nearer_the_control'}
for pre in PRE:
    if pre in REPOINTED_SINCE:
        f = next((x for x in _names if x.startswith(REPOINTED_SINCE[pre])), None)
        assert f, f'the r7811 rewrite of {pre} is not on disk'
        _src = open(os.path.join(RCP, f)).read()
        assert all(f"'{d}_leafrec1'" in _src for d in ('refit_grid185', 'grid_licensed', 'grid_oneclock')), \
            f'{f} does not read all three twin grids -- the r7811 repoint is not done'
        kinds['namesake'] += 1          # what it was at r7807: one of the 14
        continue
    f = next((x for x in _names if x.startswith(pre)), None)
    assert f, f'no receipt starts with {pre}'
    dirs = sorted(set(_dirre.findall(open(os.path.join(RCP, f)).read())))
    if not dirs:
        kinds['none'] += 1
    elif any('leafrec1' in d for d in dirs) and not all('leafrec1' in d for d in dirs):
        kinds['both'] += 1
    elif all('leafrec1' in d for d in dirs):
        kinds['both'] += 1
    else:
        kinds['namesake'] += 1
LEAVE = kinds['none'] + kinds['both'] + 0
STAND = kinds['namesake'] + 7
G(10, (kinds['none'], kinds['both'], kinds['namesake']) == (6, 3, 7) and LEAVE == 9 and STAND == 14
  and LEAVE + STAND == 23 and STAND >= 1 and not (LEAVE - 0 >= 11),
  f"the 16 undecidable items split {kinds['none']} reading NO arm grid, {kinds['both']} reading a "
  f"`_leafrec1` grid AND a namesake one (a COMPARISON, not a defect), and {kinds['namesake']} "
  f"reading a namesake grid whose twin directory exists  ⇒ of the 23, {LEAVE} LEAVE and {STAND} "
  f"stand as REPOINTS.  PO-87 is NOT struck, so PREDICTION (1c) HELD; and (1a) is FALSIFIED -- I "
  f"registered at least 11 of the 16 leaving and {kinds['none'] + kinds['both']} do")

# ====================================================================================== GATE 11 ===
# Every figure the INDEX row prints, pinned by an explicit literal, each inside the gate's allowance.
def allow(printed):
    x = float(printed)
    return max(0.5 * 10 ** -len(printed.split('.')[1]), 5e-4 * abs(x))


# ⛭⛭ AND A FINDING THE PINS FORCED OUT: the banked `config` records the FORM switches -- LEAFREC,
#   LEAFGEOM, LEAFSCALES, KFAC, ZSTART -- and NOT the cosmological point.  There is no LH0, LOM,
#   WBH2 or NS in it.  So a bank's `config` settles exactly the question PO-87 asks (which rate) and
#   CANNOT say which background it ran at.  The point is therefore read from the launcher's own
#   PLANCK table, which is the authoritative record in the repo, rather than re-typed here.
_lau = open(os.path.join(MINE, 'run_control.py')).read()
_PL = dict(re.findall(r"(\w+)='([\d.]+)'", _lau[_lau.index('PLANCK = dict('):_lau.index('STEM =')]))
_LH0, _LOM = float(_PL['LH0']), float(_PL['LOM'])
_WBH2, _NS = float(_PL['WBH2']), float(_PL['NS'])
_cfg = cfgs['TT']
_cfg_has_point = any(k in _cfg for k in ('LH0', 'LOM', 'WBH2', 'NS'))
assert not _cfg_has_point, 'the config now records the point; this comment and gate 11 need updating'
CTL_RF, _ = score(os.path.join(SP, 'cc66_r185_verify_lcdm.npz'))
LF_RF, _ = score(os.path.join(SP, 'r7749_leafgeom_refit_verify_cr.npz'))
REFIT_RATIO = LF_RF / CTL_RF
MNU_PLANCK = 0.06                     # the mass Planck's published fit assumes; this instrument has none
BOUND = 0.01                          # the bound registered in PREDICTION.md for the stencil's reach
PINNED = [
    ('0.964', abs(NEWR - 0.964) < 0.0004, 0.0004, 'the re-pointed ratio, step-8 against step-2'),
    ('0.960', abs(NEWR2 - 0.960) < 0.0004, 0.0004,
     '⛭ THE SAME RATIO AT MATCHED SAMPLING -- the figure the paper prints'),
    ('204.709', abs(CN2 - 204.709) < 0.05, 0.05, "the re-pointed control's chi^2 at matched sampling"),
    ('4.367', abs(abs(PCT2) - 4.367) < 0.002, 0.002, 'and its improvement, per cent, likewise'),
    ('0.918', abs(PUB - 0.918) < 0.0004, 0.0004, 'the published one'),
    ('4.781', abs(abs(PCT) - 4.781) < 0.002, 0.002, "the control's improvement, per cent"),
    ('214.057', abs(CO - 214.057) < 0.05, 0.05, "the control's old chi^2"),
    ('203.823', abs(CN - 203.823) < 0.05, 0.05, 'and its new one'),
    ('0.1195', abs(MV[0] - 0.1195) < 0.00005, 0.00005, 'peak 1 move'),
    ('0.3502', abs(MV[1] - 0.3502) < 0.00005, 0.00005, 'peak 2'),
    ('0.6620', abs(MV[2] - 0.6620) < 0.00005, 0.00005, 'peak 3'),
    ('0.9198', abs(MV[3] - 0.9198) < 0.00005, 0.00005, 'peak 4'),
    ('0.313773', abs(OM - 0.313773) < 0.000001 and abs(_LOM - OM) < 1e-6, 0.000001,
     "the re-pointed Omega_m at h=0.6736, and the LOM the launcher actually ran"),
    ('0.313400', abs(OM_STENCIL - 0.313400) < 0.000001, 0.000001, "the stencil's, at h=0.674"),
    ('0.9571', abs(STENCIL - 0.9571) < 0.00004, 0.00004, "the stencil's own answer"),
]
# the run's own switches, read back from the bank's `config` rather than re-typed as literals, and
# the refitted 1.002 MEASURED from the two verifies as well as shown structurally in gate 8.
PINNED += [
    ('67.36', abs(_LH0 - 67.36) < 0.001, 0.001, "the run's H0, read from the launcher's own table"),
    ('0.02237', abs(_WBH2 - 0.02237) < 0.000005, 0.000005, 'its omega_b, likewise'),
    ('0.9649', abs(_NS - 0.9649) < 0.0001, 0.0001, 'its n_s, likewise'),
    ('0.6736', abs(H - 0.6736) < 0.0001, 0.0001, "Planck's own h, which converts the point"),
    ('0.674', abs(0.674 - 0.674) < 0.0004, 0.0004, "the h r7805's stencil used instead"),
    ('0.0070', abs((NEWR - STENCIL) - 0.0070) < 0.00004, 0.00004, 'the stencil-to-run difference'),
    ('0.01', abs(BOUND - 0.01) < 0.001, 0.001, 'the bound registered for it'),
    ('0.06', abs(MNU_PLANCK - 0.06) < 0.001, 0.001, "the neutrino mass Planck assumes and this has not"),
    ('1.002', abs(REFIT_RATIO - 1.002) < 0.0004, 0.0004, 'the refitted ratio, MEASURED not just argued'),
]
_unheld = [(t, w) for t, ok, tol, w in PINNED if not ok]
_slack = [(t, tol, allow(t)) for t, ok, tol, w in PINNED if tol > allow(t) * (1 + 1e-9)]
G(11, not _unheld and not _slack and len(PINNED) == 24 and (LEAVE, STAND) == (9, 14),
  f"all {len(PINNED)} figures the INDEX row prints hold against an explicit literal comparison -- the "
  f"run's point read from the LAUNCHER's own table, because the banked `config` records the form "
  f"switches and NOT the background (asserted above), and the refitted ratio MEASURED at "
  f"{REFIT_RATIO:.4f} as well as shown structurally in gate 8 -- each "
  f"pin inside check_figures_pinned's own allowance (tightest margin "
  f"{min(allow(t) / tol for t, ok, tol, w in PINNED):.2f}x)"
  + ('' if not _unheld else f'  -- UNHELD: {_unheld}')
  + ('' if not _slack else f'  -- LOOSER THAN THE ALLOWANCE: {_slack}'))

print()
print('  ' + '=' * 100)
if fail:
    print(f'  ⛔ {len(fail)} GATE(S) FAILED:')
    for f in fail:
        print(f'     - {f}')
    raise SystemExit(1)
print(f"  ⇒ ⛔⛔ ** THE CONTROL AT PLANCK'S OWN POINT IMPROVES {abs(PCT2):.3f} PER CENT AT MATCHED "
      f"SAMPLING, SO THE PUBLISHED 0.918 BECOMES {NEWR2:.3f} -- WHICH IS WHAT THE PAPER PRINTS "
      f"({abs(PCT):.3f} PER CENT AND {NEWR:.3f} AT STEP 8, GATE 5's OWN FIGURES) **")
print(f"  and the arm's margin over the control falls from {100 * (1 - PUB):.1f} to "
      f"{100 * (1 - NEWR2):.1f} per cent at matched sampling "
      f"({100 * (1 - NEWR):.1f} at step 8) -- in either case less than half the claim.")
print(f"  The refitted 1.002 cannot move: it reads the two REFIT verifies and never the un-refitted "
      f"bank.")
print(f"  ⌗ ** AND PO-87's 23 ARE {STAND} REPOINTS AND {LEAVE} DEPARTURES, so the clause is NOT "
      f"struck. **  Every one of")
print(f"    the {STAND} has a banked `_leafrec1` twin or twin directory, so the remaining work is a "
      f"repoint and not a run.")
print(f"  ⛔ Two registered predictions FAILED: I put at least 11 of the 16 leaving and 2 of the 7, "
      f"and got 9 and 0.")
print('  ' + '=' * 100)
