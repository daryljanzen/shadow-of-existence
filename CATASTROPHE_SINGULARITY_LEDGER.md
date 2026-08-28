---
name: catastrophe-singularity-ledger
kind: FORWARD
current: r3517
job: The catastrophe / singularity-theory field-bake ledger — what bit, what bounced, and the boundary. One of the three fields listed but never thrown (the r3505 overnight order named it explicitly: catastrophe ×54). `OWED` 622.
sources: [cowork]
---

> **▣ FORWARD — the catastrophe bake, and part of the corpus.** *Three registers kept apart on
> purpose: **what bit**, **what bounced**, and **what the boundary is**. This is a field the corpus was
> never asked, and the overnight order named it in its own voice —* ***"the three never thrown:
> convexity ×143, algebraic geometry ×57, catastrophe ×54."*** *The catastrophe question is sharp here
> because the corpus's central object is a DOUBLE ROOT — the Nariai member, where the black-hole and
> cosmological horizons merge — and a double root of a one-parameter family is the textbook FOLD (A_2)
> catastrophe. So the field is not a stranger: the question is whether the corpus already WORKS the
> catastrophe content under other names, and where it stops.*
>
> **⌗ THE GUARD THE COLLISION ITSELF SETS.** *`P07` carries an explicit warning that `bifurcation` in
> this corpus is the GR **bifurcation sphere** of a Killing horizon, and that the degenerate (Nariai)
> horizon carries NO bifurcation sphere. So nothing here may be written as "the bifurcation at Nariai"
> bare — the catastrophe-theory fold and the GR bifurcation sphere are different objects that share a
> word, and `D4_fold_scaling` already respects that guard.*


## ⛭ THE BASELINE, MEASURED FIRST

**Nothing below was called a hole before the corpus was asked what it holds.** *Seventeen paper bodies,
comments and bibliography stripped, de-macroed, via `corpus/reach_baseline.py` (word-bounded counts
where the substring inflates — `fold` is ×435 raw but ×35 as a word, the rest inside `manifold`/
`unfold`/`fold`ing-as-a-verb).*

| present (word-bounded, genuine-candidate) | homonym-dominated | absent across all seventeen |
| --- | --- | --- |
| `double root` ×45 (P07×14, P03×12, P15×4, P16×4) · `degenerate critical` ×19 (P02×11, P03×4, P07×2) · `bifurcation` ×23 (P07×13, P02×9 — but see the guard) · `codimension` ×7 (P14×5, P12×2) · `turning point` ×24 · `Morse` ×1 (P02) · `unfolding` ×1 (p0) · `cusp` ×1 (P15) | `singularity` ×272 / `singular` (mostly spacetime/curvature — a physics homonym, NOT a catastrophe of a function) · `critical point` ×128 (P02×59 — the cycloid's) · `fold` ×35 | `catastrophe` · `swallowtail` · `butterfly` · `umbilic` · `Hessian` · `structural stability` · `germ` · `corank` · `saddle-node` (as a NAMED term) · `normal form` (as a NAMED term) |

⚠ **THE DOMINANT WORD IS A HOMONYM, AND THAT IS THE FIRST FINDING.** *`singular`/`singularity` ×600+
is the corpus's most-used vocabulary in this survey and almost none of it is catastrophe theory: it is
the **spacetime/curvature singularity** — a physics object — not a degenerate critical point of a
smooth function. A catastrophe bake that counted those as reach would be inventing depth. They are
kept apart explicitly below, paper by paper.*

⚑ **AND THE FIELD'S CORE CLAIM IS ALREADY WORKED.** *Before this bake, `D4_fold_scaling`
(`receipts/P07_CR_framework/`, run this pass, exit 0, 15 asserts) already classifies the Nariai double
root as a **FOLD (saddle-node)**: for the horizon cubic $h(r)=r^3-r+2M$ (gauge $\alpha=1$), at
$2M_c=2/3\sqrt3$ the double root sits at $r_c=1/\sqrt3$ with $h(r_c)=0$, $h'(r_c)=0$, $h''(r_c)=2\sqrt3\ne0$,
and the mass enters additively — the A_2 normal form — forcing the surface gravity to vanish as
$\kappa\propto\sqrt{2M_c-2M}$ (exponent $\tfrac12$ flat across four decades). So the catastrophe field
does not open empty: its central object is receipted. The bake's job is the READING — every paper named
— and finding where, past `D4`, the corpus's catastrophe content stops.*

---

## ⛭⛭⛭ REACH CLOSE — all seventeen papers WORKED or CHECKED-NEGATIVE by name (r3519)

*Four readers swept the seventeen bodies (P01/P02/P03/P05/P07 carriers; the other twelve). The field is
DEEP because its one object — the Nariai double root of the SdS horizon cubic, a FOLD (A_2) — is the
corpus's spine: two horizons coalesce at $\Lambda M^2=1/9$ (discriminant $\Delta=4-27(2M)^2=0$), $f=f'=0$,
$\kappa\to0$, geometry $\mathrm{dS}_2\times S^2$. Nearly every paper touches it. The homonyms are named
and set aside: spacetime/curvature `singularity` (a physics object, not a critical-point degeneracy),
`Thom`→Thomson scattering, `A_2/A_3`→Lie-algebra root systems (not the fold/cusp labels), `codimension`
→submanifold, `bifurcation`→GR bifurcation sphere, `unfold`→colloquial.*

| paper | status | where / why |
|---|---|---|
| `P01` | WORKED | `BH_causality`: the Nariai **double root** with $\kappa=0$; the simple-vs-double order split $f\sim\delta$ (p=1) against $f\sim\delta^2$ (p=2) — an explicit order-2 degeneracy (`P1_thermality_is_the_exponential_and_a_double_root_has_no_exponential`) |
| `P02` | WORKED | `janzen_circle`: the fullest **Morse** content — the cycloid $r=M(1+\cos z)$ critical points classified non-degenerate ($r''=\mp M\ne0$) **by Morse's lemma**; multiplicity order 2 (`P02_kretschmann_chain_rule`). Settles the cusp question: the turnaround is a Morse max, **NOT a cusp** |
| `P03` | WORKED | `SdS-slicing`: the fold split $f'(r_h)=0$ at the double root; Nariai = **singular point of the discriminant locus** (bifurcation set), $r_0=\pm1/\sqrt3$ (`Q5_nariai_on_the_locus`) |
| `P04` | **CHECKED-NEGATIVE** | `modern_parallax`: zero matches for any catastrophe term in the whole file — nothing to check |
| `P05` | WORKED | `groupoid`: the discriminant $\Delta=4-27(2M)^2$ stated, its zero = the two Nariai values = fold/bifurcation set; simple branch point ($d\Delta/d(2M)\ne0$) ⇒ monodromy a single transposition |
| `P06` | WORKED | `shadow_of_existence`: the double root where $f$ touches zero without sign change ($f=0,f'=0$); $\kappa$ and the photon-orbit Lyapunov exponent vanish at the degenerate horizon (L386–388, L468–470) |
| `P07` | WORKED | `CR_framework`: the fullest fold analysis — $f=f'=0$ at the double root (`P07_cube_root_two_is_the_2M_over_M`); one-parameter discriminant $\Delta(E)=4\alpha^4(\alpha^2(1-E^2)^3-27M^2)$ with an explicit crossing (`two_realisations`); the bead's inflection $d^2r/ds^2=0$; **`D4_fold_scaling`** (the fold + the $\kappa\propto\sqrt{\delta}$ law) |
| `P08` | WORKED | `slicing_operator`: the strongest explicit case — the versal cubic $r^3+pr+q$, discriminant $-4p^3-27q^2$ a square iff $p=0$, cover **branching where roots collide, monodromy $S_3$** (`order3_bridge`); the signed-root coalescence $3=2+1$ at scale $2/\sqrt3$ |
| `P09` | WORKED | `range_paper`: the Nariai tangency = double root at $\Lambda M^2=1/9$ where two horizon null surfaces merge, placed as the degenerate member of the vacuum kernel (L192) |
| `P10` | **CHECKED-NEGATIVE** | `canonical_time`: only "turning point" = WKB/instanton turning point (E=V), and "branch point" = the $r=0$ curvature singularity — both physics homonyms; no double-root/discriminant/degeneracy claim |
| `P11` | WORKED | `dynamics_paper`: the strata organised by root coalescence — the Nariai seam = locus where **two of three roots collide**, a fixed point of the root-permutation symmetry; the wall distinguished by carrying no colliding roots (L332) |
| `P12` | WORKED | `algebroid`: the Nariai double-root seam = the metric-singular inner boundary of the isotropy stratification, discriminant zero, isotropy jump $4\to6$, geometry $\mathrm{dS}_2\times S^2$ (L193) |
| `P13` | WORKED | `boundary_paper`: "two roots merge" at the Nariai crest, the family an $S_3$ permutation of the triple with the mass its $R$-odd value, the two coinciding at the coalescence (L374) |
| `P14` | **CHECKED-NEGATIVE** | `matter_sector`: every hit a homonym — "forced fold"/"four-fold" = generation/harmonic **count** (the $D$-dependence collapse, not $f'=f''=0$); `codimension`-one = Dirac submanifold; `A_2` = Lie; `Thom` = Thomson; `discriminant` = the quark/lepton mod-3 classifier. The coalescence it uses is inherited by citation, not stated here |
| `P15` | WORKED | `CR_cosmology`: the Nariai member = the **Ginsparg–Perry degenerate near-horizon limit** (the coincident-horizon double root), used to pin flat-$\Lambda$CDM, receipted (`P15_verify_geometry`, L1214/191) |
| `P16` | WORKED | `cosmogenesis`: the double root with its full degeneracy content — isotropy jump, geometry $\mathrm{dS}_2\times S^2$ — a property of the geometry kept apart from the crossing (L138) |
| `p0`  | WORKED | `geometric_core`: the discriminant $4-3r_0^2$-bounded **order parameter**, saturating at the Nariai double root, **explicitly contrasted with a quartic (Landau/cusp) potential** ("a quartic potential is unbounded; this order parameter is not") (`P0_the_order_parameter_is_the_offset_and_it_is_bounded_by_the_nariai_member`, L1055–1060) |

⇒ ***Seventeen of seventeen accounted for: FOURTEEN WORKED, THREE CHECKED-NEGATIVE.*** *Reach $=14/17$ —
among the deepest of any field, because the corpus's central object IS a catastrophe (the fold). The
three negatives are clean: `P04` has nothing; `P10`'s turning/branch points are WKB and curvature
homonyms; `P14`'s fold/codimension/discriminant/Thom are all homonyms (generation count, Dirac
submanifold, mod-3 classifier, Thomson).*

**⚑ THE FIELD'S OWN VERDICT, discharged this pass — `KT1` (new receipt, ALL PASS).** *The bake owed a
statement of where the catastrophe content STOPS. It stops at the fold, provably: (1) the Nariai double
root is A_2 ($h=h'=0$, $h''=2\sqrt3\ne0$); (2) **no cusp (A_3) is possible** — a triple root of the
depressed horizon cubic $r^3-r+2M$ would force its fixed linear coefficient $-\alpha^2$ to zero
($-3a=0\Rightarrow a=0$, then $3a^2=-1$ is a contradiction), so for NO mass does the family reach A_3;
(3) the cycloid turnaround is Morse-non-degenerate ($r''=\mp M\ne0$), and a cusp there would need
$\sin z=\cos z=0$ at once, impossible. So the classification is COMPLETE: the corpus's catastrophe is
exactly the fold, and P02's "not a cusp" is corpus-wide, not local. Cross-field: `KT1` builds on
`D4_fold_scaling` (P07, the fold + scaling law) and P02's Morse lemma; it duplicates neither — it adds
the completeness/impossibility statement. No correction owed to another field's receipt this pass.*

