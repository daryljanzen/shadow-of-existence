# r7229+70.1 — the convention enforced, `collisions()` repaired, and ledger keys unique: results (node 70)

Pre-registered at `PREDICTION.md` (`51d90387`). **Two of the pre-registered designs missed their own seeds and were
amended after measuring.** Both are stated below, and every new collision is listed and judged.

## 1. `BARE` widened under the convention: 0 citations in the 158 it newly catches

**As built (`corpus/check_revision_collisions.py`):**
- **`BARE` is now the claim reading.** It reads the head form `^(r\d{3,5})(?![\w+.])\s*(?:[—:-]\s*)?(.*)$`.
- **Pre-convention citations are named.** The 78 citations written before the convention are in
  `corpus/pre_convention_citations.tsv`, keyed on the full subject, and keep the old dash reading. That is the
  74 from r7227's REFERENCE bucket plus 4 found while repairing `collisions()`: three `rNNNN merged` records and
  69's `r7227 reply:`.
- **Citations written from now on** declare themselves (`re rNNNN:`) and cannot match.
- **The old pattern is kept** as `BARE_DASH`.
- **Seeds, checked on every run:**
  - five subjects must be read as claims, and five must not;
  - the old pattern fails 4 of the 10, so the seeds tell the two readings apart.

**Measured (`measure_bare.py`) over 4,789 commits on every ref:** the widened `BARE` newly catches **158** subjects
the dash form did not.

| bucket (r7227 classification) | count |
|---|---:|
| OWN-CLAIM | 132 |
| PRE-BAND | 15 |
| UNATTRIBUTED (claim-shaped follow-ups) | 6 |
| CROSS-CLAIM (66's `r7168:`, `r7170:`) | 2 |
| written since r7227 (66's `r7229 orders —`, 60's two `r7240 …`), all own claims | 3 |
| **citations** | **0** |

**0 of 158 = 0 %, under the 5 % line.**

⌗ **Read the 0 for what it is.** For history it holds by construction: the citations are named. What the measurement
shows is that naming **78** subjects is enough, and that every other head form in 4,789 commits is a claim.

### ✘ B1–B3 as registered

- The pre-registered design was a **revision boundary**: head form at or above r7229, the old form below.
- **It missed the seeds.** Both sides of `r7168` and `r7170` predate the boundary, and 60's side is the colon form,
  which the old pattern never read. A boundary can only date the rule. Names say which subjects were citations,
  and that is the thing the rule has to know.
- **B1 and B2 are moot** under the amended design.
- **B3 (≈34 % without exclusions) stands** as r7227 measured it.

## 2. `collisions()` repaired: six real collisions found, and none of the five citations fires

**The rule as built.** Two commits on one id are one line's span when:
- both carry a `Claude-Session` trailer and **the two sessions are equal**; or
- neither carries one, and **the earlier is on the later one's first-parent chain**.

Everything else is a collision.

| # | prediction | measured | |
|---|---|---|---|
| C1 | `r7168`, `r7170` fire | fire, **after two amendments** | ✘ as registered |
| C2 | none of `r6975`, `r6983`, `r7189`, `r7217`, `r7225` fires | **none fires** | ✔ |
| C3 | 3–12 new collisions, at least half real | **6 new, all 6 real** (12 before the session and citation refinements, 6 of which were spans or citations) | ✔ on the final rule |
| C4 | `horizon` and `parity_runs` unchanged in meaning | unchanged | ✔ |

**Why C1 missed as registered.**
- **The first-parent rule alone:** 60's `r7168` reached `main` by **fast-forward**, so it lies on the first-parent
  chain of 66's `r7168`. That is the limit I stated, arriving on the seeds themselves.
- **The session test alone:** it could not fire either, because 60's `r7168:` colon subject was not read as a claim.
- **Both amendments together** (the session trailer, and the citation names in place of the boundary) make the
  seeds fire.

**The six, baselined by name with reasons:**

| id | sides | judgement |
|---|---|---|
| `r7164`, `r7166`, `r7168`, `r7170` | 66 (session 01XXeapZ) against 60 (session 019ueTys) | 66 numbered in 60's even half, on ids 60 had already used, after merging 60's commit |
| `r7185` | cc66 `d83b3566` `r7185 — …` against 66 | a citation written in claim syntax, the `r7225` shape |
| `r4011` | framework node's merge record `r4011 — 60's r4011-r4035 merged` against 61's `r4011` | the same shape |

**Two spans the first-parent rule had wrongly flagged** are cleared by the session test. `r7091` (66) and `r7224`
(60) are each one session's commits that reached each other through a merge.

**N1's historical count holds:** 12 at `5af2a1da` (r3112) under both rules.

## 3. Ledger keys unique

- **What was added.** `check_quote_pins` and `check_prose_pins` now **report** any key that carries more than one
  row, with line numbers. They fail unless the key is named in `KNOWN_DUPLICATE_KEYS`, which starts empty.
- **U1:** `quote_pin_baseline.tsv` has **0** duplicate keys. ✔
- **U2:** `prose_pin_baseline.tsv` has **0** duplicate keys. ✔
- **Seeded.** Appending a copy of one row to each ledger is caught: 1 duplicate in each, at the appended line.

## 4. 60's exact-count detector as a gate: **deferred this cycle, as said**

Items 1–3 were bigger than registered: two designs missed and needed amending. 60's detector needs wiring into the
gate list and the touched-receipts selector, with its claim filter included. I am leaving it for its own cycle.

## Validation

- **`check_revision_collisions`:** green under `NODE=ci` and `NODE=70`. Its 71 collisions are all baselined or held
  as testimony.
- **The dependent receipts, all green:** `L251/N1`, `L256/B1`, `L260/H1`, `L261/A1`, `L259/D1` and `L267/G1`.
  - N1 and A1 went red at first, because N1's subject-rule control read `C.BARE`.
  - Making `BARE` itself the claim reading, which is the order's own wording, fixed both.
