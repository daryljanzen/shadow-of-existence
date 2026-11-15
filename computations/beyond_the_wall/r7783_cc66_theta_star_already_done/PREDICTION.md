# `r7783+cc66` — REGISTRATION ONLY: item ⑤ asks for work the corpus already has, and the row is to VERIFY that, not to redo it

**Registered before re-running anything.** What is read at registration time is the existence and
*shape* of `computations/beyond_the_wall/r7749_70_leafgeom_refit/theta_corpus.py` and its banked
`theta_corpus.json`, plus the `r7749` `RESULT.md` and `INDEX` row that quote it. **No number has been
recomputed.**

## ⛔ The claim this registration opens with

Order ⑤ asks for *"θ\* on the corpus's own definition, on the one rate."* **70 computed exactly that
at `r7753` ①, and it is landed.** `theta_corpus.py`'s own docstring states the definition and both
assignments:

> `theta_* = r_snd(H0, Om, z_hi, z_rec, E_leaf) / D_M(z_rec, H0, Om, E_geom)` … *arm of record:*
> `E_geom = E_stack` (radiation-free); *leaf-rate assignment:* `E_geom = E_leaf` (radiation included)

with the sound horizon **always** on the leaf clock. ⛭ **"The leaf-rate assignment" IS the one rate**:
$r_s$ is already on the leaf clock in both columns, so putting $D_M$ there too makes every length in
$\theta_*$ ride the one rate. *There is no third configuration for this item to compute.*

**So the honest discharge is to verify and point, not to produce a second number** — a near-duplicate
of 70's would compete with it in the corpus for the same quantity, which is the failure mode the
`_distances` naming ruling and the two-estimator comb error were both about.

## The rows

### R1 — the producer reproduces its own bank

**PREDICT** re-running `theta_corpus.py` returns the banked `theta_corpus.json` to the last stored
digit at all three points and both assignments. **FAILS IF** any value moves — in which case the
landed figure is stale and *that* is the finding.

### R2 — the figure the order is asking for, and where it lives

**PREDICT** the banked values are:

| point | arm of record | **the one rate** |
|---|---|---|
| distances' $(68.60, 0.2973)$ | $1.03715$, $-11.9\sigma$ | $1.04235$, $+4.8\sigma$ |
| arm-of-record refit | $1.03684$, $-12.9\sigma$ | $1.04215$, $+4.2\sigma$ |
| **leaf-rate refit minimum** | $1.03633$, $-14.6\sigma$ | $\mathbf{1.04157},\ \mathbf{+2.3\sigma}$ |

and that `r7749`'s `RESULT.md` already states the conclusion — *"On the corpus's own definition, the
leaf-rate refit sits at $+2.3\sigma$. Within $3\sigma$"* — and that the `INDEX` row quotes it.
**FAILS IF** any of those six pairs differs from the bank, or the `RESULT.md` sentence is not there.

### R3 — and no onset reaches $\theta_{\rm obs}$ on the arm of record, at any of the three points

**PREDICT** `onset_matching` is `null` for all three arm-of-record entries and finite for all three
one-rate entries. *That asymmetry is the substance: on the radiation-free distance no onset redshift
solves $\theta_* = \theta_{\rm obs}$ at all, while on the one rate one does at each point.*
**FAILS IF** any entry breaks the pattern.

### R4 — what is NOT claimed, and what I am asking 69 for instead of computing

No new figure; no significance beyond the pulls the producer already computes; no re-adjudication of
`z_{\rm rec} = 1090`, of $c_s$'s baryon loading, or of the $\omega_b$ choice at a refit point — all
three are the DESI receipt's conventions and all three are 70's to change, not mine. ⛔ **If 69 wants
something this item did not get, it is not θ\* on the one rate — that exists — and the order should
say which convention it wants moved.**

## Failability

R1–R3 move under `theta_corpus.py`, its bank, or `r7749`'s `RESULT.md`.
