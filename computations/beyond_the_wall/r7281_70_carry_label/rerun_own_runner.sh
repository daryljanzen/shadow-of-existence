#!/bin/bash
cd /home/user/shadow-of-existence
i=0
while read kind sha rec; do
  i=$((i+1)); wt=/tmp/claude-0/runs/wt$i
  git worktree add -q --detach $wt $sha 2>/dev/null
  echo "$rec" > /tmp/claude-0/runs/scope$i.txt
  (cd $wt && NODE=ci timeout 900 python3 scripts/run_all_receipts.py --from /tmp/claude-0/runs/scope$i.txt --jobs 1 --timeout 300 > /tmp/claude-0/runs/log$i.txt 2>&1)
  echo "$i $kind $sha done rc=$?" >> /tmp/claude-0/runs/progress.txt
  git worktree remove --force $wt
done < /tmp/claude-0/runs.txt
echo ALLDONE >> /tmp/claude-0/runs/progress.txt
