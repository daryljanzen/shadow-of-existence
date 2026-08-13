---
name: the-remaining-work
kind: PLAN
current: r2565+c54.206
description: THE REMAINING WORK — every outstanding thing in the programme with a route, not a status. Four veins, one verdict, two paragraphs, one publishing task. Written r2565.
sources: [chat]
---

# THE REMAINING WORK

> ***Not a status. A route for each thing, and an honest statement of which routes are cheap, which are
> programmes, and which nobody knows how to walk.***
>
> ⌗ *Written r2565, after the board reached **four veins, two leads** and the routed queue reached **five
> of fifty**. **Everything in this file is either a vein, a routed item, an open verdict, or a
> publishing task** — there is nothing else outstanding.*

---

# I · THE FOUR VEINS — what each would actually take

## ⓵ `PO-5` (`L-221`) · **THE BRIDGE FROM A GRADING TO A FIELD**

**THE QUESTION, as narrowed at r2526:** *not "is there an $R$-odd operator whose kernel is the four?"
but* ***"what BRIDGE from a grading to a field is not 'be a kernel'?"***

**⌗ WHY THE KERNEL ROUTE IS STRUCTURALLY UNAVAILABLE, and this is settled:**
*· $\{\gamma^\mu,\gamma^5\}=0$ makes $D$ anticommute with $\gamma^5$ — **a graded index exists**;*
*· $[m\cdot\mathbb 1,\gamma^5]=0$ — **mass commutes, and breaks the grading**;*
*· so $\{D+m,\gamma^5\}\ne0$ — ***an $R$-odd operator has no graded index, so its kernel is not a
  gradeable object.***

**⇒ SO THE ROUTE IS TO ENUMERATE THE ALTERNATIVES TO "KERNEL", not to keep hunting operators.** *The
standard bridges from a $\mathbb Z_2$-graded structure to a field content are: **kernel/index** (ruled
out above), **cohomology** (a complex whose degree is the grading), **a spectral projection** (a
band rather than a zero mode), **a representation-theoretic branching** (the grading labels irreps),
and **an anomaly** (the grading obstructs a symmetry).*
⇒ ***Four candidates, each testable against P14's own construction, and none has been tried.*** *The
work is: for each, ask what it would need from the substrate, and check whether the substrate supplies
it.*

**⚠ AND `L-242`'s CLOSURE IS THE CONSTRAINT THAT MAKES THIS TRACTABLE:** *electroweak breaking IS the
breaking of the substrate's orientation parity $R$, and $2M=r_0-r_0^3$ is odd — **so the $R$-odd sector
is not abstract; it has a geometric realisation with a bounded order parameter**.*
⇒ *The bridge has to land there. ***That is a much smaller target than "some operator".***

**COST:** *one session per candidate, and the first three are readable from P14 without computation.*

---

## ⓶ `PO-6` (`L-165`) · **DEFINING THE SUM · THE CLOSED-FORM $\Lambda>0$ SOLUTION · CAN ONE CONSTANT REGULATE**

**⌗ THIS VEIN IS THREE QUESTIONS AND THEY ARE NOT THE SAME SIZE.**

**(a) *Can a theory with one dimensionful constant regulate at all?*** ⛭ ***Partly answered r2564, and
the answer was already in p0:*** *$\ell_P$ is a **GAUGE**, not a scale; the Planck values are
**cross-register**; and $\alpha/\ell_P\sim10^{61}$ is **"the size of the universe in gauge-units — a
number, not a tuning."***
⇒ ***So the one-constant claim is not embarrassed by the appearance of $\ell_P$ in a formula. What
remains is the actual regularisation question: does a loop expansion on this substrate have a
cutoff-independent answer?*** *The corpus's own handle is that **the UV degree is quartic, the ordinary
zero-point degree, and compactness buys the IR free** — so the route is a **one-loop calculation on the
compactified substrate with the boundary condition closing per fibre**, and the question is whether the
quartic divergence is absorbed by the geometry or needs a counterterm the framework cannot supply.*
**COST: a real calculation, and cc54's shape.**

**(b) *Defining the sum.*** *This is the hardest thing in the programme and nobody should pretend
otherwise: **what is the measure on the space of cuts?** The corpus has the constraint algebra, the
deparametrized Hamiltonian, and the true clock — **it does not have a path-integral measure**.*
⇒ ***The honest route is not to define it but to establish what it must satisfy:*** *invariance under
the residual gauge, the right classical limit, and consistency with the per-fibre closure. ***A list of
necessary conditions is a real deliverable and is not currently written down.***
**COST: a programme. The necessary-conditions list is a session.**

**(c) *The closed-form nonlinear $\Lambda>0$ solution.*** *P11 carries the nonlinear regime **on its
classical side** and the Gowdy–de Sitter system on a true Hamiltonian.* ⇒ *The route is the **Nariai
limit as an exactly solvable point** — $dS_2\times S^2$ has a known closed form, and the corpus already
uses it. ***The question is whether it extends off the degenerate member as a perturbation series in
$M-M_N$.*** **COST: a calculation, and it is the most likely of the three to yield.**

**⌗ AND WHAT UNLOCKS WHEN THIS VEIN MOVES:** *the **non-perturbative quantization** (B·2, P8's "the
deepest open question the construction raises"). **Its kinematic half is already exhibited** — all three
of W1's instances closed — so ***what waits here is the quantization, not the dynamics***.*

---

## ⓷ `PO-9` (`L-175`) · **CAN A SECOND SLICING BE NON-ARBITRARY?**

**⌗ HALF OF THIS VEIN CLOSED AT r2552:** *the cut's four-ness **does** carry the forcing of the dynamics
— least-arbitrariness is the programme's own criterion of necessity, and it rejects exactly the
adjustable parameter a second Lovelock coefficient would be.*

**WHAT REMAINS:** ***could a SECOND slicing be non-arbitrary — its selection forced by the first?***
⇒ **THE ROUTE IS THE ONE THE FIRST SLICING USED.** *The first is forced by maximal symmetry plus
Rule 2: **the substrate is the least-arbitrary vacuum, and a symmetry-breaking modulus is the adjustable
parameter the criterion rejects.***
⇒ ***So the question is whether a second cut has an analogous uniqueness statement — and the test is
mechanical: enumerate what a second slicing would have to break, and check whether any of it is a
modulus.*** *If every choice a second slicing makes is a modulus, the answer is **no** and the vein
closes; if one is forced, that forcing is the finding.*
⌗ *And the guard holds throughout: **the chain runs CUT→DYNAMICS, never CUT→SUBSTRATE**, and the
substrate's dimension stays bounded below only.*
**COST: one session, and it is the most likely vein to close outright.**

---

## ⓸ `PO-seam` (`L-202`) · **DOES A MASSIVE TRAJECTORY CARRY A PHASE?**

**⌗ WHAT IS KNOWN:** *the null trajectories are $K$'s fixed set, and that is what fixes their phase.*
**WHAT IS NOT:** *whether a massive trajectory — not on $K$'s fixed set — carries one at all.*

⇒ **THE ROUTE IS THE ONE `L-805` JUST WALKED FOR THE NULL CASE.** *cc54 showed every mode of interest
**freezes** before the crossing because $c_sk/|aH|\to0$; the massive question is the same computation
with a **massive dispersion relation** — and the object to compute is whether $\omega/|aH|\to0$ for a
massive mode, which it need not.*
⇒ ***If a massive trajectory does NOT freeze, it carries a phase, and the seam datum's phase acquires a
derivation — which is exactly `PO-7`'s inversion route ⓷.***
⌗ ***So this vein and the one open verdict are the same object approached from two sides, and nobody has
said so before now.***
**COST: cc54's instrument, one run.**

---

# II · THE ONE OPEN VERDICT

## `PO-7` (`L-171`) · **IS 0.408 A REAL DISAGREEMENT WITH THE SKY?**

**⌗ THE STATE:** *`kills/PO-7.md` is **complete** — object named, four checks written, **all four now
pass**. ① SAME-OBJECT (and all four withdrawn quantities failed exactly it); ⑤ RELATIVE-OR-ABSOLUTE;
③ PRICE, asymmetric; **④ CHAIN, cleared at r2559 when cc54 reproduced the freezing argument**.*

**⇒ WHAT REMAINS IS NOT A CALCULATION.** *Route ② ends "**and Daryl authorises**", and `F5` forbids a
node converting. **Both nodes have declined to, correctly.***

**⚠ AND ②'s OTHER TWO INVERSIONS ARE STILL OPEN AND ARE REAL WORK:**
*· ⓶ ***the estimator could be biased by the arm's own construction*** — bounded (**undriven arms agree
to 0.013 in $\phi/\pi$**) but **the driven case is where the disagreement lives**, and nobody has tested
the estimator on a driven object with a known phase. ***That is a buildable check: inject a synthetic
spectrum with a known asymptotic phase and see whether the estimator recovers it.***
*· ⓷ ***the seam datum could acquire a derivation landing off $\{0,\pi\}$*** — `CRPHI` is currently
**assigned**. ⇒ ***And `PO-seam` above is exactly that derivation's route.***

⇒ ***So the verdict is not blocked on a decision alone: two named calculations would strengthen or
overturn it, and both are specified here.***

---

# III · THE ROUTED FLOOR — two items and two offers

| item | route | cost |
|---|---|---|
| **18** · *p0's frontier item 1, datum half* | ***the finding is that it CANNOT be derived*** — the work is writing that as a result rather than an owing, which is what the item already says | **one paragraph** |
| **50** · *trans-Planckian* | the scoping IS the content: ***finite at each finite exterior time, NOT uniformly bounded*** — one clause, with the scope attached | **one clause** |
| **52** · *the de Sitter entropy* | ⛭ ***answered r2564***: $S=3\pi/(\Lambda\ell_P^2)$ is p0's own gauge-count | **one clause** |
| **9** · **26** | ***conventions offered, not imposed*** — no owing | — |

---

# IV · THE PUBLISHING TASK

## `L-218` · **THE READER PACKAGE**

*· **⓶ done** (`COMPANION_SPEC`), and the rule tested at r2561: ***enforceable, and enforceable means
severe*** — 333 anchors against 7480 sentences, so **DISCUSSED is the fourth bucket and the default**.*
*· **⓵ pandoc-in-CI**: not present (0 hits in the workflows). ***A CI step and a format matrix — an
afternoon, no physics.***
*· **⓷ the contribution**: last, by the row's own ordering.*

⌗ ***This is the one outstanding thing with no vein connection, and it is the only one that is
publishing rather than physics.***

---

# V · WHAT THIS FILE SAYS ABOUT THE SHAPE

**⌗ FOUR VEINS, AND THEY ARE NOT FOUR PROGRAMMES:**
*· **`PO-9`** is most likely to **close outright** — one session, and its test is mechanical;*
*· **`PO-seam`** is **one cc54 run**, and it is the same object as `PO-7`'s inversion ⓷;*
*· **`PO-5`** is **four candidate bridges**, three readable without computation;*
*· **`PO-6`** is **three questions of very different size** — (c) is a calculation, (a) is a
calculation, and **(b), defining the sum, is the genuine programme and the only thing here nobody knows
how to start**.*

⇒⇒ ***So of everything outstanding, exactly ONE item is open-ended: `PO-6`(b). Everything else has a
route written above, and most are a session or a run.***

⚠ **AND THE HONEST CAVEAT:** *routes are cheap to write and this file is written by the line that has
been wrong about scope repeatedly this session — **r2536's implication, `L-230`'s population,
`VARIATIONAL_LEDGER`'s premise**. ⇒ ***Every route above should be treated as a hypothesis about cost,
not a measurement of it, and the first thing each session should do is check whether the question is
still stated correctly.***

*Written r2565. Stated for reversal.*
