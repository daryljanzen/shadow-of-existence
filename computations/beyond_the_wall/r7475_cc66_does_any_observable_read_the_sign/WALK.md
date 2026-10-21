---
kind: WALK
row: PO-88
step: does any observable read the sign of sqrt(B)?
revision: r7475+cc66.17
---

# `PO-88` — **no observable reads the sign**, and the row strikes

*Computed in `sign.py` (output `sign_out.txt`); re-proved with a control in
`receipts/P16_cosmogenesis_paper/P16_no_observable_reads_the_sign_of_the_radiation_amplitude.py`.
The pre-registration is `PREDICTION.md` beside them, committed first.*

## The whole answer is one derived line

`P16`'s interior obeys $a''+a=A/2$. Multiply by $a'$ and integrate, with $a=0,\ a'=\sqrt B$ at the branch
point:

$$\boxed{\ a'^2 \;=\; B + A a - a^2\ }$$

checked identically against $a=\tfrac{A}{2}(1-\cos\eta)+\sqrt B\sin\eta$. ⇒ **The dynamics, written as a
function of the scale factor, carries $B$ and never $\sqrt B$.** Since $B=(\sqrt B)^2$, the sign cannot
enter any quantity that is a function of $a$; and $a'(a)=\pm\sqrt{B+Aa-a^2}$, where that sign is the
**expanding-versus-contracting branch**, not the sign of $\sqrt B$.

## ⒝ The named risk, measured first — and it did not materialise

The price flagged one candidate as the place it could die: **the phase `P15`'s transfer reads**, because a
phase can be odd where an amplitude is even. The phase is the accumulated sound horizon,
$s=\int c_s\,d\eta=\int c_s\,da/a'(a)$, and on the leg

$$c_s^2(a)=\frac{B}{3(Aa+B)},\qquad a'(a)=\sqrt{B+Aa-a^2},$$

both functions of $B$ alone. ⇒ **Even.** *The flag was right to be raised — that shape exists in this
corpus — and this time it did not fire.*

## ⒞⒟ The sweep, and the count the order asked for by name

| observable (on the scale factor) | |
|---|---|
| $\rho_m$, $\rho_r$, $\rho_r/\rho_m$ | even |
| $H^2=(a'/a^2)^2$ | even |
| $a''=A/2-a$ | even |
| $c_s^2$ | even |
| $(c_s/a')^2$, the sound-horizon integrand **squared** | even — see below |
| particle-horizon integrand $1/a'(a)$ | even |
| $a_{\rm turnaround}$, the root of $a'=0$ | even |

**9 of 9 in the sweep, plus the phase: 10 observables checked, 0 read the sign.**

⛔ **This one entry took three attempts, and the first would have inverted the verdict.**

1. **Scored `ODD`.** Substituting $\sqrt B\to-\sqrt B$ tests the **expression** sympy happened to write,
   not the **quantity**: it printed $c_s$ as $\sqrt B/\sqrt{\cdots}$. But $c_s$ is a **speed** — the
   *positive root* of $c_s^2$, and $c_s^2$ carries $B$ alone. The symbol flips; the quantity does not move.
   ⌗ *Uncorrected, this single misclassification would have reported a live remainder instead of a strike.*
2. **Special-cased.** The classifier was then taught to accept "even as a positive root" when the square
   was even — which **the control immediately broke**: $a'(0)=\sqrt B$ also has an even square, so the
   branch label itself came back filed as even. *An odd quantity always has an even square, so that test
   could never tell them apart.* The control exists for exactly this and it earned its place.
3. **Swept the square.** The honest form: the sweep carries $(c_s/a')^2$, which is unambiguously even, and
   the positive-root step is **stated in prose** rather than hidden in a classifier. The classifier is back
   to `EVEN`/`ODD`/`NEITHER`, with `ODD` tested before anything involving squares.

⌗ *The second attempt is the one worth recording: it was whitelisting the answer I wanted, and the thing
that caught it was the control I had written to catch exactly that.*

## ⒠ The verdict, and the control that earns it

**No observable reads the sign of $\sqrt B$, so `PO-88` strikes on its own termination clause.** The sign
is the label on which direction along $\eta$ is called forward — *the same choice as the involution itself*
— and not a fact about the world.

⛭ **The control is what makes "even" mean anything.** Something must come out odd, or the result is
arithmetic:

- $a'(0)=\sqrt B$ — **odd.**
- $a(\eta)$ and $a'(\eta)$ at **fixed $\eta$** — **neither** even nor odd; they carry the sign.

⇒ So the even answer comes from writing each observable **on the scale factor** — i.e. from fixing the leg
by $a>0$ — and not from the algebra. ⌗ *And $a'(0)$ is exactly the branch label: the one quantity that
lives at $a=0$, where the direction is chosen and no observable is read.*

## ⛔ What is not claimed

No temperature, no abundance, no statement about $B$'s **magnitude**, which every one of these observables
does read. Nothing about a third species. And nothing about `P16`'s text: **`r7475` ③ — `P16` is not this
seat's to edit**, and the paper takes the regulated peak, the dust involution, the pressure half and this
result in its own turn.

## ⇒ The row

- **Strikes.** The sign is gauge; the magnitude is physics; the crossing's species-selectivity is in the
  sign alone, which nothing reads.
- **Nothing is left open by this step**, which is why it is a strike and not a remainder.
