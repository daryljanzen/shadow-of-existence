> **⌖ RETIRED r1552.** This was a figure and findings consolidation (r980) — the bead figures. Superseded by `FIGURE_THEOREM_LEDGER` and Lane 7.
> Kept as record; **do not work from it.**


# Figure & findings consolidation — the bead in three frames (drafted r980)

Purpose: hold everything this session produced so nothing is lost, propose where each figure
belongs, and lay out the open lead + the what's-left audit. This is the "sit with it" map.

---

## 1. Figure inventory (what exists, where)

**In P7 already:**
- `corpus/synthesis_figure.py` → `dS-SdS-synthesis.pdf` = **fig:dS_SdS**, the 6-panel grand plate
  (A hyperboloid two bundles · B observer chart · C the r-vs-τ̃ conjugate wings · D Nariai · E handoff · F lap flattened).
  STATE: r979 (two-bundle-correct). **Caption in P7 is STALE (describes the older r978 panels) and the bead
  direction in (A) is backwards** (reads blue-in/red-out; should be red B in / blue A out). Needs a re-bake.

**New this session, in `computations/` (not yet in any paper):**
- `build_all_frames.py` → `build_all_frames.png` — **the four bundles in three representations**:
  blue A rulings, red B rulings, grey at-rest photons, black S³ circles; drawn in (frame 1) the hyperboloid,
  (frame 2) the observer (τ,χ) chart, (frame 3) r-vs-complex-τ̃. Includes the photons CROSSING the seam.
- `lap_rounding.py` → `lap_rounding.png` — **the seam cusp and the lap that smooths it**: the real photon
  crossing has a cusp at r=0; the lap (imaginary excursion to +πα/3 and back) rounds it. Right panel shows the
  three-prong split (grey photon real / blue +πα/3 / red −πα/3). THIS is the crown-jewel new figure.
- Superseded exploration steps (keep as history): `bead_frames.py`, `frames_step.py`, `build1_frames.py`,
  `bundle_companion.py`.

**Receipts (verification scripts):**
- `bead_conjugate.py` — verifies τ̃→τ̃* conjugation and the 2πα/3 Wick period (r → e^{2πi/3}). PASSES.
- `photon_cross_test.py` — verifies the photon null geodesic crosses the seam into r<0 with signed r. PASSES.
- `bead_contour.py` — the Nariai contour / πα/3 lock (from earlier in the campaign).

---

## 2. The scientific findings (this session)

1. **Two-bundle correction (grounded, slicing_operator.tex:262–269).** The fundamental worldline
   X(τ)=e^{τ/α}A+e^{−τ/α}B is strung between the two null rulings: future generator **A (outgoing, +χ) = blue**,
   past generator **B (incoming, −χ) = red**. "The synchronous space *is* the second ruling B," so in the
   observer chart the B-ruling is the flat synchronous space (const τ) and the A-ruling is the null congruence.

2. **The conjugation (verified, bead_conjugate.py).** The two cosmic-time readings of a given signed r are
   complex conjugates: **τ̃ → τ̃\*** maps them, giving the +πα/3 wing and its −πα/3 mirror. The full imaginary
   period is **2πα/3**, and shifting τ̃ by i·(2πα/3) rotates r by exactly **e^{2πi/3}** — the three cube-root
   branches / the groupoid paper's order-three 2π/3 structure. The turnaround bound |Im τ̃| = πα/3 is exactly
   HALF that period. Pure complex analysis on r = A·sinh^{2/3}(3τ̃/2α); no quantum interpretation invoked.

3. **The photon crossing (verified, photon_cross_test.py) — a correction.** With the SIGNED areal radius
   (real and odd through 0: r>0 expansion, r<0 collapse), the photon null geodesics **cross the seam** and
   continue into the collapse side to −∞. They do not stop at the big bang. (Earlier I clipped them at the seam —
   wrong. The fix: integrate in τ̃, not χ, so the crossing is a bounded vertical tangent, not a blow-up.)

4. **The collapse (grounded, CR_framework.tex:596–606).** Because r is *globally* a function of τ̃
   (r = A·sinh^{2/3}(3τ̃/2α), τ̃ = τ+χ), every real curve — blue ruling, red ruling, photon path — projects onto
   the SAME r(τ̃) in the r-vs-τ̃ frame. The bundles are distinguished in the hyperboloid and (τ,χ) frames; in the
   r-τ̃ frame they collapse to one curve (purple, the mix) and separate only off the real axis.

5. **The lap = the cusp's analytic smoothing.** The real photon seam-crossing carries a cusp at r=0. The lap
   (the excursion into +πα/3 and back) is exactly the analytic rounding of that cusp. The three sheets the curve
   can take past the seam — real cusp (Im 0), +πα/3, −πα/3 — are the three cube-root branches of the law.

---

## 3. The open lead (the frontier this opened)

Rigorous: the three sheets past the seam are three and distinct (the cube-root branches).
**Unproven (the lead):** *which physical bundle rides which sheet* — the natural reading is photon = real cusp,
blue = +πα/3, red = −πα/3, but that identification is an interpretive step, not derived. It is the same class of
open question as:
- **The double-speed photon.** The corpus asserts the at-rest congruence *becomes* the null photon congruence
  but never addresses the rate; whether that congruence "moves at twice the null rate" is unmotivated in the
  text and parked for honest thought.
These two are the live research frontier. Related deep hooks: does the photon-crossing-the-seam continuity have
observational consequences (light literally from before the big bang)? Is the τ̃→τ̃* / 2πα/3 structure a theorem
in its own right, tying the cosmic-time conjugation to the groupoid's order-three roots?

---

## 4. Proposed placement (for decision)

- **fig:dS_SdS (6-panel plate):** stays in P7. Re-bake the A/B/C caption to the two-bundle version; fix the
  bead direction (red B in / blue A out).
- **NEW figure — the three frames + the lap split:** the deep new result. Recommend a single new figure in P7
  (companion to thm:bead): top row = the four bundles in the three representations; bottom = the lap rounding /
  three-prong split. Alternatives: P3 (SdS-slicing-curve, the rulings/seam) or the groupoid paper (the 2π/3).

---

## 5. What still needs doing (audit)

- [ ] Re-bake fig:dS_SdS caption (A/B/C) + fix bead direction; recompile P7 clean.
- [ ] Decide placement, then build & wire the new figure (three frames + lap split).
- [ ] Fold the **conjugation** result (τ̃→τ̃*, 2πα/3 Wick, e^{2πi/3}, ½-period turnaround) into P7 text — it is
      currently only in a figure caption. Cross-reference the groupoid's 2π/3 order-three.
- [ ] Fold the **photon-crossing continuity** (signed r, photons cross the seam) into the text — a real physical
      claim about continuity across the big bang.
- [ ] Log the two frontier questions (sheet-assignment; double-speed rate) in OPEN_PROBLEMS_MAP.
- [ ] Bibkey-alias hygiene still pending from the walk (JanzenCRframework/JanzenFramework; JanzenShadow).
- [ ] Recompile every touched paper; verify clean.
- [ ] Cut a work bundle (cr_work_r980.tar) once settled.
