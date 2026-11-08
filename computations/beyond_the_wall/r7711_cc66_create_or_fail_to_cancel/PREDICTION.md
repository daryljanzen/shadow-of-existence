# `r7711+cc66` — REGISTERED BEFORE ANY COMPUTATION

**The order** (`r7711`, 69): the question my own `r7707` registration left open. Does the projection
**create** the two-per-cent relative difference, or does it **fail to cancel** something the source
contrast hides under its own scatter? The source ratio excludes a step of the measured size but not a
tenth of one. Two routes are suggested — the source ratio at a smoothing where its own scatter falls
below a tenth of the step, or a projection of each arm's source through the **other** arm's window — and
option 3 is named in the order itself: **if nothing available separates them, say so and name what
would.**

---

## ⛔ MY REGISTERED ANSWER IS (3), AND THE TWO OBSTRUCTIONS ARE NAMED NOW SO A NULL CANNOT BE DRESSED AS A FINDING

### OBSTRUCTION 1 — widening the smoothing destroys the plateau it is measured across

From `r7707`, the source ratio's pooled plateau scatter was `0.00625`, `0.00369`, `0.00205` at half-widths
`0.175`, `0.25`, `0.35`, against a spectra step of `0.0242`, a tenth of which is `0.00242`. ⇒ **At
half-width `0.35` the scatter is already just below a tenth** (`0.00205`), and the source's own change
there is `+0.0018` — *`0.88` of its own sigma, which is why `r7707` could neither exclude nor resolve a
tenth.*

Going wider lowers the scatter but eats the low plateau: the scan starts at `0.85 + half` and the low
plateau is `q < 1.4`, so the number of low-plateau centres is `(0.55 − half)/0.05` and reaches **zero at
`half = 0.55`**. ⇒ **To be MEASURED, not assumed: the scatter and the low-plateau count as functions of
half-width, and whether any setting both resolves a tenth and keeps a plateau to measure it against.**
*My expectation is that the window closes before the resolution arrives, and that is a quantitative claim
this revision either establishes or abandons.*

### OBSTRUCTION 2 — the only banked projection kernel is one already measured to have no step

A cross-window projection is **buildable** from what exists: `r7041_accept_*` carries each arm's
`eta`, `x0` and `vis` (560 points) and its k-resolved `Dlk_samp` at eight sampled `l`, so each arm's
`G_l(k) = ∫ v j_l(k x0) dη` can be formed and one arm's source projected through the other's.

⛔ **But that kernel IS the acceptance law's kernel, and the law has already been measured not to carry
the feature under test.** `r7703`: the law's own transition is some **seven times broader** at fixed
smoothing than the step. `r7707`: the law **ramps** where the measurement steps — its seven bands rise
strictly and decelerate, with no feature in them. ⇒ **A swap test on a kernel with no step cannot show a
step moving**, and a null from it would be the `r7703` leg-B failure exactly: *a gate reporting nothing
because the thing it claims to move does not exist.*

**So the swap test gets a two-sided control, registered now:** before any cross-reading is interpreted,
the swap must be shown to move **something** — the arms' own projected band RMS under their own versus the
other's kernel. **If swapping the kernel moves nothing measurable even there, the instrument is inert and
no cross-reading from it is evidence either way.** That is the finding, and it is reported as such.

## WHAT WOULD SEPARATE THEM, NAMED IN ADVANCE

So that (3) is an answer and not a shrug:

1. **The exact transfer re-projected with swapped windows** — each arm's source through the other arm's
   *full* transfer rather than the acceptance kernel. That is an instrument run and banks that do not
   exist; it is the only reading that would put the question to the object that actually carries the step.
2. **Source banks at finer k and more precision**, so the source ratio's scatter falls below a tenth of
   the step **while the low plateau survives** — i.e. more modes per comb period rather than a wider
   window. ⌗ *The present banks hold `2547` and `1452` k samples over `x = 0.04`–`13.3`; the limit is the
   bank's sampling and not the statistic.*
3. ⛔ **And one thing that would NOT settle it:** any reading whose only discriminant is the acceptance
   law, for the reason in Obstruction 2.

## LICENCES, FIXED BEFORE THE FIGURES

- **A null is not an answer unless the instrument is shown live.** Every "no difference" below is
  reported with the two-sided control that says the perturbation reaches the output, or it is withdrawn.
- **"Fails to cancel" is not the default.** Neither alternative is privileged; if the readings cannot
  separate them, both stay open and the paper gets neither.
- **No attribution**, unchanged across `r7707`, `r7709` and here: no build removes a step the arms share.
- **Nothing printed from this revision** unless a reading separates the two, and then only with its own
  licence.

## PRICE, MEASURED FIRST

Obstruction 1 is a slide over existing state: **under 10 s**. Obstruction 2's kernel is
`spherical_jn` over 560 η by up to 2547 k at eight `l` for two arms — registered at **under 300 s**, and
if it lands over that I say what it cost rather than charging it elsewhere. The baseline of any host
receipt touched goes in `BASELINE.md` before anything is added. ⌗ *`r7705`'s wire fired on 2 per cent of
run-to-run noise against a 331 s receipt; these bounds are set wide enough not to repeat that.*

## FAILABILITY

Any gate added is perturbed and the named check watched go red, over a **green control run first**. ⛔ *A
leg reporting `0` FAIL means the perturbation went TOWARDS the gate — `r7705`'s leg A — and a control that
cannot move is the `r7703` leg-B case, which is why Obstruction 2 carries its own.*
