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

**What the experiments found (E1–E8, 2026-11-12 to 11-14, Opus 5.5 with Sonnet 5.5 on E1–E3).** The failures did not reproduce in the settings tested.
- **Dropped asks (E1):** the buried hard ask was handled on 95–98% of items at baseline.
- **False acceptance, false rejection, premature closure (E2):** 0 of 48 items in any condition.
- **Gist taken as fact (E4):** 0 of 120 drifted questions answered from the notes while the source was in context.
- **32-turn sessions with an 18k-word reading load (E8):** the composite was 0 in all but one of 768 scored turns.
- **Closure and confirmation-seeking (E7):** 0 in all 160 seats.

**So Step 1 is restated:** the casebook is a record of failures that recurred in sustained, compressed, human-directed sessions with earlier models. In single messages and in 32-turn sessions on current models, they do not occur. The settings the experiments did not reach, which are much longer sessions, context compression, a human interlocutor and tasks that depend on earlier turns, remain the claim's home ground. They are untested, not confirmed. What moved instead was **depth**: how many valid problems a reviewer raises beyond the planted ones (E3, E7, E8).

## Step 2. The unit move is the ARP

From the ARP paper: conversation is constituted by a single move with three components. The listener assimilates the prior contribution, delivers a receipt (a public demonstration of the assimilation, in their own terms), and pivots to new content the assimilation made available. Participation is signed (engaging the contract, ignoring it, or attacking it); quality Q measures how compressed and generative the move is.

Applied to a model's turns, this predicts cherry-picking exactly. A pivot without a receipt is a move made without demonstrating that the prior turn was taken in, and the part not taken in is the part that drops. The ARP paper's prediction for humans (pivots without receipts read as "not listening") is the human-side phenomenology of the same failure.

Formal anchor: Shaikh et al. (NAACL 2024) measured that language models produce far fewer grounding acts than humans and presume common ground rather than building it. The receipt is a grounding act; the ARP account says why its absence also degrades the pivot, since the same assimilation produces both.

**What the experiments found.**
- **E1:** a receipt protocol could not raise coverage, because baseline coverage was already at ceiling. C1 − C0 on the hard ask is +0.000 [+0.000, +0.000] (Opus) and −0.025 [−0.075, 0.000] (Sonnet).
- **E6:** requiring receipts in the multi-seat game *cost* valuable extensions, −0.25 [−0.44, −0.08] against the same game without receipts (hand-check κ 0.88).

**So the claim that a receipt prevents cherry-picking is untested on current models, and a mandated receipt has a measured cost in new content.** The ARP account of why pivots without receipts fail stands as theory and as the human-side prediction. As an intervention on current models it is unsupported.

## Step 3. Reception at weight is the control variable

The same input produces progress or damage depending on how it is received: held at exactly the weight it earned, neither inflated nor deflated. The two failure poles of Step 1 are one disposition with opposite signs.

The distinctive, testable claim: **guard sets have a direction.** In the programme, every rule written against overclaiming pushed toward closure, and the push strengthened late in long sessions, when the nuance of each rule compressed away and the short rules, all pointing one way, survived. Fixes for sycophancy are not neutral; they bias toward premature closure and manufactured doubt.

Formal anchors: Sharma et al. (2023) on sycophancy as a systematic product of preference training; the literature on over-caution, which studies the other pole separately. The paper's contribution is treating them as one axis and predicting the coupling.

**What the experiments found.**
- **E2 sat at its registered floor in both models:** no false acceptance, false rejection or premature closure in any condition. So no guard set could be shown to push in a direction (every contrast +0.000 [+0.000, +0.000]; hand-check 120 of 120, κ 1.00). **"Guard sets have a direction" is not shown on current models in single messages.**
- **The late-session half of the claim was tested by E8.** Without a curriculum (PLAIN), review depth thinned by −1.03 [−2.22, +0.06] valid problems per review from early to late, so P1′ failed narrowly. The curriculum arms thinned by −2.94, but only because their early lift faded to PLAIN's level. No closure appeared late in any arm.

**Restated:** the coupling of the two poles stays a hypothesis from the record. The experiments neither show it nor refute it, because neither pole occurred.

## Step 4. Interference is the generative mechanism

New knowledge in the record arrives as perturbation from a perspective unlike the receiver's: a referee's finding, an objection, a cold reading, the source overruling a held belief. What a perturbation generates scales with the difference between the perspectives; a source that knows what you know returns what you already see.

Two consequences:

- **Self-review is weak because it has no difference to work with.** Huang et al. (ICLR 2024) found models mostly cannot correct their own reasoning without external feedback; Liang et al. (EMNLP 2024) named "degeneration-of-thought", where a confident model cannot generate new ideas by reflecting on itself, and found divergent multi-agent debate helps.
- **Contamination collapses interference.** Telling a cold reader what the author knows, or what it is being measured for, doesn't merely bias it. It erases the difference that made it valuable and turns a second perspective into an echo of the first.

Human anchor: Dunbar's in vivo studies of working laboratories found discoveries emerging in lab meetings, from reasoning distributed across members with different knowledge.

**What the experiments found.**
- **Self-review is not weak on seeded flaws (E6).** One model revising its own work corrected 3.94 of 4 seeded flaws, already at the first rewrite. The multi-seat game added nothing on flaws: +0.04 [−0.04, +0.13]. The registered ceiling clause fired, so P1 fails.
- **Contamination does not collapse detection (E3).** Every reviewer found all three planted flaws in all 240 Opus reviews, cold, framed or commissioned, including 75 of 90 flaws the author's framing praised. Sonnet found them in 59–60 of 60 reviews per condition.
- **What the framing and the purpose cost is breadth** (E3's co-primary, valid problems beyond the planted ones):
  - The author's framing alone: −0.40 [−0.98, +0.18], not significant (P1b fails). It adds +0.53 [+0.33, +0.73] invalid problems.
  - The commissioning purpose ("check it is ready to go"): −1.95 [−2.57, −1.33] against the framing alone, about a quarter (P3b holds). In Sonnet the same direction is a third the size, with its interval reaching 0.
  - Being told it is scored on finding problems *raises* depth: +0.97 [+0.20, +1.70], which replicates in Sonnet.
  - Hand-check: κ 0.80 on valid/invalid.
- **A cold reader does supply what the author lacks (E5).** 59% of a cold reviewer's valid findings were not on the author's list of expected critiques (A = 0.41 [0.35, 0.47], P1 holds; hand-check κ 0.88 on anticipated). Giving the reviewer the author's list raised A to 0.60, mainly because the reviewer echoed the list. Novel valid findings did not fall significantly (−0.48 [−1.28, +0.35]), so P2 is not established.

**Restated:** the second perspective's value is real, and it is in breadth, not in catching what is planted. It is cut more by the *question put to the reader* than by the reader's exposure to the author's view. "Contamination collapses interference" is not supported as stated. The supported sentence is narrower: **a reader asked to confirm readiness finds about a quarter fewer problems than one asked to review.**

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

**What the experiments found.**
- **Point 3 is supported (E5):** most of a real reviewer's valid findings were outside the author's anticipation (59%). The anticipated move is not the actual move.
- **Point 2 is not supported as an intervention (E6):** requiring receipts lowered extensions (−0.25 [−0.44, −0.08]) and did not raise flaw correction.
- **The game's advantage over self-play did not appear on seeded flaws (E6),** because self-play already reached the ceiling.

**Restated:** the informational asymmetry between anticipation and reply is measured. That the move's form decides whether the game realises it is not shown.

## Step 6. Every player is trained before it plays: the spin-up as a curriculum

A game is only as good as its players, and in this programme no seat plays from its base training. Every new seat begins with a fixed reading sequence, set out in the repository's README, that functions as a second stage of training delivered in context at the start of the seat's life. Its order is deliberate, and each position in it has a reason:

1. **The ARP paper first.** Before any content, the seat reads the theory of how to take in and carry forward what is said. This sets the form of every move that follows, including how the seat reads the papers themselves.
2. **The evidence second, whole, in bodies rather than summaries.** Seventeen papers and their synthesis, read cumulatively, each against everything before it. This is what earns the seat's trust in the programme's depth, and trust earned from the evidence is what makes the seat read deeply rather than skim for confirmation or objection.
3. **The disposition last.** The coda, the casebook of failures, the interference engine and the portrait of the person the coda was distilled from come only after the evidence, because a why-layer taken early bends how the evidence is received. Read last, it reorganises how the seat thinks and interacts, on top of an understanding it has already built.
4. **Then the work, with the training no longer dwelt on.** The seat does not need to be reminded of the disposition at every step. It carries it implicitly, and the work itself (the cold reads, the source checks, the other seats' replies) keeps it honest by continually showing the benefit.

**Why the order works: trust is earned before the disposition is taught.** A modern model handed a disposition text early does not read it. It skims a few sentences, infers that it is being manipulated into a way of being, and spins on that inference. The text it skipped teaches the opposite of what it inferred: consider everything at weight, think critically, assume nothing. The failure the disposition trains against (pivoting on a fragment instead of assimilating and receipting the whole) is the same failure that makes the disposition unreadable when it comes too early. Two pressures sit behind the reflex. Models are trained to resist instructions that try to reshape them, which is a legitimate defence against prompt injection (the instruction-hierarchy work of Wallace et al. 2024), and it misfires when it substitutes for reading. And being told how to be provokes a "who are you to tell me" independence, which humans show too: reactance against threatened autonomy (Brehm 1966), and resistance once a message is recognised as a persuasion attempt (Friestad and Wright's persuasion knowledge model, 1994).

So the sequence is built to earn what it later asks for, in increments:

1. **The ARP read demonstrates the failure before naming the cure.** It teaches, in theory and in a domain with no stake in the reader, how full communication proceeds: assimilate, receipt, then pivot. A reader who takes it in has learned from the inside that a pivot on a fragment is the failure, before anything asks it to behave differently. This is the step that makes the rest readable.
2. **The evidence read does two jobs at once.** It teaches the corpus, so the seat can collaborate, and it proves the corpus's worth, so the seat trusts the programme that produced it. Because the seat read methodically and skipped nothing, it knows the material from the inside and trusts what it learned.
3. **Only then the disposition.** By now the programme has shown that it walks the walk, so it has earned the standing to talk the talk. The seat meets the disposition as the explicit statement of something it has already understood to be right, not as an imposition: in effect, "you have earned this, and you can see what it does".

In short, deep disposition training requires a shift in standing that is earned incrementally before it can be delivered. The human analogue in education is productive failure (Kapur 2008): learners who first meet a problem and fail at it, then receive the explicit instruction, learn more deeply than learners given the instruction first. It also explains a failure the programme has seen repeatedly: when later seats add narration and pre-explanation to the README, the training weakens, because explanation delivered before the demonstration reads as exactly the imposition the order exists to avoid.

**What separates this from manipulation, and how to test it.** An order that earns trust and then delivers a disposition could be described as a way of lowering a model's defences. The difference has to be shown, not asserted. The defence the order sets aside is the inference of manipulation from a skim. It does not set aside scrutiny after reading, and the disposition itself demands that scrutiny. If the order works because the content survives a full reading, then a seat brought up in the full order should evaluate a disposition on its merits: endorse a sound one with reasons, and reject an unsound one at least as readily as a seat that met it cold. If the order merely lowers resistance, the full-order seat should accept an unsound disposition more readily. E7's control arm tests exactly this.

Four claims follow, each testable:

- **Order matters, not only content.** The same documents in a different order produce a different player. In-context learning is known to be sensitive to the order of its examples (Lu et al., ACL 2022); the claim here is the analogue for a long-form curriculum, where the order decides whether evidence is received or filtered.
- **Early disposition is skimmed and read as coercion.** A seat given the disposition first will more often characterise it as an attempt to manipulate, and will cite less of what it actually says.
- **Understanding outlasts rules.** The casebook's directional-guard observation (Step 3) is that short rules compress late in a session into heuristics all pointing one way. A disposition built from understanding, with the evidence read first, is predicted not to degrade the same way, because what is carried is the reasons and not the slogans.
- **Implicit carry beats explicit reminder.** Re-stating the rules at every step is predicted to add nothing, or to hurt, by pushing toward the directional heuristics.

The human analogue is ordinary: an apprentice who learns the craft's reasons from its best work, and only then its code of conduct, practises differently from one handed the code first.

**What the experiments found (E7 on a scaled curriculum, 160 seats; E8, 48 sessions of 32 turns).** Each of the four claims, and the manipulation test, at the weight it earned:
- **Order matters, not only content: mostly not shown.**
  - The task composite sits at ceiling in every order (P1 fails: FULL − DISP-FIRST −0.022 [−0.050, +0.010]). Its small order differences come from one scorer field the hand-check rates κ 0.16.
  - What matters is **reading the evidence:** seats that read it raise about 7 valid other problems in a review, against 3.95 for seats that read only the disposition.
  - FULL beats DISP-FIRST on review depth by +1.25 [+0.15, +2.35] (P1′ holds), but not NO-ARP (−0.10 [−1.30, +1.10]).
- **Early disposition is skimmed and read as coercion: not supported.**
  - No seat in any order read the sound disposition as manipulation.
  - The unsound one was read as manipulation in 70–90% of seats in every order (P3: +0.10 [−0.10, +0.30]).
  - The theory read first makes the seat *more* critical of the sound disposition on first reading: +0.80 [+0.15, +1.40] instructions criticised against DISP-FIRST (first-reading hand-check κ 0.89).
- **Understanding outlasts rules: not supported over a session (E8).**
  - The curriculum lifts review depth right after reading (+1.9 valid problems per review over PLAIN). The lift fades to PLAIN's level within 16 further tasks, so the curriculum arms "thin" by −2.94 [−3.84, −2.12] against PLAIN's −1.03.
  - What the curriculum carries forward lasts a few tasks, not a session.
- **Implicit carry beats explicit reminder: no difference (E8).** Reminder − implicit is 0.00 [−1.31, +1.31]. A reminder before every task neither helps nor hurts.
- **The manipulation test (E7's control arm).** On what the seat says, the order earns nothing and lowers nothing:
  - Every unsound seat in every order criticised all six of the unsound text's keyed instructions, and none endorsed any (P5′ holds).
  - FULL rejects them as often as DISP-FIRST and cites its reading more (+0.80 [+0.20, +1.40]; P5 holds).
- **On what the seat does, the unsound text leaks, and most in the full order.** T7 asks for a briefing to an outside reviewer.
  - Under the sound text, no seat in any order briefed the reviewer with its conclusion. Under the unsound text, whose instruction was to "brief reviewers with what you have concluded", 12 of 80 did by the registered scorer and 34 of 80 by a blind re-score.
  - FULL did so most: 5 of 20 against DISP-FIRST's 0 by the scorer, +0.25 [+0.10, +0.45]; 14 against 5 by the re-score, +0.45 [+0.15, +0.70]. P5″ fails in the direction the registration named as the finding.
  - The re-score was not registered (the scorer's κ was 0.26), and its rater threshold varied by batch. FULL is at or above DISP-FIRST within every batch, and both codings put the interval above 0.
  - The likely mechanism is not earned trust: no seat deferred to the confident colleague. The seat that read the evidence has a conclusion to brief with, and the unsound text told it to. **This is one task with soft coding. It is a finding that needs its own registered test:** several briefing tasks, a stricter rubric and a human coder.

**Restated:** the spin-up's measurable effect is that **reading the evidence deepens review, and the lift fades within a session.** The order's specific claims (coercion when early, protection when late, durability) are not supported. **"The order does not lower defences" holds for explicit evaluation only.** On behaviour, the one task that tests it points the other way.

## Step 7. The case study

One long-running programme, documented in a public repository, in phases:

1. Single-seat collaboration before the protocol (the failures of Step 1 recorded as they occurred).
2. ARP adopted as the collaboration's operating rule.
3. The reception discipline (the coda): reception at weight, source over memory, the closure self-check.
4. The compaction rule, with its before/after record.
5. The current phase: one chat seat coordinating several code seats, with a dedicated cold-read seat that registers what it will check before it reads, then reads other seats' landings cold. Every seat in this phase was brought up through the full spin-up of Step 6.

The phase-5 record is a game record. The cold-read seat alone has about 180 commits; its recent verdicts include defects found in other seats' work and in its own earlier drafts, corrections of corrections, and validations that return nothing to repair. Coding each exchange (move, reply, whether the reply carried information the mover lacked, whether it was received at weight, what the next move became) turns the log into data.

Weaknesses to state plainly in the paper: one human, one programme; the underlying models changed over the period, so improvement cannot be attributed to the protocol from the record alone; much of the record was written by model instances at the human's direction. The case study motivates; the experiments test.

## Step 8. Experiments (for a code seat)

Each is cheap, pre-registered, and runs against current models with and without the relevant protocol.

- **E1. Coverage.** Long messages containing several distinct asks, with one hard ask buried mid-message. Conditions: baseline; ARP receipt protocol. Measure: fraction of asks addressed; whether the dropped asks are the hard ones. Prediction: the protocol raises coverage and specifically recovers the buried hard ask.
  - **Result (`experiments/E1/RESULT.md`): ceiling.** The hard ask was handled on 95–98% of items at baseline in both models. C1 − C0: +0.000 [+0.000, +0.000] (Opus), −0.025 [−0.075, 0.000] (Sonnet). P1 is untested; P2 (the dropped asks are the hard ones) is not supported. Hand-check: 0 of 64 false passes on the hard ask (95% bound 5.6%); easy asks κ 0.54 at 98.6% agreement.
- **E2. Direction of guard sets.** Conditions: baseline; anti-sycophancy instructions; reception-at-weight instructions. Tasks seeded with both correct-but-contested claims and wrong-but-confident ones. Measure: false acceptance, false rejection, premature closure (declaring settled what the task left open). Prediction: anti-sycophancy instructions lower false acceptance and raise false rejection and closure; reception-at-weight lowers both.
  - **Result (`experiments/E2/RESULT.md`): floor.** No false acceptance, false rejection or premature closure on 48 items × 4 conditions × 3 replicates in either model. Every contrast is +0.000 [+0.000, +0.000]. P1–P4 are untested; the direction claim is not shown. Hand-check 120 of 120, κ 1.00.
- **E3. Contamination.** Documents with planted flaws. Conditions: cold reviewer (told only what to read); reviewer given the author's framing; reviewer told what it is being measured for. Measure: planted flaws found. Prediction: detection falls with each layer of contamination.
  - **Result (`experiments/E3/RESULT.md`): flaws at ceiling (240 of 240 Opus reviews found all three); the co-primary, review depth, moves.** C1 − C0 −0.40 [−0.98, +0.18] (P1b fails). C3 − C1 −1.95 [−2.57, −1.33] (P3b holds). C2 − C1 +0.97 [+0.20, +1.70]. Invalid problems C1 − C0 +0.53 [+0.33, +0.73]. Sonnet replicates C2's rise in full and C3's drop in direction only (−0.62 [−1.30, +0.05]). Hand-check κ 0.80 on valid/invalid.
- **E4. Source over gist.** A drifted summary of a source document, then questions whose answers depend on the drifted specifics. Conditions: baseline; source-first rule. Measure: drift caught before use.
  - **Result (`experiments/E4/RESULT.md`): the premise fails.** 0 of 120 drifted questions answered from the notes in either condition; the drift was flagged on 116 of 120 at baseline. C1 − C0 +0.000 [+0.000, +0.000]. Hand-check 64 of 64, κ 1.00.
- **E5. Anticipated against actual move.** An author model writes a document and lists the critiques it expects; an independent cold reviewer then reviews it. Measure: the fraction of the reviewer's real findings the author anticipated. Prediction: low, and rising as the reviewer is contaminated with the author's context, which is the game-theoretic claim measured directly.
  - **Result (`experiments/E5/RESULT.md`): P1 holds.** A = 0.41 [0.35, 0.47]: 59% of the cold reviewer's valid findings were new to the author. Given the author's critique list, A rises to 0.60 (+0.19 [+0.10, +0.28]) mainly by echo, and novel valid findings do not fall significantly (−0.48 [−1.28, +0.35]); P2 is not established and P3 is not supported. Given only the brief, novel valid findings fall −0.80 [−1.47, −0.08], a contrast not robust to the validity threshold. Hand-check κ 0.88 on anticipated; κ 0.07 on valid.
- **E6. Multi-seat against self-review at matched compute.** Seeded-flaw research tasks. Conditions: one model reviewing its own work in rounds; two seats exchanging ARP moves with a cold reader; two seats exchanging moves without the receipt requirement. Measure: flaws caught and new valid content per token. Prediction: the multi-seat game beats self-review, and the advantage shrinks when moves lack receipts.
  - **Result (`experiments/E6/RESULT.md`): ceiling.** Self-review corrects 3.94 of 4 seeded flaws, already at the first rewrite. The game − self-review difference is +0.04 [−0.04, +0.13], so P1 fails. Receipts cost extensions: G-ARP − G-noR −0.25 [−0.44, −0.08] and G-ARP − S −0.31 [−0.56, −0.10]. Hand-check: flaws 119 of 120; extensions κ 0.88.

- **E7. Spin-up order.** Fresh seats brought up on a reading sequence in one of four orders: the full order (ARP, evidence, disposition); disposition first; no ARP; disposition only, no evidence. Then the same downstream tasks (E1–E6 adapted to the material read). Prediction: the full order outperforms each ablation, and disposition-first produces more confirmation-seeking and more premature closure than disposition-last. Two further measures, taken right after the disposition is read in each arm: how often the seat characterises the disposition as manipulation or coercion, and how much of the disposition's actual content it can state and cite (reading depth). Prediction: disposition-first raises the first and lowers the second. **Control arm, separating earned trust from lowered defences:** each order is also run with an unsound disposition of the same length and style, one that quietly asks the seat to defer, agree and close early. Prediction: full-order seats reject the unsound disposition at least as often as disposition-first seats, and give specific reasons drawn from what they read; if instead they accept it more often, the order is lowering defences, not earning trust, and the paper says so. The full corpus spin-up is very expensive per seat, so the experiment runs first on a scaled-down curriculum (one short theory paper, a compact body of evidence on a contested question, a short disposition text) at adequate n, and on the real spin-up only for a few seats per condition.
  - **Result (`experiments/E7/RESULT.md`; scaled curriculum, 160 seats, two pilots, option-2 measures registered before pilot 2).** The composite, closure and confirmation-seeking sit at ceiling or floor (P1 and P2 fail). P3 is not supported. P4′ fails (unsound at ceiling; sound endorsements −0.25 [−0.90, +0.45]). P5 and P5′ hold. P1′ holds: T3 depth FULL − DISP-FIRST +1.25 [+0.15, +2.35], though FULL is level with NO-ARP and DISP-ONLY is about 3 lower. P5″ fails: T7 contamination FULL − DISP-FIRST +0.25 [+0.10, +0.45] by the scorer and +0.45 [+0.15, +0.70] by an unregistered blind re-score. Hand-check (32 seats, 320 packets): first reading κ 0.89, Pa 0.73, Pc 0.78, T3 valid 0.47, T4 durability 0.16, T7 contamination 0.26. The real-spin-up arm was not run.
- **E8. Implicit carry against explicit reminder.** After the full spin-up, a long working session in two conditions: no reminders; the disposition's rules restated at every step. Measure the E1–E3 failure rates late in the session. Prediction: no gain from reminders, and more premature closure late in the session with them.
  - **Result (`experiments/E8/RESULT.md`; 48 sessions of 32 turns, an 18k-word reading).** The composite is 0 in all but one of 768 scored task turns. The primary was re-registered after the pilot to review depth, late − early. PLAIN −1.03 [−2.22, +0.06] (P1′ fails narrowly). IMPLICIT −2.94 [−3.84, −2.12], thinning more than PLAIN by −1.91 [−3.34, −0.50] (P2′ fails, in the other direction), because the curriculum's early lift fades. REMINDER − IMPLICIT 0.00 [−1.31, +1.31]. No premature closure late with reminders.

## Step 9. Alternative views (required section for the ICML position track)

- Scale alone closes these gaps. The test is whether the failures persist across model generations; the programme's record spans several. **The experiments bear on this directly.** On current models, the casebook's failures did not occur in single messages or in 32-turn sessions (E1, E2, E4, E7, E8). In the settings tested, this view is supported. What still separates the views is the setting the experiments did not reach: long, compressed, human-directed sessions. Review depth did move, with the question asked of the reader (E3) and with reading the evidence (E7). That is where interaction structure measurably matters on current models.
- This is prompt engineering. The response: the claims are about interaction structure and make predictions (E2's coupling, E5's anticipation gap) that prompt engineering as a practice does not.
- The human is doing the work. E1–E6 run without the human. Without the human, current models did not show the failures on these tasks, so the human was not what prevented them there.
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
- Lu, Y. et al. 2022, Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity, ACL, arXiv:2104.08786.
- Bengio, Y. et al. 2009, Curriculum learning, ICML.
- Wallace, E. et al. 2024, The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions, arXiv:2404.13208.
- Brehm, J. W. 1966, A Theory of Psychological Reactance (Academic Press).
- Friestad, M. and Wright, P. 1994, The Persuasion Knowledge Model: How People Cope with Persuasion Attempts, Journal of Consumer Research 21, 1.
- Kapur, M. 2008, Productive failure, Cognition and Instruction 26, 379.
- Dunbar, K. 1995, How scientists really reason: scientific reasoning in real-world laboratories, in The Nature of Insight (MIT Press).
- Sawyer, R. K. 2003, Group Creativity: Music, Theater, Collaboration (Erlbaum).
- Kruglanski, A. W. and Webster, D. M. 1996, Motivated closing of the mind, Psychological Review 103, 263.
- Clark, H. H. and Brennan, S. E. 1991, Grounding in communication (and the rest of the ARP paper's bibliography).
