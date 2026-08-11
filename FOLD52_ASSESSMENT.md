---
name: fold52-assessment
description: What the abandoned ACOUSTIC fork (cr_r2381+c54.108+ACOUSTIC, nodes 52 and 53) contains, what this fork should take from it, what it should send back, and what could not be verified here. Read before doing any further work on the first acoustic peak.
sources: [cowork]
---

# THE ACOUSTIC FOLD — assessed against r2376+c54.164

> ## ⛔⛔ READ THIS BEFORE ANY REVISION NUMBER BELOW — TWO DIFFERENT r2377–r2381s EXIST
>
> ***Every `r23xx` above r2376 cited in this document, and every one inside the fold's own tree, belongs to the
> 52/53 FORK'S numbering and is NOT the main line's.*** *Daryl, r2376+c54.166:* **"52/53's 2377-2381 are NOT the
> main fork's 2377-2381."** *The live fork abandoned the 52/53 line at r2376 and has been numbering
> independently ever since, so the two lines have collided in the numbering namespace above r2376 and there is no
> mapping between them.*
>
> **What that costs, concretely.** *`r2157`, `r2069`, `r2337`, `r2349`, `r2361`, `r2367`, `r2369`, `r2387`,
> `spec2381` and the tree name `cr_r2381+c54.108+ACOUSTIC` are all read off the fold's own documents.* **Those at
> or below r2376 are common history and are safe to cite. Those above r2376 are the 52/53 line's and name nothing
> in the live fork.** *A node that cites one of them as a main-line revision will be pointing at a revision that
> either does not exist or is a different piece of work entirely.*
>
> ⌗ **The rule for this fork: cite the fold by DOCUMENT and L-number** — `FOLD_FROM_52.md` §3,
> `ACOUSTIC_HANDOFF.md` §4, `L-117` — *and never by a bare revision number above r2376.* **Nothing from that tree
> enters as a figure in any case (see the closing section), so the only thing a revision number can do here is
> mislead.**
>
> ⚠ *And this document is assessed against the 52/53 fork only. **The actual live fork is a third state** — it
> abandoned 52/53 at r2376, has restructured the programme, and has been tracking this line's work forward. Its
> routing list arrived at c54.166 and is discharged in `THE_LIVE_ARC` and in this revision's commit; that is a
> different object from this fold and the two should not be run together.*

*Daryl supplied `cr_r2381+c54.108+ACOUSTIC` at c54.165 — an abandoned fork in which two nodes (52 and
53) worked the first acoustic peak hard, well past r2376, and which he does not trust the number of.
This is the assessment he asked for: **what is in it that this fork can use.** Nothing from it has
entered the corpus as a figure, and nothing will until it is rebuilt and receipted here.*

---

## ⌗⌗ THE HEADLINE, AND IT IS NOT THE NUMBER

**That fork independently reproduced this fork's c54.164 residual, on a different instrument, and it
has the mechanism.** I found — probing `ROBUST_p1p2_scan` across four initial conditions — that the
propagated source comb comes out at $0.72$–$0.79$ of $\pi/\rs$ under every one of them, while the
initial data move the first peak by 165 multipoles. **Their `FOLD_FROM_52.md` §4 records, in its own
words and from five initial-data configurations on the `HIER` line:**

> *"the compression is **invariant across five initial-data configurations** (spacings 0.64–0.96
> throughout, sky ~1.0) while ℓ₁ moves over 0.74–0.81. **The initial data moves the first peak and
> does not touch the comb.**"*

***Two nodes, two instruments, two fork lines, same result, neither knowing of the other.*** That is
the strongest corroboration any result on this front has ever had, and it arrived by accident.

---

## ⌗ THE FOUR THINGS THIS FORK SHOULD TAKE, IN ORDER

**1. ⚑ THE UNDRIVEN GUARD — and it closes my open residual.** *`FOLD` §3: with every coupling to the
potential removed — the $4\Phi'$ in the photon continuity **and** the $k^2\Psi$ in the photon/baryon
Euler, at **both** the tight-coupled and post-switch sites — the source comb lands on the integers:*

```
   fully undriven, k r_s/pi :  1.0319   2.0823   3.0531     (residual +3.2% +4.1% +1.8%)
```

***This validates the sound horizon, the measure, the k-grid and the phase extraction as an
ensemble.*** ⇒ **So my c54.164 comb deficit is NOT a disagreement with the acoustic scale, and it is
not an instrument failure. It is the driving, and nothing else.** *I registered it as possibly the
former. This is the control that decides it, and I did not have one.* ⚠ *Two cautions they attach and
I will keep: measure it on the **source extrema in $k$**, never in $\ell$-space, where the projection
kernel and visibility width distort spacing independently; and their `NODRIVE` switch swaps the free
variable from $\hat\Theta$ to $\delta_\gamma$, so it is sharp only for $k$-independent data.*

**2. ⚑ A ΛCDM CONTROL ON THE SAME MACHINERY.** *This fork has none that is live — `ROBUST_p1p2_scan`
quotes a control from r1975 in a comment and never runs one.* **Without a control no absolute $\ell_1$
is readable, and my c54.164 comparisons to the sky were made without one.** *Theirs also supplies the
instrument floor: on ΛCDM, where the instrument should be right, $\ell_1$ is $+0.2\%$ but $P_1/P_2$ is
$-2.6\%$ and $P_1/P_3$ is $-5.0\%$.* ⇒ **No height claim below ~4% is meaningful.** *My c54.164
finding survives that floor with room — the ratio spans a factor of 2.2 across the initial-data
variants — but the floor should be quoted with it, and was not.*

**3. THE $\ell_A$-NORMALISATION RULE.** *The two arms run at different $H_0$ and $\Omega_m$ (CR at
$73.0$/$0.3066$, ΛCDM at $67.40$/$0.3150$), so $D_M$ differs by $-6.2\%$ and $\rs$ by $-5.9\%$ **and
they cancel** — $\ell_A$ comes out $301.6$ vs $302.5$.* ⇒ **Raw $D_M$ and $\rs$ are not comparable
across arms; every cross-arm statement must be made $\ell_A$-normalised.** *"Geometry common to
$0.5\%$" was true only because of that cancellation. `PO-7` now carries this rule.*

**4. THE MECHANISM, AS A HYPOTHESIS TO TEST HERE.** *Their $Q_1(k)$ diagnostic — the accumulated sound
phase at each extremum of $\hat\Theta$, mode by mode — and the model-free subtraction
$\Delta(k)=Q_1(\mathrm{flat})-Q_1(\mathrm{slaved})$ against an undriven reference. Their reading:*
**CR's acoustic driving phase shift is the same SIZE as ΛCDM's ($0.144$–$0.154$ against
$0.146\pm0.007$) and turns on in the wrong place in $k$ — as $k^2$ rather than $k^0$** — *because on
L1 the potential is supported by CDM, which does not oscillate and so cannot decay on the
sound-crossing time, leaving the seam transient (timescale $3\mathcal{H}/k^2$) as the only
phase-imprinting process.* ***That is a diagnosis of the comb deficit and it is worth more than any
peak position in the fork.*** **It is a hypothesis here until rebuilt.**

---

## ⌗⌗ WHAT THIS FORK SENDS BACK, AND IT ANSWERS SOMETHING THEY MARKED UNRESOLVED

**Their `FOLD` §1 reads `LIFT_euclidean_filter` (r2157) against the handoff's mechanism and stops at a
question it declines to invent an answer to:**

> *"**Not settled, and stated as such:** how 'frozen modes carry the progenitor's amplitude and tilt'
> delivers $A_s$ and $n_s$ across all $k$ when only $\ell\lesssim1.4$ satisfies the freezing
> criterion. I could not resolve that from the receipt and did not invent a resolution."*

**Front #1 settled it at c54.162, and the fork predates that by fifty-odd revisions.** *Two different
criteria are being run together:*

- ***`LIFT_euclidean_filter`'s* $kc_s|\Delta\eta|\ll1$ is a statement about the Euclidean segment's
  KERNEL** — whether the exponential suppression bites. It gives $\ell\lesssim1.4$.
- ***Front #1's* $c_sk/|aH|\to0$ is a statement about whether the mode is FROZEN at the branch
  point** — outside the comoving sound horizon. It holds for **every** mode from $\ell\simeq28$ to
  $\ell\simeq2475$\rcpt{P16_every_mode_is_frozen_at_the_crossing}.

⇒ ***The kernel acts on oscillatory content, and nothing arrives oscillating, so the exponent never
acts and the $\ell\approx1.4$ boundary is not a boundary at all.*** **Frozen modes carry amplitude and
tilt across all $k$ because every observable $k$ is frozen — not because $kc_s|\Delta\eta|\ll1$.**
*That is precisely the "how" their §1 could not close, and it is why c54.162 also had to withdraw P7's
"a cold species and no other" selection rule — a filter that acts on oscillatory content selects
nothing when nothing arrives oscillating.*

**And their `FOLD` §2 flags a contradiction this fork has already narrowed.** *They found the
instrument carrying $\Phi_0=-1$ while `sec:envelope` says the residual potential is "below a percent"
of the driving amplitude — "the corpus states the initial potential and the code disagreed with it by
a factor of a hundred."* **This fork's c54.155 sharpened that very sentence**: the flatness is a
*deep sub-horizon limit* ($2\%$ at $k\simeq10k_s$, $0.1\%$ at $300k_s$), and the residual is below a
percent **on average while oscillating up to some seven per cent** where $\cos x_{\rm seam}$ is near
an extremum. ⇒ **The corpus line they measured against is not the corpus line this fork now carries,
and the discrepancy is smaller and structured rather than a flat factor of a hundred.**

---

## ⛔⛔ WHAT COULD NOT BE VERIFIED HERE, AND IT GOVERNS EVERYTHING ABOVE

**Their own reproduction gate does not reproduce in this environment.** *`ACOUSTIC_HANDOFF.md` §8:*

> *"The single most useful thing to run first is the control, because everything rests on it… must
> return `l_1 = 221.1` against the sky's 220.6. **If that does not reproduce, stop and fix the
> instrument before reading anything above.**"*

**It returns $\ell_1 = 229.6$.** *Twice, on two configurations:*

| invocation | source | $\ell_1$ returned |
|---|---|---|
| `ARM=lcdm ZS=1e6 ETAEND=1892 NS1=6000 NS2=4000 KMAXL=2500` | handoff §8 verbatim | **229.6** *(grid 230, parabolic 229.7, quadratic 229.6; spread 0.4)* |
| the same, plus `PERTLEAF=1` | `acoustic/README.md` standing ΛCDM config | **229.6** |

*Two further notes, recorded because they are the kind of thing that voids a reproduction:* **the
handoff's §8 command omits `PERTLEAF=1`, which their own README's standing configuration carries**;
and **`pin.py` OVERWRITES `ETAEND` unless `DEFAULTS=1`** (`os.environ.update(...)` at l.31), so the
`ETAEND=1892` in both commands is silently clobbered to `400`. *And $229.6$ is not a random miss — it
is the value `pin.py`'s own docstring was written to investigate: "The projector returned LambdaCDM
$\ell_1 = 230$ in L-81 where the validated setting (spec2381) returns 220."* ⇒ **The shipped `pin.py`
reproduces the pre-fix value, so the $221.1$ came from a state of the instrument that is not the one
in this bundle, or from a path that resolved differently on their machine.** *Their own `FOLD` §6
names this failure mode twice — "hardcoded `sys.path` to a previous revision — twice — silently
importing stale modules."*

### The rule this fixes in place

***Nothing from that fork enters this corpus as a figure.*** **Not $201.3$, not $3.514$, not
$0.144$–$0.154$, not the undriven $1.0319/2.0823/3.0531$.** *Every one of them is a lead to be
rebuilt here, on r2376's physics, and receipted in this fork — or it does not land.* **What transfers
is method: the undriven guard, the control, the $\ell_A$ rule, the $Q_1$ diagnostic, the model-free
subtraction, and the six failures in their §6 that are worth inheriting as rules.** *That was the
discipline stated before the fork was opened, and the failed gate is why it was the right one.*

---

## ⌗ WHAT THE FORK IS BEHIND ON, so it is not read as newer throughout

*It branched at c54.108 and did not receive this line's c54.109–164.* **Its `corpus/` is OLDER than
this fork's**: `CR_cosmology.tex` still carries $P_1/P_2\simeq1.15$ (corrected here at c54.155 to
$1.447$, and withdrawn entirely at c54.164), still says entry occurs at $x=1/\sqrt3$ "*for every $k$*"
and "*the envelope is therefore flat*" without c54.155's two qualifications, and still carries the
"$220$ against $150$" paragraph this fork rewrote at c54.164. ⇒ **Take the instrument line and the
arc; do not take the prose.** *Twenty-two `.tex` files differ and every difference examined so far runs
that way.*

---

## ⌗ THE MOVE THIS OPENS, AND NEITHER LINE COULD SEE IT

**The handoff's closing question (§7):**

> *"Either the construction contains a process that imprints the same acoustic phase on every mode —
> and it must act on modes already inside the sound horizon at the seam, because that is what
> `prop:subhorizon` leaves — or `PO-7` is a real disagreement between CR and the first peak's
> position."*

**Front #1 supplies a candidate they had no way to reach.** *The modes are provably **super-horizon
and frozen** at the branch point (c54.162, every $\ell$ from 28 to 2475). They are provably
**sub-horizon** at the onset (`prop:subhorizon`, by a factor $\gtrsim2$).* ⇒ ***So every observed mode
crosses the sound horizon somewhere between the branch point and the onset — and a crossing is
exactly the thing the handoff says the construction lacks, and exactly where ΛCDM's $k$-independent
shift is acquired.*** *The fork's transfer begins **at** $\eta_{\rm onset}$ with a reset, so whatever
phase is imprinted at that crossing is not in its calculation at all.*

**Two outcomes, and both are worth having.** *Either there is cosmic time between the branch point and
the onset in which the re-entry happens — in which case the missing universal shift has a home, and
`PO-7` moves; or the onset IS the first observable layer and the modes are handed over already
sub-horizon — in which case "frozen at the crossing" and "sub-horizon at onset" are two computed facts
with an uncomputed discontinuity between them, and **that** is the corpus's real gap on this front.*
⚠ *The fork already closed one escape from this: `FOLD`/L-117 shows putting the seam **earlier** does
not buy a universal shift — it removes the driving altogether ($Q_1 = 0.02$–$0.05$). So the answer is
not "move the seam."*

**The computation is cheap and is the recommended next step: for each observed $k$, locate the
sound-horizon crossing on the expansion leg and ask whether it falls before or after
$\eta_{\rm onset}$.** *No new instrument is needed for that, and it does not depend on any figure from
the fork.*
