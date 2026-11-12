# `r7747+cc66` — REGISTRATION: DOES REMOVING THE RADIATION DRIVING REMOVE THE LOWEST-BAND STEP?

⛔ **Written and pushed BEFORE a line of the computation exists.** Order `r7747` item ②: *"test whether removing the driving removes the lowest-band step on both arms. Register the reading first, with both outcomes."* Both outcomes and the licence are fixed below.

## ① THE QUESTION, AND WHY THIS IS THE CANDIDATE

`r7745+cc66` established that *"what distinguishes the first acoustic cycle from the rest"* is **not** `PO-87`'s question: the step is very largely **common to both arms**, and a feature common to both arms cannot be carried by the arms' distance ratio, which is unity when they agree. ⇒ So the carrier must live in the physics the arms **share**, and `69` names the candidate: the **radiation driving** — the first peak's modes enter the horizon in the radiation era, above `ℓ_eq ≈ 144`, and are driven.

## ② THE ARRAYS, AND THEY DIFFER IN EXACTLY ONE FLAG

Established by reading each file's own recorded `config` before registering:

| | driven | undriven |
|---|---|---|
| **CR arm** | `c54.186_cr_L3000_leafrec1.npz` | `c54.193_cr_nodrive_L3000_leafrec1.npz` |
| **control** | `c54.186_lcdm_L3000.npz` | `c54.193_lcdm_nodrive_L3000.npz` |

* The CR pair's configs are **identical but for `NODRIVE`** (`false` → `true`): same `KFAC 2.0`, `LEAFREC true`, `LEAFSCALES true`, `LMAXL 3000`, `STACKPERT false`, and the same `l_A = 302.943`. ⇒ *A one-flag difference is what makes this a controlled subtraction rather than two separate builds.*
* All four share **one identical `ℓ` grid**: `363` nodes, `ℓ 100`–`2996`, checked by array equality.
* The control carries `l_A = 301.375`. It needs no `leafrec1` twin: the recombination switch leaves the control bit-identical by construction (`r7673`).

⛔ **WHAT THESE ARRAYS ARE NOT.** They are the **leaf-recombination** configuration, not demonstrably *the arm of record* (which is the leaf-rate configuration **refitted**); this one's `l_A` is `302.943` where the arm of record's comb is `299.06` (`r7653`). ⇒ *So the reading below is on the matched driving pair that exists, and I do not call it the arm of record. Nothing here re-points a printed figure.*

⛔ **AND THE ABSOLUTE STEP VALUES HERE WILL NOT BE THE PRINTED ONES.** The printed step is read on `r6941_fine_*` with `r6959_eta_cr`'s band edges; no driving-off counterpart of that bank exists on disk, which is why this reading uses the `c54` pair instead. ⇒ *Only the WITHIN-PAIR ratio is read. A number here is never to be compared against a number in the paper.*

## ③ THE STATISTIC, FIXED NOW

Band edges are the printed reading's own, `q_edges` from `r6959_eta_cr`: `q = ℓ/l_A` at `0.85, 1.55, 2.25, 2.95, 3.65, 4.35, 5.05, 5.75` — seven bands, the **lowest being `q ∈ [0.85, 1.55)`**, the first acoustic cycle. Each arm is banded on **its own** `l_A`.

For each of the four spectra, identically:
1. **Envelope**: running mean of `Dl` over a centred window of `W = 81` grid nodes (declared here; the grid is ~8 multipoles per node, so `W` spans about two thirds of a comb period).
2. **Contrast**: `c(ℓ) = (Dl − env)/env`.
3. **Band amplitude** `A_b`: the rms of `c` within band `b`.
4. **Trend**: a least-squares line in `q` fitted to bands `2`–`7` only.
5. **Step** `S`: `A_1` minus that trend evaluated at band `1`'s centre — the lowest band's departure from the trend its own upper bands set.
6. **Normalised step** `s = S / mean(A_2..A_7)`, which is the scale-free form.

## ④ A PRECONDITION THAT CAN FAIL, AND IT IS CHECKED FIRST

**`P0`** — the **driven** pair must show an **upward** step at the lowest band on **both** arms (`S > 0`). ⇒ *If it does not, this grid and envelope do not reproduce the feature the question is about, the test has no subject, and I report that instead of a verdict. Registered because a reading whose subject is absent must not be reported as a reading about it.*

## ⑤ THE OUTCOMES, BOTH FIXED IN ADVANCE

Let `ρ = |s_undriven| / |s_driven|`, per arm.

| outcome | licence |
|---|---|
| `ρ ≤ 0.30` on **both** arms | **the driving carries it.** The sentence becomes a statement of where it is fixed: standard acoustic physics, shared by both arms. Draft that sentence with its receipt (order item ③) |
| `ρ ≥ 0.70` on **either** arm | **the driving does not carry it.** Report what is left and by how much, arm by arm, and draft no sentence |
| otherwise (`0.30 < ρ < 0.70` on both) | **partial.** Report the fractions and claim nothing about authorship; the sentence is not drafted |

⌗ *The `0.30`/`0.70` lines are set here, before the numbers exist, and will not be moved. If a measured `ρ` lands near a line I report it against the line as it stands.*

## ⑥ WHAT THIS WILL NOT CLAIM

* ⛔ Not that the driving is the **only** shared candidate — only whether it carries this step on these arrays.
* ⛔ Not anything about `PO-87`'s contrast step: that is the part that **fails to cancel** between the arms, and `r7745` separated the two objects. **No row is opened for this**, as the order directs.
* ⛔ Not a re-pointing of any printed figure, per §②.
* ⛔ Not a significance: `ρ` is a ratio of amplitudes, with no null and no error bar, and will be reported as such.
