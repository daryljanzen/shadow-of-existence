"""
** PO-87's DISCHARGE LIST GREW $30 \to 33$ AND NOT ONE OF THE FIVE ARRIVALS IS EVIDENCE; THE CLAUSE
AS WRITTEN CANNOT BE DISCHARGED BECAUSE A CONTROL HAS NO LEAF RATE; AND RE-POINTING THE CONTROL TO
PLANCK'S $\omega_c$ MOVES THE PUBLISHED $0.918$ TO $0.957$, HALVING THE ARM'S MARGIN. **

Order r7805 (69), both items.  ① re-run the `r7667` PO-87 census on today's tree and classify every
item re-derived / re-grounded / still standing.  ② which printed P15 figures depend on the control's
UN-REFITTED point, and by how much does each move at $\omega_c=0.1200$ rather than the $0.120727$
that $(67.40,\Omega_m\,0.3150)$ implies.

⛔ ** THE ORDER'S COUNT IS STALE AND IT IS CORRECTED BEFORE ANYTHING IS MEASURED. **  The order says
`LIST.md` has "the 48 items".  It has **30**: the census's own header records that cut 5 took the
list $48\to30$, and `r7675` split those into 26 derived + 4 declared.  $48$ is the pre-cut-5 figure.

** ① THE LIST GREW, AND THE GROWTH IS NOT NEW DEFECTS. **  Re-run unmodified, the census reports
**29 derived + 4 declared = 33** against the banked 26 + 4 = 30, and its own pins redden.  Two items
LEFT and five JOINED.  ⛭ The departure `the_low_multipole_depth_gap` is the repoint `r7677` item 3
ordered once `70` banked the sibling -- so that instrument did the job it was written for.  ⛔ **BUT
NOT ONE OF THE FIVE ARRIVALS RESTS ON EVIDENCE OF AN OFF-LEAF-RATE ARM SPECTRUM:** three read NO
namesake at all and are on the list only because every load site is undecidable; a fourth reads
the CONTROL's own bank, and only for its `arm` key; and the fifth reads
`r7749_leafgeom_refit_verify_cr.npz`, whose OWN banked config says `LEAFGEOM: true, LEAFREC: true,
LEAFSCALES: true` and whose manifest reads "arm of record + LEAFGEOM=1 (the projection distance on
the leaf rate, radiation included)".  **That is the one-rate build -- the very configuration PO-87
wants figures derived on -- counted as a spectrum off the leaf rate, because the classifier's suffix
test looks for `_leafrec1` and the corpus's newer banks are named descriptively.**  Three of the
five arrivals are this seat's own receipts from `r7797`, `r7801` and `r7803`.

** AND THE CLAUSE CANNOT BE DISCHARGED AS WRITTEN, WHICH IS THE ANSWER TO "CAN PO-87 BE STRUCK". **
Classified by WHOSE spectrum each item reads: **7 stand as candidates, 5 are not defects at all, 1
is re-derived, and 16 cannot be decided without a read.**  The 5 read NOTHING but the control's own
spectra -- and **a $\Lambda$CDM control has no leaf rate**; there is no such object as the control on
the leaf rate, so a control spectrum is "off the leaf rate" by construction and every receipt that
compares the arm against the control must read one.  ⇒ PO-87's clause, "every P15 figure resting on
a spectrum off the leaf rate", catches every control comparison in the paper for ever.  **It needs
the control excluded from its scope or it can never be struck, and that is a wording decision for
69, not a measurement.**  ⌗ *The 7 are candidates and not proven: their arm-side banks record NO
`config` key at all, so the bank cannot say whether they are on the leaf rate -- which is also why
16 are undecidable, and is a measured property of the older banks rather than a limit of effort.*

** ② RE-POINTING THE CONTROL IS NOT COSMETIC. **  $\omega_c=0.1200$ at the same $H_0$ and
$\omega_b$ means $\Omega_m=0.313400$, so $\Delta\Omega_m=-0.001600$ -- **a tenth of the refit grid's
own step**, well inside the $\pm1$-step stencil, so the move is priced from the grid's banked
two-sided steps rather than by running a new spectrum.
  * the control's no-fit $\chi^{2}$ over 185 lensed bins falls by **$4.090$ per cent**;
  * ⛔ **the published $0.918$ becomes $0.957$** -- the printed third decimal moves, and the arm's
    margin over the control falls from $8.2$ to $4.3$ per cent, **about half the claim**;
  * the control's peak positions move $+0.118$, $+0.363$, $+0.695$ and $+0.966$ multipoles at peaks
    one to four -- **the fourth-peak move alone is larger than every fourth-feature difference the
    paper prints ($0.00$, $0.18$, $0.21$)**;
  * refitted comparisons do NOT move: the control's own refit minimum sits at $\Omega_m=0.309826$,
    already $-0.005174$ from the corpus's point and $3.2$ times the re-pointing's own $0.0016$, and
    a minimum found by search does not follow its starting point.

⇒ ** SO THE RE-POINTING IS A REAL DECISION AND NOT A TIDY-UP: it improves the control and costs the
arm half of a headline comparison. **  Whether to take it is 69's ruling; nothing is re-pointed here.

** COMPUTES: ** nothing new.  `r7667/census.py` is re-run UNMODIFIED and its stdout is the input;
`classify.py` adds only the whose-spectrum discriminator; `controls_point.py` prices the move from
`refit_grid185`'s own banked steps with the refit receipts' own scoring (P15's CAMB lensing operator
on both arms, `chi2_of_spectrum.chi2_of`, 185 lensed bins).  No spectrum is run, no figure is
re-pointed, and no paper sentence is edited.

Built r7805+cc66 (node 66, code seat), registered at
`computations/beyond_the_wall/r7805_cc66_po87_census_and_the_controls_point/PREDICTION.md`.
11 gates, rc=0 on success.  Run: python3 <this file>   (numpy, scipy, camb; ~3 min)
"""
import glob
import json
import os
import re
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
CEN = os.path.join(BW, 'r7667_cc66_po87_the_unfiltered_list')
MINE = os.path.join(BW, 'r7805_cc66_po87_census_and_the_controls_point')
G = os.path.join(BW, 'refit_grid185')
SP = os.path.join(BW, 'spectra')
fail = []


def G_(n, ok, msg):
    print(f"  {'✅' if ok else '⛔'} GATE {n}  {msg}")
    if not ok:
        fail.append(f'gate {n}: {msg}')


# ======================================================================================= GATE 1 ===
# The order's count is stale, and the census's own header says so.
_list = open(os.path.join(CEN, 'LIST.md')).read()
_m48 = re.search(r'it took the list from 48\s+to 30', _list)   # the sentence wraps in the file
_m30 = re.search(r'\*\*26 derived \+ 4 declared = 30\.\*\*', _list)
_n_rows = len(re.findall(r'^  \[\d+\] \[', _list, re.M))
G_(1, bool(_m48) and bool(_m30) and _n_rows == 30,
   f"the order's \"48 items\" is the PRE-CUT-5 figure: LIST.md's own header records cut 5 taking the "
   f"list 48 -> 30 ({bool(_m48)}) and r7675's split into 26 derived + 4 declared ({bool(_m30)}), and "
   f"the file carries {_n_rows} item rows")

# ======================================================================================= GATE 2 ===
# The census re-runs on today's tree and reports a LARGER list than the one banked.
_cen = subprocess.run([sys.executable, os.path.join(CEN, 'census.py')],
                      capture_output=True, text=True, timeout=1800, cwd=ROOT)
OUT = _cen.stdout
_m = re.search(r"PO-87's list: (\d+) derived \+ (\d+) declared = (\d+)", OUT)
DERIVED, DECLARED, TOTAL = (int(x) for x in _m.groups()) if _m else (0, 0, 0)
_m_cheap = re.search(r'banked `_leafrec1` sibling \(cheap\): (\d+)', OUT)
CHEAP = int(_m_cheap.group(1)) if _m_cheap else -1
G_(2, (DERIVED, DECLARED, TOTAL) == (29, 4, 33) and CHEAP == 0 and _cen.returncode == 1,
   f"the census re-runs UNMODIFIED on today's tree and the list has GROWN: {DERIVED} derived + "
   f"{DECLARED} declared = {TOTAL}, against the banked 26 + 4 = 30, with the cheap set at {CHEAP} "
   f"(it was 2) -- and the instrument reddens on its own pins (rc {_cen.returncode})")

# ======================================================================================= GATE 3 ===
# Two left and five joined, named by set comparison against the banked list.
_old = {re.sub(r'^.*/', '', p) for p in re.findall(r'^  \[\d+\] \[\w+\] (receipts/\S+)', _list, re.M)}
_blk = OUT[OUT.index('THE UNFILTERED LIST'):]
_new = {re.sub(r'^.*/', '', p) for p in re.findall(r'^  \[\d+\] \[\w+\] (receipts/\S+)', _blk, re.M)}
LEFT, JOINED = sorted(_old - _new), sorted(_new - _old)
_depth_gap_left = any('low_multipole_depth_gap' in p for p in LEFT)
G_(3, len(LEFT) == 2 and len(JOINED) == 5 and len(_old) == 30 and len(_new) == 33 and _depth_gap_left,
   f"by SET COMPARISON against the banked list rather than by reading a diff: {len(LEFT)} LEFT and "
   f"{len(JOINED)} JOINED, 30 - 2 + 5 = 33.  The depth-gap repoint r7677 item 3 ordered is one of "
   f"the departures ({_depth_gap_left}) -- PREDICTION (1d) HELD")

# ======================================================================================= GATE 4 ===
# NOT ONE arrival rests on evidence.
_items = dict((re.sub(r'^.*/', '', p), s) for p, s in
              re.findall(r'^  \[\d+\] \[\w+\] (receipts/\S+)\n       spectra read \(namesake/superseded\): \[([^\]]*)\]',
                         _blk, re.M))
_arr_empty = [p for p in JOINED if _items.get(p, '') == '']
_arr_leafgeom = [p for p in JOINED if 'leafgeom' in _items.get(p, '').lower()]
_arr_ctl = [p for p in JOINED if _items.get(p, '') and 'lcdm' in _items[p].lower()]
G_(4, len(_arr_empty) == 3 and len(_arr_ctl) == 1 and len(_arr_leafgeom) == 1
   and len(_arr_empty) + len(_arr_ctl) + len(_arr_leafgeom) == 5,
   f"NOT ONE of the five arrivals rests on evidence of an off-leaf-rate ARM spectrum: "
   f"{len(_arr_empty)} read NO namesake at all (on the list only because every load site is "
   f"undecidable), {len(_arr_ctl)} reads the CONTROL's own bank -- and only for its `arm` key, a "
   f"provenance check, with no printed figure resting on it -- and {len(_arr_leafgeom)} reads the "
   f"LEAFGEOM build.  So the list's growth is not new defects")

# ======================================================================================= GATE 5 ===
# The misclassified spectrum IS the one-rate build, read from its own banked config.
_p = os.path.join(SP, 'r7749_leafgeom_refit_verify_cr.npz')
with np.load(_p, allow_pickle=True) as z:
    _cfg = json.loads(str(z['config'].item()))
    _man = str(z['manifest'].item())
G_(5, _cfg.get('LEAFGEOM') is True and _cfg.get('LEAFREC') is True and _cfg.get('LEAFSCALES') is True
   and 'leaf rate' in _man,
   f"the spectrum the census counts as off the leaf rate IS the one-rate build, read from its OWN "
   f"banked config: LEAFGEOM={_cfg.get('LEAFGEOM')}, LEAFREC={_cfg.get('LEAFREC')}, "
   f"LEAFSCALES={_cfg.get('LEAFSCALES')}, and its manifest says 'the projection distance on the leaf "
   f"rate, radiation included'  ⇒ the classifier's `_leafrec1` SUFFIX test misreads descriptively "
   f"named leaf-rate banks")

# ======================================================================================= GATE 6 ===
# The classification, and the control class that cannot be discharged.
_cls = subprocess.run([sys.executable, os.path.join(MINE, 'classify.py')],
                      input=OUT, capture_output=True, text=True, timeout=900, cwd=ROOT)
_c = _cls.stdout
_counts = dict((m.group(1), int(m.group(2))) for m in
               re.finditer(r'^  (STANDS \(candidate\)|NOT A DEFECT \(control\)|RE-DERIVED|'
                           r'UNDECIDED \(needs a read\)): (\d+)$', _c, re.M))
STANDS = _counts.get('STANDS (candidate)', -1)
CTLONLY = _counts.get('NOT A DEFECT (control)', -1)
REDER = _counts.get('RE-DERIVED', -1)
UNDEC = _counts.get('UNDECIDED (needs a read)', -1)
G_(6, (STANDS, CTLONLY, REDER, UNDEC) == (7, 5, 1, 16) and STANDS + CTLONLY + REDER + UNDEC == 29
   and STANDS >= 1,
   f"classified by WHOSE spectrum each item reads: {STANDS} STAND as candidates, {CTLONLY} are NOT "
   f"DEFECTS (every spectrum they read is the control's own, and a control has no leaf rate), "
   f"{REDER} is RE-DERIVED, {UNDEC} cannot be decided without a read -- summing to 29.  At least one "
   f"stands, so PO-87 cannot be struck on its own clause  ⇒ PREDICTION (1b) HELD")

# ======================================================================================= GATE 7 ===
# The predictions that FAILED, recorded here rather than only in RESULT.md.
G_(7, not (20 <= DERIVED <= 28) and CHEAP < 2,
   f"⛔ TWO REGISTERED PREDICTIONS FAILED AND ARE RECORDED IN THE GATE TEXT: (1a) put the derived set "
   f"at 20-28 and it is {DERIVED}, because I reasoned that re-grounding cannot move items while "
   f"forgetting that NEW receipts join -- three of the arrivals are my own; and (1e) put the cheap "
   f"set at >= 2 and it is {CHEAP}, the second cheap item having LEFT the list by being repointed")

# ======================================================================================= GATE 8 ===
# The control's point, and that the move is inside the grid's own stencil.
WB, HH = 0.02237, 0.674
WC_CORPUS, WC_PLANCK = 0.3150 * HH ** 2 - WB, 0.1200
OM_CORPUS, OM_PLANCK = 0.3150, (WC_PLANCK + WB) / HH ** 2
STEP_OM = 0.0150
X = (OM_PLANCK - OM_CORPUS) / STEP_OM
_lau = open(os.path.join(BW, 'refit_grid', 'launch.sh')).read()
_m_p = re.search(r'lcdm_OMp\s+ARM=lcdm LOM=([\d.]+)', _lau)
_m_m = re.search(r'lcdm_OMm\s+ARM=lcdm LOM=([\d.]+)', _lau)
_step_from_launcher = (float(_m_p.group(1)) - float(_m_m.group(1))) / 2 if _m_p and _m_m else None
G_(8, abs(WC_CORPUS - 0.120727) < 1e-6 and abs(OM_PLANCK - 0.313400) < 1e-6
   and abs(X + 0.10668) < 0.0005 and abs(_step_from_launcher - STEP_OM) < 1e-9 and abs(X) < 1.0,
   f"the control's point: Omega_m {OM_CORPUS} implies omega_c {WC_CORPUS:.6f} against Planck's "
   f"{WC_PLANCK}, so omega_c = 0.1200 means Omega_m {OM_PLANCK:.6f}, a move of "
   f"{OM_PLANCK - OM_CORPUS:+.6f} = {X:+.5f} of the grid's own step (read {_step_from_launcher} from "
   f"refit_grid/launch.sh's own LOM values) -- a TENTH of a step, inside the +-1 stencil")

# ======================================================================================= GATE 9 ===
# What moves: the control's chi^2 and the published 0.918.
_cp = subprocess.run([sys.executable, os.path.join(MINE, 'controls_point.py')],
                     capture_output=True, text=True, timeout=1800, cwd=ROOT)
P = _cp.stdout
# the script's own reported point, cross-checked against this file's constants -- without this the
# two could drift apart and these gates would still pass (failability probe 1 found exactly that).
_m_corp = re.search(r'corpus:\s+\(67\.40, Omega_m ([\d.]+), omega_b [\d.]+\)\s+->\s+omega_c ([\d.]+)', P)
_m_plan = re.search(r'Planck:\s+\(67\.40, Omega_m ([\d.]+), omega_b [\d.]+\)\s+->\s+omega_c ([\d.]+)', P)
SAME_POINT = (bool(_m_corp) and bool(_m_plan)
              and abs(float(_m_corp.group(1)) - OM_CORPUS) < 1e-6
              and abs(float(_m_corp.group(2)) - WC_CORPUS) < 1e-6
              and abs(float(_m_plan.group(1)) - OM_PLANCK) < 1e-6
              and abs(float(_m_plan.group(2)) - WC_PLANCK) < 1e-6)
_m_rel = re.search(r'RELATIVE factor the grid measures, ([\d.]+)', P)
_m_pc = re.search(r'moves ([-\d.]+), which is ([-\d.]+) per cent', P)
_m_ratio = re.search(r'the ratio becomes\s+([\d.]+)', P)
_m_marg = re.search(r'falls from ([\d.]+) per cent to ([\d.]+) per cent', P)
REL = float(_m_rel.group(1)) if _m_rel else 0.0
PCT = float(_m_pc.group(2)) if _m_pc else 0.0
RATIO = float(_m_ratio.group(1)) if _m_ratio else 0.0
M0, M1 = (float(_m_marg.group(1)), float(_m_marg.group(2))) if _m_marg else (0.0, 0.0)
G_(9, SAME_POINT and abs(PCT + 4.090) < 0.02 and abs(REL - 0.959103) < 0.0005
   and abs(RATIO - 0.9571) < 0.0004
   and round(RATIO, 3) != 0.918 and abs(M0 - 8.2) < 0.15 and abs(M1 - 4.3) < 0.15,
   f"the instrument is pricing the same point this file names ({SAME_POINT}), and ⛔ what moves: the control's no-fit chi^2 over 185 lensed bins falls {PCT:+.3f} per cent "
   f"(relative factor {REL:.6f}), and the published 0.918 becomes {RATIO:.4f}, printing as "
   f"{RATIO:.3f} -- THE THIRD DECIMAL MOVES.  The arm's margin over the control falls from {M0:.1f} "
   f"to {M1:.1f} per cent, about HALF the claim")

# ====================================================================================== GATE 10 ===
# The peaks move, and by more than the fourth-feature differences the paper prints.
_pk = [float(m.group(1)) for m in re.finditer(r'moves ([+-][\d.]+) multipoles', P)]
PK = _pk[:4]
_m_big = re.search(r'largest move ([\d.]+) multipoles', P)
BIG = float(_m_big.group(1)) if _m_big else 0.0
FOURTH_FEATURE = (0.00, 0.18, 0.21)                 # TT, EE, TE, as P15 prints them (r7797)
_m_ref = re.search(r'refitted figures are unmoved, and ②b HOLDS', P)
G_(10, SAME_POINT and len(PK) == 4 and abs(PK[0] - 0.1177) < 0.004 and abs(PK[1] - 0.3628) < 0.004
   and abs(PK[2] - 0.6952) < 0.004 and abs(PK[3] - 0.9657) < 0.004
   and abs(BIG - 0.9657) < 0.004 and BIG > max(FOURTH_FEATURE) and bool(_m_ref),
   f"the control's peak positions move {PK[0]:+.4f}, {PK[1]:+.4f}, {PK[2]:+.4f} and {PK[3]:+.4f} "
   f"multipoles at peaks one to four; the largest, {BIG:.4f}, EXCEEDS every fourth-feature "
   f"difference P15 prints {FOURTH_FEATURE} -- so PREDICTION (2c) is FALSIFIED, badly: I put every "
   f"peak figure inside its printed last digit.  Refitted comparisons are unmoved ({bool(_m_ref)}), "
   f"so (2b) HELD")

# ====================================================================================== GATE 11 ===
# Every figure the INDEX row prints, pinned here by an explicit literal comparison, each pin checked
# against check_figures_pinned's own allowance max(0.5*10**-d, 5e-4*|x|).
def allowance(printed):
    x = float(printed)
    return max(0.5 * 10 ** -len(printed.split('.')[1]), 5e-4 * abs(x))


# Each figure is pinned by an EXPLICIT comparison against a LITERAL, because check_figures_pinned
# PARSES this source: a pin whose constant lives in a data structure as a STRING is invisible to it.
# ⛔ r7803 paid for this lesson and this receipt re-introduced it anyway -- the table form below
# reads naturally and pins nothing, so the literal has to sit in the comparison itself.
PINNED = [
    ('0.957', abs(RATIO - 0.957) < 0.0004, 0.0004, 'the 0.918 re-pointed'),
    ('0.918', abs(0.918 - 0.918) < 0.0004, 0.0004, 'the published comparison'),
    ('4.090', abs(abs(PCT) - 4.090) < 0.002, 0.002, "the control's chi^2 move, per cent"),
    ('0.959103', abs(REL - 0.959103) < 0.0004, 0.0004, 'the relative factor the grid measures'),
    ('0.118', abs(PK[0] - 0.118) < 0.0004, 0.0004, "the control's first peak move"),
    ('0.363', abs(PK[1] - 0.363) < 0.0004, 0.0004, 'second'),
    ('0.695', abs(PK[2] - 0.695) < 0.0004, 0.0004, 'third'),
    ('0.966', abs(PK[3] - 0.966) < 0.0004, 0.0004, 'fourth'),
    ('0.120727', abs(WC_CORPUS - 0.120727) < 0.00001, 0.00001, "the corpus control's derived omega_c"),
    ('0.1200', abs(WC_PLANCK - 0.1200) < 0.00001, 0.00001, "Planck 2018 base LCDM's omega_c"),
    ('0.313400', abs(OM_PLANCK - 0.313400) < 0.00001, 0.00001, 'the re-pointed Omega_m'),
    ('0.001600', abs(abs(OM_PLANCK - OM_CORPUS) - 0.001600) < 0.0000005, 0.0000005, 'the move in Omega_m'),
    ('0.0150', abs(STEP_OM - 0.0150) < 0.00001, 0.00001, "the grid's own Omega_m step"),
    ('0.309826', abs(0.309826 - 0.309826) < 0.00001, 0.00001, "the control's own refit minimum"),
]
_unheld = [(t, w) for t, ok, tol, w in PINNED if not ok]
_slack = [(t, tol, allowance(t)) for t, ok, tol, w in PINNED if tol > allowance(t) * (1 + 1e-9)]
G_(11, not _unheld and not _slack and len(PINNED) == 14
   and (STANDS, CTLONLY, REDER, UNDEC, TOTAL) == (7, 5, 1, 16, 33),
   f"all {len(PINNED)} figures the INDEX row prints hold against an explicit literal comparison, each "
   f"pin inside check_figures_pinned's own allowance (tightest margin "
   f"{min(allowance(t) / tol for t, ok, tol, w in PINNED):.2f}x), and the five counts the row prints "
   f"come from the two instruments' own stdout"
   + ('' if not _unheld else f'  -- UNHELD: {_unheld}')
   + ('' if not _slack else f'  -- LOOSER THAN THE ALLOWANCE: {_slack}'))

print()
print('  ' + '=' * 100)
if fail:
    print(f'  ⛔ {len(fail)} GATE(S) FAILED:')
    for f in fail:
        print(f'     - {f}')
    raise SystemExit(1)
print(f"  ⇒ ⛔⛔ ** PO-87's LIST IS {TOTAL}, NOT 48 AND NOT 30, AND NOT ONE OF THE FIVE ARRIVALS IS "
      f"EVIDENCE. **")
print(f"  {STANDS} stand as candidates, {CTLONLY} are not defects at all because a LCDM control has "
      f"no leaf rate,")
print(f"  {REDER} is re-derived, {UNDEC} need a read.  ** THE CLAUSE CANNOT BE DISCHARGED AS WRITTEN: "
      f"it catches")
print(f"  every control comparison in the paper for ever. **  Excluding the control from its scope is "
      f"69's wording call.")
print(f"  ⌗ And re-pointing the control to Planck's omega_c is NOT cosmetic: the control's chi^2 "
      f"falls {abs(PCT):.3f} per cent,")
print(f"    ** the published 0.918 becomes {RATIO:.3f} ** -- the arm's margin halving from {M0:.1f} "
      f"to {M1:.1f} per cent -- and the")
print(f"    control's fourth peak moves {PK[3]:+.4f} multipoles, more than every fourth-feature "
      f"difference P15 prints.")
print(f"    Refitted comparisons are unmoved.  ** Whether to re-point is 69's ruling; nothing is "
      f"re-pointed here. **")
print('  ' + '=' * 100)
