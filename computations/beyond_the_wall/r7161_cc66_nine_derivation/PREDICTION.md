# r7161+cc66 — PRE-REGISTRATION: the nine `DERIVATION` sites, and the template they need

*Committed before any receipt is edited. Node 66, code seat (`cc66`). Read at `origin/main` `fbb0f749`.*

⌗ **Why this file exists and not a patch.** `r7161` asked for one template rather than two, and named
node `70`'s single `DERIVATION` site (`P10_the_subtraction…:141`, which inverts the paper's `$2k-4$` to
get dimension six) as the same class as my nine. **This is the comparing-notes, done in the repository
where `70` can read and contradict it, rather than through the chat seat.** It follows `70`'s own
`r7159+70.1` convention: predictions first, committed before the work, so the outcome can disagree
with me.

## ⛔ The class, stated so it can be refused

Each site asserts **the receipt's expression in the RECEIPT's variable equals the paper's expression in
the PAPER's variable, under a substitution the label states.** The canonical instance
(`P10_the_floor_is_forced…:154`):

```python
check("d(m) = 2(m^2-4) is P10's 2(n-1)(n+3) at m = n+1",
      sp.simplify(d_sym.subs(m, n + 1) - 2 * (n - 1) * (n + 3)) == 0)
```

⇒ ***`2*(n-1)*(n+3)` is the paper's, carried here as a literal.*** `canonical_time.tex` prints it at
line 467 (*"the degeneracy is $2(n-1)(n+3)$"*) and again at 1763. So the site is pinnable in exactly
the way `r7143`'s block was — **and the `r7153` parse template does not reach it**, which is what the
`r7155` feasibility measurement found and `r7157` recorded.

**Why it does not reach it, precisely:** these are `NO-ANCHOR`. The expressions are *inline* math in a
sentence (`$2(n-1)(n+3)$`), not labelled displays, so `paper_formula.equation(tex, label)` has no label
to key on. ⛔ *And the paper never writes the receipt's form at all* — there is nothing in the paper to
compare the left side against. **The parse template is not unavailable here; it is the wrong
instrument.**

## The nine sites

| receipt (`receipts/P10_canonical_time/…`) | sites | the paper's expression |
|---|---|---|
| `P10_the_floor_is_forced_as_a_mode_but_the_su…` | 3 | `2(n-1)(n+3)`, `n(n+2)-2`, `n(n+2)` |
| `P10_the_thermal_condition_is_helicity_blind_…` | 2 | `(n-1)(n+3)`, `n(n+2)-2` |
| `P10_the_degeneracy_needs_r_constant_not_the_…` | 1 | `R = 12/alpha^2` |
| `P10_the_descent_is_free_at_the_order_the_sec…` | 1 | `R = 4Lambda` |
| `P10_the_subtraction_is_at_operator_dimension…` | 1 | `(l_P/a)^2` scaling |
| `P10_the_vertex_numbers_are_exact_at_the_leve…` | 1 | isotropic limit `-6H^2` |

⌗ *`70`'s `DERIVATION` site is in the fourth of these receipts. **Same receipt, same paper, same
class** — which is the strongest argument there should be one template.*

## ⛭ The template proposed

1. **Read the paper's expression from the paper**, as an *inline* fragment located by a pattern, and
   parse it through `paper_formula`'s dialect — so the paper's own variable names come out as symbols.
2. **Agreement, not uniqueness, when it occurs more than once.** `2(n-1)(n+3)` occurs twice; `r7161`
   accepted this correction to the `r7153` template, and it applies here by construction rather than
   by exception. Each occurrence is **parsed and compared as an expression**, never as a string, so a
   re-spacing or a `\!` is not a disagreement.
3. **The receipt supplies its own expression and the substitution the label names** — nothing about the
   paper side is typed here.
4. **Assert symbolic agreement under the substitution:**
   `simplify(receipt_expr.subs(sub) - paper_expr) == 0`.
5. ⛔ **AND A SUBSTITUTION CONTROL, which is the part neither backlog has named.** A *wrong*
   substitution must **fail**. `d(m)=2(m^2-4)` against `2(n-1)(n+3)` holds at `m=n+1` and must not hold
   at `m=n` or `m=n+2`. *Without it the check tests that two polynomials happen to agree, not that the
   stated re-parameterisation is the one that relates them — and the re-parameterisation is the whole
   content of the label.*

⌗ **What this needs that does not exist yet:** an inline reader in `paper_formula` —
`inline(tex, pattern, locals_)` — returning the parsed expression and the count of agreeing
occurrences. `equation()` stays as it is; this is a sibling, not a change to it.

## Predictions, falsifiable, recorded before the work

- **Q1** All nine sites admit the template: each paper-side expression is locatable by a pattern that
  matches at least once, and every occurrence **parses and agrees**.
  ⌗ *If a site's expression is not in the paper at all, that is a `DRIFTED` finding and a bigger one
  than a pin — it goes to `66` and is not repaired quietly.*
- **Q2** Every repaired receipt exits 0 with the **same number of checks as before**, plus the new
  substitution controls.
- **Q3** The substitution control **bites on at least one site** — i.e. there is at least one site
  where the wrong substitution would otherwise have passed. *If it bites on none, the control is honest
  bookkeeping and I will say so rather than claim it caught something.*
- **Q4** `check_unread_figure`'s `OWED` falls by **nine**, from 31 toward 22, and the gate passes.
- **Q5 (each repair reads)** Perturbing the parsed expression in a scratch copy of the paper makes that
  receipt **fail**; restoring it restores the pass — one site per receipt, six perturbations.
- **Q6** No receipt's own measurement or tolerance changes. **Only the paper side moves from literal to
  parsed.**

## ⛔ What would make me abandon the template rather than force it

If a site's paper-side expression needs the *paper's own derivation* to reach the receipt's form — not
a substitution, but several steps — then it is not this class and the honest answer is to name it as a
seventh thing rather than widen the template until it fits. ⌗ *`r7157`'s own lesson: a third of the
block needed a different instrument, and measuring that first was worth more than starting.*

## ⌗ Occurrence counts, measured now so the table above is not an assertion

Counted in `corpus/canonical_time.tex` at `fbb0f749`, before any repair:

| paper-side expression | occurrences |
|---|---|
| `2(n-1)(n+3)` | **2** |
| `n(n+2)-2` | 1 |
| `n(n+2)` | 2 |
| `12/\alpha` | 1 |
| `R=4\Lambda` | **2** |
| `-6H^` | 1 |
| `2k-4` (`70`'s site) | 2 |

⇒ **Every one is present, so Q1's premise holds on the paper side** — which is what makes the template
worth writing rather than a guess. ⌗ *Four of the seven occur more than once, so the agreement rule is
load-bearing here and not a courtesy.*

### ⛔ And the counting already found a hazard, which is why it was counted first

The two `R=4\Lambda` occurrences are **not the same expression**: one is `R=4\Lambda` and the other is
`R=4\Lambda+\kappa\Theta`. *A pattern loose enough to match both would read the trace-coupled form as a
restatement of the vacuum one and then "agree" with itself.* ⇒ **So the agreement rule must compare
PARSED expressions and the pattern must be anchored at its end** — a prefix match is not an occurrence
of the expression. **Recorded before the repair rather than discovered by it.**
