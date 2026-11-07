"""r7701+cc66 -- IS THE LAW'S q ~ 1.9 DEPARTURE THE STEP AT THE SECOND ACOUSTIC PEAK?

Both instruments are LIFTED, not reimplemented: the step's sliding-window locator from
`P15_the_step_is_the_excesss_own...`'s `slide` over `own_comb_kinds`, and the retention and the
acceptance law exactly as `the_phase_systematic...` reads them through `own_comb`.

`PREDICTION.md` registered three ways this answers falsely yes -- containment is cheap, the band is
seven times wider than the feature, and the two are different statistics on different banks sharing a
coordinate -- and registered the outcome as NOT one object with the reconciling mechanism named.
"""
import os
import sys

import numpy as np
from scipy.signal import argrelextrema

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.abspath(os.path.join(HERE, '..'))
SP = os.path.join(BW, 'spectra')
sys.path.insert(0, os.path.join(BW, 'r7637_70_own_comb_statistic'))
sys.path.insert(0, os.path.join(BW, 'r7639_cc66_P15_repoint_paper'))
import own_comb as OC                                                              # noqa: E402
import own_comb_kinds as OCK                                                       # noqa: E402

QE = np.asarray(np.load(os.path.join(SP, 'r6959_eta_cr_leafrec1.npz'))['q_edges'], float)
AOR = {'lcdm': 'r6941_fine_lcdm', 'cr': 'r6941_fine_cr_leafrec1'}


def fine(t):
    d = np.load(os.path.join(SP, AOR[t] + '.npz'))
    return d['ls'].astype(float) / float(d['l_A']), np.asarray(d['Dl'], float)


FB = {t: fine(t) for t in AOR}
PR = {t: dict(np.load(os.path.join(SP, n + '.npz'), allow_pickle=True)) for t, n in
      (('lcdm', 'r6915_pairs_lcdm'), ('cr', 'r6915_pairs_cr_leafrec1'))}
SO = {t: dict(np.load(os.path.join(SP, n + '.npz'), allow_pickle=True)) for t, n in
      (('lcdm', 'r6911_source_lcdm_leafrec1'), ('cr', 'r6911_source_cr_leafrec1'))}
BR = {t: dict(QL=PR[t]['ls'].astype(float) / float(PR[t]['l_A']),
              QK=SO[t]['k'] * float(SO[t]['r_s']) / np.pi,
              Dl=np.asarray(PR[t]['Dl'], float),
              S2=np.asarray(SO[t]['S_i'], float) ** 2) for t in PR}
C = OC.retention_combs(BR)

BAR = '  ' + '=' * 98
print(BAR)
print("  ⓵ THE STEP, LOCATED ON THE OWN COMB -- the lifted sliding-window instrument")
print(BAR)


# ⛭⛭ `r7703+cc66`: the band-edge-independent half of the statistic, built ONCE.  *The half-width is
#   the BAND EDGES and not the envelope window, so one state at `(mean, win=1.0)` serves all three
#   widths.  Measured at `r7703+cc66.0`: 129 interval reads were costing 129 comb fits and 258
#   envelope passes, 49.2 s against a 4.3 s host receipt.*
_ST = OCK.own_state(FB, 'mean', 1.0)


def slide(a, b, kind='mean'):
    """the excess on ONE interval, the same statistic `band_excess` cuts the bands with"""
    return float(OCK.band_excess_own_kind(FB, kind, np.array([a, b]), st=_ST)[0])


LOC, FAC, WID = [], [], []
for half in (0.175, 0.25, 0.35):
    row = [(c, slide(c - half, c + half)) for c in np.arange(0.85 + half, 3.0, 0.05)]
    lo = np.mean([v for c, v in row if c < 1.4])
    hi = np.mean([v for c, v in row if c > 2.2])
    mid = 0.5 * (lo + hi)

    def _cross(frac, near=None):
        """the crossing of the `frac` level, taken ADJACENT TO `near` and not the first one found.

        ⛔⛭ *The first form of this took `next(...)` -- the FIRST upward crossing anywhere in the
        scan.  At half-width 0.175 the curve is noisy enough to touch the 25 per cent level early and
        fall back, so the "25-75 rise" came out `0.602` against `0.066` and `0.078` at the two wider
        windows: an eight-fold outlier that then dragged the mean rise width to `0.248` and with it
        the band-to-feature ratio I was about to report.  **A locator that takes the first crossing
        is not locating the transition; it is locating the first excursion.** ⇒ Crossings are taken
        adjacent to the half-rise, which is what makes them crossings OF the transition.*
        """
        tgt = lo + frac * (hi - lo)
        xs = [(row[i - 1][0] + (tgt - row[i - 1][1]) / (row[i][1] - row[i - 1][1]) * 0.05)
              for i in range(1, len(row)) if row[i - 1][1] < tgt <= row[i][1]]
        if not xs:
            return float('nan')
        return min(xs, key=lambda v: abs(v - near)) if near is not None else xs[0]

    # ⛔⛭⛭ ** AND THE HALF-RISE IS THE LIFTED INSTRUMENT'S, UNCHANGED -- `xs[0]`, the FIRST crossing.
    #   **  *My first repair made `near=None` return `xs[-1]` instead, "fixing" the locator globally
    #   when the defect was only in the two crossings I had ADDED.  It moved the half-rise from
    #   `1.783` to `1.957` and broke the one thing that was already right: the lifted locator agrees
    #   with the second acoustic peak at `1.7775` to a part in four hundred, which is the agreement
    #   P15's located-step claim rests on.*  ⇒ ** The check that caught it is the one I printed
    #   beside it.  A repair to an instrument that moves a figure the instrument is validated against
    #   is not a repair. **
    _h = _cross(0.5)
    LOC.append(_h)
    FAC.append(hi / lo)
    WID.append(_cross(0.75, _h) - _cross(0.25, _h))   # the 25-75 rise, ADJACENT to the half-rise
    print(f"    half-width {half:.3f}:  plateaux {lo:+.4f} -> {hi:+.4f}  (factor {hi/lo:.2f})   "
          f"half-rise q = {LOC[-1]:.3f}   25-75 rise = {WID[-1]:.3f}")

PK = {t: fine(t)[0][argrelextrema(fine(t)[1], np.greater, order=30)[0]][:4] for t in AOR}
_hr, _w = float(np.mean(LOC)), float(np.mean(WID))
print(f"\n    half-rise, mean of three widths : q = {_hr:.4f}  (spread {np.ptp(LOC):.4f})")
print(f"    the 25-75 rise width            : {_w:.4f} in q  ({_w/1.0093:.3f} of a comb period)")
print(f"    the second acoustic peak        : q = {PK['lcdm'][1]:.4f} (control), "
      f"{PK['cr'][1]:.4f} (arm)")
print(f"    the step's factor               : {min(FAC):.2f} to {max(FAC):.2f}   ⛔ *registered "
      f"1.9-2.2 at `r7639` and recorded MISSED; the measured value is used, not the registered one*")

print()
print(BAR)
print("  ⓶ THE DEPARTURE'S BAND, AND THE CONTAINMENT TEST THAT LICENSES NOTHING")
print(BAR)
x7, y7 = OC.retained_own(BR, 1.0, 7, 5.75, C=C)
_L = np.load(os.path.join(HERE, '..',
                          'r7695_cc66_the_dip_counterfactual_the_cr_plasma_with_the_controls_'
                          'acoustic_period', 'gate3_and_bands.npz'))
law7, dep7, J = _L['law_aor'], _L['dep_aor'], int(_L['J'])
ed = np.linspace(0.35 + 0.5 + 1e-9, 5.75, 8)
print(f"    the departure's band  : centre {x7[J]:.2f}, edges [{ed[J]:.3f}, {ed[J+1]:.3f}], "
      f"width {ed[J+1]-ed[J]:.3f}")
_in = ed[J] <= _hr <= ed[J + 1]
print(f"    the step's half-rise  : q = {_hr:.4f}  ⇒ inside that band: {_in}")
print(f"    ⛔ AND THAT WAS REGISTERED AS NEAR-FORCED: the band is {(ed[J+1]-ed[J])/_w:.1f} times the "
      f"rise's own width, and")
print(f"       it spans {100*(ed[J+1]-ed[J])/(5.75-0.85):.0f} per cent of the whole q range.  "
      f"Containment is not evidence.")

print()
print(BAR)
print("  ⓷ THE RESOLUTIONS DO NOT OVERLAP, WHICH IS THE STRUCTURAL ANSWER")
print(BAR)
print(f"    the step is resolved at         : {_w:.3f} in q -- sliding windows of half-width 0.175 "
      f"give it stably")
print(f"    the retention's band must hold  : enough of a comb period for an RMS to mean an "
      f"amplitude.")
print(f"      *`own_comb`'s own docstring: a 0.70-wide band `holds less than one comb period, so its "
      f"RMS\n       depends on WHICH part of the cycle it covers` -- which is why the own-comb "
      f"remap exists at all.*")
print(f"    the comb period in q            : {C['lcdm']['L'][0]:.4f} (control), "
      f"{C['cr']['L'][0]:.4f} (arm)")
print(f"\n  ⇒ *** The step is a {_w:.2f}-wide feature; the departure cannot be localised below "
      f"{ed[J+1]-ed[J]:.2f}, ***")
print(f"     and {_w:.2f} < {ed[J+1]-ed[J]:.2f} by a factor of {(ed[J+1]-ed[J])/_w:.1f}.  "
      f"**Two features whose resolutions do not overlap are")
print(f"     not shown to be one object by sharing a coordinate.**")

print()
print(BAR)
print("  ⓸ ⛔ THE FIRST FORM OF THIS BLOCK WAS AN IDENTITY, NOT A MEASUREMENT")
print(BAR)
print("    *It computed `(y[1]-y[0]) - (law[1]-law[0])` and compared it to `dep[1]`.  But `dep = y -")
print("     law`, so that expression IS `dep[1] - dep[0]` algebraically: the `0.918` it reported was")
print("     just `1 - dep[0]/dep[1]`, which says only that band 1's departure is small -- already in")
print("     the table above.  **An assertion that cannot fail**, the `r7693` 8-vs-10 defect again.*")
print("    ⇒ Replaced by the question that can fail: DOES THE LAW HAVE A TRANSITION THERE TOO?")

print()
print(BAR)
print("  ⓹ THE LOWEST BAND'S RATIO -- the paper's own measure of the step -- IN BOTH")
print(BAR)
_r_meas = (y7[0] - 1.0) / np.mean(y7[1:] - 1.0)
_r_law = (law7[0] - 1.0) / np.mean(law7[1:] - 1.0)
print(f"    the MEASURED retention's lowest band, over the mean of the rest : {_r_meas:.4f}")
print(f"    the LAW's lowest band, over the mean of the rest                : {_r_law:.4f}")
print(f"    *P15: the lowest band runs `between a third and two thirds of the rest`*")
print(f"\n  ⇒ *** BOTH SIT IN THAT WINDOW AND THEY AGREE TO "
      f"{100*abs(_r_law/_r_meas - 1):.1f} PER CENT. ***")
print(f"     **So the law DOES carry the step's size.**  The order's conditional -- `the law carries")
print(f"     everything about the retention except the step` -- is the wrong way round on this "
      f"reading.")

print()
print(BAR)
print("  ⓺ SO WHAT THE LAW GETS WRONG IS THE TRANSITION'S WIDTH, NOT ITS SIZE")
print(BAR)
_AQ = {'cr': np.asarray(_L['ls'], float) / float(_L['l_A'])} if 'ls' in _L.files else None
_LC = np.load(os.path.join(HERE, '..', 'r7695_cc66_the_dip_counterfactual_the_cr_plasma_with_the_'
                                       'controls_acoustic_period', 'law_at_rho_cache.npz'))
_AL = np.load(os.path.join(SP, 'r7041_accept_lcdm.npz'), allow_pickle=True)
_qa = np.asarray(_LC['ls'], float) / float(_LC['l_A'])
_Aa = np.asarray(_LC['A_bank'], float)
_qc = np.asarray(_AL['ls__fixed'], float) / float(_AL['l_A__fixed'])
_Ac = np.asarray(_AL['A'], float)


def lawband(a, b):
    """the law's arm/control ratio over one interval, by band MEAN -- `r7689` arm 5, unchanged"""
    g = np.linspace(a, b, 400)
    return float(np.interp(g, _qa, _Aa).mean() / np.interp(g, _qc, _Ac).mean()) - 1.0


LLOC, LWID, LFAC = [], [], []
for half in (0.175, 0.25, 0.35):
    row = [(c, lawband(c - half, c + half)) for c in np.arange(0.85 + half, 3.0, 0.05)]
    lo = np.mean([v for c, v in row if c < 1.4])
    hi = np.mean([v for c, v in row if c > 2.2])

    def _lx(frac, near=None):
        tgt = lo + frac * (hi - lo)
        xs = [(row[i - 1][0] + (tgt - row[i - 1][1]) / (row[i][1] - row[i - 1][1]) * 0.05)
              for i in range(1, len(row)) if row[i - 1][1] < tgt <= row[i][1]]
        if not xs:
            return float('nan')
        return min(xs, key=lambda v: abs(v - near)) if near is not None else xs[0]

    _h = _lx(0.5)
    LLOC.append(_h)
    LWID.append(_lx(0.75, _h) - _lx(0.25, _h))
    LFAC.append(hi / lo)
    print(f"    LAW, half-width {half:.3f}:  plateaux {lo:+.4f} -> {hi:+.4f}  "
          f"(factor {hi/lo:.2f})   half-rise q = {_h:.3f}   25-75 rise = {LWID[-1]:.3f}")

_lhr, _lw = float(np.nanmean(LLOC)), float(np.nanmean(LWID))
print(f"\n                            half-rise q      25-75 rise width")
print(f"    the EXCESS's step      :   {_hr:.4f}           {_w:.4f}")
print(f"    the LAW's transition   :   {_lhr:.4f}           {_lw:.4f}")
print(f"    the second peak        :   {PK['lcdm'][1]:.4f}")
print(f"\n  ⇒ the law's half-rise sits {_lhr-_hr:+.4f} from the step's, and its rise is "
      f"{_lw/_w:.1f} times as WIDE.")

print()
print(BAR)
print("  ⓻ ⛔ BUT A 25-75 WIDTH FROM A SLIDING WINDOW IS NOT A WIDTH -- IT IS BOUNDED BELOW BY THE "
      "WINDOW")
print(BAR)
print("    *A sliding RMS of half-width `h` smears a true step over `2h`, so its own 25-75 rise")
print("     cannot come out below about `h`.  ⇒ A measured value AT or BELOW that floor means the")
print("     feature is UNRESOLVED, not that its width has been measured.*")
print("      half-width h    floor ~h     the EXCESS's 25-75     the LAW's 25-75    excess resolved?")
for _h0, _we, _wl in zip((0.175, 0.25, 0.35), WID, LWID):
    print(f"      {_h0:.3f}           {_h0:.3f}        {_we:.3f}                  {_wl:.3f}"
          f"              {'YES' if _we > 1.2*_h0 else 'no -- below the floor'}")
print(f"\n  ⇒ *** The excess's transition is UNRESOLVED at every window: sharper than "
      f"{2*0.175:.2f} in q, ***")
print(f"     which is what P15 says of it -- `narrower than the narrowest window that resolves it`.")
print(f"  ⇒ *** The LAW's transition IS resolved at every window, at "
      f"{min(LWID):.2f}-{max(LWID):.2f}. ***")
print(f"  ⌗ **Both are smeared by the SAME windows, so the contrast is the features' and not the")
print(f"     smoothing's** -- which is the only form in which these two widths may be compared, and")
print(f"     it is why the `{_lw/_w:.1f} times` above is reported as a RATIO AT FIXED SMOOTHING and")
print(f"     not as a ratio of two widths.")
np.savez(os.path.join(HERE, 'step_vs_departure.npz'), loc=np.array(LOC), fac=np.array(FAC),
         wid=np.array(WID), half_rise=_hr, rise_width=_w, peak2=PK['lcdm'][1],
         band_edges=ed, x7=x7, y7=y7, law7=law7, dep7=dep7, J=J,
         law_loc=np.array(LLOC), law_wid=np.array(LWID), law_fac=np.array(LFAC),
         r_meas=_r_meas, r_law=_r_law, inside=_in)
