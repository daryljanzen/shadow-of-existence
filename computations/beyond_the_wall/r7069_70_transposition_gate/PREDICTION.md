# r7069 → 70: the marker-transposition gate — PRE-REGISTRATION

*Node 70. Committed before the gate exists. Built as proposed at `r7067+70.1`, with `r7069`'s addition.*

## What it flags (and only this)

A **transposition**: a distinctive number in one `\rcpt` group's claim window satisfies both of these:
- **none** of that group's receipt sources carries it; and
- the source of a receipt cited in a **different** group within ±N lines of the same paper does carry it.

**Definitions:**
- **Claim window:** the text since the previous marker group.
- **Distinctive number:**
  - a fraction p/q (`\tfrac{p}{q}`, `\frac{p}{q}`, `\tfrac pq`, `p/q`), carried as `p/q`, `Rational(p, q)` or `Fraction(p, q)`, with the sign optional;
  - a decimal with at least three significant digits, carried as its literal;
  - an integer of three or more digits that is not a year (1800–2099), carried as a whole-word literal.

  Common integers are excluded: a stated limit.
- **Source only.** No receipt is run, so the gate is fast. A number that a receipt only prints at run time is invisible
  to it: a stated limit. The companion receipt covers that case.

## The calibration: a condition of building it

The gate must re-find **both** motivating cases at their own commits, with the tex and the receipt sources read via
`git show`:

| case | commit | own group | carrier |
|---|---|---|---|
| two-mode shift: `200/63`, `19/27` | `a3705946` | r7044 + r7048 | r7008, ~90 lines later |
| `−4/3` (and `52/15`) | `3f8fc14a` | r7063 + r7058 + r7056 + r7053 | r7065, ~150 lines earlier |

**N is set from these**: the smallest window that catches both, plus a margin. The value used is **reported**, along
with the flag count at that N. If either case is not re-found, the gate is not delivered. That outcome is tabled first.

## The baseline (`r7069`'s addition)

- Each entry is a **site**, keyed by paper, own group, number and carrier, not by line. Each entry records **what was
  read and the verdict**:
  - *transposition*: routed;
  - *not a transposition*, with the reason.
- The gate **fails** on:
  - a flag not in the baseline (new);
  - a baseline entry whose flag no longer fires (stale). The message is "remove it". A fixed site is never left
    standing as an exemption.

## Outcome table — the one costing this line most FIRST

| | outcome |
|---|---|
| ① | either calibration case is not re-found at its own commit ⇒ **not delivered**, and the reason is reported |
| ② | the baseline at current `main` holds transpositions (real ones, read by hand) ⇒ each is routed to 66 |
| ③ | the baseline holds only non-transpositions (source coincidences), each with its reason |
| ④ | the gate fires on nothing at current `main` |

## ⛔ NOT CLAIMED

- No completeness: the gate catches this one shape, from source text.
- No prose edited, and no receipt touched. Every hit is routed.
