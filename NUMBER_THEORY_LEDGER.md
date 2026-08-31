---
name: number-theory-ledger
kind: FIELD-BAKE
current: r3710
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

### ⌗ PASS B — THE OTHER FIFTEEN, BY NAME

| # | paper | verdict | what was read, and what it settled |
|---|---|---|---|
| 2 | **`P03`** | ⛭ **CONFIRMED, and NOTHING OWED** | *`sec:throat-angle` in full. `prop:triple` **proves** $2M=\tfrac{2}{3\sqrt3}\sin3w$ through $\sin^{3}w=\tfrac14(3\sin w-\sin3w)$ — **Viète's trigonometric solution, derived** — and names the three roots as the three preimages of $3w$. `rem:dimension` carries it to general $D$.* ⇒ ***The prediction was right about the mathematics and wrong about the corpus.*** *What the paper does not say is why the trigonometric route is the ONLY one, which is `T50` and landed in `p0`* |
| 3 | **`P05`** | ⛔ **REFUTED** | *`sec:autA2`, `sec:deck`, `rem:galois-closure` read in full. The prediction was that an Eisenstein-lattice reading would add a relation.* **It adds none.** *`prop:autA2` already has $\mathrm{Aut}(A_2)=S_3\times\mathbb{Z}_2\cong D_6$, which **is** the full automorphism group of the hexagonal lattice, and the load-bearing step — $-1\notin W(A_2)$, so negation is outer — is stated, proved, and receipted (`negation_outer_A2`). **The ring structure $\mathbb{Z}[\omega]$ supplies nothing the group does not.*** ⌗ *And `rem:galois-closure` already identifies the sky angle as the degree-six splitting field. This paper is further into this field than the v1 ledger's one row records* |
| 4 | **`P13`** | ⛭ **ALREADY LANDED — by the paper's own abstract** | *`sec:sigma` in full. The prediction was that "a real involution is not the Wick rotation" is a Galois-cohomological statement about $\mathbb{C}/\mathbb{R}$.* ⇒ ***The general form is simpler than that and the paper already has it***: the abstract says the gauge face is *"reached by a change of signature and **not by any real-substrate operation**"*, which is **Sylvester's law of inertia** — no real change of basis alters a real quadratic form's signature — and it closes every real operation at once, not only $\sigma$. ⌗ *That is real quadratic-form theory, not arithmetic: the refinement this field would add (Hasse invariants at the finite places) **has no object**, because the substrate is over $\mathbb{R}$ and $\mathbb{R}$ is one place* |
| 5 | **`P02`** | ⛭ **CHECKED-NEGATIVE — a route, not a finding** | *`sec:ring` in full. The Newton polygon of $\epsilon r^{3}-r+2M$ in $\epsilon=1/\alpha^{2}$ has slopes $0$ and $-\tfrac12$, giving **one root of size $2M$ and two of size $\alpha$** — exactly `P02_ring_lambda_limit`'s "two roots run off to infinity, one finite horizon remains", by valuation instead of by limit.* ⛔ ***Same answer, no new relation.*** *Recorded because a second route to a result the corpus already receipts is worth naming and is not worth landing* |
| 6 | **`P12`** | ⛭ **CONFIRMED** | *`sec:weyl-a3` in full. The prediction was that `P12` uses the Weyl **group** and never the root lattice's integral quadratic form.* **It does.** *The paper's arithmetic input is the discriminant's square root — "the per-root resolution of $\sqrt\Delta$" generating the $V_4$ holonomy — which is Galois-theoretic and correct; no Gram matrix, no lattice discriminant, no dual lattice appears, and none is needed.* ⌗ *One observation, offered and not landed: the residue pairing's entries $1/f'(r_i)$ have product $-1/\Delta$, so its signature $(2,1)$ — an odd number of negative entries — **is forced by $\Delta>0$** rather than being a separate computation* |
| 7 | **`P14`** | ⛔ **REFUTED** | *`sec:whichthree` in full. The prediction was that the two three-element sets are distinguished by an $A_2$-orbit invariant.* ***They are not.*** *The paper settles it by the substrate's **null structure** — "a puncture of a hinge together with the two punctures its null generators reach", and "the causal classification of the six hinge-ends". **Causal geometry, from outside the sector, and nothing this field can reach*** |
| 8 | **`P06`** | ⛭⛭ **CONFIRMED AS PREDICTED — AND THE READ RETURNED THE FIELD'S BOUNDARY** | *`sec:least-arbitrariness` and `sec:register-boundary` in full, as the rule requires. The rigidity reading **is** an analogy, as predicted: the moduli are real and geometric, the three senses of "modulus" the paper separates are all real-parameter senses, and the transitivity statement is already `\ldg{integrable_systems}`.* ⛭ ***But the read produced the reason this field is empty, and it is a theorem the corpus proves about itself*** — see the boundary block below |
| 9 | **`P10`** | ⛔ **REFUTED** | *`sec:lock` in full. The prediction was that the paper uses the tower's discreteness and never its multiplicity arithmetic.* ***It uses the multiplicity outright*** — *"the degeneracy is $2(n-1)(n+3)$, ten at the floor $n=2$, so the shell contribution is $2n^{3}$" — and it is receipted, and a receipt exists **because that degeneracy was once assumed rather than derived**.* ⌗ *And the multiplicity is a **Weyl dimension**, not an arithmetic function; the counting function's $\tfrac13$ against $\tfrac23$ is spectral theory's Weyl law. Wrong prediction, right paper, and nothing here is this field's* |
| 10 | **`P15`** | ⛭ **CHECKED-NEGATIVE** | *`sec:largescale` in full. $k_L=\sqrt{L(L+2)}/r_0$ with integer degree $L$, quadrupole floor, flat projection through $j_\ell(k_L D_C)$. **The integrality is used and used correctly.*** ⌗ *The one place an arithmetic condition could enter — whether the discrete source ladder and the acoustic scale $\ell_A$ must be commensurable — **is not a condition of the construction**: the projection is flat and $\ell_A$ is set by $D_C$, so no ratio is required rational. Checked, and negative* |
| 11 | **`P08`** | ⛭ **CHECKED-NEGATIVE — the named test, run** | *`sec:trichotomy` in full. The test was whether the three constant-curvature slicings are a **sign** trichotomy or a **discriminant** trichotomy.* ⇒ ***A sign trichotomy***: the leaves are sorted by "the character of the held direction" of the embedding hyperboloid — spacelike, null, timelike. *Sylvester, not the discriminant* |
| 12 | **`P01`** | ⛭ **CHECKED-NEGATIVE — the named test, run** | *`sec:2` and `cor:threefold` in full. The test was whether "two of the three separations vanishing forces the third" is a **parity** argument.* ⇒ ***It is a rank/degeneracy argument about a quadratic form***: null gives $ds^{2}=0$, spatial coincidence kills the spatial part, the temporal part follows. *No counting, no arithmetic. `zeta` ×8 here is $\zeta=\partial_t$, as `T3` already scored* |
| 13 | **`P04`** | ⛭ **CHECKED-NEGATIVE — a FIFTH consecutive empty, and the test handed the material on** | *`sec:floor` read for the $\sqrt N$ accumulation. It is a **variance** argument — independent contributions, no cancellation, $\sqrt N$ growth.* ⇒ ***That is PROBABILITY's and this field hands it over rather than claiming it.*** ⌗ *`P04` has now returned empty on five fields. **Stated once, with the reason: it is the measurement paper, and its content is an exclusion built from a variance estimate*** |
| 14 | **`P07`** | ⛭ **CHECKED-NEGATIVE ON CONTENT — AND IT SUPPLIED HALF OF `T50`** | *`sec:CR-mechanics`, `sec:CR-hawking` and the quantisation sites read. **No integrality claim**: "the geometry quantises without coupling" is a winding count, and the winding's silence about magnitude is `p0`'s one-scale result, already receipted.* ⛭⛭ ***But the row predicted "empty" and `P07` is where the corpus writes "casus irreducibilis", twice.*** *The name is what made `T50` findable, and the locator did not predict it: **a paper can be empty of a field's content and still be where the field's finding starts*** |
| 15 | **`P09`** | ⛭ **CHECKED-NEGATIVE — the named test, run** | *`sec:pd` read. The Carter cut couples $\Delta_r$ and $\Delta_p$ through $\Sigma=r^{2}+p^{2}$ with two Killing fibres. **No admissibility condition is a commensurability condition** — no ratio is required rational anywhere in the separability. Predicted no, and no* |
| 16 | **`P11`** | ⛭ **CHECKED-NEGATIVE — the named test, run** | *`sec:discrete` in full. The test was whether any "discrete marker" is a residue class that **adds**.* ⇒ ***None is.*** *Colliding roots, a null$\leftrightarrow$timelike reassignment, a signature flip — three distinct geometric loci, and the wall marked by carrying none of them. The one composition present, $C=(Q\mapsto-Q)\circ(R\circ K)$, composes in $\mathbb{Z}_2$ as a **group**, with no modulus* |
| 17 | **`P16`** | ⛭ **CHECKED-NEGATIVE — the named test, run** | *`sec:interior` read. Parity and monodromy on an exact solution, a $\mathbb{Z}_2$ **label** distinguishing two behaviours and not a modulus. The network's charges and mass numbers are conservation labels, as predicted. $\zeta_3$ is `T3`'s and is used correctly* |

---

## ⛭⛭⛭ THE REACH CLOSE — the v2 §5b template, four blocks

### 1 · THE SEVENTEEN, BY NAME

| verdict | papers | count |
|---|---|---|
| ⛭ **LANDING** | `p0` — `T50`, the clause in `sec:imaginary` | **1** |
| ⛭ **WORKED, EARLIER** | `P05` — `T1`'s clause in `rem:galois`, from the v1 pass | **1** |
| ⛭ **CONFIRMED, NOTHING OWED** *(the content is there and the paper already has it)* | `P03` `prop:triple` · `P12` `sec:weyl-a3` | **2** |
| ⛭ **ALREADY LANDED** *(the general statement is the paper's own)* | `P13` — Sylvester, in its abstract | **1** |
| ⛔ **REFUTED** | `P05` (row 3, Eisenstein) · `P14` (row 7, the two threes) · `P10` (row 9, the multiplicity) | **3** |
| ⛭ **CHECKED-NEGATIVE, each with the kind stated** | `P02` *(a second route, no new relation)* · `P15` *(integrality used correctly, no commensurability required)* · `P08` *(sign trichotomy, not discriminant)* · `P01` *(rank, not parity)* · `P04` *(variance — handed to probability)* · `P07` *(no integrality — but it supplied `T50`'s name)* · `P09` *(no commensurability)* · `P11` *(no marker adds)* · `P16` *(labels, not moduli)* · `P06` *(analogy, not content — and it returned the boundary)* | **10** |

⌗ ***A `CHECKED-NEGATIVE` row here says WHICH KIND, as §5b requires***, *and three of the ten are
negative for reasons that are not "empty": `P02` because a route already exists, `P07` because the
content is absent but the name is not, `P06` because the analogy is real and the object is not.*

### 2 · THE BAR, MEASURED

| | |
|---|---|
| papers read, by name | **17 of 17** |
| Pass A predictions written **before** any paper was opened | **17**, committed at **r3706** |
| receipts written and named by THIS (v2) pass | **1** — `T50` |
| clauses landed by this pass | **1** — `p0` `sec:imaginary`, with its `\rcpt`, its `\ldg`, and its naming here |
| `\ldg{number_theory}` markers in papers | **2** — `P05` (v1) and `p0` (r3708) |
| canon rows routed | **0** |
| material handed to another field | **1** — `P04`'s $\sqrt N$, to probability |
| ⛔ **locator predictions REFUTED** | ***3 of 17*** |
| ⛔ **locator over-prediction** | *predicted **7** papers carrying, **1** owed anything.* **Wrong by six, and the six had to be read to find that out** |

⛔⛭⛭ ***AND THE SCORING CORRECTS A MISREADING OF §2 THAT THIS PASS WAS BUILT ON.*** *The v1 pass
predicted **1 carrying, 16 empty** and was right. This pass, holding §2's "a prediction of emptiness
gets more scrutiny", predicted **7 and 10** and was wrong by six.* ⇒ ***§2 is a rule about the
STANDARD OF EVIDENCE, not a prior on the answer.*** *Sixteen emptiness predictions, tested rather
than screened, held. **The rule earned its keep anyway — but not by overturning them.**
The one finding this pass produced was in `p0`, which the v1 pass had inside its eight-paper
screened row and never opened, and it was reachable only because `P03`, `P05` and `P07` were read in
full and their three pieces put together. **The locator's value was not more papers; it was the
one, and the six wrong predictions are what the reading cost.***

### 3 · WHAT IS STILL OPEN, SAID SHORT

* ***`T1`'s hypothesis now carries two theorems and is stated in one place.*** *`P05` `rem:galois`
  states the irreducibility argument; `p0`'s new paragraph cites `P05` for it rather than restating
  it. **If `P05`'s remark ever moves, two papers lose their hypothesis and only one of them says so.***
* ***The residue pairing's signature.*** *`P12`'s $(2,1)$ is forced by $\mathrm{sign}(-1/\Delta)$
  and the paper reaches it by computation. **Offered, not landed** — it is one line of a proof the
  paper does not need shortened.*
* ***`P04`'s $\sqrt N$ is owed to the probability bake***, and this ledger has not done that field's
  work for it.

### 4 · WHAT THE FIELD CHANGED, ONE LINE PER PAPER

| paper | what changed |
|---|---|
| **`p0`** | *gained a fourth instance in `sec:imaginary` **of a different kind from the other three**: one where the imaginary route is not chosen but forced* |
| **`P05`** | *nothing new — and the read established that this paper is **already further into this field** than the v1 ledger's single row recorded: the discriminant, the Galois group, the splitting field and the monodromy correspondence are all there* |
| **`P03`** | *nothing owed — and it is where the corpus's Viète solution is **proved**, which the v1 estimate table had flagged as a disagreement and left unresolved* |
| **`P07`** | *nothing owed — and it is where the theorem's **name** sits, without which `T50` would not have been found* |
| **`P13`** | *nothing owed — its general negative is Sylvester's, already in its own abstract, and stronger than the $\sigma$-specific version this field predicted* |
| **`P02` `P08` `P09` `P10` `P11` `P12` `P14` `P15` `P16` `P01` `P06`** | *nothing owed, eleven times, **each with the section read and the test named*** |

⇒ ⛔ ***READ AS A LIST, THAT SAYS ONE THING: THE CORPUS USES THIS FIELD CORRECTLY AND SPARINGLY, AND
THE ONE THING IT WAS MISSING WAS NOT CONTENT BUT A CONCLUSION IT HAD THE HYPOTHESES FOR.*** *Both of
this field's findings across both passes — `T1` and `T50` — are of that shape: **a step the corpus
takes soundly and does not justify, and a theorem the corpus has the pieces of and does not state.**
The field added no new physics and was never going to.*

---

## ⛭ THE BOUNDARY, RE-STATED WITH ITS REASON — **the v1 block said WHAT, and the v2 read found WHY**

> *The v1 boundary stands: **the corpus uses Galois theory and no other number theory**, and Galois
> theory is the part of the field that is really group theory. Nothing below strikes it.*

⛭⛭ ***AND THE REASON IS A THEOREM THE CORPUS PROVES ABOUT ITSELF.*** *`p0` `sec:ledger`: a
dimensionless magnitude needs two invariants, the substrate supplies one on either real form, and
every curvature invariant on either face is a pure power of $1/\alpha^{2}$ —
`\rcpt{P17_no_second_scale_on_either_face}`. `P06` `sec:least-arbitrariness` reaches the same place
from the other side: a structure with no unforced parameter has nothing to tune.*

⇒ ***A THEORY WITH NO DIMENSIONLESS NUMBERS OF ITS OWN HAS NO RELATIONS AMONG NUMBERS TO STUDY.***
*Number theory's objects are relations among numbers — a ratio's rationality, a constant's
transcendence, a Diophantine relation among magnitudes. **In a one-constant theory not one of those
questions can be POSED**, let alone answered.*

⛔ ***SO THE EMPTINESS IS DERIVED, NOT SCREENED, AND THAT IS THE DIFFERENCE THIS PASS MADE TO THE
BOUNDARY.*** *The v1 block established the emptiness by counting terms — the method §0 rejects. The
same emptiness now rests on a result the corpus states, receipts, and would have to give up to make
this field non-empty.* ⌗ *It also says exactly what would re-open the field: **a second invariant.**
Not a new reading — a second scale.*

⛔ *And the v1 "what this field cannot reach" note stands unchanged: whether the horizon cubic's
Galois group drops at special **rational** $2M$ is a genuine Diophantine question that bears on
nothing the corpus claims.* ⌗ ***`T50` now says why in one line: the reducible masses are DENSE,
so a rational coincidence there selects nothing — which is the same control `T50` asserts.***
