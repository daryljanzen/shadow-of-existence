# `r6929+cc66.44` — the comb's resolution, measured before it decides anything

*`r6929`'s order: **`cc66.43` made the comb the load-bearing reading** — it is the one with an
external referent, and it supports the assignment the instrument has. ⚠ **But the corpus has never
measured how sharply it discriminates**, and a reading promoted to arbiter needs its resolution
stated. So: let the weighting on $\tau$ run from the stacking clock to the leaf's through a
one-parameter family — `VISLEAF` as a **fraction** rather than a flag — and report, against that
parameter, $\ell_1/\ell_A$ against the sky's $0.7312$, the retained fraction and its $q$-slope, and
$\mathrm dr_s/\mathrm d\chi$.*

## What is in here

| script | what it runs | why |
|---|---|---|
| `geom.py` | the **background** half over fifteen values of $f$ on **both** arms — $\eta_{\rm LS}$, the FWHM, $r_D$, $\ell_A$, $r_s(\eta_{\rm LS})$ on both clocks, $\mathrm dr_s/\mathrm d\chi$ | it is all module-level, so the scan is thirty imports and no solver. ⚑ *And $\ell_A$ is what separates the order's own guard: if the comb moved only because the visibility peak relocates, $\ell_1$ would follow $\pi D_M/r_s(\eta_{\rm LS})$* |
| `launch.sh` | the **comb** half: the arm's real spectrum and its **injection** at $f = 0,\,0.1,\,0.25,\,0.5,\,0.75,\,1$, `HIER=1 LSTEP=8 LMAXL=2000` in `KSLICE` pieces of 250 — plus the gates | the injection is a $\cos(k r_s)$ source with **no plasma dynamics in it**, so it carries geometry and visibility weighting only: if its comb moves with $f$ and the real one moves with it, the motion is the visibility's; if the real one moves further, the extra is the plasma's own phase |
| `bank.py` | folds the slices into `spectra/r6929_scan_cr.npz` and the gates into `r6929_noop.npz` | ⚠ `inj_*` and `comb_*` under separate keys: the first is the projection's transfer of a known input and is **not** a spectrum of the model |

**The control is not scanned, and that is a gate rather than an assumption.** `Jac ≡ 1` there by the
rate identity, so every $f$ is the same run — `noop_lcdm_f050` against `noop_lcdm_f0`.

**And $f=1$ is re-run under the new code and gated bit-identical against `r6925`'s banked
`VISLEAF=1`.** The family's endpoint must *be* the flag; `1 + 1\cdot(\mathrm{Jac}-1)` is not
`Jac` in floating point, so the endpoint takes the r6925 expression unchanged and the identity is
checked rather than assumed.

## ⛭⛭ The switch guard is now standing, not per-launcher

*`r6925`'s launcher dropped its extra environment through a positional-argument bug and **thirty-six
slices ran as plain `VISLEAF=0`** — they completed, reported nothing wrong, and reproduced the banked
spectra, which is exactly the shape that gets banked as an answer.* 66's instruction was that the fix
should be standing: **any switch whose effect is a bit-difference should print a marker and its
launcher should fail if the marker is absent.**

⇒ The instrument prints a `__SWITCHES__` line naming every switch present in its environment, and the
**inventory is read off its own source** rather than hand-maintained — `r3512`'s flag inventory was
wider than the code, and a list derived from the `os.environ` reads themselves cannot drift from them.
So `VISLEAFF=1` is *absent* from the marker and fails the guard instead of running silently.

* `../switch_smoke.sh NAME=VAL …` — imports the instrument with that environment and asserts every
  assignment appears in the marker. One import, no solver, no projection.
* `launch.sh` smoke-tests **every distinct environment before the set goes out**, and then checks
  **every slice's own log** for the marker carrying the value asked for — a slice whose environment
  did not arrive is not marked done and re-runs.

⚠ **What it cannot catch is stated where it is built:** it proves the environment *arrived* and that
the name is one the instrument reads. It does **not** prove the value reached the physics — that is
the knob shadow (`r4558`, `cc66.36`) and it takes a differential, not a print.

⚑ Sliced on `KBATCH` boundaries; idempotent and resumable.
