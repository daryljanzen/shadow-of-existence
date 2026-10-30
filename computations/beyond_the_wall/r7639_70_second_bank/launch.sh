#!/bin/bash
# r7639+70: the second leaf-rate bank -- what the first did not cover (69's r7639 items 1-3).  Each run keeps its
# recorded launcher's form and moves the CR point to the arm of record (LEAFREC=1 is the instrument default).
# Idempotent; the r6941 switch guard on every run; longest runs first.  Raw output in $D; bank.py folds it.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank2}
mkdir -p $D/visleaf $D/cross $D/g1300 $D/g2000 $D/gone $D/lever $D/inj $D/injl $D/scan
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
H=68.570730; O=0.291246; W=0.021643; N=1.015066
PT="CRH0=$H CROM=$O WBH2=$W NS=$N"
CR="ARM=cr $PT ZSTART=3e7 LEAFSCALES=1 LEAFREC=1"          # the arm of record, as r6885-r6959 ran it
CR0="ARM=cr $PT ZSTART=3e7 LEAFREC=1"                      # the crossing set: LEAFSCALES unset (=0), as r6784 ran it
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
W_CR=43.957277107          # the arm of record's visibility FWHM (r6911_source_cr_leafrec1 eta_ls_w; was 43.591)
W_LCDM=38.042364089
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  rc=$?
  line=$(grep -m1 '^__SWITCHES__ ' "$out/$tag.log")
  for a in "$@"; do
    case " $line " in *" $a "*) ;; *) echo "  ⛔ $tag: '$a' NOT in the switch line"; rc=90 ;; esac
  done
  echo "__DONE__ rc=$rc" >> "$out/$tag.log"; echo "  done $tag rc=$rc $(date -u +%H:%M:%S)"; }
export -f run; export D
L=""
add () { L="$L
$*"; }
sl () { sub=$1; tag=$2; nk=$3; step=$4; shift 4; i=0
  while [ $i -lt $nk ]; do add $D/$sub ${tag}_k$i "$@" KSLICE=$i:$((i+step)); i=$((i+step)); done; }
# 1. r6941 visleaf at LSTEP=1 (the longest)
sl visleaf fine_cr_f1 1452 250 HIER=1 $CR LSTEP=1 LMAXL=2000 VISLEAF=1
sl visleaf finj_cr    1452 250 HIER=1 $CR LSTEP=1 LMAXL=2000 SRCINJ=sweep SRCINJRS=own
sl visleaf finj_cr_f1 1452 250 HIER=1 $CR LSTEP=1 LMAXL=2000 VISLEAF=1 SRCINJ=sweep SRCINJRS=own
# 2. the crossing set with LEAFSCALES held at 0 (README:47-50)
F178="BSPLIT=1 NK=600 LMAXL=2000 ETAEND=4000 KBATCH=300"
add $D/cross r6784_cr_crossing_hier HIER=1 $CR0 $F178 CRIC=branchpoint
add $D/cross r6784_cr_crossing_hier_noCRIC HIER=1 $CR0 $F178
add $D/cross r6784_cr_crossing_los $CR0 $F178 CRIC=branchpoint
sl cross kc 2700 450 HIER=1 $CR0 BSPLIT=1 NK=900 LMAXL=2000 ETAEND=4000 KBATCH=150 KCONT=1
# 3. the response grids, centred on the arm of record, each launcher's steps
grid () { sub=$1; shift
  add $D/$sub cr_base HIER=1 LSTEP=8 "$@" $CR
  add $D/$sub cr_H0p  HIER=1 LSTEP=8 "$@" ARM=cr CRH0=70.570730 CROM=$O WBH2=$W NS=$N ZSTART=3e7 LEAFSCALES=1 LEAFREC=1
  add $D/$sub cr_H0m  HIER=1 LSTEP=8 "$@" ARM=cr CRH0=66.570730 CROM=$O WBH2=$W NS=$N ZSTART=3e7 LEAFSCALES=1 LEAFREC=1
  add $D/$sub cr_OMp  HIER=1 LSTEP=8 "$@" ARM=cr CRH0=$H CROM=0.306246 WBH2=$W NS=$N ZSTART=3e7 LEAFSCALES=1 LEAFREC=1
  add $D/$sub cr_OMm  HIER=1 LSTEP=8 "$@" ARM=cr CRH0=$H CROM=0.276246 WBH2=$W NS=$N ZSTART=3e7 LEAFSCALES=1 LEAFREC=1
  add $D/$sub cr_WBp  HIER=1 LSTEP=8 "$@" ARM=cr CRH0=$H CROM=$O WBH2=0.022443 NS=$N ZSTART=3e7 LEAFSCALES=1 LEAFREC=1
  add $D/$sub cr_WBm  HIER=1 LSTEP=8 "$@" ARM=cr CRH0=$H CROM=$O WBH2=0.020843 NS=$N ZSTART=3e7 LEAFSCALES=1 LEAFREC=1
  add $D/$sub cr_NSp  HIER=1 LSTEP=8 "$@" ARM=cr CRH0=$H CROM=$O WBH2=$W NS=1.035066 ZSTART=3e7 LEAFSCALES=1 LEAFREC=1
  add $D/$sub cr_NSm  HIER=1 LSTEP=8 "$@" ARM=cr CRH0=$H CROM=$O WBH2=$W NS=0.995066 ZSTART=3e7 LEAFSCALES=1 LEAFREC=1; }
grid g2000 LMAXL=2000                  # refit_grid185 AND grid_licensed: the same recipe now LEAFREC=1 is the default
grid gone LMAXL=2000 LEAFGEOM=1        # r7093 grid_oneclock
grid g1300 LMAXL=1300                  # refit_grid
# 4. the loading lever's arm runs (r7201 launch_ten / launch_three)
for v in 0.1 0.5 1.5; do add $D/lever cr_rb$v HIER=1 LSTEP=8 LMAXL=2000 $CR LEAFGEOM=1 RBFAC=$v; done
add $D/lever cr_nodrive HIER=1 LSTEP=8 LMAXL=2000 $CR LEAFGEOM=1 NODRIVE=1
# 5. r6919's injections on the arm, and the control's viswap with the arm of record's width
for c in "sweepown SRCINJ=sweep SRCINJRS=own" "sweepph SRCINJ=sweep SRCINJRS=own SRCINJPH=0.5" "fixed SRCINJ=fixed" \
         "sweepstk SRCINJ=sweep SRCINJRS=stack" "viswap SRCINJ=sweep SRCINJRS=own SRCINJVIS=$W_LCDM"; do
  set -- $c; t=$1; shift; sl inj inj_${t}_cr 1452 250 HIER=1 $CR LSTEP=8 LMAXL=2000 "$@"; done
sl injl inj_viswap_lcdm 2547 250 HIER=1 $LCDM LSTEP=8 LMAXL=2000 SRCINJ=sweep SRCINJRS=own SRCINJVIS=$W_CR
# 6. r6929's VISLEAF scan, real and injected
for f in 0 0.1 0.25 0.5 0.75 1; do t=${f//./}
  sl scan comb_cr_f$t 1452 250 HIER=1 $CR LSTEP=8 LMAXL=2000 VISLEAF=$f
  sl scan inj_cr_f$t  1452 250 HIER=1 $CR LSTEP=8 LMAXL=2000 VISLEAF=$f SRCINJ=sweep SRCINJRS=own; done
echo "$L" | sed '/^$/d' | wc -l
printf '%s' "$L" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7639 SECOND BANK COMPLETE $(date -u) ==="
