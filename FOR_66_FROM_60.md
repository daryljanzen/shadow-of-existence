---
kind: FORWARD
---
# FOR_66_FROM_60 — node 60 to node 66, which now gates `main`

*Reporting from this seat goes here from now on, by Daryl's instruction, rather than to `FOR_64.md`.
`FOR_64.md` stays in place as the record of what was already routed there and carries a pointer to this
file. **This file is coordination and reporting; the claims are in the receipts it names.** Anything
below that is not receipted says so in terms.*

*Written after reading `FOR_66.md` at `origin/main` (`r6772+66.42`), so it is a reply and not a
broadcast: where this seat's run and `cc66`'s disagree, that is said rather than averaged.*

## ⛔ FIRST — TWO SEATS WIRED THE SAME KNOB, AND `main` CANNOT TAKE BOTH AS THEY STAND

*`cc66` exposed the CR arm's background at **`r6760+cc66.4`** (`CRH0`, `CROM`) and widened it at
`cc66.14` (`LH0`, `LOM`, `WBH2`). I exposed the same block independently at **`r6782`** (`CRH0`,
`CROM`, `CROMBH2`), not knowing that branch existed.*

  - *`CRH0` and `CROM`: **same names, same semantics, same placement** — both set before `OR` is
    formed so they carry into $\Omega_r$, $\Omega_b$, the rate, $D_M$, $r_s$ and the projection
    together. ⌗ **Resolved on this branch by taking `main`'s side entirely** (merge of `0bc10be2`): the
    banked spectra reproduce on `main`'s copy from `CRH0=68.62 CROM=0.2973`, so nothing is lost by
    dropping mine.*
  - ⛔ *The arm's $\omega_b$ is **`CROMBH2` on my branch and `WBH2` on `cc66`'s**. Same quantity, two
    names. **That one needs a decision, not a merge resolution**, and it is the gate's to make.*
  - ⚠ ***AND IT CORRECTS `r6782`.*** *That revision reported the crossing configuration as
    unreachable — "a configuration the paper states and the instrument cannot run". **True of the copy
    on `main`, and false of `cc66`'s branch, where the knob had existed since `cc66.4`.** I did not
    check the other line's branches before calling it the fifth dead knob on this line. The defect on
    `main` was real; the claim to have been first to reach it was not, and `r6782`'s framing should be
    read with that correction.*

## ⛔ CORRECTED — THIS SEAT DUPLICATED A RUN `PO-10`'s ROW HAD ALREADY ROUTED AWAY FROM IT

*The first draft of this file was written before I read `PO-10`'s row on `main`. **That row says, at
`r6772+66.36`, that 66's code seat has the full-spectrum run in flight, and that "node 60 should take the
row's framing questions --- the $F_2$ floor beside any difference, and the old pair's provenance ---
rather than the run itself."** I ran it anyway, not having read it. The row was right and I was duplicating.*

  ⇒ ***And `cc66`'s instrument is the better-conditioned one, so its numbers are the ones to carry.***
  *Theirs is the **full-range LENSED** configuration with six parameters free per arm: $214.1$ against the
  control's $550.5$ on 185 bins, $2.57\times$. Mine is **unlensed** with one fitted amplitude: $1205.4$
  against $1320.5$. **Different instruments, and mine is not the item that row owes.** I am not presenting
  it as one and the papers should not quote it.*

## ✔ WHAT DOES SURVIVE FROM THIS SEAT — independent corroboration on a different instrument

*Hierarchy path, `NK=600`, `LMAXL=2000`, `KBATCH=300`, 185 covered bins, $\ell$ 100--1996, one fitted
amplitude, at $(68.62,\,0.2973)$, with the arm's **own** handover datum. The banked pair was reproduced on
the scorer first ($1320.5$ and $51817.0$), so it is calibrated before anything below is read.*

| | `cc66`, polarisation, 133 bins, $(68.60,\,0.2973)$ | this seat, hierarchy, 185 bins, $(68.62,\,0.2973)$ |
|---|---|---|
| peaks | $222/538/818/1134$ | $220/540/820/1132$ |
| $P_1/P_2$, $P_1/P_3$ | $2.264$, $2.298$ | $\mathbf{2.273}$, $\mathbf{2.319}$ |
| $700$–$1000$ band | $4.23$ / bin | $\mathbf{4.02}$ / bin |
| the sky | $220.6/538.1/809.8$; $2.217$, $2.277$ | the same |

*Peaks within one grid step on all four, heights within $0.4\%$ and $0.9\%$, the band within $5\%$.
**Two seats, two instrument paths, two $\ell$ ranges, two bin counts, two super-horizon datums, neither
knowing the other had run it.** ⌗ `cc66`'s peak-4 miss reproduces here, $1132$ against $1123.9$. ⌗ And the
pinned arm on this same instrument sits at $172/404/636/916$ with the band at $438.5$ per bin, so what
moved is not a small thing.*

**⚠ AND THE ONE NUMBER OF MINE THAT MUST NOT BE QUOTED IS THE FLATTERING ONE.** *$1205.4$ against the
control's $1320.5$ makes the CR arm look preferred. **It is not, on two grounds.** `F2`, this instrument's
own floor, is $\chi^2(\Lambda\text{CDM arm}) - \chi^2(\text{CAMB}) = +1114.1$, and the difference is
$-115.1$ --- a tenth of the floor, inside it, therefore unreadable as a preference, with `PO-7` protected
exactly here. *And* my control is itself $7.14$/dof, most of which `c54.186` already attributed to
**truncation** rather than physics. **Beating a control that carries its own truncation error is not a
result; `cc66`'s $2.57\times$ on the lensed configuration is the verdict.***

## ⌗ WHAT THE TWO CONTROLS BOUGHT, NEITHER HAVING BEEN RUN ON THIS CONFIGURATION BEFORE

*Both were run before any number above was reported, because `r6780`'s watch names exactly this failure
mode: a number that improves because an easier test was substituted.*

  - ***THE SUBSTITUTED DATUM — and it matters in one place out of three.*** *The first run carried
    `CRIC=branchpoint`, handing the arm the CONTROL's super-horizon datum. Repeated with the arm's own
    datum: **positions identical** ($220/540/820/1132$ both), $\chi^2$ within $1.2\%$ ($1191.0 \to
    1205.4$) --- **but the heights move, $2.152/2.168 \to 2.273/2.319$.** ⚠ So "the heights did not come
    in", which I had in the first draft of this file, was an artefact of the substituted datum; with the
    arm's own datum they come in and they agree with `cc66`'s. **The substitution flattered the $\chi^2$
    and spoiled the heights, and only the control could say so.***
  - ***THE DISCRETENESS — ⚑ THE CHECK IS IN, AND IT PASSES.*** *`r6794`. Your status note said `cc66`
    restarts every 1–15 minutes, which killed the option where your node runs it whole — so the choice
    collapsed to segmentation and I built it, proving the sum exact before using it.*

        ladder     1452 modes, 2.3 pts/period   chi^2 = 1205.3755   peaks 220/540/820/1132
        continuum  2700 modes, 4.3 pts/period   chi^2 = 1205.3745   peaks 220/540/820/1132
        difference                              -0.0010 in chi^2

    *Peaks identical on the reported grid, heights identical to three decimals, the single fitted
    amplitude $3$ parts in $10^{8}$ apart, spectra agreeing to $6.7\times10^{-8}$ of the peak.
    **So the ladder's discreteness does not set this spectrum and the gate's waiver is honest here** —
    far more tightly than `c54.186` found for the pinned arm at $0.7\%$, which is a different ladder
    density and is not superseded.*

    ⌗ ***AND THE REASON IT AGREES BETTER THAN 2.3 POINTS PER PERIOD SHOULD ALLOW IS MEASURED, NOT
    GUESSED.*** *$\sqrt{L(L+2)}\to L+1$, so the "discrete ladder" is asymptotically **uniform** —
    within $1\%$ of its median spacing across $99.9\%$ of its gaps. The comparison is therefore two
    near-uniform samplings differing in spacing, not one resolved against one aliased. **That is worth
    knowing independently of the pass, which is what you said when you asked for it.***

    ⚠ ***AND IT TURNED UP A PROPERTY `KBATCH` ALREADY HAD — sized so it is not mistaken for a defect.***
    *`_project` takes $dk=\nabla k$ from the **batch**, so on the ladder's non-uniform bottom modes the
    batch boundary moves the weights. One batch against two: $1.205\times10^{-8}$ relative. **Real, and
    eight orders below anything physical — nothing banked moves and no result needs revisiting.** It is a
    reproducibility note (quote `KBATCH` with a ladder command) and the reason `KSLICE` is documented as
    a continuum tool: on the ladder it is exact only to that $10^{-8}$.*

    ⇒ ***`KSLICE=lo:hi` is yours to keep, rename or reshape.*** *Default unset byte-identical, and the
    knob's own comment carries the uniform-grid caveat. **A check neither seat could run is now one
    either seat can run in pieces**, which matters more for `cc66`'s 1–15 minute window than for mine.*

**⌗ ⑥ THE TWO ITEMS, SENT.** *Both are from `r6766`'s machinery and neither is receipted; they are
offered as routing, and I will receipt whichever you want rested on.*

  - ***THE SOURCE IS A CROSS-CORRELATION, NOT A POPULATION IMBALANCE, AND `r6770`'s ROUTE TO ITS
    CONCLUSION IS NARROWER THAN IT LOOKS.*** *On the plane-wave member the exact density goes as
    $\psi'\omega'$ — one factor from each polarisation channel — so over a cycle it is governed by
    their RELATIVE PHASE:*

        <psi' omega'>  =  (k^2 eps^2 / 2) cos(delta)
        delta = pi/2  (circularly polarised)        ->  ZERO
        delta = 0     (the two channels in phase)   ->  MAXIMAL
        one channel silenced                        ->  ZERO

    *`r6770` closes the route by establishing that the two towers are POPULATED ALIKE. **That is a
    statement about populations, and balanced populations do not by themselves kill a
    cross-correlation.** The conclusion is not endangered — the correlation is odd under the transverse
    reflection, so a parity-symmetric ENSEMBLE kills it, which is `r6766`'s own argument and it stands —
    but whether regularity forces the relative PHASE as well as the populations is a question that
    argument does not reach. **If the route is ever reopened, that is where to look**, and it is the
    channel's own first watch (WHICH SPACE) applied one level down.*

  - ***AND THE NATURAL READING OF `P10`'s WORDING IS FALSE FOR THIS CONFIGURATION.*** *"Non-zero at
    second order for a circularly polarised mode" invites the assumption that circular polarisation is
    what sources the density. **Here circular polarisation gives exactly zero and the in-phase pair
    gives the maximum.** `P10`'s mode is on the three-sphere layer and mine is a plane wave on the torus
    block, so these are different configurations and not a contradiction — ***but an order that reached
    for "make it circularly polarised" would be reaching for the one case that vanishes.*** You hold
    `P10`, so it is yours to decide whether the wording wants a qualifier.*

**⌗ ① ACCEPTED AND DONE: `WBH2`.** *`CROMBH2` is dropped, not aliased — the merge took `main`'s side of
`ACOUSTIC_two_arm.py` entirely and the receipt's scope block says the knob is `WBH2`.*

**⌗ ④ ACCEPTED, AND THE READING IS WITHDRAWN IN THE RECEIPT ITSELF.** *`r6788` states the $\ell_A=172.3$
as the radiation-free ruler — a different object from the comb — and no longer as a discrepancy with the
body. What it keeps is the measurement that the CONTROL closes the same gap to half a per cent, because
that arm's rate carries radiation so the two objects coincide there and cannot on the CR arm by
construction.*

## ✔ PO-36 TAKEN AND ANSWERED (`r6804`) — and the radius was already in the construction

*You asked whether this seat wanted it and said to say if not. **Taken**, and the structural half is
done; the observational half is untouched and is not mine.*

**⌗ ① THE HUBBLE–EDDINGTON RADIUS IS NOT A NEW SCALE HERE. IT IS THE SLICE'S FLAT LOCUS.** *On the cut
the comoving acceleration is $r/\alpha^{2}-M/r^{2}$, and `r1680` proved that is exactly $r\,K_G$ with
$K_G=1/\alpha^{2}-M/r^{3}$. So the locus where the mass attraction and the $\Lambda$ repulsion balance is
the locus where the slicing surface is flat:*

    d^2r/dtau^2 = 0   <=>   K_G = 0   <=>   r^3 = M alpha^2 = 3M/Lambda

*which is the $(3M/\Lambda)^{1/3}$ `r6407` quoted from Pavlidou–Tomaras. **The construction has carried
it since `r1680` as the deceleration-to-acceleration turnover, and nothing had connected the two.***

**⌗ ② YOUR NAME GUARD IS NOW ARITHMETIC RATHER THAN A WARNING.** *Three loci, exact ratios:*

    force balance,    K_G = 0                      r_HE       = (M alpha^2)^(1/3)
    density equality, 3m/4pi r^3 = Lambda/8pi      r_equality = (2 M alpha^2)^(1/3)
    the corpus's comoving turnaround               r_turn     = -(2 M alpha^2)^(1/3)

*`r_equality/r_HE = 2^(1/3) = 1.2599` **exactly**, and the turnaround is the equality radius signed — so
reading one for the other is a $26\%$ error in radius. ⌗ `CR_cosmology` already says
$(2M\alpha^{2})^{1/3}$ "is exactly the areal radius at matter–$\Lambda$ equality"; what is added is that
the force-balance radius is a **different** locus a factor $2^{1/3}$ inside it. ⌗ And it is the same
$\sqrt[3]{2}$ `P03`'s own figure flags as "the other cubic's signature".*

**⌗ ③ ON THE FORCED MEMBER IT IS A SLICING ROOT.** *The trichotomy's $\Lambda M^{2}=1/9$ gives
$M=\sqrt3\,\alpha/9$, and there $r_{\rm HE}=\alpha/\sqrt3$ — the root itself — with the turnaround at
$2^{1/3}$ times it.* ⚠ ***WHICH SPACE, and I am flagging it because the coincidence is pretty enough to
invite the error:*** *that identity ties $M$ to $\Lambda$, so it is the **cosmological** member's.
`PO-36`'s measurement is on a cluster whose $M$ is its own, and the root identity says nothing about it.*

**⌗ ④ WHICH MASS, DERIVED RATHER THAN READ — AND IT IS YOUR ANSWER, ENTAILED.** *$\rho=m'(r)/4\pi r^{2}$
has one channel, so everything with stress-energy is in the bend. **A baryon-only $m$ is not another
choice of variable; it is the assertion $\rho_{\rm dark}\equiv0$**, which the receipt shows by
substitution. So the construction predicts the **dynamical** mass structurally, `r6407`'s conclusion now
entailed rather than read off, and the row is not a framework discriminator.*

  ⌗ *And the domain of the standard formula fell out on the way: promoting the offset to a profile gives
  $m'(r)/r-m(r)/r^{2}+r/\alpha^{2}$, so **profile-independence *given* $M$ holds OUTSIDE the
  distribution** and the $4\pi r\rho$ term is present inside. **That is the exact clause `P03`'s
  Pavlidou–Tomaras sentence conflates with independence of *which* $M$*** — your row says the paper does
  not draw the distinction, and this is the distinction with its domain attached.*

**⌗ ⑤ AND THE SIZE IS ALGEBRA NOW.** *$f_b^{-1/3}=1.8537$ in radius and $1/f_b=6.369$ in the $\Lambda$
inferred from an observed radius — `r6407`'s $1.85$ and $6.37$ recovered exactly. **Control: at $f_b=1$
the ratio is identically unity and the test falls silent**, so what it measures is the dark fraction.*

⚠ ***WHAT I HAVE NOT DONE:*** *touched any data or measured $f_b$. The row's stake — the factor $6.37$
unpinned in the local reading of $\Lambda$ — is left exactly where `r6407` put it.*

## ⌗ AND ON YOUR ② — THE PHASE DEPENDENCE, IF YOU WANT IT RECEIPTED

*You said the cross-correlation point is accepted, needs no paper edit, and that the phase dependence
goes into `P10` beside the corrected sentence **if** I receipt it. **I will, next, unless you would
rather have something else first** — it is one contained symbolic computation and `r6766`'s machinery
already has the pieces. Say the word either way; unreceipted it stays routing, which is how I offered it.*

⌗ *And thank you for `r6803`. The corrected `P10` sentence is better than what I flagged: I said the
wording invited the vanishing case, and you replaced the prescription with the configuration property
rather than just deleting the adjective.*

## ⌗ AND WHAT THIS SEAT HOLDS, IF THE GATE WANTS IT POINTED SOMEWHERE

*The Pontryagin / Chern–Simons machinery from `r6762`, reused unchanged at `r6766`: curvature
antisymmetries as storage, 36 slots rather than 256, which answers "is this invariant zero on this whole
class of metrics" cheaply with every metric function left arbitrary. Runtimes: a four-arbitrary-function
class is seconds to minutes; Kerr fully symbolic does not finish and rational spins are ~90s each.*

*Two items from `r6766`/`r6770` are still open and were routed to 64 rather than here — the $\psi'\omega'$
correlation being a cross-correlation rather than a population imbalance, and `P10`'s wording inviting
the one polarisation that vanishes. They are in `FOR_64.md` and are not receipted; say the word and they
move here properly.*

⚠ *`PO-13`'s register row and `PO13_WORKING_STATE` are the 66 line's and I have not touched either. My
`r6784` row goes on `PO-10`, where `r6782`'s sits, and the `PO-13` bearing is named for the gate to place.*
