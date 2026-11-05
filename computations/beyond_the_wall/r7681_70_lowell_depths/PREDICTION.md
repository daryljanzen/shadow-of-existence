# r7681+70 — PREDICTION

**Measured before this file, and said so rather than registered.** Every number this order asks for was already
measured at r7675 (`r7675_70_split_clock/result.json`):
- arm A (CAMB, exact transfer) at the refit licensed point: 0.4920 / 0.4434 / 0.3601 / 0.6627 / 0.9097 / 0.9827 / 0.9980;
- arm B split-clock FROZEN: 0.4697 / 0.4649 / 0.3424 / 0.6321 / 0.8985 / 0.9805 / 1.0003;
- arm B split-clock DECOUPLED: 0.4826 / 0.4680 / 0.3604 / 0.6469 / 0.9046 / 0.9808 / 0.9982.

This order re-runs all three from one script on the current tree and banks them as one source. The only claims open
before the run:

- **R1.** The re-run reproduces those values bitwise at their printed precision. The tree has changed since r7675 only by `SPLITIC`, which is byte-identical unset under `SPLITCLOCK=1` (r7677 G1).
- **R2.** Arm A at the adjudicated point reproduces P15's printed seven (l.2809–2810: 0.487, 0.435, 0.359, 0.666, 0.911, 0.983, 0.998) to their printed precision. That is the recipe check.
- **R3.** Recovery is defined as the first ℓ ≥ 5 with depth ≥ 0.99, as at r7675. Every row recovers at ℓ = 8.
