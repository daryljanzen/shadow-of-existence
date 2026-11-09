#!/usr/bin/env python3
"""`r7713+cc66` THE DENSE READING, in the registered order, written BEFORE the data exists.

⛔ This file was written and committed while the build was at 4 of 56 blocks and not one of the four
   pseudo-spectra existed, for the same reason `PREDICTION.md` was committed before a line of the
   computation: a decision rule chosen after seeing the numbers is not a decision rule.  `git log` on
   this file against the mtimes of `pseudo__S_*__K_*.npz` is the check.

ORDER, fixed by `r7713+cc66.0` and not reorderable here:

  ⓵ the dense cross-kernel CONTROL (`r7711`'s, re-run on this grid) -- if the kernel swap is inert,
    nothing below is evidence and the run stops.
  ⓶ the LOG-ADDITIVITY well-posedness test.  `Pseudo(S,K)_l = sum_k G_l^K(k)^2 S(k)^2 dk/k` is a sum
    over `k`, not a product, so additivity of the three log-ratios is NOT an identity -- it is a
    measurement of how far the source and kernel differences interact.  If it fails, verdict ⒞ and
    THE THREE VERDICTS ARE NOT STATED.
  ⓷ the three ratios' steps and significances, by `r7711`'s slide unchanged.
  ⓸ the verdict, against the table in `PREDICTION.md` and nothing else.

⚠ ONE THRESHOLD WAS NOT IN THE ORIGINAL REGISTRATION AND IS FIXED HERE, BEFORE THE DATA:
   `PREDICTION.md` says the additivity check "can fail" and that verdict ⒞ follows, but it fixes no
   number for "closely".  That gap is mine.  It is closed here, with the data still absent, as:

     the interaction residual fails the check when its OWN step, read through the same slide, is both
     at least `2` sd and at least half the own x own step in magnitude.

   The reason for that form rather than a bare tolerance: what the residual would corrupt is the
   PARTITION of the step, so the quantity that matters is the residual's step measured against the
   step being partitioned, in the same units, by the same estimator -- not the residual's typical size,
   which has no scale of its own.
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7639_cc66_P15_repoint_paper'))
import own_comb_kinds as OCK                                                 # noqa: E402

OUT = os.path.join(HERE, 'pseudo')
COMB = (('lcdm', 'lcdm'), ('cr', 'cr'), ('cr', 'lcdm'), ('lcdm', 'cr'))

SD_RESOLVED = 5.0        # `PREDICTION.md`: own x own and each difference are read against 5 sd
SD_UNRESOLVED = 2.0      # `PREDICTION.md`: "under 2 sd" is the other arm of each verdict
RESID_SD = 2.0           # fixed above, before the data
RESID_FRAC = 0.5         # fixed above, before the data


def load():
    """the four assembled spectra, or a refusal naming what is missing -- never a partial read"""
    got, missing = {}, []
    for s, kk in COMB:
        p = os.path.join(OUT, f'pseudo__S_{s}__K_{kk}.npz')
        if not os.path.exists(p):
            missing.append(os.path.basename(p))
            continue
        z = np.load(p, allow_pickle=True)
        got[f'{s}|{kk}'] = (np.asarray(z['q'], float), np.asarray(z['y'], float),
                            json.loads(str(z['meta'])))
    return got, missing


def slide(xa, ya, xc, yc, halves=(0.175, 0.25, 0.35)):
    """`r7711`'s band-RMS ratio slide, UNCHANGED -- the step is read exactly as it was read there"""
    st = OCK.own_state({'lcdm': (xc, yc), 'cr': (xa, ya)}, 'mean', 1.0)
    out = []
    for h in halves:
        cs = np.arange(0.85 + h, 3.0, 0.05)
        R = np.array([OCK._rms(st['ua'], st['oa'], c - h, c + h)
                      / OCK._rms(st['xc'], st['oc'], c - h, c + h) - 1.0 for c in cs])
        L, H = R[cs < 1.4], R[cs > 2.2]
        sd = float(np.sqrt((L.var(ddof=1) + H.var(ddof=1)) / 2))
        out.append(dict(half=h, lo=float(L.mean()), hi=float(H.mean()),
                        step=float(H.mean() - L.mean()), sd=sd,
                        in_sd=float(abs(H.mean() - L.mean()) / sd) if sd else float('nan')))
    return out


def band_step(q, v, halves=(0.175, 0.25, 0.35)):
    """the same low-band-to-high-band step and pooled scatter, for a quantity that is already a
    residual rather than a ratio of two spectra -- read by band MEAN, since a residual has no
    denominator to divide out and its sign is the thing being tested"""
    out = []
    for h in halves:
        cs = np.arange(0.85 + h, 3.0, 0.05)
        R = np.array([float(np.mean(np.interp(np.linspace(c - h, c + h, 400), q, v))) for c in cs])
        L, H = R[cs < 1.4], R[cs > 2.2]
        sd = float(np.sqrt((L.var(ddof=1) + H.var(ddof=1)) / 2))
        out.append(dict(half=h, lo=float(L.mean()), hi=float(H.mean()),
                        step=float(H.mean() - L.mean()), sd=sd,
                        in_sd=float(abs(H.mean() - L.mean()) / sd) if sd else float('nan')))
    return out


def read_at(rows):
    """⛔ CORRECTED BEFORE ANY REAL DATUM, and the correction matters more than the original rule.

    The first form of this function took the MINIMUM significance across the three half-widths, on the
    reasoning that "a plateau claim is as strong as its weakest window".  A dry run on synthetic spectra,
    made while only ONE of the four real combinations existed, showed that rule makes three of the five
    rows of the registered decision table UNREACHABLE: a planted `9` per cent kernel difference, large
    enough to move the pseudo-spectrum by `19` per cent, still reported `1.66` sd and fell to verdict ⒜.

    The fault is the recurring one: THE NARROW WINDOW'S PRECISION IS NOT THE EFFECT'S SIGNIFICANCE.  A
    narrow band averages less, so its step is smaller and its scatter larger; reading its ratio as the
    measurement is reading a property of the instrument as a property of the signal.  A `5` sd bar held
    against the least precise window is a bar no amount of real signal is guaranteed to clear.

    ⇒ What `r7711`'s obstruction 1 actually required was AGREEMENT across widths, which is a separate
      GATE and is enforced as one in `agree()` below.  The significance is read at the WIDEST registered
      half-width -- fixed a priori, because the widest window averages the most and is therefore the most
      precise BY CONSTRUCTION, not because it happened to give the largest number.
    """
    return max(rows, key=lambda r: r['half'])


def agree(rows, tol=2.0):
    """`r7711`'s obstruction 1, as the gate it always was: the step must hold the SAME SIGN at every
    registered half-width, and its magnitudes must lie within a factor of `tol`.  A ratio that fails
    this has no plateau, so it gets NO significance and is reported as disagreeing -- never a verdict."""
    st = [r['step'] for r in rows]
    mag = [abs(x) for x in st]
    if min(mag) <= 0:
        return False, 'a width gives an exactly zero step'
    if not (all(x > 0 for x in st) or all(x < 0 for x in st)):
        return False, 'the step changes sign between widths'
    if max(mag) / min(mag) > tol:
        return False, f'the magnitudes span {max(mag) / min(mag):.1f}x, over the registered {tol:.0f}x'
    return True, 'same sign at every width, magnitudes within the registered factor'


def main():
    t0 = time.time()
    got, missing = load()
    print("\n" + "=" * 100)
    print("  ⛭ `r7713+cc66` THE DENSE l DISCRIMINANT -- read in the registered order")
    print("=" * 100)
    if missing:
        print("\n  ⛔ REFUSED: the four spectra are not all present, so nothing is read.")
        for m in missing:
            print(f"       missing: {m}")
        print("\n  ⌗ This is the registered refusal, not a failure: a partial grid is the thing the")
        print("    revision exists to remove, and reading three of four would reintroduce it.")
        return 2

    n = {k: len(v[1]) for k, v in got.items()}
    print(f"\n  grid: " + ", ".join(f"{k} -> {v} l" for k, v in n.items()))

    # ⓵ ---------------------------------------------------------------- THE CONTROL, FIRST
    print("\n  ⛔ ⓵ THE DENSE CONTROL -- swapping the kernel on a FIXED source must move something")
    ctl = {}
    for s in ('lcdm', 'cr'):
        qo, yo, _ = got[f'{s}|{s}']
        other = 'cr' if s == 'lcdm' else 'lcdm'
        qx, yx, _ = got[f'{s}|{other}']
        yi = np.interp(qo, qx, yx)
        rel = np.abs(yi / yo - 1.0)
        ctl[s] = dict(median=float(np.median(rel)), max=float(rel.max()),
                      identical=bool(np.array_equal(yo, yi)))
        print(f"       source {s:5s}: own kernel vs the other's -- median |move| "
              f"{100 * ctl[s]['median']:.4f}%, max {100 * ctl[s]['max']:.4f}%"
              + ("   ⛔ BYTE-IDENTICAL" if ctl[s]['identical'] else ""))
    live = all(c['median'] > 1e-6 for c in ctl.values())
    print(f"       ⇒ the kernel swap is {'LIVE' if live else '⛔ INERT'} on the dense grid")
    if not live:
        print("\n  ⛔ STOPPED. An inert perturbation separates nothing, so no ratio below is evidence.")
        print("    This is `r7703`'s leg-B case, registered in advance at `r7711+cc66.0`.")
        json.dump(dict(control=ctl, live=False, stopped_at='control'),
                  open(os.path.join(HERE, 'analyse.json'), 'w'), indent=1)
        return 1

    # ⓶ ------------------------------------------- WELL-POSEDNESS, BEFORE ANY VERDICT IS STATED
    print("\n  ⛔ ⓶ LOG-ADDITIVITY -- NOT an identity, and reported BEFORE the three verdicts")
    qd, yd, _ = got['lcdm|lcdm']
    def on_d(key):
        q, y, _ = got[key]
        return np.interp(qd, q, y)
    lo_own = np.log(on_d('cr|cr') / yd)
    lo_ker = np.log(on_d('cr|lcdm') / yd)
    lo_src = np.log(on_d('lcdm|cr') / yd)
    resid = lo_own - (lo_ker + lo_src)
    print(f"       per-l residual over {len(qd)} l: median {np.median(resid):+.6f}, "
          f"mean {resid.mean():+.6f}, sd {resid.std(ddof=1):.6f}, max|.| {np.abs(resid).max():.6f}")
    rrows = band_step(qd, resid)
    orows = slide(*got['cr|cr'][:2], *got['lcdm|lcdm'][:2])
    print("       the residual's OWN step, by the same windows:")
    print("         half     lo          hi          step        step/sd")
    for r in rrows:
        print(f"         {r['half']:.3f}  {r['lo']:+.6f}  {r['hi']:+.6f}  "
              f"{r['step']:+.6f}  {r['in_sd']:7.2f}")
    own_step = max(abs(r['step']) for r in orows)
    rs = max(rrows, key=lambda r: abs(r['step']))
    frac = abs(rs['step']) / own_step if own_step else float('inf')
    bad = (max(r['in_sd'] for r in rrows) >= RESID_SD) and (frac >= RESID_FRAC)
    print(f"       ⇒ residual step {abs(rs['step']):.6f} is {100 * frac:.1f}% of the own x own step "
          f"{own_step:.6f}; worst significance {max(r['in_sd'] for r in rrows):.2f} sd")
    own_res = max(r['in_sd'] for r in orows if r['half'] == max(q['half'] for q in orows))
    if not bad and own_res < SD_RESOLVED:
        # ⛔ a residual comparable to a step that is itself unresolved says EVERYTHING is noise, not
        #    that the partition is sound.  Calling that "well posed" would be a statement about the
        #    residual's significance dressed up as one about the partition.
        print("       ⇒ own x own is NOT resolved, so the partition's status is NOT ESTABLISHED rather")
        print("         than well posed: there is no step here to partition.")
    print(f"       ⇒ the partition is {'⛔ NOT AVAILABLE' if bad else 'not refused by this test'} "
          f"(threshold registered in this file's header: ≥{RESID_SD:.0f} sd AND "
          f"≥{100 * RESID_FRAC:.0f}% of the own x own step)")
    if bad:
        print("\n  ⛔ VERDICT ⒞ -- WITHDRAWN. The source and kernel differences interact at the scale")
        print("    of the thing they would partition, so 'creates versus fails to cancel' is not a")
        print("    question this construction answers. ⛔ THE THREE VERDICTS ARE NOT STATED.")
        json.dump(dict(control=ctl, live=True, resid=rrows, own=orows,
                       resid_frac=frac, verdict='c_withdrawn'),
                  open(os.path.join(HERE, 'analyse.json'), 'w'), indent=1)
        print(f"\n  wall {time.time() - t0:.1f} s")
        return 0

    # ⓷ ------------------------------------------------------------------- THE THREE RATIOS
    print("\n  ⛭ ⓷ THE THREE RATIOS, by `r7711`'s slide unchanged")
    print("       ratio                                   half     lo        hi       step     step/sd")
    rows = {}
    for name, (an, cn) in (("own x own      (cr|cr)/(lcdm|lcdm)", ('cr|cr', 'lcdm|lcdm')),
                           ("kernel alone   (cr|lcdm)/(lcdm|lcdm)", ('cr|lcdm', 'lcdm|lcdm')),
                           ("source alone   (lcdm|cr)/(lcdm|lcdm)", ('lcdm|cr', 'lcdm|lcdm'))):
        rows[name] = slide(*got[an][:2], *got[cn][:2])
        for r in rows[name]:
            print(f"       {name:38s} {r['half']:.3f}  {r['lo']:+.4f}  {r['hi']:+.4f}  "
                  f"{r['step']:+.4f}  {r['in_sd']:7.2f}")
    print("\n  ⚠ the three share the denominator `Pseudo(lcdm,lcdm)`, so their scatters are correlated:")
    print("    consistent signs are NOT three confirmations and no significance is combined across them.")

    nm = list(rows)
    own, ker, src = (read_at(rows[k]) for k in nm)

    # ⛔ the agreement GATE first, per `r7711`'s obstruction 1 -- a ratio with no plateau gets no number
    print("\n  ⛔ THE AGREEMENT GATE across half-widths (`r7711`'s obstruction 1, as a gate)")
    ag = {}
    for k in nm:
        ok, why = agree(rows[k])
        ag[k] = ok
        print(f"       {k:38s} {'AGREES' if ok else '⛔ DISAGREES'} -- {why}")
    if not ag[nm[0]]:
        print("\n  ⛔ own x own HAS NO PLATEAU, so there is no step to partition and no verdict is")
        print("    stated. That is a finding about the statistic, not about the physics.")
        json.dump(dict(control=ctl, live=True, resid=rrows, resid_frac=frac, rows=rows,
                       agree=ag, verdict='no_plateau'),
                  open(os.path.join(HERE, 'analyse.json'), 'w'), indent=1)
        print(f"\n  wall {time.time() - t0:.1f} s")
        return 0

    # guard 2, registered: own x own must reach 5 sd or the estimate was wrong, not the physics
    print(f"\n  ⚠ GUARD: own x own reaches {own['in_sd']:.2f} sd at the widest registered window "
          f"(half {own['half']:.3f}; registered target {SD_RESOLVED:.0f})")
    if own['in_sd'] < SD_RESOLVED:
        print("    ⇒ the 1/sqrt(n) scaling behind the grid estimate was WRONG. That is a finding about")
        print("      the estimate, not about the physics, and is reported as such.")

    # ⓸ --------------------------------------------------------------------------- THE VERDICT
    sgn = np.sign(own['step'])
    k_res = ag[nm[1]] and ker['in_sd'] >= SD_RESOLVED
    s_res = ag[nm[2]] and src['in_sd'] >= SD_RESOLVED
    k_same = np.sign(ker['step']) == sgn and abs(ker['step']) >= 0.5 * abs(own['step'])
    s_same = np.sign(src['step']) == sgn and abs(src['step']) >= 0.5 * abs(own['step'])
    creates = k_res and k_same and (src['in_sd'] < SD_UNRESOLVED or np.sign(src['step']) != sgn)
    fails = s_res and s_same and (ker['in_sd'] < SD_UNRESOLVED or
                                  (np.sign(ker['step']) == sgn and abs(ker['step']) < abs(src['step'])))
    print("\n  ⛭ ⓸ THE VERDICT, against `PREDICTION.md`'s table and nothing else")
    if creates and not fails:
        v = 'creates'
        print("       ⇒ THE PROJECTION CREATES IT.")
    elif fails and not creates:
        v = 'fails_to_cancel'
        print("       ⇒ IT FAILS TO CANCEL.")
    elif not k_res and not s_res:
        v = 'a_unresolved'
        print("       ⇒ NEITHER ⒜ -- still unresolved, and now EXHAUSTED rather than under-sampled,")
        print("         since every integer l in the band is in this reading.")
    elif k_res and s_res and k_same and s_same:
        v = 'b_not_separable'
        print("       ⇒ NEITHER ⒝ -- not separable: both differences are resolved, both of the")
        print("         measured sign, both comparable, so they do not partition the step.")
    else:
        v = 'unlicensed'
        print("       ⛔ NO ROW OF THE TABLE IS SATISFIED, so nothing is printed as a verdict.")
        print("         The pattern is reported as measured and left uninterpreted.")
    # ⌗ the agreement gate's result goes in the RECORD too, not only in the printed output: the json is
    #   what a receipt would read, and a gate whose verdict exists only on a terminal is not recorded.
    json.dump(dict(control=ctl, live=True, resid=rrows, resid_frac=frac,
                   rows=rows, verdict=v, own_sd=own['in_sd'], own_half=own['half'],
                   agree=ag, read_at={k: read_at(rows[k])['half'] for k in nm},
                   wall_s=round(time.time() - t0, 1)),
              open(os.path.join(HERE, 'analyse.json'), 'w'), indent=1)
    print(f"\n  wall {time.time() - t0:.1f} s")
    print("=" * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main())
