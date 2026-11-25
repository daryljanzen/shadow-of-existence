---
kind: RESULT
revision: r7872
node: 60
order: r7871
---

# r7872 — THE SUM RESPONSE AT SPECTRUM LEVEL, AND THE BASIN IS IN THE EXPANSION RATE

**Registered first.** `PREDICTION.md` was committed and pushed before any computation of this
revision existed, with six reads declared and every arm written as a comparison with a reachable
negative. Two of those negatives were reachable and one of them fired: the order's named candidate
is **refuted in the form it was stated**, and that is reported here rather than reshaped.

---

## Ⓐ① THE SUM RESPONSE AT THE SPECTRUM LEVEL

### What was compared, and the one thing that had to be run rather than read

The order says the response is already in the banks. **The "on" side is; the "off" side was not**,
and two separate reasons each disqualify the landed bank from serving as it:

1. The landed bank carries **no `NUFD` key and no `MNU` key at all**. It predates the switch, which
   is `r7864`'s own recorded finding — *"the gate is that the key is ABSENT… these banks cannot say,
   and that is the finding."* Calling it "off" would be reading a state off provenance that the
   record itself refuses to state.
2. **And it would not isolate the switch even if it did.** That bank also carries no `BVEL` and no
   `FOURPI` key, so landed-against-separating changes more than one thing at once — which is the
   defect `r7869`'s whole fork existed to repair.

So the off arm was **run**: `gen_pol_nufd_off.sh` is `r7870`'s separating-grid generator with
`NUFD=1` replaced by `NUFD=0`, narrowed to the control arm and the four sums, so **exactly one
switch differs between the two banks**. Each point's own config is in the record: `NUFD` false at
every sum on the off arm, true at every non-zero sum on the on arm, `MNU` carrying the sum on both.

Both banks share the same 238 multipoles, `100` to `1996` in steps of `8`, **identical element for
element**, and each ratio divides by its **own** bank's `Σ = 0` point, so no number crosses banks.
`Dl(Σ)/Dl(0)` removes a constant amplitude, the units and `exp(-2τ)` exactly, which is why the order
asks at the spectrum level. CAMB is run here at the control's own centre with the **total** matter
held and `omch2` reduced by `omega_nu` — built the same way the instrument builds it — so the
comparison waits on nobody and quotes nothing.

⚠ **The instrument's banked TT/EE/TE are UNLENSED, so CAMB's unlensed leg is the like-for-like
one.** Both legs are computed and both are reported, so the choice is a measurement and not an
assumption.

### Ⓐ①ᵇ — DEPARTS, and with the repair on the departure is small and LOCALISED

Of 238 multipoles, the count exceeding the registered band of five parts in a thousand of `Dl(0)`:

| block | Σ = 0.06 | Σ = 0.30 | Σ = 0.60 | longest surviving run (on) |
|---|---|---|---|---|
| TT, repair **on** | **0** | 5 | 15 | `ℓ = 100–212` |
| TT, repair **off** | 47 | 190 | 211 | `ℓ = 100–420` |
| EE, repair **on** | **0** | 10 | 63 | `ℓ = 100–196` |
| EE, repair **off** | 128 | 203 | 220 | `ℓ = 988–1284` |

At `Σ = 0.06` the repaired instrument's TT and EE response is inside the band at **every one of the
238 multipoles** — the same few-parts-in-a-thousand band the background itself was verified to. The
worst discrepancies with the repair on are `0.0305` (TT) and `0.0159` (EE); with it off, `0.0838`
and `0.1581`.

**And what survives sits at the BOTTOM of the band.** TT's maximum discrepancy is **at `ℓ = 100`**
at both `Σ = 0.30` and `Σ = 0.60`, and the longest departing runs are `100–212` in TT and `100–196`
in EE.

⛭ **`ℓ = 100–212` is the range the lean was located in.** `r7869` recorded the 162-fold low-end
lean at **multipoles 100–207**. The surviving spectrum-level departure and the lean occupy the same
stretch of the band. *That is a coincidence of ranges between two independently measured things, and
it is reported as that and not as a mechanism.*

### Ⓐ①ᶜ — TOWARDS, in every block, on the like-for-like leg

Mean absolute discrepancy from CAMB's unlensed response, over the multipoles where either arm
departs:

| block | Σ | repair on | repair off | |
|---|---|---|---|---|
| TT | 0.06 / 0.30 / 0.60 | 0.00142 / 0.00088 / 0.00247 | 0.00635 / 0.01693 / 0.03099 | **towards**, by 4× to 19× |
| EE | 0.06 / 0.30 / 0.60 | 0.00221 / 0.00172 / 0.00372 | 0.00907 / 0.03607 / 0.06620 | **towards**, by 4× to 18× |
| TE | 0.06 / 0.30 / 0.60 | 0.0448 / 0.1912 / 0.3823 | 0.0635 / 0.2518 / 0.4964 | **towards** |

⇒ **The Fermi–Dirac repair moves the instrument TOWARDS CAMB at spectrum level in every block.**

⚠ **On the LENSED leg the verdict is MIXED and is reported as mixed.** TT and EE are still towards,
TE goes away. The registration fixed in advance that a mixed result is not to be resolved by
choosing a block, averaging them, or weighting them — *a direction that is not common does not
exist* — and it is not. The like-for-like leg is the unlensed one and its verdict is clean; the
lensed leg's mixedness is stated beside it rather than dropped.

### Ⓐ①ᵈ — the ℓ-dependence REFUTES the order's candidate in the form it was stated

The order names the candidate as two things: *the clustering matter loses `ω_ν` at all times, and
there is no free-streaming scale.* **The second half predicts a nearly ℓ-independent response.**
Measured, at `Σ = 0.60`:

| who | at `ℓ = 100` | at `ℓ = 1996` | top / bottom |
|---|---|---|---|
| instrument, repair on | `0.070234` | `0.022702` | **0.323** |
| instrument, repair off | `0.087086` | `0.006613` | 0.076 |
| CAMB unlensed | `0.039702` | `0.022404` | **0.564** |

The instrument's response is **more** strongly ℓ-dependent than CAMB's, not less — the opposite of
what a scale-free suppression would give. **So that half of the candidate is refuted in the form it
was stated**, and the registration required saying so.

**What the shape is instead:** a **low-ℓ excess that grows with the sum**. At `ℓ = 100` the
instrument returns `1.77×` CAMB's response at `Σ = 0.60` and `1.38×` at `Σ = 0.30`, while at
`ℓ = 1996` the two agree to about **one per cent** (`0.022702` against `0.022404`). That is
consistent with the **first** half of the candidate — a subtraction from the clustering matter
applied at *all* times, including the epochs where the species was still relativistic and should not
have been subtracted.

⛔ **It does not establish it.** A shape agreeing with a mechanism is not the mechanism, and this
revision claims no mechanism.

⌗ **And the low-ℓ departure is not a lensing artefact.** CAMB's two legs differ by `0.0002` at
`ℓ = 100`, against a departure of `0.0305` there — a factor of about 150. The choice of leg matters
at the top of the band and is irrelevant at the bottom, which is where the surviving departure is.

### ⚠ TE: the criterion is applied UNMOVED, its degeneracy named, and a second form reported beside it

The registered criterion is pointwise in `|Dl(0)|`, and TE crosses zero, so near a crossing the
threshold goes to zero with it. **The criterion was applied exactly as registered** and the
degeneracy counted: `5` multipoles sit under one per cent of the block's own RMS. But `|Dl_TE|` is
small over wide stretches, not only at the exact zeros, so **the TE ratio is not readable as a
percentage anywhere near a crossing** — its maximum values (up to `37`) are that degeneracy and not
a measurement. TE's *direction* verdict is still usable, because it compares two arms against the
same reference at the same multipoles; its *size* is not.

**So the second form registered to sit beside it was computed**: each side's response normalised by
**its own** block RMS of `Dl(0)`, which stays amplitude-free (a constant amplitude cancels against
its own RMS) and stays finite straight through a crossing. ⚠ *This is a reading. The registered
verdicts above are read off the pointwise form and are not restated from this one.* Departing counts
of 238, against the same band, on the unlensed leg:

| block | Σ = 0.06 | Σ = 0.30 | Σ = 0.60 | longest surviving run (on) |
|---|---|---|---|---|
| TT, repair **on** | **0** | 8 | 23 | `ℓ = 100–276` |
| EE, repair **on** | **0** | **0** | 15 | `ℓ = 1100–1140` |
| TE, repair **on** | 21 | **0** | 72 | `ℓ = 188–308` |
| TT / EE / TE, repair **off** | 8 / 100 / 147 | 134 / 185 / 223 | 178 / 194 / 229 | — |

**It says the same thing without the TE pathology, and says it more cleanly.** TE at `Σ = 0.30` goes
to **zero** departing multipoles under this form, so the wide TE departure the pointwise form
reported there was the criterion's degeneracy and not the instrument's. TT's surviving runs are
`100–156` at `Σ = 0.30` and `100–276` at `Σ = 0.60` — the bottom of the band on both forms — and
TE's at `Σ = 0.60` is `188–308`, the bottom again. **EE is inside the band at every multipole at
both `0.06` and `0.30`.**

---

## Ⓑ② THE LOWER BASIN'S DIRECTION

### Ⓑ②ᵃ — ONE DIRECTION, and it is the expansion rate

Both of `r7870`'s recorded vectors were pushed through the instrument's **own** parameter map, not
read off a slot index — the guard being that before two stretches are identified by a label, the
label's many-to-oneness has to be checked on the object. The map returns `H0`, `OM`, `WB`, `NS` and
the sum; the fifth component of each vector is `τ`, which the profiler holds separately.

| parameter | lower basin | higher basin | separation | grid steps |
|---|---|---|---|---|
| `H0` | `65.292248` | `68.594396` | `+3.302` km/s/Mpc | **1.6511** |
| `OM` | `0.315117` | `0.314781` | `-0.000334` | 0.0223 |
| `WB` | `0.0224001` | `0.0224003` | `+2.3e-07` | 0.0003 |
| `NS` | `0.965068` | `0.965277` | `+0.000209` | 0.0104 |
| `τ` (held) | `0.0540000` | `0.0540000` | `-3.5e-09` | — |

The registered criterion — largest above one step, every other below a tenth — holds with room to
spare: the largest is **74 times** the next largest. **The basins are separated in `H0` alone.**

### Ⓑ②ᵃ′ — and there IS a barrier, so the word survives its own test

Two vectors with different `χ²` are two minima only if something sits between them. On the straight
segment joining them at `Σ = 0.400`, in 81 steps, the `χ²` rises to **`2193.8672` at `t = 0.5875`** —
`7.6718` above the **higher** end (`2186.1954`) and `20.2085` above the lower (`2173.6587`).

⇒ **A barrier. They are two minima and not one reported twice**, and `r7870`'s word for them is now
established rather than asserted.

### Ⓑ②ᵇ — UNESTABLISHED, and routed

`cc66`'s committed `r7869` record carries each ruler's fitted `H0` and **nothing that decomposes a
branch by parameter** — no key in it names a branch or a basin at all. So whether the reference
branches along `H0` is **not answered from that record**, and the order's own summary of that
measurement is not the measurement. The question is routed with what would settle it.

---

## TWO ADDITIONAL READINGS, BOTH UNREGISTERED AND LABELLED AS SUCH

Neither is in `PREDICTION.md`, neither has a criterion registered in advance, and **no registered
verdict above rests on either.**

1. **The barrier is on BOTH rungs, and it is LARGER without the offset.** Asked of the same two
   vectors on the no-offset rung: ends `2201.3554` and `2214.6605`, interior maximum `2237.5225` at
   `t = 0.5625` — **`22.8620`** above the higher end, against `7.6718` at `+0.044`. ⇒ The
   bimodality in `H0` is **not the `N_eff` offset's**; it is there on both backgrounds.
2. **Both of the reference's fitted solutions sit in the UPPER branch.** Its two rulers fit
   `H0 = 68.625` and `68.199`, which are `+0.030` and `-0.396` from the instrument's higher basin and
   `+3.333` and `+2.906` from the lower. ⇒ That says **where its fits are**, and **not** that it has
   no second one. The distinction is the whole of Ⓑ②ᵇ's verdict and is not blurred here.

---

## WHAT THIS REVISION DID NOT DO, named so the absences are decisions

- **No limit is read and no envelope crossing appears in this record at all.** The order's own
  ruling stands: a crossing is a lower envelope over the basins reached and never a limit.
- **The arm of record was not re-run.** The order puts it behind ①, and it stays there.
- **No mechanism is claimed.** Ⓐ①ᵈ refutes half the candidate and is consistent with the other
  half; consistency is not establishment.
- **The mechanism of the low-end lean stays carried**, as it has since `r7869`.
- **No other seat's receipt was edited.** `r7869`'s conversion of the one-rate census to a property
  means no census routing was owed this revision, and none was made.

## THREE THINGS IN THIS RECORD ARE THIS SEAT'S OWN

1. **The off arm nearly was not run.** The order said the response was already in the banks, and
   reading the landed bank as "off" would have been the quick path. It is the bank's own *missing*
   keys that forbid it — and the second reason, that it differs in more than one switch, is the one
   that would have made the comparison answer a different question without ever looking wrong.
2. **The order's candidate came back half refuted, and the half that failed is the one the order
   leaned on most.** Reporting that was the point of registering the ℓ-dependence as a measurement
   rather than as a diagnosis.
3. **TE's criterion is unusable for size and was kept anyway.** Swapping it after seeing the
   numbers would have been the defect this line lints for. Naming the degeneracy and computing the
   second form beside it is the repair — and the second form then *vindicated* the worry, taking
   TE's departure at `Σ = 0.30` from `119` multipoles to `0`. **A criterion kept unmoved and a
   reading added is what let that be visible at all**; a criterion quietly swapped would have
   reported the better number as the registered one.
