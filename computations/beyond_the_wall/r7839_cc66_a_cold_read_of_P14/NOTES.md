# r7839 — working notes

## The probe that established failability

Guard from `r7837`: *a probe needs a positive control — the unperturbed copy must pass by the same
route the perturbed one fails.* The receipt resolves the paper relative to `__file__`, so copies
must sit in the receipt's own directory or they crash at import and "pass" vacuously.

Control: the unperturbed copy in `receipts/P14_matter_sector_paper/` → `rc=0`.

| perturbation | pins red |
|---|---|
| `LAMBDA` 1.1056e-52 → 2.1056e-52 | 2 |
| `V_L` 246 → 300 | 5 |
| `G_WEAK` 0.65 → 0.80 | 2 |
| `M_NU` 0.05 → 0.06 eV | 3 |
| `Y_Q` 1/6 → 1/5 | 6 |
| blackbody weight `D_RHO` 15 → 16 | 1 |
| the factorisation `(3r_0^2-1)^2` → `(3r_0^2-1)` | 1 |

## A tautology caught before it landed

The first baryon-ratio arm compared `30*ZETA3/pi**4` against `(2*ZETA3/pi**2)*15/pi**2`. Both sides
read the same `ZETA3`, so perturbing `ZETA3` reddened **nothing** — the arm checked the algebraic
identity `2*15 = 30` and not the paper's figure at all. Rewritten to parse the printed integer and
the printed power out of the sentence and derive both from the two blackbody normalisations; it now
reddens when either normalisation moves.

⇒ **Guard: an arm whose two sides share an input is not a pin on that input. Perturb every constant,
not only the ones you expect to matter.**

## A regex that matched nothing, again

`r'...\\d+...'` inside a raw string is a literal backslash followed by `d` — it matches `\d` in the
LaTeX, not a digit. Three edits failed to fix it by `sed` before `cat -A` showed what was actually
on the line. Replaced `\\d` with `[0-9]`, which has no escaping question at all.

⇒ **Guard: in a receipt that parses LaTeX, every backslash is already spoken for. Use character
classes, not shorthand.**

## The ALT disjunction, needed twice

Two arms assert the *state* of a sentence the same revision changes:
- `Ⓑ⑩` accepts STATE A (the defective `4-3r_0^2`) or STATE B (the corrected form) and no third.
- `Ⓙ①` accepts `(118 sites, 98 stems)` or `(119, 99)` — the citation this receipt adds at the crest
  moves both counts, so a census pinned to one state would have gone red on its own fix.

## What the read did not settle

The sentences whose claims are not numerical. This receipt pins the figures and the one
factorisation; the physics belongs to the 98 receipts P14 cites, and this read did not re-derive it.

## The two gates that caught me, and what each one taught

Registered prediction ⑥ was that at least one gate catches something in my own landing. Two did.

1. **`check_unread_figure`** (excluded from the local batch) on
   *"the PRINTED factor $4-3r_0^2$ equals 3 there"*. The label attributed the number to the paper
   while the arm evaluated a **retyped** expression. Fixed by parsing the factor's own two integers
   out of the parenthesis the receipt has already read.
   ⇒ **Guard: parsing the FIGURE is not enough — the EXPRESSION you evaluate it with must be parsed
   too, or the attribution is still a retype one level down.** This is `r7837`'s finding, sharpened.
2. **`check_cannot_fail`** (inside the batch) on an arm ending `... or True`. Fixed by replacing it
   with a printed scope line and the three-value check that actually decides the claim.
   ⇒ **Guard: an arm that states a scope should PRINT, not `check`.**

## The red that was not mine, fixed anyway

CI on the registration commit was red on `check_quote_pins` and `check_unread_figure`, both tracing
to `6cfab7d85` — 69's own landing of `r7837`. Its rewrite of my receipt's four retyped figures into
parse patterns minted one key without adjudicating it and left four of my rows stale; and its
regulated-peak receipt attributes `4.17e52` kg to P16 without opening P16. Both fixed here: the key
adjudicated and the stale rows struck, and my own `r7837` parse ported into the regulated-peak
receipt.

⇒ **Guard: a red on your head that predates your work is still yours to fix when the fix exists —
and here the fix was a pattern I had already written.**
