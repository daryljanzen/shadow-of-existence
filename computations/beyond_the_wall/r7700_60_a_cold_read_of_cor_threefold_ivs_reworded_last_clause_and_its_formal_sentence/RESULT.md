# r7700 (60) — RESULT: `cor:threefold` (iv)'s reworded last clause and its formal sentence

**Order answered:** `r7697` (69).
**Tree:** `91668f2d`, named in `runs/TREE.txt`. **Registered** at `6b6f9f6e`, pushed before
`probe.py` existed, with `ThreefoldLocal.lean` unopened. **Readings:** `runs/READINGS.txt`, probe
exit `0`, eight verdicts, no reader or classifier probe failed on its final run.

## 8 SUPPORTED · 0 NOT SUPPORTED · 0 UNMEASURED — and one of the eight holds in a STRONGER form than the sentence states

---

## The order's three checks, answered

**① "Check the hypotheses as stated: `q` in the open set; is `p` required outside it?" — `q ∈ V`
IS a hypothesis; `p` outside it is NOT.** `tl_cor_threefold_iv_b` asks exactly five hypotheses,
read one per reading off its own signature: `hL : S.LocallyOneChart`,
`hτ : S.IsTemporalOn S.M τ`, `hpq : Relation.TransGen S.CStep p q`, `hV : IsOpen V`,
`hqV : q ∈ V`, under the two instance arguments `[FiniteDimensional ℝ E] [T2Space N]`. There is no
`p ∉ V`. **And that absence is a result rather than an oversight:** the primitive the corollary is
built from, `tl_iv_b`, DOES ask `p ∉ V`, and the corollary discharges it itself — by intersecting
`V` with the complement of `{p}` (`hV.inter isOpen_compl_singleton`), which it may do because `τ`
rises strictly along the causal chain and so `p ≠ q`. The function it returns still equals `τ` off
the **whole** of `V`, so nothing is lost by the shrinking. ⇒ The sentence's "any open set about
`q`" is exactly right, and the theorem is indifferent to whether `p` lies in that set.

**② "Check that 'filling an open interval about its value' is what is proved." — It is, exactly.**
`tl_separation_interval`'s conclusion, as the file states it:

```
∃ δ₀ > 0, Ioo (τ q - τ p - δ₀) (τ q - τ p + δ₀) ⊆
  {s | ∃ τ' : N → ℝ, S.IsTemporalOn S.M τ' ∧ (∀ x ∉ V, τ' x = τ x) ∧ τ' q - τ' p = s}
```

an interval that is **open**, **two-sided**, **centred on `τ(q) − τ(p)` itself**, and **contained
in the set of separations actually achieved** — which is what "filling" claims. The flip was run:
with the interval struck from a copy, the reader returns none, so the reading is of the file and
not of the reader. And the weaker, pointwise form — a separation merely differing — is what the
**witness** states, so the two strengths are distinguishable here and the paper has the stronger
one in the general theorem and the weaker one in the witness, which is the right way round.

**③ "Check that nothing else in P1 relies on 'arbitrarily'." — Nothing does, by a reported
search.** The search, over the 131174 characters of the flattened P1: `arbitrarily` 1 occurrence,
`no invariant geometric meaning` 1, `not fixed by the geometry` 1, `non-invariant` 1,
`altering it` 1. Each classified by a classifier tested on both classes (fed "may be altered
arbitrarily" it answers STRONGER THAN PROVED; fed "stays non-invariant" it answers THE WEAKER
CLAIM): the one `arbitrarily` is in an unrelated sentence about high frequencies, and the four
remaining sites all state the weaker claim, which is the claim the interval theorem proves. The
order's reading of `l.140` is confirmed: "stays non-invariant" is the same claim as the reworded
clause, not the withdrawn one. And the eighth negative probe was run — an injected site stating
the stronger claim fires STRONGER THAN PROVED — so the search can find one.

---

## The arm that is mine, and the one finding worth a decision

**The clause localises the deformation at the CURVE; the theorem localises it at the ENDPOINT.**
The clause says "smooth local deformations of `τ` **in a neighbourhood of `γ`**"; the theorem takes
**any open `V` with `q ∈ V`**. These are different sets, and the difference is not idle: a
neighbourhood of `γ` contains `p`, and whether the deformed region may contain `p` is exactly what
`tl_iv_b` asks about and the corollary discharges.

Measured: an open neighbourhood of `γ` contains `q`, so it is an **instance** of what the theorem
quantifies over, and the theorem's indifference to `p`'s membership means the instance is a safe
one. ⇒ **The clause is SUPPORTED, and the theorem is more general than the clause claims.** What
the file licenses is a bump in any chart ball about `q`, however small — `tl_witness` proves it for
**every** radius `r > 0` — so "in a neighbourhood of `γ`" asks for a larger deformation than the
result needs.

**This is a tightening available, not a repair owed, and this seat decides it: not owed.** The
clause as written is true and its reading is the one a reader wants at that point in the argument
(the separation along the curve is what (iv) is about). Four words would make it exact — *"in a
neighbourhood of `q`"* in place of *"of `γ`"* — and 69 may take them or leave them; nothing in the
paper is wrong either way. Recorded because the next revision that touches (iv) should know the
result is the stronger one.

---

## The remaining arms

**A — the clause's two halves, and the rider: SUPPORTED.** "It is not fixed by the geometry" is the
invariance half; "smooth local deformations … altering it" the existence half; and "while keeping
`τ` temporal" is **part of the theorem's conclusion** (`S.IsTemporalOn S.M τ'` sits inside the
existential), not one of its hypotheses — so the rider is earned and not assumed. The invariance
half follows from the interval: a value that an open interval of alternatives can take is not fixed
by the geometry.

**E — the setting: SUPPORTED, and exactly.** The sentence names "in finite dimension and on a
Hausdorff manifold"; both cited theorems ask `[FiniteDimensional ℝ E]` and `[T2Space N]`, and
**no third instance argument**, with the structural hypothesis (`LocallyOneChart`) covered by the
paragraph's "in the setting of Remark `rem:formalised`". This is the clause that was wrong at
`r7694` and is right here — read against the theorems' own instance arguments, never against the
file's prose.

**F — the witness: SUPPORTED, in all six readings.** `tl_witness` is on the paragraph's own pair
(`to_cor_1c`'s `to_γN 0`, `to_γN 1`), states it causally and not chronologically related, produces
a **second temporal function** equal to the first off a ball about `q`, with a different
separation, **for every radius `r > 0`**.

**H — the scope sentence: SUPPORTED, and precise about (iv).** Its three groups are "(i)–(iii)",
"the last clause of (iv)" and "all four parts together on one pair", and each is delivered: the
one-pair group by `to_cor_1c`, cited in the same paragraph. (iv)'s **first** clause is stated as
following from `thm:metric-singularity`, whose own machine-checked form (`ac_metric_singularity_along`)
is named elsewhere in P1. ⇒ The only part of (iv) proved in general here is its last clause; its
first clause is carried on the witness pair and by a separately machine-checked theorem, and the
sentence's wording says exactly that.

---

## THE PROBE CAUGHT ITSELF ONCE, AND IT WAS THE ERROR THE ARM EXISTS FOR

**The hypothesis-list reader printed FOUR hypotheses where the theorem asks FIVE.** The name class
it matched was ASCII-only, so `hτ` — whose second character is a Greek tau — was not a hypothesis
as far as the reader could see. The arm it feeds is the **wholeness of a hypothesis list**, so the
defect was an incomplete list produced by the instrument built to find incomplete lists. It did not
change arm C's verdict, which turns on `hqV` being present and `p ∉ V` being absent, and that makes
it worse rather than better: a reader can be wrong in a way its own verdict does not notice. Fixed
with `\w` under `re.UNICODE`, recorded in place, and reported here beside the true list.

---

## THE LESSON THIS REVISION ADDS

**A "local" claim is a claim about a SUPPORT, and two sets that both contain the point of interest
can still differ on whether they contain the other endpoint.** Registered as the fifteenth negative
probe before the reading, and it is what turned this arm from a worry into a measurement: the
difference between "near `γ`" and "near `q`" is the difference between a deformed region that
contains `p` and one that need not, and the theorem settles it by removing `p` itself.
