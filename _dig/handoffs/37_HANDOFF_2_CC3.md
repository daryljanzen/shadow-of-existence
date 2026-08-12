# Handoff #2 — one new finding (CC-3) + a CC-1 reinforcement

**Repo:** https://github.com/daryljanzen/shadow-of-existence · **base:** `f7e0362` (r2429)
**Relation to prior handoffs:** additive. CC-2 (four empty bibitems) is unchanged and still the one clean commit.
CC-1 stays withdrawn (see §B below — now *dissolved*, not merely withdrawn). This document adds **CC-3**.
Produced after completing the full primary corpus P1–P16 plus the p0/P17 geometric core.

---

## A. CC-3 — P12 §weyl-a3 is stranded after the bibliography (structural; AUTHOR-CONFIRM, do not auto-apply)

**File:** `corpus/algebroid_paper.tex` (P12). **What:** a full numbered results section,
`\section{The discrete structure is the substrate's own Weyl group}\label{sec:weyl-a3}`, is placed **after** the
bibliography and the receipts appendix. Document order:

```
§scope (L275)
\begin{thebibliography} … \end{thebibliography}   (ends L311)
\input{appendix_receipts_P12}                       (L314)
\section{… Weyl group …}\label{sec:weyl-a3}         (L317)   ← renders AFTER references + appendix
\end{document}                                       (L344)
```

**Why it's a real anomaly (facts, all reproducible):**
- It is the **only** `\section` placed after an `\end{thebibliography}` anywhere in the corpus (35 files). It
  compiles (single `\end{document}` at L344), so nothing is *dropped* — it just renders in the wrong place: a
  numbered results section appearing after the References and the receipts appendix.
- It is **load-bearing**, not a stray note: receipt-tagged (`\rcpt{GROUP_full_order48}`,
  `\rcpt{EMBEDDING_is_Td_equals_WA3}`) and its result (D₆ enlarges to W(A₃)=T_d, order 24/48) is relied on by
  **P13** (`boundary_paper.tex:303`) and **P14** (`matter_sector_paper.tex:160`).
- The same result is already **summarized in the body** at `algebroid_paper.tex:175`, so §weyl-a3 is a *fuller
  treatment that was appended and never moved back into the body* — the natural reading of how it ended up here.

**Proposed fix:** relocate the whole block (lines 317–342, the section through just before `\end{document}`) to
**before** `\begin{thebibliography}` — natural home is right after §discrete (L266) or §scope (L275). No text
needs changing; it's a cut-and-paste of the block to earlier in the file.

**Confidence:** medium-high that it's unintended (a numbered section after references is nonstandard and unique in
the corpus). **But placement is an authorial choice** — it *could* be an intentional post-appendix addendum.
So: surface and propose the relocation; **confirm with the author before committing.** Not a mechanical certainty
like CC-2.

**Reproduce the anomaly scan:**
```bash
# the only section after a bibliography, corpus-wide:
for f in corpus/*.tex; do awk '/\\end\{thebibliography\}/{b=1} b&&/\\section\{/{print FILENAME": "$0} /\\end\{document\}/{b=0}' "$f"; done
```

---

## B. CC-1 reinforcement — now *dissolved*, not just withdrawn (still: do NOT edit those sites)

The p0/P17 geometric core (`geometric_core_paper.tex` §landing, ~L1231) states the finite/infinite-curvature
duality as **doctrine**, not defect: "P1's finite-curvature species and the conjugate infinite-curvature species
are one object; and the curvature divergence at $r=0$ is the curvature of the **perspectival** metric, **real** as
that metric's … built-and-real, not an artefact." So r=0 is genuinely infinite-curvature on the perspectival
(vantage-dependent) reading **and** finite on the substrate — both real, by the shadow-reading doctrine. This
means even the two "optional clarity" items from the prior CC-1 correction (P7 §two-boundaries "genuine
infinite-curvature"; the :1398 Nariai-member phrasing) are **defensible as written**. Net: **CC-1 requires no
action of any kind.** Treat it as closed, not open.

---

## C. Everything else verified clean (negative results, corpus-wide)
No undefined `\cite` keys; no duplicate `\label`s; no broken `\ref/\eqref`; no content after `\end{document}`; no
missing `\input` appendix targets; cross-paper "the wall" references all disambiguated (P11 renamed its own to
`prop:radiative-wall`). The corpus is mechanically pristine apart from CC-2 (fix) and CC-3 (relocate, confirm).

**Bottom line for the incorporating node:** commit **CC-2**; raise **CC-3** to the author as a relocation to
approve; **CC-1 is closed**.
