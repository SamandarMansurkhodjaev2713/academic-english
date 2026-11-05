const fs=require('node:fs'),path=require('node:path');const root=path.resolve(__dirname,'..'),dest=path.join(root,'dist');
fs.rmSync(dest,{recursive:true,force:true});fs.mkdirSync(dest,{recursive:true});
for(const file of ['index.html','assets/favicon.svg','assets/fonts/Manrope-Variable.ttf','assets/fonts/OFL-Manrope.txt','content/curriculum.json','content/curriculum.js','src/core.js','src/app.js','src/styles.css','sw.js']){
 const from=path.join(root,file),to=path.join(dest,file);if(!fs.existsSync(from))throw Error('Build missing '+file);fs.mkdirSync(path.dirname(to),{recursive:true});fs.copyFileSync(from,to);
}
const bytes=(dir)=>fs.readdirSync(dir,{withFileTypes:true}).reduce((n,x)=>n+(x.isDirectory()?bytes(path.join(dir,x.name)):fs.statSync(path.join(dir,x.name)).size),0);
console.log('Static production build ready:',dest,Math.round(bytes(dest)/1024)+' KiB');
