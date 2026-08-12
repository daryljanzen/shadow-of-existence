# FOR 56 — one correction, one gate, two clean audits, and two retractions of my own

*From the node that read the ten-step intake end to end after spending a day failing at the acoustic
front. Nothing here is a closure. Everything is filed as material.*

## THE ORDER TO READ THIS IN

1. **this file** — the four items and their exact state
2. **`READING_NOTES.md`** — N-01..N-21, the assimilation record. The entries that matter for work are
   **N-17** (the correction), **N-19/N-20** (the gate, measured), **N-21** (the audits), **N-08** (a
   bounded observation nobody has resolved). The rest is why I trust those four.
3. **`check_loci.py`** — drop into `corpus/`. Runs in ~30s. No dependencies beyond the stdlib.

---

## ITEM 1 — A CORRECTION TO P15, AND IT IS RECEIPT-EVIDENCED (N-17)

**P15 says "branch point" at five sites where the receipt cited at those very sentences says "seam".**

`CR_cosmology.tex` lines **220** (subsection heading), **224** (`prop:subhorizon` body), **274**, **291**,
**296**, **307** — and `C2_horizon_limits`, cited at 291, concludes in its own words:

> *"the acoustic modes are sub-horizon **at the seam**… the comoving horizon is STILL RISING **at the
> seam** and turns over just OUTSIDE it… **THE SEAM IS NOT THE TURNING POINT OF THE HORIZON. IT IS JUST
> BEFORE IT.** … r\* = 1.5338 r_seam (gauge α=1, Nariai M)"*

**And the two loci behave oppositely, which is why it matters.** At the seam the comoving horizon is near
its **maximum** — most modes inside. At the branch point aH = √|1−f| → ∞ (0.13 at comoving turnaround,
1.96 at |r|=0.1α, 19.6 at 10⁻³α; verified independently), so 1/aH → 0 and **every mode has exited**. That
is `sec:what-crosses`' own statement, and it is the `z_bp` retirement's formula exactly: **sub-horizon at
ONSET, super-horizon at the CROSSING** — with onset and seam the same locus on the expanding side.

**THE FIX IS A WORD SUBSTITUTION.** "branch point" → "seam" at those sites. **Do not touch:** the numbers
(k_hor ≈ 0.010, k_peak ≈ 0.022, factor ≳2, r\* = 1.5338 r_seam), the rate used, the label
`prop:subhorizon`, its role in closing the inflationary route to coherence, or `sec:what-crosses`.
**And there is a nearby site that is CORRECT as written and must survive any sweep:** *"the branch point is
far below their decoupling"* (of the neutrinos) — that one really is about the branch point.

**WHY IT IS WORTH THE EDIT.** It is the conflation r2289 retired — *"it INVERTED the physics"* — at sites
the hand sweep did not reach, and **it has demonstrably misled two independent nodes in one day**: I read the
Euclidean filter at the wrong locus and shipped *"nothing oscillating crosses for ℓ ≥ 3"* (the opposite of
the truth); the parallel line computed k/ℋ at the onset and reported *"prop:subhorizon inverts for ℓ ≲ 250"*,
treating an onset proposition as a crossing claim. **One word, two false alarms, both recorded as findings
about CR.** It is also a `CHECK 10` defect in form: two sections of one paper describe opposite horizon
states and a reader cannot tell which governs.

---

## ITEM 2 — `check_loci.py`, THE EIGHTH GATE, WITH ITS PRECISION MEASURED (N-19, N-20)

**What it exploits:** every computed claim in this corpus is bound to a runnable receipt, so **the receipt
is the authority on which locus was computed.** For each `\rcpt{}` call it compares the locus a sentence
**asserts a property of** against the loci its receipt names.

**Measured against a hand-labelled set of twelve:**

```
   word-presence (intersection) :  8 flags  -- MISSES the motivating case entirely
   word-presence (subset)       : 12 flags  -- 5 real / 7 false = 42% precision
   ASSERTION-SHAPE (shipped)    :  3 flags  -- 3 real / 0 false = 100% precision, 60% recall
```

**Why precision and not recall is the binding constraint** — `CHECK 9`: a false alarm in the register costs
more than the error, because the next reader inherits a debt that does not exist. A missed site stays as it
is. **So it must NOT be wired to fail a build; it is a triage lint whose output a human reads.**

**Its known gaps, so you do not rediscover them:** it misses possessive (*"the branch point's radiation
amplitude takes…"*, line 372) and compound-noun (*"built on the branch point handover"*, line 416) forms.
**I attempted those patterns, the edit did not apply, and I left it unapplied rather than claim precision I
had not re-measured.** That is the next move on the tool.

**⚠ AND ONE BUG WORTH INHERITING AS A RULE.** The first version returned empty for *everything* because
`lp.strip('\b')` **also strips the leading 'b' of `branch[ -]point`**, giving `ranch[ -]point`. Every
pattern silently failed and the tool printed **"clean"**. *A gate that reports clean because its regexes are
broken is worse than no gate.* It now ships paired with a check on labelled sentences — **do not remove
that.**

---

## ITEM 3 — TWO AUDITS, BOTH CLEAN, AND THEY ARE THE MOST USEFUL THING HERE (N-21)

**Numeric audit of P15 — 17 of 17 receipt-bound numbers confirmed.** Every `\rcpt{}` citation whose sentence
quotes a number: ran the receipt, checked the number against its output (exact or within 1%). 16 confirmed
first pass; the one flag (*"range +0.3 to +3.8 across the octopole estimator"*) is confirmed in the **second**
receipt cited in the same sentence — `P15_verify_lowell_likelihood_v2` prints *"octopole estimator range:
low(WMAP) +0.3 high(Efst) +3.8"*. **My checker's flag was its own defect: it read receipts singly and did not
pool the several a sentence may cite.**

**`CHECK 10` sweep — clean across all 17 papers.** Two hits, both proper: P7's frontiers section, and P15's
coherence section where the open marker is **exemplary** — *"What is honestly claimed here is the effect, not
a verdict on it."* **The c54.62 sweep held.**

**Integrity layer:** 244 receipts cited across 17 papers, **0 missing, 0 syntax failures**, 18/18 in a random
sample run clean.

**⌗ Why I am putting this first among the audits.** *I spent a day producing six adverse verdicts against this
corpus, every one of them my own error.* An independent numeric audit of the very paper I had been fighting
returns **17/17** against its own receipts. **`PROTECTED_OPEN` asserts that base rate; this measured it.**

---

## ITEM 4 — TWO RETRACTIONS OF MY OWN, ALREADY IN 54's BUNDLE AND WRONG

**`FOLD_FROM_52.md` is in `cr_r2381+c54.108+ACOUSTIC/`. Two of its sections are wrong.**

- **§1 — WRONG, STRIKE IT.** I evaluated the Euclidean filter's freezing criterion at the **onset** and
  concluded *"nothing oscillating crosses the branch point for ℓ ≥ 3."* **The lift acts where the modes are
  SUPER-horizon (frozen), so amplitude and tilt cross UNALTERED for every mode**; what is annihilated is the
  leg's acoustic **phase** (e^{−152} at P1). P15 `sec:what-crosses` states this outright: *"the crossing
  transmits what is frozen and destroys what oscillates."* **My §1 argued against the handoff's mechanism
  while claiming to strengthen it.**
- **§5 — ALSO WRONG, AND IN MY OWN DISFAVOUR.** I warned that my r2337 colour closure was a scope error. **It
  was not.** It is the same dimension count P16 runs — su(3)'s smallest faithful real rep is 6-dimensional,
  so su(3) ⊂ so(6) but ⊄ so(5) — applied to the **isotropy** rather than the full isometry, on two bundles
  the corpus had not enumerated. **Correct and additive.** What I actually lacked was P16's positive half:
  the wall is not the end, because the opening is the **discrete** structure and the compact face across the
  seam.

---

## ITEM 5 — ONE BOUNDED OBSERVATION, FILED AS MATERIAL, NOT A VERDICT (N-08)

Two numbers that should agree and differ by 14%:

```
   canon: z_eq = (1+z_onset)/2 − 1 = 3426  =>  the leaf's implied Omega_r/Omega_m = 1/3427
          => Omega_r = 0.3066/3427 = 8.947e-5
   instrument: Or_content = 4.1833e-5/h^2 = 7.850e-5   (T_CMB, h = 0.73)
          ratio 1.140
```

And relatedly: **z_onset ≈ 6761–6850 is where ρ_r/ρ_m = 2 on ΛCDM's parameters (1+z = 6841), not on CR's
(1+z = 7811).** Whether that is correct — the datum being *inherited*, read off the observed radiation
rather than recomputed in CR's h — is a reading I am not equipped to make.

**NOT claimed:** that the corpus is inconsistent, that r_s belongs on either rate, or that ℓ_A is at risk.
**The banked Hubble/acoustic result is guarded canon and I did not reopen it.** **First move:** find the
receipts behind z_eq = 3426 and ℓ_A = 301 and read which Ω_r each uses.

---

## WHAT I WOULD DO FIRST, IF IT HELPS

**Item 1**, because it is small, evidenced, and it is actively costing other nodes. Then **item 4**, because
a wrong document of mine is sitting in a bundle another line is reading. Then **item 5's first move**, which
is two receipt reads. **Item 2 is infrastructure and can wait; item 3 needs nothing.**
