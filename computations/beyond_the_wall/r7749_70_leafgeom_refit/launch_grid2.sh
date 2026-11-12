#!/bin/bash
# r7749+70: the registered re-centring.  The verify run at the first grid's linearised minimum scored 189.58
# against the model's 185.07 (|diff| 4.5 > 1), so one further 9-leg grid is taken, centred on that run's point,
# with the first grid's steps.  Same switches as `r7093_directions/grid_oneclock_leafrec1/` (arm of record + LEAFGEOM=1).
# Idempotent: a leg whose log ends __DONE__ rc=0 is skipped.  Usage: launch_grid2.sh OUT_DIR
cd "$(dirname "$0")/.." || exit 1
D=${1:?OUT_DIR}; mkdir -p "$D"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
H=68.584954; O=0.296801; W=0.022469; N=0.960608
run () { tag=$1; shift
  [ -s "$D/$tag.log" ] && grep -q '^__DONE__ rc=0' "$D/$tag.log" && return 0
  env HIER=1 ARM=cr LEAFGEOM=1 LEAFREC=1 LEAFSCALES=1 LMAXL=2000 LSTEP=8 ZSTART=3e7 "$@" SAVE="$D/$tag.npz" \
    python3 -u ACOUSTIC_two_arm.py > "$D/$tag.log" 2>&1
  echo "__DONE__ rc=$?" >> "$D/$tag.log"; echo "  done $tag"; }
export -f run; export D
cat <<EOF | xargs -P 4 -L 1 bash -c 'run "$@"' _
cr_base CRH0=$H CROM=$O WBH2=$W NS=$N
cr_H0p CRH0=$(python3 -c "print($H+2.0)") CROM=$O WBH2=$W NS=$N
cr_H0m CRH0=$(python3 -c "print($H-2.0)") CROM=$O WBH2=$W NS=$N
cr_OMp CRH0=$H CROM=$(python3 -c "print($O+0.015)") WBH2=$W NS=$N
cr_OMm CRH0=$H CROM=$(python3 -c "print($O-0.015)") WBH2=$W NS=$N
cr_WBp CRH0=$H CROM=$O WBH2=$(python3 -c "print($W+0.0008)") NS=$N
cr_WBm CRH0=$H CROM=$O WBH2=$(python3 -c "print($W-0.0008)") NS=$N
cr_NSp CRH0=$H CROM=$O WBH2=$W NS=$(python3 -c "print($N+0.02)")
cr_NSm CRH0=$H CROM=$O WBH2=$W NS=$(python3 -c "print($N-0.02)")
EOF
