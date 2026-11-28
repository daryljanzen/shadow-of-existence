#!/bin/bash
# r7902+60: ** ONE RUN OF THE CONTROL ARM AT Σ = 0 WITH `SRCETA` ON, so the source's own weight can
# be read as a function of conformal time instead of only at the visibility peak. **
#
# ⌗ NOT RETYPED: every environment value is `r7900`'s `gen_isw.sh` ISW-ON arm at `S000`, with ONE
#   addition -- `SRCETA` -- and nothing removed. `SRCDEC` stays on so this run's spectrum and pairs
#   are directly comparable with the banked ones, which is the registered control: the reported
#   spectrum must come out BIT-IDENTICAL to `r7900`'s `lcdm_S000`, or the diagnostic is not inert and
#   the profile describes a different run.
# ⌗ IDEMPOTENT: a completed point is skipped.
set -u
OUT=${OUT:-"$(cd "$(dirname "$0")" && pwd)/etaprof"}
mkdir -p "$OUT"
cd "$(dirname "$0")/.."
LC_H0=67.40; LC_OM=0.3150; LC_WB=0.0224; LC_NS=0.965
f="$OUT/lcdm_S000_eta.npz"
if [ -s "$f" ]; then echo "  [have] S000 eta profile"; exit 0; fi
env BVEL=1 NUFD=1 ARM=lcdm LH0="$LC_H0" LOM="$LC_OM" WBH2="$LC_WB" NS="$LC_NS" MNU=0.00 \
    HIER=1 LMAXL=2000 LSTEP=8 NOISW=0 \
    SAVE="$OUT/lcdm_S000_tt.npz" POLSAVE="$OUT/lcdm_S000_pol.npz" \
    SRCDEC="$OUT/lcdm_S000.npz" SRCETA="$f" \
    python3 ACOUSTIC_two_arm.py > "$OUT/lcdm_S000.log" 2>&1
echo "  lcdm S000 eta rc=$?" >> "$OUT/done.txt"
echo "  [done] S000 eta profile"
