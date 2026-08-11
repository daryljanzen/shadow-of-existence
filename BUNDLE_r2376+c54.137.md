# BUNDLE — r2376+c54.137
*The c54 fork of the Cosmological Relativity programme, cut where the collapse-perturbation arc terminates: $F$ computed, the amplitude closed as a negative, and the progenitor's composition bracketed on both sides.*

**HEAD:** `9c634cd r2376+c54.137 -- F is computed: the progenitor's own vacuum is negligible too, and the parent's composition is bracketed on both sides`
**Cut:** 2026-08-10 · node c54

---

## ⌗ WHY THIS CUT

The c54.134 bundle was cut mid-arc, with $F$ named as the next step and the amplitude untouched.
**This one is cut where that step lands** — and it lands as a negative that repairs an argument the
corpus had been leaning on, together with the first two-sided constraint the programme has ever
carried on an inherited datum.

```
LEAD REGISTER: 166 registered · 162 struck · 4 open · 0 HOT
  struck fraction: 97.6%   (reported so it cannot quietly fall)
  HOT fraction of open: 0.0%  (ceiling 34%)
  FALSIFIERS DELIBERATELY ORDERED: 1 (L-171)
```

Ten gates, all green at the cut, and 17/17 papers compiling at 0 errors, 0 undefined citations,
0 undefined refs, 0 dead receipt links.

| gate | rc |
|---|---|
| `check_receipts` | 0 |
| `check_kills` | 0 |
| `check_burndown` | 0 |
| `check_currency` | 0 |
| `check_queues` | 0 |
| `check_grains` | 0 |
| `check_supersession` | 0 |
| `check_withdrawn` | 0 |
| `check_citations` | 0 |
| `check_compile` | 0 |

---

## ⌗ WHAT THIS CUT CARRIES THAT c54.134 DID NOT

**$F$ IS COMPUTED (c54.137).** The collapse-side background is a single function,
$a=M(\rho|\sigma|+\sigma^2/2)$, whose Mukhanov–Sasaki potential $2/(|\sigma|(|\sigma|+2\rho))$ is
**mass-free** — so $M$ enters only through the final division $\zeta=v/a$. The passage has exactly
three stages and each contributes one factor of $1/\rho$: the freeze on the $\beta=2$ leg; the
connection through equality, elementary because $v=a\int d\sigma/a^2$ solves the $k=0$ problem in
closed form and carries $D_k/|\sigma|$ to the constant $(3/2\rho)D_k$; and the crunch monodromy
$2\pi/\rho$ — with $a'(\eta_c)=-M\rho$ supplying the third. **The transfer law is
$\mathcal{P}=(9/2)k^3D_k^2/(M^2\rho^6)$, exactly scale-invariant on vacuum data.**

**AND IT CARRIES NO FIXED NORMALISATION.** On the progenitor's own vacuum it returns
$3\times10^{-103}$ against an observed $2\times10^{-9}$: short by $10^{94}$. So the classical,
non-vacuum character of the primordial statistics is now **derived for the source that actually
supplies them** — P15's `prop:amplitude` had established it only for the *substrate's* vacuum, which
is the one vacuum the inheritance story was not claiming. **And `L-173`'s hoped inversion is dead
with a cause of death: $A_s$ does not measure the parent's mass.**

**TWO CORRECTIONS TO c54.133, BOTH OFF THE SAME BACKGROUND.** The upper bound used the wrong
criterion — $k_\times$ is where two *blue* branches trade places, whereas the observable is the
**break** at $k=1/\rho$, where the flat branch stops existing — giving $\rho\le1.1\times10^{-3}$,
tenfold tighter, with the two independently-normalised branches matching at the break to $9/4$. And
`L-172`'s nucleosynthesis check had imported *our own* $T_{\rm eq}$ for the *parent's* leg; the
parent's follows from its own $A$ and $\rho$, and computing it gives a lower bound.
**$2.6\times10^{-6}\le\rho\le1.1\times10^{-3}$ — the child's spectrum from above, the parent's own
abundances from below.**

**THE STANDING MASS ITEM GAINS ITS FOURTH LEG.** `THE_PLAN`'s r2091 item asked for a proof, not a
shrug, that nothing determines the progenitor's mass. It had three legs — no asymptotic mass exists to
be inherited; $M$ is forced to Nariai by the slicing; the invariants are blind to it. **The fourth is
that no observable determines it either**, the amplitude having been the only candidate.

**FOUR GRAINS PROPAGATED.** `THE_PLAN`, the open-problems ledger, the open-problems map and the weave
all sat 11–20 revisions behind the register through this arc; the top grain had crossed
`check_grains`' own window. All four now carry the arc.

**BASE-RATE ENTRY EIGHT.** The other seven entries are about a true statement failing to propagate.
**This one is the reverse: a statement that propagated perfectly, into text that leaned on it for more
than it proved.** A proposition is load-bearing exactly to the width of its hypothesis, and prose does
not carry hypotheses.

---

## ⌗ WHAT REMAINS OPEN — *four rows, seven fronts, ranked; see `THE_WORK.md`*

1. Can the collapse **produce** the composition it needs (`L-150`)?
2. ✔ What the sky permits of the parent — **answered, both sides** (`L-150`).
3. Is the leading-order interior good enough — anisotropy untested (`L-150`).
4. The ultraviolet definition of the graviton tower sums (`L-165`).
5. The closed-form nonlinear $\Lambda>0$ solution (`L-165`).
6. The two internal acoustic routes, $\ell_1=220$ vs $150$ (`L-171`, deliberately ordered).
7. The likelihood comparison against $\Lambda$CDM (`L-147`, fenced, last).

---

## ⌗ CONTENTS

Same layout as every c54 bundle: `corpus/` (17 papers + figures), `computations/`, `receipts/`
(`INDEX.md` the source of truth; Appendix R generated, never hand-kept), and the standing `.md`
layer. Compiled PDFs and LaTeX artefacts are excluded as regenerable —
`cd corpus && latexmk -pdf <paper>.tex`.
