# `r7857+cc66` — REGISTERED BEFORE ANY COMPUTATION

Order `r7857` (69), items ① and ②. Written and pushed in its own commit **before a line of the
computation exists**. Item ③ waits on 60 wiring the polarisation blocks.

---

## ⚠ ① I HAVE ALREADY FOUND A CONFIGURATION DIFFERENCE, AND IT POINTS AT MY OWN SETUP

The order asks me to compare on the same configuration and, if the spreads still differ, to find
which is right. **Reading both sides' recorded settings before computing anything, they do NOT
match, and the mismatch is on the CAMB side rather than the instrument side.**

| | 60 (`r7856` `cmb_side.py`) | me (`r7855`) |
|---|---|---|
| CAMB `lmax` | **`2600`** | `set_for_lmax(2196)` — the bank's top `ell` plus 200 |
| spectrum | **`total`** | `lensed_scalar` |
| reported centre | **geometric** mean `0.5046723825` | arithmetic mean `0.503313` |
| `A_s`, `n_s` | `2.1e-9`, `0.965` | identical |

**My per-bin spread is dominated by the top of my own range** — within one to two per cent through
the middle and about `-6` per cent near `ell = 1920`, against a ceiling at `2196`. CAMB's lensed
spectrum degrades as it approaches the `lmax` it was computed to, and lensing in particular draws on
multipoles well above the one being evaluated. 60's `2600` clears the bank's top (`1996`)
comfortably; mine clears it by `200`.

**Ⓐ THE SPREAD DISAGREEMENT IS MINE, NOT A REAL DIFFERENCE BETWEEN THE INSTRUMENTS.** Re-running my
comparison at `lmax = 2600` on `total` brings the per-bin spread **below `0.02`**, from `0.056634`.
  ⇒ REFUTED if it stays above `0.02`, in which case the oscillation is real, my `r7855` reading
  stands, and I owe its size at the first three peaks as the order asks.

**Ⓑ AND THE `lmax` TRUNCATION IS THE DOMINANT CAUSE, NOT THE SPECTRUM CHOICE.** Changing `lmax`
alone, still on `lensed_scalar`, recovers **most** of the collapse — more than half the excess
spread. ⇒ REFUTED if `total`-versus-`lensed_scalar` turns out to carry more of it than `lmax` does.

**Ⓒ SO I EXPECT TO WITHDRAW MY OWN `r7855` HEADLINE, AND I AM REGISTERING THAT IN ADVANCE RATHER
THAN DISCOVERING IT.** That revision said the factor "is five times less flat than reported" and
that `"a flat factor of two" describes this bank to about five per cent`. If Ⓐ holds, **that claim
was an artefact of my own truncated `lmax`**, 60's range was right, and the retraction is owed
plainly — including in the corpus, not only here.
  ⌗ The *factor* itself (`0.5033`, and EE at `0.4972`) does not depend on the spread and is not
  expected to move more than `0.01`, because a high-`ell` tail error changes the extremes far more
  than the centre. ⇒ Ⓓ: the re-run centre stays within `0.01` of `0.5033`.

**Ⓔ AND THE CENTRES ARE NOT THE SAME STATISTIC EITHER.** 60 report a GEOMETRIC mean; I reported an
arithmetic one. On a ratio scattered by several per cent these differ in the third decimal, so the
like-for-like comparison needs both. ⇒ I will report mine both ways, and the geometric mean is
expected within `0.002` of `0.504672` once the configuration matches.

---

## ② THE SIX ABSOLUTE STATEMENTS — READ, NOT PATCHED

60's sweep named six of my receipts carrying absolute statements. The order is explicit: **read each
and say which state an absolute CMB amplitude, or a chi^2 with the amplitude HELD, that `FOURPI`
would move; list what would move and by how much; do NOT patch until their defaults are on.**

**Ⓕ MOST OF THE SIX ARE SAFE, AND THE SPLIT IS THE POINT.** A statement about a RATIO, a CONTRAST,
a PERIOD or a PHASE is invariant under a constant rescaling of the spectrum; only a statement about
an absolute amplitude, or a chi^2 computed with the amplitude held rather than fitted, moves.
I register that **at most three of the six** move under `FOURPI`.
  ⇒ REFUTED if four or more move, which would mean this seat has been writing absolute statements
  where it believed it was writing relative ones.
  ⌗ The no-fit confrontation at three per bin is the one I most expect to move, because "no fit"
  is precisely the condition under which an amplitude error cannot be absorbed.

**⚠ WHAT I WILL NOT DO:** patch them. The order says not to, and a receipt patched before the
defaults change would assert a number the tree does not yet produce.

---

## ⚠ WHAT THIS CANNOT SETTLE

Item ① can say whose configuration produced the spread, and it can say whether the oscillation
survives a matched configuration. It CANNOT say that the instrument and CAMB agree in detail at
high `ell` — a matched `lmax` removes an artefact of mine, it does not validate either side's
damping tail. And nothing here tests 60's located `4pi` and `1/2pi` factors themselves; that is
their finding, and my EE result is already cited as evidence for the polarisation half.
