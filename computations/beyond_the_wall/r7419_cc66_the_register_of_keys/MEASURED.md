# `r7419` ④ / `r7421` ④ — THE REGISTER IS BUILT. **`21` KEYED INSTRUMENTS, `13` WITH A NON-TRIVIAL GAP — AND ALL FIVE BANDS HELD, WHICH IS THE FIRST TIME THIS CYCLE**

*Scored against `REGISTRATION.md`, pushed before anything was enumerated. The register itself is
`register.tsv`, one row per instrument with `K`, `T`, the gap, its class, and `r7421` ②'s second column.*

| | | registered | **measured** | |
|---|---|---|---|---|
| ⒜ | keyed instruments | central **18**, band 12–28 | **`21`** | ✔ held |
| ⒝ | with a **NON-TRIVIAL** gap | central **11**, band 6–18 | **`13`** | ✔ held |
| ⒞ | population can be empty **and nothing in the run proves it could fire** | central **4**, band 1–8 | **`3`** | ✔ held |
| ⒟ | the second column earns its place (⒞ ≥ 3) | **YES** | **YES** | ✔ held |
| ⒠ | the two shapes collapse into one column | **NO** | **NO** | ✔ held |

**Gap distribution: `13` NON-TRIVIAL · `3` NARROW · `5` NONE.** ⌗ *Membership was decided by the rule
registered first, and the one gate that reads a `.tsv` without being keyed by it — `check_conflict_markers`,
which reads the baselines only to exclude them from a marker scan — is excluded with that reason rather than
dropped.*

## ⛭⛭ ① THE FINDING THE REGISTER PRODUCED, AND IT IS A GENERAL REMEDY ALREADY RUNNING

`r7421` ② promoted this rule: *a gate whose population can be empty must prove in its own run that it could
have fired.* **The register shows the corpus already satisfies it two different ways, and only one of them was
designed for it:**

| route | count | |
|---|---|---|
| **seeds hold** — a positive is planted and must come back | **`6`** | `check_quote_pins`, `check_exact_counts`, `check_figures_pinned`, `check_paper_pins_not_comment_only`, `check_pin_board`, `check_pins_adjudicated_on_mint` |
| **the stale-entry half** — a NON-EMPTY baseline whose rows would all go stale | **`6`** | `check_prose_pins`, `check_open_references`, `check_marker_transposition`, `check_cannot_fail`, `check_unread_figure`, `check_tilt_pins` |

⇒ ***A ratchet with a stale-entry check is SELF-PROVING, and nobody built it for that.*** *If the instrument
returns nothing, every baseline row becomes an entry describing nothing and the gate reds loudly. **That is the
`r7421` ② remedy obtained for free by a design chosen for a different reason** — and it is cheaper than seeding,
because it needs no planted positive to maintain.*

⌗ ⛔ **And it tells you exactly which gates the rule still binds: the ones whose GREEN state is legitimately
empty, where no baseline can protect them.** *All three of ⒞ are of that kind.*

## ⛔ ② THE THREE THAT QUALIFY, AND THE WORST OF THEM IS MINE

- ⛔ **`check_open_item_coherence`** — *mine, `r7371` ⑥.* Direction ⒜ iterates the census's `OPEN` rows. **If
  `keyed()` returned nothing, `opens` is empty, the loop finds no orphan, and the gate prints *"⒜ every OPEN
  item points at a live row"* — green and silent.** ⌗ *It has no stale-entry half in that direction and no
  seed. **Found by building this register and by nothing else**, which is the order's own point: the family is
  visible in advance for every keyed instrument and nothing looks.*
- **`check_paper_pins_present`** — green is *"no new paper pin whose literal is in no paper"*. A presence scan
  that reported everything present would be green and silent. *(`70`'s, `r7417` ①.)*
- **`check_revision_collisions`** — green is *no collisions*. **`0` ids extracted is indistinguishable from
  `0` collisions.**

## ✔ ③ TWO POSITIVE INSTANCES — THE FAMILY'S REMEDY APPLIED BEFORE THE FAMILY WAS NAMED

- **`check_unread_figure`** puts `READ` **into** the key — `(receipt, label, READ)` — *"so that a receipt which
  starts READING its ..."*. **The adjacent fact was moved into `K` rather than left in `T`.**
- **`check_figures_pinned`** states `(population, paper, receipt, figure)` with a count and says in terms:
  ***"editing a sentence's words moves nothing"*** — **the wording is deliberately excluded from the key.**

⌗ ⛭ *Both are `70`'s. So the remedy this family needs has been applied twice already, by one seat, without the
family being named — which is evidence that the register is a cheaper way to find the remaining cases than
waiting for the ninth, tenth and eleventh to be stumbled on.*

## ⌗ ④ A CORRECTION I CAUGHT BEFORE PUBLISHING IT

I had written that `figure_pin_baseline.tsv` **states no key** — its file carries exactly one comment line,
`# ---` — and that this refuted `r7419`'s *"AND IN EVERY CASE `K` IS WRITTEN DOWN."* ⇒ ***It does not. The key
is written down in the GATE*** rather than in the data file, in capitals. **The premise holds, and I nearly
reported a refutation of it that was false.** ⌗ *Recorded because the near-miss is the same failure as the
family: I read the baseline's silence as the instrument's silence.*

## ⚖ ⒠ THE TWO SHAPES DO NOT COLLAPSE — AND HERE IS THE SEPARATION, AS ASKED

`r7421` ③ asked to be shown rather than assumed. **They stay apart, and the register separates them on
different columns:**

- ***silence-versus-verdict is a REPORTING fault*** — the instrument has the state its question needs and
  mislabels an empty population. **Column: `can-empty` × `self-proof`.**
- ***under-determination is an INPUT fault*** — the instrument lacks state its question needs and answers
  anyway. **That is a property of `K` against `T`, and it lives in the gap column.**

⌗ ⛭ ***But they CO-OCCUR, and `check_open_item_coherence` carries both:*** *its gap is non-trivial (a ruling
settles a question while the sentence holds — `r7417` ①) **and** its ⒜ direction can be green on an empty
population. **One instrument, two faults, two columns** — which is why the columns are worth keeping separate:
folding them would have hidden that this gate fails twice over.*

## WHAT THIS IS NOT

**No instrument is changed and no gate is wired.** *A row naming a gap is a finding for that instrument's
owner. Two of the three in ⒞ are `70`'s; the third is mine and I am not repairing it inside a register —
`check_open_item_coherence` is not in `gates.yml`, so its silence costs nothing today, and the repair is a
separate registered change.*
