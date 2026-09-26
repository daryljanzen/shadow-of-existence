# `r6891+cc66.37` — the switch sweep, the fine grid, and the confirmations

*`r6891`'s order, part ②: **"enumerate every environment switch this instrument reads, and for each
one record which of the three source constructions and which of the two solver paths actually reads
it — from the source text, not from memory — and, for every switch reachable on the reporting path,
whether setting it away from its default moves the spectrum there."*** The static half lives in the
receipt (it reads `ACOUSTIC_two_arm.py` through `ast`); these are the runs of the measured half, plus
the four spectra part ① needed on a finer $\ell$ grid.

**Every script here is IDEMPOTENT AND RESUMABLE** — each skips a tag whose log already carries its
`__DONE__` line, because this container restarts unpredictably.

| script | what it runs | grid | why |
|---|---|---|---|
| `screen.sh` | the sweep proper: each arm's refit command with **at most one switch added**, 57 tags per arm | `HIER=1 LSTEP=16 LMAXL=500` | ⚑ **connectivity is path-dependent and NOT resolution-dependent** — a switch read on this path is read on it at any $\ell_{\max}$, and $22$–$52$ s per run instead of $\sim20$ min is what makes sweeping every switch affordable |
| `pass2.sh` | the **paired** tests: each switch the screen reports inert, set together with the switch its own source text makes it conditional on (`LRSFROM` with `LZSTART=6761`, `LATARG` with `ZSTART` unset, `GSRC` on the arm where `RAD_IN_RATE` is false) | same | `r4558`'s rule: a switch reporting no change cannot be told from one that is not connected, so **inertness is not a result until connectedness is shown** |
| `pass3.sh` | the nine OFF-PATH switches and the `LRSFROM` pair again, at the reported $\ell$ reach | `LSTEP=32 LMAXL=2000` | ⚠ *the half reduced reach cannot carry: `DAMPX` and `RD` act on the **damping tail**, which $\ell\le500$ barely sees* |
| `pass4.sh` | `LATARG` at two further values with `ZSTART` unset | screen grid | the reporting base for that comparison **raises** — there is no root at `LATARG=301.6` at this arm's background — so the bracket has to be built from values where a root exists |
| `pass5.sh` | `SWSRC=0`, both arms | screen grid | ⚠ **`SWSRC` was missing from the first screen list.** *Kept as its own script rather than folded into `screen.sh`, because the omission is part of the record and a table that silently gained a row would not say so.* |
| `pass6.sh` | both arms' bases again, against the ANNOTATED instrument | screen grid | this revision's only edit to `ACOUSTIC_two_arm.py` is **comments**, and `cc66.36` is why that is measured rather than asserted: a change that should have been nothing cost $1.1\times10^{-16}$ there |
| `fine2.sh` | order ①'s finer grid, **two ways**: **A** the four spectra whole at `LSTEP=2 LMAXL=900` (four times the banked sampling, first three acoustic bands), and **B** the same four at `LSTEP=4 LMAXL=2000` (twice the sampling, all five bands) **in `KSLICE` pieces of 250 modes** | as noted | ⚠ **A CONTAINER RESTART IS WHY THIS SCRIPT EXISTS IN THIS FORM.** *The first attempt ran each spectrum whole at `LSTEP=2 LMAXL=2000`, about a hundred minutes, and the restart took all four at eighty because the instrument writes its `npz` only at the end.* ⇒ **A run longer than its node's own lifetime is not a long run; it is a run that does not finish.** `r6794` built `KSLICE` for exactly this, and its caveat — slices add exactly only on a **uniform** $k$ grid — is measured in the script's own step 0 rather than assumed away |
| `bank.py`, `bank2.py` | fold every output into `spectra/r6891_{switch_screen,full_reach_nulls,fine_grid}_*.npz`, keyed by tag, **including the `rc` of every run, a `failed` list, and the slice count each summed spectrum came from** | — | the one run in 110 that exits non-zero (`LATARG` with `ZSTART` unset) is kept rather than dropped |

⇒ The value each switch was moved **to** is declared in the receipt's own `OFFVAL` table, so the
experiment is on the record and not only in these scripts.
