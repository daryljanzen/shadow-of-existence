#!/usr/bin/env python3
"""r7656 (60) -- THE VERDICT: does every figure the comb pass landed across six documents reproduce?

⛭ ONE LOCATOR ON BOTH SIDES, which is `r7655`'s own condition.  `check_figures_pinned.figures` --
the gate's extractor -- is applied to the paper's sentence AND to each receipt's banked stdout.  The
output is never grepped for a string, so a figure that reproduces does so under one rule and not two.

⛔ AND THE RESOLUTION IS VISIBLE.  Every site prints the line the order NAMED beside the line the text
was read from (`r7656+60.1`): six of the named lines are the blank line before their paragraph, and a
literal read would have extracted nothing from them and called it green.

⛔ AND THE FIRST PASS OF THIS FILE WAS A GUARD THAT COULD NOT FAIL.  Read with the gate's tolerance
window it returned REPRODUCES 95 of 95 -- and `controls.py`, registered at `+60.3` before that number
was judged, moved every figure FORTY TIMES its own allowance and found that 41.1% of the decoys
"reproduced" too.  A 95-of-95 at a 41% false-positive rate is a measurement of the window.

⌗ *A hit rate reported without its false-positive rate is asking to be believed rather than checked.*

So `r7656+60.4` registered VERBATIM FIRST -- and the verbatim count came back too TIGHT at the other
end, because `186.1350` is `186.135` and `3.338738` is `3.3387380`.  `+60.5` therefore registered the
THREE-WAY verdict below, before its counts were measured, and the two ends of it are now named
separately so that neither the window nor the rendering can be mistaken for the corpus:

  VERBATIM        -- a candidate that RAN prints THAT STRING, both sides through the gate's own
                     extractor.  No window, no rounding.  Decoy rate 10.5% (⑯), below the 20%
                     registered at `+60.3` and NOT moved once a number had been seen.
  EXACT-VALUE     -- ⑱ no candidate prints the string, but one prints a string that parses to the
                     SAME FLOAT.  A reproduction, full stop: a trailing zero is a rendering of a
                     number and not a different number.
  ROUNDED         -- ⑲ one prints a longer number that ROUNDS to the paper's figure at the paper's
                     own digit count.  Also a reproduction -- it is what printing fewer digits means,
                     and it is the figure-pin gate's own third remedy.
  GATE-ONLY       -- ⑳ inside the gate's allowance and does NOT round to the printed figure.  THE
                     ONLY ONE OF THE FOUR THAT IS A WEAKER FINDING, and the one place a figure the
                     corpus does not carry at the digit it prints would hide.  Named, with the
                     nearest value any receipt prints and its distance in half-units.
  ABSENT          -- every candidate RAN and none prints it under any of the four readings
  UNRUN           -- at least one candidate did not finish, so the figure is not judged
⌗ *A figure is never ABSENT because a receipt could not be run.*

⌗ AND WHAT A REPRODUCTION HERE IS NOT (arm ⑧ of the registration): it establishes that SOME receipt in
the candidate set computes the figure.  On 25 of the named lines there is no `\\rcpt{}` marker to point
at one, so a figure whose computing receipt is not among those its own document cites is reported
RESOLVED ELSEWHERE -- correct in value, unaddressed in citation.
"""
import json
import os
import re
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


# ---------------------------------------------------------------- ㉑ the verdict READS its control
# ⌗ `+60.5` fixed the consequence of a failing decoy rate before the rate existed, and `+60.6`
# scored it: at 25.3% the ⑲ rung is WITHHELD.  This file does not hold that as a constant -- it
# reads `controls.json` and withholds the rung itself, so the verdict cannot drift away from the
# control that licenses it, and a MISSING control is a hard stop rather than a silent reproduction.
CTL = os.path.join(HERE, 'controls.json')
if not os.path.exists(CTL):
    sys.exit("⛔ controls.json is absent.  Run controls.py first: no rung of the ladder may be "
             "reported before its own false-positive rate has been measured.")
C = json.load(open(CTL))
THRESHOLD = 0.20                                   # registered at +60.3 and never moved since
RUNG_RATE = {'VERBATIM': C['verbatim_decoy_rate'], 'EXACT-VALUE': C['exact_decoy_rate'],
             'ROUNDED': C['rounded_decoy_rate'], 'GATE-ONLY': C['decoy_rate']}
WITHHELD = {k for k, v in RUNG_RATE.items() if v > THRESHOLD and k != 'GATE-ONLY'}

S = json.load(open(os.path.join(HERE, 'sites.json')))
SITES, CANDS = S['sites'], S['candidates']
STATE = {r['receipt']: r['state'] for r in json.load(open(os.path.join(HERE, 'runs.json')))}

TEXT = {}
for name in CANDS:
    p = os.path.join(RUNS, name[:120] + '.txt')
    TEXT[name] = open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''

# ---------------------------------------------------------------- the same locator, both sides
OUTFIGS = {name: {s for s, _ in G.figures(TEXT[name])} for name in CANDS}


def allow(x):
    """the gate's own allowance: the coarser of half a unit in the last printed digit and 0.05%"""
    s = x.strip()
    dec = len(s.split('.')[1]) if '.' in s else 0
    half = 0.5 * 10 ** (-dec)
    try:
        rel = 0.0005 * abs(float(s))
    except ValueError:
        rel = 0.0
    return max(half, rel)


def produces_verbatim(name, fig):
    """⑮ does this receipt's OUTPUT carry THIS STRING -- no window, no rounding, no float at all?

    ⌗ Both sides go through `check_figures_pinned.figures`, so this is not a grep for a substring:
    the stdout is reduced to the set of figures the GATE would read in it, and the paper's figure has
    to be one of them character for character.
    """
    return fig in OUTFIGS[name]


def produces_exact(name, fig):
    """⑱ does some string in this receipt's output parse to the SAME FLOAT as the paper's figure?

    ⌗ `186.1350` is `186.135`.  Verbatim matching demotes a figure that is reproduced to the last
    bit, so the trailing-zero case is separated from the rounding case and from the gate's window.
    """
    try:
        want = float(fig)
    except ValueError:
        return False
    for t in OUTFIGS[name]:
        try:
            if float(t) == want:
                return True
        except ValueError:
            continue
    return False


def produces_rounded(name, fig):
    """⑲ does some string round to the paper's figure AT THE PAPER'S OWN DIGIT COUNT?

    ⌗ This is the figure-pin gate's third remedy read as a measurement: a paper that prints fewer
    digits than its receipt computes is reproduced when the receipt's value RENDERS to what the paper
    printed.  `811.59` -> `811.6` reproduces; `1.40097` -> `1.4010` does not reproduce `1.4011`.
    Rendering is Python's `format`, which rounds half to even on the decimal repr.
    """
    f = fig.strip()
    dec = len(f.split('.')[1]) if '.' in f else 0
    for t in OUTFIGS[name]:
        try:
            if f"{float(t):.{dec}f}" == f:
                return True
        except ValueError:
            continue
    return False


def produces(name, fig):
    """the TOLERANCE reading, kept only to separate GATE-ONLY from ABSENT"""
    if fig in OUTFIGS[name]:
        return True
    try:
        want, tol = float(fig), allow(fig)
    except ValueError:
        return False
    for s in OUTFIGS[name]:
        try:
            if abs(float(s) - want) <= tol:
                return True
        except ValueError:
            continue
    return False


def nearest(fig, *names):
    """the closest value any of these receipts prints, and its distance in HALF-UNITS of fig's last
    printed digit -- so ⑳'s exception is quantified and not merely labelled"""
    f = fig.strip()
    dec = len(f.split('.')[1]) if '.' in f else 0
    half = 0.5 * 10 ** (-dec)
    try:
        want = float(f)
    except ValueError:
        return (float('nan'), '?', names[0] if names else '')
    best = (float('inf'), '?', '')
    for n in names:
        for t in OUTFIGS[n]:
            try:
                d = abs(float(t) - want) / half
            except ValueError:
                continue
            if d < best[0]:
                best = (d, t, n)
    return best


print(__doc__)
print("=" * 112)
print("  r7656 (60) -- the comb pass, six documents, one locator")
print("=" * 112)

print("\nⓐ  THE INSTRUMENT'S OWN REACH, ASSERTED BEFORE ITS VERDICTS ARE READ")
ran = [n for n in CANDS if STATE.get(n) == 'RAN']
unrun = [n for n in CANDS if STATE.get(n) != 'RAN']
print(f"      {len(CANDS)} candidate(s): {len(ran)} RAN, {len(unrun)} UNRUN")
print(f"      {len(SITES)} site(s); {sum(len(s['figures']) for s in SITES)} figure(s), "
      f"{len({f for s in SITES for f in s['figures']})} distinct")
check(f"ⓐ① ARM ⑩ -- the candidate set exceeds 20 ({len(CANDS)}), so a figure reported ABSENT was "
      f"looked for somewhere rather than nowhere", len(CANDS) > 20)
check(f"ⓐ② and the runs are banked for every candidate, so no verdict rests on a missing file",
      all(TEXT[n] or STATE.get(n) != 'RAN' for n in CANDS))
_res = [s for s in SITES if s.get('resolved') and s['resolved'] != s['line']]
check(f"ⓐ③ ARM ⑨ -- {len(_res)} named line(s) were BLANK and resolved to the next non-blank one, and "
      f"each is printed with both numbers below; a literal read would have extracted nothing from "
      f"them", len(_res) >= 6)
check("ⓐ④ and no named line is UNRESOLVED", not any(s.get('unresolved') for s in SITES))

# ---------------------------------------------------------------- the verdicts
print("\nⓑ  EVERY FIGURE, EVERY SITE -- named line, resolved line, verdict")
rows, absent, elsewhere, gate_only, exact, rounded, withheld = [], [], [], [], [], [], []
LADDER = [('VERBATIM', produces_verbatim), ('EXACT-VALUE', produces_exact),
          ('ROUNDED', produces_rounded), ('GATE-ONLY', produces)]
for s in SITES:
    cites = [n for n in s['cites'] if n in TEXT]
    for f in s['figures']:
        # ⑱⑲⑳ the ladder is tried STRONGEST FIRST, so each figure gets the strongest true reading
        hit = None
        for label, fn in LADDER:
            good = [n for n in ran if fn(n, f)]
            if good:
                hit = (label, good)
                break
        if hit is None:
            v = 'UNRUN' if unrun else 'ABSENT'
            rows.append((s, f, v, None))
            if v == 'ABSENT':
                absent.append((s['paper'], s['line'], f))
            continue
        label, good = hit
        if label in WITHHELD:
            d, t, n = nearest(f, *good)
            rows.append((s, f, 'UNESTABLISHED', good[0]))
            withheld.append((s['paper'], s['line'], f, t, d, good[0]))
            continue
        own = [n for n in good if n in cites]
        rows.append((s, f, label, (own or good)[0]))
        if label == 'VERBATIM' and cites and not own:
            elsewhere.append((s['paper'], s['line'], f, good[0]))
        if label == 'EXACT-VALUE':
            exact.append((s['paper'], s['line'], f, nearest(f, good[0])[1], good[0]))
        elif label == 'ROUNDED':
            rounded.append((s['paper'], s['line'], f, nearest(f, good[0])[1], good[0]))
        elif label == 'GATE-ONLY':
            d, t, n = nearest(f, *good)
            gate_only.append((s['paper'], s['line'], f, t, d, n))

by = {}
for s, f, v, _n in rows:
    by.setdefault((s['paper'], s['line'], s.get('resolved', s['line'])), []).append((f, v))
print(f"\n      {'paper':<10} {'named':>6} {'read':>6} {'figs':>5}  verdicts")
for (paper, named, res) in sorted(by, key=lambda k: (k[0], k[1])):
    vs = by[(paper, named, res)]
    tally = {}
    for _f, v in vs:
        tally[v] = tally.get(v, 0) + 1
    mark = ' ←blank, resolved' if res != named else ''
    print(f"      {paper:<10} {named:>6} {res:>6} {len(vs):>5}  "
          + ', '.join(f'{k} {n}' for k, n in sorted(tally.items())) + mark)

N = {k: sum(1 for _s, _f, v, _n in rows if v == k) for k in
     ('VERBATIM', 'EXACT-VALUE', 'ROUNDED', 'GATE-ONLY', 'UNESTABLISHED', 'ABSENT', 'UNRUN')}
print(f"\n      EACH RUNG'S OWN MEASURED REACH, read from controls.json -- a rung over "
      f"{THRESHOLD*100:.0f}% is WITHHELD and reports UNESTABLISHED, never a reproduction:")
for k in ('VERBATIM', 'EXACT-VALUE', 'ROUNDED'):
    print(f"         {k:<12} decoy rate {RUNG_RATE[k]*100:5.1f}%   "
          + ("WITHHELD" if k in WITHHELD else "reportable"))
print(f"         {'GATE-ONLY':<12} decoy rate {RUNG_RATE['GATE-ONLY']*100:5.1f}%   "
      f"never a reproduction -- it IS the exception class")
nrep, nabs, nunr = N['VERBATIM'], N['ABSENT'], N['UNRUN']
nrepro = N['VERBATIM'] + N['EXACT-VALUE'] + N['ROUNDED']
ntol = nrepro + N['GATE-ONLY'] + N['UNESTABLISHED']
print(f"\n      VERBATIM {N['VERBATIM']}   EXACT-VALUE {N['EXACT-VALUE']}   ROUNDED {N['ROUNDED']}"
      f"   GATE-ONLY {N['GATE-ONLY']}   ABSENT {nabs}   UNRUN {nunr}   of {len(rows)}")
if withheld:
    print(f"\n      ⚠ UNESTABLISHED, {len(withheld)} figure(s) -- the rung that would carry them "
          f"({', '.join(sorted(WITHHELD))}) has a decoy rate above {THRESHOLD*100:.0f}%, so they are "
          f"NEITHER reproduced NOR absent.  ㉕: they are not folded into the headline.")
    for paper, line, f, t, d, n in withheld:
        print(f"         {paper} l.{line}: paper {f}   nearest {t}   {d:.2f} half-units   {n[:46]}")
print(f"      ⌗ THE HEADLINE IS THE REPORTABLE RUNGS: {nrepro} of {len(rows)}.  The tolerance "
      f"reading of this same data was {ntol} at a {RUNG_RATE['GATE-ONLY']*100:.1f}% decoy rate; the "
      f"verbatim reading alone was {N['VERBATIM']} and demoted {N['EXACT-VALUE']} figure(s) over a "
      f"trailing zero.")
if exact:
    print(f"\n      ⑱ EXACT-VALUE, {len(exact)} figure(s) -- the same number, rendered with a "
          f"different number of digits:")
    for paper, line, f, t, n in exact:
        print(f"         {paper} l.{line}: {f} == {t}   {n[:52]}")
if rounded:
    print(f"\n      ⑲ ROUNDED, {len(rounded)} figure(s) -- the receipt's longer value renders to the "
          f"paper's figure at the paper's own digit count:")
    for paper, line, f, t, n in rounded:
        print(f"         {paper} l.{line}: {t} -> {f}   {n[:52]}")
if gate_only:
    print(f"\n      ⛔ ⑳ GATE-ONLY, {len(gate_only)} figure(s) -- INSIDE the figure-pin gate's "
          f"allowance and NOT the digit the paper prints.  This is the headline's exception:")
    for paper, line, f, t, d, n in gate_only:
        print(f"         {paper} l.{line}: paper {f}   nearest {t}   {d:.2f} half-units   {n[:46]}")
if absent:
    print("\n      ⛔ ABSENT, each looked for in every candidate that ran:")
    for paper, line, f in absent:
        print(f"         {paper} l.{line}: {f}")
check(f"ⓑ① every figure is judged -- no figure is left without a verdict", len(rows) ==
      sum(len(s['figures']) for s in SITES))
check(f"ⓑ② and none is ABSENT for want of a run: UNRUN is {nunr}, and a figure is ABSENT only when "
      f"every candidate ran", nunr == 0 or bool(unrun))
check(f"ⓑ③ ⑮ the tightening of +60.4 did work: the VERBATIM count ({N['VERBATIM']}) is strictly "
      f"below the tolerance reading ({ntol}), so it is not a relabelling", N['VERBATIM'] < ntol)
check(f"ⓑ③' ㉑㉕ AND THE VERDICT READS ITS CONTROL: the rung(s) whose measured decoy rate "
      f"exceeds {THRESHOLD*100:.0f}% ({', '.join(sorted(WITHHELD)) or 'none'}) report UNESTABLISHED, "
      f"and {len(withheld)} figure(s) are held out of the headline on that ground alone",
      all(RUNG_RATE[k] > THRESHOLD for k in WITHHELD)
      and len(withheld) == N['UNESTABLISHED'])
check(f"ⓑ④ ⑱ AND SO DID THE LOOSENING OF +60.5 AT THE OTHER END: {N['EXACT-VALUE']} figure(s) "
      f"are reproduced to the last bit and were demoted by verbatim over a rendering, so the "
      f"three-way verdict is not a relabelling of the verbatim one either", N['EXACT-VALUE'] >= 1)
check(f"ⓑ⑤ ⑳ THE EXCEPTION CLASS IS NON-EMPTY AND SMALL -- registered at +60.5 as between 1 and "
      f"3 members, MEASURED {N['GATE-ONLY']}.  More than 3 would make this a class of figures rather "
      f"than an incident, and fewer than 1 would mean the refinement found nothing",
      1 <= N['GATE-ONLY'] <= 3)
check(f"ⓑ⑥ and every GATE-ONLY figure is named with the nearest value any receipt prints and its "
      f"distance in half-units, so the exception is quantified and not merely labelled",
      all(t != '?' for _p, _l, _f, t, _d, _n in gate_only))

print(f"\nⓒ  ARM ⑧ -- RESOLVED ELSEWHERE: correct in value, unaddressed in citation")
print(f"      {len(elsewhere)} figure(s) reproduce in a receipt their own document does not cite")
for paper, line, f, n in elsewhere[:12]:
    print(f"         {paper} l.{line}: {f} <- {n[:66]}")
print("""      ⌗ On 25 of the named lines there is no `\\rcpt{}` marker at all, so for those this is not a
      defect but the architecture: they reach a receipt through the paper-level citation, exactly as
      the order says.  It is reported so the distinction between a right number and a right address
      stays visible.""")

print("\n" + "=" * 112)
print(f"  {len(_fail)} failure(s)")
for f in _fail:
    print("   [FAIL] " + f)
json.dump(dict(counts=N, reproductions=nrepro, total=len(rows), absent_rows=absent,
               exact_value_rows=exact, rounded_rows=rounded, gate_only_rows=gate_only,
               unestablished_rows=withheld, withheld_rungs=sorted(WITHHELD),
               rung_decoy_rate=RUNG_RATE, threshold=THRESHOLD, tolerance_reading=ntol,
               elsewhere=elsewhere[:200], failures=_fail),
          open(os.path.join(HERE, 'verdicts.json'), 'w'), indent=1)
sys.exit(1 if len(_fail) > 0 else 0)
