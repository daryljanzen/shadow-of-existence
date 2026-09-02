# P3 rewrite — from scratch (working notes)

*Working doc opened ahead of the rewrite, per Daryl: the P3 rewrite is coming, so jot directly here as the goldmining read surfaces the pieces. The ordering Daryl set [0500–0504]: derivation first; P3 is "p2 done right"'s setup, so it gets locked before the P2 major revision and P4 minor revision. Fresh-head full read of current P3 + this plan before writing. Not canonical; refined as the read proceeds.*

## The target (one-line)
One slicing curve, read two ways — **w=0 Schwarzschild, w=180 de Sitter** — over the fixed-α dS₅ substrate; the conjugate circle a real structure; r a **signed** areal coordinate along the curve (hyperbolic arm + conjugate circle).

## Conventions to establish (the disambiguated minimal set) — settled lexicon as of [c24 0274–0294]
- **Equator** — the fixed, slicing-independent locus, radius α (P3 §195/§204). "Throat" and "waist" retired as redundant (both = equator + connotation). [caveat: "throat" ties to wormhole literature]
- **Seam** — the slicing-*dependent* turning locus (P3 §466): equatorial seam (cosmological slicing) vs front/back seams (Schwarzschild slicing's horizons).
- **Slicing hinge** — the line X1=2α (Observer 2) the slicing plane swings about like a door; vs **sweep pivot** — the revolution centre of the *sweep* (P3's "pivot": r=0 Schwarzschild / manifold axis de Sitter). Kept rigidly distinct (this was the key collision fixed).
- **w — swing angle** of the slicing plane about the hinge. **w=0 Schwarzschild, w=180 de Sitter, w=30 Nariai (the tangent).** ⚠ **FLAG (do not lock):** Daryl asserts w=0=Schwarzschild with M≠0 (M depends on α); P3's current text says r₀=0 = de Sitter M=0 (§272/§290/§630). Either swing-w ≠ gnomonic-w (where r₀=(2/√3)sin w → w=0 gives r₀=0=de Sitter), or P3 has an error the convention must FIX. **The rewrite resolves this; the doc's convention is the standard, the paper gets corrected to it — do NOT litigate the convention against the paper [0296].**
- **θ** — gnomonic sky angle (Observer 2); Nariai θ=60° on the circle, bridged to swing/gnomonic w=30° by the √3 gnomonic relation.
- **r0** — a cubic horizon radius, gauge-free (= (2/√3)sin w in the gnomonic reading); NOT a circle size.
- **σ** — the character flip A↔B (r=0 relocates B→A when generating Schwarzschild vs de Sitter).
- **r** — signed areal radius, parametric (arc-length) along the curve, real down to r=0; freely exceeds α (it's distance traveled, not a coordinate).

## What to KILL / fix
- **α→∞ framing (Q0, top priority)** — "ruining the whole corpus" [0312]; α is the FIXED invariant √(3/Λ); making the hole infinite leaves nothing to slice. **The general tell [0317]:** any named geometry reached through a *degeneracy* (M=0 Schwarzschild, α→∞ Schwarzschild, "de Sitter = the value r₀=0") instead of through a *reading at fixed α* — rewrite each to one-curve / fixed-α / two-readings. **"Massless M=0 Schwarzschild" is incoherent** [0314] — Schwarzschild is M≠0 with the cosmological term off; M=0 with it on is de Sitter, so P3 relabeled de Sitter. Schwarzschild = swing-0 reading at fixed α, M set by α.
- **r(l) as primary variable** — l (proper-length slicing parameter) blows up at Nariai, making a regular point look singular → demote; keep ONLY as a physics remark (proper length diverges logarithmically at Nariai — meaningful for cosmology) [0478–0492].
- Deprecated/redundant terminology (waist/throat collapsing into equator; the seam-vs-equator conflation) — disambiguate.
- **Φ retired [c24 0474–0477]** — Φ (r=(2/√3)cos Φ) is just r through arccos, carries nothing r0 doesn't, and its amplitude-2/√3 circle is not a real circle of the geometry (cosmetic). Re-home its root-angle facts on r0.
- **The three real parameters θ/w/r0 each flatten a different structure** (θ blind to the swing family; w the family parameter; r0 the areal value) — so the rewrite uses all three with their roles tagged ([E-PARAM]), never makes one do everything (the source of much confusion).

## Derivation spine (fill from the read)
- **σ and r0 pinned [c24 0332–0344]:** σ = the A↔B character-flip involution (which root is cosmological vs BH horizon), fixed point at Nariai; geometry stays put, only the reading swaps. r0 = the areal-radius VALUE at the designated seam (bead parameter along the slicing curve), NOT "which horizon"; r₀=0 = de Sitter (not Schwarzschild — Schwarzschild puts the seam at MAX distance from r=0). One slicing curve, two readings: w=0 curve = Schwarzschild at swing 0, de Sitter at swing 180.
- **Signed r justified at source [c24 0164–0167, from Daryl's thesis]:** r defined by g_θθ≡r², area 4πr² — "does not even require r to be positive." So r is the signed Schwarzschild-like coordinate; the sign marks which side (not negative area). The r<0 branch is real (horizonless, asymptotically flat r→−∞); Nariai's third root −2α/√3 lives there. The **fundamental ellipse** (thesis) carries the negative-root horizon on its major axis; going around it is the +r→−r passage. At Nariai r0=1/√3 a vertical slice runs r from −∞→+∞.
- **⚠ THE TWO-FUNCTIONS DISSONANCE to resolve in the rewrite [c24 0168–0169]:** the *flat* matter areal radius (§498: r=sinh^{2/3}, ṙ²=r²+1/r, no curvature, seam an ordinary ä=0 inflection) vs the *closed-SdS signed r* (thesis static-form, ṙ²=r²+2M/r−1, k=+1 curvature, seam the merged-horizon asymptote, r signed −∞→+∞). Different cosmologies. The flat reading smuggles back the rejected z=0.63=transition identification; the picture Daryl drives toward is the closed/signed one. **The rewrite must pick the closed-SdS signed-r reading and state why the flat §498 form is not the cosmological model (or how they relate).** This is likely the crux the whole rewrite has to settle.
- *(more to be filled: the bead construction [0438–0448], r(τ̃) on E=1 [0450], the signed-r embedding picture [0160–0194])*
- **The core reconciliation P3 must do [c24 0201–0221]:** three functional forms for r along the one slicing curve are unreconciled across the corpus — P2 cos (cycloid, r=M(1+cos z)), P3 sin (proper distance, r=α sin(l/α)), and the arc-length-linear-in-rim-angle the conjugate lap wants (1/3–2/3 split = root ratio 1:2). They put r=0 and the third root in different places. Linchpin derivation: integrate dr/dl=√|f|, f=(r−1/√3)²(r+2/√3), explicitly; pick ONE clean variable (NOT l — diverges at Nariai).
- **State the Schwarzschild↔de Sitter pivot/involution clearly [c24 0210–0212]:** r=0 as the Schwarzschild back-of-circle horizon AND off-axis sweep point (infinite curvature, P4 §48), the pivot trading off-axis for on-axis sweep, the BH horizon jumping front↔back. Daryl's "holy shit": the papers carry the diagnostic but do NOT state this core structure abundantly clearly — the rewrite should.

## Dependencies / propagation
- **Canonical plan artifact:** `P2_P3_OVERHAUL_PLAN.md` (c24, persisted r473; internally stamped r472) — the self-knowing rewrite spine, preserved/expunged lists, the α→∞ fix with Daryl's asymptotic-flatness argument, P2 absorption. (P4 alignment was c24's later in-session work that did not persist; the P4 findings are in C24_GOLDMINE_NOTES §4 — a rewrite do-next: fold them into the plan + rename P2_P3_P4.)
- **Rewrite SEQUENCE [c24 0502]: derivation first → P2 MAJOR revision → P4 MINOR revision → P3.** P3 is "setting up for *P2 done right*." (Note: lock the derivation and P2/P4 before P3 prose.)
- **P2 finding [0484–0486]:** P2 is a self-contained **pure-M construction** (r(z)=M(1+cos z), no Λ/α/∞); its asymptotically-flat exteriors are the cosh continuation z→±iρ (r→∞), NOT an α→∞ limit. The cosh arms ARE literally asymptotically flat (null rulings off the equator 90° either side, coming together Euclidean/parallel at ∞). **The α→∞ was P3's broken bridge to P2 — expunge it; P2 doesn't need it.**
- **P4 finding [0494–0497]:** already aligned (σ = root-exchange involution w↔π/3−w fixed at Nariai; sky angle); new P3 strengthens it (σ's geometric face, overcritical two-sheet/lifted-circle). Inherits Q0 (α→∞, line 316) + deprecated "two limits"/r(l) framing — same fix; real results (groupoid, D₃, dimensional collapse, S₃/D₆, sweep-pivot) untouched. def:vantage = start point for Q4 (charge).
- **Then full propagation** of this unified document/framework through the ENTIRE corpus (Daryl's vision).
- Check vs P2–P6 internal consistency as the convention settles.

## The hard problem the rewrite faces
- **⚠ [c24 0503 — DO NOT ACCEPT] c24 claimed the Schwarzschild cycloid r=M(1+cos z) is "not recoverable as a fixed-α reading"** — but this came right after the [0498] compaction, so it is a candidate **straw man / manufactured wall** (Daryl: "could very well be a straw man… I do not want you to just accept that result"). **Held not claimed; NOT a finding.** The genuine open question: does the swing-0 reading at fixed α yield the Schwarzschild structure without α→∞? **Must be actually worked through in the rewrite's derivation-first step** — not inherited from c24's post-compaction claim. Likely shape of the resolution (c24's own flag): the **distinction between the global slicing-curve object and P2's local M-circle**. Fold in Daryl's hard-pushed swing-0 explanation [0504] (swing 0 → both Schwarzschild AND de Sitter) at weight.
- **✓ Daryl's resolution [c24 0507, 0553] (his taxonomy — fold into the rewrite):** **pivot 0 / swing 0 leaves the hole radius untouched; down the hill = Schwarzschild, up the hill = de Sitter — ONE cut, two hill-readings.** The cycloid and the arc are the two hill-readings of the one untouched-radius cut, NOT separate slicing curves. So the cycloid IS a reading (down the hill) — the [0503] "doesn't recover" was the straw man (c24 treated the cycloid as a separate fixed-α slicing curve, found a leftover −M²(1+cos z)²/α² term, wrongly concluded α→∞ needed). The derivation-first step should show the down-hill reading of the pivot-0 cut at fixed α gives the Schwarzschild structure. (c24's leftover-term/α→∞ claims are post-compaction — suspect, do-not-bank.)

## Open forks to resolve from the read
- **✓ RESOLVED as of [c24 0226–0252] (pending the convention-overhaul naming next):** Nariai = the **tangent** slicing plane (definitional — an X-section of a doubly-ruled surface forces tangency), at **gnomonic w=30° = circle θ=60°**, **pivot FIXED at 2α** with the plane rotating about it through w∈[0,π/2]; **r0=(2/√3)sin w** the gauge-free slicing handle (a cubic horizon radius, not a circle size). Corrected triangle: pivot 2α, 60°-at-center/30°-at-pivot, tangent √3α. SdS family: undercritical w 0→30° (two real positive roots converging), Nariai w=30° (the X, double root α/√3), overcritical w 30→90° (positive roots complex, 2-sheet section). Daryl's "45/90" was the null-cone slope, self-corrected. **WATCH: the convention overhaul [0254–0344] introduces hinge/swing/σ naming — check this gnomonic-w convention survives it or gets renamed.**
- **⚠ still open:** the overcritical low-point / conjugacy-circle size law ("circles α→2α" vs constant-X0 slice √(α²+X0²) unbounded) [0233, 0241].
- Whether r(l)'s proper-length divergence remark belongs in P3 or elsewhere.

================================================================================
## P3 SKELETON (r476) — the self-knowing structure, [A]-[K] spine, Q1-Q5 baked in. Stated for reversal.
The order is the overhaul-plan spine (sec1); each preserved proposition (plan sec2) re-homes into it;
Q0 excision points marked [Q0]; resolved questions marked [Q1]..[Q5]. Prose drafted section-by-section
from this. l never the primary parameter (Q2). Schwarzschild/de Sitter never via a degeneracy (Q0).

§1  SUBSTRATE & CUT. The dS substrate; the work-surface hyperboloid -X0^2+X1^2+X2^2=alpha^2; the
    equator/throat radius alpha; the slicing hinge at 2alpha; the door swings by w; the slicing curve =
    the section the plane cuts. [Q4: the hinge is the family's SWING-PIVOT (the charting-side chart-centre
    the sky angle pivots about), not the manifold observer.] NO l yet.

§2  THE THREE PARAMETERS, DECLARED ([E-PARAM]). theta (lap position) / w (swing = sky angle, the family) /
    r0 (designated-seam areal value). What each is faithful to AND what each FLATTENS: theta flattens the
    family; w flattens the sigma involution (w<->pi/3-w); r0 flattens the sin fold (caps at 2/sqrt3) and
    lap position. Use all three; none carries what it flattened. THE organizing fact, up front -- what
    current P3 never says.

§3  HORIZON STRUCTURE, IN r0. The honest cubic r^3 - r0^3 - (r-r0)=0; the ellipse r^2 + r r0 + r0^2 = 1;
    three regimes by r0^2 vs 4/3 (under / Nariai / over). PRESERVED: prop:factor (factorisation);
    prop:involution (root-exchange, closed form, Nariai fixed point); prop:locus (line + 45deg tilted
    ellipse, major axis = backward-radial root). Defined HERE by r0 -- not by l, not by "two limits."

§4  THE FAMILY, IN w. Schwarzschild (0) / Nariai (30) / de Sitter (180); sigma involution w<->pi/3-w,
    Nariai its fixed point. The projection: prop:gnomonic (gnomonic forced); the sky angle; prop:triple
    (2M=(2/3sqrt3)sin 3w); prop:conjugacy (the chi map, the two involutions one). MASS: 2M=alpha((r0/alpha)
    -(r0/alpha)^3), alpha the invariant, M the slicing factor. Overcritical = continuation past the Nariai
    crest (sec:overcritical, 3w=pi/2+i beta); [Q5] the size law caps at sqrt3 alpha (vertex) / 2 alpha
    (conjugate circle) at swing 90. [Q0 EXCISION: Schwarzschild & de Sitter are READINGS AT FIXED alpha
    (swing 0 / swing 180), M set by alpha, NEVER via alpha->infty or M=0 degeneracy. [Q1] frame: the seam
    is one object in two synchronizations (alpha background / alpha/sqrt3 matter); the four sqrt3-ish
    factors are one sqrt3 in geometric + projective roles.]

§5  THE SEAM, THE LAP & CONJUGATION, IN theta. The equatorial seam; prop:flip (automatic signature flip)
    -- [Q3] it is the 2D slicing-SURFACE metric that flips; the spacetime/substrate is Lorentzian
    throughout. The bead; the conjugate circle; r=0 the real<->complex BRANCH POINT (not the seam); signed
    areal r = single analytic sinh^{2/3}, constant +120deg conjugate branch, no piecewise sign; both
    triple-seam values (+alpha/sqrt3 real, enter; -2alpha/sqrt3 on the 120deg ray, lap closes). [Q3] the
    conjugate region is CONTINUATION WITHIN THE ONE LORENTZIAN SUBSTRATE (the real backward-radial r<0
    branch), not a Euclidean excursion; the complex r is the sinh^{2/3} representation.

§6  CURVATURE & THE SWEEP (the interpretive payoff). prop:curvature K_G = 1/alpha^2 - M/r^3: finite
    through the static region, invisible to horizons, sign-change once at r_*=(M alpha^2)^{1/3}. The
    -M/r^3 = the forced-pivot signature. The sweep account (preserved): de Sitter = interior sweep about
    the manifold axis; Schwarzschild = exterior sweep forced off-axis onto r=0 -- the horizon-vs-
    singularity asymmetry is the geometric shadow of that forced pivot, not a feature of the manifold.

§7  THE CURVE IS INTRINSIC; THE GROUPOID. prop:rigidity (moving the charting observer changes the image,
    not the geometry); prop:morphism-generation (the discrete groupoid: within-geometry generators ->
    D_3 = S_3; same-alpha between-members = deck group of the Nariai-branched cover; mass-reflection ->
    D_6 = Aut(A_2); between-alpha = homothety). The de Sitter <-> Schwarzschild correspondence = ONE curve
    swept from two vantages (interior/exterior), carried by the seam's signature flip; structurally
    invertible -> membership in de Sitter retained.

§(remark) PROPER DISTANCE l. [Q2] NOT a parameter -- only a physics remark: the proper separation of the
    two positive horizons DIVERGES (log) at Nariai = merging horizons infinitely far apart in proper
    length (CORRECT physics, K_G finite there), not a defect, not Nariai-is-singular. The coordinate l is
    expunged from the primary ordering; it remains a derived local quantity (dl = dr/sqrt|f|) in the
    surface metric, and the K_G result is already written in r.

DEFERRED INTO THE DRAFT: the Q4 gnomonic full-family check folds into §1/§4 (the projection); P2's light
revision (name it the swing-0 special case + also-de-Sitter reading) follows the P3 skeleton; then P4
minor, then the cold read by a fresh node (wall intact).
