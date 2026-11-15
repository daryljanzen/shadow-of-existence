# `r7783+cc66` — REGISTRATION ONLY: the low-ℓ depths receipt on the one rate, item ① of `r7783`

**Registered before the new measurements are made.** What is read at registration time is `P15`'s own
prose and the already-published table of `r7779+cc66.2` (my own, landed at `r7783`). What is *not* yet
computed is the identification of which arm and point the paper's figures are, and the point and
pairing of its "$2.9$ per cent" cross-validation.

## What the paper prints, read from its own text

`sec:largescale` (and the abstract, line 134): the deficit is **$0.485$, $0.441$, $0.354$, $0.657$** of
the flat-ΛCDM expectation at $\ell = 2,3,4,5$, "recovering by $\ell \approx 8$", the minimum at
$\ell = 4$, "and the hierarchy agrees to **$2.9$ per cent** at every multipole, the octopole included,
and to under one per cent above $\ell = 5$".

## ⛔ A distinction the order's wording runs together, and the registration fixes it first

69 writes: *"Say in the receipt which point the paper's 2.9 per cent cross-validation is taken at.
Your 3.39 and 3.51 are at the refit point."*

**Those are two different comparisons, not one comparison at two points.**

 * The paper's **$2.9$ per cent** is **arm A against arm B** — the exact transfer against the photon
   hierarchy, two independent Boltzmann treatments. Its own sentence says so: *"the hierarchy agrees
   to $2.9$ per cent"*.
 * My **$3.39$ / $3.51$** is **frozen against decoupled**, two tower builds *inside arm B*. The
   source is the depth receipt's own standard: *"Both variants are reported; they agree to $3\%$,
   which is the point of running both."*

So my `r7779` `R5′` did not measure the paper's number at another point; it measured a **different
quantity**. R3 and R4 below separate them and give each its own point, which is what the rewrite
needs.

## The rows

### R0 — the paper's printed depths are arm A **(L)** at the **distances' point**

**PREDICT** `distances__armA__L` reproduces all four printed figures to half their last printed
digit — $0.485$, $0.441$, $0.354$, $0.657$ — and that `distances__armA__one_clock_gate` does **not**,
differing at **at least two** of the four at that precision. *The paper is quoting the arm of record,
at the point its distances are quoted at.*

**FAILS IF** the (L) leg misses any of the four, or the one-clock leg matches all four — either of
which would mean the paper's sentence is quoting something else and the rewrite must be told so.

### R1 — the one-rate values the rewrite should carry

**PREDICT**, at that same arm and point under `SPLITCLOCK` unset: $0.4898$, $0.4351$, $0.3594$,
$0.6677$ at $\ell = 2,3,4,5$ — i.e. **$0.490$, $0.435$, $0.359$, $0.668$** at the paper's precision.
Each pinned to half its last printed digit. **FAILS IF** any differs.

### R2 — the shape claims survive the rate, and the paper need not change them

**PREDICT** on the one rate the minimum stays at $\ell = 4$ and the recovery multipole (first
$\ell \ge 5$ with depth $\ge 0.99$) stays at $\ell = 8$ — so *"a dip whose minimum falls at $\ell=4$"*
and *"recovering by $\ell \approx 8$"* stand unchanged, and only the four numbers move.
**FAILS IF** either moves.

### R3 — the paper's $2.9$ per cent is arm A against arm B, at the distances' point, under (L)

**PREDICT** $\max_\ell |{\rm armB}/{\rm armA} - 1|$ over $\ell = 2 \dots 8$, with both legs at the
distances' point and both under (L), is $2.9\,\%$ to within $0.3$ percentage points — identifying the
sentence's point and clock. **PREDICT also** that it is under $1\,\%$ above $\ell = 5$, the paper's
second clause. **FAILS IF** either misses, in which case the sentence's provenance is not what this
row says and I report that instead.

### R4 — and what the one rate does to that cross-validation

**PREDICT** the same arm-A-against-arm-B figure under `SPLITCLOCK` unset at the same point stays
within $0.5$ percentage points of the (L) value — so *"cross-validated between two independent
transfers"* survives the rate change and the $2.9$ needs at most a small edit.
⛭ The one-clock arm-B leg at this point is the blob-confounded bank; it is used **only** on the
licence of `r7779+cc66.2`'s `R2′` (normalised-AST identity with `SPLITCLOCK` unset), and the receipt
re-runs that test rather than citing it. **FAILS IF** the identity test does not reproduce.

### R5 — the frozen/decoupled figure, kept separate and given its point

**PREDICT** frozen against decoupled is $3.39\,\%$ under (L) and $3.51\,\%$ under the one rate **at
the refit point**, and that at the **distances'** point only the (L) legs are banked, so no one-rate
frozen/decoupled figure exists there without a new run — which this item does not order.
**FAILS IF** the refit-point figures differ, or a distances-point one-clock arm-B pair turns out to be
banked after all.

### R6 — what is NOT claimed

No significance against the sky; the $\Delta(-2\ln L) = +1.7$ scoring is untouched; no claim that the
one-rate depths fit the measured multipoles better or worse. The receipt gives the rewrite its
numbers and their provenance, and nothing more.

## Failability

Every row reads banked arrays and `corpus/CR_cosmology.tex`. The figure pins move under any change to
a banked depth; R0 and R3 move under any edit to the paper's sentences; R4 moves under either blob.
The receipt's failability will be measured by perturbing the computation, as `r7779+cc66.3`'s was.
