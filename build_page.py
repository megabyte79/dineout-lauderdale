"""Generate the Dine Out Lauderdale guide as one self-contained HTML file.

The page is a single template string: CSS, markup and JS inlined, with two
placeholders filled at build time:

    __PAYLOAD__    the full payload.json, re-serialized without whitespace
    __BUILDDATE__  today's date, for the freshness note in the footer

payload.json is the source of truth and recompute.py owns every derived field
on it. Run `python3 recompute.py --check` before building; this script only
renders, it never scores.

Output: dineout_guide.html (copy to index.html to publish).
"""
import json
from datetime import date

entries = json.load(open('payload.json'))
# Compact separators shave ~6% off the shipped page; the file on disk is untouched.
PAYLOAD = json.dumps(entries, ensure_ascii=False, separators=(',', ':'))
BUILD_DATE = date.today().strftime('%B %d, %Y').replace(' 0', ' ')

HTML = r'''<!DOCTYPE html>
<html lang="en" data-theme="light"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='46' fill='%23FFD56B'/%3E%3Cg stroke='%231E67CD' stroke-width='7.5' stroke-linecap='round' fill='none'%3E%3Cpath d='M18 56 q8 -9 16 0 t16 0 t16 0 t16 0'/%3E%3Cpath d='M22 70 q8 -9 16 0 t16 0 t16 0'/%3E%3Cpath d='M30 84 q8 -9 16 0 t16 0'/%3E%3C/g%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,700;12..96,75..100,800&family=Nata+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<title>Dine Out Lauderdale 2026 — decoded</title>
<meta name="description" content="Every Dine Out Lauderdale fixed-price menu, with each dish priced against the restaurant's own everyday menu, so you can tell which deals actually save you money.">
<meta property="og:type" content="website">
<meta property="og:title" content="Dine Out Lauderdale 2026 — decoded">
<meta property="og:description" content="Every fixed-price menu priced dish by dish against the restaurant's regular menu. Which deals are real, and what to order.">
<meta property="og:url" content="https://megabyte79.github.io/dineout-lauderdale/">
<meta property="og:image" content="https://megabyte79.github.io/dineout-lauderdale/og-card.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://megabyte79.github.io/dineout-lauderdale/og-card.png">
<meta name="twitter:title" content="Dine Out Lauderdale 2026 — decoded">
<meta name="twitter:description" content="Every fixed-price menu priced dish by dish against the restaurant's regular menu.">
<script>try{if(localStorage.getItem('dol-theme')==='dark')document.documentElement.setAttribute('data-theme','dark')}catch(e){}</script>
<style>
:root{
  color-scheme: light;
  --surface-1:#ffffff; --plane:#FFFFFF; --card:#ffffff;
  --ink:#142235; --ink-2:#4B5568; --muted:#8A93A6;
  --grid:#E3E8F0; --baseline:#C7CFDD; --ring:rgba(20,34,53,0.10);
  --good:#12875A; --warning:#F2A900; --serious:#F2884B; --critical:#E0432B;
  --accent:#1E67CD; --accent-soft:#DCEBFF;
  --success-text:#0E6B46; --gold:#FFD56B; --navy:#1A222D;
  --sky:#18A3DE; --teal:#4BC3C9; --orange:#FE9B0C; --coral:#FF5027; --slate:#2D3848;
  --inset:#F2F7FD; --cobalt:#1E67CD;
  --display:"Bricolage Grotesque",system-ui,sans-serif;
}
:root[data-theme="dark"]{
  color-scheme: dark;
  --surface-1:#141B24; --plane:#0C1117; --card:#141B24;
  --ink:#F3F6FA; --ink-2:#B9C2D0; --muted:#8892A0;
  --grid:#253040; --baseline:#364256; --ring:rgba(255,255,255,0.10);
  --accent:#5B9CF2; --accent-soft:#1D3556; --success-text:#2FBE85;
  --good:#1FA971; --warning:#F2A900; --serious:#F2884B; --critical:#FF6B52;
  --gold:#FFD56B; --navy:#0C1117;
  --sky:#4FC3F0; --teal:#5BD4DA; --orange:#FFB03A; --coral:#FF7057; --slate:#DCE4F0;
  --inset:#1B2634; --cobalt:#173A6E;
}
*{box-sizing:border-box}
body{margin:0;background:var(--plane);color:var(--ink);
  font-family:"Nata Sans",system-ui,-apple-system,"Segoe UI",sans-serif;font-size:15px;line-height:1.5}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px 80px}
.topbar{background:var(--slate);color:#fff;padding:9px 0}
:root[data-theme="dark"] .topbar{background:#0A0E14}
.topbar .wrap{padding:0 20px;display:flex;align-items:center;gap:8px;font-size:13px;letter-spacing:.02em}
.topbar b{color:var(--gold);font-weight:750}
header{padding:30px 0 0;position:relative}
h1{font-family:var(--display);font-stretch:80%;text-transform:uppercase;
  font-size:44px;margin:0 0 8px;letter-spacing:.005em;font-weight:800;line-height:1.02;
  display:flex;align-items:baseline;flex-wrap:wrap;gap:0 12px}
h1 .ld{color:var(--accent)} h1 .lg{color:var(--gold)}
h1 .sun{width:.82em;height:.82em;transform:translateY(.115em);margin:0 .02em}
h1 .ltag{font-family:var(--display);font-stretch:80%;font-weight:700;font-size:19px;color:var(--slate);letter-spacing:.04em}
h1 .ltag .accent{color:var(--accent)}
.sub{color:var(--ink-2);font-size:14px;max-width:70ch;margin:0 0 4px}
.themebtn{position:absolute;top:30px;right:20px;background:var(--card);border:2px solid var(--teal);
  color:var(--ink-2);border-radius:999px;padding:6px 14px;cursor:pointer;font-size:13px;font-weight:600;font-family:inherit}
.wave{height:34px;margin:22px 0 0;background:var(--gold);
  -webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 34' preserveAspectRatio='none'%3E%3Cpath d='M0 22 C 90 2 210 2 300 16 C 390 30 510 34 600 20 C 690 6 810 2 900 14 C 990 26 1110 30 1200 16 L 1200 34 L 0 34 Z'/%3E%3C/svg%3E") 0 0/100% 100%;
          mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 34' preserveAspectRatio='none'%3E%3Cpath d='M0 22 C 90 2 210 2 300 16 C 390 30 510 34 600 20 C 690 6 810 2 900 14 C 990 26 1110 30 1200 16 L 1200 34 L 0 34 Z'/%3E%3C/svg%3E") 0 0/100% 100%}
.lede{background:var(--card);border:1px solid var(--ring);border-left:4px solid var(--accent);
  border-radius:10px;padding:14px 16px;margin:20px 0 0;font-size:14px;color:var(--ink-2);max-width:80ch}
.lede b{color:var(--ink)}
.controls{position:sticky;top:0;z-index:20;background:var(--cobalt);
  padding:14px 16px 12px;margin:0 -16px 22px;border-radius:16px;box-shadow:0 3px 10px rgba(20,34,53,.14)}
@media(max-width:640px){.controls{margin:0 -8px 18px;padding:12px 10px 10px}}
.crow{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
input[type=search],select{font-family:inherit;font-size:13px;font-weight:600;padding:8px 14px;border-radius:999px;
  border:2px solid var(--teal);background:var(--card);color:var(--ink)}
input[type=search]{min-width:210px}
.count{font-size:13px;font-weight:600;color:rgba(255,255,255,.92);margin-left:auto}
.ms{position:relative}
.msbtn{font-family:inherit;font-size:13px;font-weight:600;padding:8px 14px;border-radius:999px;cursor:pointer;
  border:2px solid var(--teal);background:var(--card);color:var(--ink);display:inline-flex;
  align-items:center;gap:7px;white-space:nowrap}
.msbtn[aria-expanded=true]{border-color:var(--gold)}
.msbtn.on{background:var(--accent-soft);border-color:var(--accent);color:var(--ink)}
.mscar{font-size:9px;color:var(--muted)}
.mspanel{position:absolute;top:calc(100% + 5px);left:0;z-index:40;min-width:230px;max-height:320px;
  overflow-y:auto;background:var(--card);border:1px solid var(--ring);border-radius:10px;
  box-shadow:0 8px 26px rgba(20,34,53,.16);padding:7px}
.msact{display:flex;gap:6px;padding:2px 4px 7px;border-bottom:1px solid var(--grid);margin-bottom:5px}
.msact button{flex:1;font-family:inherit;font-size:11.5px;padding:5px 8px;border-radius:999px;cursor:pointer;
  border:1px solid var(--ring);background:var(--inset);color:var(--ink-2)}
.msact button:hover{color:var(--ink);border-color:var(--accent)}
.msopt{display:flex;align-items:center;gap:8px;padding:6px 7px;border-radius:6px;
  font-size:13px;color:var(--ink);cursor:pointer;line-height:1.3}
.msopt:hover{background:var(--inset)}
.msopt input{margin:0;flex:0 0 auto;accent-color:var(--accent)}
.mscount{margin-left:auto;font-size:11px;color:var(--muted);font-variant-numeric:tabular-nums}
.mshint{font-size:11px;color:var(--muted);padding:5px 7px 2px;line-height:1.35}
@media(max-width:600px){.ms{position:static}.mspanel{left:14px;right:14px;min-width:0}}
.grid{display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(430px,1fr))}
@media(max-width:920px){.grid{grid-template-columns:1fr}}
.card{background:var(--card);border:1px solid var(--ring);border-radius:20px;padding:18px 18px 14px;
  display:flex;flex-direction:column;gap:11px;box-shadow:0 3px 6px rgba(0,0,0,.10);min-width:0;
  content-visibility:auto;contain-intrinsic-size:auto 620px}
.chead{display:flex;justify-content:space-between;gap:12px;align-items:flex-start}
.rname{font-size:16.5px;font-weight:800;letter-spacing:.015em;text-transform:uppercase;margin:0;line-height:1.3;color:var(--slate)}
.catpill{display:inline-block;font-size:10.5px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;
  color:var(--navy);background:var(--gold);border-radius:999px;padding:2px 8px;margin:4px 6px 0 0}
.cuisine{font-size:12.5px;color:var(--accent);font-weight:600;margin-top:3px}
.loc{font-size:12.5px;color:var(--muted);margin-top:2px}
a.ext{color:var(--accent);text-decoration:none;font-weight:600}
a.ext:hover{text-decoration:underline}
a.addr{color:var(--muted);text-decoration:none;font-weight:400}
a.addr:hover{color:var(--accent);text-decoration:underline}
.hours{font-size:12px;color:var(--ink-2);margin-top:3px;display:flex;gap:5px;align-items:baseline}
.daystrip{display:flex;gap:3px;margin-top:5px;align-items:center}
.dchip{width:19px;height:18px;border-radius:4px;font-size:10px;font-weight:700;
  display:flex;align-items:center;justify-content:center;background:var(--grid);color:var(--muted)}
.dchip.on{background:var(--accent);color:#fff}
.dnote{font-size:11px;color:var(--muted);margin-left:5px}
.hours .ic{color:var(--accent)}
.tier{flex:0 0 auto;text-align:right}
.tierp{font-family:var(--display);font-stretch:80%;font-size:27px;font-weight:800;letter-spacing:0;color:var(--accent)}
:root[data-theme="dark"] .tierp{color:var(--sky)}
.tierm{font-size:11.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}
.blurb{font-size:13.5px;color:var(--ink-2);margin:0}
.heads{font-size:12.5px;color:var(--ink-2);background:var(--inset);border-radius:7px;
  padding:8px 10px;border-left:3px solid var(--warning)}
.heads b{color:var(--ink)}
.vrow{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.verdict{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;font-weight:650;
  padding:4px 10px;border-radius:999px;border:1px solid transparent;width:fit-content}
.confchip{display:inline-flex;align-items:center;gap:5px;font-size:11.5px;color:var(--ink-2);
  padding:4px 9px;border-radius:999px;border:1px solid var(--ring);background:var(--inset)}
.v-safe{color:var(--success-text);background:rgba(18,135,90,.12);border-color:rgba(18,135,90,.35)}
.v-pick{color:var(--accent);background:rgba(30,103,205,.10);border-color:rgba(30,103,205,.32)}
.v-marginal{color:var(--ink-2);background:rgba(242,169,0,.14);border-color:rgba(242,169,0,.45)}
.v-skip{color:var(--critical);background:rgba(224,67,43,.10);border-color:rgba(224,67,43,.38)}
.v-even{color:var(--ink-2);background:var(--inset);border-color:var(--ring)}
.v-party{color:var(--ink-2);background:rgba(75,195,201,.14);border-color:rgba(75,195,201,.5)}
.v-nomenu{color:var(--muted);background:var(--inset);border-color:var(--ring)}
.pnote{font-size:12.5px;color:var(--ink-2);background:rgba(75,195,201,.10);border-radius:9px;
  padding:9px 11px;border-left:3px solid var(--teal);line-height:1.45}
.pnote b{color:var(--ink)}
.tabs{display:flex;gap:5px;background:var(--inset);border-radius:999px;padding:4px}
.tabbtn{flex:1;border:none;background:transparent;color:var(--ink-2);font-family:inherit;
  font-size:12.5px;font-weight:650;padding:7px 10px;border-radius:7px;cursor:pointer}
.tabbtn.active{background:var(--accent);color:#fff;box-shadow:0 1px 2px rgba(20,34,53,.12)}
:root[data-theme="dark"] .tabbtn.active{color:#fff}
.tabpane[hidden]{display:none}
.order{background:var(--inset);border-radius:14px;padding:12px 13px}
.oline{display:flex;gap:7px;align-items:baseline;font-size:13.5px;margin-bottom:4px}
.ocourse{flex:0 0 62px;color:var(--muted);font-size:11.5px;text-transform:uppercase;letter-spacing:.04em}
.odish{font-weight:600;color:var(--ink);min-width:0;overflow-wrap:anywhere}
.ogloss{font-size:12.5px;color:var(--ink-2);margin:1px 0 7px 69px;line-height:1.42}
.osrc{font-size:11px;color:var(--muted);margin:0 0 7px 69px;line-height:1.4;font-style:italic;overflow-wrap:anywhere}
.fullmenu{background:var(--inset);border-radius:14px;padding:12px 13px}
.course{margin-top:0}
.course+.course{margin-top:12px}
.chdr{font-size:11px;text-transform:uppercase;letter-spacing:.07em;color:var(--muted);
  font-weight:650;border-bottom:1px solid var(--grid);padding-bottom:4px;margin-bottom:7px}
.opt{display:flex;justify-content:space-between;gap:10px;align-items:baseline;padding:4px 0}
.optname{font-size:13.5px;min-width:0;overflow-wrap:anywhere}
.star{color:var(--warning);font-size:11px}
.optprice{font-size:13px;color:var(--ink-2);font-variant-numeric:tabular-nums;flex:0 0 auto}
.upg{display:inline-block;font-size:10.5px;font-weight:700;color:#8a5a00;background:#FFF0CC;
  border:1px solid #F2C94C;border-radius:999px;padding:1px 6px;margin-left:6px;white-space:nowrap}
:root[data-theme="dark"] .upg{color:#FFD98A;background:#3A2E10;border-color:#7A5F1E}
.portion{font-size:11px;color:var(--muted);line-height:1.4;font-style:italic}
.oportion{font-size:11px;color:var(--muted);margin:0 0 5px 69px;line-height:1.4;font-style:italic;overflow-wrap:anywhere}
.upgnote{font-size:12px;color:var(--ink-2);background:var(--inset);border-radius:9px;
  padding:7px 10px;margin-top:2px;line-height:1.45}
.upgnote b{color:var(--ink)}
.v-est{border-style:dashed !important}
:target.card{outline:3px solid var(--accent);outline-offset:3px}
.gl{font-size:12.5px;color:var(--ink-2);margin:2px 0 4px 0;line-height:1.42}
.src{font-size:11px;color:var(--muted);margin:-2px 0 4px 0;line-height:1.4;font-style:italic;overflow-wrap:anywhere}
.bar{margin-top:2px}
.barlab{display:flex;justify-content:space-between;font-size:12px;color:var(--ink-2);margin-bottom:5px}
.track{position:relative;height:12px;background:var(--grid);border-radius:4px;overflow:visible}
.fill{position:absolute;left:0;top:0;bottom:0;border-radius:4px}
.tick{position:absolute;top:-4px;bottom:-4px;width:2px;background:var(--navy);border-radius:1px}
:root[data-theme="dark"] .tick{background:var(--ink)}
.ticklab{position:absolute;top:14px;font-size:10.5px;color:var(--muted);transform:translateX(-50%);white-space:nowrap}
.ticklab.e0{left:0;transform:none}
.ticklab.e1{left:auto;right:0;transform:none}
.opt.pickable{cursor:pointer;border-radius:9px;padding:6px 8px;margin:0 -8px;
  border:1px solid transparent;transition:background .12s,border-color .12s}
.opt.pickable:hover{background:var(--card)}
.opt.pickable.on{background:rgba(30,103,205,.09);border-color:rgba(30,103,205,.35)}
.opt.pickable:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.mark{display:inline-block;width:13px;height:13px;border-radius:50%;border:2px solid var(--ring);
  margin-right:7px;vertical-align:-1px}
.opt.on .mark{border-color:var(--accent);
  background:radial-gradient(circle at 50% 50%,var(--accent) 0 3.5px,transparent 3.5px)}
.bhint{font-size:12px;color:var(--muted);margin:-2px 0 10px}
.bsum{margin-top:12px;padding-top:11px;border-top:1px solid var(--grid);font-size:13.5px;
  color:var(--ink-2);display:flex;justify-content:space-between;align-items:baseline;gap:10px;flex-wrap:wrap}
.bsum b{color:var(--ink);font-weight:700}
.bsum .up{color:var(--good)} .bsum .dn{color:var(--critical)}
.breset{background:none;border:none;color:var(--accent);font-family:inherit;font-size:12px;
  font-weight:650;cursor:pointer;padding:0;text-decoration:underline;white-space:nowrap}
.you{position:absolute;top:-6px;bottom:-6px;width:3px;background:var(--accent);border-radius:2px;
  box-shadow:0 0 0 2px var(--card)}
.savings{font-size:13.5px;color:var(--ink-2);margin:0 0 8px;line-height:1.4}
.savings b{font-weight:700}
.savings .up{color:var(--good)} .savings .dn{color:var(--critical)} .savings .ev{color:var(--ink)}
.barnote{font-size:12px;color:var(--ink-2);margin-top:20px}
.barnote b{color:var(--ink)}
.conf{font-size:11.5px;color:var(--muted);display:flex;align-items:center;gap:6px;margin-top:auto;padding-top:10px}
a.rep{margin-left:auto;color:var(--muted);text-decoration:none;font-weight:600}
a.rep:hover{color:var(--accent);text-decoration:underline}
.dot{width:7px;height:7px;border-radius:50%;flex:0 0 auto}
.d-verified{background:var(--good)} .d-mixed{background:var(--warning)} .d-estimated{background:var(--baseline)} .d-none{background:var(--muted)}
.empty{text-align:center;color:var(--muted);padding:60px 20px;font-size:14px}
footer{margin-top:44px;padding-top:20px;border-top:1px solid var(--grid);font-size:12.5px;color:var(--muted);max-width:80ch}
footer b{color:var(--ink-2)}
footer a{color:var(--accent)}
.legend{display:flex;gap:16px;flex-wrap:wrap;font-size:12px;color:var(--ink-2);margin-top:10px}
.legend span{display:inline-flex;align-items:center;gap:5px}
</style></head><body>
<div class="topbar"><div class="wrap"><b>DINE OUT</b> LAUDERDALE 2026 · Aug 1 – Sep 30 · unofficial value guide</div></div>
<div class="wrap">
<header>
  <button class="themebtn" id="tt">◐ Theme</button>
  <h1><span class="ld">DINE</span><svg class="sun" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="46" fill="var(--gold)"/><g stroke="var(--accent)" stroke-width="7.5" stroke-linecap="round" fill="none"><path d="M18 56 q8 -9 16 0 t16 0 t16 0 t16 0"/><path d="M22 70 q8 -9 16 0 t16 0 t16 0"/><path d="M30 84 q8 -9 16 0 t16 0"/></g></svg><span class="lg">UT</span> <span class="ltag">Lauderdale 2026 <span class="accent">/ decoded</span></span></h1>
  <p class="sub" id="subline">Every fixed-price menu priced dish by dish against the restaurant's own everyday menu, so you can tell which deals save you real money.</p>
</header>
<div class="wave"></div>
<div class="controls">
  <div class="crow">
    <input type="search" id="q" placeholder="Search restaurant or dish…" aria-label="Search">
    <div class="ms" id="category"></div>
    <div class="ms" id="city"></div>
    <select id="meal"><option value="">Lunch &amp; dinner</option><option>Lunch</option><option>Dinner</option><option>Lux</option></select>
    <select id="day">
      <option value="">Any day</option>
      <option value="we">Weekend (Sat or Sun)</option>
      <option value="5">Saturday</option>
      <option value="6">Sunday</option>
      <option value="0">Monday</option><option value="1">Tuesday</option>
      <option value="2">Wednesday</option><option value="3">Thursday</option>
      <option value="4">Friday</option>
    </select>
    <select id="price"><option value="">Any price</option><option>35</option><option>45</option><option>60</option><option>75</option></select>
    <select id="sort">
      <option value="pct">Best value (by %)</option>
      <option value="value">Biggest savings (by $)</option>
      <option value="tier">Cheapest first</option>
      <option value="verified">Verified prices first</option>
      <option value="name">A–Z</option>
      <option value="rand">Surprise me</option>
    </select>
    <span class="count" id="count"></span>
  </div>
</div>
<div class="grid" id="grid"></div>
<footer>
  <p><b>How to read this.</b> "Worth" is what the same dishes would cost à la carte at that restaurant, with portions adjusted — a 4-piece appetizer is priced against a 4-piece share of the regular 8-piece order, not the whole thing. All figures are before tax and tip. Paid add-ons (wine pairings, upcharges) are excluded; genuinely included drinks/sides are counted.</p>
  <p><b>"Order this"</b> is the highest-value pick in each course — usually the most expensive dish on the menu, which is the point. Switch to the <b>Full menu</b> tab on any card to see every option in every course with its own everyday price, and pick for yourself.</p>
  <p><b>Hours &amp; days.</b> The day strip (M T W T F S S) shows which days each special is served, read from the hours the restaurant published for that tier. Filtering by a day never hides a tier whose days weren't published — those are kept in the results and counted separately, since we can't rule them in or out. Always call ahead for a weekend booking.</p>
  <p><b>Freshness.</b> Prices last verified __BUILDDATE__. Menus change during the program; the full history of corrections is in the <a href="https://github.com/megabyte79/dineout-lauderdale/commits/main" target="_blank" rel="noopener">changelog</a>.</p>
  <p><b>Confidence.</b> A green dot means every price came off the restaurant's own current menu. Grey means the restaurant publishes no prices anywhere and the numbers are benchmarked estimates — real for ranking, not for arguing over. Menus captured from visitlauderdale.com in August 2026; restaurants change menus without notice.</p>
</footer>
</div>
<script>
const DATA = __PAYLOAD__;

/* ---------------------------------------------------- labels & helpers --- */
const ICON={safe:'✓',pick:'◆',marginal:'▵',even:'≈',skip:'✕',party:'⚑',nomenu:'—'};
const LABEL={safe:'Good however you order',pick:'Worth it only if you order right',marginal:'Barely worth it',even:'At best, you break even',skip:'Costs more than ordering normally',party:'Priced for a party, not per person',nomenu:'No menu published'};
// A confident-sounding verdict on nothing but benchmarked estimates overstates
// what we know, so the wording softens when no price came off a real menu.
const labelFor=d=>d.confidence==='estimated'&&(d.verdict==='safe'||d.verdict==='pick')
  ? 'Likely '+LABEL[d.verdict].charAt(0).toLowerCase()+LABEL[d.verdict].slice(1)
  : LABEL[d.verdict];
const CONFLAB={verified:'Prices verified on the restaurant’s own menu',mixed:'Some prices estimated',estimated:'Mostly estimated — restaurant publishes no prices',none:''};
const CONFSHORT={verified:'verified prices',mixed:'partly estimated',estimated:'mostly estimated',none:''};
const ORDER_PRIORITY=['Appetizer','Special','Side','Mid','Cocktail','Entree','Dessert'];
const CN={Appetizer:'Starter',Special:'Special',Side:'Side',Mid:'Pasta',Cocktail:'Cocktail',Entree:'Main',Dessert:'Dessert'};
const DAYL=['M','T','W','T','F','S','S'];
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const money=n=>'$'+n.toFixed(n%1?2:0);
const slug=s=>s.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'');
// A supplement costs extra on top of the base price, so only the difference counts.
const netOf=o=>o.price-(o.supp||0);
const upgChip=o=>o.supp?`<span class="upg">+${money(o.supp)}</span>`:'';
const portionOf=o=>{const p=(o&&o.portion||'').trim();return p&&!/^n\/a$/i.test(p)?p:null};
const nameOf=c=>CN[c]||c;
const courseOrder=cs=>cs.slice().sort((a,b)=>{
  const ia=ORDER_PRIORITY.indexOf(a), ib=ORDER_PRIORITY.indexOf(b);
  if(ia===-1&&ib===-1) return a.localeCompare(b);
  if(ia===-1) return 1; if(ib===-1) return -1;
  return ia-ib;
});
// drop long descriptive parentheticals — the gloss below carries them.
// keep short ones that state price, count or size (+$15, 4pc, 6oz, 1/2 rack).
const short=s=>String(s).replace(/\s*\([^)]{22,}\)/g, m =>
  /\$|\b\d+\s?(pc|piece|oz|lb)\b|1\/2/i.test(m) ? m : '').trim();
// human-readable price source, or null if the dish has no real citation on file
const srcOf=o=>{
  const s=(o&&o.src||'').trim();
  if(!s || /^n\/a$/i.test(s)) return null;
  return s;
};

/* ------------------------------------------------- filter state & hash --- */
const S={q:'',city:[],category:[],meal:'',price:'',day:'',sort:'pct'};
// Shareable filter state lives in the hash as #f&q=...&cat=a|b - anything else is a card anchor.
(function(){
  const h=location.hash;
  if(!h.startsWith('#f&')) return;
  const p=new URLSearchParams(h.slice(3));
  S.q=p.get('q')||'';
  S.category=(p.get('cat')||'').split('|').filter(Boolean);
  S.city=(p.get('area')||'').split('|').filter(Boolean);
  S.meal=p.get('meal')||''; S.price=p.get('price')||''; S.day=p.get('day')||'';
  S.sort=p.get('sort')||'pct';
})();
function updateHash(){
  const def=!S.q&&!S.category.length&&!S.city.length&&!S.meal&&!S.price&&S.day===''&&S.sort==='pct';
  if(def){ if(location.hash.startsWith('#f&')) history.replaceState(null,'',location.pathname+location.search); return; }
  const p=new URLSearchParams();
  if(S.q)p.set('q',S.q); if(S.category.length)p.set('cat',S.category.join('|'));
  if(S.city.length)p.set('area',S.city.join('|')); if(S.meal)p.set('meal',S.meal);
  if(S.price)p.set('price',S.price); if(S.day!=='')p.set('day',S.day);
  if(S.sort!=='pct')p.set('sort',S.sort);
  history.replaceState(null,'','#f&'+p.toString());
}
const cities=[...new Set(DATA.map(d=>d.city).filter(Boolean))].sort();
const cats=[...new Set(DATA.flatMap(d=>d.category||[]))].sort();

// Checkbox dropdown. Nothing ticked means "show everything", so the quickest way to
// exclude a couple of options is Select all, then untick the ones you don't want.
function multisel(hostId, allLabel, noun, values, onChange, counts, initial){
  counts=counts||{};
  const host=document.getElementById(hostId);
  host.innerHTML=
     `<button type="button" class="msbtn" aria-expanded="false"><span class="mslab">${esc(allLabel)}</span><span class="mscar">▼</span></button>`
    +`<div class="mspanel" hidden>`
    +  `<div class="msact"><button type="button" data-act="all">Select all</button><button type="button" data-act="none">Clear</button></div>`
    +  values.map(v=>`<label class="msopt"><input type="checkbox" value="${esc(v)}"><span>${esc(v)}</span><span class="mscount">${counts[v]||0}</span></label>`).join('')
    +  `<div class="mshint">Tick to narrow. To exclude a few, hit Select all then untick those.</div>`
    +`</div>`;
  const btn=host.querySelector('.msbtn'), panel=host.querySelector('.mspanel'),
        lab=host.querySelector('.mslab'), boxes=[...host.querySelectorAll('input')];
  const sync=()=>{
    const sel=boxes.filter(b=>b.checked).map(b=>b.value);
    lab.textContent = sel.length===0 ? allLabel
                    : sel.length===1 ? sel[0]
                    : sel.length===values.length ? allLabel
                    : sel.length+' '+noun;
    btn.classList.toggle('on', sel.length>0 && sel.length<values.length);
    onChange(sel.length===values.length?[]:sel);
  };
  btn.addEventListener('click',()=>{
    const open=panel.hidden;
    document.querySelectorAll('.mspanel').forEach(p=>{p.hidden=true});
    document.querySelectorAll('.msbtn').forEach(b=>b.setAttribute('aria-expanded','false'));
    panel.hidden=!open; btn.setAttribute('aria-expanded',String(open));
  });
  panel.addEventListener('click',e=>{
    const act=e.target.closest('button[data-act]');
    if(act){boxes.forEach(b=>{b.checked=act.dataset.act==='all'});sync()}
  });
  boxes.forEach(b=>b.addEventListener('change',sync));
  if(initial&&initial.length){
    // restore checkbox state without firing onChange: S already holds these
    // values (parsed from the hash) and render() has not been defined yet.
    boxes.forEach(b=>{b.checked=initial.includes(b.value)});
    lab.textContent = initial.length===1 ? initial[0]
                    : initial.length===values.length ? allLabel
                    : initial.length+' '+noun;
    btn.classList.toggle('on', initial.length>0 && initial.length<values.length);
  }
  return host;
}
const scored=DATA.filter(d=>d.verdict!=='nomenu');
const catCounts={},cityCounts={};
scored.forEach(d=>{(d.category||[]).forEach(c=>catCounts[c]=(catCounts[c]||0)+1);
  if(d.city)cityCounts[d.city]=(cityCounts[d.city]||0)+1});
multisel('category','All categories','categories',cats,v=>{S.category=v;render()},catCounts,S.category);
multisel('city','All areas','areas',cities,v=>{S.city=v;render()},cityCounts,S.city);
// reflect any hash-restored state into the plain controls
document.getElementById('q').value=S.q;
document.getElementById('meal').value=S.meal;
document.getElementById('price').value=S.price;
document.getElementById('day').value=S.day;
document.getElementById('sort').value=S.sort;
document.addEventListener('click',e=>{
  if(e.target.closest('.ms'))return;
  document.querySelectorAll('.mspanel').forEach(p=>{p.hidden=true});
  document.querySelectorAll('.msbtn').forEach(b=>b.setAttribute('aria-expanded','false'));
});

// What the bar is really saying, in dollars.
const savingsLine=d=>{
  const lo=d.worst-d.tier, hi=d.best-d.tier, a=n=>money(Math.abs(n)), z=n=>Math.abs(n)<0.005;
  // A per-person figure against a whole party's price is not a saving, it's a
  // category error. Say nothing rather than say something wrong.
  if(d.verdict==='party') return `<b class="ev">No honest figure to give</b> — see the note above.`;
  // Best case lands on the price. Quoting the gap to the cent ("you lose $0.11")
  // is false precision on a la carte prices that move between visits.
  if(d.verdict==='even') return lo>-0.005
    ? `<b class="ev">Break even either way</b> — every combination is worth about what you pay.`
    : `<b class="ev">At best you break even</b>, and you lose up to ${a(lo)} from there.`;
  if(d.best===d.worst){
    if(z(hi)) return `<b class="ev">Breaks even</b> — the food is worth what you pay.`;
    return hi>0 ? `<b class="up">You save ${a(hi)}</b> — fixed menu, no picks to make.`
                : `<b class="dn">You lose ${a(hi)}</b> — fixed menu, no picks to make.`;
  }
  if(z(lo)) return `<b class="up">You save up to ${a(hi)}</b> — at worst you break even.`;
  if(z(hi)) return `<b class="dn">You lose up to ${a(lo)}</b> — the best you can do is break even.`;
  if(lo>0) return `<b class="up">You save ${a(lo)} to ${a(hi)}</b> depending on your picks.`;
  if(hi<0) return `<b class="dn">You lose ${a(hi)} to ${a(lo)}</b> depending on your picks.`;
  return `<b class="up">Save up to ${a(hi)}</b> or <b class="dn">lose up to ${a(lo)}</b> — your picks decide.`;
};

const mapsUrl=d=>'https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(d.restaurant+' '+(d.address||'')+' '+(d.city||'')+' FL');

/* ---------------------------------------------------------------- builder ---
   The full-menu tab is interactive: tap a dish to swap it into your meal and
   the total, the savings line and the marker on the bar all move.

   Selections live in a Map outside the DOM because changing a filter rebuilds
   the entire grid, and losing a half-built meal to an unrelated click would be
   maddening. `touched` records whether the reader has actually chosen anything,
   so an untouched card keeps showing the honest best-to-worst range instead of
   quietly presenting our own recommendation as if it were their choice. */
const SEL=new Map(), TOUCHED=new Set(), DBY=new Map();
// The tier is part of the identity: six restaurants run two tiers of the same
// meal (Le Bistro has a $45 and a $60 dinner), and without it their cards
// shared a DOM id and a selection slot, so building a meal on one card
// silently used the other tier's menu and price.
const anchorOf=d=>slug(d.restaurant+'-'+d.meal+'-'+d.tier);

// Courses the builder walks. `pick` false means every item is served rather
// than chosen between, so they all count and none of them are clickable.
// Menus never change at runtime, so the built list is cached per entry:
// bTotal and toggleDish call this on every tap, and render() on every card.
const BC=new Map();
const bCourses=d=>{
  const a=anchorOf(d);
  let cs=BC.get(a);
  if(cs) return cs;
  cs=courseOrder(Object.keys(d.menu||{}).filter(c=>d.menu[c]&&d.menu[c].length))
    .map(c=>({key:c,label:nameOf(c),opts:d.menu[c],k:(d.choose&&d.choose[c])||1,pick:true}));
  const inc=d.included||[];
  if(inc.length) cs.push({key:'__inc',label:'Included',opts:inc,k:1,pick:d.included_mode==='choose'});
  BC.set(a,cs);
  return cs;
};
const defaultSel=d=>{
  const o={};
  for(const c of bCourses(d)) if(c.pick) o[c.key]=c.opts.slice(0,Math.min(c.k,c.opts.length)).map((_,i)=>i);
  return o;
};
const selOf=d=>{const a=anchorOf(d); if(!SEL.has(a)) SEL.set(a,defaultSel(d)); return SEL.get(a)};
const bTotal=(d,sel)=>{
  let t=0;
  for(const c of bCourses(d)){
    if(!c.pick){ t+=c.opts.reduce((s,o)=>s+netOf(o),0); continue; }
    for(const i of (sel[c.key]||[])) if(c.opts[i]) t+=netOf(c.opts[i]);
  }
  return Math.round(t*(d.covers||1)*100)/100;
};
// What the reader's own meal is worth against what they pay. Party-priced
// tiers get no figure here for the same reason they get no verdict.
const bLine=(d,total)=>{
  if(d.verdict==='party') return `Your picks come to <b>${money(total)}</b> per person. This tier is priced for a party, so that doesn't compare to the ${money(d.tier)}.`;
  const diff=total-d.tier;
  if(Math.abs(diff)<0.005) return `Your meal: <b>${money(total)}</b> — exactly what you pay.`;
  return diff>0
    ? `Your meal: <b>${money(total)}</b> — <b class="up">you save ${money(diff)}</b>.`
    : `Your meal: <b>${money(total)}</b> — <b class="dn">you pay ${money(-diff)} over</b>.`;
};

/* ------------------------------------------------------------- the card --- */
function card(d){
  const g=d.gloss||{};
  const catpills=(d.category||[]).map(c=>`<span class="catpill">${esc(c)}</span>`).join('');
  // Link straight to the restaurant's own site; the Dine Out listing adds nothing
  // we don't already show, and "Menu & details" competed with our own menu tab.
  const locLine=`<div class="loc">${d.site?`<a class="ext" href="${esc(d.site)}" target="_blank" rel="noopener">Website ↗</a> · `:''}<a class="addr" href="${esc(mapsUrl(d))}" target="_blank" rel="noopener" title="Open in Google Maps">${esc([d.city,d.address].filter(Boolean).join(' · ')||'Map')}</a></div>`;
  if(d.verdict==='nomenu'){
    return `<article class="card"><div class="chead"><div>
      <h2 class="rname">${esc(d.restaurant)}</h2>
      <div>${catpills}</div>
      <div class="cuisine">${esc(d.cuisine)}</div>
      ${locLine}</div></div>
      <p class="blurb">${esc(d.blurb)}</p>
      ${d.heads_up?`<div class="heads"><b>Heads up:</b> ${esc(d.heads_up)}</div>`:''}
      <div class="verdict v-nomenu">— No menu published</div></article>`;
  }
  const bcs=bCourses(d);
  // Most courses are choose-one, so picks is a one-item list; a "select two"
  // course carries both, and both need to show up in the recommendation.
  const orderLines=bcs.filter(c=>c.key!=='__inc').map(c=>{
    const ps=(d.picks&&d.picks[c.key])||(d.pick[c.key]?[d.pick[c.key]]:[]);
    return ps.map((p,i)=>{
      const gl=g[p.dish], sr=srcOf(p), po=portionOf(p);
      return `<div class="oline"><span class="ocourse">${i===0?esc(c.label):''}</span><span class="odish">${esc(short(p.dish))}${upgChip(p)}</span><span class="optprice">${money(p.price)}</span></div>`
        + (gl?`<div class="ogloss">${esc(gl)}</div>`:'')
        + (po?`<div class="oportion">Portion: ${esc(po)}</div>`:'')
        + (sr?`<div class="osrc">Source: ${esc(sr)}</div>`:'');
    }).join('');
  }).join('');
  // Items that come with the meal. When several are served, each gets its own
  // line and its own price like any course, rather than being crushed into one
  // plus-joined row where a five-course tasting reads as a single dish.
  const incAll=d.included||[];
  const incShow=incAll.length&&d.included_mode==='choose'
    ? [incAll.slice().sort((a,b)=>b.price-a.price)[0]]   // the one recompute counts
    : incAll;
  const inc=incShow.map((o,i)=>{
    const gl=g[o.dish], po=portionOf(o);
    return `<div class="oline"><span class="ocourse">${i===0?'Included':''}</span><span class="odish">${esc(short(o.dish))}</span><span class="optprice">${money(o.price)}</span></div>`
      +(gl?`<div class="ogloss">${esc(gl)}</div>`:'')
      +(po?`<div class="oportion">Portion: ${esc(po)}</div>`:'');
  }).join('');
  // range band on a 0..2x-tier scale, tick at what you pay
  const sc=v=>Math.max(0,Math.min(v/(d.tier*2),1))*100;
  const L=sc(d.worst), R=sc(d.best);
  const bandcol=d.verdict==='safe'?'var(--good)':d.verdict==='skip'?'var(--critical)'
    :(d.verdict==='even'||d.verdict==='party')?'var(--muted)':'var(--accent)';
  const sel=selOf(d);
  const menuHtml=bcs.map(c=>{
    const on=new Set(sel[c.key]||[]);
    const recN=c.pick?Math.min(c.k,c.opts.length):0;
    const opts=c.opts.map((o,i)=>{
      const gl=g[o.dish], sr=srcOf(o), po=portionOf(o);
      const chosen=c.pick?on.has(i):true;
      return `<div class="opt${c.pick?' pickable':''}${chosen?' on':''}"`
        +(c.pick?` data-c="${esc(c.key)}" data-i="${i}" role="button" tabindex="0" aria-pressed="${chosen}"`:'')
        +`><span class="optname">${c.pick?'<span class="mark"></span>':''}`
        +`${i<recN?'<span class="star" title="our recommendation">★</span> ':''}${esc(short(o.dish))}${upgChip(o)}</span>`
        +`<span class="optprice">${money(o.price)}</span></div>`
        +(gl?`<div class="gl">${esc(gl)}</div>`:'')
        +(po?`<div class="portion">Portion: ${esc(po)}</div>`:'')
        +(sr?`<div class="src">Source: ${esc(sr)}</div>`:'');
    }).join('');
    const hdr=c.pick?` — choose ${c.k===1?'one':c.k===2?'two':c.k}`:' — all served';
    return `<div class="course"><div class="chdr">${esc(c.label)}${hdr}</div>${opts}</div>`;
  }).join('');
  const anyPick=bcs.some(c=>c.pick&&c.opts.length>1);
  const hoursLine=d.hours?`<div class="hours"><span class="ic">🕒</span>${esc(d.hours)}</div>`:'';
  const dayStrip = d.days
    ? `<div class="daystrip" title="Days this special is served">${DAYL.map((L,i)=>`<span class="dchip ${d.days.includes(i)?'on':''}">${L}</span>`).join('')}</div>`
    : `<div class="daystrip" title="The restaurant did not publish serving days"><span class="dnote" style="margin-left:0">Serving days not published — call ahead</span></div>`;
  const anchor=anchorOf(d);
  DBY.set(anchor,d);
  return `<article class="card" id="${anchor}">
   <div class="chead">
     <div><h2 class="rname">${esc(d.restaurant)}</h2>
       <div>${catpills}</div>
       <div class="cuisine">${esc(d.cuisine)}</div>
       ${locLine}
       ${hoursLine}
       ${dayStrip}</div>
     <div class="tier"><div class="tierp">${money(d.tier)}</div><div class="tierm">${esc(d.meal)}${d.for2?' for 2':''}</div></div>
   </div>
   <div class="vrow">
     <span class="verdict v-${d.verdict}${d.confidence==='estimated'?' v-est':''}">${ICON[d.verdict]} ${esc(labelFor(d))}</span>
     <span class="confchip"><i class="dot d-${d.confidence}"></i>${esc(CONFSHORT[d.confidence])}</span>
   </div>
   <p class="blurb">${esc(d.blurb)}</p>
   ${d.party_note?`<div class="pnote"><b>${d.party_unclear?'We can’t score this one fairly:':'How this tier is priced:'}</b> ${esc(d.party_note)}</div>`:''}
   ${d.heads_up?`<div class="heads"><b>Heads up:</b> ${esc(d.heads_up)}</div>`:''}
   <div class="tabs">
     <button class="tabbtn active" data-tab="order">${d.verdict==='skip'?'If you go anyway, order this':'Order this'}</button>
     <button class="tabbtn" data-tab="full">${anyPick?'Build your meal':'Full menu &amp; prices'}</button>
   </div>
   <div class="tabpane" data-pane="order">
     <div class="order">${orderLines}${inc}</div>
   </div>
   <div class="tabpane" data-pane="full" hidden>
     <div class="fullmenu">
       ${anyPick?`<div class="bhint">Tap any dish to swap it into your meal. ★ is what we'd order.</div>`:''}
       ${menuHtml}
       <div class="bsum"><span class="bmine">${bLine(d,bTotal(d,sel))}</span>${anyPick?'<button class="breset" hidden>Reset to our pick</button>':''}</div>
     </div>
   </div>
   <div class="bar">
     <div class="barlab"><span>You pay <b style="color:var(--ink)">${money(d.tier)}</b>${d.for2?' (for two)':''}</span>
       <span>${d.best===d.worst
         ? `Food worth <b style="color:var(--ink)">${money(d.best)}</b>`
         : `Food worth <b style="color:var(--ink)">${money(d.worst)}–${money(d.best)}</b>`}</span></div>
     <div class="savings">${savingsLine(d)}</div>
     <div class="track">
       <div class="fill" style="left:${Math.min(L,100-Math.max(R-L,1.2)).toFixed(1)}%;width:${Math.max(R-L,1.2).toFixed(1)}%;background:${bandcol}"></div>
       <div class="tick" style="left:50%"></div>
       <div class="you" hidden title="Your picks"></div>
       <div class="ticklab e0">${money(0)}</div>
       <div class="ticklab" style="left:50%">what you pay</div>
       <div class="ticklab e1">${money(d.tier*2)}</div>
     </div>
     <div class="barnote">${d.verdict==='party'
        ? `The figures above are one person's share. Because this tier is quoted for a party, they don't line up with the <b>${money(d.tier)}</b> and we're not turning them into a verdict.`
        : d.verdict==='even'
        ? `Order as well as this menu allows and the food comes to <b>${money(d.best)}</b> against the <b>${money(d.tier)}</b> you pay — near enough to a tie that the gap is noise. Every other combination is worth less than that, down to <b>${money(d.worst)}</b>. Go for the food, not the discount.`
        : d.verdict==='safe'
        ? (d.best===d.worst
           ? `Fixed menu worth <b>${money(d.best)}</b> against the <b>${money(d.tier)}</b> you pay.`
           : `Every option on this menu beats the price — the whole range sits right of the line.`)
        : d.verdict==='skip'
        ? `Even the priciest combination comes to <b>${money(d.best)}</b>, under the <b>${money(d.tier)}</b> you pay.`
        : `Order as recommended and it's <b>${money(d.best)}</b>; pick the cheapest option each course and it falls to <b>${money(d.worst)}</b>, below what you paid.`}</div>
     ${(d.upgrades||[]).length?`<div class="upgnote"><b>Paid upgrade${d.upgrades.length>1?'s':''}:</b> ${d.upgrades.map(u=>esc(u.dish)+' (+'+money(u.supp)+')').join(', ')}. Not counted in the figures above.</div>`:''}
     ${d.courses_n>0&&d.courses_n<3?`<div class="barnote" style="margin-top:6px">Note: only ${d.courses_n} course${d.courses_n===1?'':'s'} ${d.courses_n===1?'was':'were'} published for this tier${d.courses_n===2?' — no dessert listed':''}.</div>`:''}
     ${d.best>d.tier*2?`<div class="barnote" style="margin-top:6px">The bar tops out at ${money(d.tier*2)} (twice what you pay); this menu runs past the end of it.</div>`:''}
   </div>
   <div class="conf"><i class="dot d-${d.confidence}"></i>${esc(CONFLAB[d.confidence])}<a class="rep" target="_blank" rel="noopener" href="report.html?r=${encodeURIComponent(d.restaurant)}&m=${encodeURIComponent(d.meal)}&t=${d.tier}">Spot an error? Report it</a></div>
  </article>`;
}

/* Repaint everything a selection change touches: the radio marks, the running
   total under the menu, the marker on the bar, and the savings line. The
   savings line only becomes personal once the reader has actually picked
   something; until then it keeps showing the honest best-to-worst range. */
function paintBuild(a){
  const d=DBY.get(a), cardEl=document.getElementById(a);
  if(!d||!cardEl) return;
  const sel=selOf(d), total=bTotal(d,sel), touched=TOUCHED.has(a);
  cardEl.querySelectorAll('.opt.pickable').forEach(el=>{
    const on=(sel[el.dataset.c]||[]).includes(+el.dataset.i);
    el.classList.toggle('on',on); el.setAttribute('aria-pressed',String(on));
  });
  const mine=cardEl.querySelector('.bmine');
  if(mine) mine.innerHTML=bLine(d,total);
  const btn=cardEl.querySelector('.breset');
  if(btn) btn.hidden=!touched;
  const you=cardEl.querySelector('.you');
  if(you){
    // A party-priced total has no meaningful position against the tier, so the
    // marker stays off rather than implying a comparison we just disclaimed.
    you.hidden=!touched||d.verdict==='party';
    you.style.left=(Math.max(0,Math.min(total/(d.tier*2),1))*100).toFixed(1)+'%';
  }
  const sav=cardEl.querySelector('.savings');
  if(sav) sav.innerHTML=(touched&&d.verdict!=='party')?bLine(d,total):savingsLine(d);
}

function toggleDish(cardEl,c,i){
  const a=cardEl.id, d=DBY.get(a);
  if(!d) return;
  const course=bCourses(d).find(x=>x.key===c);
  if(!course) return;
  const sel=selOf(d);
  let cur=(sel[c]||[]).slice();
  if(cur.includes(i)){
    if(cur.length<=1) return;          // a course always keeps one selection
    cur=cur.filter(x=>x!==i);
  }else{
    cur.push(i);
    while(cur.length>course.k) cur.shift();   // oldest choice drops out
  }
  sel[c]=cur; TOUCHED.add(a);
  paintBuild(a);
}

document.getElementById('grid').addEventListener('keydown', e=>{
  if(e.key!=='Enter'&&e.key!==' ') return;
  const opt=e.target.closest('.opt.pickable');
  if(!opt) return;
  e.preventDefault();
  toggleDish(opt.closest('.card'),opt.dataset.c,+opt.dataset.i);
});

document.getElementById('grid').addEventListener('click', e=>{
  const opt=e.target.closest('.opt.pickable');
  if(opt){ toggleDish(opt.closest('.card'),opt.dataset.c,+opt.dataset.i); return; }
  const rst=e.target.closest('.breset');
  if(rst){
    const cardEl=rst.closest('.card'), a=cardEl.id;
    SEL.set(a,defaultSel(DBY.get(a))); TOUCHED.delete(a); paintBuild(a);
    return;
  }
  const btn=e.target.closest('.tabbtn');
  if(!btn) return;
  // Tabs and panes both live inside the card, so scoping to it needs no ids.
  const cardEl=btn.closest('.card'), tab=btn.dataset.tab;
  cardEl.querySelectorAll('.tabbtn').forEach(b=>b.classList.toggle('active', b.dataset.tab===tab));
  cardEl.querySelectorAll('.tabpane').forEach(p=>{ p.hidden = p.dataset.pane!==tab; });
});

/* --------------------------------------------------------- sort & render --- */
const VRANK={safe:0,pick:1,marginal:2,even:3,party:4,skip:5,nomenu:6};
const CRANK={verified:0,mixed:1,estimated:2,none:3};
// "Surprise me" reshuffles each time it is picked, so the order is genuinely
// different rather than a fixed alternative ranking.
let shuf=new Map();
const reshuffle=()=>{shuf=new Map(DATA.map(d=>[d.restaurant+d.meal,Math.random()]))};
function updateLede(){
  const restCount=new Set(DATA.map(d=>d.restaurant)).size;
  const menuCount=DATA.filter(d=>d.verdict!=='nomenu').length;
  document.getElementById('subline').textContent=
    `${menuCount} fixed-price menus from ${restCount} restaurants, every dish priced against the restaurant's own everyday menu, so you can tell which deals save you real money and what to order when you go.`;
}
updateLede();
function render(){
  let r=DATA.filter(d=>{
    if(S.city.length&&!S.city.includes(d.city))return false;
    if(S.category.length&&!(d.category||[]).some(c=>S.category.includes(c)))return false;
    if(S.meal&&d.meal!==S.meal)return false;
    if(S.price&&String(d.tier)!==S.price)return false;
    if(S.day!==''&&d.days){
      const ok = S.day==='we' ? (d.days.includes(5)||d.days.includes(6)) : d.days.includes(+S.day);
      if(!ok)return false;
    }
    if(S.q){
      const hay=(d.restaurant+' '+d.cuisine+' '+d.blurb+' '+(d.category||[]).join(' ')+' '+Object.values(d.menu||{}).flat().map(o=>o.dish).join(' ')).toLowerCase();
      if(!hay.includes(S.q.toLowerCase()))return false;
    }
    return true;
  });
  const nomenu=r.filter(d=>d.verdict==='nomenu'), rest=r.filter(d=>d.verdict!=='nomenu');
  const surplus=x=>(x.best-x.tier)/x.tier;
  rest.sort((a,b)=>
      S.sort==='pct'      ? VRANK[a.verdict]-VRANK[b.verdict] || surplus(b)-surplus(a)
    : S.sort==='tier'     ? a.tier-b.tier || VRANK[a.verdict]-VRANK[b.verdict]
    : S.sort==='value'    ? (b.best-b.tier)-(a.best-a.tier)
    // trust first: fully verified, then partly, then benchmarked; best value inside each band
    : S.sort==='verified' ? CRANK[a.confidence]-CRANK[b.confidence] || surplus(b)-surplus(a)
    : S.sort==='rand'     ? (shuf.get(a.restaurant+a.meal)-shuf.get(b.restaurant+b.meal))
    : a.restaurant.localeCompare(b.restaurant));
  r=rest.concat(nomenu);
  document.getElementById('grid').innerHTML=r.length?r.map(card).join(''):'<div class="empty">Nothing matches those filters.</div>';
  const unl=rest.filter(d=>!d.days).length;
  document.getElementById('count').textContent=
    `${rest.length} menu${rest.length===1?'':'s'}` + (S.day!==''&&unl?` · incl. ${unl} with unlisted days`:'');
  // A filter change rebuilds every card from scratch, which resets the parts of
  // a built meal that live outside the entry: the personalised savings line, the
  // marker, the reset button. Re-apply them for anything the reader has touched.
  TOUCHED.forEach(a=>{ if(document.getElementById(a)) paintBuild(a); });
  updateHash();
}
const bind=(id,k)=>document.getElementById(id).addEventListener('input',e=>{S[k]=e.target.value;render()});
bind('meal','meal');bind('price','price');bind('day','day');bind('sort','sort');
// Search rebuilds all 240 cards, so it waits for a pause in typing rather than
// re-rendering on every keystroke. The selects stay immediate.
let qTimer=null;
document.getElementById('q').addEventListener('input',e=>{
  clearTimeout(qTimer);
  qTimer=setTimeout(()=>{S.q=e.target.value;render()},120);
});
document.getElementById('sort').addEventListener('change',e=>{if(e.target.value==='rand'){reshuffle();render()}});
// Light is the default for everyone. Dark is opt-in and remembered.
const themeBtn=document.getElementById('tt');
const applyTheme=t=>{
  document.documentElement.setAttribute('data-theme',t);
  themeBtn.setAttribute('aria-pressed',String(t==='dark'));
  themeBtn.title=t==='dark'?'Switch to light theme':'Switch to dark theme';
};
let saved=null; try{saved=localStorage.getItem('dol-theme')}catch(_){}
applyTheme(saved==='dark'?'dark':'light');
themeBtn.addEventListener('click',()=>{
  const next=document.documentElement.getAttribute('data-theme')==='dark'?'light':'dark';
  applyTheme(next);
  try{localStorage.setItem('dol-theme',next)}catch(_){}
});
reshuffle();
render();
</script></body></html>'''

html = HTML.replace('__PAYLOAD__', PAYLOAD).replace('__BUILDDATE__', BUILD_DATE)
open('dineout_guide.html', 'w').write(html)
print(f'dineout_guide.html: {len(entries)} entries, {len(html)/1024:.0f} KB, built {BUILD_DATE}')
