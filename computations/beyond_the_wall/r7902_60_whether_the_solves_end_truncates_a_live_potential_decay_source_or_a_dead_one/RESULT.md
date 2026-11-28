# r7902 — the cut is clean: the potential-decay source is four orders down and falling where the solve ends

This seat's own item continuing `r7900` — **not** an order. `r7900` established that the instrument's
source is integrated only to `z = 53.545` and listed as **not measured** where in conformal time the
potential-decay term's weight actually sits. That gap decided which of two things the cut is, and
`r7900` could not tell them apart.

## THE REGISTERED CONTROL

The instrument's comments say an unset diagnostic changes nothing. The claim this revision needed is
the other one — that a **set** diagnostic changes nothing *reported* — so it was tested rather than
taken on the comment's word. This run's spectrum against `r7900`'s banked `lcdm_S000`:

| | |
|---|---|
| multipole grids identical | **yes** |
| spectra identical | **yes** |
| max absolute difference | **`0.000e+00`** |

Bit-identical. So the profile below describes the same run `r7900` measured, and not a neighbour of it.

## WHAT WAS MEASURED

| | conformal time | the ISW source's weight |
|---|---|---|
| the window the solve integrates | `53.9491` → `1893.1203` (`560` nodes) | — |
| last scattering | `280.7452` | — |
| **the peak** | **`309.90466`** | `1.173123e-06` |
| **where the solve ends** | **`1893.1203`** | `4.337934e-11`, which is **`3.697764e-05` of the peak** |

and on the way down it falls below half its peak at `eta 362.82`, below a tenth at `450.30`, and below
a hundredth at `637.13` — about a third of the way through a window that runs to `1893`.

The slope fitted over the last tenth of the window, `eta 1344.9` to `1893.1`, is **`−3.6838e-13`**:
falling, not merely small.

### ⇒ `Ⓨ⓵`: THE CUT IS CLEAN, AND THE REGISTERED EXPECTATION IS MET

The weight at the cut is four orders of magnitude below its peak against a bar of `0.01` fixed before
the run, and the slope there is negative. **Both ways the cut could have been unclean are excluded** —
a live level, and a level still growing — rather than only the first.

⇒ *So `r7900`'s account stands as written: the instrument has no late ISW because the epoch that
generates one lies outside its support, and the solve is **not** truncating a contribution that was
still being made. The cut is a boundary of the instrument and not a defect in it.*

The peak sitting just **after** last scattering — `309.90466` against `280.7452` — is what an early-ISW term
looks like, and it is the first thing that would have to be false for this profile to be describing
something other than what it claims.

## ⛭ AND A NOTE ON THE GROUNDS, BECAUSE THEY ARE THE SAME GROUNDS THAT FAILED AT `r7900`

The registration said plainly that this prediction rested on the **same** reasoning as `r7900`'s
refuted one — the physics of a decaying potential — and that if it failed again the lesson would be
about the grounds. It did not fail. The grounds were sound both times; what differed is the question
they were applied to:

| | the question | the grounds bear on it? |
|---|---|---|
| `r7900` | will the band's with/without difference be **small**? | **no** — that is set by the early ISW's size in this band, which the decay argument says nothing about |
| `r7902` | does the source's own weight **die** in matter domination? | **yes** — that is exactly what the decay argument is about |

⇒ *So `r7900`'s failure was not a bad premise but a premise applied to a quantity it does not govern.
That is worth recording as sharply as the measurement, because the two are easy to confuse after the
fact and the registration is what makes the distinction checkable rather than a story told afterwards.*

## WHAT IS NOT CLAIMED

- **Not** that this is the eta-profile of what reaches multipoles `100`–`207`. The quantity measured is
  the source's own power at each conformal time; the projection weights each `eta` through the Bessel
  kernel at `x0 = eta_0 − eta`, and that weighting is not flat. One label — "where the ISW comes from"
  — covers two different objects here, and only one of them is measured.
- **Not** that extending the solve would change nothing. It would add the Λ-driven decay this window
  cannot reach; what this revision establishes is only that nothing is being cut off mid-stream at the
  current boundary. The extension stays routed to `69` with `r7900`'s recommendation.
- **Not** a statement about any sum but Σ = `0`. One run answers the truncation question; whether the
  profile's shape moves with the sum is a further question and is not opened here.
- **Not** a limit. `r7888`'s `193.545` meV is untouched.
