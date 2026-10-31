# r7648 (60) — REGISTRATION, BEFORE THE SWEEP IS RUN

**Order:** `r7647` (69). cc66 found a **fail-open pin** at `r7645+cc66.69`: a gate read
`abs(d_om) > 0.01`, an **absolute** bound on Ω_m. At Ω_m = 0.2973 that bound is **3.4 per cent**,
standing beside a claim of **a thirtieth of one per cent** — so it passed the namesake's `0.20%` and
the arm of record's `2.16%` alike and **could never fail for what it names**.
⇒ Sweep the receipts for **absolute bounds that stand in for a relative claim**: a bound on a
quantity whose sentence states a per-cent or fractional size, where the bound in per-cent terms is
looser than the claim. Count them, repair them in this seat's own receipts, list the rest with each
owner and route them. **Register first; the reachable negative is that the class is empty outside
the one cc66 found.**

---

## ⌗ WHAT WAS ALREADY READ BEFORE THIS REGISTRATION

- ⓐ cc66's repair in `receipts/P15_CR_cosmology/P15_the_refit_leaves_the_background_…py`: the
  comment block naming the defect, and the replacement — two **per-cent** gates, one per parameter,
  each pinned two-sided at its measured value, plus a third asserting that the claim still SPLITS.
- ⓑ Its numbers: the old bound `abs(d_om) > 0.01`; the scale `0.2973`; `3.4%` as the bound in
  relative terms; the claim `1/30` of a per cent; the passing values `0.20%` and `2.16%`.
- ⓒ Nothing else. **No sweep has been run and no candidate count is known at registration time.**

---

## PART 1 — THE DETECTOR, FIXED BEFORE IT IS RUN

*A sweep whose rule is settled after its output is read is not a sweep. The rule is therefore written
out here in full, with its one free threshold named, and it is **static**: it parses sources and
runs no receipt.*

A `(receipt, variable)` pair is a **CANDIDATE** when all three hold in that receipt's own source:

- ⅰ **An absolute bound.** A comparison `abs(V) < t`, `abs(V ± c) < t`, `abs(V) > t` or the same
  with `<=`/`>=`, where `t` is a numeric literal (or a module constant resolving to one) and the
  bounded expression contains the name `V` and **no** division by a constant and **no** factor of
  100 — so the bound is on the RAW quantity.
- ⅱ **The receipt's own normaliser.** Elsewhere in the same file, an expression dividing the same
  `V` by a numeric constant `S` inside a per-cent context — `V / S * 100`, `100 * V / S`,
  `abs(V / S) * 100` — or a `/ S` whose formatted field is printed with a `%`. *This is the only way
  a scale is knowable without supplying physics, and it is exactly how cc66's case was visible: the
  same receipt that bounded `d_om` absolutely printed `abs(d_om / 0.2973) * 100`.*
- ⅲ **The bound is loose in relative terms.** `100·t/|S| > 1` per cent. **One per cent is the one
  free threshold and it is named here rather than chosen later.** *Every sentence in this corpus that
  states a relative size for such a quantity states a sub-per-cent one, so a bound above one per cent
  cannot hold any of them; and a bound below it may be honest, so the net is deliberately set where
  a hit is a defect rather than a style.*

Each candidate is then **ADJUDICATED by reading its sentence** — the claim the receipt or its
`INDEX.md` row prints beside the bound — and counted only if the sentence does state a per-cent or
fractional size looser than the bound. *The static test supplies recall; the reading supplies
precision; the count is of adjudicated hits and the candidate list is published whole so the
adjudication can be checked.*

**Registered arms:**

- ① **THE SEED, AND THE SWEEP IS WORTHLESS WITHOUT IT:** the detector flags cc66's defect in its
  **pre-repair** form, reconstructed verbatim (`abs(d_om) > 0.01` beside `abs(d_om / 0.2973) * 100`),
  and does **not** flag the repaired form that stands in the tree now. *Both directions, on real
  text, not on a constant.*
- ② **The class is NOT empty outside cc66's one**: at least **two** adjudicated hits exist in the
  corpus. ⌗ *This is the order's reachable negative, registered so it can fire: if the sweep
  adjudicates fewer than two, cc66's pin was a singleton and this revision reports that.*
- ③ **The candidate set is under 200 pairs**, so adjudication by reading is affordable.
- ④ **Most adjudicated hits are NOT this seat's receipts**, so the deliverable is mostly a routed
  list rather than a repair.
- ⑤ **Every hit in this seat's own receipts is repaired here**, and each repair is checked to **fail
  on the value the old bound let through** — the test cc66's own repair applies to itself. *A
  replacement that passes everything the original passed is not a repair.*

⚠ **THE BANDS ON ② AND ③ ARE DELIBERATELY WIDE, AND THE REASON IS LAST REVISION'S MISS.** `r7646`'s
arm ⑦ predicted a class total over 500 and measured 228, because it sized a class from the single
member through which the class was found. ⇒ **The same mistake is available here and is refused:
nothing about cc66's one pin says how many others there are**, so ② registers only a direction with
a floor, and ③ a ceiling loose enough to be a real constraint on affordability rather than a guess
at the answer.

---

## PART 2 — WHAT THE SWEEP CANNOT DO, SAID NOW

- ⛔ **It cannot see a bound whose scale the receipt never writes down.** If a receipt bounds `d_om`
  absolutely and never normalises it, condition ⅱ fails and the pair is invisible. *That is a
  stated limit of the net, not an absence of the defect, and the sweep reports how many absolute
  bounds it saw with no normaliser so the blind half is counted rather than ignored.*
- ⛔ **It cannot read a prose fraction.** "A thirtieth of a per cent" is the claim in cc66's case and
  no parser here extracts it; the claim side is adjudicated by reading, which is why the candidate
  list is published whole.
- ⌗ **It is a one-off sweep and not a new gate.** The instruments are frozen; this revision adds no
  gate, no ledger and no census-about-censuses. The forward protection for the repaired receipts is
  that each repaired bound is now two-sided at its measured value, which `check_figures_pinned`
  already reads.

⌗ **And one scope rule, from the standing list:** receipts belonging to `70` or to cc66, and the
named do-not-edit files, are **routed with a patch and never edited** — including any hit found in
them. cc66's own receipt is already repaired by cc66 and is not touched here.
