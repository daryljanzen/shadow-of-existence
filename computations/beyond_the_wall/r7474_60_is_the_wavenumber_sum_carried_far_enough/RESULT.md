# r7474 — THE EXCESS IS NOT THE WAVENUMBER SUM'S, AND THE MARGIN IS NARROWER THAN IT LOOKS

**THE ORDER** (`r7471`): settle whether the kernel's acceptance in wavenumber is what this background
requires, or whether the wavenumber sum on this arm is not carried far enough to say.

**THE ANSWER.** On the one **matched** ladder-against-continuum pair in the bank — same angular
scale, same `ℓ` grid, same reported reach, spectra agreeing to `3.4×10⁻⁵` — **the contrast statistic
does not move at all: `−0.00000` to five decimals.** The reach is twice the highest reported
multipole where the banked height ratios converge by half that. ⇒ **The excess is not the sum's, and
by the order's own reading the acceptance belongs to the background** — with the default reading it
names standing: *the model does not yet do what CR requires of the projection, not that the sky has
ruled.*

**⚠ AND THE MARGIN IS NARROWER THAN THAT SOUNDS, which is the part worth carrying forward.** A
control resampled **below** the instrument's own projection guard moves the statistic by **`+0.0334`**
— **`74` per cent of the `0.045` excess.** The banked runs pass that guard at `5.7` points per
Bessel period, so the excess survives; but it survives *because the guard is doing real work*, not
because the statistic is insensitive to sampling. **The guard's own waiver for this arm — "only not
aliasing if the answer does not depend on it" — is what the matched pair now certifies, for this
statistic, for the first time.**

**⌗ AND THE COVERAGE QUALIFICATION, PREDICTED IN ADVANCE AND CONFIRMED.** **No banked projected
continuum run sits at the configuration the excess is measured in.** Of the four continuum files,
three are projected at *different* configurations and the one at the excess's own angular scale is
the **source** side. ⇒ So the convergence evidence for the statistic is transferred from a matched
pair at another configuration, and that transfer is an assumption, stated here rather than hidden.

---

## ⌈ THE THREE DEFECTS, ALL FOUND BY RUNNING, ALL THE SAME GUARD

**⛔ ① A PAIR THAT SHARES A FILE STEM AND IS NOT A PAIR.** `c54.186_cr_KCONT` against
`c54.186_cr_L3000` looks like the matched continuum twin and is not: the ladder run reports to
`ℓ 2996` on `363` points and the continuum one to `ℓ 1996` on `238`. Since `k_max = KFAC·LMAXL/D_M`,
**a different reported reach IS a different `k_max`** — their spectra differ by `1.6` per cent at the
median and `57` at the ninetieth percentile, against a banked `χ²` difference of `0.001` for the
continuum change alone. ⇒ **Arm `Ⓐ` is WITHDRAWN as a measurement** (it read `+0.00061`) and kept as
the record. *A comparison that moves two things answers about neither.*

**⛔ ② AND THE COVERAGE ARM MATCHED CONFIGURATIONS BY `ℓ_A`.** Within `0.5`, which admitted
`c54.186_cr_KCONT` at `301.600` as being "at" the refit minimum's `301.799`. **Their contrast
statistics are `−0.41` and `+1.045`** — they differ by `1.5` on a quantity of order `1`. ⇒ **`ℓ_A` is
not a configuration label**; it is many-to-one on the object. Repaired to ask what the file *is*.

**⛔ ③ AND THE THIRD WAS IN THE LANDING OF THIS RECEIPT'S OWN INDEX ROW.** The first append was
written to the **line number** that row occupied an hour earlier, and it landed on **another seat's
row**, because the trunk had inserted rows above it in the meantime. Reverted and redone by locating
the row by its receipt name. ⌗ *Nothing reached the trunk; the defect is recorded because it was made
and not because it survived.*

⇒ ***ALL THREE ARE THE REGISTERED GUARD — "before two stretches are identified by a label, check how
many-to-one the label is on the object" — firing three times in one revision on three different
labels: a file stem, an angular scale, and a line number. And the third fired on the seat that had
just written the other two up, inside the same hour, in the act of recording them.*** *The guard is
not hard to state. It is hard to remember while doing something else.*

---

## ⌈ THE CONTROLS AND THE SCORECARD

**Ⓥ① SAME INSTRUMENT — PASS.** The imported statistic reproduces all four of `r7093`'s printed rows,
worst difference `3.0×10⁻⁵`. *Loaded from that file by `ast`, so its own printing does not run.*
**Ⓥ② THE NULL — PASS**, a file against itself returning `1.000000000000` on all three numbers.
**Ⓥ③ REAL PERTURBATIONS — PASS**, every pair differing in the spectrum itself.

| arm | predicted | measured | |
|---|---|---|---|
| `Ⓐ` model `A`, ladder → continuum | `|d| < 0.01` | `+0.00061`, **pair not matched** | **WITHDRAWN** |
| `Ⓑ` the matched crossing pair | `|d| < 0.01` | `−0.00000` | **HIT** |
| `Ⓒ` the guard-failing control | `0.01 ≤ |d| ≤ 0.10` | `+0.03342` | **HIT** |
| `Ⓔ` the coverage | no projected continuum at the excess | `0` of `4` | **HIT** |
| `Ⓘ` the verdict | the excess is not the sum's | confirmed, with the margin stated | **HIT** |

*⌗ `r7462` recorded a line number going stale under another seat's edit and called it "a measurement
with a date on it." **`r7474` then used one as an identity.** The two are the same lesson at two
distances, and the second is the worse of them.*

**Four hits and one withdrawal**, and the withdrawal is this revision's own arm rather than anyone
else's claim. ⌗ *One registered prediction that deserves naming: `Ⓒ` was registered as a bound of
`0.01`–`0.10` because the guard-failing spectrum visibly aliases, and it landed at `0.033` — so the
bound was right and its CONSEQUENCE was not foreseen: `0.033` against an excess of `0.045` is a
margin, not a clearance.*

**THE PRICE:** `0.22`, `0.24`, `0.25` s — **no new spectrum, nothing refitted**, which is what the
order's instrument freeze requires. ⌗ `PO-87`'s fourth-peak half is data-gated and untouched.
**The row is the register's: supplied, not applied.**

---

*`PREDICTION.md` registered `a3ee7f7f` at `1f20bd2d`, before `kconv.py` existed. The seed is pinned
per `L-249`'s repair rule.*
