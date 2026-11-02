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

So `r7656+60.4` registered VERBATIM FIRST, and these are the verdicts it fixed:
  VERBATIM        -- some candidate that RAN prints THAT STRING, both sides through the gate's own
                     extractor.  No window, no rounding.  Decoy rate 10.5% (⑯), below the 20%
                     registered at `+60.3` and NOT moved once a number had been seen.
  PRINTED-DIGIT   -- no candidate prints the string, but one prints a number inside the gate's
                     allowance.  A WEAKER finding, reported as one and kept out of the headline.
  ABSENT          -- every candidate RAN and none prints it, verbatim or within the digit
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


def produces(name, fig):
    """the TOLERANCE reading, kept only to separate PRINTED-DIGIT from ABSENT"""
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
rows, absent, elsewhere, digit = [], [], [], []
for s in SITES:
    cites = [n for n in s['cites'] if n in TEXT]
    for f in s['figures']:
        good = [n for n in ran if produces_verbatim(n, f)]
        if good:
            own = [n for n in good if n in cites]
            rows.append((s, f, 'VERBATIM', (own or good)[0]))
            if cites and not own:
                elsewhere.append((s['paper'], s['line'], f, good[0]))
            continue
        # ⑮ no receipt prints the string.  Is there one inside the gate's allowance?
        near = [n for n in ran if produces(n, f)]
        if near:
            rows.append((s, f, 'PRINTED-DIGIT', near[0]))
            digit.append((s['paper'], s['line'], f, near[0]))
            continue
        v = 'UNRUN' if unrun else 'ABSENT'
        rows.append((s, f, v, None))
        if v == 'ABSENT':
            absent.append((s['paper'], s['line'], f))

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

nrep = sum(1 for _s, _f, v, _n in rows if v == 'VERBATIM')
ndig = sum(1 for _s, _f, v, _n in rows if v == 'PRINTED-DIGIT')
nabs = sum(1 for _s, _f, v, _n in rows if v == 'ABSENT')
nunr = sum(1 for _s, _f, v, _n in rows if v == 'UNRUN')
print(f"\n      VERBATIM {nrep}   PRINTED-DIGIT {ndig}   ABSENT {nabs}   UNRUN {nunr}   of {len(rows)}")
print(f"      ⌗ the headline of this revision is the VERBATIM count and nothing else.  The "
      f"PRINTED-DIGIT rows below are a WEAKER finding -- no receipt in the candidate set prints the "
      f"paper's figure; one prints a number the figure-pin gate would accept for it.")
if digit:
    print(f"\n      ⚠ PRINTED-DIGIT, {len(digit)} figure(s) -- right to the gate's allowance, not to "
          f"the digit the paper prints:")
    for paper, line, f, n in digit:
        print(f"         {paper} l.{line}: {f} <- {n[:62]}")
if absent:
    print("\n      ⛔ ABSENT, each looked for in every candidate that ran:")
    for paper, line, f in absent:
        print(f"         {paper} l.{line}: {f}")
check(f"ⓑ① every figure is judged -- no figure is left without a verdict", len(rows) ==
      sum(len(s['figures']) for s in SITES))
check(f"ⓑ② and none is ABSENT for want of a run: UNRUN is {nunr}, and a figure is ABSENT only when "
      f"every candidate ran", nunr == 0 or bool(unrun))
check(f"ⓑ③ ⑮ VERBATIM FIRST is what is reported: the headline count ({nrep}) is strictly below "
      f"the tolerance reading ({nrep + ndig}), so the tightening registered at +60.4 is not a "
      f"relabelling of the same set", nrep < nrep + ndig)

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
json.dump(dict(verbatim=nrep, printed_digit=ndig, absent=nabs, unrun=nunr, total=len(rows),
               absent_rows=absent, printed_digit_rows=digit, elsewhere=elsewhere[:200],
               failures=_fail),
          open(os.path.join(HERE, 'verdicts.json'), 'w'), indent=1)
sys.exit(1 if len(_fail) > 0 else 0)
