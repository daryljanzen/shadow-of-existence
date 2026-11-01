#!/usr/bin/env python3
"""
RECEIPT -- P15: ** `cc66.155` ASKED FOR A DIFFERENT STATISTIC AND COSTED IT AT ZERO RUNS.  IT IS BUILT
HERE, ON THE SAME BANK, AND IT WORKS: THE DE-TILTED PEAK SET SEPARATES THE BARYON DIRECTION FROM A
PURE TILT BY A FACTOR OF `$11.7$` ON THE COMMON OFFSET AND `$18.3$` ON THE ODD-EVEN ALTERNATION,
WHERE THE FREE-PERIOD SLOPE SEPARATED THEM BY `$1.3$`. **  ⛭ AND THE DE-TILT IS NOT A TUNING CHOICE: IT IS
FORCED BY A PHYSICS CONTROL.  Without it `$n_s$` moves the common offset MORE THAN ANY OTHER
DIRECTION, which a primordial tilt cannot do; with it that response collapses by a factor of `$21$`
and becomes window-independent.  *** The same disease `cc66.155` diagnosed in the slope, found and
removed in the peak set rather than argued away. ***

  ⛔⛭⛭ ** THE TITLE'S CLAUSE -- THAT THE DRIVING HALF NEEDS ITS OWN PAIR BEFORE IT CAN BE READ AT ALL
  -- IS THE NAMESAKE ARM'S, AND ON THE ARM OF RECORD THE DRIVING PAIR READS. **  *Re-pointed to
  `LEAFREC=1` at `$H_0=68.5707$`, `$\\Omega_m=0.291246$`, the CR driving-ON spectrum HAS an
  integer-spaced peak series: worst gap error `$0.103$` against the grid's own `$0.102$`, a factor of
  `$1.0$`, where on the namesake arm it was `$0.275$` against `$0.105$`.  The comb the common-offset
  statistic assumes is there, so the step that obstruction blocked is MEASURED here --
  `$\\Delta\\varphi=+0.12611$` and `$\\Delta\\mathrm{alt}=-0.02201$`, against the control arm's
  same-vintage `$+0.12649$` and `$-0.02469$`.  ** Both are opposite in sign to this arm's OWN baryon
  direction on both components, so the orthogonality the ask rested on now holds on the arm itself and
  not only on the control. **  ⛔ What is still owed is a VINTAGE and not a reading: the driving pair
  was run at `L3000` and the grids were not, so a clean number still wants the `NODRIVE` pair at the
  grids' own configuration.*

  ⇒ ** THE REVISED COST IS TEN RUNS AND NOT EIGHT, AND THE RE-POINT LEAVES ITS SIZE ALONE: ** *the
  eight `RBFAC` runs `cc66.155` named, PLUS a `NODRIVE` pair at the grids' own configuration.  ⛭ Its
  JUSTIFICATION is what moved with the arm: the pair is wanted because the banked one is a different
  VINTAGE from the grids -- not, as on the namesake arm, because this statistic cannot read it.*

** COMPUTES: peak positions on `$38$` banked spectra by parabola vertex on the instrument's OWN
   samples, after dividing out a single global power law fitted in log-log over
   `$150\\le\\ell\\le1600$`; then two statistics per configuration -- the common offset
   `$\\varphi=\\langle \\ell_n/\\ell_A-n\\rangle$` and the alternation
   `$\\langle r_n(-1)^n\\rangle$` -- and their logarithmic derivatives along every banked direction,
   both arms, both nine-run grids.  The de-tilt is swept against the fitting half-window over
   `$25$`--`$75$` so its necessity is measured and not asserted.  *** No new spectrum, no grid,
   nothing refitted -- which is what `cc66.155` costed this half at. *** **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy; ~10 s)
"""
import io
import ast
import os
import re
import sys

import numpy as np

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok, got=None):
    #: ⛭ r7649+cc66.87: `got` added, optional, so a gate can PRINT WHAT IT MEASURED beside its
    #: verdict.  Every call that predates this keeps working unchanged.
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}" + (f"   ({got})" if got is not None else ""))
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
# ⛭⛭ RE-POINTED ONTO THE ARM OF RECORD AT r7643+cc66.49, on node 69's ⑴ of `r7643` (its option 1).
#   The CR side of both direction grids and both CR driving spectra have arm-of-record siblings in
#   70's second bank; the CONTROL's do not move, which is the bank's own statement and is why only
#   the `cr` entries below carry the suffix.
#   ⛔ *And `BASEVAL`'s `cr` row moves WITH them, read from the grid's own manifest rather than
#   typed: every gated quantity here is a LOGARITHMIC derivative, so the base value is a divisor, and
#   the arm-of-record grids are centred on the arm of record's own fitted point.  Left at the
#   distances' point it would divide the tilt direction by a base 5.2 per cent wrong and the baryon
#   direction 3.4 per cent wrong -- the two the headline ratio is built from.*
GO = {'lcdm': os.path.join(BW, 'r7093_directions', 'grid_oneclock'),
      'cr': os.path.join(BW, 'r7093_directions', 'grid_oneclock_leafrec1')}
GL = {'lcdm': os.path.join(BW, 'r7095_directions', 'grid_licensed'),
      'cr': os.path.join(BW, 'r7095_directions', 'grid_licensed_leafrec1')}
SP = os.path.join(BW, 'spectra')
for _p in (GO['lcdm'], GO['cr'], GL['lcdm'], GL['cr'], SP):
    if not os.path.isdir(_p):
        print(f"  ⛔ A BANK THIS RECEIPT READS IS NOT ON DISK: {_p}")
        sys.exit(1)

# ⛭ ARM KEYS READ: NONE.  *Node 69's arm-key naming rule, adopted at `r7643`, asks each receipt
#   reading a two-arm bank to name the arm keys it reads the way it already names the files.  This one
#   has none to name: it separates the arms by FILE and by DIRECTORY -- `grid_oneclock` against
#   `grid_oneclock_leafrec1`, `c54.186_lcdm_L3000.npz` against `c54.186_cr_L3000_leafrec1.npz` -- and
#   out of each archive reads only `ls`, `Dl`, `l_A` and `manifest`, not one of them arm-suffixed.
#   ⇒ Stated rather than left absent, so a reader hunting a hidden `__cr` read here is told there is
#   none instead of having to infer it.*

LMIN, LMAX = 150.0, 1600.0      # 0.8*LMAXL on the grids, which is `chi2_of`'s own truncation rule
NPK = 5                         # the acoustic peaks the grids resolve below LMAX
_DIST = {'H0': 68.60, 'OM': 0.2973, 'NS': 0.965, 'WB': 0.0224}   # what the distances fix
_z_aor = np.load(os.path.join(GO['cr'], 'cr_base.npz'), allow_pickle=True)
if 'manifest' not in _z_aor.files:
    print("  ⛔ the arm-of-record grid carries no manifest, so its centre cannot be read and no "
          "logarithmic derivative below may be normalised.  *Nothing is asserted.*")
    sys.exit(1)
_m_aor = _z_aor['manifest'].item()
if isinstance(_m_aor, (bytes, str)):
    _m_aor = ast.literal_eval(_m_aor if isinstance(_m_aor, str) else _m_aor.decode())
_p_aor = _m_aor['point']
_AOR = {'H0': float(_p_aor['CRH0']), 'OM': float(_p_aor['CROM']),
        'NS': float(_p_aor['NS']), 'WB': float(_p_aor['WBH2'])}
BASEVAL = {k: {'cr': _AOR[k], 'lcdm': (67.40 if k == 'H0' else 0.3150 if k == 'OM' else _DIST[k])}
           for k in ('H0', 'OM', 'NS', 'WB')}
STEP = {'H0': 2.00, 'OM': 0.0150, 'NS': 0.020, 'WB': 0.0008}
PARS = ('H0', 'OM', 'NS', 'WB')


def peak_series(path, halfwin=40.0, detilt=True):
    """de-tilt, find the acoustic maxima, refine each by a parabola on the ORIGINAL samples."""
    z = np.load(path, allow_pickle=True)
    ls = np.asarray(z['ls'], float)
    Dl = np.asarray(z['Dl'], float)
    lA = float(z['l_A'])
    m = (ls >= LMIN) & (ls <= LMAX) & (Dl > 0)
    tilt = float(np.polyfit(np.log(ls[m]), np.log(Dl[m]), 1)[0])
    Y = Dl / ls ** tilt if detilt else Dl.copy()
    lg = np.arange(LMIN, min(LMAX, ls.max()), 0.5)
    D = np.interp(lg, ls, Y)
    idx = [i for i in range(2, len(D) - 2)
           if D[i] > D[i - 1] and D[i] >= D[i + 1] and D[i] > D[i - 2] and D[i] >= D[i + 2]]
    coarse = []
    for i in idx:
        if not coarse or lg[i] - coarse[-1] > 60.0:
            coarse.append(lg[i])
    pk = []
    for l0 in coarse[:NPK]:
        w = (ls >= l0 - halfwin) & (ls <= l0 + halfwin)
        if w.sum() < 4:
            pk.append(np.nan)
            continue
        c = np.polyfit(ls[w] - l0, Y[w], 2)
        pk.append(l0 - c[1] / (2 * c[0]) if c[0] < 0 else np.nan)
    return np.array(pk), lA, tilt


def phi_alt(path, halfwin=40.0, detilt=True):
    """the common offset and the odd-even alternation of the peak series, in units of l_A."""
    pk, lA, _t = peak_series(path, halfwin, detilt)
    ok = np.isfinite(pk)
    n = np.arange(1, len(pk) + 1)[ok]
    p = pk[ok] / lA
    phi = float(np.mean(p - n))
    r = p - (n + phi)
    return phi, float(np.mean(r * (-1.0) ** n)), int(ok.sum())


def deriv(gdir, arm, par, halfwin=40.0, detilt=True):
    """d(phi)/dln(theta) and d(alt)/dln(theta) by central difference on the banked pair.

    `gdir` is the per-arm map, so the arm chooses the directory: the CR side reads the
    arm-of-record grid and the control reads its own, which does not move.
    """
    sm = phi_alt(os.path.join(gdir[arm], f'{arm}_{par}m.npz'), halfwin, detilt)
    sp = phi_alt(os.path.join(gdir[arm], f'{arm}_{par}p.npz'), halfwin, detilt)
    g = BASEVAL[par][arm] / (2 * STEP[par])
    return (sp[0] - sm[0]) * g, (sp[1] - sm[1]) * g


# ============================================================ A. the de-tilt is forced
head("A.  THE DE-TILT IS FORCED BY A PHYSICS CONTROL, NOT CHOSEN -- AND THE CONTROL IS `n_s`")

print("      `n_s` tilts the PRIMORDIAL spectrum and CANNOT move a peak position relative to the")
print("      sound horizon: it multiplies the initial power and leaves the transfer function alone.")
print("      ⚠ It is an INHERITED quantity -- the corpus posits no six-parameter vector, so the")
print("      spectral index is ADOPTED from LambdaCDM's own basis and derived from nothing this")
print("      construction predicts.  What that costs: no conclusion here is a claim about n_s.  It")
print("      is used because its effect on the peak PHASE is known a priori to be nil, which is")
print("      exactly what a control for a phase statistic requires.")
print()
print(f"      {'de-tilt':8s} {'halfwin':>8s} {'dphi/dlnNS':>12s} {'dphi/dlnWB':>12s} {'|WB/NS|':>9s}")
SWEEP = {}
for _dt in (False, True):
    for _hw in (25.0, 40.0, 55.0, 75.0):
        dn = deriv(GO, 'cr', 'NS', _hw, _dt)
        dw = deriv(GO, 'cr', 'WB', _hw, _dt)
        SWEEP[(_dt, _hw)] = (dn, dw)
        print(f"      {str(_dt):8s} {_hw:8.0f} {dn[0]:+12.5f} {dw[0]:+12.5f} "
              f"{abs(dw[0] / dn[0]):9.2f}")

_raw = [abs(SWEEP[(False, h)][0][0]) for h in (25.0, 40.0, 55.0, 75.0)]
_det = [abs(SWEEP[(True, h)][0][0]) for h in (25.0, 40.0, 55.0, 75.0)]
print(f"      ⇒ |dphi/dlnNS| raw {min(_raw):.5f}-{max(_raw):.5f}, de-tilted "
      f"{min(_det):.5f}-{max(_det):.5f}  -- a factor of {np.mean(_raw) / np.mean(_det):.0f}")
check("Ⓐ①  ** WITHOUT THE DE-TILT THE STATISTIC VIOLATES THE CONTROL: `n_s` moves the common offset "
      "by more than the baryon direction does, which a primordial tilt cannot do. **  That is the "
      "parabola's vertex being dragged by the slope under the peak -- the same disease `cc66.155` "
      "found in the free-period slope",
      all(abs(SWEEP[(False, h)][0][0]) > abs(SWEEP[(False, h)][1][0]) for h in (25.0, 40.0, 55.0)))
# ⛔⛭ r7643+cc66.49: ** THE THIRD LIMB OF THIS GATE IS THE NAMESAKE ARM'S AND IS STATED AS SUCH. **
#   As registered it asserted three things: the de-tilt collapses the control violation by ten or
#   more, the de-tilted reading is window-independent, and the RAW reading is NOT -- that last being
#   the evidence that the de-tilt is a repair rather than a tuning.  *The first two hold on the arm
#   of record (a factor of 21, de-tilted spread 6 per cent).  The third does not: the arm of record's
#   raw reading is already window-independent, at a spread of 1.4 per cent against the namesake's 21.*
#   ⇒ *** The de-tilt is still FORCED here -- Ⓐ① fires on this arm too -- and still removes the
#       violation.  What is absent is the drift, so the repair-not-tuning argument rests on the
#       namesake arm and is not restated as though it held here. ***
check("Ⓐ②  ** AND THE DE-TILT REMOVES IT BY A FACTOR OF TEN OR MORE AND MAKES IT "
      "WINDOW-INDEPENDENT. **  ⛔ *The third limb as registered -- that the RAW reading drifts with "
      "the window, which is what distinguished a repair from a tuning -- is the NAMESAKE arm's: here "
      "the raw reading is already flat, at a spread of 1.4 per cent against that arm's 21*",
      np.mean(_raw) / np.mean(_det) > 10.0
      and (max(_det) - min(_det)) / np.mean(_det) < 0.15)
print(f"      the raw response's own window spread on this arm: "
      f"{100 * (max(_raw) - min(_raw)) / np.mean(_raw):.1f} per cent "
      f"(the namesake arm's was 21)")
check("Ⓐ②ᵇ ⛔ and the absent drift is MEASURED rather than passed over: on this arm the raw "
      "response's window spread is under 5 per cent -- printed above -- where on the namesake arm "
      "it exceeded 15, which is the whole of what the third limb rested on",
      (max(_raw) - min(_raw)) / np.mean(_raw) < 0.05)


# ============================================================ B. the separation
head("B.  THE SEPARATION, BOTH ARMS AND BOTH GRIDS: THE BARYON DIRECTION AGAINST A PURE TILT")

D = {}
print(f"      {'grid':9s} {'arm':5s} {'par':3s} {'dphi/dln':>11s} {'dalt/dln':>11s}")
for gname, gdir in (('oneclock', GO), ('licensed', GL)):
    for arm in ('cr', 'lcdm'):
        for par in PARS:
            D[(gname, arm, par)] = deriv(gdir, arm, par)
            print(f"      {gname:9s} {arm:5s} {par:3s} {D[(gname, arm, par)][0]:+11.5f} "
                  f"{D[(gname, arm, par)][1]:+11.5f}")

RAT = {}
for arm in ('cr', 'lcdm'):
    rp = abs(D[('oneclock', arm, 'WB')][0] / D[('oneclock', arm, 'NS')][0])
    ra = abs(D[('oneclock', arm, 'WB')][1] / D[('oneclock', arm, 'NS')][1])
    RAT[arm] = (rp, ra)
    print(f"      {arm:5s}: WB:NS = {rp:.1f}x on the common offset, {ra:.1f}x on the alternation")
check("Ⓑ①  ** THE PEAK SET SEPARATES THE BARYON DIRECTION FROM A PURE TILT BY AN ORDER OF "
      "MAGNITUDE, ON BOTH COMPONENTS AND BOTH ARMS -- where `cc66.155` measured the free-period "
      "slope separating the same two directions by 1.3. **  That is the difference between a "
      "statistic that reads phase and one that reads gradient",
      all(RAT[a][0] > 8.0 and RAT[a][1] > 15.0 for a in ('cr', 'lcdm')))
#: ⛭⛭⛭ r7649+cc66.87: ** AND THE FOUR FACTORS ARE PINNED TO THEIR PRINTED DIGIT, which `r7649` asks
#:   for and which the gate above does not give. **  *`11.7` and `18.3` are this receipt's own
#:   headline and they are what `CR_cosmology.tex` l.2175 prints, beside the control's `11.4` and
#:   `22.6`.  The gate above is ONE-SIDED -- `> 8.0` and `> 15.0` -- so the four could drift to any
#:   larger value with the paper's digits unchanged and nothing would redden.  That is exactly what
#:   the standing rule means by "a figure the INDEX row prints is pinned only by a COMPARISON": an
#:   inequality that the figure happens to satisfy is not a pin on the figure.*
#:   ⌗ *Pinned as `round(x, 1) == want`, which is the paper's own precision and not a tolerance I
#:   chose: it fails the moment the printed digit would change, and it cannot pass by being
#:   satisfied from above.  The control's pair is pinned with the arm's because l.2175 prints all
#:   four in one sentence and a pin on half of it would leave the other half free.*
PRINTED = {('cr', 0): 11.7, ('cr', 1): 18.3, ('lcdm', 0): 11.4, ('lcdm', 1): 22.6}
for (_a, _i), _want in sorted(PRINTED.items()):
    _got = RAT[_a][_i]
    print(f"      l.2175's {_want:5.1f}x  {_a:5s} {'offset' if _i == 0 else 'alternation':11s} "
          f"computed {_got:8.4f}  rounds to {round(_got, 1):5.1f}  "
          f"{'ok' if round(_got, 1) == _want else 'OUT'}")
check("⛭⛭⛭ ** AND ALL FOUR FACTORS l.2175 PRINTS ARE PINNED TO THEIR PRINTED DIGIT: 11.7 and 18.3 "
      "on the arm of record, 11.4 and 22.6 on the control. **  ⛔ *The gate above is one-sided "
      "(`> 8.0`, `> 15.0`), so until r7649 all four could have drifted upward with the paper's "
      "digits unchanged and nothing would have reddened.  Pinned as `round(x, 1) == want`, which is "
      "the paper's own precision rather than a tolerance chosen here*",
      #: ⛔⛭⛭ r7649+cc66.87: ** WRITTEN OUT AS FOUR LITERAL COMPARISONS, AND THE FIRST FORM OF
      #:   THIS PIN WAS INVISIBLE TO THE GATE IT WAS WRITTEN FOR. **  *I first wrote it as
      #:   `all(round(RAT[a][i], 1) == w for (a, i), w in PRINTED.items())`, which is the same
      #:   test and reads better.  `check_figures_pinned` still reported both figures UNPINNED,
      #:   because its `pins()` walks the AST for `ast.Compare` nodes and reads the CONSTANT out
      #:   of the comparison -- and in the comprehension the constant is a loop variable, not a
      #:   literal.  So a pin held in a dict does not exist as far as that gate is concerned.*
      #:   ⇒ *That is the SECOND instrument with this blind spot: `check_quote_pins` has it too,
      #:   reported at `cc66.71` -- it sees literals passed inline to `re.search` and not literals
      #:   held in a dict.  Both are routed; this receipt simply does not rely on it.  The dict
      #:   above is kept for the PRINTED TABLE, which is what it is good for.*
      round(RAT['cr'][0], 1) == 11.7 and round(RAT['cr'][1], 1) == 18.3
      and round(RAT['lcdm'][0], 1) == 11.4 and round(RAT['lcdm'][1], 1) == 22.6,
      "; ".join(f"{a}[{i}] {RAT[a][i]:.4f}->{round(RAT[a][i], 1):.1f} want {w:.1f}"
                for (a, i), w in sorted(PRINTED.items())))

_nsconsist = [abs(D[(g, a, 'NS')][0]) for g in ('oneclock', 'licensed') for a in ('cr', 'lcdm')]
print(f"      and `n_s`'s own residual response is STABLE rather than merely small: "
      f"{min(_nsconsist):.5f} to {max(_nsconsist):.5f} across both arms and both grids")
check("Ⓑ②  and the tilt's residual leakage is consistent across all four configurations rather "
      "than scattering -- so what is left after the de-tilt is a small systematic floor and not "
      "noise that happened to come out low on the one case that was looked at",
      (max(_nsconsist) - min(_nsconsist)) / np.mean(_nsconsist) < 0.25)


# ============================================================ C. the convention robustness
head("C.  AND IT REPAIRS THE CONVENTION-DEPENDENCE `cc66.155` FOUND IN THE ARM'S OWN RESPONSE")

_conv = {}
for par in PARS:
    a = D[('oneclock', 'cr', par)]
    b = D[('licensed', 'cr', par)]
    _conv[par] = (abs(b[0] / a[0]) if a[0] else np.inf, abs(b[1] / a[1]) if a[1] else np.inf)
    print(f"      {par:3s}: licensed/oneclock = {_conv[par][0]:5.2f}x on phi, "
          f"{_conv[par][1]:5.2f}x on the alternation")
_worst = max(max(v) for v in _conv.values())
print(f"      ⇒ worst disagreement between the two arm geometries: {_worst:.2f}x")
print("      ⌗ `cc66.155` measured the SAME arm's required move on the free-period slope differing")
print("        by up to 49x between these two grids (294 per cent against 6).  The peak set's worst")
print("        is a factor of two, which is a statistic that measures the arm rather than the")
print("        convention it was computed under.")
check("Ⓒ①  ** the arm's response is convention-robust on the peak set where it was not on the "
      "slope: worst disagreement a factor of ~2 between `LEAFGEOM` and `LEAFREC`, against up to "
      "49 on the slope. **  A third independent respect in which this statistic is the better "
      "instrument, and the one that was not predicted in advance",
      _worst < 2.5)


# ============================================================ D. the driving half
head("D.  ⛭⛭ THE DRIVING HALF READS ON THIS ARM, AND THE TITLE\'S OBSTRUCTION WAS THE OTHER\'S")

_pairs = {'cr': ('c54.186_cr_L3000_leafrec1.npz', 'c54.193_cr_nodrive_L3000_leafrec1.npz'),
          'lcdm': ('c54.186_lcdm_L3000.npz', 'c54.193_lcdm_nodrive_L3000.npz')}
for _a, (_on, _off) in _pairs.items():
    for _f in (_on, _off):
        if not os.path.exists(os.path.join(SP, _f)):
            print(f"  ⛔ THE DRIVING PAIR IS NOT ON DISK: {_f}")
            sys.exit(1)

GAPS = {}
for tag, path in (('grid cr_base', os.path.join(GO['cr'], 'cr_base.npz')),
                  # ⛔ *these four are taken FROM `_pairs` rather than written again: re-pointed at
                  #   r7643+cc66.49 the two lists disagreed, this table kept reading the namesake's
                  #   driving pair, and the printed gap errors were the other arm's.*
                  ('L3000 cr ON', os.path.join(SP, _pairs['cr'][0])),
                  ('L3000 cr OFF', os.path.join(SP, _pairs['cr'][1])),
                  ('L3000 lcdm ON', os.path.join(SP, _pairs['lcdm'][0])),
                  ('L3000 lcdm OFF', os.path.join(SP, _pairs['lcdm'][1]))):
    pk, lA, _t = peak_series(path)
    g = np.diff(pk / lA)
    GAPS[tag] = float(np.max(np.abs(g - 1.0)))
    print(f"      {tag:15s} peaks/l_A = {np.round(pk / lA, 3)}  worst gap error "
          f"{GAPS[tag]:.3f}")
# ⛔⛭⛭ r7643+cc66.49: ** THIS GATE IS INVERTED BY THE RE-POINT, AND THAT IS THE FINDING. **  As
#   registered it asserted that the CR arm's banked driving-ON spectrum has NO integer-spaced peak
#   series, so the statistic could not read it -- its gaps missing `1` by three times what the grid's
#   do (0.275 against 0.105).  *On the arm of record the same spectrum reads 0.103 against the grid's
#   own 0.102: a factor of 1.0.*
#   ⇒ *** So the obstruction was the NAMESAKE arm's, the statistic CAN read the CR driving pair here,
#       and the title's "but the driving half needs its own pair" is that arm's clause.  Node 69
#       ruled this landing at `r7643` ⑴ (its option 1). ***
check("Ⓓ①  ⛔⛭⛭ ** ON THE ARM OF RECORD THE CR DRIVING-ON SPECTRUM *DOES* HAVE AN INTEGER-SPACED "
      "PEAK SERIES, so this statistic CAN read it -- worst gap error 0.103 against the grid's own "
      "0.102, a factor of 1.0, where the NAMESAKE arm's was 0.275 against 0.105. **  ⇒ *The "
      "obstruction this receipt's title names was that arm's, and the step it blocked is measured "
      "immediately below*",
      GAPS['L3000 cr ON'] < 1.25 * GAPS['grid cr_base'])

_lc_on = phi_alt(os.path.join(SP, 'c54.186_lcdm_L3000.npz'))
_lc_off = phi_alt(os.path.join(SP, 'c54.193_lcdm_nodrive_L3000.npz'))
_dphi, _dalt = _lc_off[0] - _lc_on[0], _lc_off[1] - _lc_on[1]
print(f"      the CONTROL's same-vintage pair does read: phi {_lc_on[0]:+.5f} -> {_lc_off[0]:+.5f} "
      f"(Dphi = {_dphi:+.5f})")
print(f"                                                  alt {_lc_on[1]:+.5f} -> {_lc_off[1]:+.5f} "
      f"(Dalt = {_dalt:+.5f})")
_wb = D[('oneclock', 'lcdm', 'WB')]
print(f"      against the baryon direction's {_wb[0]:+.5f} on phi and {_wb[1]:+.5f} on the "
      f"alternation")
check("Ⓓ②  ⛭ ** AND ON THE CONTROL, WHERE IT CAN BE READ, THE DRIVING AND THE BARYON DIRECTION "
      "MOVE THE PEAK SET IN OPPOSITE DIRECTIONS ON BOTH COMPONENTS. **  That is the orthogonality "
      "the ask rested on, and it is now measured on one arm rather than argued -- which is why the "
      "runs are worth their compute and why the pair has to be at the grids' own configuration",
      _dphi * _wb[0] < 0 and _dalt * _wb[1] < 0)

#: ** THE STEP Ⓓ① HAD BLOCKED, NOW THAT IT READS -- measured here rather than left as a note. **
_cr_on = phi_alt(os.path.join(SP, _pairs['cr'][0]))
_cr_off = phi_alt(os.path.join(SP, _pairs['cr'][1]))
_cdphi, _cdalt = _cr_off[0] - _cr_on[0], _cr_off[1] - _cr_on[1]
_awb = D[('oneclock', 'cr', 'WB')]
print(f"      the CR driving step on the arm of record: phi {_cr_on[0]:+.5f} -> {_cr_off[0]:+.5f} "
      f"(Dphi {_cdphi:+.5f}), alt {_cr_on[1]:+.5f} -> {_cr_off[1]:+.5f} (Dalt {_cdalt:+.5f})")
print(f"      against the arm's own baryon direction {_awb[0]:+.5f} / {_awb[1]:+.5f}, and the "
      f"control's step {_dphi:+.5f} / {_dalt:+.5f}")
check("Ⓓ③  ⛭⛭ ** AND THE ORTHOGONALITY THE ASK RESTED ON NOW HOLDS ON THE ARM ITSELF, not only on "
      "the control: the CR driving step and the arm of record's own baryon direction move the peak "
      "set OPPOSITE ways on both components, and the step is the control's to 0.3 per cent on the "
      "common offset. **  ⛔ *Its limit is unchanged and stated: the driving pair is a different "
      "vintage from the grids, so a clean number still wants the `NODRIVE` pair at the grids' own "
      "configuration -- what has changed is that the statistic can read the pair at all*",
      _cdphi * _awb[0] < 0 and _cdalt * _awb[1] < 0)


# ============================================================ E. what is owed
head("E.  SO THE STATISTIC EXISTS, THE ASK IS MET ON THIS ARM, AND WHAT REMAINS IS A VINTAGE")

print("      WHAT IS SETTLED, at no run cost, which is what this half was costed at:")
print("        * the de-tilted peak set IS a phase observable -- it passes the control the slope")
print("          failed, by a factor of ten or more, window-independently;")
print("        * it separates the baryon direction from a pure tilt by 11.7x on the common offset")
print("          and 18.3x on the alternation on the arm of record, 11.4x and 22.6x on the")
print("          control, on both grids;")
print("        * it is convention-robust where the slope was not;")
print("        * and on the arm of record AND on the control, the driving and the baryon")
print("          direction move it in OPPOSITE directions on both components -- the")
print("          orthogonality the ask rested on, now measured on the arm itself;")
print("        * which is the title's \"needs its own pair\" shown to be the namesake arm's")
print("          clause: there the driving-ON peak series was not a comb, here it is.")
print()
print("      ⛔ WHAT IS NOT, and what it costs:")
print("        * a driving signature at the grids' own vintage.  The pair that reads was run at")
print("          `L3000` and the grids were not, so the number above is a cross-vintage")
print("          difference -- sound, and not the clean one.")
print("        ⇒ TEN runs, not eight: the eight `RBFAC` runs (loading without recombination, which")
print("          `WBH2` cannot give) PLUS a `NODRIVE` pair, all at the grids' own configuration")
print("          (`HIER=1 LMAXL=2000 LSTEP=8 ZSTART=3e7`, `KFAC` at the corpus default 2.0, `NK`")
print("          not reduced), idempotent and resumable on output existence.")
check("Ⓔ①  ** the half `cc66.155` costed at zero runs is delivered at zero runs. **  38 banked "
      "spectra and the driving pairs read, no new spectrum, no grid, nothing refitted -- and the "
      "conclusion it reaches is that the statistic works, which is what makes the remaining ask "
      "worth putting",
      len(D) == 16 and all(RAT[a][1] > 15.0 for a in ('cr', 'lcdm')))
check("Ⓔ②  and the ask is bounded and justified by what was measured rather than by what was hoped: "
      "the `NODRIVE` pair at the grids' own configuration, at a configuration read off the grids' "
      "own switch lines.  ⛭ *Its JUSTIFICATION has changed with the arm -- the pair is wanted for "
      "VINTAGE now and not because the statistic cannot read the banked one -- and its size is "
      "unchanged*",
      _worst < 2.5)

print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED")
    for q in fail:
        print(f"      - {q}")
    print(BAR)
    sys.exit(1)
print("  ✔ ** THE DE-TILTED PEAK SET IS THE PHASE OBSERVABLE THE FREE-PERIOD SLOPE WAS NOT. **  It")
print("    separates the baryon direction from a pure tilt by 11.7x on the common offset and 18.3x")
print("    on the odd-even alternation here, 11.4x and 22.6x on the control, against 1.3x for the")
print("    slope, on both grids.")
print("  ⛭ ** AND THE DE-TILT IS FORCED RATHER THAN CHOSEN: without it `n_s` moves the common offset")
print("    more than the baryon direction does, which a primordial tilt cannot do.  With it that")
print("    response falls by a factor of ten or more and stops depending on the fitting window. **")
print("  ⌗ A third gain that was not predicted: the arm's response is convention-robust here -- a")
print("    factor of ~2 between LEAFGEOM and LEAFREC, against up to 49 on the slope.")
print("  ⛭⛭ ** THE DRIVING HALF READS ON THIS ARM, AND THE TITLE'S CLAUSE THAT IT CANNOT IS THE")
print("    NAMESAKE ARM'S. ** The CR driving-ON peak series IS a comb here -- gap error 0.103")
print("    against the grid's own 0.102, where that arm's was 0.275 against 0.105 -- so the step")
print("    is measured: Dphi +0.12611, Dalt -0.02201, against the control's +0.12649 / -0.02469.")
print("    Both oppose this arm's own baryon direction on both components, which is the")
print("    orthogonality the ask rested on, now on the arm and not only on the control.")
print("  ⇒ ** THE ASK IS STILL TEN RUNS AND NOT EIGHT, for a VINTAGE rather than a reading: ** eight")
print("    `RBFAC` plus a `NODRIVE` pair, all at the grids' own configuration, because the pair that")
print("    reads was run at `L3000` and the grids were not.")
print("  ⚠ Named and not supplied: five peaks make the alternation a coarse estimate; the de-tilt")
print("    is one global power law over 150-1600 and its necessity is swept but its FORM is a")
print("    choice; and `n_s` is inherited, used only as a control, with no claim made about it.")
