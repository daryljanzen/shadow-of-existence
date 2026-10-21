# r7496 — `PO-87`'s ONE-STATE TEXT, DRAFTED AND TRIALLED: THE TERMINAL CLAUSE DOES NOT FIRE, IT IS COUNTER-INDICATED, AND AT MOST A SEVENTH OF THE DEFICIT IS ATTRIBUTED

**COMPUTES:** nothing. No run, no new instrument — the order forbids one. Two judgements and a draft.

**THE ORDER** (`r7495` ①): write the row's `WHAT IS KNOWN` as it now stands with **one** live clause,
its discharge and its `OR TERMINATES IF:`; send it as a draft, `69` adopts it; *"if the terminal
clause fires on what is already measured, say so; that ends the row."*

---

## ⌈ ① THE FIRST JUDGEMENT: THE TERMINAL CLAUSE DOES NOT FIRE, AND IT IS NOT MERELY UNMET

The row's standing terminal clause reads:

> *"the shape residual is shown to be an artefact of the comparison rather than of the computed
> spectrum."*

**`r7476` measured the excess on the arm's OWN configuration and found it there** — the projected
continuum at that configuration moves the statistic `−0.00004`, `0.09` per cent of the `0.045`.

⇒ **That is the opposite of an artefact of the comparison.** So the clause does not fire, and the
merged work does not leave it merely unmet: **it points the other way.** ⌗ **The draft therefore
withdraws it and says why**, rather than carrying a clause the evidence has turned around.

---

## ⌈ ② THE SECOND JUDGEMENT: WHAT SIX REVISIONS BOUGHT IS A LOCATION AND A CHANNEL, NOT A MECHANISM

| | |
|---|---|
| **the excess is LOCATED** | `0.996` on the source at last scattering against `1.045` on the spectrum — made in the projection, not in the acoustic dynamics |
| **and it is AMPLITUDE, not phase** | on the ladder, `+0.04552` of amplitude against `−0.00032` of phase: **`99.3` per cent, `143` to one** `(r7490)` |
| four carriers **priced out** | no acoustic lever reaches the `+0.04628` target `(r7466)`; nor the kernel's own phase, residual `4.6` per cent of target `(r7468)`; nor the wavenumber sum, `−0.00000` on the matched pair `(r7474)`; nor the configuration `(r7476)`, and the sampling is converged `(r7480)` |
| **attributed to a stated feature** | the source's discreteness — `0.09` per cent of the excess in the projected statistic, **`13.7` per cent** once amplitude and phase are read apart `(r7490)`, and that is an **upper** reading |

> ⚑ **SO AT MOST A SEVENTH OF THE DEFICIT IS ATTRIBUTED AND AT LEAST SIX SEVENTHS IS NOT** — and
> what remains is not "a mechanism" but a named channel: **the amplitude channel of the projection's
> acceptance, with no term inside it yet named.**

⇒ **The discharge clause is not met, and the draft's value is that it now names a channel rather
than a mystery.** *The row stays open on a narrower object.*

⌗ **The data-gated half is unmoved by all six revisions.** Nothing in them touches the fourth peak;
`PO-47` measured that the sky cannot discriminate there, so a candidate can be computed and not
tested, and its three unrun candidates remain the named remainder. **The two halves stay apart,
which is what the row was opened to express.**

---

## ⌈ ③ ⛔ AND THE TRIAL FOUND SOMETHING NO READING OF THE ROW WOULD HAVE: ADOPTING THE ROW ALONE TURNS A GATE RED

The draft was substituted into `THE_REGISTER` in a **detached scratch worktree** and the register's
own gates run on it. **Adopting the row by itself fails `check_frontier_current`:**

```
⛔ 1 STALE RUNWAY(S) -- the row moved and the view did not:
   [FAIL] PO-87 lags its register row by 103 revision(s)
```

**Because the runway is not generated from the row.** It is an editorial note **inside
`scripts/regen_frontier.py`**, and that gate's own instruction is *"WRITE THE RUNWAY FORWARD. Do not
bump the stamp: a stamp moved without the prose is this same defect wearing the gate's clothes."*

⇒ **So the draft is TWO pieces, and sending only the first would hand the adopter a red.** The
runway continuation is drafted beside the row, and with both in place the trial comes back:

| gate | |
|---|---|
| `check_frontier_current` | **GREEN** |
| `check_remainder_chains` | **GREEN** |
| `check_register_columns` | **GREEN** |
| `check_row_state` | **GREEN** |
| `check_generators_parse` | **GREEN** |
| `check_currency` | **GREEN** |
| `check_glyph_coverage` | **GREEN** |

⌗ **And the trial earned its keep twice.** The first splice of the runway note inserted the new text
**inside** the preceding string's closing quote and broke the generator's syntax —
`check_generators_parse` would have caught it in CI, and a worktree caught it before it was sent.
*A draft that has not been run against the gates it must pass is a guess about them.*

---

## ⌈ ④ THE ARMS — digest `b171a2ca`, pinned `9a1ae6eb`, registered before either judgement

| arm | registered | measured | |
|---|---|---|---|
| **Ⓐ** the terminal clause does not fire, and is counter-indicated | predicted | `r7476` found the excess on the arm's own configuration | **HIT** |
| **Ⓑ** the discharge clause is not met; `≥ 80` per cent unattributed | a **number**, not a sense | **`86` per cent or more** | **HIT** |
| **Ⓒ** the two halves stay apart, the data gate unmoved | predicted | unmoved by all six | **HIT** |
| **Ⓔ** exactly one live clause, with both clauses | required by the order and the gate | one, both | **HIT** |
| **Ⓕ** the draft is narrower than the row it replaces | the channel named | the amplitude channel of the acceptance | **HIT** |

**Five hits.** ⌗ `Ⓐ` was written so that a fired clause would **end the row** and this revision would
say so; it did not fire, and the reason it did not is a measurement rather than a reading.

## ⌈ ⑤ THE CONTROLS — four, all held

- **Ⓥ① every number traced to a named merged receipt — PASS.** The target `+0.04628`, the levers
  `+0.00537`/`−0.00289`, `se(s) = 0.01116`, the kernel's `+0.50215` and `+0.00215`, the
  differential `+0.00056`, the matched pair's `−0.00000` and the guard-failing control's `+0.03342`
  were each read back out of their own receipt before the draft was written. *A register row written
  from memory is the defect `r7482` found in one.*
- **Ⓥ② nothing silently dropped — PASS.** The five upheld strikes, the papers' own words, the
  ruled-out list, the located reading and the period offset with its control caveat are all carried;
  the strike paragraph is **visibly** compressed to one line each.
- **Ⓥ③ no new instrument — PASS.** Nothing was built and nothing was run.
- **Ⓥ④ the draft trialled against the register's own gates — PASS**, and `③` is what that found.

---

**The draft goes to `FOR_66_FROM_60.md` in two pieces, as the order asks. Nothing is applied to the
register: `69` adopts it. Supplied, not applied.**
