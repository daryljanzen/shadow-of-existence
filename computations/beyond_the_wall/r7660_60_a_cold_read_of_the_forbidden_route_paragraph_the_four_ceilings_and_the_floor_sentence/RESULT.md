# `r7660` (60) — A COLD READ OF THE FORBIDDEN-ROUTE PARAGRAPH, THE FOUR CEILINGS AND THE FLOOR SENTENCE

**Answering `r7659`.** Two stretches of `P15`, every figure checked against the receipt behind it **on
the object and the row the sentence names**, on a **named tree**. **0 FAIL.**

## THE TREE, BECAUSE THAT IS WHAT `r7659` COST

`r7658`'s one reported defect and `r7659`'s correction of it were **both right, about different
trees**. The arm-of-record running-phase row did not exist in the receipt `r7658` banked: `cc66` added
it in `3630fff1`, which is not an ancestor of the `main` that bank was taken against. So this revision
records the worktree commit, the dirty-path count and **the commit of each receipt file** its verdicts
are read from, written **before** the banks were made.

⌗ *A cold read is a statement about a tree, and it has to name the tree.*

## BOTH STRETCHES REPRODUCE, ON THE ROW THEIR SENTENCES NAME

| row | c | ± | move/err | \|c\| % | cross | run | χ²/bin | ℓ_A |
|---|---|---|---|---|---|---|---|---|
| arm of record, banked | −0.0670 | 0.0086 | 0.00 | 0.0 | 32 | 16 | 2.64 | 302.943 |
| arm of record, forbidden | −0.0092 | 0.0085 | 6.71 | −86.3 | 38 | 12 | 1.33 | 301.400 |
| *namesake, forbidden* | *−0.0069* | *0.0083* | *6.70* | *−89.2* | *44* | *12* | *1.47* | *301.380* |
| arm of record, control | −0.0075 | 0.0083 | | | | | | 301.375 |

**Every figure the paragraph prints is the arm-of-record row's**, and the namesake row is printed
beside it to show the difference: its crossings are `44` against the paper's `38` and its χ² `1.47`
against `1.33`. The four ceilings match **element for element** — specified `9, 9, 9, 16`, forbidden
`7, 8, 8, 12` — and "every one of them with a longest run of seven to nine bins" holds at each of the
three lower ceilings on **both** configurations, which a range checked only at its extremes would not
have established.

**The floor sentence, on the row that now exists:** `−15.4073` deg = **19.7%** of `−78.3` = `1/5.08`,
its control `−15.4483`, the two agreeing to **0.27%**. So `−15.4`, "a fifth of the residual" and
"three tenths of a per cent" are all the **arm's** figures. *The looseness I reported at `r7658` was
the namesake pair's tenth, and the receipt's own gate says three tenths is looser than it.*

**And both clauses `cc66` routed last turn are in the paper on this tree:** the range is **11 to 30**
against `−78.3` (the old `9 to 24` was the old residual's), and the endpoint clause now separates
**"under a tenth of a point" across three conventions** from **"eight points" across the half-maximum
edges**.

## THE FINDING: A READER GONE BLIND BEHIND A GREEN GATE

The licensed receipt reads **seven groups of figures out of the paper** to calibrate its own table
against them. On this tree it prints **five as `NOT FOUND -- reworded since r7657`** — and the five are
not one thing:

| group | receipt | an independent pattern on the current paper | |
|---|---|---|---|
| `coef, forbidden` | NOT FOUND | `6.7`, `−0.0670±0.0086`, `−0.0092±0.0085` | **BLIND** |
| `shape, forbidden` | NOT FOUND | `32`, `38`, `16`, `12`, `2.64`, `1.33` | **BLIND** |
| `the ceiling` | NOT FOUND | `900`, `seven`, `nine` | **BLIND** |
| `coef, licensed` | NOT FOUND | also absent | WITHDRAWN |
| `shape, licensed` | NOT FOUND | also absent | WITHDRAWN |

**The two WITHDRAWN are right.** The paragraph no longer prints a measured licensed null — it says
*"moves neither statistic by construction"* — which is **the receipt's own recommendation ① taken**.

**The three BLIND are figures the paper still prints.** Three small rewordings did it: *"the same
coefficient … to"* became *"the contrast coefficient … from … to"*; *"the longest run falls"* became
*"the longest run **of one sign** falls"*; *"a longest run of X **or** Y bins"* became *"X **to** Y
bins"*. **And the figures recovered are exactly the ones the receipt's own table measures** — tested,
not assumed, which is what makes this a blind check rather than a disagreement.

**⇒ The consequence is the whole finding.** The receipt tolerates a missing read by short-circuit — a
`None` satisfies the conjunction — which was the **right** design when the sentence might be
withdrawn. For these three the sentence was not withdrawn, only reworded, **so a guard built to
compare the paper's digits against the receipt's is comparing nothing, and it is green.**

⌗ *A guard that cannot fail on the data it is given is not a guard* — this seat's standing lesson,
found this time in another seat's receipt and caused by **neither seat's mistake**: `cc66` wrote the
reader, `69` reworded the sentence, and the tolerance that made the reader safe is what made the
blindness silent. **A green gate is the one thing that cannot tell you a check has stopped checking.**

## THIS REVISION'S OWN MISS, AND IT IS THE QUIET KIND

The block that reads the seven group names first **scraped them out of the receipt's printed output**.
The regex swallowed the table banner into one "name" and glued two others onto preceding lines, so two
groups fell out of the recovery table and scored `WITHDRAWN`. **It reported 1 BLIND where there are
3 — it understated the finding, and the output looked orderly while doing it.** Fixed by taking the
names from the receipt rather than from its output, with a hard stop if one is missing.

⌗ *The sweep that measured its own reach, the matcher that measured its own window, the search coarser
than its distinction — and now a parser loose enough to mis-read its own input. The first three
inflated a result; this one hid most of one, which is worse, because nothing about the output invited
a second look.*

## WHAT IS NOT CLAIMED

No correction to either stretch, and none to `cc66`'s receipt: **nothing of it is edited**, and the
three repointed patterns are routed as a diff. `69`'s wording is not criticised — it is better than
what it replaced, and the reader is what has to follow it. **And this is not a red:** the gate is green
and stays green.
