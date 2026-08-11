# r968 — P-symbol canon resolved + final coherence cleanup (everything up to references)

Continuation of r967. Daryl's instruction: *"You can decide the [P-symbol] thing... just work
everything up to the references taking as long as you need to get them done."* Standing rule: resolve
anything I honestly can myself. Only the **external references pass (AB-1)** is left for the overnight window.

## 1. The P-symbol collision — RESOLVED corpus-wide

**Decision (mine, authorized): CANON**
- `R` = the orientation / mass-reflection / A₂-diagram-automorphism parity (the orientation-reversing
  element O(5,1)\SO₀(5,1), the dS↔Schwarzschild vantage-swap, r₀↦−r₀ = 2M↦−2M), realised on spinors as `γ⁵`.
- `P` = the areal **spatial** parity r↦−r (Clifford generator γ¹γ²γ³, which anticommutes with γ⁵).
- `T` = the time reflection.

**Why this and not the reverse (P=mass-reflection):** the corpus writes **CPT / PT**, and in CPT `P` is
universally spatial parity — `P` could not name the mass-reflection without incoherence. It was also
already what boundary_paper, p0's CPT skeleton, algebroid(P12), and matter_sector's propositions used
(R=γ⁵). The reverse would have forced degrading those (physics-standard) papers. P5 even already used
`R` (=γ⁵) at §autA2 *and* `P` for the same operation elsewhere — a latent internal inconsistency the
canon repairs.

**Applied (with recompile-verify at each step):**
- **P3 (SdS-slicing-curve):** its local radius `R` (=2/√3 slicing scale; throat radius) renamed `\varrho`
  to free the letter (R_{μν} Ricci left alone); 18 mass-reflection `P`→`R`; convention footnote + header note.
- **P5 (groupoid):** 30 mass-reflection `P`→`R` (unifying with its own §autA2 R=γ⁵); footnote + header note.
  The `rem:P-dS-Schw` label was left intact (it's a label string, not a symbol).
- **p0 (geometric_core):** L884 backward-radial `P`→`R`. L649 CPT-skeleton `P` (spatial) and L665 `R`
  (mass-reflection) were already canonical.
- **matter_sector (P14):** L213 note rewritten (mass-reflection = `R`=γ⁵; spatial parity = `P`); header
  saga comment marked RESOLVED. Propositions' R=γ⁵ unchanged.
- **dynamics_paper (P11):** its one passing diagram-automorphism `P` rewritten to "(the mass-reflection
  parity R=γ⁵ of the groupoid paper)" — R is the Gowdy area there, so no bare-letter collision introduced.
- **shadow_of_existence (P6):** 9 mass-reflection `P`→`R` (eigenspace split f = R-even + R-odd); footnote.
- **Unchanged (already canonical):** boundary_paper (P=spatial, R=γ⁵), algebroid (R=γ⁵), CR_framework.

**Verified:** exhaustive corpus grep → **zero** mass-reflection `$P$` remain (every surviving `$P$` is the
spatial parity); **no** `$R$` used as spatial parity; all touched papers recompile clean.

## 2. Remaining coherence items — ALL CLOSED

- **P9 Type-D speciality ratio:** paper defines ratio = 27J²/I³, which is **1** for Type D (I³=27J²), not 4.
  Fixed range_paper `\equiv4`→`\equiv1`. Receipt: `computations/petrov_typeD/typeD_speciality_ratio.py`.
- **p0 L630:** stale "(match here, over-predict there)" → corrected two-sidedness (match on rate+abundances;
  parameter-free falsifiable acoustic-shape prediction — low-multipole a CV-limited wash, damping an open build).
- **p0 rung count:** verified already consistent at six (§unification six `\item`s incl. the constraint-algebra
  rung; abstract + body say "six"). No fix needed.
- **P7 figure + dependency matrix:** refreshed via `scripts/depmatrix.py`. All 17 rows now match the resolver
  exactly (verified by diff); fig:dependency-structure harmonised (P1 20→21, P6 7→8, P4→P5 7→8, P5→P6 2→3).
  Drift came from DESI/damping edits (P7→P15=19, P15→P16=10, P16→P15=9) and the r968 P-symbol footnotes
  (P3→P5=10, P3→P13=5, P6→P5=3) plus a few others.
- **P5 "Proposition 8" locator** and **P8 JanzenDynamics cite+bibitem** — confirmed already closed at r967.

## 3. State

All 17 papers compile clean, zero undefined references. Corpus is coherent and cohesive up to the
external references. **Only open item: the external references pass (AB-1)** — flags compiled in
`UNFINISHEDNESS_AND_COHERENCE_r967.md §4`, for the overnight/contained window.

Backups of the 5 originally-scoped papers before the P-symbol rename: `_backup_r968_psymbol/`.
