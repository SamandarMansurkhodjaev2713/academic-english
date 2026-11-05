#!/usr/bin/env python3
"""Browser DOM/UI integration. Uses inline static assets because sandbox blocks localhost navigation."""
from pathlib import Path
from playwright.sync_api import sync_playwright
from time import time
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'

def launch_page(browser,mobile=False,seed=''):
 w,h=(390,844) if mobile else (1440,900)
 page=browser.new_page(viewport={'width':w,'height':h},device_scale_factor=1,is_mobile=mobile,has_touch=mobile)
 errors=[]
 page.on('pageerror',lambda err:errors.append(str(err)))
 page.set_content('<html lang="ru"><head><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><style>'+ (DIST/'src/styles.css').read_text()+'</style></head><body><a class="skip-link" href="#content">Перейти</a><div id="app"></div></body></html>')
 page.evaluate("""seed => {window.__storage = seed ? JSON.parse(seed):{};Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem(k){return window.__storage[k]||null},setItem(k,v){window.__storage[k]=v},removeItem(k){delete window.__storage[k]}}});} """, seed)
 for path in ['content/curriculum.js','src/core.js','src/app.js']:page.add_script_tag(content=(DIST/path).read_text())
 return page,errors

def click_route(page,route):
 page.evaluate('(r)=>{location.hash=r}',route)
 page.wait_for_timeout(75)

def next_step(page):
 page.locator('[data-action="lesson-next"]').click()
 page.wait_for_timeout(75)

def choice(page,idx=0):
 box=page.locator('.question').nth(idx)
 box.locator('input[type="radio"]').last.check()
 box.locator('[data-action="submit-exercise"]').click()
 page.wait_for_timeout(80)

def main():
 with sync_playwright() as p:
  browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox','--no-proxy-server'])
  pg,errs=launch_page(browser)
  assert pg.get_by_text('Your next chapter starts here.').count()==1
  pg.locator('#onboard-name').fill('Learner')
  for _ in range(4):pg.locator('[data-action="onboard-next"]').click()
  pg.locator('[data-action="onboard-finish"][data-target="lesson/1"]').click()
  pg.wait_for_timeout(80)
  assert pg.get_by_text('Your learning goal').count()>=1
  assert not errs,errs
  next_step(pg) # vocabulary
  assert pg.get_by_text('Vocabulary & useful phrases').count()==1
  pg.locator('[data-action="reveal-word"]').first.click()
  assert pg.get_by_text('академическая поддержка').count()>=1
  next_step(pg) # reading
  pg.locator('[data-action="lookup"]').first.click()
  assert pg.locator('.lookup-card').count()==1
  next_step(pg) # reading quiz
  for i in range(2):choice(pg,i)
  next_step(pg) # listening
  assert pg.locator('.audio-box').count()>=1
  pg.locator('[data-action="toggle-transcript"]').first.click()
  assert pg.locator('.transcript-panel').count()==1
  next_step(pg) # listening questions
  for i in range(2):choice(pg,i)
  next_step(pg) # grammar
  choice(pg,0)
  next_step(pg) # practice: matching 4 + situation + fill
  pg.locator('.question[data-question*="-fill-"] input').first.fill('academic support')
  pg.locator('.question[data-question*="-fill-"] button[data-action="submit-exercise"]').first.click()
  pg.wait_for_timeout(75)
  for select in pg.locator('.match-row select').all(): select.select_option(select.get_attribute('data-term'))
  pg.locator('.question[data-question$="-match"] button[data-action="submit-exercise"]').click()
  pg.wait_for_timeout(75)
  pg.locator('.question[data-question$="-situation"] input[type="radio"]').first.check()
  pg.locator('.question[data-question$="-situation"] button[data-action="submit-exercise"]').click()
  pg.wait_for_timeout(75)
  next_step(pg) # speaking
  assert pg.locator('#speaking-text').count()==1
  pg.locator('#speaking-text').fill('It is a pleasure to meet you. I can help you check the required documents and the next steps.')
  pg.locator('[data-action="speak-reveal"]').click()
  pg.locator('[data-action="speak-complete"]').click()
  next_step(pg) # writing
  pg.locator('#writing-answer').fill('Dear colleague, thank you for contacting our Academic Support Department. I would be glad to help check your documents and explain the procedure. Please send us the request details and we will direct it to the authorised team. Kind regards, Alex.')
  pg.locator('[data-action="writing-reveal"]').click()
  pg.locator('[data-action="writing-complete"]').click()
  next_step(pg) # summary
  assert pg.get_by_text('Well done. Keep building.').count()==1
  stored=pg.evaluate('JSON.stringify(window.__storage)')
  print('LESSON COMPLETE; saved payload bytes:',len(stored))
  click_route(pg,'vocabulary/review')
  assert pg.locator('.study-card').count()==1
  pg.locator('[data-action="review-reveal"]').click()
  pg.locator('[data-action="review-rate"]').nth(2).click()
  click_route(pg,'settings')
  pg.locator('[data-action="setting-theme"][data-value="dark"]').click()
  assert pg.evaluate('document.documentElement.dataset.theme')=='dark'
  pg.screenshot(path='/mnt/data/academic-settings-dark.png',full_page=True)
  click_route(pg,'conversation')
  assert pg.locator('#conversation-response').count()==1
  pg.locator('#conversation-response').fill('Hello, thank you for asking. I can check your request with the relevant academic team and update you soon.')
  pg.locator('[data-action="conv-reveal"]').click()
  pg.locator('[data-action="conv-next"]').click()
  click_route(pg,'emails')
  assert pg.locator('[data-action="email-select"]').count()==15
  pg.locator('[data-action="email-select"]').nth(2).click()
  assert pg.get_by_text('Following Up on a Request').count()>=1
  click_route(pg,'assessment/placement')
  for question in pg.locator('.assessment-question').all():question.locator('input[type="radio"]').first.check()
  pg.locator('[data-action="assessment-submit"]').click()
  assert pg.locator('.assess-summary').count()==1
  stored=pg.evaluate('JSON.stringify(window.__storage)')
  assert not errs,errs
  print('BROWSER FLOW PASS; no page errors. Final state bytes',len(stored))
  pg2,errs2=launch_page(browser,seed=stored)
  assert pg2.locator('.onboard-frame').count()==0
  click_route(pg2,'dashboard')
  assert 'Пройдено уроков' in pg2.locator('#content').inner_text()
  click_route(pg2,'lesson/1/10')
  assert pg2.get_by_text('Well done. Keep building.').count()==1
  assert not errs2,errs2
  print('PERSISTENCE PASS: onboarding, Day 1 completion, placement')
  for wh in [(375,812),(390,844),(768,1024),(1280,800),(1440,900)]:
   pg2.set_viewport_size({'width':wh[0],'height':wh[1]});pg2.wait_for_timeout(100)
   overflow=pg2.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')
   print('VIEWPORT',wh,'overflow',overflow)
   assert overflow<=3,(wh,overflow)
   if wh==(390,844):pg2.screenshot(path='/mnt/data/academic-mobile-lesson.png',full_page=True)
  assert not errs2,errs2
  click_route(pg2,'dashboard')
  pg2.set_viewport_size({'width':1440,'height':900})
  pg2.screenshot(path='/mnt/data/academic-dashboard-desktop.png',full_page=True)
  browser.close()

if __name__=='__main__':main()
