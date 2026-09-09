#!/usr/bin/env python3
"""
gen_live_edition.py -- builds BOOK_INTRO_cosmiCave/live_edition.html

** THE ONE DESIGN RULE, AND IT IS THE CORPUS'S OWN LESSON. **  The page does NOT
embed the frontier.  It FETCHES `THE_FRONTIER.md` from the CDN at read time and
renders it in the browser.

  A page that baked in the open-row count would be a SECOND HOME for that count,
  and every second home in this corpus has gone stale -- the register's masthead
  (r4487), THE_PLAN's grain cell (r4479), OPEN_PROBLEMS_MAP (r4515), THE_FRONTIER's
  own headline (r4551).  The frontier is generated from THE_REGISTER by
  regen_frontier.py, which is the one source; this page reads that artefact and
  owns no copy of it.

The paper list IS baked, because it changes on the scale of years and a wrong
title is visible on sight.  The PDFs are served from jsDelivr, a CDN over the
repo: raw.githubusercontent is not built for reader traffic and rate-limits.

Usage:  python3 scripts/gen_live_edition.py        (from the repo root)
"""
import os
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'BOOK_INTRO_cosmiCave', 'live_edition.html')
CDN = 'https://cdn.jsdelivr.net/gh/daryljanzen/shadow-of-existence@main'
RAW = 'https://raw.githubusercontent.com/daryljanzen/shadow-of-existence/main'

# P-number -> tex stem, from P7's dependency matrix ordering.
ORDER = [
    ('p0', 'geometric_core_paper'), ('P1', 'BH_causality_v2'),
    ('P2', 'janzen_circle_v3'), ('P3', 'SdS-slicing-curve_v2'),
    ('P4', 'modern_parallax'), ('P5', 'groupoid_paper'),
    ('P6', 'shadow_of_existence'), ('P7', 'CR_framework'),
    ('P8', 'slicing_operator'), ('P9', 'range_paper'),
    ('P10', 'canonical_time'), ('P11', 'dynamics_paper'),
    ('P12', 'algebroid_paper'), ('P13', 'boundary_paper'),
    ('P14', 'matter_sector_paper'), ('P15', 'CR_cosmology'),
    ('P16', 'cosmogenesis_paper'), ('P18', 'CR_synthesis'),
]


def title_of(stem):
    p = os.path.join(ROOT, 'corpus', stem + '.tex')
    if not os.path.exists(p):
        return None
    s = open(p, encoding='utf-8', errors='replace').read()
    m = re.search(r'\\title\{(.+?)\}\s*\n\s*\\author', s, re.S)
    if not m:
        return None
    t = re.sub(r'\\\\|\s+', ' ', m.group(1))
    t = re.sub(r'\\[a-zA-Z]+\{?|\}', '', t)
    return re.sub(r'\s+', ' ', t).strip()


def main():
    papers = []
    for num, stem in ORDER:
        t = title_of(stem)
        if not t:
            print(f'  [WARN] no title for {stem}, skipped')
            continue
        pdf = f'corpus/{stem}.pdf'
        if not os.path.exists(os.path.join(ROOT, pdf)):
            print(f'  [WARN] no PDF for {stem}, listed without a link')
            papers.append((num, t, None))
            continue
        papers.append((num, t, f'{CDN}/{pdf}'))

    rows = []
    for num, t, url in papers:
        head, _, tail = t.partition(':')
        sub = f'<span class="sub">{tail.strip()}</span>' if tail.strip() else ''
        link = f'<a href="{url}">PDF</a>' if url else '<span class="nolink">—</span>'
        rows.append(
            f'    <li><span class="pn">{num}</span>'
            f'<span class="ti"><b>{head.strip()}</b>{sub}</span>{link}</li>')
    paper_list = '\n'.join(rows)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cosmological Relativity — the live edition</title>
<style>
  :root {{ --ink:#1c2733; --faint:#8b98a6; --line:#e2e8ee; --pole:#b5462a; --bg:#fbfcfd; }}
  * {{ box-sizing:border-box }}
  body {{ margin:0; background:var(--bg); color:var(--ink);
         font:16px/1.6 Georgia,'Iowan Old Style',serif; }}
  .wrap {{ max-width:52rem; margin:0 auto; padding:3rem 1.25rem 5rem; }}
  h1 {{ font-size:1.9rem; line-height:1.25; margin:0 0 .4rem; font-weight:600; }}
  h2 {{ font-size:1.15rem; margin:2.8rem 0 .3rem; font-weight:600;
        letter-spacing:.01em; }}
  .lede {{ color:#4a5765; margin:0 0 .2rem; }}
  .note {{ color:var(--faint); font-size:.86rem; }}
  ul.papers {{ list-style:none; padding:0; margin:1rem 0 0; }}
  ul.papers li {{ display:flex; align-items:baseline; gap:.7rem;
                  padding:.5rem 0; border-bottom:1px solid var(--line); }}
  .pn {{ flex:0 0 2.4rem; color:var(--pole); font-weight:600; font-size:.9rem; }}
  .ti {{ flex:1 1 auto; }}
  .ti .sub {{ display:block; color:var(--faint); font-size:.88rem; }}
  ul.papers a {{ flex:0 0 auto; color:var(--pole); text-decoration:none;
                 font-size:.82rem; letter-spacing:.06em; }}
  ul.papers a:hover {{ text-decoration:underline; }}
  .nolink {{ color:var(--line); }}
  #frontier {{ margin-top:1rem; }}
  .row {{ padding:.7rem 0 .8rem; border-bottom:1px solid var(--line); }}
  .row .id {{ color:var(--pole); font-weight:600; font-size:.85rem;
              margin-right:.5rem; }}
  .row .what {{ font-weight:600; }}
  .row .disc {{ display:block; color:#4a5765; font-size:.92rem; margin-top:.2rem; }}
  .status {{ color:var(--faint); font-size:.86rem; }}
  footer {{ margin-top:3.5rem; padding-top:1rem; border-top:1px solid var(--line);
            color:var(--faint); font-size:.84rem; }}
  a {{ color:var(--pole); }}
</style>
</head>
<body>
<div class="wrap">

<h1>Cosmological Relativity</h1>
<p class="lede">The live edition. Every paper below is served from the repository
itself, so what you open is what the work currently is — not a copy taken on a
date.</p>
<p class="note">For a citable, frozen version, use a tagged release rather than
this page.</p>

<h2>The papers</h2>
<ul class="papers">
{paper_list}
</ul>

<h2>The open edge</h2>
<p class="lede">This is not a summary written for the page. It is fetched from the
programme's own frontier, which is generated from its register of open problems,
and it changes when the work does.</p>
<div id="frontier"><p class="status">Fetching the current frontier…</p></div>

<footer>
Source: <a href="https://github.com/daryljanzen/shadow-of-existence">the
repository</a>. Papers via jsDelivr; the frontier read live at page load.
</footer>

</div>
<script>
(async function () {{
  const el = document.getElementById('frontier');
  const urls = ['{CDN}/THE_FRONTIER.md', '{RAW}/THE_FRONTIER.md'];
  let text = null;
  for (const u of urls) {{
    try {{
      const r = await fetch(u, {{cache: 'no-cache'}});
      if (r.ok) {{ text = await r.text(); break; }}
    }} catch (e) {{ /* try the next source */ }}
  }}
  if (text === null) {{
    el.innerHTML = '<p class="status">The frontier could not be reached just ' +
      'now. It lives at <a href="{RAW}/THE_FRONTIER.md">THE_FRONTIER.md</a>.</p>';
    return;
  }}
  // Rows are markdown table lines: | **PO-n** | what | ... | discharge |
  const rows = [];
  for (const line of text.split('\\n')) {{
    if (!line.startsWith('|')) continue;
    const c = line.split('|').map(s => s.trim());
    if (c.length < 4) continue;
    const id = (c[1].match(/PO-\\d+/) || [])[0];
    if (!id) continue;
    if (c[1].includes('~~')) continue;          // struck
    // c[2] is the question; c[9] is the row's own note, which carries the
    // discharge condition.  Indexed by position rather than from the end so a
    // trailing column added later cannot silently shift what is read.
    rows.push({{id: id, what: c[2] || '', disc: c[9] || ''}});
  }}
  if (!rows.length) {{
    el.innerHTML = '<p class="status">Fetched the frontier but read no open ' +
      'rows from it — the format may have moved. ' +
      '<a href="{RAW}/THE_FRONTIER.md">Read it directly.</a></p>';
    return;
  }}
  const clean = s => s.replace(/\\*\\*/g, '').replace(/`/g, '')
                      .replace(/</g, '&lt;').trim();
  const n = rows.length;
  let html = '<p class="status">' + n + ' open ' +
             (n === 1 ? 'question' : 'questions') + ', read from the register.</p>';
  for (const r of rows) {{
    const d = clean(r.disc);
    html += '<div class="row"><span class="id">' + r.id + '</span>' +
            '<span class="what">' + clean(r.what) + '</span>' +
            (d && d.length > 3 ? '<span class="disc">' + d.slice(0, 400) +
             '</span>' : '') + '</div>';
  }}
  el.innerHTML = html;
}})();
</script>
</body>
</html>
"""
    with open(OUT, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print(f'  live_edition.html written: {len(papers)} papers listed, '
          f'frontier fetched at read time (not embedded).')


if __name__ == '__main__':
    main()
