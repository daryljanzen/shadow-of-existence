#!/bin/bash
# ** r6941's order (66 heads it `r6939`): THE FOURTH PEAK, AND THE LOCATOR BEFORE THE RESIDUAL. **
#
#   ⓶ FIRST, THE INSTRUMENT AND NOT THE PHYSICS: *establish the locator's own precision at each of the
#     four peaks before reading any residual off them.*  `cc66.44` validated it at l_1 on the banked
#     `LSTEP=1` spectrum (0.004 of a multipole), but ** l_4 sits where the damping has flattened the
#     peak **, and a locator's precision at a suppressed extremum is a different number.
#       ⇒ So: the reported configuration is run again at `LSTEP=1` -- eight times the multipole
#         sampling -- on BOTH arms, and the coarse grid's locator is measured against it peak by peak.
#         *The control is the null that makes it readable: there the sky's own peaks are what the
#         control reproduces, so a locator error shows up as a residual on an arm that has none.*
#   ⓷ THEN the three-way separation at l_2, l_3, l_4 -- which needs the `VISLEAF` endpoints, so the
#     arm's real spectrum AND its injection are run fine at f=0 and f=1.
#
# ⚑ `LSTEP=1 LMAXL=2000` is 1900 multipoles against the reported 238, and one cr slice costs 4m37s, so
#   the set is sliced on `KBATCH` boundaries as usual and is idempotent.  ** r6893 lost a whole
#   LSTEP=2 run to a container restart at eighty minutes of a hundred: this instrument writes its npz
#   only at the end, and a run longer than its node's own lifetime is not a long run. **
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6941; mkdir -p $D/fine $D/inj
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"
CR="ARM=cr CRH0=68.581133 CROM=0.297209 ZSTART=3e7 LEAFSCALES=1 WBH2=0.021524 NS=0.997952"

run () { out=$1; tag=$2; shift 2
  [ -s "$out/$tag.log" ] && grep -q '^__DONE__ rc=0' "$out/$tag.log" && { echo "  skip $tag"; return 0; }
  env HIER=1 "$@" SAVE=$out/$tag.npz python3 -u ACOUSTIC_two_arm.py > $out/$tag.log 2>&1
  rc=$?
  line=$(grep -m1 '^__SWITCHES__ ' "$out/$tag.log")
  for a in "$@"; do
    case " $line " in *" $a "*) ;; *) echo "  ⛔ $tag: '$a' NOT in the instrument's switch line"; rc=90 ;; esac
  done
  echo "__DONE__ rc=$rc" >> "$out/$tag.log"; echo "  done $tag rc=$rc $(date -u +%H:%M:%S)"
  [ $rc -eq 0 ] || { echo "  ⛔ $tag FAILED"; return 1; }; }
export -f run; export D

echo "=== the standing switch guard, on every distinct environment, before the set goes out ==="
ok=1
bash switch_smoke.sh $LCDM LSTEP=1 LMAXL=2000 || ok=0
bash switch_smoke.sh $CR LSTEP=1 LMAXL=2000 || ok=0
bash switch_smoke.sh $CR LSTEP=1 LMAXL=2000 VISLEAF=1 || ok=0
bash switch_smoke.sh $CR LSTEP=1 LMAXL=2000 SRCINJ=sweep SRCINJRS=own || ok=0
bash switch_smoke.sh $CR LSTEP=1 LMAXL=2000 VISLEAF=1 SRCINJ=sweep SRCINJRS=own || ok=0
[ $ok -eq 1 ] || { echo "⛔ the switch guard failed -- nothing launched"; exit 1; }

LIST=""
add () { tag=$1; sub=$2; nk=$3; shift 3
  i=0
  while [ $i -lt $nk ]; do
    j=$((i+250))
    LIST="$LIST
$D/$sub ${tag}_k${i} $* KSLICE=${i}:${j}"
    i=$j
  done; }
# ⓶ the fine reference on BOTH arms, at the reported configuration
add fine_lcdm  fine 2547 $LCDM LSTEP=1 LMAXL=2000
add fine_cr    fine 1452 $CR   LSTEP=1 LMAXL=2000
# ⓷ and the VISLEAF endpoints on the arm, real and injected, so the three-way split is read fine too
add fine_cr_f1 fine 1452 $CR   LSTEP=1 LMAXL=2000 VISLEAF=1
add finj_cr    inj  1452 $CR   LSTEP=1 LMAXL=2000 SRCINJ=sweep SRCINJRS=own
add finj_cr_f1 inj  1452 $CR   LSTEP=1 LMAXL=2000 VISLEAF=1 SRCINJ=sweep SRCINJRS=own
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6941 LAUNCH COMPLETE $(date -u) ==="
