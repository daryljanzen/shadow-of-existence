# Bundle r989 — bead-arc audit + the one contained fix (the sheet-assignment de-assertion)

Closes the c39 bead arc (r973→r988) with a source-level audit. One error found, isolated, fixed;
everything else verified sound. Full record: `retired/gate_notes_bead_audit.md`; changelog: CORPUS_MAP r989.

## Verified sound (kept): thm:bead (contour re-run), first fact (conjugate pair), second fact
(photon crosses seam, re-run), lem:twoturnings (math re-derived — the honest deflation of the
groupoid↔bead bridge), P5 (no node-added lemma; prop:autA2 bead touch correct), and the r976
deep-bake into the 16 companions (spot-checked P16, p0 — only the sound closed-bead propagated).

## The one error (contained to P7 + one receipt), fixed:
the "two null bundles A, B take the ±πα/3 wings" bijection collapsed the DOUBLE ruling of the
one-sheeted hyperboloid (A, B are two distinct null rulings — verified orthogonal at the waist —
not one bundle under a sign; the wings are the τ̃↔τ̄̃ conjugate pair of ONE continuation).
De-asserted in: P7 thm:bead third fact, §frontiers item, panel-(D) caption; `sheet_assignment.py`
step [3] withdrawn (steps [1][2] kept); figure legend + docstring corrected and figure regenerated;
`JanzenGroupoid` cite on the e^{2πi/3} period dropped. P7 recompiles clean (latexmk, 39pp, 0 undefined).
Working records (ANTIMATTER_FRONT_PLAN, WP_C3) flagged with the r989 correction.

## Held open (the real next work): (1) the sheet↔ruling assignment — the honest panel-D question;
(2) the antimatter naming — do-not-assert, unworked both sides.

Bundle excludes only regenerable compiled PDFs and build cruft.
