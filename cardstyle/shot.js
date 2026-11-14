// 사용: node cardstyle/shot.js <카드 html 경로> <저장 폴더>
// 섹션(.c)마다 1080×1080 PNG 를 01.png, 02.png … 로 저장한다.
const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
(async()=>{const [,,html,out]=process.argv;if(!html||!out){console.error('usage: node shot.js <html> <outdir>');process.exit(1)}
fs.mkdirSync(out,{recursive:true});const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1080}});
await p.goto('file://'+path.resolve(html));await p.waitForTimeout(600);
const miss=await p.evaluate(()=>[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.getAttribute('src')));
if(miss.length){console.error('[IMG_MISS]',miss.join(', '))}
const secs=await p.$$('section.c');let i=0;for(const s of secs){i++;await s.screenshot({path:path.join(out,String(i).padStart(2,'0')+'.png')})}
console.log('saved',i,'cards →',out);await b.close();if(miss.length)process.exit(2)})();
