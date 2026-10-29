#!/bin/bash
# r7635+70: DRY re-point -- run a receipt on the arm of record WITHOUT editing it, for the seat that owns it.
# Builds a detached worktree of HEAD in $W, copies every spectra/<stem>_leafrec1.npz over spectra/<stem>.npz there,
# runs the receipt in both trees and diffs the two outputs.  The diff is the receipt's old -> new figures; its
# [FAIL] lines are the pins that move.  Nothing in the real tree is touched.
#   usage: bash dry_repoint.sh <receipt stem without .py> [<more stems>...]
set -u
ROOT=$(git -C "$(dirname "$0")" rev-parse --show-toplevel)
W=${W:-${TMPDIR:-/tmp}/r7635_dry_wt}; O=${O:-${TMPDIR:-/tmp}/r7635_dry_out}; mkdir -p "$O"
if [ ! -d "$W" ]; then
  git -C "$ROOT" worktree add -q --detach "$W" HEAD
  (cd "$W/computations/beyond_the_wall/spectra" && for f in *_leafrec1.npz; do cp "$f" "${f%_leafrec1.npz}.npz"; done)
fi
for r in "$@"; do
  p=$(cd "$ROOT/receipts" && ls */"$r".py | head -1)
  (cd "$W/receipts/$(dirname "$p")" && timeout 1800 python3 "$r.py" > "$O/$r.new" 2>&1; echo "rc=$?" >> "$O/$r.new")
  (cd "$ROOT/receipts/$(dirname "$p")" && timeout 1800 python3 "$r.py" > "$O/$r.old" 2>&1; echo "rc=$?" >> "$O/$r.old")
  echo "== $r: $(tail -1 "$O/$r.old") -> $(tail -1 "$O/$r.new"), [FAIL] $(grep -c '\[FAIL\]' "$O/$r.old") -> $(grep -c '\[FAIL\]' "$O/$r.new")"
  diff "$O/$r.old" "$O/$r.new" | grep '^[<>]' | cut -c1-240
done
