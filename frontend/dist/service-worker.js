if(!self.define){let e,s={};const i=(i,n)=>(i=new URL(i+".js",n).href,s[i]||new Promise((s=>{if("document"in self){const e=document.createElement("script");e.src=i,e.onload=s,document.head.appendChild(e)}else e=i,importScripts(i),s()})).then((()=>{let e=s[i];if(!e)throw new Error(`Module ${i} didn’t register its module`);return e})));self.define=(n,r)=>{const t=e||("document"in self?document.currentScript.src:"")||location.href;if(s[t])return;let c={};const l=e=>i(e,t),o={module:{uri:t},exports:c,require:l};s[t]=Promise.all(n.map((e=>o[e]||l(e)))).then((e=>(r(...e),c)))}}define(["./workbox-db5fc017"],(function(e){"use strict";e.setCacheNameDetails({prefix:"frontend"}),self.addEventListener("message",(e=>{e.data&&"SKIP_WAITING"===e.data.type&&self.skipWaiting()})),e.precacheAndRoute([{url:"/index.html",revision:"9e1a23f08439f39bfbc2a6b99b17a6dc"},{url:"/manifest.json",revision:"4b14c64efaf846819b9a229b4193c8b7"},{url:"/robots.txt",revision:"b6216d61c03e6ce0c9aea6ca7808f7ca"},{url:"/static/css/59.4ffe13cc.css",revision:null},{url:"/static/css/chunk-vendors.b0250df5.css",revision:null},{url:"/static/img/FRR.17adbd06.png",revision:null},{url:"/static/js/59.5bc263a2.js",revision:null},{url:"/static/js/746.35daa82f.js",revision:null},{url:"/static/js/app.82973fee.js",revision:null},{url:"/static/js/chunk-vendors.7e68f1e5.js",revision:null}],{})}));
//# sourceMappingURL=service-worker.js.map
