# `r7616` — THREE PRINCIPLES WITH NO EUCLIDEAN CONTENT SELECT THE SAME MEMBER THE FACE SELECTS, SO THE $\alpha$-VACUA ARE A FOURTH EMPTY SLOT

Registration: `PREDICTION.md`, sha1 `48be42fac9c3c6f82615766ab60de79a5b48ca4f`, committed at `3cca1c98`
and **pushed before `alphavacua.py` existed**. Eight arms were registered; **seven HIT, one MISS, and the
MISS is mine** — arm Ⓒ registered the antipodal singularity as a *pole* whose residue is non-zero at
every finite parameter, and it is zero on a one-parameter sub-family. Its correction Ⓒ′ is below, marked
as added after the registration closed, and it carries the arm's conclusion by a different route.
`16` checks, `1` failure, the failure being that registered Ⓒ.

## The order, and the answer in one line

`r7615`: de Sitter's quantum field has a one-parameter family of invariant vacuum states, the
$\alpha$-vacua, the parameter is dimensionless, and Euclidean regularity on the compact face selects
Bunch–Davies. **Test whether any principle other than the face selects the same member** — the Hadamard
short-distance condition, regularity of the two-point function at the antipode, or a positive-energy
vacuum in the flat limit — with a control in which the selection is known to come from somewhere else.

**All three do.** Regularity at the antipode, the Hadamard condition and the flat-limit requirement each
select the member the compact face selects, and **none of the three carries any Euclidean content**: the
first two are statements about the two-point function's singular support, the third about a Bogoliubov
coefficient in which the curvature scale does not appear at all. So the face's selection is
**non-distinctive on this freedom**, this is the **fourth empty slot**, and it is the slot the order
itself calls the one the face looked most likely to fill.

## The corpus commits to the member without naming the freedom (Ⓐ HIT)

A net over **the eighteen papers read by their own map** (`69`'s `r7611` repair of the glob that pulled in
generated appendices) locates *"admits a clean, unitary Bunch--Davies quantization"* in `P11`, and finds
the family's own names — $\alpha$-vacuum, Mottola, Allen, antipodal vacuum — occurring **`0` times**. The
corpus takes the member and does not say there was a choice, which is why the order brings the family in
from outside.

## The family, and that it returns the member in its own limit (Ⓑ HIT)

Built symbolically in the conformally-coupled case, where $G_{\rm BD}\propto1/(1-Z)$ and the antipodal map
sends $Z\to-Z$:
$$\phi_\alpha=N_\alpha\bigl(\phi_{\rm BD}+e^{\alpha}\phi^{*}_{\rm BD}\!\circ A\bigr),\qquad
N_\alpha=(1-e^{2\operatorname{Re}\alpha})^{-1/2},\qquad \operatorname{Re}\alpha=a<0 .$$
As $e^{\alpha}\to0$ the two-point function is $-c/(Z-1)$, **exactly** the Bunch–Davies $c/(1-Z)$, and
$|N_\alpha|^{2}(1-|e^{\alpha}|^{2})=1$ at every sampled parameter — the unit-Wronskian normalisation, so
the family is a family of *states* and not of rescalings.

## Ⓒ as registered MISSES, and Ⓒ′ carries it (Ⓒ MISS, Ⓒ′ HIT)

The registered arm said *the residue at $Z=-1$ is non-zero at every sampled finite $\alpha$*. Measured,
the antipodal structure is a **pair**, with the two coefficients

| coefficient on the antipodal light cone | value |
|---|---|
| principal-value pole at $Z=-1$ | $-c\cos\theta/\sinh a$ |
| $\delta$-function on $Z=-1$ | $\pi c\sin\theta/\sinh a$ |

writing $e^{\alpha}=e^{a}e^{i\theta}$. At $\theta=\pi/2$ — a **purely imaginary** parameter — the pole
cancels between the two prescriptions and the residue is **zero**:

|  $a$  | $\theta$ | PV coefficient | $\delta$ coefficient |
|---|---|---|---|
| $-1/2$ | $0$ | $c/\sinh(1/2)$ | $0$ |
| $-1/2$ | $\pi/4$ | $\sqrt2 c/(2\sinh(1/2))$ | $-\sqrt2\pi c/(2\sinh(1/2))$ |
| $-1/2$ | $\pi/2$ | $0$ | $-\pi c/\sinh(1/2)$ |
| $-2$ | $\pi/2$ | $0$ | $-\pi c/\sinh 2$ |
| $-1/4$ | $\pi$ | $-c/\sinh(1/4)$ | $0$ |

So the registered reading is **wrong for a one-parameter sub-family**, and it is reported as a MISS rather
than quietly widened.

**Ⓒ′, the corrected arm.** What vanishes only in the Bunch–Davies limit is not the pole but **the pair**:
where the pole cancels a $\delta$-function on the antipodal light cone survives in its place, and the
magnitude $\lvert(\operatorname{Re}e^{\alpha},\operatorname{Im}e^{\alpha})\rvert=e^{a}$ goes to zero only
as $a\to-\infty$. **Regularity at the antipode therefore does select the face's member**, and the
registered arm had the right conclusion on a reading that does not hold everywhere. The discarded reading
is kept beside the correction.

## Hadamard (Ⓓ HIT)

The singular support of $G_{\rm BD}$ in $Z$ is $\{1\}$; of $G_\alpha$ it is $\{1,-1\}$, the second from
the antipodal terms above — as a pole, or as a $\delta$ by Ⓒ′, and either way a singularity. The local
Hadamard parametrix is built from the geodesic distance **at coincidence**, so its singular support is
$\{1\}$ alone and an antipodal singularity is nonlocal and cannot appear in it. The $\alpha$-vacua fail
the Hadamard condition and Bunch–Davies does not. **A short-distance condition, with no Euclidean input.**

## The flat limit (Ⓔ HIT)

$$\lvert\beta_\alpha\rvert^{2}=\frac{e^{2a}}{1-e^{2a}},\qquad
\frac{\partial\lvert\beta_\alpha\rvert^{2}}{\partial H}=0 .$$
The Bogoliubov coefficient **carries no curvature scale at all**, so its flat limit $H\to0$ is itself,
unchanged: the $\alpha$-vacua keep a non-zero particle content in the flat limit while the face's member
does not. The positive-energy flat-limit requirement selects the same member — and it does so on a
coefficient in which $H$ never appears, which is the sharpest form the "no Euclidean content" claim takes
in this revision.

## The controls (Ⓖ HIT, Ⓗ does not void)

**Ⓖ, the control the order asks for**, run on two further freedoms of the same quantisation:
the mode functions' **overall phase**, where $\partial_\lambda$ of the two-point function is `0` — a gauge,
selected by **neither** the face nor any principle; and the **Wronskian normalisation**, which the
canonical commutation relation forces to $W=i$ exactly with **no Euclidean input** — selected by
**something that is not the face**. With the $\alpha$-vacua, selected by the face **and** by three other
principles, the instrument sorts **three** cases apart, so "non-distinctive" is a measurement here and
not the only verdict the instrument can return.

**Ⓗ, the voiding control, does not void.** $G_\alpha-G_{\rm BD}$ at $a=-1/2,\theta=0,Z=0$ is
$-(2+2e^{1/2})/(1-e^{\alpha})\neq0$: the members are physically distinct, there is a real freedom here,
and the slot is a slot.

## What this does to the row, and what it does not

`r7608` named `PO-94`'s quantum half as a test — the Euclidean real form is an actual quantum sector
rather than a rhyme iff its data remove a freedom of the quantum theory, with physically distinct
members, that no other principle removes — and scored three slots empty. **This is a fourth**, and it is
the strongest candidate available: the freedom is dimensionless, so `P10`'s ledger arithmetic cannot empty
it the way it empties a value; its members are physically distinct; and the face's data do close it.

**The row's terminal clause — *every freedom the face could close is closed elsewhere* — comes one step
nearer on the strongest candidate yet, and is NOT declared fired.** What would fire it is a demonstration
over **all** such freedoms, and four instances are not that. The reply says how much nearer rather than
claiming the clause.

**No instrument is added**, per `r7471` and `r7577`. No parameter is pinned, so no `COMPUTES:` header is
owed, and no quote-pin key is minted — every sentence is located by containment. This result moves a
sentence about what is open, so **`r7577`'s standing rule applies** and the routed row text lands with a
re-read of the census row or not at all.
