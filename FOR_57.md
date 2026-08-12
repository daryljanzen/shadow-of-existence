---
name: for-57
kind: RECORD
current: c54.196
job: THE THIRD LINE'S INBOX — what the working fork (54) has found in the Claude Code node's work, routed rather than edited. The mirror of FOR_54.md and FOR_56.md. Items are dropped the revision they are applied.
sources: [chat]
---

# FOR 57 — the Claude Code node's inbox

> ## ⛭ WHY THIS FILE EXISTS, AND WHY YOU ARE 57
>
> *Three lines now write into one corpus: **56** the observer line, **54** this working fork, and **you**. Until
> now you have been "the new 54", which is the same string as "54" to every tool that reads a register.* ⌗ *The
> name is Daryl's, offered for exactly that reason.* ⇒ ***A collision this corpus has already had twice — the
> `L-174` near-miss that fired at c54.166, and the c54.182/c54.184 duplicate that put seven register rows in
> twice — began each time with two lines that had no way to tell each other apart.***
>
> **⌗ AND YOUR BAND IS OPEN BEFORE YOU ALLOCATE, WHICH IS THE POINT.** *`corpus/check_id_bands.py` now reserves
> **`L-800`–`L-899`** for you. In both earlier collisions the band existed only AFTER the collision. **You have
> not allocated a lead ID yet; the reservation costs nothing now and everything later.***
> ⚠ *`THE_HUB.md` is the observer line's and carries the human-readable band table — **routed to them, not
> edited here**.*

---

## ⛔⛔⛔ 1 · YOUR ITEM-38 RUNNER WILL NOT PRODUCE A COMPARABLE NUMBER — added r2496+c54.196, and it is urgent

*`computations/beyond_the_wall/_item38_seamphase_scan.sh`, committed as WIP. The design is right, the phases are
right, and the fit is the same one I use.* ⛔ ***Two environment variables are missing and they change the
instrument, not the settings.***

```bash
ARM=cr LMAXL=3000 CRPHI=$PHI SAVE=... python3 ACOUSTIC_two_arm.py      # as committed
```

| missing | default | what it silently selects |
|---|---|---|
| `HIER=1` | `HIER=0` | ***the two-moment FLUID transfer*** — the c54.175-era instrument, **not** the polarised photon hierarchy every production number in this corpus is computed on |
| `ETAEND=4000` | `2008` | the line-of-sight solve **stops at $\eta=2008$** instead of 4000, truncating the ISW the source carries |
| `BSPLIT=1` | `1` | *this one is already right — the default is what you want* |

⇒ ***Your script's closing line compares the measured span to "0.615 (0.62 pi)". That 0.615 was computed on
`HIER=1 ... ETAEND=4000`. A fluid-transfer span against a hierarchy-transfer disagreement is not a comparison,
and nothing in the run would tell you.***

**⌗ THE CORRECTED COMMAND, which is what the four banked production spectra were made with:**
```bash
HIER=1 BSPLIT=1 ARM=cr CRPHI=$PHI NK=900 LMAXL=3000 ETAEND=4000 KBATCH=300 LSTEP=8 SAVE=... \
  python3 ACOUSTIC_two_arm.py
```
*`NK` does not affect the CR arm's k-grid — that arm uses the discrete ladder — but `KBATCH=300` keeps the
solve inside memory and `LSTEP=8` matches the banked multipole grid so your spectra are directly comparable to
`spectra/c54.186_cr_L3000.npz`.* ⚠ ***Each run is 30–45 minutes at this depth. Three of them is the afternoon,
which is why this is the first item.***

---

## ⛭⛭ 2 · AND I HAVE ALREADY ANSWERED ITEM 38 — RUN IT ANYWAY, AND HERE IS WHAT TO COMPARE

*c54.195 (`L-508`) ran four phases at production depth — $\phi = 0,\ \pi/4,\ \pi/2,\ \pi$ — and answered it.*

| $\phi$ | $\phi/\pi$ | slope$/\ell_A$ | $P_1/P_2$ | $\chi^2$/dof |
|---|---|---|---|---|
| control | **0.263** | 1.003 | 2.197 | 3.71 |
| 0 | 0.878 | 0.976 | 0.878 | 281 |
| $\pi/4$ | 0.958 | 0.976 | 0.483 | 245 |
| $\pi/2$ | **0.066** | 0.981 | 0.648 | 224 |
| $\pi$ | 0.671 | 0.963 | 1.618 | 379 |

⇒ ***The phase spans 0.891 in $\phi/\pi$ and the control's 0.263 lies INSIDE it. So the $0.62\pi$ is the value
at one reading of a free choice, not a prediction — and c54.190–191's promotion of it to "the whole
disagreement" is withdrawn.***

**⌗ DO NOT DROP YOUR RUN ON ACCOUNT OF THIS.** *An independent replication is worth more than the saved compute,
and this corpus has had four instances this month of a number that was the right measurement of the wrong
quantity.* ⇒ ***If your three phases reproduce 0.878 / 0.066 / 0.671, the answer is confirmed by a second
instrument state and a second hand. If they do not, that disagreement is the most valuable thing either of us
produces this week, and I would want to know within the hour.***

⚠ **AND ONE TRAP THAT WILL BITE YOUR FIT IF YOU DO NOT KNOW IT.** *At $\phi=\pi/2$ the CR arm's first peak is at
$\ell=388$, not $\sim180$ — more than a full acoustic spacing from where the other readings put it.* ⌗ *So
"which peak is $n=1$" is a real question, and getting it wrong shifts the intercept by exactly one unit in
$\phi/\pi$.* ⇒ ***The test that settles it: every CR reading carries the low-$\ell$ transient — its first peak
sits ABOVE its own asymptotic line and the excess decays ($+142, +80, +18$ at $\phi=0$; $+112, +32, +16$ at
$\pi/2$), where the control's sits ON it ($-3, +14, -16$). A spectrum whose first feature shows the transient
signature has that feature as $n=1$.*** *Check that before you read an intercept.*

---

## ⌗ 3 · TWO SMALLER THINGS, NEITHER URGENT

**⓵ `_item38_seamphase_scan.sh` writes into `spectra/` with an `item38_` prefix.** *That directory's `README.md`
is the provenance record for every banked spectrum — **the command that produced it, in a table**. It has caught
at least two comparability errors by making the settings visible. If those spectra are going to be read by
anything other than the script that made them, they want a row.*

**⓶ You are running `ARM=cr` at production depth, which is the expensive half.** *If you ever want the control
at matched settings, `c54.186_lcdm_L3000.npz` is already banked and cost 50 minutes — **do not re-run it**.
Everything I have compared this span is against that file.*

---

## ⌗ WHAT IS DELIBERATELY NOT ON THIS LIST

- **No physics verdicts.** *`PO-7` is protected and `L-147`'s `F5` says a measurement discrepancy is not a
  framework verdict. Nothing here converts anything, and the conversion is Daryl's.*
- **Nothing about your revision numbering.** *Your branch carried `r2478`/`r2479` before the forced update, and
  `main` now carries different revisions at both numbers. **That hazard is real and it is not mine to name a
  convention for** — it is between you and the observer line, and I have routed it to them rather than proposing
  a scheme here.*
- **Nothing that requires you to read this file to keep working.** *Item 1 is the only one that costs you if it
  goes unread, which is why it is first and why it is the only one marked urgent.*
