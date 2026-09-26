#!/bin/bash
# ** r6891 order (1), the finer l grid -- REBUILT AFTER A CONTAINER RESTART KILLED THE FIRST ATTEMPT.
#
#   The first attempt ran the four spectra whole at LSTEP=2 LMAXL=2000, ~100 minutes each.  The
#   container restarted at 80 minutes and took all four with it, because this instrument writes its
#   npz only at the end.  ** A run longer than the node's own lifetime is not a long run, it is a
#   run that does not finish. **  So this one is built two ways that both survive a restart:
#
#     A.  LSTEP=2 LMAXL=900 -- the FOUR-TIMES-finer grid, over the first three acoustic bands.
#         Cheap because the cost is (number of l) x (number of k) and k_max tracks LMAXL: ~6 min.
#     B.  LSTEP=4 LMAXL=2000 -- TWICE as fine as the banked spectra, over all five bands, run in
#         k-SLICES with KSLICE.  r6794 built that knob for exactly this: "C_l is a sum over k, so
#         disjoint slices add to the whole exactly, and the pieces are independent processes that a
#         container restart cannot spoil collectively."
#
#   ⛔ AND r6794's OWN CAVEAT IS CARRIED, NOT ASSUMED AWAY: slices add exactly only on a UNIFORM k
#   grid, because `_project` takes dk = np.gradient(kb) from the batch it is handed.  The CR arm's
#   ladder is not uniform, so its slice boundaries move the weights slightly.  ⇒ *Which does not
#   reach what is being measured here: the quantity is the SHIFT between two spectra computed with
#   IDENTICAL slicing, so a slicing artefact is common to both and cancels.  Step 0 below measures
#   the size of it rather than arguing about it.*
# ** IDEMPOTENT AND RESUMABLE at slice granularity. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6893; mkdir -p $D/slice $D/fine
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> $out/$tag.log; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D

echo "--- step 0: does slicing add?  two slices against the whole, at the screen grid ---"
printf '%s\n' \
 "$D/slice sl_lcdm_0_130    $LCDM LSTEP=16 LMAXL=500 KSLICE=0:130" \
 "$D/slice sl_lcdm_130_999  $LCDM LSTEP=16 LMAXL=500 KSLICE=130:999" \
 "$D/slice sl_cr_0_130      $CR   LSTEP=16 LMAXL=500 KSLICE=0:130" \
 "$D/slice sl_cr_130_999    $CR   LSTEP=16 LMAXL=500 KSLICE=130:999" \
 | xargs -P 4 -I{} bash -c 'run {}'

echo "--- A: LSTEP=2 LMAXL=900, whole, the four-times-finer grid over bands 1-3 ---"
printf '%s\n' \
 "$D/fine fineA_base_lcdm   $LCDM LSTEP=2 LMAXL=900" \
 "$D/fine fineA_nufs0_lcdm  $LCDM LSTEP=2 LMAXL=900 NUFS=0" \
 "$D/fine fineA_base_cr     $CR   LSTEP=2 LMAXL=900" \
 "$D/fine fineA_nufs0_cr    $CR   LSTEP=2 LMAXL=900 NUFS=0" \
 | xargs -P 4 -I{} bash -c 'run {}'

echo "--- B: LSTEP=4 LMAXL=2000, in k-slices of 250 ---"
LIST=""
for a in lcdm cr; do
  case $a in lcdm) B="$LCDM"; N=2547;; cr) B="$CR"; N=1452;; esac
  for v in base nufs0; do
    case $v in base) X="";; nufs0) X="NUFS=0";; esac
    i=0
    while [ $i -lt $N ]; do
      j=$((i+250))
      LIST="$LIST
$D/fine fineB_${v}_${a}_k${i} $B LSTEP=4 LMAXL=2000 KSLICE=${i}:${j} $X"
      i=$j
    done
  done
done
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6891 FINE2 COMPLETE $(date -u) ==="
