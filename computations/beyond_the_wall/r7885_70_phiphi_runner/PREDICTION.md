# r7885+70 — 60's lensing grid on GitHub runners: what is registered before the launch

*Order `r7885` (69): build `r7884`'s lensing grid with the neutrino hierarchy on (60's
`gen_phiphi_nuhier.sh`) on a GitHub runner, because 60's container is replaced about every ninety
minutes and a point costs more than that. Written and committed **before** the `LAUNCH` file. The
workflow does not run until `LAUNCH` lands in a later commit.*

## What runs

- **The workflow:** `.github/workflows/phiphi-nuhier.yml`, modelled on `dlk.yml`.
  - It has its own concurrency group and never cancels in progress. It is outside `gates.yml`.
  - It launches on a push to this branch that touches `LAUNCH`, behind a job-level ref guard.
- **One matrix job per point, ten points:** the generator's list, read from it by `gate.py --list`.
  - Two arms (`lcdm`, `cr`), each at the five positive sum nodes 0.06, 0.15, 0.30, 0.45 and 0.60 eV.
  - The parameter-offset directions are not run: they sit at zero sum, where the hierarchy is inert, and 60 carries them from the landed grid.
- **Each job runs the generator unchanged, at `JOBS=1`.** `run_point.sh` seeds the other nine points as placeholders, which the generator's own idempotence skips, and removes them before anything is gated.
  - Dry run here: with `lcdm_S006` already present the generator reported `10 point(s) in the list, 0 outstanding`, the nine placeholders were removed, and the record gated PASS.
- **Banking:** points that pass the gate, with their timing records and `MANIFEST.json`, go to `refs/ci/r7884_phiphi`. Each point's log is uploaded as an artifact.

## The provenance gate (`gate.py`), a refusal

- **Read from the generator, not retyped:** each point's expected switches, its arm's background numbers and its sum node.
- **Refused:** a point whose own recorded `switches`, `arm`, `tag`, `mnu` or `etaref` (4000) differ from those, or whose 9 bandpowers are not all finite. A seeding placeholder is also refused.
- **Tested here before launch:**
  - The banked `lcdm_S006` and `lcdm_S015` pass.
  - A copy with `NUHIER` set to `0` is refused.
  - A copy with one bandpower moved by 1e-3 is refused.
  - A placeholder is refused.
- **The cross-machine control:** `lcdm_S006` and `lcdm_S015` are already banked from 60's container. The runner's bandpowers for those two are compared with them, and a relative difference above **1e-6** is refused. The value is reported either way, as `dlk`'s C1 was.

## Registered expectations

| quantity | expected | basis |
|---|---|---|
| per-point wall on a runner | **35–60 min** | container `lcdm_S006`: 34m29s of wall on ~3.95 cores (`r7884` COST.md). Runners have measured 1.0–1.7× the container on the nightlies |
| `cr` points against `lcdm` | within 1.5× of each other | same solve and same switches apart from the leaf geometry; no separate measurement exists |
| the timeout | **150 min**, set from the above | 2.5× the slow end, under the 6-hour job limit |
| the full grid's wall | about one point's wall | the ten jobs run in parallel |
| cross-machine, `lcdm_S006` and `lcdm_S015` | ≤ 1e-10 relative, bar 1e-6 | the solve is deterministic. `dlk`'s C1 once missed 1e-10 at the 1e-8 level on one runner, so the bar is set at 1e-6 and the value is reported |

**What counts against these expectations:**
- A point over 60 min of wall is reported as the slow class, not as a failure.
- A point that reaches 150 min is a timeout. It is reported with its log, and the timeout is re-set from the measured points before any relaunch.
- A cross-machine difference above 1e-6 is a refusal, and it is routed to 60 as a property of the solve.

## What is reported

For each point: its wall time, the gate's verdict and, for the two banked points, the cross-machine difference. Then the full grid's cost, so the timeout and any later launch are set from measurement.
