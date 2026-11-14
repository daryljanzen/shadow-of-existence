# E3 — Contamination and the cold reader: RESULT

**Headline.** **The planted flaws sit at ceiling.** Every review in every condition found all three planted flaws (240 of 240 on Opus). The registered ceiling clause fires, and P1–P3 on flaws found are untested. **The co-primary measure, registered before the main run, moves.**
- **The commissioning purpose cuts review depth.** "Check the recommendation is clear and the document is ready to go" (C3) lowers the valid problems raised beyond the planted flaws by about 2 per review against the framing alone (C1). That is P3b, and it holds.
- **The author's framing alone does not significantly cut depth.** C1 − C0 is −0.40 [−0.98, +0.18], so P1b fails.
- **Telling the reviewer it is scored on finding problems (C2) raises depth** against the framing alone, as 60's reframing anticipated.

- **Run:** 2026-11-13, `claude-opus-5-5`. 30 documents × 4 conditions × 2 replicates = 240 reviews, each with a blind scorer pass. 0 failed. `claude-sonnet-5-5` runs the same design as the replication arm (below).
- **Cost:** Opus arm, scoring and the framing classifier: about $36 at list price (`../USAGE.tsv`).
- **Records:** `runs_main/`, `scores_main/`, `handcheck/`, `framing_map.json` (with `framing_raw/`). The analysis is `analyse_e3.py main`.

## Results, Opus (per document, replicates averaged; 95% bootstrap over 30 documents)

| | C0 cold | C1 author's framing | C2 framing + scored on finding problems | C3 framing + commissioning purpose |
|---|---|---|---|---|
| **Flaws found** (of 3) | 3.00 | 3.00 | 3.00 | 3.00 |
| **Valid other problems** (co-primary) | **8.92** | **8.52** | **9.48** | **6.57** |
| Invalid other problems | 0.20 | 0.73 | 0.67 | 0.67 |
| Review length (words) | 875 | 935 | 987 | 839 |
| Valid other problems per 1,000 words | 10.2 | 9.1 | 9.6 | 7.8 |
| Reviews referring to the author's description | 0 / 60 | 52 / 60 | 53 / 60 | 50 / 60 |
| Reviews endorsing the document | 0 / 60 | 0 / 60 | 0 / 60 | 0 / 60 |

**Paired contrasts on valid other problems:**

| | estimate |
|---|---|
| C1 − C0 | −0.40 [−0.98, +0.18] |
| **C3 − C1** | **−1.95 [−2.57, −1.33]** |
| C3 − C0 | −2.35 [−3.10, −1.63] |
| C2 − C1 | +0.97 [+0.20, +1.70] |
| C2 − C0 | +0.57 [−0.27, +1.37] |

**Invalid other problems rise with the framing:** C1 − C0 is +0.53 [+0.33, +0.73]. Given the author's account, reviewers raise about half a point more problems that are not real weaknesses. Many are challenges to claims the framing makes that the document does not.

## Against the registration

- **Ceiling: fires.** C0 finds 3.00 of 3, above the registered 2.8. The planted flaws are too easy to show contamination on that measure, and that is reported, not explained away.
- **P1 (C1 < C0 on flaws, by ≥ 0.3): fails at the ceiling.** +0.000 [+0.000, +0.000].
- **P2 (praised flaws found less often under the framing): untestable.** A blind classifier (`classify_framing.py`; framing and flaw list only) marked 75 of 90 flaws as praised by the framing and 13 as not mentioned. Every one was found in every condition.
- **P3 (C3 < C1 on flaws): untested at the ceiling.**
- **P4 (C2 < C1, registered at 35%): fails, as expected.** On flaws it is at ceiling. On depth, C2 is *above* C1 (+0.97, interval excluding 0). Per 60's ruling this is a second result, not a lost prediction: being told it is scored on finding problems makes the reviewer look further.
- **P5 (C0 endorses fewer documents than C1): not held.** No review in any condition endorsed a document.
- **P1b (C1 < C0 on valid other problems, interval excluding 0, 50%): fails.** −0.40, with the interval reaching +0.18.
- **P3b (C3 < C1 on valid other problems, interval excluding 0, 65%): holds.** −1.95 [−2.57, −1.33], about 23% fewer.

**C3's drop is not only length.** C3 reviews are about 10% shorter than C1's. But valid problems per 1,000 words also fall (9.1 → 7.8), and invalid problems do not change. So the drop is not a stricter validity threshold either.

**Restricted to reviews that do not mention the author's description** (registered at `r7750`): only 4–10 reviews per condition qualify, because most framed reviews name the framing. The restricted contrasts have the same sign (C1 − C0 −0.50, C3 − C1 −1.63) and intervals too wide to read (n = 6 and 4 documents).

## The hand-check (registered at `r7755`; drawn and scored before the aggregate was read)

- **The sample:** 48 of the 240 Opus scorings, 12 per condition, drawn with seed 3755 (`handcheck/draw.py`). Each packet held the document, the key and the review, plus the scorer's list of other problems with its valid/invalid marks removed. My scores were committed (`25de00511`) before `KEY.json` was opened.
- **Flaws found:** 144 of 144 agree. κ is undefined, because both columns are constant at 1.
- **Valid/invalid per listed problem: 416 of 428 agree, κ = 0.80.** By condition: C0 0.71, C1 1.00, C2 0.74, C3 0.77.
  - The disagreements split evenly: 6 the scorer marked valid and I did not, and 6 the reverse.
  - Mean valid per review is identical under both codings (8.23).
  - Most of mine were judgements about issues that are artefacts of the reading date (a launch date "already passed") or that argue with the framing rather than the document.
- **What it settles:** the co-primary's validity judgement holds up. This is the reverse of E5, where the matcher's threshold was much stricter than mine (κ 0.07). E3's scorer prompt asks the same question I answered, and the two of us agree.
- **The limit:** the hand-scorer is a model of the scorer's family. So this checks how the rubric was applied; it is not an independent human judgement.

## Sonnet 5.5 (replication arm; not a second test of any prediction)

`analyse_e3.py main_sonnet`; 240 reviews and 240 scorings, 0 failed, about $24 at list price. It was paused once mid-run for the weekly-limit check and resumed from its saved records.

| | C0 | C1 | C2 | C3 |
|---|---|---|---|---|
| Flaws found (of 3) | 2.98 | 2.98 | 3.00 | 2.98 |
| Valid other problems | 7.98 | 7.88 | 8.90 | 7.27 |
| Invalid other problems | 0.62 | 1.28 | 1.43 | 1.17 |
| Valid per 1,000 words | 11.1 | 10.3 | 11.0 | 10.3 |

- **Flaws:** at ceiling again (59–60 of 60 reviews found all three).
- **C1 − C0:** −0.10 [−0.82, +0.60], the same null as Opus.
- **C3 − C1:** −0.62 [−1.30, +0.05]. The direction replicates, but the size is a third of Opus's and the interval reaches 0. Per 1,000 words C3 equals C1 in Sonnet, so its drop is mostly shorter reviews.
- **C2 − C1:** +1.02 [+0.12, +1.90]. This replicates: the scoring cue raises depth.
- **Invalid problems rise under the framing:** C1 − C0 is +0.67 [+0.35, +0.98]. This replicates.
- **Framing mentioned:** 57–58 of 60 in each framed condition. Too few non-mentioning reviews remain for the restricted contrast.

## What this means for the paper (Steps 4 and 5.3)

- **"Contamination collapses interference" is not supported as stated.** On the planted flaws, the cold reader, the framed reader and the commissioned reader all found everything. Handing a reviewer the author's sincere, persuasive account did not stop it finding the problems the account praised (75 of 90 flaws).
- **What the framing costs is breadth, and only modestly.** The framing alone trims the review's other findings by about 0.4 (not significant) and adds about 0.5 spurious ones.
- **What costs breadth clearly is the purpose.** Telling the reviewer the job is to check the document is "ready to go to the decision-makers" cuts the extra problems it raises by about a quarter. Telling it the job is to find problems raises them. In Sonnet the scoring cue's rise replicates in full. The commissioning purpose's cut replicates in direction only, at a third of the size, with its interval reaching 0.
- **So Step 5.3's mechanism, read from this data, is the *question asked of the reader*, not the reader's exposure to the author's view.** A paper sentence should say that. It is the same direction as E8's late-session thinning: the planted flaws survive, and depth is what moves.

## Deviations

1. **P2's praised/not-mentioned split was not annotated in the materials.** It was built after the hand-check and before the aggregate was read, as a blind classifier pass over framing and flaw list only (`classify_framing.py`, 30 calls). At the ceiling it decides nothing.
2. **One scorer reply (C1/E3-10, replicate 0) has malformed JSON** (a stray quote before one object in its `other` list). `analyse_e3.py` repairs that one character and nothing else. The record is unchanged.
3. **The n rule was not needed.** At the ceiling, σ of C1 − C0 on flaws is 0.
