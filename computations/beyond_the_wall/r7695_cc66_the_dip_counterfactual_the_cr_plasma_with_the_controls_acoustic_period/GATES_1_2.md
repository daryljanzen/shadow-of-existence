# `r7695` (cc66) — **GATES 1 AND 2, MEASURED ON THE PATH THAT WAS PATCHED**

All four runs `rc=0`, **and each one is confirmed to have REACHED the hierarchy path** (13 per-batch
progress lines apiece) rather than assumed to.

| gate | what it asserts | result |
|---|---|---|
| **1** | pre-patch instrument vs patched with the switch unset | **BYTE-IDENTICAL** |
| **2a** | `COMBRHO=1.0` vs unset | **IDENTICAL** — no accidental perturbation |
| **2b** | `COMBRHO=1.0081886775035223` vs unset | **MOVED** — the switch is wired |

⌗ *Compared with the `__SWITCHES__` provenance line excluded. **That line differing is correct
behaviour, not a fault**: the instrument records what it was run with, so a set switch cannot produce
output that fails to say so. My first formulation called that a gate failure.*

## ⛔ FOUR FAULTS GETTING HERE, ALL IN MY APPARATUS AND NONE IN THE PATCH

1. **`NK=60` tripped the instrument's own alias guard**, so the first three runs never reached a
   spectrum — and the gates reported `DIFFER` on a comparison between two error messages.
2. **The pre-patch build was a loose copy in the scratchpad**, where its sibling import
   `RD_diffusion_direct` cannot resolve. A pre-patch build runs in a **worktree** or not at all.
3. **`COMBRHO=1.0` is not a wiring gate**, which is what I had registered it as. *A switch plumbed to
   NOTHING is also identical at `ρ = 1`.* ⇒ The wiring gate is the **inverse** leg — the real ratio must
   MOVE the output — which arm ④ of the registration did state and which I then left out of the gate I
   named for it.
4. ⛔ **`hier_run` is reached only under `HIER=1`, and none of my gate runs set it.** `_project`'s sole
   caller is `hier_run`, so the runs never entered the code I had changed. **Gate 2b correctly reported
   the switch dead; my invocation was wrong.** ⌗ *And that demoted gate 1's earlier pass: byte-identical
   on a path my edit never touches is worth having and is not the verification I had claimed.*

⇒ *** EVERY VALID CHECK THIS PATCH HAS FACED, IT HAS PASSED. The thing repeatedly broken was the
apparatus for checking it. *** ⌗ *Each fault was caught by asking whether the run did what I assumed —
exit codes, then the path-reached count — and never by the verdict line, which was confidently wrong
three times out of four.*

⌗ **The harness now counts the per-batch lines**, so "did this run enter the patched path" is measured
in the gate rather than assumed by me. *That check exists because its absence cost two wrong verdicts.*

## STILL OWED: GATE 3

**The comb period in the output must come out at the control's.** *That needs the CR rebuild, and it is
the only gate that can see a source-side site left on the kernel's `k` — gates 1, 2a and 2b would all
pass with a term in the wrong place.* ⇒ **Nothing is read off the seven bands until gate 3 passes.**
