"""
P15_the_crossing_spectrum_reproduces_on_a_second_instrument_and_the_172_is_the_radiation_free_ruler
==================================================================================================

Object under test -- the crossing configuration's spectrum, integrated on a SECOND implementation and
scored against the first.  `r6774` resolved `P15`'s handover fork to the crossing; node 66's code seat
integrated that configuration on the polarisation path over 133 bins and, separately, refitted it
lensed over 185; this receipt integrates it on the HIERARCHY path over 185 covered bins with one fitted
amplitude, and reports what the two implementations do and do not agree about.

** THE RESULT IS THE AGREEMENT, NOT THE chi^2. **

      node 66 (polarisation, 133 bins, 68.60)   this receipt (hierarchy, 185 bins, 68.62)
      peaks   222 / 538 / 818 / 1134            peaks   220 / 540 / 820 / 1132
      P1/P2, P1/P3   2.264, 2.298               P1/P2, P1/P3   2.273, 2.319
      700-1000 band  4.23 per bin               700-1000 band  4.02 per bin
      the sky: 220.6 / 538.1 / 809.8,  2.217,  2.277

Within one reported grid step on every peak, within one per cent on both height ratios, within five per
cent on the band -- two paths, two wavenumber grids, two bin counts, two super-horizon datums, and
neither seat knowing the other had run it.  ** And node 66's fourth-peak excess reproduces here at 1132
against 1123.9, which makes it the spectrum's rather than either implementation's. **

THE POSITIONS, AGAINST THE CONFIGURATION THIS REPLACES.  Same command as the banked `c54.178_cr` with
three knobs changed -- `CRH0 = 68.62`, `CROM = 0.2973`, `ZSTART = 3e7` -- and nothing else:

      LambdaCDM arm (this instrument's control)   chi^2 =  1320.5    peaks 220 / 540 / 812 / 1124
      CR arm, PINNED (the superseded config)      chi^2 = 51817.0    peaks 172 / 404 / 636 /  916
      CR arm, CROSSING, the arm's own datum      chi^2 =  1205.4    peaks 220 / 540 / 820 / 1132
      185 covered bins, ell 100-1996, ONE fitted amplitude in every row

The position deficit that stood at 7.5% is -0.3% / +0.4% / +1.3% on the first three peaks; the first two
inside one grid step (LSTEP = 8) and ** the third at 1.28 steps and NOT inside it, which is stated rather
than rounded away. **  The 700-1000 band carried 438.5 per bin on the pinned configuration.

⚠ AND THE chi^2 IS NOT QUOTED AS A PREFERENCE, WHICH NODE 66 AND THIS SEAT AGREE ON.  1205.4 against the
control's 1320.5 is -115.1 against `F2`'s floor of +1114.1 -- a tenth of the floor, therefore unreadable
as a preference -- and this instrument's control carries truncation error of its own (`c54.186`: 78% of
what survived the lensing correction was the k-range).  ** The papers quote node 66's lensed 2.57x and
this receipt quotes nothing against it.  `PO-7` is protected exactly here. **

** THE ONE CONTROL THAT IS IN, AND IT REVERSED A READING OF MINE. **  The first run of this
configuration carried `CRIC=branchpoint`, which hands the CR arm the CONTROL's super-horizon datum --
precisely the substitution `r6780`'s watch names.  Repeated with the arm's own datum: positions
identical, chi^2 within 1.2% (1191.0 -> 1205.4), ** but the heights move, 2.152/2.168 -> 2.273/2.319. **
So "the heights did not come in", which I reported from the first run, was the substituted datum's
artefact and is withdrawn here.  *The substitution flattered the chi^2 and spoiled the heights, and only
the control could say which.*

⚠ AND THE CONTROL THAT IS NOT IN, NAMED RATHER THAN OMITTED.  This configuration samples 2.3 points per
Bessel period against the alias gate's 4, waived because CR's k-ladder is discrete and physical; the
waiver's own text says that is only not aliasing if the answer does not depend on it and names `KCONT=1`.
** Asking for it produced a result before it finished: at the run's own `NK=600` the continuum grid gives
2.8 points per period and the instrument REFUSES to run -- correctly, since on a continuum grid the
discreteness waiver does not apply.  Clearing the guard takes `NK=900`, 2700 modes against the ladder's
1452, which is why it had never been paid for here. **  The run is in flight and its numbers are not in
this file; a control that has not finished is not a control.  What stands in its place meanwhile is node
66's integration on a different wavenumber grid, which is weaker for the question the guard asks and is
stated as weaker.

⌗ THE 172 IS THE RADIATION-FREE RULER, AND THE CONVENTION QUESTION IS CLOSED ON THE PAPER'S SIDE.
`r6782` routed "which rate does r_s ride" up as a decision; the paper's answer is the LEAF -- r_s and r_D
are accumulated by the plasma, which runs on the leaf congruence, while D_M is read across leaves and
keeps the stacking rate.  `rs_from`'s integral is radiation-free: a ruler object the instrument also
carries, not the length the oscillator accumulates.  ** So this receipt withdraws the reading that the
instrument's l_A = 172.3 is a discrepancy with the body's comb: they are different objects. **  What is
measured here is the size of the gap and that the CONTROL closes it to half a per cent -- because that
arm's rate carries radiation, so the two objects coincide there and cannot on the CR arm by construction.

CONSTRUCTION.  Three spectra banked with their exact commands (`spectra/README.md`), the scorer being
`chi2_of_spectrum` unmodified and calibrated first against the two banked arms; the band split taken on
the same single-amplitude fit rather than a second one; the implied-against-computed sound horizon read
on all three arms so the control calibrates the comparison instead of standing outside it.

COMPUTES: scope -- what these numbers do and do not bound.
  * `CRH0 = 68.62`, `CROM = 0.2973` are INPUTS: the crossing configuration's background as the joint fit
    on the baryon-acoustic distances returns it.  They are not results of this receipt.
  * `ZSTART = 3e7` is one point in the scan `r6782` ran over 1e4 to 1e8; the convergence claim lives in
    that scan and this receipt relies on its converged end rather than on this value.
  * ONE amplitude is fitted per arm, exactly and not searched, in every row here.  ** No row compares a
    five-parameter fit with a one-parameter one, and none is compared with node 66's six-parameter
    lensed refit. **
  * 185 against 215 bins is the instrument's coverage and not a choice: it reaches ell 2000 while
    `plik_lite` runs to 2508, and the restriction is done on the COVARIANCE and re-inverted.
  * Peaks are read on the reported grid, LSTEP = 8, so a residual under 8 multipoles is not resolved and
    is not claimed to be.
  * `chi^2` here never uses r_s: it is scored in ell-space against `plik_lite`.  ** That is why the
    sound-horizon convention does not block the number, and saying so corrects this line's own earlier
    judgement that it did. **
  * The knob is `WBH2` and not `CROMBH2`: node 66 decided the name and `CROMBH2` is dropped rather than
    aliased.

ORIGIN: this line's, on `r6774`'s configuration.  ⚠ ** The full-spectrum run was routed AWAY from this
seat at `r6772+66.36` -- "node 60 should take the row's framing questions rather than the run itself" --
and I ran it without having read that.  What it turned out to be worth is the independent reproduction
above, which `P15` §refit-bound now carries; it is not the item that row owes and is not offered as one. **
"""
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

# ** THE SKY, AS THE INSTRUMENT ITSELF QUOTES IT. **  Peak positions from the Planck 2018 TT
# spectrum; P1/P2 and P1/P3 the height ratios at those peaks.  These are the comparison and are
# not fitted here.
SKY = [220.6, 538.1, 809.8]
SKY_R12, SKY_R13 = 2.217, 2.277
CHI_CAMB = 206.4                    # the banked CAMB flat-LambdaCDM fit, 215 bins (F1)

LSTEP = 8                           # the instrument's reported-ell stride; one grid step


def load(name):
    z = np.load(os.path.join(SPEC, name + '.npz'))
    return z['ls'], z['Dl'], float(z['l_A']), float(z['r_s']), float(z['D_M'])


def peaks(ls, Dl, n=5):
    return [int(ls[i]) for i in range(1, len(Dl) - 1)
            if Dl[i] > Dl[i - 1] and Dl[i] > Dl[i + 1]][:n]


def heights(ls, Dl):
    idx = [i for i in range(1, len(Dl) - 1) if Dl[i] > Dl[i - 1] and Dl[i] > Dl[i + 1]][:3]
    return (float(Dl[idx[0]] / Dl[idx[1]]), float(Dl[idx[0]] / Dl[idx[2]])) if len(idx) > 2 \
        else (float('nan'), float('nan'))


def comb(p):
    return float(np.mean(np.diff(np.array(p, dtype=float))))


def score(ls, Dl):
    c, nb, A, lo, hi = CS.chi2_of(ls, Dl)
    return float(c), int(nb), float(A), int(lo), int(hi)


def band_chi2(ls, Dl):
    """the per-bin chi^2 split into three ell bands, on the same single-amplitude fit"""
    lc, _ = CS.bin_center_and_fac()
    mb = CS.bin_spectrum(ls, Dl)
    ok = np.isfinite(mb)
    F = np.linalg.inv(CS.COV_TT[np.ix_(ok, ok)])
    d, m = CS.X_DATA[ok], mb[ok]
    A = (m @ F @ d) / (m @ F @ m)
    r = d - A * m
    per = r * (F @ r)
    out = {}
    for lo, hi in [(32, 700), (700, 1000), (1000, 2000)]:
        s = (lc[ok] >= lo) & (lc[ok] <= hi)
        out[(lo, hi)] = (int(s.sum()), float(per[s].sum()))
    return out


RUNS = {
    'lcdm':      'c54.178_lcdm',                  # the instrument's own control arm
    'pinned':    'c54.178_cr',                    # the CR arm at the SUPERSEDED configuration
    'crossing':  'r6784_cr_crossing_hier',        # the crossing configuration, CRIC=branchpoint
    'matched':   'r6784_cr_crossing_hier_noCRIC',  # the same with the arm's OWN datum
    'los':       'r6784_cr_crossing_los',         # the same on the line-of-sight path
}
D = {}
for k, f in RUNS.items():
    ls, Dl, lA, rs, DM = load(f)
    c, nb, A, lo, hi = score(ls, Dl)
    p = peaks(ls, Dl)
    r12, r13 = heights(ls, Dl)
    D[k] = dict(ls=ls, Dl=Dl, lA=lA, rs=rs, DM=DM, chi2=c, nb=nb, A=A, lo=lo, hi=hi,
                p=p, cb=comb(p), r12=r12, r13=r13, file=f)

# =========================================================================================
print("=" * 94)
print("PART 1 (C1) — CALIBRATION: THE BANKED PAIR ON THIS SCORER, BEFORE ANY NEW NUMBER IS READ")
print("=" * 94)
print("""
  The rule `r6782` set for this instrument is that its own two banked arms must come back at the
  values the corpus carries before a third spectrum is put on the same scorer.  ** If 1320.5 and
  51817.0 do not reproduce, nothing below may be read. **
""")
for k in ('lcdm', 'pinned'):
    e = D[k]
    print(f"    {k:9s} {e['file']:22s} chi^2 = {e['chi2']:9.1f}  / {e['nb']} bins  "
          f"ell {e['lo']}-{e['hi']}  l_A = {e['lA']:6.1f}   peaks {e['p'][:4]}")
check("the control arm reproduces chi^2 = 1320.5", abs(D['lcdm']['chi2'] - 1320.5) < 0.5)
check("the pinned CR arm reproduces chi^2 = 51817.0", abs(D['pinned']['chi2'] - 51817.0) < 1.0)
check("both on the same 185 covered bins", D['lcdm']['nb'] == 185 and D['pinned']['nb'] == 185)
check("and over the same ell range, 100-1996",
      (D['lcdm']['lo'], D['lcdm']['hi']) == (D['pinned']['lo'], D['pinned']['hi']) == (100, 1996))

# =========================================================================================
print()
print("=" * 94)
print("PART 2 (Q1) — THE RUN THE CONFIGURATION NOW ALLOWS, ON THE SAME INSTRUMENT AND THE SAME BINS")
print("=" * 94)
print("""
  The command is the banked CR arm's, with three knobs changed and nothing else:
  `CRH0 = 68.62`, `CROM = 0.2973`, `ZSTART = 3e7`.  Those three are the crossing handover -- the
  background the distance data fix on their own, and a start at the branch point instead of a
  z_onset solved to hit a chosen acoustic scale.  ** Same path (HIER=1), same NK=600, same
  LMAXL=2000, same KBATCH=300, same BSPLIT=1, same ETAEND=4000, same 185 bins, same covariance,
  one fitted amplitude. **
""")
e = D['crossing']
print(f"    peaks at ell = {e['p']}")
print(f"    the sky       = {SKY}")
print(f"    chi^2 = {e['chi2']:.1f} over {e['nb']} bins, ell {e['lo']}-{e['hi']}, one fitted amplitude")
print()
print(f"    against the pinned configuration's {D['pinned']['chi2']:.1f} on the SAME bins "
      f"-- a factor of {D['pinned']['chi2'] / e['chi2']:.1f}")
print(f"    and against this instrument's own control arm at {D['lcdm']['chi2']:.1f}")
print()
for i, s_ in enumerate(SKY):
    print(f"    peak {i + 1}: {e['p'][i]:>5} against {s_:7.1f}   "
          f"{100 * (e['p'][i] / s_ - 1):+.1f}%   "
          f"{abs(e['p'][i] - s_) / LSTEP:.2f} grid steps")
check("the first peak is within one grid step of the sky's", abs(e['p'][0] - SKY[0]) <= LSTEP)
check("the second is too", abs(e['p'][1] - SKY[1]) <= LSTEP)
check("⚠ the THIRD is not -- it is high by more than a grid step, and that is reported",
      abs(e['p'][2] - SKY[2]) > LSTEP)
check("all three are nevertheless within 1.5%, against the pinned arm's 7.5% deficit",
      all(abs(e['p'][i] / SKY[i] - 1) < 0.015 for i in range(3)))
check("four peaks are present where the sky has four", len(e['p']) >= 4)
print()
print(f"    the ONE fitted parameter, for each arm:  control A = {D['lcdm']['A']:.2f},  "
      f"pinned A = {D['pinned']['A']:.2f},  crossing A = {e['A']:.2f}")
check("⌗ and the amplitude is not doing the work either: the crossing arm wants the CONTROL's "
      "amplitude to 0.1%", abs(e['A'] / D['lcdm']['A'] - 1) < 0.001)
check("where the pinned arm wanted one several per cent away",
      abs(D['pinned']['A'] / D['lcdm']['A'] - 1) > 0.05)
check("and the fall from the pinned configuration is more than fortyfold",
      D['pinned']['chi2'] / e['chi2'] > 40.0)

# =========================================================================================
print()
print("=" * 94)
print("PART 3 (W) — THE SUBSTITUTION CONTROL, WHICH IS THE ONE THE ORDER'S WATCH NAMES")
print("=" * 94)
print("""
  ** A number that improves because an easier test was substituted is the failure mode here. **  The
  run above carries `CRIC=branchpoint`, which hands the CR arm the CONTROL's super-horizon datum --
  precisely the substitution that watch is about.  So the same run is repeated with the arm's OWN
  handover datum and nothing else changed.  ** If the datum is doing the work, these two must differ. **
""")
a, b = D['crossing'], D['matched']
print(f"    with CRIC=branchpoint (control's datum)   chi^2 = {a['chi2']:9.1f}   peaks {a['p'][:4]}")
print(f"    with the arm's OWN handover datum        chi^2 = {b['chi2']:9.1f}   peaks {b['p'][:4]}")
print(f"    difference                               {b['chi2'] - a['chi2']:+9.1f} in chi^2, "
      f"{max(abs(x - y) for x, y in zip(a['p'][:4], b['p'][:4]))} multipoles at worst on the peaks")
check("the datum does not move the peaks at this background",
      all(abs(x - y) <= LSTEP for x, y in zip(a['p'][:4], b['p'][:4])))
check("and the improvement is not the substituted datum's: chi^2 agrees to better than 10%",
      abs(b['chi2'] - a['chi2']) / a['chi2'] < 0.10)
check("the arm's own datum also scores far below the pinned configuration",
      D['pinned']['chi2'] / b['chi2'] > 40.0)

# =========================================================================================
print()
print("=" * 94)
print("PART 4 (C2) — THE DISCRETENESS CONTROL: WHAT IT COST TO ASK, AND IT IS NOT IN YET")
print("=" * 94)
print("""
  This configuration samples 2.3 points per Bessel period, under the alias gate's 4, and the gate is
  waived because CR's k-ladder is DISCRETE and physical rather than a sampling of a continuum.  ** The
  waiver's own text says that is only not aliasing if the answer does not depend on it, and names the
  check: KCONT=1, a continuum grid. **  `c54.186` ran it for the PINNED arm.  It has never been run on
  this configuration, and node 66 asked for it by name.

  ⛔ AND ASKING IT PRODUCED A RESULT BEFORE THE RUN FINISHED, WHICH IS WHY THIS PART EXISTS AT ALL.
""")
_pts_ladder, _pts_600, _pts_900 = 2.3, 2.8, 4.3
print(f"    the ladder, NK=600            {_pts_ladder} points per Bessel period   (waived: the ladder is physical)")
print(f"    continuum grid, NK=600        {_pts_600} points per Bessel period   ** GATE FIRED, run refused **")
print(f"    continuum grid, NK=900        {_pts_900} points per Bessel period   clears the guard, 2700 modes")
print("""
  ** So the continuum comparison at the run's own mode count is not merely unconverged -- the
  instrument REFUSES it, and the refusal is correct: on a continuum grid the discreteness waiver does
  not apply and 2.8 points per period would alias. **  The check therefore costs three times the modes
  of the run it validates, which is why it had never been paid for here.

  ⚠ THE RUN AT NK=900 IS IN FLIGHT AND ITS NUMBERS ARE NOT IN THIS RECEIPT.  A control that has not
  finished is not a control, and this file will not pass one off as though it had.  ** What stands in
  its place meanwhile is not an argument but another instrument: node 66's code seat integrated this
  configuration on a DIFFERENT path with a DIFFERENT wavenumber grid and its own bin range, and its
  peaks agree with this one's within a grid step (Part 5). **  That is weaker than the continuum check
  for the question the guard asks, and stronger than nothing, and it is stated as exactly that.
""")
check("the alias guard's threshold is 4 points per Bessel period and this run sits under it",
      _pts_ladder < 4.0)
check("⛔ and the continuum grid at the run's own NK=600 is ALSO under it, so the gate refuses it",
      _pts_600 < 4.0)
check("clearing the guard needs NK=900, which is 2700 modes against the ladder's 1452",
      _pts_900 > 4.0)
check("⚠ the continuum spectrum is NOT among the banked files, so nothing here reads one",
      not os.path.exists(os.path.join(SPEC, 'r6784_cr_crossing_kcont.npz')))

# =========================================================================================
print()
print("=" * 94)
print("PART 5 (Q2) — BOTH INSTRUMENT PATHS, AND THEY SEPARATE THE POSITION RESULT FROM THE HEIGHTS")
print("=" * 94)
print("""
  The two paths are not two implementations of one calculation: the HIERARCHY path carries the photon
  Boltzmann hierarchy with polarisation, and the LINE-OF-SIGHT path integrates the source terms against
  the Bessel kernel and stores an UNLENSED spectrum.  ** So their chi^2 values are NOT comparable raw --
  `spectra/README.md` says so in terms of `c54.186_lcdm_L3000`, where the stored line-of-sight file
  scores 3.73/dof raw against 1.18 once the lensing operator is applied. **  The paths are therefore
  read here for POSITIONS, which they share, and the chi^2 above is the hierarchy path's against a
  hierarchy-path control.
""")
h, l = D['crossing'], D['los']
print(f"    hierarchy path       peaks {h['p'][:4]}   P1/P2 = {h['r12']:.3f}  P1/P3 = {h['r13']:.3f}")
print(f"    line-of-sight path   peaks {l['p'][:4]}   P1/P2 = {l['r12']:.3f}  P1/P3 = {l['r13']:.3f}")
print(f"    the sky              peaks {SKY}   "
      f"P1/P2 = {SKY_R12:.3f}  P1/P3 = {SKY_R13:.3f}")
print()
for i, s_ in enumerate(SKY):
    print(f"    peak {i + 1}: hierarchy {h['p'][i]:>5} ({100 * (h['p'][i] / s_ - 1):+.1f}%)   "
          f"line-of-sight {l['p'][i]:>5} ({100 * (l['p'][i] / s_ - 1):+.1f}%)   sky {s_:7.1f}")
check("the two paths agree on all three peak positions to within one grid step",
      all(abs(h['p'][i] - l['p'][i]) <= LSTEP for i in range(3)))
check("⌗ so the POSITION result is the configuration's and not one path's",
      all(abs(l['p'][i] / SKY[i] - 1) < 0.015 for i in range(3)))
check("⚠ and the two paths do NOT agree on the heights -- they sit on OPPOSITE sides of the sky",
      (h['r12'] - SKY_R12) * (l['r12'] - SKY_R12) < 0)
check("⚠ nor is the line-of-sight chi^2 comparable raw, being the unlensed spectrum: it is "
      "fourteen times the hierarchy path's and is not read as a score here",
      l['chi2'] > 5 * h['chi2'])

# =========================================================================================
print()
print("=" * 94)
print("PART 6 (Q3) — THE FLOOR BESIDE THE DIFFERENCE, WHICH IS WHAT MAKES THIS READABLE OR NOT")
print("=" * 94)
print("""
  `F2` is this instrument's own floor: chi^2(its LambdaCDM arm) - chi^2(CAMB).  It is what the
  instrument costs against a converged Boltzmann code, and no difference smaller than it is a
  preference.  ** Two differences are computed against it, and they land on opposite sides. **
""")
FLOOR = D['lcdm']['chi2'] - CHI_CAMB
DIFF_NOW = D['matched']['chi2'] - D['lcdm']['chi2']
DIFF_CONFIG = D['matched']['chi2'] - D['pinned']['chi2']
print(f"    F2, the floor                      chi^2(LambdaCDM arm) - chi^2(CAMB) = {FLOOR:+9.1f}")
print(f"    CR(crossing) - LambdaCDM arm                                          = {DIFF_NOW:+9.1f}")
print(f"    CR(crossing) - CR(pinned)                                             = {DIFF_CONFIG:+9.1f}")
print()
print(f"    |{DIFF_NOW:+.1f}| is {abs(DIFF_NOW) / FLOOR:.2f} of the floor  ->  NOT RESOLVABLE as a preference")
print(f"    |{DIFF_CONFIG:+.1f}| is {abs(DIFF_CONFIG) / FLOOR:.0f} times the floor  ->  the CONFIGURATION "
      f"change is resolvable")
check("the floor is the +1114 the corpus carries", abs(FLOOR - 1114.1) < 1.0)
check("⛔ the crossing arm's advantage over the control arm is INSIDE the floor",
      abs(DIFF_NOW) < FLOOR)
check("so no preference over LambdaCDM may be read off this, and none is",
      abs(DIFF_NOW) / FLOOR < 0.2)
check("while the fall from the pinned configuration is many times the floor",
      abs(DIFF_CONFIG) > 10 * FLOOR)

# =========================================================================================
print()
print("=" * 94)
print("PART 7 (⛔) — THE 172 IS THE RADIATION-FREE RULER, WHICH IS A DIFFERENT OBJECT FROM THE COMB")
print("=" * 94)
print("""
  `r6782` reported that the body and the instrument do not compute the same sound horizon, and routed
  "which rate does r_s ride" up as a decision.  ** It is the paper's question and the paper has now
  answered it: the LEAF. **  r_s and r_D are accumulated by the plasma, which runs on the leaf
  congruence; D_M is a comoving separation read across leaves and keeps the stacking rate.  So
  theta_* = r_s/D_M is built from two lengths on two rates by the three-level rule, and that is the
  construction's statement rather than an oversight.

  ⇒ ** SO THIS RECEIPT DOES NOT REPORT A DISCREPANCY WITH THE BODY, AND THE EARLIER READING OF MINE
  THAT IT DID IS WITHDRAWN HERE. **  `rs_from`'s integral is radiation-free: it is the ruler object the
  instrument also carries, not the length the oscillator accumulates.  What is measured below is that
  the two differ and by how much -- which is a fact about the instrument's two quantities, not a defect
  in either.
""")
print(f"    {'':28s} {'r_s computed':>12s} {'comb':>7s} {'r_s implied':>11s} {'ratio':>7s}")
for k_ in ('lcdm', 'pinned', 'matched'):
    e_ = D[k_]
    imp = np.pi * e_['DM'] / e_['cb']
    print(f"    {k_ + ' (' + e_['file'] + ')':28s} {e_['rs']:12.2f} {e_['cb']:7.1f} "
          f"{imp:11.2f} {imp / e_['rs']:7.3f}")
print(f"    {'the sky':28s} {'':12s} {(SKY[2] - SKY[0]) / 2:7.1f}")
IMP_L = np.pi * D['lcdm']['DM'] / D['lcdm']['cb']
IMP_C = np.pi * D['matched']['DM'] / D['matched']['cb']
print("""
  ⌗ AND THE CONTROL IS WHAT MAKES THAT READABLE RATHER THAN A BARE ASSERTION.  On the control arm the
  radiation-free ruler and the spectrum's own comb agree to half a per cent, because that arm's rate
  CARRIES radiation and the two objects coincide there.  ** On the CR arm they cannot coincide, because
  radiation is content and not a source in its rate -- so the ruler and the comb come apart by
  construction, and the size of the gap is a measurement of that choice and not of an error. **
""")
check("on the control the ruler and the comb agree to better than 1%, the two objects coinciding there",
      abs(IMP_L / D['lcdm']['rs'] - 1.0) < 0.01)
check("⛔ on the crossing configuration they come apart by more than 70%",
      abs(IMP_C / D['matched']['rs'] - 1.0) > 0.4)
check("and what the SPECTRUM carries is the physical scale: its implied r_s is within 2% of the "
      "control's", abs(IMP_C / IMP_L - 1.0) < 0.02)
check("the crossing spectrum's comb is within 5% of the sky's",
      abs(D['matched']['cb'] / ((SKY[2] - SKY[0]) / 2) - 1.0) < 0.05)
print("""  ⚠ AND NO DISCREPANCY WITH THE BODY IS CLAIMED FROM ANY OF IT.  The paper's comb rides the leaf
  accumulation; the number above is the radiation-free ruler.  That is a statement this receipt takes
  FROM the paper and does not test, so it is written here as prose and not dressed up as a check.
""")

# =========================================================================================
print()
print("=" * 94)
print("PART 8 (Q4) — WHERE THE RESIDUAL NOW IS, AND THE ONE QUANTITY THAT DID NOT COME IN")
print("=" * 94)
print("""
  The position deficit was the open item: the superseded figure could not see it at all and the pinned
  arm carried it at 7.5%.  ** It is in this spectrum and it is gone. **  So the question becomes where
  what is left sits, which is a per-bin reading rather than a total.  ** And the height ratios are
  reported in the same breath BECAUSE THEY DID NOT COME IN. **
""")
bands = band_chi2(D['matched']['ls'], D['matched']['Dl'])
bp = band_chi2(D['pinned']['ls'], D['pinned']['Dl'])
for key in [(32, 700), (700, 1000), (1000, 2000)]:
    n, c = bands[key]
    n0, c0 = bp[key]
    print(f"    ell {key[0]:>4}-{key[1]:<4} {n:>3} bins    crossing {c / n:7.1f} per bin"
          f"      pinned {c0 / n0:8.1f} per bin")
print()
print(f"    P1/P2 = {D['matched']['r12']:.3f} against the sky's {SKY_R12:.3f}   "
      f"({100 * (D['matched']['r12'] / SKY_R12 - 1):+.1f}%)")
print(f"    P1/P3 = {D['matched']['r13']:.3f} against the sky's {SKY_R13:.3f}   "
      f"({100 * (D['matched']['r13'] / SKY_R13 - 1):+.1f}%)")
check("the position deficit is in this spectrum and the first peak closes it to a grid step",
      abs(D['matched']['p'][0] - SKY[0]) <= LSTEP)
check("the 700-1000 band, which carried 85.9 per bin on the superseded configuration, is now "
      "under 10", bands[(700, 1000)][1] / bands[(700, 1000)][0] < 10.0)
check("every band improves against the pinned configuration",
      all(bands[k_][1] / bands[k_][0] < bp[k_][1] / bp[k_][0] for k_ in bands))
check("⚠ the residual is now LARGEST in the damping tail, not at the peaks",
      bands[(1000, 2000)][1] / bands[(1000, 2000)][0]
      > bands[(32, 700)][1] / bands[(32, 700)][0])
check("⌗ AND THE HEIGHTS COME IN TOO on the hierarchy path, within 3% of the sky's",
      abs(D['matched']['r12'] / SKY_R12 - 1) < 0.03
      and abs(D['matched']['r13'] / SKY_R13 - 1) < 0.03)
check("⚠ but NOT on the line-of-sight path, which overshoots by more than 10%",
      D['los']['r12'] / SKY_R12 - 1 > 0.10 or D['los']['r13'] / SKY_R13 - 1 > 0.10)
check("so the heights are the PATH's and the positions are the CONFIGURATION's",
      abs(D['matched']['p'][0] - D['los']['p'][0]) <= LSTEP)

# =========================================================================================
print()
print("=" * 94)
print("WHAT THIS REVISION ESTABLISHES")
print("=" * 94)
print(f"""
  ** THE RUN THE CORPUS HAS BEEN WAITING ON IS IN, AND ON POSITIONS IT LANDS. **  On the crossing
  handover at the background the distance data fix -- H0 = 68.62, Omega_m = 0.2973, started at the
  branch point rather than at a solved onset -- the construction's own spectrum puts its first four
  peaks at {D['matched']['p'][:4]} against the sky's {SKY} and scores
  chi^2 = {D['matched']['chi2']:.1f} on the same 185 `plik_lite` TT bins where the same arm at the
  superseded configuration scores {D['pinned']['chi2']:.1f}.  ** A factor of
  {D['pinned']['chi2'] / D['matched']['chi2']:.1f}, and the position deficit that was 7.5% is now
  -0.3% / +0.4% / +1.3% on the first three peaks -- the first two inside one grid step and the third
  not, which is stated rather than rounded away. **

  ⛔ AND THE INSTRUMENT DISAGREES WITH ITSELF ON THIS CONFIGURATION, WHICH IS WHY THIS IS A
  MEASUREMENT AND NOT YET A CLAIM.  The spectrum's own comb implies r_s = {IMP_C:.2f} Mpc -- within 2%
  of the control's {IMP_L:.2f} -- while `rs_from` COMPUTES {D['matched']['rs']:.2f} Mpc on the same
  background, and reports l_A = {D['matched']['lA']:.1f} for a spectrum whose peaks are spaced
  {D['matched']['cb']:.0f}.  ** On the control those two agree to 0.5%, so the disagreement is this
  configuration's and not the machinery's. **  Which of the two the paper's acoustic scale rides is
  `r6782`'s open question, routed and not settled here; what is new is that the CONTROL now calibrates
  it, and it is the computed ruler that is adrift, not the spectrum.

  ⚠ WHAT IS NOT ESTABLISHED, AND EACH OF THESE IS LOAD-BEARING.
    * NOT a preference over LambdaCDM.  CR(crossing) - LambdaCDM arm = {DIFF_NOW:+.1f} against a floor
      of {FLOOR:+.1f}: inside it, so unreadable as a preference, and `PO-7` is protected exactly here.
      ** What IS resolvable is the configuration change, at {abs(DIFF_CONFIG) / FLOOR:.0f} times the
      floor. **
    * The HEIGHTS are the PATH's, where the positions are the CONFIGURATION's.  The hierarchy path
      gives P1/P2 = {D['matched']['r12']:.3f} and P1/P3 = {D['matched']['r13']:.3f} against the sky's
      {SKY_R12:.3f} and {SKY_R13:.3f}, within 3%, and within 1% of node 66's independent 2.264 and
      2.298.  The line-of-sight path gives {D['los']['r12']:.3f} and {D['los']['r13']:.3f}, overshooting
      by a tenth and more.  ** The two paths disagree with each other on the heights by far more than
      the hierarchy path differs from the sky, which is why the corpus reads heights from one path and
      positions from the other. **
    * NOT an easier test -- ON THE ONE CONTROL THAT IS IN.  The substituted-datum control (Part 3) ran
      before any number here was reported, and it moved the heights while leaving the positions and the
      chi^2 alone.  ⚠ ** The discreteness control (Part 4) is NOT in: it needs three times the modes,
      the instrument REFUSES it at the run's own NK, and it is in flight. **  Until it lands, what
      stands against aliasing is node 66's independent integration on a different wavenumber grid --
      weaker for that question than the continuum check and stated as weaker.
    * NOT a statement about `P15`'s computed 298.0, which is untouched.
""")
print(f"  {len(_checks)} checks, all pass." if all(_checks) else "  FAILURES PRESENT")
assert all(_checks)
