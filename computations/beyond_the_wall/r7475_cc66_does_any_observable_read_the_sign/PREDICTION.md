---
kind: PREDICTION
row: PO-88
step: does any observable read the sign of sqrt(B)?
revision: r7475+cc66.16
written: before any line of the build
---

# Pre-registration — does any observable read the sign of $\sqrt B$?

*Committed before the computation exists. `r7471` ③ / `r7475` ② put the pre-registration in its own file;
this is that file.*

## What `r7475` ① asks, and what it decides

`r7473+cc66.12` found the crossing hands out $(A,-\sqrt B)$ — species-selective **in sign only**. The
question is whether that sign is observable. ⇒ **If the magnitude is all any observable reads, `PO-88`
strikes on its own termination clause**, and the answer owes a **count of observables checked**. If one
reads the sign, that is the row's live remainder.

Two candidates are named in the order: the expansion leg's **radiation-to-dust ratio at the onset**
(`P16` §`peak`), and the **sign of the potential** the leg hands to `P15`'s transfer.

## The arithmetic done in advance, so it is not priced

$a(\eta)=\tfrac{A}{2}(1-\cos\eta)+\sqrt B\sin\eta$, and the densities are $\rho_m=A/\lvert a\rvert^3$,
$\rho_r=B/\lvert a\rvert^4$.

- **The named candidate ⒜ is settled by inspection:**
  $\rho_r/\rho_m \propto (B/A)\,\lvert a\rvert^{-1}$ carries **$B$, not $\sqrt B$**, and $B=(\sqrt B)^2$,
  so the sign cancels identically. *That one cannot read the sign and I am not pricing it.*
- **And the sign is not free once the leg is fixed.** $a'(0)=\sqrt B$, so with $\sqrt B<0$ the scale factor
  goes **negative** just past the branch point — not a state the matter can be in. The physical leg is the
  one with $a>0$, and flipping $\sqrt B$ while reversing the direction of $\eta$ returns the *same* $a$,
  which is the involution itself. ⇒ **The sign of $\sqrt B$ and the direction called "forward" are one
  choice, not two.** *That is the shape of the expected answer, and it is why the prediction below is what
  it is.*

## ⚠ The one place I cannot settle it in advance

**Candidate ⒝, the potential handed to `P15`'s transfer.** `P15`'s machinery carries **phases and a
monodromy**, and a phase is exactly the kind of quantity that can be odd where an amplitude is even — the
corpus has already measured one such case (`P16`'s monodromy $4\pi/\rho$, and the scalar/tensor phase work
in `P15`). So the live risk is that some phase the leg hands over is odd in $\sqrt B$ even though every
density is even. ⌗ *That is where this price can die, it is named here, and the build measures it first.*

## The answers, each falsifiable alone

| # | what is computed | pre-registered answer |
|---|---|---|
| ⒜ | $\rho_r/\rho_m$ at the onset | **even** — carries $B$ and not $\sqrt B$ |
| ⒝ | the potential/phase `P15`'s transfer reads | **even** ⚠ *the risky one* |
| ⒞ | a swept set of leg observables — $\rho_m$, $\rho_r$, their ratio, $H=a'/a^2$, $\ddot a$'s sign, the sound speed, the sound-horizon and particle-horizon integrals, the freeze-out epoch | **every one even**, once the leg is fixed by $a>0$ |
| ⒟ | the **count** of observables checked, which `r7475` ① asks for by name | **9** (⒞'s eight plus ⒝), band **7–14** |
| ⒠ | so: does `PO-88` strike | **YES — it strikes on its own termination clause**, the sign being a labelling of which direction is forward and not a fact about the world |

**What would kill it:** any one of the swept observables coming back odd in $\sqrt B$; the potential or a
phase coming back odd (⒝, the named risk, and the outcome that would make the sign the row's live
remainder); or the leg turning out **not** to be fixable by $a>0$, which would mean both signs describe
physical histories and the choice is not gauge after all.

## Cost

| what | predicted (band) |
|---|---|
| the computation script | **170** lines (110–280) |
| `WALK.md` | **100** lines (70–170) |
| wall time | **15 s** (2–90) — *raised: the last one took 17 s on `Abs` simplification* |
| measurement runs | **4** (2–8) |
| turns to the result | **2** (1–4) |
| a receipt | ⚠ **owed, with a control** (`r7475` ②): a quantity that **is** odd in $\sqrt B$ before the leg is fixed — $a'(0)$ itself — so that "even" is shown to come from the leg condition and not from the algebra |

⌗ **And one constraint recorded so it cannot be forgotten mid-build:** `r7475` ③ — **`P16` is not mine to
edit.** The paper takes the regulated peak, the dust involution and this result in `P16`'s own turn, by
`69`. Anything this revision finds about `P16`'s text is routed, never written.
