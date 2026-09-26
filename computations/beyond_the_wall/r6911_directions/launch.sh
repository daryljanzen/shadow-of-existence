#!/bin/bash
# ** r6911's order: WHERE IS THE ACOUSTIC CONTRAST MADE -- in the source, or in the projection? **
#
#   The order asks for ONE statistic applied at TWO points in the chain.  The ell end is banked
#   (`cc66_r185_verify_{lcdm,cr}`, the adjudicated minima, contrast ratio 1.040); the k end was
#   never saved, so `SRCSAVE` is added and run here.  It writes, on the run's own k grid:
#     * the source at last scattering, term by term -- g(Theta_0+Psi), the Doppler dipole,
#       the ISW, the polarisation pair -- and their sum, gated against `S` itself;
#     * each term's eta-integral, which is the SAME transfer with the Bessel kernel taken out;
#     * and, via `SRCXS`, the same source projected with the OTHER arm's comoving distance.
#
#   ⇒ Three stages, one statistic: source at last scattering -> source eta-integrated (no kernel)
#     -> the reported D_l.  The stage the ratio moves at is the answer.
#
# ** EVERY LONG RUN IS SLICED ON KBATCH BOUNDARIES **, exact to 1e-16 on both arms (r6895+cc66.38),
# so a container restart costs one slice and not a run.  ** IDEMPOTENT AND RESUMABLE. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6911; mkdir -p $D/noop $D/src
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
# the swap ratios are each arm's OWN D_M divided into the other's, from the banked minima:
#   control 13954.353506 Mpc, arm 14017.038576 Mpc -- 0.449% apart, the ARM'S LARGER.
XS_LCDM=1.004492152      # the control's source through the arm's distance
XS_CR=0.995527938        # the arm's source through the control's distance
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D

echo "--- the no-op gate: the SRCSAVE edit must change nothing when it is unset ---"
printf '%s\n' \
 "$D/noop noop_lcdm  $LCDM LSTEP=16 LMAXL=500" \
 "$D/noop noop_cr    $CR   LSTEP=16 LMAXL=500" \
 | xargs -P 2 -I{} bash -c 'run {}'

echo "--- and the SRCXS guard: set WITHOUT SRCSAVE it must also change nothing ---"
printf '%s\n' \
 "$D/noop xsonly_lcdm  $LCDM LSTEP=16 LMAXL=500 SRCXS=1.5" \
 "$D/noop xsonly_cr    $CR   LSTEP=16 LMAXL=500 SRCXS=1.5" \
 | xargs -P 2 -I{} bash -c 'run {}'

echo "--- the source at both ends of the chain, both arms, the REPORTED configuration ---"
LIST=""
mk () { arm=$1; env=$2; nk=$3; xs=$4
  i=0
  while [ $i -lt $nk ]; do
    j=$((i+250))
    LIST="$LIST
$D/src src_${arm}_k${i} $env LSTEP=8 LMAXL=2000 KSLICE=${i}:${j} SRCXS=${xs} SRCSAVE=$D/src/src_${arm}_k${i}_fields.npz"
    i=$j
  done; }
mk lcdm "$LCDM" 2547 "$XS_LCDM"
mk cr   "$CR"   1452 "$XS_CR"
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6911 LAUNCH COMPLETE $(date -u) ==="
