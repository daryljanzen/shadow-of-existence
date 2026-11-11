#!/usr/bin/env python3
"""`r7741` ** THE `g`/`chi` DIVISION OF THE LOCATED STEP IS SET BY A GRID MATCHING NOTHING FIXES, SO THE
DISTANCE RATIO IS THE ONLY ATTRIBUTION THE ARMS' OWN ARRAYS DETERMINE. **

The acceptance law reads this arm's visibility `g` as a function of the comoving distance `chi`, and the
two arms' quantities live on DIFFERENT conformal-time grids.  Reading one arm's `g` against the other
arm's `chi` therefore requires MATCHING the two grids, and nothing in the theory fixes the matching.

⛭ ** WHAT IS MEASURED HERE IS A ONE-PARAMETER FAMILY OF MATCHINGS, NOT TWO RIVAL CHOICES. **  A matching
is parametrised by the scalar `ratio` that rescales the borrowed `chi` map about the visibility peak.
`ratio = 1.0` is the identity, so it is exactly 70's own index matching -- asserted below at `0`, in both
directions, rather than argued.  Across `ratio = 1.000` to `1.155`, the span the two arms actually
differ by, the distance map's share of the `l`-varying variance falls `95.06 -> 58.41 -> 26.70 -> 7.10`
per cent and the visibility's rises to meet it, strictly monotonically, crossing near `1.07`.

⇒ *** At one member of the family NEITHER quantity carries three fifths of it.  So the division is not
merely convention-dependent: it passes continuously through a regime in which the question has no
answer, driven by a scalar the physics does not fix. ***

⛭ ** WHAT SURVIVES IS WHAT NEEDS NO MATCHING. **  `r7733`'s `93.6` per cent is read on `r7729`'s four
arrays, whose cross term scales the SOURCE arm's OWN `x0` by a scalar, so no `eta` grid of one arm ever
meets the other's.  It is constant along this whole family by construction.  ⇒ *The distance ratio is
the attribution these arrays determine; any finer division between `g` and `chi` is a choice.*

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM. **
 * ** Not that 70's index matching is wrong. ** It is declared, reasoned, and its own author flagged the
   consequence first (`r7737+70.1`).  What is wrong is reading a `g`/`chi` attribution off any single
   member of the family without saying it is one.
 * ** Not that the acceptance law's prose needs changing. ** `P15` speaks of the visibility being
   `15.5` per cent wider IN `chi` -- the visibility read as a function of `chi`, with no `g`/`chi` split
   in it.  69 ruled at `r7741` that the law's prose stands, and this receipt does not reopen it.
 * ** Not that a matching-independent finer split is impossible in principle ** -- only that it would
   have to be CONSTANT along this family, and that nothing finer than the distance-ratio decomposition
   is.  The `rs` leg is nearly so (`0.66`-`0.77` per cent) and is reported, not claimed.
 * ** Nothing here is a null test or a significance. ** Every number is a variance share.

COMPUTES: scope.
 * ** THE INPUT IS A COMMITTED ARTEFACT, AND THE `G` BUILDS ARE UPSTREAM OF IT. **  Each member of the
   family costs two `G_l(k)` builds at about `33` minutes -- `698` multipoles x `1450` wavenumbers x
   `560` nodes of `spherical_jn` -- so the family is some four hours and cannot run in a receipt's
   budget, and 70's arrays live at a `refs/ci` ref in a scratchpad rather than in the tree.
   `computations/beyond_the_wall/r7741_cc66_the_pairing_continuum/build_continuum.py` reduced them to
   the `l`-vectors the verdict is read off (`89 436` bytes) and recorded every input's sha256, which
   this receipt asserts before computing anything.
   ⛔ *So this receipt verifies the REDUCTION -- every share, ratio, monotonicity and crossing below is
   recomputed here from those vectors, and the `ratio = 1.0` identity is recomputed from the maps
   themselves at full precision.  It does NOT re-derive the `G` builds.  Said plainly because a receipt
   that reduces a committed array can look as though it verified the array.*
 * ** NO `PREDICTION.md` GOVERNS `r7741`, AND THAT IS DELIBERATE. **  Every figure here was measured,
   reported and MERGED at `r7739+cc66.2`-`.8` before `r7741` was written; this revision pins published
   numbers and drafts prose for them, so there is nothing left to fit.  The registration that governs
   these figures is `r7739`'s own `PREDICTION.md`, whose second row fired.
 * NOTHING IS FITTED anywhere in this receipt, and no cosmological parameter is read.
 * ** COST, MEASURED ALONE ON THIS CONTAINER AND NOT ESTIMATED: see the run record; the arithmetic is
   `l`-vector reductions over `698` points, so it is seconds, and this receipt is NOT declared long. **
"""
import hashlib
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
ART = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                   'r7741_cc66_the_pairing_continuum', 'r7741_continuum.npz')
TEXP = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')

# the shas `build_continuum.py` recorded for 70's two handed-over artefacts
SHA_70 = {
    'r7737_grid.npz': '546977c4f05f2cffb4299900586f5a6d3ab452f561b13f9272a24bdab7dc7305',
    'r7737_vis.npz': 'c3da5390680d86b2f9dddcae3738a01e88974545b1a5d1ea4c36a2739ceb6ba4',
}
ART_SHA = 'f793acc2c466ba352c2df4313a32c48627b4bf458d3b047dfc943d8efcd2c03c'

FAILS = []


def check(label, ok, witness=''):
    tag = 'PASS' if ok else 'FAIL'
    if not ok:
        FAILS.append(label.split('**')[0].strip()[:60])
    print(f"    [{tag}] {label}")
    if witness:
        print(f"             {witness}")


def lrms(x):
    """the fit-free l-structured rms: `r7737`'s own statistic, no amplitudes anywhere"""
    x = np.asarray(x, float)
    return float(np.sqrt(((x - x.mean()) ** 2).mean()))


print("=" * 100)
print(__doc__)
print("=" * 100)

# ------------------------------------------------------------------ 1 provenance
h = hashlib.sha256(open(ART, 'rb').read()).hexdigest()
check("⛭ `r7741` ** ① THE COMMITTED ARTEFACT IS THE ONE BUILT FROM 70's RECORDED ARRAYS ** ⇒ *its own "
      "sha256 is asserted here, and it carries the sha256 of every input it was reduced from, so the "
      "chain from 70's `refs/ci` artefacts to these vectors is checkable without them being in the tree*",
      h == ART_SHA, f"artefact sha256 {h}")

Z = np.load(ART, allow_pickle=True)
recorded = {}
for line in [str(s) for s in Z['input_sha']]:
    f, s = line.split('=', 1)
    recorded[f] = s
check("⛭ `r7741` ** ② AND 70's TWO ARTEFACTS ARE THE OBJECTS 70 RECORDED ** ⇒ *the same two sha256s "
      "`r7739` asserted, so this receipt and the merged verdict read the same arrays*",
      all(recorded.get(f) == s for f, s in SHA_70.items()),
      "; ".join(f"{f} {'ok' if recorded.get(f) == s else 'MISMATCH'}" for f, s in SHA_70.items()))

# ------------------------------------------------------------------ 2 the family, and P1 inside it
x0 = {'lcdm': Z['x0_lcdm'], 'cr': Z['x0_cr']}
vis = {'lcdm': Z['vis_lcdm'], 'cr': Z['vis_cr']}


def rescale(src, brw, ratio):
    """the borrowed map, pivoted at the visibility peak, its spread rescaled by `ratio`"""
    x = x0[brw]
    piv = x[np.argmax(vis[src])]
    return piv + (x - piv) / ratio


d1 = max(float(np.abs(rescale('lcdm', 'cr', 1.0) - x0['cr']).max()),
         float(np.abs(rescale('cr', 'lcdm', 1.0) - x0['lcdm']).max()))
check("⛔ `r7741` ** ③ 70's INDEX MATCHING IS THE `ratio = 1.0` MEMBER OF THE FAMILY, EXACTLY ** ⇒ *this "
      "is what makes the four readings FOUR POINTS ON ONE CURVE rather than two rival conventions, and "
      "it is the claim the drafted sentence rests on, so it is asserted at zero and not argued*",
      d1 == 0.0, f"max abs deviation over both directions {d1:.3e}, required exactly 0")

RATIOS = {'P1': 1.0, 'grid_span': float(Z['ratio__grid_span']),
          'sigma_(mine)': float(Z['ratio__sigma_(mine)']), '70s_W': float(Z['ratio__70s_W'])}
check("⛭ `r7741` ** ④ THE FAMILY'S THREE NON-TRIVIAL SCALARS ARE THE SPANS THE ARRAYS THEMSELVES OFFER ** "
      "⇒ *the grid span, the g-weighted sigma in `chi`, and 70's own declared `W`; bracketed rather "
      "than picked, because the `span over the visibility's support` has no unique definition here*",
      abs(RATIOS['grid_span'] - 1.060251) < 5e-7
      and abs(RATIOS['sigma_(mine)'] - 1.104473) < 5e-7
      and abs(RATIOS['70s_W'] - 1.155482) < 5e-7,
      f"{RATIOS['grid_span']:.6f}, {RATIOS['sigma_(mine)']:.6f}, {RATIOS['70s_W']:.6f}")

# ------------------------------------------------------------------ 3 the shares
lc = np.log(Z['A_base'])
u_r = np.log(Z['A_rs']) - lc
SH = {}
for key in RATIOS:
    u_g = np.log(Z[f'A_g__{key}']) - lc
    u_x = np.log(Z[f'A_x__{key}']) - lc
    s = {'g': lrms(u_g), 'x': lrms(u_x), 'r': lrms(u_r)}
    t = sum(s.values())
    SH[key] = {n: v / t for n, v in s.items()}

print("\n      the curve, recomputed here from the committed vectors:")
for key, r in RATIOS.items():
    print(f"          ratio {r:.6f}   chi {100 * SH[key]['x']:6.2f} %   "
          f"g {100 * SH[key]['g']:6.2f} %   rs {100 * SH[key]['r']:5.2f} %")

check("⛭⛔ `r7741` ** ⑤ THE DISTANCE MAP'S SHARE OF THE `l`-VARYING VARIANCE FALLS `95.06`, `58.41`, "
      "`26.70`, `7.10` PER CENT ACROSS THE FAMILY ** ⇒ *the printed range: from about nineteen "
      "twentieths down to about one fourteenth, which is the figure the drafted sentence states*",
      abs(100 * SH['P1']['x'] - 95.06) < 5e-3
      and abs(100 * SH['grid_span']['x'] - 58.41) < 5e-3
      and abs(100 * SH['sigma_(mine)']['x'] - 26.70) < 5e-3
      and abs(100 * SH['70s_W']['x'] - 7.10) < 5e-3,
      f"{100 * SH['P1']['x']:.2f}, {100 * SH['grid_span']['x']:.2f}, "
      f"{100 * SH['sigma_(mine)']['x']:.2f}, {100 * SH['70s_W']['x']:.2f}")

check("⛭⛔ `r7741` ** ⑥ AND THE VISIBILITY'S SHARE RISES TO MEET IT: `4.23`, `40.81`, `72.52`, `92.24` "
      "PER CENT ** ⇒ *so the division does not merely shift, it INVERTS -- each quantity in turn takes "
      "the overwhelming majority of the structure, under matchings nothing distinguishes*",
      abs(100 * SH['P1']['g'] - 4.23) < 5e-3
      and abs(100 * SH['grid_span']['g'] - 40.81) < 5e-3
      and abs(100 * SH['sigma_(mine)']['g'] - 72.52) < 5e-3
      and abs(100 * SH['70s_W']['g'] - 92.24) < 5e-3,
      f"{100 * SH['P1']['g']:.2f}, {100 * SH['grid_span']['g']:.2f}, "
      f"{100 * SH['sigma_(mine)']['g']:.2f}, {100 * SH['70s_W']['g']:.2f}")

order = sorted(RATIOS, key=RATIOS.get)
xs_ = [SH[k]['x'] for k in order]
gs_ = [SH[k]['g'] for k in order]
check("⛭ `r7741` ** ⑦ STRICTLY MONOTONE IN THE MATCHING SCALAR, IN BOTH LEGS AND IN OPPOSITE "
      "DIRECTIONS ** ⇒ *a monotone dependence on an unfixed scalar is what makes this a CONTINUUM and "
      "not a disagreement between two readings; the direction was registered at `r7739` as a "
      "falsifiable expectation BEFORE the two outer members were built*",
      all(xs_[i] > xs_[i + 1] for i in range(3)) and all(gs_[i] < gs_[i + 1] for i in range(3)),
      f"chi {' > '.join(f'{100 * v:.2f}' for v in xs_)};  g {' < '.join(f'{100 * v:.2f}' for v in gs_)}")

check("⛔ `r7741` ** ⑧ AT THE `grid span` MEMBER NEITHER QUANTITY CARRIES THREE FIFTHS OF THE STRUCTURE ** "
      "⇒ *** the regime where the question has NO answer, which is the strongest form of the finding: "
      "the curve does not jump between two attributions, it passes through having neither ***",
      SH['grid_span']['x'] < 0.60 and SH['grid_span']['g'] < 0.60,
      f"chi {SH['grid_span']['x']:.4f} and g {SH['grid_span']['g']:.4f}, both below 0.60")

lo, hi = RATIOS['grid_span'], RATIOS['sigma_(mine)']
check("⛭ `r7741` ** ⑨ THE TWO LEGS CROSS INSIDE THE FAMILY, BETWEEN `1.060` AND `1.105` ** ⇒ *the "
      "crossing is bracketed by two measured members rather than interpolated to a value, because the "
      "curve is sampled at four points and a crossing read off four points is a bracket*",
      (SH['grid_span']['x'] - SH['grid_span']['g']) > 0
      > (SH['sigma_(mine)']['x'] - SH['sigma_(mine)']['g']),
      f"chi-g is {SH['grid_span']['x'] - SH['grid_span']['g']:+.4f} at {lo:.6f} and "
      f"{SH['sigma_(mine)']['x'] - SH['sigma_(mine)']['g']:+.4f} at {hi:.6f}")

rr = [SH[k]['r'] for k in order]
check("⛭ `r7741` ** ⑩ THE COMB PERIOD'S SHARE IS NEARLY CONSTANT ALONG THE FAMILY, `0.66`-`0.77` PER "
      "CENT ** ⇒ *reported because the ruling turns on what is CONSTANT along the curve: this leg "
      "nearly is, and is small; the distance-ratio decomposition exactly is. Neither is a claim that "
      "the `rs` leg is matching-free -- it is a measured near-constancy*",
      abs(100 * min(rr) - 0.66) < 5e-3 and abs(100 * max(rr) - 0.77) < 5e-3,
      f"min {100 * min(rr):.2f} %, max {100 * max(rr):.2f} %")

# ------------------------------------------------------------------ 4 why the scalar leg cannot stand in
xsc = float(Z['xs'])
u_n = np.log(Z['A_norm']) - lc
u_n_scaled = np.log(Z['A_norm_rs_scaled']) - lc
collapse = lrms(u_n_scaled) / lrms(u_n)
check("⛭⛔ `r7741` ** ⑪ A PURE SCALAR STRETCH OF THE MAP IS NEARLY INVISIBLE TO THIS NORMALISED "
      "ACCEPTANCE RATIO, AND THE MECHANISM IS ASSERTED RATHER THAN ARGUED ** ⇒ *`A_l` is divided by its "
      "own integral, so a pure rescaling of `chi` is a reparametrisation of wavenumber that CANCELS in "
      "the ratio, leaving only its mismatch against the comb phase, which does not rescale. Scale the "
      "comb period by the same scalar and the leg collapses to round-off.* ⛔ *This is why the scalar "
      "term that carries `98.3` per cent of the UN-NORMALISED ladder's distance leg cannot be read "
      "across to this object, and why no substitute on this arm can speak for that one.*",
      collapse < 1e-3 and abs(xsc - 1.0128706133) < 5e-10,
      f"collapse factor {collapse:.3e} (required < 1e-3), xs {xsc:.10f}")

# ------------------------------------------------------------------ 5 the clause this must sit beside
TEX = open(TEXP, encoding='utf-8').read()
_ANCHOR = 'the distance ratio carries $93.6$ per cent'
_RATIO_NAME = "the ratio of the two arms' distances to last scattering"
check("⛭⛔ `r7741` ** ⑫ AND THE CLAUSE THIS ONE REFINES IS STILL IN THE PAPER: THE `93.6` PER CENT AND "
      "THE DISTANCE-RATIO NAMING ** ⇒ *the drafted sentence says the finer division is unfixed WHILE "
      "that figure stands; if the `93.6` per cent clause leaves `P15`, this sentence loses the thing it "
      "is a qualification of and has to be written again rather than inherited*",
      _ANCHOR in TEX and _RATIO_NAME in TEX,
      f"93.6 clause present {_ANCHOR in TEX}, distance-ratio naming present {_RATIO_NAME in TEX}")

print("\n" + "=" * 100)
print(f"  {'OK  ' if not FAILS else 'FAIL'}  {12 - len(FAILS)} of 12 gates;  "
      f"{len(FAILS)} failure(s)" + ("" if not FAILS else ": " + "; ".join(FAILS[:2])))
print("=" * 100)
sys.exit(1 if FAILS else 0)
