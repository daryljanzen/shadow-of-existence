> **⌖ RETIRED r1552.** This was a cleanup checklist (r551) — *close EVERYWHERE*. Spent.
> Kept as record; **do not work from it.**


# Cleanup checklist — r551 (close EVERYWHERE, verify each)

## Thread A — excise the "reassigned substrate" taxonomy error
Canonical (algebroid P12): substrate = dS₅ (4-geometries are *cuts* via **slicing**);
**reassignment** "holds one background geometry fixed and involutes the causal roles of the
generating null ruling." So: reassignment acts on a *de Sitter background* (held fixed), NOT the
substrate; dS₅ substrate is never reassigned. Correct substrate usages ("the de Sitter substrate
*determines/fixes* the structure") are KEPT.

- [x] A1. P13 title (l.59): "from a reassigned de~Sitter substrate" → "from causal reassignment on a de~Sitter background"
- [x] A2. P13 subsection (l.95): "The reassigned substrate and the Nariai member" → "The causal reassignment and the Nariai member"
- [x] A3. P13 abstract (l.70): "from a single de~Sitter substrate by a causal reassignment" → "by a causal reassignment on a de~Sitter background"
- [x] A4. P13 intro (l.77): same conflation → same fix
- [x] A5. VERIFY corpus-wide: zero "reassigned … substrate" and zero "substrate (by|via) … causal reassignment"; correct "substrate determines" usages intact

## Thread B — P13 stops presenting as "the scalar perturbations paper"; it IS the cosmology paper
Parallel to P7 (CR_framework / JanzenCRframework). JanzenCRcosmology is now free (P7's old key).

- [x] B1. Rename file scalar_perturbations_paper.tex → CR_cosmology.tex
- [x] B2. Rename cite key JanzenScalar → JanzenCRcosmology corpus-wide (cites + bibitems; CR_framework 11×, dynamics 2×)
- [x] B3. Standardize P13 bibitem TITLE → its current cosmology title (CR_framework l.843, dynamics l.209; both stale "What the seam transmits…")
- [x] B4. Fix prose labels for P13: "scalar(-perturbation) paper" / "companion scalar paper" → "cosmology paper" (CR_framework)
- [x] B5. Update LIVE meta-docs filename/identity refs (README spine, KICKOFF_GATE, KICKOFF_CODA_REVIEW, CORPUS_MAP); leave dated historical docs verbatim
- [x] B6. VERIFY: zero JanzenScalar remnants; file renamed; no live "scalar perturbations paper" as P13's identity

## Close-out
- [x] Recompile all 14 papers (0 undefined refs/cites)
- [x] Re-bundle r551; prepend changelog; mark every box above [x]

**CLOSED r551** — both threads verified corpus-wide; all 14 papers compile 0 undefined; live layer propagated; history left verbatim.
