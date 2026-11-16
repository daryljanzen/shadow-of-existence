# r7807+cc66 — PREDICTION, registered before a line of the computation exists

**Order (69, r7807), three items**, after both of r7805's recommendations were ruled in: PO-87's
clause is now scoped to **arm** spectra (the control is outside it), and the control is **re-pointed
to Planck 2018's published base-ΛCDM best fit**.

① **The 7 candidates and the 16 undecidable items, read by hand.** Per item: on the leaf rate (it
leaves), off it (re-derive or re-ground), or a control-only read (it leaves under ruling 1). Report
whole with a verdict each. When none stands, PO-87 is struck.
② **Run the control at Planck's published point** — not a stencil — and re-derive every P15 figure
resting on the control's un-refitted point: the `0.918` (abstract, `sec:refit-bound`, the explainer),
the control's four-peak row, the fourth-feature differences, and anything else my sensitivity list
named. Show the refitted `1.002` does not move. Bank it **with a `config`**.
③ The comb receipt's filename stays — ruled at r7797, nothing to do.

## Two facts about the instrument, established before the run and reportable either way

* ⛔ **The instrument carries NO neutrino mass.** It has a massless free-streaming hierarchy
  (`LN` depth, `FNU` fraction, `DNEFF` for ΔN_eff) and no `mnu` anywhere. Planck's published best fit
  assumes Σm_ν = 0.06 eV. So **the control at Planck's point in this instrument is not exactly
  Planck's model**, and the receipt will say so rather than imply a fidelity it does not have. 69's
  conditional — "if the instrument carries the 0.06 eV neutrino mass, use it, and if not, say so" —
  is answered: it does not.
* **The instrument takes `LOM` (Ω_m), not ω_c**, so Planck's point must be converted at **its own
  h = 0.6736**, not the 0.674 the corpus's rounded control used:
  `Ω_m = (0.1200 + 0.02237)/0.6736² = 0.313773`.
  ⛭ *My r7805 stencil priced `Ω_m = 0.313400` at a FIXED `H₀ = 67.40`. The real re-pointing moves
  `H₀` too (67.40 → 67.36) and `n_s` (0.965 → 0.9649), so this run is not the stencil's own
  prediction re-measured — it is a different point, and the comparison between them is a test of
  how far the stencil's scope reached.*

**The run's switches:** `ARM=lcdm LH0=67.36 LOM=0.313773 WBH2=0.02237 NS=0.9649 HIER=1 LSTEP=8
LMAXL=2000`, matching the 185-bin scoring the `0.918` is computed on, with `POLSAVE` for the
fourth-feature differences in EE and TE.

## PREDICTIONS

**① The hand read.**
* ①a **The 16 undecidable items mostly LEAVE.** They were conservative inclusions — the census
  records zero namesake load sites for them — so a hand read should find most reading either nothing
  banked or the control only. **I predict at least 11 of the 16 leave.** FALSIFIED below 11.
* ①b **Of the 7 candidates, at least 2 are control-only or leaf-rate reads in disguise**, because
  four of them ([01], [06], [15], [16]) read a *mixture* and the census flags the whole item on its
  arm-side component. FALSIFIED if fewer than 2 leave.
* ①c ⛔ **PO-87 is NOT struck this round: at least one item genuinely stands.** The two reading
  `cc66_r185_verify_cr.npz` ([28], [29]) rest on the 185-bin refit verify of the *namesake* arm,
  whose LEAFGEOM twin sits at a different refit minimum, so neither is a drop-in repoint.
  **FALSIFIED if every one of the 23 leaves or is re-grounded.**
* ①d **The banks will mostly carry no `config`**, so the verdicts come from tracing producers rather
  than from reading the bank. I predict **fewer than 5 of the 23 have a `config` key**.

**② The re-pointed control.**
* ②a **The `0.918` lands between 0.94 and 0.97.** My stencil said 0.957 at fixed `H₀`; moving `H₀`
  down by 0.04 and `n_s` by 0.0001 should not undo a 4-per-cent χ² move. FALSIFIED outside that band.
* ②b **The stencil's 0.957 is within 0.01 of the real run**, i.e. the stencil's scope reached this
  far. *Held least firmly: the stencil held `H₀` fixed, and the `0.918` is a χ² ratio, which the peak
  positions enter steeply.* FALSIFIED if they differ by more than 0.01.
* ②c **The refitted `1.002` does not move** by more than its printed last digit, because the refit
  re-minimises and the control's own 185-bin minimum already sits further from the corpus's point
  than this re-pointing moves it. FALSIFIED if it moves.
* ②d **The control's peak positions move by ~1 multipole at the fourth peak**, as the stencil said,
  so the fourth-feature differences in TT/EE/TE all move. FALSIFIED if every peak moves by less than
  its printed last digit.
* ②e **The control's χ² IMPROVES** (falls) at Planck's point. That is the whole reason the `0.918`
  rises: a better control is a harder comparison. FALSIFIED if the control's χ² gets worse.

**③ A cross-cutting prediction.** The massless-neutrino gap will matter **less than the re-pointing
itself**: I predict the control's χ² at Planck's point, in this instrument, still falls by more than
2 per cent against the corpus's rounded point, despite the instrument not modelling Σm_ν = 0.06 eV.
FALSIFIED if the fall is under 2 per cent.

## How it is run

Item ② runs the corpus's own `ACOUSTIC_two_arm.py` through an **idempotent** launcher (a finished
`.npz` is skipped), checking for a running solver by reading `/proc/*/environ` for
`ACOUSTIC_two_arm` rather than by a bare name test, at the corpus default `KFAC` 2.0. Scoring is the
refit receipts' own: P15's CAMB lensing operator on both arms, `chi2_of_spectrum.chi2_of`, 185 lensed
bins, one amplitude in closed form. The bank is written **with a `config`**, as ordered. Item ① reads
receipts and traces producers; no instrument is rewritten.
