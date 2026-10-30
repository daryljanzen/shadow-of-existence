# `r7642` (60) — LAYER 2 REACHES THE REGISTERED NEGATIVE, AND TWO OF THE FOUR DIFFERENCES ARE A SWITCH THAT REACHED ONE PATH AND NOT ANOTHER

**Receipt:** `layer2.py` in this directory — **23 of the 24 read.** **Registered:** `PREDICTION.md`, its own commit, with the
Layer-2 negative inherited from `r7640`'s arm ④ rather than re-registered.
**Order:** `r7641` (69) — Layer 2 on the 24 the instrument will build, and the two `P10` cubics the
nightly's cap killed.

## ⚑ THE REGISTERED NEGATIVE IS REACHED

`r7639`'s words, carried by `r7640`'s arm ④ and confirmed standing by `r7641`: *one or more of the 36
besides `r6885_dp0` differs from its namesake under its own configuration by more than `1e-11`.*
**It does. Four files differ, three of them new.**

| | reading | what it means |
|---|---|---|
| **the arm's alone** | **19 of the 23 read**: 9 **bit-identical**, 10 within `1e-11` (worst 1.7e-14) — one of the nine a pair that carries no spectrum at all and is bit-identical across every one of the 26 arrays it does carry | the bank's old → new diff for these carries nothing but the arm move |
| **over** | `r6885_dp0_cr` 6.13e-01 · `r6784_cr_crossing_los` 2.21e-01 · `r6794_cr_crossing_kcont_summed` 1.61e-08 · `r6784_cr_crossing_hier_noCRIC` 1.63e-09 | the diff carries an instrument change too |

## ⚑ TWO OF THE FOUR ARE NAMED, AND BOTH ARE PROVED BY A BIT-IDENTITY

Both have the **same shape**, and it is the shape the instrument's own source already names for a third
switch: ***a switch reached one path of three.***

**ⓐ `r6885_dp0_cr` — the Doppler-dipole switch did not reach the hierarchy path.**
- Its namesake is **bit-identical** to the namesake of the *same command with the switch absent*, and
  bit-identical to **today's** run of that switch-free command. ⇒ the switch did nothing at its build,
  and what moved is the switch and not the rest of the instrument.
- Today that switch changes the same spectrum by **6.129e-01** — the whole of the measured difference.
- ⛭ **The control says it is the path and not the switch:** on the **line-of-sight** path the same
  switch was already live at the build and is live now, to the same figure — **6.178e-01 then,
  6.178e-01 now.**
- ⇒ And the instrument's source **names the commit**: *`_SWSRC` and `_DPSRC` wired here at
  `r6889+cc66.36`*, with the note recording the very measurement this census reproduced — *"`DPSRC=0`
  there returned a BIT-IDENTICAL spectrum on both arms (`r6885+cc66.35`)."*

**ⓑ `r6784_cr_crossing_los` — the initial-condition switch did not reach the line-of-sight path.**
- Its namesake is **bit-identical** to today's run of its own command **with `CRIC` removed**, while
  its command *with* `CRIC` misses the namesake by **2.206e-01**.
- ⛭ **The control is its own group's hierarchy member**, which carries the same switch and reproduces
  at **2.334e-15** ⇒ the switch was live *there* at the build.
- ⇒ And the switch's **action** did not change at all: with against without, on the path that had it,
  is **2.069e-01 then and 2.069e-01 now**. **What changed is its REACH.**

**⇒ THE CONSEQUENCE FOR THE BANK, IN BOTH CASES.** The banked namesake is a run of the command
**without** the switch its name claims. So its old → new diff carries that switch's whole effect on
top of the arm move — and the file is mislabelled, not merely stale. The receipts that read each are
located and listed below.

## ⌗ TWO ARE MEASURED AND NOT NAMED, SAID RATHER THAN LEFT OUT

`r6784_cr_crossing_hier_noCRIC` (1.631e-09) and `r6794_cr_crossing_kcont_summed` (1.607e-08) sit on
the **one path-and-switch combination the two findings do not cover** — the hierarchy path with the
initial-condition switch unset. Both are small. **The search, named:** the three switches the two
findings implicate were each tested against their own controls above; the instrument's source carries
no note with a revision after `r6784` describing a change to the hierarchy's CR handover; and the
clone is shallow, so history cannot be asked. ⚠ And `r6794`'s namesake **cannot be reproduced by one
run of its command at all** — its mode count is reached by slicing and summing, so for that file the
recorded command is not the recorded run, and the note saying so is carried beside the number rather
than behind it.

## ⌗ WHAT LAYER 2 SETTLED THAT LAYER 1 COULD ONLY INDICATE

- **Both of `r7640`'s recovered commands are confirmed on the spectrum.** The entry the bank marked
  *"digits unrecorded"* rebuilds **bit-identical** at the four figures quoted beside that phrase, and
  the entry marked *"none recorded, ⚠ low confidence"* rebuilds **bit-identical** too. A background
  match leaves the solver and the source free; a bit-identical spectrum does not.
- **`r7640`'s `LEAFSCALES` correction is settled where it can be settled, now on two members.** Both
  `cc66_cr_x_h686_pol` and `cc66_cr_x_h686_L2000` are **bit-identical** at the value the namesakes
  chose, against the value `MANIFEST_old.json`'s `held` prose claims for them.
- **One of the 36 is not a spectrum on either side.** `r6959_eta_cr`'s namesake carries 28 keys and
  neither of the two the comparison needs: it is the source-weight save. Compared on the 26 arrays the
  pair shares, **all 26 are bit-identical.**

## ⛔ THREE CORRECTIONS AGAINST THIS LINE, ALL THE SAME MISTAKE IN DIFFERENT SIZES

All three are *the right arrays under the wrong name* — the confusion this census exists to catch.
- The switch that writes the source-weight save is a **path, not a flag**, so the first attempt wrote
  the right arrays to a file named after the flag value and left the comparison pointing at a spectrum
  the namesake does not have.
- That writer emits no resolved-switch key, so the check that every rebuild ran at its claimed command
  had to read **that file's own recorded fields** instead — path, leaf scaling, taper, slicing. All
  four check out.
- ⚠ And the first form of that comparison **would have passed vacuously on a perfect match**: it
  tracked the worst reading upward from a floor of zero, and a set of all-zero readings never rose
  above it. Corrected to take the maximum over the readings and to require that at least twenty were
  taken. *A guard that cannot fail on the data it is given is not a guard, and this one was found by
  the data being perfect rather than by the guard being read.*

## ⚠ WHAT IS NOT CLAIMED

- Not that the four over the threshold are the only ones. **Arm ⑥ is a HIT and this is its
  measurement: the 24 do not all complete in this container.** `r6941_fine_cr` — the finest multipole
  step in the set, `LSTEP=1` against `8` for its nine siblings at the same point — was given **6000 s,
  exceeded it, and wrote no file**, having reached three quarters of its mode batches. It is named here
  with that cost rather than implied either way, and a longer attempt is running. ⌗ *The 23 that did
  complete cost 639 s at the cheapest and 4446 s at the dearest, one thread each, several at a time —
  which is why they were run that way rather than serially.*
- Not that the twelve the instrument refuses are covered. `r7640` established that they cannot be read
  at all, and nothing here changes it.
- No paper is edited, no figure moves, and no receipt belonging to another seat is touched. The
  corrections to the bank's records are **routed** with their measurements.
