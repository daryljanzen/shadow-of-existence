# r7413+70 — PRE-REGISTRATION: what the `reads` zero means (pushed before the test runs)

*Order `r7413` ①, second half. The suite timing in the first half was registered at r7411+70.1 (L-b,
central 8 min, band 2–30). It finished before this order arrived and is scored in RESULT.*

**The two readings, and what separates them.** The `reads` scope is, by its job name, *"on what this push
deleted or renamed"*. A push that only modifies or adds files cannot make an existing read resolve to
nothing, so the scope is meant to be empty then. That gives two hypotheses:
- **H-design:** 0 of 20 because none of the 20 revisions deleted or renamed a file that any receipt reads.
- **H-broken:** the selector returns nothing even when a traced read is deleted.

| arm | test | prediction |
|---|---|---|
| **R-a** | deletions and renames across the same 20 revisions, from `git diff --name-status -M` | `0` deleted or renamed files that any index entry reads (band `0`–`2`) |
| **R-b** | `scope(idx, changed=∅, gone={f}, added=∅, 'reads')` with `f` a file in some receipt's traced `r` list | **fires**: ≥ 1 receipt, and the receipt `f` came from is among them |
| **R-c** | the same with `f` a renamed glob member (one of a receipt's traced `g` patterns) | **fires** |
| **R-d** | the same with `f` a file no receipt reads | **0**, the control |

**Verdict rule, fixed now:** if R-b and R-c fire and R-d is 0, the zero is **H-design**, and R-a must then
show no traced deletions. If R-b or R-c is 0, it is **H-broken**.
