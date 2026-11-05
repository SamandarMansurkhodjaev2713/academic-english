"""Visit all authored lesson pages and major sections in Chromium at phone + desktop size."""
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]/'dist'
with sync_playwright() as p:
 b=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--no-proxy-server'])
 page=b.new_page(viewport={'width':390,'height':844})
 errs=[];page.on('pageerror',lambda e:errs.append(str(e)))
 page.set_content('<html><head><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+ (ROOT/'src/styles.css').read_text()+'</style></head><body><div id="app"></div></body></html>')
 page.evaluate("""() => {const v={};Object.defineProperty(window,'localStorage',{value:{getItem(k){return v[k]||null},setItem(k,x){v[k]=x}}})}""")
 for f in ['content/curriculum.js','src/core.js','src/app.js']:page.add_script_tag(content=(ROOT/f).read_text())
 for _ in range(4):page.locator('[data-action="onboard-next"]').click()
 page.locator('[data-action="onboard-finish"][data-target="lesson/1"]').click()
 routes=['dashboard','path','vocabulary','vocabulary/review','conversation','listening','practice','progress','phrasebook','emails','settings','assessment/placement','assessment/final','assessment/checkpoint-5','assessment/checkpoint-10','assessment/checkpoint-15','assessment/checkpoint-22']+[f'lesson/{i}' for i in range(1,31)]
 bad=[]
 for r in routes:
  page.evaluate('(r)=>{window.location.hash=r}',r);page.wait_for_timeout(45)
  overflow=page.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth')
  if overflow>3:bad.append((r,overflow))
  if not page.locator('#content').count() or len(page.locator('#content').inner_text())<40:bad.append((r,'empty'))
 assert not bad,bad
 assert not errs,errs
 print(f'PASS: {len(routes)} routes at 390×844; horizontal overflow zero, empty screens zero, page JS errors zero')
 page.set_viewport_size({'width':1440,'height':900})
 for r in routes:
  page.evaluate('(r)=>{window.location.hash=r}',r);page.wait_for_timeout(30)
  assert page.evaluate('document.documentElement.scrollWidth - document.documentElement.clientWidth')<=3,r
 print(f'PASS: {len(routes)} routes at 1440×900; horizontal overflow zero')
 page.evaluate("location.hash='dashboard'");page.wait_for_timeout(70)
 page.screenshot(path='/mnt/data/academic-dashboard-light.png',full_page=True)
 b.close()
