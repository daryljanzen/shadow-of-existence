#!/bin/bash
# r7635+70: the r6885-r6959 family (one recorded point, clean launchers), regenerated on the arm of record.
# Each run keeps its launcher's switches verbatim and changes only the CR point and LEAFREC.
# Idempotent; the r6941 switch guard on every run.  Raw outputs go to $D; bank.py folds them into spectra/.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank}
mkdir -p $D/plain $D/src $D/kcont $D/dec $D/fine $D/eta
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
CR="ARM=cr CRH0=68.570730 CROM=0.291246 ZSTART=3e7 LEAFSCALES=1 LEAFREC=1 WBH2=0.021643 NS=1.015066"
XS_CR=0.987292934      # D_M(control)/D_M(arm of record) = 13954.3535/14133.9546
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  rc=$?
  line=$(grep -m1 '^__SWITCHES__ ' "$out/$tag.log")
  for a in "$@"; do
    case "$a" in SRCSAVE=*|SRCDEC=*|SRCETA=*) continue;; esac
    case " $line " in *" $a "*) ;; *) echo "  ⛔ $tag: '$a' NOT in the switch line"; rc=90 ;; esac
  done
  echo "__DONE__ rc=$rc" >> "$out/$tag.log"; echo "  done $tag rc=$rc $(date -u +%H:%M:%S)"; }
export -f run; export D
L=""
add () { L="$L
$*"; }
# plain LSTEP=8 runs (refit_grid185/verify.sh, r6885 launch/launch2, r6889 launch)
add $D/plain r185_verify_cr HIER=1 $CR LSTEP=8 LMAXL=2000
add $D/plain r6885_dp0_cr   HIER=1 $CR LSTEP=8 LMAXL=2000 DPSRC=0
add $D/plain r6885_los_cr   $CR LSTEP=8 LMAXL=2000
add $D/plain r6885_losdp0_cr $CR LSTEP=8 LMAXL=2000 DPSRC=0
add $D/plain r6885_lossw0_cr $CR LSTEP=8 LMAXL=2000 SWSRC=0
add $D/plain r6889_nufs0_cr HIER=1 $CR LSTEP=8 LMAXL=2000 NUFS=0
add $D/eta   eta_cr HIER=1 $CR LSTEP=8 LMAXL=2000 SRCETA=$D/eta/eta_cr_prof.npz
for i in $(seq 0 250 1451); do add $D/src src_cr_k$i HIER=1 $CR LSTEP=8 LMAXL=2000 KSLICE=$i:$((i+250)) SRCXS=$XS_CR SRCSAVE=$D/src/src_cr_k${i}_fields.npz; done
for i in $(seq 0 250 2546); do add $D/kcont src_crkc_k$i HIER=1 $CR KCONT=1 LSTEP=8 LMAXL=2000 KSLICE=$i:$((i+250)) SRCXS=$XS_CR SRCSAVE=$D/kcont/src_crkc_k${i}_fields.npz; done
for i in $(seq 0 250 1451); do add $D/dec dec_cr_k$i HIER=1 $CR LSTEP=8 LMAXL=2000 KSLICE=$i:$((i+250)) SRCDEC=$D/dec/dec_cr_k${i}_pairs.npz; done
for i in $(seq 0 250 1451); do add $D/fine fine_cr_k$i HIER=1 $CR LSTEP=1 LMAXL=2000 KSLICE=$i:$((i+250)); done
printf '%s' "$L" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7635 CLEAN BATCH COMPLETE $(date -u) ==="
