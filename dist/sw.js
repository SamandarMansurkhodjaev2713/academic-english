/* Offline fallback scoped to this application. */
const CACHE='academic-english-offline-v2';
const STATIC=['./','./index.html','./src/styles.css','./src/core.js','./src/app.js','./content/curriculum.js','./content/curriculum.json','./assets/favicon.svg'];
self.addEventListener('install',event=>event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(STATIC)).then(()=>self.skipWaiting())));
self.addEventListener('activate',event=>event.waitUntil(Promise.all([caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('academic-english-offline-')&&k!==CACHE).map(k=>caches.delete(k)))),self.clients.claim()])));
self.addEventListener('fetch',event=>{
 const req=event.request, url=new URL(req.url);
 if(req.method!=='GET'||url.origin!==self.location.origin||!url.pathname.startsWith(new URL(self.registration.scope).pathname))return;
 event.respondWith(fetch(req).then(response=>{if(response.ok){const copy=response.clone();caches.open(CACHE).then(c=>c.put(req,copy));}return response;}).catch(()=>caches.match(req)));
});
