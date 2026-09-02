# The anchor — the cut → stress-energy map and its four data
*Corpus consolidation note (the algebroid's **anchor map**, gathered from P5/P6 and the
`anchor_*`/`adm*` scripts; the momentum sector completed and lifted to the general-covariant
level at Move 5, r208, 2026-06-12). Not one of the 10 papers — a corpus support/spine note, like
the singularity-taxonomy and Gowdy–dS consolidations. All receipts clean-zero (sympy). Tags:
[established]/[computed]/[reading]/conjecture.*

## Why this exists
The **anchor** of the action Lie algebroid is the map from an infinitesimal cut-deformation to the
geometry/stress-energy it produces — the general-cut Einstein tensor as a functional of the cut
(`THE_VISION.md` §3). Its sectors were computed and verified piecemeal — the energy sector across
P5 (`slicing_operator.tex`) and `adm2`/`anchor_stress_1`, the momentum sector in `anchor_momentum_1`,
the stress sector in `anchor_stress_1` — but were **never consolidated into a corpus deliverable**, and
the momentum sector was never stated at the general-covariant level the energy sector reached, nor tied
to P6's $J=Ma$. This note gathers the four sectors as one functional of the cut and records the Move-5
completion. **[the anchor is the conjecture home; its four sectors are [computed], below]**

## The cut, and its four data
A cut is the 3+1 data the construction reads off the substrate, which are exactly the ADM data
(P5 §lapse, P6 §70 — *leaf · lapse · shift · vantage*):

| datum | ADM object | sector it sources | the matter content |
|---|---|---|---|
| **leaf** | 3-metric $\gamma_{ij}$ (the spatial cut) | energy (⊥⊥, Hamiltonian constraint) | $\rho$ = the **bend of the leaf** |
| **shift** | $N^i$ (frame-drag cross term) | momentum (⊥$i$, momentum constraint) | $j_i$ = the **bend of the shift** |
| **lapse** | $N$ (time-stacking) | stress ($ij$, evolution) | $S_{ij}$ = the **bend of the stacking** |
| **vantage** | radial signature | signature | hole ($f{>}0$) vs cosmos ($f{<}0$) |

Energy and momentum are the **constraints** (initial data on the leaf); stress is the **evolution**.
Vacuum is where the relevant bend vanishes. The throat $\alpha=\sqrt{3/\Lambda}$ is the one substrate scale.

## 1. Energy sector — $\rho$ is the leaf's bend (⊥⊥, the Hamiltonian constraint) **[computed; general]**
$$16\pi\rho = {}^3R + K^2 - K_{ij}K^{ij} - 2\Lambda,$$
the energy density as the leaf's intrinsic-curvature departure from the de Sitter substrate leaf.
- vacuum substrate leaf = round $S^3$, ${}^3R=2\Lambda$, $H=0$ — verified both vantages, $\sigma$ (the
  vantage flip) redistributing the *same* $2\Lambda$ between ${}^3R$ and $K^2-K_{ij}K^{ij}$
  (`scripts/adm2.py`, clean);
- spherical leaf: $\rho=m'(r)/4\pi r^2$, the radial growth-rate of enclosed mass — the bend off the
  constant-$M$ vacuum profile (`scripts/anchor_stress_1.py`; = P5 Prop bend; = C2). **[computed]**

## 2. Momentum sector — $j_i$ is the shift's bend (⊥$i$, the momentum constraint) **[computed; Move 5]**
$$16\pi j_i = -2\,D_j\!\left(K^{j}{}_{i} - \delta^{j}{}_{i}K\right),$$
with the shift entering through the extrinsic curvature; for a stationary cut
$K_{ij}=\tfrac{1}{2N}(D_iN_j+D_jN_i)$ — the shift's symmetrized gradient. So $j_i$ is a **clean
second-order functional of the shift datum alone**: the momentum sector **separates cleanly** (the
Move-5 *can-return* — "may not separate at the representational level" — resolved positively).
- spherical instance: a twisted SdS cut, shift $N^\phi=\omega(r)$, gives the frame-drag ODE with
  vacuum solution $\omega = C_0 + 2J/r^3$ ($C_0$ the rigid co-rotation, $2J/r^3$ the localized mode,
  $\Lambda$ cancelling for $1/r^3$) — verified **two ways that agree**: the direct spacetime $G_{t\phi}$
  (`scripts/anchor_momentum_1.py`) and the 3+1 momentum constraint above
  (`scripts/anchor_momentum_2.py`), equal up to an overall $2\sqrt{r}\sin\theta$ — the same equation,
  confirming $j_i$ = the shift's bend is the construction's own momentum constraint, not an imported model;
- the amplitude is **not free**: $J=Ma/\Xi^2$ — the mass-offset times the twist (P6 §rotation,
  Prop kerr, established at source). Offset alone ($\omega{=}0$) is SdS; twist alone ($M{=}0$) is de
  Sitter (maximally symmetric, not a new geometry); only the offset in a twisted slice carries $J$.
  **[computed (the sector); $J=Ma$ established in P6]**

## 3. Stress sector — $S_{ij}$ is the stacking's bend ($ij$, the evolution) **[computed; spherical]**
The lapse split (P5 §lapse, recovered from scratch in `scripts/anchor_stress_1.py`):
$$8\pi(p_r+\rho) = \frac{f}{r}\,\partial_r\ln\frac{A}{f},$$
so radial pressure is carried by the divergence of the time-stacking $A$ from the leaf $f$. Locked
($A=f$): $p_r=-\rho$, the rigid vacuum-$\Lambda$ equation of state (its kernel); unlocked: general
$p_r,\,p_t$. So matter **stress = the stacking's departure** — the third datum — exactly as energy = the
leaf's bend and momentum = the shift's bend. **[computed]**

## 4. Vantage — the radial signature **[established, P5]**
The choice of which direction the cut reads as time: $f>0$, $r$ spacelike, the static exterior of the
hole; $f<0$, $r$ timelike, the expanding cosmology. The vantage fixes the signature; the leaf the
density; the stacking the pressure; the shift the frame-drag (P5 §dictionary).

## 5. The anchor closes (as one functional of the cut) **[computed on the spherical class]**
$T^a{}_b$ of the cut is assembled sector by sector and each verified against the corpus: leaf→energy,
shift→momentum, lapse→stress, vantage→signature. The spherical instance is P5's leaf/lapse/vantage
split with the shift turned off; the general anchor **adds the shift (momentum)** and states all four as
one functional. Energy and momentum are the constraints; stress is the evolution.

## Honest scope, and what remains
- **Verified on the spherical class** (here + `anchor_momentum_1/_2`, `anchor_stress_1`, `adm2`); the
  energy sector's general covariant form is the Hamiltonian constraint (verified on the dS leaf and the
  spherical bend). **[computed]**
- The **general statement** is the covariant ADM constraints/evolution with the CR bend-reading; the
  **explicit non-spherical matter functionals** (homogeneous, axisymmetric/rotating-type-I) are P6's
  open item 2, **not collected**; the **dS₅-slicing restriction** (which cuts are admissible — the
  range read as a condition on $\mathcal{C}$) remains. **conjecture**
- **Next algebroid step (Move 6): bracket closure** — whether the cut-deformation bracket closes and the
  anchor is a Lie-algebra homomorphism. $j_i$ being a *clean functional of the shift* is its input. The
  bracket can fail to close on the confined cut (the falsifiable check). **conjecture**

## Receipts (`scripts/`, all clean-zero)
- `adm2.py` — Hamiltonian constraint $=0$ on the vacuum dS leaf, both vantages ($\sigma$ redistributes $2\Lambda$).
- `anchor_stress_1.py` — energy $\rho$, the lapse split, $A{=}f\Rightarrow p_r{=}-\rho$ (energy + stress sectors).
- `anchor_momentum_1.py` — the direct spacetime $G_{t\phi}$ frame-drag, $\omega=C_0+2J/r^3$.
- `anchor_momentum_2.py` — the 3+1 momentum constraint (shift as cut datum), reproducing the direct
  frame-drag; $j_i$ = the shift's bend; separates cleanly (Move 5).
- **The wider ADM / canonical recast chain** (`adm1`–`adm7`, `adm_so51_1`, `adm_strata_1`,
  `adm_skeleton_strata_1`, `adm_wall_1`, `adm_dynamics_1`) **is indexed in `corpus/adm_recast_index.md`** —
  reach for those receipts rather than recreating any ADM split, Hamiltonian/momentum constraint, bracket
  closure, stratification, or deparametrization.
