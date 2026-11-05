#!/usr/bin/env python3
"""Content integrity checks. This is structural QA, not an external language exam."""
from __future__ import annotations
from pathlib import Path
from collections import Counter
import json
import sys
ROOT=Path(__file__).resolve().parents[1]
D=json.loads((ROOT/'content/curriculum.json').read_text('utf-8'))
issues=[]
def check(condition,message):
 if not condition: issues.append(message)
modules=D.get('modules',[])
lessons=D.get('lessons',[])
check(len(lessons)==30,'Expected 30 lessons')
check([l.get('day') for l in lessons]==list(range(1,31)),'Lesson days must be exactly 1..30')
check(len(modules)==5,'Expected five modules')
unique_words=[];ids=[];all_qids=[]
for lesson in lessons:
 day=lesson['day'];label=f'Day {day}'
 check(lesson.get('id')==f'day-{day:02}',label+' invalid ID')
 check(lesson.get('module') in range(5),label+' invalid module')
 check(bool(lesson.get('title')) and bool(lesson.get('titleRu')),label+' title missing')
 check(len(lesson.get('objectives',[])) in range(3,6),label+' requires 3–5 measurable objectives')
 check(len(set(lesson.get('objectives',[])))==len(lesson.get('objectives',[])),label+' objectives duplicate')
 check(len(lesson.get('vocab',[]))>=10,label+' vocabulary fewer than 10 items')
 check(len(lesson.get('phrases',[]))>=5,label+' phrases fewer than 5 items')
 check(len(lesson.get('reading',{}).get('text','').split())>=180,label+' reading fewer than 180 words')
 check(len(lesson.get('dialogue',{}).get('lines',[]))>=6,label+' dialogue fewer than six turns')
 check(len(lesson.get('readingChecks',[]))>=2,label+' reading checks fewer than two')
 check(len(lesson.get('listeningChecks',[]))>=2,label+' listening checks fewer than two')
 check(len(lesson.get('grammar',{}).get('examples',[]))>=2,label+' grammar examples missing')
 check(bool(lesson.get('speaking',{}).get('prompt')) and bool(lesson.get('speaking',{}).get('sample')),label+' speaking incomplete')
 check(bool(lesson.get('writing',{}).get('prompt')) and bool(lesson.get('writing',{}).get('sample')),label+' writing incomplete')
 check(bool(lesson.get('challenge')),label+' challenge missing')
 for v in lesson.get('vocab',[]):
  ids.append(v.get('id'))
  unique_words.append(v.get('term','').casefold())
  for k in ('term','ru','definition','example'):
   check(bool(v.get(k)),label+f' vocabulary {v.get("id")}: {k} missing')
 for phrase in lesson.get('phrases',[]):
  check(bool(phrase.get('en')) and bool(phrase.get('ru')),label+' phrase incomplete')
 for line in lesson.get('dialogue',{}).get('lines',[]):
  check(bool(line.get('speaker')) and len(line.get('text',''))>15,label+' dialogue line too short')
 for cat in ['readingChecks','listeningChecks']:
  for i,q in enumerate(lesson.get(cat,[])):
   all_qids.append(f'{lesson["id"]}-{cat}-{i}')
   check(bool(q.get('q')) and bool(q.get('explanation')),label+f' {cat} missing question/explanation')
   check(len(q.get('options',[]))>=3,label+f' {cat} options < 3')
   check(q.get('answer') in range(len(q.get('options',[]))),label+f' {cat} answer out of range')
   check(len(set(q.get('options',[])))==len(q.get('options',[])),label+f' {cat} duplicate options')
 for field in ['grammarCheck','situational']:
  q=lesson[field]
  check(q.get('answer') in range(len(q.get('options',[]))),label+f' {field} answer index invalid')
  check(len(set(q.get('options',[])))==3,label+f' {field} duplicate options')
  check(bool(q.get('explanation')),label+f' {field} explanation missing')
check(len(ids)==len(set(ids)),'Duplicate vocabulary IDs')
check(len(all_qids)==len(set(all_qids)),'Duplicate question IDs')
for key,bank in D.get('assessments',{}).items():
 check(len(bank)>=15,f'Assessment {key} has fewer than 15 questions')
 check(len(set(q['id'] for q in bank))==len(bank),f'Assessment {key}: duplicate ID')
 for q in bank:
  check(q['answer'] in range(len(q['options'])),f'Assessment {key}: invalid answer {q["id"]}')
check(len(set(l['title'] for l in lessons))==30,'Duplicate day titles')
check(len(set(l['reading']['text'] for l in lessons))==30,'Duplicate reading texts')
check(len(set(tuple(x['text'] for x in l['dialogue']['lines']) for l in lessons))==30,'Duplicate dialogues')
print(f"LESSONS={len(lessons)} MODULES={len(modules)} VOCAB={len(ids)} UNIQUE_TERMS={len(set(unique_words))} PHRASES={sum(len(l['phrases']) for l in lessons)} READING_WORDS={sum(len(l['reading']['text'].split()) for l in lessons)} AUDIO_SCRIPTS={len(lessons)} QUESTION_ITEMS={sum(len(l['readingChecks'])+len(l['listeningChecks'])+2 for l in lessons)}")
if issues:
 print('FAILED: '+str(len(issues))+' issue(s)')
 for issue in issues[:100]:print(' -',issue)
 sys.exit(1)
print('PASS: structural lesson and assessment integrity')
