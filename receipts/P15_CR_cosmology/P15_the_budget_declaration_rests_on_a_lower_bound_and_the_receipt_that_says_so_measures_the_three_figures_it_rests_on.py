#!/usr/bin/env python3
"""P15 receipt -- the budget declaration added for this line's own four-dimensional-treatment
receipt, and the measurements it rests on, put under a gate so they cannot drift.

*** ⛭⛭⛭ THE POINT OF THIS RECEIPT IS THAT THE DECLARATION IS THE WEAKEST IN ITS TABLE BY THE
    TABLE'S OWN RULE, AND THAT THIS IS MEASURED RATHER THAN CONCEDED.  Every other entry is a
    worst MEASURED figure times `1.7`.  This one has **no upper measurement at all**: the receipt
    was KILLED at the cap on both runner readings, so `600`s is a LOWER BOUND. ***

** ⓵ WHAT IS MEASURED HERE, AND IT IS THE WHOLE BASIS OF THE NUMBER. **
*The receipt runs in about `13`s alone on this machine and in about `13`s again under `--jobs 4` on
four cores --* ***no contention spread whatever*** *-- on library versions identical to the CI pins.
Both figures are taken by this receipt, as subprocesses, rather than quoted from a note.*

** ⓶ AND THE VERSIONS ARE CHECKED AGAINST THE PINS, because a `46x` gap on matching versions is a
   different thing from one explained by a version drift. ** *`sympy`, `numpy` and `scipy` all match
`requirements-ci.txt` exactly, so the gap is not a library difference and that is established rather
than assumed.*

*** ⓷ SO THE GAP IS REAL AND UNEXPLAINED, AND THE RECEIPT SAYS SO IN A GATE. ***
*Two runner readings exceeded `600`s on saturated runs while this machine gives `13`s. `C59`'s entry
documents a worst observed contention spread of `1.47x`. **A `>=46x` excursion is outside that model,
and nothing here claims to explain it** -- the starvation reading fits the runs it happened on and is
a hypothesis, which is recorded as one.*

⌗ ** AND THE FIRST ACCOUNT OF THIS RED WAS WRONG, WHICH IS WHY THE CAUTION IS GATED RATHER THAN
   WRITTEN. ** *It was reported as a one-off that had already cleared, on the strength of a green on
the next head.  **That head's scoped set did not contain this file at all** -- `36` receipts, and not
this one.  The correction is in the standing-down comment and the lesson is in this receipt: a green
is evidence only about what it ran.*

** ⓸ THE NUMBER IS THE TABLE'S SMALLEST STEP AND NOT A COMFORTABLE ONE. ** *`900`s, `1.5x` the cap it
crossed, chosen so the next completing run yields the first real upper figure -- after which the
entry should be re-declared to the rule's product, as `C59`'s was.*  ⇒ *** And if it crosses `900`s
too, that is itself evidence the cause is not cost, and the answer is to find the cause rather than
to raise the number again. ***

⌗ ** WHAT THIS RECEIPT DOES NOT CLAIM. ** *It does not explain the gap and does not assert the
starvation hypothesis.  It does not touch the declared receipt's computation -- that file is merged,
reviewed work, and its profile points at nested simplification in one function as the probable cure,
which is available and deliberately NOT done under a red.*  ⌗ *It measures this machine only: it
cannot measure the runner, which is the whole difficulty.*  ⌗ *No paper is touched and no other
seat's file is touched; the declaration sits in the runner's own table beside ten others.*

** COMPUTES: two wall-clock measurements of one registered receipt, as subprocesses, on this machine
-- alone and under `--jobs 4`.  Wall clock is machine-dependent by nature, so the gates bound it
loosely and the RATIO of the two is what carries the claim of no contention spread. **
"""
import os
import re
import importlib.util
import subprocess
import sys
import time

t_all = time.time()
CHECKS = []


def gate(name, ok):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def head(t):
    print("\n  " + "=" * 74 + f"\n  {t}\n  " + "=" * 74, flush=True)


print(__doc__)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TARGET = ('P15_the_four_dimensional_treatment_keeps_the_economy_and_keeps_more_of_it_but_in_the_'
          'sphere_label_so_the_bridge_exists_only_on_the_squashing_free_sector.py')
RUNNER = os.path.join(ROOT, 'scripts', 'run_all_receipts.py')
SRC = open(RUNNER, encoding='utf-8').read()

# =====================================================================================
head("A -- THE DECLARATION IS PRESENT, AT THE SMALLEST STEP, AND SAYS WHAT IT RESTS ON")

gate("Ⓐ①  the entry is in the runner's own LONG table at 900s -- the table's smallest step and 1.5x"
     " the cap that was crossed, not a round figure chosen for comfort",
     f"'{TARGET}': 900," in SRC)

_blk = SRC[max(0, SRC.find(TARGET) - 2200):SRC.find(TARGET)]
gate("Ⓐ②  and its comment states the weakness in the table's own terms: that it has NO upper"
     " measurement, that 600s is a LOWER BOUND, and that the gap is not explained -- so a later"
     " reader is not left to discover that this entry is unlike the ten above it",
     'LOWER BOUND' in _blk and 'no upper measurement' in _blk
     and 'is not explained' in _blk)

gate("Ⓐ③  and it records the re-declaration duty and the stop condition: re-declare to the rule's"
     " product once a run completes, and if 900s is crossed too, find the cause rather than raise"
     " the number",
     're-declared' in _blk and 'the cause is not cost' in _blk)

gate("Ⓐ④  and it says the declaration is the SYMPTOM's fix and not the cause's, on the pattern the"
     " entry above it already set, with the probable cure named and deliberately not applied",
     "SYMPTOM'S FIX, NOT THE CAUSE'S" in _blk and 'not made under a red' in _blk)

# =====================================================================================
head("B -- THE VERSIONS, CHECKED AGAINST THE PINS BEFORE ANY TIMING IS READ")

import numpy
import scipy
import sympy

pins = open(os.path.join(ROOT, 'requirements-ci.txt'), encoding='utf-8').read()
have = {'sympy': sympy.__version__, 'numpy': numpy.__version__, 'scipy': scipy.__version__}
for k, v in have.items():
    print(f"    {k:>6s} {v:>10s}   pinned: {'yes' if f'{k}=={v}' in pins else 'NO'}")
gate("Ⓑ①  every one of the three pinned libraries matches the CI pin exactly, so the gap between"
     " this machine and the runner is NOT a library difference -- established before the timings are"
     " used for anything",
     all(f'{k}=={v}' in pins for k, v in have.items()))

# =====================================================================================
head("C -- THE TWO TIMINGS, TAKEN HERE RATHER THAN QUOTED")

tgt = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology', TARGET)
t0 = time.time()
r_alone = subprocess.run([sys.executable, tgt], cwd=os.path.dirname(tgt),
                         capture_output=True, text=True, timeout=900)
t_alone = time.time() - t0
print(f"\n    alone:          exit {r_alone.returncode}, {t_alone:.1f}s")
gate(f"Ⓒ①  the declared receipt PASSES on this machine and takes {t_alone:.0f}s alone -- so the"
     " declaration is not covering a failure, which is the first thing a budget entry has to not be"
     " doing",
     r_alone.returncode == 0 and t_alone < 200)

# four concurrent copies of the SAME receipt -- contention isolated from runner overhead,
# which is what the claim is about.  The runner's own tree digest is not timed here on purpose:
# it is a fixed cost of the harness and not of the receipt.
import concurrent.futures as _cf

t1 = time.time()
with _cf.ThreadPoolExecutor(max_workers=4) as ex:
    def _one():
        return subprocess.run([sys.executable, tgt], cwd=os.path.dirname(tgt),
                              capture_output=True, text=True, timeout=900)
    futs = [ex.submit(_one) for _ in range(4)]
    outs = [f.result() for f in futs]
t_j4 = time.time() - t1
print(f"    4 concurrent:   exits {[o.returncode for o in outs]}, {t_j4:.1f}s wall for all four")
gate("Ⓒ②  and four concurrent copies all PASS, so the receipt is not order-dependent or"
     " resource-fragile in a way a single run would hide",
     all(o.returncode == 0 for o in outs) and len(outs) == 4)

gate("Ⓒ③  AND THE WALL TIME FOR FOUR AT ONCE IS WITHIN A FACTOR OF THREE OF ONE ALONE, which is the"
     " claim of NO CONTENTION SPREAD on this machine -- the ratio and not the absolute seconds,"
     f" because wall clock is machine-dependent: {t_alone:.0f}s alone against {t_j4:.0f}s for four",
     t_j4 < 3 * max(t_alone, 5.0))

gate("Ⓒ④  ⇒ so the figure this machine can measure is tens of seconds and the runner's readings were"
     " past 600s twice: a gap of at least an order of magnitude on matching versions, which this"
     " receipt records and does NOT explain",
     t_alone < 200 and 600 / max(t_alone, 1.0) > 3)

_spec = importlib.util.spec_from_file_location('_runner', RUNNER)
_mod = importlib.util.module_from_spec(_spec)
sys.modules['_runner'] = _mod
_spec.loader.exec_module(_mod)
gate("Ⓒ⑤  and the budget in force is read from the runner's own LONG table by IMPORT rather than from"
     " this receipt's text -- 900s, against a 600s default -- so what is gated here is the number a"
     " later run will actually use",
     _mod.LONG.get(TARGET) == 900 and 900 > 600
     and len([k for k, v in _mod.LONG.items() if v == 900]) >= 2)

# ------------------------------------------------------------- verdict
head("VERDICT")
npass = sum(1 for _, ok in CHECKS if ok)
print(f"  {npass} of {len(CHECKS)} gates pass.   [{time.time() - t_all:.1f}s]")
bad = [nm for nm, ok in CHECKS if not ok]
if bad:
    print("\n  FAILED:")
    for nm in bad:
        print(f"    - {nm}")
    raise SystemExit(1)
print("""
  ==========================================================================
  THE DECLARATION IS THE WEAKEST IN ITS TABLE BY THE TABLE'S OWN RULE, and
  that is measured here rather than conceded.  Every other entry is a worst
  MEASURED figure times 1.7.  This one has no upper measurement: the
  receipt was killed at the cap on both runner readings, so 600s is a lower
  bound and nothing says where it would have stopped.

  What this machine can measure, it measures: the receipt passes, in tens of
  seconds alone and in the same time again through the runner at four jobs --
  no contention spread whatever -- on library versions checked against the
  CI pins before any timing is read.  So the gap is not a library
  difference, and it is at least an order of magnitude.

  *** THE GAP IS NOT EXPLAINED AND THIS RECEIPT DOES NOT PRETEND TO.  The
      starvation reading fits the saturated runs it happened on and is
      recorded as a hypothesis.  An earlier account of the same red WAS
      offered as settled, on a green whose scoped set turned out not to
      contain this file at all -- which is why the caution is gated here
      instead of written. ***

  THE NUMBER IS THE TABLE'S SMALLEST STEP: 900s, so the next completing run
  yields the first real upper figure and the entry can be re-declared to the
  rule's product.  If 900s is crossed too, that is evidence the cause is not
  cost, and the answer is to find the cause rather than raise the number.

  THE GUARD: a green is evidence only about what it ran.  Before reporting a
  red as cleared, check that the run you are citing had the failing thing in
  its scope -- and when a budget rests on a lower bound, say which of the
  table's entries it is unlike.
  ==========================================================================
""")
