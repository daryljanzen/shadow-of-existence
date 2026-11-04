# `r7671` (cc66) — THE SPLIT IS **4 / 13 / 13**, AND THIRTEEN OF THE THIRTY ARE THE CONTROL SIDE OF TWO-ARM READS

**Receipt:** `split.py` — 12 checks, 0 failures.
**Registered:** `PREDICTION.md`, its own commit (`r7671+cc66.3`), pushed before a line of `split.py` existed.
**Tree:** branch `claude/shadow-of-existence-setup-5tjf0b`, base `origin/main` at `b9e12a98e`.
**Generated list:** `SPLIT.md` — thirty items, each with verdict, sentence anchor, reason and spectra.

## THE SPLIT

| | items |
|---|---|
| **RE-GROUND** → 69 in one batch (`FOR_69.md`) | **4** |
| **REBUILD** → 70 (`FOR_70.md`), 21 distinct spectra, 18 repoint / 3 build | **13** (10 traced, 3 untraced) |
| **HELD** — control side, pending 70's measurement | **13** (11 control-leg reads, 2 control-figure sentences) |

## ⛭⛭ THE RESULT THAT WAS NOT ORDERED, AND IT IS THE USEFUL ONE

**Thirteen of the thirty rest on the CONTROL side, and that is `r7669`'s own finding turned round.**
`r7635`/`r7643` moved each receipt's CR legs onto the arm of record and **could not** move the
control legs, because no arm-of-record grid carries one — four families, four times zero. The shape
it leaves is visible in the receipts themselves: `_grid_for(tag)` sends `cr*` to
`refit_grid185_leafrec1` and the control to `refit_grid185`; `BANK = {'cr': …_leafrec1, 'lcdm': …}`
appears verbatim in four receipts; `_SRC`, `_VER`, `_FINE`, `_PAIRS`, `GRIDS` and `SPEC` all have the
same two-entry shape with one entry moved and one not.

⇒ **So PO-87's list is not mainly a rebuild backlog. It is mainly the control side of two-arm reads,
and 70's single ordered measurement of whether `LEAFREC` reaches the control decides thirteen items
at once.** *That is the cheapest thing on either routing page, and it is already ordered.*

## THE REGISTERED ARMS — ONE FALSIFIED, FOUR HIT

**① FALSIFIED, on the high side.** Registered: 4 to 10 of the thirty held as control-only. **13 are**
— 11 resting on a control leg and 2 more printing nothing but the control's own figures. *The cause
is the structural finding above, which I had the evidence for at `r7669` and did not carry into the
registration: I registered the count as if the control-only class were a residue, when the bank's
shape makes it the majority.*

**② HIT.** Registered: at least 12 REBUILD. **13.** *The only arm of the five that did not move under
the reading, and the number 70 is sized by.*

**③ HIT, and this one was registered in the direction that costs me.** Registered: the wording regex
(`this arm` / `crossing arm` / `the arm of record`) disagrees with the read verdict on at least 5 of
the thirty. **It disagrees on 22 and agrees on 8.** Seven disagreements are sentences whose words
carry *"this arm"* while the item rests entirely on the control side; six more are control-side items
the regex would hand 69 as RE-GROUND wordings to land. ⇒ *The cheap signal is falsified a sixth time,
and this time as a prediction rather than as a refusal. `ITEM2_TRIAGE.md` said in its header that the
regex was worthless; the measurement is now on the record.*

**④ HIT, at the floor.** Registered: at least 3 items whose sentence is still RE-GROUND because the
figure it prints is a **method or instrument property** no re-derivation would move. **3 are:** the
acceptance law's stability under refinement, the Bessel route's documented aliasing failure, and the
low-multipole sweep's provenance against its own producer. *This is the open question I put to 69 at
`r7671+cc66.1`; it is now a count rather than an opinion.*

**⑤ HIT, and it is the only gate that reaches the reading itself.** Registered: 30 of 30 reasons
anchored in their own sentence. **30 of 30.** `Ⓐ③` asserts that each verdict's reason quotes a
fragment appearing **verbatim** in one of that item's own precise citing sentences. ⇒ *A verdict I
invented rather than read would fail there.*

## WHAT THE GATES CAUGHT IN THIS FILE'S OWN FIRST RUN

Three failures, all mine, all corrected to the measured state rather than relaxed:

1. **`Ⓐ④` caught three spectrum paths that do not exist.** I had put `cr_nodrive.npz`, `cr_rb0.5.npz`
   and `cr_rb1.5.npz` in `r7093_directions/grid_oneclock/`, reading the literals out of the receipts
   without checking which directory constant they join. They live in `r7201_cc66_loading_lever/`,
   **which has a `_leafrec1` sibling carrying all four CR legs.** ⇒ *So three items I had called
   builds are repoints, and the "to build" count fell from 6 to 3. A path I had routed to 70 as work
   would have sent it to a directory that has never held the file.*
2. **`Ⓐ⑤` caught two items where the gate itself was too strong, not the verdict.**
   `derived_lensing_on_the_lcdm_arm` and `the_joint_fit_leaves_the_gaussian` read **one** control
   spectrum and nothing else, so requiring a live `_leafrec1` read of them asserted something false.
   The two grounds are now separate and **both halves are asserted**: `ctrl-read` must name an
   arm-of-record path, `ctrl-only` must name none and declare nothing but control legs.
3. **`Ⓐ③` caught one anchor that was not verbatim** — the paper writes `$\approx0.487$` and I had
   quoted `$0.487$`. *A one-character miss, and exactly the failure mode the gate exists for.*

## AND THE SENTENCE TEST'S SIXTH CUT, WHICH MOVED THE SENTENCES AND NOT THE LIST

`r7671+cc66.2`'s cut 5 bounded a sentence at brace depth **zero**. That is right for body prose and
wrong inside a `\caption{...}`, where every period sits deeper: no boundary was ever found, the
enclosing-group search asked for the wrong depth on the closing brace, and the span ran to the end of
the file. **One citation in `Fig.~\ref{fig:acoustic-nofit}`'s caption produced an 80 kB "sentence".**

Cut 6 bounds a sentence at **the depth of its own citation**, inside the brace group that encloses it,
and admits `.}` before whitespace as a boundary. ⛭ **The figure-printing count is 30 before and after,
and no span fails the contains-its-own-citation test.** ⇒ *That is the convergence `r7667`'s `Ⓒ④`
claims, tested by the one change that could have broken it.*

⛔ **And the sentence test now lives in ONE place.** Three instruments carried their own copy —
`census.py`, `classify.py` and `sentence_at.py` — and the copies drifted; `classify.py` was still
carrying the crude one after the census's was fixed, so its own subset counts inherited the same
inflation. `r7667/sentence.py` is now the single definition all three import. Re-scored on it,
`classify.py`'s figure-printing handover subset falls from 24 to **17**, and its arm-② gate — which
had been pinned against the literal `22`, the census's count on the **crude** test — now **imports the
census and compares the two populations as SETS**: 15 against 17, the census's a strict subset, the
two extra being the both-arm items its candidate rule excludes.

⌗ **Two reporting errors in `census.py` were corrected at the same time.** Four items printed
`re-derivable by repointing: YES` while the cheap/expensive split counted them **expensive** — `cheap`
also requires that no load site be undecidable and the printed line did not. And a sentence citing an
item twice was printed twice.

## WHAT THIS DOES NOT SETTLE

No figure is re-derived and no sentence in `corpus/CR_cosmology.tex` is edited. The five RE-GROUND
wordings are **proposals**; 69 lands them and reads each where it lands. The REBUILD list is **paths
with configurations**; 70 prices it, and the three untraced items are flagged so no build budget is
spent on a spectrum that may already be read on the arm of record. The thirteen HELD items are not
verdicts at all until 70's control measurement comes back.
