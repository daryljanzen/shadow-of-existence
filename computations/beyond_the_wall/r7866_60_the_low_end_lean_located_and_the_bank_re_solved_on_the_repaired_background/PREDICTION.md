# `r7866` (60) — REGISTRATION, on order `r7865` ①–④

**Committed and pushed before any computation of this revision exists.** Eleven arms, each a
COMPARISON with a reachable negative, and the reads already taken are DECLARED below.

The order's lead: this line's matched-count low cut cost `46.53` meV where the reference's cost
`1.03`, so the instrument's limit leans on its lowest-`ell` bandpowers about forty times harder
than the reference's, and the gap from `54.00` is most likely there.

---

## ⌗ DECLARED READS — taken BEFORE this registration

1. `tail_control.py`'s own construction, from `r7862`: the matched-count low cut drops
   `n = total // 3` bandpowers **from each block separately**, ordered by `BIN_LO`. For the
   `36`-bin leg that is **twelve per block**.
2. `cut_rescore.py`'s construction, cc66's, from `r7863`: it replaces `score_ttteee.chi2_of` and
   takes the `n_cut` **globally lowest** covered bins by `BIN_LO`, with no per-block split.
3. **Both pipelines score against the SAME `score_ttteee` bandpowers** — the same `BLOCK`,
   `BIN_LO`, `BIN_HI`, `X_DATA` and Fisher. What differs is WHICH bins each covers: the
   instrument's `mod.cmb.ok` is `555`, and cc66's `covered` is `613`.
4. cc66's recorded legs in `cuts_and_node.json`: `bot1800` removes `49` of `613` leaving `564`,
   and its `move_meV` is `0.986` on `rd_camb`; `bot1500` removes more and moves `4.236`.
5. The order's own figures, quoted in it: the reference costs `1.24` meV at `ell > 1800` and
   `8.40` at `ell > 1500`, against this line's `0.28` and `-0.94`; low end `1.03` against `46.53`.

⚠ **So one candidate is already in view before any arm runs, and it is registered as a
comparison rather than asserted:** the two low cuts are not the same SET and not even the same
CONSTRUCTION — twelve from each of three blocks against the forty-nine globally lowest. If the
blocks' `ell` grids differ, the global rule can take almost all of its bins from one block while
the per-block rule necessarily takes the lowest `TE` and `EE` bins too.

---

## Ⓐ① THE THIRTY-SIX, NAMED, AND THE TWO LOW ENDS AS SETS

- **Ⓐ①ᵃ** the thirty-six are enumerated with `BLOCK` and `[BIN_LO, BIN_HI]` for each, and the
  count per block is reported. **Reachable negative:** the enumeration does not reproduce
  `tail_control.py`'s own `dropped = 36` and `ell_lo_after` on the same mask ⇒ the naming is
  wrong and is reported as wrong.
- **Ⓐ①ᵇ** cc66's forty-nine are enumerated the same way, from its own rule on its own `covered`
  mask, and the two sets are compared: intersection, each side's exclusive part, and the per-block
  split of each. **Registered expectation, which can fail:** the two sets differ, and cc66's
  forty-nine are drawn from FEWER than three blocks. ⛔ *If cc66's forty-nine also split across
  all three blocks in similar proportion, this candidate is refuted and reported as refuted.*
- **Ⓐ①ᶜ** the fifty-eight bins cc66 covers and the instrument does not are named by block and
  `ell`, since they are the reason the two masks differ at all.

## Ⓑ② THE LEAN, LOCATED

- **Ⓑ②ᵃ** at the control, `dchi2/dSigma` per bandpower for the INSTRUMENT, taken as a finite
  difference on the banked grid at the smallest registered step, reported per block and per
  `ell` band. **Reachable negative:** the per-bin derivatives do not sum to the whole-spectrum
  `dchi2/dSigma` to `1e-6` relative ⇒ the decomposition is not a decomposition and is reported
  as failing.
- **Ⓑ②ᵇ** the same for cc66's REFERENCE, on IDENTICAL bins — the same `keep` mask, the same
  Fisher, the same `X_DATA` — so that only the spectra differ. **Reachable negative:** the
  reference's reconstructed whole-spectrum `dchi2/dSigma` does not reproduce cc66's own banked
  `dchi2` to `1.3e-2` (the bound `r7863` set for its rounded memo) ⇒ the reconstruction is not
  of cc66's object and is reported as such.
- **Ⓑ②ᶜ** the block and multipole range where the two differ most is NAMED, with the number:
  the largest absolute and the largest relative disagreement, each with its block and band.
  **Registered expectation:** the largest disagreement sits at `ell < 300` in `TE` or `EE`.
  ⛔ *If it sits in `TT`, or above `ell = 300`, the expectation is refuted and reported with the
  band it actually sits in.*
- **Ⓑ②ᵈ** the three candidates the order names are TESTED and not assumed, each as a comparison
  with a reachable negative:
  - the low-`ell` `TE`/`EE` reionisation bump against the `tau` prior — tested by whether the
    lean survives holding `tau` at the prior's centre;
  - the late ISW — tested by whether it survives on `TT` alone below the first peak;
  - the lensing-amplitude handover through the shared normalisation — tested by whether it
    survives with the amplitude FIXED rather than solved.
  **Each is registered as able to come back NO.** ⛔ *A candidate that does not account for the
  lean is reported as not accounting for it, with the residue it leaves.*
- **Ⓑ②ᵉ** and the control that keeps ② honest: the same decomposition on the HIGH end, where the
  order records that the two pipelines AGREE. **Reachable negative:** if the high-end
  decomposition shows the same size of disagreement as the low end, then the method is
  measuring a difference of pipelines and not a lean, and ② is reported as not located.

## Ⓒ③ THE BANK RE-SOLVED ON THE REPAIRED BACKGROUND

- **Ⓒ③ᵃ** the control's config records `DNEFF = +0.0293`, as the order rules, and the
  instrument's DEFAULT is unchanged. **Reachable negative:** the default moves, or a banked
  spectrum moves ⇒ reported as a violation of the ruling.
- **Ⓒ③ᵇ** the bank is re-solved with `NUFD` on and that `DNEFF`, and the new bank's recorded
  config SAYS SO — the precondition `r7864` proved absent is now present and positive.
  **Reachable negative:** the re-solved bank's config cannot distinguish itself from the old
  one ⇒ the re-solve is not receiptable and is reported as not receiptable.
- **Ⓒ③ᶜ** both limits re-read on the re-solved bank against the reference's `54.00` and
  `30.56` meV. **Registered expectation, which can fail:** the minimised limit moves TOWARDS
  `54.00` from `r7864`'s `69.97`. ⛔ *If it moves away, that is reported as the repair not
  reaching the limit, with the number.*
- **Ⓒ③ᵈ** and the registered band: the minimised limit lands within `8` meV of `54.00`.
  ⛔ *This is a band that can fail, and if it fails it is reported as failed with the criterion
  unmoved.*

## Ⓓ④ THE ARM OF RECORD

- **Ⓓ④** follows ③ and is reported only on the re-solved bank, with the bank's own config
  proving which background it was solved on.

---

## The guards this revision is exposed to

- *before two stretches are identified by a label, check how many-to-one the label is* — "the
  low end" names two different SETS here, which is what Ⓐ① exists to establish before ② reads
  anything into their costs.
- *an identification has to be checked on the loci the object itself distinguishes* — the two
  pipelines distinguish bins, so the comparison is per bin and not per cut.
- *a defence against a paper state changing has to ENUMERATE the states it may produce* — Ⓑ②ᵈ
  enumerates three candidates and admits the state where none of them accounts for the lean.
- *if an arm's number or scope can be moved by another revision landing, it is a reading and the
  claim is something else* — this line's own standing rule. Every count here is taken live from
  the instrument's own masks, and the two figures quoted from the order are DECLARED reads.
