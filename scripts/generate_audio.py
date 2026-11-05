import asyncio, hashlib, json, pathlib
import edge_tts
root=pathlib.Path(__file__).resolve().parents[1]
data=json.loads((root/'content/curriculum.json').read_text(encoding='utf-8'))
out=root/'assets/audio'; out.mkdir(parents=True,exist_ok=True)
items={}
def add(text,voice='en-GB-SoniaNeural'):
 key=voice+'\n'+text
 name=hashlib.sha256(key.encode()).hexdigest()[:20]+'.mp3'
 items[key]=name
for l in data['lessons']:
 for v in l['vocab']: add(v['term'])
 for v in l['phrases']: add(v['en'])
 add(l['speaking']['prompt'])
 voices=['en-GB-SoniaNeural','en-GB-RyanNeural','en-GB-LibbyNeural','en-GB-ThomasNeural','en-GB-MaisieNeural','en-US-AndrewNeural']
 speakers=list(dict.fromkeys(line['speaker'] for line in l['dialogue']['lines']))
 for i,line in enumerate(l['dialogue']['lines']):
  add(line['text'], voices[speakers.index(line['speaker']) % len(voices)])
  if i==0: add(line['text'])
(root/'assets/audio-map.js').write_text('window.ACADEMIC_AUDIO='+json.dumps(items,ensure_ascii=False,separators=(',',':'))+';',encoding='utf-8')
sem=asyncio.Semaphore(8)
async def run(key,name):
 path=out/name
 if path.exists() and path.stat().st_size>0:return
 voice,text=key.split('\n',1)
 async with sem:
  for attempt in range(4):
   try:
    await edge_tts.Communicate(text,voice).save(str(path)); return
   except Exception:
    if attempt==3: raise
    await asyncio.sleep(2**attempt)
async def main():
 print('Generating',len(items),'audio clips',flush=True)
 await asyncio.gather(*(run(k,v) for k,v in items.items()))
 print('Done',flush=True)
asyncio.run(main())
