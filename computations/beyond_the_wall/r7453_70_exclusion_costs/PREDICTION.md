# r7453+70 — PREDICTION: the six exclusions of `turn_gates.sh`, re-measured (registered before any timing)

**Order:** `r7453` ③. Re-measure each of the six `EXCLUDE_NAMES` costs on current `main`, here and in CI, and
report both. State whether each reason still holds at the measured figure. For a trigger reason, say what fires
it now. Then answer whether the exclusion set can be derived. **`EXCLUDE_NAMES` is not changed by this
revision**, because a ground and its re-verdicts do not go in one revision.

**Method:**
- **Local:** wall seconds of `python3 -W ignore corpus/<g>.py` on this container (4 cores), `NODE=70`, one run each, sequential, nothing else running. These are the numbers `turn_gates.sh` would see.
- **CI:** the gate's own span in the latest completed job on `main` that runs it. For gates in a looped step, the span runs from its `── <g>` line to the next one, using the log line timestamps. For a gate that has its own step, it is the step's started→completed time.
- **Matching:** no process matching by name (`pgrep -f`). Every timing comes from the timer around the one call.

| arm | gate | stated reason | local central (band) | CI central (band) | reason holds? |
|---|---|---|---|---|---|
| **X-1** | `check_quote_pins` | 947 s (r7343) | 950 s (700–1300) | 1260 s (1000–1600; `cc66`'s ~21 min) | holds: > 280 s turn timeout either way |
| **X-2** | `check_cross_row_dupes` | 128 s | 140 s (90–260) | 180 s (110–360) | **⚠ 60 %: no longer holds as a cost.** It sits under the 280 s turn timeout. The exclusion is then a choice to save ~2 min, not a necessity. |
| **X-3** | `check_tilt_pins` | > 120 s probe (r7411) | 240 s (120–700) | 300 s (150–900) | holds only if > 280 s: 50 % |
| **X-4** | `check_receipts_run` | CACHED, red when the tree digest moves | 20 s (2–120) to run the gate itself | 114 s (60–240; r7321 measured 1.9 min) | **it is a trigger.** It fires when the tree digest differs from the cached run's. Predicted red here now: 80 % |
| **X-5** | `check_compile` | needs pdflatex | pdflatex IS present here: 600 s (240–1500) for 17 papers | 480 s (240–1200) for the step; job incl. texlive-full install 15 min (8–25) | **⚠ the stated reason is false in this container** (70 %). The reason that holds is cost, or the install in CI |
| **X-6** | `check_sitemap_resolves` | needs the assembled `_site` | with no `_site`: exits non-zero at once (< 5 s). That is its own presence assertion, not a pass | 3 s (1–30) | holds as a trigger: no working tree has `_site` |

**The structural answer, predicted:** **yes for the cost half, no for the environment half.**
- **Cost half (X-1–X-3):** each gate declares a measured `COST_S` with its date. `turn_gates.sh` excludes it when the declared cost exceeds `GATE_TIMEOUT` and prints the declaration. A declared cost is checked against a measured one by the sweep, so it cannot drift silently.
- **Environment half (X-4–X-6):** these reasons are about the subject (cache, toolchain, `_site`). A `NEEDS` marker is derivable, but it would describe, for example, `check_compile` as needing a toolchain this container has.
- **Guard against silent growth:** the derived set's names are printed every run, as now. Any change in the set fails the roster unless it is matched by a declared cost change in the same diff.

**EFFORT:** 2.5 h (1.5–4). The `check_quote_pins` run and the CI log reading dominate.
