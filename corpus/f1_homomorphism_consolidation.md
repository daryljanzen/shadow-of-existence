# F1 — the field-theoretic homomorphism: what is established (orbit transversality) and what stays open (the term-for-term bracket)

**Provenance.** Re-derived at honest weight from a *suspect* gift bundle (`..._r228_corrupted.zip`) whose
framing was contaminated across ~5 uncaught compactions. Every calculation below was **re-run at source**
(sympy 1.14.0) and the headline result **independently re-derived** by a second route; the gift's
"RESOLVED / homomorphism closes" framing is **discarded**, and none of the gift's capstone/map/plan/vision
edits were adopted. What survives is the arithmetic, re-weighted here.

---

## 1. The genuine new result — orbit transversality of the 𝔰𝔬(5,1)-action on 𝒞  **[computed; independently verified]**

On the SdS static spatial 3-slice $ds^2_3 = dr^2/f + r^2 d\Omega^2$, $f = 1-2M/r-r^2/\alpha^2$ (the corpus's
actual spatial leaf — the static, $K=0$ vacuum cut):

- $^3R = 6/\alpha^2 = 2\Lambda$, **M-independent** — every SdS vacuum cut shares it. This is the
  Hamiltonian-constraint anchor at $K=0$, $\rho=0$ ($^3R = 2\Lambda$), confirmed two ways and as the
  cross-check $^3R - 2\Lambda = 0$.
- $R_{ab}R^{ab} = 6M^2/r^6 + 12/\alpha^4$, **M-dependent** ($M{=}0 \to 12/\alpha^4 = 3(2/\alpha^2)^2$, the
  constant-curvature 3-space value — sanity check passes).

A diffeomorphism invariant ($R_{ab}R^{ab}$) therefore **separates different-$M$ cuts** while $^3R$ does not:
different-$M$ slices are **non-isometric**, so **no $\mathfrak{so}(5,1)$ element connects them**.
⟹ **The $\mathfrak{so}(5,1)$-action on $\mathcal{C}$ is non-transitive; $M$ (the within-stratum modulus)
is transverse to the orbits.** This settles the "action on 𝒞, or a second bundle?" joint in favour of a
**non-transitive action with transverse moduli**.

Consistency (real): the $M^2/r^6$ signature here is the *same* one in the codim-1 Gauss obstruction
$-3M^2/r^6$ (`scripts/f1_sds_codim1_test.py`, r227). "SdS is not a substrate-isometry image of dS" and
"SdS does not embed codim-1 in dS₅" are the same fact — so the codim-1 failure for matter was never a wall
against F1; it is the **correct algebroid structure** (a non-transitive action whose structure function
varies across the transverse modulus).

*Scripts:* `scripts/f1_orbit_transversality.py` (the gift's, re-run), `scripts/f1_orbit_transversality_independent.py`
(independent re-derivation: full Riemann → Ricci contraction, scalar checked two ways, constraint + $M{=}0$
cross-checks).

## 2. The per-stratum subalgebra identification (F2)  **[honest weight: dims established in P6 and verified at source; grading verdict FIRM — the symmetric cases geometry-pinned, the non-symmetric ones dimension-forced; the generator-realization softness cannot reach the verdict]**

Each P6 range/Petrov stratum embedded in $\mathfrak{so}(5,1)$, tested for the symmetric-space grading
$[\mathfrak{m},\mathfrak{m}]\subset\mathfrak{h}$:

| stratum | isotropy | dim (KV) | grading |
|---|---|---|---|
| Type O — dS/FLRW | $\mathfrak{so}(4,1)$ | 10 | **symmetric** |
| Type D — SdS | $\mathbb{R}_t\times \mathfrak{so}(3)$ | 4 | non-symmetric |
| Type D — Nariai | $\mathfrak{so}(2,1)\times\mathfrak{so}(3)$ | 6 | **symmetric** |
| Type D — Kerr–dS | $\mathbb{R}\times\mathfrak{so}(2)$ | 2 | non-symmetric |
| Type I — Bianchi I | 3 KV (abelian) | 3 | non-symmetric |
| Type I — Zipoy/Weyl | $\mathbb{R}\times\mathfrak{so}(2)$ | 2 | non-symmetric |
| wall — Type N | none | 0 | non-symmetric |

The **isotropy dimensions are the honest Killing-vector counts P6 establishes** (range_paper Thm/Props,
§§51/97/159: O→so(4,1); SdS R×SO(3); Nariai SO(2,1)×SO(3) the frozen-2-sphere seam; Kerr–dS R×SO(2);
Bianchi I 3 KV; Zipoy 2 KV; wall 0) — checked at source, **not modeled**. The two **symmetric** cases are
known symmetric-space facts ($\mathrm{dS}_5=SO(5,1)/SO(4,1)$; the Nariai block-diagonal
$SO(5,1)\supset SO(2,1)\times SO(3)$ Grassmannian pair), and "non-symmetric elsewhere" is robust (a generic
2-/4-dim subgroup of $\mathfrak{so}(5,1)$ is not a symmetric subgroup). **Verdict: clean symmetric-space
grading survives at {Type O, Nariai} only; everywhere else the structure function genuinely varies — this
*is* the algebroid connection.** **Soft spot resolved (verified at source, 2026-06-14).** The P6 isotropy types/dimensions are confirmed by reading P6 directly (`range_paper.tex` §§51/65/90/97/159: the de Sitter geometry's full isometry is $SO(4,1)$; SdS $\mathbb{R}_t\times SO(3)$; Nariai $=\mathrm{dS}_2\times S^2$, hence $SO(2,1)\times SO(3)$, the frozen-2-sphere seam; Kerr–dS and Zipoy $\mathbb{R}\times SO(2)$; Bianchi I three abelian KV; wall $0$ — Killing-*vector* counts, which P6 §162 makes the governing measure, not the Carter Killing tensor). And the generator-realization softness cannot threaten the verdict: the symmetric-pair isotropy dimensions of $\mathfrak{so}(5,1)$ are exactly $\{6,7,10\}$ (computed, `f1_so51_independent_check.py`), so the two symmetric strata sit at the only symmetric-permitting dimensions and are the geometry-pinned pairs ($\mathrm{dS}_4$'s $SO(4,1)$, dim 10; $\mathrm{dS}_2\times S^2$'s $SO(2,1)\times SO(3)$, dim 6), while every generic stratum (dims $4,3,2,0\notin\{6,7,10\}$) is non-symmetric by dimension alone, independent of which generators realize it. The verdict is firm.

*Script:* `scripts/f1_per_stratum_subalgebra_id.py`.

## 3. Reconfirmations of standing results  **[computed; reconfirm]**

- `scripts/f1_so51_independent_check.py` (now clean — the trailing coset-signature crash fixed): rebuilds
  $\mathfrak{so}(5,1)$ from scratch (dim 15), the proper symmetric-subalgebra dims $\{6,7,10\}$, the grading
  at Type O (dim 10) and Nariai (dim 6), the failure at SdS (dim 4), and the Type-O coset Killing-form
  signature $(1,4)$ Lorentzian (eigenvalues $[-2,-2,-2,-2,+2]$). Independent reconfirmation of r225.
- `scripts/f1_twofaces_exhaustiveness.py`: the SdS horizon cubic $r^3-\alpha^2 r+2M\alpha^2$, discriminant
  $-4\alpha^4(27M^2-\alpha^2)$, double root $\Lambda M^2=1/9$ (Nariai). Reconfirms Move 11; **honestly states
  exhaustiveness is not closed** — it is pinned to the per-stratum subalgebra ID, the same open computation
  as the term-for-term step below.

## 4. What stays OPEN — the term-for-term bracket homomorphism  **[reach — open exactly as r227]**

The full bracket-level homomorphism — that the base-variation **is** the $\mathfrak{so}(5,1)$-action on
$\mathcal{C}$ **term for term** — is **not closed**. The r223 "F1 CLOSED" was an over-claim (corrected r224);
the gift's "RESOLVED" headline is the same over-claim recurring and is discarded. The transversality result
(§1) **sharpens what closure would mean** — a non-transitive action with $M$ a transverse modulus, the
structure-function variation across the modulus being the algebroid connection rather than a failure of
closure — but does not establish it. The open path is **intrinsic closure through P3's slicing curve** (the
codim-1/embedding route being dead for matter, r227), pinned to Move 4's dimensional reconciliation
(gravity-minimal $\mathrm{dS}_5$ vs gauge-capable $\mathrm{dS}_6/M^7$). This is the Entry-5 single-carrier
test: F1 closing intrinsically would be the slicing curve carrying the continuous (matter = bend) face;
it can still return *no*.

**First step done (2026-06-14, `scripts/f1_intrinsic_carrier.py`) [reach — verified; scope held].** The
intrinsic carrier exists and is identified. The slicing surface $ds^2=dl^2+r^2\,d\phi^2$ (P3
`SdS-slicing-curve` §curvature) has Gaussian curvature $K_G=-f'/(2r)=1/\alpha^2-m/r^3+4\pi\rho$, so the
matter density $\rho$ (the bend, `slicing_operator`) sits *literally* in the surface's **intrinsic**
curvature — Theorema Egregium, from the first fundamental form, embedding-free. So the codim-1 embedding's
death (SdS class 2) does **not** block the intrinsic route: the extrinsic embedding is dead, the intrinsic
$K_G$ is alive and carries the matter. The connection is intrinsic too — the HDA structure-function
variation $\partial_M h^{rr}=-2/r$ (the $[\mathfrak{m},\mathfrak{m}]\to\mathfrak{m}$ leak) and
$\partial_M K_G=-1/r^3$ are the same $f$-bend read in the 3-leaf and the 2-surface
($K_G=-\partial_r h^{rr}/2r$), with $^3R=(2/r^2)(1-f)+4K_G$ tying the leaf's Hamiltonian anchor
($^3R=2\Lambda$ in vacuum) to the surface curvature. **What this does NOT yet show:** that the full
bracket-level (smeared, infinite-dim) HDA homomorphism *closes* through this carrier — that is the open
field-theoretic completion. The step removes the embedding-death objection and identifies the carrier; the
bracket closure through it is the next sub-step. **[reach — the carrier established and intrinsic; the
bracket closure through it open]**

**Second step (2026-06-14, `scripts/f1_grading_through_KG.py`) [reach — verified; scope held].** The
*grading itself* closes through the intrinsic carrier. By the symmetric-space principle
($[\mathfrak{m},\mathfrak{m}]\subset\mathfrak{h}\Leftrightarrow$ covariantly-constant curvature), the
symmetric strata are exactly the slicing curve's two constant-curvature configurations: $M=0$
($K_G\equiv1/\alpha^2$, de Sitter, Type O, $\mathfrak{so}(4,1)$ dim 10) and the Nariai double root
(horizon-cubic discriminant $-4(27M^2-1)=0$ at $M=\sqrt3/9$, $r_N=1/\sqrt3$, turning points merged
$\to\mathrm{dS}_2\times S^2$, the constant-curvature product, $SO(2,1)\times SO(3)$ dim 6). These are
precisely the $\{$Type O, Nariai$\}$ of §2, and the leak (the algebroid connection) is exactly where $K_G$
varies ($\partial_r K_G=3M/r^4$, the vacuum mass $M$ — a straight cut, distinct from the matter bend $m'\neq0$). No ambient embedding enters: $K_G$ is intrinsic, the
turning-point/cubic structure the curve's own. So the grading — the bracket's closing-vs-leaking — closes
through the intrinsic carrier. **Remaining open:** the term-for-term *smeared, infinite-dim* identity — the
Dirac bracket coefficients equal to the $\mathfrak{so}(5,1)$ structure constants quantitatively, the leak
$=$ the specific $\mathfrak{m}$-component $=\nabla K_G$ — the field-theoretic completion. **[reach — the
carrier and the grading both reproduced intrinsically through the slicing curve; the term-for-term smeared
closure open]**

**Third step (2026-06-14, `scripts/f1_smeared_bracket_KG.py`) [reach — verified; structure-function level].**
The actual *smeared* HDA bracket closes through the intrinsic carrier at the structure-function level: for
radial lapses on the slicing-curve leaf, $\{\mathcal{H}_\perp[N],\mathcal{H}_\perp[M]\}=\mathcal{H}_r[f(NM'-MN')]$
— closing on the tangential constraint with coefficient $h^{rr}=f$, the $K_G$-carried object, constant at
$M=0$ (genuine Lie) and varying off it (genuine algebroid, the variation $\partial_M h^{rr}=-2/r$ the
connection). This is the standard HDA combined with steps 1–2, made explicit at the smeared bracket. **The
genuinely deepest remaining piece is the *mode* level:** the finite $\mathfrak{so}(5,1)$ structure constants
matched term-for-term to specific smeared lapse modes — $\mathfrak{so}(5,1)$ realized as the finite-dim
isometry-generating-mode subalgebra inside the infinite-dim HDA, the bracket of two coset-modes reproducing
$[X,Y]\in\mathfrak{h}$ quantitatively, the non-isometry modes the genuine field degrees of freedom. **[reach —
the structure-function level of the smeared closure done; the finite-mode subalgebra term-for-term is the
remaining research step]**

**Fourth step (2026-06-14, `scripts/f1_mode_level_closure.py`) [reach — verified, decisive at the symmetric
cut].** The finite-mode subalgebra closes term-for-term **at the symmetric (de Sitter) cut**. The coset
generator $M_{a5}=X_a\partial_5-X_5\partial_a$ is purely normal at the cut $X_5=0$ (lapse $N_a=X_a$, the de
Sitter harmonics; zero shift), so the smeared bracket of two coset-lapse modes is
$\xi^c=h^{cd}(X_a\partial_d X_b-X_b\partial_d X_a)$. On the dS$_4$ static-patch spatial leaf this reproduces
the isotropy Killing vectors exactly: $\{X_1,X_2\}\to\partial_\phi=M_{12}$, $\{X_4,X_1\}\to M_{41}$,
$\{X_1,X_3\}\to M_{13}$, each verified Killing ($\mathcal{L}_\xi g_{\rm leaf}=0$). So $\mathfrak{so}(5,1)$ is
realized as the isometry-generating-mode subalgebra inside the HDA: $[\mathfrak{m},\mathfrak{m}]\subset
\mathfrak{h}$ holds at the **mode** level, reproducing $[M_{a5},M_{b5}]=M_{ab}$ (adm\_so51\_1) through the
actual smeared bracket — the term-for-term smeared homomorphism at the symmetric cut. **Remaining [reach]:**
(a) the off-symmetric (matter) cuts — the same modes' Killing-failure $=$ the connection $=\nabla K_G$ at the
mode level (needs the slicing-curve embedding of the matter leaf in dS$_5$); (b) the non-isometry modes as
the genuine field degrees of freedom. The $SO(3)$ sub-closure ($\{X_1,X_2\}\to\partial_\phi$) is manifestly
retained at every cut. **[reach — the mode-level term-for-term closure established at the symmetric cut; the
matter-cut connection and the field-DOF statement remain]**

**Fifth step (2026-06-14, `scripts/f1_offsymmetric_mode_leak.py`) [reach — verified; vacuum-M scope].** The
symmetric-cut closure of step 4 *leaks* off the symmetric cut, and the leak is the connection. On the vacuum
SdS leaf ($M\neq0$): the retained $SO(3)$ mode $\{X_1,X_2\}\to\partial_\phi$ stays Killing for all $M$, but
the broken dS-translation $\{X_4,X_1\}$ — which closed as the isometry $M_{41}$ at $M=0$ — is no longer
Killing: $\mathcal{L}_\xi g\neq0$, every component carrying a factor $M$, all vanishing at $M=0$ (recovering
step 4). The leak enters solely through $h^{rr}=f$ in $\xi^\rho$, whose $M$-variation $\partial_M f=-2/\rho$
is the structure-function connection (steps 1–3). So the $[\mathfrak{m},\mathfrak{m}]\to\mathfrak{m}$ leak
*is* that connection, at the mode level — and the full per-stratum grading is now realized at the mode level
end to end: closure into $\mathfrak{h}$ at the symmetric cut, connection-leak into $\mathfrak{m}$ off it,
$SO(3)$ retained throughout. **Precision:** this leak is the *vacuum mass* $M$ (a straight cut,
$SO(4,1)\to\mathbb{R}_t\times SO(3)$), not matter; the matter bend ($m'\neq0$, the $+4\pi\rho$ in $K_G$) is a
distinct further source. **Remaining [reach]:** the genuine matter mode level ($m'\neq0$); the non-isometry
modes as field DOF; and no closed-form $\nabla K_G$ identity is claimed (only that the leak is driven by
$\partial_M f$ and vanishes at the symmetric stratum). **[reach — the per-stratum grading realized at the mode
level, closure and connection-leak both; the matter-bend mode level and the field-DOF statement remain]**

**Sixth step (2026-06-14, `scripts/f1_matter_mode_leak.py`) [reach — verified].** Turning on genuine matter
($m'(r)\neq0$, density $\rho=m'/4\pi r^2$, the bend) shows the mode-level connection-leak *splits by
component*. The retained $SO(3)$ mode $\{X_1,X_2\}\to\partial_\phi$ stays Killing for any $m(r)$; the broken
dS-translation $\{X_4,X_1\}$ leaks, and the leak separates: the **angular** components carry the *enclosed
mass* $m(r)$ only (no $m'$), while the **radial** component carries the *matter density* $m'(r)$. The
genuine-matter piece of the radial leak is exactly linear in $m'$, vanishes iff $m'=0$ (vacuum straight cut),
and in terms of the density reads $8\pi\alpha^2 r^2\rho\,\sin\theta\cos\phi/[\sqrt{\alpha^2-r^2}\,(-\alpha^2
r+2\alpha^2 m+r^3)]$. So genuine matter — the bend, the density — *does* source the mode-level connection,
distinctly through the radial leak, mirroring $K_G$'s mass/matter split ($-m/r^3$ vs $+4\pi\rho$); the vacuum
limit $m=M$ recovers step 5. **Scope [reach]:** the component structure (mass$\to$angular,
density$\to$radial) is the finding; no closed-form $\nabla K_G$ identity is claimed. **[reach — the
per-stratum grading and its connection realized at the mode level for vacuum (mass) and matter (density)
alike; the non-isometry modes as the genuine field degrees of freedom remain the deepest open piece]**

**Seventh step (2026-06-16, r270, `scripts/f1_full_bracket_table_symmetric.py`) [reach — verified; symmetric-cut, spatial-isometry scope].** Step 4 closed only $[\mathfrak{m},\mathfrak{m}]\subset\mathfrak{h}$ at the mode level. This completes the **full mode-level bracket table at the symmetric (de Sitter, $M=0$) cut**, in step 4's exact construction (the $S^3$ spatial leaf, the coset-lapse modes $X_a$, $\xi_{ab}:=$ HDA$\{X_a,X_b\}$). All three bracket types close term-for-term through the smeared HDA bracket: $[\mathfrak{m},\mathfrak{m}]\subset\mathfrak{h}$ ($\xi_{ab}$ Killing, re-verified for all six $a<b$); $[\mathfrak{h},\mathfrak{m}]\subset\mathfrak{m}$, i.e. $\mathcal{L}_{\xi_{ab}}X_c=\delta_{bc}X_a-\delta_{ac}X_b$ exactly (the $X_c$ transform as an $\mathfrak{so}$-vector); and $[\mathfrak{h},\mathfrak{h}]\subset\mathfrak{h}$, i.e. $[\xi_{ab},\xi_{cd}]_{\mathrm{Lie}}=\delta_{bc}\xi_{ad}-\delta_{ac}\xi_{bd}-\delta_{bd}\xi_{ac}+\delta_{ad}\xi_{bc}$ exactly (the $\mathfrak{so}(4)$ structure constants). Normalization is **unit** — $\xi_{12}=\partial_\phi=M_{12}$, no spurious constant — so $M_{a5}\mapsto\mathcal{H}_\perp[X_a]$, $M_{ab}\mapsto\mathcal{H}_a[\xi_{ab}]$ is a genuine Lie-algebra homomorphism, not merely a grading match. **So the finite isometry subalgebra is realized as a *closed* subalgebra inside the infinite-dim HDA at the symmetric cut — the whole bracket table, not just its coset-coset part** (the piece step 3 named the deepest of the symmetric-cut closure). **Honest scope [reach]:** (i) the spatial leaf ($t=0$) carries the compact spatial-rotation sector ($\mathfrak{so}(5)\supset\mathfrak{so}(4)$: 4 coset-lapse modes + 6 isotropy rotations); the boosts and the full $(5,1)$ signature involve the time direction $X_0$, not carried by the $t=0$ spatial bracket. (ii) Symmetric ($M=0$) cut only — off it the closure *leaks* (steps 5–6, the connection). (iii) Isometry modes only — the non-isometry modes as field DOF remain the separate past-the-wall frontier (the genuine infinite-dim completion). This firms the finite-mode term-for-term homomorphism fully at the symmetric cut; it does **not** close the infinite-dim completion. **[reach — the full finite spatial-isometry bracket table closes term-for-term inside the HDA at the symmetric cut, unit normalization; the boosts, the off-symmetric leak (=connection, done for [m,m]), and the field-DOF completion remain]**

**Eighth step (2026-06-16, r271, `scripts/f1_offsymmetric_full_bracket_table.py`) [reach — verified; off-symmetric vacuum-M, spatial scope].** The off-symmetric ($M\neq0$) companion to step 7: steps 5–6 leaked only $[\mathfrak{m},\mathfrak{m}]$ off the symmetric cut, step 7 closed the full table *at* $M=0$ — this completes the full table *off* it, in step 5's construction (SdS leaf $f=1-2M/\rho-\rho^2/\alpha^2$, the same $X_a$, $\xi_{ab}:=$HDA$\{X_a,X_b\}$, now $M$-dependent). **Result:** the $SO(3)$ rotation subalgebra ($\xi_{12},\xi_{13},\xi_{23}$ and their action on $X_1,X_2,X_3$) is retained **exactly for all $M$** — a genuine closed subalgebra off the symmetric cut — across both $[\mathfrak{h},\mathfrak{m}]$ ($\mathcal{L}_{\xi_{12}}X_1=-X_2$ etc., $M$-free) and $[\mathfrak{h},\mathfrak{h}]$ ($[\xi_{12},\xi_{13}]$ the $\mathfrak{so}(3)$ structure constant, $M$-free). The broken (dS-translation, $X_4$-involving) sector carries the **connection-leak**: in $[\mathfrak{h},\mathfrak{m}]$, $\mathcal{L}_{\xi_{14}}X_1=-X_4+\,2M\alpha^2\sin^2\theta\cos^2\phi/[\rho\sqrt{\alpha^2-\rho^2}]$ — the deviation linear in $M$, vanishing at $M=0$ (recovering step 7); and in $[\mathfrak{h},\mathfrak{h}]$ where the bracket should return a *retained* generator, e.g. $[\xi_{14},\xi_{24}]=-\xi_{12}+O(M)$, the $O(M)$ the leak. **Nuance (kept, not flattened):** the leak is **not** blanket on every broken bracket — $[\xi_{14},\xi_{12}]=\xi_{24}$ closes **exactly for all $M$** (two $M$-covariant generators bracketing consistently); the leak enters specifically where the connection $\partial_M f=-2/\rho$ (steps 1–3) enters, i.e. where the bracket would cross from the $M$-covariant broken sector to an $M$-invariant ($SO(3)$/mode) target. **So the mode-level algebroid picture is now complete for the whole bracket table:** a Lie algebra at the symmetric cut (step 7, all three types close term-for-term) and an algebroid off it (this step, the $SO(3)$ isotropy $M$-invariant, the connection $\partial_M f$ the leak across all types) — extending steps 4–6's $[\mathfrak{m},\mathfrak{m}]$-only grading to $[\mathfrak{h},\mathfrak{m}]$ and $[\mathfrak{h},\mathfrak{h}]$. **Honest scope [reach]:** same as step 7 — spatial ($\mathfrak{so}(5)\supset\mathfrak{so}(4)$) sector; the boosts/full $(5,1)$ (time-normal sector, the timelike coset $M_{05}=\varepsilon$/deparametrization, overlapping the lock), and the non-isometry field-DOF infinite-dim completion, remain. **[reach — the per-stratum grading realized at the mode level for the full bracket table, closure at the symmetric cut and connection-leak off it; the time/boost sector and the field-DOF completion remain]**

**Ninth step (2026-06-16, r272, `scripts/f1_time_boost_sector_chart.py`) [reach — charting result; finite so(5,1) complete].** The time/boost sector, charted by classifying all 15 dS$_5$ Killing vectors at the leaf (the $S^3$, $X_0{=}X_5{=}0$, two normals: the substrate-$\chi$ $e_5$ and the spacetime-time $e_0$). The split is exact: **6 tangential** ($M_{ab}$, the $SO(4)$ rotations — shift; r270/r271); **4 $\chi$-normal lapse** ($M_{a5}$, profile $X_a$; r270/r271); **4 time-normal lapse** ($M_{0a}$, the boosts, profile $X_a$ in the $e_0$ direction) — these close by the **identical leaf-metric HDA bracket** as the $\chi$-normal modes (verified: $\{\mathcal{H}_\perp[X_1],\mathcal{H}_\perp[X_2]\}\to\partial_\phi=M_{12}$, the standard spacetime ADM Dirac bracket, same result as r270); and **1 cross-normal** ($M_{05}$, the $(0,5)$ boost) which **vanishes at the leaf** — it is the generator relating the substrate-slicing normal ($\chi$) to the spacetime-time normal ($t$), i.e. the deparametrization / one-clock direction, **the F1$\leftrightarrow$lock bridge** built by the lock (r246–r250) and the one-clock test (r268), not a fresh leaf computation. **So the finite $\mathfrak{so}(5,1)$ mode realization is complete:** the spatial sector explicit (r270/r271, closure + connection), the boost sector the time-normal copy by identical structure, and $M_{05}$ the lock-bridge. **The sole remaining OPEN F1 piece is therefore the infinite-dim field-DOF completion** — the non-isometry modes, the field-theoretic Gowdy–dS model, which is **consolidated and re-verified** (Plan Moves 2–3, r190/r191: `corpus/dynamics_frontier_gowdy-dS_canonical.md` + `scripts/gowdy_ds_*.py`, all receipts clean-zero — *not* the stale "unconsolidated/un-re-verified in `archive/`" status, which was the r186 starting-state line carried forward; corrected r273). So the open work is not a re-verification but the model's own open frontier: the **nonlinear Λ>0 evolution / FORCE-vs-ADMIT** (`dynamics_frontier_gowdy-dS_canonical.md` §6, §9), whose first bite — the de Sitter background and the cosmic-time clock that replaces the failed area-time gauge — is computed at r273 (`scripts/gowdy_ds_lambda_pos_background.py`); the graviton back-reaction is next. **[reach — the finite so(5,1) charted complete across all sectors; the only open F1 tail is the infinite-dim field-DOF = the nonlinear Λ>0 dynamics frontier, now underway]**

## 4a. The intrinsic realization, consolidated — steps 1–6 as one result  **[reach — the grading and its connection realized intrinsically from carrier to mode level, vacuum and matter, closing the symmetry-reducible sector; the field DOF a separate past-the-wall frontier]**

Steps 1–6 are one reach with one through-line: **through P3's slicing curve, with no ambient embedding, the per-stratum grading of §2 and its algebroid connection are realized intrinsically at every level from the carrier up to the finite isometry-generating-mode subalgebra — for vacuum (mass) and matter (density) alike.** The codim-1 embedding route is dead for matter (SdS class 2, r227); this arc is the intrinsic route that death does not block. The levels, in order:

- **Carrier (step 1).** The matter density sits literally in the slicing surface's *intrinsic* Gaussian curvature $K_G=1/\alpha^2-m/r^3+4\pi\rho$ (Theorema Egregium, from the first fundamental form), and the connection is intrinsic with it: $\partial_M h^{rr}=-2/r$ in the 3-leaf and $\partial_M K_G=-1/r^3$ in the 2-surface are one $f$-bend read two ways. The carrier exists, is intrinsic, and survives the embedding-death.
- **Grading (step 2).** The symmetric strata are exactly the curve's two constant-curvature configurations — $M=0$ (de Sitter, Type O) and the Nariai double root ($\mathrm{dS}_2\times S^2$) — matching §2's $\{$Type O, Nariai$\}$, the leak located where $K_G$ varies. The closing-vs-leaking grading is reproduced through the intrinsic carrier.
- **Smeared closure, structure-function level (step 3).** The full (infinite-dim) smeared HDA bracket closes: $\{\mathcal{H}_\perp[N],\mathcal{H}_\perp[M]\}=\mathcal{H}_r[f(NM'-MN')]$ for arbitrary radial lapses, coefficient $h^{rr}=f$ the $K_G$-carried object — Lie at $M=0$, algebroid off it ($\partial_M f$ the connection).
- **Finite-mode subalgebra, term-for-term (steps 4–6).** Inside that infinite-dim HDA the isometry-generating modes are the de Sitter harmonics $X_a$, and their smeared bracket reproduces $\mathfrak{so}(5,1)$ term-for-term. It **closes into $\mathfrak{h}$ at the symmetric cut** ($\{X_a,X_b\}\to M_{ab}$ Killing, reproducing $[M_{a5},M_{b5}]=M_{ab}$; step 4) and **leaks into $\mathfrak{m}$ off it — the connection at the mode level** — for both the **vacuum mass** ($\{X_4,X_1\}$ leaks $\propto M$, vanishing at $M=0$, driven by $\partial_M f$; step 5) and **matter density** (the leak splits: enclosed mass $m\to$ angular, density $m'\to$ radial, the matter piece linear in $m'$ and reading $\to\rho$; step 6), the split mirroring $K_G$'s $-m/r^3$ vs $+4\pi\rho$. $SO(3)$ ($\{X_1,X_2\}\to\partial_\phi$) is retained at every cut.

**So the grading and its connection are realized intrinsically and at the mode level, end to end — this arc closes the algebroid's actual home, the symmetry-reducible (range/Petrov) sector.** What stays open divides into one internal caveat and one separate frontier. **Internal caveat — resolved (r267, `f1_leak_gradKG_identity.py`):** the closed-form $\text{leak}=\nabla K_G$ identity does **not** hold, and the obstruction is structural, not a missing simplification. $K_G=1/\alpha^2-m/r^3+4\pi\rho$ carries the density term $4\pi\rho=m'/r^2$, so $\nabla K_G=\partial_r K_G=(r^2m''-3rm'+3m)/r^4$ carries $m''$ (and the Hessian $m'''$), while the mode-level leak $\mathcal{L}_\xi g$ is a function of $(m,m')$ **only** — a derivative-order mismatch no simplification can bridge. The leak's *positive* closed form is therefore the **transverse-modulus data itself**: the angular components are exactly linear in the enclosed mass ($\mathcal{L}_\xi g_{\theta\theta}/m=-4\alpha^2\sin\theta\cos\phi/\sqrt{\alpha^2-r^2}$, independent of $m,m'$), the radial carries the density $m'$ — the mass$\to$angular / density$\to$radial split confirmed exactly. So the connection is a **transverse-modulus ($\partial_M$) object — the bend/density itself — not the spatial gradient of the intrinsic curvature**; the earlier "*driven by* $\partial_M f$" is now the verdict, with $\nabla K_G$ positively ruled out. **[reach — for the one-clock test (Entry 8): this pins the connection's *transverse* face in closed form as the modulus data $(m,m')$ and rules out $\nabla K_G$ as that face; it sharpens but does not resolve the test, whose along-orbit trivialization is untouched here.]** **Separate frontier (not an unfinished corner of this arc):** the genuine field degrees of freedom. The grounding places these correctly (`algebroid_closure_consolidation.md` §8, vision journal Entry 5): $\mathfrak{so}(5,1)$ is finite and the algebroid is the home of the symmetry-reducible sector; the wall (isotropy$\to0$, Type N) is its boundary, and *past the wall the free transverse degrees of freedom — the graviton's two polarizations — take over* (Move 8). By Birkhoff the symmetry-reducible sector has no local gravitational DOF, so the field DOF are not a leftover of steps 1–6 but the separate past-the-wall dynamics frontier (the recovered Gowdy–dS field-theoretic model). Receipts: `f1_intrinsic_carrier.py`, `f1_grading_through_KG.py`, `f1_smeared_bracket_KG.py`, `f1_mode_level_closure.py`, `f1_offsymmetric_mode_leak.py`, `f1_matter_mode_leak.py`, `f1_leak_gradKG_identity.py`, `f1_full_bracket_table_symmetric.py` (r270 — full finite-isometry table closed at the symmetric cut), `f1_offsymmetric_full_bracket_table.py` (r271 — the same table off the symmetric cut: SO(3) retained, the connection-leak across all types), `f1_time_boost_sector_chart.py` (r272 — the time/boost sector charted; finite so(5,1) complete, M_05 the F1↔lock bridge).

## 4b. The handoff to dynamics — the intrinsic curvature is the single carrier of the bend, static and dynamical  **[reach — carrier-level handoff verified; the full connection$=$dynamics identity open]**

§4a closes the algebroid's home (the symmetry-reducible sector) and places the genuine field DOF past it — the propagating graviton, worked in the Gowdy–dS canonical model at the Type-I edge (isotropy 2; re-verified `adm_dynamics_1.py`: $\partial_x,\partial_y$ Killing, $\partial_t,\partial_z,$ boost broken by a generic wave). This subsection records the first carrier-level bridge between the two (Move 8); receipt `f1_move8_carrier_handoff.py`.

The bridge is the **intrinsic curvature**. Step 1 put the static bend (matter density $\rho$) in the slicing surface's intrinsic curvature $K_G$, and steps 5–6 made its moduli-variation the algebroid connection. The Gowdy leaf's intrinsic curvature $^3R$ **contains the graviton gradient $\psi_z^2$** — the propagating bend sits in the intrinsic curvature too — and the graviton's potential energy in the *true* Hamiltonian ($2R\psi_z^2$) **equals** the lapse-weighted intrinsic-curvature term $N\sqrt h(-{}^3R)$ ($N=e^{\gamma-\psi}$ the Gowdy lapse; both $2R$, exact). So the field-DOF energy is carried by the leaf's intrinsic curvature — the same type of object that carries the static matter bend and whose moduli-variation is the connection. The intrinsic curvature is the **single carrier of the bend across the static/dynamical divide** — Entry 5's single-carrier picture realized at the intrinsic-curvature/Hamiltonian level.

**Scope [reach].** (i) This is a *carrier-level* link — both faces ride on the intrinsic curvature — **not** a proof that the algebroid connection literally *equals* the graviton dynamics as one equation; that full identity stays open. (ii) The full reduced Gowdy $\mathcal{H}$ is *not* literally $\sqrt h(2\Lambda-{}^3R)$: the area/clock-sector terms ($R_z\gamma_z$, $R_{zz}$) differ by the reduction's IBP; the clean match is the graviton/bend ($\psi_z^2$) piece, the field-DOF content. (iii) Sector note (face 14): steps 1–6 are the spherical ($SO(3)$) sector, the Gowdy edge the planar ($T^2$) sector — this is the common intrinsic-curvature carrier *across* sectors, not a within-sector continuation of one leaf into the other.

## 4c. The carrier's boundary — the intrinsic-curvature carrier ends exactly at the wall  **[reading — synthesis of §4b (computed) + the range theorem (established) + the wall's VSI (computed)]**

§4b carried the bend's single carrier (the leaf's intrinsic curvature) down the algebroid ladder to the Type-I edge — the confined Gowdy graviton, the last cut. This locates where that picture ends: exactly at the wall. Two grounded legs:

- **Past the wall is not a cut (range theorem).** Past the wall the geometry has no continuous symmetry (`range_paper.tex` §wall), hence no sweep-subgroup of $SO(4,1)$, hence it is not reachable as a slicing/cut of the substrate — it is ordinary evolution, a non-isometry primitive the corpus does not carry. (`pastwall_typeN_1.py`: the explicit dS-conformal pp-wave ansatz *fails* for exactly this reason — the dS conformal factor sits on $u+v$, which contains the wave's null direction — and the cut-vs-evolution verdict is settled first-hand by the range theorem, not the ansatz.) The §4b carrier is the *cut's* intrinsic curvature; with no cut past the wall, there is no cut-curvature to carry the bend there.
- **The wall is VSI (`wall_ppwave_check.py`).** Ricci scalar and Kretschmann both vanish; all polynomial curvature invariants are zero. So even the free wave's content is not in the curvature scalars — it lives in the null radiative ($R_{uu}$) sector, to which the intrinsic-curvature *scalar* carrier is blind.

So the carrier arc is complete and bounded: the intrinsic curvature carries the bend through the entire symmetry-reducible ladder up to the last cut (the Type-I edge), and **its boundary is exactly the wall**, coinciding with the algebroid's boundary. Past the wall is the open dynamics frontier (Move 9/10): ordinary evolution of a free radiative DOF whose content is null-radiative, not a cut's curvature. This *demarcates* where the single-carrier picture holds and where the genuinely-new past-wall regime begins; it does not cross that boundary. **[reading — the boundary located by established + computed pieces; the past-wall dynamics remain open]**

## 5. The base coordinate — the transverse modulus folds at the Nariai seam  **[computed cross-check; reading for the placement]**

The base $\mathcal{C}$ is the slicing offsets $r_0$ (observer-2), with the mass tied to the offset by P3's
map $2M=\alpha(u-u^3)$, $u=r_0/\alpha$ (`algebroid_base_and_substrate.md` §2). Since the
$\mathfrak{so}(5,1)$-action carries a cut to an *isometric* cut (fixed $M$ — §1 transversality), $M(r_0)$
is the coordinate **transverse** to the orbits. Computing that map (`scripts/f1_offset_modulus_fold.py`):
it rises from $M=0$ at the centered cut, is stationary at $u=1/\sqrt3$ with $M=\alpha/(3\sqrt3)$, i.e.
$\Lambda M^2=1/9$ — **exactly the Nariai double root** (cross-checked against the horizon-cubic discriminant
$-4\alpha^4(27M^2-\alpha^2)$, same value by an independent route) — then falls. So the offset coordinate
covers the Type-D family up to the maximal (Nariai) mass, **two-to-one below the fold**, the fold sitting on
the metric-singular seam.

**Placement (answers the §4 open question at the orbit level).** Combined with §1, this fixes the
orbit structure of $\mathcal{C}$ under $\mathfrak{so}(5,1)$: the action is **non-transitive**, $\mathcal{C}$
is **not** a homogeneous $\mathfrak{so}(5,1)$-space, and $M(r_0)$ is the continuous **transverse modulus**
labelling the orbits, folding at Nariai — *not* a second structure-group (the observer-1 discrete vantage
$\sigma$ is the separate $\mathbb{Z}_2$ already distinguished from the continuous $\mathfrak{so}(5,1)$). So
the term-for-term homomorphism is the **along-orbit** (fixed-$M$) statement — the symmetric-space grading at
the symmetric cut (Move 6), the firmed structure-function form at the SdS/Type-D orbit (r225) — while the
structure function's variation across the transverse modulus (folding at the seam) is the **algebroid
connection**, not a closure failure. **Still open [reach]:** full closure across $\mathcal{C}$ remains pinned
to the leaf$\leftrightarrow$coset (3-dim Riemannian leaf vs 5-dim $(1,4)$ coset) reconciliation — Move 4's
open dimensional sub-axis — which the next move attacks.

## 6. The leaf↔coset reconciliation — the dimensional pin, settled by computation  **[computed for the vacuum; the matter bound established]**

The pin on the term-for-term homomorphism was the 5-dim coset vs 3-dim leaf mismatch (Move 4's open
dimensional sub-axis). Computed at source (`scripts/f1_leaf_coset_reconciliation.py`, building on the
verified dS₄-in-dS₅ slice `f1_4d_in_5d_slice.py`): the dS₅ static patch has spatial $S^3=d\chi^2+\sin^2\chi\,
d\Omega_2^2$, and the (1,4) coset tangent decomposes exactly as

$$(1,4)\;=\;\underbrace{(\rho,\theta,\phi)}_{\text{3 spacelike, Riemannian}}\;\oplus\;\underbrace{t}_{\text{1 timelike}}\;\oplus\;\underbrace{\chi}_{\text{1 spacelike}},\qquad (0,3)+(1,0)+(0,1)=(1,4).$$

- the **3-spacelike leaf block** $(\rho,\theta,\phi)$ is the HDA structure function: inverse leaf metric
  $h^{ab}=\mathrm{diag}(f,\,1/\rho^2,\,1/(\rho^2\sin^2\theta))$, $h^{rr}=f=1-\rho^2/\alpha^2$ — the $M{=}0$ SdS
  leaf form, the same leaf the transversality result (§1) used;
- the **timelike** direction $t$ is the lapse — the problem-of-time sign $\varepsilon$;
- the **spacelike** direction $\chi$ is the **5th dimension**: the extra $S^3$ angle, the totally-geodesic
  codim-1 normal ($K=0$ at $\chi=\pi/2$, r227). dS₄ $=\{\chi=\pi/2\}$.

So the 3-dim Riemannian leaf metric **is** the 3-spacelike block of the 5-dim coset, and P5/P6's
dimension-agnostic "1-D curve on a 2-D section swept by $SO(3)$" builds exactly that block (the curve is
the $\rho$ direction, the $SO(3)$ sweep the $S^2=(\theta,\phi)$). The dimension-agnostic framing was
describing the **leaf**; the dS₅-codim-1 picture adds the timelike lapse and the spacelike $\chi$ — the two
square. **The 5th dimension is $\chi$.**

**What this settles for the term-for-term homomorphism (honest weight).** At the symmetric/vacuum cut
(Type O, dS₄) the coset **literally contains** the leaf as its 3-spacelike block, so the homomorphism closes
there exactly (Move 6, term-for-term) — consistent with the per-stratum grading being symmetric at {Type O,
Nariai} (§2). Turning on matter ($M\neq0$) deforms $h^{rr}=f$ by $-2M/r$ in a direction **transverse** to the
coset — SdS does **not** sit as a $\chi$-slice of dS₅ (class 2, $-3M^2/r^6$, §1), and $M$ is transverse to the
$\mathfrak{so}(5,1)$-orbits (§1), folding at Nariai (§5). So the homomorphism does **not** extend to matter by
the coset structure: the $M$-variation is the **algebroid connection**, not an action bracket.

**Resolution of F1's term-for-term question** (no over-claim): the naive form — *base-variation $=$ the
$\mathfrak{so}(5,1)$-action on $\mathcal{C}$ term-for-term, everywhere* — is settled **negatively**: it holds
along the orbits (vacuum/symmetric, where the leaf is the coset block) and not across the transverse modulus
(matter/$M$, the connection). The structural home is therefore **built and now dimensionally grounded** — an
action Lie algebroid with a non-transitive $\mathfrak{so}(5,1)$-action, the leaf the 3-spacelike coset block
at the symmetric cut, the transverse modulus the connection — which is what F1 was for. The remaining genuinely
open piece is narrower: the **full field-theoretic (smeared, infinite-dim) HDA** beyond the finite
$\mathfrak{so}(5,1)$ pattern, and the gauge-theoretic dS₅-vs-dS₆ horn (Move 13). **[the dimensional
reconciliation computed; the algebroid grounded; the field-theoretic completion + Move 13 remain]**
