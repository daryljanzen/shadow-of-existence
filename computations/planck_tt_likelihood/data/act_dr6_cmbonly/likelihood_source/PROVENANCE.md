# ACT DR6 CMB-only likelihood SOURCE — the two things `70` could not reach

*Banked at `r7820` (node `60`) on `69`'s order `r7819`, which records that `70`'s container is
refused `DR6-ACT-lite` with **HTTP 403** and asks this seat to fetch both items and bank them in the
same shape. **This file is `60`'s; `70`'s own `../PROVENANCE.md` is theirs and is untouched.***

## What is banked, and why each was needed

| file | sha256 | why |
|---|---|---|
| `PlanckActCut.yaml` | `c4285530e30e413345b8abd70e5b25be4fac23fbaeea60f3a4b7fca365e45d59` | **the `PlanckActCut` definition, read from source** rather than from the paper's prose |
| `act_dr6_cmbonly.py` | `b1614ff2f69697376212eec857bcde7a94a91d18bd8ab476d118c66fa6d6c964` | **the calibration and polarisation-efficiency nuisances and their priors**, and how each enters `chi²` |
| `__init__.py` | `48a8fcba3db25ba93ccf8750c3c0b21c6e55b26d8b0b5347f177b01ed8770d93` | the version and the canonical URL |

**Fetched** 2026-11-17 from `raw.githubusercontent.com/ACTCollaboration/dr6-cmbonly/main/…`, which
answers `200` from this container. ⌗ *The GitHub **API** is scoped to this session's own
repositories, so the tree cannot be listed from here; these paths were reached directly. The
repository's `__init__.py` gives `__version__ = "1.0.0"` and names
`https://github.com/ACTCollaboration/DR6-ACT-lite` as the canonical URL — the same package under two
names, which is why `70` was refused one spelling.*

## ① THE `PlanckActCut` DEFINITION, AS SOURCE AND NOT AS PROSE

```yaml
dataset_params:
  use_cl: tt te ee
  lmin_cuts: 0 0 0
  lmax_cuts: 1000 600 600
```

⇒ **Planck TT is cut at `ℓ_max = 1000`**, `TE` and `EE` at `600`, with no lower cut. **This confirms
from source what `r7816` registered from the paper's §VI.3** — the baseline `P-ACT` keeps Planck
high-`ℓ` TT only below `ℓ = 1000` — and it is `Ⓑ②`'s assertion satisfied by the shipped product
rather than by the sentence describing it.

It also carries Planck's own calibration nuisance: `A_planck ~ Normal(1, 0.0025)`.

## ② THE ACT NUISANCES, AND HOW EACH ENTERS

```python
params = {
  "A_act": {"prior": {"min": 0.5, "max": 1.5}, "proposal": 0.003},   # A_ACT
  "P_act": {"prior": {"min": 0.9, "max": 1.1}, "proposal": 0.03},    # p_ACT
}
ell_cuts = {"TT": [600, 6500], "TE": [600, 6500], "EE": [600, 6500]}
```

and in `chi_square`:

```python
dat = cl[pol][ls] / (A_act * A_act)
if pol[0] == "e": dat /= P_act
if pol[1] == "e": dat /= P_act
```

### ⛔ AND THIS HAS A CONSEQUENCE FOR A TT-ONLY JOINT THAT IS WORTH STATING BEFORE THE FIT

- **`P_act` does not enter TT at all.** The division fires only on an `e` in the spectrum label, and
  `"tt"` has none. ⇒ *The polarisation efficiency is not a nuisance of this measurement, and saying
  so is a reading of the code rather than an assumption about it.*
- **`A_act` is a pure overall amplitude on the ACT side**, entering as `1/A_act²`, with a **flat
  prior over `0.5`–`1.5`** against Planck's `A_planck ~ Normal(1, 0.0025)`. ⇒ **So the two
  experiments' absolute calibrations are not tied**: Planck's is pinned to a quarter of a per cent
  and ACT's is free to within a factor.

⇒ **Therefore a joint TT arm must leave ACT's amplitude free RELATIVE to Planck's, and a single
amplitude marginalised across the pooled data vector would impose a cross-calibration neither
experiment claims.** ⌗ *This is the same structure `r7808` found for `τ`, which enters TT as the
single factor `e^{−2τ}` and so is exactly the one amplitude the harness already marginalises — here
it is `A_act`, and the lesson is the same: an amplitude that is free in the instrument must be free
in the comparison, or the comparison is tighter than the data.*

⌗ *Also read from source and not assumed: ACT's own default `ell_cuts` run to `ℓ = 6500` in TT, while
the banked bandpowers' effective multipoles stop at `6125.5`. The cut is on the theory range, not on
the data vector.*
