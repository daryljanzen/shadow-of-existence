#!/bin/bash
# r7641+70: cc66's gap list at the arm of record, each by its own launcher's form (r6893 screen.sh/fine2.sh,
# r6925 launch.sh, r6885 launch.sh, r6889 launch.sh).  Idempotent; raw output in $D; bank.py folds it.
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=${D:-/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank3}
mkdir -p $D/screen $D/fine $D/slice $D/vl $D/knob $D/r6889
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
CR="ARM=cr CRH0=68.570730 CROM=0.291246 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021643 NS=1.015066"
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  echo "__DONE__ rc=$?" >> "$out/$tag.log"; echo "  done $tag $(date -u +%H:%M:%S)"; }
export -f run; export D
L=""
add () { L="$L
$*"; }
# the r6885 knob pairs, BOTH arms, and r6889's three (HIER=1 LSTEP=8 LMAXL=2000) -- the long ones first
for k in "ln24 LN=24" "noisw NOISW=1" "dre0 DRE=0" "drc0 DRC=0"; do set -- $k
  add $D/knob ${1}_cr   HIER=1 LSTEP=8 LMAXL=2000 $CR $2
  add $D/knob ${1}_lcdm HIER=1 LSTEP=8 LMAXL=2000 $LCDM $2; done
add $D/r6889 noop_cr HIER=1 LSTEP=8 LMAXL=2000 $CR
add $D/r6889 hdp0_cr HIER=1 LSTEP=8 LMAXL=2000 $CR DPSRC=0
add $D/r6889 hsw0_cr HIER=1 LSTEP=8 LMAXL=2000 $CR SWSRC=0
# r6893 fine grid: A whole, B in slices of 250, and the slice-sum pair
for v in "base" "nufs0 NUFS=0"; do set -- $v
  add $D/fine fineA_${1}_cr HIER=1 $CR LSTEP=2 LMAXL=900 $2
  for i in 0 250 500 750 1000 1250; do add $D/fine fineB_${1}_cr_k$i HIER=1 $CR LSTEP=4 LMAXL=2000 KSLICE=$i:$((i+250)) $2; done; done
add $D/slice sl_cr_0_130   HIER=1 $CR LSTEP=16 LMAXL=500 KSLICE=0:130
add $D/slice sl_cr_130_999 HIER=1 $CR LSTEP=16 LMAXL=500 KSLICE=130:999
# r6925 visleaf: the injection and the comb under VISLEAF=1
for i in 0 250 500 750 1000 1250; do
  add $D/vl injvl_cr_k$i  HIER=1 $CR LSTEP=8 LMAXL=2000 KSLICE=$i:$((i+250)) VISLEAF=1 SRCINJ=sweep SRCINJRS=own
  add $D/vl combvl_cr_k$i HIER=1 $CR LSTEP=8 LMAXL=2000 KSLICE=$i:$((i+250)) VISLEAF=1; done
# r6893 switch screen, the cr half (screen.sh's list, verbatim switch values; LEAFSCALES variant at 0)
G="HIER=1 LSTEP=16 LMAXL=500"
while read -r t sw; do add $D/screen ${t}_cr $G $CR $sw; done <<SCR
base
BSPLIT BSPLIT=0
CRAMP CRAMP=onset
CRIC CRIC=branchpoint
CRPHI CRPHI=0.7854
CRPSI CRPSI=envelope
CRXE CRXE=0.70
CRH0 CRH0=69.0
CROM CROM=0.3100
DPSRC DPSRC=0
DRC DRC=0.5
DRE DRE=0.5
ETAEND ETAEND=3000
GSRC GSRC=1
KBATCH KBATCH=100
KCONT KCONT=1
KFAC KFAC=3.0
KSLICE KSLICE=0:200
LATARG LATARG=310.0
LG LG=32
LH0 LH0=68.0
LMAXL LMAXL=600
LN LN=16
LOM LOM=0.3200
LRSFROM LRSFROM=start
LSTEP LSTEP=20
LZSTART LZSTART=1.0e7
NK NK=320
NLOS NLOS=700
NODRIVE NODRIVE=1
NOISW NOISW=1
NOTC NOTC=0
NS NS=0.9800
NUFS NUFS=0
ORFAC ORFAC=1.5
PHASEONLY PHASEONLY=1
PHASEPOW PHASEPOW=1
PHASEPOWon PHASEONLY=1 PHASEPOW=1
PISRC PISRC=0
POLC POLC=0.0
RBFAC RBFAC=1.1
RTOL RTOL=1e-6
STACKPERT STACKPERT=1
TCSW TCSW=5.0
WBH2 WBH2=0.02250
ZSTART ZSTART=1.0e7
LEAFSCALES LEAFSCALES=0
DAMPX DAMPX=2.0
DSCAN DSCAN=1
DSAVE DSAVE=$D/screen/junk_dsave_cr.npz
NOPROJ NOPROJ=1
PHISAVE PHISAVE=$D/screen/junk_phi_cr.npz
QK QK=0.02,0.05,0.10
QMIN QMIN=1
QTURN QTURN=vel
RD RD=8.0
RD_2 RD=3.0
SCR
echo "$L" | sed '/^$/d' | wc -l
printf '%s' "$L" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r7641 THIRD BANK COMPLETE $(date -u) ==="
