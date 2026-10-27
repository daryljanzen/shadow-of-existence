# `r7619+cc66` — does the construction supply the cutoff function itself?

**Registered before a line of this row's computation exists.** As at `r7611`, `r7613` and `r7615`.

`r7615` left the gauge half with a field and no coupling, and `r7619` names the one candidate that
could still fix it: the spectral action is $\mathrm{Tr}\,f(D/\Lambda)$, its Yang–Mills coefficient is a
**moment of $f$**, and the construction supplies a trace of its own — the horizon's thermal state at
$\beta=2\pi\alpha$, a Gibbs weight. A thermal trace *is* a particular $f$, with $\Lambda$ set by $\beta$.
**So: is the face's thermal trace a spectral action for the `r7615` triple?**

---

## ⛭ WHAT THIS ORDER CHANGES ABOUT `r7615`'s ARGUMENT, STATED FIRST BECAUSE IT WEAKENS MY OWN RESULT

`r7615` closed the coupling by a **dimensional** argument: the face's data are two lengths, $\alpha$ and
$\beta=2\pi\alpha$, the exponents force $p_\alpha=-p_\beta$, and the only dimensionless monomial is the
ratio $2\pi$ — not a moment of a cutoff function.

⚠ **That argument does not reach $\Lambda$, and I did not notice.** $\Lambda$ is **not** dimensionless:
it is an inverse length, and $\beta^{-1}=1/(2\pi\alpha)$ is exactly that. **So the construction does
supply a $\Lambda$**, and `r7615`'s dimensional reasoning never ruled it out — it ruled out a
dimensionless *coupling* being formed from lengths, which is a different slot. ⇒ *The spectral action
needs two things, $f$ and $\Lambda$, and one of them the construction has. This row is therefore not a
re-run of `r7615` with a different label; it is the question `r7615` left genuinely open, and I am
registering that my own earlier framing understated it.*

---

## The source question — read from the papers before anything is computed

| what I need | where I looked | what it says |
|---|---|---|
| what $\beta=2\pi\alpha$ *is* | `boundary_paper.tex` | the de Sitter horizon's Gibbons–Hawking thermal state, *"a Euclidean continuation of period $\beta=2\pi\alpha$ — and that Euclidean is the **same** face"* |
| what generates the construction's evolution | `CR_framework.tex` | the deparametrized *true Hamiltonian*: *"the scalar constraint … takes the deparametrized form $p_\tau+H_{\mathrm{phys}}=0$ and is solved for the generator of advance, $i\,\partial_\tau\Psi=\hat H_{\mathrm{phys}}\Psi$"* |
| what `D` is | `P13` / my `r7615` | the face's Dirac operator, spectrum $\pm(5/2+k)/\alpha$, least eigenvalue $5/2\alpha$ |

⇒ **The first row is the one that makes this order non-trivial.** Because the Euclidean section *is*
the face, the thermal circle of circumference $\beta=2\pi\alpha$ is a **great circle of the face
itself** — the periodicity is internal to the manifold `D` lives on, not on some other space. *That is
the strongest form of the order's suggestion and it is the form I will test.*

⚠ **And the vocabulary is still mine.** `spectral action`, `cutoff function`, `Yang–Mills coefficient`
occur in no corpus paper and in no receipt but `B61`'s own absence list (measured at `r7615`). Nothing
to inherit, nothing to check my arithmetic against — the same exposure as `J` at `r7613`.

---

## THE QUESTIONS, PRICED BEFORE COMPUTING

| # | question | confidence |
|---|---|---|
| ① | Is the thermal weight's generator a **function of `D`**? (If $H=h(D)$ then $e^{-\beta H}=f(D/\Lambda)$ and the action is a spectral action.) | **medium-high it is NOT** |
| ② | Under the *most favourable* reading — the generator is translation along the face's own great circle of circumference $\beta$ — is it a function of `D` then? | **medium-high still NOT** |
| ③ | Does $\Lambda$ come out right dimensionally, i.e. is $\beta^{-1}$ an admissible spectral-action scale? | **high YES** — and this is what `r7615` missed |
| ④ | **If** ① or ② held, would the Yang–Mills coefficient then be fixed? | **high YES** — a definite moment of a definite $f$ at a definite $\Lambda$ |

**⚠ THE REACHABLE NEGATIVE, NAMED AS THE ORDER REQUIRES.** The thermal weight is on a *different
operator*: the Hamiltonian, not `D`. Under the corpus's own reading that operator is
$\hat H_{\mathrm{phys}}$, which generates advance along **cosmic time** and does not even act on
spinors over the face. So the trace is not a spectral action of this triple, and the gauge half then
rests on the composite route alone.

**⌗ WHERE I AM LEAST SURE, AND IT IS NOT WHERE `r7615` WAS.** Question ② is the live one. `D` commutes
with the Lie derivative along a Killing field, so the circle generator $H_\theta$ and `D` **do**
commute — and a naive reading could stop there and conclude $e^{-\beta H_\theta}$ is a function of `D`.
**Commuting is not being a function of.** A function of `D` is **constant on every `D`-eigenspace**, and
the test is therefore whether $H_\theta$ restricted to one `D`-eigenspace is a multiple of the
identity. ⇒ *That is countable and exact, and it is the hinge of the row: if $H_\theta|_{\ker(D-\lambda)}$
is scalar for every $\lambda$ the negative is wrong and the construction fixes a coupling.* I expect it
is not scalar — the `D`-eigenspaces of $S^5$ are large and carry many angular momenta — **but I am
registering the possibility that I am wrong, because this is the one question whose answer I cannot
predict from a dimension count.**

⌗ *And one asymmetry worth owning in advance: ④ means a positive answer here would **overturn my own
`r7615` verdict** on the coupling. I have an incentive to find the negative, so the controls below are
built to make the positive **visible** if it is there, not merely to certify the negative.*

---

## CONTROLS — five, and two of them exist because of what the last two rows cost

1. **A cutoff function that DOES fix a coupling.** The order asks for this by name. Take an explicit
   $f$ and compute the relevant moment in closed form, then show the coefficient **moves** when $f$
   changes. *Without this, "no $f$ means no coupling" is rhetoric rather than a measurement — the exact
   charge I levelled at a dimensional argument in `r7615` and must not now earn myself.*
2. **A pair of operators that ARE functions of one another**, where the "constant on eigenspaces" test
   must come back **positive**. If the test cannot say yes, its no is worthless. *This is `r7613`'s
   lesson: a checker that cannot certify a true instance certifies nothing.*
3. **A commuting pair that is NOT a function pair** — the discriminator for ②, showing that commuting
   and being-a-function-of come apart, so the hinge is measured rather than asserted.
4. **Non-vacuity on the eigenspace test**: the `D`-eigenspace used must be of dimension $>1$, since on
   a one-dimensional eigenspace **every** operator is scalar and the test would pass for free.
   *`r7615`'s second fault was exactly a test that could not fail; the guard goes in before the test.*
5. **$\Lambda$'s dimension solved, not asserted** — the same exponent solve as `r7615`, run on
   $[\Lambda]=[\text{length}]^{-1}$ rather than on a dimensionless coupling, so ③ is a measurement and
   the correction to `r7615`'s framing is itself checked.

---

## OUTCOMES, PRE-REGISTERED

1. **The thermal trace IS the spectral action** → a coupling the construction fixes, which meets the
   gauge half's test, and `r7615`'s coupling verdict is **overturned by this row**. I would report it
   that way, in those words.
2. **It is NOT** → the gauge half rests on the **composite/emergent** route alone, which is then the
   next order, and `B59`'s last untouched route becomes the only one left.
3. **It is not even comparable** — the weight acts on a different Hilbert space, so the question is
   ill-posed rather than answered negatively. *This is a distinct outcome from 2 and I will not let it
   be reported as 2: "not a spectral action" and "not the same kind of object" are different findings.*
4. **The corpus's own statements turn out incomplete** → larger than this row, **routed**, not claimed.

## SCOPE

No paper edited; the register row is `69`'s; instruments frozen per `r7577`. `PO-5` is **struck** and was
never the coupling's row — `69`'s correction at `r7619`, and my `r7615` line naming it was wrong; the
coupling sits inside `PO-94`'s gauge half. `B59` and `B61` now set aside sentences stating the face
result, so my prose may name it; it still stays out of the papers. The `C71`/`C81` census point stays
with the `P15` receipts' owner, my rename clearing it for now.
