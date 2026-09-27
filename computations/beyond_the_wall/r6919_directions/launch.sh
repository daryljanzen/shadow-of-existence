#!/bin/bash
# ** r6919's order: PROJECT A SOURCE WITH NO PHYSICS IN IT, then swap the geometric factors. **
#
#   ⓵ Feed both arms' projection machinery the same analytic oscillating source and measure how much
#     of its oscillation each arm's projection retains, as a function of q.  If the arm-to-control
#     ratio reproduces cc66.41's 1.054 and its +0.0139 slope, the effect is the projection's geometry
#     and the source is irrelevant to it.
#   ⓶ Then swap the geometric factors one at a time.
#
# ⛔ ** AND THE ORDER'S NAMED CANDIDATE IS IN THE INSTRUMENT, BUT NOT WHERE THE ORDER PUTS IT. **
#   The order proposes that the kernel's argument chi(eta) is a distance read on the other clock.
#   It is not: `x0 = eta_0 - EE` on both arms, so chi(eta) = eta_0 - eta and d chi / d eta == 1 on
#   each -- there is nothing there to exchange.
#     ⇒ ** The two clocks sit between r_s and eta. **  The acoustic phase accumulates in LEAF
#       conformal time and x0 is in STACKING conformal time; on the control Hleaf and Hphys are
#       character-identical so Jac = d eta_leaf / d eta_stack is 1.000000 everywhere, and on the arm
#       it runs 0.789 to 0.913 across +-3 FWHM of the visibility.  Term-independent, growing with k,
#       and vanishing for a window under one period -- the three properties cc66.41 measured.
#   ⇒ So ⓶'s swap is done in the INJECTION, where the phase accumulator is the only thing that
#     moves: same background, same visibility, same kernel, same k grid.  `SRCINJRS=stack` forces
#     both arms onto one clock; `SRCINJVIS` swaps the other factor, the visibility's width.
#
# ** The solver is SKIPPED on these runs because the analytic source replaces `S` entirely, so each
#    is seconds of setup plus the projection.  Sliced on KBATCH boundaries; idempotent, resumable. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6919; mkdir -p $D/noop $D/inj
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
W_LCDM=38.042        # each arm's own visibility FWHM, from the header
W_CR=43.591
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D

echo "--- the no-op gate: the SRCINJ edit must change nothing when it is unset ---"
printf '%s\n' \
 "$D/noop noop_lcdm  $LCDM LSTEP=16 LMAXL=500" \
 "$D/noop noop_cr    $CR   LSTEP=16 LMAXL=500" \
 | xargs -P 2 -I{} bash -c 'run {}'

echo "--- the injected source: eight configurations, both arms, the REPORTED grids ---"
LIST=""
add () { tag=$1; arm=$2; env=$3; nk=$4; shift 4
  i=0
  while [ $i -lt $nk ]; do
    j=$((i+250))
    LIST="$LIST
$D/inj inj_${tag}_${arm}_k${i} $env LSTEP=8 LMAXL=2000 KSLICE=${i}:${j} $*"
    i=$j
  done; }
# ⓵ the physical injection: each arm's own clock convention, two phases
add sweepown lcdm "$LCDM" 2547 SRCINJ=sweep SRCINJRS=own
add sweepown cr   "$CR"   1452 SRCINJ=sweep SRCINJRS=own
add sweepph  lcdm "$LCDM" 2547 SRCINJ=sweep SRCINJRS=own SRCINJPH=0.5
add sweepph  cr   "$CR"   1452 SRCINJ=sweep SRCINJRS=own SRCINJPH=0.5
# the other phase convention: no advance across the visibility at all
add fixed    lcdm "$LCDM" 2547 SRCINJ=fixed
add fixed    cr   "$CR"   1452 SRCINJ=fixed
# ⓶a the CLOCK swap: both arms' phase accumulated on the stacking clock
add sweepstk lcdm "$LCDM" 2547 SRCINJ=sweep SRCINJRS=stack
add sweepstk cr   "$CR"   1452 SRCINJ=sweep SRCINJRS=stack
# ⓶b the VISIBILITY-WIDTH swap: each arm given the other's FWHM about its own peak
add viswap   lcdm "$LCDM" 2547 SRCINJ=sweep SRCINJRS=own SRCINJVIS=$W_CR
add viswap   cr   "$CR"   1452 SRCINJ=sweep SRCINJRS=own SRCINJVIS=$W_LCDM
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6919 LAUNCH COMPLETE $(date -u) ==="
