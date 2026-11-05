# r7682 (60) — RESULT: the runtime tail is a random draw inside `factor`, and the coin is seedable

**Order:** the item `69` routed inside `r7679` (`r7679+1`), **because this seat's own stop condition
fired** — `P15_the_four_dimensional_treatment…` crossed the `900 s` budget `r7188+60` gave it, on
main's scoped suite at `f74bb3324`, and that entry says in its own words that crossing `900 s` is
*"evidence the cause is not cost, and the right response is to find the cause rather than to raise
this number again"*.
**Tree and machine:** `runs/TREE.txt` — worktree `2bd74b0c…`, HEAD `449d2881`, base `083fa947`;
4 CPUs, every trial with the cores otherwise **idle** and **one process at a time**.
**Registered before the distribution was read:** `PREDICTION.md`, on its own commit, pushed on #635.

> ### ⛭⛭⛭ THE RECEIPT'S RUNTIME IS A COIN FLIP INSIDE `factor`. ⛭⛭⛭
> **Not contention, not the read trace, not the hash seed, not memory, not the environment, not the
> cost of the trig chain. One random draw, in Wang's multivariate factorisation, reached from a
> nested `simplify` on the receipt's own line 196 — and the cure is one line that seeds it.**

**THE BUDGET IS NOT RAISED AND NOT ONE PRINTED FIGURE MOVES.** The receipt is merged, reviewed work;
the only admissible change was one that leaves its whole output identical, and arm ② holds that.

---

## THE ONE REGISTERED ARM — ① THE TAIL

`30` trials each way, sequential, one process at a time, cores idle, the scoped suite's own child
environment, a `900 s` cap on each — the very cap the runner hit. Raw readings in `runs/ab.txt`,
harness in `ab.sh`.
⌗ *`UNSEEDED` here is the registration's `unpatched` arm, renamed only because the cure is now the
  receipt and the comparison arm is the file built by stripping it out.*

| | min | median | max | spread | over `60 s` | killed at `900 s` | exit codes |
|---|---|---|---|---|---|---|---|
| **UNSEEDED** | `10 s` | `11 s` | **`900 s`** | **`90.0×`** | **7 of 30** | **4 of 30** | `0`, `124` |
| **SEEDED** | `10 s` | `11 s` | `12 s` | `1.2×` | **0 of 30** | **0 of 30** | `0` |

The unseeded arm's whole sorted sequence: `10` thirteen times, `11` ten times, then
`66`, `68`, `186`, `900`, `900`, `900`, `900`. **The distribution is not heavy-tailed around a
drifting mean — it is a sharp mode with a handful of excursions**, which is the signature of a draw
that is usually lucky, and it is why eight single readings in a row can all say `11 s` while the
runner dies.

⇒ **The registered negative is NOT reached:** the seeded arm shows **no tail at all**. Four of
thirty unseeded trials hit the cap on an idle machine; none of thirty seeded ones exceeded `12 s`.

## ② THE VERDICT TEXT — **20 OF 20 TRIALS IDENTICAL, AND SO IS THE SLOW ONE**

`runs/ident.txt`, harness `ident.sh`: each trial's whole output kept, its one wall-time line
normalised to `[WALL]`, the rest digested.

| | trials | exit | lines | normalised digest |
|---|---|---|---|---|
| **UNSEEDED** | `10` | all `0` | all `181` | `14479474cb2eec07` — **10 of 10** |
| **SEEDED** | `10` | all `0` | all `181` | `14479474cb2eec07` — **10 of 10** |
| the banked baseline | `1` | `0` | `181` | `14479474cb2eec07` |

**One digest across all twenty-one readings.** Not a line, not a figure, not a verdict, not an
ordering differs — the only byte that moves anywhere in `181` lines is the wall time the receipt
prints about itself.

⌗ **The reading that matters is the slow one.** One unseeded trial in that pass took **`91 s`** — a
genuinely unlucky draw — and its digest is **the same sixteen hex digits** as every fast trial's and
as the banked baseline's. *So the draw moves the runtime and nothing else: an unlucky evaluation
point costs minutes and prints the same verdict.* That is the measurement that licenses the change,
because it is the one that could have forbidden it.

## ③ THE EXIT CODES — THE SEGFAULTS WERE THE INSTRUMENT'S, NOT THE RECEIPT'S

Two trials under the stall probe exited `139` (`SIGSEGV`), and the registration said only the plain
arm could decide whether that belonged to the receipt. **It does not.** Across `60` plain trials the
exit codes are `0` and `124` (`timeout`) and nothing else. The two `139`s are
`faulthandler.dump_traceback_later` dumping a stack that is **thousands of frames deep** —
`dmp_mul` recursing through `densearith` — which is exactly where `runs/stall_traceback.txt` shows
the process sitting. *A segfault in a landed receipt would have been a different and worse finding;
it was registered as its own arm for that reason, and the arm cleared it.*

---

## HOW THE CAUSE WAS FOUND, AND WHAT WAS ELIMINATED TO FIND IT

Everything in this section was measured **before** the registration and is recorded there as *found*
rather than predicted.

**⛔ Six explanations eliminated, each by a measurement with the rest held fixed.**

| explanation | the measurement that kills it |
|---|---|
| the read trace (`69`'s hypothesis) | the scoped suite's step is `--from scope.txt --jobs 4 --timeout 600` and traces **nothing**; the tracing lives in the runner-read sweep and the index, different jobs on different runners |
| library versions | sympy `1.14.0`, numpy `2.4.6`, scipy `1.17.1`, mpmath `1.3.0` — each **equal** to `requirements-ci.txt`'s pin |
| the child environment | `13.6 s` plain against `11.1 s` under the suite's own env — **faster**, not slower |
| `NODE` branching | the receipt contains no `NODE`, `environ` or `getenv` at all, so it **cannot** branch on who runs it |
| memory | peak RSS **`59 MB`**, **0** major page faults; four copies are `236 MB` and no runner swaps for that |
| hash ordering | `69` already swept `PYTHONHASHSEED` `0`–`7` at `10`–`11 s` each |

**⛔ AND THE EXPLANATION THE `r7188` ENTRY ITSELF RESTS ON IS FALSE.** That entry closes by calling a
`7.5×` four-way contention spread *"the missing factor"*. It is not: **the excursion needs nothing
beside it.** One fresh process, cores otherwise idle, load `1.00` on 4 — `546 s` and still running,
RSS grown from `59 MB` to `178 MB`. *A contention explanation cannot survive a reproduction on an
idle machine, and this one does not.* The entry is corrected in place at this revision rather than
left standing.

**⌗ The cost is localised to ONE loop, by timing the receipt's own output lines.** The docstring and
section Ⓐ take `0.59 s`; Ⓑ's three reductions take `1.31`, `3.01` and `4.64 s`; Ⓒ, Ⓓ and the verdict
take `0.33 s`. ⇒ **Ⓑ's `ell` loop is `8.96 s` of `9.88 s`, 91 per cent.** And the runner died
**after** printing `ell=1` and **before** printing `ell=2` — so it spent more than `900 s` inside a
step that costs `3.01 s` here, **a factor of at least 183 on that one step.**

**⛭⛭⛭ AND THE CAUSE IS NAMED, CAUGHT IN THE ACT.** `probe.py` runs each trial under
`faulthandler.dump_traceback_later(45, repeat=True)`, so a slow trial prints **where it is** and a
fast one prints nothing. Eleven trials: nine at `9`–`12 s`, then one at `45 s` and one at `135 s`
(`runs/stall_trials.txt`), and **every slow trial stalled in the same place**
(`runs/stall_traceback.txt`):

```
receipt line 196  radial
  → simplify → trigsimp → futrig → _futrig → minrule → chain_rl → _eapply
  → factor → _generic_factor → _symbolic_factor → _symbolic_factor_list → factor_list
  → dmp_factor_list → dmp_zz_factor → dmp_zz_wang → dmp_zz_wang_hensel_lifting
  → dmp_expand → dmp_mul (six deep) → dmp_add
```

`dmp_zz_wang` is **Wang's multivariate factorisation**. Its signature is
`dmp_zz_wang(f, u, K, mod=None, seed=None)`, it draws its evaluation points from
`sympy.core.random`'s `_randint`, and it **retries on an unlucky draw** — a draw that decides how
large the Hensel lifting's intermediate expansion gets.

⇒ ***THE RUNTIME IS A RANDOM DRAW, AND THE DRAW IS INVISIBLE TO EVERY INSTRUMENT ALREADY POINTED AT
IT.*** A `PYTHONHASHSEED` sweep cannot see it, because it is not hashing. A single reading cannot see
it, because the mode is `11 s`. A contention measurement cannot see it, because it needs no
competitor. *Three instruments agreed on the wrong answer because none of them was measuring a coin.*

## WHAT THE ENTRY'S OWN GUESS AT THE CURE DOES — BOTH CHEAPER ROUTES ARE WORSE

The `r7188` entry says the cost *"is concentrated in nested `simplify` over trig in one function, so
a cheaper canonicalisation there is the probable cure"*, and the order repeats it: *"make the cheaper
canonicalisation the entry names, or show why not."* **Here is why not, measured:**

| candidate | verdict | wall |
|---|---|---|
| `trigsimp(…, method='fu')` | **identical** | `107 s` — **ten times the median** |
| `cancel(expand(…rewrite(exp)))` | — | **did not finish in `600 s`**, reaching `ell=2` and no further |
| **seeding `sympy.core.random`** | **identical** | `10`–`12 s`, `1.2×` spread |

⇒ **The entry's guess is wrong for a reason worth keeping: the expense is not the trig chain. It is
one draw inside it.** Replacing the chain with a cheaper one keeps the draw, or loses the
canonicalisation the gates need — and the receipt's assertions are equalities on canonical forms, so
a weaker canonicaliser is not a cheaper route to the same verdict but a different verdict.

## WHAT IS CHANGED, AND WHAT IS NOT

- **The receipt gains one import, one comment block and one call:** `_sprandom.seed(20260105)`,
  immediately after `import sympy as sp`. *It changes no mathematics — the factorisation is exact
  whichever points it picks — and arm ② holds that the whole printed output is unmoved.* It makes the
  draw a property of **this receipt** instead of a property of **the process**, which is the
  difference between a verification and a lottery ticket.
- **The `r7188+60` entry is corrected**, in place, with the falsified contention explanation marked
  false rather than deleted, the cause recorded, the distribution recorded, and the stop condition
  marked **DISCHARGED — by a cause, not by a number.**
- **The budget stays at `900 s`, and is now declared to be known too large.** *That is a third state,
  different from both of the entry's earlier ones, and it is said rather than left to be noticed.*
  The variance the budget was covering is removed at its source, so the right figure is a product on
  the seeded receipt — but **every reading here is on this machine, and a budget is a claim about the
  runner.** A later seat holds the tightening until the runner has shown a seeded distribution;
  lowering it on this machine's `12 s` would be the same mistake as raising it on this machine's
  `13 s` was.
- **Nothing else.** No assertion, no tolerance, no printed figure, no gate, no ledger row, no
  instrument. ⌗ *`.github/workflows/gates.yml`, `70`'s and `cc66`'s receipts and the five probe
  families on the do-not-edit list are untouched.*

---

## ⌗ THE LESSON, IN THIS SEAT'S CHAIN

*A matcher loose enough to mis-read its own input answers about the matcher. A cold read is a
statement about a tree and it has to name the tree. An instrument that counts what it was told to
count cannot tell you the set was the wrong set. A dependence test is not a correctness test. A label
is attached by position, not by presence. A conjunct's quantifier is part of the claim. A claim about
"every" is a claim about a binder.* And now:

> ### ⛭ A SINGLE READING CANNOT MEASURE A DISTRIBUTION, AND A SPREAD IS NOT A CAUSE.
> **Three readings of `11 s`, eight hash seeds of `11 s` and a contention ratio all agreed, and all
> three were answers to a question nobody had asked: what the receipt costs *usually*. The runner was
> not asking that. The number that mattered was the one the measurements never took — how often it is
> unlucky — and it took thirty trials and a stall dump to take it.**

⌗ *Corollary, for the budget table: every entry in it is a worst measured figure times `1.7`, which
is an instrument for a COST. Three of its entries — `Q1`'s `INNER = 600`, this one's draw, and
whatever `P14`'s turns out to be — are not costs at all, and a bigger number is the symptom's fix in
every one of them.*
