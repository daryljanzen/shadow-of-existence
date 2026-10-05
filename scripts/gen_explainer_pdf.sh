#!/usr/bin/env bash
# The explainer's PDF, printed from the same generated page a reader opens, so
# the two cannot disagree.  Used by the Pages build; runnable locally.
#   usage: scripts/gen_explainer_pdf.sh [in.html] [out.pdf]
set -euo pipefail
IN="${1:-BOOK_INTRO_cosmiCave/explainer.html}"
OUT="${2:-BOOK_INTRO_cosmiCave/explainer.pdf}"
CHROME="${CHROME:-}"
if [ -z "$CHROME" ]; then
  for c in google-chrome google-chrome-stable chromium chromium-browser \
           /opt/pw-browsers/chromium-*/chrome-linux/chrome; do
    if command -v "$c" >/dev/null 2>&1 || [ -x "$c" ]; then CHROME="$c"; break; fi
  done
fi
[ -n "$CHROME" ] || { echo "no Chrome/Chromium found" >&2; exit 1; }
"$CHROME" --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer \
  --print-to-pdf-no-header --print-to-pdf="$OUT" "file://$(realpath "$IN")" 2>/dev/null
test -s "$OUT"
echo "  explainer.pdf written: $(wc -c < "$OUT") bytes"
