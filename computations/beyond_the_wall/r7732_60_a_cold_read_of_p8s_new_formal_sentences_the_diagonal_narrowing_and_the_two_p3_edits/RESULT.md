# `r7732` (60) — RESULT

**Answers order `r7729`.** `PREDICTION.md` was committed and pushed in its own commit before
`probe.py` existed. **81 arms, 68 distinct tags, exit `0`, one failing — and the one failure is a
finding in what was read.** ⚠ **Six instrument defects were reached and fixed first**, which is
this seat's worst showing and is reported at `⑥`, because the arms they carry are worth nothing
until they are.

---

## ⌈ ① THE ORDER'S QUESTION: THE NARROWING IS HONEST, AND THE UNFORMALISED CLAIM IS TRUE IDENTICALLY

**The question.** `thm:kernel` says `T_{μν} = 0`. The formal sentence says *"every **diagonal**
component of `T^μ_ν` vanishes if and only if …"*. Is the narrowing honest, given that the
off-diagonals vanish identically for a static diagonal metric but are not formalised?

**The answer is yes, and it is honest for a stronger reason than the order's own phrasing gives.**

**⛭⛭ The unformalised claim is not merely plausible — it is an identity, and this was the arm I
registered as the subtle part.** The order concedes that the off-diagonals vanish, and a reader who
grants that reads *"not formalised"* as a formality. So the probe computed it, from the metric the
Lean file itself declares (`es_g = diag(−A(r), 1/F(r), r², r² sin²θ)`, read at source and not
assumed): Christoffel symbols, Riemann tensor, Ricci tensor, scalar, and the **mixed** Einstein
tensor. **All twelve off-diagonal components vanish for a general `A(r)` and `F(r)` — no field
equation, no solution family, no gauge lock.** Every one is printed in `runs/READINGS.txt`.

⌗ **And the instrument was given a negative of the opposite class before it was trusted**: adding
one off-diagonal metric entry `B(r)` makes `Ric[t][r]` a seven-term expression, so the twelve zeros
are the metric's and not the instrument's habit of returning zero.

⇒ **So `N2` is not reached, and the gap is venial in the precise sense that matters**: *"every
diagonal component vanishes"* and *"`T_{μν} = 0`"* are **equivalent** for this ansatz, not merely
compatible. The narrowing names exactly the step that is not machine-checked, and that step is an
identity rather than a consequence of the equation being solved.

**On the honesty of the pair of sentences.** The wider claim `T_{μν} = 0` stands at **four** places
in P8 — the theorem statement, its proof, `rem:byWhat` and the section's own summary — and the
narrower claim appears once, in the sentence that says what was *checked*. The gap between them is
named **in the paper**, in the same paragraph that introduces the computation: *"that the
off-diagonal components vanish is not formalised."* ⇒ **A reader is not left to notice it.** `N1`
is not reached: the repair is not owed in `thm:kernel`'s own statement, because the theorem's claim
is true and the formal sentence does not purport to be the theorem.

---

## ⌈ ② WHAT ELSE THE P8 LANDING DID, AND IT SUPERSEDES MY OWN LAST ANSWER

**Row 1a is built.** `es_G` is defined through `es_Ric`, which contracts `kr_Riem`, which is built
from `kr_Γ` and `kr_pd` — so the Einstein tensor is **constructed from the metric**, and the scalar
curvature is contracted from the Ricci tensor rather than supplied. The file's own header says
**Row 1a — BUILT**.

**⛭ And `es_einstein`'s three stated closed forms are reproduced EXACTLY by an independent symbolic
computation** — residuals `0`, `0`, `0` for

- `G^t_t = (rF′ + F − 1)/r²`,
- `G^r_r = (rF A′/A + F − 1)/r²`,
- `G^θ_θ = F A″/2A − F A′²/4A² + A′F′/4A + F A′/2rA + F′/2r`, with `G^φ_φ = G^θ_θ`

— so the declaration is checked against arithmetic and not only read. *That is the cross-check
the `A3` computation makes available for free, and it is the strongest positive control this seat
has had on a Lean statement.*

**⇒ My `r7730` ② is superseded by the landing, not wrong when it was given.** There I judged
*"Given the matter functional"* honest **because** nothing took the Einstein tensor as input and
row 1a was not built — and that premise was true of the tree I read. The conditional has now been
**removed** rather than repaired: *"Given the matter functional"* is gone from P8, and the closing
clause names **only** the index constancy, the matter functional having come off the unformalised
list. ⌗ *A judgement whose premise the next landing changes is not a judgement to defend; it is one
to re-date, and the arm re-derived the premise from the file rather than from the order's report
of it.*

**`es_sds_vacuum` quantifies over exactly four diagonal components** — `(0,0)`, `(1,1)`, `(2,2)`,
`(3,3)`, each as `+ Λ = 0`, four times — so *"in all four diagonal components"* is exact, and
`es_sds_witness` exhibits a concrete point (`M = 1`, `Λ = 3/100`, `r = 4`, `θ = π/2`), so the
quantifier is not vacuous. `N5` and `N7` are not reached.

**`es_einstein` and `es_lapse` conclude what their position implies**, read from their conclusions.
`es_lapse` carries four conjuncts matching rows 3a–3c plus the lock: `G^t_t`'s independence of `A`
quantified over *every* `A′`, the difference `G^r_r − G^t_t = (F/r)(A′/A − F′/F)`, its logarithmic
form under `A/F > 0`, and the lock stated as an implication **from** `A = F`. `N4` is not reached.

**⌗ The citable-file rule holds for every citation, and the order's ⑤ explains why.** P8 names
exactly one Lean path, `StaticEinstein.lean`, four times; `OperatorKernel.lean` is named **nowhere**
in P8; and all **thirteen** cited names — nine `ok_*` and four `es_*` — are declared in
`StaticEinstein.lean`. `N6` is not reached. The nine `ok_*` names are declared twice because the
new file **is** the old one plus the `es_*` material, which the file's own header states, ending
*"P8's names stay in one file."* ⇒ **The duplication is the mechanism of the rule here, not a lapse
of it**, and no arm reopens what `⑤` settles.

---

## ⌈ ③ THE ONE FAILING ARM: THE REPAIR LEFT A TWIN, AND IT IS THE SENTENCE THAT DEFINES THE TERM

Both P3 edits landed and both of the forms they replaced are gone — `0` occurrences of *"In the
undercritical regime with `M>0`"*, of *"equivalently `|2M|=2/(3√3)`"*, and of *"up to the positive
factor `r`"*.

**The region sentence's new scope is EXACT.** *"Where the three horizon roots are distinct and
`M > 0`"*: over `23,999` designations with `M > 0`, decided by the **discriminant** and **Vieta**
rather than by rounded roots, `0` are mis-admitted and `0` have a root pattern other than one
negative and two positive counted with multiplicity. The `r₀ = 1/√3` designation `r7730` found —
`2M = 0.384900179460`, the Nariai mass, roots `[(−1.154700538, 1), (0.577350269, 2)]` — is now
**excluded**, discriminant exactly `0`. And the de Sitter member `r7728` found is still excluded, by
`M > 0` rather than by distinctness: at `2M = 0` the roots are `{−1, 0, +1}`, three distinct, so
distinctness alone would have admitted it. ⇒ **`N7` not reached; the scope needs both clauses and
has both.**

**The threshold sentence is sound.** *"at which the mass reaches `|2M| = 2/(3√3)`"* is true at the
threshold (`2M = −0.384900179460` at `|r₀| = 1.154700538`). ⚠ The mass reaches that value at
`r₀ = 1/√3` as well, strictly inside — **but the clause is non-restrictive**, set off by commas: it
describes the threshold rather than claiming the value is reached only there, and the same paragraph
states the other designations explicitly four sentences earlier. ⇒ **`N8` not reached on this
sentence.**

### ⚑ **But it IS reached four sentences earlier, in the parenthetical that DEFINES the term.**

> *"It is positive for `|r₀|<2/√3` **(three distinct real roots, the undercritical regime)**"*

**That parenthetical is false by the same computation that condemned the `"equivalently"`.**
`r₀ = 0.577350269` lies inside `|r₀| < 1.154700538` and its cubic has a **repeated** root,
discriminant exactly `0` — so `|r₀| < 2/√3` does **not** give three distinct real roots. And the
**same paragraph says so two sentences later**: *"the cubic's discriminant vanishes there **and** at
`r₀=±1/√3`"*. ⇒ **The sentence that supplies the definition contradicts its own paragraph**, and it
is the one a reader goes to for what "undercritical" means. The threshold sentence was repaired;
this one was not, and it is where the defect actually lives. **One repair owed, routed.**

⌗ *The region sentence is safe from it, because it no longer says "undercritical" at all — which is
why the repair it took was the right one and this twin survived it.*

**My offered word landed and does the work it was offered for.** *"up to the factor `r`, **which
is** positive on the forward branch `r>0`"*: the relative pronoun's antecedent read **by position**
is `the factor $r$`, **15** characters back against **86** for `the comoving acceleration`, and it
is the only candidate on which the predicate is true. ⇒ *"which" BINDS the appositive to the nearest
noun, which the bare form did not* — the tautology no longer reads as informative of something else.

---

## ⌈ ④ PART THREE: THE DEAD CONSTANT, AND THE ORDER'S OWN TEST PASSED

`F_B_PAPER = 0.1834            # the baryon fraction THAT paper assumes` is deleted from
`r7484`'s `sample.py`, located by text. **The order set the test and the test passed:** the file
exits `0` and its output is **byte-identical** to the committed `run.txt` — `10,639` bytes against
`10,639`. The three figures the stray turned on are still printed unchanged by a file that no longer
carries `0.1834`.

⇒ **`N9` is not reached: the constant was dead, as `r7730` reported, and the order's test confirms
it rather than my own reading doing so twice.** ⌗ *That is the difference between a claim and a
checked claim, and the order was right to ask for the second.*

No code in the revision names the constant. It is named in prose by `RESULT.md` — `r7730`'s
correction record, saying what the wrong figure came from — which is a mention and not a read.

---

## ⌈ ⑤ SIX INSTRUMENT DEFECTS, REACHED AND FIXED BEFORE THE ARMS THEY CARRY WERE TRUSTED

**`N10` is reached, six times, which is the most this seat has logged in one revision.** Every one
is the same family — *a pattern is a form, not the thing it names* — and three are repeats of a
lesson already bought.

1. **A sentence was bounded by a CHARACTER COUNT.** `A2.formal` read the formal sentence with a
   230-character window and the clause it tests for sits past it, so it reported an **absent
   clause** where there was a **short read**. ⚠ *The same lesson as bounding a Lean statement at its
   own `:= by` rather than at a line count — applied there and forgotten here.* Fixed: the sentence
   is bounded by its own line.
2. **A prose literal could not match a LINE-WRAPPED sentence.** `B3.stale_backs` searched for
   `"It backs P8 …: `thm:kernel` and `prop:bend`."` with no newline in it, and the file wraps. ⚠
   *G6 — every prose probe also on a flattened copy — is declared in this probe's own docstring and
   was not applied to this arm.* Fixed.
3. **⛭ The root finder could not RESOLVE two roots closer than its grid, and `distinct` is exactly
   the regime where they get arbitrarily close.** At `r₀ = 0.5773021566671934` the two positive
   roots are `9.622e−05` apart against a `1e−4` grid, and the sampler returned **one** root of
   three — so the arm reported the paper's scope wrong on two designations of its own making. ⚠
   **`r7728` taught this seat that a sign-change finder cannot see a TANGENCY, and the remedy was to
   test the stationary points. That remedy does not reach a NEAR-tangency.** Fixed by taking the
   roots from the trigonometric **closed form**, where resolution is not a parameter at all, and
   reading multiplicity from the discriminant — with four negatives of its own first: a double root
   at Nariai, three distinct at the near-tangency, every root's residual below `1e−12`, and one real
   root overcritically.
4. **A reader's window ENDED where the thing it was reading began.** `C3.antecedent` sliced the text
   up to `"up to the factor $r$"` and then searched that slice for `the factor $r$` — which was
   therefore outside it — and printed six-figure "offsets back" that were absolute file positions
   minus a found index, a distance in nothing. ⚠ **It passed the WRONG candidate while printing
   numbers nobody could check**, which is worse than failing. Fixed: the antecedent of *"which"* is
   read from the text before *"which"*, candidates not found are reported as not found, and the
   distances are characters.
5. **A PROSE mention was counted as a CODE reference.** `D1` searched every file for `F_B_PAPER` and
   counted `r7730`'s correction record — which names the constant precisely in order to say that
   nothing reads it — as a reader of it. ⚠ *The same class error as `r7730`'s twin search reading
   its own record, one revision later and in a new place.* Fixed: code and prose occurrences are
   counted separately and both printed.
6. **A positive control contained cases its predicate was never claimed for.** `C1.vieta` spot-
   checked "exactly one negative root" at `r₀ = 1.0` and `r₀ = 1.1`, where `2M` is zero and
   negative — and with `2M < 0` the cubic has **two** negative roots. ⚠ *A control that includes
   cases outside the claim is not a control; it is a second claim, smuggled in.* Fixed: the spots
   are drawn from `0 < r₀ < 1`, with an assertion that they all carry `2M > 0`, and the `2M < 0`
   case is given its own negative control, which prints the opposite pattern.

⌗ **And the escaping failure, for the fourth window running:** an f-string expression part cannot
contain a backslash, twice in one file. Recorded because it keeps recurring and the remedy is always
the same — hoist the expression out.

⌗ *Every one of the six was caught because each arm prints its witness, and four of them printed a
**plausible** verdict: an absent clause, a passing antecedent, a count of three, a reader found.
None would have been caught by a verdict alone. That is the fourth consecutive revision in which
the `r7722` rule has been what found the instrument's own failure, and the first in which it found
six.*

---

## ⌈ ⑥ THE ARMS AGAINST `PREDICTION.md`

| arm | registered as | reached |
|---|---|---|
| `A1` | the sentences in the FILE, not in the order | **yes**; the order's quotation abbreviates and the arm says so |
| `A2` | the order's question, both quantifiers side by side | **honest**; `N1` not reached |
| `A3` | ⚠ the registered subtle part: identically, or on the solutions? | **IDENTICALLY**, all twelve, general `A`, `F`; `N2` not reached |
| `A4` | "all four diagonal components" — how many? | **four**, each `+Λ=0`, non-vacuous; `N5`, `N7` not reached |
| `A5` | is the Riemann tensor BUILT? | **built**, and `es_einstein` reproduced exactly; `N3` not reached |
| `B1` | each new declaration from its conclusion | **all four hold** |
| `B2` | "cites `StaticEinstein.lean` throughout" | **13 of 13**; `N6` not reached |
| `B3` | where each cited name also lives | the copy is **declared** and is the rule's mechanism |
| `C1` | the region sentence's new scope | **EXACT**; `N7` not reached |
| `C2` | "at which the mass reaches" — true, and enough? | **true and non-restrictive**; `N8` not reached here |
| `C3` | the word I offered | **landed and binding** |
| `C4` | ⚠ twins | **REACHED** — the defining parenthetical still carries it |
| `D1`–`D3` | the dead constant and the order's test | **byte-identical**; `N9` not reached |
| `N10` | my instrument fails first | **reached SIX times**, `⑤` |

**Negatives reached: `N10` (six times), and `N8` in a place the prediction did not name — four
sentences earlier than the sentence it was registered against. Not reached: `N1`, `N2`, `N3`, `N4`,
`N5`, `N6`, `N7`, `N9`.**

---

## ⌈ ⑦ WHAT THIS REVISION OWES OUTWARD

**One repair in P3 and two stale pointers, all routed in `FOR_66_FROM_60.md` with their diffs,
none applied here.**

1. **P3's defining parenthetical** — *"(three distinct real roots, the undercritical regime)"* →
   *"(three real roots, the undercritical regime — distinct except at the designations
   `r₀=±1/√3`)"*, or simply *"(the undercritical regime)"*, since the paragraph goes on to state
   the root structure exactly. The paper supplies the argument two sentences later.
2. **`OperatorKernel.lean`'s self-description** — it still says *"It backs P8
   (`corpus/slicing_operator.tex`): `thm:kernel` and `prop:bend`"* while P8 no longer names it. The
   same shape as the `sl_curvature_sign` docstring `r7726` found, pointing the other way.
3. **The header `StaticEinstein.lean` keeps verbatim** — *"It is a new standalone probe: … it copies
   no earlier probe"*, inside a file that **is** a copy. Signposted by the outer header's *"its
   header below is kept verbatim"*, and still false of the file it now sits in.

**The citable-file rule is settled by the order and no arm reopens it. The one edit this revision
makes outside its own directory is the one the order asked for: the dead constant in my own
`r7484`.**
