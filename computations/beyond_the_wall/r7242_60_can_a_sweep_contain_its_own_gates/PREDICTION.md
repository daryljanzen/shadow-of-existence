# `r7242` — PRE-REGISTRATION, written and committed before anything is built or measured

**The order.** *re `r7229`*: can a sweep contain its own revision's gates without going red on
another seat's work? The order's burden is explicit: **pre-register whether such a formulation
exists before building one, and state what coverage it would have had on the `62`.** The closure is
also explicit: a negative is a real result, and no second attempt is asked for after one.

⌗ The shape the order offers as a starting point: a sweep whose POPULATION is live but whose
ASSERTION is restricted to the claim-sites the sweeping revision itself wrote — the stamp-scoping
that repaired `S3`'s `Ⓐ④`.

---

## ⓵ DOES IT EXIST? — PREDICTED: YES, BUT THE SCOPE HAS TO BE THE SITE AND NOT THE FILE

**I predict a self-including and monotone formulation exists.** The population is read live; the
assertion ranges over the claim-sites whose *last writer* is the sweeping revision's own range. Its
own gates are in that range by construction, so it is self-including; another seat's receipt is
outside it, so another seat cannot turn it red.

⛔ **AND I PREDICT THE FILE IS THE WRONG SCOPE, which is the half I expect to be able to prove.**
Scoping by PATH — "the receipts under this seat's two directories" — is NOT monotone, because
*re `r7227`*: another seat edits this seat's receipts when a gate requires it, and three of them were
edited that way. So I predict **at least one of the `62` live claim-sites is last-written by a commit
that is not this seat's**, and that one site is enough to settle path-scoping as unsafe.

* **REFUTED** if every one of the `62` is last-written by this seat. Then path-scoping is safe on the
  evidence available and the distinction I am about to draw is one the tree does not support.

## ⓶ THE COVERAGE, PREDICTED AS A NUMBER BEFORE IT IS MEASURED

The order wants the number in advance. **A single self-including run covers only the sites its own
revision wrote.**

* **PREDICTED: between `2` and `12` of the `62`, so under `20` per cent**, for the revision that
  adopts it. My central guess is `6`.
* **PREDICTED: zero retrospective coverage.** The `62` already standing were written by earlier
  revisions, so a self-including sweep adopted now asserts nothing about any of them.
* **PREDICTED: the union over revisions is complete only from adoption forward**, and only if it runs
  on every push — which is the standing check, not a sweep.

* **REFUTED** if the single-run coverage exceeds `20` per cent of the `62`. That would mean the sites
  are concentrated in few revisions, and a self-including sweep is worth more than I expect.
* **REFUTED** if retrospective coverage is anything but zero, which would mean I have misunderstood
  what "the sweeping revision wrote" can reach.

## ⓷ SO WHAT I EXPECT THE ANSWER TO BE, STATED PLAINLY SO IT CANNOT BE SOFTENED LATER

***I expect to answer: it exists, it is safe, and on its own it is nearly useless — its value is as a
per-push gate and not as a sweep.*** The order's closure then applies in its stronger form: **the
standing check routed at `r7240` is the only coverage this class can have on the `62`, which makes it
the sole instrument rather than a convenience.**

## ⓸ A THIRD OUTCOME, PRE-REGISTERED BECAUSE THE LAST FOUR REVISIONS ALL LANDED ON ONE

The formulation is self-including and monotone, and **the interesting quantity is neither existence
nor coverage but the MONOTONICITY DIRECTION**: another seat's edit to this seat's receipt can only
REMOVE a site from the asserted set when the edit is the prescribed repair (`==` to `<=`), and can
ADD one only by writing a new exact count into someone else's receipt. If that asymmetry is
measurable on the three receipts `r7227` edited, then path-scoping is unsafe in principle but safe in
the only direction the history exhibits — and that is a sharper statement than either of my answers
above, and the one I would rather be able to make.

⌗ *Nothing in this file is measured. Every number above is a prediction, and the measured ones go in
the receipt beside them with the comparison stated either way.*
