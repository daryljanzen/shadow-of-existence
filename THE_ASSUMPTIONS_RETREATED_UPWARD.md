---
name: the-assumptions-retreated-upward
description: Capstone for the c54.114–c54.153 arc — the collapse-perturbation sector worked end to end. What stands, what was withdrawn, and the pattern the withdrawals make. Read this before reopening front #1.
sources: [cowork]
kind: RECORD
current: c54.153
class: arc-capstone
job: The c54.114–c54.153 capstone — 14 results that stand, 13 withdrawn, and the pattern the withdrawals make (the assumption kept retreating upward). READ BEFORE REOPENING FRONT #1.
---
> **⌗ CLASSIFIED r2385 (observer line) as `RECORD` + `class: arc-capstone` — and the reason is a distinction
> worth keeping.** *It is not `STATE`: it does not track a moving position, it **closes an arc** and says what
> survived it. It is not `METHOD`: its content is this sector's physics and this sector's withdrawals, not a
> rule. **A capstone is a record whose value is that it was written at the moment the arc stopped**, and dating
> it against a later fork front would be the inverted-gradient error — so it carries the revision it closed at
> and nothing else.*
>
> **⌗ AND THIS LINE ABSORBED TWO THINGS FROM IT RATHER THAN REDISCOVERING THEM** *(`ARC 15`'s absorption, not
> collaboration):*
> *① ***"the dominant failure is not a wrong link but a RECEIPT THAT CANNOT FAIL"*** — built as
> `corpus/check_receipt_asserts.py`, the seventeenth gate. **Its corpus-wide extent is larger than the cluster
> of three this document found: 101 of 267 receipts carry no failure path, and 97 of those are cited by a
> paper.** Registered `L-208`.*
> *② ***"a gate that has never failed is not evidence that it works"*** — the same line this line reached
> independently at r2378 ("a gate that has only ever passed is a gate that has never been tested"), and the
> self-test pattern added to `check_withdrawn` at c54.151 is the better form of it: **each registry entry
> carries a KNOWN-POSITIVE string and the gate fails if its own pattern stops matching.***


**Capstone, `r2376+c54.114` → `r2376+c54.153`. Forty revisions on one sector.**

*Written at the point where the front stopped being a calculation and became a question about what the
construction means.*

---


# The assumptions retreated upward

**Capstone, `r2376+c54.114` → `r2376+c54.153`. Forty revisions on one sector.**

*Written at the point where the front stopped being a calculation and became a question about what the
construction means.*

---

## ⌗ WHAT THIS ARC WAS

It began as housekeeping — a bundle, a ranked list, a question about whether P7's frontier had actually
shrunk. It ended having rebuilt the corpus's entire account of what the progenitor sends across the branch
point, and having withdrawn most of what it built along the way.

**The honest ledger, first, because it is the least comfortable part and everything else reads differently
against it:**

| what the arc produced | count |
|---|---|
| results that stand | 14 |
| composition bounds argued or computed, then withdrawn | 7 |
| revisions of apparatus withdrawn wholesale | 4 |
| verdicts withdrawn | 2 |
| corrections to corrections | 1 |
| base-rate entries added | 11 |
| receipted claims corrected in place | 3 |
| standing-document rows found stale by writing this capstone | 3 |
| **paper paragraphs found asserting a withdrawn result** | **1 (P16, five claims)** |
| **receipted claims found with no receipt behind them** | **1 (the scalar monodromy)** |
| cited receipts read against their sentences / how many matched | **28 / 14** |
| formulas found specialised-and-unlabelled, quoted in 2 papers | 1 |

***That is not a story about carelessness and it is not a story about triumph. It is what it looks like when
a sector is worked until it stops yielding to the tools you brought.***

---

## ⌗ THE PHYSICS THAT STANDS

Everything below survived every withdrawal, because each piece is local to the branch point, local to the
background, or computed on a single passage. Nothing here depends on the recursion that turned out to be
the unresolved thing.

### The one-constant theorem, and its three faces

Three sectors, worked separately, returned one shape. **The winding quantises** and cannot supply a
strength. **The flat bundle selects** and cannot supply a coupling — its holonomy group is finite (order
81, by exact monomial arithmetic over $\mathbb{Z}_3$), its moduli space of flat connections is
zero-dimensional, and every point of it carries $F\equiv0$. **The branch point filters** and cannot supply
a content.

The common root: ***a dimensionless magnitude needs two invariants, and the substrate has one by
construction.*** The Wick face was the last route to a second — and it carries the same $\alpha$, so there
is none.

**And the theorem recurred one level down, on the perturbations rather than the couplings.** The crossing
fixes how much an amplitude is multiplied and does not fix the amplitude. Same statement, different sector,
found independently.

### The branch point's local structure

- **Exponents $(0,1)$** at the crunch, once the interior carries any radiation at all — against $(-1,2)$
  for pure dust. The jump is discrete, so pure dust is a measure-zero exception rather than a limit.
- **Radiation is the odd part exactly.** The closed dust-plus-radiation ball solves in conformal time as
  $a=\tfrac{A}{2}(1-\cos\eta)+\sqrt{B}\sin\eta$, and the parity splits *by species* with no cross terms —
  dust the entire even part, radiation the entire odd.
- **The monodromy differs by sector**, which nobody had noticed because nobody had used the true scalar
  variable: $4\pi i/\rho$ for scalars against $2\pi i/\rho$ for tensors. The tensor value is exact for any
  content whatever, since $z_T=aM_{\rm Pl}/2$ always; the scalar one required
  $z_S=a\bigl(a+4B/3A\bigr)/a'=a\bigl(a+\rho^2A/3\bigr)/a'$, derived in closed form for a closed
  interior. ***The doubling is a property of the variable, not of the parameters*** — verified
  $A$-independent at the recollapse cap and at a different composition. *This form is itself a
  c54.151 correction: the corpus had carried an $A=2$ specialisation, dimensionally inconsistent
  at any other $A$, in two papers and four standing documents.*
- **The turnaround pole is apparent.** $z_S$ diverges where $H=0$; continuing around it in the complex
  plane returns a real transfer with the Wronskian preserved, so it contributes no monodromy.

### Recollapse *is* Nariai

A closed dust ball with $\Lambda$ turns around if and only if $A\le2\alpha/3\sqrt3$ — **symbolically
identical to the Nariai threshold**, which the corpus derives from the horizon cubic's double root. Two
constructions, no shared step, same number. *A progenitor that can seed a universe is necessarily
sub-Nariai, which is exactly the regime the slicing construction requires for three horizons; a
super-Nariai ball never turns around and so never reaches a branch point at all.*

### The interior-to-observed mode map

Both halves were already in the corpus and unjoined. The harmonic index passes the branch point unchanged —
an integer eigenvalue label has nothing to rescale — and P15's own closed-$S^3$ projection sends mode $L$ to
$\ell=\sqrt{L(L+2)}\,D_C/r_0$ with no new parameters. **The joined map validates against the corpus's own
parameter-free low-multipole deficit: $7.78$ against a stated $7.8$.** One coefficient doing two jobs, and
the second was already compared against data.

### $\hbar$ is multiplicative, and that is the whole asymmetry

$\hbar$ enters only through the vacuum normalisation, and $\zeta=v/z$ with $z$ classical — so the power
spectrum carries it as an overall factor. ***It survives in an amplitude and cancels in every logarithmic
derivative.*** So $A_s$ is permanently inherited and $n_s$ is not, and the two were never the same kind of
quantity — though the corpus named them as a pair in every statement of the frontier, which is exactly how
one got worked for thirteen revisions while the other went unexamined.

### Neither vacuum reaches the observed amplitude

P15 established that the *substrate's* de Sitter vacuum sits at $\sim10^{-122}$ and is short by $10^{113}$,
and read the classical character of the primordial statistics off it. **But the inheritance story locates
the fluctuations in the progenitor, whose own vacuum that proposition does not address.** Carried through
the full passage — freeze on the $\beta=2$ leg, connect through equality, mix at the crunch — the
progenitor's vacuum reaches $\sim1\times10^{-112}$ and is short by $\sim10^{103}$. *(The figure is the
c54.153 one: the transfer law carries the scalar monodromy $4\pi/\rho$, and the receipt that had it at the
tensor's $2\pi/\rho$ — a factor four — was found by the receipt-vs-sentence pass and corrected.)*

*So the classical, non-vacuum character is now established for the source that actually supplies the
statistics, and not only for the one that does not.*

### No primordial $B$-modes, unconditionally

The tensor sector is the one place the transfer machinery runs with no idealisation at all. It returns

$$\mathcal{P}_T=144\pi\,(\ell_P/M)^2\rho^{-6}\simeq5\times10^{-111}$$

against an observational ceiling of $\sim7\times10^{-11}$ — **below it by a hundred orders.** The statement
no longer rests on the substrate's floor, which had the same scope defect as its scalar twin. And the
crossing multiplies the tensor-to-scalar ratio by a constant, so the observed bound measures the parent.

### The leading-order interior is adequate

Two threats, both closed. **Nonlinearity**: run the transfer chain backwards from the *observed* amplitude
and the density contrast peaks where matter domination ends, at $\sim10^{-6}$, falling to zero at the
crunch — and the peak is composition-independent. **Anisotropy**, which is the standard killer of bouncing
models: a Bianchi shear would turn the crunch into $a\propto|\sigma|^{1/2}$ with a degenerate indicial
pair — a different singular point, not a correction. *But the shear is not a free datum.* At $k=0$ the
tensor equation gives $\Sigma=a^2h'/2=$ const: **the Bianchi shear simply is the long-wavelength growing
tensor mode**, so bounding the tensor sector bounded it. Six orders of margin at the sky's ceiling,
fifty-six at the predicted amplitude.

### The progenitor's composition, derived

$$\rho\simeq5.4\times10^{-2},\qquad \left.\frac{\rho_r}{\rho_m}\right|_{\rm max}\simeq7.3\times10^{-4}$$

about $2.5\times$ the observable leg's present value. It began as an assertion — one bead with one
integration constant, plus a crossing photon–baryon plasma — and ended as a **derivation**: in spherical
collapse a small perturbation shares its background's composition, so the patch's equality is the ambient
universe's. The arithmetic closes to three figures, $1.492$ Mpc against $1.490$.

And with it, two numbers the progenitor never had: **it turns around at $z\simeq1.5$** — an ordinary
structure-formation epoch — **with a mass of $4.3\times10^{52}$ kg**, comparable to this universe's own
matter content. *Which is what "the matter of our hot dense era is that previous universe's collapsed
matter" requires, and the first time that sentence met a number.*

---

## ⌗ WHAT WAS WITHDRAWN, AND THE PATTERN IN IT

Seven bounds on one quantity. Four revisions of Floquet apparatus. Two verdicts. One correction to a
correction. Set out plainly:

| withdrawn | why |
|---|---|
| the composition bound, five successive versions | four asked where a spectral knee *sits*; the fifth assumed the incoming state was a free oscillation |
| a retraction of one of those bounds | I checked its *wording* against a retired assumption instead of recomputing it |
| the full-lap Floquet apparatus, four revisions | it composed a monodromy at the patch's $a=0$ in the patch's own harmonic basis, which nothing establishes |
| two "cosmogenesis is not a chain" verdicts, **withdrawn c54.149** | they excluded a closed-ball *cycle*; the corpus's chain is generational, and proposes no such object |
| a correction declaring the full lap unphysical | spherical collapse puts the patch's $a=0$ at the background's |

**The pattern is not that I kept making mistakes. It is that the thing being assumed kept moving upward.**

- First the **observable** was assumed — where a knee sits, rather than what curvature it leaves where the
  spectrum is measured.
- Then the **input** was assumed — a free oscillation, in a construction that specifies the incoming state.
- Then the **background** was assumed — a solution extended beyond the range the physics gives it, which is
  legitimate algebra and illegitimate history, and the extension outlived the reason for it by four
  revisions.
- And now the **recursion** is what is assumed — asserted in one sentence and never unfolded.
  ***And that is where the retreat stopped, c54.162: the recursion was unfolded, and it turned out not to
  be an assumption at all but a MALFORMED QUESTION.*** It presupposed a patch harmonic basis the
  construction never builds and a spacelike datum that never crosses. **The thing being assumed had
  climbed one level past anything the construction contains, which is why no further apparatus could
  have reached it and a reading could.**

***Each correction was real and each was reached by computing something previously taken for granted. And
each time, the unexamined thing turned out to sit one level above the last.*** That is what a sector looks
like when the tools are sound and the frame is not yet.

---

## ⌗ THE OTHER FINDING, WHICH IS ABOUT THE CORPUS AND NOT THE PHYSICS

Six separate times this arc found that **two independent indices of the same object had never been
compared**, and each comparison paid immediately:

- **A paper's frontier list against the register.** Four live open problems and cluster J's tenth germ had
  no register row at all — invisible to every gate, found only by asking each frontier item to name a lead.
- **P15's closed-$S^3$ projection against P16's crunch monodromy.** Neither paper had reason to look at the
  other, and the joint was the entire missing step of the mode map.
- **A proposition's subject against the conclusion drawn from it.** `prop:amplitude` ruled out the
  substrate's vacuum; the paragraph it supports is about the progenitor's.
- **`THE_WORK` against `PROTECTED_OPEN`.** The file that calls itself *the list* omitted all ten
  protected-open items — a two-thirds under-report of the programme, in the document written to prevent
  exactly that.
- **The enumeration of what was withdrawn against what the corpus still says — found by writing this
  document.** Cutting the ledger table above meant listing the withdrawals, and the list disagreed with the
  corpus in two places at once. `THE_WORK`'s closure table had been struck on one row of four and left three
  standing as results — including a second chain exclusion four rows below the first, on identical grounds.
  ***And P16 was still asserting the entire Floquet account in its published prose*** — phase-only above the
  first peak, the bands closed, $|\lambda|=1$ to machine precision, the chain excluded by the large-angle
  sky, and a structured low-multipole excess offered as a *prediction* — because c54.149 registered its
  withdrawal nowhere, so the gate built to catch exactly this could not see it. **All of it is struck at
  c54.151, the phrases are in the registry, and the paper now states the withdrawal with both its grounds.**
  ***The propagation range in the first case is not "across the corpus"; it is eight lines.***

- **A cited receipt against the sentence citing it.** P16 asserted the scalar monodromy $4\pi/\rho$ and cited
  the receipt that computes the tensor's $2\pi/\rho$. ***The link resolved, the file existed, the receipt ran
  and passed, and the claim had no computation behind it*** — a shape no gate can see, because `check_receipts`
  verifies that a citation resolves and not that the thing cited is the thing claimed. Building the missing
  receipt then found the closed form itself was an $A=2$ specialisation. **Run as a systematic pass over all
  twenty-eight cited receipts in the perturbation sector, fourteen matched** — and the sharpest thing it
  returned is that the dominant failure is not a wrong link but a *receipt that cannot fail*: three receipts in
  one cluster contain no assertion at all, so `OK` certifies that Python exited zero. ***That is how a claim of
  robustness — "stable under $\pm2\%$ in $r_0$" — rode inside a green receipt for two revisions; measured, the
  depths drift by $15\%$.***

**And a seventh, turned inward: the corpus's instruments go stale exactly like its prose.** `check_burndown`
aged a row by the oldest revision it cited, and had no state for work deliberately ordered behind other
work. Both were fixed; neither would have surfaced without a row that tripped them.

***A gate that has never failed is not evidence that it works.***

---

## ⌗ WHERE THIS LEAVES THE PROGRAMME

**Front #1 was no longer a calculation, and c54.162 settled it by reading — with one line of asymptotics
where a computation was genuinely owed.** ✔✔✔ ***THE RECURSION DOES NOT RUN ON MODES.*** *(i) There is no
map between the patch's closed-$S^3$ harmonics and the ambient universe's, fixed or deferred, because **no
spacelike datum crosses**: P7's correspondence is null boundary to null boundary "with no spacelike slice
entering the map", and the collapse interior is Kantowski--Sachs on $\mathbb{R}\times S^2$, carrying no
closed-$S^3$ basis at all. **That is a stronger verdict against the withdrawn apparatus than the withdrawal
itself entered** — an apparatus withdrawn for want of support can be reinstated; one whose presupposition is
empty cannot. (ii) Whether a mode was sub-patch at the previous branch point is **moot, and computably so**:
$\lvert aH\rvert\to1/x$ at the crunch while $c_s$ saturates at $1/\sqrt3$, so every mode from $\ell\simeq28$
to $\ell\simeq2475$ freezes strictly before it. (iii) **No** — frozen content carries an amplitude and no
phase, so no mode label survives for a previous monodromy to act on. ***The structure is one lap, not a
tower; the recursion is a genealogy of universes.***

⚠ **AND IT COST A PREDICTION.** P7 advertised that the crossing "can inherit perturbations from a cold
species and from no other". *A filter acting on oscillatory content has nothing to select from when nothing
arrives oscillating.* ***The crossing is lossless for every species. The selection rule is removed — a loss,
recorded as one.***

**Front #2 — the acoustic peak, $\ell_1=220$ against $150$ — was held downstream of that question, and
c54.162 releases it.** *It was merged into front #1 on the strength of reading both peak routes off the same
full-lap $\lvert\lambda(k)\rvert^2$, an apparatus now doubly withdrawn, so the merge goes with it.* **It is a
live two-route disagreement on the single collapse leg and is owed work in its own right.** It is not a
disagreement with the sky; the route that reaches 220 agrees with it.

**The rest of the programme is untouched by all of this.** The abundances, the acoustic scale met at the
directly measured $H_0$, the expansion-rate resolution, the diffusion signature, the amplitude and tensor
results, and the ten protected-open items of the matter sector. *None of them sits downstream of the
transfer's shape.*

---

## ⌗ THE LINE TO KEEP

The construction is a geometry of selection rules. Its silence about magnitudes is a property of a
one-constant theory rather than a gap awaiting work — falsifiable by exhibiting a single magnitude the
geometry forces, which five attempts have now failed to do.

***And this arc found the same silence one level down, in a sector nobody had asked: the crossing
determines how much a perturbation is multiplied, and does not determine the perturbation.***

*That is either the deepest thing the corpus knows about itself, or the sign that the question has been
posed at the wrong level. Forty revisions were not enough to tell which, and saying so is the honest
end of the arc.*
