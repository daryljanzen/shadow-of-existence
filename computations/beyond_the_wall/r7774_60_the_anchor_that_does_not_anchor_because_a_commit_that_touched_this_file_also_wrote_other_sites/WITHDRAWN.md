# r7774 — WITHDRAWN UNRUN, BY ORDER, AND ITS PREMISE WAS FALSE ANYWAY

**Two independent reasons, and both are recorded rather than one being used to hide the other.**

## ⛔ ① By order

`r7765` (69): *"**Stand down from the S11 gate work (r7772, r7774).** Instruments that measure
instruments are not the work now; the photon-family stale-key successor (r7770) is enough. Leave
r7774's registration unrun."*

**Stood down. No arm of this registration was run, no repair was built, and `S11` is not edited by
this revision.** The registration stays in place, unrun, because a registration that is deleted
leaves no record that it was made.

## ⛔⛔ ② AND ITS PREMISE WAS FALSE — WHICH ALSO WITHDRAWS A FINDING `r7772` PUBLISHED

The registration's premise, taken from `r7772`, was that `S11`'s six failing gates *"each assert a
figure scored on one past push and recomputed live"*, and that `S11` is **red on `main`**. Measured
after the registration was pushed, before the stand-down arrived:

* **`S11` exits `0` on a FULL clone.** The six gates were never stale.
* **This clone was shallow, and that is the whole cause.** `git blame` attributes **`459` of `596`**
  lines of that receipt to a graft-boundary commit, and the receipt's `Ⓓ` block pins a commit
  (`9ce054ba`) that **does not resolve here at all** — `git cat-file` returns *"Not a valid object
  name"*. Two of the eight receipts pin commits this clone could not resolve.
* **⛔ And `r7772`'s "red on `main`" test could not have detected this.** It ran each receipt in a
  detached worktree of `origin/main` — **which shares this clone's object store**, so a worktree of
  `main` is as shallow as the branch. *A worktree is not a second clone, and I read it as one.*

**Re-run on a full clone (`git fetch --unshallow`, `7956` commits from HEAD), the eight receipts
`r7772` reported as red on `main` come back:**

| receipt | shallow | full clone |
|---|---|---|
| `L248/R1` | red | **green** |
| `L253/S1` | red | **green** |
| `L_probability/S11` | red | **green** |
| `L_probability/S13` | red | **green** |
| `L_probability/S59` | red | **green** |
| `P15/C60` | red | **green** |
| `L_probability/S1` | red | **still red** — the genuine one, cc66's undeclared input, which `r7765` says is now patched and passing |
| `L_probability/S55` | red | **over the 900 s budget, undecided** — it needs a longer budget on the deeper history and is not called either way here |

⇒ **`r7772`'s finding that eight receipts fail on `main` is WITHDRAWN. Six of them fail only in a
shallow clone; one was the real red, already fixed by the gate; one is undecided.** The part of
`r7772` that stands is the `Ⓔ①` repair itself — a populated set, an in-run seed, a printed count —
and the observation that a gate which passes either way is invisible to every verdict list.

## ⛭ What the shallow clone was costing, beyond this

The five reds this line has called *"the five structural shallow-clone reds"* for many revisions, and
the `⛔ HORIZON: THE CLONE IS SHALLOW` warning the revision-id checker printed on every landing, are
the same artefact. **After `--unshallow` the checker's horizon warning is gone.** *The deepening is a
one-command fix that was available the whole time, and this line validated around the artefact
instead of removing it.*

## The guard this costs, offered for the standing list

**A worktree shares its clone's object store, so a worktree of the base branch tests the branch and
not the clone.** To separate "red on the base" from "red in this checkout", the thing that must
change is the OBJECT STORE — deepen it, or clone afresh — and not the ref you check out.
