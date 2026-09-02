# Node 4 — the first telescope image (tensor/graviton sector). r444, c23 with Daryl.
> **⌖ RETIRED r1535 — verified landed.** This was the first telescope image, tensor/graviton sector (r459). **Landed:** the graviton sector is in P11 (×13) — ghost-free to all orders, the reduced energy positive-definite.
> Kept as record; **do not work from it.** Its numbering and era predate the current corpus.



## The crux is answered (the field exists, P10 built it)
"Does the bounded throat admit a coherent field with phase across the aperture?" — YES, and it
was already in the corpus. P10 (canonical_time §lock, eq:tt-action / eq:lock-schrodinger): a TT
perturbation on the bounded throat a(T)=alpha cosh(T/alpha) decomposes into the tensor harmonics
of the closed S^3, h_ij = sum_n phi_n(T) Y^(n)_ij, discrete eigenvalues mu_n^2 = n(n+2)-2, n>=2;
each mode a unitary Schrodinger oscillator; "the closed topology enters as the DISCRETENESS of
the tower." The projection to the observer frame is built too (§172: discrete index -> continuous
wavenumber). State at the seam = de Sitter horizon Hartle-Hawking, T=hbar/2pi alpha k_B. So the
telescope's prerequisite (a coherent, phase-carrying field on the aperture, with a projection to
the sky) is PROVEN for the tensor sector.

## The first image (computed, alpha=1 units)
Evolved each mode  phi'' + 3 tanh(T) phi' + mu_n^2 sech^2(T) phi = 0  (the eq:tt-action EOM on
a=cosh T), oscillator ground-state (adiabatic-vacuum) IC at the throat T=0, to late time; frozen
super-horizon amplitude -> dimensionless tensor power Delta^2(n) ~ mu_n^3 |phi_n|^2. Figure:
`/mnt/user-data/outputs/CR_telescope_first_image_tensor.png`.

RESULT (the shape the aperture forms):
1. **Scale-invariant plateau at high n.** std/mean over n>=20 is 0.001 — flat. The bounded throat
   RECOVERS the de Sitter scale-invariant tensor spectrum at small scales. (Mechanism verified:
   the tower freezes correctly; this is the sanity check that the field-on-throat reproduces known
   physics where it must.)
2. **Low-n (large-scale) suppression.** Delta^2(n=2)/plateau ~ 0.90, n=3 ~ 0.99, returning to the
   plateau by n~5 — the largest-scale modes, which cross the horizon nearest the throat (where the
   dynamics depart from pure de Sitter), are suppressed. The AMPLITUDE (~10% at n=2) is
   IC-dependent (sensitive to the throat state choice); the EXISTENCE of low-n suppression is the
   robust, IC-independent feature.
3. **Intrinsic large-scale cutoff.** The lowest mode is n=2 (mu=sqrt6); the closed S^3 admits NO
   wavelength larger than the throat, so there is NO mode below it — a hard large-scale cutoff,
   not a suppression. This is the closed-topology signature with no analogue in a flat continuum.
4. **Discreteness.** The spectrum is a comb (n integer), not a continuum — the bounded aperture's
   own fingerprint.

## Closed-topology signatures (the tensor-sector predictions)
Discreteness + low-n suppression + a hard large-scale cutoff at n=2. These are FORM predictions
keyed to the aperture (the throat S^3 of radius alpha), the diffraction-figure character.

## DO-NOT-ASSERT (held)
- The observed CMB has a known low-ell anomaly (quadrupole/large-scale deficit). The bounded
  throat predicts low-ell suppression + a cutoff. This is SUGGESTIVE and is NOT asserted to
  explain the anomaly. Held for honest comparison once the full angular projection is done.
- No number is steered toward any observed value.

## Scope / what remains (honest)
- This is the **tensor (graviton / primordial-GW / B-mode) sector** — NOT the scalar acoustic
  peaks. The famous ell_1~=220 is SCALAR (density), which needs the scalar analogue of the tower
  = problem #1 (does a density mode ring on the bounded throat). The graviton tower is the
  template; same machinery, scalar sector.
- This is the **primordial spectrum P(n)** (the source). The full angular C_ell needs the
  projection n -> ell (hyperspherical Bessel functions on the closed S^3) and the transfer to last
  scattering in the observer frame (§172). Next refinement; the primordial shape above is its skeleton.

## What this establishes
The telescope is real and assembling: a coherent field lives on the aperture (P10, proven), it
freezes into a definite spectrum whose form is keyed to alpha, and that form carries unambiguous
closed-topology signatures (discreteness, low-ell suppression, a hard large-scale cutoff). The
first image is the tensor sky; the scalar acoustic sky is the next sector (problem #1).

## Second image — the angular projection (r445). PARTIAL: cap rigorous, peak walked back.
Projecting the primordial tower to the observer sky via the closed-S^3 hyperspherical Bessel
functions Phi^beta_ell(chi) (P10 §172 is the projection step). Status:
- **RIGOROUS (the cap):** Phi^beta_ell ∝ sin^ell(chi) C^{ell+1}_{beta-1-ell}(cos chi) is nonzero
  iff ell <= beta-1 (Gegenbauer degree >= 0; verified beta=3->ell<=2, 5->ell<=4, 10->ell<=9,
  normalization-independent). So the discrete tower projects to a discrete, CAPPED set of angular
  contributions; the lowest modes are confined to the lowest multipoles; the lowest tensor mode
  n=2 reaches only the bottom of the ell range, with no mode below it.
- **RESULT (signatures survive):** the closed-topology character is PRESERVED under projection --
  discreteness, a hard largest-scale floor (lowest mode), and the primordial low-n suppression all
  carry into the observable, concentrated at LOW ell. A flat continuum cannot produce a discrete,
  floored, low-ell-concentrated spectrum; the bounded throat does and the projection keeps it. The
  signature is observable in KIND.
- **WALKED BACK (do not re-inherit):** the peak-location computation (where each mode's power peaks
  in ell, and the tidy "ell_cutoff ~ sqrt6 sin chi_* ~ 2, on the quadrupole") used the scalar
  kernel WITHOUT the proper ell-dependent hyperspherical-Bessel normalization, which distorts the
  ell-weighting that sets the peak. Those numbers are UNRELIABLE and are NOT a result. The clean
  "cutoff at ell=2 = the observed deficit" is NOT established -- it is exactly the too-good number
  the discipline ejects. Flagged, not presented.
- **REFINEMENTS for the precise C_ell (the honest next target):** (1) proper hyperspherical-Bessel
  normalization; (2) the tensor spin-2 kernel (scalar used as projection geometry only); (3) chi_*
  = comoving distance to last scattering = problem #2; (4) the tensor transfer. The location and
  amplitude of the low-ell feature are gated on these -- chiefly chi_* (problem #2).
- **DO-NOT-ASSERT:** the low-ell deficit resonance is suggestive and held, harder now since the
  tempting number was the unreliable part. Tensor sector, not the scalar anomaly sector.

## chi_* — the comoving angle to last scattering, bounded (r446)
The background bounded throat a(T)=alpha cosh(T/alpha) fixes the conformal structure exactly.
Comoving angle from the beginning (throat, T=0): chi(T)=2 arctan(e^{T/alpha})-pi/2 (Gudermannian).
- **HARD BOUND (established):** total throat -> infinite future = pi/2 EXACTLY (int_0^inf sech = pi/2).
  A photon from the beginning reaches comoving angle pi/2 (the S^3 equator), NEVER the antipode
  (chi=pi); the de Sitter cosmological horizon sits at chi=pi/2. So the whole observable universe
  is chi_* <= pi/2 -- at most a quarter-turn of the S^3 is ever in view.
- **Seam=recombination candidate:** last scattering at the throat -> chi_* ~ pi/2 (maximal, at the horizon).
- **Problem #2 quantified (its teeth):** naive observable map D_M/alpha = 13935/5379 = 2.591 rad
  EXCEEDS the ontological max pi/2=1.571. The observable distance overshoots the available comoving
  angle -> the observable-to-S^3 map is NOT the naive ratio; the reassignment (matter sinh^2/3 <->
  background cosh) compresses 2.59 naive rad into (0,pi/2]. That compression IS problem #2, now a
  specific quantified remap (overshoot factor ~1.65) rather than a vague gap.
- **Cutoff consequence:** the lowest mode (n=2, nothing below it) projects within chi_*<=pi/2 to
  LOW ell (large angular scales), geometrically guaranteed. The exact ell_cutoff is NOT given here:
  it turns on O(1) factors (ell~1 below the observable floor vs ell~2 the quadrupole) that require
  the PROPERLY-NORMALIZED hyperspherical-Bessel projection -- deliberately not hand-waved after the
  r445 normalization walk-back. chi_* now bounded/bracketed; the proper projection at this chi_* is
  the next computation.
- **DO-NOT-ASSERT:** chi_*~pi/2 is a candidate; no cutoff multipole asserted.

## Proper projection — the low-ell signature is MILD, not a cutoff (r447). Hard-cutoff overclaim RETRACTED.
Fixed the hyperspherical-Bessel recursion (downward from the cap ell=beta-1, normalized to exact
Phi^beta_0=sin(beta chi)/(beta sin chi)); VERIFIED against the flat limit Phi^beta_ell -> j_ell(beta chi)
(ratios 0.999 at ell=2,5 in the relevant ell<~beta*chi regime); weight w(beta)=1/beta (degeneracy
beta^2 x scale-invariant 1/beta^3) gives the flat SW plateau. Closed-universe scalar SW C_ell:
- **RESULT:** a MILD low-ell suppression, concentrated at the quadrupole, GROWING with chi_*:
  ell(ell+1)C_ell / plateau at ell=2 is ~0.98 (chi_*=0.5), ~0.93 (chi_*=1.0), ~0.91 (chi_*=pi/2,
  seam=recombination). So ~7-10% quadrupole deficit at maximal chi_*, deepest when last scattering
  is nearest the seam. (Precision limited: a spurious ell=15 recursion artifact; read only the
  robust low-ell trend. Scalar geometry, not the tensor spin-2 kernel.)
- **RETRACTION (the r444/r445 "hard large-scale cutoff" overclaim, walked down):** the PRIMORDIAL
  spectrum has a genuine hard floor (no mode below n=2). But PROJECTED to the observable C_ell that
  floor becomes a MILD SUPPRESSION, NOT a cutoff: the cap ell<=beta-1 limits how HIGH each mode
  reaches, not how low, so low ell is fed from above by all higher modes (beta=3,4,5,... all feed
  ell=2) and never goes to zero. The observable signature of the bounded throat is a gentle low-ell
  deficit of order ~10%, chi_*-dependent -- not a wall. "Hard cutoff in the observable" was too
  strong; corrected.
- **What stands:** a low-ell deficit IS a genuine prediction of the bounded throat -- right sign,
  right location (largest scales), growing with chi_* (problem #2). What does not: the dramatic
  cutoff framing.
- **DO-NOT-ASSERT (reinforced):** the observed quadrupole deficit is (a) scalar not tensor, (b)
  cosmic-variance-limited/debated in magnitude, (c) met here only at qualitative precision. The ~10%
  is a computed tendency, not a claimed match.

## The scalar sector and the make-or-break peak crux (r448)
Grounded P11's scalar perturbation: linearizing on de Sitter gives the massless Mukhanov equation
W''+(k^2-2/t^2)W=0 -- a healthy scale-invariant scalar. So the scalar ENVELOPE mirrors the tensor:
scale-invariant plateau + the SAME closed-topology low-ell deficit, now in the OBSERVABLE
(temperature) sector where the quadrupole anomaly lives. That transfers.
THE PEAK CRUX (sharply posed, not claimed both ways):
- Acoustic peaks (ell_1~220) are coherent oscillations of a PRESSURE-supported medium ringing at
  c_s, caught mid-oscillation at last scattering. CR's matter is the BEND -- projected density,
  rho_eff ~ a^-3, Omega_m "a clock reading" (P7 §541; P5 §531-541), NO radiation era ever (status
  doc). Dust is pressureless: c_s=0. A pressureless medium has NO acoustic oscillations. So CR's
  NATIVE content produces NO standard acoustic peaks -- the ringing medium is simply absent.
- The observed peaks are robust data. So CR must do one of: (a) a plasma INSTANTIATES (problem #1;
  strained -- CR has no radiation era), or (b) REORGANISED acoustics -- peak structure from the
  APERTURE (bounded throat), not a plasma sound-horizon integral = the telescope.
- THE TELESCOPE IS ELEVATED: from optional reframing to the LEADING (near-necessary) candidate for
  how CR makes acoustic structure AT ALL, since the plasma mechanism is grounded-out absent.
- THE HARD PART (from the first image): the frozen tower projects to a SMOOTH envelope (modes
  freeze super-horizon, don't oscillate at last scattering) -- discreteness alone gives NO peaks.
  Peaks need coherent oscillation in k. So "reorganised acoustics" must produce oscillatory
  k-structure from the aperture BEYOND mode-freezing -- a mechanism genuinely unbuilt and non-obvious.
- STATUS: the scalar low-ell deficit transfers to the observable sector (real). The acoustic peaks
  are the sharply-posed make-or-break frontier -- gated on whether CR has a peak MECHANISM at all
  (its matter can't ring), not on a hard calculation. Neither failure nor success: the open question
  the whole CMB correspondence rests on. DO-NOT-ASSERT both directions.

## The telescope is LITERAL (not metaphor): aperture diffraction + the sqrt3 = c/c_s conjecture (r449)
Correction to my own reading: Daryl intended the telescope LITERALLY -- a finite aperture (the seam)
producing a genuine Airy-type diffraction pattern, read from two geometries (dS4 background where the
aperture sits, and the matter frame reassigned from it). This DISSOLVES the r448 "peak crux": the peaks
were never acoustic oscillations of a medium (so "CR's matter can't ring" is IRRELEVANT to them) --
they are INTERFERENCE FRINGES of a finite aperture. No medium, no sound speed needed; aperture +
coherent field. r448's crux was an artifact of my metaphor-reading, not CR's.
- **The sqrt3, verified exactly (sympy):** Nariai seam (matter/SdS frame) areal radius alpha/sqrt3,
  area 4 pi alpha^2/3; de Sitter throat/horizon (background frame) alpha, area 4 pi alpha^2. Ratio
  sqrt3 (radius) / 3 (area) -- exact, from the double-root algebra f=f'=0 -> r=alpha/sqrt3.
- **c_s <-> c conjecture (grounded both ends, DO-NOT-ASSERT the identity):** radiation c_s=c/sqrt3 ->
  c/c_s=sqrt3; the seam's two-frame areal-radius ratio = sqrt3; c_s^2/c^2 = 1/3 = the seam 2-sphere's
  two-frame AREA ratio. The radiation w=1/3 and the seam's factor-3 rescaling are the SAME 1/3 IF
  identified. Shape: "sound at c/sqrt3" = light at c read through the reassignment's seam rescaling.
  Established: two exact sqrt3's coincide. Not established: the mechanism identifying them.
- **Diffraction -- encouraging + the hurdle:** Airy rings sit at the J1 zeros (3.83,7.02,10.17,...),
  ROUGHLY EQUALLY SPACED -- qualitatively the observed acoustic-peak series (Delta ell ~ 300). A finite
  aperture naturally gives evenly-spaced rings (not yet a discriminator: harmonic acoustic peaks are too).
  HURDLE: rings need a sharp edge OR a propagating wave with a wavelength. The closed S^3 seam has no
  edge, and the FROZEN tower projects SMOOTH (no rings). So the rings must come from the LIGHT-FRAME
  PROPAGATING null field diffracting through the seam aperture (alpha, background frame), THEN read into
  the matter frame via sqrt3 -- consistent with "the telescope sits in the dS4 background, calling to us."
- **The live computation (set up, not yet run):** propagating null field, seam aperture alpha, hyperspherical
  (not flat-disk) diffraction kernel, then sqrt3 into the matter frame; ring spacing -> peak spacing,
  the sqrt3 -> c_s. THE CRUX CHOICE: what wavelength the diffracting field carries (the naive photon
  wavelength gives absurd scales; the field/perturbation wavelength is cosmological) -- to settle next
  WITH Daryl before computing, not dash (two rushed numbers already walked back this session).
- **Figure asset corrected:** the BLACK-ring legend now states the throat alpha (background) vs merged
  horizon alpha/sqrt3 (matter) two-frame reading instead of the conflated "areal radius alpha."

---

## r450 — the wavelength settled, the aperture is TEMPORAL not spatial, c_s consistency

The "crux choice — what wavelength the field carries — to settle with Daryl before
computing" (flagged at the close of the r449 entry) is now settled, in three steps.

### 1. The wavelength DEMARCATES (not one free guess)
- **GEOMETRIC (in hand):** every clean throat scale is ~alpha (aperture, lowest hyperspherical
  mode, de Sitter thermal wavelength 2 pi alpha). lambda ~ alpha => the diffraction first ring
  sits at ell ~ k alpha ~ O(few): the LOW-ell envelope / deficit regime. The geometry cleanly
  suggests the low-ell scale, AND the SPEED c_s = c/sqrt3 (the seam two-frame sqrt3).
- **EXTERNAL (recombination):** the acoustic PEAK scale ell_1 ~ 220 needs lambda ~ 2 pi alpha/220
  ~ 154 Mpc ~ the sound horizon r_s; the factor alpha/r_s ~ 35 is NOT geometric (only Planckian
  large numbers are). It tracks z_rec ~ 1090 (atomic physics) = problems #1/#2.
- **VERDICT:** the geometry fixes the low-ell end and the speed (c_s=c/sqrt3); the peak SCALE
  imports the one non-geometric epoch (recombination). Not arbitrary, not geometric -- recombination.

### 2. The flat-disk Airy FAILS at the kernel level -> the aperture is not spatial
Simplest realization (uniform circular aperture): bright rings (C_ell maxima) at the J2 zeros
x_n = [5.14, 8.42, 11.62, 14.80, 17.96]. Spacings -> pi (equally spaced -- the right KIND of
structure, GOOD). But first-ring/spacing = 1.60 and ratios x_n/x_1 = [1,1.64,2.26,2.88,3.5],
vs OBSERVED ell_n = [220,540,810,1120,1430], ratios [1,2.45,3.68,5.09,6.5], first-peak/spacing
= 0.73. The Airy puts the first peak too HIGH relative to the spacing; the ratio pattern is wrong
at the KERNEL level (not tuning-fixable). => the peaks are NOT the rings of a spatial aperture.

### 3. The aperture is TEMPORAL -- and this resolves the r448 crux PROPERLY (no medium)
The field propagates from the seam over a finite conformal time to recombination; the FRINGES
are cos(k c_s eta_rec). cos(k c_s eta) is just the PHASE of a field propagating at speed c_s --
it needs NO ringing plasma; ANY field with a propagation speed shows it. CR's c_s is NOT a
medium's sound speed: it is light (c, the null green bundle) READ THROUGH the seam's sqrt3
rescaling, c_s = c/sqrt3. So the peaks ARE interference fringes (literal-telescope), of LIGHT
rescaled by the seam geometry, not oscillations of a medium. r448's "CR's dust can't ring" is
now fully irrelevant: the fringes were never the dust's.

### 4. Consistency: the PARAMETER-FREE geometric c_s = c/sqrt3 lands the acoustic SCALE
With c_s = c/sqrt3 (baryon-free radiation sound speed, here from PURE GEOMETRY -- no radiation
era), eta_rec ~ 281 Mpc and D_M ~ 13900 Mpc (standard ballparks):
  r_s = eta_rec/sqrt3 ~ 162 Mpc;  ell_A = pi D_M / r_s ~ 269.
With the real r_s = 147 (baryon loading lowers it): ell_A ~ 297 ~ observed (~301). The sqrt3 is
in the right place to ~10%, the residual being the known baryon loading. c_s = c/sqrt3 is
PRECISELY the w=1/3 radiation sound speed; CR gets it from the seam with no plasma. That is the
prize, and it is numerically consistent.

**DO-NOT-ASSERT a precise fit.** eta_rec and D_M here are standard-LCDM ballparks. The honest CR
numbers need: CR's sinh^(2/3) conformal time eta_rec (internal, computable), the reassignment
remap D_M (problem #2, the 2.59 -> <=pi/2 compression), and z_rec (external, atomic). Consistency
is shown; the precise CR ell_A is NOT yet computed. The NEXT real step is the CR eta_rec + D_M
(problem #2) + z_rec assembly -- the full CR acoustic-scale computation, the standing frontier.

---

## r451 — the full CR acoustic scale, done straight, REPRODUCES THE CHIMERA (and shows why)

Ran the full assembly: ell_A = pi D_M / r_s, with c_s = c/sqrt3 (geometric), D_M and r_s on
CR's matter+Lambda rate H(z)=H0 sqrt(Om(1+z)^3 + OL) -- NO radiation term (CR's defining claim) --
z_rec = 1089.8 (external). Standard-LCDM cross-check through the same integrator first: r_s=144,
ell_A=302 (validates the machinery).

**CR result: r_s = 277 Mpc, ell_A = 158, ell_1 ~ 0.74 ell_A ~ 117.**

**This is the disavowed chimera, reproduced.** r432/r443 quarantined exactly "r_s ~ 268 / ell ~ 117."
The tell is mechanical: with no radiation era H ~ (1+z)^1.5, so the sound-horizon integrand falls
only as (1+z)^-1.5 -- a SLOW tail. 71% of r_s comes from z>2 z_rec, 45% from z>5 z_rec (a < a_rec/5),
22% from z>20 z_rec -- DEEP in the a->0 region P5 §211 disavows (real geometry never below the throat
alpha; the integral-to-a->0 STRETCHES the bounded throat = the +74% balloon, r431/r433). Standard r_s
is robust ONLY because radiation (H ~ (1+z)^2) kills that tail fast; CR has no radiation, so the naive
matter-frame integral runs straight into the shadow the corpus already forbids.

**r450 CORRECTION (owned).** r450's "c_s=c/sqrt3 lands ell_A to ~10%" borrowed the RADIATION-ERA
conformal time eta_rec ~ 280 Mpc -- the thing CR claims does not exist. CR's own no-radiation
conformal time seam->rec is ~480 Mpc (1.7x larger), and that factor is the ENTIRE 269 -> 158 gap.
The consistency was the borrow, not CR. r450 did flag eta_rec as a standard ballpark and held
not claimed (so it was not asserted), but the headline was too warm; corrected here.

**What survives cleanly (unaffected -- they do not depend on the borrowed eta):**
- c_s = c/sqrt3 as the seam two-frame sqrt3 (the geometric speed);
- the TEMPORAL-fringe mechanism: peaks are light's interference fringes rescaled by the seam sqrt3,
  no ringing medium (r450 step 3; resolves r448);
- D_M ~ 13935 Mpc (z<z_rec, radiation negligible, robust).

**Where the clean answer lives (problem #2, pointing the right way).** The honest conformal time is
the BACKGROUND bounded throat (a_bg = alpha cosh, never below alpha), NOT the matter-frame a->0.
The bounded throat has NO a->0 blowup -> SHORTER conformal time -> SMALLER r_s -> LARGER ell_A,
lifting back up from 158 toward ~300. The direction is forced by the SAME §211 that kills the tail.
The exact value is the seam->recombination remap on the bounded throat = problem #2, genuinely unbuilt.

**Status: 158 is the SHADOW-frame FLOOR on ell_A; the bounded throat (problem #2) is what lifts it,**
**and we now know that lift is the whole remaining job.** Not a CR failure (the lift is required and
goes the right way), not a success (no clean 300 until problem #2 is built). DO-NOT-ASSERT both ways.
The next real computation is the background-frame bounded-throat conformal time seam->recombination
(problem #2) -- the one piece that converts 158 into a CR number.

---

## r452 — grounded at source: P9 §687 names this exactly; the answer is BRACKETED and ACHIEVABLE

Before building further, grounded the blocker at source. **P9 §687 already names it precisely:**
r_s "remains uncomputed, blocked on two unbuilt pieces" -- (i) the early-universe MEDIUM and its
sound speed c_s (unconstructed); (ii) the cosmological BEGINNING and the INTEGRATION LIMITS --
where the seam sits relative to recombination, and "whether a pre-recombination sound-travel
integral exists on this side at all," unconstructed. And §687 states outright that "any theta_*
obtained by retaining the standard sound-travel integral while removing only radiation from the
rate is a HYBRID belonging to neither framework." **That is exactly r451 (r_s=277): the named
hybrid. The corpus called it in advance.** The c_s = c/sqrt3 conjecture (r449) is the proposed
answer to (i); (ii) is the live blocker.

**§661 sharpens (ii):** the matter worldlines (areal radius = the sinh^(2/3) law) and the PHOTON
congruence (the at-rest closed-slicing geodesics, areal radius R = alpha cosh(T/alpha)) are
DIFFERENT families on the de Sitter hyperboloid. So the integration limits live in the relation
between the matter time (sinh^(2/3)) and the background time (cosh) -- the crux of (ii).

**The answer is BRACKETED, and the target sits inside the bracket:**
- TARGET (what CR must deliver for ell_A ~ 301): r_s = pi D_M/ell_A = 145 Mpc, i.e. comoving
  eta_seam->rec = sqrt3 * r_s = 252 Mpc.
- UPPER bracket (rigorous ceiling) = the matter-frame a->0 chimera, r_s = 277 Mpc (eta = 480) --
  the MAXIMUM, since it includes the full disavowed a->0 stretch (P5 §211).
- LOWER bracket = the bounded throat with a naive time-identification pushes recombination toward
  the seam (no a->0 blowup), r_s -> small (the "seam ~ recombination" limit, §687's "whether a
  pre-rec integral exists at all").
- => 0 < TARGET 145 < CEILING 277. The target is INSIDE the bracket: ACHIEVABLE. The bounded-throat
  correction must supply a ~1.91x reduction in eta (480 -> 252 Mpc) -- exactly the removal of the
  a->0 shadow stretch, the right sign and size.

**The one remaining construction, now fully specified (no longer vague):** build the
matter-time (sinh^(2/3)) <-> background-time (cosh) relation on the bounded throat (§661's two
families on the hyperboloid); the matter redshift z_rec = 1090 then fixes where recombination sits
on the throat; that gives eta_seam->rec, hence r_s, hence ell_A. This is §687(ii). Target eta ~ 252
Mpc, ceiling 480, the reduction = de-shadowing. DO-NOT-ASSERT until built. Next computation: the
tau~(matter) <-> T(background) relation from the P9 §498/§531 sinh^(2/3) law and the §436 cosh law.

---

## r453 — BUILT the tau~<->T construction: it is two-faced, the seam regularizes, and §687(ii) sharpens to "does a sound horizon exist at all"

Built the seam->recombination conformal time two ways from source (P9 §498 metric, §531 clock,
§436/P3 cosh background).

**Reading A (synchronous, standard flat-LCDM redshift-distance framework).** D_M = 2.59 alpha =
13935 Mpc is the ROBUST observable (§498 reproduces the redshift-distance relation). But
r_s = INT c_s dt/a to the lower limit DIVERGES into a->0 -- the chimera, r_s = 277, ell_A = 158.
Fails because the lower limit (the seam) runs into the shadow §211 forbids.

**Reading B (the actual NON-synchronous §498 metric, ds^2 = -dtau^2 + (d_chi r)^2 dchi^2 + r^2 dOmega^2,
tau~ = tau + chi).** Here the seam->rec comoving integral dchi = dtau~/(sqrt3 r' + 1) CONVERGES:
r' -> inf at the seam KILLS the integrand, so the a->0 divergence is GONE -- the bounded throat
regularizes it, as intended. BUT the corpus clock (Omega_m/Omega_L = csch^2 s, §531) places
recombination at s_rec ~ 4e-5, i.e. essentially AT the seam (chi_sound ~ 5e-7), giving an enormous
ell_A; and this metric's comoving coordinate is not the observable (chi_LSS = 0.367 != D_M = 2.59),
so its number is exploratory, not a clean observable.

**The two framings BRACKET the target concretely: 158 < 301 < enormous** -- confirming r452.
Neither is correct: A diverges at the seam; B regularizes but puts recombination ~at the seam and
sits in the wrong coordinate. The positive finding: the bounded throat DOES regularize the
divergence (B), so the chimera is a synchronous-gauge artifact, not a real infinity.

**The crux sharpens to exactly §687(ii):** "whether a pre-recombination sound-travel integral
exists on this side at all, is unconstructed." Reading B's verdict -- recombination sits
essentially at the seam -- is the concrete form of that doubt: if there is no pre-recombination
this-side history, there is NO sound horizon to integrate, and the peak scale cannot come from
r_s at all. It would then come from the SEAM/APERTURE structure directly -- looping straight back
to node 4's literal telescope: the peaks as the aperture's diffraction figure, not a sound horizon.

**Honest state.** Established: (1) the bracket is real and concrete; (2) the bounded throat
regularizes the divergence (chimera = synchronous artifact); (3) the open crux is §687(ii), now
sharp -- does a pre-rec sound integral exist at all, and reading B says plausibly NOT; (4) if not,
the peak scale is the aperture figure (node 4), not r_s -- the two node-4 threads (sound horizon
vs literal telescope) may resolve in favour of the telescope. NEEDS DARYL (architectural): how the
observable D_M sits in the non-synchronous comoving coordinate, and whether this-side pre-rec
history exists at all. DO-NOT-ASSERT both ways; reading B's number is exploratory, not asserted.

---

## r454 — coordinate reconciliation: the whole peak scale reduces to ONE physical unknown, z_seam (and r453's regularization was a coordinate illusion)

Took the hinge computation: how the observable D_M sits in the non-synchronous §498 coordinate.

**The observable comoving distance is the conformal-time integral, and it is robust.**
D_M = INT dtau~/(a/a0), rec->now = 2.591 alpha = 13936 Mpc -- exactly the flat-LCDM value
(§498 reproduces the redshift-distance relation, as the corpus states). This is the observable.

**CORRECTION of r453 (owned).** The §498 spatial COORDINATE chi (reading B, dchi=dtau~/(r'+1))
gives 0.367 rec->now -- NOT equal to D_M = 2.59. So the §498 chi is NOT the observable comoving
distance; it is a gauge coordinate. Reading B's CONVERGENCE of the seam->rec integral was therefore
a COORDINATE ILLUSION, not a physical regularization of the observable r_s. The chimera divergence
is REAL in the observable (conformal-time) framework -- r453's "the bounded throat regularizes it,
chimera = synchronous artifact" was wrong on that point. The divergence is physical, and it is
controlled by where the lower limit sits.

**The clean result: the entire peak scale is a monotonic function of ONE physical unknown, z_seam**
(the redshift at which the seam sits). With D_M robust and c_s = c/sqrt3:
  r_s(z_seam) = INT_{z_rec}^{z_seam} (c/sqrt3) dz / H(z),   ell_A = pi D_M / r_s(z_seam).
  z_seam = 1500 -> r_s= 41,  ell_A=1071
  z_seam = 3400 -> r_s=120,  ell_A= 364
  z_seam = 4831 -> r_s=145,  ell_A= 301   <-- the OBSERVED acoustic scale
  z_seam ->inf  -> r_s=276,  ell_A= 159   <-- the §687 HYBRID (a->0, the §661 matter-frame seam)
  z_seam = z_rec-> r_s-> 0,  ell_A->inf   <-- pure seam=LSS: NO sound horizon (peaks = APERTURE)

**This is exactly §687(ii), reduced to a single question: what is z_seam?** Nothing else is free.
D_M is robust; c_s is the geometric sqrt3; r_s = r_s(z_seam). The whole acoustic-scale frontier is
the placement of the seam in redshift.

**What it does to the seam-as-LSS hypothesis -- the fork is now sharp and quantitative:**
- **seam = LSS (z_seam = z_rec):** r_s -> 0, NO acoustic sound horizon. The peaks then CANNOT be a
  sound horizon at all; they must be the APERTURE/diffraction figure (node 4's telescope). This is
  the reading consistent with reading B's "recombination sits at the seam."
- **pre-recombination history (z_seam ~ 4831):** a genuine this-side (or bounce-fed) phase from
  z~4831 down to z~1090, giving the standard-like sound horizon r_s = 145 with the GEOMETRIC
  c_s = c/sqrt3 -- the observed ell_A = 301, no tuning beyond placing the seam at z~4831.
- The §661 matter-frame ruler-collapse (r -> 0 at the seam) points to z_seam -> inf, which gives
  the disavowed hybrid (159) -- so the naive matter frame does NOT land the scale; the resolution
  needs the genuine seam structure to fix a finite z_seam (or to send it to z_rec = telescope).

**The polarization adjudicates (steady-hands constraint, recorded earlier):** the measured TT/TE/EE
phase-lock requires a real oscillating fluid behind the peaks. The pure-aperture (z_seam=z_rec with
peaks conjured from geometry) cannot source the velocity-offset E-modes; the pre-rec-history reading
(z_seam~4831, real oscillations) can, and the collapse-fed seam=LSS can IF the imaged seam carries
the prior collapse's real oscillations. So the data pushes toward EITHER pre-rec history OR a
collapse-fed seam that images a genuinely-oscillated surface -- NOT pure geometric diffraction.

**Honest state.** D_M robust; the peak scale = r_s(z_seam), one unknown; observed ell_A <=> z_seam
~ 4831; z_seam->inf = the disavowed hybrid; z_seam=z_rec = no sound horizon (aperture only).
r453's regularization corrected as a coordinate illusion. The remaining question is purely physical
and architectural: where does the seam sit in redshift, and is there genuine pre-recombination
history (this-side or collapse-fed)? DO-NOT-ASSERT; no z_seam is asserted.

---

## r455 — decoupling conjecture tested; the fork is now pruned to one unbuilt construction

**Tested Daryl's decoupling conjecture** (radiation rings -> sets c_s and sources the peaks, but
does NOT leak to the rate -> expansion stays geometric sinh^(2/3), Lambda-fixed):
- Literal computation (real photon-baryon c_s on the CR no-radiation rate, integral to infinity):
  r_s = 254 Mpc, ell_A = 172 -- the §687 HYBRID. Decoupling alone does NOT land 301; it deepens
  the hybrid, because removing radiation from H makes H smaller at high z -> sound horizon LARGER
  -> ell_A pushed DOWN. The decoupling moves the scale the wrong way on its own.
- Matching 301 still needs an upper CUTOFF: z_top ~ 6847 (real c_s) ~ 2.00 z_eq, or ~4831
  (geometric c_s=c/sqrt3) ~ 1.41 z_eq, where shadow equality z_eq = 3423. Cutting AT z_eq overshoots
  (ell_A = 427). So the cutoff is the SAME ORDER as the shadow equality but ~1.4-2x higher, and the
  factor shifts with c_s -- NOT a clean z_eq identity (the 2.00 with real c_s is reverse-engineered,
  not robust). Verdict: decoupling is necessary (CR-faithful) but NOT sufficient; all the work is in
  the high-z cutoff z_top = z_seam, which decoupling does not determine.

**The fork, now pruned by data + polarization to ONE unbuilt construction:**
- (A) naive matter-frame, seam at z->inf (a_m->0, §661 literal): gives the hybrid ell_A=159-172.
  DISFAVORED by the data (observed 301). So the data itself rules against the naive a_m->0 reading
  -- CR's peak scale is NOT the naive matter-frame sound horizon.
- (B/pure-aperture) peaks from pure geometric diffraction, no fluid: DISFAVORED twice -- the frozen
  tower projects SMOOTH (no rings, r447), and the measured TT/TE/EE phase-lock needs a real velocity
  field that pure geometry cannot source. Out.
- (C) a REAL oscillating fluid behind the peaks, with the sound integral cut at z_seam = where the
  seam/imprint sits. "This-side pre-rec history" (z_seam~5000->z_rec) and "collapse-imprinted at
  seam=LSS" are the SAME fluid physics, plausibly one structure across the NBC seam (cf. the r431
  seam-question dissolution). This is the surviving branch.

**So it is a FORK that resolves into a single unbuilt CONSTRUCTION, not a calculation:** the seam's
thermal/dynamical structure -- what fluid exists, at what z it is imprinted/turns on (= z_seam), with
what oscillation phase -- which is exactly §687(i)+(ii) / problem #1, and which the corpus states is
unconstructed. The calcs have done their job: everything is pinned to that one construction, the
naive and pure-aperture alternatives are ruled against, and the peak scale is r_s(z_seam) with
z_seam the sole unknown. Determining z_seam is the architectural build (what CR claims happens
between the seam and recombination), not a number the present geometry hands over. DO-NOT-ASSERT.


## r456 (c23 with Daryl) — the projection: FORM is geometric, SCALE is in the field (quantified). DO-NOT-ASSERT.
Carried node 4's projection (throat-aperture modes -> observer sky). GROUNDED setup:
- dS4 closed slicing is conformal to a FINITE Einstein-static slab x S^3: cosh(T/alpha)=sec(eta),
  eta in (-pi/2,pi/2), width exactly pi; a(eta)=alpha*sec(eta). Photon field conformally invariant
  in 4D -> conformal factor drops -> field on the bare finite slab x S^3 (the literal bounded aperture).
- Conformally-invariant tower: omega_n = n+1 (n(n+2)+1=(n+1)^2), EVENLY SPACED.
- Radial nulls deta=dchi -> throat (eta=0) seen at comoving S^3 radius chi_LSS=eta_0.
  Projection ell_n ~ (n+1)*(D_M/alpha): evenly-spaced tower -> evenly-spaced peaks = the FORM.
RESULT (numbers): alpha=sqrt(3/Lambda)=c/(H0 sqrt(OmegaL))=5379 Mpc; D_M=13935 Mpc (robust, flat-LCDM).
  Unit-tower spacing Delta-ell = D_M/alpha = 2.59 vs observed ~308: geometric aperture UNDERSHOOTS by ~120.
  Peaks demand comoving scale ~45 Mpc ~ alpha/120 (r450's 'alpha/35'); alpha/r_s~37, ell_A=pi D_M/r_s~298.
READING: the FORM (constant spacing) is the geometric prediction and survives. The SCALE is NOT geometric
  -- the bare tower undershoots by ~2 orders of magnitude, so the observed peaks are NOT consecutive tower
  modes; the fine structure (~alpha/120, r_s-order) is set by the field's lambda (687(i)) + the seam<->
  recombination relation (open #2), NOT by any single geometric knob. This quantitatively answers 'why not
  just fit z_seam': the gap is ~120x, not a one-parameter shift; it lives in the field. Machinery now in
  place to turn the field into predicted ell_n once built. Held not claimed; nothing forced toward 220.
NEXT: the coherent field on the throat -- what mode instantiates, what sets lambda (687(i)).


## r457 (c23 with Daryl) — FIELD ON THE THROAT OPENED: interference mechanism = "reorganized acoustics". CANDIDATE, DO-NOT-ASSERT.
Opened 687(i). Conformally-invariant field on the finite slab x S^3: modes T_n''+omega_n^2 T_n=0,
omega_n=n+1 -> EVERY mode oscillates in conformal time (no plasma needed; the closed geometry rings).
MECHANISM (candidate): oscillating tower + any coherent seam state -> interference fringes. A fluctuation
frozen at recombination carries at degree n a factor cos^2((n+1) eta_rec); PEAKS at (n+1)eta_rec=m*pi,
evenly spaced, spacing ~ pi/eta_rec. eta_rec (seam->recombination conformal interval) plays the sound-horizon
role; the closed-slab dispersion omega_n=n+1 plays c_s. Fringes are dS MODE PHASES, not a ringing medium =
"reorganized acoustics" concretely; "the big bang as a telescope" literal.
SCALE: one parameter eta_rec = OPEN #2 (seam<->recombination), and it IS FITTABLE from the peak spacing
(Daryl's point, in the RIGHT model -- not the chimera's z_seam-integration-limit). Sharpens/supersedes r456's
naive D_M/alpha projection: the proper scale-setter is mode interference (pi/eta_rec).
PULLED BACK (honesty): did NOT hand a fitted eta_rec -- the n->ell projection carries an unpinned factor
(~D_M/alpha~2.6), so the number is held. ROBUST regardless: the fit drives eta_rec small -> recombination
near the throat = status-doc live "seam ~ recombination" candidate; consistent with (NOT predicting) z~1090
for a late observer (a_rec~alpha, T_0/alpha~7.7). Flag, not finding.
LEFT TO DERIVE (construction proper, in order): (1) seam state from NBC (665) -> peak phases/heights/first-peak
offset; (2) eta_rec from throat geometry + recombination physics (open #2) -> turns fit into prediction (Gate 2);
(3) the n->ell projection factor; (4) EM transverse-vector tower vs scalar toy; (+) thermal sky as projection
(throat is cold), inside open #2. All numbers stated without being claimed.

## r458 (c23 with Daryl) — interference FORM on the settled metric seam; offset phi~0.29 = two-ruling seam phase. DO-NOT-ASSERT.
ONTOLOGY HELD (Daryl, corrected hard): Psi is METRIC; the seam is the finite-curvature metric singularity at
areal radius alpha joining the collapse horizon to the Nariai horizon -- ONE surface (figure: "metrically exact").
No "free seam" -- that framing (r457) is dead; seam condition is definite on the metric waist.
RESULT: interference peaks (n+1)eta_rec=m*pi -> evenly spaced; spacing matches observed ~308 (the eta_rec scale).
GAP (honest): bare cos^2 gives harmonic-from-zero ratios 1:2:3:4; observed 1:2.45:3.68:5.14 = evenly spaced
with first-peak phase offset phi=1-ell_1/Delta~0.29 (~quarter-wave). Spacing right, offset not from bare cos^2.
DIRECTION (not result): phi~0.29 ~ quarter-wave = velocity/density two-component admixture at the seam = the
TWO RULING FAMILIES (matter family-1 + mystery family-2, blue+orange through the waist). Scalar toy = one
component -> phi=0; the real two-ruling field carries both, their relative seam phase sets phi. Ties node 4 -> node 1.
NEXT (live): the two-ruling field state at the metric seam -> derive phi from the families' relative phase; upgrade
scalar toy -> the actual (photon/tensor + two-ruling) field; pin the n->ell projection; then eta_rec scale fit. Held not claimed.

## r459 (c23) — CORRECTION to r458: the quarter-wave offset story is REFUTED by computation. DO-NOT-ASSERT.
r458 floated phi~0.29 as a "generic velocity-density quarter-wave from the two rulings". COMPUTED it
(cos^2 + R_v sin^2): NO first-peak offset for any R_v<1 (peak stays at pi). So that mechanism is WRONG,
struck -- not a pending direction. SOLID part stands: interference gives evenly-spaced peaks, spacing = the
eta_rec scale, matches observed ~308. OPEN/unexplained: the first-peak offset phi~0.29 (ell_1=220 < spacing 308).
It needs the actual two-ruling field equations + seam dynamics, not a cos^2/sin^2 toy. No mechanism asserted for it.
