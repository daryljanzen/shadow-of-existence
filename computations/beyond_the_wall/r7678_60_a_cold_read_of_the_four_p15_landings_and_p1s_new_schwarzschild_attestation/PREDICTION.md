# r7678 (60) — REGISTRATION, BEFORE A CLAIM IS SCORED

**Order:** `r7677` (69), two objects on a named tree.

> **1.** The four P15 landings. *Does each citation now sit on the clause whose figure its receipt
> computes? Is `l.1857`'s relabelling faithful to `the_band_rms_ratio`'s schemes?*
> **2.** P1's new paragraph after the Eddington–Finkelstein corollary in Section 3, against
> `SchwarzschildKruskal.lean` (`sk_cor_EF_events`) and `SchwarzschildKilling.lean`
> (`sq_cor_EF_coincident`). *Check every hypothesis and conclusion it states. 71 reports that
> `𝓗⁺ ⊆ M` fails on its `N` because the frontier meets the white-hole singularity. Does the
> paragraph claim anything that rests on `𝓗⁺` as the frontier in `N`?*

**The tree is named in `runs/TREE.txt`:** worktree `f438c622…`, HEAD `c12b46f3`, previous
`5f2513f4`.

---

## ⌗ WHAT WAS READ BEFORE THIS REGISTRATION — AND NOTHING WAS SCORED

- ⓐ **The diff is measured, not assumed:** `5f2513f4..c12b46f3` touches `corpus/CR_cosmology.tex`
  (12 lines), four `P15` receipts, `corpus/BH_causality_v2.tex` (+2 lines), and adds two Lean probe
  files of **8009** and **4155** lines with 71's `PREDICTION.md` and two `RESULT` files.
- ⓑ **P1's new paragraph is ONE paragraph of two sentences plus a third of four words**, located
  immediately after the EF corollary's `\end{corollary}`. Its claim set is fixed below at **fifteen**
  claims before any is scored.
- ⓒ **The corollary it attests has THREE paragraphs**: a setup, a substantive paragraph with a causal
  half and a coincidence half, and a *"Thus…"* paragraph about the EF **diagram**. ⌗ *So "both
  halves" has at least two readings, and the count is registered as a thing to measure rather than
  resolved by assumption.*
- ⓓ **71's two `RESULT` files were read.** `RESULT_1.md` states that one registered clause was
  **false and corrected**: `S.H J` is **not** `{U = 0}`; it is `{U = 0} ∪ {U < 0, UV = 1}`, and only
  `S.H J ∩ M = {U = 0}`. `RESULT_A.md` states **`3c` (the EF diagram's vertical extent) is
  interpretive and stays NOT BEGUN**, and that curvature was neither checked nor used in either file.
- ⓔ **Nothing has been scored.** No claim carries a verdict, no probe has been run, and no figure or
  theorem text has been parsed by an instrument.

---

## PART 1 — THE METHOD, FIXED BEFORE IT RUNS

*"Cold" is operational: every verdict is scored from text **parsed out of** the Lean files, the
receipts and the `.tex`, and never from 71's or 69's description of what they did.*

1. **The claim set is fixed in this file**, below, before anything is parsed. Each claim is one
   assertion the paragraph or the landing makes, written as the paragraph's own words.
2. **Each claim is scored SUPPORTED / NOT SUPPORTED / UNMEASURED**, and a claim whose verdict depends
   on which of two readings a phrase takes is scored **TWO-TO-ONE** and reported as both.
3. **No verdict is a constant.** Every verdict is a function of readings parsed in the run, and the
   flip family re-evaluates each with its readings negated.
4. **The citation-placement question is answered through the gate's own scope**, not a new one:
   `check_figures_pinned.sites()` on the live tree, restricted to the landing's sentences, so the
   answer is about what the corpus counts.
5. **`l.1857`'s relabelling is checked against the receipt's own scheme names**, parsed out of
   `P15_the_band_rms_ratio_does_not_move_with_any_numerical_setting.py`, not against the prose.

### THE GUARD FAMILIES — six, and the two newest are `r7676`'s own

- **G1 — the conjunct probe.** Every verdict runs through the same predicate, probed on a known-true
  and a known-false conjunct.
- **G2 — the anchored-marker family.** Three anchor forms only: `\b`, an escaped control sequence,
  an escaped math delimiter. An unanchored marker is REFUSED, each form probed.
- **G3 — the flip family.** Every derived verdict re-evaluated with its readings negated.
- **G4 — the classifier probe family.** Every class a classifier can emit, probed on a member and a
  non-member.
- **G5 — the reader probes.** `r7674`'s lesson: *a dependence test is not a correctness test.* Every
  shape the source actually contains is pinned, with NEGATIVE probes. For a Lean conclusion this
  means: a conjunct under a `∀` over a segment, a conjunct under an `∃` over splittings, and — the
  one that matters here — **a probe that an EXISTENTIAL conjunct is NOT read as a universal one.**
- **G6 — the flattening probes.** `r7664`'s rule, made a family at `r7676`: every prose probe runs
  on a whitespace-flattened copy, because a phrase that wraps reads False on the raw text. Probed
  on a phrase that wraps and for idempotence.
- ⌗ **And `r7676`'s positional corollary carries over:** *a label is attached by position, not by
  presence.* Where a claim names one of two objects in one sentence, the marker must sit on the
  object and not merely in the sentence.

---

## PART 2 — THE CLAIM SET, FIXED NOW

### Object A — the four P15 landings (⒜–⒠)

- **⒜** `l.1890` now reads **"±3 full widths at half maximum"**, the repair `r7676` asked for, and
  the figures beside it are unchanged.
- **⒝** The retention receipt is **repointed onto the arm of record** and no longer reads a namesake
  acceptance bank for the arm.
- **⒞** Its agreement gate is **moved to the arm-of-record pair with a 1 pp window**, and it passes
  on that window.
- **⒟** The three `\rcpt{}` placements make the gate read the ten figures `r7676` found invisible,
  **and each citation sits on the clause whose figure its receipt computes** — the order's own
  question, which is about CLAUSES and not sentences, so both scopes are measured.
- **⒠** `l.1857`'s relabelling is **faithful to `the_band_rms_ratio`'s two schemes**: the figure it
  now calls *"with the phase held fixed"* is that receipt's `fixed`, and the pair it calls *"with
  each arm on its own clock"* is its `sweepown`.

### Object B — P1's new paragraph (①–⑮)

- **①** *"Both halves of the corollary are machine-checked."*
- **②** *"on the radial plane of the Schwarzschild geometry in Kruskal coordinates"*
- **③** *"with the metric `−F(r) dU dV` on `r > 0`"*
- **④** *"the horizon at `U = 0`"* ⌗ *the order's named question points here.*
- **⑤** *"a static observer at `r₀ > r_h`"*
- **⑥** *"Two events on a generator of `U = 0` are … distinct"*
- **⑦** *"… causally ordered"*
- **⑧** *"… not chronologically related"*
- **⑨** *"… and both at `r = r_h`"*
- **⑩** *"(`sk_cor_EF_events`, in `computations/formalisation/lean/probes/SchwarzschildKruskal.lean`)"*
  — the address resolves and the theorem is there.
- **⑪** *"along that generator the static Killing field `∂_t = (V∂_V − U∂_U)/4M` is null"*
- **⑫** *"so the two events are metrically coincident"*
- **⑬** *"with `Δx = Δτ = 0`"*
- **⑭** *"(`sq_cor_EF_coincident`, in `SchwarzschildKilling.lean`)"* — the address resolves.
- **⑮** *"Neither uses the curvature."*

---

## PART 3 — THE REGISTERED ARMS

Each arm is a **comparison**, not an expected verdict.

- ① **THE SPLIT.** The counts of SUPPORTED / NOT SUPPORTED / UNMEASURED over the twenty claims.
  *No predicted split.*
- ② **THE ORDER'S NAMED QUESTION.** How many of the fifteen P1 claims rest on `𝓗⁺` as the frontier
  **in `N`** rather than in `M`, and which. *Registered as a count with no predicted value: `0`
  would mean the paragraph is clear of 71's correction, and any number above `0` names the clauses.*
- ③ **"BOTH HALVES" IS MEASURED, NOT ASSUMED.** The number of readings the phrase admits on the
  corollary as it stands, and the verdict of ① **under each**. ⌗ *Registered this way because
  `r7670` fixed that a registered arm naming one direction of a mismatch cannot see the other.*
- ④ **THE EXISTENTIAL.** Whether the Lean's `Δx = 0` sits under a `∀` or an `∃`, parsed from the
  statement, and whether the paragraph's wording matches the quantifier it sits under.
- ⑤ **THE ROUTE.** Whether the corollary's own derivation — *"spatially coincident in the sense of
  Theorem (b); the theorem therefore applies"* — is the route the Lean takes, or a different route
  to the same conclusion. *No predicted branch.*
- ⑥ **THE OMISSIONS.** Which conclusions `sk_cor_EF_events` and `sq_cor_EF_coincident` prove that
  the paragraph does **not** state. *A count, no predicted value; an omission is not a defect by
  itself and is reported as its own class.*
- ⑦ **THE LANDINGS.** ⒜–⒠, each SUPPORTED or not, and for ⒟ the clause scope **and** the sentence
  scope separately.
- ⑧ **THE GUARDS FIRE.** Every probe in G1–G6, including G5's negative probe that an existential
  conjunct is not read as a universal one.

**⛔ The reachable negative:** all twenty claims hold, no claim rests on `𝓗⁺` in `N`, "both halves"
admits one reading only, and the five landings are faithful. ⌗ *Registered as reachable so that
reaching it is a result and not a silence.*
