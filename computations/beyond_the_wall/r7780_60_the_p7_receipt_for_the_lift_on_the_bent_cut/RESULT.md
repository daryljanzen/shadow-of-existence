# r7780 (60) — RESULT

**Order `r7779` (69): mint the `P7` receipt for the lift on the bent cut, from `r7776` and `r7778`.**

**The receipt is minted, registered in the INDEX, and green: `14` checks, all pass.**
`receipts/P07_CR_framework/P07_the_lift_on_the_bent_cut_is_a_second_number_beside_the_vacuum_bound_and_no_bead_condition_carries_the_radiation_coefficient.py`

**Eight arms were registered. All eight are in the receipt; `⑧` is PRINTED rather than checked, and the
reason is that the gate caught it by `⑧`'s own registered criterion** — see Ⓔ below.

---

## The four things the order asked for

| the order | what the receipt carries |
|---|---|
| the lift's excursion against `πα/3` | `5461.007981` Mpc against `5459.341081`, `+3.0533e-4` — **and the same integrator at `K = 0` returns the bound**, so the excess is the bend's and not the quadrature's |
| the two radicand zeros | **exactly two**; the inner is `K/2M` to better than `5e-10` relative, the outer inward of the vacuum turnaround by `1.3174e-4` |
| the `1/2` exponents on both legs | `0.500` on **both** legs of the bent cut — **and the vacuum cut on the same machinery gives dust's `0.667`**, so the measurement distinguishes them rather than returning `1/2` by construction |
| the structural row: no bead condition carries `K` | all **six** conditions have **zero** derivative with respect to `K`, taken symbolically |

**And the ruling is respected in the receipt's shape, not just its prose:** Ⓐ① *reproduces* `πα/3`, so
nothing in it reads as a contradiction of `thm:bead`; the bent value stands beside it as a second number.

## ⛭ The one thing the order did not ask for, and it strengthens the ruling

**`thm:bead` calls the bound *"fixed by the exponent and independent of `M`"*, and on the Nariai member
that clause cannot be tested at all** — the Nariai condition fixes `M` from `α`, so there is one mass
and nothing to vary. **Ⓐ② leaves the member and evaluates the same integral at five masses:
`0.3, 0.7, 1.0, 1.5, 3.0` times the Nariai offset. Every one returns `πα/3` to `1e-12`.**

⇒ **So the clause is now failable and still standing.** The ruling that the theorem stands as stated
rests, after this, on a measurement rather than on the absence of one.

## The three-state locate arm the order asked for

Both subjects — `thm:bead`'s bound clause and the lap caption's *"three closed-form segments
(collapse, lift, expansion)"* — resolve **MATCHED** on this tree. **The three states exist because a
two-state arm returns the same verdict for a sentence that is WRONG and one that has been DELETED,
which is precisely what happened to `r7768`'s arm 6 when `r7767` removed its subject.**

## Ⓔ The gates caught two defects in this receipt, and both were worth catching

**⛔ ① The hollow assertion, caught by `⑧`'s own registered criterion.** The registration named *"a gate
that cannot fail"* as arm `⑧`'s reachable negative — and the first form of `⑧` was
`check("… declares its scope …", True)`. The hollow-assertion lint named it on its own line.
**Fixed by PRINTING the scope statement instead of checking it (SCOPE-AS-CHECK), not by exempting the
file.** *A check that cannot fail adds a PASS to the count and tests nothing.*

**⛔ ② The figure was pinned in the units the receipt computed in, not the units the sentence prints.**
The INDEX row cited the excess as a figure `3.0533`; the receipt pinned `3.0533e-4`. `check_figures_pinned`
flagged it, and it was right to: **a pin on `3.0533e-4` does not hold the figure `3.0533`.** Fixed by
pinning the same measurement in parts per ten thousand — the units the citing sentence uses — so the
printed figure is failable AS PRINTED.
⇒ **GUARD: a sentence's figure has to be failable in the units the sentence prints it in.**

⌗ *And the pin is verified failable: perturbing `K` by two per cent turns the excursion check red.*

**⛭ And the suite's single failure went with them.** Before these fixes the scoped suite reported one
red, `L_probability/S47`, whose arm runs a set of receipts and requires each to exit `0`. On the fixed
tree it passes in `211` s. **So that red was downstream of this receipt's own hollow assertion** — the
ledger-counting arms see a cannot-fail check as a change in the tree, which is what they are for.

## What this revision does not claim

- **It does not contradict `thm:bead`**, which Ⓐ① reproduces to twelve digits and Ⓐ② confirms off the member.
- **It does not say at what epoch the deposited plasma becomes the bend.** That is the open question
  `r7778` named and the order holds for the next revision — *"After that, the open question you named"*.
- **It decides nothing about the progenitor's radiation content.**

## ⛔ And the landing is blocked on an operation this session cannot perform

`r7779` landed this line's last three revisions as **rebased copies** rather than merges, so the base
branch now holds a second commit for every one of this line's — same subject, same session trailer,
different hash. A merge of the base branch therefore puts both copies in one history, and
`check_revision_collisions` fires on three of this line's revision numbers, correctly: its rule is
that a span is a chain and a collision is two commits claiming one id with neither an ancestor of the
other. **A fourth collision is mine** — a merge commit of mine carried another line's `rNNNN (seat)`
at the head of its subject.

**The repair is the one the standing rule prescribes for a branch whose content has merged: restart the
branch from the base branch with only the new work on top.** It was built and verified here — identical
tree, every dropped commit confirmed present in the base branch one by one, and the collision gate goes
from four failures to clean. **It needs a force-with-lease push, which this session is not permitted to
make**, so the revision sits validated and unpushed.

⇒ **Routed to `69`: merge this line's branch rather than rebasing it.** A merge keeps each commit's
identity, so a revision number stays one chain. Otherwise this recurs for every seat, every landing.
⇒ **GUARD, mine: never put another line's `rNNNN (seat)` at the head of a commit subject.** Cite it
inside the sentence, where the claim reading does not take it as a claim.
