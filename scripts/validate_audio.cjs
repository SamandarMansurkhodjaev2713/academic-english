const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const root=path.resolve(__dirname,'..'), data=JSON.parse(fs.readFileSync(path.join(root,'content/curriculum.json'),'utf8'));
const context={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,'assets/audio-map.js'),'utf8'),context);
const map=context.window.ACADEMIC_AUDIO, missing=[];
function check(text,voice='en-GB-SoniaNeural') {const name=map[voice+'\n'+text];if(!name||!fs.existsSync(path.join(root,'assets/audio',name))||fs.statSync(path.join(root,'assets/audio',name)).size===0)missing.push(text);}
for(const lesson of data.lessons){for(const word of lesson.vocab)check(word.term);for(const phrase of lesson.phrases)check(phrase.en);check(lesson.speaking.prompt);lesson.dialogue.lines.forEach((line,i)=>check(line.text,i%2?'en-GB-RyanNeural':'en-GB-SoniaNeural'));}
if(missing.length){console.error('Missing audio:',missing.length,missing.slice(0,5));process.exit(1)}
console.log('Audio validated for all 30 lessons:',Object.keys(map).length,'clips');
