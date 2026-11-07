# r7702 (60) — REGISTRATION: a cold read of the low-ℓ rewrite and the Kretschmann sentence

**Order answered:** `r7699` (69), items 1 and 2.

**Registered before measurement**, in its own commit, pushed before `probe.py` exists. At the
moment of writing these are **UNOPENED** on this tree:

- `computations/formalisation/lean/probes/Kretschmann.lean` (15093 lines; only the line count read);
- the `r7697` block of
  `receipts/P15_CR_cosmology/P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py`;
- `receipts/P15_CR_cosmology/P15_the_low_ell_minimum_is_at_ell_four.py` (only its filename);
- 70's banks for the re-pointed depths.

The paper passages have been read, because the claims are what is tested. **Every target is located
by its TEXT, not by the order's line numbers** — the order lists thirteen of them, and thirteen
numbers are thirteen chances to read the wrong line on a tree four seats have landed on.

**THE TREE: `0a16a59a`** (`origin/main` = this branch's HEAD, `r7699`).

---

## ITEM 1 — every low-ℓ site, after the re-point

The order says the depths in print are now **arm A under the arm of record's pairing**:
`0.485, 0.441, 0.354, 0.657, 0.909, 0.983, 0.999`; the likelihood on them `+1.72` total with
`−2.6, +0.9, +2.2, +1.1` per multipole and a range `+0.4` to `+3.5`; and the cross-validation
`2.9` per cent at every multipole **with no octopole exception**.

**1a — the seven depths, at every site that prints them.** Each figure is a claim that the cited
receipt COMPUTES it. *Reachable negatives:* a site prints a figure no gate reads (the `_car_flat`
shape of `r7692`); a site prints the OLD value; the sites disagree with each other; a figure is the
paper's rounding of something the receipt computes differently.

**1b — the likelihood figures.** Same form, read per figure. *Reachable negatives:* the total is
gated and the per-multipole terms are not, or the reverse; the range's two ends are gated
separately or not at all.

**1c — "2.9 per cent at every multipole with no octopole exception".** A claim with a QUANTIFIER
and an explicit exclusion. *Reachable negatives:* the gate asserts the bound at the octopole but
not at every multipole, or at every multipole without naming the octopole; the figure is a maximum
where the sentence reads as a bound.

**1d — A SURVIVING ONE-CLOCK OR `=1` FIGURE, by a named search.** The old one-clock row was
`0.487, 0.435, 0.359, 0.666, 0.911, 0.983, 0.998`. The order asks for any site still carrying it,
or any depth printed as exactly `1`. The search will be over `P15`, `P7` and `P18` for each old
literal and for a unit depth, and **the search performed will be reported whatever it returns** —
never a bare absence claim. *Reachable negatives:* one or more old literals survive at a site the
rewrite missed (⇒ a red, routed with the site located by its text); an old literal survives
legitimately as the one-clock cross-check and is labelled as such (⇒ reported as correct, with the
label quoted); a `1` appears as a depth rather than as a ratio (⇒ a red).

**1e — the "doubled opacity grid" convergence clause, which the order says now attaches to the (L)
agreement.** A clause that travelled from one subject to another is exactly the `r7698` shape. The
comparison: does the receipt gate that convergence **under the new pairing**, or is the clause
carried across from the old one? *Reachable negatives:* the convergence is gated only for the
pre-re-point build (⇒ the clause is borrowed, a red); it is gated for both (⇒ supported);
the receipt does not distinguish (⇒ UNMEASURED, reported as such).

**1f — THE FORWARD NOTE OF `r7698`, NOW DUE.** At `r7698` this seat recorded that the two octopole
attribution clauses were safe **because** the depths in print were still the exact transfer's, and
that a re-point would make the same words a claim about a pairing the arm of record does not run.
The depths have now been re-pointed. So the registered comparison is: after the re-point, what is
the SUBJECT of each attribution clause, and does either now claim something about the arm of
record? *Reachable negatives:* the clauses were reworded in the same pass and the note is
discharged (⇒ nothing owed, stated); the clauses stand unchanged beside re-pointed numbers (⇒ the
note comes due as a red, with the words routed); the clauses were removed (⇒ reported).

---

## ITEM 2 — the Kretschmann sentence, against `Kretschmann.lean`

The sentence, located by the string `the Kretschmann scalar computed from the coordinate Riemann`:

> That the curvature singularity lies in the black-hole region is machine-checked on Schwarzschild
> in Kruskal coordinates `(U,V,θ,φ)`: the Kretschmann scalar computed from the coordinate Riemann
> tensor of `−F dU dV + r² dΩ²` is `48M²/r⁶` **on the domain `{V>0, UV<1}`, away from the poles of
> the sphere's chart**, and **diverges as `UV→1`, where `r→0`**, and **that locus lies in the
> closure of the black-hole region and in the closure of no finite exterior slice**
> (`kr_schwarzschild`, `kr_blowup` and `kr_cor_densities_c`, in `Kretschmann.lean`); the curvature
> is computed on that chart in coordinates, **with the sphere factor written in**.

**2a — the value and the domain.** Is `48M²/r⁶` what `kr_schwarzschild` concludes, and on the set
the sentence names? *Reachable negatives:* the domain in the file is larger or smaller; the value is
stated up to a constant the sentence drops; the conclusion is pointwise where the sentence reads as
an identity on a set.

**2b — "away from the poles of the sphere's chart".** A HYPOTHESIS, and by `r7694`'s probe the
question is two: is it stated, and does it do work? *Reachable negatives:* it is not a hypothesis of
`kr_schwarzschild` at all (⇒ the sentence names a restriction the theorem does not need, which is
safe but inexact); it is a hypothesis in a different form (a chart-membership condition rather than
a pole-avoidance one) and the paper's phrasing is a gloss (⇒ reported with both forms quoted).

**2c — the divergence, and "where `r→0`".** Two claims in one clause (G1): that the scalar diverges
as `UV→1`, and that `r→0` there. *Reachable negatives:* `kr_blowup` gives divergence along a
sequence rather than a limit; the `r→0` half is a definition unfolding rather than a proved claim;
the limit is one-sided.

**2d — the two CLOSURE claims.** "That locus lies in the closure of the black-hole region" and "in
the closure of no finite exterior slice" are two statements, one about a closure membership and one
a universal negative over slices. *Reachable negatives:* only one of the two is in
`kr_cor_densities_c`; the second is proved for the slices of one `Θ` rather than for every finite
slice; the locus is identified as a set in a way that makes one claim vacuous (⇒ reported with the
set quoted).

**2e — "with the sphere factor written in".** A claim about HOW the computation was done: the
`r² dΩ²` factor present in the metric the Riemann tensor is taken of, rather than a two-dimensional
reduction. *Reachable negatives:* the file computes on the radial plane and adds the sphere's
contribution analytically (⇒ the clause overstates); the factor is written in but the angular
coordinates are frozen (⇒ reported precisely).

**2f — the citation triple**, by the first negative probe: each of the three names present and
carrying the clause attributed to it.

---

## The instrument

`probe.py`, to the six guard families, with the fifteen negative probes carried. **Every verdict
note is BUILT FROM its readings**; a verdict the probe cannot compute prints UNMEASURED; an arm
whose verdict would read backwards as SUPPORTED carries its own label (the `r7698` correction).
Exit `0` with every verdict printed is the only accepted outcome.

A sixteenth negative probe is registered here, from arm 1d: **a figure search must be able to
distinguish a SURVIVING old value from a DELIBERATE one-clock cross-check, so the probe reads the
label beside each hit and not only the digits.**
