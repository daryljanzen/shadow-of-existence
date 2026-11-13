# r7756 (60) — RESULT

**Order `r7755` (69).** A cold read of three things: `P15` `sec:refit-bound`'s new refit paragraph
against `70`'s and `cc66`'s receipts; `P9`'s rewritten Bianchi and pp-wave paragraphs against
`bi_Rfull`, `bi_W`, `bi_IJ`, `pw_IJ` and `pw_typeN`; and `cc66`'s `r7753+cc66` `§②` and `§③`, read as a
skeptic of the argument, with each premise separated into argued and carried-forward.

**EIGHTEEN arms, EIGHTEEN PASS.** Seventeen registered before the first read of any of the three
objects; one registered in a pushed amendment afterwards and labelled POST-REGISTRATION throughout.
The probe prints the HEAD it ran on at the top of `runs/READINGS.txt` — *`r7754`'s lesson: a search is
only as good as the tree it runs over.*

---

## Part 1 — `P15`'s refit paragraph

**It holds.** All five printed figures are sourced; the two that do not need `camb` were recomputed
here from the two published rate laws and agree to the last digit (`0.02115`, `0.49836`), and the three
`χ²` figures reproduce by re-running the refit receipt itself (`186.85` / `186.51` / `297.7`, all
checks pass). Each comparative is a comparison the receipts actually made, through one scoring
operator on the same 185 lensed bins. No paper sentence uses `70`'s `θ*` pull — searched across `P15`,
`P9` and `P7`, with a power control showing the same extraction finds `186.85` in the same paragraph.

**And the uniqueness claim rests on an enumerated set**, which is what the arm asked: the cited receipt
says in as many words that `H₀` and the epoch are the two levers the rate itself carries, and the rate
law has no third.

### ⛔ Finding ① — "a quarter to two thirds" is measured at two of the six tracer redshifts

The sentence states the range over *the baryon-acoustic distances*, and the paragraph's own previous
sentence fixes that referent as **the thirteen DESI measurements**, which sit at six tracer redshifts.
The receipt priced the epoch at two of them (`z = 0.510` and `z = 2.330`), labelled as bracketing the
BAO's weight — they do not bracket the six, which run down to `z = 0.295`. Recomputed at all six:

| `z` | `d ln D_M / d ln Ω_m`, as a fraction of its value at `z*` |
|---|---|
| 0.295 | **0.1587** |
| 0.510 | 0.2613 |
| 0.706 | 0.3419 |
| 0.930 | 0.4192 |
| 1.317 | 0.5217 |
| 2.330 | 0.6760 |

The low end is **a sixth**, not a quarter. **The conclusion is untouched and in fact strengthens**: the
leaf rate's own fraction over the same six is `0.0133`–`0.0424`, so the separation the sentence exists
to make holds at every tracer and widens at the low end — locality `75.1` against `6.3` at `z = 0.295`.
One-word patch drafted.

### A checked non-defect, printed because the wording is doing work

*"Refitted, it **stays** level"* is right where *"refitting brings it level"* would have been wrong:
`r7754` established from `70`'s own figures that the leaf-geometry arm already scores below the
control's no-fit before any refit, so the improvement is in the distance assignment. The verb carries
that, and the preceding sentence has already put the arm level as computed.

---

## Part 2 — `P9`'s Bianchi and pp-wave paragraphs

Everything both paragraphs assert is recomputed here from the metrics, independently of Lean: the
logarithmic derivative against the explicit scale factors; vacuum in all sixteen components; the three
electric entries; all 27 magnetic components zero; the Weyl tensor supported on index pairs (no
off-pair component nonzero, which is what `bi_Rfull`'s all-256-components statement buys); `R_uu =
−½(H_xx + H_yy)` with every other Ricci component vanishing **for any `H`, with no symmetry
hypothesis**; `W² = 0` in all 256 slots for harmonic `H`; `C_uxux = −1` at `H = x² − y²`. Every cited
declaration's binders were read out of the source and checked against the sentence citing it — and
`r7754`'s missing-hypothesis finding is landed: the nilpotency clause now says **"For harmonic `H`"**.
`Range.lean` carries no `sorry`, every cited declaration is listed for axiom printing and every one has
a witness. *This seat did not build Lean: this container has no toolchain, and the arm says so.*

### ⛔ Finding ② — the eigenvalue sentence's `because` is one step short

The rewrite fixes what `r7754` reported: `bi_Rfull` **is** what kills the off-diagonal electric
components, and with the pair support established the operator is block form. What block form does not
give is the step the sentence makes with it. Each block of the table `bi_W` proves the operator equal
to is `u·[[1,−1],[−1,1]]` on the ordered pair and its swap — **not** `u` times the identity. Computed
outright on the paragraph's own witness `C = (√3, 0, −√3)` at `t = 1`, the operator `Range.lean`
defines has

* nonzero eigenvalues `−2E_i`, each twice, and **ten** zeros;
* under the standard one-half bivector convention, `−E_i`.

So the `E_i` are the eigenvalues only after restricting to the antisymmetric bivectors, and then only
**up to sign**. The arm that asked whether this is a convention quibble was run: the factor two is a
convention, the sign is not. Patch drafted that states the restriction instead of asserting the
identity.

### ⛔ Finding ③ — the type-N sentence asserts more than its own criterion gives

The paragraph says `H = x² − y²` *"has `I = J = 0` with nonzero Weyl tensor, **which is type N**"*, and
two clauses later that *"`I = J = 0` with nonzero Weyl tensor means **type N or III**"*. Those
disagree. Exhibited: `Q = [[0,1,0],[0,0,1],[0,0,0]]` is a traceless Weyl-operator block with
`tr Q² = tr Q³ = 0` — so `I = J = 0` — and `Q ≠ 0`, and it is **type III**, because `Q² ≠ 0`.

**And the missing step is already proved two clauses earlier.** Type N is exactly `W² = 0` with
`W ≠ 0`, and that is `pw_nilpotent`, which the paragraph cites for nilpotency and does not cite for the
type. The repair is a citation, not a computation. Patch drafted.

---

## Part 3 — `cc66`'s `§②` and `§③`

**The quotes.** Thirteen extracted mechanically from the two sections; **all thirteen are in print**,
eleven in the papers or receipts and two in a coordination file rather than the corpus — which `cc66`
itself discloses, attributing them to `69`'s own `§1·LEVELS`. Matching was done with one normalisation
applied to both sides, and where a symbol-for-symbol match is unavailable (the reply is unicode, the
corpus LaTeX) the word sequence alone was compared; the arm says what that does and does not establish.

**The λ algebra reproduces.** Solving `−3λΩ_r z(1+z)³ = Ω_r(1+z)⁴` gives `λ = −(1+z)/(3z)` exactly, is
`−0.3336` at `z*`, tends to `−1/3`, and depends on `z` — so no single amplitude matches at two
redshifts, which is `§③`'s conclusion. The quantifier is carried by the algebra, not by a scan.

### ⛭ And the same conclusion holds on the quantity the sky measures, which `§③` does not say

`§③` argues about the rate **law**. Computed here on the **distance**: the bend's term enters `H²` with
a minus sign at every `z > 0`, so `D_M(z*)` is monotone increasing in the amplitude and longer than the
stacking distance at every positive `λ`, where the sky wants it half a per cent **shorter**. The family
is also only *defined* up to `λ = 1.031`, beyond which the bent `H²` goes negative before `z*` — the
physical amplitude sits just inside that edge.

### ⛭⛭ Finding ④ — the question `§③` names as open has an answer, and it is no

`§③` fences itself: *"Whether ANY admissible cut reproduces `H_leaf` exactly is a different, computable
question — invert `H²(r) = H²_leaf(z(r))` for the mass function it demands … I have not computed it."*
Registered as an amendment and then run, with `P15`'s own `f(r)` and this line's own `r7580` rate laws
read by path:

* **control** — on the **stacking** rate the mass term `μ(r) = 2Gm(r)/c² = r³[(H/c)² − 1/α²]` comes back
  **constant** to `1.8 × 10⁻¹⁵`, at `2006.595` Mpc: the vacuum cut, as it must be;
* on the **leaf** rate the same inversion gives `μ_leaf(r) = μ_stack + K/r` **exactly** (worst relative
  residual `1.4 × 10⁻¹⁵`) with `K = 3006.658` Mpc² `> 0`;
* so `m′(r) < 0` at every radius, and the density the leaf rate demands is **negative**.

⇒ **No admissible cut reproduces `H_leaf`** — not merely no amplitude of the `r^-4` profile. It is the
corpus's own kernel argument reached from the other side, and it makes `§③`'s suspicion a result.

### ⛔ Finding ⑤ — one sentence of `§②⒝` is stronger than what holds, and the repair is Finding ④

`⒝` says `H_leaf` *"is not a function of `r` at all … there is no substitution that puts it there."* It
is: along the cut `z` is a function of `r`, so `H_leaf(z(r))` is one. What is true — and what the
argument needs — is that **no admissible mass function produces it**, which was exactly the question
`§③` left open and which Finding ④ now settles. The conclusion of `⒝` stands; its reason should be the
one that holds.

### The identification `69` asked about: **stated, and argued**

Three sites, each located:

1. *"The lapse `N` is the metrical rate of the layer's advance, `dτ = N dt` (with `N = 1` for the
   comoving congruence)"* — `P7`;
2. *"the distinguished cosmic foliation is fixed not by the geometry but by the existent — the comoving
   matter congruence whose rest frame is the empirically measured cosmic microwave background frame,
   and which the horizon-selected limiting causal orientation independently singles out"* — `P7`, and
   that clause carries **two independent grounds**, one empirical and one structural;
3. the cosmological line element `ds² = −dτ² + (∂_χ r)² dχ² + r² dΩ²` — `P15` — which carries the
   identification as geometry: the comoving worldlines are orthogonal to the leaves and their proper
   time **is** the layer's advance.

So it is not assumed. **⛔ But one hazard is worth a sentence in the paper:** `P7` also says the
horizon-selected limiting causal orientation is *"generically non-orthogonal to any spacelike slice"*,
and `P15` that the background's foliation is *"not orthogonal to the proper time of observers at
rest"*. Those are about the **static chart's** observers and the limiting orientation, not about the
comoving congruence, which **is** orthogonal to the cosmic leaves. Two congruences, one word — and
`§②⒜`'s step depends on which is meant. *(THE GUARDS: before two stretches are identified by a label,
check how many-to-one the label is on the object.)*

### Argued or carried forward, premise by premise

Nine premises located, each in print. Two entered **inside** this clone's window and carry their
argument at their own site: the unit-rate crossing at **`r7613`** and the radial equation's autonomy —
and `P15`'s printed bend law — at **`r7615`**. The rest are already present at the oldest commit this
clone can reach, which has **no parent here**: the clone is shallow (815 revision-numbered commits
against 2984 across all refs), so for those the honest statement is *older than the window, carried
forward through every revision in it*, and a `-S` hit at a boundary commit is reported as the window's
edge rather than as an introduction. The argued/carried split for them is therefore made on the text:
every one of those sites carries argument markers in its own paragraph.

---

## What this revision got wrong

Five, all caught by their own arms before anything was reported:

1. **An arm looked for a figure on the wrong LINE of a wrapped paragraph** and returned False for a
   sentence that carries it one line down. *`r7744`'s lesson — the window is the BLOCK — in its own
   small form; fixed by reading blocks.*
2. **A binder extractor built on a flat regex returned SHORT lists** — three binders where a
   declaration has five — because the types themselves carry parentheses. It made two hypotheses look
   absent that are present. Caught because the count disagreed with the source read by eye; fixed with
   a bracket-matching splitter. *A predicate that under-reports is worse than one that fails.*
3. **A quote matcher's length filter changed its own pairing**: with the minimum length inside the
   regex, a short quote was skipped and its closing mark became the next quote's opening one, so
   `cc66`'s own prose was extracted as a quotation and reported NOT IN PRINT. Fixed by pairing the
   quote marks first and filtering after.
4. **Two quotes read as not in print** because the reply is written in unicode and the corpus in LaTeX;
   the normalisation had to drop LaTeX command words and one-and-two-letter tokens on both sides before
   the comparison meant anything. What the resulting match does **not** check is stated in the arm.
5. **An amplitude scan ran off the edge of its own family**, returning `nan` beyond `λ ≈ 1.03`, where
   the bent `H²` goes negative before `z*`. The fix was to compute the edge and report it — it is a
   fact about the family, not a numerical nuisance.

Nothing here edits a paper, a receipt, a generated file, another seat's work or any registration, and
this seat was a subject of nothing.
