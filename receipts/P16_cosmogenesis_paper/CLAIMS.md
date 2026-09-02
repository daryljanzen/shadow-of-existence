# P16 — cosmogenesis_paper — CLAIMS inventory & eleven-avenue worksheet

## Whole-read digest (r1399)
The BBN / cosmogenesis paper: the cosmic beginning as a previous universe's collapse through the finite-curvature
degenerate (kappa=0) Nariai seam, re-expanding as ours; the light-element abundances as a FOSSIL of that collapse.
Two halves: (A) the synthesis spine -- the Big Bang as a deductively FORCED conjunction of 8 corpus results (each a
cited theorem, not a posit); (B) the quantitative edge -- a genuine BBN network on the cooling leg.
Maturity marks: established / argued / open. Thesis: the abundance pattern is PRODUCED, not fitted.
- **sec:synthesis** -- 8-link deductive chain (each cites its home paper): (1) foliation measured [P4, redshift isotropy <3e-6], (2) augmentation necessary+sufficient [P7], (3) collapse becomes a universe, any symmetry [P7 central thm; P1], (4) completion = Nariai kappa=0 seam, a foliation-preserving reassignment [P11,P5,P8,P9,boundary], (5) rate = geometric stacking flat-LCDM sinh^{2/3} [P10,cosmology], (6) matter inherited = corollary [P8], (7) discrete matter sector, (8) acoustic peaks follow.
- **sec:lap** -- the collapse lap as fossil (what is to be computed).
- **sec:rate** -- window rate = standard Friedmann: H^2=(8piG/3)rho+Lambda/3 -> |H|=sqrt(8piG rho_r/3) at BBN densities; contracting layer has SAME |H| as expanding at same rho; rate a reaction competes against is IDENTICAL to standard BBN. [cooling_leg_reduction.py]
- **sec:scoping** -- two rate-objects (window/leaf-level L2 radiation-included vs cosmological/foliation-level L1 geometric stacking); scoping = what the reassignment IS, not an assumption. Quantitative: seam factor [(rho_m+rho_r)/rho_m]^{1/2}=sqrt3 at rho_r/rho_m~2; FATAL checks -- stacking law in window ~300x below standard at T_D (H0 sqrt(Om)(T_D/T0)^{3/2} vs 1.66 sqrt(g*) T_D^2/M_Pl); local law past seam re-manufactures Hubble tension. L3 = E=1 projection. Outward: recombination diffusion L1 -> ~15% rate / ~9% diffusion (= cosmology paper's damping signature).
- **sec:trev** -- freeze-out is time-reversal violating: lives only on the cooling leg.
- **sec:peak** -- adiabatic (optical depth ~1e20, T ~ rho^{1/3}); rho_hor=3c^6/32piG^3M^2 is a FLOOR not peak; infall KE ~ rest mass/nucleon (GM/R_s c^2=1/2 at horizon) -> T_pk~170 MeV (QCD scale) >> T_D~0.07 MeV, M-INDEPENDENT -> freeze-out exists for every progenitor. [peak_temperature.py] Exact regulated peak open, downstream-irrelevant.
- **sec:network** -- genuine multi-nuclide network on cooling leg at eta_10=6.14: Y_p=0.247 (obs 0.245), D/H=2.51e-5 (obs 2.53e-5), He3/H=1.05e-5, Li7/H=5.1e-10 (obs 1.6e-10); two libraries (StarLib/REACLIB, D/H 2% spread); Y_p Born 0.243 -> 0.247 (+1.6% rad/Coulomb); d ln(D/H)/d ln eta=-1.6; lithium valley recovered; baryon number conserved. [bbn_network.py, Yp_freezeout.py, validate_bbn.py]
- **sec:verdict** -- joint confrontation at Planck eta_10=6.13+/-0.04: D at -0.5sigma, He-4 at +0.5sigma (Cooke2018 DLA, Aver2021 He), Li-7 at 6-8sigma (lithium problem). [theory_error_and_likelihood.py, fig:schramm] Reckoning on theory-choice axis (requires vs permits, P6). Two successes + one shared problem, from the collapse.

## AVENUE 11 -- receipt inventory (computations/p16_bbn/, ALL to trace+run+verify+WIRE; P16 currently UNWIRED)
| # | claim | script | status |
|---|-------|--------|--------|
| 1 | peak temperature floor T_pk~174 MeV, M-independent, >> T_D | `peak_temperature.py` (CITED) | ✔✔ |
| 2 | window rate = standard Friedmann rate + fatal checks + adiabatic + metals | `cooling_leg_reduction.py` | ✔✔ |
| 3 | multi-nuclide abundances at eta_10=6.14 (Y_p, D/H, He3, Li7) | `bbn_network.py` (via gate) | ✔✔ |
| 4 | helium-4 freeze-out Y_p | `Yp_freezeout.py` | ✔✔ |
| 5 | validation vs standard BBN (d ln D/H/d ln eta=-1.6, valley) | `validate_bbn.py` | ✔✔ |
| 6 | theory error + likelihood (D -0.5sig, He4 +0.5sig, Li 6-8sig) | `theory_error_and_likelihood.py` | ✔✔ |
| 7 | scoping FATAL check (~300x stacking-law-in-window) | IN cooling_leg_reduction (294x) | ✔✔ |
| - | figures | make_abundance/schramm/sensitivity.py | (figure gen, not receipts) |

## AVENUES 1-10 -- first-pass observations (off the whole-read; to execute)
- A1 Q-mine: disciplined (established/argued/open). Scan the "produced not fitted" / "empirically favoured"-style claims for standing.
- A2 own accomplishments: BBN network as a genuine computation (not correspondence); freeze-out-exists-for-every-progenitor as an established result; the synthesis spine as a forced deduction. Check nothing undersold.
- A3 press the gap: honest edges (exact regulated peak open; inherited-datum derivation open; last-percent precision open; lithium NOT dissolved). Check no overclaim in "produced not fitted" given the argued peak floor.
- A4 identity: title = cosmogenesis synthesis + the light-element fossil. Confirm at weight.
- A5 positive-face: leads on the forced synthesis + produced abundances; inflation/hot-phase contrast as requires-vs-permits.
- A6 symmetry: collapse leg vs expanding leg (time-reverse at equal density); the two rate-objects kept apart; check no conjugate/leg dropped.
- A7 bespoke two-way: forward -- requires-vs-permits hot phase is a P6 instance (cited). backward -- P6 world-vs-description on the inherited eta / progenitor spectrum opens.
- A8 dissolution census: dissolves -- non-spherical collapse (P7 causal thm), the r=0 singularity/wall (seam=passage), the seam decoupling-mechanism question, coincidence (via cosmology). lithium NOT dissolved (honest). Census at weight.
- A9 checklist: the 3-4 opens flagged; unification recap (spine into P7/corpus); the two-datum idiom (eta vs rho_r/rho_m) consistent with P15.
- A10 forward-refs: dense (P1,P2,P3,P4,P5,P7,P8,P9,P10,P11,boundary,cosmology,P6 + external Planck/Cooke/Aver/Cyburt/Sallaska/Borsanyi/Silk). Check completeness.

## STATUS r1403: P16 FULLY SWEPT (avenue 11 + avenues 1-10). See below.
## (r1402) AVENUE 11 COMPLETE for P16. All 6 receipts ✔✔ (peak_temperature, cooling_leg_reduction[+scoping fatal], bbn_network/validate_bbn, Yp_freezeout, theory_error_and_likelihood). Every .py mention cited; 0/0/13pp checker green. Data confrontation D -0.5s / He-4 +0.5s / Li +7.8s reproduced. NEXT: avenues 1-10 on P16 off the whole-read.

## AVENUES 1-10 -- EXECUTED r1403 (off the whole-read, at source). VERDICT: all ten pass; one computation built (below).
- **A1 Q-mine -- PASS.** Disciplined (established/argued/open). Hedges have standing ("stated without being claimed", "may remain measured boundary data at no cost", "the one miss"). Nothing to strip.
- **A2 own accomplishments -- PASS.** The network "debt paid" and "produces now stands earned at the criterion of necessity"; the synthesis "bar met in full"; He-4 "computed from first principles". Claimed at weight, nothing undersold -- the paper owns running the network that discharged its open debt.
- **A3 press the gap -- PASS.** "Produces" scoped precisely: earned for the synthesis + He-4 (computed) + the joint network pattern (debt paid); the DERIVATION of eta explicitly "a frontier the title does not stake itself on". "Empirically favoured" is a JOINT (P16 abundances even + P15 Hubble discriminating) claim, correctly attributed to the companion -- on the light elements alone the paper says "neither better nor worse than LCDM". Lithium honestly the one miss. No overclaim.
- **A4 identity -- PASS.** Title = the Big Bang a deductively forced synthesis + the abundances it produces; delivered, and explicitly audited ("the title, held honestly and fairly").
- **A5 positive-face -- PASS.** Requires-vs-permits hot phase ("what LCDM supplies as an initial hot phase, CR supplies as the far side of a collapse it already had"); leads on the forced synthesis + produced pattern.
- **A6 symmetry -- PASS (emphatic).** Both legs carried (contracting=expanding at equal rho, same |H|), the T-violating asymmetry correctly located at freeze-out (cooling-leg only, sec:trev); the conjugate r<0 branch carried as the ANTIMATTER progenitor (R-conjugation, the C=(Q->-Q).(R.K) seat, sec:lap). No leg/conjugate dropped. [The sec:trev "Boltzmann two-species toy confirms" was an unreceipted computation -> BUILT P16_freezeout_trev_toy.py, verified, cited.]
- **A7 bespoke two-way -- PASS.** Forward: requires-vs-permits hot phase is a P6 instance (cited). Backward: P6's requirement-vs-permission applied to separate "a debt to pay" (the network, discharged) from "a horizon honest to leave open" (the eta derivation) -- "the criterion that tells them apart ... is the same one the reckoning turns on".
- **A8 dissolution census -- PASS (at weight).** Non-spherical collapse (P7 causal thm, "dissolved not a separate case"); r=0 singularity/wall (seam a passage, P1/P2/P3/P8); the seam decoupling-mechanism question ("dissolves rather than answers: radiation never sourced the cosmological rate"); coincidence (via cosmology). Lithium NOT dissolved (honest).
- **A9 checklist -- PASS.** Opens flagged (exact regulated peak, eta derivation, last-percent precision); the spine IS the unification recap (8 links into the corpus); two-datum idiom (eta vs rho_r/rho_m) consistent with P15.
- **A10 forward-refs -- PASS.** Extremely dense; each spine link cites its home paper (P1-P12, boundary, cosmology, P6) + external (Planck/Cooke/Aver/Sbordone/Cyburt/Sallaska/Borsanyi/Silk). Bibliography complete.

## P16 FULLY SWEPT (r1403): avenue 11 (6 receipts incl. the genuine BBN network, every computation run) + avenues 1-10 (all pass). The avenue-6 read surfaced one unreceipted computation (the sec:trev freeze-out toy) -> built + verified + cited, so the sweep also tightened coverage.
