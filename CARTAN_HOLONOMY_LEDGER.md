---
name: cartan-holonomy-ledger
kind: FORWARD
current: r3445
job: The Cartan / connections-and-holonomy field-bake ledger — what bit, what bounced, and the boundary. First of the four fields `L-272`'s re-survey left outstanding. `OWED` 622.
sources: [cowork]
---

> **▣ FORWARD — the Cartan bake, and part of the corpus.** *Three registers kept apart: **what bit**,
> **what bounced**, **what the boundary is**. `L-272`'s re-survey put this field first of four, on ×84
> word-bounded with every occurrence load-bearing — and because station Ⓖ threw the **algebroid** half
> (`L-265`, the Atiyah sequence) while the **connection-and-holonomy** half was never thrown.*


## ⛭ THE BASELINE, MEASURED FIRST

| present, and load-bearing | absent across all seventeen, word-bounded |
| --- | --- |
| `monodromy` ×55 · `holonomy` ×33 · `connection` ×35 · `Cartan` ×11 · `gauge field` ×4 · `flat connection` ×3 · `parallel transport` ×2 · `curvature form` ×2 | `Ambrose–Singer` · `principal bundle` · `frame bundle` · `structure equation` · `covariant derivative` · `torsion` · `G-structure` · `reduction of structure group` · `Wilson loop` · `Christoffel` · `Levi-Civita` · `vierbein` · `soldering` |

⚠ **AND THE BASELINE CAUGHT A FALSE HOLE IN THE OTHER DIRECTION, WHICH IS NEW.** *`G-structure` came
back ×1 — matching inside* ***breakin**g-structure*** *, in a sentence about symmetry breaking.* ⇒ **The
third substring artefact in one session**, *after `bit` ×253 inside `orbit` and `norm` ×118 inside
`normal`.* ⌗ ***So the word-bounded count is now reported by `corpus/reach_baseline.py` itself — the
mirror of its existing DE-MACROED flag. Where a de-macroed count being HIGHER means a macro is hiding
real uses, a word-bounded count being LOWER means the substring is inventing them.***


## ⛭⛭ WHAT THE CORPUS CLAIMS

`P07` and `P14` both report it. *The residue pairing the horizon roots' surface gravities carry* **"has
a holonomy about the branch points — a Klein four-group ... and adjoining it closes the Weyl group of
$\so(6,\mathbb{C})$"**, *with the verdict* ***"so the excess is substrate-derived rather than
assumed."***


## ⛭⛭ THE COMPUTATION — from scratch, no group theory put in

*Three roots of $r^3-r+2M$ and three branches of $\sqrt{f'(r_i)}$, continued numerically around each
Nariai branch point and around infinity.*

| | result |
| --- | --- |
| $\gamma_\pm$ | **transpositions** — the two roots that collide at each Nariai point |
| $\gamma_\infty$ | a **3-cycle** — the cube-root branching at infinity, the corpus's deck $\mathbb{Z}_3$ |
| relation | $\gamma_+\gamma_-\gamma_\infty = 1$ **on the roots** — the thrice-punctured sphere's own relation |
| the group generated | **order 24**, root image $S_3$, kernel of order 4 |
| the kernel | $\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\}$ — ***exactly `P05`'s Klein four-group***, the even-sign patterns, arrived at by continuation rather than by unimodularity |
| element-order profile | $\{1{:}1,\;2{:}9,\;3{:}8,\;4{:}6\}$ — **$S_4$'s, and no other order-24 group's** |

⇒ ***So $G \cong S_4 = W(A_3) = W(D_3) = W(\so(6,\mathbb{C}))$. The corpus is right.***

**Controls, both directions.** *A loop enclosing no branch point returns the identity. One lasso alone
returns a group of order **4**, not 24 — so the method can tell a small group from a large one and the
24 is a measurement. Robust across three base points and three lasso radii.*


## ⛔⛭⛭ WHAT BIT — the closure is GENERIC TO CUBICS

| family | $\lvert G\rvert$ | root image | kernel | $S_4$? |
| --- | --- | --- | --- | --- |
| $r^3-r+2M$ **the horizon cubic** | 24 | $S_3$ | 4 | ✔ |
| $r^3-r+M$ | 24 | $S_3$ | 4 | ✔ |
| $r^3-4r+M$ | 24 | $S_3$ | 4 | ✔ |
| $r^3+r+M$ *(no real merger at all)* | 24 | $S_3$ | 4 | ✔ |
| $r^3-7r+3M$ | 24 | $S_3$ | 4 | ✔ |

⇒ ***ANY one-parameter depressed cubic family, taken with its per-root square root, delivers this
group. The horizon cubic is not special here.***

⛭ **So "substrate-derived rather than assumed" is sound about the DERIVATION and misplaces the
surprise.** *The Klein four-group really does come from the residue pairing's square roots and is not
put in by hand — that part stands entire. What the genericity shows is that **the group is forced by
the cubic**, so the weight belongs on the other side: **what is not forced is that the substrate's Weyl
group is the same group.***


## ⛭⛭ AND THAT MATCH IS $D_3$ ALONE

$\lvert W(D_n)\rvert = 2^{n-1}n!$ · $\lvert W(A_n)\rvert = (n+1)!$ · $\lvert W(B_n/C_n)\rvert = 2^n n!$

| rank | $A_n$ | $B_n/C_n$ | $D_n$ | = 24? |
| --- | --- | --- | --- | --- |
| 2 | 6 | 8 | 4 | — |
| **3** | **24** | 48 | **24** | ✔ **both** |
| 4 | 120 | 384 | 192 | — |
| 5 | 720 | 3840 | 1920 | — |
| 6 | 5040 | 46080 | 23040 | — |

*and the exceptionals are 12, 1152, 51840, 2903040, 696729600 — none is 24.*

⇒ ***Among every classical and exceptional Weyl group of rank two or more, the cubic's 24 selects
$A_3 = D_3$ and nothing else — and the two coincide because $\so(6,\mathbb{C}) \cong
\mathfrak{sl}(4,\mathbb{C})$, a low-rank exceptional isomorphism.***

⛭ **So the closure is a RANK-THREE FACT, in the same shape as `P03`'s `rem:dimension`: it holds where
it holds and fails immediately on either side.** *At $\so(8,\mathbb{C})$ the cubic still gives 24 and
the Weyl group gives 192.* ⌗ ***That is a stronger statement than the papers make, and a narrower one
— which is the trade a bake is supposed to find.***


## ⌗ WHAT BOUNCED — and the corpus is ahead of the field

*The relation that the deck $S_3$ is generated by the two Nariai transpositions, with the 3-cycle at
infinity their composite, looked like the bake's second finding.* ⛔ **It is not a finding. `P05`
carries it as `prop:monodromy`, and `rem:monodromy-group` states the condition a naive version
misses:**

> ***"Two transpositions generate $S_{3}$ only if they differ, so the generation claim ... rests on
> the two Nariai monodromies transposing different pairs of sheets, which is a computation."***

*and records* **"Verified numerically by continuation in the complex $2M$-plane."** ⇒ **A bounce, and a
clean one: the field's framing adds nothing the paper did not already have, including the caveat.**


## ⚠ THE APPARATUS IS ABSENT AND THE CONCLUSION TURNS ON IT

*The corpus computes holonomy ×33 and monodromy ×55, asserts* **"the bundle is flat. Flat holonomy
supplies exact selection rules and no curvature"**, *and carries none of the structure holonomy is
normally defined in.* ⇒ ***`Ambrose–Singer` ×0 is the load-bearing absence: it is the theorem that
makes a FLAT connection have discrete holonomy, which is what licenses reading monodromy AS holonomy —
the step every computation in this ledger relies on.***

⌗ **What is owed is the name of a theorem, not a section.** *Nothing computed here is wrong for want of
it. But a reader asked to accept that the monodromy of a cubic IS the holonomy of a connection is being
asked to supply the bridge themselves.* ⛭ *Fifth instance of the corpus's characteristic shape — the
Atiyah sequence, $N_{\rm eff}$, the baby universe, matched-procedure control, and now Ambrose–Singer.*


## ⌗ THE BOUNDARY — what this bake did not reach

- **The connection itself.** *`P07` says the substrate's canonical connection is "genuinely
  non-abelian, with holonomy in $\so(4,1)$". **This bake computed the monodromy of the CUBIC, not the
  holonomy of that connection**, and the two are identified in the papers rather than here. Named as
  unreached rather than letting the computation stand in for it.*
- **Curvature.** *`curvature form` ×2. The flatness claim is asserted in `P14` and not recomputed here;
  a bake verifying it would be checking the premise this one used.*
- **The $\su(3)$ argument.** *"A real bundle's complexification carries a parallel conjugation, so its
  holonomy lands in the real form" is a genuine holonomy-theoretic argument and it is `P14`'s own. Read
  and not disputed; not independently recomputed.*
- **Ambrose–Singer applied rather than named.** *Whether stating it buys anything beyond the name — a
  curvature computation making the flatness a theorem in the corpus's own voice — is the obvious next
  probe and is **not** claimed to be free.*

⛔ **AND THE ONE THING THIS BAKE MUST NOT BE READ AS SAYING:** *nothing here weakens the corpus's group
identification. The order, the root image, the Klein four-group and the $S_4$ are all confirmed by
independent computation. What changed is **where the surprise lives** — not in the cubic, which forces
the group, but in the substrate, whose Weyl group matches it at rank three and nowhere else.*


---

# ⛭⛭ BROUGHT TO THE BAR — r3445

> *The r3164 bake's content stands entire and is not restated. What it lacked against
> `THE_FIELD_BAKE_PLAN` was **numbered probes and a receipt** — and this ledger's every conclusion
> turns on one numerical computation that had none. **Closed, and the receipt caught two errors in
> its own construction while being written.***

## ⌗ THE LEAD REGISTER — *no new field while any row is unmarked*

| # | probe | state |
|---|---|---|
| `C0` | baseline, word-bounded | ⊢ **WORKED** r3164 — *and it caught a false hole: `G-structure` ×1 was matching inside **breaking-structure**, the third substring artefact of that session, which is why `reach_baseline.py` now reports word-bounded counts* |
| `C1` | are the two Nariai monodromies transpositions of **different** pairs? | ⊢ **WORKED** r3445, **receipted** |
| `C2` | what group do they generate, and is the kernel `P05`'s Klein four-group? | ⊢ **WORKED** r3445, **receipted** |
| `C3` | what does order 24 select among the Weyl groups? | ⊢ **WORKED** r3445, **receipted** |
| `C4` | is the closure special to the horizon cubic? | ⛔ **BITE** — *generic to depressed cubics; receipted r3445* |
| `C5` | does the deck $S_3$ generation add anything the corpus lacks? | ⟐ **BOUNCE** — `P05` `prop:monodromy` has it **with** the caveat a naive version misses |
| `C6` | is `Ambrose–Singer` ×0 a load-bearing absence or a vocabulary gap? | ⛔ **LOAD-BEARING** — *it is the theorem that makes a **flat** connection have discrete holonomy, and the corpus asserts flat holonomy with exact selection rules and no curvature* |
| `C7` | does the null-loop control distinguish a small group from a large one? | ⊢ **WORKED** r3445, **receipted** — *identity returned; one lasso alone gives order 4, not 24* |
| `C8` | is the substrate's Weyl group forced to be the same group? | ⚑ **NO, AND THAT IS WHERE THE WEIGHT BELONGS** — *the cubic forces 24; the coincidence with $W(\so(6,\mathbb C))$ is not forced* |

---

## ⊢ C1–C4, C7 — **RECEIPTED**, and the receipt caught two errors while it was written

*`storyboard_receipts/CH_C1_C3_the_holonomy_is_S4.py`, all asserts pass.*

- **`C1`** — $\gamma_+$ and $\gamma_-$ come back as transpositions of **different** pairs, $\gamma_\infty$
  as a 3-cycle, and a null loop as the identity. ***That "different pairs" is exactly the condition
  `P05` `rem:monodromy-group` says a naive version misses***, and this is the computation that supplies it.
- **`C2`** — order **24**, root image $S_3$, kernel of order 4 equal to
  $\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\}$ — ***exactly `P05`'s Klein four-group, reached by
  continuation rather than by unimodularity*** — and element-order profile $\{1{:}1,2{:}9,3{:}8,4{:}6\}$,
  which is $S_4$'s and no other order-24 group's.
- **`C3`** — among all classical Weyl groups of rank 2–6 and all five exceptionals, **only** $W(A_3)$
  and $W(D_3)$ have order 24, and they coincide because $\so(6,\mathbb C)\cong\mathfrak{sl}(4,\mathbb C)$.
- **`C4`** — every depressed cubic family tested returns **24**: $r^3-r+q$, $r^3-4r+q$, $r^3-7r+q$, and
  ***$r^3+r+q$, whose branch points are off the real axis entirely*** — a stronger genericity statement
  than the r3164 entry had.

**⚠ TWO CONSTRUCTION ERRORS THE RECEIPT'S OWN ASSERTS CAUGHT, recorded because they would have passed
unnoticed in prose.** *First, generalising $f'$ to $3r^2+p$ I dropped the $p$ — the group collapsed from
24 to **6** and the profile to $\{1{:}1,2{:}3,3{:}2\}$. Second, the branch points of $r^3+pr+q$ sit at
$q=\pm2(-p/3)^{3/2}$, which is **imaginary** for $p>0$; lassoing the real axis there enclosed nothing and
returned $\lvert G\rvert=1$.* ⇒ ***A ledger that asserts a number in prose cannot catch either.***

---

## ⛭⛭ THE BAR, MEASURED

| | this bake | the FULL tier's range |
|---|---|---|
| lines | **~215** | 189–978 ✔ |
| numbered probes | **9** (`C0`–`C8`) | 10–17 ⚠ *one short* |
| receipts, all running | **1** | 2–10 ⚠ *one short* |
| papers touched | `P05`, `P07`, `P14`, `P03` = **4** | 6–11 ⚠ |
| lead register | **9 rows, none unmarked** | — |

⚠ ***THREE SHORT, AND NAMED RATHER THAN ROUNDED UP. This field is not yet at the bar.***
