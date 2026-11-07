# r7704 (60) — RESULT: the two landed fixes, and `prop:cycloid`'s scope

**Order answered:** `r7701` (69), items 1 and 2.
**Tree:** `84fb2b59`, named in `runs/TREE.txt`. **Registered** at `1c860464`, pushed before
`probe.py` existed, with `janzen_circle_v3.tex` unopened beyond two `grep` hits.
**Readings:** `runs/READINGS.txt`, probe exit `0`, seven verdicts, no reader or classifier probe
failed on its final run.

## ITEM 1: 3 of 3 SUPPORTED · ITEM 2: THE SCOPE FLAG HOLDS — P2 READS AS GENERAL

---

## ITEM 1 — both fixes are in place, and the row now agrees at all three sites

**1a — `l.2612`'s repaired row: SUPPORTED, figure by figure.** The site prints `−2.6`, `+0.9`,
`+2.2`, and each is the gated arm A `(L)` value (`−2.56`, `+0.93`, `+2.16`, pinned two-sided at
`6e-3`). **And the structural claim still holds of the new row**: the gated terms make `ℓ=4`'s
`+2.16` the largest of the four, which is what the sentence says. That was the one thing the
repair could have broken, since the claim and the digits were previously true of different rows.

**1b — THE ORDER'S CHECK: the per-multipole figures agree at EVERY site.** Three sites print two
or more terms of the row, read side by side as the same quantity:

| site | `ℓ=2` | `ℓ=3` | `ℓ=4` | `ℓ=5` |
|---|---|---|---|---|
| `l.2612` | `−2.6` | `+0.9` | `+2.2` | — |
| `l.2814` | `−2.6` | `+0.9` | `+2.2` | `+1.1` |
| `l.2903` | `−2.6` | `+0.9` | `+2.2` | — |

**No multipole is printed with two different values anywhere.** The cross-site reader's negative
probe was run: with one site's octopole term altered on a copy, it sees both values.

**1c — the doubled-opacity clause, branch (b) as landed: SUPPORTED.** The clause now reads "the
hierarchy's depths, swept on the control's background, do not move under a doubled opacity grid,
…", the old wording that attached the convergence to the `(L)` agreement is gone, and every bank
the receipt's two knob sweeps use is a **control** bank — which is exactly what the new wording
names. So the clause and its evidence are now about the same object.

⌗ Branch (a) — the knobs recorded in the `(L)` configs and the sweep run on `(L)` — is ordered to
`70` and is not this seat's.

---

## ITEM 2 — `prop:cycloid`: 71's flag holds, and eleven markers searched over the whole of
`janzen_circle_v3.tex` (659 lines, read at source) return the restriction NOWHERE in P2

**The proposition, quoted from this tree:**

> **Proposition (Lemaître–Tolman cycloid form).** Within the Schwarzschild interior `r ∈ (0, 2M)`,
> the radial proper-time parameter `τ` along **a radial timelike geodesic** satisfies
> `r(η) = M(1 + cos η)`, `τ(η) = M(η + sin η)`, for `η ∈ [0, π]`, with `η = 0` corresponding to the
> horizon `r = 2M` and `η = π` corresponding to `r = 0`. The proper-time interval from horizon to
> `r = 0` is `τ(π) − τ(0) = Mπ`.

**2a — the statement reads as GENERAL, and so does the whole paper.** The searches, reported
whatever they returned: the markers `E = 0`, `E=0`, `marginally bound`, `released from rest`,
`at rest`, `specific energy`, `zero energy`, `vanishing energy`, `momentarily static`,
`parabolic`, `critically bound` return **NONE in the statement, NONE in the proof, and NONE
anywhere in P2**. The object is named "a radial timelike geodesic" — the general member.

**And the restriction is nevertheless there, in the proof's first line.** The proof opens with

> `dτ² = dr²/(2M/r − 1) = r/(2M − r) dr²`

which is `(dr/dτ)² = 2M/r − 1`, i.e. the `E = 0` member of `(dr/dτ)² = E² − 1 + 2M/r`. So the
restriction is **used and not stated** — the shape `r7694`'s hypothesis probe was built for, here
in its sharpest form: the hypothesis does the work and appears in no hypothesis list.

**2b — the amplitude: SUPPORTED as a reading.** The paper writes `r(η) = M(1 + cos η)` (amplitude
`2M`), `τ(η) = M(η + sin η)`, and the interval `Mπ`.

**2e — THE FLAG CHECKED RATHER THAN ACCEPTED, by computing.** 71's general amplitude is
`2M/(1 − E²)`; at `E = 0` that is `2M`, **which is the paper's**. So flag and paper agree at
`E = 0`, and the scope is therefore the only question — which is what makes this a scope finding
and not a disagreement about the solution. Then the interior proper time was integrated here for
the general member, under the substitution `r = r_max sin²θ` that removes the turning-point
singularity analytically:

| `E` | `r_max` | interval |
|---|---|---|
| `0.00` | `2.000 M` | **`3.141593 M`** = `πM` to `5e-15` — the paper's figure |
| `0.25` | `2.133 M` | `2.370868 M` |
| `0.50` | `2.667 M` | `1.891199 M` |
| `0.75` | `4.571 M` | `1.566498 M` |
| `0.90` | `10.526 M` | `1.418173 M` |
| `1.00` | unbounded | `1.333333 M` = `4M/3`, the from-rest-at-infinity member |
| `1.20` | unbounded | `1.189787 M` |

⇒ **The printed `πM` is the `E = 0` member's, and it is `2.36` times the `E = 1` member's.** It is
the largest of the seven values computed here and the family's value falls monotonically across
them — seven points, so a measurement of the family at those values and not a proof that `πM` is
the supremum. The flip was run: the same integral at `E = 0.5` returns neither `πM` nor `4M/3`.

**2c — EVERY using site reads as general too, and they were found by content as well as by
reference.** Only ONE site carries `\ref{prop:cycloid}` (`l.168`, the interior-metric derivation).
Two more **use** the proposition without citing the label: `l.136` (the proof's own closing "The
total proper time is `τ(π) = Mπ`") and — the one that matters — **`l.458`, a summary item**:

> The infalling worldline reaches `r = 0` in finite proper time (`τ = Mπ` from horizon-crossing)
> and ends there …

whose subject is "**The infalling worldline**", with no restriction in its own context. A
proposition can be correctly scoped and still be used out of scope; here it is unscoped in both
places at once.

**2d — THE ORDER'S QUESTION, answered in its own terms: P2 READS AS GENERAL.** The restriction is
stated nowhere that the search above reaches — the eleven markers listed in 2a, run over the
proposition, its proof and the whole of `janzen_circle_v3.tex` (659 lines, read at source),
which return none — and all three using sites inherit that.

### ROUTED

1. **The proposition's hypothesis**, six words: *"along the radial timelike geodesic with `E = 0`"*
   in place of *"along a radial timelike geodesic"* — or, if the general family is wanted, the
   amplitude becomes `2M/(1 − E²)` and the interval is no longer `Mπ`.
2. **`l.458`'s summary item**, four words: *"reaches `r = 0` in finite proper time (`τ = Mπ` from
   horizon-crossing **for the `E = 0` member**)"*. The weaker general statement that is true of
   the whole family as measured here is **"at most `πM`"**.
3. ⌗ **A note for the formalisation starting this turn**: the `E = 0` relation
   `dτ² = dr²/(2M/r − 1)` is what the proof actually uses, so a formal statement built from the
   proposition as written would carry a hypothesis the prose does not — the cheapest moment to fix
   that is before the statement is transcribed, which is why `r7701` ordered this read now.

---

## THE PROBE CAUGHT ITSELF TWICE

**① The row reader could not see `l.2903` — the site the order named.** Its first form required the
figure to be the whole math expression (`$-2.6$`), and at `l.2903` the same term is printed inside
a larger one (`$\Delta(-2\ln L)\approx-2.6$`). So the reader was blind to exactly the comparison it
was built for, and reported two sites where there are three. **Third instance in three revisions of
one family** — `r7700`'s ASCII-only hypothesis names, `r7702`'s three-place-only figures, and now
this: **an instrument reads the FORM it was given, not the QUANTITY.** Fixed to match the signed
figure wherever it sits in a math span, with digit boundaries so `−2.65` cannot pass as `−2.6`.

**② The interval integral returned `3.139527 M` against `πM`** — a relative error of `7e-4` that
failed this arm's own `1e-4` tolerance and made a correct reading print NOT SUPPORTED. The
integrand diverges as `r → 2M`, so a uniform rule under-resolves the one endpoint that carries the
answer. **The fix was the quadrature, not the tolerance:** loosening the tolerance to admit a weak
instrument would have hidden the instrument and left the arm passing for the wrong reason. With the
singularity removed by substitution the integral returns `πM` to `5e-15`.

---

## THE LESSON THIS REVISION ADDS

**A tolerance is part of the instrument, so a reading that misses by more than its tolerance is
two claims — one about the object and one about the method — and the first thing to test is the
method.** The `7e-4` miss above looked like a disagreement with the paper's `πM`; it was a
disagreement with my own quadrature.

And the standing one it exercises, now for the third revision running: *an instrument reads the
form it was given, not the quantity.* The guard that follows is to write every figure reader
against the quantity and let the form vary — precision, delimiters, surrounding expression and
alphabet all included.
