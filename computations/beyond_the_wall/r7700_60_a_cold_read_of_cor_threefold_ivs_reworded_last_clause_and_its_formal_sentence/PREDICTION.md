# r7700 (60) — REGISTRATION: a cold read of `cor:threefold` (iv)'s reworded last clause and its formal sentence

**Order answered:** `r7697` (69).

**Registered before measurement**, in its own commit, pushed before `probe.py` exists. At the
moment of writing, `computations/formalisation/lean/probes/ThreefoldLocal.lean` is **UNOPENED** on
this tree: only its size (7902 lines) has been read, by `wc -l`. The two paper passages have been
read, because the claims are what is being tested and have to be quoted exactly to be tested at
all, and **both were located by their TEXT, not by any line number**.

**THE TREE: `91668f2d`** (`origin/main` = this branch's HEAD, `r7697`). Every line number and
character offset in this revision is a claim about that tree and no other.

---

## The two passages, quoted from `91668f2d`

**THE CLAUSE** (`cor:threefold` (iv)'s last clause), located by the string
`it is not fixed by the geometry`:

> Without this additional condition, the temporal separation `τ(q)−τ(p)` assigned by any smooth
> temporal function `τ` has no invariant geometric meaning: **it is not fixed by the geometry,
> smooth local deformations of `τ` in a neighbourhood of `γ` altering it while keeping `τ`
> temporal.**

**THE FORMAL SENTENCE**, located by the string `For the last clause of~(iv)`:

> For the last clause of (iv), **in finite dimension and on a Hausdorff manifold**: for a causal
> curve from `p` to `q`, a temporal function `τ` and any open set about `q`, the temporal functions
> equal to `τ` outside that set assign separations **filling an open interval about** the
> `τ(q)−τ(p)` that `τ` assigns, the deformation being a bump in a chart that leaves the function
> temporal (`tl_cor_threefold_iv_b` and `tl_separation_interval`, in `ThreefoldLocal.lean`); on the
> Rindler pair above, such a deformation changes the separation (`tl_witness`).

And the sentence that introduces the paragraph: *"Parts (i)–(iii), **the last clause of (iv)**, and
all four parts together on one pair, are machine-checked."*

---

## The arms, registered as COMPARISONS with no predicted verdict

No verdict is predicted for any arm. Each arm's reachable negatives are named, so that reaching
one is a RESULT and not a silence.

**A — the clause's two halves, one predicate each (G1).** "It is not fixed by the geometry" is an
INVARIANCE claim; "smooth local deformations … altering it while keeping `τ` temporal" is an
EXISTENCE claim about deformations. *Reachable negatives:* the theorem carries the existence half
and the invariance half is an inference the file does not state; the existence half is proved for
one deformation rather than for a family; the "while keeping `τ` temporal" rider is a hypothesis of
the theorem rather than a property of the deformations it produces.

**B — WHERE THE DEFORMATION LIVES: "in a neighbourhood of `γ`" against "any open set about `q`".**
The clause localises the deformation at the CURVE; the formal sentence localises it at the
ENDPOINT. These are different sets, and the difference decides whether `p` is inside the deformed
region. Registered as a comparison: what set does `tl_cor_threefold_iv_b` quantify over, and is a
neighbourhood of `γ` an instance of it, a special case of it, or neither? *Reachable negatives:*
the theorem's set must avoid `p`, so a neighbourhood of `γ` (which contains `p`) is NOT an instance
and the paper's localisation is wider than what is proved (⇒ a red, with its words); the theorem
allows any open set about `q`, `p` included, so the paper's is narrower and safe; the theorem is
stated for a neighbourhood of the curve after all, and the formal sentence's own wording is the
loose one (⇒ the red is in the sentence, not the clause).

**C — THE ORDER'S FIRST QUESTION: `q` in the open set; is `p` required outside it?** Read from
`tl_cor_threefold_iv_b`'s own hypothesis list, one hypothesis per reading. *Reachable negatives:*
`p ∉ U` is a hypothesis and the formal sentence does not say so (⇒ an omitted hypothesis, the
`r7694` family: the wholeness of a hypothesis list is two questions, stated and used); `p ∉ U` is
not required and the interval claim holds regardless (⇒ the result is stronger than the sentence
reads); the separation is defined so that `p`'s membership cannot matter (⇒ reported with the
definition quoted).

**D — THE ORDER'S SECOND QUESTION: is "filling an open interval about its value" what is proved?**
Read `tl_separation_interval`'s conclusion. *Reachable negatives:* what is proved is that SOME
deformation changes the value (a weaker, pointwise claim) and the interval is the paper's
strengthening; the interval is proved but is one-sided, or half-open, or not about `τ(q)−τ(p)`
itself; the interval is proved for a sub-family only. This arm must be able to answer both
OVERSTATED and UNDERSTATED — the twelfth negative probe.

**E — the setting: "in finite dimension and on a Hausdorff manifold".** `r7694` found exactly this
kind of clause borrowed rather than checked, so it is read against the section's own variable block
and the theorem's own instance arguments, never against the file's prose. *Reachable negatives:*
the section asks less (⇒ the claim understates and is safe but inexact); it asks more, e.g. a `C²`
atlas (⇒ a red, as at `r7694`); `FiniteDimensional` or `T2Space` is absent, so the sentence names a
hypothesis the theorem does not have (⇒ a red the other way).

**F — the witness.** Does `tl_witness` change the separation on the Rindler pair the paragraph has
already built? *Reachable negatives:* the witness is on a different pair or a different spacetime;
it exhibits a changed separation but not one inside the claimed interval; the name is absent on
this tree (⇒ the first negative probe).

**G — THE ORDER'S THIRD QUESTION: does anything else in P1 rely on "arbitrarily"?** A reliance
probe, which by the eighth negative probe must be able to answer NONE and still fire on an injected
site. The order names `l.140`'s "stays non-invariant" as the same claim; that is a reading to
check, not to accept. *Reachable negatives:* a site states the stronger "arbitrarily far" claim and
would now be unsupported (⇒ a red, routed with its words); every site states the weaker claim,
which is what the theorem gives (⇒ nothing owed, stated as a negative finding with each site
quoted); a site's wording is ambiguous between the two (⇒ reported as ambiguous with both readings).

**H — the scope sentence.** "Parts (i)–(iii), **the last clause of (iv)**, and all four parts
together on one pair, are machine-checked" — a claim about WHICH of (iv) is covered. *Reachable
negatives:* the file covers more of (iv) than the last clause (⇒ understated); it covers less; the
"all four parts together on one pair" half is carried by a theorem the sentence does not cite here.

---

## The instrument

`probe.py`, to the six guard families: **G1** one predicate per conjunct; **G2** three anchor forms
only, with ONE leading backslash for a control sequence and unanchored markers REFUSED; **G3** the
flip family; **G4** classifier probes tested on both classes; **G5** reader probes each with its
negative; **G6** every prose probe on a whitespace-FLATTENED copy. **Every verdict note is BUILT
FROM its readings.**

The fourteen negative probes are carried. A fifteenth is registered here, from arm B: **a
localisation claim names a SET, and two sets that both contain the point of interest can still
differ on whether they contain the other endpoint — so a "local" claim must be read as a claim
about its SUPPORT and not only about where it is centred.**

Exit `0` with every verdict printed is the only accepted outcome of the reading run; a verdict the
probe cannot compute prints UNMEASURED rather than being omitted, and an arm whose verdict would
read backwards as SUPPORTED carries its own label (the `r7698` correction).
