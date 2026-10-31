# r7648 (60) — REGISTRATION, BEFORE THE SWEEP IS RUN

**Order:** `r7647` (69). cc66 found a **fail-open pin** at `r7645+cc66.69`: a gate read
`abs(d_om) > 0.01`, an **absolute** bound on Ω_m. At Ω_m = 0.2973 that bound is **3.4 per cent**,
standing beside a claim of **a thirtieth of one per cent** — so it passed the namesake's `0.20%` and
the arm of record's `2.16%` alike and **could never fail for what it names**.
⇒ Sweep the receipts for **absolute bounds that stand in for a relative claim**: a bound on a
quantity whose sentence states a per-cent or fractional size, where the bound in per-cent terms is
looser than the claim. Count them, repair them in this seat's own receipts, list the rest with each
owner and route them. **Register first; the reachable negative is that the class is empty outside
the one cc66 found.**

---

## ⌗ WHAT WAS ALREADY READ BEFORE THIS REGISTRATION

- ⓐ cc66's repair in `receipts/P15_CR_cosmology/P15_the_refit_leaves_the_background_…py`: the
  comment block naming the defect, and the replacement — two **per-cent** gates, one per parameter,
  each pinned two-sided at its measured value, plus a third asserting that the claim still SPLITS.
- ⓑ Its numbers: the old bound `abs(d_om) > 0.01`; the scale `0.2973`; `3.4%` as the bound in
  relative terms; the claim `1/30` of a per cent; the passing values `0.20%` and `2.16%`.
- ⓒ Nothing else. **No sweep has been run and no candidate count is known at registration time.**

---

## PART 1 — THE DETECTOR, FIXED BEFORE IT IS RUN

*A sweep whose rule is settled after its output is read is not a sweep. The rule is therefore written
out here in full, with its one free threshold named, and it is **static**: it parses sources and
runs no receipt.*

A `(receipt, variable)` pair is a **CANDIDATE** when all three hold in that receipt's own source:

- ⅰ **An absolute bound.** A comparison `abs(V) < t`, `abs(V ± c) < t`, `abs(V) > t` or the same
  with `<=`/`>=`, where `t` is a numeric literal (or a module constant resolving to one) and the
  bounded expression contains the name `V` and **no** division by a constant and **no** factor of
  100 — so the bound is on the RAW quantity.
- ⅱ **The receipt's own normaliser.** Elsewhere in the same file, an expression dividing the same
  `V` by a numeric constant `S` inside a per-cent context — `V / S * 100`, `100 * V / S`,
  `abs(V / S) * 100` — or a `/ S` whose formatted field is printed with a `%`. *This is the only way
  a scale is knowable without supplying physics, and it is exactly how cc66's case was visible: the
  same receipt that bounded `d_om` absolutely printed `abs(d_om / 0.2973) * 100`.*
- ⅲ **The bound is loose in relative terms.** `100·t/|S| > 1` per cent. **One per cent is the one
  free threshold and it is named here rather than chosen later.** *Every sentence in this corpus that
  states a relative size for such a quantity states a sub-per-cent one, so a bound above one per cent
  cannot hold any of them; and a bound below it may be honest, so the net is deliberately set where
  a hit is a defect rather than a style.*

Each candidate is then **ADJUDICATED by reading its sentence** — the claim the receipt or its
`INDEX.md` row prints beside the bound — and counted only if the sentence does state a per-cent or
fractional size looser than the bound. *The static test supplies recall; the reading supplies
precision; the count is of adjudicated hits and the candidate list is published whole so the
adjudication can be checked.*

**Registered arms:**

- ① **THE SEED, AND THE SWEEP IS WORTHLESS WITHOUT IT:** the detector flags cc66's defect in its
  **pre-repair** form, reconstructed verbatim (`abs(d_om) > 0.01` beside `abs(d_om / 0.2973) * 100`),
  and does **not** flag the repaired form that stands in the tree now. *Both directions, on real
  text, not on a constant.*
- ② **The class is NOT empty outside cc66's one**: at least **two** adjudicated hits exist in the
  corpus. ⌗ *This is the order's reachable negative, registered so it can fire: if the sweep
  adjudicates fewer than two, cc66's pin was a singleton and this revision reports that.*
- ③ **The candidate set is under 200 pairs**, so adjudication by reading is affordable.
- ④ **Most adjudicated hits are NOT this seat's receipts**, so the deliverable is mostly a routed
  list rather than a repair.
- ⑤ **Every hit in this seat's own receipts is repaired here**, and each repair is checked to **fail
  on the value the old bound let through** — the test cc66's own repair applies to itself. *A
  replacement that passes everything the original passed is not a repair.*

⚠ **THE BANDS ON ② AND ③ ARE DELIBERATELY WIDE, AND THE REASON IS LAST REVISION'S MISS.** `r7646`'s
arm ⑦ predicted a class total over 500 and measured 228, because it sized a class from the single
member through which the class was found. ⇒ **The same mistake is available here and is refused:
nothing about cc66's one pin says how many others there are**, so ② registers only a direction with
a floor, and ③ a ceiling loose enough to be a real constraint on affordability rather than a guess
at the answer.

---

## PART 2 — WHAT THE SWEEP CANNOT DO, SAID NOW

- ⛔ **It cannot see a bound whose scale the receipt never writes down.** If a receipt bounds `d_om`
  absolutely and never normalises it, condition ⅱ fails and the pair is invisible. *That is a
  stated limit of the net, not an absence of the defect, and the sweep reports how many absolute
  bounds it saw with no normaliser so the blind half is counted rather than ignored.*
- ⛔ **It cannot read a prose fraction.** "A thirtieth of a per cent" is the claim in cc66's case and
  no parser here extracts it; the claim side is adjudicated by reading, which is why the candidate
  list is published whole.
- ⌗ **It is a one-off sweep and not a new gate.** The instruments are frozen; this revision adds no
  gate, no ledger and no census-about-censuses. The forward protection for the repaired receipts is
  that each repaired bound is now two-sided at its measured value, which `check_figures_pinned`
  already reads.

⌗ **And one scope rule, from the standing list:** receipts belonging to `70` or to cc66, and the
named do-not-edit files, are **routed with a patch and never edited** — including any hit found in
them. cc66's own receipt is already repaired by cc66 and is not touched here.

---

# ⛔ AMENDMENT `r7648+60.1` — REGISTERED BEFORE THE SECOND PASS IS RUN, AND BEFORE ITS OUTPUT IS SEEN

**The first pass ran as registered and its result is kept below in full. It must not be reported as
the answer, and the reason is the net and not the corpus.**

**What the registered detector returned:** `1140` receipts parsed, `517` carrying an absolute bound,
**2** candidate pairs — and **4566** absolute bounds whose receipt never normalises the same
variable, so condition ⅱ could not be evaluated on them. Both candidates were adjudicated by
reading and **neither is the class**: each is a two-sided pin at a measured value that a wrong run
would fail, with the relative claim separately held by its own per-cent gate. ⇒ **Arm ② FIRES** on
the registered detector: no adjudicated hit outside cc66's one.

⛔ **AND THAT VERDICT IS NOT REPORTABLE AS "THE CLASS IS EMPTY", BECAUSE THE NET SAW 2 OF 4568.**
*A sweep with 0.04 per cent visibility that returns nothing has measured its own reach and not the
corpus — which is the same shape this seat has twice caught as a guard that cannot fail on the data
it is given. The registered limit ⅱ was declared as a limit; it turns out to be the whole net.*

**The second pass therefore replaces how the SCALE is obtained, and nothing else.** The flaw in ⅱ
was requiring the receipt to normalise the variable somewhere else in the file. But an absolute bound
in the pinned form `abs(V − c) < t` **carries its own scale**: `c` is the value the bound is pinned
at, so `100·t/|c|` is the bound's size in per cent with no normaliser needed. That reaches the
pinned population, which is most of the 4566.

**The widened rule, fixed here before it is run:** a `(receipt, variable)` pair is a CANDIDATE when

- ⅰ′ an absolute bound `abs(V − c) <|> t` with `t` and `c` numeric and `c ≠ 0` — relative size
  `B = 100·t/|c|` — or the first pass's form, a raw bound plus a normaliser;
- ⅱ′ **the receipt itself names a PER CENT for that same variable**: an f-string field whose
  expression contains `V` and whose following literal text begins with `%` or `per cent`. *This is
  the claim side made objective — the receipt's own printed relative size for the quantity it is
  bounding — and it needs no prose parsing, which the first registration named as a limit.*
- ⅲ′ `B > P`, where `P` is the **smallest** such printed per-cent magnitude the receipt names for
  `V`: **the bound, in per-cent terms, is looser than the per-cent the receipt itself prints.**

**Registered arms for the second pass:**

- ⑥ **The seed holds on the widened rule too**: cc66's pre-repair form flags (bound `3.36%` against
  its own printed `2.16%`), and the repaired form does not.
- ⑦ **And the two first-pass candidates do NOT flag under ⅱ′/ⅲ′**, because each prints a per-cent
  for its variable that is *larger* than its bound — `36.35%` against `2.56%` in one — which is the
  adjudication above, reproduced by the rule rather than asserted.
- ⑧ **The widened net reaches at least ten times as many bounds as the first**, i.e. over `20`
  candidate pairs. *Registered as a floor on REACH, not on hits: the first pass's failure was reach.*
- ⑨ **Arm ② is re-read on the widened net.** If it still finds no adjudicated hit outside cc66's,
  *then* the order's reachable negative is reported as reached — and the blind count is reported
  beside it either way, because a sweep's verdict is only as wide as its net.

⌗ *No threshold was moved and no bound was relaxed to make a hit appear: `PCT_FLOOR` stays at one
per cent and ⅲ′ is strictly sharper than ⅲ, since it compares against the receipt's own printed
figure rather than against a fixed floor. The amendment widens WHERE the scale comes from, which is
the limit the first registration had already named.*

---

# ⛔ AMENDMENT `r7648+60.2` — THE ADJUDICATION FOUND A SHARPER RULE THAN THE ORDER'S, AND IT IS REGISTERED HERE BEFORE IT IS RUN

**Two things happened on the widened net and both are kept.**

**ⅰ. Condition ⅲ′ is WITHDRAWN as defective, caught by its own registered arm ⑦.** It wanted the
receipt's own printed per-cent for `V` and tried to read it off the literals inside the printed
expression. *A printed field is an EXPRESSION, not a number:*
`{100*(Om_b/Om_fid-1):+.2f}%` carries the scale `Om_fid = 0.307`, so the rule returned `P = 0.31`
where the field prints `−36.35`. ⇒ **No static reading of a printed field's value exists**, which is
what the first registration said when it put the claim side in a human reading. The net falls back
to the already-registered ⅲ (`B > 1` per cent); the withdrawn `P` is printed beside each candidate
rather than described.

**ⅱ. AND THE READING OF THE CANDIDATES FOUND THE CLASS'S REAL DISCRIMINATOR, WHICH IS NOT
"ABSOLUTE".** The widened net returned **93** candidates in **40** receipts, **30** of them on a
real (non-unity) scale. Reading them:

- `P15_damping_reabsorption:111` — `abs(dlnob + 0.305) < 0.005` beside the paper's `ω_b^{−0.31}`.
  The bound is **exactly half a printed digit** of the claim, and the per-cent claim beside it
  (*"a percent-level ω_b shifts it well under a percent"*) has its **own** gate on the next line.
- `M2_reabsorption_minimization:73` — `abs(Om_b − 0.1954) < 0.005` with the relative claim held
  separately by `abs(100*(Om_b/Om_fid − 1) + 36.35) < 1.0`.
- `P15_the_ratio_is_the_onset_in_imported_units:169` — `abs(ratio − 1.72) < 0.05`, two-sided at the
  printed value, and a wrong run fails it.

⇒ ***Every one of them is PINNED AT A MEASURED VALUE, which makes an absolute bound two-sided and
failable — and that is the healthy shape, not the defect.*** cc66's was `abs(d_om) > 0.01`:
**one-sided, pinned at nothing.** So the discriminator the order reaches for is not *absolute versus
relative* at all; **it is PINNED versus UNPINNED**, and "absolute" is how the one instance happened
to present. *Before two shapes are identified by a label, check how many-to-one the label is on the
object — the label "absolute bound" is many-to-one here, and almost all of what it covers is sound.*

**THE THIRD PASS, fixed here before it is run.** A `(receipt, variable)` pair is a HIT when:

- ⅰ″ **the bound is UNPINNED**: `abs(V) < t` or `abs(V) > t` — `abs` of an expression carrying `V`
  with **no additive constant** inside it, `t` numeric, and no division or factor of 100 inside;
- ⅱ″ the receipt **names a relative size for that same `V`** — either a normaliser `V/S` in a
  per-cent context (pass 1's ⅱ) or a printed field carrying `V` followed by `%` (pass 2's ⅱ′);
- ⅲ″ and, where a scale is available, the bound in per-cent terms exceeds one per cent.

**Registered arms:**

- ⑩ **THE SEED:** cc66's pre-repair `abs(d_om) > 0.01` is a HIT and its repaired form is not — and
  **the three candidates read above are NOT hits**, because each is pinned. *The reading is
  reproduced by the rule and not asserted; the arm that caught ⅲ′ is the reason this is checked.*
- ⑪ **The hit count is small: under 20.** *A direction with a ceiling, not a guess at the answer —
  and deliberately not scaled from cc66's one, which is `r7646`'s arm ⑦ mistake and is refused again.*
- ⑫ **Arm ④ is already decided and is reported as it stands: NONE of the 93 candidates is in this
  seat's own receipts** — 89 are in `P15_CR_cosmology` and 4 in `L557/R1_…`, none in this seat's
  `S`-band. ⇒ **Arm ⑤ is therefore VACUOUS and is reported as vacuous, not as satisfied.** *A guard
  that cannot fail on the data it is given is not a guard; an arm with no instance to score is not
  a pass. The deliverable is a routed list, which is what arm ④ predicted.*
