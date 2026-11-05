const http=require('node:http'), fs=require('node:fs'), path=require('node:path');
const root=path.resolve(process.argv[2]||'.');const port=Number(process.env.PORT||4173);
const mime={'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.json':'application/json; charset=utf-8','.svg':'image/svg+xml','.png':'image/png','.txt':'text/plain; charset=utf-8'};
http.createServer((req,res)=>{
 let url;try{url=decodeURIComponent(new URL(req.url,'http://localhost').pathname)}catch{res.writeHead(400).end('Bad request');return;}
 const target=path.resolve(root,'.'+url,(url.endsWith('/')?'index.html':''));
 if(!(target===root||target.startsWith(root+path.sep))){res.writeHead(403).end('Forbidden');return;}
 fs.stat(target,(e,stat)=>{if(e||!stat.isFile()){res.writeHead(404).end('Not found');return;}res.setHeader('Content-Type',mime[path.extname(target)]||'application/octet-stream');res.setHeader('Cache-Control','no-store');fs.createReadStream(target).pipe(res);});
}).listen(port,'127.0.0.1',()=>console.log(`Academic English ready: http://localhost:${port}`));
