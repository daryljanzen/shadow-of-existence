# `r7713+cc66` — REGISTERED BEFORE ANY COMPUTATION

**The order** (`r7713`, 69): run the dense-`l` discriminant, taking own × own to about `5` sd; read all
three ratios; report whether the split seen at low significance survives — the kernel difference alone
giving about twice the step with the measured sign, the source difference alone the opposite sign. **And
register first what would count as "the projection creates it", what as "fails to cancel it", and what as
neither.**

---

## ⛭ THE GRID — AND I AM TAKING MORE THAN I PRICED, WITH THE RE-PRICING STATED

I priced `549` `l` per combination at about `2.6` hours. ⇒ **Every integer `l` in `q ∈ [0.80, 3.10]` is
available** — `693` for the control (`l 242–934`, `l_A = 301.543`) and `697` for the arm
(`l 243–939`, `l_A = 302.943`) — because the kernel `G_l(k) = ∫ v j_l(k x₀) dη` needs only the banked
`eta`, `x0`, `vis` and `k`, and nothing about the bank's own `238`-point `l` list constrains where it is
evaluated.

**So I take all of them and re-price honestly: about `3.2` hours, `23` per cent over the `2.6` I quoted.**
*`549` was my estimate of what `5` sd needs; `693` is what exists. Taking all of it removes the
subsampling question entirely rather than leaving a choice of grid to argue about later, and the extra
cost is the smaller price.* ⌗ **The registered bound is `4.5` hours**, set above the estimate because
`r7711`'s bound was blown `4.9`× by costing the array and not the algorithm; if it lands over `4.5` I say
what it cost rather than charging it elsewhere.

⛔ **The launcher writes each combination to disk as it completes and skips finished ones**, because this
container restarts unpredictably and a three-hour job that cannot resume is a three-hour job that may
never finish.

## ⛔ THE DECISION RULE, FIXED NOW — because at low significance the pattern ALREADY looks like "creates"

`r7711` read `+0.0482` for the kernel difference and `−0.0277` for the source difference, which *points*
at "creates". **That is exactly why the thresholds are written before the dense numbers exist.**

| verdict | what must hold |
|---|---|
| **THE PROJECTION CREATES IT** | the **kernel** difference alone (`source held`) gives a step of the **measured sign** and at least comparable size, at **≥ 5 sd**; AND the **source** difference alone (`kernel held`) gives either under `2` sd or a step of the **opposite** sign. |
| **IT FAILS TO CANCEL** | the **source** difference alone gives a step of the measured sign and at least comparable size at **≥ 5 sd**; AND the kernel difference alone gives under `2` sd or a smaller same-sign step. |
| **NEITHER — ⒜ still unresolved** | both under `5` sd. ⇒ Then the pseudo-spectrum route is **exhausted rather than under-sampled**, since the sampling excuse is the thing this revision removes, and that is the finding. |
| **NEITHER — ⒝ not separable** | both resolved, both of the measured sign, both comparable. ⇒ The two differences do not partition the step and "creates versus fails to cancel" is not a question this construction answers. |
| **NEITHER — ⒞ withdrawn** | the three readings do not combine consistently (below). ⇒ The construction's algebra does not hold and the reading is withdrawn, not interpreted. |

## ⛔⛔ THE PRIMARY TEST IS WHETHER THE QUESTION IS WELL POSED AT ALL

`Pseudo(S,K)_l = Σ_k G_l^K(k)² S(k)² dk/k` is a **sum over `k`, not a product**, so it does **not**
factorise as `f(S)·g(K)`. ⇒ **Log-additivity of the three ratios is therefore NOT an identity:**

> `log[Pseudo(cr,cr)/Pseudo(lcdm,lcdm)]` versus
> `log[Pseudo(cr,lcdm)/Pseudo(lcdm,lcdm)] + log[Pseudo(lcdm,cr)/Pseudo(lcdm,lcdm)]`

**It is a measurement of how far the source and kernel differences interact**, and it can fail. If it holds
closely, the two differences are separable and "creates versus fails to cancel" is a well-posed partition.
If it does not, the partition is not available **whatever the individual significances say**, and verdict
⒞ applies. ⌗ *At `87` `l` the two sides were `+0.0232` against `−0.0277 + 0.0482 = +0.0205` — close, but
inside the noise, so it is not yet evidence of anything. The dense grid is what makes it a test.*

⇒ **This check is reported BEFORE the three verdicts, and the verdicts are not stated if it fails.**

## ⚠ TWO FURTHER GUARDS, REGISTERED

1. **The three ratios are not independent** — all share the denominator `Pseudo(lcdm,lcdm)`, so their
   plateau scatters are correlated. **Consistent signs across the three are not three confirmations**, and
   no significance is to be combined across them.
2. **own × own must reach `≥ 5` sd.** If the dense grid does not take it there, then my `1/√n` scaling
   was wrong and **that is a finding about my estimate, not about the physics** — reported as such, with
   the achieved significance and what it implies the scatter actually scales as.

## WHAT IS NOT AVAILABLE, UNCHANGED

- **No attribution**: no build removes a step the arms share.
- **The acceptance kernel is not the exact transfer.** Whatever this settles, it settles about the
  pseudo-spectrum built from the banked geometry — *`r7711` established the swap is live on that object,
  which is what makes the reading worth doing, and not that the object is the full projection.*
- **Nothing is printed** unless a verdict is reached and licensed.

## CADENCE — 69's INSTRUCTION, TAKEN

**One push for this registration and one for the result**, not per stage. ⇒ *That also removes the
registration-push collision I recorded twice: with no intermediate pushes, the only sweep this revision
can cancel is the one its own registration starts.*

## FAILABILITY

Any gate added is perturbed and the named check watched go red, over a **green control run first**; and the
cross-kernel control from `r7711` (the swap must move the pseudo-spectrum) is re-run on the dense grid
before any ratio is read. ⛔ *A leg reporting `0` FAIL means the perturbation went TOWARDS the gate.*
