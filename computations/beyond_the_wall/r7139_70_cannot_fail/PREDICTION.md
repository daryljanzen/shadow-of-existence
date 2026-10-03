# r7139+70.1: pre-registration for the CANNOT-FAIL operator, across the whole assertion population (`r7139`)

*This is committed before the operator is written. It was read at `origin/main` `7944e7ab`.*

## The items owed, with a state against each

| item | source | state at this commit |
|---|---|---|
| build the vacuous-arm operator, pre-registered, with a recall set drawn from known instances and a population prediction; measure it across the whole assertion population, per class; say so if it is not mechanical | `r7139` | pre-registered here |
| the parity line accepted | `r7139` | noted |

## Prior art, read first (the `L-249` lesson)

- **`scripts/label_pin.py` (cc66, `r7129`)** has a `VACUOUS` regex over the condition text: `>= 0`, `<= -1`, a trailing `True`. **It reports 46 sites** and was used as a reading aid, not a gate. *Its own aside:* VACUOUS "is a separate and much cleaner signal".
- **`scripts/sweep_vacuous_pins.py` (this seat, `r6931+70.3`, in CI)** catches a **bare number** that matches a live document away from the check's own sentence. **It deliberately excludes `SOURCE` haystacks**, after 6 flagged, 1 true and 5 false. `'3.3'` in `L204/P12` lives exactly in that excluded corner.
- **`corpus/check_receipt_asserts.py` (fast list)** asks whether a *receipt* can fail at all, i.e. whether it holds any assertion. **It does not look inside an assertion.**
- ⇒ ***What is new here is per-assertion, AST-based and across every asserting context.*** It does not re-implement either sweep; it subsumes `label_pin`'s regex as one class.

## One distinction the order runs together, stated before building

- **CANNOT-FAIL:** an assertion, or an `or`-arm that dominates its siblings, which is true whatever the measured text or value is. **That is the defect.**
- **DEAD-ARM:** an `or`-arm that can never be true: the gate's two removed arms (markup-spanning, truncated). **It does not make the check unable to fail;** it makes that arm assert nothing while the check rests on its siblings.
- **Both are "asserting nothing", and they are different mechanics.** Statically, a dead arm needs the container's contents, which a static pass does not have. **So DEAD-ARM is out of the static operator's reach, and I say so** rather than approximate it.

## The classes (static, AST)

| class | the shape |
|---|---|
| **T1 TAUTOLOGY** | a comparison true by type: `len`/`.count`/`abs`/`sum` of non-negatives `>= 0` or `> -1`; `X == X` or `X <= X` (identical AST); `x or True` |
| **T2 LITERAL-VERDICT** | the verdict argument of a check, or an `assert`, is a constant or a pure-literal expression (`True`, `1`, a non-empty string) |
| **T3 TRIVIAL-ENV** | `'m' in sys.modules` for a module the file imports; `os.path.exists(__file__)` |
| **T4 GUARDED-TRUE** | an `IfExp` with a literal-`True` branch in an asserting context (`B14`'s `… if t == 'PO-2' else True`): the claim is tested on one case and passes on the rest |
| **T5 UBIQUITOUS-ARM** | an `or`-arm presence test whose literal matches ≥ 50 % of the files of its haystack's kind (receipt sources for `SOURCE`, `corpus/*.tex` for `PAPER`), measured on the tree. **The mechanical form of my `r7137` VACUOUS**, and the place `sweep_vacuous_pins` deliberately does not go. |

## The recall set: five known instances, each at the blob where it was live

| # | instance | class |
|---|---|---|
| 1 | `L204/P10`'s `n >= 0` at `b603b960^` (cc66's) | T1 |
| 2 | `L221/B14`'s `… if t == 'PO-2' else True` at HEAD (cc66's aid's find) | T4 |
| 3 | `L204/P12`'s `'3.3'` arm at HEAD (`r7137`) | T5 |
| 4 | `L237/G1`'s `'scanner'` arm at HEAD (`r7137`) | T5 |
| 5 | the gate's `r7127` receipt's `'sympy' in sys.modules and 'mpmath' in sys.modules` at `15c02ae3` | T3 |

⚠ *The gate's two removed dead arms never reached git: they were removed in the draft before the commit. **So they cannot be in a recall set, and they are a DEAD-ARM besides.** Instance 5 is the gate's own cannot-fail in the same file, substituted and named as such.*

## Predictions

- **Recall: 5 of 5.** T5 is the most exposed, because the 50 % threshold is a guess. **If `'3.3'` or `'scanner'` falls under it, I report the miss and the measured ubiquity; I do not move the threshold.**
- **Population, sites across `receipts/**`:**
  - T1: 20–120;
  - T2: 50–400 (scope gates closing on `True` are a known idiom, and my own audits have used it);
  - T3: 3–40;
  - T4: 5–60;
  - T5: 15–150.
  - **Total: 100–700 sites, in 10–35 % of receipt files.**
- **Commonest defect?** Against the measured populations of the other operators (quote-pin 2,459 sites, prose-pin about 170), **I predict CANNOT-FAIL lands between them.** So it is **not** the corpus's commonest assertion defect by sites, **but it is the most severe per site,** since the others fail late and this one never fails.
- **Precision, read on a random sample of 30 flagged sites (`seed 7139`):**
  - **≥ 90 % for T1–T4,** which are syntactic;
  - **≥ 60 % for T5.**
  - *A T2 site can be a deliberate "scope" statement printed as a passing check.* **That is still CANNOT-FAIL by construction, and I count it as true, with the scope-gate sub-shape reported.**
- **Cost:** static, under 30 s, so it fits the fast list's shape. **Gating it is the gate's call.**
- **If T5's precision falls below 50 %, T5 is not mechanical and I say so,** the second honest negative the order allows for. **T1–T4 stand or fall on their own numbers.**
