# r7131+70.1: pre-registration for the five `SOURCE/XOR` quote-pin keys (`PO-78`, `r7131`)

*This is committed before any of the five sites is read. It was read at `origin/main` `56628e4b`. What I have seen so far is only the five baseline rows: receipt, literal, `SOURCE`, `TOKEN`, `ALT,XOR`, `UNADJUDICATED`.*

## The items owed, with a state against each

| item | source | state at this commit |
|---|---|---|
| read the five `SOURCE/XOR` keys and give each a verdict | `r7131` | pre-registered here |
| `PO-77` ⓵ answered against my reading: the census is the vacuum curve's expansion leg, not the leaf | `r7131` | **acknowledged in the reply.** It was the check I named, and it changed the answer. |
| the standing observation on the gate's two reversals | `r7131`, offered | noted |

## What I expect, and why, before reading

- **The `XOR` flag fires on `==` as well as `!=` between two non-literal operands.** That is how I built it at `r7125+70.1`, because the form that broke was `(A and B) != C`.
  - But **`(lit in X) == (lit in Y)` is a consistency check** ("the two files agree"), not an exclusive disjunction over states.
  - **Prediction:** at least 3 of the 5 are `==` or `!=` comparisons of two presence tests across two files or two states. **At most one is the hazard the flag was built for:** an exclusive "one state or the other" that a third state can break.
- **The literals are short TOKENs** (`"at"`, `"stress tensor"`, `"c54.226"`, two regexes). **Prediction:** at least one is a false positive of the operator itself, not a quote-pin. `"at"` in `L250/Q1`, the quotepin helper's own receipt, is the likeliest: a probe string in a test of the helper.
- **The verdict names in the baseline header are `DELIBERATE`, `ALT-OK` and `REPAIR-OWED`.** I expect to use:
  - `DELIBERATE` for consistency checks;
  - `REPAIR-OWED` for any true exclusive-state pin;
  - **a stated `NOT-A-PIN`** for an operator false positive. *That name is new, and I will say so rather than force a site into an existing bucket.*
- **The flag itself:** if most of the five are `==` consistency checks, **I will propose narrowing `XOR` to `!=`** (and `==` against a negated state), **and report the count change.** I will not change the operator's output format.

**Where the verdicts go:** the order says to give each a verdict. Adjudications live in `corpus/quote_pin_baseline.tsv`, which is the gate's file. **I will write the five verdicts there, with what was read, and say so in the reply, so the gate can revert any single row.** The ceiling is not touched: the unread count can only fall.
