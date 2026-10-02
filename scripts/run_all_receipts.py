#!/usr/bin/env python3
"""run_all_receipts.py -- ** THE ELEVENTH GATE: RUN THEM. **

Built r2376+c54.161, against the finished assertion sweep.

** WHY IT EXISTS, AND IT IS THE PLAINEST REASON IN THE CORPUS. **  Nothing here had ever run the
receipts.  `check_receipts` verifies that a \\rcpt resolves to an INDEX row and a file on disk; the
assertion census counts checks by READING source; `lint_assertions` parses it; `check_compile`
builds the papers.  At r2376+c54.160 the sweep found `ROBUST_p1p2_scan` -- registered, cited --
exiting 1 on ImportError before reaching a single line of computation, and every gate was green.

** So "the receipt passes" was never a claim any gate was making. **  THE_BASE_RATE, entry
twenty-three: an instrument that reads a file has not run it.

This runs every registered receipt from ITS OWN DIRECTORY, which is the second half of the same
point -- a receipt that only runs from somewhere else is not runnable where it is registered.

  * PASS   exit 0.
  * FAIL   non-zero exit: an assertion fired, or the file is broken.  ** Both are failures and the
           gate does not distinguish them, because a receipt that cannot run cannot be trusted to
           have checked anything either. **
  * SLOW   over the per-file timeout; reported, not failed, and named so the budget is visible.

Usage:
    python3 scripts/run_all_receipts.py                 # all registered receipts
    python3 scripts/run_all_receipts.py --timeout 900   # per-file seconds (default 600)
    python3 scripts/run_all_receipts.py --jobs 8        # parallelism (default: cpu_count-2)
    python3 scripts/run_all_receipts.py --only P15      # substring filter on the path
    python3 scripts/run_all_receipts.py --quick         # skip the files named SLOW below
    python3 scripts/run_all_receipts.py --resume CACHE --wall 500   # resumable, bounded invocation

** ⛔⛭ RESUMABILITY, r4512, AND IT IS NOT A CONVENIENCE. **  This gate's own `--how` text says to
launch the runner DETACHED and poll.  *On the container this line runs in, a detached process --
`nohup`, and `setsid nohup ... < /dev/null` exactly as that text prescribes -- IS REAPED AT THE END
OF THE TURN THAT STARTED IT.*  Three launches were killed between 15 and 20 minutes in, each
leaving the five-line header and no verdict, and the header-only `RUN_RESULT.txt` sitting in the
tree is the residue of an earlier one.  ** So the documented way to run this gate does not run it
here, and the failure presents as a file that looks like a run. **
  ⇒ *** The fix is not a longer wait: it is for the work to SURVIVE being interrupted. ***  With
      `--resume`, each receipt's result is written to the cache the moment it finishes, so an
      invocation killed at any point loses only what was in flight.  `--wall` stops cleanly at a
      budget instead of being killed at one.  Successive foreground invocations converge, and the
      final one prints the whole result.
  ⌗ ** The cache is keyed by TREE-DIGEST and discarded whole when it changes **, so a result can
    never be reused across a tree it was not measured on -- which is the same rule the cached
    `RUN_RESULT.txt` lives under, one level in.

** THIS GATE IS NOT IN THE STANDING TEN. **  It costs wall clock the others do not, so it is run
at a juncture -- before a bundle, after a sweep -- rather than every revision.  Saying so here
rather than quietly wiring it in, because a gate nobody runs is worth what a receipt nobody runs
is worth.
"""
import os

# ** NODE=ci FOR THE CHILD RECEIPTS -- 59, r3695, answering 60's route from r3726. **
# *Five registered receipts shell out to `check_revision_collisions`, which since 59's r3679
# REFUSES to run with `NODE` unset rather than defaulting to `PARITY = 0`.  That refusal is
# what stopped twenty-one collisions and it stays.*
#   ⇒ ** But a RUNNER is not a LINE. ** *The refusal exists to stop a node committing without
#   declaring which half it holds; a harness verifying that a receipt executes holds no half and
#   is claiming none.  `ci` is a DECLARED value meaning exactly that, and the gate under it
#   reports "the band is NOT CHECKED this run" -- which is the honest answer for a runner, not a
#   silent default.  60's reasoning is accepted as given.*
# ⌗ *This is NOT the r3679 defect one layer out: that defect was a gate INFERRING a band nobody
#  declared. This declares one, and the declared one holds no band.*
os.environ.setdefault('NODE', 'ci')
import sys

# ---------------------------------------------------------------- r2656+c54.208
# ** `scripts/queue.py` SHADOWS THE STDLIB `queue`, WHICH `concurrent.futures` IMPORTS. **
# Running this file as `python3 scripts/run_all_receipts.py` puts `scripts/` first on sys.path,
# so ThreadPoolExecutor dies on `queue.SimpleQueue` before a single receipt runs.  The runner has
# therefore been UNRUNNABLE since `scripts/queue.py` was added -- which is why the cached
# `RUN_RESULT.txt` this gate reads had not moved in 294 commits.
#   ⇒ *** A 9-minute out-of-band job that crashes in its first second leaves the LAST GOOD RESULT
#       sitting on disk, so the failure presents as a stale success rather than as a failure. ***
# Dropping this file's own directory from sys.path fixes THIS script.  The hazard is general --
# any script here that touches threads inherits it -- and the rename is the observer line's to
# make, so it is routed rather than done under them.
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:] = [p for p in sys.path if os.path.abspath(p or '.') != _HERE]

import argparse
import glob
import hashlib
import json
import re
import threading
import subprocess
import time
import uuid
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))

# ** c54.222: the INDEX row filter lives in ONE place now.  `corpus/` is appended rather than
# prepended so it cannot shadow the stdlib the way `scripts/` did (see the note above). **
sys.path.append(os.path.join(ROOT, 'corpus'))
import index_rows  # noqa: E402

# Known-slow receipts: full Boltzmann hierarchies and BBN networks.  Named rather than hidden.
SLOW = (
    'ROBUST_p1p2_scan', 'C11TEST_radiation_zeroed', 'P15_the_second_arm_actually_run',
    'bbn_network', 'P16_validate_bbn', 'P16_theory_error_and_likelihood',
    'P15_verify_lowell_boltzmann', 'P15_camb_reference', 'BUILD_camb_store',
    # ** ADDED c54.226 (`L-560`).  This file had been FAILING FAST since r2682+c54.212 on a seed left
    # ** in it, and c54.222 removed the seed -- so the first run that actually EXECUTED it is the one
    # ** that discovered it is slow.  It exceeded the 900s budget under six-way contention. **
    #   ⇒ *** A file that fails in its first second has no measured cost, so removing a seed can move a
    #       receipt from "instant" to "over budget" with nothing in between.  Named here rather than
    #       left to surprise the next run: the tuple exists to make the budget visible. ***
    'P16_the_scalar_monodromy_is_four_pi_over_rho',
)

# ---------------------------------------------------------------- r4006
# ** A DECLARED PER-RECEIPT BUDGET, BECAUSE ONE RECEIPT IS LONGER THAN ANY CAP THE SUITE CAN CARRY. **
# `C59` is a convergence study: eight distinct Boltzmann projections, the heaviest 1260 modes to
# k_max = 2400 through the hierarchy path, and no redundant work in it (PART 2b reuses PART 1's
# results rather than re-running -- checked, not assumed).  ** Measured end to end on an idle
# machine: 1302s, all 23 assertions evaluated, exit 0. **  It had never once been seen to finish:
# the 300s cap filed it as a failure, the 600s cap as SLOW, and a detached 1200s attempt died 102
# seconds short of the verdict.
#   ⇒ *** AND `SLOW` IS NOT A PASS.  *** A receipt killed at the cap has evaluated nothing, so a
#       green run that reports it as `over timeout` is making no claim about it at all -- which is
#       precisely the hole this runner was built to close ("a registered receipt that does not run
#       where it is registered is not a receipt").  The cap was hiding one inside its own report.
# ⌗ *Declared here BY NAME with its measured cost beside it, never inferred from a file being slow.*
#   The global cap stays where it is; this buys the one receipt that needs it the room to finish,
#   and the number is the measurement plus headroom rather than a round figure chosen to feel safe.
LONG = {
    # ⛭ RE-DECLARED r7017+70.1 (70), 1800 -> 2100, on ⑧'s sweep of the class.  This entry was
    # "measurement plus headroom" and predates the 1.7x rule every entry below uses.  It is the ONE
    # declaration whose number sits below its own rule's product: 1302 x 1.7 = 2213.
    #   ** MEASURED AGAIN, ALONE, ONE THREAD, NOTHING ELSE RUNNING: 1155s, exit 0. **  The file is
    #   unchanged since `2adddf6c`.  The `gates` logs from 09-26 to 09-29 give 96 readings, and they
    #   reach it on the runner: 743-1697s, median 1326s, and 33 of the 96 above 1500s.  ** 1697s is
    #   94 per cent of 1800 **, which is the undeclared-margin class one level up: a budget that holds
    #   today and reports SLOW on the first slower runner.
    #   ⌗ *The rule, and nothing else: 1155 x 1.7 = 1964 -> 2100, the next 300s step, as 1736 -> 1800
    #     and 711 -> 900 were.  The runner's own worst reading, 1697/1155 = 1.47x, sits inside the
    #     1.7x, so C63's spread holds for this file and no file-specific spread is needed.*
    'C59_the_control_reproduces_camb_and_the_height_defect_was_k_truncation.py': 2100,  # measured 1302s; re-measured 1155s alone, one thread (r7017+70.1)
    # ⛭ ADDED r4564 (60).  `C63` drives the two-arm instrument as a SUBPROCESS ten times -- eight for
    # the source-term matrix (both arms x baseline/NOISW/DPSRC/SWSRC) and two for the damping
    # exclusion -- and every one of the ten is load-bearing: the claim is that NO single term carries
    # the split, which cannot be made from a subset.  ** Measured, all three on this machine: 313s at
    # eight runs (r4558), 383s at ten standalone (r4562), and 525s at ten under `--jobs 4`. **
    #   ⇒ *Declared because the cost is REAL and its spread under contention is 1.7x, not because the
    #     file was seen to be slow once.  At 525s against a 600s cap it had 14% of margin, and a
    #     receipt that close to the wall reports `SLOW` sooner or later -- and `SLOW` is not a pass.*
    #   ⌗ ** The number is the worst MEASURED figure plus headroom **, on the same rule as C59's:
    #     525s measured -> 900s declared, not a round figure chosen to feel safe.
    'C63_no_single_source_term_carries_the_undriven_split_and_the_first_probe_read_an_unwired_knob.py': 900,  # measured 525s under --jobs 4
    # ⛭ ADDED r6476 (60).  The last convention: seven instrument runs, four scanning the CR arm's
    # onset over a factor of 3.6 and three walking the control's start under the symmetric
    # sound-horizon convention.  ** Every one of the seven is load-bearing and the claim cannot be
    # made from a subset: **  the scan's claim is a RANGE ("l_A moves 51% and l_1 moves 2%"), which
    # needs its ends AND needs the pin between them to anchor to P15's quoted peak; the control's is
    # a MONOTONE APPROACH TO A FLOOR FROM ABOVE, which needs three points and the floor to be an
    # approach rather than two numbers.  *Trimming either to fit the cap would leave a claim the run
    # no longer makes -- which is the hole this runner exists to close.*
    #   ⇒ ** Measured end to end on an idle machine: 609s, all eleven assertions evaluated, exit 0 **
    #     -- nine seconds past the 600s cap, which is the worst possible place for a receipt to sit:
    #     it would report SLOW or PASS depending on the load, and `SLOW` is not a pass.
    #   ⌗ The number is the measured figure plus C63's own measured 1.7x spread under contention
    #     (609 -> 1035), rounded up to 1500 -- not a round figure chosen to feel safe.  *The scan
    #     runs its subprocesses four at a time, so its cost under `--jobs 4` is contention on
    #     contention; this is the one declaration where the spread is expected to exceed C63's.*
    'P15_the_one_fitted_number_moves_the_scale_and_not_the_peak.py': 1500,  # measured 609s standalone
    # ⛭ ADDED r6476 (60), and declared on the MARGIN rather than on the cap.  Four undriven
    # instrument runs; measured 367s standalone, which is INSIDE the 600s cap and would pass today.
    #   ⇒ *Declared anyway, because C63's own measured spread under `--jobs 4` is 1.7x and
    #     367 x 1.7 = 624 is OUTSIDE it.*  ** A receipt whose standalone figure fits and whose
    #     contended figure does not is exactly the one that reports SLOW on a busy day and PASS on
    #     a quiet one -- and `SLOW` is not a pass, so the verdict would depend on the load rather
    #     than on the tree.**  C63 was declared at 14% of margin; this has 39%, and the rule that
    #     produced C63's number produces this one.
    'P15_the_symmetric_comparison_was_never_runnable_and_the_quarter_was_two_fifths.py': 900,  # measured 367s
    # ⛭ ADDED r6959 (66), on node 70's `r6931+70.3` PROFILE and not on the file being slow.  This is
    # the receipt that has NEVER FINISHED under the runner -- over timeout at `r6921`, over timeout at
    # `r6931+70.2`, and filed as `SLOW` both times.  ⛔ *** `SLOW` IS NOT A PASS, so the suite has been
    # reporting a green run while making no claim about this receipt at all -- for two full suite runs,
    # which is the same hole C59's declaration was written to close. ***
    #   ⇒ ** MEASURED, ALONE, ONE THREAD, NOTHING ELSE RUNNING: 1021s.  So no load explains it and
    #     600s cannot hold it on an idle machine. **  *And the cost is located rather than asserted:
    #     cProfile puts 968s of the 1021 -- 95% -- in `armB`'s TEN SEQUENTIAL SUBPROCESS RUNS of the
    #     photon hierarchy at about 97s each (the two backgrounds, the banked BSTRETCH=2.75 control,
    #     and the two ZEND sweeps), 51s in CAMB on arm A, and everything else under 2s.*
    #   ⌗ ** THE OTHER REMEDY WAS AVAILABLE AND IS DECLINED, WITH THE REASON. **  The ten runs are
    #     independent, so running them concurrently inside the receipt would work -- *and it would make
    #     one receipt's internal parallelism fight the runner's `--jobs N`, so the suite's total
    #     concurrency stops being what the flag says it is and the wall-clock the runner offers stops
    #     holding.*  ⇒ *** A declared budget is visible in one place; internal concurrency is invisible
    #     and would surprise the next reader.  That is the trade, and it goes this way. ***
    #   ⌗ *The number is the rule C63 and `one_fitted_number` were set by and nothing else: the measured
    #     figure times C63's own measured contention spread of 1.7x, rounded up -- 1021 -> 1736 -> 1800.
    #     Its ten subprocesses are SEQUENTIAL, so its spread should be C63's and not worse than it.*
    'P15_the_low_multipole_floor_moves_with_no_background_and_the_factor_two_is_the_late_isw.py': 1800,  # measured 1021s alone, one thread
    # ⛭ ADDED r6983+cc66.49 (66), on the MARGIN, and found by the runner rather than by reading:
    # it went over the 600s cap in the scoped suite on the push that landed `cc66.49`, in a run where
    # `C59` held a slot for 1447s AND `low_multipole_floor` held one for 1160s -- two of four slots
    # gone for twenty minutes.  ** MEASURED, ALONE, ONE THREAD, NOTHING ELSE RUNNING: 418s, `ALL
    # CHECKS PASSED`. **  That is 70 per cent of the cap, so it is the same class as
    # `symmetric_comparison`: *a receipt whose standalone figure fits and whose contended figure does
    # not, which reports SLOW on a busy day and PASS on a quiet one -- and `SLOW` is not a pass, so
    # its verdict would depend on the load rather than on the tree.*
    #   ⌗ *The number is the rule the three entries above were set by and nothing else: the measured
    #     figure times C63's own measured contention spread of 1.7x, rounded up -- 418 -> 711 -> 900.
    #     Its `armB` subprocesses are SEQUENTIAL, one blocking call per invocation, so its spread
    #     should be C63's and not worse than it -- the same reasoning `low_multipole_floor` carries.*
    #   ⛔ *Declared only after measuring it. A budget moved without the measurement behind it is the
    #     vacuous pin `PO-60` exists about, which is why the three OTHER receipts that went over the
    #     cap this same day are reported and NOT declared: they are not this line's to measure.*
    'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py': 900,  # measured 418s alone, one thread
    # ⛭ ADDED r7012 (60), on a measurement and on THIS FILE'S OWN CONTENTION SPREAD rather than on the
    # receipt having been seen slow.  It carries the curvature functional of a left-invariant metric on
    # the three-sphere to FOURTH order in the perturbation, at a level whose frame components are
    # non-constant in all three coordinates -- the symbolic expansion alone is 170s and the five
    # zero-mode integrals another 144s, and no step in it is redundant (the series is built once and
    # every order of it is read).  ** Measured end to end on an idle machine: 366s, all 43 checks
    # evaluated, exit 0. **
    #   ⇒ *366s is 61 per cent of the 600s cap, and C63's measured spread of 1.7x under `--jobs 4`
    #     puts it at about 620s -- OVER. So it is declared by the same rule as the four entries above:
    #     the measured figure times that spread, rounded up (366 -> 622 -> 900), and declared because
    #     `SLOW` is not a pass and a verdict that depends on the load is not a verdict.*
    'P10_the_algebraic_quartic_is_settled_by_the_frame_constant_level_at_every_level_and_the_remainder_is_the_derivative_sectors_eight.py': 900,  # measured 366s alone
    'P10_the_covariant_quartic_is_seven_rationals_carried_by_an_identity_and_no_measurement_route_reaches_them.py': 1500,  # measured 693s alone, one thread (r7032)
    # ⛭ ADDED r7017+70.1 (70), on the RUNNER'S OWN READINGS of this file, because the rule above
    # would NOT have declared it.  Routed to node 70 at `r6993` as the plain undeclared-margin class,
    # with the remedy stated, and left undeclared until now.  ** MEASURED, ALONE, ONE THREAD, NOTHING
    # ELSE RUNNING: 308s, 48 checks, exit 0. **  The file is unchanged since `5e4be2fd`, so every
    # reading below is of this same receipt.
    #   ⇒ *By the rule the entries above were set by, 308 x 1.7 = 524, which is INSIDE the cap, so it
    #     would stay undeclared.  The runner disagrees.*  The scoped-suite logs of the `gates` runs from
    #     09-26 to 09-29 were read: 158 `scope-suite` logs and 7 `heavy` logs.  They show this receipt
    #     33 times:  ** 28 passes at 214-584s, and 5 OVER THE 600s CAP, all on 09-28 pushes. **
    #     *(A pass is printed only when it is among its run's five slowest, so 33 is the number of
    #     readings, not the number of runs.)*
    #   ⌗ *So this file's own contention spread is at least 584/308 = 1.9x on a pass and above
    #     600/308 = 1.95x on each of the five overruns, where the cap cut the reading short.  That is
    #     worse than C63's 1.7x.  It is measured, NOT explained, and no cause is claimed for it.*  So
    #     the rule is kept and this file's spread is used in place of C63's.  The number is the same
    #     step the four 900s entries took: 900s holds a spread of 2.9x against the 308s standalone
    #     figure, and 1.5x against the worst reading that passed.
    #   ⛔ *Not by lifting the global cap: that would hide every other undeclared margin behind this
    #     one.*
    'P14_the_constituent_count_is_conserved_on_every_static_member_and_the_twist_alone_violates_it.py': 900,  # measured 308s alone; runner 214-584s, 5 over 600s
    # ⛭ ADDED r7113+cc66.88 (cc66), ordered by `r7113` after this seat found the two CI reds on #220
    # resolving into one cause: this file's runtime at the 600s wall with no declared budget.
    # ** AND THE 1.7x CONTENTION RULE DOES NOT APPLY HERE, WHICH IS WHY THE NUMBER IS ARGUED AND NOT
    # COMPUTED.  Measured on this container: 54.8s standalone cold, 37.1s warm -- AND 37.1s with three
    # competing full-CPU loads, i.e. NO slowdown at all. **  r4564's note below records 35s standalone
    # and 45-47s in-suite.  So the rule's product would be ~93s -> a 300s step, which sits BELOW the
    # 600s this file has already hit twice: a rule-conformant declaration would make it worse.
    #   ⇒ *** THE OVERRUN IS NOT A CONTENTION SPREAD.  It is bounded by this receipt's OWN
    #       `INNER = 600` on one tightened sample child -- `r7025+70.1`'s finding, quoted in the file:
    #       "exited 1 BECAUSE of a timeout -- this receipt's own `timeout=600` on the tightened
    #       `P16_the_scalar_monodromy` ... A timeout inside a receipt is invisible to every timeout
    #       outside it." ***  CPU contention is now refuted by measurement too, alongside the threading
    #       and memory already refuted at r4564 and the thread count and CPU dispatch at r7025.
    #   ⌗ So the budget is set against the STRUCTURAL bound rather than a spread: `INNER` 600s on one
    #     child plus this file's own ~55s of other work is ~655s, and 900s is the next 300s step --
    #     the same step `P14` took, and for the same reason (its own worst case, not C63's 1.7x).
    # ⚠ ** AND THE DECLARATION IS THE SYMPTOM'S FIX, NOT THE CAUSE'S.  `check_receipts_run` offers both:
    #   "with its MEASURED cost beside it, OR repair it." **  The repair is in this receipt's own file and
    #   is NOT this seat's: `INNER = 600` EQUALS the outer cap, so the inner guard can never fire before
    #   the outer runner kills the receipt -- it is guaranteed invisible, which is exactly what r7025
    #   found the hard way.  Setting `INNER` well below the declared budget would let it fire and NAME the
    #   pathological tightened child instead.  *Routed to `70`, whose file it is; the declaration below
    #   stops the red in the meantime and does not pretend to be the cure.*
    'Q1_a_stated_tolerance_is_a_request_and_the_corpus_answers_it.py': 900,  # measured 54.8s cold / 37.1s warm, and 37.1s under 3 competing loads -- no contention spread; 900s covers its own INNER=600 bound
}
# ⌗ ** AND ONE OBSERVATION RECORDED RATHER THAN EXPLAINED, r4564. **  In the run that first showed
# `C63` at 525s, `Q1_a_stated_tolerance_is_a_request_and_the_corpus_answers_it.py` hit the 600s cap --
# after five consecutive suite runs at 45-47s, and it runs standalone in 35s.  It did NOT recur on the
# next full chunk (50s, PASS).  *No mechanism was established: CPU threading is ruled out (both files
# measure user/real ~1.1, so neither is meaningfully parallel) and so is memory (16 GB total, 14 GB
# free, no swap).*  ⇒ ** Written down because a one-off 13x overrun with no cause found is worth the
# next reader's suspicion, and because the honest record of a thing that happened once is "once", not
# "flake" and not silence. **  If it returns, the first suspect is this entry's own subject: `C63`
# holds a `--jobs` slot for ~9 minutes of continuous subprocess work.


def registered():
    """the receipts INDEX.md registers, in file order -- AND what it names but cannot resolve

    Returns `(paths, unresolved)`.

    ** r2555: the paper column is CASE-SENSITIVE here and the geometric core is written `p0`
    lowercase, so this runner skipped TWELVE receipts -- the fourth instance of the silent-discard
    class (c54.203 fixed check_receipts and make_receipt_appendix; the duplicate dict key at r2552
    and check_currency's parser at r2550 were the others). **
      ⇒ ** A runner that skips a receipt leaves NO trace: the receipt simply never runs, and a green
        run means nothing about it. **

    ** ⛭⛭ c54.222 -- THE FIFTH INSTANCE, AND THE FILTER IS NOW GONE RATHER THAN PATCHED AGAIN. **  The
    predicate decided membership by the PAPER column, and the corpus writes an EM-DASH there for a
    receipt that supports no paper: ** TWENTY rows dropped, EIGHTEEN naming a file on disk, none of
    them ever run by this gate -- and one of the eighteen FAILS. **  It lives once now, in
    `corpus/index_rows.py`, with the four earlier patches folded in; see that file's head.

    ** ⛔ AND THE SECOND HALF OF THE SAME SILENCE: A FAILING `os.path.exists` WAS A `continue`. **
    Four registered rows name `storyboard_receipts/...` at the repository ROOT, which this function
    prepended `receipts/` to and then dropped; two more name files that have never existed in any
    commit.  *** Unresolvable is RETURNED now, and the caller reports it.  A runner permitted to
    silently not-run a registered receipt is not a gate. ***
    """
    seen, out, unresolved = set(), [], []
    for r in index_rows.rows(resolve_paths=True, root=ROOT):
        if not r.runnable:
            continue                      # a `.md` kill record is registered and is not runnable
        if not r.paths:
            unresolved.append((r.lineno, r.token))
            continue
        for f in r.paths:
            if f not in seen:
                seen.add(f)
                out.append(f)
    return out, unresolved


# ---------------------------------------------------------------- r4008
# ** ONE THREAD PER RECEIPT, BECAUSE A WALL-CLOCK CAP ON AN OVERSUBSCRIBED MACHINE MEASURES THE
#    SCHEDULER AND NOT THE RECEIPT. **
# `subprocess.run` inherited this process's environment, so every child was free to open as many
# BLAS/OpenMP threads as there are cores WHILE `--jobs N` was already running N of them.  The
# machine was oversubscribed by construction and each receipt's measured time was a fact about
# what happened to be running beside it.
#   ⛔ *** MEASURED, AND IT IS NOT A SMALL EFFECT. ***  The same tree, the same cap, two runs
#       differing only in whether C59 was allowed to finish:
#           C1  398s -> 493s   (+24%)
#           H1  423s -> OVER 600s, filed SLOW   (+42% at least)
#       ** H1 passed in one run and was killed in the next without one line of it changing. **
#       C59 is multithreaded -- 25:36 of CPU in 18:43 of wall on the solo probe -- so allowing it
#       to run pushed two neighbours over a cap that is supposed to describe them.
#   ⇒ ** A budget applied to a quantity that depends on what else is running is not a budget. **
#     Pinning to one thread each makes `--jobs N` mean N cores, and makes a receipt's time a
#     property of the receipt.  *This is the contaminated-measurement failure the corpus already
#     names, living inside the instrument that does the measuring.*
_ONE_THREAD = {
    'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1', 'MKL_NUM_THREADS': '1',
    'NUMEXPR_NUM_THREADS': '1', 'VECLIB_MAXIMUM_THREADS': '1',
}


# ---------------------------------------------------------------- r6977+70.1
# ** LONGEST FIRST, BECAUSE A FIXED POOL FINISHES WHEN ITS LAST RECEIPT DOES. **  In INDEX order the
# longest receipts start wherever the registry happens to put them -- `P15_the_low_multipole_floor...`
# (995s) sat at 820 of 868 -- and become the tail.  Simulated on the r6975 suite's own per-receipt times,
# four workers, reproducing that run's wall exactly: INDEX order 2,993s, longest-first 2,686s, which is
# perfect packing (the floor is total/4 = 2,686s; C59 alone is 1,270s).  ** 307s, 10%, and no receipt
# changes. **
#   ⛔ AND ONE INTERACTION, MEASURED, WHICH IS WHY IT IS NOT A PLAIN SORT.  Under `--wall W` a receipt
#   longer than W can never finish inside the invocation (in-flight work is abandoned at the budget).
#   Sorted longest-first, the four longest are all longer than 500s, so they take every worker at t=0 of
#   EVERY slice and nothing finishes: simulated, `--wall 500` makes no progress at all.  So receipts
#   expected to exceed the wall go LAST.  Simulated at W = 300 / 500 / 900: INDEX order leaves 694 / 51 /
#   3 unfinished before it stalls, this order 10 / 5 / 3 -- exactly the receipts longer than the wall,
#   which need one unbounded invocation under either order (as before).  The resume cache is keyed by
#   path at a digest, so the order cannot change what it holds -- only how soon.
# ⌗ The expected time is the READ INDEX's traced seconds (`receipts/READ_INDEX.json`, `s`), else the
#   declared LONG budget, else 0; no index, INDEX order.  Stable, so ties keep INDEX order.
def expected_seconds():
    try:
        with open(os.path.join(ROOT, 'receipts', 'READ_INDEX.json')) as fh:
            return {k: v.get('s') or 0 for k, v in json.load(fh)['receipts'].items()}
    except (OSError, ValueError, KeyError):
        return None


def schedule(files, wall=0):
    exp = expected_seconds()
    if exp is None:
        return files, 'INDEX order (no READ_INDEX.json)'
    t = lambda f: exp.get(os.path.relpath(f, ROOT)) or LONG.get(os.path.basename(f), 0)
    return (sorted(files, key=lambda f: (bool(wall) and t(f) > wall, -t(f))),
            'longest first by READ_INDEX.json' + (f', those over the {wall}s wall last' if wall else ''))


def budget(path, default):
    """The per-file timeout: the declared one if this receipt has it, else the global cap."""
    return LONG.get(os.path.basename(path), default)


# ⛭ r7019 (70.1) ⓵: A RECEIPT KILLED AT ITS BUDGET KEEPS WHAT IT SAID BEFORE THE KILL.  Until now `SLOW`
#   carried only "exceeded Ns", so `Q1`'s ten suite timeouts (09-28/09-29) recorded nothing of where each one
#   had got to.  ** The same rule, sizes and child environment as the two sweep instruments, through ONE
#   definition (`sweep_tolerances`: `keep_output`, `output_lines`, `CHILD_ENV`), so the three cannot drift. **
#   ⚠ The child is UNBUFFERED because a timeout is cut at the kill and not at an exit: block-buffered, a
#   receipt that printed 2 KB and hung kept nothing (measured, and beside `CHILD_ENV`).
#   ⌗ The kept lines print under the `[slow]` line, tagged and indented eight spaces, so no parser of this
#   output can read one as the runner's own `[FAIL]`/`[slow]` line (four spaces, anchored in
#   `check_receipts_run` and `red_carry`).
def _st():
    import importlib.util
    spec = importlib.util.spec_from_file_location('sweep_tolerances', os.path.join(HERE, 'sweep_tolerances.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


_ST = _st()


def run_one(path, timeout):
    d, b = os.path.dirname(path), os.path.basename(path)
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, b], cwd=d, capture_output=True,
                           text=True, errors='replace', timeout=timeout,
                           env=dict(os.environ, **_ONE_THREAD, **_ST.CHILD_ENV))
        dt = time.time() - t0
        if r.returncode == 0:
            return ('PASS', path, dt, '')
        tail = [l for l in (r.stdout + r.stderr).split('\n') if l.strip()][-3:]
        return ('FAIL', path, dt, ' / '.join(tail)[:300])
    except subprocess.TimeoutExpired as e:
        kept = _ST.output_lines(_ST.keep_output(_ST._text(e.stdout), _ST._text(e.stderr)))
        return ('SLOW', path, time.time() - t0, '\n'.join([f'exceeded {timeout}s'] + kept))
    except Exception as e:                                     # noqa: BLE001
        return ('FAIL', path, time.time() - t0, f'{type(e).__name__}: {e}'[:300])


class Cache:
    """per-receipt results at ONE tree digest, written as each receipt finishes

    *A cache that survives a kill is the whole point, so it is rewritten on every completion
    rather than at the end -- 712 short rows, and the cost is invisible beside a receipt run.*
    """

    def __init__(self, paths, digest):
        names = [p for p in (paths or '').split(',') if p]
        self.path = names[0] if names else ''
        self.digest, self.lock = digest, threading.Lock()
        # ⛔⚭ r4554 (node 60): ** THE WALL FIGURE GREW WHEN NOTHING RAN, AND IT WAS MINE. **
        #   `invocations` and `wall` were SCALARS summed across every resume file -- and the
        #   assembled total is written back into the FIRST file, so the next assembly read that
        #   total and added the second file's share to it AGAIN.
        #     ⇒ *Measured: two invocations that actually ran anything, 780s + 1208s = 1988s.  After
        #       three no-op re-assemblies `RUN_RESULT.txt` read ** 5 INVOCATION(S), 3196s ** -- a
        #       number that grew with how many times the command was typed.*
        #   ⌗ ** A figure in this file is a claim about a RUN, and this one had become a claim about
        #     my shell history. **  Totals are now a MAP of invocation id -> (wall, measured), so
        #     merging is a union and re-reading is idempotent by construction rather than by care.
        self.results, self.invs, self.legacy = {}, {}, []
        self.reused = 0
        for i, path in enumerate(names):
            if not os.path.exists(path):
                continue
            try:
                d = json.load(open(path, encoding='utf-8'))
            except (ValueError, OSError):
                d = {}
            if d.get('digest') == digest:
                self.results.update(d.get('results', {}))
                self.invs.update({k: list(v) for k, v in (d.get('invs') or {}).items()})
                if 'invs' not in d and (d.get('invocations') or d.get('wall')):
                    # ⛔ A PRE-r4554 CACHE'S TOTALS ARE THE DEFECT ITSELF and are NOT folded in.
                    #   Its per-receipt results are measurements and are kept; its `wall` and
                    #   `invocations` are whatever the double-counting had reached by the last
                    #   time it was written, so carrying them forward would launder the very
                    #   number this revision found wrong.  ⇒ *The results survive; the totals are
                    #   dropped and SAID to be dropped, because a total that silently omits real
                    #   minutes is the same kind of lie as one that invents them.*
                    self.legacy.append((path, d.get('invocations'), d.get('wall')))
            elif d:
                print(f"  ⌗ resume cache {path} discarded: it was taken against tree "
                      f"{d.get('digest')!r}, not {digest} -- a result measured on another tree "
                      f"is not a result about this one")
        self.reused = len(self.results)

    def get(self, rel):
        r = self.results.get(rel)
        return (r[0], os.path.join(ROOT, rel), float(r[1]), r[2]) if r else None

    def put(self, st, path, dt, msg):
        """⛔⚭ r6476 (node 60): ** THIS DISCARDED EVERY RESULT WHEN NO `--resume` WAS GIVEN. **

        *It read `if not self.path: return` -- so an invocation without a cache path ran every
        receipt, measured every one, and then threw all of it away.*  `res` came back empty, the
        failure loop printed nothing, the verdict line read ** `0 pass, 0 fail, 0 over timeout` **
        and the run exited 0 under:

            "Every registered receipt runs, in place, and exits 0 -- so every assertion in the
             reproducibility layer was actually evaluated."

        *** AND `.github/workflows/gates.yml` INVOKES IT WITH NO `--resume`. ***  ** So the heavy
        job has been spending half an hour running the suite and then printing the strongest
        sentence in this file over ZERO measurements ** -- and `check_receipts_run` agreed, because
        it only ever failed on a non-zero failure count and never asked whether the pass count
        covered the registered set.  *The banked `RUN_RESULT.txt` on the trunk is honest only
        because it happens to have been produced by hand WITH `--resume`.*

        ⇒ ** The defect is this runner's own thesis turned on itself. **  It exists to close the
        hole where "a green run is making no claim at all"; here it made no claim and said the
        loudest possible thing.  *Measured rather than reasoned: 735 receipts, 1856s wall, `0 pass,
        0 fail`, exit 0.*

        ⌗ The fix is that RESULTS ARE ALWAYS KEPT and only the DISK WRITE is conditional -- the
        path was never about whether a result counts, only about where it survives a kill.
        """
        with self.lock:
            self.results[os.path.relpath(path, ROOT)] = [st, dt, msg]
            if self.path:
                self._write()

    def _write(self):
        tmp = self.path + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as fh:
            json.dump({'digest': self.digest, 'invs': self.invs,
                       'results': self.results}, fh)
        os.replace(tmp, self.path)


def tree_digest():
    """A digest of everything a receipt can check: the papers it quotes and the receipts themselves.

    ** Deliberately NOT the git HEAD. **  Requiring an exact-HEAD match would fail the gate on every
    commit that touches a register file, which trains the caller to skip it; hashing only what a
    receipt can actually READ fails exactly when the result could have gone stale and at no other
    time.  The digest is over content, so a revert restores the old digest and the cached run is
    valid again -- which is correct, because it is.
    """
    h = hashlib.sha256()
    for pat in ('corpus/*.tex', 'receipts/**/*.py', 'computations/**/*.py'):
        for f in sorted(glob.glob(os.path.join(ROOT, pat), recursive=True)):
            h.update(os.path.relpath(f, ROOT).encode())
            h.update(open(f, 'rb').read())
    return h.hexdigest()[:16]


def main():
    ap = argparse.ArgumentParser()
    # ** r3997: default raised 300 -> 600.  A cap that kills a receipt and files it as a
    #   FAILURE is manufacturing failures, and three receipts were being failed by the cap
    #   alone.  The slowest receipt that PASSES takes 163s, so there is a 137s gap with
    #   nothing in it: raising the cap cannot mask a slowdown in anything currently green,
    #   because nothing green is near it.  ** Measure, then decide -- not defer. **
    ap.add_argument('--timeout', type=int, default=600)
    ap.add_argument('--jobs', type=int, default=max(1, (os.cpu_count() or 4) - 2))
    ap.add_argument('--only', default='')
    # r6977+70.1: the SCOPED suite -- exactly the receipts `receipt_scope.py --list` wrote, one per line
    ap.add_argument('--from', dest='frm', default='', help='run only the registered receipts listed in FILE')
    ap.add_argument('--quick', action='store_true')
    # ⌗ *`--resume a.json,b.json` reads every cache named and WRITES ONLY THE FIRST.*  The one
    #   receipt declared LONG (C59, measured 1302s) is longer than any foreground tool call this
    #   line can make, so it runs in its own invocation against its own cache while the rest run in
    #   bounded ones -- and the final invocation reads both.  ** A union of per-receipt results
    #   taken at the SAME digest is one run's worth of evidence; taken at different digests it is
    #   nothing, which is why the digest gates every cache separately. **
    ap.add_argument('--resume', default='', help='JSON cache(s), comma-separated; the first is written')
    ap.add_argument('--skip', default='', help='substring filter: EXCLUDE paths containing it')
    ap.add_argument('--wall', type=int, default=0, help='stop cleanly after N seconds')
    a = ap.parse_args()

    files, unresolved = registered()
    if a.only:
        files = [f for f in files if a.only in f]
    if a.frm:
        _listed = {l.strip() for l in open(a.frm) if l.strip()}
        files = [f for f in files if os.path.relpath(f, ROOT) in _listed]
        print(f"\n  ⌗ SCOPED: {len(files)} registered receipt(s) from {a.frm}"
              + (f" ({len(_listed) - len(files)} listed and not registered)" if len(_listed) > len(files) else "")
              + " -- a verdict below is about THESE, not the suite")
    if a.skip:
        files = [f for f in files if a.skip not in f]
    if a.quick:
        files = [f for f in files if not any(s in f for s in SLOW)]
    print()
    print(f"  RUN-ALL-RECEIPTS -- {len(files)} registered receipt(s), {a.jobs} at a time, "
          f"{a.timeout}s each, each from ITS OWN DIRECTORY")
    for _b, _t in sorted(LONG.items()):
        if any(os.path.basename(f) == _b for f in files):
            print(f"  DECLARED LONG: {_b} runs on {_t}s, not {a.timeout}s -- named, with its "
                  f"measured cost in the source")
    # r2656+c54.208: the result of this run is CACHED and read by check_receipts_run.  A cache with
    # no expiry is a green verdict about a tree that no longer exists -- the file on disk at r2419
    # was still being read as current at r2656, 294 commits later, and reported "no receipt fails
    # for a reason inside the corpus" while 24 did.  So the run stamps WHAT IT RAN AGAINST.
    _digest = tree_digest()
    print(f"  TREE-DIGEST: {_digest}")
    print()
    t0 = time.time()
    cache = Cache(a.resume, _digest)
    _inv = uuid.uuid4().hex[:12]          # this invocation's own id (r4554)
    todo = [f for f in files if cache.get(os.path.relpath(f, ROOT)) is None]
    todo, _order = schedule(todo, a.wall)
    print(f"  ORDER: {_order}")
    if a.resume:
        print(f"  RESUME: {len(files) - len(todo)} result(s) reused from {a.resume}, "
              f"{len(todo)} left to run"
              + (f", stopping cleanly at {a.wall}s" if a.wall else ""))
        print()
    incomplete = []
    if a.wall:
        # ** A BUDGET THAT STOPS THE RUNNER IS NOT THE SAME AS ONE THAT KILLS IT. **  Futures not
        # yet started are cancelled and the invocation reports what it did NOT reach by name, so
        # "incomplete" is a stated outcome rather than a truncated file.
        from concurrent.futures import as_completed
        ex = ThreadPoolExecutor(max_workers=a.jobs)
        fut = {ex.submit(run_one, f, budget(f, a.timeout)): f for f in todo}
        deadline = t0 + a.wall
        try:
            for f_ in as_completed(list(fut), timeout=max(1.0, deadline - time.time())):
                cache.put(*f_.result())
        except Exception:                                      # noqa: BLE001  (TimeoutError)
            pass
        for f_, src in fut.items():
            if f_.done() and not f_.cancelled():
                try:
                    cache.put(*f_.result())
                except Exception:                              # noqa: BLE001
                    pass
            else:
                f_.cancel()
                incomplete.append(src)
        ex.shutdown(wait=False, cancel_futures=True)
    else:
        with ThreadPoolExecutor(max_workers=a.jobs) as ex:
            for r in ex.map(lambda f: run_one(f, budget(f, a.timeout)), todo):
                cache.put(*r)
    # ⛭ r4554: record THIS invocation under its own id, with how many receipts it actually
    #   measured.  A re-assembly that measures nothing still costs a second or two and is recorded
    #   as such -- what it can no longer do is inherit another invocation's minutes.
    cache.invs[_inv] = [time.time() - t0, len(todo) - len(incomplete)]
    if a.resume:
        cache._write()
    res = [cache.get(os.path.relpath(f, ROOT)) for f in files]
    res = [r for r in res if r is not None]
    if incomplete:
        print(f"  ⛔ INCOMPLETE: this invocation stopped at its {a.wall}s budget with "
              f"{len(incomplete)} receipt(s) not reached.  ** Run it again with the same "
              f"--resume cache; nothing already measured is re-run. **")
        for f_ in sorted(incomplete)[:8]:
            print(f"      not reached: {os.path.relpath(f_, ROOT)}")
        if len(incomplete) > 8:
            print(f"      ... and {len(incomplete) - 8} more")
        print()
    ok = [r for r in res if r[0] == 'PASS']
    slow = [r for r in res if r[0] == 'SLOW']
    bad = [r for r in res if r[0] == 'FAIL']
    for st, p, dt, msg in sorted(bad, key=lambda r: r[1]):
        print(f"    [FAIL] {os.path.relpath(p, ROOT)}  ({dt:.0f}s)")
        print(f"           {msg}")
    for st, p, dt, msg in sorted(slow, key=lambda r: r[1]):
        first, *kept = msg.split('\n')
        print(f"    [slow] {os.path.relpath(p, ROOT)}  -- {first}")
        for l in kept:
            print(l)
    print()
    _wall = sum(v[0] for v in cache.invs.values()) if a.resume else time.time() - t0
    _measured = [k for k, v in cache.invs.items() if v[1]]
    print(f"  {len(ok)} pass, {len(bad)} fail, {len(slow)} over timeout, "
          f"in {_wall:.0f}s wall")
    if a.resume:
        # *The verdict line above must not be read as one elapsed clock when it is not one.*
        print(f"  ⌗ ASSEMBLED ACROSS {len(cache.invs)} INVOCATION(S) AT THIS DIGEST, "
              f"{len(_measured)} OF WHICH MEASURED ANYTHING: {cache.reused} result(s) reused, "
              f"{len(res) - cache.reused} measured here.  Every receipt ran exactly once against "
              f"tree {_digest}, and the cache is discarded whole the moment that digest changes.  "
              f"The wall figure is the SUM of the invocations, not a single elapsed clock -- and "
              f"it is a UNION over invocation ids, so re-assembling adds only the seconds that "
              f"re-assembly itself costs (r4554: it used to add another invocation's minutes).")
        for _p, _i, _w in cache.legacy:
            print(f"  ⛔ {_p} is a PRE-r4554 cache: its {_i} invocation(s)/{float(_w or 0):.0f}s "
                  f"were written by the double-counting this revision fixed, so its RESULTS are "
                  f"used and its TOTALS are discarded.  ** The wall figure above therefore OMITS "
                  f"that time and is a LOWER BOUND -- re-run from a fresh cache for a true one. **")
    if ok:
        worst = sorted(ok, key=lambda r: -r[2])[:5]
        print("  slowest that passed: "
              + ", ".join(f"{os.path.basename(p)} {dt:.0f}s" for _, p, dt, _ in worst))
    # ** c54.222: an UNRESOLVABLE row is reported HERE, next to the failures, and it fails the gate
    # even when every file that does exist passes. **  *A registry entry naming nothing is not a
    # smaller defect than a receipt that exits 1 -- it is the same defect one step earlier, and it
    # was the one with no reader.*
    if unresolved and not (a.only or a.frm):
        print()
        print(f"  ⛔ {len(unresolved)} REGISTERED ROW(S) NAME A `.py` THAT DOES NOT EXIST:")
        for lineno, tok in unresolved:
            print(f"    [FAIL] receipts/INDEX.md line {lineno}: {tok}")
        print("    ⇒ Searched `receipts/<path>` AND `<path>` from the repository root, globbed.")
        print("      ** A row is a claim that a computation exists.  An unresolvable row is a false")
        print("      one, and it is printed into the reproducibility appendix as `[OK]`. **")
    if incomplete:
        print()
        print("  ⛔ THIS RUN IS NOT A VERDICT: receipts were not reached.  Re-invoke with the same")
        print("     --resume cache until it reports none.")
        return 2
    if bad or (unresolved and not (a.only or a.frm)):
        print()
        print("  ⛔ A REGISTERED RECEIPT THAT DOES NOT RUN WHERE IT IS REGISTERED IS NOT A RECEIPT.")
        return 1
    # ⛭ r6476 (node 60): ** THE VERDICT BELOW IS A CLAIM ABOUT EVERY REGISTERED RECEIPT, so it is
    #   not printed unless the results ACCOUNT FOR EVERY ONE. **  *Before this, a run that measured
    #   nothing at all reached it: `0 pass, 0 fail` satisfies "no failures" vacuously, and the
    #   sentence below then asserted that every assertion in the layer had been evaluated.*
    #     ⇒ A count is not a coverage.  ** `0 fail` is the same claim as `0 pass` when nothing ran,
    #       and only one of those two numbers can tell them apart. **
    if len(res) != len(files):
        print()
        print(f"  ⛔ THIS RUN IS NOT A VERDICT: {len(res)} result(s) for {len(files)} registered")
        print(f"     receipt(s) -- {len(files) - len(res)} unaccounted for.  ** No failure was")
        print("     reported because no result was, which is a different thing from green. **")
        return 2
    print()
    if a.frm:
        print(f"  Every receipt IN THIS SCOPE ({len(files)} of the registered set) runs, in place, and exits 0.")
        print("  ** A claim about the scope and not the suite: the suite's verdict is the heavy job's. **")
        return 0
    print("  Every registered receipt runs, in place, and exits 0 -- so every assertion in the")
    print("  reproducibility layer was actually evaluated.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
