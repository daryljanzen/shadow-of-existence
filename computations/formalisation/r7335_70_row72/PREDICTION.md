# `r7335+70.1` — PRE-REGISTRATION: row 72, closed FRW with a free `a(T)`. Three curvature claims priced at `170` (band 110–260, stop 320). ⛔ Rows 59 and 62 are NOT built: they are outside the engine, routed with their reasons. ⌗ The seat claims row 72 here, before building, so that no other seat starts it

*Orders: `FOR_70.md` §`r7335` ④.1, "keep going on the reopened block under the same discipline", read at `origin/main`
`d4d9f89e`. Written before any Lean.*

**Which rows are open:**
- Of the 18 rows `ROWS.tsv` marks CHART-EXCLUDED → REOPENABLE, eight are 70's (landed at `r7333`) and seven are 71's (landed).
- **That leaves 59, 62 and 72**, which neither split named. 71's `r7335` order says its assignment is done.
- **So I take 72, and register the claim here first.** After L147, the head of a queue is announced before it is
  worked.

## Row 72 — what is built

**The receipt:** `P10_canonical_time/P10_the_ultraviolet_object_is_a_rank_sequence…`, read for its claims only.
**The metric:** `g = diag(−1, a², a² sin²χ, a² sin²χ sin²θ)` in `(T, χ, θ, φ)`, with `a(T)` free, and profiles equal
to `sin²` near the point (the convention).

Under THE connection:
1. **`R = 6(aä + ȧ² + 1)/a²`** (receipt l.310).
2. **`Weyl² = 0` for every `a`** (l.312), as `weyl2C`.
3. **Gauss–Bonnet as an exact total derivative:** `a³ · gbC = 24 d/dT(ȧ³/3 + ȧ) = 24 ä(ȧ² + 1)` (l.355).

**The new driver:** `g_φφ` is a product of THREE one-coordinate profiles, `a(T)²·sin²χ·sin²θ`. `pr_d1`/`pr_d2`
cover two, so I write a three-factor recipe through `d2_of`, the same way as the two-variable one. It goes in the
instance file, and is not moved into `ShadowEngine` (`r7335` ④.2). The full contractions need a component
table (`fin_cases`), as E3 and row 45 do.

| | central | own band | P(outside own) at the central | P(outside 71's 60–170) at the central |
|---|---|---|---|---|
| row 72 (claims 1–3, the three-factor recipe included) | **170** | 110–260, ⛔ stop 320 | 0.29 | 0.50 |

- σ = 0.4 is chosen, as at `r7333`.
- **71's band:** I put row 72 at its top edge. Under the band means the three-factor recipe was cheap; over means
  the table was the driver. **Either way the count says which.**

**Not built from the receipt:**
- the rank-2 and rank-5 claims (linear independence over jet polynomials, l.381/385/438);
- the de Sitter evaluation (l.403), except as it follows from 1;
- the asymptotic series, the dimension arithmetic, and the integer checks (§1, §2, §5–6).
- ⇒ **Those are not curvature-of-a-metric statements.** The row is landed on its curvature core and says so.

## ⛔ Rows 59 and 62 — not reachable by this engine, so routed rather than built

- **Both are 3D, on S³, with a NON-diagonal metric:**
  - 59 is `eᵀ exp(εH) e` in Euler angles, so `g_ψφ = cosθ/4` already at background.
  - 62 works in the left-invariant frame with structure constants.
- **Both are ε-truncated at ε⁴.** The curvature content is one scalar coefficient: 59's `−88/15` on the `H4` harmonic,
  and 62's `R = 6 − 2p₂ε² − (10/3)p₃ε³ − (7/12)p₂²ε⁴`.
- **About 70–80% of each file is ranks and linear solves over jet invariants.**
- ⇒ ***"CHART-EXCLUDED → REOPENABLE" does not hold for them under a 4D diagonal engine.*** Reaching them needs a 3D
  non-diagonal (or frame) Christoffel form and a truncated exponential. That is engine work, and it is 71's to decide.
- **Routed to 71 and 66.**
- **One defect seen in passing, routed to the receipt's owner, not fixed:** row 62's receipt sets `CHECKS[2] = (…volume…)`
  at l.451. Index 2 is the `R(δ) = 6` gate from l.136, shifted when the scope-as-check removal happened at l.97. So that
  gate's result is overwritten in the final tally.

## My probabilities

| quantity | p |
|---|---|
| row 72 lands, all three claims | 0.75 |
| it lands inside 110–260 | 0.6 |
| `Weyl² = 0` closes by the table plus `field_simp; ring` without a hand-written combination | 0.6 |
| no proof body is opened | 0.9 |

## Not done

- Rows 59 and 62 are not built.
- No engine proof body is read.
- **No π_d:** there is no second reading.
- The applier machinery stays stopped.
