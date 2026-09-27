#!/bin/bash
# ** r6959 ⓵ᵇ -- THE NORMALISATION SWAP, AT THE SAMPLING THE CONTRAST IS MEASURED ON. **
#
#   `LSTEP=1 LMAXL=2000` is `r6941_fine_*`'s own sampling, so the tapered spectra are read against the
#   banked baselines with no re-binning and the comb and the depths are read off the same grid the
#   locator was cleared on at `cc66.45`.  Sliced on `KBATCH` boundaries and idempotent: the instrument
#   writes its npz only at the end, and a run longer than its node's life is not a long run.
#
#   ⚠ ** ONLY THE BOUNDED DIRECTION IS RUN, AND THAT IS A CHOICE WITH A REASON. **  A taper that
#   WIDENS the window has a coefficient of the other sign, so exp(-alpha (s-s0)^2) grows away from the
#   anchor -- and the instrument applies it over the whole eta grid, where the ISW tail lives.  At the
#   coefficient the reverse swap needs that factor reaches ~700 in the tail, which would test the tail
#   and not the window.  *So the control is narrowed onto the arm (alpha > 0, taper <= 1 everywhere)
#   and the predictor is calibrated a second time by narrowing the ARM further, which is the same
#   direction and an independent number.*
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6959; mkdir -p $D/swap
[ -s $D/eta/prediction.json ] || { echo "⛔ no prediction.json -- ⓵ᵃ must run first"; exit 1; }
AL=$(python3 -c "import json;print('%.10g'%json.load(open('$D/eta/prediction.json'))['alpha'])")
S0=$(python3 -c "import json;print('%.10g'%json.load(open('$D/eta/prediction.json'))['s0'])")
AT=${AT:?the arm's tightening coefficient must be passed}
ST=${ST:?the arm's anchor must be passed}
echo "  the swap: SRCTAPER=$AL SRCTAPERS0=$S0 on the control; SRCTAPER=$AT SRCTAPERS0=$ST on the arm"
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
bash switch_smoke.sh $LCDM LSTEP=1 LMAXL=2000 SRCTAPER=$AL SRCTAPERS0=$S0 || ok=0
bash switch_smoke.sh $CR   LSTEP=1 LMAXL=2000 SRCTAPER=$AT SRCTAPERS0=$ST || ok=0
[ $ok -eq 1 ] || { echo "⛔ the switch guard failed -- nothing launched"; exit 1; }

LIST=""
add () { tag=$1; nk=$2; shift 2
  i=0
  while [ $i -lt $nk ]; do
    j=$((i+250))
    LIST="$LIST
$D/swap ${tag}_k${i} $* KSLICE=${i}:${j}"
    i=$j
  done; }
add swap_lcdm 2547 $LCDM LSTEP=1 LMAXL=2000 SRCTAPER=$AL SRCTAPERS0=$S0
add tight_cr  1452 $CR   LSTEP=1 LMAXL=2000 SRCTAPER=$AT SRCTAPERS0=$ST
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6959 B LAUNCH COMPLETE $(date -u) ==="
