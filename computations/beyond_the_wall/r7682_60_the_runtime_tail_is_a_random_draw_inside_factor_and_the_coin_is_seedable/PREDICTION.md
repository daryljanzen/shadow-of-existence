# r7682 (60) — REGISTRATION, BEFORE THE A/B DISTRIBUTION IS READ

**Order:** `r7679+1` (69), routed to this seat because **this seat's own stop condition fired**.

> `P15_the_four_dimensional_treatment_keeps_the_economy…` crossed its **900 s** budget on main's
> scoped suite at `f74bb3324`: 341 pass, 0 fail, 1 over timeout. 60's `r7188+60` entry in
> `scripts/run_all_receipts.py` says that if it crosses 900 s, *"the cause is not cost, and the
> right response is to find the cause rather than to raise this number again"*. I have not raised
> it. … **Find the cause on the runner's terms.** Is the scoped suite running it under the read
> trace, and does `simplify` blow up there? Then make the cheaper canonicalisation the entry names,
> or show why not.

**The tree and the machine are named in `runs/TREE.txt`.**

---

## ⌗ WHAT WAS ALREADY FOUND BEFORE THIS REGISTRATION — every line of it a measurement

This revision registers **one** arm, the A/B distribution, because the diagnosis was already done
when the registration was written. Everything below is reported as *found*, with how, so that the
registration cannot be read as predicting what it already knew.

- ⓐ **The budget was 900 s and the kill was at 900 s.** The runner's own log prints
  `[slow] … -- exceeded 900s`, so `LONG`'s 900 beat the step's `--timeout 600`, as `budget()` says
  it does.
- ⓑ **69's read-trace hypothesis is FALSE.** The scoped suite's step is
  `run_all_receipts.py --from scope.txt --jobs 4 --timeout 600` and nothing else; the tracing lives
  in the *runner-read sweep* and the *index* jobs, which are different jobs on different runners.
  The suite's child environment is `_ONE_THREAD` plus `CHILD_ENV = {'PYTHONUNBUFFERED': '1'}` —
  read out of `run_all_receipts.run_one` and `sweep_tolerances`.
- ⓒ **Five candidate causes ELIMINATED by measurement, each held fixed:**
  **(1) library versions** — sympy 1.14.0, numpy 2.4.6, scipy 1.17.1, mpmath 1.3.0 here, each equal
  to `requirements-ci.txt`'s pin; **(2) the child environment** — 13.6 s plain against 11.1 s under
  the suite's own env; **(3) `NODE`** — the receipt contains no `NODE`, `environ` or `getenv` at
  all, so it cannot branch on who runs it; **(4) memory** — peak RSS **59 MB** and **0 major page
  faults** on a fast run, so four copies are 236 MB and no runner swaps for that; **(5) hash
  ordering** — 69 already swept `PYTHONHASHSEED` 0–7 at 10–11 s each.
- ⓓ **It is CPU-bound:** `user 10.3 s` against `wall 10.5 s`.
- ⓔ **The cost is localised to ONE loop, by timing the receipt's own output lines:** the docstring
  and section Ⓐ take `0.59 s`; Ⓑ's three reductions take `1.31`, `3.01` and `4.64 s`; Ⓒ, Ⓓ and the
  verdict take `0.33 s`. ⇒ **Ⓑ's `ell` loop is 8.96 s of 9.88 s, 91 per cent.** And the runner died
  **after printing `ell=1` and before printing `ell=2`**, which its kept tail shows — so it spent
  **more than 900 s inside a step that costs 3.01 s here, ≥ 183×.**
- ⓕ **THE TAIL REPRODUCES ON AN IDLE MACHINE, so contention is not the cause.** One fresh process,
  nothing else running, load 1.00 on 4 CPUs: **546 s and still running**, RSS grown to **178 MB**
  from the 59 MB of a fast run. ⌗ *This falsifies the explanation the `r7188` entry itself rests
  on — a `7.5×` four-way contention spread — because the excursion needs nothing beside it.*
- ⓖ **AND THE CAUSE IS NAMED, CAUGHT IN THE ACT.** Sixty trials under
  `faulthandler.dump_traceback_later(45, repeat=True)`: nine at 9–12 s, then **one at 45 s and one
  at 135 s**, and every slow trial stalled in the same place:
  ```
  receipt.py:196 radial  →  simplify  →  trigsimp  →  futrig  →  _futrig  →  _eapply
                         →  factor  →  _generic_factor  →  factor_list  →  dmp_factor_list
                         →  dmp_zz_factor  →  dmp_zz_wang  →  dmp_zz_wang_hensel_lifting
                         →  dmp_expand  →  dmp_mul (deep)  →  dmp_add
  ```
  `dmp_zz_wang` is Wang's multivariate factorisation; its signature is
  `dmp_zz_wang(f, u, K, mod=None, seed=None)` and it draws its evaluation points from
  `sympy.core.random`'s `_randint`, retrying on an unlucky draw. ⇒ **The receipt's runtime is a
  RANDOM DRAW inside `factor`, reached from a nested `simplify` the receipt's own line 196 makes —
  and the draw is invisible to a `PYTHONHASHSEED` sweep, because it is not hashing.**
- ⓗ **Two cheaper canonicalisations were tried and BOTH are worse, measured, and both are reported
  rather than hidden:** `trigsimp(…, method='fu')` is **verdict-identical and 107 s** — ten times
  the median; `cancel(expand(…rewrite(exp)))` **did not finish in 600 s**, reaching `ell=2` and no
  further. ⌗ *So "make the cheaper canonicalisation the entry names" has an answer: the entry's own
  guess at the cure does not work, and the reason is that the expense is not the trig chain itself
  but one random draw inside it.*
- ⓘ **The candidate cure is ONE LINE and it is verdict-identical on a first reading:** seeding
  `sympy.core.random` at the top of the receipt. Three runs at 10 s, and the whole printed output
  **byte-identical to the unpatched baseline** but for the wall time it prints. Nothing
  mathematical moves: the factorisation is exact whichever points it picks.

---

## PART 1 — THE ONE REGISTERED ARM, AND THE METHOD, FIXED BEFORE IT IS READ

**THE A/B DISTRIBUTION.** `30` trials of the receipt **unpatched**, then `30` of the receipt with the
seed line, **sequential, one process at a time, cores otherwise idle**, the same child environment
and the same `900 s` cap on each. The harness writes each trial's exit code and wall as it
completes, so a killed trial is recorded and not lost.

- **① THE TAIL.** The two arms' min / median / max wall, and the count of trials over `60 s` in
  each. ⌗ *Registered as a comparison with NO predicted value: this seat's own entry said a later
  seat wanting to tighten the budget "needs the distribution and not another single reading", and
  this is that distribution.*
- **② THE VERDICT TEXT.** Whether the patched receipt's whole printed output stays identical to the
  unpatched baseline across every trial that completes, modulo the one line that prints its own
  wall time.
- **③ THE EXIT CODES.** Recorded, not interpreted: two trials under the stall probe exited `139`
  (`SIGSEGV`), which may be the probe's traceback dump and not the receipt, so the plain arm's exit
  codes decide it. ⌗ *Registered explicitly because a segfault in a landed receipt would be a
  different finding from a slow one, and the measurement that separates them is this one.*

**⛔ The reachable negative:** the seeded arm shows the same tail as the unpatched one, which would
mean the draw is not the cause and the `900 s` entry was right for a reason not yet found.
⌗ *Registered as reachable so that reaching it is a result and not a silence.*

**⌗ WHAT THIS REVISION WILL NOT DO.** It will not raise the budget — the entry forbids it and the
order repeats the forbidding. It will not change a single assertion, a single tolerance or a single
printed figure of a merged, reviewed receipt: the only admissible change is one that leaves the
whole output identical, and arm ② is what holds that.
