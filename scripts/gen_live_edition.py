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

# P-number -> tex stem, in the corpus's own numbering.  The geometric core is
# P17 and sits seventeenth; the older `p0` tag put it first and is deprecated.
ORDER = [
    ('P1', 'BH_causality_v2'),
    ('P2', 'janzen_circle_v3'), ('P3', 'SdS-slicing-curve_v2'),
    ('P4', 'modern_parallax'), ('P5', 'groupoid_paper'),
    ('P6', 'shadow_of_existence'), ('P7', 'CR_framework'),
    ('P8', 'slicing_operator'), ('P9', 'range_paper'),
    ('P10', 'canonical_time'), ('P11', 'dynamics_paper'),
    ('P12', 'algebroid_paper'), ('P13', 'boundary_paper'),
    ('P14', 'matter_sector_paper'), ('P15', 'CR_cosmology'),
    ('P16', 'cosmogenesis_paper'), ('P17', 'geometric_core_paper'),
    ('P18', 'CR_synthesis'),
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



def detex(t):
    """LaTeX fragment -> readable HTML. Emphasis and bold are kept because the
    corpus uses them to carry weight; everything else is stripped."""
    t = re.sub(r'(?m)^\s*%.*$', '', t)
    t = re.sub(r'\\(?:label|rcpt|ldg|cite|citep|footnote)\{[^}]*\}', '', t)
    t = re.sub(r'\\(?:emph|textit)\{([^{}]*)\}', r'<em>\1</em>', t)
    t = re.sub(r'\\(?:textbf|strong)\{([^{}]*)\}', r'<strong>\1</strong>', t)
    t = re.sub(r'\$([^$]*)\$', r'<code>\1</code>', t)
    t = re.sub(r'\\[a-zA-Z]+\*?\s*', ' ', t)
    t = t.replace('---', '\u2014').replace('--', '\u2013')
    t = re.sub(r'[{}]', '', t).replace('~', ' ')
    t = re.sub(r'[ \t]+', ' ', t)
    paras = [x.strip() for x in re.split(r'\n\s*\n', t) if x.strip()]
    return paras


def abstract_of(stem, max_paras=3, cap=1400):
    """The abstract's opening, not the whole thing: several run past ten
    thousand characters, which is a paper rather than a preview."""
    fp = os.path.join(ROOT, 'corpus', stem + '.tex')
    if not os.path.exists(fp):
        return None, False
    s = open(fp, encoding='utf-8', errors='replace').read()
    m = re.search(r'\\begin\{abstract\}(.+?)\\end\{abstract\}', s, re.S)
    if not m:
        return None, False
    paras = detex(m.group(1))
    if not paras:
        return None, False
    kept, total, truncated = [], 0, False
    for para in paras:
        if kept and (len(kept) >= max_paras or total + len(para) > cap):
            truncated = True
            break
        kept.append(para)
        total += len(para)
    if len(kept) < len(paras):
        truncated = True
    return kept, truncated


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
            papers.append((num, t, None, stem))
            continue
        papers.append((num, t, f'{CDN}/{pdf}', stem))

    rows, n_abs = [], 0
    for num, t, url, stem in papers:
        head, _, tail = t.partition(':')
        sub = f'<span class="sub">{tail.strip()}</span>' if tail.strip() else ''
        link = f'<a href="{url}">PDF</a>' if url else '<span class="nolink">—</span>'
        paras, cut = abstract_of(stem)
        if paras:
            n_abs += 1
            body = ''.join(f'<p>{x}</p>' for x in paras)
            if cut:
                body += ('<p class="more">The abstract continues in the paper '
                         f'itself. <a href="{url}">Open the PDF.</a></p>'
                         if url else '<p class="more">The abstract continues in '
                                     'the paper itself.</p>')
            rows.append(
                f'    <li><details><summary><span class="pn">{num}</span>'
                f'<span class="ti"><b>{head.strip()}</b>{sub}</span></summary>'
                f'<div class="abs">{body}</div></details>{link}</li>')
        else:
            rows.append(
                f'    <li><span class="pn">{num}</span>'
                f'<span class="ti"><b>{head.strip()}</b>{sub}</span>{link}</li>')
    paper_list = '\n'.join(rows)

    html = rf"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Shadow of Existence — the live edition</title>
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
  details {{ border-bottom:1px solid var(--line); }}
  summary {{ cursor:pointer; padding:.55rem 0; display:flex; gap:.7rem;
             align-items:baseline; list-style:none; }}
  summary::-webkit-details-marker {{ display:none }}
  summary::before {{ content:'\203A'; color:var(--faint); flex:0 0 .6rem;
                     transition:transform .15s; }}
  details[open] > summary::before {{ transform:rotate(90deg); }}
  summary .sub {{ display:block; color:var(--faint); font-size:.88rem; }}
  .abs {{ padding:.2rem 0 1.1rem 1.3rem; font-size:.95rem; }}
  .abs p {{ margin:0 0 .7rem; }}
  .intro {{ font-size:1rem; }}
  .intro p {{ margin:0 0 1rem; }}
  .intro h3 {{ font-size:1.08rem; margin:2rem 0 .6rem; font-weight:600;
               color:var(--ink); }}
  .intro figure {{ margin:1.4rem 0; }}
  .intro figcaption {{ color:var(--faint); font-size:.86rem; margin-top:.5rem;
                       line-height:1.5; }}
  .intro .more {{ color:var(--faint); font-size:.86rem; font-style:italic; }}
  .intro code {{ font-size:.9em; background:#f1f4f7; padding:.05em .3em;
                 border-radius:3px; }}
  .abs .more {{ color:var(--faint); font-size:.88rem; }}
  .intro h2, .intro h3 {{ font-size:1rem; margin:1.2rem 0 .3rem; }}
  .matrix table {{ border-collapse:collapse; font-size:.72rem; }}
  .matrix td, .matrix th {{ border:1px solid var(--line); padding:.15rem .3rem;
                            text-align:center; }}
  .matrix {{ overflow-x:auto; }}
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

<h1>The Shadow of Existence</h1>
<p class="lede">The live edition. Every paper below is served from the repository
itself, so what you open is what the work currently is — not a copy taken on a
date.</p>
<p class="note">For a citable, frozen version, use a tagged release rather than
this page.</p>

<h2>Introduction</h2>
<p class="lede">What the programme is, the eighteen papers and how they depend on
one another, where to come in, and at what weight each claim is held.</p>
<div id="introbox"><div class="intro">
  <p class="status">Fetching the introduction…</p>
</div></div>

<h2>The papers</h2>
<p class="note">Click a title for its abstract; the link opens the paper.</p>
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

// The introduction and the matrix are fetched for the same reason the frontier
// is: a copy pasted into this page is a second home, and second homes go stale.
(async function () {{
  const box = document.querySelector('#introbox .intro');
  try {{
    const r = await fetch('{CDN}/INTRODUCTION.md', {{cache: 'no-cache'}});
    if (!r.ok) throw 0;
    const md = await r.text();
    const esc = t => t.replace(/&/g, '&amp;').replace(/</g, '&lt;');
    const inline = t => esc(t)
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.+?)\*/g, '<em>$1</em>')
      .replace(/`(.+?)`/g, '<code>$1</code>');
    let html = '', para = [], inFig = false;
    const flush = () => {{ if (para.length) {{
      html += '<p>' + inline(para.join(' ')) + '</p>'; para = []; }} }};
    for (const line of md.split('\n')) {{
      // The introduction carries its own <figure> for the matrix.  Replace that
      // block with a slot and drop the live table into it, so the matrix sits
      // where the text already explains it rather than beside the text.
      if (/^<figure>/.test(line.trim())) {{
        flush(); inFig = true;
        html += '<figure class="matrix"><div id="matrixslot">' +
                '<p class="status">Fetching the matrix\u2026</p></div>';
        continue;
      }}
      if (inFig) {{
        const cap = line.match(/<figcaption>([\s\S]*)/);
        if (cap) html += '<figcaption>' + cap[1].replace(/<\/figcaption>.*/, '') +
                         '</figcaption>';
        if (/<\/figure>/.test(line)) {{ html += '</figure>'; inFig = false; }}
        continue;
      }}
      if (/^#{{1,3}} /.test(line)) {{
        flush();
        html += '<h3>' + inline(line.replace(/^#+ /, '')) + '</h3>';
      }} else if (!line.trim()) {{ flush(); }}
      else {{ para.push(line.trim()); }}
      if (html.length > 40000) break;
    }}
    flush();
    html += '<p class="more">The introduction as the repository currently ' +
            'holds it \u2014 it changes when the work does.</p>';
    box.innerHTML = html;
    placeMatrix();
  }} catch (e) {{
    box.innerHTML = '<p class="status">The introduction could not be reached ' +
      'just now. <a href="{RAW}/INTRODUCTION.md">Its source is here.</a></p>';
  }}
}})();

// The matrix belongs INSIDE the introduction, at the figure the introduction
// already carries for it -- not as a sibling accordion.  It is fetched for the
// same reason everything else here is.
async function placeMatrix() {{
  const slot = document.getElementById('matrixslot');
  if (!slot) return;
  try {{
    const r = await fetch(
      '{CDN}/BOOK_INTRO_cosmiCave/assets/dependency_matrix.html',
      {{cache: 'no-cache'}});
    if (!r.ok) throw 0;
    const doc = new DOMParser().parseFromString(await r.text(), 'text/html');
    const tbl = doc.querySelector('table');
    if (!tbl) throw 0;
    slot.innerHTML = '';
    slot.appendChild(tbl);
  }} catch (e) {{
    slot.innerHTML = '<p class="status">The matrix is at ' +
      '<a href="{RAW}/BOOK_INTRO_cosmiCave/assets/dependency_matrix.html">' +
      'dependency_matrix.html</a>.</p>';
  }}
}}
</script>
</body>
</html>
"""
    with open(OUT, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print(f'  live_edition.html written: {len(papers)} papers listed, '
          f'{n_abs} with abstracts, frontier fetched at read time '
          f'(not embedded).')


if __name__ == '__main__':
    main()
