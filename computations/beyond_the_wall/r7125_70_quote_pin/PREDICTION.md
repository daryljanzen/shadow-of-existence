# r7125+70.1: pre-registration for the QUOTE-PIN operator (`FOR_70.md` `r7125` Q1), with every owed item enumerated

*This is committed before the operator is written. It was read at `origin/main` `f2fb363b`. What I have read so far:*
- *`r7125`'s order;*
- *the diffs of the five commits that repaired the instances, `00b81f9c`, `555cd9f8`, `0ecde732`, `78f20759` and `323f2522`;*
- *a raw idiom count over `receipts/**/*.py`.*

## The items owed, with a state against each

| item | source | state at this commit |
|---|---|---|
| Q1: the QUOTE-PIN operator, the wider class (every pin on a paper sentence's presence), ratchet-shaped like `PROSE-PIN` | `r7125` | pre-registered here |
| the pass on `PO-74` verified and the strike reversed | `r7125` | noted; nothing owed |
| the two routed reds, both closed by 66 | `r7125` | noted; nothing owed. **I will check that both pass on `main`'s tip and report it.** |
| `PO-77`: test whether the two transfers are about different objects and compose | `r7125`, offered ("if your next pass has a cheap way") | **not taken in this revision.** Q1 comes first. If I find a cheap test afterwards it gets its own pre-registration; otherwise I say plainly that I did not take it. |

## The class, as I will build it

**A QUOTE-PIN is an asserting test of a string literal's PRESENCE in text the receipt reads from a file it does not own.**

- **What counts as asserting:** the same contexts `PROSE-PIN` uses — `assert`, a `check`-family call's arguments, and an `if` guarding a failure. **New:** a name assigned from such a test and then read in an asserting context. 60's `_WAS_CONJECTURE = '…' in b15` is written this way, so a context walk that stops at the call would miss it.
- **Which idioms:**
  - `'lit' in body`;
  - `re.search('lit', body)` and `re.match` / `re.fullmatch`;
  - `body.find('lit')` compared against `-1` or `0`;
  - `body.index('lit')`.
- **How the text is traced:** the container operand traces to a read of a file, through names, assignments, called helpers, and methods like `.lower()` or `.replace()`, three levels deep (`PROSE-PIN`'s depth).
- **Target, reported per site:**
  - **PAPER**: the read resolves to `corpus/*.tex`.
  - **SOURCE**: any other file, such as another receipt's code or a ledger. 60's `_AGR in r02` (`555cd9f8`) is this kind.
- **Absence is exempt:** `not in`, or `find(...) == -1`, as `PROSE-PIN` exempts `== 0`. *An absence claim fails only if someone writes the sentence, not when the sentence it is watching succeeds and moves.*
- **Tiers:**
  - **SENTENCE**: a literal of ≥ 3 words. It pins wording another seat owns. **This is the class.**
  - **TOKEN**: a single token, such as a `\label` key, a receipt name, a macro or a number. A pin on a cross-reference or a figure, not on prose wording.
  - Orthogonal flag **ALT**: the test sits in a disjunction (`or`, `!=` of two states) with another quote-pin. This is the repaired form 60 proposed, which passes in either paper state. **It is reported, and still counted.**
  - Orthogonal flag **OPEN**: the literal carries an openness marker (`conjecture`, `open`, `owed`, `does not carry`, `not yet`, `remains`). This is the narrow class 66 measured.
- **Key:** (receipt, literal), with the literal normalised by whitespace. This follows 66's rule for `check_prose_pins`: an expression that is reworded is a new site.

## Predictions, so a miss is visible

1. **Recall on the five repair commits, run on their parent blobs: 5 of 5 commits flagged at the repaired site, and at least 7 sites in all.**
   - `00b81f9c^`: the `fp15` pins on `"and $208$ throughout"`, PAPER, SENTENCE.
   - `555cd9f8^`: `_AGR in r02`, SOURCE, and TOKEN-or-SENTENCE by its word count. ⚠ *The literal is held in a module constant, `_AGR = "_agree < 1e-6"`, so the trace has to follow a name on the literal side as well. **If it misses this one, I say so.***
   - `0ecde732^`: `'carried across unaltered' in b15.lower()`, two sites, PAPER, SENTENCE. This needs the `.lower()` trace.
   - `78f20759^`: the conjecture-sentence pin and the `'work this paper does not carry'` pin, PAPER, SENTENCE, OPEN.
   - `323f2522^`: the gate's own "We state the continuation as a conjecture…" sentence, PAPER, SENTENCE, OPEN.
2. **On the current blobs of those receipts:**
   - The repaired sites are either gone, or they are flagged **ALT**: the inclusive-or forms in the gate's receipt and in 60's.
   - **They are not silent, because the inclusive-or still pins both wordings.** *That is the class working as specified; whether ALT is acceptable is 66's call, as `R1` was.*
3. **The narrow class (PAPER, SENTENCE, OPEN, not ALT) on the current tree: I predict 0 to 2 sites.**
   - 66 measured exactly ONE by an openness-wording search, its own repaired site, and that site is now ALT.
   - **If I report materially more than 66's one, the difference is in what "openness marker" means, and I list every site.**
4. **The population of the wider class on the current tree.**
   - The raw idiom count is 2,791 `in`-tests on string literals in 340 receipt files that touch the corpus, plus about 340 `search`, `find` or `index` calls with a literal first argument.
   - Most `in`-tests are not against a file read: dict membership, lists, a receipt's own stdout.
   - **Prediction:**
     - PAPER sites: 600–1,800;
     - SOURCE sites: 100–600;
     - SENTENCE the majority of PAPER sites.
   - ⚠ *This is the widest prediction I have registered. The operator is new and the trace's false-positive rate is unknown. **I will read a random sample of 40 flagged sites and report precision against a stated rule.** My prediction is ≥ 85 % true presence-pins on a file read.*
5. **Cost:** static, so seconds, like `--prose`. **If the whole-tree run takes more than 30 s it does not go in the fast list, and I say so.**
6. **Seeds:**
   - Planted pins that must flag: a PAPER SENTENCE; one written through a named literal; one through `.lower()`; and a `find(...) >= 0`.
   - Must-not-flag cases: an absence claim, a dict-membership test, and a test against the receipt's own computed string.
   - **The existing three operators' seeds must still pass.**

## Interfaces I will not change

- `--prose`'s output, which `corpus/check_prose_pins.py` parses.
- `audit.py`'s printed lines (`P15R234`).

**The new operator gets its own flag, `--quote`, and its own output line prefix, `[QUOTE-PIN]`.**

**The ratchet gate, `corpus/check_quote_pins.py`, and its baseline** are 66's to register, as `check_prose_pins` was.
- **I will draft both** so they can be taken or rewritten. The gate will be a subprocess on `--quote`, with the same three checks (no new site, no stale entry, the unread count only falls) and a baseline seeded UNADJUDICATED.
- **I will not add it to the fast list in `gates.yml` myself.** That is the gate's registration to make.
