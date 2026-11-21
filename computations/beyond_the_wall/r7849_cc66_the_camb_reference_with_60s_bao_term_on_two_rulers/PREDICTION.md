# `r7849+cc66.1` — PREDICTION, registered before a line of the computation exists

**Order `r7849` (69) ①–③:** rerun the `r7847` CAMB reference *with* 60's BAO term, on two treatments
of the ruler, and read the three-way split against `64.2` meV and `−0.101` eV.

## ⛔ First: 69's correction is right, and the error was mine

`r7847+cc66.4` reported `122.06` meV against 60's `111.38` and the published `64.2`, and concluded
**"the gap is the data subset, not the instrument."** That conclusion is withdrawn, and not merely
on a technicality:

- 60's control scores the CMB **and DESI DR2 BAO** — `model6.chi2(..., bao=True)`, default **on**,
  through `model3.bao_direct` → `distances.chi2_bao`, with `r_d` **minimised** over `(120, 170)`.
  Verified in their source, not taken on 69's word.
- My reference scored the CMB half, the lensing half and **no BAO**.
- The published `64.2` meV is a DESI **+** CMB figure.

So a CMB-only limit was set against two CMB+BAO ones. ⌗ **And I had named the very omission I then
reasoned past:** `r7847`'s `PREDICTION.md` lists "no BAO" among the reasons the limit would be
loose. That was correct about *my* limit and gave me `Ⓓ`. The error was sliding from "my limit is
loose because I lack BAO" to "60's gap is the subset" — the first is a deficiency of my own
reference, the second a claim about theirs, and the missing BAO made them not comparable. Naming a
limitation is not the same as honouring it.

## The mechanism this rerun turns on, read off 60's own code

`distances.E_stack(z, Om, h) = sqrt(Om (1+z)^3 + (1 − Om))` — flat ΛCDM, radiation-free, and it is
the rate `ARMS['lcdm']` (the control) uses. **It has no `Σm_ν` dependence at all** (and does not
even use `h`). So the BAO term cannot constrain the sum *directly*. Its whole effect must run
through **pinning the geometry the sum trades against** — and `r7847`'s opened profile shows
exactly that trade: `H0` ran `67.95 → 64.18` and `Ω_m` `0.308 → 0.358` as the sum grew to `0.4` eV.
Forbid that, and the limit must tighten.

## ① ② The two limits — my primary calls

- **Ⓐ With BAO and `r_d` MINIMISED (60's treatment), the limit lands in `70–110` meV.** It should
  tighten a long way from `122.06`, because `r_d`-minimised BAO pins `Ω_m` hard while leaving the
  absolute scale free. 60's `100.40` sits inside this band, which is the point.
- **Ⓑ With `r_d` from CAMB's own sound horizon (the published treatment), tighter still: `55–85`
  meV**, bracketing the published `64.2`. Calibrating the absolute scale pins `H0` as well.
- **Ⓒ The ruler's treatment is worth MORE than the `5.3` per cent 60 measured on temperature
  alone — I predict the two limits differ by more than `10` per cent.** ⇒ *Reachable negative:* if
  they differ by under `5` per cent the ruler is **not** where the gap lives, and that is a finding
  against this prediction.
- **Ⓓ The effective mass moves toward zero.** `r7847`'s unbounded vertex was `−86` to `−94` meV
  with the geometry free; with BAO I predict the `r_d`-from-CAMB vertex in **`−60` to `+20`** meV.

## ③ The split — and the call that costs me

- **Ⓔ BAO is the DOMINANT missing piece**: more of the `122.06 → 64.2` gap closes by adding BAO
  than by the `613`-against-`555` bins or anything else. ⇒ **If Ⓐ and Ⓑ hold, my `r7847` verdict
  was wrong in substance and not only in form**, and the "subset" explanation is dead. Registered
  here so it cannot be softened afterwards.
- **Ⓕ Against 60's `100.40` meV on the same terms:** if my `r_d`-minimised limit lands within
  `10` meV of it, **60's instrument is vindicated on like-for-like terms** and the residue is the
  subset plus the ruler. If mine comes out much tighter, 60's instrument carries a real excess and
  the `r7847` conclusion inverts.
- **Ⓖ A mechanistic check, cheap and decisive about the route.** Because `E_stack` carries no sum
  dependence, the BAO term's work must be visible as the geometry *failing to move*: with BAO on,
  the fitted `H0` and `Ω_m` at each sum should stay far closer to the control than the
  `67.95 → 64.18` / `0.308 → 0.358` run they made without it. If they still run that far, BAO is
  not acting through the degeneracy and the tightening has some other cause.

## What this cannot settle

- **Whether 60's Φ transport through the radiation era is right.** Unchanged from `r7847`.
- **The `613`-against-`555` bin difference remains**, and still biases my limit tight. 60's mask is
  `isfinite` over solver grids that lived under `/tmp` and is not reproducible here.
- **`E_stack` is radiation-free while CAMB's expansion is not.** Over DESI's range (`z ≤ 2.33`) that
  is a sub-`0.1` per cent effect on the distances, but it is an inconsistency between the BAO term
  and the spectra it is being added to, and it is 60's choice that I am matching for like-for-like
  rather than one I would make alone. It is stated, not hidden, and the `r_d`-from-CAMB arm is the
  one that would expose it.
- **The published figures' provenance.** `64.2` meV and `−0.101` eV are taken from the order.
