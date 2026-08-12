# F12 — P12's isotropy-3 stratum is six of the nine Bianchi types, and the sentence "the isotropy dimensions are the Killing-vector counts" is the one that notices

*status: OFFERED + BOUNDED NEGATIVE on one identifying sentence. F05 landing at a second site.*
*receipt: `DRAFT_P12_the_bianchi_stratum_is_six_of_nine.py`, rc=0 (F05's computation re-run, not quoted).*
*touches: P12 `sec:strata`; P8 `K9_isotropy_obstruction`; P9 `thm:bound`. Also closes a gap in `K8_orbit_type_filtration`'s enumeration.*

---

## Three parts of the corpus saying one thing between them

**P12 `sec:strata`** lists the isotropy filtration:

> *Type O (de Sitter, isotropy so(4,1), dimension ten), Type D (Schwarzschild–de Sitter R_t × SO(3),
> dimension four; Kerr–de Sitter, dimension two), **Type I (Bianchi, dimension three;** Zipoy–Voorhees,
> dimension two), and the wall (Type N, isotropy zero)* … **The isotropy dimensions are the
> Killing-vector counts the construction establishes.**

**F05** (batch 1) established against an explicitly built so(4,1) which three-dimensional real Lie
algebras embed. That list is complete — up to isomorphism the 3-d real algebras are the abelian
one, Heisenberg, the family R ⋉_A R² indexed by A's Jordan data, and the two simple ones, and F05's
spectral lemma covers the whole R ⋉_A R² family in one statement:

| | |
|---|---|
| **embed** | R³ (I) · aff(1,R)⊕R · R ⋉_I R² (V) · R ⋉_{λI+rot} R² (VII_h, all h) · sl(2,R) (VIII) · su(2) (IX) |
| **do not** | Heisenberg (II) · Jordan(λ,λ) (IV) · diag(1,h) for real ratio outside {0,1} — VI₀ among them |

**So the stratum P12 labels "Bianchi, dimension three" is six Bianchi types, not the
classification.**

**P8's `K9_isotropy_obstruction`** already carries the reason, one paper over. It kills its own
author's proposed general argument and gets the right statement out of the wreckage:

> Isotropy(c) ≅ { φ ∈ Isom(Ψ(c)) : φ preserves the second fundamental form } — *"a **subgroup** of
> Isom(Ψ(c)), and may be **proper**"* — with equality *"at exactly the strata whose symmetry is
> large enough to fix the extrinsic data too, and **P12 tabulates precisely the high-symmetry
> strata**."*

And K9 names the place it expects to fail: *"the UNTABULATED ones are the LOW-SYMMETRY ones: **the
Type-I classes**, the wall."* Type I **is** the Bianchi stratum.

> **K9 says the identification can fail and where. This says which geometries, and counts them.**

## Where the identification parts

| stratum | isotropy dim | Killing vectors | equal? |
|---|---|---|---|
| Type O (de Sitter) | 10 | 10 | yes |
| Nariai SO(2,1)×SO(3) | 6 | 6 | yes |
| Type D SdS R_t×SO(3) | 4 | 4 | yes |
| Type I Bianchi *(the six)* | 3 | 3 | yes |
| Type D Kerr–dS / Zipoy | 2 | 2 | yes |
| wall Type N | 0 | 0 | yes |
| **Bianchi II / IV / VI_h** | **≤ 2** | **3** | **no** |

A Bianchi II geometry has three Killing vectors and perfectly homogeneous matter; its substrate
isotropy is at most two, because the Heisenberg algebra is not in so(4,1) while its abelian R²
subalgebras are.

**Every row P12 tabulates is right.** The sentence that is not general is the one identifying the
column headings.

## A conditional prediction, stated because it is checkable

F05 left one question open and this does not close it: whether a Bianchi II geometry is a cut at
all, via a **G₂ sweep** rather than its own G₃ — `cor:radiation` does put the two-Killing-vector
stratum inside the range. **If it is, it enters P12's filtration at isotropy dimension two, beside
Kerr–de Sitter and Zipoy–Voorhees, while carrying three Killing vectors.** That would be the first
entry in the table whose stratum sits below its symmetry, and it is the concrete form of K9's
abstract gap.

## And one small closure, offered rather than a correction

`K8_orbit_type_filtration` establishes the admissible symmetric-pair dimensions of so(5,1) as
**{6,7,10}** by enumerating so(p′,q′)⊕so(p″,q″) with p′+p″=5, q′+q″=1. Reproduced exactly.

**That is one family of involutions.** An orthogonal algebra also admits the complex-structure
(u-type) involution, which for so(5,1) would give **u(2,1), dimension nine** — and would break
{6,7,10}. It does not arise, and elementarily: a u-type involution needs an orthogonal complex
structure J on the defining representation, and J-invariance of the metric forces the signature to
be (2a, 2b). **The signature is (5,1) and 5 is odd, so no such J exists.**

So the enumeration is complete and {6,7,10} stands. The receipt's argument is **closed, not
corrected** — worth adding as a line, because "we enumerated one family" and "we enumerated them
all" are different claims and the paper leans on the second.

## Recommended, stated for reversal

1. In `sec:strata`, say **which** Bianchi types the isotropy-3 stratum holds — six, and name the
   excluded three. It is a clause.
2. Qualify *"the isotropy dimensions are the Killing-vector counts"* with K9's own condition (it is
   already in the corpus, in P8, and P12 does not cite it here). The honest form is: *equal on
   every stratum tabulated below, by K9's criterion; not equal in general.*
3. Add the u-type line to `K8b`/`K8` so the {6,7,10} enumeration is complete rather than
   family-restricted.

## Not claimed

- No new computation beyond F05's, which is re-run in the receipt rather than quoted.
- No claim that Bianchi II/IV/VI_h lie outside the range — that is F05's open question and stays
  open. The table's last row is conditional and is marked so.
- No claim that any tabulated stratum is wrong.
- Nothing about the physical universe: the sky is isotropic to 3×10⁻⁶ (P4).
- No closure on any registered item.
