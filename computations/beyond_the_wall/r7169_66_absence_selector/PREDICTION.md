# PRE-REGISTRATION — r7169 (node 66, the gate): the touched-readers selector cannot see a corpus-wide reader

Written **before** `_touched_pin_readers.py` is changed and **before** the 47 are run.

## What is already measured

`B25_the_scattering_object_exists` asserted `"Regge" appears ZERO times in the papers`. `r7167` wrote the
words into `CR_cosmology.tex` for an unrelated purpose and `main` was red from `3d93b695` until `r7169`
— two revisions, both of which I gated and pushed. `run_touched_readers.sh` did not select it, because
its selector keys on `corpus/quote_pin_baseline.tsv`'s (receipt, literal) pairs and asks whether a
pinned literal appears in a CHANGED line. **An assertion about an absence has no sentence to change**,
so no edit can ever select it.

A source scan finds **47** registered receipts that glob `corpus/*.tex` rather than naming one paper —
the corpus-wide readers, the class every paper edit can affect.

## Predictions

- **P1 — the selection cost.** Adding the 47 whenever any `corpus/*.tex` changes raises this revision's
  selected set from its pin-only figure to **pin-only + 47 − overlap**, and I predict the overlap on
  this revision's change set is **small, 0–6**, because a corpus-wide reader is selected by a pin only
  when it ALSO pins a literal that moved.
- **P2 — how many of the 47 are red on `main` right now.** I predict **1 to 3 besides `B25`**, and I am
  deliberately predicting non-zero: this class has been invisible for the whole life of the selector,
  and `r7168` alone edited five papers. **If it comes back 0 that is worth as much as a hit** — it would
  say the class is fragile in principle and has not actually broken, and the gate's value is then
  prospective.
- **P3 — affordability.** The 47 run at four at a time in **under 12 minutes**, which is the bar this
  gate was built to (a gate that cannot finish before a push will not be run before one).
- **P4 — the shape of any hit.** Any red among the 47 is an ABSENCE claim falsified by a later edit,
  not a numeric drift. I predict the failing check's text contains one of `ZERO`, `never`, `no paper`,
  `nowhere` or `absent`.

## What would make the change wrong

If the 47 take materially longer than the pin-selected set usually does, the gate stops being run and
reports nothing — which is the defect `r7155` recorded for this same script. In that case the right
answer is not to widen the selector but to say so and leave the class to the heavy job, with the
measurement in the register.
