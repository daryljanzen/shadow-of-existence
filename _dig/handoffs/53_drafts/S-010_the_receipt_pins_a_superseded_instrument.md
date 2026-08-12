---
name: s-010-stale-pin
kind: FINDING (draft, uncommitted) — supersedes my own first diagnosis, which was wrong
current: r2428 / c54.178
job: P15_two_arm_control_and_guard.py pins its control and CR figures from the c54.168 instrument. The instrument was rebuilt at c54.178 — baryons split at their own contrast, photon fluid replaced by a Boltzmann hierarchy with polarisation — and both pinned sets have moved. The receipt passes because it checks its own constants, and its stated drift-detector watches the one layer that did not move.
sources: [chat]
---

# S-010 · THE RECEIPT PINS A SUPERSEDED INSTRUMENT — AND WATCHES THE WRONG LAYER FOR DRIFT

> ## ⛔ FIRST, THE DIAGNOSIS I HAD AND WITHDREW
>
> **My first draft said the sampling guard's `>= 4.0` threshold was too loose and that the pinned
> 224 was an under-sampled reading.** *That was a good story and it is false.* **Run at 4.2 points
> per Bessel period — barely clearing the guard — the current instrument gives 220/532/812/1116,
> identical to 10.2 and to 20.5.** *Three samplings spanning a factor of five, one answer.*
> ⇒ ***The control is converged at the threshold. The guard is fine. I was wrong, and the run that
> discriminated took four minutes.***

---

## WHAT IS ACTUALLY THE CASE

| | pinned in the receipt | **current instrument, this container** |
|---|---|---|
| **ΛCDM control** | `CTRL = (224, 536, 808, 1116)` · ℓ₁/l_A **0.7433** | **220 / 532 / 812 / 1116** · ℓ₁/l_A **0.7300** |
| **CR, discrete ladder** | `CR_DISCRETE = (172, 396, 624, 904)` | **172 / 396 / 628 / 908** |
| **CR, continuum `KCONT=1`** | `CR_CONTINUUM = (172, 396, 624, 904)` | **172 / 396 / 628 / 908** |

**Every figure reproduced at two or more independent samplings:**

| arm | pts / Bessel period | peaks | ℓ₁/l_A |
|---|---|---|---|
| ΛCDM `NK=290` | 4.2 | 220/532/812/1116 | 0.7300 |
| ΛCDM `NK=700` | 10.2 | 220/532/812/1116 | 0.7300 |
| ΛCDM `NK=1400` | 20.5 | 220/532/812/1116 | 0.7300 |
| CR `NK=260` discrete | 2.3 | 172/396/628/908 | 0.5703 |
| CR `NK=1200` `KCONT=1` | 17.6 | 172/396/628/908 | 0.5703 |

## THE CAUSE: THE INSTRUMENT WAS REBUILT UNDER THE PIN

**The receipt says `Built r2376+c54.168`. `ACOUSTIC_two_arm.py` now carries c54.178 work:**

- `BSPLIT` — *"baryons at their **OWN** contrast (c54.178)"*; *"**THE MATTER SECTOR IS SPLIT INTO
  BARYONS AND CDM AT c54.178.** Until now it was ONE fluid"*;
- *"**THE PHOTON BOLTZMANN HIERARCHY WITH POLARISATION** (r2376+c54.178) — **what this replaces**:
  until now the photons were a two-moment **FLUID**"*;
- *"the baryons enter the potential at **their own contrast** (c54.178)"*.

⇒ **The pinned numbers are the fluid instrument's. The file is now the hierarchy instrument.**

## ⚠ AND THE RECEIPT'S OWN DRIFT-DETECTOR WATCHES THE LAYER THAT DID NOT MOVE

The receipt states its guard against exactly this:

> *"FIGURES PINNED BELOW are produced by `ACOUSTIC_two_arm.py`; the four runs cost several minutes
> each and are not re-run here. **What IS recomputed is every background quantity they rest on, which
> is cheap and is where a drift would show first.**"*

⛔ **The background did not drift.** D_M = 13005, r_s = 135.46, l_A = 301.6 on the CR arm and
D_M = 13865, r_s = 144.53, l_A = 301.4 on the control — **identical to the receipt's own values.**
**What changed is the perturbation machinery**, which the receipt does not recompute.

⇒ ***The drift showed exactly where the detector was not pointed, and the reasoning that placed it —
"the background is where a drift would show first" — is what made the blind spot.*** *It is a
sensible prior and it was wrong here for a specific reason: a fluid→hierarchy rebuild changes the
source, not the background it rides.*

⌗ **So this is the corpus's own class, one notch in.** *`THE_HUB` lists among the semantic defects git
cannot catch:* **"95 receipts that ran green and could not fail."** *This one **can** fail — it has
real assertions and a real gate — but it checks **its own constants**, so it stays green while the
instrument that produced them is replaced beneath it.* **A pinned figure is a claim with a
freshness date, and nothing here carries one.**

---

## ⇒ WHAT CHANGES, AND MOST OF IT IS AN IMPROVEMENT

1. **Re-pin both sets against the c54.178 instrument:** `CTRL = (220, 532, 812, 1116)`,
   `CR_DISCRETE = CR_CONTINUUM = (172, 396, 628, 908)`.
2. **The control's position floor improves by a factor of ten: 1.66% → 0.16%.** *The receipt's
   headline —* **"a 23% deficit against a 1.7% floor, a factor of fourteen in margin"** *— becomes a
   factor of ~140.* **The CR deficit is untouched in size and direction: ℓ₁/l_A = 0.5703 both before
   and after, on the nose.**
3. **The heights do not improve and should not be quoted as if they had:** converged P1/P2 = 2.447
   against the sky's 2.217 (**10.4%**), P1/P3 = 2.974 against 2.277 (**30.6%**). *PART 2's "no height
   claim below ~25%" stands and is the honest line.*
4. **⚠ The documented invocation still does not run.** `ARM=lcdm python3 ACOUSTIC_two_arm.py`
   — the Usage block's own control line — gives 3.8 points per period against a threshold of 4.0 and
   **exits 1**. *Independent of everything above; five percent short.* **Name an NK in the Usage
   block.** *(`NK=290` suffices and costs two minutes.)*
5. **A general one, offered rather than asserted:** *a receipt that pins figures from an instrument it
   does not re-run should record **the instrument revision the pin was taken at**, so a later reader
   can tell a stale pin from a live one without re-running anything.* **This receipt names its own
   build (`c54.168`) in its header, which is what made the diagnosis possible — it is one field short
   of self-checking.**

---

## ⌗ AND WHAT THIS DOES NOT TOUCH

**The receipt's physics conclusions all survive.** The guard still passes on both arms; the control
still lands on the sky; the CR arm's 23% first-peak deficit is unchanged to four figures. **What is
stale is three of the twelve pinned integers and one derived percentage** — *and the percentage moves
the receipt's way.*

⌗ *Every figure above is from a log kept beside this note: `twoarm_lcdm_nk290.log`,
`twoarm_lcdm_nk700.log`, `twoarm_lcdm_nk1400.log`, `twoarm_cr.log`, `twoarm_cr_conv.log`.*
