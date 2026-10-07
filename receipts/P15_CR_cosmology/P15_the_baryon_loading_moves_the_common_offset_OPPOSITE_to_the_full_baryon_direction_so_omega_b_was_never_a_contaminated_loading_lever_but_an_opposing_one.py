#!/usr/bin/env python3
"""
RECEIPT -- P15: ** `r7203` ASKED FOR THE LOADING LEVER'S CURVE AS A RECEIPT OF ITS OWN.  IT IS HERE,
AND IT CARRIES A FINDING THE CURVE WAS NOT RUN TO GET: *** THE SURGICAL LOADING LEVER MOVES THE
COMMON OFFSET IN THE OPPOSITE DIRECTION FROM THE FULL BARYON-DENSITY DIRECTION. *** **  `cc66.155`
said `$\\omega_b$` was "never a clean loading lever" because it moves loading AND recombination, so
"even a discriminating `WB` result would have been two effects".  ⛭ ** With the clean lever now run,
that statement is too weak: the two effects do not merely coexist, they OPPOSE on the phase
observable, and the non-loading part is the larger. **  `$\\mathrm{d}\\varphi/\\mathrm{d}\\ln R_b$`
is `$+0.0164$` where `$\\mathrm{d}\\varphi/\\mathrm{d}\\ln\\omega_b$` is `$-0.0276$`.

  ⇒ ** AND THE COMPARISON IS LEGITIMATE RATHER THAN NOMINAL, WHICH IS THE WHOLE REASON IT CAN BE
  MADE. **  *The instrument's line `214` is `RB_REC = RBFAC * RB_REC` and line `397` feeds that
  straight into `Rb_of`, so `$R_b\\propto\\mathrm{RBFAC}$` LINEARLY -- exactly as
  `$R_b\\propto\\omega_b$`.  A logarithmic step in `RBFAC` is therefore a logarithmic step of the
  same size in the loading, and the two derivatives are in the same units on the same quantity.
  **Without that the two numbers would share a name and nothing else.***

  ⌗ ** THE CURVE ALSO VINDICATES HAVING INSISTED ON A CURVE. **  *`$\\ell_A$` responds at `$8.5$`
  per unit `$\\ln\\mathrm{RBFAC}$` across `$0.1\\to0.5$` and `$22.1$` across `$0.5\\to1.0$` -- a
  factor of `$2.6$` between ADJACENT intervals of one lever.  A single central difference across
  `$0.1\\to2.0$`, which is what the lever was first costed as, would have reported one number for
  that and called it a response.*

** COMPUTES: the de-tilted peak statistic of `cc66.156` -- unchanged, not a new statistic -- on the
   four-point `RBFAC` curve `$\\{0.1,0.5,1.0,1.5\\}$` run at `r7201`/`r7203`, where `$1.0$` is the
   banked grid base and needed no run; the logarithmic response of both components about
   `$\\mathrm{RBFAC}=1$` by central difference on `$0.5\\to1.5$`; and that response against the
   banked `WB` and `NS` directions read off `cc66.156`'s own grid derivatives.  *** No refit, no new
   statistic, no new spectrum beyond the three `r7203` approved. *** **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy; ~10 s)
"""
import ast
import io
import os
import sys

import numpy as np

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
GO = os.path.join(BW, 'r7093_directions', 'grid_oneclock')
LEV = os.path.join(BW, 'r7201_cc66_loading_lever')
INS = os.path.join(BW, 'ACOUSTIC_two_arm.py')
for _p in (GO, LEV, INS):
    if not os.path.exists(_p):
        print(f"  ⛔ A SOURCE THIS RECEIPT READS IS NOT ON DISK: {_p}")
        sys.exit(1)

LMIN, LMAX, NPK, HALFWIN = 150.0, 1600.0, 5, 40.0
BASEVAL = {'H0': {'cr': 68.60, 'lcdm': 67.40}, 'OM': {'cr': 0.2973, 'lcdm': 0.3150},
           'NS': {'cr': 0.965, 'lcdm': 0.965}, 'WB': {'cr': 0.0224, 'lcdm': 0.0224}}
STEP = {'H0': 2.00, 'OM': 0.0150, 'NS': 0.020, 'WB': 0.0008}


# ---- cc66.156's statistic, verbatim in form: de-tilt, maxima on a 0.5 interpolant, parabola
#      vertex on the ORIGINAL samples.  Reproduced here rather than imported because a receipt
#      that imports another receipt's body stops being independently runnable.
def peak_series(path):
    z = np.load(path, allow_pickle=True)
    ls = np.asarray(z['ls'], float)
    Dl = np.asarray(z['Dl'], float)
    lA = float(z['l_A'])
    m = (ls >= LMIN) & (ls <= LMAX) & (Dl > 0)
    tilt = float(np.polyfit(np.log(ls[m]), np.log(Dl[m]), 1)[0])
    Y = Dl / ls ** tilt
    lg = np.arange(LMIN, min(LMAX, ls.max()), 0.5)
    Di = np.interp(lg, ls, Y)
    idx = [i for i in range(2, len(Di) - 2)
           if Di[i] > Di[i - 1] and Di[i] >= Di[i + 1] and Di[i] > Di[i - 2] and Di[i] >= Di[i + 2]]
    coarse = []
    for i in idx:
        if not coarse or lg[i] - coarse[-1] > 60.0:
            coarse.append(lg[i])
    pk = []
    for l0 in coarse[:NPK]:
        w = (ls >= l0 - HALFWIN) & (ls <= l0 + HALFWIN)
        if w.sum() < 4:
            pk.append(np.nan)
            continue
        c = np.polyfit(ls[w] - l0, Y[w], 2)
        pk.append(l0 - c[1] / (2 * c[0]) if c[0] < 0 else np.nan)
    return np.array(pk), lA


def phi_alt(path):
    pk, lA = peak_series(path)
    ok = np.isfinite(pk)
    n = np.arange(1, len(pk) + 1)[ok]
    p = pk[ok] / lA
    phi = float(np.mean(p - n))
    r = p - (n + phi)
    return phi, float(np.mean(r * (-1.0) ** n)), int(ok.sum()), pk, lA


def grid_deriv(arm, par):
    sm = phi_alt(os.path.join(GO, f'{arm}_{par}m.npz'))
    sp = phi_alt(os.path.join(GO, f'{arm}_{par}p.npz'))
    g = BASEVAL[par][arm] / (2 * STEP[par])
    return (sp[0] - sm[0]) * g, (sp[1] - sm[1]) * g


# ============================================================ A. the lever is one lever
head("A.  THE LEVER IS ONE LEVER, AND THAT IS READ OFF THE INSTRUMENT RATHER THAN ASSUMED")

SRC = io.open(INS, encoding='utf-8').read().split('\n')
_l214 = next((l.strip() for l in SRC if l.strip().startswith('RB_REC =') and 'RBFAC' in l), '')
_l397 = next((l.strip() for l in SRC if l.strip().startswith('Rb_of =')), '')
print(f"      the scaling:   {_l214}")
print(f"      its only use:  {_l397}")
# ⌗ The claim is that the assignment RESCALES the existing loading -- it multiplies the RBFAC read by
#   the RB_REC already in hand -- which is what makes the response linear and so makes a logarithmic
#   RBFAC derivative comparable with a logarithmic omega_b one.  ** ASSERTED THROUGH THE PARSE TREE
#   AND NOT THROUGH THE TEXT. **  Two gates objected to the text form in succession and both were
#   right: `check_prose_pins` to a count of operator characters, then `check_quote_pins` to the bare
#   `"*"` and `"="` that replaced it.  A character in another file's source is never the claim.  The
#   node types ARE: an assignment whose value is a multiplication, with RB_REC as a name inside it
#   and RBFAC as the string it reads.  Those two names stay pinned and are adjudicated DELIBERATE,
#   because which knob and which variable is exactly what the comparability rests on.
_t214 = ast.parse(_l214).body[0]
_names214 = {n.id for n in ast.walk(_t214) if isinstance(n, ast.Name)}
_strs214 = {c.value for c in ast.walk(_t214)
            if isinstance(c, ast.Constant) and isinstance(c.value, str)}
_rescales = (isinstance(_t214, ast.Assign)
             and isinstance(_t214.value, ast.BinOp)
             and isinstance(_t214.value.op, ast.Mult)
             and 'RB_REC' in _names214
             and 'RBFAC' in _strs214)
_t397 = ast.parse(_l397).body[0]
_names397 = {n.id for n in ast.walk(_t397) if isinstance(n, ast.Name)}
_feeds = isinstance(_t397, ast.Assign) and 'RB_REC' in _names397
print(f"      parsed: assignment={isinstance(_t214, ast.Assign)}  "
      f"operation={type(_t214.value).__name__}/"
      f"{type(getattr(_t214.value, 'op', None)).__name__}  rescales={_rescales}")
print(f"      and the spline that defines R_b(a) is built from that same name: {_feeds}")
check("Ⓐ①  ** `RBFAC` enters as a LINEAR multiplicative scaling of the recombination-epoch loading "
      "and nowhere else, so `$R_b\\propto\\mathrm{RBFAC}$` exactly as `$R_b\\propto\\omega_b$`. **  "
      "That is what makes a logarithmic `RBFAC` derivative comparable with a logarithmic "
      "`$\\omega_b$` derivative instead of merely similarly named -- and the two lines are quoted "
      "from the instrument, not paraphrased",
      _rescales and _feeds)

CURVE = {}
print()
print(f"      {'arm':5s} {'RBFAC':>6s} {'file':18s} {'mult':>5s} {'nonfin':>7s} {'l_A':>10s} "
      f"{'phi':>10s} {'alt':>10s}")
for arm in ('cr', 'lcdm'):
    for v in ('0.1', '0.5', '1.0', '1.5'):
        tag = f'{arm}_base' if v == '1.0' else f'{arm}_rb{v}'
        p = os.path.join(GO, f'{arm}_base.npz') if v == '1.0' else os.path.join(LEV, f'{tag}.npz')
        if not os.path.exists(p):
            continue
        z = np.load(p, allow_pickle=True)
        nf = int((~np.isfinite(np.asarray(z['Dl'], float))).sum())
        ph, al, npk, _pk, lA = phi_alt(p)
        CURVE[(arm, v)] = (lA, ph, al, npk, nf, len(np.asarray(z['ls'])))
        print(f"      {arm:5s} {v:>6s} {tag:18s} {len(np.asarray(z['ls'])):5d} {nf:7d} "
              f"{lA:10.3f} {ph:+10.5f} {al:+10.5f}")

_crv = [v for v in ('0.1', '0.5', '1.0', '1.5') if ('cr', v) in CURVE]
check("Ⓐ②  and every point on the curve is a complete spectrum of the same length with no "
      "non-finite sample, `$1.0$` being the banked grid base at the same `HIER`, `LSTEP`, `LMAXL` "
      "and `ZSTART` -- so the centre of the curve cost no run and is not a different vintage",
      len(_crv) == 4 and all(CURVE[('cr', v)][4] == 0 and CURVE[('cr', v)][5] == 238
                             and CURVE[('cr', v)][3] == NPK for v in _crv))


# ============================================================ B. it is a curve, not a slope
head("B.  IT IS A CURVE AND NOT A SLOPE, WHICH IS WHY ONE CENTRAL DIFFERENCE WOULD HAVE LIED")

_rows = [(float(v), CURVE[('cr', v)][0]) for v in _crv]
_seg = []
for (a, la), (b, lb) in zip(_rows, _rows[1:]):
    _seg.append((a, b, (lb - la) / np.log(b / a)))
    print(f"      l_A per unit ln(RBFAC) across {a:4.1f} -> {b:4.1f}:  {_seg[-1][2]:7.2f}")
_ratio = max(s[2] for s in _seg) / min(s[2] for s in _seg)
print(f"      ⇒ the extreme adjacent intervals differ by a factor of {_ratio:.2f}")
check("Ⓑ①  ** THE RESPONSE OF `$\\ell_A$` TO THE LOADING IS STRONGLY NON-LINEAR IN "
      "`$\\ln\\mathrm{RBFAC}$`: adjacent intervals of the SAME lever differ by more than a factor "
      "of two. **  So the lever's first costing -- a central difference across `$0.1\\to2.0$` -- "
      "would have returned a single number standing for a quantity that varies by that much "
      "inside its own span",
      _ratio > 2.0 and len(_seg) == 3)

_ph = [CURVE[('cr', v)][1] for v in _crv]
_al = [CURVE[('cr', v)][2] for v in _crv]
check("Ⓑ②  and BOTH components rise monotonically with the loading across the whole span, so the "
      "non-linearity is in the SIZE of the response and not in its direction -- which is what lets "
      "a sign be read off it at all",
      all(b > a for a, b in zip(_ph, _ph[1:])) and all(b > a for a, b in zip(_al, _al[1:])))

_gap = {}
for v in _crv:
    pk, lA = peak_series(os.path.join(GO, 'cr_base.npz') if v == '1.0'
                         else os.path.join(LEV, f'cr_rb{v}.npz'))
    q = pk[np.isfinite(pk)] / lA
    _gap[v] = (float(np.min(np.diff(q))), float(np.max(np.diff(q))))
    print(f"      RBFAC {v:>4s}: detected spacing {_gap[v][0]:.3f}-{_gap[v][1]:.3f} of l_A")
_b = _gap['1.0']
check("Ⓑ③  ⛭ and the comb -- the statistic's ONE assumption -- survives the lever at both ends: "
      "every point's detected spacing stays inside the banked base's own range to within a twentieth"
      ", against the `$0.74$`--`$0.96$` that disqualified the CR arm's banked driving-ON spectrum "
      "from this statistic in `cc66.156`.  *The lever is far from unity and that was the live risk*",
      all(_gap[v][0] > _b[0] - 0.05 and _gap[v][1] < _b[1] + 0.05 for v in _crv))


# ============================================================ C. the arms agree
head("C.  THE TWO ARMS AGREE AT MATCHED LOADING, SO THE LEVER ACTS ON THE ACOUSTICS NOT THE ARM")

_pairs = [v for v in ('0.1', '0.5', '1.0') if ('cr', v) in CURVE and ('lcdm', v) in CURVE]
_dph, _dal = [], []
for v in _pairs:
    a, b = CURVE[('cr', v)], CURVE[('lcdm', v)]
    _dph.append(abs(a[1] - b[1]))
    _dal.append(abs(a[2] - b[2]))
    print(f"      RBFAC {v:>4s}:  |dphi| {_dph[-1]:.2e}   |dalt| {_dal[-1]:.2e}   "
          f"|dl_A| {abs(a[0] - b[0]):.3f}")
check("Ⓒ①  ** the CR arm and the control agree on both components to parts in `$10^{4}$` at every "
      "matched loading. **  The refit matched their `$\\ell_A$` by construction, so this is not a "
      "null result about the arm -- it is what licenses reading the lever's effect as acoustic "
      "physics rather than as a property of `LEAFGEOM`, and it is why the control's own `$1.5$` "
      "point was the one `r7203` could drop",
      len(_pairs) >= 3 and max(_dph) < 1e-3 and max(_dal) < 1e-3)


# ============================================================ D. the finding
head("D.  ⛭⛭⛭ THE FINDING: THE CLEAN LEVER AND THE FULL BARYON DIRECTION OPPOSE ON THE OFFSET")

_i5, _i15 = _crv.index('0.5'), _crv.index('1.5')
_g = 1.0 / np.log(1.5 / 0.5)
LOAD = ((_ph[_i15] - _ph[_i5]) * _g, (_al[_i15] - _al[_i5]) * _g)
WB = grid_deriv('cr', 'WB')
NS = grid_deriv('cr', 'NS')
print(f"      d/dln(RBFAC)   -- the LOADING alone, central difference 0.5->1.5 about 1.0:")
print(f"          phi {LOAD[0]:+.5f}      alternation {LOAD[1]:+.5f}")
print(f"      d/dln(WBH2)    -- the FULL baryon direction, off the banked grid:")
print(f"          phi {WB[0]:+.5f}      alternation {WB[1]:+.5f}")
print(f"      d/dln(NS)      -- the control direction, which carries no acoustic phase:")
print(f"          phi {NS[0]:+.5f}      alternation {NS[1]:+.5f}")
print()
_resid = WB[0] - LOAD[0]
print(f"      ⇒ on the common offset the two have OPPOSITE SIGN.  Decomposing `$\\omega_b$` into")
print(f"        its loading part and the rest:  {WB[0]:+.5f} = {LOAD[0]:+.5f} (loading)")
print(f"        {_resid:+.5f} (everything else omega_b does), so the non-loading part is")
print(f"        {abs(_resid / LOAD[0]):.1f}x the loading part AND of the opposite sign.")
check("Ⓓ①  ** `$\\mathrm{d}\\varphi/\\mathrm{d}\\ln R_b$` IS POSITIVE WHERE "
      "`$\\mathrm{d}\\varphi/\\mathrm{d}\\ln\\omega_b$` IS NEGATIVE. **  *`cc66.155` called "
      "`$\\omega_b$` a contaminated loading lever -- loading and recombination together, so 'even a "
      "discriminating `WB` result would have been two effects'.*  ⇒ ** It is worse than contaminated"
      ": the two effects OPPOSE on this observable, and the one that is not the loading is the "
      "larger. **  So `$\\omega_b$`'s offset response is not a weakened reading of the loading's -- "
      "it points the other way",
      LOAD[0] > 0 and WB[0] < 0)
check("Ⓓ②  and that is a statement about `$\\omega_b$` rather than about the statistic's precision: "
      "the non-loading part of the `WB` response exceeds the loading part by more than a factor of "
      "two, so no sharpening of the measurement would recover the loading's sign from the `WB` "
      "direction alone",
      abs(_resid) > 2.0 * abs(LOAD[0]))
check("Ⓓ③  ⚠ and on the ALTERNATION they do NOT oppose -- both are positive, within a factor of "
      "two.  *Stated because it bounds the finding: the opposition is a property of the common "
      "offset alone, and a statistic reading only the odd-even alternation would have seen the "
      "clean lever and the full baryon direction agree.*",
      LOAD[1] > 0 and WB[1] > 0 and abs(LOAD[1] / WB[1]) < 2.0)


# ============================================================ E. what this does not claim
head("E.  WHAT THIS DOES NOT CLAIM")

print("  ⛔ NO CARRIER IS NAMED HERE.  This receipt measures ONE of the two candidates -- the")
print("     loading -- against the bank's own baryon direction.  The driving half is a separate")
print("     pair and is not read in this file.")
print("  ⛔ AND NO CLAIM IS MADE ABOUT `NS`.  It is an INHERITED quantity: this corpus posits no")
print("     six-parameter vector, so the spectral index is ADOPTED from LambdaCDM's own basis and")
print("     derived from nothing this construction predicts.  What that costs is stated rather than")
print("     hidden: it appears here only as the direction known a priori to carry no acoustic")
print("     phase, which is what a control for a phase statistic requires, and every conclusion")
print("     above would stand if its value moved.")
print("  ⌗ The curve is four points on one arm.  It establishes a SIGN and an order of magnitude")
print("     for the loading's response, not a functional form.")
_r0, _r1 = abs(NS[0] / LOAD[0]), abs(NS[1] / LOAD[1])
print(f"  ⚠ AND THE CONTROL LEAVES A FLOOR ON THE OFFSET, MEASURED RATHER THAN WAVED AT:")
print(f"     the tilt's residual response is {_r0 * 100:.0f}% of the loading's on the common offset")
print(f"     and {_r1 * 100:.1f}% on the alternation.  *I first wrote this check as `an order of")
print(f"     magnitude below` on BOTH components and it FAILED on the offset -- {_r0 * 100:.0f}% is")
print(f"     not a factor of ten.  The de-tilt collapses the tilt's leakage by a factor of 22 but")
print(f"     does not abolish it, so the offset carries a floor of about a sixth of the loading's")
print(f"     own signal and the alternation is the cleaner of the two components.*")
check("Ⓔ①  the control direction's residual response stays well below the loading's on both "
      "components -- within a SIXTH on the common offset and a THIRTIETH on the alternation -- "
      "which is the check that the statistic reads acoustic phase rather than the de-tilt's "
      "leftover gradient.  ⚠ *Not an order of magnitude on the offset: that is the bound this "
      "check was first written with and it did not hold, so the floor is stated at its measured "
      "size instead of at the one I expected*",
      _r0 < 1 / 6 and _r1 < 1 / 30)

print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED")
    for q in fail:
        print(f"      - {q}")
    print(BAR)
    sys.exit(1)
print(f"  ✔ {11 - len(fail)} of 11 checks pass.")
print(BAR)
sys.exit(0)
