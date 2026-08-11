# The ADM / canonical recast chain — a receipts index (so it is used, not recreated)
*Corpus support/spine note. The `adm*` scripts are a coherent, hard-won analysis chain — the 3+1
(ADM) recast of the construction that grounds the anchor's energy sector, the constraint algebra, the
canonical-time/true-Hamiltonian resolution, and the (negative) quantum-grammar probes. They were
scattered across other consolidations or unreferenced; this note gathers the whole chain in one place
so a later instance reaches for the receipt rather than rebuilding it. Each entry: what the script
computes, its verdict, and where the result is consolidated. All receipts clean (sympy). Tags
[computed]/[established]/[reading]/[reach] as marked. Stated for reversal.*

## The core chain — `adm1`–`adm7`

- **`adm1.py` — the 3+1 split of the construction-gauge metric.** $ds^2=-f\,dt^2+dr^2/f+r^2d\Omega^2$:
  lapse $N=\sqrt f$, shift $0$, spatial 3-metric, 3-Christoffel/3-Ricci; with $f=1-2m(r)/r-\Lambda r^2/3$
  the Hamiltonian constraint gives $\rho=({}^3R-2\Lambda)/16\pi = m'(r)/4\pi r^2$ — the spherical
  **energy-sector anchor** in intrinsic ADM form. **[computed]** *(Consolidated in
  `anchor_consolidation.md`; the energy sector.)*
- **`adm2.py` — the Hamiltonian constraint on the vacuum dS leaf.** $H={}^3R+K^2-K_{ij}K^{ij}-2\Lambda=0$,
  checked in **both vantages** ($\sigma$ redistributes the $2\Lambda$ between $^3R$ and $K^2$). **[computed]**
  *(Consolidated in `anchor_consolidation.md` Receipts.)*
- **`adm3.py` — the constraint algebra under the $S_3$ generators.** $\sigma$ (signature flip,
  $\varepsilon\to-\varepsilon$, order 2) and $\tau$ (sky-angle triality on the cubic roots, order 3)
  generate $S_3=\mathrm{Weyl}(A_2)$; the permutation rep is trivial $\oplus$ standard-2d. The discrete
  stabilizer skeleton inside the continuous $\mathfrak{so}(5,1)$. **[computed]** *(Consolidated in
  `algebroid_closure_consolidation.md` §5, §7.)*
- **`adm4.py` — deparametrization in the $E{=}1$/Nariai clock.** The horizon cubic $r^3-r+2M$
  (gauge $\alpha{=}1$) has discriminant zero at the Nariai mass $2M=2/(3\sqrt3)$, double root
  $r_0=1/\sqrt3=\sigma$'s fixed point ($w=\pi/6$): the two $\sigma$-swapped roots (the standard-2d
  carrier) **merge exactly at the clock**. **[computed]** *(Canonical-time content; P8
  `canonical_time.tex`.)*
- **`adm5.py` — are the three horizon roots the spectrum of a natural operator? — NO.** $\tau$'s
  standard-2d eigenvalues are cube roots of unity (not the roots); the roots are the orbit-vector
  *components*, not operator eigenvalues; the companion matrix returns them only by construction
  (circular, not geometrically natural). The $S_3$-invariant discriminant $\to0$ at Nariai (the orbit
  collapses). A **negative** result. **[computed — negative]** *(The QG-grammar probe; see vision §5.)*
- **`adm6.py` — does a quantized spectrum carry the standard-2d $S_3$ rep? — NO.** The flat-FLRW
  dust+$\Lambda$ reduction is single-DOF ($a$, $p_a$) with no sky-angle $w$ among its variables: the
  homogeneous reduction has fixed the member to Nariai ($\sigma$'s fixed point), so the $S_3$ that lives
  on $w$ is not in the Hilbert space at all — quantizing gives a standard 1-DOF quantum cosmology with
  **no** standard-2d structure. **Sector gap, confirmed structurally.** **[computed — negative]**
  *(This is the receipt behind the vision's "‘$S_3$ on a quantum spectrum’ as a quantum gravity is
  **dead**, not to be re-inflated" — §5. Do not re-explore this route without reading these two first.)*
- **`adm7.py` — the deparametrized physical Hamiltonian $H_{\text{phys}}$ and its $\tau$-evolution.**
  Promoting $H_{\text{phys}}\to$ operator on $L^2((0,\infty),da)$ gives a genuine time-dependent
  Schrödinger equation $i\,\partial_\tau\Psi=\hat H_{\text{phys}}\Psi$ generating **unitary
  $\tau$-evolution** — *not* the frozen Wheeler–DeWitt constraint. The foliation is fixed by the
  absolute clock, so there is a true Hamiltonian and a true time: **the problem-of-time resolution**
  (with the honest technical caveat — operator ordering of $p_a^2/a$ and the half-line self-adjoint
  extension — flagged in the script, the spectrum not fabricated). **[computed; the QG content of P8]**
  *(Canonical-time content; P8 `canonical_time.tex`.)*

## The rest of the ADM family (already homed; listed for completeness)

- **`adm_so51_1.py`** — bracket closure on the symmetry-reducible sector: $\mathfrak{so}(5,1)=\mathfrak h\oplus\mathfrak m$,
  the three symmetric-space inclusions, $[\mathfrak m,\mathfrak m]\subset\mathfrak h$ at the symmetric cut
  (Move 6). *(`algebroid_closure_consolidation.md` §2–4.)*
- **`adm_strata_1.py`** — the isotropy stratification and the Nariai inner coincidence (horizon-cubic
  discriminant $-4\alpha^4(27M^2-\alpha^2)$, the isotropy jump $4\to6$ at $\Lambda M^2=1/9$) (Move 7).
  *(`algebroid_closure_consolidation.md` §6.)*
- **`adm_skeleton_strata_1.py`** — the discrete skeleton anchored at the strata (Nariai $=$ the $S_3$
  transposition fixed point) (Move 11). *(`algebroid_closure_consolidation.md` §7.)*
- **`adm_wall_1.py`** — the wall (Type N) is **not** a metric singularity (non-degenerate metric, VSI),
  so cosmogenesis is bounded to the Killing-horizon strata (Move 9). *(`algebroid_closure_consolidation.md` §6;
  vision §6/§7.)*
- **`adm_dynamics_1.py`** — Move 8: locating the confined Gowdy–dS wave in the isotropy stratification
  (which stratum the first bend sits on). *(`dynamics_frontier_gowdy-dS_canonical.md`.)*

## Move 12 — the lock: cosmological-sector canonical receipts

The lock (Move 12, THE_PLAN) is the identity **CMB frame $=$ comoving congruence $=$ NBC's $S^3$** on the closed-$S^3$ Nariai model, lifting P8's deparametrized $i\partial_\tau\Psi=\hat H_{\mathrm{phys}}\Psi$ off the flat minisuperspace toy. **STATUS: ASSEMBLED & WRITTEN INTO P8 §lock (r246–r250); the deepest [reach] returned YES structurally.** Its canonical receipts (distinct from the `adm*` chain), banked in sequence below with their as-of-banking tags; the r250 capstone at the end records the write-up and supersedes the "open core" / "can return no" caveats those earlier tags carried:

- **`canonical_sds_1.py` — the closed cosmological member's reduced canonical object, in the construction.** The $E{=}1$ Painlevé–Gullstrand comoving congruence gives the frozen reduced constraint $H_c=\tfrac12 P^2-M/r-r^2/2\alpha^2\approx0$ ($P$ conjugate to the areal radius $r$), whose Hamilton flow is the $E{=}1$ master equation and whose solution is the $\sinh^{2/3}$ flat-$\Lambda$CDM law; matter ($2M/r^3$) and $\Lambda$ ($1/\alpha^2$) are the geometry's own, Nariai fixing $M$ by $\alpha$. **[computed]** *(Flat comoving reading; `slicing_operator.tex` §cosmology.)*
- **`canonical_sds_2.py` — the two readings of one geometry, and what is genuinely open.** Flat comoving ($E{=}1$/PG, $\sinh^{2/3}$) vs closed synchronous; the dissolution is the corpus resolution (the clock is the external ontological cosmic time, the move is the selection, no internal-clock knot). **Carries a retraction note:** its $R(T)=\alpha\cosh(T/\alpha)$ is the **pure-dS ($M{=}0$) substrate**, not the $M\neq0$ ontological layer — do not build on that line. The dust-free deparametrization **form** on the closed object is the lock's open core. **[reading; partly retracted]**
- **`lock_flat_closed_transform.py` — the flat$\leftrightarrow$closed transform, verified in the dS embedding.** Closes `canonical_sds_2` open piece (b): the flat comoving and closed synchronous readings are **one comoving congruence under two synchronizations**. Verified (clean $0/{-}1$): the $(x,y,z){=}\text{const}$ worldlines are unit timelike geodesics on the hyperboloid ($\ddot X=X/\alpha^2$); $\eta(X,B)=\alpha e^{\tau/\alpha}$ depends only on $\tau$ (flat slices $=$ horospheres on the past null ruling $B$); $X_0$ depends on $\tau$ **and** $\rho^2$ (closed slice $T{=}$const is non-synchronous — the seam $\tilde\tau=\tau+\chi$, with $T=\tau$ only at $\rho{=}0$); $R^2=\alpha^2+X_0^2$ (closed $S^3$ of radius $\alpha\cosh(T/\alpha)$). $B$ (common past null generator) $=$ the NBC past boundary. **This establishes the lock's middle identity** — CMB frame $=$ substrate comoving congruence, with flat $\Lambda$CDM and the closed $S^3$ two synchronizations of that single frame, $B$ the NBC anchor. **[computed — at the substrate (pure-dS) level; the $M\neq0$ layer reading (matter $=$ the bend of the flat slicing, read leftward) and the dust-free deparametrization FORM remain — the lock's open core; [reach], can return no].** *(`slicing_operator.tex` §cosmology/§synchronous.)*

**The canonical–geometric loop (closes at source, no new receipt).** P8's deparametrized $i\partial_\tau\Psi=\hat H_{\mathrm{phys}}\Psi$ (with $H_{\mathrm{phys}}$ on the abstract remaining DOF $(q^A,p_A)$, lapse $d\tau=N\,dt$) and the dynamics paper's `dynamics_paper.tex` §gowdy are the **same deparametrized structure**: same form, same clock $d\tau=N\,dt$ ($N=e^{\gamma-\psi}$), with the remaining DOF made concrete as $\psi$ = the leaf's TT shear (the propagating graviton); the ENERGY/MOMENTUM constraints carry the wave entirely in the shear ($\psi_t^2+\psi_z^2$) — matter/radiation $=$ the bend (the §dissolution geometric face). The dust-free clock question (`canonical_sds_2` (a)) is **resolved against the internal-clock route** by §gowdy's two regimes: at $\Lambda{=}0$ the area $R$ serves as internal clock, but at $\Lambda{>}0$ that fails and the substrate cosmic time is forced — "the absolute foliation earns its necessity precisely where an internal clock breaks down." **Scope:** both models are wrong-model for the closed-$S^3$ lift (P8 flat FLRW; dynamics planar Gowdy $T^2$); both flag the closed-$S^3$ realization as open. So the loop closes at "canonical & geometric faces $=$ one deparametrized structure on the forced external clock"; the closed-$S^3$-specific $H_{\mathrm{phys}}$ (written on the r246 frame identity) and the quantization details remain the lock's open core. **[established — structural match at source; [reach] — the closed-$S^3$ H_phys remains].**

**`lock_hphys_background.py` — the lock's $H_{\mathrm{phys}}$, lifted to the closed-$S^3$ background geometry (verified).** On the background geometry (the reassigned-dS$_4$ that best represents the ontological layer; closed dS$_4$, $a(T)=\alpha\cosh(T/\alpha)$), a TT graviton mode (one $S^3$ tensor harmonic, eigenvalue $\mu_n^2$) has action $S_n=\tfrac12\!\int\! dT\,a^3[\dot\phi_n^2-(\mu_n^2/a^2)\phi_n^2]$; Euler–Lagrange gives the standard TT equation $\ddot\phi_n+3H\dot\phi_n+(\mu_n^2/a^2)\phi_n=0$ (residual $0$), and the Hamiltonian $H_{\mathrm{phys},n}=\pi_n^2/2a^3+\tfrac12 a\mu_n^2\phi_n^2$ reproduces it (verified). Deparametrized on cosmic time: $i\partial_T\Psi=\hat H_{\mathrm{phys}}\Psi$, $\hat H_{\mathrm{phys}}=\sum_n[\pi_n^2/2a^3+\tfrac12 a\mu_n^2\phi_n^2]$ — a **discrete tower of time-dependent oscillators** (one per $S^3$ TT harmonic; $\omega_n^2(T)=\mu_n^2/a^2$, mass $a^3$), unitary $T$-evolution (the standard graviton-on-dS squeezing Hamiltonian). **So the lock's $H_{\mathrm{phys}}$ closes structurally on the background geometry:** the TT graviton modes are P8's abstract remaining DOF made concrete; the closed-$S^3$ feature is the discrete tower (vs the planar Gowdy's continuum); it deparametrizes unitarily on cosmic time; no structural obstruction. **[computed — GIVEN the standard TT perturbation action (used, not re-derived from EH here); background-geometry (ontological-layer) level. Open: explicit $\mu_n^2$ ($S^3$ TT spectrum); the Nariai *representational* reading (the $M\neq0$ matter bend under the dS-null bundle); self-adjointness/ordering. [reach] returned YES at the structural level, not no.]**

**`lock_rep_reading.py` — the representational reading: $H_{\mathrm{phys}}$ in the Nariai observer frame (closes the arc; verified).** The same ontological graviton tower, projected under the dS-null bundle into the Nariai observer frame (the fundamental/reassigned-ruling congruence, scale factor the areal radius $a(\tau)=(2M\alpha^2)^{1/3}\sinh^{2/3}(3\tau/2\alpha)$, flat slices $\to$ continuous $k$). Verified: (i) the Friedmann readout $H^2=(\dot a/a)^2=2M/a^3+1/\alpha^2$ (residual $0$) — the $M\neq0$ **matter bend** $2M/a^3$ (dust) $+$ $\Lambda$, vs the background geometry's pure-$\Lambda$ $H_{\mathrm bg}^2\to1/\alpha^2$ (cosh); the matter is the representational difference, exactly P7's "matter $=$ the bend of the slicing." (ii) the graviton mode has the same deparametrized structure — E–L gives $\ddot\phi+3H\dot\phi+(k^2/a^2)\phi=0$ (residual $0$), $H_{\mathrm{phys}}=\pi^2/2a^3+\tfrac12 ak^2\phi^2$, $i\partial_\tau\Psi=\hat H_{\mathrm{phys}}\Psi$ unitary — now with the bend carried in $a(\tau)$; the observer's spectrum is the flat-$\Lambda$CDM primordial-GW spectrum. (iii) mode content: the **discrete $S^3$ tower** (background, global/compact — the ontological spectrum) reads as **continuous $k$** (observer, local non-compact horosphere patch) — the two slicings of r246's one congruence; consistent, not in tension. **So the lock's arc closes:** the deparametrized graviton tower lives on the closed-$S^3$ ontological layer (background, r248), and projects under the dS-null bundle to the observable flat-$\Lambda$CDM graviton an observer sees (representational), with the matter bend entering as a projection feature, not an ontological one. **[computed — closes the arc at background + representational level. Open (unchanged): explicit $\mu_n^2$ & the discrete$\to$continuous restriction map; TT action from EH (used, not re-derived); self-adjointness/ordering.]**

**r250 — WRITTEN INTO P8 §lock + the three open items sharpened (the capstone).** The receipts above (r246–r249) are assembled into `canonical_time.tex` §\ref{sec:lock}, "The closed-$S^3$ lift: the graviton sector on the layer" (after §deparam, before §dissolution). The three items the earlier tags left open are now sharpened to referee level in-paper: (i) the explicit $S^3$ TT spectrum $\mu_n^2=n(n+2)-2$, $n\ge2$; (ii) the reduced TT action $S_n=\tfrac12\int dT\,a^3[\dot\phi_n^2-(\mu_n^2/a^2)\phi_n^2]$ (the second-order EH tensor sector, standard reduction — stated, not re-derived from scratch); (iii) self-adjointness — each graviton mode a full-line $L^2(\mathbb{R})$ oscillator (clean), with the half-line/ordering residual correctly relocated to the **background scale-factor** sector, not the propagating one. **This supersedes the "open core" / "can return no" / "Open: …" caveats in the r246–r249 tags above:** the representational reading (r249) closed the arc, and the $\mu_n^2$/action/self-adjointness items (r250) are discharged in P8. Compiles clean (9 pp). **Remaining residuals, honest and background-sector only:** scale-factor self-adjointness on the throat/half-line domain; super-quadratic tower↔background couplings. **[the lock assembled & written up; [reach] returned YES structurally; residuals are background-sector technical closure].**

**One-clock reading (r268) — the lock receipts ground the one-clock test at the connection level (THE_PLAN one-clock bullet).** The lock arc is exactly the connection-level one-clock identity on its own member: r247 (`lock_flat_closed_transform.py`) anchors the one comoving congruence at $B$ (the NBC past boundary); r248=r249 (`lock_hphys_background.py`, `lock_rep_reading.py`) give the *same* deparametrized $H_{\mathrm{phys}}$ on both synchronizations — so the along-orbit trivialization (one clock) underwrites both faces; and r267 (`f1_leak_gradKG_identity.py`) fixes the transverse restriction as the modulus $=$ the bend $=$ the representational projection of that same congruence (matter $=$ the bend, P7). So the along-orbit and transverse restrictions of the one connection are the **same data** on the lock member; the falsifiable NO (independent trivializations) is closed there. The one-clock test is thereby downgraded from a wide-open [reach] to **resolved-on-the-member**, residual the general-strata along-orbit synchronization-independence. *[synthesis, no new receipt; state for reversal.]*

## How this chain sits in the programme

The chain is the **canonical (ADM) face** of the construction: `adm1`–`adm2` are the anchor's energy
sector; `adm3` is the constraint algebra and its discrete $S_3$ skeleton; `adm_so51_1`/`adm_strata_1`/
`adm_skeleton_strata_1`/`adm_wall_1` build the algebroid's bracket/stratification (Moves 6–11);
`adm4`/`adm7` are the deparametrization and the true Hamiltonian that resolve the problem of time (P8);
and `adm5`/`adm6` are the **negative** probes that closed the "$S_3$-spectrum as a quantum gravity"
route. Reach for these before recomputing any ADM split, Hamiltonian/momentum constraint, bracket
closure, stratification, or deparametrization in this programme.
