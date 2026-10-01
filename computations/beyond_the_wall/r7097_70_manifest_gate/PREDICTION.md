# r7097 (70) — the manifest gate, built and registered as a ratchet; the 13 default-model figures, enumerated

*Pre-registered before the gate is built or the list is drawn. The order is `FOR_70.md` `r7097`, Q1 and Q2. **Nothing is run through the transfer. No banked file, no prose and no other seat's receipt is edited.***

## Q1 — the ratchet, and the choice it rests on

**The choice.** The baseline is **a manifest of the existing artefacts, keyed by path and pinned by content hash**. Each entry carries the backfill grade and the evidence the r7095 prototype found.

**Why that, and not the alternatives:**
- **A dated baseline** (artefacts "older than" the gate pass) needs a date the repository does not keep. Git preserves no mtime, and a commit date is the date of the *last* touch, so a re-banked file would inherit an old date. It cannot tell a new artefact from an old one that was rewritten.
- **The fingerprint as a fallback** would admit any *new* artefact whose ℓ_A happens to fingerprint. That re-opens the hole for exactly the class that should be closed, so it is used to *grade* entries, never to *admit* them.
- **A name-only manifest** is the symptom-pinning the order warns of. It would still pass a file regenerated in place, with different content and still no switches.
- **The content hash is what makes it a ratchet and not a pin.**
  - An entry admits *those bytes*.
  - A rewrite (new bytes) must carry `config`.
  - A deleted artefact leaves a STALE entry, which **fails** and must be removed (the transposition gate's r7069 rule).
  - An artefact that gains `config` makes its entry STALE too, so the manifest can only shrink.

**The gate fails on:**
- a banked `.npz` with no `config` and no manifest entry (NEW);
- a manifest entry whose file is gone or now carries `config` (STALE);
- a manifest entry whose hash no longer matches (REWRITTEN);
- a `config` that is not a JSON object carrying the defining switches resolved (MALFORMED).

**Predicted:** it passes on today's 215 and fails on each of four planted cases (new, stale, rewritten, malformed), each tested on a scratch copy and never in the bank. It runs in under 10 s, so it belongs in the fast list.

**The six (four unplaced, two with no producer).** For each I find the registered receipts that **read** it. **Predicted:** most are read by nothing registered. My recommendation will follow the readers:
- an artefact read by a registered receipt should be **re-derived** (cc66's queue) or its reader re-pointed;
- one read by nothing should be **marked UNPLACEABLE in the manifest permanently**, which is cheaper than retiring it and keeps the record honest.

## Q2 — the 13, complete and unfiltered

This is the census's 13 rows, re-read against the **current** `P15`, after `r7097` withdrew the polarisation pulls. For each:
- the figure as printed today (or WITHDRAWN);
- the paragraph's line range and its first words;
- what the figure is (control, bin count, or CR);
- whether it now stands beside a reported-model figure in the same comparison.

**Predicted:**
- the four pull figures read WITHDRAWN;
- 2.10 still has no carrier;
- the rest are control figures or bin counts, none standing beside a B figure in the same comparison, except that the control's 0.1792 stands beside the B arm's 0.1717. **That is a control-against-arm comparison, not a seam**, and it is listed because the order asks for the complete list.
