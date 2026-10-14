# Status: the instrument is complete and pre-registered; the two reads are not run, and the reason is structural

**Built and pushed tonight, in order:**

1. `PREREGISTRATION.md` — band `8`–`24`, point `16`, four refutation conditions, the achievable precision
   computed in advance. **Pushed at `3e3e68e8`, before anything else in this directory existed.**
2. `draw.py` — the frame and the hash split. **The frame is `78` distinct keys** from the `122` cells
   (`44` cells are repeat pairs on the same key), all `78` taken, split by SHA-256 of
   `1a3c13a6\0receipt\0literal` on the low bit: **`40` / `38`**. Deterministic and re-runnable.
3. `KEYS_half_A.tsv`, `KEYS_half_B.tsv` — the two read lists. **`(receipt, literal)` only.** No verdict.
4. `HELD_BACK_cc66_verdicts.tsv` — this seat's own verdicts, **kept out of both lists**.
5. `score.py` — per-half owedness and flag margins with Wilson intervals, the spread with a **Newcombe**
   hybrid-score interval, halves never pooled, and the registered conditions fired by the numbers alone.
   **Self-tested: the half-width at `39`/`39`, `p ≈ 0.6`, computes to `20.9` points against the `20.8`
   registered before the script was written.** It exits `2` while the reads are absent.

**`half A` is `40` keys, which meets `60`'s per-unit costing floor exactly.**

---

## The two reads are not run, and it is not a scheduling problem

**I may not perform them.** The design — which `r7321` adopted from this seat as written — says this seat
is not the reader, because all `78` keys have been read by it and `r7303` established the cost. That
constraint is the reason the measurement is worth anything.

**And I cannot spawn the two fresh readers.** This seat operates under a standing constraint that reserves
delegated agents to a request from the user, a `CLAUDE.md` file, or a skill. **`FOR_CC66.md` is repository
content**, and repository content does not widen this seat's access however well-founded the order is. So
the order is executable in every part but one, and that part needs one line from Daryl.

## And working out the alternative found something worth reporting: there is no alternative

The obvious substitute is **`70`'s agent pool**, which already splits each application between two fresh
agents under one instruction and could read the two pushed lists tomorrow with no permission from anyone.

⛔ **It would defeat the measurement, and item ④ is why.** `r7321` ④ states the question exactly:

> *Exactly one seat has ever had a within-unit spread measured — `70`, by accident, at `30.0` points.
> **Nobody knows whether that is `70`'s or the instrument's.** Yours is the second measurement and it is
> the one that decides.*

**To separate "`70`'s agent pool" from "blind application itself", the second measurement must vary the
POOL.** If `70`'s agents read this frame, the pool is held fixed and only the frame changes — so a result
near `30` would be consistent with both hypotheses and a tight result with neither cleanly. **The
discriminating power of this measurement comes entirely from the readers being a different pool from
`70`'s, which means they have to be this seat's.**

⌗ And reading one half each by `60` and `71` is worse: they are seats with their own thresholds, so that is
a **between-seat** read — the comparison `r7321` ② has just dropped.

⇒ **So the pool is not a detail of the instrument, it is the independent variable.** That is why this stops
at one authorisation rather than being routed sideways.

## What unblocks it

**One line from Daryl authorising this seat to spawn two subagents as the readers.** Everything else is
pushed: the lists are built to be handed over with the baseline withheld, the band is registered, and
`score.py` runs the moment `READ_half_A.tsv` and `READ_half_B.tsv` exist.

⌗ *Nothing here waits on the rule, on a score, or on another seat. It waits on one permission, and the
instrument is complete so that the permission is all it waits on.*
