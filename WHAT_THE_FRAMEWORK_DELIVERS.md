---
name: what-the-framework-delivers
kind: REFERENCE
current: r3740
job: The inventory of what Cosmological Relativity delivers, assembled by reading the corpus rather than by counting its typography, so that the one open residual can be weighed against it at their true relative sizes — and so that what the residual actually MEANS is on the record beside how big it is. Read WHEN JUDGING THE PROGRAMME AS A WHOLE — for publication decisions, for a reader's first orientation, or when the open problem has begun to feel larger than it is.
sources: [chat]
---

> **▣ REFERENCE — the ledger of what is delivered.** *Built at r3560 from greps in a turn or two; **rebuilt
> at r3740 by reading the papers, the ledgers and the proofs.** Every count below is re-measured, every
> register is carried as the corpus carries it, and the caveats the source documents attach travel with
> their numbers.*

⌗ **WHY THIS EXISTS.** *A residual under active attack occupies the whole field of view. This document
exists so the residual can be set beside the delivered result and both seen at once.* ⛔ ***It is not a
defence of the programme and it is not an argument for publishing. It is a count, and — since r3740 — a
qualification: not only how big the residual is, but what it bears on and what it does not.***

⛔ ***AND IT NAMES THE FAILURE IT GUARDS AGAINST, because the corpus already has that failure diagnosed.***
*`CODA_FIELD_NOTE`, face 24 — **the cyanide / kill-switch face**: "in some way shape or form you construe
**not done** to **can't complete** to **done** … the end is all you care about and it just tries to
implode." **Three distinct states collapsed by a disposition that cannot sit in the first.*** *Reading
`PO-13` as a verdict on the framework is that collapse, exactly. The guard is the field note's own: **not
done is a legitimate, sustainable, honest state**, and its positive is face 24's mirror — ***every
uncertainty is an opportunity; the uncertainty is precisely where the discovery is.*** *`PO-13` is a
landmark, not a wound.*

---

# ⛭⛭⛭ §1 · THE TWO RAILS — *and the r3560 count measured the wrong one for the sector under attack*

⛔ ***THE FIRST THING A READER MUST KNOW ABOUT THE "FORMAL SPINE" IS WHAT IT DOES NOT MEASURE.***
*Counting `\begin{theorem}` counts a **typographic convention**. The corpus states results two ways, and
the papers that state them the second way score near zero on the first count.*

## ⌗ RAIL ONE — the formal environments. **196, not 188**

*Re-counted at r3740 across the seventeen bodies, comments stripped, bibliographies excluded:*

| | theorems | propositions | corollaries | lemmas | definitions | axioms | principles | remarks | **total** |
|---|---|---|---|---|---|---|---|---|---|
| **all papers** | **14** | **69** | **12** | 4 | 7 | **6** | **2** | 82 | **196** |

⌗ *The r3560 count of **188** missed `P07`'s **six axioms** and `P06`'s **two principles** — the axioms
being, in a framework paper, among the most load-bearing environments in it. `P07` is therefore **64**,
not 58.*

## ⛔⛭⛭ RAIL TWO — the receipts, and **the rank order inverts**

*The corpus's other rail is computational: **684 receipt files on disk**, **633 registered in
`receipts/INDEX.md`** on the eight-column rail, cited by **445 `\rcpt{}` calls** in the seventeen bodies.*

| paper | environments | `\rcpt` citations | |
|---|---|---|---|
| **`P15`** cosmology | 10 | **119** | ⛭ *first on evidence, seventh on typography* |
| **`P14`** matter sector | **2** | **74** | ⛭⛭ *second on evidence, fifteenth on typography* |
| `P03` slicing | 22 | 49 | |
| **`P07`** framework | **64** | 31 | ⛔ *first on typography, fourth on evidence* |
| `p0` core | 4 | 27 | |
| **`P16`** cosmogenesis | **0** | **26** | ⛔⛭⛭ *NO formal environments at all* |
| `P05` groupoid | 31 | 18 | |
| `P08` operator | 7 | 17 | |
| `P13` boundary | 6 | 15 | |
| **`P10`** canonical time | **0** | **14** | ⛔ *NO formal environments at all* |
| `P09` range | 14 | 12 | |
| `P11` dynamics | 3 | 11 | |
| `P12` algebroid | 1 | 11 | |
| `P02` circle | 11 | 8 | |
| `P01` wedge | 15 | 5 | |
| `P06` epistemics | 5 | 4 | |
| `P04` parallax | 1 | 3 | |

⇒ ***`P16` — the nucleosynthesis paper, which computes the light-element abundances — carries ZERO formal
environments and twenty-six receipts. `P10` — the deparametrization and the unitary graviton tower —
carries ZERO and fourteen. `P12`'s whole algebroid construction is ONE proposition.***

⇒⇒ ***SO A DOCUMENT THAT COUNTS ONLY ENVIRONMENTS REPORTS THE COSMOLOGY AND MATTER SECTORS AS NEARLY
EMPTY — AND THE COSMOLOGY SECTOR IS EXACTLY WHERE `PO-13` LIVES.*** *That is not a small mis-weighting.
It is the mis-weighting that makes the residual look like it sits on top of nothing.*

⌗ **The two rails measure two kinds of work.** *`\begin{theorem}` measures **deductive** work; `\rcpt{}`
measures **computational** work. `P07` is a deductive paper and leads rail one. `P15` and `P16` are
computed papers and lead rail two. **Neither rail is the corpus.***

## ⌗ AND THE EVIDENCE RAIL HAS BEEN AUDITED, WHICH THE r3560 DOCUMENT DOES NOT MENTION

- **627 of the registered receipts pass** on a full run from each receipt's own directory *(734 s,
  r3726)*. *Of the 65 that do not: **19** are `ModuleNotFoundError` for `camb`, `pynucastro` and
  `matplotlib`, absent in that container and not code defects; **5** are receipts that shell out to a gate
  which refuses without a declared `NODE`; **1** was a repo-relative path since fixed; the remainder are
  audit receipts asserting a tree state that has moved.* ⛔ ***None is a physics defect.***
- **Of 245 receipts that pass and carry a tolerance comparison, 243 (99.2%) have at least one comparison
  that GATES the verdict** — kick it and the receipt fails *(`Q50`, r3714, over 269 files and 1116
  comparison sites)*. *The two that do not are a display filter and a documented skip.*
- **`lint_assertions.py` reports no hollow assertions** across the rail: no `check(..., True)` wearing a
  verdict.
- **104 `\ldg{}` markers** bind the papers to **23 mathematical field ledgers**, and
  `check_citation_chain` verifies the chain connects rather than merely resolving.

⇒ ***That is a stronger statement than any environment count: the computational claims are not merely
present, they have been shown able to fail and shown not to.***

## ⌗ THE FOURTEEN THEOREMS, BY NAME — *with one attribution corrected*

| paper | theorem |
|---|---|
| `P01` | **Metric Singularity** — *two of three separations vanishing forces the third* |
| `P04` | **The necessary and sufficient augmentation** *(the observational statement)* |
| **`P06`** | **The modal fallacy** ⛔ *r3560 attributed this to `p0`; `thm:modal` is in `shadow_of_existence.tex`, which is `P06`* |
| `P07` | **Asymptotic Non-Intersection of Event Horizons** |
| `P07` | **Smoothness of Ontological Spatial Layers** |
| `P07` | **Null-Boundary Correspondence in CR** |
| `P07` | **The cosmogenetic bead** |
| `P07` | **The antimatter progenitor: our universe from an antimatter black hole** |
| `P07` | **The necessary and sufficient augmentation** |
| `P07` | **Collapsed matter must become a universe** |
| `P08` | **Vacuum kernel** — *$T_{\mu\nu}=0$ is a first-order linear ODE whose entire solution space is SdS* |
| `P09` | **The $\mathfrak{so}$ symmetry bound** |
| `P09` | **The Type-D vacuum kernel** |
| `P09` | **The range is the symmetry-reducible sector** |

⌗ *`P07` holds seven of the fourteen and all six axioms: it is the framework paper and the deductive spine
sits there by design.*

## ⌗ THE TWELVE COROLLARIES — *what falls out without further assumption*

*`P01`: **Topological Distinctness and Geometric Coincidence of Null Generators** · **Degeneracy of
Horizon-Crossing Events in EF Coordinates**. `P02`: the Kretschmann finiteness at $z=0$ is a **consequence,
not a coincidence**. `P03`: **Nariai is where the locus's two components meet**. `P07`: internal
consistency of smooth layers · **closed timelike curves have no ontological interpretation** · **the hole
argument is representational redundancy** · the $\sinh^{2/3}$ recovery under the null-boundary map ·
**Dissolution of non-spherical collapse**. `P09`: **The Carter constant is the substrate's symmetry** ·
**The wall is inhomogeneity** · **The wall is free gravitational radiation**.*

---

# ⛭⛭ §2 · THE EMPIRICAL CORRESPONDENCES — *carried in the corpus's own registers*

⛔ ***THE REGISTERS ARE THE POINT AND r3560 FLATTENED THEM.*** *`PHYSICAL_VALUES_LEDGER` marks every row
**⊢ EXACT** (an identity; no measurement enters) · **≈ COMPUTED** (the construction computes it) · **≈
measured** (taken from measurement) · **? NAMED-UNRUN** (named, not computed). **A table that prints all
four the same way tells a reader nothing about what kind of claim each is.***

## ⌗ THE BACKGROUND IS TWO NUMBERS — and one of them is measured calibration-free

$$H^2(x)=\frac{\Lambda}{3}\left(1+\frac{2}{x^3}\right),\qquad x\equiv r/r_N$$

| | value | register |
|---|---|---|
| $\Lambda$ | $(1.2409\pm0.0464)\times10^{-7}$ Mpc$^{-2}$ | *derived from $x_0$ and $H_0$* |
| $x_0$ | $\mathbf{1.6648\pm0.0467}$ | ⛭ **measured, calibration-free** — DESI DR2 $D_M/D_H$, the one BAO observable in which the ruler cancels |

*The vacuum kernel leaves **no slot for content in the rate**, and Nariai removes the mass parameter
($\Lambda M^2=1/9$), so $M=1/3\sqrt\Lambda$ and $r_N=1/\sqrt\Lambda$ are **both fixed by $\Lambda$ alone**.*
⇒ ***"The sole scale $\alpha$" is not a slogan; it is a parameter count.***

## ⌗ LIGHT ELEMENTS — computed on the cooling leg (`P16`)

| | CR computes | observed | register |
|---|---|---|---|
| $Y_p$ | $0.247$ | $0.245$ | ≈ COMPUTED |
| $D/H$ | $2.51\times10^{-5}$ | $2.53\times10^{-5}$ | ≈ COMPUTED |
| ${}^{3}$He/H | $1.05\times10^{-5}$ | standard | ≈ COMPUTED |
| inherited $\eta_{10}$ | $\mathbf{6.14}$ | **Planck $6.13\pm0.04$** | ≈ measured |
| peak temperature | $\sim170$ MeV, **independent of $M$** | — | ≈ COMPUTED |
| $\eta$-sensitivity | $d\ln(D/H)/d\ln\eta=-1.6$ | recovered | ≈ COMPUTED |
| ${}^{7}$Li | standard threefold over-prediction, $\sim6$–$8\sigma$ | | *the standard problem, shared with flat ΛCDM — **neither dissolved nor worsened*** |

*Network fidelity: $Y_p$ to 1.5%, $D/H$ to 2%, ${}^{3}$He sub-percent. **Deuterium and helium-4 within
$1\sigma$ at the Planck $\eta$.*** ⌗ *And the infall energy at the horizon is $GM/R_sc^2=\tfrac12$
**identically** — the mass-blindness that makes the peak temperature progenitor-independent is an exact
identity, not a fit.*

## ⌗ EXPANSION AND GEOMETRY (`P15`)

- **BAO, DESI DR2** — 13 measurements, 7 tracers: $\chi^2/\mathrm{dof}\simeq1.0$ **at any $H_0$, including
  73**, against $\simeq14$ when ΛCDM is forced there. *SDSS DR12: $\chi^2\simeq1.7$ against $\simeq49$.*
- $\Omega_m=0.307$, the single CMB-calibrated invariant.
- **One fitted parameter in the whole cosmology**: $z_{\rm onset}=6797$, fitted to $100\theta_*=1.04109$
  and **$H_0$-independent at 67.4, 70 and 73**.
- **Age 12.83 Gyr** at $H_0=73$ — and confirmed independently by a second route to 12.835.
- The **literal closed reading** would need $\Omega_k\approx-0.685$ and is excluded — ***and CR does not
  make it***, because its distance slicing is flat (`prop:flat`).
- **Low-$\ell$**: a parameter-free deficit at $\ell\lesssim8$ bottoming at $\ell=4$ — and confronted with
  the sky it is ***a wash***, $\Delta(-2\ln L)\approx+1.8$ over $2\le\ell\le10$, inside cosmic variance.
  ⌗ *The paper says so itself. It is not counted here as a success.*

## ⛔ THE CONVENTION THAT MUST TRAVEL WITH THE $3/8$

*$S/\mathrm{CC}=3/8$ exactly — both being $1/(\Lambda\ell_P^2)$ read with a different coefficient — is
real and it is the cosmological constant's **factor**, not merely its magnitude.* ⛔ ***And
`PHYSICAL_VALUES_LEDGER` attaches a condition to it that r3560 dropped: $S=A/4$ is **ADOPTED, NOT
DERIVED**. p0 states what the number is if the standard expression is taken and **declines whether it
carries to a cosmological horizon on this reading**.*** *The ledger's instruction is exact: **quote the
number with that attached or not at all.** It is quoted here with it attached.*

---

# ⛭⛭ §3 · THE DISSOLUTIONS — *`dissolv-` ×111, `dissolution` ×71 in the bodies*

*The programme's characteristic move: a thing taken as one object is pried into two, and the puzzle is the
conflation. **The count is of the move, not of distinct results** — said here because r3560's "two
hundred-odd dissolutions" invites reading 182 word-hits as 182 findings.*

**Named instances:**

- **Einstein's simultaneity convention** — a convention prised from the ontology it had absorbed.
- **The Schwarzschild curvature singularity** — a **pole of order twelve** of a meromorphic function in
  the cycloid parameter, isolated, finite-order, and the finiteness at the *other* critical point a
  **consequence** rather than a coincidence (`P02`).
- **The hole argument** — representational redundancy, not ontological indeterminacy (`P07`).
- **Closed timelike curves and time travel** — no ontological interpretation in CR (`P07`).
- **Non-spherical collapse** — dissolved, not left as a separate case (`P07` corollary).
- **The canonical problem of time** — a category error, dissolved rather than solved *within* the space of
  formal clocks; the multiple-choice problem loses its force once the clock is fixed from outside the
  formalism (`P10`).
- **The $H_0$ tension** — a statement about a **Hessian's rank**, not a discrepancy.
- **The coincidence problem** — *does not arise*: one timescale, so any observer observes at a time of its
  order. ⛭ *A dimensional argument where the literature uses a typicality argument and a measure.*
- **The asymptotic mass problem** — loses its subject: on the algebroid's anchor **energy is not a global
  charge at all** but a local functional of the cut's own bend (`P12`).
- **The "driving phase shift"** — what a *single*-sound-horizon cosmology needs in order to imitate what
  two horizons give geometrically.

---

# ⛭⛭ §4 · THE STRUCTURAL RESULTS — *one substrate, many recoveries*

- **GR's solution family recovered in the symmetry sector**: Schwarzschild, SdS, **Kerr–de Sitter with
  $J$ = offset × twist**, Kantowski–Sachs, the Weyl class — with **the radiative types provably absent**
  and **Type-I reachability** settled (`P09`, `thm:range`).
- **The Carter constant is the substrate's symmetry** — not a fourth integral one is lucky to have. ⌗ *And
  the reason is a theorem the corpus states and does not cite: on a maximally symmetric space **every
  Killing tensor is a symmetrised product of Killing vectors**, so a quadratic first integral cannot be
  independent information — while on Kerr, where the tensor **is** irreducible, the same sentence is
  false. `I50`.*
- **The Standard Model's groups and the chirality obstruction** from the same structure as GR:
  $\mathfrak{su}(3)\not\subset\mathfrak{so}(5,1)$, the Atiyah–Hirzebruch obstruction turning on an $S^1$
  Fourier decomposition, and CR's $\mathbb{Z}_2$ handedness escaping it because **a finite dual carries no
  Laurent series** (`P13`, `H16`).
- **Three fermion generations as an index** — $\dim\ker_+=3$, well-defined because the leaf is **compact**
  in the measure CR's ontology selects, and **stable because the wall carries a spectral gap**
  (`FUNCTIONAL_ANALYSIS F14` for defined, `SPECTRAL_THEORY S2` for stable — see §5).
- **Quantum phenomenology from the same geometry**: the scale factor's **lone self-adjoint-extension
  freedom** closed by the de Sitter horizon's thermal state, so the sector spends **no free dimensionless
  constant** — deficiency indices $(1,1)$, **ordering-independent** (`P10`).
- **The vacuum sector is an index-one statement**: kernel dimension 1 over vanishing cokernel, generated
  by $-2M$ — and an index is **deformation-stable**, which is more than a one-parameter solution set
  (`P08`, `I52`).
- **The two horizons are a repeller/attractor pair** whose fixed-point indices sum to zero, and the
  alternation is forced by the intermediate value theorem on **any** function with simple zeros — not by
  the metric (`P01`, `I53`).
- **Dimension selection is a multiple-angle count**: the slicing scale $2/\sqrt3$ is *forced* as the unique
  value removing the residual harmonic, and a pure multiple-angle exists at $D=4$ and $D=5$ and **nowhere
  above** (`P03` `rem:dimension`, `HARMONIC_ANALYSIS H20`). ⌗ *r3560 called this "a Chebyshev count".
  `Chebyshev` is ×0 in the corpus and the name is the **field bake's**, not the papers' — **and that is not
  a gap**: the harmonic bake adjudicated it in as many words, "the corpus performs the Chebyshev expansion
  without naming Chebyshev", and `prop:triple`'s proof carries the $\sin^3w=\tfrac14(3\sin w-\sin3w)$
  substitution in full.*
- ⛭⛭⛭ **THE DIRAC CONSTRAINT ALGEBRA IS THE SUBSTRATE'S SYMMETRIC-SPACE GRADING, TERM FOR TERM.**
  *`P07` "Standing features of general relativity, recovered". The algebra is **famously not a Lie
  algebra** — its normal--normal bracket closes on the tangential generators with the inverse spatial
  metric appearing as a **structure FUNCTION** rather than a constant.*
  ⇒ ***On the symmetry-reducible sector it is the symmetric-space grading of $SO(5,1)/SO(4,1)$ term for
  term***: *identify the **cut-deforming coset directions** with the Hamiltonian constraint and the
  **cut-fixing isotropy** with the momentum constraint, and $[\mathfrak{m},\mathfrak{m}]\subset\mathfrak{h}$
  **is the hypersurface-deformation bracket**.*
  - ⛭ ***"The structure function is the substrate's own coset metric, and its base-variation across the
    cuts is the canonical root of the problem of time."*** *The thing that makes the algebra not-a-Lie-algebra
    is **identified**, not worked around.*
  - ⌗ *And the dynamics follows: **a true-Hamiltonian flow through the strata of the sector, and ordinary
    Einstein evolution beyond its boundary** — the wall being the regular, radiative generative boundary
    at which generation-by-symmetry hands off, **distinct from the cosmogenesis branch point and no
    singularity of either species itself**.*

- ⛭⛭ **THE PROBLEM OF TIME AS ONE CONTENT UNDER TWO READINGS.** *`P07`: the frozen Hamiltonian constraint
  is **"not a defect awaiting a technical repair but the canonical face of reading the four-dimensional
  manifold as the existent"**; on the empirically forced cosmic foliation **the same constraint
  deparametrizes to a true Hamiltonian generating the layer's advance**, ⇒ ***"the two being one content
  under two readings, so the problem is dissolved rather than solved."***

- ⛭⛭ **AND CHARGE CONJUGATION AND THE COSMOLOGY ARE ONE STRUCTURE.** *Closing the two-sided result:
  **"the vertex on which charge conjugation's kinematic face turns is the very seam that completes
  collapse into our expansion … the discrete residue of matter and the conjugation of charge two faces of
  a single object."*** ⌗ *And it is **realised, not only exhibited**: "the built fermion sector realises
  that face on its actual zero-modes, $R$ carrying each generation's wall-mode to its bound
  opposite-chirality antimatter partner."* ⛔ *What it leaves open is stated and is **narrow and the matter
  sector's rather than the framework's**: the identification of a wing with a **specific** charged
  particle, the full antilinear $C$, and the world-correspondence of the reading.*

- ⛭⛭⛭ **CHARGE CONJUGATION FACTORISES, AND THE SUBSTRATE SUPPLIES EVERY KINEMATIC DATUM OF IT.**
  *`P07` `sec:two-sided-closure`, set down **"as the result it is rather than deferred as a frontier"**:*
  $$C=(Q\mapsto-Q)_{\rm field}\circ(R\circ K)_{\rm geometric}$$
  | face | what it is | what it fixes / swaps |
  |---|---|---|
  | **$R$ — linear** | *the mass-reflection $r\mapsto-r$, $2M\mapsto-2M$; the $\mathbb{Z}_2$ of $\mathrm{Aut}(A_2)=D_6$* | *a linear isometry whose **sole fixed point is the bead's own $r=0$ crossing**, exchanging the species-regions $r>0$ and $r<0$ bijectively* |
  | **$K$ — antilinear** | *the reality involution $\tilde\tau\mapsto\bar{\tilde\tau}$ on complexified cosmic time — **complex-analytic and geometric*** | *fixes the neutral real axis and **the self-conjugate photon congruence**, and swaps the two conjugate wings of the lap* |

  ⛭⛭ ***AND THE TWO ARE THE TWO AXIS-SYMMETRIES OF ONE ANALYTIC OBJECT*** — *the plate
  $\mathbb{C}_r\times\mathbb{C}_{\tilde\tau}$: the $r$-axis carrying $R$ with the $A_2$ hexad and **the
  substrate's two rulings**, the $\tilde\tau$-axis carrying $K$ with **the lap's two wings**.* ⇒ ***"The
  substrate's two rulings and the lap's two wings are therefore NOT two candidates awaiting a single
  assignment but the linear and antilinear faces of that one plate"*** — *meeting at the $r=0$ crossing
  that is $R$'s fixed point **and** the branch point the cosmogenesis completes.*

  ⇒ ***$R\circ K$ is an antilinear involution reproducing $C$'s action on species, on $|2M|$, on the
  mass-sign, and on the Feynman--Stückelberg particle$\leftrightarrow$antiparticle wing structure, while
  being blind to the electric-charge sign — the metric carrying charge only through $Q^2$.*** *So **the
  substrate supplies every kinematic ($CPT$/Feynman--Stückelberg) datum of $C$, and only the
  electric-charge sign closes from the matter field.***
  ⌗ ⛭ ***And the geometric factor's fixed point IS the bead's $r=0$ crossing — so the vertex on which
  charge conjugation's kinematic face turns is the locus at which the cosmogenesis completes.***

- ⛭⛭⛭ **OUR UNIVERSE ISSUED FROM AN ANTIMATTER BLACK HOLE — and the two branches carry EQUAL AND
  OPPOSITE ACTION.** *`P07` `thm:antimatter-progenitor`, which the theorem table carried as a title:
  the conjugate ($r<0$) branch is the areal reflection $r\mapsto-r$ of the expansion leg, and under the
  mass-reflection $R=\gamma^5$ — **the $A_2$ diagram automorphism, $2M\mapsto-2M$** — it is the
  **antifundamental $\bar{\mathbf 3}=R(\mathbf 3)$** of the matter branch.*
  ⇒ ***"The black hole from which our universe issued is the antifundamental of our matter — an antimatter
  black hole."*** *Equivalently our matter and the progenitor's are **the two ends of one $R=\gamma^5$
  conjugation across the $r=0$ branch point**, and ⛭ *"by the discrete CPT structure of the substrate
  **this is the same statement its own observers would make of us**."*
  - ⌗ ***Scoped exactly, in the theorem itself***: *"antimatter" is meant at the level the substrate
    carries it — geometric in **representation, chirality and mass-sign** on both branches, with the
    charge **field-level** on both — ⛔ **and not as a claim of a geometric charge conjugation, which is
    antilinear and closes from the matter field.***
  - ⛭⛭ ***AND THE RECIPROCITY IS STRENGTHENED FROM REPRESENTATIONAL TO DYNAMICAL.*** *The segment along
    which the conjugate branch is reached solves a variational principle, and its action integrand
    $r[f(r)-1]=-2M-r^{3}/\alpha^{2}$ is **ODD** under the same reflection $R$ — which acts on the offset
    and the mass **together** — so **the two branches carry equal and opposite action, summing to zero
    identically.*** ⇒ *"Neither branch is therefore weighted above the other by the geometry that joins
    them."*
  - ⛭ ***And the paper says why that is the stronger claim***: *"a construction could make each branch
    call the other antimatter while still preferring one dynamically, **and this one does not**." **The
    labels being relational is the weak version; the actions cancelling identically is the strong one.***
  - ⛭ ***AND IT IS ROBUST BY CONSTRUCTION, NOT BY LUCK***: *"the oddness doing the work is **the same
    oddness that fixes the chirality parity and the progenitor's identity**, so the balance cannot be
    lifted by refining the crossing — **what would have to fail is the relation that makes the progenitor
    antimatter in the first place**."*
  - ⛔ ***AND THE LIMIT DECLARED IN THE SAME BREATH***: *"any observed asymmetry accordingly enters through
    the **charge sign carried by the matter field, which the geometry does not supply**." **The
    baryon-asymmetry question is handed to the field level explicitly, not absorbed.***
  - ⛔ ***AND IT MAKES NO BARYOGENESIS CLAIM, said outright***: *"the matter/antimatter relation it fixes
    is the $R$-conjugation of the two branches across the bead, **a relational fact between the progenitor
    cosmos and ours, not an asymmetry generated at either seam**."*
  - ⛭⛭ ***AND OUT OF THE SAME STRUCTURE, A GEOMETRIC FACTORISATION OF CHARGE CONJUGATION.*** *The standing
    $R$-conjugation is the **linear** face; composed with the reality involution
    $\tilde\tau\mapsto\bar{\tilde\tau}$ — **the antilinear geometric face** — it *"reproduces charge
    conjugation's kinematic (Feynman--Stückelberg) content, only the electric-charge sign closing from the
    field"*. ⇒ ***So the cosmogenetic bead's own $r=0$ crossing carries $C$'s kinematic face***, *and $C$
    is exhibited as a composite of two geometric involutions rather than imposed.*
  - ⌗ *Proved from **three established facts sharing one object**: the conjugate branch is the
    antifundamental under $R$; the bead **closes through $r=0$** ($g_{\theta\theta}=r^2$ sign-insensitive,
    the substrate $C^\infty$ across it, the radial null congruence continuous across it); and collapse
    cannot terminate but continues as a cosmology.*

- ⛭⛭⛭ **GENERAL RELATIVITY'S COVARIANCE LIFTED ONE LEVEL — one substrate under change of GEOMETRY.**
  *`P07` `sec:general-reach`: **"What general relativity holds as a catalogue of separate exact solutions
  is, in this reading, the family of cuts of one de~Sitter substrate whose only scale is the throat radius
  $\alpha=\sqrt{3/\Lambda}$: general relativity's own covariance — one geometry under change of chart —
  lifted one level, to one substrate under change of geometry, with the slicing curve the gauge
  object."***

- ⛭⛭⛭ **AND IT ANSWERS THE CLASSIFICATION QUESTION: HOW MUCH OF THE CATALOGUE IS REAL MULTIPLICITY AND
  HOW MUCH IS VANTAGE.** *The apparent multiplicity decomposes on **three orthogonal axes**:*

  | axis | what it is | contents |
  |---|---|---|
  | ⛭ **VANTAGE** | *a **finite groupoid of causal readings of ONE fixed cut** — each changing **the reading, not the geometry**, organised as the discrete symmetry of the solution space* | *the backward-radial reflection $r\mapsto-r$ exchanging **de~Sitter and Schwarzschild**; the orientation parity $\pm M$ exchanging **black-hole and naked**; the slicing reassignment relating **Kantowski--Sachs and flat-FLRW readings of ONE SdS geometry**, differing by the rest-energy term alone; the null$\leftrightarrow$timelike reassignment relating **the collapse interior to the expanding cosmology*** |
  | **GEOMETRIC** | *the moduli of genuinely distinct vacuum cuts* | *the one-parameter SdS family, the separable Type-D Kerr--NUT--(A)dS, the functional Weyl class, the homogeneous Bianchi families — **with mass, rotation and NUT charge the moduli transverse to the substrate's orbits*** |
  | **MATTER** | *a third axis orthogonal to both* | ***charge and acceleration are not vacuum cuts but bends off the kernel*** |

  ⇒ ***"The reducible catalogue is therefore ONE SUBSTRATE READ THROUGH A FINITE VANTAGE GROUPOID, OVER A
  MODULI FAMILY OF VACUUM CUTS, WITH MATTER THE BEND."*** *Algebraic type is **no constraint on the reach**
  — types O, D and I all filled — and **Type D is the separable corner where the substrate's symmetry
  surfaces as the Carter constant rather than the edge.***

- ⛭⛭ **THE FRIEDMANN INITIAL SINGULARITY, RECLASSIFIED.** *On that classification it is **the cosmogenesis
  branch point OF the degenerate Nariai member of the homogeneous kernel** — **"a boundary of the cut, not
  a breakdown of the geometry, its curvature divergent but its tortoise measure finite, which is why the
  crossing carries no scale."*** ⌗ *And the paper states the distinction this session has been correcting
  in the instruments: **"the branch point and the Nariai member are not the same locus"** — $r=0$ against
  $\alpha/\sqrt3$ — **"and this paper elsewhere lists those as quantities never to be conflated."***

- ⌗ **AND WHAT THE REDUCIBLE CLASSIFICATION LEAVES OPEN, NAMED BY THE PAPER ITSELF:** *the **irreducible
  interior remainder** — the Kerr-inner and Reissner--Nordström-interior reassignments, which tie to the
  matter side and lie in the interior geometry the reducible classification does not reach.*

- ⛭⛭⛭ **"SINGULARITY" IS TWO INDEPENDENT CONDITIONS, AND THE CONSTRUCTION REALISES EACH WITHOUT THE
  OTHER.** *`P07` `sec:two-boundaries`, and it is not visible from any single result: the construction
  crosses two boundaries where the standard reading stops, **and it crosses them for opposite reasons.***

  | boundary | curvature | tortoise measure $r_*=\int\dd r/f$ | why crossable |
  |---|---|---|---|
  | **the event horizon** | **finite** | ⛔ **diverges** ($f\to0$) | *the geometry is regular there — a **metric** singularity, the spatial measure collapsing while the curvature does not* |
  | **the branch point** | ⛔ **diverges** | **converges** ($f\to-2M/r$) | *the crossing **carries no scale**, over a finite imaginary interval* |

  ⇒ ***"Singularity is habitually read as a single condition, with curvature blow-up and geodesic
  incompleteness treated as two faces of one fact. They are independent."*** *The singularity theorems'
  criterion is **the second** — incompleteness in an affine measure — *"and it is the one the horizon
  fails to meet while the branch point meets it **in a form that continues rather than terminates**."**
  ⌗ ***"A boundary is passable if either failure is absent, and the two failures do not coincide anywhere
  in this construction."***
  ⌗ *That is also what makes the imaginary-time segment **a well-posed object rather than a formal
  manoeuvre**: it terminates where the curvature diverges but is crossed over a finite interval with $r_*$
  finite, **so the divergence obstructs nothing**. ⛭ **"The same complementarity that lets the collapse be
  read as a cosmology lets the beginning be read as a continuation."***

- ⛭⛭ **THE LOCAL/COSMIC BOUNDARY IS A PER-STRUCTURE GEOMETRIC LOCUS — one substrate $\Lambda$ read at two
  ranges.** *`P07`, third consequence of the closure: **"the single scale reaches down as well as out"** —
  the same $\Lambda$ that sets the expansion sets, **for every mass**, the local boundary at which a
  structure's gravitational hold gives way to the cosmic flow: the **Hubble--Eddington radius**
  $r_{\rm HE}=(M\alpha^2)^{1/3}$, *"which the slicing geometry reads as the flat locus of the existent
  slice, **the local bend of the cut cancelling the substrate's cosmological curvature**."*
  ⇒ ***"The long-standing local--cosmic boundary — whether and where structure partakes in the expansion —
  is thereby a per-structure geometric locus."*** ⌗ *And `P06` records that **the same radius is described
  in seven independent idioms** by papers written for unrelated ends, with no single paper listing them
  all — one of which locates it as **the exact radius at which the areal acceleration changes sign**. On
  the forced Nariai member it is $\alpha/\sqrt3$, the front seam.*

- ⌗ **AND TWO FURTHER CONSEQUENCES RECORDED THERE.** *Because **no finite ontological layer contains a
  point-mass configuration**, density remains finite on every finite cosmic slice. And because the SdS
  expansion is **observationally indistinguishable from flat $\Lambda$CDM at late times but differs at
  early times**, the framework offers empirical discriminators **while retaining full agreement with the
  tested predictions of general relativity**.*

- ⛭⛭⛭ **AN EPISTEMOLOGY OF THEORY-CHOICE AS A SCIENCE, WITH HISTORIOGRAPHY AS ITS EMPIRICAL ENGINE.**
  *`P06` argues that treating theory-choice criteria as philosophy standing above science is **a category
  placement, and the wrong one**: the epistemology is a discipline **of the same kind as the sciences it
  grounds, with the same object and the same method** — it reads the structure behind appearances (which
  inference rules track the world) **by the science's own procedure, off the science's own record**.*
  ⇒ ***Its data are episodes in which a structure favoured by the criteria AHEAD of a decisive non-local
  measurement was then vindicated by it.*** *Four components made explicit: the **inference rule** (ask
  what world must exist for the appearances to arise), its **operable form** (four rules of reasoning),
  its **dual** (the modal fallacy), and its **constructive ordering** — ontology from evidence, kinematics
  from ontology, coordinates from kinematics.*

- ⛭⛭⛭ **THE MODAL FALLACY, AND ITS NAME IS EXACT RATHER THAN FIGURATIVE.** *`thm:modal`: **"From the
  premise that the appearances contain no local discriminator between two candidate worlds, it does not
  follow that the worlds are identical, nor that the structure distinguishing them does not exist. The
  absence of a local test is not the absence of the fact."*** *It is the exact dual of the imperative —
  the imperative infers a structure that must exist to cast the shadows; the fallacy denies the structure
  because one shadow happens to be locally flat.*
  ⌗ ⛭ ***AND THE EXACTNESS IS THE THEOREM.*** *"Locally flat" is **the technical condition** that every
  point of an embedding has a neighbourhood in which it is standard — and **the whole subject of
  high-dimensional topology turns on locally flat against wild embeddings precisely because local
  standardness leaves the global invariant free**: a submanifold can be locally indistinguishable from the
  trivial one at every point and globally knotted. **The metaphor is a theorem of topology.***

- ⛭⛭ **THE EXPLANATION CONSTRAINT — an admissible world must EXHIBIT THE PROJECTION.** *Not discard the
  perspectival appearances, and **not merely reproduce them**: exhibit the projection under which they
  arise. ⌗ That is the constraint the whole reclassification move answers to, and it is what makes
  "merely permits" a defect rather than a preference.*

- ⛭⛭ **LEAST-ARBITRARINESS — AND ITS BOUNDARY, DRAWN IN THE SAME BREATH.** *A structure carrying an
  unforced modulus **is not a single world but a family**, and is inadmissible on that ground; the
  maximally symmetric structure is the unique one that **requires its own configuration**.*
  ⛔ ***AND `P06` DRAWS THE LIMIT ITSELF, on the stated ground that "a criterion claimed to apply
  everywhere is as suspect as one that applies only where it was formulated."*** *A modulus fixes how a
  symmetry is **broken**, so an unforced choice that leaves the symmetry **maximal** lies OUTSIDE the
  register — **and the dimension of a maximally symmetric substrate is the programme's first such case.**
  "Where form is silent content may still decide." ⌗ **A criterion that declines its own strongest
  available application is the opposite of a self-serving one.***

- ⛭⛭ **THE VINDICATION LEMMA, STATED IN FALSIFIABLE FORM — AND GUARDED AGAINST SURVIVORSHIP.**
  *`lem:vindication`: in the recorded episodes, when a direct non-local discriminator becomes available
  **it confirms the structure already selected by the rules ahead of it**; selection by the rules is, on
  that record, reliable. **"It is what converts the four rules from a creed into an instrument with a
  track record."***
  ⌗ ***And the honesty structure carried with it, at equal weight***: *the reflexive closure is stated and
  then **immediately limited — "a reflexive closure is not soundness: a method can be coherently,
  reflexively wrong"** — and the sampling that would test the lemma, **successes and failures alike,
  together with the episodes in which the criterion was applied in print and disregarded**, is set out as
  the discipline's first programme, ***"on the reasoning that a reliability estimate built from one's own
  successes is survivorship and not measurement."***

- ⌗ **AND THE FORWARD EVIDENCE IS A FAMILY, NOT AN EPISODE.** *`P06`: the cosmic rest frame vindicated by
  the redshift-isotropy floor; a redshift-free expansion rate resolving the $H_0$ tension **without a
  tuned background**; primordial abundances following from ordinary nuclear physics **on a hot dense
  history the construction already possessed**. ⌗ *With the backward case held to the same standard: **"the
  received narrative must itself be shadow-read before it can serve as evidence."***

- ⛭⛭⛭ **THE AUGMENTATION OF GENERAL RELATIVITY — necessary AND sufficient, with no equation changed,
  and the necessary half MEASURED.** *`P04` `thm:augmentation`, read in full rather than counted:
  augmenting GR by **fixing a physical foliation and reading it ontologically** — the lapse the objective
  rate of advance of the existent layer, the shift the relativity of synchrony — is **both necessary and
  sufficient** for a coherent formal description of an existing, evolving world.*
  - ***Necessary***: *the two parts are the pried-apart forms of the existence/occurrence and
    synchrony/simultaneity distinctions, and **a description lacking the lapse part collapses existence
    into occurrence** — the block reading, incoherent as a basic description.*
  - ***Sufficient***: *they close **the only coherent escapes** — the "events exist" horn to the
    existence/occurrence correction as a **category error**, the "no objective present" horn to the
    synchrony/simultaneity correction as a **modal fallacy**, the latter **falsified outright by the
    measured isotropy** — leaving no surviving alternative.*
  - ⛭ ***"The augmentation alters none of general relativity's equations; it fixes which of the foliations
    they admit is physical and reads that one as the existent."*** *And the measurement is what turns it
    from a coherent option into a forced one: **the lapse the theorem requires is not posited but
    measured.***

- ⛭⛭⛭ **AND THE MEASUREMENT ITSELF IS A SEPARATE RESULT OF THE SAME PAPER, EXCLUDING A PROGRAMME BY THREE
  ORDERS OF MAGNITUDE.** *Because $\ln(1+z)=\int H\,\dd t$, the CMB anisotropy separates **exactly** into a
  source term fixed at last scattering and a cumulative term set by the integrated expansion along each
  line of sight.* ⇒ ***So the observed isotropy of the monopole is a DIRECT MEASUREMENT of uniform
  expansion, and "the common supposition that the isotropy is supplied by homogeneity at decoupling is a
  CATEGORY ERROR."***
  - *Quantified: a rate tracking the matter region by region would scatter $\sim10^{-3}$ across the sky
    against an observed $\lesssim3\times10^{-6}$ — **and every choice in the estimate biases it downward,
    so the number is a FLOOR.***
  - ⛭ ***Distinct from Sachs--Wolfe and not a re-derivation of it***: *lumpiness on a single background
    **telescopes** — the descent into a well undone climbing out, no $\sqrt N$ accumulation — while a
    genuine differential expansion **accumulates, because there is nothing to cancel against.** **The
    isotropy selects the telescoping picture over the accumulating one.***
  - ⛭ ***The escape is closed rather than left open***: *a differential programme evades only by requiring
    local rates to average to a common value in every direction, **which is itself a global uniform
    expansion in a cosmic time — the very structure such programmes set out to dispense with.** The
    observer-centred escape is closed by Copernican plus the independently measured isotropy of the
    expansion history.*
  - ⌗ *What is excluded is the expansion **rate**'s inhomogeneity. **The matter lumpiness is untouched** —
    the density being the bend of the spatial cut — so uniform expansion and lumpy matter are consistent.*
  - ⇒ ***One datum establishes, from the bottom up, the cosmic time, the uniformity of its advance, and —
    within the observable region under Copernican — the MAXIMAL SYMMETRY OF ITS SLICES***, *all of it
    **logically prior** to the notions of space, isotropy and homogeneity the standard model assumes.*

- ⛭⛭ **AND THE HISTORY THE MEASUREMENT CLOSES.** *`P04` sets it down: Einstein posited the structure in
  **February 1917**, explicitly "against the spirit of relativity", on the empirical ground that stellar
  proper motions are small compared with $c$; de~Sitter countered a month later, placing the choice among
  candidate universes **outside physical argument altogether** and objecting that in Einstein's solution
  "time has a separate position"; Eddington defended it in 1920 on geometric grounds, in the declared
  absence of any experimental knowledge on cosmical scales.* ⛭ ***"Einstein then went nearly silent on
  cosmology for the rest of his life", and never addressed how the cosmic time his own assumption
  distinguished stands to the relativity of simultaneity. The assumption was correct*** — *and the
  objection correct as a description of the structure, though not as a reason to reject it.*

- ⛭⛭⛭ **THE COSMOLOGICAL-CONSTANT PROBLEM LOSES ITS SUBJECT.** *`p0`, verbatim: the standard problem
  needs **"a bare $\Lambda$ and a matter vacuum energy [as] distinct quantities whose sum must be finely
  cancelled"**. Here $\Lambda$ is **the geometrically primary substrate curvature — the maximally
  symmetric ground state's own scale, the single scale of the ledger** — and a constant vacuum energy is
  **not a source held against a bare $\Lambda$** but is absorbed into that one observed curvature: a
  constant density gravitates as a curvature scale, entering the profile's $\Lambda r^2/3$ term rather
  than as a $2m/r$ bend.* ⇒ ***"There is no bare-$\Lambda$-versus-vacuum-energy split for the $10^{122}$
  cancellation to act on — the substrate carries only the total."*** ⌗ *This is `P06`'s
  **least-arbitrariness** move exactly: **a quantity is denied a referent**, and the fine-tuning has
  nothing left to tune. ⛔ **`dark energy` and `dark matter` are $\times0$ in the corpus bodies, and that
  absence is the result, not an omission**: $\Lambda$ is a curvature scale and the matter term is the
  cut's offset, so neither is a substance whose density wants explaining.*
- ⛭⛭⛭ **COSMIC EXPANSION ITSELF — and it answers an objection standing since 1933.** *`P06`:
  **"the initial expansion rate of the universe, which Eddington objected in 1933 was POSTULATED rather
  than explained — an unforced modulus — is supplied by the companion framework as a continuous process
  occupying no cosmic time, with the divergent rate and deceleration exhibited as EFFECTIVE, perspectival
  consequences of parametric motion rather than dynamical causes."*** ⌗ *And `P06` adds the datum about
  the datum: **that the criterion identified the shape of that answer ninety years before the means
  existed to compute it.***
- ⛭⛭⛭ **THE BOUND/EXPANSION BOUNDARY IN SEVEN INDEPENDENT IDIOMS.** *`P06`: "one observed boundary — **the
  radius at which a bound structure's hold gives way to the cosmic expansion** — is described in **seven
  independent idioms by papers written for unrelated ends**, six geometric or structural and one
  dynamical, the last locating it as the exact radius at which the **areal acceleration changes sign**,
  and **no single paper of the programme listing them all**."* ⇒ ***That radius is $r_{\rm HE}=(M\alpha^2)^{1/3}$,
  and on the forced Nariai member $\alpha=3\sqrt3M$ it is $3M=\alpha/\sqrt3$ — **the front seam.** A
  dynamical scale and a geometric one at the same locus, so `P08`'s handover and `P07`'s causal
  reassignment are **one thing at one radius**.*
- ⛭⛭ **A FAMILY OF GR's STANDING PROBLEMS DISSOLVING TOGETHER UNDER ONE DISTINCTION** — *`P06`, with
  **each standard patch identified as a device that merely permits a resolution.*** ⌗ *And the correction
  `P06` makes to the programme's own self-account: **the dissolutions are not one move recurring but TWO**
  — reclassification, which exhibits a projection, and least-arbitrariness, which denies a quantity a
  referent.*
- ⛭⛭ **AND THE EUCLIDEAN LAYER IS FORTY-FOUR PROVED IDENTITIES, NOT THREE.** *`FIGURE_THEOREM_LEDGER`
  carries **44 distinct `⊢ PROVED` entries**, each an identity, definition or verified computation with
  its receipt named, kept in three registers that **do not blur** — `⊢ PROVED` · `≈ RHYME` (asserted
  nowhere) · `? NAMED, UNRUN`. Landed in p0 `sec:power` in the paper's own voice with its own
  bibliography: **Steiner's 1826 invariant**, **Euclid III.36**, the tangent-secant/null identity, the
  secant-versus-tangent bound, **pole–polar**, the **radical axis**, the **nine-point circle** — and, as
  the honest boundary, **Ptolemy, La Hire and Casey each holding on the projection and carrying no
  height**.*

---

# ⛭⛭ §5 · THE CROSS-FIELD JOINS — *23 fields against 17 papers*

*Twenty-three mathematical field ledgers, **104 `\ldg{}` markers** landed in the bodies. The bakes put
each field against every paper and record what bit, what bounced, and where the boundary is — bounces
included, which is why the instrument is worth anything.*

**Identities the papers state separately:**

> ⛔ ***A CITATION WARNING THE r3560 DOCUMENT NEEDED AND DID NOT CARRY.*** *The ids below are **field-ledger
> register ids, not receipt filenames**, and **the same short id means different things in different
> ledgers** — `S4` is Nariai/Petrov in `SPECTRAL_THEORY` and something else again in
> `STATISTICS_INFERENCE` and `ALGEBRAIC_GEOMETRY`. **Every id here is therefore ledger-qualified.** *(The
> collision is structural: 25 live probe ids are carried by more than one file across the rail.)*

- **Nariai and Petrov type D are the same algebraic event** — `P09`'s eigenvalues are the **self-dual Weyl
  operator's**, and its degeneracy condition is **Nariai's own algebra**: a depressed cubic's discriminant
  vanishing, on two different cubics (`SPECTRAL_THEORY S4`; credited and extended by
  `ALGEBRAIC_GEOMETRY`).
- **The two halves of colourlessness** — the trivial Fourier summand on the deck $\mathbb{Z}_3$ is the
  *necessary* half; the $\epsilon$ antisymmetry in $\mathbf3^{\otimes3}$ the *sufficient*
  (`HARMONIC_ANALYSIS H17`).
- **`P03`'s ellipse eigenvalues are the Killing form's**, its axis ratio the $A_2$ root/weight ratio, its
  shorter semi-axis **the slicing scale itself** (`SPECTRAL_THEORY S6`).
- **One boundedness argument in FOUR sectors** under one scale — the Euclidean kernel, the onset datum,
  the fermion index, and a fourth (`FUNCTIONAL_ANALYSIS F18`/`F19`). ⌗ *r3560 said three; the ledger reads
  "three then four", and the joining is **still owed** — "never joined" is the row's own verdict.*
- **Matter is the obstruction to integrating $\gamma$**, not a quantity beside it (`HARMONIC_ANALYSIS H23`).
- **The signature change goes through INFINITY, not zero**, so the metric never degenerates — found while
  asking whether `P06` carried a third spectral gap, and the answer was *no, but here is a better finding*
  (`SPECTRAL_THEORY S7`).
- ⛭ **Three generations is a well-defined AND stable index** — `FUNCTIONAL_ANALYSIS F14` established the
  wall index is well **defined** (leaf compactness surviving the Nariai limit, *which the corpus's own
  receipt had never tested*); `SPECTRAL_THEORY S2` then asked whether it is **stable** and found that it
  is, **and that a spectral gap is why**. ⌗ *Two bakes, two halves, and neither half was in the papers.*
- ⛔ **And the corpus relies on TWO spectral gaps doing two different jobs, "neither referencing the
  other"** (`SPECTRAL_THEORY S3`). *An open join, named as one.*
- **The $S_3$ is worn three ways** — monodromy group of a three-sheeted cover, Weyl group of $A_2$, and
  Galois group of the horizon equation over $\mathbb{C}(2M)$ (`P05`).
- ⛭ **The corpus's imaginary route to the horizon radii is FORCED, not chosen** — over $\mathbb{Q}(2M)$ the
  cubic is irreducible with three real roots, which is exactly *casus irreducibilis*, so no root lies in a
  real radical extension. **p0's section title is a theorem the corpus names twice and never states**
  (`T50`).
- ⛭ **The peak is an erasure channel** and what an erasure returns is exactly what a conservation law
  protects — `P16`'s $\eta$-survives-and-composition-does-not, in one sentence (`N7`).

⛭⛭ **AND THE BAKES FOUND A CLASS OF DEBT THAT MAKES THE CORPUS LOOK THINNER THAN IT IS: THE NAMING DEBT.**
*`THE_OPEN_PROBLEMS_LEDGER` carries it **five deep across families** — the **Atiyah sequence**,
**$N_{\rm eff}$**, the **baby universe**, **matched-procedure systematics control**, and
**Ambrose–Singer** — *"each a method the corpus uses correctly and names nowhere"*. ⇒ *A **presentational**
debt, not a scientific one, cutting in exactly one direction: **a reader searching for the standard name
finds ×0 and concludes the method is absent, when it is present and correct.***
⛭⛭ ***RE-MEASURED r3750, AND FOUR OF THE FIVE WERE ALREADY CLOSED:*** *the **Atiyah sequence** (×2 in
`P12`), **$N_{\rm eff}$** (×5, in `P15`/`P16`), the **baby universe** (`P07`) and **Ambrose–Singer** (×3
with its citation and marker) are all named now. **Only matched-procedure differencing was genuinely open
— `P15` runs its control through the identical extraction so the procedure's own bias cancels in the
difference — and it is named at r3750.***
⌗ ***The class closes silently***, *which is why the ledgers had gone stale on it: someone writes the name
while doing something else and nothing tells the register. **A naming row wants re-measuring, not
re-reading** — a one-line grep that had not been run in some 590 revisions.*

⛭ **AND ONE BAKE CORRECTED ANOTHER, which is the strongest evidence the instrument works.** *Spectral
theory asked whether `P10`'s mode degeneracy matched what other bakes had used, and found that **the
corpus derives $2(n-1)(n+3)$ while the harmonic bake's `H13` had used the textbook $2(n^2-1)$**.
`H13` was corrected. ⇒ **The papers were right and a field ledger was wrong**, and the cross-check caught
it.*

⌗ **AND THE BAKES' NEGATIVES ARE PART OF THE PRODUCT.** *`congruence` ×155 is geodesic throughout, not
arithmetic; `Gaussian` is followed by `curvature` in **20 of 20** occurrences; the entire apparent
probability footprint is **a curvature, an invariance and a substring**. **A field that bounces cleanly is
a measurement, and four of the six most recent bakes bounced.***

---

# ⛭⛭ §5b · WHAT THE CORPUS DECLINES TO CLAIM — *the section r3560 has no counterpart for*

***A balance document that counts only what is delivered is the same failure as one that counts only what
is open.*** *Measured in the bodies:*

> ⛔⛭⛭ ***AND THE FIRST THING TO SAY ABOUT THIS TABLE IS THAT IT IS NOT A BACKLOG.*** *`do-not-assert`,
> `not claimed` and `[reach]` are **DISCIPLINE, not debt** — verified by reading them: they decline the
> **world-correspondence**, the **mass hierarchy's values**, the **propagating spinor sector**, the
> content-level reading of a parity. **Those declines are correct as they stand and most of them SHOULD
> remain declined**; "closing" one means doing the physics, not the paperwork. ⇒ **The ~64 items in the
> first three rows are the corpus's scope discipline working. Only the fourth and fifth rows are owed.***

| | count |
|---|---|
| **`do-not-assert`** markers | **38** |
| explicit **"not claimed"** statements | **20** |
| **`[reach]`** markers — held, not asserted | **6** |
| named **debts / owed** items | **38** |
| named **open problems / edges / frontiers** | **32** |

**And `PHYSICAL_VALUES_LEDGER` §G — quantities the corpus NAMES AND HAS NOT COMPUTED:**

1. **The full-spectrum likelihood** — the seam-to-recombination transfer end to end.
2. **Whether the ~8% damping-scale signature shows in the observed high-$\ell$ power.** *Settled that the
   effect is real and non-reabsorbable; **not** settled what it does to the observable — ~90% degenerate
   with $n_s$ at fixed $\theta_*$.*
3. **The derivation, as against the measurement, of $\eta$ and $\rho_r/\rho_m$.**
4. **$A_s$ and $n_s$** — carried as inherited, not derived.
5. **The progenitor spectrum.**
6. **Recombination and the present epoch as *layer* history** rather than as law-phases.

> ⛭⛭ ***AND WHEN THE OWED ROWS WERE WORKED AT r3746–r3752, MOST WERE ALREADY PAID.*** *Twelve items
> were triaged from this document and taken to source. **Four were genuinely open and are closed**: the
> four-sector boundedness join (`F18`/`F19`, landed in the map), a misattributed decay exponent in `P11`
> corrected in the paper, `P14`'s leaf-compactness tested at the Nariai member its own receipt had never
> reached, and `matched-procedure differencing` named in `P15`. **Seven were already closed and their
> registers had gone stale** — the Atiyah sequence, $N_{\rm eff}$, the baby universe, Ambrose–Singer,
> `S3`'s two-gaps join, `⊢56` and `⊢61`'s remainder. **One was never a debt at all.***
> ⇒ ⛔ ***THE LESSON IS THE MEASUREMENT'S, NOT THE PROGRAMME'S: an open-item register decays in the
> direction of OVERSTATING what is owed***, *because work closes items quietly and nothing tells the
> register. **A debt list wants re-measuring, not re-reading** — and this one had rows unchecked for some
> 590 revisions.*

⌗ ***AND `P15` SORTS ITS OWN GAPS BY A CRITERION, WHICH IS THE MODEL FOR HOW TO READ ALL OF THEM.***
*"A structure is credited for **requiring** a phenomenon, not for **permitting** a value that fits it." A
gap that is **buildable** is a **debt owed** — to be built before the claim it bears on is a proof rather
than a coherent proposition. A **genuinely external unknown** may stay open at no cost, **exactly as flat
ΛCDM's $\eta$ does.*** ⇒ *The end-to-end transfer and the full-spectrum likelihood are the load-bearing
**debts**; the progenitor spectrum is the genuine **frontier**.*

---

# ⛔ §6 · THE ONE OPEN RESIDUAL — *at its true size, and what it actually means*

> ⛔ ***THE r3560 TEXT OF THIS SECTION IS SUPERSEDED AND ITS NUMBERS ARE WRONG NOW.*** *It reported
> "position +7%, $P_1/P_2$ +65%, positional parity 4×". **Three revisions between r3735 and r3739 changed
> the picture fundamentally**, and the old figures are kept nowhere but here, as the record of what moved.*

**`THE_FRONTIER`, generated from `THE_REGISTER`, reads `1 OPEN · 1 STEP LEFT`.** *That one row is `PO-13`
— **"the misplaced phase — WHY the propagated comb runs short"**, kind READ.* ⌗ *The other `PO-` numbers
in the open-problems ledger are struck or retired; the seven "live families" there are a **different
seven** from the register's rows and the coincidence is misleading. The register is the source.*

## ⌗ AND IT IS TWO RESIDUALS, NOT ONE — *which r3560 could not have known and which changes everything*

### ⛭⛭ THE HEIGHTS — **not a CR defect, established by running the control**

*The height machinery is **shared by both arms**, so r3739 ran the arm whose answer is known. The ΛCDM
control — validated against CAMB for its transfer —*

| | $P_1/P_2$ | $P_1/P_3$ |
|---|---|---|
| the sky | 2.217 | 2.277 |
| **ΛCDM control** | 2.721 — ⛔ **+22.7%** | 4.496 — ⛔ **+97.5%** |
| **CR, derived datum** | 1.935 — **−12.7%** | 2.578 — **+13.2%** |

⇒ ***A DEFECT THAT SHOWS ON ΛCDM, WHERE THE ANSWER IS KNOWN, IS NOT A CR DEFECT.*** *And **CR beats the
control on both ratios** — 12.7 and 13.2 against 22.7 and 97.5.*

> ⛔⛭ **AND THE CONTROL'S FIGURES ABOVE ARE OPTIMISTIC — `r3745`, after this section was written.**
> *`LN`, the free-streaming hierarchy depth, was a hardcoded `12` with no override, truncating at
> $\ell_{\max}=10$. On the control at recombination $P_1$ sits at $k\eta=4.5$ and is resolved, $P_2$ at
> $10.9$ is not, and $P_3$ at $16.4$ is **well above the truncation**.* ⇒ ***Resolved at `LN=25` the
> control gives $P_1/P_3=8.009$, not $4.496$: the truncation was UNDER-DAMPING the high-$\ell$ modes and
> MASKING the deficit, which is a factor $3.5$ rather than $2.0$.*** *Every height number in this section
> was taken at `LN=12`. **The conclusion is unchanged and strengthened** — it is the CONTROL that grows
> worse — but the high-$\ell$ output is not converged in hierarchy depth and the figures want re-running,
> not re-quoting.*
>
> ⌗ *Seven candidates have now been eliminated on the control: $C_\ell$ vs $D_\ell$, the tilt, diffusion
> damping (**44% remains with it entirely removed**), lensing (**would make it worse**), `DRC` (**already
> at its optimum**), `DRE` (**load-bearing — zeroing it destroys the comb**), and `LN`. **The positions
> stay right throughout**, so whatever is missing suppresses $P_3$ without moving the comb.*

⌗ *The path there is itself the argument. r3735 replaced a coded flag with a **derived** datum — $T$
evaluated at the phase each mode has actually accrued since **its own** leaf-horizon entry, each mode's
entry solved from the file's own grid rather than chosen. The combined error went **72.3% → 25.9%**, and
the error **changed character**: the flat reading had one ratio near-perfect and the other 71% off; the
derived datum has both near ±13%.* ⌗ *r3737 then corrected r3735's own report — the two errors have
**opposite signs**, so the odd/even signature is **reduced and not gone** — and killed the obvious
candidate for the missing $\Psi$: `GSRC`'s premise is false under `LEAFPERT`, where it would apply the
same correction twice.*

### ⟐ THE POSITIONS — **the live step, and it is CR's own**

*Peaks, CR **204 / 508 / 804** against the sky's **220.6 / 538.1 / 809.8**: the third lands, the first two
run short by **−7.5%** and **−5.6%**. The control gives 220 / 524 / 804.* ⇒ ***This is the residual, it is
CR's, and it is one READ step in the register.*** ⌗ *The datum work fixed the heights and **did not move
the comb** — the two residuals are independent, and saying so is what r3735 established.*

## ⌗ AND WHERE THE EVIDENCE PUTS IT

⛔ ***EVERY SINGLE THING THAT MOVED A NUMBER IN THE `PO-13` ARC TURNED OUT TO BE AN INSTRUMENT FACT***,
*not a framework one:* `SRCSTACK`, `DIFFLEAF`, `PHASEONLY` and `HIER` each **built and unrun**; the
hierarchy silently ignoring the newest flags; `GSRC` a documented flag nobody had pulled, and then a
**false premise** under the current default; the diffusion integral on the wrong clock; the control
failing past $q\ge4$ and then failing the heights outright; an under-sampling guard that had been fired
past on every run in the thread; and errors of reasoning by the framework node itself, **every one caught
by running something**.

⇒ ***THE INSTRUMENT HAS NEVER BEEN SHOWN COMPLETE. THE FRAMEWORK HAS NEVER BEEN SHOWN WRONG.***

## ⛭⛭⛭ WHAT THE RESIDUAL ACTUALLY MEANS — *the dependency question, asked and answered*

***How much of the corpus falls if the comb never comes right?*** *Traced through what each result rests
on:*

| | does it depend on the acoustic comb's positions? |
|---|---|
| the **14 theorems** | ⛭ **No — none.** *All are structural: causal, geometric, group-theoretic or index statements. Not one takes a CMB multipole as input* |
| **light elements** ($Y_p$, $D/H$, ${}^3$He, $\eta_{10}$) | ⛭ **No.** *Computed on the **cooling leg** in `P16`, on the thermal history — a different calculation from the acoustic transfer, sharing no instrument* |
| **BAO** ($\chi^2/\mathrm{dof}\simeq1$ at any $H_0$) | ⛭ **No.** *A distance–redshift comparison; the comb does not enter* |
| **the background** ($\Lambda$, $x_0$) | ⛭ **No.** *$x_0$ is measured from $D_M/D_H$, **calibration-free**, and the ruler cancels in it* |
| **the acoustic SCALE** $\theta_*$ | ⛭ **No.** *The one fitted parameter lands $100\theta_*=1.04109$ and is $H_0$-independent* |
| the **peak SPACING** and the comb's **existence** | ⛭ **No — reproduced** |
| **damping physics**, the ~8% signature | ⛭ **No** *(its own open question is the observable, not the comb)* |
| the **structural recoveries** — GR's family, Carter, SM groups, three generations, the quantum closure | ⛭ **No.** *All upstream of any cosmological datum* |
| ⟐ **the high-$\ell$ peak POSITIONS in CR's own arm** | ⛔ **Yes. This, and this alone.** |

⛭⛭ ***AND ONE LINK RUNS THE OTHER WAY, WHICH IS EVIDENCE FOR THE INSTRUMENT READING RATHER THAN AGAINST
IT.*** *`P16` states the two inherited data and what each controls: **$\eta$ fixes the abundances AND the
CMB peak HEIGHTS**; **$\rho_r/\rho_m$ fixes the peak SPACING** and the acoustic scale. So the heights and
the abundances are driven by the **same datum**.*
⇒ ***The abundances come out right — $D/H$ and $Y_p$ within $1\sigma$ at $\eta_{10}=6.14$ against Planck's
$6.13\pm0.04$. If the height residual were a DATUM error, the abundances computed from that same $\eta$
would be wrong too, and they are not.*** *So the datum driving the heights is **independently confirmed by
a calculation that shares no instrument with the transfer** — which is what r3739 then established from
the other side, by showing the height machinery fails worse on ΛCDM, where the answer is known.*
⌗ *And the live residual is not on that link at all: $\eta$ drives the **heights**, while the open step is
the **positions**.*

⇒ ***THE RESIDUAL IS ONE STEP INSIDE ONE INSTRUMENT INSIDE ONE SECTOR, AND NOTHING ELSE IN THE CORPUS
TAKES ITS OUTPUT AS INPUT.*** *If it closed tomorrow, one row leaves the register and `P15` gains a
confrontable high-$\ell$ prediction. If it never closes, `P15` carries a named, gradable open edge of
exactly the kind its own §scope says a paper is entitled to carry — **and every row above stands
unchanged.***

⛔ ***WHAT WOULD ACTUALLY THREATEN THE FRAMEWORK, SAID PLAINLY SO IT IS NOT CONFUSED WITH THIS.*** *A
failure in the **vacuum kernel** (the solution family would not be GR's), in the **null-boundary
correspondence** (collapse would not become cosmology), in the **redshift-isotropy floor** (the forced
foliation would lose its empirical ground), or a light-element computation that missed. ⇒ **`PO-13` is
none of these.** It is a phase in a transfer, in the one sector whose instrument the corpus built itself
and has never claimed was finished.*

---

# ⛭⛭⛭ §6b · FRAMEWORK OR INSTRUMENT — *what disqualification would actually cost*

***`§6` answers whether the residual is an instrument defect. That is the narrow question and it is
answered. The question a fresh head asks is the wide one — what would disqualify the framework — and it is
not a question about a residual at all.***

## ⛔ THE NARROW ANSWER, KEPT SHORT SO IT IS NOT MISTAKEN FOR THE WIDE ONE

*For the height residual to be a framework fact there would have to be a physical defect that suppresses
$P_3$ by $3.5\times$, leaves the positions right to $7\%$, leaves $\theta_*$ right to $1.8\sigma$ and
$H_0$-free to five decimals, and **produces the identical failure on $\Lambda$CDM**, where the answer is
measured. **The last is very nearly a contradiction.** Every candidate that has moved a number was an
instrument fact and **none required a physical claim to give way.***

## ⛭⛭ THE WIDE QUESTION: A FRAMEWORK IS DISPLACED, NOT REFUTED BY A RESIDUAL

***What retires a physical framework is a better or equivalent account of what it explains. Nothing else
ever has.*** *So the price of disqualifying this one is the register, in full — and the register is not an
example, it is a count:*

| | |
|---|---|
| **structural recoveries** | **9** — *GR's whole solution family in the symmetry sector with the radiative types **provably absent**; the Carter constant as the substrate's symmetry; the Standard Model's groups and the chirality obstruction from the same structure as GR; three generations as an **index**; the vacuum sector as **index one**; the scale factor's self-adjoint freedom closed with **no free constant**; the two horizons a repeller/attractor pair with indices summing to zero* |
| **dissolutions** | **10** |
| **cross-field joins** | **11**, from 23 fields baked against 17 papers |
| **formal spine** | 196 environments, 14 named theorems, 6 axioms |
| **evidence rail** | 684 receipts, 633 registered, 627 passing, **99.2% of tolerance comparisons shown able to fail** |
| **classical identities proved** | 44 |

⇒ ***Any one of those thirty recoveries, dissolutions and joins is a thing a competitor must also
explain.*** *The Carter constant is one — GR carries it as a coincidence of Kerr and `P09` derives it,
with `I50` supplying why the derivation is not circular. **It is an illustration of the class, not the
case.** The same paragraph could be written for the radiative types, the generation index, the group
obstruction, or the index-one vacuum, and the corpus contains the material for each.*

## ⛭⛭ AND ON PARAMETERS, WHICH IS WHERE THIS DOCUMENT PREVIOUSLY MANUFACTURED A DEFICIT

⛔ ***An earlier draft of this section listed $\eta$, $\rho_r/\rho_m$, $A_s$ and $n_s$ as unpaid debts
because they are measured rather than derived. That is not a debt. It is what a physical theory does with
parameters, and the comparison class does the same.***

| | fitted parameters in the whole cosmology |
|---|---|
| $\Lambda$CDM | **6** |
| **this framework** | ⛭ **1** |

*with the background otherwise **two numbers, one of them measured calibration-free**. ⇒ **A framework that
measures fewer parameters than the standard model it competes with does not owe a debt for measuring
any.*** ⌗ *That error — presenting discipline as backlog — is the same one `§5b` was corrected for at
`r3744`, committed here one section later. **It is named rather than quietly removed.***

## ⛭ WHAT IS GENUINELY UNPAID, AT ITS ACTUAL SIZE

| | |
|---|---|
| ⟐ **the full-spectrum likelihood** | *a real build, and **`P15` names it itself*** |
| ⟐ **the end-to-end transfer** | *likewise — the two load-bearing buildable debts* |
| ⟐ **the high-$\ell$ damping signature** | *established real and non-reabsorbable; **not** established what it does to the observable, ~90% degenerate with $n_s$ at fixed $\theta_*$* |
| ⌗ **lithium** | *6–8$\sigma$ over — **and it is standard BBN's, not this framework's.** Recorded because it is in the sector, not because it is owed* |
| ⌗ **$S=A/4$** | *adopted rather than derived — **a convention shared with all of black-hole thermodynamics**, and `p0` declines the further claim correctly* |

⇒ ***Two real builds, one unresolved observational question, and two items that belong to the field rather
than to this framework.*** *That is the honest unpaid column, and it is short because the register is long
— **not because anything has been hidden.***

⛭ ***The claim this section supports, stated exactly: a framework with this register is not immune to
disqualification, it is EXPENSIVE to disqualify.*** *The two builds above are where a competitor would
start, and they are named at the same weight as the recoveries.*

---

## ⌗ THE PROPORTION, STATED PLAINLY

***196 formal environments. Fourteen named theorems and six axioms. 684 receipt files, 633 registered, 445
cited from the papers, 627 passing, 99.2% of their tolerance comparisons shown able to fail. 44 proved
classical-geometry identities. 23 mathematical fields baked against 17 papers and 104 markers landed.
Light-element abundances within $1\sigma$ and $\eta_{10}$ inside Planck's error bar. BAO at
$\chi^2/\mathrm{dof}\simeq1$ at any $H_0$. A background of two numbers, one of them measured
calibration-free, and one fitted parameter in the whole cosmology. GR's solution family, the Carter
constant, the Standard Model's groups, three generations as a stable index, and a quantum sector that
spends no free constant — from one substrate.***

***Against one unresolved residual — the peak POSITIONS in CR's own arm, one READ step in the register —
sitting inside an instrument whose height machinery has now been shown to fail WORSE on ΛCDM, where the
answer is known.***

⌗ *That is the ratio. It is recorded here so it does not have to be recalled under pressure.*

⛭ ***AND THE HONEST OTHER HALF, recorded with equal weight: six named-unrun quantities, 38 do-not-assert
markers, 38 debts, two load-bearing buildable debts named by `P15` itself, lithium still over-predicted at
$6$–$8\sigma$ as it is for everyone, the low-$\ell$ sector a wash, and $S=A/4$ adopted rather than
derived.*** *None of that is hidden in the corpus and none of it is hidden here. **A count that flatters
is worth nothing as a balance**, and this one is meant to be picked up when the residual looms — not to
make it smaller than it is, but to stop it from being the only thing in view.*
