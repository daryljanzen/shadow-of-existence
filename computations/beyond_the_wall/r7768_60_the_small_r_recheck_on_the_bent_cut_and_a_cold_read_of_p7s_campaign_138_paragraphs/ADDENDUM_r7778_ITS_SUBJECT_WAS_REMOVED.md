# ADDENDUM to `r7768`, written at `r7778` — **ARM 6's SUBJECT NO LONGER EXISTS, AND THE ARM CANNOT SAY SO**

`r7768`'s arm 6 found that `P15 sec:scope` carried a clause true only of the radial-profile reading
this line had itself made at `r7756` and withdrawn at `r7762`. A patch was routed, nothing was edited.

**`r7767` (69) rewrote `P15` on one rate, and the rewrite removed both sentences the arm reads.**
Measured on the two commits, not inferred:

| the sentence arm 6 locates | before `r7767` | after `r7767` |
|---|---|---|
| *"Nor does putting radiation into the cut supply the leaf rate"* | **1 occurrence** | **0** |
| *"… taken as the radial profile …"* | **1 occurrence** | **0** |

**⇒ The finding is DISCHARGED by the rewrite, and the routed patch is spent.** The one site the
correction had not reached has been reached.

## ⛔ And re-running the probe on the new tree exposes a defect of mine

`arm 6`'s gate is a conjunction that includes *finding* the two sentences, so with them gone the arm
still reports **FAIL** — the same verdict as before, now for the opposite reason. **And its
explanatory prose is printed UNCONDITIONALLY**, so a re-run on the current tree prints

> *"⛔⛔ THE SENTENCE IS TRUE ONLY OF A READING THE CORPUS HAS SINCE WITHDRAWN … The paragraph has not
> been reached by the correction."*

beside a measurement that located **no sentence at all**. The numbers underneath are still correct —
the profile reading departs from the leaf rate by order unity and the pressure-work reading matches it
to `2.2e-16` — but the sentence pinning them to the paper is gone, and the output does not say so.

**⇒ THE GUARD: a verdict that cannot distinguish *the defect is present and wrong* from *the defect's
subject is absent* reports the same word for a live fault and a fixed one.** `r7770`'s successor
instrument already answers this shape with three states — MATCHED, WITHDRAWN, STALE — and arm 6 has
two. *The three-state form is what a located-in-the-paper arm needs, and this arm predates it.*

⌗ **`r7768`'s probe is NOT rewritten here.** It is a landed record of what was measured at `r7768`
against the paper as it then stood, and a receipt edited after the fact to agree with a later tree is
no longer a record of either. This note is the correction; the probe stays as it ran.
