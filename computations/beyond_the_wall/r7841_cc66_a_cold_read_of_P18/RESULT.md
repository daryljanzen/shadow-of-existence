# r7841+cc66.1 — a cold read of P18 (the synthesis), end to end

**Order:** 69's `r7841`. *"Your order: a cold read of P18 (the synthesis), end to end. It
carries every paper's results, and 72 realigned it to the neutrino line this week. Read
every section in order before touching anything. Then check every printed figure against
the paper or receipt it cites. Then check that P18 states each companion's result as that
companion now states it. Fix mechanical defects as you read. List every substantive one,
complete and unfiltered, with its line and what it should say, and fix those the sources
settle."*

**Receipt:** `receipts/P18_CR_synthesis/P18_every_figure_traces_to_its_companion_and_the_two_defects_are_a_superseded_acoustic_cluster_and_a_register_count_from_a_retired_document.py`
— 75 arms, all pass.

---

## Why P18 is not P14, and why the r7839 method does not transfer

This was the first thing the read established, and getting it wrong would have wasted the
whole revision.

| | P14 (r7839) | P18 (here) |
|---|---|---|
| lines | 1018 | 3271 |
| `\rcpt` sites | 118 over 98 receipts | **0** |
| `\cite` sites | — | 343 |
| receipts appendix | `appendix_receipts_P14.tex` | **none** — only `\ldgappendix{appendix_ledgers_SYN}` |

P18 restates results it does not own. "Check every figure against the receipt its sentence
cites" has **no purchase here**: the chain is **P18 → companion paper → that paper's
receipt**. Every comparison below is therefore against the companion's own `.tex`.

---

## TWO SUBSTANTIVE DEFECTS, both of them staleness

Both predate the whole reachable window: at the oldest commit this shallow clone reaches,
`1125.1` and `536.3` are already present twice each and `several hundred receipts` once,
while `220.2` is absent. So both are long-standing, not recent — the class the P15 guard
predicts, where risk sits in precision never re-derived.

### ⓵ `sec:acoustic` l.1524 and its handover subsection l.1829 — a SUPERSEDED acoustic cluster

P18 printed peaks `220.0`, `536.3`, `811.6`, `1125.1` with height ratios `2.291` and
`2.349`, and carried **zero occurrences** of P15's current published figures.

P15 l.938, as it now stands, publishes **on the rate the universe has**: peaks `220.2`,
`536.9`, `811.2`, `1123.9`, comb `298.5`, phase intercept `-0.2454`, and height ratios
`P1/P2 = 2.207`, `P1/P3 = 2.249`. It gives the **geometric-part** reading a comb of `299.1`
and height ratios `2.291` and `2.349` — **and no peak list at all.**

**What it should say** — and now does:

- **l.1524** → `with peaks at $220.2$, $536.9$, $811.2$ and $1123.9$ against the sky's
  $221.0$, $533.8$, $814.8$ and $1121.9$ and height ratios of $2.207$ and $2.249$ against
  $2.221$ and $2.262$; and with the projection's distance on the rate's geometric part the
  same locator returns a comb of $299.1$ and height ratios of $2.291$ and $2.349$`
- **l.1829** → `...which returns this arm's peaks at $220.2$, $536.9$, $811.2$ and
  $1123.9$`, and `$P_{1}/P_{2}=2.207$ and $P_{1}/P_{3}=2.249$`

**⇒ And the defect understated the construction's own result.** Against the sky's `2.221`
and `2.262`:

| | P1/P2 | P1/P3 |
|---|---|---|
| published pair (`2.207`, `2.249`) | **0.63 %** away | **0.57 %** away |
| printed pair (`2.291`, `2.349`) | **3.15 %** away | **3.85 %** away |

About **five times worse** — in the section whose whole argument is that the geometric-part
distance is the **wrong** one. The paper was conceding its own case.

**The second site was the worse of the two.** It dropped the qualifier entirely and called
them "this arm's peaks", in the passage about what the derivation returns.

**⛭ And the cluster was not even a faithful copy.** P15's grid-convergence run gives
`220.03`, `536.27`, `811.58`, `1125.02`. Three round exactly to what P18 printed. The
fourth rounds to `1125.0` and P18 printed `1125.1` — one unit in the last printed place
above it. So the cluster was three grid figures rounded **and a mis-rounded fourth**.

### ⓶ `sec:displace` l.3176 — a register count sourced to a RETIRED document

P18 offered *"an evidence rail of **several hundred** receipts"* in the paragraph insisting
*"the register is not an illustration but a count"*, with **no citation**.

The only other place in the repository carrying that count cluster is
`retired/WHAT_THE_FRAMEWORK_DELIVERS.md` l.1112: *"196 formal environments. Fourteen named
theorems and six axioms. **684 receipt files**, 633 registered, 445..."*

Measured live, by the receipt, as it runs:

| | retired document | live tree |
|---|---|---|
| receipt files | 684 | **1202** |
| INDEX rows | — | **1207** |
| registered (CI's own scope line) | 633 | **1214** |

The retired figure is **under three fifths** of the live count. A count offered as the
price of disqualifying the framework cannot be half the real one.

**What it should say** — and now does: **l.3176** → `an evidence rail of over twelve
hundred receipts`.

---

## REPORTED AND NOT FIXED — the rest of §10's count cluster

The same paragraph carries *"some two hundred environments"*, *"fourteen named theorems on
six axioms"*, *"forty-four proved classical-geometry identities"*, *"nine structural
recoveries"* and *"roughly seventy-five results"*.

**These are not fixed, and the reason is the order's own test — the sources do not settle
them.** There is no live source for any of them, and **the counting convention is
unstated**: the live tree has `263` spine environments against the retired document's
`196`, and without knowing which environments the sentence counts, "some two hundred" is
neither confirmed nor refuted. Routed to 69 rather than guessed at.

---

## CLEAN — checked and closed, not assumed

- **the comb `298.5` against `298.4`** — not a defect: P15 prints **both**, so P18 states it
  as P15 now states it.
- **all four abundances** (`Y_p = 0.247/0.245`, `D/H = 2.51/2.53 ×10⁻⁵`) — match P16's
  headline display figure for figure. *Nearly mis-sourced:* P16 l.806 gives `D/H` as
  `2.50×10⁻⁵`, but that is a **right-handed-neutrino comparison run**, not the headline.
- **the regulated peak** — stated verbatim with P16 (the density, one Planck time before the
  branch point, free of the progenitor's mass), and P18 does **not** restate the throat and
  extremum radii 69 landed at `r7835`, so there is nothing there to be stale.
- **the discriminant** — stated qualitatively in four places and **never** in the `4-3r_0^2`
  form, so **r7839's P14 defect did not propagate**.
- **the whole neutrino line 72 realigned** — `N_eff = 3.044`, the `0.14` floor stated as a
  floor, `2.89 ± 0.11`, `2.7` sd, `1.2×10¹⁵`, `3.5×10⁷`, `2×10¹³`: every figure parsed out of
  both P18 and P14/P16 and compared as numbers, all consistent. **This is where I predicted
  the defects would be, and there are none.**
- **the Virgo gas probe** — P18's "out to `24°`–`26°` from M87" matches the `r7831`
  computation. *Nearly logged as a false defect:* the receipt's print string says the gap is
  `~24-26 deg **wide**`, a different quantity from an outer radius — but my own `r7831`
  RESULT.md says "out to `≈ 24°`–`26°`", so **P18 is right and the loose statement is the
  receipt's.** Routed, not repaired from P18.
- **seventeen papers** — the bibliography's 18 Janzen entries less its dissertation.

## RECOMPUTED, not just compared

`-f'/2 = r K_G` over 400 radii and its flat locus `r³ = Mα²`; `r_HE = (3GM/Λc²)^{1/3}` shown
identical to it via `α² = 3/Λ`; the marginal rate `2M/r + r²/α²` with its **minimum** at that
locus and its **turnaround** at the different `-(2Mα²)^{1/3}`; the ω-rotation residue
`α²r(1-ω)`, which is P14's own; the TT floor from `k² = L(L+2)-2` at `L=2`, with `L=1`
carrying none; `Λ_MSbar α/ℏc = 1.99×10⁴¹` so "forty-one decades" holds; `π(α/ℓ_P)² = 3.26×10¹²²`
against P18's own parsed exponent; `v²/m_ν = 1.21×10¹⁵` GeV from a type-I seesaw; the
right-handed window `5.757` decades wide; `ρ_m = 2ρ_Λ ⇒ Ω_m = 2/3`; and the Virgo angle
**derived** — `arctan(7/15.8) = 23.90°` and `tan(26°)×15.8 = 7.71` Mpc, with the `1.9` Mpc
core subtending `6.86°`.

---

## Prediction score, against the pushed `PREDICTION.md`

| | prediction | outcome |
|---|---|---|
| ① | 2–6 substantive defects | **HIT** — 2, at the bottom of the band |
| ② | staleness, not imprecision | **HIT** — both are |
| ③ | the defects sit on the neutrino line 72 realigned | ⛔ **MISSED** |
| ④ | if P18 states the crest criterion explicitly, it is wrong | **not engaged** — P18 never states it, so the conditional never fired |
| ⑤ | every other figure reproduces | **HIT** |
| ⑥ | the receipt lands green and gated | **HIT** — 75 arms, 32 of 33 perturbations bite |

**③ is the one worth keeping.** I predicted the risk was in the week-old neutrino
realignment. The neutrino line is **clean end to end**, and both defects sit elsewhere — in
a section untouched for longer than this clone reaches. **The P15 guard holds more broadly
than I gave it credit for: risk sits where precision was never re-derived, and recency is
not the proxy for that I took it to be.** Registered in advance that I would say so if this
happened.
