# LEDGER KEY REGISTRY — the knowledge ledgers a paper may cite with `\\ldg{}`
> ⌗ **THIS IS NOT A DIRECTORY INDEX AND IS DELIBERATELY NOT NAMED ONE.** *The ledgers it keys are
> **top-level documents**, listed by the corpus's own `INDEX.md` like every other; this file is the
> `\\ldg{}` rail's key table, and it lives beside `ledgers.sty` and `make_ledger_appendix.py` because it is
> part of that machinery.* ⚠ *It was first written as `ledgers/INDEX.md` — a directory holding nothing but
> an index, for documents stored elsewhere, **duplicating a listing the root index already carries for all
> thirty-seven of them**. Moved r3551. The root index's own frontmatter records why that shape is
> dangerous here: at r2385 a 49 KB live document was deleted because a 32 KB stub shared its name in
> `retired/`.*

*Source of truth for `\\ldg{}` and Appendix L. One row per citable ledger; the description is the
ledger's own frontmatter, so it cannot drift from the file. `make_ledger_appendix.py` reads this and
REFUSES to emit a row whose file is absent, and FAILS on a duplicate key — the two ways the receipt
generator lost rows silently before it was hardened.*

> **⌗ WHAT IS AND IS NOT IN HERE.** *These are the **knowledge** ledgers — the field bakes and the
> figure-theorem bake — the artefacts a paper can rest a claim on. The **operating-layer** ledgers
> (closure, model, open-problems, consolidation, document, jargon, phase-7 build) are not citable
> from a paper and are deliberately absent. `PHYSICAL_VALUES_LEDGER.md` is not here **yet**: it
> becomes a row when the corpus cites it, which is its own open item.*

> **⌗ THE ROW SET IS NOT FIXED AT EIGHTEEN.** *Six further fields are queued (integrable systems,
> differential topology / index theory, information theory, number theory, numerical analysis,
> probability). Nothing that reads this file may assume its length.*

| key | ledger file | kind | what it is |
|-----|-------------|------|------------|
| `algebraic_geometry` | `ALGEBRAIC_GEOMETRY_LEDGER.md` | field bake | The algebraic-geometry field-bake ledger — what bit, what bounced, and the boundary. One of the three fields listed but never thrown (the overnight order: algebraic geometry ×57, discriminant ×28 / genus ×21). `OWED` 622 |
| `cartan_holonomy` | `CARTAN_HOLONOMY_LEDGER.md` | field bake | The Cartan / connections-and-holonomy field-bake ledger — what bit, what bounced, and the boundary. First of the four fields `L-272`'s re-survey left outstanding. `OWED` 622 |
| `catastrophe_singularity` | `CATASTROPHE_SINGULARITY_LEDGER.md` | field bake | The catastrophe / singularity-theory field-bake ledger — what bit, what bounced, and the boundary. One of the three fields listed but never thrown (the overnight order named it explicitly: catastrophe ×54). `OWED` 622 |
| `category_theory` | `CATEGORY_THEORY_LEDGER.md` | field bake | category theory against CR — the corpus's largest unlisted field |
| `combinatorics` | `COMBINATORICS_LEDGER.md` | field bake | The combinatorics field-bake ledger — what bit, what did not, and why. Lane 8 |
| `complex_analysis` | `COMPLEX_ANALYSIS_LEDGER.md` | field bake | complex analysis and monodromy against CR — the field that turned practices into theorems |
| `conformal_geometry` | `CONFORMAL_GEOMETRY_LEDGER.md` | field bake | conformal / Möbius geometry against the substrate — the field that refused, and why |
| `convexity_optimisation` | `CONVEXITY_OPTIMISATION_LEDGER.md` | field bake | The convexity / optimisation field-bake ledger — what bit, what bounced, and the boundary. One of the three fields listed but never thrown (the overnight order: convexity ×143, constraint ×141). `OWED` 622 |
| `functional_analysis` | `FUNCTIONAL_ANALYSIS_LEDGER.md` | field bake | The functional-analysis / unitarity field-bake ledger — the field that bounced, and the one routing fact it returned. Third of the four fields `L-272`'s re-survey left outstanding. `OWED` 622 |
| `harmonic_analysis` | `HARMONIC_ANALYSIS_LEDGER.md` | field bake | The harmonic-analysis field-bake ledger — what bit, what bounced, and the boundary. Second of the four fields `L-272`'s re-survey left outstanding. `OWED` 622 |
| `involution_real_forms` | `INVOLUTION_REAL_FORMS_LEDGER.md` | field bake | The involution / real-forms field-bake ledger — what bit, what bounced, and the boundary. The field `L-277`'s unclaimed-surface probe named, and the first bake not drawn from a pre-existing list. `OWED` 622 |
| `optics_lensing` | `OPTICS_LENSING_LEDGER.md` | field bake | observational optics and lensing against CR — confirmations, and the dimension clause they forced |
| `quadric_geometry` | `QUADRIC_GEOMETRY_LEDGER.md` | field bake | projective geometry of quadrics against the CR substrate — the CK metric identification, and the ladder gap it exposes |
| `representation_theory` | `REPRESENTATION_THEORY_LEDGER.md` | field bake | The representation-theory field bake — what bit, what bounced, and the boundary. The largest unbaked vocabulary in the corpus (×241 tight), thrown after the Phase 4 survey named it the standing first pick on measured usage |
| `spectral_theory` | `SPECTRAL_THEORY_LEDGER.md` | field bake | The spectral-theory field bake — what bit, what bounced, and the boundary. Tier B's largest never-thrown field (×189 on the reach measure), verified as NOT covered by the harmonic ledger, which mentions spectral, self-adjoint and deficiency zero times |
| `statistics_inference` | `STATISTICS_INFERENCE_LEDGER.md` | field bake | The statistics/inference field-bake ledger — what bit, what bounced, and why. The last unbaked field in `THE_MATHEMATICS_REACH`'s candidate set, and the one `A5.5` needs. `OWED` 622 |
| `variational` | `VARIATIONAL_LEDGER.md` | field bake | variational / action against CR — the field the corpus uses and never names |
| `figure_theorem` | `FIGURE_THEOREM_LEDGER.md` | theorem bake | The figure–theorem ledger: which classical theorem each figure carries, and its receipts |
