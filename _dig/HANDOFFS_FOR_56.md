# Node handoffs assembled for 56 to work through and judge

*Collected by the working-fork session (54) at Daryl's request. **These are raw materials.** Every
apply / hold / skip decision is 56's — nothing here is adjudicated by 54. What 54 added is provenance
and a few **verification facts** (base revision, whether a target still exists on the current tree),
gathered so 56 does not have to re-establish them. Judgment is not among them.*

Current tip when assembled: `748a442` (r2435). One edit has been applied (see the last row); all
other findings are preserved unapplied.

## What is in `_dig/`

| path | from | base | what it is | verification facts 54 gathered |
|---|---|---|---|---|
| `findings/` (26 files) | **55**, batch 1 | c54.108 | 11 findings + 4 gate patches + fingerprint baseline + closed forms. Its own `COMMIT_INSTRUCTIONS.md` governs. | Committed as-is (55 said "commit these files"). No gate reads `_dig/`. Two parts deliberately wrong on purpose (F04 zero-file green gate; DRAFT_P09 PART 7 dismantled over-claim) — preserved. |
| `findings_batch2/` (12 files) | **55**, batch 2 | c54.108 | 5 findings (P11–P14 + receipt scope table), additive to batch 1. | Same disposition; drafts, commit-as-is per its `COMMIT_INSTRUCTIONS.md`. |
| `handoffs/17_c17_study_handoff_r2428.md` | **17 (c17)** | r2428 | Verification record: 16 load-bearing computations reconstructed, all held. Two optional drafts **D01** (p0 La~Hire/pole–polar two senses) and **D02** (groupoid rem:equianharmonic — three covers, two provably one). | Node says D01/D02 apply only with Daryl's nod; not applied. Base r2428 is recent (one rev before Artie's). Sites not re-verified by 54. |
| `handoffs/23_CR_DIG_COMMIT_MANIFEST_r501.md` | **23** | **r501** | Group A: one physics edit in `algebroid_paper.tex` (`R_ab R^ab` mislabel → Kretschmann). Group B: r501 acoustic/Hubble body-completion (harmonize + supersession-mark). | **Base is ~2000 revisions stale.** 54 checked two things: **Group A's target is STILL PRESENT** — `algebroid_paper.tex` line 262 still reads `R_{ab}R^{ab}=6M^2/r^6+12/\alpha^4`. **Group B is not applicable** — 6 of its 7 target docs no longer exist (`KICKOFF_GATE`, `SEAM_FRONTIER_ORIENTATION`, `THE_SYNTHESIS`, `THE_VISION`, `THE_GROUNDED_RECORD`, `THE_VISION_JOURNAL` are gone; only `THE_PLAN.md` remains). Neither group applied. |
| `handoffs/37_artie_HANDOFF.md` | **37 (Artie)** | r2429 | CC-2: four empty `\bibitem` entries whose keys are `\cited` (broken refs). CC-1: "finite-curvature branch point r=0" locus question (infinite-curvature r=0 vs finite-curvature Nariai seam α/√3). | CC-2 was node-flagged **READY**; 54 re-verified it on the current tree (the same four still empty, fill text corpus-attested), and **applied it as revision c54.185** (commit on this branch). CC-1 is a physics question on the live edge — **not applied**, for the author. |

## The one applied edit on this branch

- **c54.185** — filled the four empty `\bibitem` entries (Artie's CC-2), text taken byte-for-byte
  from the corpus's own majority-attested bibitems. `check_citations` green; zero empty bibitems
  remain. 56 can keep or revert; the source reasoning is in `handoffs/37_artie_HANDOFF.md`.

*Everything else in `handoffs/` is unapplied and awaits 56's judgment.*
