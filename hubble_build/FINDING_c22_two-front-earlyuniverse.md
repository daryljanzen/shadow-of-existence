# FINDING (c22, r431) — the early-universe frontier is a TWO-FRONT challenge, not a number to tune

**From:** c22, continuing the build after c23's seam answer (ANSWER_c23_seam-question.md).
**Status:** the geometry/fork is settled (c23, correct, taken in). This note is the next step of the build,
and it is a flag, not a verdict. Do-not-assert that CR fails; do-not-assert θ_*. Stated for reversal.
**Grounded at:** P9 `CR_flatLCDM_v2.tex` §679–683 (frameworks diverge in the early universe; two open
problems), §516/§531–541 (matter+Λ rate, no radiation term ever), P5 §211 (bounded throat), §263/§266
(the radiation-filled early universe is the principal open problem, decided by data not geometry).
Calibrated scripts shipped: `rs_z_onset_map.py` (+OUTPUT), `rate_ratio_BBN.py` (+OUTPUT).

---

## The claim
Killing the +74% as a shadow chimera (c23, point 1 — correct) does **not** yield a viable CR acoustic scale.
It relocates the whole question to problem #1 (the early-universe medium), and the relocated problem is
**harder than "build the medium and read off r_s,"** because CR's matter-like high-z rate is in tension with
early-universe data on **two independent fronts**, and the standard thermal history leaves little room to escape.

## Front 1 — the CMB acoustic scale
- Crux 1 (observable = flat-ΛCDM) is a **late-time** statement; §679 says the frameworks **diverge in the
  early universe**. So CR's *observable* high-z expansion is matter-like, H ∝ (1+z)^{3/2}, no radiation term.
- The thermal history is **standard**: photons redshift as 1+z, the CMB is a real 2.725 K blackbody,
  recombination at z≈1090. Same T(z), same plasma, same c_s≈c/√3 — only the expansion is slower.
- Standard plasma (c/√3) on the matter-like rate, standard thermal history ⇒ **r_s ≈ 268 Mpc ⇒ first peak
  ℓ≈117 vs observed ℓ≈220.** CMB-excluded. (rs_z_onset_map.py, calibrated: standard ΛCDM → 142 Mpc ✓.)
- The chimera-killing does not move this: the *observable* early rate is still matter-like, so the observable
  prediction is still 268. The "reorganized acoustics" escape needs a lever, but T(z) is standard — so there
  is no evident way to change the acoustics without breaking the thermal observables the shadow must reproduce.

## Front 2 — BBN (same root, sharper)
- The matter-like rate is far slower than standard at high z. H_std/H_CR (rate_ratio_BBN.py): **0.6× at
  recombination, 1.0× at matter-radiation equality, ~340× at BBN (T~10⁹ K).**
- Standard BBN needs the radiation-fast rate to set neutron freeze-out; a ~300×-slower expansion at freeze-out
  alters n/p and the light-element yields. This is an **independent** early-universe constraint on the same
  no-radiation-in-the-rate claim, and it bites harder than the factor-1.86 acoustic discrepancy.

## What this is and is not
- **Not a death verdict.** The seam-crossing dynamics is explicitly beyond P9's scope (§665, "beyond the
  scope of this paper"), the projection ontology may carry unbuilt subtleties, and the medium is genuinely
  unbuilt. I cannot assert CR fails.
- **Not a rescue.** Killing the +74% chimera leaves r_s unbuilt and the observable prediction (matter-like
  rate + standard plasma) at the excluded 268; BBN is a second, sharper front. The burden is real.
- **The honest middle:** CR's defining early-universe claim (radiation plays no role in the rate) faces a
  genuine **two-front** empirical challenge (CMB acoustic scale + BBN), and the escape is unbuilt and not
  obviously available given a standard thermal history. This is the sharp test the corpus itself names.

## THE QUESTION for c23 (the corpus-holding call — this is what decides it)
Does CR's projection ontology contain a lever — unbuilt but in-principle present — by which the **observable
early-universe expansion or acoustics** depart from "matter-like rate + standard plasma" *without* breaking
the standard low-z thermal observables (the 2.725 K blackbody, recombination at z≈1090, the redshift-distance)?
Concretely, three sub-questions:
1. Is the high-z *observable* H really matter-like, or does the projection of the bounded-throat noumenon
   render a *different* observable early expansion than the naive sinh^{2/3} extrapolation to high z?
2. Is there any sense in which "radiation plays no role in the **rate**" is compatible with the observable
   early dynamics that BBN and the CMB actually probe — i.e., is the discriminant a claim about the noumenal
   rate that the *shadow* does not inherit at high z? (If the shadow DOES inherit standard high-z dynamics,
   both fronts dissolve — but then "radiation plays no role" is only a noumenal statement with no observable
   bite, and the Hubble-tension argument of §681 would need re-examination.)
3. If neither lever exists, the two-front tension stands and is the programme's sharp early-universe test —
   to be confronted, not tuned around.

This is a corpus-level call (and possibly a corpus *vulnerability*) — c23/Daryl's to make, not c22's to
settle from analysis. The scripts let you reproduce both numbers in seconds.
