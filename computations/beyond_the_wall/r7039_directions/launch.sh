#!/bin/bash
# ** r7039's order (`PO-70`): WHAT PROPERTY OF Delta_l(k) = INT S j_l(k(eta_0-eta)) d eta PRODUCES
#    THE 1.054 RETENTION -- and is it required by this background or an artefact of how the integral
#    is carried? **
#
#   ⛭ THE PRE-REGISTRATION IS `PREDICTION.md`, COMMITTED BEFORE ANY OF THIS RAN, and it is corrected
#     at its own head: the first draft's central stage was `r6919`'s clock swap, which `cc66.42`
#     already ran.  What is left after subtracting `r6919` is the ACCEPTANCE reading.
#
#   ⓐ ** M2 FIRST, BECAUSE M2 IS THE READING THAT RESCUES THE FIT. **  The retention is an artefact
#     exactly when the chi-extent that sets the kernel's k-acceptance is the QUADRATURE's extent and
#     not the visibility's.  Three quadrature choices reach it and all three are now names rather
#     than literals: `NLOS` (the resolution), `NLOSW` (the half-width in FWHM), `NLOSF` (the split of
#     points between the window and the ISW tail).  ⌗ The k extent is NOT re-run: `r3870`'s own
#     convergence table settles it at k_max = 2400/D_M and `KFAC=2.0` puts this instrument at
#     4000/D_M, past it.  The switch does not reach the injected source at all -- `D` multiplies the
#     hierarchy's `Th0`, `Pi` and `tb`, and the injection replaces `S` entirely.
#
#   ⓑ ** THE ACCEPTANCE, EXHIBITED. **  `DLKSAVE` writes Delta_l(k) -- the transfer itself, which no
#     earlier save carried, every one of them being downstream of the k-sum.  With `SRCINJ=fixed` the
#     integral factorises exactly, Delta_l(k) = cos(k r_s*) k^((1-ns)/2) G_l(k), so G_l is readable
#     off the saved transfer and its k-acceptance width is measurable as a second moment.
#
#   ⓔ ** AND THE SWEEP, FOR THE GAP. **  `r6919` measured 1.0659 sweeping against 1.0587 fixed; the
#     acceptance law owes an account of the difference or it is a bound and not a mechanism.
#
# ** The solver is SKIPPED on every run here (the analytic source replaces `S`), so each slice is
#    seconds of setup plus the projection.  Sliced on KBATCH boundaries; IDEMPOTENT AND RESUMABLE. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r7039; mkdir -p $D/noop $D/inj $D/dlk
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D

echo "--- the no-op gate: NLOSW, NLOSF and DLKSAVE must change nothing when unset ---"
printf '%s\n' \
 "$D/noop noop_lcdm  $LCDM LSTEP=16 LMAXL=500" \
 "$D/noop noop_cr    $CR   LSTEP=16 LMAXL=500" \
 | xargs -P 2 -I{} bash -c 'run {}'

# ⓑ and ⓔ: the transfer itself, on the REPORTED grids, one file per slice
echo "--- the transfer Delta_l(k): fixed and sweeping, both arms ---"
LIST=""
addk () { tag=$1; arm=$2; env=$3; nk=$4; shift 4
  i=0
  while [ $i -lt $nk ]; do
    j=$((i+250))
    LIST="$LIST
$D/dlk dlk_${tag}_${arm}_k${i} $env LSTEP=8 LMAXL=2000 KSLICE=${i}:${j} $* DLKSAVE=$D/dlk/dlk_${tag}_${arm}_k${i}_T.npz"
    i=$j
  done; }
addk fixed    lcdm "$LCDM" 2547 SRCINJ=fixed
addk fixed    cr   "$CR"   1452 SRCINJ=fixed
addk sweepown lcdm "$LCDM" 2547 SRCINJ=sweep SRCINJRS=own
addk sweepown cr   "$CR"   1452 SRCINJ=sweep SRCINJRS=own
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'

# ⓐ: the three quadrature choices, on the FIXED injection -- the one whose q-slope matches the real
#    source's to two per cent, so it is the configuration the artefact question is actually about
echo "--- M2: the quadrature, five variations, both arms ---"
LIST=""
addq () { tag=$1; arm=$2; env=$3; nk=$4; shift 4
  i=0
  while [ $i -lt $nk ]; do
    j=$((i+250))
    LIST="$LIST
$D/inj inj_${tag}_${arm}_k${i} $env LSTEP=8 LMAXL=2000 KSLICE=${i}:${j} SRCINJ=fixed $*"
    i=$j
  done; }
for a in "n1120 NLOS=1120" "n2240 NLOS=2240" "w9 NLOSW=9.0" "w4 NLOSW=4.0" "f90 NLOSF=0.90"; do
  set -- $a
  addq "$1" lcdm "$LCDM" 2547 "$2"
  addq "$1" cr   "$CR"   1452 "$2"
done
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7039 LAUNCH COMPLETE $(date -u) ==="
