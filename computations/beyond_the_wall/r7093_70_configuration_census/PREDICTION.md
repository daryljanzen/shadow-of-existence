# r7093 (70) — the configuration census: which model is each acoustic figure in `P15` a figure of?

*Pre-registered before the census is taken. The order is `FOR_70.md` `r7093`, Q1 and Q2. **Nothing is run through the transfer**; every artefact read is banked. No prose is edited, and no other seat's receipt is touched. The deliverable is the TABLE, not verdicts.*

## Already known before looking, stated so it does not read as found

- The banked spectra I have opened (`refit_grid185/*.npz` and `spectra/cc66_r185_verify_*.npz`) carry the keys `ls, Dl, l_A, D_M, r_s, arm`. **None of them records a switch** (`LEAFSCALES`, `STACKPERT`/`LEAFPERT`, `VISLEAF`, `ZSTART`, `KFAC`, `NK`, `LSTEP`, `LMAXL`). A configuration can therefore only be **recovered** from a launcher, a log, a README or a receipt's own environment. It is never **read** from the artefact.
- The refit grid's CR runs are launched with `ZSTART=3e7 LEAFSCALES=1` (`refit_grid185/launch.sh`). The CR base has ℓ_A = 302.889.

## Method

1. **The figures.**
   - Sections: every `P15` (`corpus/CR_cosmology.tex`) section whose content is the two-arm acoustic transfer (`sec:refit-bound` and the contrast, retention, acceptance and comb sections; the list is given in the log).
   - Figures: every number in their prose that a cited receipt computes from a two-arm transfer artefact.
2. **The artefact.** For each figure: the file the computing receipt reads. That is a banked `.npz`, a `/tmp` bank (marked **NOT IN THE REPOSITORY**), or a run the receipt launches itself with an explicit environment.
3. **The configuration**, in four grades:
   - **RECORDED-IN-ARTEFACT**: the file carries its switches.
   - **RECOVERED**: from a launcher, log or receipt in the repository, naming which.
   - **DEFAULT**: the receipt runs the instrument with the switch unset, so the code's default holds. The default is read at source.
   - **UNRECORDED**: nothing in the repository says.
4. **Q2.** Compare the refit grid's CR configuration with the reported spectrum's, switch by switch.
   - If both are banked at each configuration, the receipt's own contrast statistic is read on both. That is one number, and nothing is run.
   - If one is not banked, I say so and stop. That belongs to cc66.

## Outcomes, the one that costs another seat most first

1. **The refit grid and the reported spectrum are different models**, so figures quoted against each other cross a seam that 66 must re-point. **Predicted: yes, different.** The reported CR arm solves its onset (`ZSTART` unset), while the refit fixes it at 3e7. I predict **at least two** published figures quoted across the seam beyond 66's own "one quantity" sentence.
2. **Figures with no recorded configuration**, the number the order asks me to guess before looking. **Predicted: every figure's artefact is UNRECORDED-in-artefact**, since no `.npz` carries switches. Among them, **predicted 30–50 % UNRECORDED in the repository at all**: the `/tmp` banks and runs whose launcher is not committed. The remainder are RECOVERED.
3. **The contrast difference between the two configurations**, if both are banked. **Predicted: under 1 %**, small against the 6.4 % the data ask for. This is a guess.
