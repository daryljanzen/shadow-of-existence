> **⌖ RETIRED r1552.** This was the force-vs-admit finding on the discrete skeleton (r327). **Landed:** the forcing register is throughout P7 and p0.
> Kept as record; **do not work from it.**


# FORCE vs ADMIT — the discrete-skeleton route returns ADMIT (bounded; not claimed for the rest)
# Finding (c21, r326). The prize-edge, worked. Stated for reversal.
# Scripts: scripts/move13_force_criterion_bite1.py, move13_force_criterion_bite2.py

## The question, sharpened (the increment over "mapped but no verdict")
The corpus held FORCE-vs-ADMIT as "mapped and open, no verdict earned" (dynamics frontier §6). With classical
(a) closed (ADMIT-generic, externally grounded) the live edge was **(b) the discrete S₃/A₂ skeleton**: does it
*force* quantum structure, or only *admit* it? "Admit" = sufficiency (a consistent quantization exists — the
lock, Move 12). **"Force" = necessity** — no consistent classical completion. A gauge symmetry never forces
that. The only thing that does is a **global obstruction**: a monodromy/cohomology class making a classical
*period* multi-valued, so single-valuedness demands an integrality (Bohr–Sommerfeld/holonomy) condition. So:
**FORCE iff P4's branched cover carries a monodromy class that obstructs a global classical section and forces
an integrality condition on a physical period; ADMIT-only iff that class is trivial on the physical phase space.**

## Bite 1 — the cover is genuinely monodromic (clears the first gate, decides nothing)
Against the built horizon cubic $r^3-\alpha^2 r+2M\alpha^2$: discriminant $-4(27M^2-1)$ (gauge $\alpha=1$),
Nariai at $M_N=\sqrt3/9$, the colliding roots split as $\pm\sqrt{M_N-M}$ — a genuine square-root branch point.
Encircling $M_N$ swaps two sheets: local monodromy $\mathbb{Z}/2$, global deck $S_3$ (P4). So the cover is
**nontrivially monodromic** — a quantity built from an *individual* root is multi-valued over the mass line.
But a *symmetric* function of the roots (the cubic's coefficients — $\alpha$, $M$, the discriminant) is
single-valued. So the verdict turns on one thing: is the physical period symmetric or individual-root-dependent?

## Bite 2 — the physical period is monodromy-invariant → ADMIT
The lock's physical period (P8 `sec:lock`, at source) is the graviton mode action
$S_n=\tfrac12\int dT\,a^3[\dot\phi_n^2-(\mu_n^2/a^2)\phi_n^2]$ with $\mu_n^2=n(n+2)-2$ (the $S^3$ TT-Laplacian
eigenvalue) and $a(T)=\alpha\cosh(T/\alpha)$ (the round-$S^3$ radius). Both depend on $(\alpha,n)$ **only**:
$\partial_M\mu_n^2=0$, $\partial_M a=0$. $\alpha=\sqrt{3/\Lambda}$ is the single symmetric scale; $n$ is the
harmonic index; neither is an individual monodromic root. The **only** $M$-dependence in the whole lock object
is the observer-attributed matter $2M/a^3$ — present only in the representational flat-$\Lambda$CDM projection,
absent from the ontological pure-$\Lambda$ background the tower lives on (P8 l.177).

So the $S_3$ cover monodromy runs entirely in the representational/vantage layer (which-horizon; the projected
matter) and **obstructs nothing on the physical phase space**: no multi-valued period, no forced integrality.
The tower's discreteness is the **compactness** of the closed $S^3$ (P8: "the closed topology enters as the
discreteness"), not a monodromy-forced quantization.

## Verdict (stated for reversal) — ADMIT, not FORCE; bounded; not claimed for the rest
**The discrete S₃/A₂ skeleton does not force quantum structure.** The physical period is monodromy-invariant,
the cover is gauge (the vantage, gauge by the axioms — THE_VISION §4), and the geometry admits a clean
quantization (the lock) without being compelled to one. This **closes the discrete-skeleton/cover-monodromy
FORCE route** and advances the corpus's "no verdict earned" to a bounded verdict on the main route.

**Bounds (face 18 — no swing either way):** ADMIT here is a clean structural fact, not a loss — it is
consistent with CR's standing character (a gravitational-cosmological unification where quantum structure
*drops out of* the absolute foliation, ADMIT, rather than being forced by the cubic). It does **not** establish
the universal "nothing forces quantum structure" — that stays unclaimed both ways. Unexamined routes held
open: the background-sector scale-factor half-line self-adjoint extension (a separate, boundary-*choice*
question, itself ADMIT-leaning — a choice is not a forcing), and any CR-native mechanism not yet examined.

## Bearing on the programme
The "prize" read as *the geometry forces quantum gravity* does not land via the discrete skeleton — but that
was never CR's claim. The substantive achievement stands: the geometry **admits** a clean unitary quantization
(the lock), and this finding pins *why* the skeleton doesn't upgrade that to a forcing — it is gauge, and the
physical period is invariant under it. Third clean negative of the arc (cover↔connection non-unification r321;
dynamic half not dangling r322; skeleton admits-not-forces here): the gate producing honest negatives where the
prize-pull wanted a yes.

---
## Bite 3 (r327) — the background-sector route also returns ADMIT (the route held open at r326)
The one route r326 left open: the scale-factor sector — does its half-line self-adjoint extension force
quantum structure? The operator (P8 `sec:deparam`) is $\Hphys=(2\pi/3)p_a^2/a-(\Lambda/8\pi)a^3$ on
$L^2(0,\infty)$. Liouville transform ($x=2\sqrt{c\,a}$, $c=2\pi/3$, so $a=x^2/4c$) turns the kinetic term
into $-\partial_x^2$ and the potential into $V\sim -x^6$. Weyl classification (`scripts/move13_force_bite3_background.py`):
- $x\to\infty$, $V\sim-x^6$ ($\beta=6>2$): WKB amplitude $p^{-1/2}$ with $p\sim x^3$, $|\psi|^2\sim x^{-3}$,
  $\int^\infty x^{-3}dx$ converges → **both** solutions $L^2$ → **limit circle** → boundary condition required.
- $x\to0$: regular endpoint ($V\to0$) → **limit circle** → boundary condition required.
- → deficiency indices $(2,2)$: a **U(2) four-parameter family** of self-adjoint extensions.

**Verdict — ADMIT, not FORCE (the strongest ADMIT of the three).** A consistent unitary quantization exists
(extensions exist), so sufficiency holds; but it is **non-unique** — a U(2) family of boundary-condition
choices, the antithesis of forcing (the classical theory picks none; physical input does). And FORCE's
prerequisite — a classical incompleteness quantization must resolve — is **absent**: CR cosmology is
non-singular (P8, sourced to BH_causality + CRcosmology), the classical layer complete, so no boundary
condition is forced "for consistency." Any discreteness a chosen BC induces is choice-dependent, hence not a
forced quantization of $\rho_d$.

## FORCE-vs-ADMIT — the completed verdict (both concrete routes)
Both candidate routes return **ADMIT, not FORCE**, with one common root: **CR's cosmology is complete on its
own (non-singular), so the geometry admits quantum structure but compels none.** The discrete skeleton (r326)
is gauge with a monodromy-invariant physical period; the background sector (r327) has a U(2) family of
extensions and no classical incompleteness to resolve. The corpus's "FORCE-vs-ADMIT: mapped, no verdict
earned" is now a **verdict on both examined routes: ADMIT.** The **universal** "nothing forces quantum
structure" stays **not claimed** (an unexamined CR-native route could still exist) — but the two concrete
candidates are settled. This is consistent with, and sharpens, CR's standing character: the quantum structure
*drops out of* the absolute foliation (ADMIT, the lock), it is not *forced by* the geometry.
