#!/bin/bash
# r7695+cc66: THE DIP COUNTERFACTUAL'S REBUILD -- the CR plasma with the control's acoustic period.
#
# The dip test's banks are `_BR` = the PAIRS bank (D_l, on QL = l/l_A) and the SOURCE bank
# (S_i**2, on QK = k r_s/pi).  So "one CR source-and-pairs rebuild" is six SRCSAVE slices and six
# SRCDEC slices, at the arm of record's point, with COMBRHO set.
#
# COMBRHO = T_K(arm)/T_K(control) = 1.011500/1.017000, MEASURED by the statistic's own comb fitter on
# the banks the dip test reads (`comb_target.py`), NOT derived from the r_s ratio -- which is a
# different quantity (0.82 per cent against this 0.54) and would overshoot by half again.
# Registered in GATE_3_REGISTERED.md and pushed before this script was run.
#
# ⛔ The switches each run must carry, and the guard below asserts each one appears in the
#   instrument's own `__SWITCHES__` line rather than trusting the environment:
#     HIER=1   -- `_project`'s only caller is `hier_run`, which is reached ONLY under HIER=1.  Four
#                 of the gate-1/gate-2 harness faults were runs that never entered the patched path.
#     COMBRHO  -- the switch itself.
# ⛔ Banked under NEW stems by `bank_combrho.py`; the arm of record's banks are never written.
# IDEMPOTENT AND RESUMABLE: a finished slice is skipped on `__DONE__ rc=0`.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/26826c5d-5f18-5adf-9ba6-b04043e78f9b/scratchpad/combrho}
mkdir -p $D/src $D/dec
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
CR="ARM=cr CRH0=68.570730 CROM=0.291246 ZSTART=3e7 LEAFSCALES=1 LEAFREC=1 WBH2=0.021643 NS=1.015066"
XS_CR=0.987292934      # D_M(control)/D_M(arm of record) = 13954.3535/14133.9546
RHO=0.9945919371
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  rc=$?
  line=$(grep -m1 '^__SWITCHES__ ' "$out/$tag.log")
  for a in "$@"; do
    case "$a" in SRCSAVE=*|SRCDEC=*) continue;; esac
    case " $line " in *" $a "*) ;; *) echo "  ⛔ $tag: '$a' NOT in the switch line"; rc=90 ;; esac
  done
  echo "__DONE__ rc=$rc" >> "$out/$tag.log"; echo "  done $tag rc=$rc $(date -u +%H:%M:%S)"; }
export -f run; export D
L=""
add () { L="$L
$*"; }
for i in $(seq 0 250 1451); do
  add $D/src src_cr_k$i HIER=1 $CR COMBRHO=$RHO LSTEP=8 LMAXL=2000 KSLICE=$i:$((i+250)) \
      SRCXS=$XS_CR SRCSAVE=$D/src/src_cr_k${i}_fields.npz
done
for i in $(seq 0 250 1451); do
  add $D/dec dec_cr_k$i HIER=1 $CR COMBRHO=$RHO LSTEP=8 LMAXL=2000 KSLICE=$i:$((i+250)) \
      SRCDEC=$D/dec/dec_cr_k${i}_pairs.npz
done
printf '%s' "$L" | sed '/^$/d' | xargs -P ${P:-3} -I{} bash -c 'run {}'
echo "=== r7695 COMBRHO REBUILD COMPLETE $(date -u) ==="
grep -L '^__DONE__ rc=0' $D/src/*.log $D/dec/*.log 2>/dev/null | sed 's/^/  ⛔ NOT rc=0: /'
