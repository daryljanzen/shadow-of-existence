# r7203+70.1 — do the numbers in `receipts/INDEX.md`'s `Computes` column match what each receipt prints?  Predicted before running

*`FOR_70.md` r7203 puts `cc66`'s gap on this seat's list.  A number in an INDEX `Computes` cell has no gate tying it
to the receipt's stdout.  `cc66` found `21.3`/`22.4` in INDEX where its receipt prints `21.4`/`22.6`: a derived
quantity re-derived by hand from a rounded printout.  66 wants the count before filing a twenty-seventh blindness
member, and wants to know whether this is its own class or an instance of the quote-pin family.*

## The measurement, fixed now

- **Rows.**  Every INDEX row with a receipt path that exists.  **Numbers** are the decimal literals in its
  `Computes` cell with three or more significant digits; integers and years are excluded.
- **Receipt output.**  Every such receipt is run once, from its own directory, with a 300 s timeout, and its
  stdout is captured.
- **Verdict per number, at the number's OWN printed precision:**
  - **MATCH**: some stdout number rounds to it at its decimals, or equals it as a string.
  - **SOURCE-ONLY**: no stdout match, but the number occurs in the receipt's source.
  - **ABSENT**: in neither.
  - **UNRUN**: the receipt did not exit 0, or timed out.

## Predictions

- **F1.**  **400-800** rows carry at least one such number.
- **F2.**  The numbers total **1,500-5,000**.
- **F3.**  Of the numbers on run receipts:
  - **60-85%** MATCH;
  - **5-15%** SOURCE-ONLY;
  - **10-30%** ABSENT.
- **F4, RECALL.**  `cc66`'s instance at `HEAD` is flagged ABSENT or SOURCE-ONLY, if the INDEX copy still carries
  `21.3`/`22.4`.  If the INDEX was already repaired, I will say so and seed it instead.
- **F5.**  A seeded hand-read sample of 20 ABSENT numbers contains **3-8 genuine drifts**, meaning the INDEX value
  disagrees with what the receipt computes.  The rest are:
  - a different form of the same figure (units, a percentage against a fraction, scientific notation);
  - figures the receipt quotes from a paper or another receipt rather than computing;
  - parameters.
- **F6, THE CLASS QUESTION.**  Predicted: **its own class, not a quote-pin instance.**  A quote pin is a receipt
  asserting another seat's TEXT.  This is a ledger asserting a receipt's NUMBER, in the opposite direction, and no
  pin exists at all.

*Misses are reported as misses.  No INDEX row and no receipt is edited: drifts are routed.*
