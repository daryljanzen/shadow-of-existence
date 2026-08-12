# _dig/findings_batch2 — the second batch

*Continues `_dig/findings/` (F01–F11, already handed off). Same discipline: nothing here is a
closure, every item states what it does not claim, every recommendation is stated for reversal.*

**This batch works the eight papers batch 1 left unread at source: P02, P05, P06, P11, P12, P13,
P14, P17.**

| # | one line | kind | artefact | verified at source? |
|---|---|---|---|---|
| **F12** | P12's isotropy-3 stratum labelled "Bianchi" is **six of the nine** types; and *"the isotropy dimensions are the Killing-vector counts"* is general only under K9's criterion, which P12 does not cite here. Plus a one-line closure of `K8`'s {6,7,10} enumeration (no u-type involution on odd signature) | offered + bounded negative on one sentence | `F12_the_bianchi_stratum_is_six_of_nine.md` + `DRAFT_P12_the_bianchi_stratum_is_six_of_nine.py` (rc=0) | yes — F05's computation re-run, not quoted |
| **F13** | so(6,ℂ) has **four** real forms, not two, and su(3) embeds in exactly one — the compact one. So `sec:face-status`'s opening concession (*"nothing in the group theory privileges one"*) gives away more than it needs; the ontological argument that follows is untouched | offered (sharpens one sentence's setup) | `F13_su3_fits_exactly_one_real_form.md` + `DRAFT_P13_su3_fits_exactly_one_real_form.py` (rc=0) | yes — su(3)⊂so(6) built explicitly; the other three forms ruled out by maximal-compact dimension + the rep-dimension floor |
| **F14** | P14's leaf-compactness claim — what carries the generation index where P13's bulk index is obstructed — is receipted at M = 0.62 M_N (three simple roots) and **diverges logarithmically at the Nariai member**, where the horizon root is double. Finite on the whole open family, infinite at its endpoint, and the endpoint **is the seam**. The paper does not name its member | bounded negative (scope of a stated hypothesis) + a question | `F14_the_leaf_is_compact_except_at_the_seam.md` + `DRAFT_P14_the_leaf_is_compact_except_at_the_seam.py` (rc=0) | yes — receipt's 1.7671 reproduced exactly; divergence rate α/√3 per e-fold confirmed against the log law |
| **F15** | the **scope table** — what parameter values each receipt actually runs at, the half nothing in the suite asks. First yield: P15's receipt layer carries **two internally consistent parameter sets** (Ω_m 0.307/z_rec 1100 for the C-chain; 0.3066/1089.9 for the integrator group), differing by **0.76 % in r_s and 0.72 % in θ_\***, and the paper draws on both | instrument + bounded negative | `F15_the_scope_table_and_two_parameter_sets.md` + `DRAFT_receipt_scope_table.py` (rc=0, ~1 s) | yes — one code path, swapping only the set |
| **F16** | P11 `sec:strata` already says substrate isotropy and geometric isometry part company **at the wall alone**. F05's open question is exactly whether that holds — and it now has a sharp form: Bianchi II's abelian G₂ is orthogonally transitive but **unpolarized** (g_xy = −z a², no constant basis change removes it), so it sits one step beyond the polarized Gowdy–dS class P11 builds | offered (sharpens F05/F12) | `F16_where_the_two_notions_part_company.md` + `DRAFT_P11_where_the_two_notions_part_company.py` (rc=0) | yes — symbolic, three Killing vectors + orthogonal transitivity + the polarization obstruction, with a control |

## Why this batch exists separately

Batch 1 went out as `CR_DIG_BUNDLE.py` while this session kept working. Keeping them apart means
the second handoff is additive and the committing node never has to diff two versions of the same
file.

## Where batch 2 is going

The named gap is the **matter sector** — P13, P14, and the boundary/algebroid pair — where the
corpus's own live conceptual debt has collected (`L-136` is where two struck items converged). F12 and F13 are the first two steps in — F12 came out of reading P12 `sec:strata` and noticing
that a batch-1 result lands there too; F13 out of P13 `sec:face-status`, where the paper concedes
a symmetry the group theory does not actually have.

**Still unread at source: P02, P05, P06, P17.**

## The batch-2 pattern, so far

Batch 1's pattern was *connective tissue drifts, computations hold*. Batch 2 is turning up a
second one: **a claim verified at one point of a family, stated as if it held on the family.**

- F12 — a stratum labelled "Bianchi", true of six of the nine types.
- F13 — a concession about "two real forms", where there are four and only one takes su(3).
- F14 — leaf compactness receipted at 0.62 M_N and stated unqualified, where the member that
  matters most is the one it fails at.

In each case the corpus's own material contains the correction (K9 for F12; `P13_qm_S4_vs_S5` for
F13; `P14_leaf_compactness`'s own control for F14) — the gap is that nothing compares the scope of
a receipt against the scope of the sentence citing it.

**F15 is that gap, made into an instrument.** `DRAFT_receipt_scope_table.py` reports what parameter
values each receipt runs at; the reading against the citing sentence stays a reading, but it becomes
cheap. Its first run found the two parameter sets in P15 that F11 had caught only one seam of.

## One arc runs through this batch

F05 (batch 1) → F12 → F16 are one thread, and it closes on a single cheap question:

**F05** three of the nine Bianchi algebras are not in so(4,1), so they cannot be the sweep — but a
G₂ sub-sweep might still reach them. *Open.*
**F12** so the isotropy-3 stratum is six of nine, and P12's *"isotropy dimensions are the
Killing-vector counts"* is general only under K9's criterion.
**F16** P11 already names the phenomenon — geometric isometry exceeding substrate isotropy — and
localises it to **the wall alone**. And Bianchi II's G₂ is orthogonally transitive but
**unpolarized**, so it sits one step beyond the polarized Gowdy–dS class P11 builds.

⇒ **Is the orthogonally-transitive unpolarized G₂ class in the range?** One class, one counting
argument at k = 2, and it settles a sentence in each of P11 and P12 and closes F05.

## Probed and left alone — recorded because "nothing here" is a result

The corpus's own discipline says a negative is worth writing down. These were worked at source and
returned nothing:

- **P05 `prop:deck` / `rem:galois`.** Checked the Galois claim: for r³ − r + 2M, Δ = 4 − 27(2M)²
  (correct), not a square in ℂ(2M), and the cubic is irreducible there (if it had a root in ℂ(M)
  then M would be a degree-3 polynomial in r, forcing degree 1). So Gal = S₃ — **right**. And
  `rem:monodromy-group` already flags that the generation claim *"rests on the two Nariai
  monodromies transposing different pairs of sheets, which is a computation"* and does it.
- **P06 `lem:vindication`.** I went in expecting the batch-2 shape — a universal lemma supported by
  one arc. **§boundary gets there first, and harder than I would have:** *"a reliability estimate
  built only from successes is **survivorship, not measurement**."* It names counter-instances
  (ether, caloric, Kepler's solids), names a third class the reference class would miss (the
  criterion applied *and disregarded* — Einstein's 1931 λ-term paper, with Eddington's objection),
  restates the lemma as a falsifiable base-rate differential, and says *"The outcome is not presumed
  here."* **Nothing to add.**
- **P02 `cor:Kretschmann_at_z0`.** The counterfactual (*"had the chart labelled the horizon critical
  point r = 0, K would diverge there"*) reads oddly for a scalar, whose value at a point is
  label-independent. But it is a claim about **which function is taken to be the areal radius** —
  r ↦ 2M − r exchanges the two critical values of r(z) — and `rem:divergence_tracks_label` states
  the invariance worry explicitly and defers the ontology to `sec:ontology`. Defensible as written.
- **P16 `sec:peak`.** Checked the M-independent peak: for E = 1 infall, KE/m = M/r = ½ at r = R_s,
  giving 469 MeV/nucleon — correct. My worry (comoving dust has no relative velocity to thermalise)
  is answered in the paper's own sentence: *"its thermalization is not a further assumption but what
  the convergence **is**: worldlines arriving metrically coincident cannot remain cold coherent
  dust."*
- **L-146's strike** (batch 1's dig). I suspected it retired r2241's control worry with an argument
  about a different correction. It does not: the exact/WKB transmission ratio **is** the direct
  measure of how badly the adiabatic approximation fails, so answering an O(1) parameter estimate
  with a 4 % computed value is the right move, not a substitution.

Five findings and five clean probes is the honest ratio for this batch.
