/* Academic English — deterministic learning and progress logic. Dependency-free UMD. */
(function(root,factory){const result=factory(); if(typeof module==='object'&&module.exports)module.exports=result; root.AcademicCore=result;})(typeof globalThis!=='undefined'?globalThis:this,function(){
 'use strict';
 const VERSION=1;
 const STORAGE_KEY='acls_progress_v1';
 const stages=['Начало','Vocabulary','Reading','Reading check','Listening','Listening check','Grammar','Practice','Speaking','Workplace challenge','Результат'];
 function localDate(d=new Date()) {const y=d.getFullYear(),m=String(d.getMonth()+1).padStart(2,'0'),day=String(d.getDate()).padStart(2,'0');return `${y}-${m}-${day}`;}
 function addDays(dateString,n){const parts=dateString.split('-').map(Number);const d=new Date(parts[0],parts[1]-1,parts[2]+n,12,0);return localDate(d);}
 function normalize(text){return String(text||'').toLocaleLowerCase('en').normalize('NFKC').replace(/[’‘]/g,"'").replace(/[^\p{L}\p{N}']+/gu,' ').replace(/\s+/g,' ').trim();}
 function init(){return {version:VERSION,onboarded:false,name:'',theme:'system',fontScale:'normal',rate:0.92,lessons:{},reviews:{},saved:[],activities:[],attempts:[],assessments:{},notes:{},conversation:{},lastRoute:'dashboard',createdAt:new Date().toISOString()};}
 function safeObject(value){return !!value&&typeof value==='object'&&!Array.isArray(value);}
 function sanitizeProgress(value){if(!safeObject(value))throw Error('Неверный формат данных: ожидался JSON-объект.');if(value.version!==VERSION)throw Error('Неподдерживаемая версия сохранения.');
  for(const key of ['lessons','reviews','notes','conversation','assessments'])if(value[key]!==undefined&&!safeObject(value[key]))throw Error(`Некорректное поле: ${key}`);
  for(const key of ['saved','activities','attempts'])if(value[key]!==undefined&&!Array.isArray(value[key]))throw Error(`Некорректное поле: ${key}`);
  const out={...init()};out.onboarded=!!value.onboarded;out.name=String(value.name||'').slice(0,80);out.theme=['system','dark','light'].includes(value.theme)?value.theme:'system';out.fontScale=['normal','large'].includes(value.fontScale)?value.fontScale:'normal';out.rate=Number.isFinite(Number(value.rate))?Math.max(.6,Math.min(1.3,Number(value.rate))):.92;
  out.createdAt=typeof value.createdAt==='string'?value.createdAt:out.createdAt;
  for(const [id,v]of Object.entries(value.lessons||{})){if(!/^day-\d\d$/.test(id)||!safeObject(v))continue;out.lessons[id]={stage:Number.isInteger(v.stage)?Math.max(0,Math.min(10,v.stage)):0,doneStages:Array.isArray(v.doneStages)?v.doneStages.filter(x=>Number.isInteger(x)&&x>=0&&x<=10):[],answers:safeObject(v.answers)?v.answers:{},speaking:safeObject(v.speaking)?v.speaking:{},writing:safeObject(v.writing)?v.writing:{},completedAt:typeof v.completedAt==='string'?v.completedAt:null};}
  for(const [id,v]of Object.entries(value.reviews||{})){if(!/^w\d\d-\d\d$/.test(id)||!safeObject(v))continue; const interval=Number(v.interval);out.reviews[id]={repetitions:Math.max(0,Math.min(999,Number(v.repetitions)||0)),ease:Math.max(1.3,Math.min(3,Number(v.ease)||2.5)),interval:Number.isFinite(interval)?Math.max(0,Math.min(365,interval)):0,next:typeof v.next==='string'&&/^\d{4}-\d\d-\d\d$/.test(v.next)?v.next:localDate(),last:typeof v.last==='string'?v.last:null,history:Array.isArray(v.history)?v.history.slice(-60).filter(x=>safeObject(x)):[]};}
  out.saved=[...new Set((value.saved||[]).filter(x=>typeof x==='string'&&/^w\d\d-\d\d$/.test(x)))].slice(0,1000);
  out.activities=[...new Set((value.activities||[]).filter(x=>typeof x==='string'&&/^\d{4}-\d\d-\d\d$/.test(x)))].slice(-1000);
  out.attempts=(value.attempts||[]).filter(x=>safeObject(x)&&typeof x.id==='string').slice(-3000);
  out.assessments={};
  for(const [type,a]of Object.entries(value.assessments||{})){
   if(!/^(placement|final|checkpoint-(5|10|15|22))$/.test(type))continue;
   if(!safeObject(a))throw Error(`Некорректный тест: ${type}`);
   if(a.history!==undefined&&!Array.isArray(a.history))throw Error(`Некорректная история теста: ${type}`);
   const safeAnswers=raw=>Object.fromEntries(Object.entries(safeObject(raw)?raw:{}).filter(([id,n])=>typeof id==='string'&&id.length<=120&&Number.isInteger(Number(n))&&Number(n)>=0&&Number(n)<=3).slice(0,100).map(([id,n])=>[id,Number(n)]));
   const safeScore=raw=>safeObject(raw)&&Number.isFinite(Number(raw.correct))&&Number.isFinite(Number(raw.total))&&Number(raw.total)>0?{correct:Math.min(100,Math.max(0,Math.floor(Number(raw.correct)))),total:Math.min(100,Math.max(1,Math.floor(Number(raw.total)))),answered:Math.min(100,Math.max(0,Math.floor(Number(raw.answered)||0))),pct:Number.isFinite(Number(raw.pct))?Math.min(100,Math.max(0,Math.round(Number(raw.pct)))):null}:null;
   const history=(a.history||[]).filter(x=>safeObject(x)&&safeScore(x.result)).slice(-60).map(x=>({at:typeof x.at==='string'?x.at:'',result:safeScore(x.result),answers:safeAnswers(x.answers)}));
   const result=safeScore(a.result)||history.at(-1)?.result||null;
   if(!result)continue;
   if(history.length===0&&a.completedAt)history.push({at:String(a.completedAt),result,answers:safeAnswers(a.answers)});
   out.assessments[type]={answers:safeAnswers(a.answers),result,completedAt:typeof a.completedAt==='string'?a.completedAt:'',history};
  }
  out.notes=Object.fromEntries(Object.entries(value.notes||{}).filter(([id,text])=>/^day-\d\d$/.test(id)&&typeof text==='string').map(([id,text])=>[id,text.slice(0,8000)]));
  out.conversation=safeObject(value.conversation)?value.conversation:{};
  return out;
 }
 function load(storage){try{const raw=storage.getItem(STORAGE_KEY);return raw?{data:sanitizeProgress(JSON.parse(raw)),error:null}:{data:init(),error:null};}catch(e){return {data:init(),error:'Не удалось прочитать сохранение. Старые данные не перезаписаны. Вы можете экспортировать их вручную через инструменты браузера.'};}}
 function persist(storage,data){storage.setItem(STORAGE_KEY,JSON.stringify(data));}
 function lessonState(data,day){const id=`day-${String(day).padStart(2,'0')}`;if(!data.lessons[id])data.lessons[id]={stage:0,doneStages:[],answers:{},speaking:{},writing:{},completedAt:null};return data.lessons[id];}
 function activity(data,date=localDate()){if(!data.activities.includes(date))data.activities.push(date);}
 function recordAnswer(data,day,id,isCorrect,skill,answer){const l=lessonState(data,day);const old=l.answers[id];const tries=(old?.tries||0)+1;
  l.answers[id]={correct:!!isCorrect,skill,answer,tries,updatedAt:new Date().toISOString()};data.attempts.push({id,day,correct:!!isCorrect,skill,at:new Date().toISOString()});data.attempts=data.attempts.slice(-3000);activity(data);return {firstCorrect:!!isCorrect&&!old?.correct,tries};}
 function markStage(data,day,stage){const l=lessonState(data,day);if(!l.doneStages.includes(stage))l.doneStages.push(stage);l.stage=Math.max(l.stage,Math.min(10,stage+1));activity(data);return l;}
 function completeLesson(data,day){const l=lessonState(data,day);if(!l.completedAt)l.completedAt=new Date().toISOString();l.stage=10;activity(data);return l;}
 function dueReview(record,today=localDate()){return !!record&&(!record.next||record.next<=today);}
 function review(record,rating,today=localDate()){
  if(![1,2,3,4].includes(rating))throw Error('Rating must be 1..4');
  const p=record?{...record,history:[...(record.history||[])]}:{repetitions:0,ease:2.5,interval:0,next:today,history:[]};
  if(rating===1){p.repetitions=0;p.interval=1;p.ease=Math.max(1.3,p.ease-.2);}
  else if(rating===2){p.repetitions=Math.max(1,p.repetitions);p.interval=p.interval<=1?1:Math.max(1,Math.round(p.interval*1.2));p.ease=Math.max(1.3,p.ease-.15);}
  else if(rating===3){p.repetitions+=1;p.interval=p.repetitions===1?1:p.repetitions===2?3:Math.max(4,Math.round(p.interval*p.ease));}
  else {p.repetitions+=1;p.ease=Math.min(3,p.ease+.12);p.interval=p.repetitions===1?4:p.repetitions===2?7:Math.max(8,Math.round(p.interval*p.ease*1.3));}
  p.interval=Math.max(1,Math.min(365,p.interval));p.next=addDays(today,p.interval);p.last=today;p.history.push({date:today,rating,interval:p.interval});p.history=p.history.slice(-60);return p;
 }
 function streak(dates,today=localDate()){const set=new Set(dates);let cursor=set.has(today)?today:addDays(today,-1);let n=0;while(set.has(cursor)&&n<2000){n++;cursor=addDays(cursor,-1);}return n;}
 function stats(data,content){const finished=content.lessons.filter(x=>data.lessons[x.id]?.completedAt).length;
  const attempted=data.attempts.length;const bestById=new Map();for(const [key,l]of Object.entries(data.lessons)) for(const [id,a]of Object.entries(l.answers||{}))bestById.set(`${key}:${id}`,a);
  const measured=[...bestById.values()].filter(x=>['reading','listening','grammar','vocabulary','workplace'].includes(x.skill));
  const correct=measured.filter(x=>x.correct).length;const accuracy=measured.length?Math.round(correct/measured.length*100):null;
  const practicedSpeaking=Object.values(data.lessons).filter(x=>x.speaking?.practised).length;
  const practicedWriting=Object.values(data.lessons).filter(x=>x.writing?.practised).length;
  const today=localDate();const due=Object.values(data.reviews).filter(x=>dueReview(x,today)).length;
  const totalReviewed=Object.keys(data.reviews).length;
  const mastery={};for(const skill of ['reading','listening','grammar','vocabulary','workplace']) {const subset=measured.filter(x=>x.skill===skill);mastery[skill]={count:subset.length,correct:subset.filter(x=>x.correct).length,pct:subset.length?Math.round(subset.filter(x=>x.correct).length/subset.length*100):null};}
  // XP granted once per successful exercise ID and once per completed stage; no rewards for simply opening the app.
  const uniqueSuccess=new Set(data.attempts.filter(x=>x.correct).map(x=>`${x.day}:${x.id}`));
  const stagePoints=Object.values(data.lessons).reduce((sum,l)=>sum+(l.doneStages?.length||0)*3,0);
  const xp=uniqueSuccess.size*10+stagePoints+finished*75+Object.values(data.reviews).reduce((sum,r)=>sum+(r.history?.length||0)*2,0);
  return {finished,attempted,correct,measured:measured.length,accuracy,practicedSpeaking,practicedWriting,due,totalReviewed,xp,streak:streak(data.activities,today),mastery};
 }
 function MC(id,skill,label,q){return {id,type:'choice',skill,label,q:q.q,options:q.options,answer:q.answer,explanation:q.explanation};}
 function getLessonExercises(l){const reading=l.readingChecks.map((q,i)=>MC(`${l.id}-reading-${i}`,'reading','Reading comprehension',q));
  const listening=l.listeningChecks.map((q,i)=>MC(`${l.id}-listening-${i}`,'listening','Listening comprehension',q));
  const grammar=[MC(`${l.id}-grammar`,'grammar','Grammar in context',l.grammarCheck), {id:`${l.id}-correction`,type:'self',skill:'grammar',label:'Error correction',q:`Correct this sentence: ${l.errorCorrection.incorrect}`,sample:l.errorCorrection.correct,explanation:l.errorCorrection.explanation}];
  const eligible=l.vocab.filter(v=>normalize(v.example).includes(normalize(v.term)));
  const fill=[];for(const v of [eligible[0],eligible[4]||eligible[1]].filter(Boolean)){
   const regex=new RegExp(v.term.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'),'i');
   const prompt=v.example.replace(regex,'__________');
   fill.push({id:`${l.id}-fill-${v.id}`,type:'fill',skill:'vocabulary',label:'Complete the sentence',q:prompt,answers:[v.term],explanation:`${v.term} — ${v.ru}. ${v.definition}`});
  }
  const terms=l.vocab.slice(2,6);const match={id:`${l.id}-match`,type:'match',skill:'vocabulary',label:'Match terms and meanings',items:terms.map(v=>({id:v.id,term:v.term,ru:v.ru}))};
  const phrase=l.phrases[0];const build={id:`${l.id}-builder`,type:'builder',skill:'workplace',label:'Build a useful phrase',q:phrase.ru,answer:phrase.en};
  const situation=MC(`${l.id}-situation`,'workplace','Professional decision',l.situational);
  const translation={id:`${l.id}-translation`,type:'self',skill:'writing',label:'Translate into English',q:l.phrases[1].ru,sample:l.phrases[1].en,explanation:'Several professional translations may be valid. Compare tone and meaning with this model.'};
  return {reading,listening,grammar,practice:[...fill,match,build,situation,translation]};
 }
 function achievements(data,content){const s=stats(data,content);return [
  {id:'first',icon:'spark',name:'First Steps',desc:'Завершить первый урок',earned:s.finished>=1},
  {id:'five',icon:'layers',name:'First Module',desc:'Завершить пять уроков',earned:s.finished>=5},
  {id:'streak',icon:'flame',name:'Consistent Learner',desc:'Три дня с учебной активностью подряд',earned:s.streak>=3},
  {id:'words',icon:'book',name:'Vocabulary Builder',desc:'Повторить не менее 30 карточек',earned:Object.values(data.reviews).reduce((n,x)=>n+(x.history?.length||0),0)>=30},
  {id:'voice',icon:'mic',name:'Conversation Starter',desc:'Отметить пять выполненных речевых практик',earned:s.practicedSpeaking>=5},
  {id:'all',icon:'award',name:'Course Completed',desc:'Завершить все 30 уроков',earned:s.finished===30},
 ];}
 function assessmentQuestions(content,type){return content.assessments[type]||[];}
 function assessmentScore(answers,questions){const valid=questions.filter(q=>Object.prototype.hasOwnProperty.call(answers||{},q.id));return {correct:valid.filter(q=>Number(answers[q.id])===q.answer).length,total:questions.length,answered:valid.length,pct:valid.length===questions.length?Math.round(100*valid.filter(q=>Number(answers[q.id])===q.answer).length/questions.length):null};}
 return {VERSION,STORAGE_KEY,stages,localDate,addDays,normalize,init,sanitizeProgress,load,persist,lessonState,activity,recordAnswer,markStage,completeLesson,dueReview,review,streak,stats,getLessonExercises,achievements,assessmentQuestions,assessmentScore};
});
