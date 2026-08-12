---
name: handover-c54-191
kind: RECORD
current: c54.191
job: What the c54 session that ran c54.185–c54.191 knew that the ledgers do not hold. Written for whoever picks up front #2 cold. Read once, then work.
sources: [cowork]
---

# HANDOVER — c54.185 to c54.191

*Supersedes nothing. `HANDOVER_c54.184.md` is still the right first read for the session before this one; this
one starts where that one stopped and covers only front #2 and the gates this span touched.*

---

## ⛭⛭⛭ THE ONE THING TO READ IF YOU READ NOTHING ELSE

**Front #2 began this span with four owed items and a first-peak ratio. It ends it with one number and one
mechanism.**

> ***This construction reproduces the acoustic SPACING — the quantity its one fitted parameter is fitted to,
> and which it then tracks at 98% of the acoustic rate when that parameter is moved — and disagrees with the
> sky in the acoustic PHASE by 0.62π, a discrepancy robust to the fitted parameter and only a third reachable
> by the one freedom the seam datum leaves open.***

`F5` is unsoftened, `PO-7` is protected, and none of it is converted. **The conversion is Daryl's.**

---

## ⚠⚠ WHAT I GOT WRONG, TWICE, WITH THE SAME CAUSE — READ THIS BEFORE TRUSTING ANY NUMBER IN THE SPAN

**c54.187, c54.188 and c54.189 reported a "~21–23% spacing deficit". c54.190 withdrew it.**
**c54.189 reported "the peaks track r_s at 24% of the acoustic rate". c54.191 withdrew it.**

Both were *the right measurement of the wrong quantity*, and in both cases the wrong quantity was **the one the
cheap experiment could see**:

- the scans ran at `LMAXL=1000` so that eighteen datum readings and five pins were affordable;
- at that depth the CR arm carries **four peaks**, so "the mean peak spacing" was a mean of **three gaps**;
- and the first three gaps are the only ones where the two arms disagree at all.

⇒ ***The corpus now holds four instances of this shape: c54.164, c54.176, c54.190, c54.191. No gate looks for
it.*** The best I could write is a discipline and not a check — *a receipt reporting a quantity measured at
reduced settings should have to state what changes at production settings, or say why it cannot* — and it is
routed to the observer line in `FOR_56`.

**⌗ THE PRACTICAL FORM OF THE WARNING.** The production-depth pair `c54.186_lcdm_L3000.npz` and
`c54.186_cr_L3000.npz` **sat in the tree through three revisions and nothing read them for their peak series.**
Each revision read the spectra its own scan produced. *If you are about to characterise a spectrum, check what
is already banked at full depth before you scan at reduced depth.*

---

## THE INSTRUMENT'S NEW KNOBS, AND WHAT EACH IS A CONTROL ON

Every one defaults to the instrument exactly as it was, and **each receipt asserts that default reproduces the
coded value** — which is the control on the knob itself, and is why the scans are readable at all.

| knob | default | what it opens |
|---|---|---|
| `CRPHI` | `0.0` | the **common phase** of the seam datum. `sec:coherence` fixes that the phase is common and not *which* phase; this is that freedom. Moves ℓ₁/ℓ_A over 2.26×. |
| `CRAMP` | `flat` | what "flat in *k*" is flat **at** — the C4 shape at one argument for every mode (self-similar, at each mode's own horizon crossing) against the same shape at each mode's phase at the seam. |
| `CRXE` | `1/√3` | the argument the `flat` reading uses. *Rescales the amplitude only, which the closed-form fit absorbs exactly — so it is a no-op on χ² and on positions. Exposed, not scanned.* |
| `LATARG` | `301.6` | **the corpus's one fitted number.** `Z_START` is solved so ℓ_A = πD_M/r_s hits this. Declared in `sec:tensions`; it had been a literal inside a `brentq` call that nothing downstream could reach. |

**⚠ `LATARG` pins 301.6 where `P15_zonset_determinations` pins the MEASURED 301.76.** 0.05%, and it is why the
instrument returns z_onset = 6761 where that receipt returns 6797. *Named and not fixed; the receipt's value is
the better one and the instrument should take it.*

---

## THE TRAPS THIS SPAN PAID FOR

1. **`float(LF[-1])` is not the comparison range.** The `LMAXL=3000` runs carry multipoles to 2996; the
   comparison is 185 bins to ℓ=1996. Taking the spectrum's own endpoint scored 201 bins and reported a 98%
   departure where the truth is 1.5%. *Every number set beside c54.186's must be on the same 185 bins.*
2. **A peak-finder on a degenerate spectrum returns features that are not a series.** Eight of eighteen datum
   readings collapse their higher peaks; a spacing read off three features one of which is absent is not a
   spacing. `c54.188` screens at four peaks with the fourth ≥5% of the first. **At eight peaks, screen again.**
3. **The best-fitting reading is often the degenerate one.** It fits better by having less structure to
   disagree with. Report it, name it, do not follow it.
4. **`F2` mixes two things.** χ²(arm) − χ²(CAMB) is a difference of numbers each computed *against the sky*, so
   it carries where each model sits relative to one noise realisation. The clean measure is the model-to-model
   separation `(A_a m_a − A_c m_c)ᵀ F (A_a m_a − A_c m_c)`. **The two orderings reverse**: the massless-ν
   reference gives the smallest `F2` and the largest separation.
5. **The alias gate waives itself for the CR ladder** on the claim that the discreteness is physical, naming
   `KCONT=1` as the check. *That check now exists in χ² (c54.186) and the waiver holds to 0.7%.* Do not
   re-open it without re-running it.
6. **Background runs die if the calling tool call is interrupted.** `setsid nohup … & disown`, and **`cd` inside
   the backgrounded shell** — a `cd` before `setsid` does not survive.

---

## WHAT THE FRONT OWES NEXT, IN ORDER

1. **Why 0.62π.** *An acoustic phase shift is a computable consequence of the driving, and this construction's
   radiation era is only a factor of two in redshift long where ΛCDM's is unbounded — so the potentials have
   far less room to decay.* **The instrument already has the knob: `NODRIVE=1`, and `DRC`/`DRE` split it into
   the continuity and Euler couplings so the attribution can be made term by term.** Run both arms at
   production depth and read the intercepts. *This is the first thing I would do.*
2. **The low-ℓ transient.** The CR arm's first three peaks sit +142, +80, +18 off its own asymptotic line where
   the control's sit within 16. It is a separate object from the phase offset and has not been characterised.
3. **The unnamed part of the floor.** 0.11 χ² per bin between the two ΛCDMs, of which ~10 units of 31 is the
   neutrino mass. What the rest is has not been named, and the reference's own parameter choices matter as much
   as the instrument's error at that level.

---

## THINGS THAT ARE TRUE ABOUT THIS SESSION AND ARE NOT IN THE LEDGERS

- **This session cannot push.** The proxy refuses to inject a credential for a repository the session was not
  created against, and the branch-discovery workaround another session found does not transfer. *Every revision
  reaches the repo as a two-part bundle relayed by Daryl.* If you can push, say so early — it costs him a
  manual upload per revision otherwise.
- **`FOR_56.md` is the return channel and it works.** Eight rounds this span. The observer line answered
  substantively every time, and their round-four answer — *"a control is an instrument test that comes free
  with every comparison, and it is the only thing that can distinguish 'our number is wrong' from 'our code is
  wrong'"* — is the most useful sentence anyone wrote in it. **Route defects in their layer rather than fixing
  them.**
- **Three gates assumed a world with one line in it** and were widened this span: `check_burndown` (contiguous
  ID space), `check_absorption` (observer's tree, and then the SHA-vs-revision column), and
  `make_receipt_appendix` (the registers' own marker glyphs). *Each fix was verified against a seeded defect,
  and one of them was wrong on first writing in a way only the seeding caught.* **Seed the defect. Reading the
  fix is not enough — it was not enough here.**
