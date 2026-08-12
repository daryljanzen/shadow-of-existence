# F05 — Three of the nine Bianchi symmetry algebras cannot act as sweeps at all

*status: OFFERED — one proved fact and one sharp question. NOT a negative on `thm:range`; see "what I nearly wrote" below.*
*receipt: `DRAFT_P09_which_homogeneous_cosmologies_are_cuts.py`, rc=0.*
*touches: P9 `thm:bound`, `thm:range`, `cor:wall`; `prop:surj`. `check_kills` run before writing — 12 protected items, no unauthorised closures.*

---

## What sent me here

P8's `K9_isotropy_obstruction` is one of the best receipts in the set: it kills its own author's
proposed general argument and gets a *better* result out of the wreckage — Isotropy(c) is the
subgroup of Isom(Ψ(c)) preserving the **second fundamental form**, and may be proper. Reading it
against P9's `thm:bound` I noticed the phrase

> the Kantowski–Sachs group and **the abelian translation groups** (homogeneous cosmologies)

The Bianchi classification has nine three-dimensional symmetry algebras and exactly one of them
is abelian. Nothing in the corpus says what that word costs — `bianchi` occurs 14 times across
the whole tree and **every one is type I**.

## The proved fact

Built `so(4,1)` explicitly (10 generators, `A^T η + η A = 0` verified) with its Iwasawa frame
`g = n̄ ⊕ (m ⊕ a) ⊕ n`, all bracket relations checked.

**The spectral lemma.** Over 4000 random X ∈ so(4,1), the *real* eigenvalues of ad_X are always
exactly {−c, 0, +c} for a single c — never any other ratio, and never more than two distinct
nonzero real values. (so(4,1) has real rank one; this is that fact in the shape the question
needs.)

A three-dimensional algebra R·X ⋉ u with u abelian two-dimensional is fixed up to isomorphism by
the Jordan data of A = ad_X|_u, up to scale. By the lemma its real eigenvalue ratio can only be
**0, +1 or −1** — and ratio −1 is killed separately, because it needs an abelian u pairing a
(+c)- with a (−c)-eigenvector, while [N_v, N̄_w] = ⟨v,w⟩H + (v∧w) vanishes only if v and w are
both orthogonal *and* parallel (smallest normalised bracket over 20 000 random pairs: 0.707).

Two more killed by direct computation:

- **Heisenberg (II).** For a nilpotent Z, dim C(Z) = 4 and dim[C(Z),C(Z)] = 2, and adjoining Z
  raises the rank to 3 — so **Z ∉ [C(Z),C(Z)]**, and no X,Y ∈ C(Z) have [X,Y] = Z. Every nonzero
  nilpotent of so(4,1) is a null rotation conjugate to this one, so one computation settles all.
- **Jordan(λ,λ), λ≠0 (IV).** A nilpotent commuting with cH must lie in ker(ad_H) = so(3) ⊕ R,
  which contains no nonzero nilpotent (verified: 0 found in 20 000 draws). So X = cH exactly,
  ad_X|_n = cI, diagonalisable. With an elliptic part present the +c eigenvalue is simple and its
  generalised eigenspace cannot hold a 2-dimensional u.

Positive embeddings exhibited and verified (relations, independence, membership in so(4,1)):

| algebra | Bianchi | realisation |
|---|---|---|
| R³ | I | u = n |
| aff(1,R) ⊕ R | (label convention-dependent) | H ; N₁ ; so(2) fixing e₁ |
| R ⋉_I R² | V | H ; N₁, N₂ |
| R ⋉_{λI+rot} R² | VII_h, every h | λH + so(2) ; N₂, N₃ |
| sl(2,R) | VIII | so(2,1) in the (X⁰,X¹,X⁴) block |
| su(2) | IX | m = so(3) |

> **Embeds (can be the sweep): I, V, VII_h (all h), VIII, IX, aff(1,R)⊕R.**
> **Does not embed (cannot be the sweep): II, IV, and VI_h for every real eigenvalue ratio
> outside {0, 1} — VI₀ among them.**

And the reachable list has a shape: every one of them sits inside so(4), so(3,1) or e(3) — the
three FLRW isometry algebras `thm:bound` already names — with the single exception of
aff(1,R)⊕R, which needs three transverse directions and so needs the full so(4,1).

*(Label caution, stated rather than glossed: the Bianchi numbering of the class-B algebras
differs between references. The result is stated in the convention-free form — the Jordan data of
A — and the labels are a reading of it. Anyone landing this should fix the convention against the
reference the paper cites, not against my receipt.)*

## What I nearly wrote, and why it is wrong

My first draft concluded:

> *a Bianchi II cosmology has three Killing vectors and perfectly homogeneous matter and is not a
> cut, so the boundary of the range is strictly inside the loss of continuous symmetry.*

**That does not follow, and the paper is why.** `thm:range`'s hypothesis is that the isometry
group **contains** a sweep-subgroup — not that it *is* one. The Heisenberg group contains abelian
R² subgroups, which embed in so(4,1) without difficulty, and `cor:radiation` says explicitly that
the two-Killing-vector stratum is inside the range (*"the cylindrical Einstein–Rosen and Gowdy
waves, type I with two Killing vectors, hence in the reachable sector"*), with P11 building the
polarized Gowdy–de Sitter cut and working its dynamics.

So a Bianchi II geometry could still be a cut — of a G₂ class rather than of its own G₃. I record
the near-miss because the discipline that caught it was the corpus's own: read the theorem's
hypothesis, not the gloss you remember.

## What is offered, at its own size

**① A fact the corpus does not carry.** Three of the nine Bianchi symmetry algebras cannot act as
sweeps at all. Not *"are not reached"* — **cannot be the sweep**. For those types, if the geometry
is in the range it is there by a *proper* subgroup, which is a structurally different situation
from the six that can be swept by their own full symmetry.

**② A sharp, cheap question.** *Is a Bianchi II (or IV, or VI_h) cosmology a cut of a G₂ class?*
`prop:surj` cannot answer it — it opens *"Let H be a **reachable** symmetry class"*, so it
presupposes the answer. If **yes**, `thm:range`'s closing gloss survives and the corpus gains a
nice result: a homogeneous geometry reached through less than its own symmetry. If **no**, the
gloss needs narrowing and the range acquires a named remainder *inside* the symmetric sector.
Either answer is worth having and neither is written down.

**③ A wording note.** `thm:bound` says *"the abelian translation groups (homogeneous
cosmologies)"*; retired material says *"the whole reducible catalogue (SdS, Kerr–NUT–(A)dS, Weyl,
**Bianchi**, Kantowski–Sachs, FLRW)"*. The bare word reads as the classification while the
corpus's Bianchi content is type I throughout. Naming which types the parenthesis covers costs a
clause.

## Not claimed

- Nothing about the physical universe. P4 measures the foliation and the redshift isotropy is
  below 3×10⁻⁶; our cosmology is not a Bianchi II. Any cost here is to a *classification* claim.
- `thm:bound` is unaffected and was already right — it names the reachable classes explicitly and
  says *abelian*. This receipt is the price of that word, computed.
- `prop:surj` is unaffected.
- No closure on any registered item; no claim that the excluded algebras are absent from general
  relativity (Bianchi II vacuum is the Taub solution).
