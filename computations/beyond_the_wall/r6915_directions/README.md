# `r6915+cc66.41` — each source term projected through its own kernel

*`r6915`'s order: **which term carries the contrast excess after projection?** `cc66.40` located the
stage — the excess is made between $k$ and $\ell$ — and this asks what inside the projection does it,
with the monopole–Doppler pair named as the first place to look because $j_\ell$ and $j_\ell'$ are a
quarter period out of phase.*

| script | what it runs | why |
|---|---|---|
| `launch.sh` | **the no-op pair** (both arms at the screen grid with `SRCDEC` unset), then **the ten term pairs** on both arms at `LSTEP=8 LMAXL=2000` in `KSLICE` pieces of $250$ | the projected pieces are a different object from `SRCSAVE`'s: that banks the source *before* the kernel, and this banks what the kernel does to each term. ⌗ Same `LSTEP` and `LMAXL` as `r6911`, so the two receipts read **one** configuration — gated |
| `bank.py` | folds the slices into `spectra/r6915_pairs_{lcdm,cr}.npz` and the no-op pair into `spectra/r6915_noop.npz` | gates that the slice starts **tile the $k$ axis with no gap and no overlap**, that every slice reports the same multipoles, and that the pair **order** is identical slice to slice — a permuted column set would otherwise read as a plausible answer |

## ⛔ The order's closure gate needed correcting before it could be passed

*The order says: "the projection is linear in the source, so the separately projected pieces must sum
to the full spectrum. Gate that first… and read nothing below it if it fails."*

⚠ **The transfer is linear in the source and the pieces do add there. $C_\ell$ is quadratic in the
transfer, so the projected spectra cannot add** — they are short by exactly the cross terms, which is
the object the order's *first* outcome is about. *The four diagonal pieces alone fall short of $D_\ell$
by up to 46 per cent.*

⇒ **So `SRCDEC` banks the full bilinear decomposition.** With $\Delta^a_\ell(k)=\int \text{term}_a\,
j_\ell\,\mathrm d\eta$, one transfer per source term,
$$C_\ell = \sum_{a\le b} w_{ab} \sum_k P\,\Delta^a\Delta^b,\qquad w=1 \text{ on the diagonal},\ 2 \text{ off it}$$
— ten numbers per multipole that close on $D_\ell$ to $1.1\times10^{-15}$ and $1.3\times10^{-15}$
relative on the two arms. **That is the gate the order asked for, in the form that can hold.**

⌗ **The Bessel evaluation is shared with the reported spectrum**, so this costs four trapezoids per
multipole and not a second projection: $j_\ell$ is the whole cost and it is computed once. *`SRCDEC`
is loaded only inside guarded blocks and is bit-identical when unset on both arms, gated as
`SRCSAVE` and `SRCXS` were.*

⚑ **Sliced on `KBATCH` boundaries** — exact to $10^{-16}$ on both arms (`r6895+cc66.38`), here
re-gated on eleven columns instead of one. Idempotent and resumable: a finished slice is skipped on
the marker in its own log.
