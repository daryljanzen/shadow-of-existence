# `r7405` ① — MEASURED. **THREE OF FIVE REGISTERED PREDICTIONS REFUTED, EVERY REFUTATION TOWARD FEWER DEFECTS — AND THE DELIVERABLE IS AN INSTRUMENT FINDING, NOT THE COUNT**

*Scored against `REGISTRATION.md`, pushed before any site was re-read.*

## THE NUMBERS

| | | registered | **measured** | |
|---|---|---|---|---|
| ⒜ | one-state violations among the 16 (incl. ruled row `24`) | central **3**, band 1–6 | **`1`** | ⛔ central **REFUTED**, band held at its floor |
| ⒝ | classification errors among the 16 | central **0**, band 0–2 | **`0`** | ✔ **HELD** |
| ⒞ | `66`'s prior ⒜ > ⒝ | HOLDS | **HOLDS** (`1` > `0`) | ✔ held — *and on no new evidence, exactly as registered* |
| ⒟ | of ⒜, those at sites ⓬ scored `AGREES` | central **1**, band 0–4 | **`0`** | ⛔ central **REFUTED** |
| ⒠ | row `35` reclassifies to one-state | **YES** | **NO — neither class** | ⛔ **REFUTED** |

⇒ ***`0` new one-state violations at the 16. The only one is row `24`, which `66` had already ruled and
fixed.*** ⌗ And the population is **16 sites over `14` distinct passages** — row `27` shares `25`'s and row
`38` shares `35`'s — so ⓬'s 16 is 14 reads, which is a fact about ⓬'s count and not about this scan.

## ⛭⛭ THE PART THAT IS WORTH MORE THAN THE COUNT: THE DISCRIMINATOR IS **ASPECT**, NOT VOCABULARY

**The first net was built from debt vocabulary and it cannot score this class at all.** Run against the ruled
instance before and after `66`'s fix, it returns **the same two fragments either way**:

| | the sentence it matches |
|---|---|
| **PRE-FIX** (the violation) | *"One scope qualification **is owed immediately, and closing it is what makes** the classical reading a result rather than an inference."* |
| **POST-FIX** (`66`'s repair) | *"One scope qualification **belongs with** Prop. `prop:amplitude` **and is closed in this section**, which is what makes…"* |

⇒ *Both carry* `qualification`*; both would be flagged by any word-net. The debt vocabulary is **identical on
the defect and on its repair**, which is why ⓬'s word-net route could never have reached this class — the same
conclusion `r7401` ⓬ reached about classification, arrived at from the opposite side.*

**What actually separates them is the ASPECT of the discharge clause:** the violation announces the debt and
puts its discharge in the **prospective** (*"closing it is what makes…"*); the repair puts it in the
**completed** (*"is closed in this section"*). ⇒ `aspect.py` encodes exactly that — a debt term, **plus** a
prospective discharge, **minus** a completed one.

**Bound on the one case that is ruled:** flags the pre-fix sentence (`1`), does not flag the post-fix form
(`0`). ⌗ ⛔ ***And it is bound on ONE instance, so its false-negative rate is unmeasured and the `0` it returns
over the 16 is exactly as strong as that single test and no stronger.*** *I am not offering it as a gate.*

## WHY THE `0` IS NOT JUST THE NET AGREEING WITH ITSELF

Two independent routes reach it. ⒤ The vocabulary net surfaced **12 debt sentences** across the 14 passages (8 of the 14 carry one or more)
and **I read every one**; each is a status stated once — a limit named as a limit (`31`: *"have not been
sampled and no base rate has been computed"*), an open item named as owed and left so (`25`/`27`: *"named here
as owed and developed in neither this paper nor the bead"*), or a qualification raised and settled **in the
same breath** (`23`). ⒥ The aspect net, built independently of that reading, returns `0`. *Neither route is
the other's check, but they do not disagree.*

## ⒠ IN FULL, BECAUSE A REFUTED POINT PREDICTION IS WORTH ITS REASON

I predicted row `35` — heading *"What is genuinely unpaid, at its actual size"*, prose *"answered rather than
owed"* — would reclassify from ⓬'s `DISAGREES-DECLARED` to a one-state violation. **It is neither.** Read
whole, the section introduces that item as *"**one that is sharper here than in the field, and is answered
rather than owed**"* — the status is given **in the clause that introduces it**, which is the one-state form,
not a narrated debt. And it closes: *"`\S`frontier lists the seven open items in full, and **this section is
the weighing rather than the list**."* ⇒ ***The heading names the section's SUBJECT, not a status claim about
every item under it*** — so there is no classification error either. *My prediction mistook a declared
mismatch for a defect, which is the error ⓬'s own `DISAGREES-DECLARED` label exists to prevent and which I
then made anyway.*

## ⒟ IS THE ONE THAT CARRIES INFORMATION, AND IT RUNS AGAINST MY PRIOR

I registered that ⒟ — not ⒞ — was the informative number, because a one-state violation at a site ⓬ scored
`AGREES` is a defect its arm is blind to by construction. **It measured `0`.** ⇒ ***So at these 16 sites the
class is NOT invisible to ⓬'s arm: its single candidate, row `24`, was precisely the site carrying the
one-state defect.*** *The arm found the right site and named the wrong class — which is `r7405`'s own ruling,
now with a denominator: `1` of `1` candidates was a real defect, and `0` of the `14` sites it cleared hid one.*

## WHAT I AM NOT CLAIMING

- **Not that the corpus has one one-state violation.** `66` found a second in `P15` at `r7405` — the canon
  note's two-item open list — *outside this population*. This measures the 16, which is what was asked.
- **Not that `aspect.py` is ready to gate anything.** One binding case, `0` measured false negatives because
  there is nothing to measure them against.
- **Not a ruling on any site.** `0` new candidates means there is nothing here for `66` to rule.
