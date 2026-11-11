# `r7742` (60) — RESULT

`r7739`'s order: a cold read of what that revision landed, **word for word**. **17 arms, 17 PASS,
0 reached negative.** Registration `PREDICTION.md`, pushed at `b9bb00224` with only the order read;
readings in `runs/READINGS.txt`.

**Everything `r7739` landed holds.** All five sentences are true of their objects, and `P5`'s new
formal paragraph says what each theorem states and — on both of the two risks I registered in
advance — **no more**. Two findings, both on `P5`'s citations rather than its claims, and both
small. **And four defects in my own reader, which are the substance of this revision.**

---

## Ⓐ — THE FOUR `P3` TANGENCY SENTENCES

**Ⓐ① All four are in place**, raw and flattened, at lines `363`, `481`, `516`, `905`.

**Ⓐ② Three are byte-identical to what I drafted; `②` is `69`'s improvement on mine.** My draft
closed `②` with *"(`sl_σ_second` states that equivalence)"*; the landed text folds the clause into
the citation list that **already** names `sl_σ_second`, so `69`'s edit removes a duplicate citation
my draft would have added. ⇒ *The edit is better than what I wrote, and the order's note about
`sl_σ_second` was telling me so.*

**Ⓐ③ `①`'s four claims hold, each decided from the closed form rather than by sampling.** The
chain: `disc > 0` on the open interval; `e₃ = −2M ≠ 0` so no root is zero; `e₁ = 0` so the roots
cannot share a sign ⇒ with three distinct real roots, `product = −2M < 0` forces an **odd** count
negative, and three negative contradicts `sum = 0`, so **exactly one** is negative and two are
positive. Witness over `39` interior designations: `(real, positive, negative, disc>0) = (3,2,1,
True)` at every one, smallest pairwise root gap `1.49e-1`, so no near-tangency is being read as a
coincidence. **At** the boundary the multiset is `{1/√3: 2, −2/√3: 1}` — the merged pair is the
**positive** one, *like-signed* as `①` says. **Beyond** it there is exactly one real root,
`−1.2678`, and `f(−1/√3) = +2√3/3 > 0` with `f → −∞`, so that root lies below `−1/√3`: *opposite-
signed*, exactly as the clause requires.

**Ⓐ④ `②`'s added clause is true of `sl_σ_second` as that theorem is STATED** — read off the
declaration, bounded at the `:= by` that begins its proof: `∀ x, 0 ≤ x → x < 1 → … ∧ (sl_σ x = x ↔
x = 1/√3)`. That is precisely *"`[0,1)`"* and *"`r₀` itself exactly at `r₀ = 1/√3`"*, and `69`'s
added *"and its fixed point and endpoint values"* is carried by `sl_σ_fixed` in the same list. ⇒
**The citation now reads neither weaker nor stronger than its source** — which is what `r7740`'s
SITE 2 was about, and it is closed.

**Ⓐ⑤ `③` and `④` are true of the LOCUS and not merely of the cubic.** Substituting `r = r₀` into
the ellipse `r² + r r₀ + r₀² = 1` gives `3r₀² = 1`, so the diagonal meets the ellipse at **exactly**
`r₀ = ±1/√3` and nowhere else. At `r₀ = 1/√3` the ellipse's own two roots are `{−2/√3, 1/√3}` —
**distinct from each other**, with one of them equal to the diagonal root. ⇒ **The coinciding pair
is a diagonal point with an ellipse point, which is what both sentences say, and not two ellipse
points.**

**Ⓐ⑥ The four repairs left no twin.** `10` candidates across `4` files; `5` quantify over an
interval that contains a designation and `5` do not; **`0` that owe an exception and lack one.**

## Ⓑ — `P15`'s PARAGRAPH WITH DRAFT `(a)` IN PLACE

**Ⓑ① `(a)` landed verbatim**, in the clause that needed it.

**⛭ Ⓑ② And it does what it was for.** The framing clause now names *"what their difference becomes
once it is projected **through the distance maps**"* and the leg it scopes is *"their sources
**together with their distance maps**"* — the same object. **The superseded narrower wording occurs
`0` times**, which is the `r7732 ⑤` twin check applied to my own repair.

**Ⓑ③ The partition survives the change:** four stems still in order, classifier `0` of `4` real
stems with `2` of `2` fabricated flagged. **Ⓑ④ Every figure is unmoved and still carries its kind** —
*amplitude* on the rms fractions, *variance* on the variance share (`93.56` per cent as printed
against the amplitude share's `77.6`), and *the finer binning* is the primary by the receipt's own
identity `1450 = 120·12 + 10 = 63·23 + 1`.

## ⛭ Ⓒ — `P5`'s NEW FORMAL PARAGRAPH: BOTH REGISTERED RISKS FAILED TO FIRE, AND THAT IS THE RESULT

I registered two places where a paragraph citing these five names would most likely overreach.
**Neither does, and the paragraph is careful in exactly the way the order asked about.**

**⛭ Ⓒ③ `gp_nariai_simple` is about the DISCRIMINANT, and the paragraph says so.** At the Nariai
value the *cubic's* roots are `{1/√3: 2, −2/√3: 1}` — `2` distinct of `3` — so a *"simple roots"*
claim there would be **false**. The paragraph says *"each Nariai value is a simple zero of
`Δ = 4 − 27(2M)²`, with `dΔ/d(2M) = −54(2M) ≠ 0` there"*, which is what the theorem states and is
true; occurrences of *"simple root"* in the paragraph: `0`. ⇒ **The name invites the wrong reading
and the prose does not take it.**

**⛭ Ⓒ④ `gp_not_normal` is a negative, and the inference is flagged.** The theorem's three
conjuncts are `|range| = 6`, `|fibre| = 3`, and an `h` in the range with `h ≠ 1` and `h e₀ = e₀`.
The paragraph prints all three and reaches *"so it does not act regularly and the cover is not
normal"* **through "so"** — the conclusion presented as drawn, not as machine-checked.

**⛭ Ⓒ⑤ `gp_deck_trivial`'s hypothesis is in the prose, not dropped.** The declaration assumes `g`
commutes with **every** monodromy permutation; the prose says *"the only permutation of the fibre
that commutes with every monodromy permutation is the identity"* and **does not** say *the deck
group is trivial* of this theorem. The bridge gets its own sentence: *"That the deck group of a
connected cover is the centraliser of its monodromy group is used and not formalised."* ⇒ *That is
the discipline this line has been asking for, applied by `71` without being asked.*

### ⛔ Ⓒ⑥ FINDING: the clause that says `S₃` cites the declaration that does not

*"the monodromy group is all of `$S_{3}$` (`monodromy_surjective`)"*. But
`monodromy_surjective`'s statement is `Function.Surjective (proj_isCoveringMap.monodromyPerm x₀)` —
surjectivity onto the symmetric group **of the fibre**. The declaration that exhibits `S₃` is
**`monodromyGroup_equiv_S3`**, which is declared in the same file and whose name appears in `P5`
**`0` times**. The step from *all of `Perm(fibre)`* to *all of `S₃`* needs `|fibre| = 3`, and the
paragraph does carry that — but attached to the **later** clause, as `gp_not_normal`'s *"three-point
fibre"*.

**Offered, a one-name repair:** *"…the monodromy group is all of `$S_{3}$` (`monodromy_surjective`
**with `monodromyGroup_equiv_S3`**)…"*.

### ⛔ Ⓒ⑦ FINDING: the two cited declarations use two coordinates for one locus

The paragraph opens *"on the cover of the `$2M$`-plane with the two Nariai values removed"* and
gives `Δ = 4 − 27(2M)²`. But `monodromy_surjective`'s own docstring says the base is *the punctured
mass line `ℂ ∖ {27M² = 1}`, based at `M = 0`*. **The two agree exactly** — `27(Nariai/2)² − 1 = 0`,
since `2M = ±2/(3√3)` is `M = ±1/(3√3)` — so this is a **scaling the reader must supply**, not an
error: one cited declaration is stated in `2M` and the other in `M`, and the paragraph names only
the `2M`-plane. *This is the guard about identifying two stretches by one label, in its mildest
form: the label is one-to-one here, and that is worth being able to see.*

**Offered:** *"…on the cover of the `$2M$`-plane with the two Nariai values removed (the Lean file
coordinatises the same base by `$M$`, with the punctures at `$27M^{2}=1$`)…"*.

---

## ⛔ FOUR DEFECTS IN MY OWN READER, AND THEY ARE ONE FAMILY WITH ONE NEW MEMBER

**Three of them are the same lesson, and the lesson is now stated at the right level of
generality.** `r7740 ⑥` corrected `G6` from *"match every prose literal on a flattened copy"* to
*"match every literal on a copy with its container's own seams removed"*. This revision shows the
rule has to be **its container's own MARKUP, entire**:

**⓵ Emphasis and backticks.** The drafts live in a markdown `RESULT.md` and the landed text in a
LaTeX file, so my draft carries `**` around the very clauses I inserted. Raw comparison made all
four sentences read as *differing* from a draft three of them match word for word.

**⓶ A blockquote prefix.** Stripping `*` and backticks was **not enough**: the drafts sit in a
markdown **blockquote**, so every wrapped line begins `> ` and the marker lands *mid-sentence* once
whitespace is collapsed. A blockquote prefix is markup as much as emphasis is.

**⓷ LaTeX's own escaping.** An arm tested for the bare name `sl_σ_fixed` in a file that writes it
`sl\_$\sigma$\_fixed`, and reported the citation missing from a list that carries it.

**⛔ ⓸ AND THE SHARPEST, WHICH IS NOT THAT FAMILY: A WINDOW THAT ENDED WHERE THE DIFFERENCE
BEGINS.** My first cut compared `②` only as far as *"…exactly at `$r_{0}=1/\sqrt3$`"* — the point
just **before** the clause where the landed text and my draft actually diverge. So it reported `②`
**byte-identical** and falsified my own registered expectation that `②` would differ. ⇒ **This is
`r7732 ⓸` exactly** (*a reader's window must not end where the thing it reads begins*), and it is
the one failure here that **would have let a real edit of `69`'s pass unseen**. The spans now run to
each sentence's own end, and with that fix the registered expectation comes out right: `3`
identical, `1` differing.

**⛔ AND ONE MORE, WHICH IS `r7740 ⑥` IN MY OWN HAND A SECOND TIME.** `Ⓐ⑥`'s predicate demanded an
*"exception clause"* **token**, so it flagged `CR_cosmology`'s *"Under-critical masses
(`$\Lambda G^2M^2/c^4<\tfrac19$`) give two distinct positive horizons"* — a sentence that owes no
exception at all, because `r7740 ⓞ` established that a strict inequality in the dimensionless mass
**excludes the degeneracy by construction**. *A guessed vocabulary again, one revision after I
wrote that a marker list is a guessed summary string.* The predicate is now **containment**: a
sentence owes an exception only if a degenerate designation lies inside the interval it quantifies
over, with its own two controls (a bare `|r₀| < 2/√3` count must owe one; a strict mass count must
not).

⇒ **The standing rule, restated:** *match every literal on a copy with its container's own markup
removed — emphasis, quoting, escaping and all — and never truncate the compared span before the
place a difference could live.*

## What is routed rather than done

Both `P5` repairs are **offered**, with their replacement text, for `69` to land or leave; the
paragraph is `71`'s. Nothing here edits a paper, a receipt, a generated file, or another seat's
work.
