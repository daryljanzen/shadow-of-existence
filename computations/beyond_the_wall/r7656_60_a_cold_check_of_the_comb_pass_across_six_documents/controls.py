#!/usr/bin/env python3
"""r7656+60.3 (60) -- THE MATCHER'S OWN REACH, measured before its 95-of-95 is reported.

⛔ THE PROBLEM, STATED BEFORE IT WAS MEASURED.  `cold_check.py` searches ONE HUNDRED receipts' stdout
for any number within half a unit of the target's last printed digit.  For a two-significant-digit
figure the chance that SOME number in a hundred outputs lands inside that window is high WHATEVER THE
CORPUS SAYS -- so a 95-of-95 is exactly what a matcher with no discriminating power returns.

⌗ *A guard that cannot fail on the data it is given is not a guard.  The way to find out is a negative
control, not a re-reading.*

TWO CONTROLS, both registered at `+60.3` before this file existed:
  ⑪⑫⑬  DECOYS -- every real figure moved WELL OUTSIDE its own tolerance, magnitude and digit count
        kept, run through the SAME matcher against the SAME bank.  Threshold fixed in advance: a decoy
        rate above 20% means the matcher is the result and not the corpus.
  ⑭     MULTIPLICITY -- how many of the hundred receipts produce each figure independently.  One is a
        located figure; forty is a coincidence of the window.

⛔ AND THE CONTROL FIRED: 41.1% against a threshold of 20%.  `r7656+60.4` therefore registered the
tightening BELOW, before the number it would produce was seen:
  ⑮     VERBATIM FIRST -- a figure counts as reproduced only when the receipt's output carries THAT
        STRING, extracted by the same `check_figures_pinned.figures` on both sides, with NO tolerance
        window at all.  Tolerance-only matches are reported separately as WITHIN THE PRINTED DIGIT,
        which is a weaker finding and is labelled as one.
  ⑯     AND ITS OWN DECOY RATE IS MEASURED under the SAME 20% threshold, which is the one already
        registered at `+60.3` and is NOT moved now that a number has been seen.
  ⑰     THE REACHABLE NEGATIVE OF THAT AMENDMENT is that verbatim matching is ALSO too loose, and it
        is registered against: if ⑯ fires, this revision reports that the order's question cannot be
        answered by figure-matching against banked stdout at all, and says what would answer it.
"""
import json
import os
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
RUNS = os.path.join(HERE, 'runs')
sys.path.insert(0, os.path.join(ROOT, 'corpus'))
import check_figures_pinned as G                                           # noqa: E402

_fail = []


def check(label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        _fail.append(label)


S = json.load(open(os.path.join(HERE, 'sites.json')))
SITES, CANDS = S['sites'], S['candidates']
STATE = {r['receipt']: r['state'] for r in json.load(open(os.path.join(HERE, 'runs.json')))}
RAN = [n for n in CANDS if STATE.get(n) == 'RAN']

OUTFIGS = {}
for name in CANDS:
    p = os.path.join(RUNS, name[:120] + '.txt')
    txt = open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''
    OUTFIGS[name] = {s for s, _ in G.figures(txt)}


def allow(s):
    dec = len(s.split('.')[1]) if '.' in s else 0
    half = 0.5 * 10 ** (-dec)
    try:
        return max(half, 0.0005 * abs(float(s)))
    except ValueError:
        return half


def hits(fig):
    """which receipts that RAN produce this figure, through the same rule cold_check uses"""
    try:
        want, tol = float(fig), allow(fig)
    except ValueError:
        return []
    out = []
    for n in RAN:
        if fig in OUTFIGS[n]:
            out.append(n)
            continue
        for s in OUTFIGS[n]:
            try:
                if abs(float(s) - want) <= tol:
                    out.append(n)
                    break
            except ValueError:
                continue
    return out


def hits_verbatim(fig):
    """⑮ which receipts that RAN print THIS STRING -- no window, no rounding, no float at all.

    ⌗ The same extractor runs on both sides, so this is not a grep: the receipt's stdout is reduced
    to the set of figures the GATE would see in it, and the paper's figure has to be one of them
    character for character.
    """
    return [n for n in RAN if fig in OUTFIGS[n]]


def decoy(fig):
    """move it WELL outside its own tolerance, keeping magnitude and digit count.

    ⌗ The shift is 40 times the figure's own allowance -- far outside any rounding reading of it --
    and the decoy is re-rendered with the SAME number of decimals, so it is a figure of exactly the
    shape of a real one that the corpus should not carry at that site.
    """
    try:
        x = float(fig)
    except ValueError:
        return None
    dec = len(fig.split('.')[1]) if '.' in fig else 0
    d = x + 40.0 * allow(fig)
    s = f"{d:.{dec}f}"
    return None if s == fig else s


print(__doc__)
print("=" * 112)
print("  r7656+60.3 -- the matcher's reach: decoys and multiplicity")
print("=" * 112)

FIGS = [f for s in SITES for f in s['figures']]
print(f"\n  {len(FIGS)} real figure(s) over {len(RAN)} receipt(s) that ran")

# ---------------------------------------------------------------- ⑭ multiplicity
mult = {f: len(hits(f)) for f in sorted(set(FIGS))}
per = [mult[f] for f in FIGS]
med = statistics.median(per)
print(f"\nⓐ  ⑭ MULTIPLICITY -- how many of the {len(RAN)} receipts produce each figure independently")
print(f"      median {med:.0f}   mean {statistics.mean(per):.1f}   min {min(per)}   max {max(per)}")
_one = [f for f in sorted(set(FIGS)) if mult[f] == 1]
_many = [f for f in sorted(set(FIGS)) if mult[f] >= 20]
print(f"      produced by exactly ONE receipt: {len(_one)} distinct figure(s)  {_one[:10]}")
print(f"      produced by TWENTY OR MORE:      {len(_many)} distinct figure(s)  {_many[:10]}")

# ---------------------------------------------------------------- ⑪⑫⑬ decoys
print(f"\nⓑ  ⑪ DECOYS -- each real figure moved 40x its own allowance, same digit count")
dec_rows = []
for f in FIGS:
    d = decoy(f)
    if d is None:
        continue
    dec_rows.append((f, d, len(hits(d))))
nd = len(dec_rows)
nhit = sum(1 for _f, _d, h in dec_rows if h > 0)
rate = nhit / nd if nd else 0.0
print(f"      {nd} decoy(s) built; {nhit} of them ALSO 'reproduce' -> false-positive rate "
      f"{rate*100:.1f}%")
print(f"\n      {'real':>10} {'decoy':>10} {'receipts hit':>13}")
for f, d, h in dec_rows[:14]:
    print(f"      {f:>10} {d:>10} {h:>13}")
if nd > 14:
    print(f"      ... and {nd-14} more")

# ---------------------------------------------------------------- ⑮⑯⑰ verbatim first
print(f"\nⓒ  ⑮ VERBATIM FIRST -- the same figure STRING on both sides, no tolerance window at all")
vb_rows = [(f, hits_verbatim(f)) for f in FIGS]
n_vb = sum(1 for _f, h in vb_rows if h)
tol_only = [f for f, h in vb_rows if not h and hits(f)]
n_none = sum(1 for f, h in vb_rows if not h and not hits(f))
print(f"      of {len(FIGS)} figure(s): VERBATIM {n_vb}   WITHIN THE PRINTED DIGIT {len(tol_only)}   "
      f"NEITHER {n_none}")
print(f"      ⌗ the {len(tol_only)} tolerance-only match(es) are a WEAKER finding and are NOT folded "
      f"into the headline:")
for f in sorted(set(tol_only))[:16]:
    print(f"         {f}  -- a receipt prints a number inside the gate's allowance; none prints it")
if len(set(tol_only)) > 16:
    print(f"         ... and {len(set(tol_only))-16} more distinct")

vmult = {f: len(hits_verbatim(f)) for f in sorted(set(FIGS))}
vper = [vmult[f] for f in FIGS if vmult[f]]
if vper:
    print(f"      multiplicity among the verbatim ones: median {statistics.median(vper):.0f}   "
          f"mean {statistics.mean(vper):.1f}   max {max(vper)}")

print(f"\nⓓ  ⑯ THE VERBATIM MATCHER'S OWN DECOY RATE, under the threshold registered at +60.3")
vdec = [(f, d, len(hits_verbatim(d))) for f, d, _h in dec_rows]
vnhit = sum(1 for _f, _d, h in vdec if h > 0)
vrate = vnhit / len(vdec) if vdec else 0.0
print(f"      {len(vdec)} decoy(s), the SAME ones; {vnhit} of them are printed verbatim somewhere "
      f"-> false-positive rate {vrate*100:.1f}%")
if vnhit:
    print(f"\n      {'real':>10} {'decoy':>10} {'receipts hit':>13}")
    for f, d, h in [r for r in vdec if r[2] > 0][:14]:
        print(f"      {f:>10} {d:>10} {h:>13}")
print(f"      ⌗ a decoy that is ITSELF a figure the corpus carries elsewhere is this instrument's "
      f"irreducible floor: a shift of 40 allowances lands on a round number often enough.")

print(f"""
  ⌗ ⑬ THE RATE IS PUBLISHED EITHER WAY, with the decoys themselves, because a cold check that
  reported its hit rate without its false-positive rate would be asking to be believed rather than
  checked.""")

# ⌗ ⑫ IS SCORED, NOT HIDDEN.  It was registered at `+60.3` with its threshold and it FAILED at
# `+60.4`; the record keeps the failing condition printed with the number that broke it, separately
# from the conditions this revision still stands on, because a miss folded into a pass is a lie about
# what was asked.
_miss = []
if not rate <= 0.20:
    _miss.append(f"⑫ THE REGISTERED THRESHOLD -- the tolerance matcher's decoy rate is at or below "
                 f"20% -- MEASURED {rate*100:.1f}%, scored a MISS at +60.4.  The 95-of-95 was the "
                 f"width of the window and not the corpus.")
print(f"\n  [MISS] {_miss[0] if _miss else ''}" if _miss else
      f"\n  [PASS] ⑫ the tolerance matcher's decoy rate is {rate*100:.1f}%")

print("\n  THE CONDITIONS THIS REVISION STANDS ON, after the tightening registered at +60.4:")
check(f"⑯ THE VERBATIM MATCHER'S OWN DECOY RATE is at or below the SAME 20% registered at +60.3 "
      f"({vrate*100:.1f}%) -- the threshold was NOT moved once a number had been seen, so a verbatim "
      f"reproduction is a statement about the corpus and not about this matcher's reach",
      vrate <= 0.20)
check(f"⑮ and the tightening DOES WORK rather than relabel the same set: {len(tol_only)} "
      f"figure(s) that 'reproduced' under the window do NOT reproduce verbatim, and they are reported "
      f"as WITHIN THE PRINTED DIGIT instead of in the headline", len(tol_only) >= 1)
check(f"⑭ and the median figure is produced by a SMALL number of the {len(RAN)} receipts "
      f"({med:.0f}), so a reproduction locates a figure rather than finding it everywhere",
      med <= 10)
check(f"⑮ and the verbatim multiplicity is SMALLER still (median "
      f"{statistics.median(vper) if vper else 0:.0f}), which is what a located figure looks like",
      bool(vper) and statistics.median(vper) <= 4)

print(f"""
  ⌗ ⑰ THE REACHABLE NEGATIVE OF `+60.4` IS REGISTERED AGAINST AND WAS LIVE UNTIL THE NUMBER
  ABOVE.  Had the verbatim rate come in over 20% as well, this revision's answer to the order would
  be that the question is NOT measurable by figure-matching against banked stdout at all, and that
  what would answer it instead is each comb-pass receipt's own banked artefact -- the arrays it
  writes, compared field by field against the paper's table -- rather than its printed text.""")

print("\n" + "=" * 112)
for m in _miss:
    print("   [MISS] " + m)
print(f"  {len(_fail)} failure(s) among the conditions this revision stands on")
for f in _fail:
    print("   [FAIL] " + f)

json.dump(dict(decoys=nd, decoy_hits=nhit, decoy_rate=round(rate, 4),
               verbatim_decoys=len(vdec), verbatim_decoy_hits=vnhit,
               verbatim_decoy_rate=round(vrate, 4),
               verbatim=n_vb, within_printed_digit=len(tol_only), neither=n_none,
               tolerance_only_figures=sorted(set(tol_only)),
               median_multiplicity=med, mean_multiplicity=round(statistics.mean(per), 2),
               one_receipt_only=_one, twenty_or_more=_many,
               rows=[dict(real=f, decoy=d, hits=h) for f, d, h in dec_rows],
               scored_miss=_miss, live_failures=_fail),
          open(os.path.join(HERE, 'controls.json'), 'w'), indent=1)
sys.exit(1 if len(_fail) > 0 else 0)
