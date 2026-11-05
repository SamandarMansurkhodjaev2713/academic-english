"""Generate offline curriculum from human-authored module source files."""
import json, sys, collections
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parent))
from part1 import LESSONS as L1
from part2 import LESSONS as L2
from part3 import LESSONS as L3
from part4 import LESSONS as L4
from objectives import OBJECTIVES
LESSONS=L1+L2+L3+L4
if [l['day'] for l in LESSONS] != list(range(1,31)): raise SystemExit('Non-contiguous lessons')
modules = [
 {'name':'Communication foundations','sub':'Представление, small talk и ясные вопросы','days':[1,5],'color':'mint'},
 {'name':'Academic operations','sub':'Программы, расписания и документы','days':[6,10],'color':'lilac'},
 {'name':'Student academic support','sub':'Поддержка, оценки и сложные ситуации','days':[11,15],'color':'peach'},
 {'name':'International communication','sub':'Письма, встречи и университетские партнёры','days':[16,22],'color':'blue'},
 {'name':'Advanced workplace communication','sub':'Решения, отчёты и интегрированная практика','days':[23,30],'color':'yellow'},
]
for l in LESSONS:
 l['objectives']=OBJECTIVES[l['day']]
 l['module']=next(i for i,m in enumerate(modules) if m['days'][0]<=l['day']<=m['days'][1])
# diagnostics and final contain independent input-based questions, rather than fabricated scores
bank=[]
for l in LESSONS:
 for cat in ['readingChecks','listeningChecks']:
  for i,q in enumerate(l[cat]):
   bank.append({**q,'id':f"{l['id']}-{cat}-{i}",'day':l['day'],'skill':'reading' if cat=='readingChecks' else 'listening'})
 bank.append({**l['grammarCheck'],'id':f"{l['id']}-grammar",'day':l['day'],'skill':'grammar'})
# Independent quizzes deliberately sample different modules and skills; not a CEFR certificate.
placement_days=[1,2,3,4,6,7,9,11,12,14,16,18,20,22,24,27,28]
final_days=[2,5,6,9,10,12,15,16,18,20,21,22,23,25,27,28,29,30]
def assessment(days):
 result=[]
 for day in days:
  picks=[x for x in bank if x['day']==day]
  choice=picks[(day*7)%len(picks)].copy()
  result.append(choice)
 return result
payload={'title':'Academic English · 30-Day Course','version':'1.0.0','modules':modules,'lessons':LESSONS,
         'assessments':{'placement':assessment(placement_days), 'final':assessment(final_days)},
         'metadata':{'language':'International English','audience':'Academic Support','level':'B1 → B1+ / toward B2','dailyMinutes':70}}
output=Path(__file__).resolve().parents[1]/'content'/'curriculum.json'
output.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
output.with_suffix('.js').write_text('window.ACADEMIC_DATA = '+json.dumps(payload,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print('Built',output,'lessons',len(LESSONS),'vocabulary',sum(len(x['vocab']) for x in LESSONS),'words reading',sum(len(x['reading']['text'].split()) for x in LESSONS),'questions',len(bank),'size',output.stat().st_size)
