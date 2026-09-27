#!/bin/bash
# ** r6959 ⓵ᵇ -- THE NORMALISATION SWAP, AT THE SAMPLING THE CONTRAST IS MEASURED ON. **
#
#   `LSTEP=1 LMAXL=2000` is `r6941_fine_*`'s own sampling, so the tapered spectra are read against the
#   banked baselines with no re-binning and the comb is read off the grid the locator was cleared on at
#   `cc66.45`.  Sliced on `KBATCH` boundaries and idempotent: the instrument writes its npz only at the
#   end, and a run longer than its node's life is not a long run.
#
#   TWO tapers, both on the CONTROL and both with alpha > 0, so the taper is bounded by 1 everywhere:
#     `swap`  -- the literal ⓵ᵇ operation: the ARM's spread in r_s,leaf/r_s imposed on the control.
#                The measurement predicts f = 1.001 .. 1.007, so this run's job is to show the
#                instrument moves the contrast by the amount measured and NOT by the amount observed.
#     `big`   -- the taper that WOULD deliver the observed excess at the top band (f = 1.0762 there).
#                It answers what the candidate needs rather than what it has, and it is where the
#                predictor is calibrated at an amplitude large enough to read cleanly.
#
#   ⚠ ** THE REVERSE DIRECTION IS NOT RUN, AND THAT IS A CHOICE WITH A REASON. **  Widening a window
#   takes alpha < 0, so exp(-alpha (s-s0)^2) GROWS away from the anchor -- and the instrument applies it
#   over the whole eta grid, where |s - s0| reaches 427 Mpc and the ISW tail lives.  That would test the
#   tail and not the window.  *Both runs here narrow, and narrowing is the direction the hypothesis
#   needs: the arm is the LESS smeared of the two.*
cd /home/user/shadow-of-existence/computations/beyond_the_wall || exit 1
D=/tmp/n66/r6959; mkdir -p $D/swap
[ -s $D/eta/prediction.json ] || { echo "⛔ no prediction.json -- ⓵ᵃ must run first"; exit 1; }
rd () { python3 -c "import json;print('%.10g'%json.load(open('$D/eta/prediction.json'))['$1'])"; }
AL=$(rd alpha); AB=$(rd alpha_big); S0=$(rd s0)
echo "  the swap: SRCTAPER=$AL   the big taper: SRCTAPER=$AB   both at SRCTAPERS0=$S0"
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
LCDM="ARM=lcdm LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248"

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
bash switch_smoke.sh $LCDM LSTEP=1 LMAXL=2000 SRCTAPER=$AB SRCTAPERS0=$S0 || ok=0
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
add big_lcdm  2547 $LCDM LSTEP=1 LMAXL=2000 SRCTAPER=$AB SRCTAPERS0=$S0
printf '%s' "$LIST" | sed '/^$/d' | xargs -P 4 -I{} bash -c 'run {}'
echo "=== r6959 B LAUNCH COMPLETE $(date -u) ==="
ls $D/swap/*.npz | wc -l
