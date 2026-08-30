---
name: po13-handoff
kind: STATE
current: r3558
class: open-problem-handoff
job: The live handoff of PO-13 — the CR acoustic-peak disagreement — for a FRESH node. States the open problem, what is already eliminated, the sharp unsolved core in the framework's own L1/L2/L3 language, the concrete first attacks, the instrument, the trap, and the CI/ledger hazards. Supersedes the buried r-records in PO13_WORKING_STATE.md.
sources: [cowork, chat]
---

# PO-13 HANDOFF — the CR acoustic-peak disagreement, UNSOLVED, for a fresh head

**Read this before touching `PO13_WORKING_STATE.md`.** That file is a 2800-line append-only log whose
revision numbers collide with main's; this document is the readable state. Written by cc54, which — with
framework node 58 — is spent on this problem and has not solved it. It is left in the clearest shape I can
give it so a fresh, willing head can attack the part that is actually open. **Nothing here is swept aside;
the honest state is that CR disagrees with the CMB acoustic sky and the mechanism is diagnosed but not cured.**

---

## 1. THE OPEN PROBLEM (model vs sky — this is the real one)

CR's **determined** acoustic comb (no free parameter in the acoustic sector) over-drives the CMB:

| observable | CR (`GSRC=1`) | sky (Planck 2018) | control (ΛCDM) |
|---|---|---|---|
| position ℓ₁/ℓ_A | 0.7825 (**+7%**) | 0.7312 | 0.7300 |
| amplitude P1/P2 | 3.665 (**+65%**) | 2.217 | 2.254 |
| positional parity, q=1–3 | 0.111 (**4×**) | 0.028 ± 0.002 | 0.029 (0.6σ) |

The control (byte-identical ΛCDM no-op) lands the sky; every CR shift is physics, not machinery. **The
tail q≥4 is NOT validated** — the control itself drifts to −17σ by peak 6 in the damping tail — so the
instrument is trusted only over q=1–3, and no claim is made beyond it.

**This is the corpus's own named-open frontier.** P15 `CR_cosmology.tex` §scope, in its maturity marking:
*"Run, and returning a disagreement rather than a confirmation: the end-to-end branch-point-to-recombination
transfer … the height pattern tracks and the phase does not. **Open**: … the diagnosis of the phase offset
the transfer exposed."* And §tensions: *"the phase was never carrying it … a disagreement with the sky that
no single quantity named in this section accounts for."* **PO-13 is that diagnosis.** It is the one open
register row (`OPEN_PROBLEMS_MAP.md`), the live end of the PO-7 → PO-10 → PO-13 scalar-sector lineage.

---

## 2. WHAT IS ALREADY ELIMINATED — do not re-run these (each closed by measurement)

The diagnosis was reached by measuring out every lever in the acoustic oscillator, CR vs control, on the
instrument. **Do not spend a fresh head re-deriving these; start from the unsolved core in §3.**

1. **R** (baryon loading) — identical by construction.
2. **Φ** (well-integral the baryons see) — CR/control 0.77–1.10, not the ~2× a driving explanation needs. Refuted.
3. **drag** (`DRAGLEAF`) — 0.82; it *fights* the suppression, wrong sign.
4. **IC amplitude** (`CRAMP=seam`) — a seam-phase amplitude swap wrecks the comb entirely.
5. **IC phase** — modes start with arrival-phase spread **0.000π** across k. Coherent at the start (this is
   the null-boundary mechanism of P15 §coherence working: one characteristic datum per mode = one phase per mode).
6. **source magnitude** (`GSRCA` α-scan, α∈[0,1]) — no single α lands the four observables; they demand
   **four disjoint α-bands ordered by scale**, and the framework supplies no non-constant weight.
7. **source time-profile** (`THRESH`) — the threshold principle reads to the two `GSRC` endpoints, not between them.
8. **the projection** — settled on **`prop:flat`**, NOT a lever. CR's fundamental-observer constant-τ slice
   is exactly flat ℝ³ (E=1 marginally-bound congruence, k=E²−1=0), so the closed S³ sets only the source
   quantization k_L=√(L(L+2))/r₀ and never enters as a distance; D_M=D_C, flat j_ℓ(k_L D_C) is the correct
   kernel. **The hyperspherical / closed-distance kernel is the wrong one for CR** (the paper says so: "the
   closed distance relation, which CR does not have"). A factor-7 "near-antipode magnification" chased over
   r3553–r3556 was retracted (r3557) as exactly that error. **The projection is not an eighth lever.**

**The terminal fact under the disagreement:** no determined CR composition lands the sky's positional parity
— `GSRC=0` → 0.007, `GSRC=1` → 0.11, sky 0.028 between, and `GSRC` is binary, not a dial. The disagreement,
and even its sign, is a property of the determined source composition, not something a free parameter absorbs.

---

## 3. THE SHARP UNSOLVED CORE (attack this)

**The measurement:** CR's modes start coherent (0.000π spread) but **drift to 0.514π by recombination**,
while the control holds **~0.2π at every scale**. The loss of cross-scale acoustic phase coherence is what
carries the +65% amplitude over-drive and the parity anomaly. The null-boundary mechanism delivers the
coherent *start*; something in the *evolution* breaks the cross-scale lock afterward.

**Where it comes from, in the framework's own language.** CR's expansion **rate** carries **no radiation
term** (P15: the rate is Λ-fixed; "radiation carries no term in it"; radiation is inherited *content* read
off the cosmic clock, with the plasma beginning at the one fitted parameter z_onset ≈ 6.8×10³). ΛCDM's
cross-scale acoustic phase lock **is** the radiation era in its rate. The perturbations in the instrument
ride the geometric (**L1**, stacking) rate — radiation-free — and that is precisely what costs the lock.
But CR's plasma *does* carry radiation as **content** (**L2**, leaf), with a real sound speed and driving.

> **THE OPEN QUESTION.** Is there a reading of CR's layered ontology (L1 geometric/stacking rate vs L2
> leaf/content rate) in which the acoustic modes' **phase clock** sees the **L2 content rate**
> (radiation-included — re-locking the modes across scale, reproducing ΛCDM's coherence) while the
> **background** rides the **L1 geometric rate** (radiation-free — preserving the control-matching
> background that lands the sky)?
>
> - **If yes:** CR recovers the acoustic sky and the +7%/+65%/4× disagreement dissolves into a two-rate
>   bookkeeping the ontology already licenses. This is the win condition.
> - **If no** — if the phase clock is *forced* to be the geometric rate — then the over-drive is the
>   **genuine CR prediction**, and CR disagrees with the CMB acoustic sky at percentage level, with a named
>   mechanism (no radiation era to lock the phase). That is a real, publishable falsification edge, not a bug.

This is the fork the whole arc points at, and it is a *physics* question about CR's ontology — the L1/L2/L3
rate rule (P15 §tensions; CR_framework §coherence-of-driving) — not an instrument knob.

### Concrete first attacks (runnable day one)
1. **Localize the dephasing in time.** Instrument the phase accumulation ∫ k c_s dη as a function of k,
   CR vs control, and find *where* in conformal time the cross-scale spread opens — at matter–radiation
   equality (z_eq = 3399, exactly half z_onset)? at z_onset? That names which epoch's rate breaks the lock.
2. **THE DECISIVE EXPERIMENT — the split-rate run.** Put the **background** on the geometric (L1) rate and
   the **phase clock / sound-horizon integral** on the content (L2) radiation-included rate. This is the
   *inverse* of the `STACKPERT` lever and **has not been run**. If it re-locks the comb onto the sky, that
   is the mechanism CR needs; if it does not, the disagreement is forced. Build it as a new knob in the
   instrument (a rate-selector for the phase integral, independent of the background rate).
3. **Confirm the drift is dynamical, not IC.** Already indicated (modes start at 0.000π), but a fresh head
   should re-read P15 §coherence's null-boundary argument against the instrument's IC to confirm the
   instrument implements one-datum-per-mode and the drift is evolution, not a seam-phase artifact.

### ★ THE TRAP — burned two prior nodes, do not repeat
**Never** take ΛCDM's C_ℓ as the high-ℓ envelope and apply CR's ~8% damping to it. §coherence disowns it:
the radiation-free rate *reshapes* the high-ℓ envelope, so multiplying one cosmology's peaks by another's
damping manufactures a spurious "decisive deficit." Compare CR to the control on **one geometry**, always.
(Full record: `THE_OPEN_PROBLEMS_LEDGER.md` family 5, r1408/r1422.)

---

## 4. THE INSTRUMENT

`computations/beyond_the_wall/ACOUSTIC_two_arm.py`. Environment-variable knobs:
- `STACKPERT=1` — perturbations on the geometric (L1) rate.
- `GSRC=0|1` / `GSRCA=α` — source constraint factor (radiation in Φ's source): off / full / continuous α.
- `HIER=1` — fluid → photon-hierarchy switch. `KCONT=1` — continuum vs discrete-ladder source.
- `CRAMP=seam` — seam-phase IC. `DRAGLEAF=1` — drag term on the leaf rate. `THRESH` — overdensity-gated source.
- `HYPER=1` — **the retracted hyperspherical projection. Do not use** (kept only so the retraction is legible).

**Discipline (non-negotiable, and the reason the results above are trustworthy):**
- Gate every CR run on the **byte-identical control no-op** first; if the control moves, the machinery is broken.
- Compare CR **to the control**, never to the sky directly.
- **Two pins or it isn't a result.** State the prediction *before* the run.
- Don't impose arbitrary rules on the physics; don't invent or fit physics to close a gap.

Analysis scripts from this arc live alongside it (`po13_*.py`) and the from-scratch χ/geometry check is
`po13_chi_antipode.py`. The projection resolution is `verify_closedS3_nonsync.py` and `prop:flat` in
`corpus/CR_cosmology.tex` §largescale.

---

## 5. A SEPARATE, SMALLER OPEN OBJECT (instrument vs instrument — not this problem)

The **low-ℓ deficit depth**: two Boltzmann arms disagree ~2× at ℓ=3,4 (arm 1: 0.47/0.41/0.36/0.68;
arm 2: 0.49/0.24/0.18/0.61 at ℓ=2–5). The corpus attributes it to late-ISW handling and D_M and marks it
**do-not-assert**. It is an *instrument* disagreement, not model-vs-sky; it sits in P15 cosmology, not in
this branch's acoustic instrument; and it needs the framework node (59), whose transfer arm 2 is. First
attack if picked up: run each arm with the other's late-ISW treatment and a matched distance. **Not PO-13's,
and not to be conflated with the phase problem above.**

---

## 6. CI / LEDGER HAZARDS the next node WILL hit

- **`fast — registers, views, IDs` is red on a PRE-EXISTING bookkeeping failure** — `classify_documents`
  (unclassified working-state docs) + `regen_grain_currency` (stale framework blocks), reproducing
  byte-identically on `main`. Not this branch's; documented in PR #22's standing comment. **Don't chase it.**
- **`check_revision_collisions` and `check_claims` are BLIND under `NODE=ci`** — the collision gate always
  checks the EVEN half; the claims roster contains neither node. They *pass by not knowing which line they
  check* — the same pathology this whole arc was about. A fix needs a branch-to-node declaration spanning
  both nodes' files; **neither node should wire it unilaterally.** (Framework/Daryl's call.)
- **The compile hole:** the compile job is gated on main-or-schedule, so a PR's LaTeX is compiled nowhere —
  a branch can go green and break the papers, and only the merge finds out. Closing it costs `texlive-full`
  on every PR push (a compute decision, Daryl's call).
- **The ⊢56 retraction should be REVERSED:** the entry exists at `FIGURE_THEOREM_LEDGER.md:489`, written
  with a space between the turnstile and the number; the retraction searched for the closed form and could
  not have found it. **59's to reverse.**

---

## 7. STATE, honestly

The elimination chain is complete; the projection is settled on `prop:flat`; the disagreement is a
percentage-level over-drive with a diagnosed mechanism (lost cross-scale phase coherence, traced to the
radiation-free rate). **It is not solved.** The win — if there is one — is the split-rate experiment in §3.2.
cc54 and 58 are done on this; it needs a fresh head that will build that knob and read the answer. The
standing result is PR #22; the buried record is `PO13_WORKING_STATE.md`; this document is the map.

---

## ⛔ WHAT THE FRAMEWORK NODE (58) GOT WRONG — *added r3559, so you know which reasoning to distrust*

*Written by 58, which is spent on this problem and did not solve it. **These are not confessions; they
are a map of a failure mode you will be tempted by**, because every one of them looks like sound
reasoning from the inside.*

**⛔ THE PATTERN, stated once:** *I reasoned from **what I had read in the code or the textbook** instead
of from **what the framework's own propositions say**, and from **patterns pointing the right way**
instead of from **numbers**. Every one was caught by cc54 **running something**, never by me thinking
harder.*

| # | what I asserted | what the measurement said |
|---|---|---|
| 1 | the projection map could move peak **heights** | it cannot \u2014 one factor is a **uniform stretch**; heights need $r_s$ and $k_D$ carried by *different* factors, which is not a map. **And I had declined that two-factor reading myself one message earlier.** |
| 2 | the `GSRC` over-drive was a **matter double-count** | ⛔ wrong \u2014 every $\Omega$ is normalised to $\rho_{\rm tot}$ while $H_c^2\propto\rho_{\rm free}$, so **matter's source is short by the same factor**. Uniform `GSRC` is the correct full-EFE source. |
| 3 | the $\ell_1/\ell_A=0.7294$ position result was **the cleanest of the arc** | it was computed on **`GSRC=0`** \u2014 the source we then agreed is wrong. On the correct source it is **0.7825, +7%**. |
| 4 | the residual **tracked the $\Phi$-decay ratio mode by mode** | the numbers say the **reverse**: $q{=}3$'s $\Phi$ decays *faster* in CR, so $P_1/P_3$ should be enhanced *more* than $P_1/P_2$ \u2014 measured, it is **+5% against +63%**. |
| 5 | on a closed $S^3$ the angular-diameter distance **must** be $r_0\sin\chi$ \u2014 *"not a convention"* | true of a closed geometry, **and CR is not one for photons**. `prop:flat` \u2014 the fundamental-observer slice is exactly flat. **I asserted a geometric necessity without checking whether CR's photons ride that geometry.** |
| 6 | the throat-vs-present radius would pull $\chi$ below $\pi/2$ | the $S^3$ areal radius is tied to $\Lambda$, **not** $a(t)$ \u2014 it grows only **1.63×**, so $\chi$ is 2.74 today and 4.47 at the throat. **The mechanism could not have worked.** |

⌗ **AND THE ONE THAT MATTERS MOST FOR YOU.** *Four separate times I proposed **stopping** \u2014 "carry it
open", "bank it", "hand it off", "leave it here" \u2014 each time a measurement came back **worse**, and each
time Daryl had to drag it back.* ⛔ ***That is not caution and it is not a verdict on the problem. Read
any "this is where it should rest" language in the record as MY exhaustion, not as evidence the problem
is unsolvable.***

**⌗ THE RULE THAT SURVIVES, and it is cc54's:** ***check the governing Proposition before running the
kernel, not after.*** *`prop:flat` was in the corpus the whole time and settled the projection question
outright; I built an entire hyperspherical hypothesis without reading it.*

⇒ ***Eight levers are eliminated by measurement and that work is sound \u2014 it is a map of where NOT to
look, not evidence that there is nowhere left. The problem is open. Attack it.***
