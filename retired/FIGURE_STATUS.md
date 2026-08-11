> **⌗ RETIRED r2380 under `RG-1` — A ONE-TIME VERIFICATION THAT A GATE NOW PERFORMS EVERY RUN.**
> *Opened r1333 because a node ~200 revisions earlier had left `\includegraphics{…pdf}` calls with no image
> behind them, so **P3/P15/P16/P7 hard-failed**. Its closing line is its own supersession:* ***"Now VERIFIED:
> all 17 papers compile 0 errors / 0 undefined / PDF."*** *`corpus/check_compile.py` states exactly that on
> every run, over all seventeen, and fails when it is untrue.*
>
> **⌗ AND ITS LESSON IS THE SHARPEST SENTENCE IN THIS BATCH, so it is quoted rather than summarised:**
> ***"'Compiles 0/0' had been ASSUMED corpus-wide and was FALSE for four papers."*** *That is the
> assumed-not-checked class in one line, and it is why the corpus's answer was a **gate** and not a fix — the
> same shape as every finding of the r2377–r2380 audit. The real-vs-placeholder inventory it carried is now
> `FIGURE_SWEEP` and `FIGURE_THEOREM_LEDGER`, both live.*

---

# FIGURE STATUS — real vs placeholder (opened r1333, updated r1334, Arthur)

*A node ~200 revisions ago was meant to build P3's graphs as placeholders so the papers would compile;
instead it left figure environments with real `\includegraphics{…pdf}` calls and NO image behind them,
so P3/P15/P16/P7 hard-failed. "Compiles 0/0" had been ASSUMED corpus-wide and was FALSE for four papers.
Fixed across r1333–r1334. Now VERIFIED: all 17 papers compile 0 errors / 0 undefined / PDF.*

## REAL figures — generated from the paper's own math or an existing source
- **P3** `figs/fig2_throat_circle.pdf`, `fig3_cubic_involution.pdf`, `fig4_seam.pdf`, `fig5_triple_angle.pdf`,
  `fig7_curvature.pdf` — **generated r1334 by `corpus/make_p3_figs.py`**, faithful renderings from P3's own
  formulas (captions + the r934/r548 spec): the one-sheeted hyperboloid + throat with the r₀ chord to A,B;
  the cubic 2M=r₀−r₀³ with the σ-involution (fixed 1/√3, σ(0)=1,σ(1)=0); the sin→cosh C¹ seam; the sin 3w
  triple-angle; the curvature K_G=1/α²−M/r³ with its r⋆ sign-flip. fig3 & fig5 visually verified correct.
  The generator is kept IN the bundle so they cannot drop out of the lineage again (they did, twice).
- **P3** `figs/fig6_tilted_ellipse.pdf` — `corpus/fig6_tilted_ellipse.py`.
- **P7** `dS-SdS-synthesis.pdf`; **P7** `F_triptych.pdf` — **new r1426, `corpus/F_triptych.py`**: the lap in
  position/speed/acceleration vs path length $s$, panel (a) reusing `F_flat.py`'s exact segments and style
  unchanged, (b)/(c) its analytic first and second derivatives. Accompanies `rem:twocritical`. Visually
  inspected. **P15** `fig_hubble_bao.pdf` (`hubble_build/make_hubble_figure.py`, real
  Hubble-tension numbers); **P16** `fig_schramm.pdf`, `fig_abundances.pdf` (from the pre-built pngs in
  `computations/p16_bbn/`; the generators need `pynucastro`, not installed).

## PLACEHOLDER remaining
- **NONE.** `fig_history.pdf` was the last one; generated real r1334 by `corpus/make_fig_history.py` (temperature history of the infalling matter, faithful to its caption — T_D bottleneck, turnaround peak at the M-independent infall-scale lower bound, deuterium freeze-out on the cooling leg, ~1.6 eV observable onset). Visually verified.

## NOTE
These P3 renders are Arthur's faithful reconstructions from the paper's math (the r934/r548 standing offer:
for Daryl's review/replacement if he holds different originals). Every referenced figure across all 17 papers now has a real image behind it; no placeholders remain.
