---
name: s-009-heavy-tier
kind: FINDING — POSITIVE (draft, uncommitted)
current: r2428 / c54.178
job: THE_HUB records the heavy receipt tier as unverifiable in this container. It is not — camb and pynucastro install cleanly from pip, and all 288 registered receipts then pass in place in five minutes. The reproducibility layer is fully green for the first time, and RUN_RESULT.txt is stale.
sources: [chat]
---

# S-009 · THE HEAVY TIER IS VERIFIABLE HERE, AND ALL 288 RECEIPTS PASS

**`THE_HUB` §CI records the limit:**

> ⚠ ***The heavy tier is where this container cannot verify***: *ten receipts import
> `camb`/`pynucastro`, declared by name in `check_receipts_run`. **In CI they can actually run**,
> which is a genuine gain — the fork's own rule,* **"a registered receipt that does not run where it
> is registered is not a receipt"**, *becomes checkable everywhere rather than only where the fork
> sits.*

**And `receipts/RUN_RESULT.txt` is the last recorded run:**

> `276 registered receipt(s)` · **`264 pass, 8 fail, 4 over timeout, in 543s wall`**
> — *every one of the eight failures an ImportError on `camb` or `pynucastro`, none of them reaching
> a line of computation.*

---

## ⇒ IT IS NOT AN ENVIRONMENTAL LIMIT. IT IS TWO PIP INSTALLS.

```
pip install camb pynucastro --break-system-packages
```

Both resolve and import first time, with no build toolchain beyond what is already present:

| | version |
|---|---|
| python | 3.11.15 |
| numpy | 2.4.4 |
| scipy | 1.17.1 |
| sympy | 1.14.0 |
| **camb** | **2.0.1** |
| **pynucastro** | **2.12.0** |

## THE RESULT, RUN IN PLACE

```
python3 scripts/run_all_receipts.py --jobs 2 --timeout 240
```

> **`288 pass, 0 fail, 0 over timeout, in 304s wall`**
> *slowest that passed: `P16_validate_bbn.py` 77s · `P15_the_second_arm_actually_run.py` 53s ·
> `P15_the_collapse_leg_is_scale_invariant.py` 41s · `P15_verify_lowell_exact_measure.py` 36s ·
> `P16_theory_error_and_likelihood.py` 31s*
>
> *"Every registered receipt runs, in place, and exits 0 — so every assertion in the reproducibility
> layer was actually evaluated."*

**Three things follow, and each is checkable:**

1. **The eight ImportError failures are gone** — `BUILD_camb_store`, `P15_camb_reference`,
   `P15_damping_ratio_clean`, `P15_damping_reabsorption`, `P15_full_transfer_verdict`,
   `P15_verify_lowell_boltzmann`, `P16_theory_error_and_likelihood`, `P16_validate_bbn`. **Each now
   reaches its computation and exits 0.** *So the ~9% damping result, the CAMB reference, the BBN
   validation and the likelihood are, for the first time in the recorded history of this gate,
   **evaluated** rather than skipped.*
2. **The four timeouts are gone**, and not by loosening: the previously-`[slow]`
   `P15_the_collapse_leg_is_scale_invariant.py` now completes in **41s**, well inside the old 120s
   bar it was breaching. *The old run used `--jobs 4` on a 2-core box; the contention was the
   timeout, not the receipt.* ⇒ **`--jobs 2 --timeout 240` on two cores is a better configuration
   than `--jobs 4 --timeout 120`, and it is faster in wall clock too: 304s against 543s.**
3. **The register has grown 276 → 288** since that run, and all twelve new ones pass.

---

## ⇒ WHAT TO CHANGE

**① `receipts/RUN_RESULT.txt` is stale and it is the artefact a node trusts.** It currently records
264/8/4 and closes with *"⛔ A REGISTERED RECEIPT THAT DOES NOT RUN WHERE IT IS REGISTERED IS NOT A
RECEIPT"* — a true motto sitting on top of a result that says eight of them do not. **Refresh it.**

**② `THE_HUB`'s CI table should say the heavy tier needs two pip installs, not that it cannot be
verified here.** The current wording reads as an environmental constraint and it is a dependency
list. *The distinction matters because it is the difference between "wait for CI" and "run it now",
and the cost is five minutes.*

⌗ **And the gain is exactly the one `THE_HUB` names**: *"a registered receipt that does not run where
it is registered is not a receipt"* becomes checkable **before** a push rather than only in CI —
which matters most for the fork, whose own rule it is, and which does not run CI.

**③ `run_all_receipts.py`'s docstring says the gate "is not in the standing ten … it costs wall clock
the others do not."** *At 304s on two cores with the right job count, that is now a weak reason.*
**Worth re-asking whether it belongs in the standing set**, given its own stated origin: at c54.160 a
registered, cited receipt was exiting 1 on ImportError and *"every gate was green."*

---

## ⌗ WHAT THIS DOES NOT ESTABLISH

- **It is not a check of the physics.** 288 exit-zeros means every assertion was *evaluated*, not
  that any is *right*. `THE_BASE_RATE` entry twenty-three is the relevant one and it cuts here too:
  the corpus's own r2377–r2406 consolidation found **95 receipts that ran green and could not fail**.
  ⇒ ***A green suite is a floor, not a verdict.***
- **It does not touch `check_receipts_run`'s named-exclusion list**, which still declares those ten
  by name. *Whether that list should now be empty is a decision for whoever owns the gate — the list
  is a correct record of a real dependency, and removing it would only be right if the dependency is
  made a documented requirement rather than an ambient accident of my container.*
