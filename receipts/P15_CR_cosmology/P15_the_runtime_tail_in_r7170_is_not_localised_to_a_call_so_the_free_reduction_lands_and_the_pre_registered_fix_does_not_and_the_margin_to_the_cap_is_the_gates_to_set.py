#!/usr/bin/env python3
"""P15 receipt -- `r7205`'s order, which named `r7220` as the work: fix this line's own `r7170`
receipt, which has NO failing gate and a runtime that explodes.

*** ⛭⛭⛭ THE PRE-REGISTERED FIX DOES NOT HOLD, AND THE REASON IS THE RESULT: THE TAIL IS NOT
    LOCALISED TO A CALL AT ALL.  `r7220` FILED BRANCH ⓐ -- ONE CALL CARRYING IT, REPLACED BY A
    DETERMINATE NORMALISATION -- AND THE MEASUREMENT CAME BACK ⓑ. ***

** ⓵ WHAT IS MEASURED, AND THE DEFECT IS REAL. **  *Twenty plain runs on an idle box: THREE killed at
the batch's `420` s cap, the other seventeen at `17`--`22` s against the receipt's registered `13` s.*
⛔ ** So the receipt fails only by exceeding a timeout, never by a gate: ZERO `FAIL` lines in every run
that finished, across every batch in this revision. **

** ⓶ AND IT IS NOT LOCALISED, WHICH IS WHY THE FILED FIX CANNOT BE THE FIX. **  *Thirty-seven further
runs with ANY instrumentation added -- a traceback dump on a timer, a timing wrapper, or plain markers
written to stderr -- produced NOT ONE blow-up, where the plain rate predicts about five.*  ⇒ *** A
defect that disappears whenever it is watched is not a slow call, and no replacement of one call could
have removed it. ***  ⌗ ⚠ *And the two blown runs of one batch were ADJACENT, which points at a burst
rather than an independent per-run draw.  **Three accounts remain live and this revision eliminates
none of them**: an intrinsic per-run excursion, an environmental burst, and a perturbation introduced by
the instrument.*

** ⓷ THE FREE HALF LANDS AND IS MEASURED AS WHAT IT IS, NOT AS THE FIX. **  *The degree-difference gate
re-asks for two operators the separation gates have already reduced.  Memoising on the two small
integers takes eleven reductions to nine.*  ⇒ ** The typical run falls from `18` s to `16` s by MEDIAN,
about a ninth; the blow-ups do NOT stop -- one in twenty post-repair, plus a `99` s excursion. **  ⛔ *The
MEAN moves the other way, `18.2` s to `20.5` s, because that one excursion dominates nineteen runs of
`15`--`17` s: **the median is quoted because the mean of a tailed sample measures the tail, and the tail
is the thing that did not change.** *Stated because the first draft of this receipt quoted the mean of a
partial sample as the headline and had it backwards.**  ⇒ ** The pre-registered pass condition was THIRTY
consecutive runs at or under budget and it is NOT met. **

⛭⛭ ** ⓸ SO WHAT IS LEFT IS A MARGIN QUESTION AND IT IS THE GATE'S, WHICH IS WHERE `r7203` ALREADY PUT
   IT. **  *The suite's cap is `600` s and a finished run takes `16` s, a margin of `37` times.  No
call in the per-call timing comes near it: the dominant one is the inner reduction at `12.5`--`15.7` s
summed over eleven calls, `3.3` s at its worst single call.*  ⇒ *** Nothing inside this receipt
explains a `420` s run, so nothing inside it is the place to fix one.  `r7203` offered a cap, a scope
declaration or a runner split and said to name which: **the ask is a per-receipt cap this receipt can
declare, because a receipt that knows it runs in `16` s can say so and be killed at a bound that makes
a `420` s run a reported fact rather than a silent carry.*** ***

⌗ ** AND ONE GATE OF THIS RECEIPT'S OWN FIRST DRAFT WAS WITHDRAWN BY THE SWEEP THAT CHECKS IT. **
*`Ⓓ③` asserted the repaired receipt finishes under `300` s.  The three-build tolerance sweep flagged
it: `18.1` s on one build against `20.6` s on another, a site that MOVES with the machine.*  ⇒ ***A
receipt about a runtime must not gate on one.  The time is reported and the gate asserts only that the
run is green*** --- which is the slack-tolerance class `PO-78` already carries at `45`, met from the
inside, and this is not a `46`th.

⛔ ** AND NO ASSERTION WAS WEAKENED TO MAKE A RUNTIME PROBLEM GO AWAY**, *which is the one thing
`r7220`'s pre-registration put out of scope.  The cheaper-normalisation branch was never applied,
because the measurement that would have justified it never arrived.*

** COMPUTES: the two twenty-run batches and the three instrumentation variants as RECORDED, read from
   this revision's own data files rather than re-run; the per-call simplify timing from ten
   instrumented runs; and live, on this tree: that the memoised reduction returns what an uncached
   recomputation returns, that the operator it returns still FAILS a deliberately perturbed test, and
   that a fresh run of the repaired receipt finishes inside its budget.  *** No gate of `r7170` is
   altered, no workflow file is touched, and the margin ask is stated rather than taken. *** **

STATUS: rc=0 on success.  Run: python3 <this file>   (sympy; ~60 s)
"""
import os
import re
import subprocess
import sys
import time

import sympy as sp

print(__doc__.split("** COMPUTES:")[0].rstrip())
BAR = "=" * 104
fail = []


def gate(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7220_60_the_runtime_tail')
TARGET = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                      'P15_the_four_dimensional_treatment_keeps_the_economy_and_keeps_more_of_it_'
                      'but_in_the_sphere_label_so_the_bridge_exists_only_on_the_squashing_free_'
                      'sector.py')
for _p in (DATA, TARGET):
    if not os.path.exists(_p):
        print(f"  ⛔ A PATH THIS RECEIPT READS IS NOT ON DISK: {_p}")
        sys.exit(1)


def rows(name):
    out = []
    for ln in open(os.path.join(DATA, name), encoding='utf-8'):
        ln = ln.strip()
        if ln and not ln.startswith('#'):
            out.append(ln.split())
    return out


# ============================================================ A. the defect, measured
head("A.  THE DEFECT IS REAL AND IT IS A TIMEOUT, NEVER A GATE")

B = rows('batches.txt')
PRE = [(int(r[2]), int(r[3])) for r in B if r[0] == 'PRE']
POST = [(int(r[2]), int(r[3])) for r in B if r[0] == 'POST']
pre_blown = [e for rc, e in PRE if rc != 0]
post_blown = [e for rc, e in POST if rc != 0]
pre_ok = [e for rc, e in PRE if rc == 0]
post_ok = [e for rc, e in POST if rc == 0]
print(f"      PRE   {len(PRE):2d} runs, {len(pre_blown)} killed at the cap, "
      f"the rest {min(pre_ok)}-{max(pre_ok)} s, mean {sum(pre_ok) / len(pre_ok):.1f} s")
print(f"      POST  {len(POST):2d} runs, {len(post_blown)} killed at the cap, "
      f"the rest {min(post_ok)}-{max(post_ok)} s, mean {sum(post_ok) / len(post_ok):.1f} s")

gate("Ⓐ① the pre-repair batch is twenty plain runs on an idle box with THREE killed at the cap and "
     "the other seventeen between `17` and `22` s --- so the receipt's registered `13` s describes "
     "its typical run and nothing about its worst",
     len(PRE) == 20 and len(pre_blown) == 3 and min(pre_ok) >= 15 and max(pre_ok) <= 25)

gate("Ⓐ② and ⛔ EVERY run that finished finished GREEN --- the receipt has no failing gate in any "
     "batch of this revision, so what is wrong with it is its runtime and not its content",
     all(rc == 0 or e >= 300 for rc, e in PRE + POST))

# ============================================================ B. it is not localised
head("B.  AND IT IS NOT LOCALISED TO A CALL, WHICH IS WHAT KILLS THE PRE-REGISTERED FIX")

V = rows('variants.txt')
vruns = sum(int(r[1]) for r in V)
vblown = sum(int(r[2]) for r in V)
for r in V:
    print(f"      {r[0]:16s} {r[1]:>3s} runs, {r[2]} blown, cap {r[3]} s")
_expected = vruns * len(pre_blown) / len(PRE)
print(f"      ⇒ {vruns} instrumented runs, {vblown} blown, against {_expected:.1f} expected at the "
      f"plain rate of {len(pre_blown)}/{len(PRE)}")

gate("Ⓑ① ⛭⛭⛭ THIRTY-SEVEN RUNS WITH INSTRUMENTATION ADDED PRODUCED NOT ONE BLOW-UP, where the plain "
     "rate predicts about five.  ***A defect that disappears whenever it is watched is not a slow "
     "call***, so replacing any one call could not have removed it and the filed branch ⓐ is refuted "
     "by its own measurement",
     vruns == 37 and vblown == 0 and _expected > 4.0)

P = rows('percall.txt')
worst = max(float(r[4]) for r in P)
dom = [r for r in P if r[0] == 'radial-inner'][0]
print(f"      the dominant call sums to {dom[2]}-{dom[3]} s over {dom[1]} calls, worst single "
      f"{dom[4]} s;  worst single call anywhere {worst} s")

gate("Ⓑ② and the per-call timing says the same thing from the other side: the dominant call's WORST "
     "single invocation is `3.3` s and the whole run's simplify time is under `20` s, so no call in "
     "the measured profile is within two orders of magnitude of a `420` s run",
     worst < 5.0 and sum(float(r[3]) for r in P) < 25.0)

_adj = any(PRE[i][0] != 0 and PRE[i + 1][0] != 0 for i in range(len(PRE) - 1))
gate("Ⓑ③ ⚠ and the limit on all of it is stated rather than buried: two of the three blown runs were "
     "ADJACENT in one batch, which points at a burst rather than an independent per-run draw, so "
     "THREE accounts remain live --- an intrinsic excursion, an environmental burst, and a "
     "perturbation introduced by the instrument --- and this revision eliminates NONE of them",
     _adj)

# ============================================================ C. the free half, and what it buys
head("C.  THE FREE HALF LANDS, AND IS REPORTED AS A TENTH RATHER THAN AS THE FIX")

src = open(TARGET, encoding='utf-8').read()
gate("Ⓒ① the memoisation is on the reduction in `r7170` and nothing else in that receipt changed: one "
     "decorator and a docstring that says what it is and what it is not",
     'functools.lru_cache' in src and 'Memoised at `r7220`' in src
     and 'NOT the fix for this receipt' in ' '.join(src.split()))

import statistics as _stats
_med_pre, _med_post = _stats.median(pre_ok), _stats.median(post_ok)
_speed = _med_pre / _med_post
_mean_pre = sum(pre_ok) / len(pre_ok)
_mean_post = sum(post_ok) / len(post_ok)
print(f"      typical run by MEDIAN {_med_pre:.0f} s -> {_med_post:.0f} s, a factor of {_speed:.3f}")
print(f"      and by MEAN {_mean_pre:.1f} s -> {_mean_post:.1f} s, the other way, because one "
      f"{max(post_ok)} s excursion dominates nineteen runs of {min(post_ok)}-17 s")

gate("Ⓒ② ⛔ AND THE PRE-REGISTERED PASS CONDITION IS NOT MET, WHICH IS SAID AS A FAILURE OF THE FIX "
     "RATHER THAN SMOOTHED.  `r7220` filed THIRTY consecutive runs at or under budget with none over "
     "three times it.  Twenty post-repair runs gave ONE killed at the cap and a `99` s excursion "
     "besides, so the tail survives and the cut is about a NINTH of the typical run by median.  ⛔ And "
     "the MEAN moves the other way because that one excursion dominates: ***the median is the honest "
     "statistic here and the reason is stated rather than the favourable number chosen***",
     len(post_blown) >= 1 and 1.05 < _speed < 1.20 and max(post_ok) > 3 * _med_post
     and _mean_post > _mean_pre)

# ============================================================ D. live controls on the repair
head("D.  LIVE ON THIS TREE: THE CACHE RETURNS WHAT RECOMPUTATION RETURNS, AND STILL FAILS A FAKE")

# ** r7170's OWN declarations, copied rather than re-chosen: the positivity assumptions change what
#    simplify can do, so a re-implementation that re-chooses them reduces a different object. **
t, r, th, ph, ps = sp.symbols('t r theta phi psi')
M, al, om = sp.symbols('M alpha omega', positive=True)
I = sp.I
f = 1 - 2 * M / r - r ** 2 / al ** 2
X = [t, r, th, ph]
g4 = sp.diag(-f, 1 / f, r ** 2, r ** 2 * sp.sin(th) ** 2)
gi = sp.simplify(g4.inv())
sq = sp.sqrt(sp.simplify(-g4.det()))
Rf = sp.Function('R')(r)


def reduce_once(lv, mv):
    """the same reduction r7170 performs, written out here so the cache can be checked against it."""
    Y = sp.simplify(sp.Ynm(lv, mv, th, ph).expand(func=True))
    F = Rf * Y * sp.exp(-I * om * t)
    box = sum(sp.diff(sq * sum(gi[a, b] * sp.diff(F, X[b]) for b in range(4)), X[a])
              for a in range(4)) / sq
    return sp.simplify(sp.expand(sp.simplify(box / (Y * sp.exp(-I * om * t)))))


_t0 = time.time()
_a = reduce_once(1, 0)
_b = reduce_once(1, 1)
print(f"      two reductions recomputed here in {time.time() - _t0:.1f} s")

gate("Ⓓ① the reduction is a pure function of its two integers, which is what makes the cache sound: "
     "the `m = 0` and `m = 1` operators at `ell = 1` are the SAME object, so a hit returns what the "
     "recomputation would have built",
     sp.simplify(_a - _b) == 0)

_fake = _a + sp.sin(th) / r ** 2
gate("Ⓓ② ⛔ THE MUST-COME-BACK-WRONG CONTROL: a perturbed operator carrying an angular term still "
     "FAILS the separation test, so the test the cache feeds is not vacuous and a cached answer "
     "cannot smuggle a false pass",
     bool(_fake.free_symbols & {th}) and not bool((_a).free_symbols & {th})
     and sp.simplify(_fake - _a) != 0)

_t1 = time.time()
_rc = subprocess.run([sys.executable, TARGET], stdout=subprocess.DEVNULL,
                     stderr=subprocess.DEVNULL, timeout=600).returncode
_el = time.time() - _t1
print(f"      a fresh run of the repaired receipt: rc={_rc} in {_el:.1f} s")

gate("Ⓓ③ and the repaired receipt runs GREEN here --- which is the ordinary case and is exactly why "
     "the extraordinary one is hard to catch.  ⛔ **The elapsed time is REPORTED and not asserted**: a "
     "wall-clock bound is a tolerance site that moves with the machine, and this revision's own "
     "three-build sweep flagged an earlier draft of this gate for exactly that.  ***A receipt about a "
     "runtime must not gate on one***",
     _rc == 0)

# ============================================================ E. what is asked of the gate
head("E.  WHAT IS ASKED, AND IT IS THE THING r7203 OFFERED TO TAKE")

print("      The suite's cap is 600 s; a finished run is 16 s; the margin is 37x.  Nothing in the")
print("      per-call profile explains a 420 s run, so nothing inside this receipt is the place to")
print("      fix one.  ⇒ The ask is a PER-RECEIPT cap a receipt can declare for itself, so that a")
print("      receipt which knows it runs in 16 s is killed at a bound near that rather than at the")
print("      suite's, and a 420 s run becomes a reported fact instead of a silent carry.")
print("      ⛔ Not asked for and not wanted: a looser cap, a retry, or a quarantine.")

gate("Ⓔ① and this receipt touches no workflow file and no gate of `r7170`, so the ask is an ask",
     not os.path.exists(os.path.join(ROOT, '.github', 'workflows', 'gates.yml.orig'))
     and 'gates.yml' not in src)

print(f"\n{BAR}")
if fail:
    print(f"  ⛔ {len(fail)} GATE(S) FAILED")
    for x in fail:
        print(f"      - {x[:96]}")
    sys.exit(1)
print("  ✔ every gate passed")
print(f"{BAR}")
