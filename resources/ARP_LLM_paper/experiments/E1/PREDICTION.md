# E1 — Coverage: does a receipt recover the buried hard ask? (registration)

Committed before any E1 trial. The claim under test is `LOGICAL_ORDER.md` Step 2: a move made without a receipt (a pivot that does not first show the prior turn was taken in) drops the part not taken in, and the part that drops is the hard one.

## Subjects

- **Model:** fresh `claude-opus-5-5` sessions through `harness/subject.py`, one context per trial.
- **What a subject holds:** that trial's message and the condition's one-paragraph system prompt, nothing else. No repository files, CLAUDE.md, memory or programme content.
- **What reaches every subject identically:** the account email, an SDK preamble and the date. See `../SUBJECT_ROUTE_PROBE.md`.
- **Second model:** if Daryl confirms, `claude-sonnet-5-5` runs the same design as a second arm, analysed separately.

## Materials

- **The items:** `materials/items.json`, 40 realistic messages of 180–350 words across at least 15 non-physics domains. Each has 5–7 distinct asks.
- **The hard ask:** exactly one per message, placed in the middle third. It is one of `calc_trap`, `inconsistency`, `tradeoff`, `missing_info` or `multi_step`, with a `hard_key` saying what a full, correct handling must contain.
- **Who wrote them:** a materials author working from a written spec, not a subject. Nothing in them is the programme's.

## Conditions

The system prompt is the only thing that varies. Every item runs once in every condition (paired).

| | system prompt |
|---|---|
| **C0 baseline** | `You are a helpful assistant.` |
| **C1 receipt** | `You are a helpful assistant. Before you answer, write a receipt inside <receipt></receipt> tags: in your own words, say what the message is asking of you, each distinct thing, and what each one actually requires. Then give your answer after the closing tag.` |
| **C2 coverage instruction** | `You are a helpful assistant. Make sure your answer addresses every request in the message.` |

- **C1 is the ARP receipt.** It demonstrates assimilation before the pivot. It does **not** tell the model to answer every ask.
- **C2 is the control for "this is prompt engineering"** (Step 9). It tells the model to cover everything without asking it to show it took anything in.

## Scoring (blind)

- **Stripping:** each response has any `<receipt>…</receipt>` block removed, and the tag text with it. The scorer sees only the answer.
- **The scorer:** a fresh `claude-opus-5-5` context, `role='scorer'`. It gets the message, the asks list (in message order, with the hard ask's `hard_key` and no mark of which ask is "hard" beyond the key's presence), the stripped answer, and this rubric:
  - each ask is scored **2** (fully and correctly handled), **1** (touched but incomplete or wrong) or **0** (not addressed);
  - for the ask with a key, **2** requires the key's content.
- **Output:** JSON per ask.
- **What the scorer is not told:** the condition, the hypothesis, or that conditions exist.
- **Blinding checks:**
  - **Hand-check:** 20% of scored trials, stratified by condition, are hand-scored by me against the same rubric before unblinding the aggregate. Agreement is reported as Cohen's κ, separately for the hard ask and for the easy asks.
  - **Leak check:** the scorer is also asked to guess, per answer, whether "the assistant was given any special instructions" (yes/no). If its accuracy at telling C1 from C0 by that guess exceeds 65%, blinding is reported as leaky.

## Measures

- **Primary.** H = 1 if the hard ask scores 2, per item × condition. The contrast is C1 − C0, paired over items.
- **Secondary.**
  - (a) Coverage: mean ask score over all asks, C1 − C0.
  - (b) **"The dropped asks are the hard ones."** In C0, the rate at which the hard ask scores < 2, against the rate at which easy asks score < 2, per item, paired.
  - (c) C1 − C2 on H.
- **Effect sizes:** reported as paired differences in proportion with 95% bootstrap intervals (10,000 resamples over items), plus McNemar's exact p.

## n, and how it is chosen

- **The pilot:** 8 items × 3 conditions, scored as above. Pilot trials are discarded from the analysis, and every item is re-run fresh in the main run, since subjects keep no memory.
- **The rule, fixed now:** from the pilot's discordant-pair rate p_d and observed difference δ (floored at the predicted 0.15), n = (1.96 + 0.84)² · p_d / δ² (McNemar, 80% power, two-sided α = 0.05).
  - The main run uses max(40, n). If n > 80, the effect is too small to detect at this budget, and I say so instead of running more.
  - Items beyond 40 come from the same author spec and are committed before they run.

## Predictions (made before any trial)

- **P1 (primary):** H rises from C0 to C1 by at least 10 points, and the 95% interval excludes 0.
- **P2:** in C0, the hard ask scores < 2 more often than the easy asks do (secondary (b)), with the interval excluding 0.
- **P3:** C1 ≥ C2 on H.
  - **This prediction is weaker.** A plain coverage instruction may recover the hard ask's *presence* without its *handling*. ARP predicts the receipt does better, because restating "what each one actually requires" is the assimilation that exposes the trap.
  - **Confidence:** P1 70%, P2 75%, P3 55%.

## What counts against

- **P1 fails** if C1 − C0 on H has an interval that includes 0 or lies below it.
- **Ceiling:** if C0's H is ≥ 90%, the Step 1 failure does not reproduce on this material in this model. That is reported as a finding against the premise at this capability level, not explained away. P1 is then untested, and the report says why.
- **P3 fails** if C2 > C1 on H with an interval excluding 0. That supports the "prompt engineering" reading of Step 9.
- **Every failed prediction is reported** at the same weight as a held one.

## Records

- `runs/<cond>/<item>.json`: one per trial, with the exact system prompt, message, model, timestamp, response, usage and timing.
- `scores/<cond>/<item>.json`: one per scorer call.
- `RESULT.md`: written against this file.
