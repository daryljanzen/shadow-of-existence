# r7137+70.1: pre-registration for the `SOURCE/ALT` keys, measured rather than read (`PO-78`, `r7137`)

*This is committed before any `SOURCE/ALT` site is read. It was read at `origin/main` `8a5cd6f7`. What I have seen so far is only the baseline's counts:*
- *142 `SOURCE/ALT` keys across 55 receipts;*
- *137 of them unadjudicated, plus the 5 `XOR` keys done at `r7131`.*

## The items owed, with a state against each

| item | source | state at this commit |
|---|---|---|
| sample the `SOURCE/ALT` keys; does one verdict cover them? what separates an `ALT` that **admits the state its own result may produce** from one that **enumerates the states its author could foresee**? mechanical or semantic? | `r7137` | pre-registered here |
| the seventeen accepted; the live shear pair retired and repaired by the gate | `r7137` | noted; nothing owed |

## The method, fixed now

1. **A random sample of 30 of the 137 unadjudicated keys** (`random.seed(7137)`), each read at its site.
2. **Each disjunction is classified by what its arms are:**
   - **SPELLING**: the arms are alternative spellings or encodings of **one** fact (`'nu_R' or '\\nu_R'`, a case or LaTeX variant, a regex and its literal). **Not a state disjunction at all.**
   - **STATE-ENUM**: the arms are **two or more states of a moving text** (old wording / new wording, pre / post a revision, open / closed). **This is `60`'s guard: the failure mode is enumerating states.**
   - **SELF-ADMITTING**: a STATE-ENUM one of whose arms is the state **this receipt's own result** would produce. *That is the repaired form `r7125` wanted.*
   - **OTHER**: anything else, read and named.
3. **A mechanical candidate, tested against my classification:**
   - **Token overlap between the arms' literals:** high overlap or a shared core suggests SPELLING; low overlap suggests STATE-ENUM.
   - **Plus a revision-token check:** a disjunct literal naming an `r\d+` or `c54.\d+` revision, or a state word (`open`, `owed`, `closed`, `struck`, `~~`), suggests STATE-ENUM.

## Predictions

- **SPELLING ≥ 50 % of the sample; STATE-ENUM ≤ 30 %; SELF-ADMITTING ≤ 10 %.** `ALT` was built as the repaired form, but on `SOURCE` targets (code, ledgers, headers), arms that are encodings of one fact should dominate.
- **SPELLING against STATE-ENUM is mechanical:** the overlap/revision-token rule agrees with my reading on **≥ 80 %** of the sample.
- **SELF-ADMITTING against plain STATE-ENUM is NOT mechanical.** Deciding it needs to know what the receipt's own result would do to the text it reads, which is semantic. **I expect to report it as a backlog-by-reading, not a flag.**
- **If SPELLING dominates, the class verdict for those is `NOT-A-PIN`'s neighbour, a tolerance of encoding.** I will propose a verdict name for it rather than force it into `ALT-OK`, **and verdict only the sample**, as ordered.
