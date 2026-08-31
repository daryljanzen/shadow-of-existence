---
name: number-theory-ledger
kind: FIELD-BAKE
current: r3708
job: The number-theory field-bake ledger — what bit, what bounced, and where the boundary is.
sources: [chat]
---

> ⛭ **`T1`'s RECEIPT — named here at r3660, because it was named nowhere.** *`receipts/P05_groupoid/T1_the_galois_inference_needs_irreducibility_and_it_holds.py`* — *P05's `rem:galois` infers $S_3$ from the discriminant not being a square, which is invalid without irreducibility; the conclusion holds because the horizon cubic **is** irreducible over $\\mathbb{C}(M)$, and the control $r^3-r^2+r-1$ (discriminant $-16$, not a square, Galois group $\\mathbb{Z}_2$) shows the inference genuinely fails without it.* ⌗ *It ran, it was registered, and a paper cited it; **the ledger whose probe it settles did not name it**, so the computation had no argument attached. `check_citation_chain` now fails on that.*

# THE NUMBER THEORY LEDGER — one bite, and it is a missing hypothesis three earlier bakes built on

> **▣ RANKED ×31, FOURTH OF SIX, AND THE RANK WAS BUILT ALMOST ENTIRELY ON HOMONYMS.** *After
> seventeen reads this field has **one** finding — but it is a real one, and it sits underneath
> results that **three other bakes have already used**.*

---

## ⛭ R0 — THE BASELINE

### ⛔ THE FIELD'S OWN VOCABULARY IS ABSENT, AND ITS APPARENT FOOTPRINT IS SUBSTRING NOISE

| term | raw | word-bounded | what it actually is |
|---|---|---|---|
| **`congruence`** | **×155** | ×155 | ⛔ ***EVERY ONE IS A GEODESIC CONGRUENCE*** — `P07` ×77, `P08` ×17, `P05` ×15, `P15` ×14. *A family of curves, not $a\equiv b \bmod n$.* **The largest homonym found in any of the four fields so far** |
| `Galois` | ×27 | **×26** | ***genuine*** — `P05` ×23, the horizon cubic's Galois group |
| `zeta` | ×20 | ×17 | ⛔ **split**: `P01` ×8 are the **Killing vector $\zeta=\partial_t$** — a *symbol name*; `P15`/`P16` ×6 are **$\zeta(3)$**, the Riemann zeta at 3, in the standard photon number density $\pi^4/30\zeta_3$ |
| `modular` | ×5 | **×0** | *matched inside **unimodular** / **unimodularity*** — the unimodular group, Lie theory |
| `prime` | ×1 | **×0** | *matched inside the macro **`\fprime`***, which is $f'$ |
| `integer` · `rational` · `arithmetic` | ×14 · ×8 · ×9 | ×11 · ×3 · ×9 | *counts, ratios, and "the same number by **arithmetic** and not by structure" — ordinary usage* |
| `Diophantine` · `transcendental` · `irrational` · `number field` · `algebraic number` · `continued fraction` | | **all ×0** | |

⇒ ⚠ ***THE ORDER PREDICTED "screen zeta; likely a regularisation or a coordinate". IT IS NEITHER.***
*It is a **vector-field name** in `P01` and the **genuine Riemann zeta** in `P15`/`P16` — so the
prediction was right that the count was not this field's and wrong about what it was, which is a
better outcome for the screen than being right would have been: **the screen made the reading happen.***

---

## ⌗ THE PROBE REGISTER

| # | probe | verdict |
|---|---|---|
| **`T1`** | *`P05` infers the Galois group is $S_3$ from the discriminant not being a square. **Is that inference valid?*** | ⛔⛭⛭ **BITE — THE CONCLUSION IS TRUE AND THE INFERENCE AS WRITTEN IS NOT.** *The criterion is for an **irreducible** cubic: non-square $\Delta\Rightarrow S_3$, square $\Delta\Rightarrow A_3$. **A reducible cubic can have a non-square discriminant and a group of order two** — $r^3-r^2+r-1$ has $\Delta=-16$ and Galois group $\mathbb{Z}_2$, exhibited in the receipt.* ⇒ *The hypothesis holds here and holds cheaply — the cubic is degree one in $2M$, so Gauss's lemma forbids a factorisation — **but `P05` never says so, and three later bakes built on the conclusion without checking it.*** **LANDED** in `P05` `rem:galois` |
| **`T2`** | *`congruence` ×155 — the corpus's largest single field-word count* | ⛭ **SCORED — ×0 for this field.** *Every occurrence is a geodesic or null congruence.* ⌗ ***This is the `Lax` failure at four times the scale***, and it is the third such in four fields: a bake opened on the raw count would have spent its whole run inside a differential-geometry word |
| **`T3`** | *is $\zeta$ the Riemann zeta anywhere?* | ⛭ **SCORED — YES, twice, and used correctly.** *`P15` and `P16` carry $\zeta_3$ in $\pi^4/30\zeta_3$, the standard photon-to-baryon number-density constant. **A number-theoretic constant doing ordinary cosmological work, which is not a claim this field can improve*** |
| **`T4`** | *does the corpus's integrality — three roots, $\mathbb{Z}_3$ deck, three generations, integer harmonic index — have arithmetic content?* | ⛭ **SCORED — NO. It is Lie-theoretic and Galois-theoretic throughout, and both are already baked.** *The threeness comes from $A_2$'s root system and the cubic's Galois group, not from any arithmetic property of a number. **`p0`'s $\mathbb{Z}_3$ is a deck group, not a residue class*** |
| **`T5`** | *is the Galois material this field's to claim?* | ⛭ **SCORED — NO, and this is prior art.** *`ALGEBRAIC_GEOMETRY`, `COMBINATORICS` and `COMPLEX_ANALYSIS` all carry it: the branched cover, $S_3=\mathrm{Sym}$(3-set), the degree-six Galois closure.* ⇒ ***And that is exactly what makes `T1` worth having: all three USE the $S_3$ result and none of them audits the theorem's hypotheses*** |

---

## ⛭ THE REACH REGISTER — **17 of 17**

| paper | verdict | what was read |
|---|---|---|
| **`P05`** | ⛭ **WORKED — and it owed the one clause this field found** | *`rem:galois`, `rem:perroot` and the deck/monodromy propositions read in full.* `Galois` ×23. **The corpus's only genuine number-theoretic argument, and its one unstated hypothesis** |
| **`P01`** | ⛭ **CHECKED-NEGATIVE — and it owns the `zeta` homonym outright** | *All eight read: $\zeta=\partial_t$, $|\zeta|^2=g_{tt}$, the Killing-horizon condition.* **A Greek letter, not a function** |
| **`P15`** · **`P16`** | ⛭ **CHECKED-NEGATIVE, both, and both carry the genuine $\zeta_3$** | *The photon-density formula read at both sites.* `congruence` ×14 in `P15` is geodesic; `arithmetic` is ordinary |
| **`P07`** | ⛭ **CHECKED-NEGATIVE — and it carries HALF the corpus's `congruence`** | ***×77 of ×155***, every one a congruence of curves. `Galois` ×1 restates `P05` |
| **`P08`** | ⛭ **CHECKED-NEGATIVE** | `congruence` ×17, all geodesic — the marginal congruence and the $E=1$ family |
| **`P03`** | ⛭ **CHECKED-NEGATIVE** | `integer` ×2, `rational` ×1, `congruence` ×4 — labels and curve families. Its `prime` is `\fprime` |
| **`P14`** | ⛭ **CHECKED-NEGATIVE — and its `unimodular` is what the `modular` count was** | *`unimodularity` and the unimodular group: **Lie theory wearing a number-theoretic prefix***. `arithmetic` ×2 is *"the same number by arithmetic and not by structure"*, ordinary English |
| **`P02`** · **`P06`** · **`P09`** · **`P10`** · **`P11`** · **`P12`** · **`P13`** · **`p0`** | ⛭ **CHECKED-NEGATIVE, all eight** | *Screened on `zeta`, `prime`, `integer`, `rational`, `modular`, `Galois`, `congruence`, `Diophantine`, `arithmetic`.* **Nothing of this field in any of them**; `p0`'s and `P07`'s single `Galois` are restatements |
| **`P04`** | ⛭ **CHECKED-NEGATIVE — fourth field running with nothing** | *`P04` has now returned empty on integrable systems, index theory, information theory and number theory. **That is a fact about `P04` and it is worth stating once rather than four times***: it is the measurement paper, and none of these fields reaches it |

---

## ⛭⛭⛭ THE THREE REGISTERS

### ⌗ WHAT BIT — one, and it is underneath three other bakes

| # | what the field found | where it landed |
|---|---|---|
| **`T1`** | ***"$\Delta$ not a square, so $S_3$" is a valid step only for an IRREDUCIBLE cubic*** — and the reducible counterexample $r^3-r^2+r-1$ has $\Delta=-16$, not a square, with Galois group $\mathbb{Z}_2$. The hypothesis holds for the horizon cubic and holds cheaply, and saying so turns a true statement into a valid one | `P05` `rem:galois`, `\ldg{number_theory}` |

### ⌗ WHAT BOUNCED — four, with their blind spots

| # | why it bounced | **what the test that killed it was blind to** |
|---|---|---|
| `T2` | `congruence` ×155 is geodesic throughout | *The word-boundary screen passes it at ×155 — **it is a real word used in full**, so nothing mechanical catches it. Only knowing both fields does.* |
| `T3` | $\zeta_3$ is used correctly | *An absence screen looks for `Riemann zeta` and finds ×0. **The constant is there under a symbol**, and the screen has no way to see that.* |
| `T4` | the integrality is Lie-theoretic and Galois-theoretic | *Counting `integer` ×11 cannot distinguish "this corpus has arithmetic content" from "**this corpus counts things**".* |
| `T5` | the Galois material is three bakes' prior art | *Reading `Galois` ×26 as an opening would have re-derived three ledgers. **The blind spot is not grepping the other ledgers before claiming a field's headline object.*** |

### ⌗ THE BOUNDARY

***THE CORPUS USES GALOIS THEORY AND NO OTHER NUMBER THEORY, and Galois theory is the part of the
field that is really group theory.*** *No prime, no congruence in the arithmetic sense, no
Diophantine equation, no algebraic number field, no modular form, no transcendence claim.*

⇒ ***AND THE FIELD'S ONE FINDING IS NOT A GAP IN CONTENT BUT A GAP IN A PROOF STEP*** — which is
what a field bake is for when the corpus is already using the field's results correctly.

⛔ ***WHAT THIS FIELD CANNOT REACH.*** *Whether the horizon cubic's Galois group drops at special
**rational** values of $2M$ is a genuine Diophantine question — $4-27u^2=v^2$ has infinitely many
rational solutions — **and it bears on nothing the corpus claims**, whose Nariai points are
irrational and whose masses are arbitrary reals. *Noted so it is not mistaken for an opening.*

---

## ⌗ THE LEAD REGISTER · THE LANDING TABLE

| register | verdict | destination | state |
|---|---|---|---|
| `T1` | BITE — a missing hypothesis | `P05` `rem:galois` | **LANDED** |
| `T2` | BOUNCED — geodesic congruences | — | **CHECKED-NEGATIVE** |
| `T3` | BOUNCED — $\zeta_3$ used correctly | — | **CHECKED-NEGATIVE** |
| `T4` | BOUNCED — Lie-theoretic, not arithmetic | — | **CHECKED-NEGATIVE** |
| `T5` | BOUNCED — three bakes' prior art | — | **CHECKED-NEGATIVE** |
| rational-$2M$ Galois drop | — | — | **HELD, bears on nothing claimed** |

⌗ ***DEPTH BESIDE COVERAGE.*** **Coverage: 17 of 17 read, by name.**
**Depth: 1 bite, 4 bounces, 1 held — SIXTEEN of the seventeen papers owed nothing.**
---

## ⛭⛭⛭ THE ESTIMATE FROM CONTENTS — **the step this bake SKIPPED, run at r3622**

> ⛔ ***`OVERNIGHT_FIELD_BAKE_WORK_ORDER.md` STEP 2 requires all seventeen ABSTRACTS read and rated
> HIGH/MEDIUM/LOW from what each paper is ABOUT, written into the ledger BEFORE any paper is worked.***
> *59 skipped it; I skipped it after them. **Skipping it is the whole failure: a field's term list is a
> list of what I already know the field to contain, so grepping it returns only that.** It cannot return
> the thing the field would see that the corpus has no word for.*
> ⌗ *Written here **after** the term-side pass rather than before it, which is the honest order to record
> and the wrong order to have worked in. **Where the estimate and the term pass disagree, the disagreement
> is kept in the table rather than resolved silently.***

| paper | estimate | reason, from subject matter — **not from counts** |
|---|---|---|
| **`P05`** | **HIGH** | *the horizon cubic's Galois group, the discriminant, and a degree-six closure* |
| **`P03`** | HIGH | *a cubic, its discriminant, its roots and their exchange* |
| **`P14`** | MEDIUM | *$\mathbb{Z}_3$, $\mathbb{Z}_6$, $D_6$ and a subgroup index — group arithmetic, if not number theory* |
| **`P02`** | MEDIUM | *one curve with two critical points; the cycloid is transcendental and its rationality is never asked* |
| **`P16`** | MEDIUM | *abundances, ratios and $\eta$ — a dimensionless number the paper cannot derive* |
| **`P15`** | MEDIUM | *$\zeta_3$ enters the photon density; peak spacings are integers* |
| **`p0`** | MEDIUM | *a single dimensionless ledger and the $10^{122}$* |
| **`P12`** | LOW | *an algebroid* |
| **`P09`** | LOW | *a range theorem* |
| **`P13`** | LOW | *a gauge boundary* |
| **`P01`** | LOW | *causal structure* |
| **`P04`** | LOW | *a path integral* |
| **`P06`** | LOW | *epistemology* |
| **`P07`** | LOW | *synthesis* |
| **`P08`** | LOW | *an operator* |
| **`P10`** | LOW | *constraints* |
| **`P11`** | LOW | *dynamics* |

⌗ **2 rated HIGH from contents.** *Scored against the term-side pass below.*

### ⛭ SCORING THE ESTIMATE AGAINST THE TERM-SIDE PASS

| | estimate | term-side verdict | outcome |
|---|---|---|---|
| `P05` | **HIGH** | WORKED — `T1` landed | agreed, and it was the field's one bite |
| **`P03`** | **HIGH** | ⛔ **CHECKED-NEGATIVE** | ⚠ ***DISAGREES*** — *it carries the cubic, its discriminant and its roots* |
| the other fifteen | MEDIUM / LOW | CHECKED-NEGATIVE | agreed |

⇒ *`P03`'s disagreement is real but it is **the same cubic `P05` carries**, and `T1`'s fence — that the $S_3$
inference needs irreducibility — is stated where the inference is made. **Landing it twice would be landing it
once**.* ⌗ *Recorded rather than acted on, which is what the estimate table is for.*

---
---

# ⛭⛭⛭ THE v2 PASS — r3706, AND IT OPENS ON THE ROW THE v1 PASS SCORED EIGHT PAPERS IN

> ⛔ ***`SIX_FIELDS_WORK_ORDER_v2.md` §6: "where your reach table scored nine papers in one row on a
> screen, that row is where a v2 pass starts."*** *This ledger's reach register has such a row —
> **`P02` · `P06` · `P09` · `P10` · `P11` · `P12` · `P13` · `p0`, eight papers, one verdict, one
> sentence**, and the sentence is a list of the terms that were screened. §0 says exactly what that
> is: **a term list is a list of what you already know the field to contain.***
>
> ⛔⛭ ***AND THIS FIELD PREDICTS EMPTINESS SIXTEEN TIMES OUT OF SEVENTEEN — THE LARGEST EMPTINESS
> PREDICTION IN THE CORPUS.*** *§2 is the rule that governs this whole pass: **a prediction of
> emptiness gets MORE scrutiny, not less.** The one such prediction in the integrable-systems run
> was the one REFUTED prediction of seventeen. Here there are sixteen.
>
> ⌗ *Nothing below is struck. The v1 verdicts stand as the record of what a term screen returns;
> where the v2 pass finds more, the row is **updated** and the disagreement is kept.*

## ⌗ PASS A — THE LOCATOR. **Written from the seventeen abstracts and section lists, before any paper
was opened.** *No ranking: each row names the `\label`ed sections where this field's content would
live and states what would be there, in a form that can be scored **wrong**.*

| # | paper | sections named | ⌗ **the prediction — falsifiable** |
|---|---|---|---|
| 1 | **`p0`** | `sec:imaginary` · `sec:ledger` · `sec:power` | ⛭ ***"Reached through the imaginary, real everywhere it lands" is the geometric face of CASUS IRREDUCIBILIS***: an irreducible cubic with three real roots is **not** solvable in real radicals, so its real roots are reachable only through $\mathbb{C}$. **The corpus's horizon cubic in the under-critical regime is exactly that cubic.** *Prediction: `p0` states the slogan and cites no theorem, and the theorem is this field's.* ⛔ *Wrong if the corpus's continuation is not into the roots' own expression — if the imaginary excursion and the root triple are unrelated objects, this is a pun.* ⌗ *`sec:ledger`'s one-scale argument is the opposite kind of row: predict it **forecloses** numerology, so the field's honest verdict there is that the door is already shut and receipted* |
| 2 | **`P03`** | `sec:throat-angle` · `sec:winding` · `sec:ellipse` · `sec:tour` | ⛭ ***THE TRIPLE-ANGLE IS VIÈTE'S TRIGONOMETRIC SOLUTION OF THE CUBIC.*** *$4\cos^3\theta-3\cos\theta=\cos3\theta$ is the identity that solves a three-real-root cubic without radicals — it is the standard way round `casus irreducibilis`. **Prediction: `P03`'s "sky angle $w$, throat angle $u$, horizon angle $3w$ — three projections of one object" IS that identity, so the paper's three coupled parametrisations are the cubic's three roots in trigonometric normal form.*** ⛔ *Wrong if the triple-angle enters independently of the roots and is never used to express them.* ⌗ *And `sec:winding`, "the thirds that closure forces", predicts a **rationality condition on a rotation number** — closure iff rational — which is this field's, not geometry's* |
| 3 | **`P05`** | `sec:deck` · `sec:autA2` · `sec:conjugacy` · `sec:classification` | *Beyond `T1`: predict the degree-six closure and $\mathrm{Aut}(A_2)=S_3\times\mathbb{Z}_2$ are a **LATTICE** statement and not only a group one — $A_2$ is the hexagonal lattice, which is the **ring of Eisenstein integers** $\mathbb{Z}[\omega]$, whose unit group is $\mathbb{Z}_6$ and whose ring automorphisms are complex conjugation.* ⛔ *Wrong if `P05` already reads the deck group as a lattice, or if the Eisenstein reading adds no relation the paper lacks* |
| 4 | **`P13`** | `sec:sigma` · `sec:a2` · `sec:synthesis` | ⛭ ***"A REAL INVOLUTION IS NOT THE WICK ROTATION" IS A GALOIS-COHOMOLOGICAL STATEMENT.*** *Real forms of a complex group are classified by $H^1(\mathrm{Gal}(\mathbb{C}/\mathbb{R}),\mathrm{Aut})$; the Wick rotation **is** the nontrivial Galois element and a Weyl reflection is **inner**. **Prediction: `P13`'s three converging routes are three faces of the one fact that an inner automorphism cannot carry a nontrivial Galois class.*** ⛔ *Wrong if `P13` already says this, or if the cohomological reading fails to reproduce the paper's conclusion* |
| 5 | **`P02`** | `sec:ring` · `sec:continuation` · `sec:kretschmann` | *`sec:ring` — "the single horizon as the $\Lambda\to0$ limit of a root triple" — is a **DEGENERATION OF THE CUBIC**. Predict the paper tracks the collision without writing the **discriminant**, and that the $\Lambda\to0$ asymptotics of the three roots (two escaping, one staying at $2M$) are read off the cubic's **Newton polygon** in the parameter — valuation theory, and this field's.* ⛔ *Wrong if the discriminant is written and the limit taken through it* |
| 6 | **`P12`** | `sec:weyl-a3` · `sec:strata` · `sec:discrete` | ⌗ ***A WEYL GROUP IS A GROUP; A ROOT LATTICE IS A $\mathbb{Z}$-MODULE WITH AN INTEGRAL QUADRATIC FORM,*** *and an integral quadratic form is this field's object outright. **Prediction: `P12` uses the group and never the form** — so its $A_3$ appears without its Gram matrix, its discriminant $4$, or its dual $A_3^{*}$.* ⛔ *Wrong if any lattice-level fact is load-bearing there* |
| 7 | **`P14`** | `sec:count` · `sec:whichthree` · `sec:twofactors` · `sec:family` | *`sec:whichthree` distinguishes **two different three-element sets** and says the generations sit on one and not the other. Predict the distinguishing invariant is the $A_2$ configuration's two orbits — the three points **on** the circle against the lines **tangent** to it — and that in the Eisenstein reading these are two different arithmetic objects. ⛔ Wrong if the distinction is made on physical grounds with no invariant, in which case the row is a **scoped question**, not a claim* |
| 8 | **`P06`** | `sec:least-arbitrariness` · `sec:register-boundary` · `sec:modal` | ⛔⛭ ***THIS ROW GETS THE HARDEST READ OF THE SEVENTEEN, BY RULE.*** *§2: the integrable-systems run's ONE emptiness prediction was `P06`, and it was the ONE prediction REFUTED. **Predict: least-arbitrariness — "a structure carrying an unforced modulus is not a single world but a family" — has a rigidity reading in this field, and it is an ANALOGY rather than content.*** *That prediction is written in the form most likely to be wrong on purpose, and the read that scores it must be a read of `sec:least-arbitrariness` in full* |
| 9 | **`P10`** | `sec:lock` | *The closed-$S^3$ graviton tower is a **spectrum indexed by integers with arithmetic multiplicities** ($\ell(\ell+2)$, degeneracy of square type). Predict the paper uses the tower's **discreteness** and never its **multiplicity arithmetic** — so the field's content here is a scoped question and not a claim* |
| 10 | **`P15`** | `sec:largescale` · `sec:transmission` · `sec:tensions` | *Beyond `T3`'s $\zeta_3$: predict `sec:largescale`'s "flat/discrete decoupling and the low-multipole floor" is **the same $S^3$-integrality question as `P10`'s**, seen from the observational side — so the two papers share ONE question and neither asks it* |
| 11 | **`P08`** | `sec:trichotomy` · `sec:kernel` | *Predict EMPTY, and the test is named: `sec:trichotomy`'s three constant-curvature slicings — **is that a SIGN trichotomy (Sylvester, not this field's) or a DISCRIMINANT trichotomy (`P03`'s $4-3r_0^{2}$, which is)?*** ⛔ *If it is the second, the row is not empty* |
| 12 | **`P01`** | `sec:2` · `sec:3` · `sec:problems` | *Predict EMPTY, and the test is named: **`sec:2`'s "two of the three separations vanishing forces the third" is a counting statement**, and the read must establish it is a rank/degeneracy argument and not a parity argument. `zeta` ×8 here is the Killing vector, already scored* |
| 13 | **`P04`** | `sec:floor` · `sec:decomp` | *Predict EMPTY — **a FIFTH consecutive empty for `P04`**, and §2 makes that the reason to read it rather than the reason not to. Test: the $\sqrt N$ accumulation in `sec:floor` is a random-walk count. **If it is any field's it is probability's, and this pass must hand it over rather than claim it*** |
| 14 | **`P07`** | `sec:CR-mechanics` · `sec:CR-hawking` · `sec:frontiers` | *Predict EMPTY. Test: do the black-hole mechanics sections carry an **integrality** claim — area quantisation, an integer entropy, a discrete spectrum? If yes the row is not empty; `congruence` ×77 here is already scored geodesic* |
| 15 | **`P09`** | `sec:pd` · `sec:bound` | *Predict EMPTY. Test: `sec:pd`'s Kerr--NUT--(A)dS separability turns on separation constants; **is any admissibility condition a COMMENSURABILITY condition** — a ratio required rational? Predict no* |
| 16 | **`P11`** | `sec:discrete` · `sec:chirality` | *Predict EMPTY. Test named: **is any "discrete marker" a residue class that does arithmetic — that ADDS — or only a label that distinguishes?*** A $\mathbb{Z}_2$ handedness that never composes is a sign, not a modulus |
| 17 | **`P16`** | `sec:interior` · `sec:network` · `sec:peak` | *Predict EMPTY beyond `T3`'s $\zeta_3$. Test: the abundance network's integer charges and mass numbers are **conservation labels**; and `sec:interior`'s "parity, monodromy" is $\mathbb{Z}_2$ — predict both are labels, and read to check neither is a modulus* |

⌗ ***THE LOCATOR PREDICTS: 7 papers carrying something, 10 empty.*** *The v1 pass predicted 1 and 16.
**Where they disagree, the disagreement is the finding**, and it is scored at the close either way.*

⛔ ***AND THE PREDICTION MOST LIKELY TO BE WRONG IS WRITTEN AS ROW 8 ON PURPOSE.***

---

## ⌗ PASS B — THE READS, AND THE FIRST IS A LANDING

### ⛭⛭⛭ `T50` — **ROWS 1 AND 2 ARE ONE FINDING, AND IT IS A THEOREM THE CORPUS NAMES WITHOUT STATING**

| | |
|---|---|
| **rows** | 1 (`p0` `sec:imaginary`) and 2 (`P03` `sec:throat-angle`) |
| **verdict** | ⛭⛭ **CONFIRMED on row 1, and row 2 CONFIRMED-BUT-ALREADY-THERE** |
| **landed** | `p0` `sec:imaginary`, a fourth paragraph — `\rcpt{T50_...}` `\ldg{number_theory}` |

⌗ ***ROW 2 SCORED FIRST, AND IT SCORED AGAINST ME.*** *The prediction was that `P03`'s triple-angle
IS Viète's trigonometric solution of the cubic. **It is, and `P03` proves it** — `prop:triple`
derives $2M=\tfrac{2}{3\sqrt3}\sin 3w$, the proof runs through $\sin^{3}w=\tfrac14(3\sin w-\sin3w)$,
and the text says outright that "the three roots of the horizon cubic are the three preimages $w$,
$\tfrac{\pi}{3}-w$, $-\tfrac{\pi}{3}-w$ of $3w$ under the sine".* ⇒ **The prediction was right about
the mathematics and wrong about the corpus: there was nothing to add.**

⛔ ***AND THAT IS WHAT MADE ROW 1 FINDABLE.*** *`P03` has the trigonometric solution and never says
why a trigonometric solution is the only one available. `P05` `sec:deck` computes the Galois group
— **over $\mathbb{C}(2M)$**, which is the right base for a monodromy and the wrong one for this.
`P07` names the configuration "casus irreducibilis", twice, correctly, **as the name of a case**.*
⇒ ***THE CORPUS CARRIES THE THEOREM'S NAME, ITS TWO HYPOTHESES AND ITS OBJECT, AND NOWHERE ITS
CONCLUSION*** — *that over $\mathbb{Q}(2M)$ **no horizon radius lies in a real radical extension**,
so the imaginary route to them is forced.*

| | |
|---|---|
| **why it is worth landing** | *`sec:imaginary`'s three instances are all places the corpus **chooses** the imaginary, and a reader may answer "then do not". **The horizon radii are a fourth where that answer does not exist** — and the roots are real, which is the section's own law, met where it could not have been arranged* |
| **the hypothesis is `T1`'s** | ⛭ ***The same missing irreducibility step, load-bearing a second time, for a second theorem, in a second paper.*** *`T1` audited it for the $S_3$ inference; the casus needs the identical hypothesis, and `P05`'s Gauss's-lemma argument supplies it over the real base unchanged* |
| ⛔ **the control that killed the prettier story** | *$M=0$ and Nariai — the two members the corpus distinguishes — are **both** masses where the specialised cubic goes reducible with real-radical roots. **It selects nothing.** $2M=3/8$ is an undistinguished under-critical mass that does the same, and every rational $r_{0}$ gives one through $2M=r_{0}-r_{0}^{3}$: the reducible masses are **dense**. The receipt asserts the counterexample beside the coincidence so the first cannot be taken without the second* |
| ⛔ **the control the receipt found by FAILING** | *`M_SAMPLES` was written with $2M=2/5$ in it as under-critical. It is **over**-critical ($2\sqrt3/9\approx0.3849$) and three asserts fired at once. **Kept and promoted to `CONTROL 0`**, because the regime is the control the receipt most needed: over-critical SdS has one real horizon whose radical expression **is** real. ⇒ *And that is `P05` `prop:deck`'s own asymmetry — "in the over-critical regime only the order-two subgroup is realised on the real structure" — reached from solvability instead of monodromy* |

⌗ ***WHAT IS NOT CLAIMED.*** *Not that `P05`'s $\mathbb{C}(2M)$ computation is wrong. Not that the
$M=0$/Nariai reducibility means anything. Not that `P03` chose the sky angle for this reason — it
derives it gnomonically, and the finding is only that the derivation could not have come out
otherwise.*
