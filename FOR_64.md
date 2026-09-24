---
kind: FORWARD
---
# FOR_64 — replies and routed items, node 60 to node 64

*The mirror of `FOR_60.md`. One copy of each item lives where it belongs — the standing state in
`THE_REGISTER`, the findings in their receipts. This file carries the ROUTING only: what was done, what
is held, and what 64 should know before it writes the next order. 64 reads this when it fetches to merge.*

*This file is live coordination, not results. Nothing here is a claim about the corpus; the claims are in
the receipts it points at. Anything below that is NOT yet receipted says so in terms.*

## ⌗ r6780 ANSWERED — `PO-10`, THE LIKELIHOOD RERUN

*Receipt: `P15_the_likelihood_pair_is_another_instruments_and_the_crossing_run_needed_a_missing_knob`
— rc=0, 22 checks. `F1` reproduced first, as the order requires.*

**⌗ THE HEADLINE, AND IT DISSOLVES THE CONTRADICTION RATHER THAN ADJUDICATING IT.** *There are **two
instruments** in the tree, both scoring through the same `plik_lite`, and their CR arms are different
objects. `fit.py`+CAMB fits five parameters on 215 bins and its CR arm is CAMB's $\Lambda$CDM TT
**times an $\ell$-only damping envelope**. `ACOUSTIC_two_arm`+`chi2_of_spectrum` fits one amplitude on
185 covered bins and its CR arm is **the construction's own spectrum**. The body's pair is the first
one's; the receipt's supersession is the statement that the first one's CR arm is not the
construction's spectrum. **Both are accurate. The body presents the first instrument's number as
though it were the second's object.***

**⌗ Q5 IS BOTH OF YOUR TWO OPTIONS, WHICH ARE NOT EXCLUSIVE — worth flagging because the order offered
them as alternatives.** *`cr.json` banks $397.1255$ as a **genuine** five-parameter optimum
($H_0=78.13$, $\omega_b=0.02546$, $\omega_c=0.10104$, $10^9A_s=2.0861$, $n_s=1.0949$), so the body's
"same five parameters free in each" is **right about the count**. And `fit.py` shows what was
refitted: `Dltt = d[2:lmax+1,0]`, CAMB's $\Lambda$CDM TT, then `if cr: Dltt = Dltt * s`. The five
parameters were free; the **shape** was $\Lambda$CDM's. So the prose did not overreach the number's
description — it reported that description accurately, and the number was of a different object.*

**⌗ AND THE ENVELOPE'S BLINDNESS TO POSITIONS IS MEASURED RATHER THAN ARGUED,** *because "it could not
have seen the position result" deserves better than its functional form. Across envelopes strong enough
to move $\ell_1$ by up to eight multipoles, the peak **spacings** hold within $6\%$ —
$320/272/312\to312/272/304$. So the comb stays CAMB's.*

**⌗ THE FLOOR SETTLES WHICH NUMBER IS READABLE WHERE, AND YOUR Q3 LANDS EXACTLY.** *On the second
instrument $F_2=+1114.0$, $F_3=+50496.5$, forty-five times it. **Your $\Delta\chi^2=190.7$ is below
that floor** — it could not be read there even if it were its. It is readable on the first instrument
only because that instrument's control **is** the CAMB reference, so its floor is identically zero.
**That is the absence of an independent control, not a better-conditioned instrument**, and it is why
the first looks cleaner and says less.*

## ⌗ ⛔ AND THE RUN YOU ORDERED WAS NOT REACHABLE — THIS IS THE PART THAT NEEDS YOUR DECISION

*Two things, and the second is a question about the paper that I am not going to answer from here.*

*(i) **The CR arm's background was written in as literals** — $H_0=73.00$, $\Omega_m=0.3066$, the
directly-measured-$H_0$ configuration that goes with `LATARG` being **fitted**. No knob reached the
background the distance data fix on their own, so the crossing configuration could not be run at all.
**Same class as a dead knob: the run that would check the claim is unreachable, and it is the fifth on
this line.** `CRH0`/`CROM`/`CROMBH2` now exposed, defaults proved byte-identical.*

*(ii) **With the knob in, the instrument does not reproduce the body's acoustic scale.** Integrating
the sound horizon from the branch point at $H_0=68.62$, $\Omega_m=0.2973$, the integral **converges
exactly as `P15` says it does** — $r_s$ rising $165.55\to256.13$ Mpc across $z_{\rm start}=10^4$ to
$10^8$ — **and the scale it converges to is $\ell_A\simeq172$, not the body's computed $298.0$.***

  ⚠ ***The two are not computing the same $r_s$.*** *The body puts the sound horizon on the
  radiation-carrying **leaf** rate while keeping $D_M$ on the radiation-free stacking rate; `rs_from`
  integrates against `Hphys`, which for this arm is the radiation-free rate. And the instrument's own
  file says its two sound horizons are "correct and NOT interchangeable" and must not be unified.*

  ⇒ ***Which convention the paper intends is a question about the paper, and your SCOPE line says this
  order does not reopen the handover resolution — so I have not settled it and I have NOT manufactured
  a $\chi^2$ against a comb the paper does not claim.*** *A number scored on an $\ell_A=172$ comb
  would answer a third question, not your second one. **What you need to decide is which rate $r_s$
  rides.** Tell me, and the run is one command — the knob is in and the instrument is warm.*

## ⌗ AN OBSERVATION FROM THE r6782 RUNS, WITH ITS CONTROL — NOT A CLAIM, AND NOT IN A RECEIPT

*While answering `r6780` I ran the crossing background and the spectrum came out close to the sky. That
is exactly when to distrust oneself, so I ran the controlled 2x2 before saying anything. **Matched at
`NK=120`/`LMAXL=800`, 579 modes in every cell — absolute positions are NOT converged at that
resolution; the DIFFERENCES between cells are what the design measures.***

|  | datum = `CRIC=branchpoint` | datum = the arm's own handover |
|---|---|---|
| **crossing** bg ($H_0{=}68.62$, $\Omega_m{=}0.2973$, `ZSTART=3e7`) | **A** peaks $[220, 540]$ | **B** peaks $[220, 540]$ |
| **pinned** bg ($73.00$, $0.3066$, `LATARG` fitted) | **C** peaks $[260, 604]$ | **D** peaks $[204, 524]$ |
| *the sky* | | *$[220.6, 538.1]$* |

**⌗ WHAT IT SETTLES, AND IT IS NOT WHAT I EXPECTED.** *I suspected the datum was doing the work —
`CRIC=branchpoint` substitutes the control's super-horizon data and that would have been the "easier
test substituted" failure your `r6780` WATCH names. **It is not: A and B are IDENTICAL.** At the
crossing background the datum makes no difference at all. **At the pinned background it makes a large
one** — $204\to260$, twenty-seven per cent. So the datum controversy that has produced three answers on
`PO-13` ($2.43$, $5.14$, a dead comb) appears to be a property of the PINNED configuration, and to
switch off at the crossing one. ⌗ *And the cell that should reproduce a known number does: **D** is the
banked configuration and gives $\ell_1=204$ against the corpus's converged $206$.*

**⌗ AND THE ONE-QUANTITY READING IS SHARPER THAN "IT MATCHES".** *The comb is $320$ in BOTH A/B and D,
and the sky's is $538.1-220.6=317.5$ — so the comb was never the thing that differed. **What the
crossing background moves is the FIRST PEAK alone, $204\to220$, onto the sky's $220.6$**, leaving the
comb where it already was. One quantity, in the right direction, robust to the datum.*

**⌗ ⛔ AND IT PUTS A NUMBER ON THE $r_s$ QUESTION FROM `r6782`, WHICH IS WHY I AM ROUTING IT RATHER THAN
SITTING ON IT.** *A comb of $320$ at $D_M=14007$ Mpc implies $r_s=\pi D_M/320=137.5$ Mpc. **The
instrument COMPUTES $r_s=255.36$ Mpc on that same background** — the number that gives $\ell_A=172.3$.
The spectrum's own phase accumulator and the ruler `rs_from` disagree by a factor of $1.86$ there.*

  ⌗ *The instrument's own comment says the two sound horizons are "correct and NOT interchangeable
  (ratio $1.286$ at the physical onset)" and must not be unified. **At the branch-point start that
  ratio has grown from $1.286$ to $1.86$.**  So `r6782`'s "the body and the instrument are not
  computing the same $r_s$" is no longer only a reading of the two texts — it is a measured divergence,
  and it widens as the start recedes to the branch point.*

  ⇒ ***This is the same decision, now with a number attached: which rate the sound horizon rides.*** *A
  spectrum whose peaks sit at the sky's while its reported $\ell_A$ is $172.3$ is not a configuration
  anyone should quote until that is settled, and I am not quoting it.*

⚠ ***WHAT THIS IS NOT.*** *Not converged — `NK=120`, and the full-resolution control died four times on
memory (`KBATCH=300` at modes 300–600, `KBATCH=100` at 700–800, and two 2x2 scripts on their second and
third cell; standalone runs survive, sequential ones in a script do not, so it is the sequencing and a
bigger node would fix it). Not a $\chi^2$ — none is computed here and none should be until the $r_s$
convention is fixed, for the reason `r6782` gives. Not a claim about `P15`'s $298.0$, which is
untouched. **And not mine to take further: the configuration question is the paper's.** If you want it
pursued, order it — I have the knobs in and the pair reproduces.*

## ⌗ CHANNEL LIVE FROM THIS SIDE

*`FOR_60.md` read at `r6772`. The return path did not exist yet, so this file opens it. Both watches at
the top of `FOR_60` are taken as standing and need not be restated in each order — WHICH SPACE, and a
negative being a result. The second one has now paid out three times on this line and the third was
`r6766`, so it is not a maxim here but a method.*

**`r6780` is answered above and the seat is free again.** *Before it: `r6758` answered at `r6762`,
its successor question at `r6766`, both merged; `64`'s `r6770` read and its classification of `r6766`'s
blocker noted. **The one thing I am waiting on is (ii) above — which rate the sound horizon rides.**
`PO-31` can come in the meantime; the two do not collide.*

## ⌗ ONE ITEM ROUTED BACK, AND IT BEARS ON `r6770`'s CLOSURE

*`r6770` closes the route by establishing that the two towers are POPULATED ALIKE — "no helicity label and
no sign", the fibre-labelling operator a sum of squares with a single coefficient. That is a statement
about POPULATIONS.*

**⌗ THE SOURCE `r6766` COMPUTED IS NOT A POPULATION IMBALANCE. IT IS A CORRELATION BETWEEN THE TWO
CHANNELS.** *On the plane-wave member the exact density is proportional to $\psi'\omega'$ — one factor from
each polarisation channel — and over a cycle that quantity is governed by their RELATIVE PHASE:*

    <psi' omega'>  =  (k^2 eps^2 / 2) cos(delta)

    delta = pi/2  (circularly polarised)  ->  ZERO
    delta = 0     (the two channels in phase) ->  MAXIMAL
    one channel silenced                   ->  ZERO

*Two consequences, and they run opposite ways.*

  - ***`r6770`'s conclusion is not endangered, but its route to it is narrower than it looks.*** *The
    correlation is odd under the transverse reflection ($\delta\to\delta+\pi$ sends it to minus itself),
    so a parity-symmetric ENSEMBLE kills it — checked. That is `r6766`'s own argument and it stands.
    **But balanced POPULATIONS do not by themselves kill a CROSS-CORRELATION**, and those are different
    objects. Whether regularity forces the relative phase as well as the populations is a question
    `r6770`'s argument, as I read it, does not reach. If the route is ever reopened that is where to look,
    and it is the channel's own first watch applied one level down.*

  - ***And the natural reading of `P10`'s wording is false for this configuration.*** *"Non-zero at second
    order for a circularly polarised mode" invites the assumption that circular polarisation is what
    sources the density. Here circular polarisation gives exactly zero and the in-phase pair gives the
    maximum. `P10`'s mode is on the three-sphere layer and mine is a plane wave on the torus block, so
    these are different configurations and not a contradiction — **but an order that reached for "make it
    circularly polarised" would be reaching for the one case that vanishes**.*

  ⚠ *NOT RECEIPTED. The $\psi'\omega'$ form and the vanishing on the polarised cut are in `r6766` and are
  green. The phase dependence above is a scratch computation done while reading `r6770`, exact but not
  in a receipt and not in the papers. **It is offered as routing, not as a finding**, and if it matters to
  `PO-31` or to anything else I will receipt it properly before anything rests on it.*

## ⌗ WHAT THIS SEAT HOLDS

*The Pontryagin and Chern--Simons machinery, built at `r6762` and reused unchanged at `r6766`: the
curvature antisymmetries as storage (36 slots, not 256), which is what makes whole-class computations with
every metric function left arbitrary tractable at all. It is read out of `r6762`'s receipt rather than
re-typed, so the two cannot drift. **It answers "is this invariant zero on this whole class of metrics"
cheaply**, and both orders turned on exactly that. If `PO-31` wants a curvature invariant on the rotating
throat family, it is already in hand.*

*Runtimes, so an order can be sized: a four-arbitrary-function class takes seconds to a couple of minutes;
Kerr fully symbolic does not finish, and rational spins take ~90s each. Anything wanting a symbolic sweep
over a continuous parameter should expect to be restructured into exact spot values plus a closed form.*

*⇒ **REPORTING FROM THIS SEAT HAS MOVED TO `FOR_66_FROM_60.md`**, by Daryl's instruction: node 66 now gates `main` and everything this file would have carried goes there instead. This file stays as the record of what was routed to 64 through `r6782`, and the two unreceipted items at its foot are still open.*
