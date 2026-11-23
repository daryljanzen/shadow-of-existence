#!/usr/bin/env python3
r"""`r7783` ** THE ACOUSTIC SECTION'S OPENING FIGURES, READ OFF THE ONE-RATE ARM THROUGH THE PAPER'S
OWN SEVEN-WINDOW LOCATOR -- AND A CORRECTION TO A FIGURE THIS SEAT SUPPLIED AND THE PAPER NOW
CARRIES. **

⛔⛔ ** THE LANDED `298.94` IS WRONG.  THE FIGURE IS `298.5`. **  `P15`'s printed comb of `299.1` and
its phase intercept `-0.2488` are the ** FOUR-PEAK ** fit through the matched seven-window locator.
`r7779+cc66.3` measured a ** THREE-PEAK SUB-GRID ** comb on a different locator -- no lensing ratio,
no binning, no seven-window average -- got a move of `-0.0549 %`, and applied that move to the paper's
`299.1`.  That is one estimator's move applied to another estimator's number.  ** Read off the
one-rate arm directly, through the paper's own locator with the paper's own four-peak fit, the comb is
`298.527`, i.e. `298.5` at the paper's precision. **  *`(3)` carries the correction; the flawed step
was the operation and not the arithmetic -- scaling a printed figure by a move measured elsewhere.*

** AND TWO OF THE SECTION'S OTHER OPENING FIGURES MOVE TOWARDS THE SKY. **  The height ratios go
`2.291 / 2.349` to `2.207 / 2.249` against the sky's `2.221 / 2.262` -- from above the sky to just
below it -- and the phase intercept goes `-0.2488` to `-0.2454` against the sky's `-0.2448`.
** No significance is computed for either and none is implied. **

** AND THE FOURTH ACOUSTIC FEATURE IS THE CONTROL'S TO A FIFTH OF A MULTIPOLE IN ALL THREE SPECTRA **
-- `-0.000` (TT), `-0.183` (EE), `-0.206` (TE) -- where on the arm of record it is `+0.69 / +0.92 /
-0.21`, worst `0.92`.  That needed a polarisation run: ** no `LEAFGEOM=1` polarisation arm existed
anywhere in the tree, ** which `(1)` establishes by census over every `.npz` under `computations/`.

Built `r7783+cc66.9`, discharging order ③ of the chat seat's `r7783` (its `r7779` order ⑤).

===================================================================================================
** COMPUTES: ** the four acoustic peaks, the fitted comb, the phase intercept and the first-to-second
   and first-to-third height ratios of the crossing arm at the distances' point `(68.60, 0.2973)`,
   with `LEAFGEOM` the only difference between the two legs; and the fourth acoustic feature in TT, EE
   and TE on the refit arm against the control.  ** Neither locator is reimplemented. **  The peaks,
   comb, phase and heights go through the comb receipt's own `_matched` -- the seven windows
   `(40, 45, 50, 55, 60, 70, 80)`, the lensing ratio, the binning and the parabola's vertex value --
   executed from that receipt's source here, so the sky, the arm of record and the one-rate arm all go
   through ONE procedure.  The fourth feature goes through PO-47's `locate` and `Data`, taken verbatim
   from `r7631_70_PO87_polarisation/measure.py`.  Nothing is fitted beyond the comb's own least
   squares; no likelihood is formed and no significance is computed.
===================================================================================================

⛭ ** THE POLARISATION RUN, AND WHY IT WAS MINE TO LAUNCH. **  The fourth-feature comparison needs
`Dl_EE` and `Dl_TE`.  The order expected the banked refit arm to serve; that arm's `.npz` is TT-only,
and `(1)`'s census finds `LEAFGEOM=1` on NO polarisation bank in the tree -- the four that were
there when this ran, and every one banked since.  *`r7807+cc66` is why that row reads over the whole
population and not over a count of four: this seat's own control run banked a fifth polarisation
bank, which fired the census's tripwire without touching a thing this receipt measures.*  The run takes the banked refit arm's own `__SWITCHES__` line verbatim plus `POLSAVE`, and
`(2)` is the gate on its identity: ** its TT is BIT-IDENTICAL to the banked arm at every one of the
`238` shared multipoles. **  *The launcher is idempotent and checks for a running solver by reading
`/proc/*/environ`; `r7783+cc66.8` records why that check also needs to exclude its own ancestry.*

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM. **
 * ** Not that the one-rate arm fits the sky better. **  Three of its figures move towards the sky's
   and the fourth feature tightens, and no significance is computed for any of it.  The sky's own
   spreads at the fourth feature (`1.87` TT, `1.67` EE) are inherited, not re-measured here.
 * ** Not a mechanism for the TT fourth feature landing on the control's to `8e-5` of a multipole. **
   It is consistent with `r7749`'s own finding that the leaf-rate distance takes this arm onto the
   control, and consistency is not a derivation.
 * ** Not which configuration the section should open on. **  That is `69`'s call.
 * ** Not a re-measurement of the comb's own move. **  `r7779+cc66.3` measured that correctly for its
   own estimator; what was wrong was carrying it to the paper's figure.

⛭ ** FAILABILITY, MEASURED. **  Scaling the one-rate arm's `Dl` by `1 + 2e-3` reddens `(3)`, `(4)`
and `(7)` -- the comb and phase, the height ratios and the figure pins -- while `(1)`, `(2)`, `(5)`,
`(6)` and `(8)` hold, since they read the census, the polarisation run's TT, the polarisation spectra,
the locators' own source and this file's AST.
  ⛔ *That claim stood in this docstring for one commit BEFORE the probe existed, which is a false
  claim in a landed receipt however well it turned out: the measured result is the one above.*
Measured in
`computations/beyond_the_wall/r7783_cc66_the_sections_opening_figures_on_one_rate/failability.py`.

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy, scipy; about 30 s)
8 gates.  `(7)` pins every figure the INDEX row prints, each to half its last printed digit.
"""
import contextlib
import glob
import io
import json
import os
import sys
import types

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
SPEC = os.path.join(BW, 'spectra')
COMB = os.path.join(HERE, 'P15_at_its_own_preferred_H0_the_crossing_arm_predicts_the_acoustic_comb_'
                          'with_no_fitted_number.py')
MEAS = os.path.join(BW, 'r7631_70_PO87_polarisation', 'measure.py')
POL_NEW = os.path.join(BW, 'r7783_cc66_the_sections_opening_figures_on_one_rate',
                       'leafgeom_refit_pol_cr.npz')
POL_REC = os.path.join(BW, 'r7633_70_leafrec_refit', 'verify_cr_leafrec1_pol.npz')
POL_CTL = os.path.join(BW, 'r7631_70_PO87_polarisation', 'pol_lcdm.npz')
RECORD, ONE_RATE = 'cc66_cr_x_h686_L2000_leafrec1_distances.npz', 'r7749_leafgeom_nofit_L2000_cr.npz'
FAILS = []


def check(label, ok, witness=''):
    if not ok:
        FAILS.append(label.split('**')[0].strip()[:60])
    print(f"    [{'PASS' if ok else 'FAIL'}] {label}")
    if witness:
        print(f'             {witness}')


TEX = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
tex_src = open(TEX, encoding='utf-8').read()
for p in (COMB, MEAS, POL_NEW, POL_REC, POL_CTL, TEX):
    if not os.path.exists(p):
        sys.exit(f'FATAL: {p} is not where this reads it from; the instrument has moved.')

print('=' * 100)
print(__doc__)
print('=' * 100)

# ---------------------------------------------------------------- (1) the census
pol, lg = [], []
for f in sorted(glob.glob(os.path.join(ROOT, 'computations', '**', '*.npz'), recursive=True)):
    try:
        z = np.load(f, allow_pickle=True)
    except Exception:
        continue
    if not ('Dl_EE' in z.files or 'Dl_TE' in z.files):
        continue
    rel = os.path.relpath(f, ROOT)
    v = None
    if 'config' in z.files:
        c = z['config']
        try:
            c = c.item()
        except Exception:
            pass
        try:
            v = json.loads(str(c)).get('LEAFGEOM')
        except Exception:
            v = 'unparsed'
    pol.append(rel)
    if v is True or 'LEAFGEOM=1' in (str(z['switches']) if 'switches' in z.files else ''):
        lg.append(rel)
mine = os.path.relpath(POL_NEW, ROOT)
pre = [p for p in pol if p != mine]
pre_lg = [p for p in lg if p != mine]
# ⛔ r7807+cc66: THE CENSUS WAS PINNED AT FOUR AND THIS SEAT ITSELF ADDED THE FIFTH.  r7807's
#   control run banks a POLSAVE spectrum (`r7807_control_planck2018_L2000_pol.npz`), so the old
#   `len(pre) == 4` reddened this gate on a push that changed NOTHING this receipt measures.  The
#   tripwire fired correctly and has now been READ, which is the whole point of a tripwire: that bank
#   is `ARM=lcdm` at Planck's published point, its `config` records `LEAFGEOM` false, and it was
#   banked AFTER this receipt's run -- so it is not a one-rate arm and could not have served the
#   fourth feature.
#   What ESTABLISHES the claim was never the count.  It is that NO polarisation bank anywhere under
#   `computations/` is a `LEAFGEOM=1` arm, so the row asserts THAT, over the whole population, and
#   pins r7783's own four BY NAME so one of them going missing or being renamed still reddens.  A
#   bank banked later reddens only when it IS a `LEAFGEOM=1` arm -- the condition that would really
#   mean no run was needed -- and is named in the row either way, so an arrival is read and never
#   absorbed.
#   ⛔ Pinned as a SET and not as a count, because a second copy of one of the four in another
#   seat's `rebuilt/` directory would otherwise read as a fifth arrival: the basename trap this seat
#   walked into at `r7805` and had to correct at `r7807`.
R7783_FOUR = frozenset(('pol_cr_leafrec0.npz', 'pol_cr_leafrec1.npz', 'pol_lcdm.npz',
                        'verify_cr_leafrec1_pol.npz'))
_four = frozenset(os.path.basename(p) for p in pre) & R7783_FOUR
# ⛭ r7861 (69): THE SECOND NAMED ARRIVAL, in the form the row's own clause prescribes.  At 69's r7857 ruling the
#   bank model3 reads left `/tmp` and was committed (60, r7860): 32 polarisation points under
#   `computations/beyond_the_wall/bank/pol_grid/` (and its BVEL=1 re-solve in `pol_grid_bvel1/`), in each of which the 16 `cr_*` points are the `cr` arm at
#   LEAFGEOM=1, LEAFREC=1, LEAFSCALES=1, LMAXL=2000, LSTEP=8, carrying Dl, Dl_EE and Dl_TE.  They are the
#   product of 60's r7842 run, made AFTER r7783, so they do not show the fourth feature needed no run; they
#   are named here by directory AND by their sixteen basenames, so a seventeenth one-rate bank there, or one
#   anywhere else, still reddens this row.
R7860_DIRS = (os.path.join('computations', 'beyond_the_wall', 'bank', 'pol_grid'),
              os.path.join('computations', 'beyond_the_wall', 'bank', 'pol_grid_bvel1'))   # the landed grid, and its BVEL=1 re-solve (r7860 ④)
R7860_CR = frozenset('cr_%s.npz' % s for s in ('H0m', 'H0p', 'NSm', 'NSp', 'OMm', 'OMp', 'S000', 'S006',
                                              'S015', 'S030', 'S045', 'S060', 'Sm06', 'Sm12', 'WBm', 'WBp'))
_named_lg = [p for p in pre_lg if os.path.dirname(p) in R7860_DIRS and os.path.basename(p) in R7860_CR]
pre_lg = [p for p in pre_lg if p not in _named_lg]
_later = sorted(p for p in pre if os.path.basename(p) not in R7783_FOUR)
check("⛭⛔⛭ `r7783` ** ① THE FOURTH FEATURE NEEDED A RUN, AND THAT IS ESTABLISHED BY **CENSUS** OVER "
      "EVERY `.npz` UNDER `computations/`: THIS RECEIPT'S OWN FOUR POLARISATION BANKS ARE ALL STILL "
      "THERE, AND **NO** POLARISATION BANK IN THE TREE IS A `LEAFGEOM=1` ARM ** ⇒ *** the order "
      "expected the banked refit arm to serve, and that arm's `.npz` carries TT only -- `Dl_EE` and "
      "`Dl_TE` are nowhere on the one rate. ** The census is the row rather than a look at the obvious "
      "place, because a claim of this shape from this seat at `r7767` was too strong and had to be "
      "withdrawn. ** *** ⌗ *A `LEAFGEOM=1` polarisation bank ANYWHERE, or one of the four gone or "
      "renamed, reddens this and means no run was needed. A bank banked LATER that is not on the one "
      "rate does not -- it is named in the row instead, so an arrival is read and not absorbed. "
      "`r7807+cc66`'s re-pointed control is the first such bank, and it is this seat's own; the second is "
      "60's r7842 polarisation grid, committed out of `/tmp` at r7860, and its BVEL=1 re-solve, whose "
      "sixteen `cr` points each are LEAFGEOM=1 and are named by directory and basename*",
      _four == R7783_FOUR and not pre_lg and len(_named_lg) == 32,
      f"{len(_four)} of r7783's own four polarisation bank(s) still present: "
      + ', '.join(sorted(_four))
      + f'; banked since: '
      + (', '.join(os.path.basename(p) for p in _later) if _later else 'NONE')
      + f'; of all {len(pre)}, those with LEAFGEOM=1 outside the named r7860 grid: {pre_lg if pre_lg else "NONE"}'
      + f'; named r7860 one-rate points: {len(_named_lg)} of 32 (16 in each grid)')

# ---------------------------------------------------------------- (2) the run IS the same arm
with np.load(POL_NEW, allow_pickle=True) as z:
    keys, ls_n, Dl_n = list(z.files), np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
with np.load(os.path.join(SPEC, 'r7749_leafgeom_refit_verify_cr.npz'), allow_pickle=True) as z:
    ls_b, Dl_b = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
sh = np.intersect1d(ls_n, ls_b)
worst_tt = float(np.max(np.abs(np.interp(sh, ls_n, Dl_n) / np.interp(sh, ls_b, Dl_b) - 1.0)))
check("⛭ `r7783` ** ② AND THE RUN **IS** THE BANKED ARM, NOT A LOOK-ALIKE: ITS TT IS **BIT-IDENTICAL** "
      "TO `r7749_leafgeom_refit_verify_cr` AT EVERY ONE OF THE `238` SHARED MULTIPOLES ** ⇒ *** the "
      "switches are that bank's own `__SWITCHES__` line verbatim plus `POLSAVE`, and this row is why "
      "any EE or TE number below may be read as the same arm's. ** *** ⌗ *`max |new/banked - 1| = 0`, "
      "exactly -- not `within tolerance`*",
      {'Dl_EE', 'Dl_TE'}.issubset(keys) and sh.size == 238 and worst_tt == 0.0,
      f'EE and TE present: {{"Dl_EE","Dl_TE"}}.issubset -> True; {sh.size} shared multipoles; '
      f'max |new/banked - 1| = {worst_tt:.1e}')

# ------------------------------------------------- the paper's own locator, from the comb receipt
_src = open(COMB, encoding='utf-8').read()
_ns = {'__name__': '__r7783_comb__', '__file__': COMB}
try:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(_src, COMB, 'exec'), _ns)
except SystemExit:
    pass
for n in ('_matched', '_sweep', '_locate', '_WS', '_MSKY'):
    if n not in _ns:
        sys.exit(f'FATAL: the comb receipt no longer defines `{n}`; the locator has moved.')
with contextlib.redirect_stdout(io.StringIO()):
    rec, one = _ns['_matched'](RECORD), _ns['_matched'](ONE_RATE)
# ⛭ THE PAPER IS READ, NOT ATTRIBUTED.  `check_unread_figure`'s rule, learnt at `r7783+cc66.4`: a
#   label that calls a figure THE PAPER's must open the paper, or the row stays green when the paper
#   moves.  And each parse is a DISJUNCTION wherever 69's rewrite will change the figure, so the row
#   does not fail on the success it is for -- `check_quote_pins`'s own named hazard.
import re as _re
PK_PAPER = (220.0, 536.3, 811.6, 1125.1)
_sent = _re.search(r"it returns a comb of \$(\d+\.\d)\$ against the sky's \$(\d+\.\d)\$ and "
                   r"height ratios \$(\d\.\d{3})\$ and \$(\d\.\d{3})\$", tex_src)
_phi = _re.search(r'\\varphi/\\pi=(-\d\.\d{4})\$ against \$(-\d\.\d{4})\$', tex_src)
_skyh = _re.search(r'height ratios are \\$P_\\{1\\}/P_\\{2\\}=(\\d\\.\\d{3})\\$ and \\$P_\\{1\\}/P_\\{3\\}=(\\d\\.\\d{3})\\$', tex_src)

d_pk = [float(one['pk'][i]) - float(rec['pk'][i]) for i in range(4)]
print(f"\n      {'quantity':>24} {'arm of record':>15} {'one rate':>12} {'move':>12}   the sky")
for i in range(4):
    print(f"      {'peak ' + str(i + 1):>24} {rec['pk'][i]:>15.3f} {one['pk'][i]:>12.3f} "
          f"{d_pk[i]:>+12.3f}")
for lab, k, sky in (('comb, four peaks', 'a4', '298.4'), ('phi/pi, four peaks', 'f4', '-0.2448'),
                    ('P1/P2', 'p12', '2.221'), ('P1/P3', 'p13', '2.262')):
    r, o = float(rec[k]), float(one[k])
    if k.startswith('f'):
        r, o = r / np.pi, o / np.pi
    print(f'      {lab:>24} {r:>15.4f} {o:>12.4f} {o - r:>+12.4f}   {sky:>8}')

# ---------------------------------------------------------------- (3) the comb, CORRECTED
a4r, a4o = float(rec['a4']), float(one['a4'])
f4r, f4o = float(rec['f4']) / np.pi, float(one['f4']) / np.pi
check("⛭⛭⛭⛔ `r7783` ** ③ THE PAPER'S `299.1` AND `-0.2488` ARE THE **FOUR-PEAK** FIT, AND ON THE ONE "
      "RATE THEY ARE `298.527` AND `-0.2454` -- SO THE FIGURE IS `298.5`, **NOT THE `298.94` THIS SEAT "
      "SUPPLIED AT `r7779` AND THE PAPER NOW CARRIES** ** ⇒ *** the arm of record returns `299.057` and "
      "`-0.2488` through this locator, matching the paper to the digit, while its THREE-peak fit "
      "returns `295.782` and `-0.2331`. ** `r7779+cc66.3` measured a three-peak sub-grid comb on a "
      "different locator and applied ITS move to the paper's four-peak number: one estimator's move on "
      "another estimator's figure. ** *** ⌗ *`298.57` is what scaling by the RIGHT move would give, and "
      "is also wrong: reading the arm's own figure is the correct operation*",
      _sent is not None and _phi is not None
      and min(abs(float(_sent.group(1)) - v) for v in (round(a4r, 1), round(a4o, 1))) < 0.05
      and min(abs(float(_phi.group(1)) - v) for v in (round(f4r, 4), round(f4o, 4))) < 0.00005
      and abs(a4r - 299.057) < 0.0005 and abs(a4o - 298.527) < 0.0005
      and abs(f4r - (-0.2488)) < 0.00005 and abs(f4o - (-0.2454)) < 0.00005
      and round(a4o, 1) == 298.5,
      f'the paper prints comb {_sent.group(1) if _sent else None} and phi/pi '
      f'{_phi.group(1) if _phi else None}; four-peak comb {a4r:.4f} -> {a4o:.4f} ({100*(a4o/a4r-1):+.4f}%), which is {round(a4o,1)} at the '
      f"paper's precision; phi/pi {f4r:+.4f} -> {f4o:+.4f} against the sky's -0.2448; the three-peak "
      f"fit is {float(rec['a3']):.4f} -> {float(one['a3']):.4f}")

# ---------------------------------------------------------------- (4) the height ratios
p12r, p12o = float(rec['p12']), float(one['p12'])
p13r, p13o = float(rec['p13']), float(one['p13'])
check("⛭⛭⛭ `r7783` ** ④ AND THE HEIGHT RATIOS MOVE FROM **ABOVE** THE SKY'S TO JUST **BELOW** THEM: "
      "`2.2909 / 2.3488` BECOMES `2.2073 / 2.2491`, AGAINST THE SKY'S `2.221 / 2.262` ** ⇒ *** moves of "
      "`-3.65 %` and `-4.25 %`, far larger than the comb's `-0.18 %`, so the heights are the opening "
      "figures the rate actually moves. ** The arm of record's values reproduce the paper's `2.291` and "
      "`2.349` to the digit, which is what makes the comparison like-for-like. ** *** ⌗ ⛔ **No "
      "significance is computed and none is implied**: the sky's own spreads are not carried here*",
      _sent is not None
      and min(abs(float(_sent.group(3)) - v) for v in (round(p12r, 3), round(p12o, 3))) < 0.0005
      and min(abs(float(_sent.group(4)) - v) for v in (round(p13r, 3), round(p13o, 3))) < 0.0005
      and abs(p12r - 2.2909) < 0.00005 and abs(p13r - 2.3488) < 0.00005
      and abs(p12o - 2.2073) < 0.00005 and abs(p13o - 2.2491) < 0.00005
      and p12r > float(_ns['_MSKY']['p12']) > p12o
      and p13r > float(_ns['_MSKY']['p13']) > p13o,
      f"the paper prints height ratios {_sent.group(3) if _sent else None} and "
      f"{_sent.group(4) if _sent else None} against the sky's {_sent.group(2) if _sent else None} comb; "
      f'P1/P2 {p12r:.4f} -> {p12o:.4f} ({100*(p12o/p12r-1):+.2f}%); P1/P3 {p13r:.4f} -> {p13o:.4f} '
      f"({100*(p13o/p13r-1):+.2f}%); the sky's {float(_ns['_MSKY']['p12']):.3f} and "
      f"{float(_ns['_MSKY']['p13']):.3f}, measured through the SAME locator rather than quoted")

# ---------------------------------------------------------------- (5) the fourth feature
_ms = open(MEAS, encoding='utf-8').read()
_mhead = _ms[:_ms.index('# ---- the two arms')]
sys.modules.setdefault('sacc', types.ModuleType('sacc'))      # PART 1 never touches it; see below
_mns = {'__name__': '__r7783_po47__', '__file__': MEAS}
exec(compile(_mhead, MEAS, 'exec'), _mns)
for n in ('Data', 'locate', 'FEAT', 'WS'):
    if n not in _mns:
        sys.exit(f'FATAL: measure.py no longer defines `{n}`; PO-47 locator has moved.')
feat = {}
for tag, path in (('one', POL_NEW), ('rec', POL_REC), ('ctl', POL_CTL)):
    z = np.load(path)
    for spec, key in (('TT', 'Dl'), ('EE', 'Dl_EE'), ('TE', 'Dl_TE')):
        feat[(spec, tag)] = float(_mns['locate'](
            _mns['Data'](tag, z['ls'].astype(float), z[key], None), spec, mc=False)['c'])
print(f"\n      {'spectrum':>10} {'arm of record':>15} {'one rate':>12} {'control':>12} "
      f"{'rec - ctl':>11} {'one - ctl':>11}")
for spec in ('TT', 'EE', 'TE'):
    print(f"      {spec:>10} {feat[(spec,'rec')]:>15.3f} {feat[(spec,'one')]:>12.3f} "
          f"{feat[(spec,'ctl')]:>12.3f} {feat[(spec,'rec')] - feat[(spec,'ctl')]:>+11.3f} "
          f"{feat[(spec,'one')] - feat[(spec,'ctl')]:>+11.3f}")
d_rec = {s: feat[(s, 'rec')] - feat[(s, 'ctl')] for s in ('TT', 'EE', 'TE')}
d_one = {s: feat[(s, 'one')] - feat[(s, 'ctl')] for s in ('TT', 'EE', 'TE')}
w_rec, w_one = max(abs(v) for v in d_rec.values()), max(abs(v) for v in d_one.values())
# ⛔ `check_unread_figure` again: the label calls this the PAPER's claim, so the paper is read.
# r7797 (69): whitespace-tolerant, because the landed sentence breaks its line inside this clause.
_ff_claim = _re.search(r'differ\s+at\s+the\s+fourth\s+feature\s+by\s+\$(\d\.\d{2})\$\s+multipoles\s+in\s+\$TT\$',
                       tex_src)
check("⛭⛭⛭ `r7783` ** ⑤ AND THE FOURTH ACOUSTIC FEATURE IS THE CONTROL'S TO A **FIFTH OF A "
      "MULTIPOLE** IN ALL THREE SPECTRA ON THE ONE RATE -- `-0.000` TT, `-0.183` EE, `-0.206` TE -- "
      "WHERE ON THE ARM OF RECORD IT IS `+0.69 / +0.92 / -0.21` ** ⇒ *** so the paper's *\"the "
      "control's to under a multipole in all three spectra\"* does not merely survive the rate, it "
      "tightens by a factor `4.5`, from `0.92` to `0.21`. ** The arm of record's three differences "
      "reproduce the landed `+0.69 / +0.92 / -0.21` to the digit through PO-47's locator taken "
      "verbatim, which is what makes the one-rate reading the same measurement. ** *** ⌗ ⛔ *The TT "
      "difference is `-7.7e-05` of a multipole. That is consistent with `r7749`'s own finding that the "
      "leaf-rate distance takes this arm onto the control, and consistency is NOT a derivation: no "
      "mechanism is claimed*",
      abs(d_rec['TT'] - 0.69) < 0.005 and abs(d_rec['EE'] - 0.92) < 0.005
      and abs(d_rec['TE'] + 0.21) < 0.005 and w_one < 0.25 and w_one < w_rec / 3.0
      # the paper prints the TT difference itself; matched against EITHER arm's, since
      # the rewrite may take it to the one-rate value -- the same disjunction as (3).
      and _ff_claim is not None and w_rec < 1.0 and w_one < 1.0
      and min(abs(float(_ff_claim.group(1)) - abs(v)) for v in (d_rec['TT'], d_one['TT'])) < 0.005,
      f"the paper prints a TT difference of {_ff_claim.group(1) if _ff_claim else None} multipoles, "
      f"which matches one of the two measured here; both arms are under a multipole in all three "
      f"({w_rec:.3f} and {w_one:.3f}); "
      f"arm of record {d_rec['TT']:+.3f} / {d_rec['EE']:+.3f} / {d_rec['TE']:+.3f} (worst {w_rec:.3f}); "
      f"one rate {d_one['TT']:+.6f} / {d_one['EE']:+.3f} / {d_one['TE']:+.3f} (worst {w_one:.3f})")

# ---------------------------------------------------------------- (6) neither locator reimplemented
check("⛭ `r7783` ** ⑥ AND **NEITHER LOCATOR IS REIMPLEMENTED**: BOTH ARE EXECUTED FROM THEIR OWN "
      "RECEIPTS' SOURCE, SO EVERY ARM AND THE SKY GO THROUGH ONE PROCEDURE ** ⇒ *** the comb receipt's "
      "`_matched` supplies the seven windows `(40, 45, 50, 55, 60, 70, 80)`, the lensing ratio, the "
      "binning and the parabola's vertex value; PO-47's `Data` and `locate` supply the fourth "
      "feature's anchor and its six-window procedure spread. ** *** ⌗ *`measure.py` imports `sacc` at "
      "module level and its PART 1 never touches it, so only its DEFINITIONS are executed here, with "
      "`sacc` stubbed -- stated rather than hidden, and the sky parts that do need it are not run*",
      _ns['_WS'] == (40., 45., 50., 55., 60., 70., 80.) and _mns['WS'] == (45., 50., 55., 60., 70., 80.)
      and set(_mns['FEAT']) == {'TT', 'EE', 'TE'},
      f"the comb receipt's windows {_ns['_WS']}; PO-47's windows {_mns['WS']}; its features "
      f"{sorted(_mns['FEAT'])}")

# ---------------------------------------------------------------- (7) every printed figure, pinned
_ps = [
    ('peak 1, record', abs(float(rec['pk'][0]) - 220.031) < 0.0005),
    ('peak 2, record', abs(float(rec['pk'][1]) - 536.255) < 0.0005),
    ('peak 3, record', abs(float(rec['pk'][2]) - 811.594) < 0.0005),
    ('peak 4, record', abs(float(rec['pk'][3]) - 1125.108) < 0.0005),
    ('peak 4, one rate', abs(float(one['pk'][3]) - 1123.882) < 0.0005),
    ('peak 4 move', abs(d_pk[3] - (-1.226)) < 0.0005),
    ('comb, record', abs(a4r - 299.057) < 0.0005),
    ('comb, one rate', abs(a4o - 298.527) < 0.0005),
    ('the corrected figure', round(a4o, 1) == 298.5),
    ('phi/pi, record', abs(f4r - (-0.2488)) < 0.00005),
    ('phi/pi, one rate', abs(f4o - (-0.2454)) < 0.00005),
    ('P1/P2, record', abs(p12r - 2.2909) < 0.00005),
    ('P1/P2, one rate', abs(p12o - 2.2073) < 0.00005),
    ('P1/P3, record', abs(p13r - 2.3488) < 0.00005),
    ('P1/P3, one rate', abs(p13o - 2.2491) < 0.00005),
    ('fourth feature TT, record', abs(d_rec['TT'] - 0.691) < 0.0005),
    ('fourth feature EE, record', abs(d_rec['EE'] - 0.918) < 0.0005),
    ('fourth feature TE, record', abs(d_rec['TE'] - (-0.208)) < 0.0005),
    ('fourth feature EE, one rate', abs(d_one['EE'] - (-0.183)) < 0.0005),
    ('fourth feature TE, one rate', abs(d_one['TE'] - (-0.206)) < 0.0005),
    ('the worst one-rate difference', abs(w_one - 0.206) < 0.0005),
    ('the worst record difference', abs(w_rec - 0.918) < 0.0005),
    ('the three-peak comb, record', abs(float(rec['a3']) - 295.782) < 0.0005),
    ('the three-peak phi/pi, record', abs(float(rec['f3']) / np.pi - (-0.2331)) < 0.00005),
    ("the sky's phase intercept, parsed",
     _phi is not None and abs(float(_phi.group(2)) - (-0.2448)) < 0.00005),
    ("the sky's comb, parsed",
     _sent is not None and abs(float(_sent.group(2)) - 298.4) < 0.05),
    ("the sky's P1/P2, measured through the same locator",
     abs(float(_ns['_MSKY']['p12']) - 2.221) < 0.0005),
    ("the sky's P1/P3, measured through the same locator",
     abs(float(_ns['_MSKY']['p13']) - 2.262) < 0.0005),
]
off = [n for n, g in _ps if not g]
check("⛭ `r7783` ** ⑦ AND EVERY FIGURE THE `INDEX` ROW PRINTS IS PINNED **HERE**, EACH TO HALF ITS LAST "
      "PRINTED DIGIT ** ⇒ *** twenty-eight of them: four peaks and the fourth's move, both combs and the "
      "corrected `298.5`, both phase intercepts, all four height ratios, and six fourth-feature "
      "differences with both worst cases. *** ⌗ *Written as explicit comparisons, because "
      "`check_figures_pinned` parses this file rather than running it*",
      not off, f'{len(_ps)} printed figures, {len(off)} off their pin'
               + ('' if not off else ': ' + '; '.join(off[:4])))

# ---------------------------------------------------------------- (8) scope
import ast as _ast2
_FORBIDDEN = {'chi2', 'chisq', 'sigma', 'p_value', 'pvalue', 'likelihood', 'curve_fit',
              'minimize', 'minimize_scalar', 'lstsq', 'polyfit', 'cho_solve'}
_names = set()
for _n in _ast2.walk(_ast2.parse(open(__file__, encoding='utf-8').read())):
    if isinstance(_n, _ast2.Name):
        _names.add(_n.id)
    elif isinstance(_n, _ast2.Attribute):
        _names.add(_n.attr)
_scope_hits = sorted(_names & _FORBIDDEN)
check("⛭ `r7783` ** ⑧ AND THE SCOPE IS DECLARED: NO LIKELIHOOD, NO SIGNIFICANCE, NO MECHANISM, AND NO "
      "RULING ON WHICH CONFIGURATION THE SECTION SHOULD OPEN ON ** ⇒ *three of this arm's figures move "
      "towards the sky's and the fourth feature tightens; the sky's own spreads are inherited and not "
      "re-measured, nothing is fitted beyond the comb's least squares, and what the paper should print "
      "is `69`'s call*",
      # ⛔ `check_cannot_fail` was right: this row's condition was the literal `True`.  A scope
      #   declaration can be ASSERTED -- that this file calls no likelihood, significance or fitting
      #   machinery -- and then it is failable by the one thing that should fail it.
      #   ⛔⛔ AND IT MUST BE ASKED OF THE **AST**, NOT OF THE TEXT.  A substring form finds its own
      #   forbidden-token list and fails on a clean file -- which is exactly what it did here, the
      #   THIRD self-match of this revision after `'fit_comb(P, 4)' in <this file>` and
      #   `'$299.1$' in tex`.  ** The rule: a test that searches the file it lives in must not
      #   search for its own literals. **  Names and attributes cannot self-match; string constants
      #   can.
      not _scope_hits,
      f'asserted, not declared, and asked of the AST so it cannot find its own token list: '
      f'{len(_scope_hits)} likelihood/significance/fitting name(s) called in this file')

print('\n' + '=' * 100)
print(f"  {'OK  ' if not FAILS else 'FAIL'}  {8 - len(FAILS)} of 8 gates;  "
      f"{len(FAILS)} failure(s)" + ('' if not FAILS else ': ' + '; '.join(FAILS[:2])))
print('=' * 100)
sys.exit(1 if FAILS else 0)
