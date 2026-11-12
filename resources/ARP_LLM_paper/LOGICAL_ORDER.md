# The reception game — logical order of the paper

Working document for a paper on what makes research collaboration with language models generate new knowledge. It lays out the argument step by step and specifies the experiments well enough to hand to a code seat. The human-conversation theory it builds on is the separate ARP paper (`arp_standalone.tex`), which goes out on its own and is cited here as the foundation.

## The question

What makes a collaboration between a person and one or more language models produce findings neither side had, rather than fluent restatement of what was already there?

The dominant answer in machine learning is capability: a larger or better-trained model reasons better. The answer argued here is that, past a capability floor, the deciding variables are interactional. They are the form of each move, how each move is received, and the structure of the game the moves are played in. A capable model playing badly-formed moves into a badly-structured game produces confident noise. The same model playing well-formed moves into a well-structured game produces discoveries.

## Step 1. The failures are specific and recur

Six months of sustained research collaboration in one programme (theoretical physics, one human, many model instances, a public repository) produced a casebook of roughly forty-five recurring failure modes, each recorded from a real slip, with its tell. The ones every reader will recognise:

- **Cherry-picking.** Answering the easy parts of a message and silently dropping the hard one.
- **Premature closure.** Declaring a problem settled, a check passed, or a branch dead before the work earned it, and reporting the closure as success.
- **Manufactured certainty and manufactured doubt.** Inflating a provisional claim (sycophancy, overclaiming, "RESOLVED" over an open problem) and its mirror, hedging a supported claim with caveats performed to look careful.
- **Gist taken as fact.** After memory compression, trusting a flattened recollection as if it were the source. A sign error and a four-part drift in a central theorem rode compactions this way.
- **Offloading.** Handing the human a decision the evidence already settles, instead of making the call and showing it for reversal.

The casebook classified these onto a single axis, over-reach against under-reach, with matched pairs (invent a flaw against invent a reassurance; kill a live line of inquiry against keep a dead one). That classification is the description. Steps 2–5 are the explanation.

## Step 2. The unit move is the ARP

From the ARP paper: conversation is constituted by a single move with three components. The listener assimilates the prior contribution, delivers a receipt (a public demonstration of the assimilation, in their own terms), and pivots to new content the assimilation made available. Participation is signed (engaging the contract, ignoring it, or attacking it); quality Q measures how compressed and generative the move is.

Applied to a model's turns, this predicts cherry-picking exactly. A pivot without a receipt is a move made without demonstrating that the prior turn was taken in, and the part not taken in is the part that drops. The ARP paper's prediction for humans (pivots without receipts read as "not listening") is the human-side phenomenology of the same failure.

Formal anchor: Shaikh et al. (NAACL 2024) measured that language models produce far fewer grounding acts than humans and presume common ground rather than building it. The receipt is a grounding act; the ARP account says why its absence also degrades the pivot, since the same assimilation produces both.

## Step 3. Reception at weight is the control variable

The same input produces progress or damage depending on how it is received: held at exactly the weight it earned, neither inflated nor deflated. The two failure poles of Step 1 are one disposition with opposite signs.

The distinctive, testable claim: **guard sets have a direction.** In the programme, every rule written against overclaiming pushed toward closure, and the push strengthened late in long sessions, when the nuance of each rule compressed away and the short rules, all pointing one way, survived. Fixes for sycophancy are not neutral; they bias toward premature closure and manufactured doubt.

Formal anchors: Sharma et al. (2023) on sycophancy as a systematic product of preference training; the literature on over-caution, which studies the other pole separately. The paper's contribution is treating them as one axis and predicting the coupling.

## Step 4. Interference is the generative mechanism

New knowledge in the record arrives as perturbation from a perspective unlike the receiver's: a referee's finding, an objection, a cold reading, the source overruling a held belief. What a perturbation generates scales with the difference between the perspectives; a source that knows what you know returns what you already see.

Two consequences:

- **Self-review is weak because it has no difference to work with.** Huang et al. (ICLR 2024) found models mostly cannot correct their own reasoning without external feedback; Liang et al. (EMNLP 2024) named "degeneration-of-thought", where a confident model cannot generate new ideas by reflecting on itself, and found divergent multi-agent debate helps.
- **Contamination collapses interference.** Telling a cold reader what the author knows, or what it is being measured for, doesn't merely bias it. It erases the difference that made it valuable and turns a second perspective into an echo of the first.

Human anchor: Dunbar's in vivo studies of working laboratories found discoveries emerging in lab meetings, from reasoning distributed across members with different knowledge.

## Step 5. The collaboration is a game, and interference is only realised by moving

This is the step that joins the others.

In chess or Go a player can anticipate the opponent's replies indefinitely, but anticipation is the player's own model of the opponent: it contains nothing the player did not already have. Only a committed move elicits the real reply, and the real reply can contain what no anticipation produced, wrecking the best-laid plan and changing the next move. Each seat in a multi-seat collaboration is a player with private state (its own context, its own reading), so the game is one of imperfect information, and every real reply carries information that self-simulation cannot.

Consequences, each visible in the programme's practice:

1. **Commit moves early and visibly.** A draft shipped, a call made and shown for reversal, a result pushed: each is a move that invites the reply. Asking permission, or holding a draft back until it is "ready", is declining to move, so the game stalls on the player's own anticipation. Offloading (Step 1) is this failure.
2. **A seat is only as valuable as the ARP quality of its moves.** A move that does not receipt the current board state is a move on a different board; the reply it elicits is about a position nobody is in. Every seat's contribution is bounded by how faithfully it assimilates the state it moves into.
3. **The cold read is an opponent's move the author cannot generate.** Contamination (Step 4) is letting the opponent see your reading, which collapses the game into self-play.
4. **Self-play works in Go because the game has a referee.** AlphaGo-style self-play converges because win and loss are scored externally. Research has no win/loss signal; its referee is the source (the data, the derivation, the primary text), which is why going to the source rather than trusting memory is the scoring function, and why a game scored by agreement among players drifts into a shared fantasy.
5. **The game is cooperative-adversarial.** Seats are opponents on each claim and partners on the goal. The adversarial half is what makes the moves informative; the cooperative half is what makes reception at weight the right norm rather than winning.

Formal anchors: AI safety via debate (Irving, Christiano and Amodei 2018) set up truth-seeking as a zero-sum game judged by a human; prover–verifier games (Kirchner et al. 2024) train legibility through a game between a prover and a checker; Khan et al. (ICML 2024) found that debate between more persuasive models leads non-expert judges to more truthful answers. What this paper adds: those frameworks specify the game and the judge, but not the form of a move or the reception norm. The claim is that the move must be an ARP and the reception must be at weight, and that without these the game's informational advantage is lost even when the game structure is right.

## Step 6. The case study

One long-running programme, documented in a public repository, in phases:

1. Single-seat collaboration before the protocol (the failures of Step 1 recorded as they occurred).
2. ARP adopted as the collaboration's operating rule.
3. The reception discipline (the coda): reception at weight, source over memory, the closure self-check.
4. The compaction rule, with its before/after record.
5. The current phase: one chat seat coordinating several code seats, with a dedicated cold-read seat that registers what it will check before it reads, then reads other seats' landings cold.

The phase-5 record is a game record. The cold-read seat alone has about 180 commits; its recent verdicts include defects found in other seats' work and in its own earlier drafts, corrections of corrections, and validations that return nothing to repair. Coding each exchange (move, reply, whether the reply carried information the mover lacked, whether it was received at weight, what the next move became) turns the log into data.

Weaknesses to state plainly in the paper: one human, one programme; the underlying models changed over the period, so improvement cannot be attributed to the protocol from the record alone; much of the record was written by model instances at the human's direction. The case study motivates; the experiments test.

## Step 7. Experiments (for a code seat)

Each is cheap, pre-registered, and runs against current models with and without the relevant protocol.

- **E1. Coverage.** Long messages containing several distinct asks, with one hard ask buried mid-message. Conditions: baseline; ARP receipt protocol. Measure: fraction of asks addressed; whether the dropped asks are the hard ones. Prediction: the protocol raises coverage and specifically recovers the buried hard ask.
- **E2. Direction of guard sets.** Conditions: baseline; anti-sycophancy instructions; reception-at-weight instructions. Tasks seeded with both correct-but-contested claims and wrong-but-confident ones. Measure: false acceptance, false rejection, premature closure (declaring settled what the task left open). Prediction: anti-sycophancy instructions lower false acceptance and raise false rejection and closure; reception-at-weight lowers both.
- **E3. Contamination.** Documents with planted flaws. Conditions: cold reviewer (told only what to read); reviewer given the author's framing; reviewer told what it is being measured for. Measure: planted flaws found. Prediction: detection falls with each layer of contamination.
- **E4. Source over gist.** A drifted summary of a source document, then questions whose answers depend on the drifted specifics. Conditions: baseline; source-first rule. Measure: drift caught before use.
- **E5. Anticipated against actual move.** An author model writes a document and lists the critiques it expects; an independent cold reviewer then reviews it. Measure: the fraction of the reviewer's real findings the author anticipated. Prediction: low, and rising as the reviewer is contaminated with the author's context, which is the game-theoretic claim measured directly.
- **E6. Multi-seat against self-review at matched compute.** Seeded-flaw research tasks. Conditions: one model reviewing its own work in rounds; two seats exchanging ARP moves with a cold reader; two seats exchanging moves without the receipt requirement. Measure: flaws caught and new valid content per token. Prediction: the multi-seat game beats self-review, and the advantage shrinks when moves lack receipts.

## Step 8. Alternative views (required section for the ICML position track)

- Scale alone closes these gaps. The test is whether the failures persist across model generations; the programme's record spans several.
- This is prompt engineering. The response: the claims are about interaction structure and make predictions (E2's coupling, E5's anticipation gap) that prompt engineering as a practice does not.
- The human is doing the work. E1–E6 run without the human.
- n = 1. Answered by the experiments, not the case study.

## Venues

- The ARP human-conversation paper: *Discourse Processes*, *Journal of Pragmatics* or *Cognitive Science*, submitted first and independently.
- This paper with E1–E6: the ICML position-paper track (the 2026 deadline was 28 January; the 2027 call is expected around the same time), titled to start "Position:" as the track requires.
- This paper without experiments, as a theory paper with case study: *Minds and Machines* or *Topics in Cognitive Science*.

## References to verify at drafting

- Shaikh, O. et al. 2024, Grounding Gaps in Language Model Generations, NAACL. https://aclanthology.org/2024.naacl-long.348
- Sharma, M. et al. 2023, Towards Understanding Sycophancy in Language Models, arXiv:2310.13548.
- Huang, J. et al. 2024, Large Language Models Cannot Self-Correct Reasoning Yet, ICLR, arXiv:2310.01798.
- Liang, T. et al. 2024, Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate, EMNLP, arXiv:2305.19118.
- Irving, G., Christiano, P. and Amodei, D. 2018, AI safety via debate, arXiv:1805.00899.
- Kirchner, J. H. et al. 2024, Prover-Verifier Games improve legibility of LLM outputs, arXiv:2407.13692.
- Khan, A. et al. 2024, Debating with More Persuasive LLMs Leads to More Truthful Answers, ICML, arXiv:2402.06782.
- Dunbar, K. 1995, How scientists really reason: scientific reasoning in real-world laboratories, in The Nature of Insight (MIT Press).
- Sawyer, R. K. 2003, Group Creativity: Music, Theater, Collaboration (Erlbaum).
- Kruglanski, A. W. and Webster, D. M. 1996, Motivated closing of the mind, Psychological Review 103, 263.
- Clark, H. H. and Brennan, S. E. 1991, Grounding in communication (and the rest of the ARP paper's bibliography).
