import json
payload = open('payload.json').read()

HTML = r'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dine Out Lauderdale 2026 — decoded</title>
<style>
:root{
  color-scheme: light;
  --surface-1:#ffffff; --plane:#F5F8FC; --card:#ffffff;
  --ink:#142235; --ink-2:#4B5568; --muted:#8A93A6;
  --grid:#E3E8F0; --baseline:#C7CFDD; --ring:rgba(20,34,53,0.10);
  --good:#12875A; --warning:#F2A900; --serious:#F2884B; --critical:#E0432B;
  --accent:#1E67CD; --accent-soft:#DCEBFF;
  --success-text:#0E6B46; --gold:#FFD56B; --navy:#1A222D;
}
@media (prefers-color-scheme: dark){
  :root:where(:not([data-theme="light"])){
    color-scheme: dark;
    --surface-1:#141B24; --plane:#0C1117; --card:#141B24;
    --ink:#F3F6FA; --ink-2:#B9C2D0; --muted:#8892A0;
    --grid:#253040; --baseline:#364256; --ring:rgba(255,255,255,0.10);
    --accent:#5B9CF2; --accent-soft:#1D3556; --success-text:#2FBE85;
    --good:#1FA971; --warning:#F2A900; --serious:#F2884B; --critical:#FF6B52;
    --gold:#FFD56B; --navy:#0C1117;
  }
}
:root[data-theme="dark"]{
  color-scheme: dark;
  --surface-1:#141B24; --plane:#0C1117; --card:#141B24;
  --ink:#F3F6FA; --ink-2:#B9C2D0; --muted:#8892A0;
  --grid:#253040; --baseline:#364256; --ring:rgba(255,255,255,0.10);
  --accent:#5B9CF2; --accent-soft:#1D3556; --success-text:#2FBE85;
  --good:#1FA971; --warning:#F2A900; --serious:#F2884B; --critical:#FF6B52;
  --gold:#FFD56B; --navy:#0C1117;
}
*{box-sizing:border-box}
body{margin:0;background:var(--plane);color:var(--ink);
  font-family:system-ui,-apple-system,"Segoe UI",sans-serif;font-size:15px;line-height:1.5}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px 80px}
.topbar{background:var(--navy);color:#fff;padding:9px 0}
.topbar .wrap{padding:0 20px;display:flex;align-items:center;gap:8px;font-size:13px;letter-spacing:.02em}
.topbar b{color:var(--gold);font-weight:750}
header{padding:30px 0 0;position:relative}
h1{font-size:29px;margin:0 0 6px;letter-spacing:-.02em;font-weight:800}
h1 .accent{color:var(--accent)}
.sub{color:var(--ink-2);font-size:14px;max-width:70ch;margin:0 0 4px}
.themebtn{position:absolute;top:30px;right:20px;background:var(--card);border:1px solid var(--ring);
  color:var(--ink-2);border-radius:8px;padding:6px 12px;cursor:pointer;font-size:13px;font-family:inherit}
.wave{height:16px;margin:22px 0 0;
  background: radial-gradient(circle at 10px -7px, transparent 13px, var(--gold) 14px) 0 0/20px 20px repeat-x;
  opacity:.9}
.lede{background:var(--card);border:1px solid var(--ring);border-left:4px solid var(--accent);
  border-radius:10px;padding:14px 16px;margin:20px 0 0;font-size:14px;color:var(--ink-2);max-width:80ch}
.lede b{color:var(--ink)}
.controls{position:sticky;top:0;z-index:20;background:var(--plane);
  padding:14px 0 12px;border-bottom:1px solid var(--grid);margin-bottom:22px}
.crow{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
input[type=search],select{font-family:inherit;font-size:13px;padding:7px 10px;border-radius:8px;
  border:1px solid var(--ring);background:var(--card);color:var(--ink)}
input[type=search]{min-width:210px}
.chip{font-size:12.5px;padding:6px 11px;border-radius:999px;border:1px solid var(--ring);
  background:var(--card);color:var(--ink-2);cursor:pointer;font-family:inherit}
.chip[aria-pressed=true]{background:var(--navy);color:#fff;border-color:var(--navy)}
.count{font-size:13px;color:var(--muted);margin-left:auto}
.ms{position:relative}
.msbtn{font-family:inherit;font-size:13px;padding:7px 10px;border-radius:8px;cursor:pointer;
  border:1px solid var(--ring);background:var(--card);color:var(--ink);display:inline-flex;
  align-items:center;gap:7px;white-space:nowrap}
.msbtn[aria-expanded=true]{border-color:var(--accent)}
.msbtn.on{background:var(--accent-soft);border-color:var(--accent);color:var(--ink)}
.mscar{font-size:9px;color:var(--muted)}
.mspanel{position:absolute;top:calc(100% + 5px);left:0;z-index:40;min-width:230px;max-height:320px;
  overflow-y:auto;background:var(--card);border:1px solid var(--ring);border-radius:10px;
  box-shadow:0 8px 26px rgba(20,34,53,.16);padding:7px}
.msact{display:flex;gap:6px;padding:2px 4px 7px;border-bottom:1px solid var(--grid);margin-bottom:5px}
.msact button{flex:1;font-family:inherit;font-size:11.5px;padding:5px 8px;border-radius:6px;cursor:pointer;
  border:1px solid var(--ring);background:var(--plane);color:var(--ink-2)}
.msact button:hover{color:var(--ink);border-color:var(--accent)}
.msopt{display:flex;align-items:center;gap:8px;padding:6px 7px;border-radius:6px;
  font-size:13px;color:var(--ink);cursor:pointer;line-height:1.3}
.msopt:hover{background:var(--plane)}
.msopt input{margin:0;flex:0 0 auto;accent-color:var(--accent)}
.mshint{font-size:11px;color:var(--muted);padding:5px 7px 2px;line-height:1.35}
.grid{display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(430px,1fr))}
@media(max-width:920px){.grid{grid-template-columns:1fr}}
.card{background:var(--card);border:1px solid var(--ring);border-radius:14px;padding:18px 18px 14px;
  display:flex;flex-direction:column;gap:11px;box-shadow:0 1px 2px rgba(20,34,53,.04)}
.chead{display:flex;justify-content:space-between;gap:12px;align-items:flex-start}
.rname{font-size:17px;font-weight:700;letter-spacing:-.01em;margin:0;line-height:1.25}
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
.dchip.on{background:var(--accent-soft);color:var(--accent)}
.dnote{font-size:11px;color:var(--muted);margin-left:5px}
.hours .ic{color:var(--accent)}
.tier{flex:0 0 auto;text-align:right}
.tierp{font-size:21px;font-weight:750;letter-spacing:-.02em;color:var(--navy)}
:root[data-theme="dark"] .tierp{color:var(--ink)}
@media (prefers-color-scheme: dark){:root:where(:not([data-theme="light"])) .tierp{color:var(--ink)}}
.tierm{font-size:11.5px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}
.blurb{font-size:13.5px;color:var(--ink-2);margin:0}
.heads{font-size:12.5px;color:var(--ink-2);background:var(--plane);border-radius:7px;
  padding:8px 10px;border-left:3px solid var(--warning)}
.heads b{color:var(--ink)}
.vrow{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.verdict{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;font-weight:650;
  padding:4px 10px;border-radius:999px;border:1px solid transparent;width:fit-content}
.confchip{display:inline-flex;align-items:center;gap:5px;font-size:11.5px;color:var(--ink-2);
  padding:4px 9px;border-radius:999px;border:1px solid var(--ring);background:var(--plane)}
.v-safe{color:var(--success-text);background:rgba(18,135,90,.12);border-color:rgba(18,135,90,.35)}
.v-pick{color:var(--accent);background:rgba(30,103,205,.10);border-color:rgba(30,103,205,.32)}
.v-marginal{color:var(--ink-2);background:rgba(242,169,0,.14);border-color:rgba(242,169,0,.45)}
.v-skip{color:var(--critical);background:rgba(224,67,43,.10);border-color:rgba(224,67,43,.38)}
.v-nomenu{color:var(--muted);background:var(--plane);border-color:var(--ring)}
.tabs{display:flex;gap:4px;background:var(--plane);border-radius:9px;padding:3px}
.tabbtn{flex:1;border:none;background:transparent;color:var(--ink-2);font-family:inherit;
  font-size:12.5px;font-weight:650;padding:7px 10px;border-radius:7px;cursor:pointer}
.tabbtn.active{background:var(--card);color:var(--navy);box-shadow:0 1px 2px rgba(20,34,53,.08)}
:root[data-theme="dark"] .tabbtn.active{color:var(--ink)}
@media (prefers-color-scheme: dark){:root:where(:not([data-theme="light"])) .tabbtn.active{color:var(--ink)}}
.tabpane[hidden]{display:none}
.order{background:var(--plane);border-radius:9px;padding:12px 13px}
.olab{font-size:11px;text-transform:uppercase;letter-spacing:.07em;color:var(--muted);
  font-weight:650;margin-bottom:7px}
.oline{display:flex;gap:7px;align-items:baseline;font-size:13.5px;margin-bottom:4px}
.ocourse{flex:0 0 62px;color:var(--muted);font-size:11.5px;text-transform:uppercase;letter-spacing:.04em}
.odish{font-weight:600;color:var(--ink)}
.ogloss{font-size:12.5px;color:var(--ink-2);margin:1px 0 7px 69px;line-height:1.42}
.osrc{font-size:11px;color:var(--muted);margin:0 0 7px 69px;line-height:1.4;font-style:italic}
.fullmenu{background:var(--plane);border-radius:9px;padding:12px 13px}
.course{margin-top:0}
.course+.course{margin-top:12px}
.chdr{font-size:11px;text-transform:uppercase;letter-spacing:.07em;color:var(--muted);
  font-weight:650;border-bottom:1px solid var(--grid);padding-bottom:4px;margin-bottom:7px}
.opt{display:flex;justify-content:space-between;gap:10px;align-items:baseline;padding:4px 0}
.optname{font-size:13.5px}
.best{font-weight:650}
.star{color:var(--warning);font-size:11px}
.optprice{font-size:13px;color:var(--ink-2);font-variant-numeric:tabular-nums;flex:0 0 auto}
.gl{font-size:12.5px;color:var(--ink-2);margin:2px 0 4px 0;line-height:1.42}
.src{font-size:11px;color:var(--muted);margin:-2px 0 4px 0;line-height:1.4;font-style:italic}
.bar{margin-top:2px}
.barlab{display:flex;justify-content:space-between;font-size:12px;color:var(--ink-2);margin-bottom:5px}
.track{position:relative;height:12px;background:var(--grid);border-radius:4px;overflow:visible}
.fill{position:absolute;left:0;top:0;bottom:0;border-radius:4px}
.tick{position:absolute;top:-4px;bottom:-4px;width:2px;background:var(--navy);border-radius:1px}
:root[data-theme="dark"] .tick{background:var(--ink)}
@media (prefers-color-scheme: dark){:root:where(:not([data-theme="light"])) .tick{background:var(--ink)}}
.ticklab{position:absolute;top:14px;font-size:10.5px;color:var(--muted);transform:translateX(-50%);white-space:nowrap}
.ticklab.e0{left:0;transform:none}
.ticklab.e1{left:auto;right:0;transform:none}
.savings{font-size:13.5px;color:var(--ink-2);margin:0 0 8px;line-height:1.4}
.savings b{font-weight:700}
.savings .up{color:var(--good)} .savings .dn{color:var(--critical)} .savings .ev{color:var(--ink)}
.barnote{font-size:12px;color:var(--ink-2);margin-top:20px}
.barnote b{color:var(--ink)}
.conf{font-size:11.5px;color:var(--muted);display:flex;align-items:center;gap:6px;margin-top:auto;padding-top:10px}
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
  <h1>Dine Out Lauderdale 2026 — <span class="accent">decoded</span></h1>
  <p class="sub" id="subline">Every prix fixe dish priced against the restaurant's regular menu, portion-adjusted, across all 16 Dine Out categories.</p>
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
      <option value="pct">Best value first</option>
      <option value="tier">Cheapest first</option>
      <option value="value">Most food for the money</option>
      <option value="name">A–Z</option>
    </select>
    <button class="chip" id="safe" aria-pressed="false">Can't go wrong</button>
    <button class="chip" id="worth" aria-pressed="false">Hide the duds</button>
    <button class="chip" id="ver" aria-pressed="false">Verified prices only</button>
    <button class="chip" id="pp" aria-pressed="false" title="Show the two dinner-for-two tiers as price per person">Per person</button>
    <span class="count" id="count"></span>
  </div>
</div>
<div class="grid" id="grid"></div>
<footer>
  <p><b>How to read this.</b> "Worth" is what the same dishes would cost à la carte at that restaurant, with portions adjusted — a 4-piece appetizer is priced against a 4-piece share of the regular 8-piece order, not the whole thing. All figures are before tax and tip. Paid add-ons (wine pairings, upcharges) are excluded; genuinely included drinks/sides are counted.</p>
  <p><b>"Order this"</b> is the highest-value pick in each course — usually the most expensive dish on the menu, which is the point. Switch to the <b>Full menu</b> tab on any card to see every option in every course with its own everyday price, and pick for yourself.</p>
  <p><b>Hours &amp; days.</b> The day strip (M T W T F S S) shows which days each special is served, read from the hours the restaurant published for that tier. Filtering by a day never hides a tier whose days weren't published — those are kept in the results and counted separately, since we can't rule them in or out. Always call ahead for a weekend booking.</p>
  <p><b>Confidence.</b> A green dot means every price came off the restaurant's own current menu. Grey means the restaurant publishes no prices anywhere and the numbers are benchmarked estimates — real for ranking, not for arguing over. Menus captured from visitlauderdale.com in August 2026; restaurants change menus without notice.</p>
</footer>
</div>
<script>
const DATA = __PAYLOAD__;
const ICON={safe:'✓',pick:'◆',marginal:'▵',skip:'✕',nomenu:'—'};
const LABEL={safe:'Good however you order',pick:'Worth it only if you order right',marginal:'Barely worth it',skip:'Costs more than ordering normally',nomenu:'No menu published'};
const CONFLAB={verified:'Prices verified on the restaurant’s own menu',mixed:'Some prices estimated',estimated:'Mostly estimated — restaurant publishes no prices',none:''};
const CONFSHORT={verified:'verified prices',mixed:'partly estimated',estimated:'mostly estimated',none:''};
const ORDER_PRIORITY=['Appetizer','Special','Side','Mid','Cocktail','Entree','Dessert'];
const CN={Appetizer:'Starter',Special:'Special',Side:'Side',Mid:'Pasta',Cocktail:'Cocktail',Entree:'Main',Dessert:'Dessert'};
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const money=n=>'$'+n.toFixed(n%1?2:0);
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

const cities=[...new Set(DATA.map(d=>d.city).filter(Boolean))].sort();
const cats=[...new Set(DATA.flatMap(d=>d.category||[]))].sort();

// Checkbox dropdown. Nothing ticked means "show everything", so the quickest way to
// exclude a couple of options is Select all, then untick the ones you don't want.
function multisel(hostId, allLabel, noun, values, onChange){
  const host=document.getElementById(hostId);
  host.innerHTML=
     `<button type="button" class="msbtn" aria-expanded="false"><span class="mslab">${esc(allLabel)}</span><span class="mscar">▼</span></button>`
    +`<div class="mspanel" hidden>`
    +  `<div class="msact"><button type="button" data-act="all">Select all</button><button type="button" data-act="none">Clear</button></div>`
    +  values.map(v=>`<label class="msopt"><input type="checkbox" value="${esc(v)}"><span>${esc(v)}</span></label>`).join('')
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
  return host;
}
multisel('category','All categories','categories',cats,v=>{S.category=v;render()});
multisel('city','All areas','areas',cities,v=>{S.city=v;render()});
document.addEventListener('click',e=>{
  if(e.target.closest('.ms'))return;
  document.querySelectorAll('.mspanel').forEach(p=>{p.hidden=true});
  document.querySelectorAll('.msbtn').forEach(b=>b.setAttribute('aria-expanded','false'));
});

// What the bar is really saying, in dollars.
const savingsLine=d=>{
  const lo=d.worst-d.tier, hi=d.best-d.tier, a=n=>money(Math.abs(n)), z=n=>Math.abs(n)<0.005;
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

let cardSeq=0;
function card(d0){
  // "Per person" halves the money on the two dinner-for-two tiers so they compare like-for-like
  const half=S.pp&&d0.for2;
  const d=half?Object.assign({},d0,{tier:d0.tier/2,best:d0.best/2,worst:d0.worst/2}):d0;
  const g=d.gloss||{};
  const cid='c'+(cardSeq++);
  const catpills=(d.category||[]).map(c=>`<span class="catpill">${esc(c)}</span>`).join('');
  const locLine=`<div class="loc">${d.url?`<a class="ext" href="${esc(d.url)}" target="_blank" rel="noopener">Menu &amp; details ↗</a> · `:''}<a class="addr" href="${esc(mapsUrl(d))}" target="_blank" rel="noopener" title="Open in Google Maps">${esc([d.city,d.address].filter(Boolean).join(' · ')||'Map')}</a></div>`;
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
  const courses=courseOrder(Object.keys(d.menu||{}).filter(c=>d.menu[c]&&d.menu[c].length));
  const orderLines=courses.map(c=>{
    const p=d.pick[c]; if(!p) return ''; const gl=g[p.dish]; const sr=srcOf(p);
    return `<div class="oline"><span class="ocourse">${esc(nameOf(c))}</span><span class="odish">${esc(short(p.dish))}</span><span class="optprice">${money(p.price)}</span></div>`
      + (gl?`<div class="ogloss">${esc(gl)}</div>`:'')
      + (sr?`<div class="osrc">Source: ${esc(sr)}</div>`:'');
  }).join('');
  const inc=(d.included||[]).length
    ? `<div class="oline"><span class="ocourse">Included</span><span class="odish">${esc(short(d.included_mode==='choose'?d.included[0].dish:d.included.map(i=>i.dish).join(' + ')))}</span></div>` : '';
  // range band on a 0..2x-tier scale, tick at what you pay
  const sc=v=>Math.max(0,Math.min(v/(d.tier*2),1))*100;
  const L=sc(d.worst), R=sc(d.best);
  const bandcol=d.verdict==='safe'?'var(--good)':d.verdict==='skip'?'var(--critical)':'var(--accent)';
  const menuHtml=courses.map(c=>{
    const opts=d.menu[c].map((o,i)=>{
      const gl=g[o.dish]; const sr=srcOf(o);
      return `<div class="opt"><span class="optname ${i===0?'best':''}">${i===0?'<span class="star">★</span> ':''}${esc(short(o.dish))}</span>`
        +`<span class="optprice">${money(o.price)}</span></div>`
        +(gl?`<div class="gl">${esc(gl)}</div>`:'')
        +(sr?`<div class="src">Source: ${esc(sr)}</div>`:'');
    }).join('');
    return `<div class="course"><div class="chdr">${esc(nameOf(c))} — choose one</div>${opts}</div>`;
  }).join('');
  const incMenu=(d.included||[]).length?`<div class="course"><div class="chdr">Included${d.included_mode==='choose'?' — choose one':''}</div>`
    + d.included.map(o=>`<div class="opt"><span class="optname">${esc(short(o.dish))}</span><span class="optprice">${money(o.price)}</span></div>`).join('')+`</div>`:'';
  const hoursLine=d.hours?`<div class="hours"><span class="ic">🕒</span>${esc(d.hours)}</div>`:'';
  const DAYL=['M','T','W','T','F','S','S'];
  const dayStrip = d.days
    ? `<div class="daystrip" title="Days this special is served">${DAYL.map((L,i)=>`<span class="dchip ${d.days.includes(i)?'on':''}">${L}</span>`).join('')}</div>`
    : `<div class="daystrip" title="The restaurant did not publish serving days"><span class="dnote" style="margin-left:0">Serving days not published — call ahead</span></div>`;
  return `<article class="card">
   <div class="chead">
     <div><h2 class="rname">${esc(d.restaurant)}</h2>
       <div>${catpills}</div>
       <div class="cuisine">${esc(d.cuisine)}</div>
       ${locLine}
       ${hoursLine}
       ${dayStrip}</div>
     <div class="tier"><div class="tierp">${money(d.tier)}</div><div class="tierm">${esc(d.meal)}${d.for2?(half?' / person':' for 2'):''}</div></div>
   </div>
   <div class="vrow">
     <span class="verdict v-${d.verdict}">${ICON[d.verdict]} ${LABEL[d.verdict]}</span>
     <span class="confchip"><i class="dot d-${d.confidence}"></i>${esc(CONFSHORT[d.confidence])}</span>
   </div>
   <p class="blurb">${esc(d.blurb)}</p>
   ${d.heads_up?`<div class="heads"><b>Heads up:</b> ${esc(d.heads_up)}</div>`:''}
   <div class="tabs" data-card="${cid}">
     <button class="tabbtn active" data-tab="order">${d.verdict==='skip'?'If you go anyway, order this':'Order this'}</button>
     <button class="tabbtn" data-tab="full">Full menu &amp; prices</button>
   </div>
   <div class="tabpane" data-card="${cid}" data-pane="order">
     <div class="order">${orderLines}${inc}</div>
   </div>
   <div class="tabpane" data-card="${cid}" data-pane="full" hidden>
     <div class="fullmenu">${menuHtml}${incMenu}</div>
   </div>
   <div class="bar">
     <div class="barlab"><span>You pay <b style="color:var(--ink)">${money(d.tier)}</b>${d.for2?(half?' per person':' (for two)'):''}</span>
       <span>${d.best===d.worst
         ? `Food worth <b style="color:var(--ink)">${money(d.best)}</b>`
         : `Food worth <b style="color:var(--ink)">${money(d.worst)}–${money(d.best)}</b>`}</span></div>
     <div class="savings">${savingsLine(d)}</div>
     <div class="track">
       <div class="fill" style="left:${L.toFixed(1)}%;width:${Math.max(R-L,1.2).toFixed(1)}%;background:${bandcol}"></div>
       <div class="tick" style="left:50%"></div>
       <div class="ticklab e0">${money(0)}</div>
       <div class="ticklab" style="left:50%">what you pay</div>
       <div class="ticklab e1">${money(d.tier*2)}</div>
     </div>
     <div class="barnote">${d.verdict==='safe'
        ? (d.best===d.worst
           ? `Fixed menu worth <b>${money(d.best)}</b> against the <b>${money(d.tier)}</b> you pay.`
           : `Every option on this menu beats the price — the whole range sits right of the line.`)
        : d.verdict==='skip'
        ? `Even the priciest combination comes to <b>${money(d.best)}</b>, under the <b>${money(d.tier)}</b> you pay.`
        : `Order as recommended and it's <b>${money(d.best)}</b>; pick the cheapest option each course and it falls to <b>${money(d.worst)}</b>, below what you paid.`}</div>
     ${d.courses_n>0&&d.courses_n<3?`<div class="barnote" style="margin-top:6px">Note: only ${d.courses_n} courses were published for this tier${d.courses_n===2?' — no dessert listed':''}.</div>`:''}
     ${d.best>d.tier*2?`<div class="barnote" style="margin-top:6px">The bar tops out at ${money(d.tier*2)} (twice what you pay); this menu runs past the end of it.</div>`:''}
   </div>
   <div class="conf"><i class="dot d-${d.confidence}"></i>${esc(CONFLAB[d.confidence])}</div>
  </article>`;
}

document.getElementById('grid').addEventListener('click', e=>{
  const btn=e.target.closest('.tabbtn');
  if(!btn) return;
  const cid=btn.closest('.tabs').dataset.card;
  const tab=btn.dataset.tab;
  document.querySelectorAll(`.tabbtn[data-card="${cid}"]`).forEach(b=>b.classList.toggle('active', b.dataset.tab===tab));
  document.querySelectorAll(`.tabpane[data-card="${cid}"]`).forEach(p=>{ p.hidden = p.dataset.pane!==tab; });
});

const S={q:'',city:[],category:[],meal:'',price:'',day:'',sort:'pct',worth:false,ver:false,safe:false,pp:false};
const VRANK={safe:0,pick:1,marginal:2,skip:3,nomenu:4};
function updateLede(){
  const restCount=new Set(DATA.map(d=>d.restaurant)).size;
  const catCount=new Set(DATA.flatMap(d=>d.category||[])).size;
  document.getElementById('subline').textContent=
    `${restCount} restaurants across ${catCount} Dine Out categories, August 1 – September 30. Every prix fixe dish priced against the restaurant's regular menu, portion-adjusted.`;
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
    if(S.worth&&!(d.verdict==='safe'||d.verdict==='pick'))return false;
    if(S.safe&&d.verdict!=='safe')return false;
    if(S.ver&&d.confidence!=='verified')return false;
    if(S.q){
      const hay=(d.restaurant+' '+d.cuisine+' '+d.blurb+' '+(d.category||[]).join(' ')+' '+Object.values(d.menu||{}).flat().map(o=>o.dish).join(' ')).toLowerCase();
      if(!hay.includes(S.q.toLowerCase()))return false;
    }
    return true;
  });
  const nomenu=r.filter(d=>d.verdict==='nomenu'), rest=r.filter(d=>d.verdict!=='nomenu');
  const surplus=x=>(x.best-x.tier)/x.tier;
  rest.sort((a,b)=>
      S.sort==='pct'   ? VRANK[a.verdict]-VRANK[b.verdict] || surplus(b)-surplus(a)
    : S.sort==='tier'  ? a.tier-b.tier || VRANK[a.verdict]-VRANK[b.verdict]
    : S.sort==='value' ? b.best-a.best
    : a.restaurant.localeCompare(b.restaurant));
  r=rest.concat(nomenu);
  document.getElementById('grid').innerHTML=r.length?r.map(card).join(''):'<div class="empty">Nothing matches those filters.</div>';
  const unl=rest.filter(d=>!d.days).length;
  document.getElementById('count').textContent=
    `${rest.length} menu${rest.length===1?'':'s'}` + (S.day!==''&&unl?` · incl. ${unl} with unlisted days`:'');
}
const bind=(id,k)=>document.getElementById(id).addEventListener('input',e=>{S[k]=e.target.value;render()});
bind('q','q');bind('meal','meal');bind('price','price');bind('day','day');bind('sort','sort');
['worth','ver','safe','pp'].forEach(id=>document.getElementById(id).addEventListener('click',e=>{
  S[id]=!S[id];e.target.setAttribute('aria-pressed',S[id]);render()}));
document.getElementById('tt').addEventListener('click',()=>{
  const cur=document.documentElement.getAttribute('data-theme');
  const dark=cur?cur==='dark':matchMedia('(prefers-color-scheme: dark)').matches;
  document.documentElement.setAttribute('data-theme',dark?'light':'dark');
});
render();
</script></body></html>'''

open('dineout_guide.html','w').write(HTML.replace('__PAYLOAD__', payload))
print('written')
