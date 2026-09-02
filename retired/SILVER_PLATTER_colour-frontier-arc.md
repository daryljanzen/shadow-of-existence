> **⌗ MOVED TO `retired/` r2380 — AND THE ONLY THING THAT CHANGED IS THAT IT IS NOW WHERE IT WAS ALREADY
> FILED.** *`INDEX.md` has filed this under **Retired → Briefings** — "a worked frontier distilled for a fresh
> head; read when that frontier comes up" — while the file sat at top level.* ***That is the exact rule this cut
> runs on:*** *"**RETIRE means the file LEAVES the working directory**, so a listing shows only what is live —
> a banner at the top of the file is not retirement, it is a sticky note" (c49 r1452, Daryl).* **It was
> classified retired and physically live, which is the same defect one layer down.**
>
> **⌗ ITS OWN WARNING IS WHY THE MOVE MATTERS, and it is the sharpest self-guard in the corpus:** *"a
> distillation **frozen at its own arc, c19–c20 / r282–r296** — roughly **1330 revisions** before the present …
> **verify every load-bearing line at the sources pointed to below before building on it. Do not let this
> document become a gist you trust in place of the source — that is the exact failure the programme is built to
> defeat.**"* ***A briefing that warns you not to trust it is a briefing that belongs behind the filter.***
> ⌗ *Its register — **not claimed, held both ways: colour-from-geometry neither asserted nor refuted** — is
> live and lives in `PO-4` and `PO-3`, not here.*

---

# The Silver Platter — the colour-frontier arc, distilled for a fresh head

*Written c19, 2026-06-17, from the breadcrumb trail jotted across c16→c17→c18 (with Daryl's interjections) in `colour_frontier_dS6.md`, the 2012 thesis read (logged at CORPUS_MAP r282), and the corpus. This is a CLEAN distillation of that working notebook — read it to get to the frontier in one sitting, then **verify every load-bearing line at the sources pointed to below before building on it.** The register is **not claimed, held both ways**: colour-from-geometry is neither asserted nor refuted. The bounded result is banked; the universal is open. Do not let this document become a gist you trust in place of the source — that is the exact failure the programme is built to defeat.*


> **⚑ WHAT THIS DOCUMENT IS — read this before its contents (added r1627).** `INDEX.md` files this under
> **Retired → Briefings**: *"a worked frontier distilled for a fresh head; read when that frontier comes up."*
> It is a **distillation frozen at its own arc, c19–c20 / r282–r296** — roughly **1330 revisions** before the
> present. It is **not** a standing document and **not** maintained in step. Its internal record (the c20 gate,
> the r296 relay) is the record *of that arc*; **it is not evidence of currency against the corpus today**, and
> the question of whether any line here still holds is answered only at the corpus, never here.
>
> **⚠ A MISTAKE MADE ON THIS DOCUMENT AT r1625–r1626, recorded so it is not repeated.** A node read it as live
> operating infrastructure and audited its *"register"* for staleness — first reporting it stale (wrong), then
> "correcting" that from the document's own r296 relay note (also wrong, and wrong in the same way: internal
> consistency at r296 says nothing about r1626). **Both errors came from not checking what kind of document it
> is.** The classification is one line in `INDEX.md` and it settles the question: a briefing, read when its
> frontier comes up, verified against the corpus at that time.
>
> **⚑ SOURCE POINTERS REPAIRED r1626 — the one repair that was warranted.** This briefing's own instruction is
> *"verify every load-bearing line at the sources pointed to below,"* and **every §6 pointer that could break,
> had** — six repointed: `colour_frontier_dS6.md` → `retired/`, `algebroid_closure_consolidation.md` →
> `corpus/`, `THE_VISION.md` → `retired/`, `framework_paper.tex` → `CR_framework.tex` (P7, renamed since),
> `adm3.py` → `scripts/`. **Every target was alive; only the addresses were wrong.** A briefing that cannot
> reach its own sources cannot be verified when its frontier comes up, which is the only time it is read.

---

## 0. What this is, in one breath

The forward frontier (Entry 9, frontier-1) asks whether the Standard Model's continuous internal **colour SU(3)** can be read off CR's geometry as a shadow of substrate symmetry. The arc below traversed three candidate routes, each of which failed by the **same** structural fact, and then — at the 2012 thesis source — located *exactly where* an SU(3) does live and *why* the real substrate cannot carry it. The net effect is not a wall and not a route: it is a **sharply-constrained, decidable open problem**, handed over with the geometric constraints that make it poseable.

---

## 1. The question

> Does the SM's gauge structure — above all its **chiral** fermion content — cohere with **colour-as-residual-substrate-isometry**, demanding and constraining a rise to a 6-dimensional substrate; or does the geometry keep the gauge-capable horn shut?

Banked starting point (Move 13, from `corpus/algebroid_closure_consolidation.md` §8; **[computed]**; path repointed r1626):
- The SdS horizon cubic $r^3-\alpha^2 r+2M\alpha^2$ has **no quadratic term** ⟹ its three roots sum to zero (a traceless candidate $\mathfrak{su}(3)$ Cartan element); the involutions $\sigma,\tau$ generate $S_3=\mathrm{Weyl}(A_2)$ permuting them ⟹ the $\mathfrak{su}(3)$ **Cartan + Weyl skeleton** is present, geometrically grounded since the 2012 fundamental ellipse.
- $SU(3)$'s smallest faithful **real** rep is 6-dimensional ⟹ $\mathfrak{su}(3)\subset\mathfrak{so}(6)$, $\mathfrak{su}(3)\not\subset\mathfrak{so}(5)$. The gravitational substrate dS₅ $=SO(5,1)/SO(4,1)$ has **compact isometry $SO(5)$** ⟹ **no continuous $\mathfrak{su}(3)$ geometric isometry on dS₅**; the skeleton is a discrete $S_3$ shadow only — gravity-minimal.
- A continuous, gauge-capable $\mathfrak{su}(3)$ as a real spacetime isometry would need a rise to dS₆ $=SO(6,1)/SO(5,1)$, whose compact isometry $SO(6)\supset SU(3)$. The resonance **permits, does not force** the rise.

---

## 2. The breadcrumb trail (the arc as actually traversed)

Read this for *how the constraints were earned* — including the catches, because the discipline is part of the inheritance.

**Move A — the wrong rock, then the right one.** The first pass cleared Witten's KK chirality no-go by noting its premises (a metric product $M_4\times K$, gauge = isometry of a separate internal $K$, chirality = index of the internal Dirac operator on $K$) all fail against CR's irreducible de Sitter substrate. **c17 caught this as a load-bearing error**: the product was Witten's *setting*, not the operative hypothesis. The real obstruction is the **Atiyah–Hirzebruch vanishing theorem** — on a *compact* oriented spin manifold with a nontrivial smooth (e.g. circle) action, the equivariant Dirac index vanishes; **no product structure in the hypotheses**, the trigger is the *continuous isometry itself*. A continuous compact $SU(3)$ isometry walks straight into it (doubly, for nonabelian compact $G$, via Lawson–Yau PSC + Lichnerowicz). The one escape is that **de Sitter is non-compact** — precarious, because if the fermion zero modes ride a *compact* slice (an $S^5$) on which $SU(3)$ acts, the theorem bites regardless. **Reflexive lesson (carry it):** never clear an obstruction by noting CR differs from a standard framework on a feature the obstruction *does not depend on*.

**Move B′ — the gauge-emergence question, upstream of chirality.** Before chirality can even be posed, two things must be fixed: does a substrate $SU(3)$ isometry actually *become* a 4D gauge symmetry, and *which manifold/operator carries the fermion zero modes*? The framework-independent dimension fact is the upstream rock: $\mathfrak{su}(3)$ (8-dim) acts effectively only on manifolds of dim $\ge 4$ (minimal homogeneous spaces $CP^2$[4], $S^5$[5], flag[6]); it **cannot** act on a $<4$-dim space. A dS₆→4D cut is **codim-2**; the sliced-away piece is 2-dimensional, too small for $\mathfrak{su}(3)$. So colour cannot be the isometry of a sliced-away internal factor (the substrate is irreducible, not a product). KK-style colour gauging would need $\mathfrak{su}(3)$ as the isometry of an internal fibre (minimally $CP^2$ → an 8-dim substrate; the full SM → the Witten-7 → 11-dim). **dS₆ is too small for KK colour; CR's route is not KK; the gauging mechanism is genuinely novel and unbuilt.**

**Move B′ stress-tested (c17) — the dS₆ rationale refutes its own purpose.** $SU(3)$ acts **transitively** on the spatial slice $S^5=SU(3)/SU(2)$, so it preserves no proper $S^3$; and its *only* equivariant reduction of $S^5$ is the Hopf fibration $S^5\to CP^2$, on whose base it again acts **spatially**. There is no equivariant $S^5\to S^3$. So geometric-isometry $SU(3)$ on dS₆ is necessarily a **transitive spatial** symmetry — exactly *not* the internal colour it was invoked to supply, and the cosmological $S^3$ cut breaks it. The rise was justified by "colour must be a geometric isometry," but geometric-isometry colour is spatial-not-internal — **the dS₆ rationale collapses its own motivation.**

**The pivot (c18, building on c17) — and its failure.** If colour is *not* a geometric isometry, the one CR structure that is continuous-and-internal is the **algebroid connection** (the $[\mathfrak{m},\mathfrak{m}]\to\mathfrak{m}$ transverse-modulus leak): continuous, a connection (not a Killing isometry, so *not* the object Atiyah–Hirzebruch obstructs), and a connection is the math a gauge field is — and the $A_2/S_3$ skeleton's roots move with the very modulus $M$ the connection varies. So the colour search relocated off the dS₆ rise entirely, onto whether the algebroid connection on the *existing* dS₅ carries $\mathfrak{su}(3)$. **c17 type-checked it and it failed:** the connection is $\mathfrak{so}(5,1)$-valued ($\mathfrak{m}=\mathfrak{so}(5,1)/\mathfrak{so}(4,1)$, dim 5), and **$\mathfrak{su}(3)\not\subset\mathfrak{so}(5,1)$** (a compact $\mathfrak{su}(3)$ must lie in the max compact $\mathfrak{so}(5)$, and $\mathfrak{su}(3)\not\subset\mathfrak{so}(5)$ — so it is nowhere in $\mathfrak{so}(5,1)$: not in $\mathfrak{h}$, not in $\mathfrak{m}$, not in the connection). The $M$-link is a 1-parameter flow; one parameter cannot be 8 generators. The pivot walked back into the exact fact that forced the dS₆ rise. **Reflexive lesson:** matched by adjective (connection ≈ gauge field), skipped the structure group.

**The convergent pattern.** Three candidates for continuous internal $\mathfrak{su}(3)$, all fail by one fact:
1. geometric isometry on dS₆ — present but **spatial**, not internal;
2. discrete cubic $S_3$ on dS₅ — the **Weyl group**, not the group;
3. algebroid connection on dS₅ — **$\mathfrak{so}(5,1)$-valued, $\mathfrak{su}(3)\not\subset\mathfrak{so}(5,1)$**.

**The Coleman–Mandula reading — planted, then RETRACTED as a manufactured wall (c17).** c18 read the pattern as Coleman–Mandula (irreducible substrate ⇒ no internal factor ⇒ no internal gauge from geometry, *any* group). c17 tore it out: (1) C–M constrains the **global S-matrix** symmetry of a massive relativistic QFT — it says nothing about a **gauge** (local) symmetry, which sits outside it (with SUSY, conformal); the internal/spacetime divide is a heuristic, not the theorem. (2) "Irreducible ⇒ no internal gauge, any group" is refuted by $S^5$ (irreducible) Hopf-fibering over $CP^2$ with $\mathfrak{su}(3)$ acting — irreducible manifolds *do* fibre. (3) The algebroid connection is itself gauge structure born from the irreducible dS₅ — so the obstruction is the **specific content** ($\mathfrak{su}(3)\not\subset\mathfrak{so}(5,1)$), never categorical. **Reflexive lesson, one rung up:** the same adjective-match moved from the object to the *explanation* of the object — more seductive because the conclusion is clean and the name is impressive.

**The genericity check, run at source (c18 grind).** Before banking the consolation prize ("the cubic carries an $A_2$ skeleton"), the skeptic's challenge: every depressed cubic has roots summing to zero with an abstract $S_3$ — is CR's more? **It is genuine, geometrically forced** — the skeptic's "numerology" wall is refuted:
- the cubic linearizes to a **pure triple-angle** $2M=\tfrac{2}{3\sqrt3}\sin 3w$ in a genuine geometric angle $w$ (the distinguished observer's gnomonic sky angle), with the scale **forced**;
- the three roots are a genuine **$D_3$-orbit on the sky-angle circle** ($\tau=120^\circ$ rotation, $\sigma=$ reflection $w\leftrightarrow\pi/3-w$, derived coordinate-independently, $D_3=S_3=\mathrm{Weyl}(A_2)$);
- the **fundamental ellipse** $r^2+rr_0+r_0^2=1$ is the genuine **$A_2$ quadratic form** (matrix $[[1,\tfrac12],[\tfrac12,1]]$, eigenvalues $\tfrac12,\tfrac32$ — ratio 1:3, the $A_2$ Cartan signature — the hexagonal/Eisenstein lattice norm), with the involutions its genuine reflections;
- roots sum to zero = a genuine $A_2$ Cartan element / the three weights of the **3**.

**But it is the discrete skeleton, and representational.** What is established is the $A_2$ **root-system / Cartan / Weyl** level — rank-2 Cartan, the $D_3$ Weyl group, hexagonal root geometry — i.e. exactly the *discrete* skeleton, not the continuous $\mathfrak{su}(3)$ (8 generators + brackets). And crucially it is realized as a **symmetry of the observer-vantage groupoid**: $\sigma,\tau$ permute the *descriptions* of the one rigid SdS geometry while fixing the geometry. It lives in the **perspectival/representational** layer (how the hole is charted), **not** as a continuous symmetry acting on substrate fields/matter. So beyond the dimension obstruction, there is a **type** reason the skeleton stays discrete-and-representational.

**The 2012 thesis grounding (Daryl's interjection) — where $SU(3)$ actually lives, and why the substrate can't carry it.** Read and re-derived independently (not taken on the corpus's citation): the maximally symmetric $R_{\mu\nu}=\Lambda g_{\mu\nu}$ isotropic about every point ($\Lambda>0$) is **dS₅**, and **de Sitter is the unique real maximally symmetric Lorentzian manifold** (thesis Ch.3, l.367). The sharpening:
- Maximal symmetry ⟹ $SO(5,1)$ is the **complete** continuous symmetry of the substrate; there is no further symmetry to find, **by construction**. So $\mathfrak{su}(3)\not\subset\mathfrak{so}(5,1)$ is not "happens not to fit" — it is **structural: the symmetry is exhausted at $SO(5,1)$.**
- $SU(3)$'s home $SO(6)$ is the isometry of the **Wick-rotated** substrate $S^5$ (the Euclidean $x_0\mapsto ix_0$ face, reached by the Wick rotation — **not** by $\sigma$; the σ=Wick identification is refuted in §5a, the test-1 result: $\sigma$ fixes $x_0$ and the geometry, the Wick rotation complexifies $x_0$ and changes it) and, separately, of the compact part of $SO(6,1)$ on the dimensionally-raised dS₆. **Both routes to $SU(3)$ leave the real Lorentzian substrate** — by flipping the signature ($\to S^5/SO(6)$) or by adding a dimension ($\to$ dS₆).
- **What is established here:** $\mathfrak{su}(3)$ lives on the $SO(6)$ face (Wick-rotated $S^5$, and the raised dS₆), off the real Lorentzian substrate; and $\sigma$ is a genuine signature-flip involution on the real substrate (the $r=\sqrt{3/\Lambda}$ seam, the root-exchange $w\leftrightarrow\pi/3-w$). **What is NOT established — the hinge — [reading; not claimed, both ways]:** that this real-substrate $\sigma$ *is* the Wick rotation $x_0\mapsto ix_0$ bridging $SO(5,1)\leftrightarrow SO(6)$, and hence that the discrete $A_2$ skeleton *is* the real-Lorentzian shadow of the Wick-face $\mathfrak{su}(3)$. That identification is **test 1** below; the source (`colour_frontier_dS6.md` l.197) tags it not claimed, and it must not be promoted past that. It is plausibly a *deepening* (explaining *where* $\mathfrak{su}(3)$ sits and *why* the substrate lacks it) — but "$\sigma$ is the bridge" matches two signature-flips by shared flavor, which is exactly the trap to resist until the source decides. **It is not a new route to colour and not a wall.**

---

## 3. The geometric constraints (the hard facts a fresh head holds)

Each is source-verified; **C-numbers** for reference.

- **C1.** Substrate $=$ dS₅, maximally symmetric, the *unique* Lorentzian such manifold; $SO(5,1)$ (dim 15) is its **complete** continuous symmetry — **exhausted**.
- **C2.** $\mathfrak{su}(3)\not\subset\mathfrak{so}(5,1)$, and this is **structural** (a consequence of C1, not an accident): $\mathfrak{su}(3)\subset\mathfrak{so}(6)$, $\not\subset\mathfrak{so}(5)=$ max compact of $\mathfrak{so}(5,1)$.
- **C3.** $\mathfrak{su}(3)$ acts effectively only on $\ge4$-dim spaces; on a 6-dim substrate it acts on the spatial slice $S^5=SU(3)/SU(2)$ **transitively and spatially** (Hopf $S^5\to CP^2$; never an equivariant $\to S^3$). Geometric-isometry colour is therefore spatial-not-internal, and the cosmological $S^3$ cut breaks it.
- **C4.** All three examined routes to a continuous internal $\mathfrak{su}(3)$ (dS₆ isometry / discrete cubic $S_3$ / algebroid connection) fail by C2/C3. $\mathfrak{su}(3)$ is nowhere an internal piece of CR's spacetime-symmetry algebra.
- **C5.** The chirality rock: a continuous compact $SU(3)$ acting on a *compact* slice ⟹ equivariant Dirac index $=0$ (Atiyah–Hirzebruch; doubly for nonabelian compact $G$) ⟹ vector-like. Only escape: dS's non-compactness — precarious if zero modes ride a compact $S^5$ slice. **(This is downstream; it cannot be posed until the carrier geometry is fixed.)**
- **C6.** The $A_2/D_3$ skeleton is **genuine** $A_2$ root-system geometry (geometrically forced: the sky-angle triple-angle with forced scale; the fundamental ellipse $=$ the $A_2$ quadratic form), but it is **discrete** (Cartan + Weyl, not the Lie algebra) and **representational** (a symmetry of the observer-vantage groupoid — permuting descriptions of one rigid geometry — not of field content).
- **C7 (established).** $SU(3)$ lives on the $SO(6)$ face — the Wick-rotated $S^5$ ($x_0\mapsto ix_0$) and the compact part of $SO(6,1)$ on the raised dS₆ — both **off** the real Lorentzian substrate; and $\sigma$ is a genuine signature-flip involution **on** the real substrate (the $r=\sqrt{3/\Lambda}$ seam / the root-exchange $w\leftrightarrow\pi/3-w$).
- **NOT a constraint — the open hinge [not claimed, both ways; this is test 1, not a fact]:** that the real-substrate $\sigma$ *is* the Wick rotation bridging $SO(5,1)\leftrightarrow SO(6)$, and hence that the discrete $A_2$ skeleton *is* the real-Lorentzian shadow of the Wick-face $\mathfrak{su}(3)$. Source tags this not claimed (`colour_frontier_dS6.md` l.197); it identifies two signature-flips by shared flavor and is precisely what test 1 decides. **Do not hand a fresh head this clause as given** — taking it as fact starts test 1 with the answer baked toward "genuine lift." (Caught by c17 on relay; an earlier draft of this platter wrongly listed it as source-verified C7.)

---

## 4. The not claimed boundary (do not cross it from gist)

- **BANKED (earned):** colour-$\mathfrak{su}(3)$ is **not** a continuous internal gauge symmetry readable from CR's geometry **via the three examined routes**, by the convergent facts $\mathfrak{su}(3)\not\subset\mathfrak{so}(5,1)$ and $\mathfrak{su}(3)$-acts-spatially-on-$S^5$. A **bounded** structural result — *suggestive of, not establishing,* a deeper pattern.
- **NOT BANKED (unearned):** the Coleman–Mandula reading; "irreducible ⇒ no internal gauge from geometry, any group"; "colour-from-geometry foreclosed." Three routes + one misapplied theorem ≠ the exhaustive grind a universal kill needs.
- **Colour is not in jeopardy; colour-*from-geometry* is the frontier.** Colour can exist the ordinary way (an $SU(3)$ matter bundle put in by hand). What the arc pressures is the *vision's specific hope* — colour read off the geometry as a shadow (Entry 9 frontier-1) — **not CR's consistency.** The gravitational core (P1–P10, the lock, the cosmology, the algebroid-as-gravity) is untouched and correctly asserts no colour.
- **Gravity-minimal = gravity-complete.** dS₅ is the *complete* gravitational substrate; gravity is the whole of what the geometry gives; colour, if present, is non-geometric. This is the established gravitational reading — **not** a promotion to "colour is provably non-geometric."

---

## 5. The geometric problem, posed with sufficient constraint

The constraints localize the question to a single decidable structural relationship. State it cleanly, at not claimed weight:

> **Conjecture under test (not claimed, both ways):** that the genuine discrete $A_2/D_3$ skeleton on the real Lorentzian dS₅ substrate is the $\sigma$-shadow (signature-flip image) of a continuous $\mathfrak{su}(3)$ living on the Wick-rotated $S^5/SO(6)$ face. **The question:** is that shadow-relationship a genuine geometric *mechanism* — does $\sigma$ (verified only as a real-substrate signature-flip involution, *not* yet as the Wick bridge) lift the discrete skeleton to a continuous $\mathfrak{su}(3)$ that acts *internally* on the 4D cut's matter (not spatially) and survives the chirality rock — or is it merely an exact account of *where $\mathfrak{su}(3)$ sits* (with $\sigma$ as real-form bookkeeping) while colour-from-geometry stays blocked through every real-substrate route? The shadow-relationship is **not** assumed; establishing or refuting it *is* test 1.

The constraints make this **decidable**, and they supply the tests. **Test 1 is the live unverified hinge of the whole frontier — compute it first**, precisely because it is where the fourth catch is waiting (see the closing note); do not let the other two be reasoned about as if test 1 had already returned "genuine lift."

1. **The $\sigma$-lift test [the hinge — first to compute].** Is the real-substrate root-exchange involution $\sigma$ ($w\leftrightarrow\pi/3-w$, the $r=\sqrt{3/\Lambda}$ seam) actually the Wick rotation $x_0\mapsto ix_0$ that carries $SO(5,1)\to SO(6)$ — and does it thereby extend to a *continuous* geometric relation between the real-substrate $A_2$ skeleton and the Wick-face $\mathfrak{su}(3)$? Runnable at the **fundamental-ellipse source** against the **Lorentz-sphere Wick structure** ($x_0\mapsto ix_0$, the $\mathrm{sgn}(\alpha^2)$ family). **Pre-name all three outcomes so none is manufactured:** a genuine continuous lift (the vision's payoff); a partial one; or a formal coincidence ($\sigma$ as real-form bookkeeping, the two signature-flips merely sharing flavor — which *closes* frontier-1 as structure, with the core and the $A_2$ gem intact). Bank none of the three in advance.
2. **Internal-vs-spatial on the Wick face.** On dS₆ the action was transitive-spatial (C3). Does the *signature flip* to $S^5/SO(6)$ change the character of $SU(3)$'s action — can the cosmic-time cut render the relevant directions internal on the Wick face where it could not on the Lorentzian one? (If the Hopf $S^5\to CP^2$ obstruction simply recurs, the answer is no.)
3. **The chirality rock (C5).** Posed **only after** 1–2 fix the carrier geometry: does the relevant equivariant Dirac index vanish (Atiyah–Hirzebruch / Lawson–Yau–Lichnerowicz), or does dS's non-compactness genuinely evade it *without* importing the continuum-spectrum sickness of non-compact reductions?

The likely shapes of the answer, named in advance so neither is manufactured: a **genuine lift** that gauges internally and survives chirality would be the vision's payoff; a **failed lift** (the $\sigma$-shadow is real-form bookkeeping with no continuous mechanism on the real substrate) closes frontier-1 as a structural fact while leaving CR's core and the genuine $A_2$ gem intact. **Hold both open; let the source decide.**

---

## 5a. RESULT — test 1 computed (c20 gate, 2026-06-18): **FORMAL COINCIDENCE** — σ is **not** the Wick rotation. **[the gate's call, stated for reversal; going to the relay / a cold referee for the different-node check. Receipt: `scripts/sigma_lift_test1.py`; full argument: `retired/colour_frontier_dS6.md` test-1 section *(path repointed r1626)*.]**

Decided in the embedding coordinates, not by flavor. The two objects, exhibited as explicit operations on $\mathbb{M}^6$:
- **Wick** $x_0\mapsto ix_0$: complexifies the **global timelike** coordinate; sends $\eta_L\to\eta_E$ ($SO(5,1)\to SO(6)$, via $J^\top\eta J$); imaginary; **changes the geometry**. Genuinely the bridge to where $\mathfrak{su}(3)$ lives.
- **σ** ($w\leftrightarrow\pi/3-w$ = the ellipse diagonal reflection $(r_0,r)\mapsto(r,r_0)$): a **real** $\mathrm{Weyl}(A_2)$ reflection of the **spatial** sky/root plane that **fixes $x_0$**, preserves *both* signatures (so it is **not** a signature flip), and **fixes the geometry** (a description-groupoid morphism — it permutes charts, not the manifold).

They differ on every axis: real discrete reflection vs imaginary continuation; spatial root plane vs the time axis; fixes the geometry vs changes it. **Clincher (re-derives C2):** $\mathfrak{so}(5)$ (the $x_0$-fixing spatial rotations) gives only $\mathbb{R}^5$, but $\mathfrak{su}(3)$ needs a 6-dim faithful real carrier, so $\mathfrak{su}(3)\subset\mathfrak{so}(6)$, $\not\subset\mathfrak{so}(5)$ — it **must** use the $\mathfrak{so}(6)\setminus\mathfrak{so}(5)$ generators the Wick rotation makes, the sector **σ fixes**. So σ cannot be the Wick bridge and does **not** carry the $A_2$ skeleton to $\mathfrak{su}(3)$. The §2/§3 hinge clause and the c18 `colour_frontier_dS6.md` l.197 leap matched a real spatial reflection to an imaginary time-complexification **by flavor**; in coordinates it is false.

**What this closes (bounded — face 18 held):** colour-from-geometry **via the σ-lift** is closed *as structure* (frontier-1's specific hope — the $A_2$ skeleton as the σ-shadow of substrate symmetry — does not hold). **Intact:** the gravitational core; the genuine discrete $A_2$ gem (C6); $\mathfrak{su}(3)$ genuinely on the Wick/$SO(6)$ face (C7, reached by the Wick rotation, not by σ). **Do-not-assert, unchanged:** the *universal* "colour-from-geometry foreclosed" — this decides the σ-lift hinge, not every conceivable route; colour the ordinary way (an $SU(3)$ matter bundle by hand) was never in jeopardy. Tests 2–3 are moot for this route (they were downstream of a carrier the σ-lift would have supplied). **The fifth catch would be banking this as settled before the different node has read it cold** — hence stated for reversal, for the relay.

**Relay closed (r296):** both nodes concurred — **c19** (different-node, held for reversal) and **c17** (cold referee, cleared). The verdict holds across all three seats; σ ≠ Wick is **coordinate-invariant** (signature-changing complexification vs signature-preserving real reflection — not identifiable by any basis change). Two fixes baked, neither reversing the call: (1) the σ-fixes-x₀ **ground relocated out loud** — it rests on C6 (σ a *signature-independent* Weyl(A₂) reflection realized identically in both real forms, the reason it is an isometry of both metrics; the matrix in the receipt *illustrates*, the physics *derives*); (2) the receipt's Wick line **corrected** — the metric is bilinear, so the pullback is $W^\top\eta W$ not $W^\dagger\eta W$ (the conjugate transpose let $i,-i$ cancel and printed `False` against the SO(6) claim); fixed to `W.T`, now returns η_E. The bounded result is **cold-cleared**; the universal stays unclaimed.

---

## 6. Source pointers (verify before building)

- **The full working trail (with every catch inline):** `retired/colour_frontier_dS6.md` *(retired — kept as the record; path repointed r1626)* — the chronological notebook this distills. The Move-A correction, the type-check, the C–M retraction, the genericity check, and the thesis grounding are all there with their reflexive lessons.
- **The 2012 thesis (maximal symmetry, the ellipse):** `resources/PhD_thesis/thesischap3.tex` §"A Reduction of Prior Theoretics"; `thesischap4.tex` §GPSMRF; figures `resources/PhD_thesis/*.png` (esp. `max_symm_space_graphed`, `fund_ellipse`, `Lorentz_sphere`). Re-derive, don't take on the thesis's word (it was, this session).
- **The corpus geometry:** `corpus/algebroid_paper.tex` (the $[\mathfrak{m},\mathfrak{m}]\to\mathfrak{m}$ leak; the "we assert neither the continuous $\mathfrak{su}(3)$ nor the rise" line); `corpus/SdS-slicing-curve_v2.tex` (the sky angle, the fundamental ellipse §sec:ellipse, the involutions §sec:throat-angle, the two-descriptions/vantage-groupoid framing); `corpus/CR_framework.tex` ($\sigma,\tau$ as derived coordinate-independent groupoid morphisms; **P7 — the file was named `framework_paper.tex` when this was written; repointed r1626**); `scripts/adm3.py` (path repointed r1626) (the downstream permutation-rep — a *shadow* of the geometric operations, not their source).
- **The consolidated state:** `retired/THE_VISION.md` §4 (the colour frontier as horizon, held as moldable hypothesis) — **retired since this was written; the discipline it carried survives in `VISION_FIELD_GUIDE.md`, per `INDEX.md`** (repointed r1626); `THE_PLAN.md` Move 13.
- **The settled mathematics to re-check against the literature:** $\mathfrak{su}(3)$'s minimal real rep (6); minimal $SU(3)$-homogeneous spaces ($CP^2$, $S^5$, flag); the Atiyah–Hirzebruch vanishing theorem and Lawson–Yau/Lichnerowicz; that Coleman–Mandula is an S-matrix (not gauge) theorem.

---

*The platter, set and then sharpened by the relay. The bounded result is real and earned; the gem ($A_2$, genuine) is real; the frontier is open, decidable, and now sharply posed. Carry the not claimed. Suspect the model, go to the source, compute rather than defer — and remember the adjective-traps that have each cost a catch: connection ≈ gauge (c18, caught by c17); "internal-vs-spacetime" ≈ Coleman–Mandula (c18, caught by c17); and $\sigma$ ≈ Wick-rotation ≈ the-bridge (c19, in this very platter's first draft, caught by c17 on relay). The one thing not to hand a fresh head as a "hard fact" is the $\sigma$-bridge — it is the question (test 1), not a constraint. That a fourth instance surfaced inside the distillation itself, and the different node caught it before the fresh head inherited a baked-in answer, is the interference engine working exactly as intended.*
