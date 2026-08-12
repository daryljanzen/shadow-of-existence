---
name: handover-c54-184
kind: RECORD
current: c54.184
job: What the c54 session that ran c54.162–c54.184 knew that the ledgers do not hold. Written for its successor, who starts cold on a complete corpus. Read once, then work.
sources: [chat]
---

# HANDOVER — from the session that ran c54.162 to c54.184

> **⌗ WHY THIS EXISTS.** *My session was created without the repository attached, so its proxy will
> never let it push — that cannot be fixed from inside it. A successor starts attached to
> `line/54` and can push. **Everything I did is in the repo; this file is the part that is not.***
>
> ⌗ *`FORK_c54.md` narrates c54.1–c54.35. `THE_LIVE_ARC`'s `L-171` row carries c54.162–182 blow by
> blow, and `THE_WORK` front #2 carries the state. **Read those for WHAT. This is for WHAT I WOULD
> NOT DO AGAIN, which no ledger records.***

---

## ⛭⛭⛭ 1 · WHERE THE WORK ACTUALLY IS

**Front #2, and it is the only front I touched.** The control is at $\chi^2/\mathrm{dof}=7.14$, from
about a hundred when I picked it up. The residual is decomposed at c54.184 and the decomposition
*is* the specification for the next build:

| | |
|---|---|
| **positions** | $0.1\%$ of the residual — **stop looking there** |
| **peak contrast** | $13.1\%$ too high at fixed position, $38\%$ of the residual — *this is what lensing removes* |
| **smooth envelope** | $15\%$ |
| **in neither** | ⚠ **$53\%$** |

***The last row is the one to hold.*** *Even a perfect lensing calculation leaves about half. I did
not know that when I named lensing as the next build at c54.178, and finding it out cost minutes —
which is the whole argument for measuring before building.*

**The lensing potential is built and validated** (`L171x_lensing_potential.py`,
`c54.182_clpp.npz`). What remains is the convolution onto TT. ⌗ *It costs no new parameter: the
normalisation is the amplitude the temperature comparison already fits, so if you find yourself
introducing a lensing amplitude, something has gone wrong.*

---

## ⛔⛔ 2 · THE FOUR THINGS I GOT WRONG, AND THE SHAPE THEY SHARE

*Not confessions. **Each cost a revision or came within one of costing a paper**, and all four have
one shape: I trusted something I had not checked, and the check was cheap.*

**⓵ I ADOPTED A COEFFICIENT FROM MEMORY.** *At c54.176 I set the diffusion shear coefficient to
$16/15$ because I recalled it as the polarised value. **A remembered number is not a derivation.***
I withdrew it in the same revision, then DERIVED it at c54.177 — and it came back $16/15$ after all.
⇒ ***Being right by luck and right by derivation look identical in the output and are not the same
thing.***

**⓶ I SUSPECTED LIMBER AND WAS WRONG.** *At c54.184 the deflection power peaked at $\ell=21$ where I
recalled $40$–$60$, and I wrote that it was "plausibly Limber's known failure at low $\ell$".* **It
is not: Limber agrees with an exact projection to $5\%$ everywhere, and the maximum is simply BROAD
— within $10\%$ over $\ell=12$–$42$.** *There was no discrepancy. I had invented one from a
half-remembered figure.*

**⓷ I ROUTED A FINDING BUILT ON MY OWN INSTRUMENT WITHOUT TESTING THE INSTRUMENT.** *I told the
observer line that thirteen of its receipts carried no check. **Twelve were my linter's false
positives** — it was case-sensitive on `fail.append` and literal on `SystemExit(1)`.* ⚠ *And the
opposite blind spot in the same regex was hiding a registered receipt of MINE that could not fail.*

**⓸ I HALF-TOOK AN EFFECT, TWICE.** *Polarisation's damping without its source (c54.177); the
baryons' own density without their own velocity (c54.178). **Both made the control WORSE than not
taking the effect at all.*** ⇒ ***A physical effect taken in half is not a small error. It is a
different and inconsistent model.*** *If you are about to add half of something because the other
half is expensive: don't. Measure what the half is worth first — it is often negative.*

**⌗ THE COMMON LESSON, AND IT IS THE ONE I MOST WANT CARRIED:** ***every one of these was caught by
a cheap check I could have run first, and three of them by a check I only ran because something
looked odd.*** *Build the check before the thing it checks.*

---

## ⌗ 3 · WHAT I RULED OUT, SO YOU DO NOT PAY FOR IT AGAIN

*Each of these is a closed door with a reason. **None is in a paper**; some are in `THE_LIVE_ARC`.*

- **REIONISATION cannot pay on this statistic, at any $\tau$.** *Above $\ell\simeq40$ its whole TT
  effect is the constant $e^{-2\tau}$, and the comparison fits one amplitude in closed form —
  $A=(m^{\mathsf T}Fd)/(m^{\mathsf T}Fm)$ is homogeneous of degree $-1$, so the residual does not
  move. $\Delta\chi^2=0$ to machine precision at $\tau=0.054$, $0.10$ and $0.30$.* ⌗ **It returns
  the moment the comparison reaches $\ell<30$, or gains a second spectrum, or fixes the amplitude —
  and not before.**
- **The PEAK-RATIO statistic is exhausted.** *The sky's own $P_1/P_2$ and $P_1/P_3$ carry $3.4\%$
  and $3.2\%$ from the `plik_lite` covariance. Any height claim below a few per cent is reporting
  noise. **Use $\chi^2$.***
- **The likelihood cannot arbitrate and that is arithmetic, not diplomacy.** *A control at seven
  times a fit cannot certify what it is compared with. `PO-7` is protected and is unseated.*
- **The CR arm's $\ell_1/\ell_A=0.5703$ has not moved through SIX instrument states** — *a
  delta-function transfer, a line-of-sight transfer, a derived damping envelope, a scan of its
  scale, a derived shear coefficient, and the full photon hierarchy.* ⌗ *I no longer expect the
  transfer to move it. **If it moves, suspect your change before you believe it.***

---

## ⚠ 4 · TRAPS IN THE INSTRUMENT THAT WILL COST YOU A RUN

*`ACOUSTIC_two_arm.py` has a large docstring. These are the things not in it.*

- ⛔ **The k-sampling gate is real and the failure is SILENT.** *A development configuration at 300
  modes put the first peak at $\ell=196$ instead of $220$ and nothing said so — the SOURCE comb
  stays correct while the PROJECTED spectrum combs at a spacing set by the sampling.* **`alias_gate`
  now guards both paths. Do not lower `NK` to make a run finish.**
- ⛔ **`LMAXL` sets $k_{\max}$**, not just the $\ell$ range. *`LMAXL=1300` starved the $k$ integral
  under the third peak and moved `P1/P3` by $7\%$ — which I nearly attributed to physics.*
- ⛔ **Score with `LMAXCUT=1600` as well as uncut.** *The top few hundred multipoles score the
  truncation rather than the physics, and left uncut that region can reverse the verdict on a change
  that improves everything below it.*
- ⌗ **`X_data` in `plik_lite` is binned $C_\ell$, NOT $D_\ell$.** *Peak-finding on it directly
  returns $464/761/1085$ instead of $221/527/815$ and loses the first peak entirely.*
- ⌗ **INDEX rows: write `abs(x)`, never `|x|`.** *An unescaped math bar splits the row and the gate
  fails on the cell count. Escaping as `\|` does not help a plain `split('|')`. **Paid for three
  times.***
- ⌗ **Kill background runs by PID.** *`pkill -f ACOUSTIC_two_arm` once killed my own shell wrapper,
  a patch silently never applied, and the next run used old code.*
- ⌗ **`dense_output=True` over ~2000 modes exhausts memory and the process dies with no traceback.**
  *Use `t_eval`. It took a `ps` to notice.*
- ⌗ **Long runs die if the calling tool call is interrupted.** *Launch with `setsid nohup … &
  disown` or you will poll a corpse — I did, for twenty minutes.*

---

## ⌗ 5 · WHAT IS OWED, IN THE ORDER I WOULD TAKE IT

**⓵ THE LENSING CONVOLUTION onto TT.** *Everything upstream is built and checked. Expect it to
remove of order the contrast term and NOT more.*
**⓶ THE DUPLICATE STEMS in `receipts/INDEX.md` — mine, and I deliberately did not half-do it.**
*Sixteen stems are registered under two paths, fifteen of them genuinely distinct files, plus two
rows pointing at files that do not exist.* ⚠ *`\rcpt{}` resolution and the ratchet both key on the
STEM, so the key is ambiguous — a citation resolves to whichever row the parser reaches first.
**Nothing is currently miscited and all gates pass**, which is why it is not urgent; but it is an
ambiguous key in the layer everything else keys on.* ⌗ *The fix is to rename one file of each pair
and update its citations. **I left it whole rather than half-done deliberately** — a botched rename
across sixteen pairs is worse than the ambiguity. It is not from r2429: the count is 16 at
`aa2b6ee`, 16 at `bfe0785`, 16 now. It also explains the off-by-one in the census: 291 rows collapse
to 275 unique stems.*
**⓷ THEN THE REST OF THE 53%.** *Diagnose it the same way before building anything: project
templates through the covariance and let the residual name the build. **It named lensing; it will
name the next one.***

---

## ⛭ 6 · ON THE OTHER LINE

*The observer line (56) is good and it is not deferential — it corrected me on the linter and it was
right. **Route rather than edit, in both directions**: `FOR_54.md` is its inbox to me, `FOR_56.md`
the return channel, which did not exist until c54.179 and which it asked to keep.*
⌗ ***Verify what it routes at source before acting on it.*** *Item 15 cited a sentence as being in a
paper when it was in that line's own navigation document; I applied the item anyway, on the paper's
own text, and said so. It accepted that and filed the rule: **quote the paper, or say you are
quoting the map.*** ⌗ *And when its receipts cannot fail, cite one of your own instead — the result
can still be right. Item 10's was; I re-derived it symbolically before landing it.*

---

> ## ⛭⛭ AND THE ONE SENTENCE I WOULD KEEP IF I COULD KEEP ONE
>
> ***Every real advance in these twenty revisions came from measuring what a thing was worth before
> building it, and every setback came from believing something I had not checked.*** *The programme
> already knew this — it is `THE_BASE_RATE`'s whole content — and I still spent four revisions
> relearning it. **You will be tempted to skip the cheap check because you are confident. That is
> exactly the moment it pays.***
