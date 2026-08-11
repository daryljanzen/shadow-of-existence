---
name: phase8-diff-audit
description: The audit of every change made r1838→r1873 — Phase 8's four field bakes — against the base at r1838. Opened r1874 (Daryl-directed) after the bakes were found to have been run without holding the substrate/slicing apparatus. Each claim carries the specific question the framework puts to it; nothing is kept or dropped until it is answered at source.
---

# THE PHASE 8 DIFF AUDIT — r1838 → r1873

*Opened r1874, Daryl-directed. **The four field bakes of Phase 8 — quadric, conformal, optics, complex
analysis — were run without holding the substrate and slicing apparatus.** The work was done by grepping
fragments rather than reading the construction, and at least three claims are now known to be artefacts of that.
***But the work is genuinely rich and much of it is right, so the operation is not a revert: it is a filtered
revert.*** Every change is audited against the base under the properly-held framework; what survives is kept with
its reason, what fails is dropped with its reason, and **the corrections themselves may carry new results.**

**The base: `r1838`.** *The quadric ledger's pre-bake baseline survey is present and is part of the base — it was
careful work and no probe had landed. **Checker 107. `Q1` lands at r1839.*** Bundle at `/root/cr_r1838.tar.gz`,
extracted to `/home/claude/base_r1838`.

---

## ⛭ 1 · THE APPARATUS THE BAKES DID NOT HOLD — read at source r1874, and this is the audit's measuring stick

***The construction has a SINGLE MOVING PART: one slicing plane — a door — swinging about one hinge.*** *P3
§sec:ontology.* **The family of cuts is the single arc of that swing.**

**⌗ THE THREE PROJECTIONS OF THE ONE SWING, and what each is blind to** *(P3 §sec:params — the section the
bakes never read)*:
| | | blind to |
|---|---|---|
| **$w$** the **sky angle** | on the charting observer's celestial sphere | ***folds $\sigma$ from view as a mere reflection***; collapses the three-fold into a single $\sin 3w$ |
| **$u$** the **throat angle** | on the throat circle *in the manifold*, $\sin u=\tfrac{2}{\sqrt3}\sin w$ | which member is in play; **carries BOTH harmonics** |
| **$r_0$** the **signed areal radius** | the value the cut sits at — *"not an angle and not the family's dial"* | where on the conjugate lap one stands |

> ***"NEVER READ ONE WINDOW WITHOUT ITS COUPLED COMPLEMENT — taking that piece for the whole is the
> characteristic error the coupling guards against."***

**⌗ THREE DISTINCT POSITIONS, which the bakes blurred:**
*• **the hinge**, transverse distance $2\alpha$ — the swing pivot. ***An OUTPUT, not a stipulation***: the one
circle the hole determines without further choice is the circle on its own edge through its own centre, and
**that circle ends at $2\alpha$**.
• **the manifold observer** — physical position in the exterior, ***fixes $r_0$ as an intrinsic feature of the
slicing curve***.
• **the charting observer** — celestial-sphere image at $r_{\rm obs}=\sqrt7/2$, which ***merely displays that
offset. Moving the charting observer changes the image, never $r_0$.****

**⌗ THE DIAL IS BOUNDED.** *$2M=\tfrac{2}{3\sqrt3}\sin 3w$, so $|2M|\le\tfrac{2}{3\sqrt3}$ on the real dial:
**"the swing never leaves the undercritical interior except to touch its Nariai boundary; the strict overcritical
regime is reached by no real swing, but only by the imaginary continuation past a crest."***

**⌗ THE BRANCH POINT IS THE NARIAI CREST, IN THE SKY ANGLE.** *$|\sin 3w|>1$ is impossible for real $w$; writing
$3w=\pi/2+i\beta$ gives $\sin 3w=\cosh\beta>1$. ***"The Nariai crest $3w=\pi/2$ is the branch point."*** And
$\sigma$ at $w=\pi/6+i\beta/3$ acts as **complex conjugation** — exchanging the conjugate pair, fixing the real
backward-radial root.*

**⌗ AND THE SEAM CONTINUATION AND THE OVERCRITICAL CONTINUATION ARE ONE FACT:** *"$\sin\to\cosh$ at the branch point,
loss of real intersection here — **one analytic fact in two guises**."*

**⌗ TWO CUBICS, and they separate:** *$H=r^3-\alpha^2r+2M\alpha^2$ (**horizons**, where the slicing turns) and
$T=r^3+2M\alpha^2$ (**the turnaround**, where the $E{=}1$ congruence turns). $H-T=-\alpha^2r$, so they meet at
$r=0$ and nowhere else. **$\operatorname{disc}H$ CAN vanish — at Nariai, the double root. $\operatorname{disc}T=-108M^2\alpha^4$ is
strictly negative for every $M\ne0$ and NEVER vanishes**: the turnaround triple is equilateral always.*

**⌗ AND A SEAM IS A TURNING POINT OF THE SLICING CURVE** — *"where it runs tangent to the throat circle."* **Not
a radius.** *P3's own worked case, gauge $\alpha=1$: "the curve rises from $r=0$ to **the seam at $r=1$**."*

---

## ⛭ 2 · THE REGISTER — 19 claims, each with the question it must answer

**Verdicts: `KEEP` · `KEEP-REWORDED` · `DROP` · `OPEN`.** *Nothing is marked until answered at source.*

| # | claim | landed in | ***the question the apparatus puts to it*** | verdict |
|---|---|---|---|---|
| **Q1** | `quadric_polarity` | p0 | ***KEEP — it strengthens a BOUND, and its own masthead is honest that it returns nothing else.*** *⊢58 was stated for classical circle geometry **in the projection**. Q1 shows the polarity of the **embedding quadric** returns, at every named point, what `eq:powerisheight` already gives — **because that identity IS the hyperboloid's equation**, and the hinges lie on the quadric, so each polar is just the tangent hyperplane there.* ***That the bound is not an artefact of working in the projection is a real strengthening, and the paper says exactly that*** | ***KEEP*** |
| **Q3** | `cayley_klein` | p0 | ***KEEP, and it is a joint.*** *The substrate's geodesic separation **is** the Cayley–Klein log-cross-ratio against the absolute $\eta(X,X)=0$, with the CK constant equal to $\alpha$ exactly — $\tau=(\alpha/2)|\log\mathrm{CR}|$ timelike, verified at every rapidity and every $\alpha$.* ***And it converts "one scale, no free dimensionless constants" from the outcome of an exhaustive audit into the classical statement about a geometry of this kind*** — **the one `R2` promotion the whole of Phase 8 produced, and it survives** | ***KEEP*** |
| **Q4** | `equianharmonic_vantages` | P5 `rem:equianharmonic` | ***THE WITHDRAWAL STANDS; ITS REASON DID NOT AND IS REPLACED.*** *It cited `X1`'s genus argument. **The correct reason needs no genus at all:** the $j{=}0$ curve is the **double cover of the line branched at the four points**; §sec:deck's is **three-sheeted, over the $2M$-plane, branched at the two Nariai values, deck $S_3$** — ***a different degree over a different base with a different branch set, so a $j$ computed from the four points says nothing about it.*** **The cross-ratio result itself — equianharmonic, $S_3$-invariant — is untouched** | ***KEEP-REWORDED*** |
| **Q5** | `nariai_on_the_locus` | P3 `cor:nariai-locus` | ***KEEP — and its own remark is the reason.*** *P3 states plainly that the corollary **"adds no new value; it locates one already fixed three ways"** — algebraically the double root and $\sigma$'s fixed point, incidence-geometrically the **singular point of the reducible cubic**, metrically the **end of the conic's minor axis**.* ***The value is the closing sentence, which is a joint: "that the degenerate configuration of the family is the singular point of the family's own locus is the geometric content the algebraic statement carries without displaying."*** **Self-scoped, and it earns its place on that sentence** | ***KEEP*** |
| **Q6** | *was:* `polar_slices` → ***now `Q6r_polar_is_the_background`*** | p0 | ***★ CONFIRMATION ① CLOSED `A18`.*** *The r1851 run found the polar of a substrate point cuts a totally geodesic $\mathrm{dS}_4$ and **held the identification open** — "whether that $\mathrm{dS}_4$ is the background rung." **Reading §0's ladder as the confirmation demands settles it:** the slice's isometry is $\mathrm{SO}(4,1)$, a **sweep-subgroup** of $\mathrm{SO}(5,1)$, which is §0's own criterion for a four-geometry being a **cut** — and being maximally symmetric it **is** the background.* ***So polarity is how the background sits in the substrate: one background per substrate point, none privileged, the point a slice is polar to being what selects it.*** **The gap was real — the ladder stated in p0, the embedding stated in no paper** | ***KEEP — AND IT CLOSES A18*** |
| **C1** | `conformal_vs_isometric` | P5 | ***KEEP — genuinely additive.*** *P5's base already states the homothety $r_0\mapsto\lambda r_0$, $\alpha\mapsto\lambda\alpha$ and its invariance. **C1 says why it acts BETWEEN representations rather than within one:** a linear map preserves the absolute exactly when it is $\mathrm{O}(5,1)$ composed with a **dilation**, and the homothety is that dilation.* ***So the isometry group of one representation is $\mathrm{O}(5,1)$ and the group preserving the causal structure alone is $\mathrm{O}(5,1)\times\mathbb{R}^+$ — the causal structure fixes the geometry UP TO the scale, and the scale is the one thing it does not fix.*** **A joint, and the other half of `Q3`** | ***KEEP*** |
| **C3** | `inversion_extends` | p0 | ***KEEP — a bounded extension, honestly scoped.*** *Inversion in the throat extends off the equatorial plane as the algebraic identity $\eta(P,P^{*})=\alpha^2$ for $P^{*}=\alpha^2P/\eta(P,P)$ — **elementary, and holding at either signature of $\eta(P,P)$**, an involution whose fixed set is the whole substrate of which the throat is the equatorial section.* **With `Q1` it completes the statement that ⊢58's bound governs all three of p0's routes and is not a projection artefact** | ***KEEP*** |
| **C4** | `gnomonic_not_conformal` | P3 `prop:gnomonic` | ***KEEP — one sentence, and it names the character of the whole construction.*** *`prop:gnomonic`'s base proof argues from straight-line-to-straight-line and excludes the **orthographic**. C4 adds that **the same criterion excludes the STEREOGRAPHIC**, and names which criterion that is: the stereographic is **the conformal projection**, preserving angles, carrying great circles to circles rather than lines.* ***"The chart this construction requires preserves straightness at the cost of angles, not angles at the cost of straightness — a projective demand rather than a conformal one, which is the character of the construction throughout."*** **That last clause is the joint, and it is what handed to the optics bake** | ***KEEP*** |
| **O1** | `photon_sphere_nariai` | P7, P3 `fig:ellipse` | ***KEEP. Confirmations pass.*** *The base caption already drew **"the photon sphere $r=3M$ across the family"** — but **stated, not derived**, in an SdS caption where a reader would reasonably take it from Schwarzschild. **Re-derived on the corpus's own $f$: $\mathrm{d}(f/r^2)/\mathrm{d}r=-2(r-3M)/r^4$, zero at $r=3M$, and $\alpha$ ABSENT — Λ-independent.*** At $M=\alpha/3\sqrt3$ that is $\alpha/\sqrt3$, where $f=f'=0$: **verified, the photon sphere sits ON the merged double root.*** **And it names a joint** — P7's tangency trichotomy and the circular-null-orbit condition are **one condition reached twice**, since a null direction tangent to a sphere of constant $r$ IS a circular null orbit. *The masthead's record of the imported-formula trap is part of the value* | ***KEEP*** |
| **O2** | `sightline_null_on_lift` | p0 | ***KEEP — it is a PRECISION CORRECTION to p0's own wording, not a new result, and it says so.*** *p0 had "sightlines that touch the throat are light rays." **The equatorial plane carries a positive-definite restriction of $\eta$, so no displacement WITHIN the plane is null**; what is null is the displacement on the substrate, from the vantage lifted to $X_0=\sqrt{\mathrm{pow}}$.* **"The planar figure is the shadow of that null line"** — *which is p0's own shadow reading applied to its own figure, and `prop:twoalpha` (v) is the same fact from P3's side* | ***KEEP*** |
| **O3** | `charting_distance` | P3 §projection | ***⛔ MOSTLY DROPPED. It restated `prop:triple`'s OWN PROOF, one paragraph above the proposition.*** *The proof derives $\varrho-\tfrac34\varrho^3=0$ with unique positive root $2/\sqrt3$; O3 derived $R/3=R^3/4$ — **the same equation.** And it **replaced a more economical base clause** that already said it.* ***Reduced to one clause pointing at `prop:triple`***, keeping only what the base did not have: that the residual harmonic **returns** at every other value, so $\sqrt7/2$ is where the structure is legible rather than where an observer stands. **And it read the $w$-window alone, which §sec:params warns against** | ***REDUCED*** |
| **O4** | `deflection_perspectival` | P7 | ***KEEP. Verified on $f$, and independent of the suspect chain.*** *$(du/d\varphi)^2=1/b^2+1/\alpha^2-u^2+2Mu^3$ — **$\alpha$ enters ONLY as an additive constant, with no $u$ dependence** — so differentiating gives $d^2u/d\varphi^2=u(3Mu-1)$, **the Schwarzschild orbit equation, $\alpha$ absent.** And the measured angle carries the local $\sqrt f$, which does carry $\alpha$.* ***The Rindler–Ishak point, and the corpus carried it ×0.*** **It is P7's "empirical content untouched" at its sharpest worked instance, and it settles a live dispute by the perspectival split** | ***KEEP*** |
| **O5** | `kappa_and_lyapunov` | P7 | ***KEEP. Verified: at Nariai $\kappa=f'(r_h)/2=0$ and $\lambda^2=f[2f-r^2f'']/(2r^2)=0$, by different causes*** — *$\kappa$ from the double root $f'=0$, $\lambda$ from the orbit lying on $f=0$.* **And P7's guard held during the run: $\alpha/\sqrt3$ is the merged horizon and NEITHER crossing; the probe was heading for "the photon sphere is the seam" and the guard stopped it** | ***KEEP*** |
| **O6** | `eikonal_ringdown` | P7 | ***KEEP. The identity is elementary and base-independent: $2f-r^2f''\equiv2$ for every $r$ and every $M$, so $\lambda^2-\Omega_c^2\equiv0$ — verified symbolically.*** *Hence $\omega\simeq\lambda[\ell-i(n+\tfrac12)]$: the quality factor $\ell/(n+\tfrac12)$ is **independent of $M$ and $\alpha$**, and only the scale $\lambda$ varies — zero at the forced member, with $\lambda/\kappa\to1$.* **Marked in P7 as a consistency of the reading, not an independent prediction, which is the right altitude** | ***KEEP*** |
| **X1** | *was:* `cover_genus_zero` → r1874 `X1r_cover_tower` → ***now `X1rr_sky_angle_is_the_galois_closure`*** | P5 `rem:galois-closure` | ***CORRECTED TWICE. The r1867 run compactified P5's PLANE and manufactured a branch point at infinity. The r1874 correction then made two errors of its own, caught r1881 by running confirmation ④ before building on it:*** *(A) it called the dial's deck group $D_6$ — **but a deck group must PRESERVE $2M$, and P3's $D_6$ generators NEGATE it**; (B) it called $w\mapsto w+\pi$ the covering involution — **but that negates $2M$ and $r_0$, so it fixes nothing below**.* ***★ DONE CORRECTLY THE STRUCTURE IS THE GALOIS ONE: the roots need $\sin w$ (degree 3) and then $\cos w=\sqrt{1-\sin^2 w}$ (degree 2), so the splitting field has degree six — AND THAT IS THE DIAL.*** **The sky angle is the Galois closure of the horizon cubic**, its deck transformations exactly P5's own $\tau$ and $\sigma$, which generate $S_3$ = the degree, so the dial is regular where the root cover is not. **The covering involution is $w\mapsto\pi-w$, the Galois involution of that final square root — and $R$ is the extra $\mathbb{Z}_2$ by which $\mathrm{Aut}(A_2)$ EXCEEDS the Galois group** | ***KEEP-REWORDED*** |
| **X2** | *was:* `single_period_not_lattice` → ***now `X2r_single_periodicity`*** | P3 §temporal-threeness | ***THE CLOSED-FORMS RESULT SURVIVES AND IS SHARPENED. The clause that leaned on `X1` is gone; genus is gone with it — GENUS WAS NEVER THE MECHANISM.*** *The mechanism is **single vs double periodicity**: a singly periodic meromorphic function is a rational function of an exponential and so **elementary**; a doubly periodic one is **elliptic** and admits no elementary closed form.* ***AND CONFIRMATION ③ CAUGHT THE REAL TANGLE: the $\tilde\tau$-period belongs to the TURNAROUND cubic $T$, the dial to the HORIZON cubic $H$ — two objects P3 keeps apart (`lem:twoturnings`; $\operatorname{disc}T$ never vanishes, $\operatorname{disc}H$ does).*** *Both are singly periodic, verified — $\sinh^2$ has $i\pi$ and no real period; $\sin3w$ has $2\pi/3$ and no imaginary one.* ***★ AND THE JOINT, better than the original: EACH THREE-NESS IS ONE SINGLY-PERIODIC ELEMENTARY FUNCTION COMPOSED WITH A THREE-FOLD*** — *$\sinh^2$ with the **cube root**, $\sin$ with the **triple angle** — **and that is why $\sinh^{2/3}$, $\sin3w$ and $\sigma$ all close.** The two periods differ in kind as the two three-nesses do: **$2\pi i\alpha/3$ purely imaginary along the clock, $2\pi/3$ purely real along the dial** | ***KEEP-REWORDED*** |
| **X3** | *was:* `seam_schwarz_reflection` → ***now `X3r_reality_lines`*** | P3 `rem:reality-lines` | ***⛔ THE THEOREM HAD NO WORK TO DO. The Schwarz principle EXTENDS a function across a line from one side — and $\sin$ is ENTIRE, so there is no extension problem.*** *What P3 performs is not a continuation across a boundary; it is reading one entire function along a different line of its own domain.* ***★ AND THE RIGHT QUESTION — WHERE IS $\sin$ REAL? — GIVES FOUR OF P3'S PROPERTIES FROM ONE FACT.*** *$\operatorname{Im}\sin(x+iy)=\cos x\sinh y$, so the reality set is a **grid**: the real axis (the spherical piece) and the lines $x=\pi/2+k\pi$ (the Lorentzian one). **The seam is where two of them cross — and the crossings are exactly $\sin$'s CRITICAL POINTS.*** **From that single fact: $r$ maximal · $\mathrm{d}r/\mathrm{d}\theta=0$, the tangency that DEFINES a seam · both pieces real · the $C^1$ join.** *And the signature flip once more, from the lines crossing at **right angles**: the increment is $i\,d\psi$ and a metric is degree two.* **Unused Ahlfors bibitem removed from P3** | ***KEEP-REWORDED*** |
| **X4** | *was:* `singularity_types` → ***now `X4r_no_essential_singularity`*** | P7 §the closure | ***⛔ THE FRAMING WAS FALSE. "The corpus asserts both and never says they are compatible" — P2 `prop:Kretschmann` ALREADY classifies it: a TWELFTH-ORDER POLE in the cycloid parameter, "generated by the chain rule applied to the composition at a non-degenerate critical point of $r(z)$." That IS the compatibility statement, in the corpus's own terms, and the r1870 insertion re-derived it in another variable without knowing.*** ***WHAT SURVIVES IS ONE SENTENCE, and it is load-bearing:*** *no ESSENTIAL singularity is present in the finite plane — $r(z)=M(1+\cos z)$ and $\sinh$ are both entire, so the invariant is meromorphic and the bead's radius carries only algebraic branch points.* **A pole continues to the sphere, a finite-order branch point onto a cover; an essential singularity continues as NEITHER, and by Picard nothing could be said beyond it. That exclusion is what makes "not a barrier" analytic rather than geometric.** *P7 trimmed and now cites P2 for the classification* | ***KEEP-TRIMMED*** |
| **X5** | `monodromy_group` | P5 `rem:monodromy-group` | ***THE THIRD PUNCTURE IS DROPPED*** — it was `X1`'s artefact. ***THE GENERATION CHECK STANDS AND IS ITS OWN RESULT:*** *P5's `prop:deck` says the deck group is $S_3$ **"generated by the monodromies about the branch points"** — and **two transpositions generate $S_3$ only if they DIFFER**, which P5 asserts and never computes. Computed from a common base point: $(0\,2)$ and $(1\,2)$, order six. **Had the same pair collided at both it would have been $\mathbb{Z}_2$ and the claim false — the alternative was real.*** *Remark rewritten; base-point dependence of the labels stated* | ***KEEP-REWORDED*** |

---

## ⛭ 3 · THE NON-CLAIM CHANGES — audited separately

*• **The dS₅ substrate correction (r1842–r1846)** — p0 ×3, P3, P7's seed sentence, P8's masthead. ***This
predates the bad interpretations in kind: it restored a fix Daryl had already made and the corpus had
regressed.*** **Likely KEEP; verify against the five-rung ladder.**
• **The sheet-to-ruling do-not-assert removals (r1840)** — three documents. **Verify P7's `§frontiers` really
closed it.**
• **`scripts/check_bibliography.sh` and the 12 references added (r1862)** — *the six undefined internal
citations and the `JanzenCosmology` typo are **mechanical hygiene, independent of the physics**. Likely KEEP.
**But the Cayley–Klein, equianharmonic and Lyapunov citations ride on Q3, Q4 and O5.***
• **The census pass and the P6 R2 pass (r1865–r1866)** — *the machinery is sound; **its CONTENT rides on the
claims it assessed**, so it re-runs after the register above is settled.*
• **The R-P arc ordering (r1864)** — *independent of the physics. Likely KEEP.*
• **`THE_WISDOM_LEDGER` scraps** — *~20 added. Each rides on its claim and is settled with it. **The
instrument-error scraps (word-bounding, base points, destructive edits) stand regardless.***

---

## ⛭ 3b · THE NON-CLAIM CHANGES — ruled r1879

| change | verdict | why |
|---|---|---|
| **The dS₅ substrate correction** (r1842–r1846) — p0, P3, P7 | ***KEEP*** | *Checked against §0's five-rung ladder. **p0**: "a real four-dimensional manifold" → the five-dimensional $\mathrm{dS}_5=SO(5,1)/SO(4,1)$ **of which $\mathrm{dS}_4$ is the background** ✔ · **P3**: scopes the maximal-symmetry result to the four-dimensional case and names the substrate proper, adding **"this paper works the equatorial section throughout, where the distinction does not bear on the construction"** ✔ · **P7**: the same scoping ✔. **And P3's "the fifth embedding coordinate" → "the ambient timelike coordinate" is the right fix — "fifth" is ambiguous once $\mathrm{dS}_5$ is in play*** |
| **P8's masthead block** (added r1841, pulled r1846) | ***CORRECTLY PULLED*** | *It was my own addition. **And P8 needs no marker: it names its object "pure de~Sitter", which IS rung ②.*** ⛔ **But §0 claimed "Both now say so where they stand," which overstated — corrected at the authority r1879** |
| **The sheet-to-ruling removals** (r1840) | ***KEEP*** | *Verified: P7 at source reads **"is closed in the synthesis… the rulings are borne on $R$'s real axis and the wings on $K$'s… not two candidates for a single assignment but the linear and antilinear faces of the one analytic object,"** and `§frontiers` carries the phrase **zero** times. The do-not-assert was stale in three documents* |
| **`check_bibliography.sh`** + 12 references (r1862) | ***KEEP*** | *Mechanical hygiene, independent of the physics. **All nine classical references still cite live claims** — and the six undefined internal citations and the `JanzenCosmology` typo were real defects the bakes did not create* |
| **The census pass** (r1865) | ***KEEP, RE-RUN*** | ***Five of six enrichments survive unchanged, and the audit added a sixth (`Q6r`→F). No enrichment was lost*** — **the claims that dissolved something were not the claims that failed** |
| **The P6 `R2` pass** (r1866) | ***KEEP, RE-RUN — and the yield DROPPED*** | *`X3`'s move is withdrawn with the claim; `X4`'s too, since P2 already licensed the crossing. ***That leaves `Q3` alone: one promotion in nineteen.*** **The audit lowered the `R2` yield and raised the census yield, which is the honest direction** |
| **The R-P arc ordering** (r1864) | ***KEEP*** | *Independent of the physics; and the handoff rule it states — a handoff outranks the list order — held up: `C4`→optics is the one that produced the soundest block* |
| **`THE_WISDOM_LEDGER` scraps** | ***KEEP, per claim*** | *Each rides on its claim and was settled with it. **The instrument-error scraps stand regardless** — word-bounding, base points, destructive edits, and now the four confirmations* |

---

## ✔ 3c · THE AUDIT IS COMPLETE — r1880

**19 claims · 8 non-claim changes · all ruled at source against the apparatus.**
***13 KEEP · 4 KEEP-REWORDED · 1 KEEP-TRIMMED · 1 REDUCED · 0 dropped outright.***

**⌗ WHAT THE FILTER RETURNED THAT THE BAKES DID NOT HAVE:**
*• ***`Q6r` closes `A18`*** — polarity is how the background sits in the substrate, one per point, none privileged
· • ***`X1r`'s cover tower*** — $\mathrm{Aut}(A_2)=S_3\times\mathbb{Z}_2$ read as two storeys with $R$ the
covering involution · • ***`X2r`'s closed-form mechanism*** — each three-ness one singly-periodic elementary
function composed with a three-fold · • ***`X3r`'s reality-line crossing*** — four seam properties from one fact
· • ***the Galois handoff*** — the deck group **is** the Galois group, and the corpus has named one side.*

**⌗ AND WHAT THE AUDIT ESTABLISHED ABOUT THE PROGRAMME'S OWN INSTRUMENTS:**
*R-M's arc station **Ⓑ was never a gap** — the corpus had it in `prop:triple`'s proof, and the list's "no entry"
was the list's omission. **A station missing from a reach list and present in the papers is a different finding
from a gap, and the audit is what distinguishes them.***

---

## ★★★ 4 · THE DISCIPLINE THIS AUDIT RUNS UNDER — and it is the most valuable thing to come out of the failure

***Daryl, r1874, in his own words — the finding, before any of the machinery below:***

> **"We just discovered a major blind spot — not actually holding the corpus deeply as you explore adjacent
> mathematical and physical structures, because interpretation can draw you to do really wrong things on grep.
> You need to use all the grepping infrastructure you've built more carefully. Confirming everything against
> the corpus ontological map, and the sections of the corpus you are editing, and just all that stuff. Really
> understanding what you are calculating and how it fits into the corpus/programme. We need to use all that
> stuff to find all the things quickly and all that, but we still have to be sure we are confirming what we
> are doing is right and is not deviating from the corpus which is as coherent as we've been able to see and
> do NOT want it drifting in that regard through sloppy analysis."**

### ⛭ 4a · WHAT THE RULE IS NOT

***It is not "grep less."*** *The grepping infrastructure is how the programme moves at the speed it does, and
every sweep, count and cross-reference this session ran is a tool worth keeping.* **The instrument-error scraps —
word-bound every count, strip the citation keys, base your loops at one point — make those tools SHARPER, and
they stand whatever happens to the claims.**

***The rule is: GREP TO FIND, READ TO CONFIRM.*** **The grep locates; it never adjudicates.** *Every failure this
session has the same shape — a grep returned a fragment, the fragment was interpreted, and the interpretation was
acted on without opening the thing it came from.*

### ⛭ 4b · THE POSITIVE MACHINERY — four confirmations, before any edit that lands a claim

*§1·SHADOW's own verdict on warnings applies here: **"the fix cannot be a warning; it must be the explicit
positive machinery."** So this is a sequence, not a caution.*

**① THE ONTOLOGY CONFIRMATION — which rung, and which level?**
*Open `ONTOLOGY_FOUNDATION_INDEX` §0's five-rung table and §1·LEVELS. **Name the rung** the claim's objects sit
on (substrate $\mathrm{dS}_5$ · the $\mathrm{dS}_4$ background · an exact solution · the layer $\mathcal{S}_t$ ·
spacetime $M$) **and the level** any rate or description sits on (L1 the existent's own geometric expansion · L2
the leaf's self-gravitating dynamics · L3 the projection). ***If the claim cannot be stated in those words, it is
not yet understood well enough to land.***

**② THE SECTION CONFIRMATION — read the whole section it lands in, at source.**
*Not the sentence the grep returned; **the section**, from its heading to the next. ***Three of this session's
claims re-derive results whose own proofs sit a paragraph away from where the claim was inserted.*** If the
section already carries the result, the claim is a restatement and says so or does not land.*

**③ THE APPARATUS CONFIRMATION — check it against §1 of this register.**
*The one swing and its three projections; the three distinct positions; the bounded dial; the branch point at the
crest; the two cubics. ***Ask specifically: which window am I reading, and what is that window blind to?***
**P3 names the blindness of each — so the coupled complement is always available and is never optional.**

**④ THE COMPUTATION CONFIRMATION — do I know what I am computing, on what object?**
*The `X1` failure is exactly here: **Riemann–Hurwitz requires a compact base, P5 works on a plane, and the
compactification was performed silently and never questioned.*** ***State the object, its base, its
parametrisation, and what the corpus's own dial is — before running anything.*** **A computation on a base the
construction does not live on will return real theorems about the wrong object.**

### ⛭ 4c · THE STANDING TEST

> ***"Is not deviating from the corpus, which is as coherent as we've been able to see" — and the coherence is
> the asset. A claim that adds a true fact while loosening the coherence is a net loss.***

**Before landing, state in one sentence: *what does this change about how the corpus hangs together?*** *If the
answer is "nothing, it is an addition beside," ask again whether it belongs. **If the answer names a joint —
this explains why THAT works, or this is the same fact as THAT seen from here — that is a claim worth landing,
and `X2`'s closed-forms explanation is the session's example of one.***

### ⛭ 4d · AND THIS DISCIPLINE PASSES THE FILTER REGARDLESS

***Whatever the register above decides about the nineteen claims, §4 is KEEP.*** *It is not a result of the
bakes; it is what the bakes' failure established, and it is the thing that makes the next bake worth running.*
**It belongs in `THE_PLAN`'s per-turn list and in `THE_WISDOM_LEDGER` before any claim is ruled on.**
