# r7635+70 — PREDICTION (pushed before any run of the bank)

**Order (69, r7635):** bank every CR spectrum CENSUS.md §B lists, regenerated on the arm of record — `LEAFREC=1`
at H0 68.570730, Ωm 0.291246, ω_b 0.021643, n_s 1.015066 — in the form each receipt reads, under the same name
with a `_leafrec1` suffix, with a manifest giving LEAFREC and the point for each file. Push the bank before any
receipt is re-pointed. Then re-point the receipts that have no living author.

**What is banked.** The 36 distinct CR files §B names. Each keeps its recorded switches (path, ℓ range and step,
KCONT, KSLICE summing, SRCSAVE/SRCDEC/SRCETA, CRPHI, NODRIVE, ISW, CRIC, polarisation, LMAXL=3000) and changes
only the point and `LEAFREC`. Where the old file's point was not r6941's fitted one (a solved z_onset, a pinned
ℓ_A, an injected ℓ_A=340), the manifest says what was held and what moved. `SRCXS` on the arm becomes the new
distance ratio, D_M(control)/D_M(arm) = 13954.35/14133.95 = **0.987293** (was 0.995528).

**Gates on the bank itself (all must hold, or the file is not banked):**
- G1 the plain arm regenerated here (`cc66_r185_verify_cr_leafrec1`) equals r7633's `verify_cr_leafrec1.npz` bit for bit;
- G2 every `_leafrec1` file's own `config` reads `LEAFREC: true`, and each sliced file's slices tile [0, nk) with no gap;
- G3 every recorded switch appears on the run's `__SWITCHES__` line (the r6941 launcher's guard);
- G4 the r6911/r6915 decompositions close on the new arm as they did on the old (terms sum to `S` ≤1e-15; pairs to D_ℓ ≤1e-14).

**Bands on figures I can read from the bank without re-pointing anyone's receipt (p ≈ 0.7 each):**
- the arm/control acoustic contrast ratio ‖Δ‖ (1.040 on the old arm, P15 l.1122) stays above 1, in [1.02, 1.07];
- the NUFS=0 shift still agrees between arms to under 0.5 multipole at each of the first four peaks;
- the KCONT=1 continuum still reproduces the ladder to under 1% of the peak (c54.186 / r6794 / r6911 kcont);
- the fine-grid fourth-peak arm − control stays within 0.3 of r7633's LSTEP=8 refitted value +0.52 (§A).

**Reachable negative (named, per the order):** on the arm of record a figure P15 builds an argument on changes
sign or crosses its stated bound. The ones I judge nearest the edge: the collapse ratio at the adjudicated
ratio, r = 1.0231 against 1 (l.485, l.647 — the endpoint "sets its sign"); the 133-bin χ² preference 2.10
(l.921); and the contrast-excess ratio 1.040 against 1. Any of these crossing is the negative.

**The outcome that closes PO-87:** the residual on the arm of record is shown to be the control's own too
(the r6941 fine-grid and the "three quarters / four fifths of the arm's residual is the control's" family,
already 0.91 on the coarse grid in §A, carried to the fine grid).

**EFFORT.** Recipes recovered from the launchers (r6885–r6959 share one point and are clean; the c54/cc66/item38/
r4494/r6784 files are older and need their recipes reconstructed). Compute on 4 cores: the LSTEP=8 runs a few
minutes each; r6941's LSTEP=1 fine grid ~30 core-min; the L3000 runs longer. Estimate 2–4 h wall for the whole
bank, then the ownerless receipts. If an old recipe cannot be reconstructed, that file is named as unbankable
rather than guessed.
