# Perturbations in the SdS Representation: the Primordial / CMB Scalar Sector of Cosmological Relativity
> **⌖ RETIRED r1521 — superseded, verified.** This is a draft of the perturbation paper (r528). **Its work landed in P15** — the low-ℓ shape is built there on a genuine Boltzmann transfer, gate-validated, and Lane 1 A1.2 is struck DONE at r1006.
> Kept as record; **do not work from it.**


### Working prose draft (status-tagged) — companion to P9 (CR_flatLCDM); scalar-sector counterpart to the built tensor sector of the dynamics paper.

> STATUS TAGS, per claim: **[E]** established (verified cold this pass); **[R]** reach
> (real reasoning + leading-order computation, O(1) ambiguity flagged); **[I]** reading
> (defensible interpretation); **[O]** open (named, not filled). Verification: every
> [E]/[R] result re-derived from corpus source forms in `computations/perturbation_verify/`.
> CANON: Einstein's equations are unchanged; the construction is ontological, not
> "merely representational"; "manufactured/projection/perspectival" mean built-by-
> construction-and-real, never unreal.

---

## §0. The decomposition thesis

P9 establishes the SdS cosmology — the flat-ΛCDM expansion history recovered exactly from
the Λ-set $\sinh^{2/3}$ geometry by causal reassignment, the rate fixed by the cosmological
constant alone with radiation carrying no term in it — and names, in its outlook, the
treatment of perturbations within that representation as open. This paper takes up the
scalar (matter/CMB) sector of that frontier. The tensor sector is already built (the
dynamics paper: the transverse-traceless shear, the Gowdy–de Sitter wave, the ghost-free
massless de Sitter mode); this is its scalar counterpart.

The central claim is a **decomposition**, and it is one sentence:

> The CR primordial/CMB scalar spectrum factorizes into a part the de Sitter **substrate
> geometry determines** and a part the **progenitor collapse supplies**, with the seam's
> null-and-degenerate geometry assigning each its job.

Substrate-determined (this paper's positive content): the coherence of the acoustic phases;
a parameter-free low-multipole discreteness floor; the classical, non-vacuum character of
the fluctuations; and — proven, not assumed — that the seam *transmits* rather than imprints
the spectral shape. Progenitor-supplied (inherited boundary data, not derived here): the
amplitude $A_s$ and tilt $n_s$. This division is not a division of labor we impose; it is
forced by two facts about the seam — that it is a null surface, and that it is a degenerate
(double-root) horizon — each of which is established geometry.

**One unification with P9, held at weight.** P9 already carries a progenitor-supplied
boundary datum: the radiation amplitude $\rho_r/\rho_m\approx2$ that calibrates the acoustic
scale is fixed by the hot handover of the progenitor collapse — this universe having formed
at the event horizon of a black hole in a previous one — exactly as flat ΛCDM carries the
baryon-to-photon ratio $\eta$ from a baryogenesis it does not model (P9 §687–693). The
transmission result below routes $A_s$ and $n_s$ through the *same* handover. There is one
boundary-condition supplier, not two: the η-analogue, generalized from a single amplitude to
the primordial spectrum.

**The certification guard, kept explicit.** That this paper's transmission result lands on
the same handover P9 reached independently is *coherence, not correspondence*: it shows the
picture is internally consistent, not that it is true. The field's verdict is owed to the
argument, and a cold reading is owed to this draft. The fit is not the argument.

---

## §1. Background: the resolved scale, and the sub-horizon seam

### 1.1 What is already banked, and not re-opened here

The acoustic **scale** and the Hubble tension are resolved upstream, in P9 §687–691, and
this paper builds on that resolution rather than re-deriving or re-opening it. In brief:
the Hubble tension dissolves as a consequence of the radiation-free rate — there is no
second $H_0$ to reconcile, the directly measured rate being the geometry read at the present
epoch, while the CMB's lower inference rests on a radiation-governed sound horizon the
construction does not share. The acoustic scale $\ell_A$ is then met at the *directly
measured* $H_0$ by a single measured early-universe parameter, the radiation amplitude
$\rho_r/\rho_m\approx2$ at the seam ($z\approx6850$, $T\approx1.6$ eV) — the structural
analogue of $\eta$, a measured matter-content initial condition, $O(1)$-reasonable from
collapse energetics and not tuned, with $c_s$ the ordinary baryon-loaded fluid value (the
seam matter being pressureless; the geometric ratio $\sqrt3$ does **not** set $c_s$). [E — P9 §687–691]

A methodological note this paper must respect, because it is the corpus's own: the
"$\sim$1.9× tension" in the acoustic scale that earlier readings reported is a *chimera* —
the standard radiation-governed sound horizon (the sound-travel integral to $z\to\infty$)
laid on the radiation-free rate, a calculation belonging to neither model. It is in no
paper. The scale is not in tension; it is a one-parameter accommodation that succeeds. What
this paper develops is the **spectrum** (the heights, phases, and large-scale structure of
the fluctuations), which is genuinely downstream of the scale and genuinely open — distinct
from the scale, not a re-opening of it. [E — CORPUS_MAP CURRENT STATE]

The standing, falsifiable claim, reaffirmed, is the prior one: radiation carries no term in
the expansion rate. The dissolved tension and the one-parameter scale are its consequences,
and the sound horizon at a geometrically fixed $H_0$ is where CR and the standard
radiation-governed history part on data in hand. The discriminator is a strength, not a
frontier. [E — P9 §691]

### 1.2 The rate, read leftward

The expansion rate is fixed by $\Lambda$: $H^2 = \tfrac{\Lambda c^2}{3}\coth^2(\tfrac12\sqrt{3\Lambda}\,c\,\tilde\tau)$,
the $\sinh^{2/3}$ areal radius primary and the Friedmann densities bookkeeping for one
$\Lambda$-set geometry, with $\Omega_{m,0}$ recording the cosmic epoch at which we observe
rather than an independent amount of stuff (P9 §amplitude). Radiation, like matter, is
inherited content whose density is read off the geometry's clock, not a term that sources
the rate; there is no radiation-dominated era. Consequently the objection that a perturbing
radiation fluid "must gravitate and so must alter the rate" is a category error against a
theory that reads the Friedmann relation leftward: the rate is set, and the fluid's energy
is among the contents the set rate carries. [E — P9; the corrected reading]

### 1.3 The seam is sub-horizon for the acoustic modes

The cosmological beginning is the finite-curvature horizon seam, not the $r=0$ singularity
(P9 §665, §673). At the seam redshift $z\approx6850$ the comoving Hubble wavenumber, on the
radiation-free rate, is

$$k_{\rm hor}(\text{seam}) = \frac{H_0\,E(z)}{(1+z)\,c}\Big|_{z\approx6850} \approx 0.010\ \text{Mpc}^{-1},$$

while the acoustic peaks sit at $k\sim\pi/r_s\approx0.022\ \text{Mpc}^{-1}$ and above — a
factor $\gtrsim2$ inside the horizon. [E — verify_numeric.py, anchor 7] The acoustic-scale
modes are therefore *sub-horizon at the seam*: they are not frozen super-horizon data
waiting to re-enter, as in the inflationary initial-condition story, but modes already
inside the horizon when the cosmological side begins. Whatever fixes their amplitudes and
phases is the seam handover itself, not a super-horizon freeze-out. This is the hinge on
which the rest of the paper turns: it is *why* the substrate's role is to transmit and
gate rather than to generate, and it is *why* the initial conditions are inherited.

---

## §2. What the substrate determines — coherence from the null seam

The acoustic peaks of the CMB are sharp because the oscillating modes are *coherent*: at
last scattering the modes of a given wavenumber share a common phase, so their power adds
in a regular comb rather than washing out. In the inflationary account this coherence is
produced dynamically — modes are frozen while super-horizon and re-enter with a common
phase. Section 1.3 showed that mechanism is unavailable here: the acoustic modes are
sub-horizon at the seam, never frozen super-horizon. CR must obtain the coherence
differently, and the seam's geometry supplies it.

The seam is a **null** surface — the cosmological horizon promoted to the initial layer
(P9 §665). The initial-value problem on a null surface is characteristic, not Cauchy: the
data that determine the future are one free function per mode on the surface, together with
regularity along the generators, rather than a field and an independent momentum. A single
function per mode is a single phase per mode — there is no second, independently specifiable
datum to randomize the relative phase. Coherence is therefore not imposed; it is what
characteristic data on a regular null surface *is*. [R — the mechanism is the standard
structure of the characteristic IVP; its sufficiency for observational coherence is reasoned,
not yet proven through the full transfer]

Illustratively, integrating the acoustic modes forward from a common seam surface produces a
regular comb at $\Delta k=\pi/r_s$, while the same integration from phases drawn at random
produces broadband power with no comb — the expected qualitative contrast, recorded as an
illustration rather than a verified amplitude. [I — illustrative; not re-derived cold] The
structural point stands on the characteristic-data argument: where inflation freezes the
phase dynamically, CR fixes it geometrically, on the single null layer.

## §3. What the substrate determines — the amplitude floor and the classical character

The de Sitter substrate has a vacuum, and one might ask whether the observed fluctuation
amplitude is that vacuum's — the natural CR analogue of the inflationary story, in which the
spectrum *is* the (quantum) vacuum stretched. It is not, by a margin that settles the
question. The substrate's curvature scale is the cosmological constant scale: in Planck
units $\Lambda\,\ell_P^2\approx3\times10^{-122}$, and the de Sitter vacuum metric-fluctuation
power is of the same order, $\sim(H_\Lambda/M_P)^2\sim10^{-122}$. The observed scalar
amplitude is $A_s\approx2\times10^{-9}$. The substrate vacuum is therefore roughly **$10^{113}$
times too small** to be the observed spectrum. [E — verify_numeric.py anchor 5; the prefactor
($\sim10^{-122}$ vs $\sim10^{-123}$) is a $2\pi$ / reduced-vs-full Planck-mass convention, and
the conclusion is robust to it]

Two consequences follow, and both are clean predictions of character rather than of number:

- The observed amplitude is **inherited classical content**, not the substrate vacuum. It
  enters as boundary data from the progenitor, not as a quantum fluctuation generated within
  the SdS era. [E/I]
- There is **no inflationary consistency relation**. The relation $r=-8n_t$ presupposes that
  scalar and tensor spectra are the *same* vacuum stretched by the *same* expansion; with the
  amplitude not vacuum-sourced, that link is absent. Equally, the tensor floor of the
  substrate vacuum is the same $\sim10^{-122}$ — so there are **no substrate-sourced primordial
  B-modes**; any observed tensors would themselves be inherited content, not a measure of a
  substrate inflationary scale. [E/I]

This is the sense in which the substrate "determines" the statistics without supplying the
amplitude: it fixes that the fluctuations are classical, inherited, and not governed by a
vacuum consistency relation — and leaves their size to the handover.

## §4. What the substrate determines — the throat and isotropization

At the Nariai seam the near-horizon geometry is, exactly, $\mathrm{dS}_2\times S^2$ with the
two factors sharing the curvature radius $1/\sqrt\Lambda$: the merged double root sits at
$r_\star=\alpha/\sqrt3=1/\sqrt\Lambda$, with $f''(r_\star)=-2\Lambda$ (so the $\mathrm{dS}_2$
radius$^2$ is $1/\Lambda$) and the $S^2$ two-Ricci $R_2=2/r_\star^2=2\Lambda$. [E —
verify_geometry.py anchor 2; Ginsparg–Perry] This is the geometry the perturbations see as
they cross.

A field on $\mathrm{dS}_2\times S^2$ decomposes in $S^2$ spherical harmonics; the harmonic of
degree $\ell$ becomes a $\mathrm{dS}_2$ field of effective mass $m^2=\ell(\ell+1)/r_\star^2$,
i.e. $m^2/H_{\mathrm{dS}_2}^2=\ell(\ell+1)$. In $\mathrm{dS}_2$ the index is
$\nu^2=\tfrac14-m^2/H^2$, so the monopole $\ell=0$ has $\nu=\tfrac12$ — the scale-invariant
base — while every $\ell\geq1$ has $\ell(\ell+1)\geq2$, hence $\nu^2<0$: the heavy principal
series, which oscillate and **decay** through the throat. [R/I — the geometry is [E]; the mode
tower and its reading are interpretation] The anisotropic harmonics are suppressed crossing
the seam: an angular no-hair, the throat **isotropizing** what passes through it.

**Guard, load-bearing:** the $\ell$ of this throat tower is the $S^2$-harmonic index of the
*near-horizon* geometry; it is **not** the observable CMB multipole. The throat sits at
areal radius $1/\sqrt\Lambda$, the observed sky at the last-scattering 2-sphere of radius
$D_C$; the map between them is §6, not an identity. Conflating the two would manufacture a
prediction the geometry does not make. [guard]

## §5. Large scales — the flat/discrete decoupling and the low-ℓ floor

This is the section where the construction makes its sharpest large-scale statement, and the
load-bearing piece is established, not reach.

**The decoupling is P9's own property.** In the fundamental-observer frame the line element
is $ds^2=-d\tau^2+(\partial_\chi r)^2 d\chi^2+r^2 d\Omega^2$ (P9 eq:SdS-fundamental), and the
slices of constant $\tau$ are Euclidean. Verified directly: on a constant-$\tau$ slice
$(\partial_\chi r)^2 d\chi^2=dr^2$, so the induced 3-metric is $dr^2+r^2 d\Omega^2$, whose
Riemann tensor is identically zero — exactly flat $\mathbb{R}^3$. [E — verify_geometry.py
anchor 1] The distance slicing is therefore flat: $\Omega_k=0$, no curvature term in the
redshift–distance relation, consistent with observation to high precision. Meanwhile the
*cosmological* layers — the surfaces of constant $\tilde\tau=\tau+\chi$ — are the closed
$S^3$ that fills the upper sheet (P9 §661). The non-synchrony $\tilde\tau=\tau+\chi$ is the
decoupling itself: flat distances and a closed $S^3$ of comoving worldlines coexist because
they live on *different slicings of one geometry*. [E — P9 + anchor 1]

A literal closed-FLRW reading would put $\Omega_k=-\Omega_\Lambda\approx-0.685$ into the
distance relation and be excluded at many $\sigma$; CR avoids that not by tuning but because
its distance slicing is the flat constant-$\tau$ one, while the curvature lives on the
constant-$\tilde\tau$ layers. **Spatial curvature and dark energy are one $\Lambda$ read on
two slicings** — the same identity that runs through the rest of the corpus, here at the
observational rung. [E identity / I reading]

**The low-multipole floor.** The closed $S^3$ carries a discrete mode spectrum: modes are
labelled by integer degree $L$, the lowest physical mode being $L=2$ (the dipole $L=1$ is
not a temperature observable). Projecting the discrete $S^3$ modes to angular multipole at
the last-scattering sphere gives, to leading order,

$$\ell_L \simeq \sqrt{L(L+2)}\;\frac{D_C}{r_0},$$

with $r_0$ the present $S^3$ areal radius and $D_C$ the comoving distance to last scattering.
Both are fixed without new parameters: $D_C\approx13927$ Mpc is the flat-ΛCDM observable, and
$r_0\approx5064$ Mpc follows from the Nariai amplitude $2^{1/3}/\sqrt\Lambda$ at the present
epoch $u=\mathrm{asinh}\sqrt{\Omega_\Lambda/\Omega_m}\approx1.18$. The lowest physical mode
then lands at $\ell_2\approx7.8$, with the tower quasi-continuous by $L\sim20$ ($\ell\sim58$).
[R — verify_numeric.py anchor 6] So CR predicts a **discreteness floor at low multipole, set
parameter-free by $\Lambda$**, in the same region ($\ell\sim$ a few) as the observed
large-angle power deficit.

**[BUILT r522–r523 — see `corpus/scalar_perturbations_paper.tex` §largescale.]** The non-synchronous
transfer is now built. The distance slicing is flat (prop:flat → $D_M=D_C$, cross-checked by
$\ell_A\approx301$ vs the $r_0$-chimera's 110), so the discrete closed-$S^3$ source projects through the
**flat** $j_\ell(k_L D_C)$ — NOT the hyperspherical transfer of a literal closed universe (which would
wrongly send the lowest mode to the quadrupole and give no deficit). Result [E, flat-limit-verified]: a
low-multipole **deficit** below $\ell\approx8$ ($\ell_2\approx7.8$, none below) that **survives the late
ISW** — the cumulative term is the standard SW+ISW (P7 §floor), sourced by the same discrete spectrum and
so itself starved below $k_2$, filling the deficit only partway — and sits a factor $\sim3$ below
flat-$\Lambda$CDM at $\ell=2$–4, in the region of the observed anomaly. Receipts: `verify_closedS3_nonsync.py`,
`verify_isw_lowell.py`. Solid: the deficit's existence, parameter-free scale, location ($\ell\lesssim8$,
geometric), ISW survival, AND now the depth at full radiative order (~0.2 of ΛCDM), the data confrontation (quadrupole match, octopole tension), and the Doppler completion. [E — see scalar paper §largescale/§scope, r522–r528]

## §6. Throat → cosmology propagation

The link from the throat geometry (§4) and the closed-$S^3$ discreteness (§5) to the observed
sky runs through the seam continuation, which is structurally invertible: P3's
$\sin\theta\to\cosh\psi$ continuation across the throat is analytic and rigid, so it carries
the *shape* of what crosses faithfully while leaving amplitude and tilt to be set (this is
the same rigidity that the transmission proof of §7 makes precise). [E structural] What is
**open** is the depth: the non-synchronous photon transfer is now BUILT (r522 — the flat
projection of the discrete closed-$S^3$ source, §5), giving the low-$\ell$ deficit below
$\ell\approx8$; what remains is the exact depth at full radiative order, beyond the leading
ordinary-SW + late-ISW estimate of §5, not the deficit's parameter-free existence, location,
or ISW survival. The depth at full radiative order is the remaining computation of the
large-scale sector, and it is named, not finessed. [R depth]

## §7. What the progenitor supplies — the transmission proof

The decomposition's load-bearing proof is here: *why* the substrate transmits the spectral
shape rather than imprinting one of its own. It turns on whether the seam horizon is
degenerate.

Consider a mode falling toward a horizon where the metric function behaves as $f\sim(r-r_h)^p$.
The tortoise coordinate $r_*=\int dr/f$ controls the approach. For a **non-degenerate**
horizon ($p=1$, $f\sim2\kappa(r-r_h)$, surface gravity $\kappa>0$) the integral is
logarithmic, $r_*\sim(1/2\kappa)\ln(r-r_h)$, so the approach is exponential, $(r-r_h)\sim
e^{2\kappa r_*}$ — the thermal/Hawking law, and the mechanism by which a de Sitter horizon
*imprints* a scale-invariant spectrum ($n_s\to1$): the exponential redshift erases the
infaller's spectral information and stamps the horizon's own thermal scale. For a
**degenerate** horizon ($p=2$, the Nariai double root, $f\sim\Lambda(r-r_\star)^2$, $\kappa=0$)
the integral is instead $r_*\sim-1/[\Lambda(r-r_\star)]$, so the approach is power-law,
$(r-r_\star)\sim-1/(\Lambda r_*)$ — **scale-free**: no thermal scale is stamped, and the
infalling spectrum is **transmitted faithfully**. [E — verify_geometry.py anchor 4]

CR's seam is the Nariai double root (verified degenerate in §4). Therefore the seam is a
**faithful, scale-free transmitter**: the amplitude $A_s$ and tilt $n_s$ are the progenitor
collapse's spectrum, carried across unaltered, **not** imprinted by the seam. The degeneracy
is the *proven reason* CR carries the primordial tilt rather than manufacturing it — and the
same reason CR has no inflationary scale-invariant attractor: the mechanism that would
produce $n_s\to1$ is exactly the non-degenerate approach the Nariai seam does not have. [E]

What the transmitter carries is therefore **open from the SdS side**: $n_s$ and $A_s$ are
inherited, fixed by the progenitor collapse and not derived here — the same handover that
fixes $\rho_r/\rho_m$ and the light-element abundances in P9. [O]

## §8. Predictions and falsifiable signatures

Tagged individually, strongest to most open:

- **Classical, non-vacuum primordial statistics; no inflationary consistency relation; no
  substrate-sourced primordial B-modes.** [E/I — §3]
- **The transmission character:** the seam carries the progenitor tilt and does not drive
  $n_s\to1$; CR has no inflationary scale-invariant attractor. [E — §7]
- **Flat distances ($\Omega_k\simeq0$) coexisting with a closed-$S^3$ low-multipole
  low-multipole *deficit* below $\ell\approx8$, set parameter-free by $\Lambda$, surviving the ISW to sit
  a factor $\sim3$ below flat-$\Lambda$CDM at $\ell=2$–4** — a signature of neither flat nor
  standard-closed ΛCDM. [E decoupling+deficit / R depth — §5]
- **Coherent acoustic peaks from geometric (null-seam) phase-fixing, not super-horizon
  freeze-out.** [R — §2]
- **Acoustic scale $\ell_A$:** resolved upstream (P9); the radiation-free rate is the
  standing CR-vs-ΛCDM discriminator on data in hand — a strength to cite, not this paper's
  to assert. The only open remainder at the scale is a *parameter-free* derivation of
  $z_{\rm onset}$ (deriving, rather than measuring, the η-analogue). [E (banked) / O (derivation)]
- **Spectrum heights and $n_s$, $A_s$:** inherited from the progenitor handover (downstream
  matter-sector work, P5/P6). [O]

## §9. Boundary, and the named next construction

The substrate carries everything the seam's null-and-degenerate geometry lets it carry —
coherence, isotropization, the discreteness floor, the classical character, and the faithful
transmission — and the degeneracy proves precisely where it stops: the spectrum's amplitude
and tilt are not the substrate's to set. This is the same shape as inflation parametrizing
its observables through an unknown inflaton potential; CR routes them through an unknown
progenitor collapse, but with the arrival constrained — whatever the collapse supplies must
reach the seam coherent, isotropized, scale-freely transmitted, and classical.

The next construction, a separate paper, is that progenitor: a specific collapse, its
perturbations evolved to the horizon, yielding the inherited spectrum. The progenitor is a
*chosen input*, not a CR prediction — exactly as $\eta$ is a measured input to flat ΛCDM —
and the honest target is consistency (the inherited composition and spectrum matching the
measured primordial abundances and $n_s$, $A_s$), not derivation from the geometry alone. [O]

## §10. Relation to the corpus

This is the scalar-sector companion to the dynamics paper's (built) tensor sector, and the
perturbation companion to P9's (banked) background and scale. It rests on P1 (the
metric-singularity/causality keystone — the decisive structural test, on which none of the
cosmology bears), P3 (the slicing continuation, current at r478+: underlying geometry de
Sitter, Schwarzschild mass perspectival), P9 (the cosmology and the resolved scale), and the
algebroid/groupoid classification (the $A_2$/$D_6$ discrete structure, which bears on the
handover's orientation content). The spectrum's heights live downstream, in the matter
sector P5/P6 name as open.

---

*Draft complete in the body; all [E]/[R] claims rest on the cold-verification pass
(`computations/perturbation_verify/`). Held for the council's cold read: the
throat-tower reading and its non-identity with the
observable $\ell$ (§4), and the A₂/D₆ constraints on the handover (§7/§9). CLOSED since draft: the coherence mechanism (§2 — coherent/incoherent comb contrast COMPUTED, `verify_coherence_comb.py`; full seam-to-recombination transfer the residual honest flag); and the low-$\ell$ deficit depth (§5/§6 — full radiative order ~0.2 of ΛCDM, data CONFRONTED with quadrupole match + octopole tension cosmic-variance-limited, Doppler completed and shown not to differentiate $\ell$=2/3; `verify_lowell_full_radiative.py`, `confront_lowell_data.py`, `verify_doppler_lowell.py`). Coherence is not correspondence;
this draft is internally consistent and owes the cold read and the field's verdict.*
