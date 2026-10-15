# ⛭⛭ `r7351+cc66.4` — `L255`: `7` of `8` rows retired by replacing STRING PINS WITH EXECUTION. Three folded into seeds that already existed, four into two seeds that did not — and the timeout seed lowers the cap in its own copy of the gate rather than sleeping past the real one

*`REPAIR-OWED` `144` → **`137`**; `L255` `8` → **`1`**. These eight rows were a different kind from `P16`'s
and `L269`'s: **not spans that pointed badly, but CODE TOKENS STANDING FOR BEHAVIOUR** — an assignment
line, a report line, a common word — so the repair is not a better string. It is execution.*

## ① THE SHAPE OF THE BLOCK, WHICH `r7281+69` HAD ALREADY DIAGNOSED

| row | what it was | what it was owed |
|---|---|---|
| `'STALE EXEMPTION'`, `'subprocess.run'` | a common word and an assignment line, standing for "it runs each marked receipt and fails on exit 0" | ⒜ *"the behaviour is already tested by seeds in ⓹ … so the repair is to delete ⓸ᵇ's text conjuncts or fold them into ⓹"* |
| `'header(t)'` | a code token for the behaviour its own check tests on the line above | ⒜ *"adds nothing but rename fragility. Owed deletion."* |
| `'MARK = re.compile'`, `'with no reason given'` | an **assignment line** and a report line, standing for "the convention is kept" | ⒝ *"no seed tests a reasonless mark. Owed a seeded marked receipt with no reason, shown to fail the gate."* |
| `'TimeoutExpired'`, `'not judged either way'` | two report lines standing for the timeout branch | ⒝ *"No seed tests a timeout. Owed a seeded marked receipt that sleeps past a short cap, with the gate shown not to count it as stale."* |
| `'REPAIRED'` | a common word present `5` and `6` times across three receipts | **not done here** — see ④ |

## ② ⒜ THREE RETIRED BY FOLDING INTO A SEED THAT ALREADY EXISTED — VERIFIED BEFORE DELETING

**`⓹` already runs the gate over a seeded marked receipt in a temp tree and asserts
`seeds['green'] == (1, True)`** — exit `1` **and** the word `STALE` in its output. ⇒ *So the behaviour both
`'STALE EXEMPTION'` and `'subprocess.run'` stood for is tested by execution, and `⓸ᵇ` is folded into `⓹`'s
label.* **I confirmed the seed asserts that before deleting the conjuncts, not after.**

*And `'header(t)'`'s own check asserts `not MARK.search(_rh.header(_mid))` on the line above it — the
behaviour directly. The conjunct was pure rename fragility and is gone.*

## ③ ⒝ FOUR RETIRED BY WRITING THE TWO SEEDS NOBODY HAD WRITTEN

*Both follow `⓹`'s idiom exactly, including its convention that **the mark is ASSEMBLED and never
written**, for the reason `⓹` already gives: this receipt must not itself look marked, because the gate
RUNS what it marks.*

- **`⓹ᵇ` reasonless mark** → measured **`(1, True, False, False)`**: the gate **exits `1`** and prints
  `no reason given`. *That is "the convention is kept", demonstrated instead of quoted.* ⌗ **An assignment
  line is the clearest case in the block: a regex can be rewritten without changing what it matches, and
  the seed survives that where the pin does not.**
- **`⓹ᶜ` sleeps past the cap** → measured **`(0, False, True, False)`**: **exit `0`**, no `STALE`, and
  `not judged either way` present. *The timeout branch is reached and the receipt is reported, not counted
  stale — which is exactly what the two pinned report lines stood for.*

### ⛭ AND THE TIMEOUT SEED REQUIRED A DECISION, WHICH IS IN THE RECEIPT RATHER THAN IMPLICIT

`TIMEOUT = 420` is a **module constant** in the gate, not configurable, so sleeping past it would cost
seven minutes every run. **The seed copies the gate with the cap at `1` s and sleeps `3`.**

⇒ ***What is under test is the `except subprocess.TimeoutExpired` BRANCH, not the number — and a seed that
cost seven minutes would be deleted by the next person who timed this receipt.*** ⌗ **The `re.subn` that
lowers the cap asserts it matched EXACTLY ONCE, and if the constant ever moves the seed records
`'TIMEOUT constant not found'` instead of silently testing nothing.** *That is the cannot-fail shape this
line keeps finding in other instruments, guarded against in one it wrote itself.*

## ④ THE EIGHTH ROW IS NOT DONE AND IS NOT GUESSED

`'REPAIRED'` — *`r7281+69`: "a common word present `5` and `6` times in two of them, tied to no line, and
the third passes on the other arm. **Owed a check on each receipt's own live recurrence assertion.**"*
⇒ **That needs the three receipts' recurrence assertions read one by one, which I have not done.** *It is
the last row in the block and it stays owed rather than being closed by a plausible-looking edit — the
same discipline that made me measure `69`'s prescribed spans in `L269` instead of transcribing them.*

⌗ **Verification:** *receipt `rc=0` with `0` FAIL lines, and both new seeds pass with the exact tuples
above; the extractor re-run on the file gives `3` live keys against `10` baseline rows, from which the `7`
stale and `0` new were computed mechanically; after the two further folds the receipt was **re-run from
scratch** rather than assumed to still pass. `check_quote_pins` follows and is reported rather than
assumed, per `r7347` ④.*
