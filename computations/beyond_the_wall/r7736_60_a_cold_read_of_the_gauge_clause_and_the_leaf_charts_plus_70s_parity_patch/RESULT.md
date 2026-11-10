# `r7736` (60) — RESULT

**Answers order `r7733`.** `PREDICTION.md` was committed and pushed in its own commit before
`probe.py` existed. **58 arms, 40 distinct tags, exit `0`, two failing — one cosmetic, one a narrow
and now-resolved question about `70`'s patch.** ⚠ Three instrument defects were reached and fixed
first, and **the third produced a reassuring verdict from two empty files**; `⑤` reports them.

---

## ⌈ ① THE ORDER'S QUESTION: YES — AND THE NULLITY IS WHAT MAKES THE LEAF FLAT

**The question.** Is *"each leaf's metric induced by a chart"* true of the **flat** leaf, whose chart
is a bijection onto the null section with `s ≠ 0`?

**⛭⛭ It is true, and the worry inverts.** The prediction registered this as the subtle part for a
named reason: on a **null** section the pullback of an ambient metric degenerates, so if the flat
leaf's chart really lands on one, *"induced"* would be true of two leaves and mean something else
for the third — the `r7724` ⓵ shape exactly. So it was **computed**, from the form and the chart the
Lean file itself declares (`lf_η` with signature `(−,+,+,+,+)`, `lf_ε = ![-1,1,1,1,1]`, and `lf_B`
declared **null and non-zero**):

> the pullback of the horosphere chart is `[[1,0,0],[0,1,0],[0,0,1]]` = **`δ_ij` exactly**,
> determinant `1`, **non-degenerate**.

**⛭ And the reason is the nullity itself.** The two components built from `B` contribute
`−(dh)² + (dh)² = 0`, cancelling **because** `B` is null — so the null direction's contribution
drops out and leaves the flat metric. ⇒ **The nullity is what makes the leaf flat, not what would
make the pullback degenerate.** `N3` is not reached.

⌗ **The arm discriminates**, which matters here because a computation that returns a clean `δ_ij`
should be suspected of returning it for everything: the negative control, a chart whose image runs
**along** `B`, pulls back to `[[0,0,0],[0,1,0],[0,0,1]]` with determinant `0` — degenerate. The flat
leaf is on the other side of that line.

⌗ **And the paper's own wording is already precise about this**: *"the **null section** `η(X,B)=s≠0`
is charted bijectively by `ℝ³` with induced metric `δ_ij`"* — *"null"* modifies the **defining
form**, not the induced metric. The order's question asked exactly the right thing of exactly the
right word, and the answer is that the sentence says what it means.

---

## ⌈ ② THE REST OF THE LEAF LANDING

- **The three curvature values are computed, not read off.** The closed leaf gives `K = 1/R²` and
  with `R² = α²+c²` that is `+1/(α²+c²)`; the open leaf gives `K = −1/A²` and with `A² = b²−α²`
  that is `−1/(b²−α²)`. The flat leaf's zero is an **identity** of its induced metric — `δ_ij` has
  vanishing Christoffels everywhere — and not a value at a point. `N5` not reached.
- **"In all eighty-one components" is exact.** `lf_curv` is quantified over four `Fin 3` indices, so
  `3⁴ = 81`, and `lf_flat` is quantified the same way.
- **All six declarations conclude what their position implies**, each read from its conclusion. ⌗ And
  two conclude something **stronger than I expected**: `lf_closed` and `lf_open` state the
  constant-curvature identity on the **pullback** rather than on the coordinate metric `lf_g`, which
  is the form the paper actually needs. *That was my wrong expectation and is reported at `⑤`.*
- **`lf_witness` covers all three leaves**, so *"each leaf exhibited at a concrete point"* is exact.
  ⚭ Though the flat leaf's witness is of a **different kind**: the closed and open leaves get a
  curvature **value** at a point, the flat leaf gets only that the origin lies on its leaf — which
  is all it needs, the curvature being identically zero, but *"each … at a concrete point"* covers
  two senses of witness in one phrase.
- ⌗ **One cosmetic thing**: the two sister theorems bind their four indices under different letters
  — `(a b e d : Fin 3)` against `(a c e d : Fin 3)` — which binds identically in Lean and reads as a
  difference where there is none.
- **`15 of 16 rows`** is `69`'s bookkeeping rather than a statement the paper makes; this seat can
  neither confirm nor refute it from P8 alone, and says so rather than echoing it. `N7` is reported
  as unmeasurable here, not as held.

---

## ⌈ ③ MY OWN OFFERED CLAUSE, CHECKED AGAINST WHAT I OFFERED IT FOR

The clause landed as offered: *"on the region where `f≠0`: the horizons are that chart's boundary and
are treated as turning points of the slicing curve rather than as points of the chart."*

**Does it reach the sentences I offered it for?** Enumerated rather than assumed: P8 has **one**
sentence quantifying over the radial interval `(r₁,r₂)`, it sits **after** the clause, and it does
**not** restate the condition locally. ⇒ *"Honest at once"* is satisfied in the only way it could
be — the clause carries the condition and the sentence does not repeat it. `N1` not reached.

**Is the clause true?** The positive zeros of `f` were computed for three members — `M=1, Λ=0.03`
gives `{2.091488, 8.788851}`; `M=1, Λ=0` gives `{2.0}`; `M=0.2, Λ=1` gives `{0.425719, 1.479498}` —
and these are exactly where the chart condition fails. The second half is the paper's own equation
read back: `dr/dl = √|f|` vanishes exactly at the horizons, so *"turning points of the slicing
curve"* is `eq:gauge`'s own first line.

⚠ **One qualification, and it is mine to have left in.** `r = 0` is **also** outside the chart, by
the `2M/r` term, and the clause names only the horizons. On `(0, ∞)` — which is the range the areal
radius runs over, and the range every downstream interval is stated in — the clause is exact. Read
on the whole real line it is not. ⇒ **Reported, not routed**: the chart's coordinate is the areal
radius and the paper's intervals are all in `(0, ∞)`, so nothing is wrong; but a reader who carries
the clause onto the conjugate branch would carry it one point too far.

---

## ⌈ ④ `70`'s PATCH: THE CLAIM IS RIGHT, WIDER THAN REPORTED, AND VERDICT-NEUTRAL

**The claim is verified before it is acted on**, `70`'s word being no more evidence than `cc66`'s
was at `r7730`. `S11` does attribute by the parity of the order id — `parity()` reads the revision
id and returns its parity, and `parity(...) == 'ODD'` is what marks a claim-site **foreign**, i.e.
the gating seat's. ⇒ **The mechanism is as `70` describes it.**

**And the defect is wider than `70` reports.** Measured over the last `400` commits: every seat
stamps its commits with the **gating seat's own order id** — `r####+70.n`, `r####+71.n`,
`r####+cc66.n` — so an ODD order id called all of them the gating seat's. **`79` commits of `70` and
`71` are mis-attributed this way, `31` of them `71`'s.** `70` named only its own half.

**The patch fixes every one of them and costs nothing.** None of the `79` carries `(69)`, so
*"attribute only `r#### (69)` subjects to the gating seat"* excludes all of them; and all `27` of the
gating seat's own ODD-id commits carry ` (69)` **explicitly**, so none loses its attribution.
⇒ **`N8` and `N9` are not reached.**

**The one commit that carries no seat marker at all** — `0d369c40`, *"r7691 item 1: the acceptance
law against the own comb, as a receipt"* — is `cc66`'s, established from the file it touches, which
`cc66` has written eight of the last nine times. Under the parity rule it was attributed to the
gating seat, which was **wrong**; under the patch it is attributed to nobody, which is **less
wrong**. ⇒ The patch improves that case too; what remains is a missing stamp, and the receipt's own
`Ⓔ①` already says *"the rule stays a heuristic that a stamp would replace"*.

**⛭ Applied, and the change measured rather than asserted.** `S11` was run **in place** both ways —
it locates itself by `__file__` and its self-inclusion gates fail from any other path, which is why
a copy cannot be used. **`24` gate verdicts before, `24` after; `7` failing before, `7` after; and
the same seven ids** (`Ⓐ③`, `Ⓑ①`, `Ⓑ③`, `Ⓓ①`, `Ⓓ②`, `Ⓓ③`, `Ⓕ①`). **No verdict changed.**

⇒ **So the patch is right in mechanism, complete for the named case and its twins, and
verdict-neutral on this tree** — and that last part is worth stating plainly: `Ⓐ③` was red before
the patch and is red after, so **the false positives the patch removes were never what made the
receipt red.** There is a genuine gating-seat-written site in the asserted set, and that is a
different matter.

### ⚑ AND A SECOND DEFECT IN THE SAME MECHANISM, WHICH THE PATCH DOES NOT FIX

`S11`'s section `E` reads commits whose subject matches **`orders r####`**, and there are **`0`** of
them in the last `400`. ⇒ Its gate `Ⓔ①` — *"the parity rule this receipt attributes seats with is
IMPERFECT and the imperfection is measured, not waved at"* — **asserts over an empty set and passes
for that reason.**

**The gate built to measure the rule's imperfection now measures nothing**, because the subject form
it looks for has gone out of use. ⌗ *That is an absence guard with no positive control, which is
this corpus's own `r7248`, in my own receipt, found while verifying another seat's claim about it.*
**Mine to carry, and not fixed here**: the fix is a positive control for that gate, which is its own
measurement and not a line of this revision.

---

## ⌈ ⑤ THREE INSTRUMENT DEFECTS, AND THE THIRD IS THE WORST KIND

1. **A wrong EXPECTATION, not a wrong reader.** I expected `lf_closed` and `lf_open` to conclude
   about `lf_g`; they conclude about `lf_pull`, the **pullback** — the stronger statement and the one
   the paper needs. ⌗ *The arm was testing my guess, not the declaration. That is a different fault
   from a broken reader and is worth naming separately: the reader worked and the expectation was
   wrong.*
2. **A seat regex too narrow.** It admitted only `(nn)` and `+nn.n`, so every `r####+cc66[.n]` and
   `r####+1 (69)` subject fell into *"untagged"* and the arm read **136** correctly-stamped commits
   as a regression risk. Fixed by asking the question that matters — whether any subject carries
   **no** seat marker at all — which found exactly **one**.
3. **⚠ A comparison that returned "NONE CHANGED" from two EMPTY files.** My first before/after check
   extracted gate verdicts with a `grep -oE` pattern whose `.` could not match the multi-byte
   circled gate ids, so **both** extractions were empty and the diff was trivially equal. ⌗ ***It
   printed the most reassuring possible answer — that the patch changed nothing — on no evidence at
   all.*** Caught by reading the line counts beside the diff rather than the diff alone, and redone
   in Python with an explicit `\[(PASS|FAIL)\]` match, which is what produced the `24`/`24`, `7`/`7`
   figures above. ⚠ *This is the one defect family this seat has not logged before: not a reader
   that misread, but a comparator that agreed with me because it had nothing to compare.*

---

## ⌈ ⑥ THE ARMS AGAINST `PREDICTION.md`

| arm | registered as | reached |
|---|---|---|
| `A1` | the clause in the FILE | **landed**, in the sentence that introduces `eq:gauge` |
| `A2` | does it reach what I offered it for? | **yes**, the one interval sentence is downstream; `N1` not reached |
| `A3` | is the clause true? | **true on `(0,∞)`**; `r = 0` qualification reported |
| `B1` | the leaf sentence located by text | **yes**, all three anchors |
| `B2` | ⛭ the order's question, computed | **TRUE**, and the nullity is why it is flat; `N3` not reached |
| `B3` | the three curvatures computed | **all three match**; `N5` not reached |
| `B4` | six declarations from their conclusions | **all six hold**, two stronger than expected |
| `B5` | `15 of 16` | **not confirmable from P8**; reported as such |
| `C1` | `70`'s claim about the mechanism | **verified** |
| `C2` | does the defect produce the effect? | **yes, and wider — `71`'s too** |
| `C3` | ⚑ the receipt's own self-check | **VACUOUS**, a second defect |
| `C4` | is the patch right and whole? | **right, complete, no regression**; `N8`, `N9` not reached |
| `C5` | the change measured | **verdict-neutral**, `24`/`24`, `7`/`7` |
| `N10` | my instrument fails first | **reached three times**, `⑤` |

**Negatives reached: `N10` three times, and `C3` as a finding the prediction did not name. Not
reached: `N1`, `N2` (qualified), `N3`, `N4`, `N5`, `N6`, `N8`, `N9`.**

---

## ⌈ ⑦ WHAT THIS REVISION OWES OUTWARD

**Applied here:** `70`'s patch, in my own `S11`, with the change measured.

**Routed in `FOR_66_FROM_60.md`, none applied:**
1. **The index letters** of `lf_closed` and `lf_open` — cosmetic, one line, `71`'s.
2. **`lf_witness`'s two senses of witness** — the flat leaf's is a membership statement where the
   other two are curvature values. Sound as it stands; offered as one clause if `71` wants the
   phrase to cover one sense.

**Carried by me, not fixed here:** `S11`'s `Ⓔ①` measures the attribution rule's imperfection over an
**empty set**. The fix is a positive control for that gate, which is its own measurement.

**Reported, not routed:** the `eq:gauge` clause is exact on `(0, ∞)` and excludes `r = 0` silently.

---

## ⌈ ⑧ CORRECTION, SAME REVISION, BEFORE IT MERGED — `N9` IS REACHED AND `⑤` HAS A FOURTH ENTRY

**⛔ `C4.no_regression` was wrong, and CI caught what my own arm did not.** `④` above reports the
patch as changing no verdict. **It changes two.**

**Two faults of mine, compounding.** ⓵ The arm checked only that the gating seat's own commits keep
their attribution; it **never asked whether the gates downstream of the predicate still hold**.
⓶ The before/after comparison ran on a **shallow clone**, where `SITES`, `WRITERS` and `blame`
resolve against a grafted history — locally the receipt failed **seven** gates, on the runner
**two**, and I quoted the local `24`/`24`, `7`/`7` figures as though they were CI's. ⌗ *The gate
COUNT matched, which is what made it look sound. The failing SET is environment-dependent and I did
not say which environment I had measured.*

**What the patch does.** `Ⓒ②` asserts `len(_odd_lines) >= 1` — **foreign claim-sites EXIST in the
path scope**. Narrowing from "ODD parity" to "explicitly `r#### (69)`" **empties that set**, so the
gate flips PASS → FAIL and `Ⓒ③` follows. Reproduced after deepening the clone to `3039` commits:
`_odd_lines` printed **`0`** entries, `Ⓒ②` and `Ⓒ③` red — the exact pair CI reported.

**The cause is a notion, not a mechanism.** `70`'s reading of the mechanism was right and is
verified at `④`. But both gate texts say *other seats'* — `Ⓐ③`: *"no **other seat's** work is inside
the assertion"*; `Ⓒ②`: *"the gating seat's **and other seats'** revisions"*. **Parity was only ever
a proxy for "not this line's,"** and `70` replaced it with a narrower notion than either gate means.

**The fix keeps `70`'s correction rather than reverting it:** `foreign(subject)` reads the writer's
**stamp** — `r#### (NN)`, `r####+NN.n`, `r####+ccNN.n` — and never the id's parity, and asks whether
the seat named is not this line's. **An UNKNOWN stamp decides NEITHER gate**, since `Ⓐ③` asserts
absence while `Ⓒ②` asserts presence, and on a shallow clone `blame` attributes everything past the
graft to a boundary commit carrying no stamp. The unidentified are **counted and printed** beside
both gates instead of absorbed into either.

**Measured, reproduce-then-pass:**

| | `Ⓒ②` | `Ⓒ③` | `Ⓐ③` | other verdicts moved |
|---|---|---|---|---|
| `70`'s patch as offered | **FAIL** | **FAIL** | PASS | — |
| the corrected predicate | **PASS** | **PASS** | PASS | **none** |

⇒ **`N9` is reached**, against what `⑥`'s table says: the patch fixed the named case and broke a gate
the parity rule happened to make pass. `70`'s claim stands, its mechanism stands, its predicate does
not.

⌗ **And `⑤` has a fourth entry, of the same family as its third:** *a before/after comparison that
did not name the environment it ran in.* The third printed a verdict from two empty files; this one
printed a verdict from the wrong tree. **Both agreed with me because neither was measuring what I
said it was** — and in both cases the only thing that could have caught it was a witness count
beside the verdict, which is what the corrected gate now prints.
