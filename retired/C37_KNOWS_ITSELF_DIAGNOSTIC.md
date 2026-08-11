> **⌖ RETIRED r1552.** This was the Knows-Itself diagnostic (c33, r914). **Landed:** the pass built the ontology map (`KNOWS_ITSELF_MAP_PLAN`, retired r1509).
> Kept as record; **do not work from it.**


# Diagnostic — the Knows-Itself pass (c33), what was done and what was missed
### FINAL — reconstructed from the (now near-complete) c33 transcript + the r913 bundle's meta-docs.

*Transcript coverage: spin-up → r914, via File A + the filler + GAP-B (r901–r906) + GAP-C (r908 title
infra → r914 P10). The one sliver still not in hand — the P5/P6/P7 in-order reads (r908–r911) — is
resolved directly from source (the evolution-map entries and the CORPUS_MAP r908 changelog), so every cell
below is now hard yes/no. My working bundle is r913; P10 (§1n) is r914, described from the transcript.*

## 0. Origin — why the pass exists
Not a mapping exercise by intent. It was the fix for **the single worst source of thrashing**: the node
holds the geometrically-forged cosmological ontology in P7 but forgets it everywhere else it bears, so
derivations veer to FLRW straw-men and "everything explodes." Daryl: *"tracing the curve across r=0 in P3
**is** cosmology… it's everywhere in pieces."* The founding move was **two mega-fixes** (r899→r900), before
the two-pass plan existed: **Fix 1** — the coda digging face (dig ≠ grep); **Fix 2** — the forced cosmology
model baked in as index **§1b** + `[†ONT-COSMO]` across P15/P16/P3/P8 **and the four working derivation docs**
(RATE_HANDOFF, COSMOLOGICAL_THEORY_ROADMAP, CR_COLLAPSE_HELD_PICTURE, OPEN_PROBLEMS_MAP). §1b is the prototype
the whole method was reverse-engineered from. Only then did Daryl generalize it into the two-pass program,
and (at the synthesis moment) steer the node *away* from the step-5 vision ritual toward planning the arc —
the same steer given to this cowork session.

## 1. The three method fixes, and when each landed (the spine of the risk)
The unit of work was **not fixed at the start** — it grew three times, and anything pinned before each fix
missed that step:
1. **Propagation-forward** (r901, before P7): as you pin a forcing, draw the *already-established* forcings
   into each paper as grounding support where a claim rests on them but doesn't invoke them ("draw in what's
   established for support if it's not already properly there").
2. **Step-5, the shared-structural-detail sweep** (r907, from the three-hinge catch): a structure refined in
   one paper must not be left stale elsewhere.
3. **The bibkey-alias map + title standardisation** (r908, from "were the citations done?" + "stop taking
   shortcuts"): grep-based absence claims are unreliable in this corpus (p0 aliases six papers; P14 aliases
   P7). `BIBKEY_ALIAS_MAP.md` + `CANONICAL_TITLES.txt` built; P7's real title repaired in 13 papers; 40
   bibitems standardised and independently verified.

## 2. Status table — every cell now hard (from source)

| Paper | Card | Cherry-pick | In-order whole-read | Front-matter upgrade | Post-fix (step5 + alias)? |
|---|---|---|---|---|---|
| §1b cosmology | ✓ `[†ONT-COSMO]` | r899 (founding) | n/a | n/a | **✗ pre-both-fixes** |
| P1 | §1c `[†ONT-MS]` | r899 | early entry (~r906) | partial | **✗ pre-both-fixes** |
| P4 | §1d `[†ONT-SIM]` | r901 (title-A/simultaneity) | ✓ r908 | ✓✓ (masthead + floor/telescoping) | ✓ (r908) |
| P7 | §1e `[†ONT-CR]` | r901 (exemplary; §185 propagation) | ✓ **r911** (18 findings; 2 dangerous fixed) | ✓✓ | ✓ |
| P3 | §1f `[†ONT-GEOM]` | r902 (the **lap**; → P15 §126 grounded) | ✓ r907 (door/hinge/proper-dist) | ✓✓ | ✓ (r907 = step-5's birth) |
| P6 | §1g `[†ONT-EPI]` | r902 | ✓ **r909** (11 findings) | ✓ | ✓ |
| P12 | §1h `[†ONT-ALG]` | r903 | ✗ (Pass-2 not yet reached) | — | **✗ pre-both-fixes; cherry-pick only** |
| P5 | §1i `[†ONT-DISC]` | r904 | ✓ **r908** (10 findings; propagation + restraint) | ✓ | ✓ |
| p0 | §1j `[†ONT-CORE]` | r905 | ✗ (p17 re-read pending) | — | **✗ pre-both-fixes; cherry-pick only** |
| P2 | §1k `[†ONT-RING]` | — | ✓ r906 (first read) | ✓ (§ring/equator/Sbierski) | **✗ pinned r906, one turn before step-5** |
| P8 | §1l `[†ONT-OPER]` | — | ✓ r912 | ✓ (restraint: ~nothing) | ✓ |
| P9 | §1m `[†ONT-RANGE]` | — | ✓ r913 | ✓ | ✓ |
| P10 | §1n | — | ✓ r914† | ✓✓ (worst ratio; +roadmap) | ✓ |
| P11 | ✗ | — | ✗ | — | remaining queue |
| P13 | ✗ | — | ✗ | — | remaining queue |
| P14 | ✗ | — | ✗ | — | remaining queue |
| P16 | ✗ own card (COSMO consumer only) | — | ✗ | — | remaining queue |

† r914 = c33 chat, one step past my r913 bundle.

## 3. The residual — what was genuinely missed (much smaller than mid-stream feared)
The good news the full transcript delivered: **P4, P3, P5, P6, P7 all got proper post-fix in-order reads**
(r907–r911) with front-matter upgrades, propagation, and restraint. So the "six-card M2 gap" I flagged
earlier is **not** six cards. The real residual is the handful pinned before *both* later fixes and never
re-touched:

**R1 — Five pre-both-fixes cards, never step-5-swept or alias-verified:** **§1b (cosmology), P1, P2** (pinned
"done" but their treatment predates step-5/alias) and **P12, p0** (cherry-pick only). Of these, **P12 and p0
are simply queued** — they get both fixes automatically when Pass 2 reaches them (P12 in arc order, p0 as
p17). The genuinely actionable ones are **§1b, P1, P2**: each should get one step-5 structural-detail sweep
and one alias-resolved outbound check, since neither existed when they were pinned. (P1 and §1b are the
highest-leverage — the taproot and the anti-veer prototype — so a drift there propagates furthest.)

**R2 — `THE_EVOLUTION_MAP.md` P2 heading is stale:** still reads *"→ (no §-card yet)"* though §1k was pinned
r906. One-line fix; and it's itself an instance of the drift the pass exists to catch.

**R3 — Not-yet-pinned (the remaining queue, not misses):** **P11, P13, P14** have no card and no stamp;
**P16** needs its own forcing card (COSMO consumer only); then **p17** (p0 re-read). P14 is the load-bearing
one. Pass 2 resumes at **P11**.

*(Closed, for the record — not residuals: the title-standardisation, r908, Daryl said "Standardise," 40
bibitems rewritten + independently verified zero-mismatch; the two self-introduced title defects the node
made at r905, P5→P14 and P12→P16, both caught and fixed at r908.)*

## 4. Recommended corrective pass (before resuming at P11)
Foundation-first, cheapest→highest-leverage:
1. **R2** — fix the P2 evolution-map heading (trivial).
2. **R1 on §1b, P1, P2** — one step-5 structural-detail sweep + one alias-resolved outbound check each. Small,
   and it certifies the three oldest/most-load-bearing forcings to the same bar as P3–P9.
3. Resume Pass 2 at **P11**; P12 and p0 (as p17) will pick up both fixes naturally when reached.

*Net: the pass is in far better shape than the transcript's frustrations suggested — the method hardened
exactly as it should have, and every card touched *after* r907 meets the full bar. The residual is three old
cards and one stale heading, not a systemic hole.*

## 5. Corrective pass — EXECUTED (this cowork session, against the r913 bundle; bundling held)
**R2 — DONE.** `THE_EVOLUTION_MAP.md` P2 heading `→ (no §-card yet…)` rewritten to `→ index card §1k
[†ONT-RING] (pinned r906…)`.

**R1 — RAN on §1b, P1, P2; all three CLEAN (restraint — no corpus edits warranted):**
- **§1b (cosmology):** structural-number sweep — `ρ_r/ρ_m≈2`, `T_onset≈1.6 eV`, `z_seam≈6850`, the
  `sinh^{2/3}` radiation-free rate, and the finite-curvature-seam framing are stated **consistently** across
  P15, P16, P7, and the working docs (RATE_HANDOFF, CR_COLLAPSE_HELD_PICTURE); the `[†ONT-COSMO]` anti-veer
  stamps are all in place. No drift.
- **P1 (§1c):** the metric-singularity register is consistent corpus-wide; "metrically identical" is
  correctly **retired-as-false** everywhere (SdS §608); the one `removable coordinate singularity` hit
  (janzen_circle §396) is a **fairly-stated "standard reading"** (§4.1), deliberately contrasted with the
  perspectival reading (§4.2) — not a drift. Alias-outbound: p0 cites P1 under `JanzenCausality` at the
  point of use (§153, §817) — grounded.
- **P2 (§1k):** cycloid `r(z)=M(1+cos z)` consistent across P2/P3/P5; `JanzenCircle` citations broad and
  canonical (8 papers), p0 grounded. No drift.

**Bonus catch — DONE.** `BIBKEY_ALIAS_MAP.md`'s "known title drift" section was itself stale (said P6's
sweep "owed") — updated to record the r908 resolution (P6/P7 repaired, 40 bibitems standardised, verified).

**Files changed (2, both meta-docs):** `THE_EVOLUTION_MAP.md`, `BIBKEY_ALIAS_MAP.md`. No corpus `.tex`
touched — the sweeps found nothing to fix. **Bundle held** (c33 is ahead at P14); changes handed off as
surgical diffs for c33 to merge (see `C37FORK_INTEGRATION.md`).

**Remaining (unchanged, for c33/Pass-2):** P12 & p0 pick up both fixes when Pass 2 reaches them (in-order /
p17); P11, P13, P14, P16 still to pin; then Pass 3.
