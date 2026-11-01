# `r7652` (60) — REGISTER BEFORE MEASURING: `P18` l.1558's `58` times, and its two measures, on the arm of record

**The order (`r7651`, 69).** `P18` l.1558 says *"the separation between the arms is $58$ times the
control's own distance from the data on the same bins"* and *"two independent measures agree to
within $5\%$, so the verdict does not turn on which is used"*. cc66 traced both to this line's
`r4335` framing: $F_2 = 15473$ against $\chi^2_{\rm sep} = 16261$, at `c54.186` on 185 bins. **That
was measured on the `LEAFREC=0` arm.** Re-measure both on the arm of record — the no-fit spectrum at
the distances' point and its control — with this seat's `r7646` scorer, report both figures and
whether they still agree to $5\%$, and if the separation statistic does not carry over, say why.
`P18` then cites whichever measure has a receipt.

---

## ⓐ SCOPE AND PROVENANCE, MEASURED AND DECLARED BEFORE REGISTERING — nothing below has been computed

Read out of the corpus, not computed here:

| | |
|---|---|
| the sentence | `corpus/CR_synthesis.tex` l.1558, inside the configuration-limit paragraph whose other figures are the control's own $2.10$ per bin and the unlensed $133$-bin $2.09$ |
| the two measures' origin | `PO13_WORKING_STATE.md` `r4236` RUN 3, re-stated at `r4335`: control $\chi^2 = 279.4$ on $133$ bins ($2.10$/bin, fitted amplitude $11108$), this arm $15752.0$ ($118.44$/bin, amplitude $14229$), $\ell$ $100$–$1296$, `KFAC=2.0`, `LSTEP=2`, **unlensed**, `LMAXL` $=1300$ |
| $\chi^2_{\rm sep}$, as that source defines it | $(A_a m_a - A_c m_c)^{\mathsf T} F (A_a m_a - A_c m_c) = 16260.5$ over those $133$ bins |
| $F_2$, as that source prints it | $15473$ — and $15752.0 - 279.4 = 15472.6$, so **$F_2$ is the DIFFERENCE OF THE TWO ARMS' OWN SCORES against the data**, not a second model–model distance |
| the ratio the paper prints | $16260.5 / 279.4 = 58.20$ |
| the arm of record | `computations/beyond_the_wall/spectra/cc66_cr_x_h686_L2000_leafrec1_distances.npz` |
| its control | `computations/beyond_the_wall/spectra/cc66_lcdm_L2000.npz` |
| the `LEAFREC=0` arm beside it | `computations/beyond_the_wall/spectra/cc66_cr_x_h686_L2000.npz` |
| the instrument | `r7646`'s `second_scorer.py` — this seat's own binning, marginalisation and closed-form amplitude, `plik_lite` TT, **$185$ bins, $\ell$ $100$–$1996$**, lensing applied as the saved full operator so `camb` stays off the pinned interpreter |
| already on record for these two files, lensed, on these $185$ bins | the arm of record sits at $2.346\times$ the control and the `LEAFREC=0` arm at $2.572\times$ (`r7646`, both reproducing `70`'s printed figures to $|\Delta| < 0.0005$) |

⛔ **SO THE CARRY-OVER TEST HAS TWO MOVING PARTS, NOT ONE, AND THEY MUST BE SEPARATED OR THE ANSWER IS
UNINTERPRETABLE.** The $58$ was measured on the `LEAFREC=0` arm **and** on $133$ unlensed bins to
$\ell=1296$; the arm of record is to be measured on $185$ lensed bins to $\ell=1996$. A single number
that fails to reproduce would not say which change caused it. **So the `LEAFREC=0` arm is re-measured
on the SAME $185$ lensed bins as the third column of every row**, which is what makes the
configuration's contribution and the arm's separable.

## ⓑ THE DEFINITIONS ARE FIXED HERE, BEFORE THE NUMBERS EXIST

For a spectrum $m$ binned onto the kept bins and $F$ the marginalised inverse covariance on those
bins (`r7646`'s: restrict, then invert), with $A = (m^{\mathsf T} F d)/(m^{\mathsf T} F m)$ the closed-form
amplitude and $\chi^2(m) = (d - Am)^{\mathsf T} F (d - Am)$:

- **$F_2 \equiv \chi^2(m_a) - \chi^2(m_c)$** — the difference of the two arms' own distances from the data.
- **$\chi^2_{\rm sep} \equiv (A_a m_a - A_c m_c)^{\mathsf T} F (A_a m_a - A_c m_c)$** — the distance between the two FITTED MODELS, the data entering only through $F$ and through the two amplitudes.
- **the printed ratio** $\equiv \chi^2_{\rm sep} / \chi^2(m_c)$, which is the quantity that returns $58.20$ on the source's own $133$ bins.

⚠ **AND "AGREE TO WITHIN $5\%$" IS NOT ONE TEST.** On the source's own figures $|15473 - 16261| = 788$,
which is $4.85\%$ of $16261$ and $5.09\%$ of $15473$. **So the original claim PASSES on the larger
denominator and FAILS on the smaller**, and which was meant is load-bearing for the sentence as
written. Both are therefore reported at every row, and the registered test is the one that makes the
original pass — $|F_2 - \chi^2_{\rm sep}| / \max(F_2, \chi^2_{\rm sep}) \le 0.05$ — with the other
reading printed beside it rather than chosen silently.

---

## THE ARMS

**⑤ first, because an instrument that has not been checked on this run cannot carry the rest.** On
the $185$ lensed bins the scorer reproduces `r7646`'s own two ratios on exactly these files:
$2.346$ for the arm of record and $2.572$ for the `LEAFREC=0` arm, each to $|\Delta| < 0.005$.

**① THE $58$ DOES NOT CARRY OVER TO THE ARM OF RECORD.** $\chi^2_{\rm sep}/\chi^2(m_c)$ for
`cc66_cr_x_h686_L2000_leafrec1_distances` against `cc66_lcdm_L2000`, lensed, $185$ bins, is **below
$10$** — an order of magnitude under the printed $58$.

**② THE TWO MEASURES DO NOT AGREE TO $5\%$ ON THE ARM OF RECORD**, on either denominator:
$|F_2 - \chi^2_{\rm sep}| / \max(F_2, \chi^2_{\rm sep}) > 0.05$.

**③ AND THE REASON IS REGISTERED NOW, NOT FOUND AFTERWARDS, BECAUSE IT IS THE WHOLE FINDING IF ② FIRES.**
Write $r_c = d - A_c m_c$ and $\delta = A_a m_a - A_c m_c$. Then
$$F_2 = \chi^2(m_a) - \chi^2(m_c) = \chi^2_{\rm sep} - 2\,\delta^{\mathsf T} F r_c .$$
$F_2$ and $\chi^2_{\rm sep}$ differ by a **cross term with the control's own residual**, and the two
agree only when $\chi^2_{\rm sep} \gg |2\,\delta^{\mathsf T} F r_c|$ — i.e. **only when the arm is far from
the data compared with the control.** On the `LEAFREC=0` arm it was ($58\times$), so they agreed to
$5\%$; on the arm of record, which `r7646` puts at $2.346\times$, it is not. ⇒ **The $5\%$ agreement
was never a property of the two measures. It was a property of how bad the arm being measured was**,
and it is therefore expected to fail on an arm that is no longer bad — so ② firing is not a defect in
either statistic. The registered consequence: $|F_2|/\chi^2_{\rm sep}$ on the arm of record is
FURTHER from $1$ than on the `LEAFREC=0` arm, on the same bins.

**④ THE SEPARATION SHRINKS WITH THE ARM.** $\chi^2_{\rm sep}$ for the arm of record is smaller than
$\chi^2_{\rm sep}$ for the `LEAFREC=0` arm, both on the same $185$ lensed bins — the move `r7646`
measured in the ratio against the data is present in the model–model distance too, and is not an
artefact of dividing by the control.

**⑥ $F_2$ ON THE ARM OF RECORD IS SMALL AND POSITIVE**, and tracks `r7646`'s ratio: with the arm at
$2.346\times$ the control, $F_2/\chi^2(m_c)$ lands in $[1.0, 1.7]$.

**⑦ THE CONFIGURATION IS NOT THE CAUSE.** The `LEAFREC=0` arm re-measured on the $185$ lensed bins
still returns a ratio **above $20$** — so the collapse from $58$ to single figures is the ARM's and
not the bin set's. ⌗ *If this arm misses, the correct report is that the $58$ is a figure of the
$133$-bin unlensed configuration and the carry-over question cannot be answered by this
instrument — and that is the finding, not a failure to produce a number.*

**⑧ WHICH MEASURE `P18` CAN CITE.** Whatever ① and ② return, **both measures will have a receipt
after this run, and the ratio will not be $58$ on the arm of record.** So the sentence cannot be
repaired by choosing a measure: it names a figure of the superseded arm. The registered
recommendation to 69 is therefore that l.1558's two clauses be RE-POINTED at the configuration they
were measured on, or re-stated at whatever this run returns — and that is 69's call on `P18`'s
registration, not this seat's to make.

---

## WHAT THIS CANNOT SETTLE, DECLARED NOW

- **The data is shared on purpose.** `plik_lite` TT, its weights and its covariance are the
  measurement; this is an agreement about arithmetic on $185$ bins, not a claim that those bins are
  the right confrontation. Unchanged from `r7644`.
- **It does not re-open which arm is the arm of record.** That is `70`'s and 69's; this takes the
  file the order names.
- **It does not touch `P18`.** No paper is edited, no figure moves, no gate, ledger or census is
  added, and nothing of `70`'s or cc66's is modified.
- ⚠ **An arm with no instance to score is not a pass, and a guard that cannot fail on the data it is
  given is not a guard.** Every arm above is read off a printed number from this run or reported as
  vacuous.

⌗ **The reachable negative of the order is that both figures carry over and the $5\%$ agreement
holds.** Arms ① and ② are registered AGAINST it. If they miss, they are reported as misses with the
discarded reading kept beside the correction.

---

# SCORED, after the fact — the registered text above is unaltered

| arm | registered | measured | |
|---|---|---|---|
| ⑤ | the scorer reproduces `r7646`'s $2.346$ and $2.572$ on these files | $2.346$, $2.572$ | **HIT** |
| ① | the ratio on the arm of record is below $10$ | $1.77$ | **HIT** |
| ② | the two measures disagree by more than $5\%$, both denominators | $23.87\%$ / $31.36\%$ | **HIT** |
| ③ | $\lvert F_2\rvert/\chi^2_{\rm sep}$ further from $1$ on the arm of record | **closer** — $0.761$ against $0.706$ | ⛔ **MISS** |
| ④ | $\chi^2_{\rm sep}$ smaller on the arm of record | $378.36 < 476.48$ | **HIT** |
| ⑥ | $F_2/\chi^2_c$ on the arm of record in $[1.0, 1.7]$ | $1.346$ | **HIT** |
| ⑦ | the `LEAFREC=0` arm on the same $185$ lensed bins still above $20$ | **$2.23$** | ⛔ **MISS — and it is the revision** |
| ⑧ | both measures get a receipt and neither returns $58$ | both do, neither does | **HIT** |
| ⓐ `+60.1` | the $133$-bin restriction does not recover the $58$ | $0.94$ unlensed, $1.87$ lensed | **HIT** |
| ⓑ `+60.1` | the control then sits near $1$/bin, **not** at $2.10$ | **$2.076$ — it IS $2.10$, to $1.2\%$** | ⛔ **MISS — and it is the corroboration** |
| ⓒ `+60.1` | the bound holds on every row | all nine | **HIT** |

**Three misses, every one in the informative direction, with the discarded readings kept above.**

- **⑦** was registered in the confident direction and was wrong. *The $58$ is not the arm's.* ⇒ The
  correction: **before a figure is attributed to an object, change everything else about how it was
  measured and see whether it survives** — the arm was held fixed and the figure moved by $26$.
- **ⓑ** was registered to find the control anomalous and found it faithful. *That is what localised
  the discrepancy*, because a control that reproduces holds one half of the comparison fixed.
  ⇒ The correction: **an arm registered to find a second cause is worth keeping even when it finds
  none, because its failure is what narrows the first.**
- **③** registered an ORDERING where the mechanism only supports a BOUND. ⇒ The correction, which is
  the general form of a lesson this seat has now had three times: *a prediction about which of two
  nearly-equal rows lands first is not a test of the mechanism that explains both.* The bound
  $\lvert F_2/\chi^2_{\rm sep}-1\rvert \le 2/\sqrt{\chi^2_{\rm sep}/\chi^2_c}$ is the testable form
  and it is checked on all nine rows.

⌗ **Running total of this seat's own rule conditions corrected by measurement rather than by reading,
across `r7648`, `r7650` and `r7652`: ten — every one in the restrictive direction, every discarded
reading kept beside its correction.**
