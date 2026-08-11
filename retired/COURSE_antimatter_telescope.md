> **⌖ RETIRED r1552.** This was the antimatter-telescope course (r1089) — an exposition. Its physics is `thm:antimatter-progenitor` and P16.
> Kept as record; **do not work from it.**


# The course: the mystery bundle, charge, and the big bang as a telescope

Charted at r440 (c23 with Daryl). One connected frontier, four nodes in dependency order,
each cashing in already-built structure and discovering forcings as it goes. Gate work:
chart and drive, adapt to forcings, do not hand a menu. Nothing below is baked into a corpus
paper yet; nodes 2-4 are the frontier.

Reference figure for all of this: `figures/CR_background_geometry_reference.png` (+ .md) --
the background dS geometry, the two ruling families, the seam ring of radius alpha.

## Node 1 -- the mystery bundle is the PT partner of matter. DONE (grounded).
The double-ruling swap (matter ruling <-> mystery bundle) IS the one Z_2 the corpus built
across r378-r409: substrate orientation parity O(5,1)\SO_0 = A_2 diagram automorphism =
graviton chirality = (on CR's ontology) the mass-reflection 2M->-2M (P11 sec-chirality,
P12 sec-discrete, P4, P3). P (orientation): the swap reverses orientation. T (causal sense):
sec661 selects matter as the future-directed family matching the collapse-horizon generators,
so the mystery bundle has the opposite/past-directed causal sense = the white-hole branch
eta->-eta (circle P2 sec253). So the mystery bundle is the PT image of matter -- orientation-
and causal-sense-reversed, mass-reflected. Antimatter = CPT = PT + C; C is the gap.

## Node 2 -- electrovac extension of the slicing reach + the Q-flip test. RESOLVED (r442) — NOW BAKED CORPUS (range_paper §rem:charge, RN-dS + Kerr-Newman-dS; re-synced c31).
VERIFIED (Reissner-Nordstrom-dS, Einstein-Maxwell check Ein+Lambda g = 2 T^EM exact, all
components): electric charge IS reachable as a cut. Delta = 1 - 2m(r)/r - Lambda r^2/3 with
m(r) = M - Q^2/(2r), so the charge is THE BEND m'(r)=Q^2/2r^2 != 0, sourced by the Maxwell
field A=-(Q/r)dt. So charge is MATTER (the bend, range paper's own thesis), NOT a vacuum/
substrate parameter (the vacuum kernel stays mass/rotation/NUT). The Q-flip test resolves:
the metric sees Q^2 -> C-BLIND; C lives in the Maxwell potential A (linear in Q, A->-A under
Q->-Q), a MATTER-FIELD operation; the geometric mystery-bundle swap carries P and T but
cannot touch Q. ANTIMATTER FACTORISES: PT is geometric and automatic (the mystery bundle =
the reassigned mirror cut); C is independent (the sign of the Maxwell bend's potential). A CPT
antimatter partner = the PT-mirror geometry (mystery bundle) CARRYING a sign-flipped Maxwell
bend. The geometry cannot supply C because it is C-blind by construction. (Rotating case
Kerr-Newman-(A)dS: DONE AND BAKED, range_paper §rem:charge — Delta_r=(r^2+a^2)(1-Lambda r^2/3)
-2Mr+Q^2, Q only via +Q^2, decoupled from a and M, geometry C-blind. NOT pending; it is in the
paper. [re-synced c31: this line formerly read "extends this via the range paper's rotating
corner" — a forward-pointer never closed once it graduated into range_paper.])
DELIVERS TO NODE 4: charge = the bend = a FIELD on the cut -- the same kind of object node 4's
aperture needs. The matter sector is field-on-geometry, exactly the telescope's input.

## Node 3 -- the fermionic C / spinor sector. THE DEEP DESTINATION. [C-STRUCTURE RESOLVED c31; sector-build still the major unbuilt undertaking]
**C-structure question (c31; ⛔ ENLARGED r1089/A3 — the bare "C is FIELD-LEVEL" is a DEAD reason):** the Dirac C is antilinear and **no substrate isometry** — but *not not-geometric*. Only the charge **SIGN** is field-level; C's **kinematic (CPT/FS) face is geometric** — the complex-analytic reality involution `τ̃↔τ̄̃` (`K`), so `C = (Q↦−Q)_field ∘ (R∘K)_geometric` (P13 `sec:closure`, `eq:C-factor`). Read the rest of this node with that correction.
Linear vs antilinear: the substrate's geometric ops (P=spatial parity/lap, gamma^5=hop, X0-reflection)
are LINEAR Clifford elements (psi->M psi); charge conjugation is ANTILINEAR (psi^c = C gamma^0^T psi*,
acts on psi*). The C-matrix exists (C=i gamma^2 gamma^0, C gamma^mu C^-1 = -(gamma^mu)^T verified) but
the OPERATION needs complex conjugation, which acts on the field's charge/complex structure = MATTER,
not geometry. The metric is Q^2-blind (range_paper §rem:charge), so the charge SIGN is field-level for the
SAME reason for Maxwell and Dirac alike -- unifying node 2 (classical) and node 3 (fermionic). But (r1089)
C's KINEMATIC face is geometric (R o K): antimatter = [PT + C's kinematic/FS face] geometric + charge-SIGN
field-level, identically for both. CPT = [geometric linear P,gamma^5,T-skeleton + the antilinear geometric
K-face] x [field-level charge SIGN] -- a full geometric CPT still not auto-yielded (the sign is external),
its kinematic content geometric. Answers the conjugacy conjecture at the closure weight: the substrate does
NOT auto-yield a FULL geometric CPT (the charge SIGN is external, field-level), but its kinematic (PT/FS)
content IS geometric -- PT the linear reflections, and C's kinematic/FS face the antilinear geometric
K=τ̃↔τ̄̃; only the charge sign closes from the field. [Bounded positive result, r1089/A3; supersedes the
earlier "C closes it from the field / no geometric CPT" negative-boundary phrasing.]
**STILL OPEN (unchanged): the actual fermion-sector BUILD** -- a propagating spinor field, the SM content,
the chiral population. That is the major unbuilt undertaking (P14 §109); this session resolved the
C-STRUCTURE (where C lives), not the sector.
The Dirac C, charge conjugation on a spinor field. CR has no fermion sector (P13 sec109:
matter is the classical bend rho=m'/4pi r^2, no spinor, no Dirac operator). The chirality
wall (P13 sec97-145) maps the perimeter: SM chiral fermions are charged under a CONNECTED
gauge group, and geometric chirality lives only in the DISCONNECTED orientation parity
(r400 mechanism), so a geometric-isometry fermion sector is forced vector-like. Building a
genuine fermion sector is the major unbuilt undertaking. Nodes 2 and 4 do not wait on it.

## Node 4 -- the big bang as a telescope. WHAT THE CHAIN IS FOR.
Take the fields and compute the diffraction/acoustic sky with the EVENT-HORIZON/SEAM as the
APERTURE. The throat ring (radius alpha) is the objective; the photon field through it,
fanning up the horn (widest crossing at the throat, closing to parallel up the horn -- the
computed fanning), is the optics; the angular pattern matter reads on its sky is the image.
The CMB acoustic peaks = the diffraction figure of the big-bang aperture, angular scales
keyed to alpha (~lambda/alpha). PREDICTS THE FORM before the computation: an angular power
spectrum whose first scale is fixed by alpha and the field wavelength -- a falsifiable shape,
not a fit. **NO PRIOR NUMBER TO IMPROVE ON (chimera correction, r443).** The "l1~=91" carried
in a compaction summary has NO verified computation behind it -- it is the same species as the
status doc's quarantined chimera (theta*~=1.76, r_s~=251/268: standard photon-baryon plasma +
sound-horizon integral grafted onto CR's radiation-free rate, a model of neither). The
authoritative status (CMB_ACOUSTIC_FRONTIER_STATUS.md r366; CORPUS_MAP r431) is firm: the CR
acoustic scale is UNCOMPUTED; CR has NO radiation-dominated era and NO native standard
sound-horizon mechanism; everything localises to PROBLEM #1 (does a medium/field on the bounded
throat ring, what is it, over what range), with the bounded-throat ontology's structural
expectation being REORGANISED acoustics. Hold DO-NOT-ASSERT on every acoustic number until the
field is built and the scale computed honestly -- never force it toward 220.
node 4 IS the approach to problem #1: a DIFFERENT mechanism from the (blocked) sound-horizon
integral. The integral needs c_s + integration limits (both blocked); aperture DIFFRACTION sets
the scale by lambda/alpha -- geometric, not a sound-travel integral, and the status doc states
the classical scale needs only c and alpha (BOTH IN HAND) with D_M robust. So the diffraction
mechanism may not need the blocked inputs.
GATE (the genuine crux, reframed): node 4 needs a coherent FIELD with phase across the aperture
-- a field that diffracts, with some wavelength lambda. That is problem #1 reframed from "does a
plasma ring at c_s" to "does a coherent field instantiate on the bounded throat and what is its
lambda/mode." Node 2 gave the template (matter = a field on the cut, the Maxwell bend, verified).
The aperture is in hand (exact, alpha-scaled, node 1's surface); the coherent propagating field
is what's owed; the telescope is the two together. Build the field and the diffraction figure
(angular scale lambda/alpha) is the predicted form -- to be computed honestly, do-not-assert.

## Through-line
Identify the mirror bundle (1) -> give the geometry charge so the mirror can be antimatter (2)
-> build the matter that carries charge as a field (3) -> point the fields through the seam and
read the sky the aperture forms (4). The big bang as a bloody telescope, with alpha for an aperture.
