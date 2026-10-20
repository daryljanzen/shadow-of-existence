# r7453+70 — RESULT: the six exclusions of `turn_gates.sh`, re-measured (registration `0a5da2b37`)

**How the readings were taken:**
- **Local:** this container, 4 cores, one sequential run per gate, `NODE=70`, 15:56–16:12 UTC 2026-10-20, on `main` `187c5e53e`. Each time is a timer around the one call; no process was matched by name.
- **CI:** the gate's own span on the two latest completed `main` runs that ask it.
  - **Fast job:** `39391528454` (10-20, `b57bfc6e`) and `39050998044` (10-17, `b57bfc6e`). For a gate inside the looped text-gates step, the span runs from its `── <g>` line to the next gate's line, using the log timestamps.
  - **Own step:** step start → step end. That covers `compile`, `heavy`, and the sitemap step of `pages` run `39452174294`.
- **One sample here, two in CI.** The bands were for one reading.

| arm | gate | stated reason | local | CI | arm | the reason at the measured figure |
|---|---|---|---|---|---|---|
| **X-1** | `check_quote_pins` | "947 s measured (r7343)" | **595 s** (band 700–1300) | **186 s, 279 s** (band 1000–1600) | **REFUTED LOW, both** | **Still over the 280 s turn timeout here, so the exclusion still holds locally.** The figure is stale: it is 0.63× here, and CI runs it **2.1–3.2× faster** than this container. *One gate, two values.* |
| **X-2** | `check_cross_row_dupes` | "128 s; sweep_gates.sh asks it" | **145 s** (90–260) | **90 s, 135 s** (110–360) | holds here; CI one in band, one below | **⚠ It no longer holds as a cost: 145 s is half the 280 s timeout.** The second half of the reason is incomplete: the **fast job asks it on every push**, and `sweep_gates.sh` is in no workflow. |
| **X-3** | `check_tilt_pins` | "exceeded a 120 s probe at r7411; the nightly backstop job asks it" | **170 s** (120–700) | **no reading exists** | local holds; **CI: the arm cannot be scored** | **⛔ Both halves are wrong.** At 170 s the gate is under the turn timeout. The backstop that "asks it" is **monthly** (`0 4 1 * *`), not nightly. Its tilt step was wired at `cdd0241da` on **2026-10-02**, one day after the last firing (2026-10-01). No `workflow_dispatch` has run since 09-28. ⇒ ***The gate excluded from the turn has never been asked in CI. It is a question asked nowhere, and the next asking is 2026-11-01.*** |
| **X-4** | `check_receipts_run` | "CACHED — red whenever the tree digest moves" | **139 s, rc 1** (2–120; 80 % red) | step **60 s**, rc 1 (60–240) | local **REFUTED HIGH**: the gate runs the 1096-receipt hollow-assertion lint in-process. Red as predicted. CI holds | **It is a trigger.** Here it fires on a **STALE cache**: the cached run is against tree `c45c0984`, the tree is now `65db5aff`. In CI it fires for a different reason: **the 1 receipt over the per-receipt timeout** (the P15 runtime tail, routed `r7349`). The cost half of the printed reason ("a 9-minute re-run") describes the *remedy*, not the gate, which takes 139 s. |
| **X-5** | `check_compile` | "needs pdflatex" | **51 s, rc 0**: pdflatex **is** on this container (70 %) | step **38 s, 39 s**; job 7.0–8.1 min, of which the texlive-full install is 7.0 min (8–25) | **REFUTED LOW, both** (band 240–1500, 240–1200) | **⚠ The reason is false here**, and the gate is green in 51 s. It holds only on a container without TeX. In CI, the cost is the install, not the gate. |
| **X-6** | `check_sitemap_resolves` | "needs the assembled `_site`" | **< 0.1 s, rc 1**: "⛔ _site/ does not exist" | **< 1 s** (both timestamps 15:51:22) | **HOLDS** | **It holds, as a trigger.** No working tree has `_site`. The gate's own presence assertion refuses the vacuous pass, as r7435 designed. |

**The measured cost of the whole exclusion set, here:** 595 + 145 + 170 + 139 + 51 + 0 = **1100 s**.
- **Three of the six (X-2, X-3, X-5), 366 s together, fit under the 280 s turn timeout on this container.** One gate (X-1) does not.
- X-4 and X-6 are triggers. A turn running X-4 or X-6 would always read red for a reason no edit can fix.

**EFFORT:** 2.5 h (1.5–4) registered. **≈ 0.6 h** of wall time (15:52 → 16:30 UTC), because the CI logs were readable directly and `check_quote_pins` took 10 min, not 16.

## ⓐ–ⓒ, for each exclusion
- **ⓐ Cost here and in CI:** in the table. Every cost-type reason (X-1–X-3) has a different value in CI. **X-1 differs by 2.1–3.2×**, which is wider than `cc66`'s 33 %.
  - **I cannot reproduce `cc66`'s ~21 min CI reading of `check_quote_pins`.** In both `main` fast jobs read, the *whole text-gates step* took 9.8 and 14.9 min. The gate was 3.1 and 4.7 min of that.
  - ~21 min matches no span I can find. Without its run id I can't say what it measured. I am **not** claiming it was wrong. I am asking for the run.
- **ⓑ Does the reason hold:**
  - **X-1:** holds locally; the figure is stale.
  - **X-2:** does not hold as a cost.
  - **X-3:** does not hold, and its "asked elsewhere" is false.
  - **X-4:** holds as a trigger.
  - **X-5:** holds only without TeX.
  - **X-6:** holds.
- **ⓒ What fires each trigger now:**
  - **X-4 here:** a tree-digest mismatch, `c45c0984` → `65db5aff`.
  - **X-4 in CI:** one receipt over the per-receipt timeout. The two triggers are different.
  - **X-5:** the absence of `pdflatex`. That is false here and true in the fast job, which declares `COMPILE_UNRUN_OK`.
  - **X-6:** the absence of `_site`, always true outside `pages.yml`.

## The structural question: can the exclusion set be derived?

**Yes, for the environment half. No, for the cost half. The measurements decide it, and they reverse half my prediction.**

- **Cost half (X-1–X-3): no.** I predicted a declared `COST_S` per gate. The figures refute it.
  - **One gate measures 947, 595, 279 and 186 s** across two containers and three dates. A declared cost is one value of a quantity that has at least two at any moment.
  - A set derived from it would grow or shrink with whichever machine last wrote the number, silently. That is the outcome the order rules worse than a hand list.
  - And the timeout already derives the cost exclusion live: a gate over `GATE_TIMEOUT` is printed `[UNRUN]` by name every run. The hand list only saves the 280 s it would burn.
  - **So the cost entries stay hand-written. Each states both values and its date.**
- **Environment half (X-5, X-6): yes.** Each condition is a **fact the script can test at run time**, not an estimate:
  - `command -v pdflatex` for X-5;
  - `[ -d _site ]` for X-6.
  - A gate declaring `NEEDS: pdflatex` is skipped and printed as `NOT ASKED (no pdflatex here)` when that is true. When it is false, the gate runs: X-5 would run here, green, in 51 s.
  - This set cannot grow silently. A precondition that is met turns the gate back on, and every skip prints its test.
- **X-4 is the exception: neither half.** Its "precondition" (the cache is current) is the question the gate exists to answer. Deriving the exclusion from it would make the gate run only when it must pass. **It stays hand-listed, with the reason.**

**Proposed, not applied:** these are `EXCLUDE_NAMES` changes, and the order forbids them in this push. They are 66's call.
1. Drop X-2 and X-3 from the list. They measure under the timeout, and X-3 is otherwise asked nowhere until 2026-11-01.
2. Restate X-1's reason as "595 s here, 186–279 s in CI (r7453)".
3. Replace X-5 and X-6 with a `NEEDS` test.
4. Separately, and on its own merits: **put `check_tilt_pins` where it is asked**, the nightly or the fast job (170 s here; CI has run the fast-job gates 1.1–3.2× faster than this container), because the monthly slot has not yet fired.
