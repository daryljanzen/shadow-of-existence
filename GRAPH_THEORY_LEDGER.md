---
name: graph-theory-ledger
kind: FIELD-BAKE LEDGER
current: r4068
job: The graph-theory / percolation field bake — what bit, what bounced, and where the boundary is. Thrown at r4009 after the survey was found to carry 21 fields with graph theory not among them, while `probability / stochastic processes` was in the table and had been baked.
sources: [corpus, arXiv:2603.03257]
---

# THE GRAPH-THEORY LEDGER — *what bit, what bounced, and the boundary*

> **▣ WHY THIS FIELD WAS THROWN.** *`corpus/field_survey.py` carries **24 registered fields** and graph
> theory is not one of them. **The omission is structured rather than accidental**: `probability /
> stochastic processes` **is** in the table (line 116) and **was** baked — so the field percolation
> lives inside was surveyed, and the graph-theoretic question was never put.*
>
> ⇒ ***Measured here, not inherited.*** *`PROBABILITY_LEDGER.md` is **347 lines** and contains
> **zero** instances of `percolation`, `phase transition`, `critical probability`, `lattice`,
> `transitiv*`, `cluster` and `isoperimet*`. Its only two matches on `graph` are **`graphic`** and
> **`graphy`** — inside `historiographic` and `historiography`. **So the field was thrown and this
> was not in it.***

---

## ⓪ R0 — THE BASELINE, BEFORE ANY HOLE IS ASSERTED

*Step 1 of the plan's six, and it is run on **both halves** of the corpus: `reach_baseline.py` reads
the seventeen paper bodies, `prior_art.py` reads the receipts. **The instrument's own head says why
both are needed** — two bakes of this line turned on an operator settled at `r2819` and verdicted at
`r2825`, consulting neither.*

### ⌗ THE PAPERS — *and the vocabulary trap fired exactly as predicted*

| term | total | inside longer words | genuine |
|---|---|---|---|
| `percolation` | **0** | — | **0** |
| `critical probability` | **0** | — | **0** |
| `phase transition` | **0** | — | **0** |
| `isoperimetric` | **0** | — | **0** |
| `adjacency` · `clique` · `chromatic` · `spanning tree` | **0** | — | **0** |
| `expander` · `volume growth` · `growth rate` | **0** | — | **0** |
| `critical` | 236 | **154** | ~82 |
| `edge` | 143 | **51** | ~92 |
| `graph` | 158 | 5 | ~153 |
| `node` | 34 | 0 | 34 |
| `automorphism` | 66 | 0 | 66 |
| `transitive` | 12 | 6 | ~6 |
| `bipartite` | **1** | 0 | **1** |

> ⛔ **THE COUNTS ARE MOSTLY VOCABULARY AND THE INSTRUMENT SAID SO.** *`edge` ×143 is inflated by
> **`wedge`** — P15×11, P07×5 of the word-bounded matches. `critical` ×236 is inflated by
> `supercritical`, `subcritical`, `critically`. `node` ×34 is P07×30 and is the **nodal line** of a
> function, not a vertex. `graph` ×153 is overwhelmingly **the figure sense**.* ⇒ *Had the bake read
> the raw counts as reach it would have reported a field that is present and it is not.*

### ⌗ THE RECEIPTS — *and `prior_art.py` fired on this field*

**Four things the corpus has already adjudicated, which a bake must not claim:**

1. **`I21_least_arbitrariness_and_superintegrability_join_at_transitivity`** — ⛔ **already joins two
   of the three transitivity statements.** *P06's "maximal symmetry leaves nothing to choose", I17's
   maximal superintegrability, and P12's non-transitive `SO(5,1)` action on the cut space. I21 states
   the join **in one direction**, leaves the converse **explicitly open**, and asserts three
   NON-relations so a later reader cannot infer more.* ⇒ ***A bake arriving to announce that join
   would be claiming settled work as its own.***
2. **`P03_hexagon_null_triple`** — the six hinge-ends, the causal trichotomy, and *"the symmetry group
   is transitive on the six punctures, so an absolute assignment is **forbidden**, not merely absent"*.
3. **P12** — the mass is *"a modulus **transverse to the orbits**"* and the action on the cut space is
   **non-transitive**.
4. **P14** — *"`Aut(A_2)=D_6` realised as the dial's hexagonal symmetry … fundamental domain [0,30]"*.

---

## Ⓐ WHAT BIT — *three findings, two receipted*

### ⛭⛭ G1 — THE SIX HINGE-ENDS CARRY AN OCTAHEDRON, AND ITS ANTIPODES ARE THE HINGES ⊢

> **The question the field asks that the corpus does not.** *P03 computes the causal character of all
> fifteen pairs of the six hinge-ends and reads **one** of the three classes as a graph. **What are the
> other two, and what is their complement?***

`P03_hexagon_null_triple` computes, from `X·Y = α²(−3εε′ + 4cos(θₐ−θ_b))`:

```
TIMELIKE  ⟺ SAME HINGE   3 pairs      spacelike ⟺ SAME HORN   6 pairs      NULL ⟺ NEITHER   6 pairs
```

*3 + 6 + 6 = 15 = C(6,2), so **the trichotomy is a complete edge-3-colouring of K₆**.* Read as graphs
— **recomputed from P03's own formula**, not quoted:

| class | edges | degrees | graph |
|---|---|---|---|
| timelike ⟺ same hinge | 3 | all 1 | **perfect matching** (1-factor) |
| spacelike ⟺ same horn | 6 | all 2 | **two disjoint triangles**, 2K₃ |
| null ⟺ neither | 6 | all 2 | **the hexagon** C₆ — *P03's own reading* |

> ⇒ ***AND DELETING THE TIMELIKE MATCHING FROM K₆ LEAVES THE OCTAHEDRON.*** *Twelve edges,
> 4-regular, **every vertex with exactly one non-neighbour** — which is the definition of `K_{2,2,2}`.
> **Its three antipodal pairs are exactly the three hinges.***

**Why the name earns its place.** *`K_{2,2,2}` is vertex-transitive **and** edge-transitive, and the
only structure distinguishing one vertex from another is which antipode it has.* ⇒ *So **"an end is
characterised by its hinge and nothing else" is a graph-theoretic statement**, and the octahedron is
the graph that says it.*

⌗ **HONEST BOUND.** *This establishes **no new physics**. Every causal value is P03's, verified rather
than assumed. What is new is the naming: the corpus reads one of three classes as a graph and leaves
the other two, and their complement, unnamed. **A name is not a theorem** — it is what lets the next
reader see three facts as one object.*

**⊢ RECEIPT:** `receipts/L831_graph_theory/G1_the_six_hinge_ends_carry_an_octahedron_and_the_hinges_are_its_antipodes.py` — **14 checks, ALL PASS.**

---

### ⛭ G2 — P03's OWN GRAPH ARGUMENT IS SOUND, AND ITS BIPARTITE CLAUSE IS LOAD-BEARING

> **The question.** *P03 writes: "six vertices of degree two, bipartite between the horns, **which is
> why** the closed figure is a hexagon and why it alternates." **Is that argument complete, or is
> `bipartite` decoration?***

**It is complete, and the clause is doing real work.** *2-regular on six vertices permits **two**
shapes: C₆, or C₃ + C₃. **Bipartiteness excludes the second**, because a bipartite graph has no odd
cycle.* ⇒ ***So the hexagon is forced, and it is forced by the clause P03 states.*** *Removing the word
`bipartite` would leave the conclusion unproved.*

⌗ *Verified inside G1 by **walking** the null relation rather than asserting it: from any end the walk
returns to its start after exactly six steps, visiting six distinct vertices — one hexagon, not two
triangles.*

> ⛭ **This is the field's most useful verdict on this corpus and it is a positive one.** *The one place
> the corpus argues graph-theoretically, it argues **correctly**, and the load-bearing hypothesis is
> the one it names.*

---

### ⛭ G3 — THE CORPUS HAS NO ISOPERIMETRIC FUNCTION, AND THAT IS THE CONCEPT THE 2026 THEOREM TURNS ON

> **The question.** *The theorem's conclusion is governed by `Φ`, the isoperimetric function. **Does the
> corpus have one, for any object?***

**No.** *`isoperimetric` **×0**, `expander` **×0**, `volume growth` **×0**, `growth rate` **×0**,
`surface-to-volume` **×0** across the seventeen bodies.* ⌗ *`boundary` ×578 is a **causal** boundary
throughout — horizons, null boundaries, boundary conditions — never a **combinatorial** one, and 476
of the 578 are inside longer words.*

⇒ ***This is a clean absence and it is the interesting kind.*** *The corpus reasons constantly about
boundaries and never once about the **ratio of a boundary to what it encloses**. That ratio is what
carries the 2026 theorem, and it is what a percolation reading would need.*

---

## Ⓑ WHAT BOUNCED — *and a bounce is data*

### ⛔⛭⛭ G4 — THE 2026 THEOREM MISSES, AND THE HYPOTHESIS THAT FAILS IS FINITENESS, NOT TRANSITIVITY ⊢

> **The paper, read at source rather than from a summary.** Diskin, Easo, Ramanan Radhakrishnan,
> Sudakov, Tassion, *Supercritical sharpness of percolation*, **arXiv:2603.03257**, submitted
> **3 March 2026**. Abstract, verbatim:
>
> > *"We prove that for supercritical percolation on every infinite transitive graph, the probability
> > that the origin belongs to a finite cluster of size at least n decays exponentially in Φ(n), where
> > Φ is the isoperimetric function of the graph."*

⌗ ***The summary this bake was handed said the theorem is "about transitivity where the old lattice
proofs used the lattice". That is true and it is not the whole content**: the conclusion is governed by
the **isoperimetric function**. The lattice is replaced by `Φ`, not merely by transitivity.*

**"The corpus's graphs are finite so the theorem misses" is true and is not a probe**, because it does
not say which hypothesis does the work. Checked separately:

| hypothesis | verdict |
|---|---|
| the graph is **infinite** | ⛔ **FAILS** — six vertices |
| the graph is **transitive** | ✔ **HOLDS** — octahedron and C₆ both vertex-transitive, by exhausting S₆ |
| a **percolation process** runs on it | ⛔ **ABSENT** — `percolat*` ×0 in the bodies |

> ⇒ ***AND FINITENESS IS BINDING FOR A REASON INSIDE THE CONCLUSION.*** *The isoperimetric function of
> a finite connected graph **vanishes on the whole vertex set** — `Φ(|V|) = 0`, because `V` has empty
> edge-boundary. "Decays exponentially in `Φ(n)`" therefore degenerates to "decays exponentially in 0"
> exactly where a finite graph runs out of room.* **The conclusion is not merely unavailable on a
> finite graph; it is empty there.** *Checked: `Φ(6) = 0` for both, while `Φ(3) = 6` and `Φ(3) = 2`
> respectively — so the vanishing is finiteness, not a peculiarity of these two graphs.*

**⊢ RECEIPT:** `receipts/L831_graph_theory/G4_the_2026_sharpness_theorem_misses_and_finiteness_is_the_binding_hypothesis.py` — **12 checks, ALL PASS.**

⚠ **NOT CLAIMED**, and asserted as non-relations in the receipt so no later reader can infer them:
*(a)* that percolation has nothing to say to the corpus — *what is ruled out is one theorem reaching
two graphs, not a field*; *(b)* that the corpus should acquire an infinite graph to meet the
hypothesis — ***a hypothesis is not a target.***

---

### ⛔ G5 — NO RANDOM PROCESS RUNS ON ANY DISCRETE STRUCTURE IN THE CORPUS

> **The question.** *Percolation is a measure on edge-subsets. **Does the corpus carry any random
> process on a discrete structure at all?***

**No.** *`PROBABILITY_LEDGER.md`, the ledger of the field that was baked, carries zero `cluster`, zero
`lattice`, zero `phase transition`.* ⇒ *So the gap is not that percolation was **considered and
rejected** — it is that **the discrete-probability half of the probability field was never in view**.*
⌗ *That is a fact about the earlier bake, recorded here without re-litigating it.*

---

### ⛔ G6 — THE `Aut(C₆) = Aut(A₂) = D₆` COINCIDENCE IS PRIOR ART, NOT A FINDING

> **The question.** *P03/P14 count **twelve designations** = `|Aut(A₂)|`, over **six arcs** = the Weyl
> chambers, between **six marks**. The dial is a 6-cycle and `|Aut(C₆)| = 12`. **Is that identity
> structural, and does the corpus have it?***

**It is structural, it is trivial once seen, and the corpus already has it.** *`A₂`'s roots form a
regular hexagon, so its automorphism group **is** the hexagon's symmetry group — computed here,
`|Aut(C₆)| = 12 = |D₆|`.* ⇒ ⛔ ***And P14's receipt already says it in those words**: "`Aut(A_2)=D_6`
realised as the dial's hexagonal symmetry".*

> ⌗ **RECORDED AS A BOUNCE BECAUSE THAT IS WHAT IT IS.** *A field bake that reported this as a finding
> would be re-deriving a receipt. `prior_art.py` is what caught it, on its second use in this bake.*

---

## Ⓒ THE BOUNDARY — *where the field's word and the corpus's word are not the same word*

### ⛭⛭ G7 — "TRANSITIVE" IS TWO DIFFERENT STATEMENTS AND THE CORPUS USES THE OTHER ONE

> ***This is the boundary of the whole field and everything else sits on one side of it or the other.***

| | graph theory | this corpus |
|---|---|---|
| what acts | `Aut(G)`, a **discrete** group | an isometry / gauge group, a **Lie** group |
| what it acts on | a **finite or countable vertex set** | a **continuous homogeneous space**, orbits, cut spaces |
| what transitivity buys | *every vertex looks alike* → a **hypothesis** of the theorem | *no modulus to choose* → an **ontological** argument (P06) and a **dynamical** one (I17) |
| what its failure looks like | some vertex is distinguishable | **a modulus appears** (P12: mass transverse to the orbits) |

> ⇒ ***The two are genuinely analogous and they are not the same statement.*** *`I21` has already
> worked the continuous side and joined two of its three appearances, one-directionally, converse
> open. **The discrete side is what this bake could add, and G1 is the whole of what it adds**: two
> six-vertex graphs, both vertex-transitive, on which nothing further is available.*

---

### ⛭⛭ G8 — THE DISCRETE FORM OF `p0`'s SEVENTH FACE IS **TRIVIAL** WHERE THE CONTINUOUS FORM IS SUBSTANTIVE

> **The question, and it is the sharpest one the field asks of this corpus.** *`p0`'s seventh face
> states transitivity as physics — "one maximally symmetric substrate is one standard the same at every
> point … **universality is not a postulate over the geometry but the maximal symmetry read as the
> invariance of the measure**". **A vertex-transitive graph is the discrete form of exactly that
> sentence. Is it more than a restatement?***

**It is less, and the direction of the loss is the finding.** *In the continuous case, "the measure is
invariant" is a **substantive** claim: a homogeneous space carries an invariant measure because the
group action supplies one, and `p0`'s argument is that universality follows from it rather than being
assumed alongside it.* ⇒ ***In the discrete case the corresponding statement is automatic.*** *A
vertex-transitive graph's invariant measure is the **counting measure**, and counting measure is
invariant under **every** permutation, transitive or not. **The discrete analogue of the load-bearing
step carries no load.***

> ⛔ ***So the analogy inverts.*** *`p0`'s face reads as though a graph would make it concrete. **A
> graph makes it vacuous** — which is a reason the corpus is right to state it where it does, over a
> continuum with a measure that can fail to be invariant, and not over a discrete set where it cannot.*

---

### ⛭ G9 — THE GROUPOID IS NOT A GRAPH, AND READING IT AS ONE LOSES THE STRUCTURE THAT DOES THE WORK

> **The question.** *P12's groupoid of observer descriptions — vertices the vantages, edges the
> reassignment morphisms — is proved **rigid**: forced discrete generators, no continuous moduli,
> `D₃ ≅ S₃`. **Is the graph reading available, and does it buy anything?***

**Available, and it buys nothing, and the loss is specific.** *A groupoid has **composition**: two
composable morphisms have a product, and the rigidity result is a statement about the **generators of
that composition** — "discretely generated by the unique involution together with sky-angle
periodicity" (P03).* ⇒ ***The underlying graph forgets composition.*** *`D₃ ≅ S₃` is a fact about a
group; the graph reading retains only which vantages are related, which is the least of what P12
proves.*

⌗ ***So the honest verdict is that the corpus is right not to use the graph language here***, and a
bake that pressed it would be replacing a structure with its shadow. *A forgetful functor is not a
finding.*

---

### ⛔⛭ G10 — THE `P07` PARALLEL IS A SHARED **SHAPE** AND NOT A SHARED **MECHANISM**

> **The question, as it was put to this bake.** *Sharpness was proved on lattices in the 1980s by a
> method that could not be adapted because it **used the lattice**; the 2026 proof works because it
> **never uses the lattice, only transitivity**. `P07`'s central theorem ③ has the same shape — collapse
> holds **for any symmetry**, the horizon's causal structure following "from Lorentzian causal structure
> alone, making no use of spherical symmetry". **Shared mechanism, or only a shared shape?***

**Only a shape, and the reason is that the two discarded structures are of different kinds.**

| | the lattice, in percolation | spherical symmetry, in P07 ③ |
|---|---|---|
| what it is | a **combinatorial scaffold** — the proof's counting ran on it | a **symmetry assumption** on the solution |
| what replaced it | an **inequality**: the isoperimetric profile `Φ` | **nothing** — the causal argument never needed it |
| the move | *substitute a weaker quantitative hypothesis* | *delete a hypothesis and re-derive* |

> ⇒ ***Both are "the special-case proof leaned on structure the result never needed", and that is where
> the resemblance stops.*** *The percolation proof **replaces** its scaffold with a measurable quantity
> and the theorem's conclusion is stated **in terms of that quantity**. `P07` **removes** its hypothesis
> and the conclusion is unchanged.* ⌗ ***A replacement and a deletion are not one mechanism**, and the
> corpus gains nothing by treating them as one.*
>
> ⌗ *This probe was thrown with its answer suspected — "I suspect only a shape, and I want to be shown
> either way." **Shown: only a shape**, and the discriminator is whether the conclusion mentions the
> replacement.*

---

### ⛭ G11 — WHAT THE `K₆` DECOMPOSITION IS **NOT**

> **The question.** *G1 exhibits one perfect matching among K₆'s edges. **K₆ has a 1-factorization into
> five** disjoint perfect matchings. **Are the other four anywhere in the corpus?***

**No, and they should not be.** *The corpus's matching is **distinguished by physics** — it is the
same-hinge relation, and the hinge is an object of the construction. The other four 1-factors of `K₆`
are combinatorially available and carry **no** causal meaning.* ⇒ *So the corpus has **one** marked
1-factor, not a 1-factorization, and the field's natural next question — "which factorization?" — is
**not a question about this object**.*

⌗ *Recorded because a bake that found a perfect matching and reached for the factorization would be
importing a question the corpus's object does not pose.*

---

### ⛔ G12 — NO COLOURING, FLOW, MATCHING-OPTIMISATION OR CONNECTIVITY QUESTION ARISES ANYWHERE

> **The question.** *The field's working problems — chromatic number, max-flow/min-cut, maximum
> matching, `k`-connectivity, planarity. **Does any of them arise?***

**None.** *`chromatic` ×0, `clique` ×0, `spanning tree` ×0, `adjacency` ×0. The corpus's discrete
objects are **six vertices and twelve designations**; at that size every such question is answered by
inspection and none is load-bearing.* ⌗ *The one apparent exception is G1's edge-3-colouring, and it is
not a colouring **problem** — the colours are given by causal character, not sought.*

---

## ⌗ THE VERDICT, AND IT IS AN HONEST SMALL ONE

> ***Graph theory has ONE genuine contact with this corpus, and the rest is vocabulary.***
>
> The contact is **G1**: six hinge-ends, a complete edge-3-colouring of `K₆`, and an octahedron whose
> antipodes are the hinges — with **G2** establishing that the corpus's own graph argument, in the one
> place it makes one, is sound and its stated hypothesis load-bearing.
>
> Everything else bounces, and the bounces are informative rather than empty: **G4** the theorem misses
> on *finiteness* while *passing* transitivity, with the conclusion **empty** rather than unavailable;
> **G8** the discrete form of `p0`'s seventh face is **vacuous** where the continuous form is
> substantive; **G10** the `P07` parallel is a shape and not a mechanism; **G9** the groupoid is more
> than its graph.
>
> ⛭ ***This is a THIN field honestly measured, and the plan's own standard is that saying so is the
> point***: *"An honest outcome is that graph theory has one or two genuine contacts and the rest is
> vocabulary. Say so if that is what you find … a thin bake that claims completeness is worse than an
> honest empty one."*

## ⌗ CONSEQUENCES — *carried, or ROUTED with the clause stated*

| # | consequence | disposition |
|---|---|---|
| G1 | the octahedron naming | **ROUTED, NOT APPLIED** to `P03` §`sec:tour`. *Exact clause for the paper-holder:* **"The three classes are a complete edge-3-colouring of $K_6$: the timelike pairs a perfect matching, the spacelike pairs two triangles, the null pairs the hexagon already named. Deleting the timelike matching leaves the octahedron $K_{2,2,2}$, whose antipodal pairs are the three hinges."** *Not applied here because `P03` is under active reach-pass by another line and a naming addition is that pass's call, not this bake's.* |
| G2 | `bipartite` is load-bearing | **NO EDIT OWED.** *The paper already states the clause that carries the argument.* |
| G4 | the theorem's reach | **CARRIED HERE ONLY.** *No paper claims contact with it, so there is nothing to correct — recorded so a later reader meeting the Quanta article does not open the question again.* |
| G8 | the inversion | **ROUTED, NOT APPLIED** to `p0`. *Clause:* **"The discrete analogue — a vertex-transitive graph — is not the concrete form of this face; counting measure is invariant under every permutation, so the discrete statement carries no load. The face is substantive because the measure is continuous."** |
| G6 | prior art | **NOTHING OWED.** *`P14`'s receipt already states it.* |

