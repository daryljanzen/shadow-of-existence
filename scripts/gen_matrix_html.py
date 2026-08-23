#!/usr/bin/env python3
# Regenerates BOOK_INTRO_cosmiCave/assets/dependency_matrix.html as STATIC HTML (no JS) so it renders in every viewer, incl. sandboxed mobile previews.
# Usage: from corpus/, run gen_matrix_html_table.py > /tmp/table.html, then gen_matrix_html.py. Or fold both into one call. Counts recomputed from source; resolver mirrors BIBKEY_ALIAS_MAP.md.
import os
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   'BOOK_INTRO_cosmiCave', 'assets', 'dependency_matrix.html')

table = open('/tmp/table.html').read().split('<!--TABLE-->\n',1)[1].strip()
head = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CR corpus — dependency matrix</title>
<style>
  :root{
    --ink:#1c2733; --faint:#9aa7b4; --line:#e2e8ee; --pole:#b5462a;
    --bg:#fbfcfd;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--ink);
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
    padding:20px 14px 40px;-webkit-font-smoothing:antialiased}
  h1{font-size:19px;font-weight:650;margin:0 0 4px;letter-spacing:-.01em}
  .sub{color:var(--faint);font-size:13px;margin:0 0 18px;line-height:1.5;max-width:640px}
  .sub b{color:var(--pole)}
  .scroll{overflow-x:auto;-webkit-overflow-scrolling:touch;
    border:1px solid var(--line);border-radius:12px;background:#fff;
    box-shadow:0 1px 3px rgba(20,40,60,.04)}
  table{border-collapse:collapse;font-variant-numeric:tabular-nums;margin:0 auto}
  th,td{width:30px;height:29px;text-align:center;font-size:12.5px;
    border:1px solid #eef2f6}
  thead th{font-weight:600;color:var(--ink);background:#f6f9fb;position:sticky;top:0}
  tbody th{font-weight:600;background:#f6f9fb;text-align:right;padding-right:7px;
    width:40px;position:sticky;left:0}
  td.diag{background:#eef2f6;color:#c2ccd6}
  td.zero{color:#d3dbe2}
  .polecol{box-shadow:inset 2px 0 0 var(--pole), inset -2px 0 0 var(--pole)}
  thead th.poleh,tbody th.poleh{color:var(--pole)}
  tr.polerow th, tr.polerow td{border-top:2px solid var(--pole);border-bottom:2px solid var(--pole)}
  .corner{background:#f6f9fb;color:var(--faint);font-weight:500;font-size:11px}
  .lz{color:var(--pole);font-weight:700}
  .legend{margin:16px auto 0;max-width:640px;font-size:12.5px;color:#54626f;line-height:1.6}
  .legend .row{display:flex;gap:14px;flex-wrap:wrap;margin-top:8px}
  .chip{display:inline-flex;align-items:center;gap:6px}
  .sw{width:15px;height:15px;border-radius:3px;border:1px solid #e2e8ee}
  .names{margin-top:14px;font-size:11.5px;color:#7a8794;line-height:1.7}
</style>
</head>
<body>
  <h1>Cosmological Relativity — the corpus dependency matrix</h1>
  <p class="sub">Entry (row&nbsp;<i>i</i>, col&nbsp;<i>j</i>) = number of times paper&nbsp;<i>i</i> cites paper&nbsp;<i>j</i>, shaded by weight.
    The two <b>poles</b> are marked in red: <b>P7</b> (framework) and <b>p0</b> (geometric core) — the only rows-and-columns that are <i>full</i>,
    each bidirectionally coupled to the whole corpus. ◇ marks the P1↔P4 complementarity (independence, not dependency).</p>
  <!-- Table baked as static HTML (no JS) so it renders in every viewer incl. sandboxed mobile previews. Numbers refreshed r926; regenerate via scripts/depmatrix.py after any citation change. -->
  <div class="scroll">'''
tail = '''</div>
  <div class="legend">
    <div><b>Reading:</b> a <i>row</i> is what a paper rests on; a <i>column</i> is what it feeds. P7 draws on the whole spine (heaviest row); P3 is the most-drawn-on hub (its column); <b>P16</b> (cosmogenesis) is the newest synthesis node — its row rests on the whole spine it conjoins (leaning hardest on P15 and P8), its column shows the whole corpus now points into it. p0's last row &amp; column are the reciprocity engine's product — the core built from everyone and pointing back to everyone, P16 included.</div>
    <div class="row">
      <span class="chip"><span class="sw" style="background:#eef4fa"></span>1–2</span>
      <span class="chip"><span class="sw" style="background:#bcd6ee"></span>3–6</span>
      <span class="chip"><span class="sw" style="background:#6ea3d6"></span>7–12</span>
      <span class="chip"><span class="sw" style="background:#2f6fb3"></span>13–20</span>
      <span class="chip"><span class="sw" style="background:#14416f"></span>34</span>
    </div>
    <div class="names">
      P1 wedge · P2 circle · P3 slicing · P4 modern parallax · P5 groupoid · P6 shadow · <b style="color:var(--pole)">P7 framework</b> ·
      P8 operator · P9 range · P10 canonical time · P11 dynamics · P12 algebroid · P13 boundary · P14 matter · P15 cosmology · P16 cosmogenesis · <b style="color:var(--pole)">p0 geometric core</b>
    </div>
  </div>
</body>
</html>
'''
open(OUT,'w').write(head+'<table>'+table+'</table>'+tail)
print("written. total bytes:", len(head+table+tail))
