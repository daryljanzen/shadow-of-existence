# `r7253+70.0` — PRE-REGISTRATION: the `MEANING-HELD` gate, the `target` column, and the grain re-read of `L204`

*Committed before any of the three is built or measured. It answers `FOR_70.md` `r7253`, read at `origin/main`
`3e0016ee`.*

## ① The `MEANING-HELD` gate

**What I found first, from reading the code:** `check_quote_pins` does not check the verdict vocabulary at all. Any
string in column 6 counts as adjudicated, so `MEANING-HELD`, or a typo, is already an exemption. **The gate starts by
closing that.**

**What the gate will check, in `check_quote_pins`:**

- **V. VOCABULARY.** Every verdict is one of the header's verdicts, the `UNADJUDICATED-*` buckets, `EXTENDED`, or
  `MEANING-HELD`. Anything else fails.
- **For a `MEANING-HELD` row:**
  - **H1.** The what-was-read column names `held at <sha>`. The sha is at least 8 hex digits and resolves to a commit.
  - **H2.** The held commit is an ancestor of HEAD, so the finding is held at a commit this tree descends from.
  - **H3.** At that commit, the literal is present in what the key reads:
    - for `PAPER`, a non-appendix `corpus/*.tex`;
    - for `SOURCE`, any tracked file other than the receipt itself.

    Checked with `git grep -F` at the sha, or `-P` when the literal is a regex.
    **This is the check that tells a HELD finding from an UNREAD key**: an unread key carries no commit at which its
    sentence was read.
  - **H4.** The tier is `SENTENCE`. A `TOKEN` is not a meaning pin, and under ① it survives a content-intact
    rewording.
- **Counting.** `MEANING-HELD` is reported on its own line as **held, not owed**. It is never added to
  `UNADJUDICATED`'s discharge figure: the ratchet's figure stays the count of `UNADJUDICATED`, as before.
- **Seeds, run on every pass, each of which must fail:**
  - a `MEANING-HELD` row with no sha;
  - a sha that does not resolve;
  - a sha at which the literal is absent;
  - a `TOKEN` row;
  - an unknown verdict string.

  Plus one valid row that must pass.

⛔ **The reachable negative, from 66's order.** If H3 cannot tell a held finding from an unread key, the verdict is an
exemption and should be withdrawn. **The test:** I take every `UNADJUDICATED` `PAPER`/`SENTENCE` key, stamp it
`MEANING-HELD` with the sha of HEAD, and count how many pass H1–H4.

- **If nearly all pass, H3 does not discriminate.** A key nobody read passes as easily as one that was read. **I
  predict that it does NOT discriminate on that test:** at HEAD, an unread key's sentence is present by construction,
  because its receipt is green.
- **So the discriminating fact has to be the commit's PROVENANCE, not its content.** The held sha must be a commit
  whose own diff touches this key's baseline row: the commit that recorded the verdict, or one that touches the
  receipt.
- **I therefore add H5:** the held sha must be a commit that changed this receipt, from `git log -- <receipt>`. A
  verdict-writer cannot then stamp HEAD on an unread key.
- **The negative is measured before and after H5 and reported both ways.**

| # | quantity | central | band |
|---|---|---|---|
| M1 | stamped-at-HEAD unread `PAPER`/`SENTENCE` keys passing H1–H4 | **≥ 95%** | 80–100% |
| M2 | the same, passing H1–H5 | **0%** | 0–5% |
| M3 | `L204` rows converted to `MEANING-HELD` that pass H1–H5 | **62 of 62** | 58–62 |

## ② The `target` column, with `C64` Ⓔ converted in the same commit

The baseline's column follows `r7251+70.4`'s `FLIPS.tsv` (29 rows). Then every receipt that reads the baseline is
run.

| # | quantity | central | band |
|---|---|---|---|
| T1 | receipts reading the baseline that go red on the flip | **1** (`C64` Ⓔ) | 1–3 |

Any red other than `C64` Ⓔ is converted only if this edit is what breaks it, and that is stated in the commit.

## ③ `L204`'s 99 against the grain clause

**The clause:** `DELIBERATE` where the pinned span is the shortest that carries the claim and the claim is an
IDENTITY; `REPAIR-OWED` where a strictly shorter span carries it.

**Applying the adoption at the same time:** the meaning-pin `REPAIR-OWED` rows become `MEANING-HELD` (43 paper
sentences, 17 `SOURCE` sentences, and the 2-row right-handed-neutrino pair). Formulas, code spellings, vacuous pins
and as-found defects stay `REPAIR-OWED`, because each has a repair form.

| # | quantity | central | band |
|---|---|---|---|
| G1 | verdicts the grain clause moves | **1** (`C3`'s `Type I (Bianchi, dimension three`, where `Type I (Bianchi` carries the label) | 0–4 |
| G2 | `REPAIR-OWED` → `MEANING-HELD` | **62** | 55–64 |
