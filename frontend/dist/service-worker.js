if(!self.define){let s,e={};const i=(i,n)=>(i=new URL(i+".js",n).href,e[i]||new Promise((e=>{if("document"in self){const s=document.createElement("script");s.src=i,s.onload=e,document.head.appendChild(s)}else s=i,importScripts(i),e()})).then((()=>{let s=e[i];if(!s)throw new Error(`Module ${i} didn’t register its module`);return s})));self.define=(n,r)=>{const t=s||("document"in self?document.currentScript.src:"")||location.href;if(e[t])return;let c={};const l=s=>i(s,t),o={module:{uri:t},exports:c,require:l};e[t]=Promise.all(n.map((s=>o[s]||l(s)))).then((s=>(r(...s),c)))}}define(["./workbox-db5fc017"],(function(s){"use strict";s.setCacheNameDetails({prefix:"frontend"}),self.addEventListener("message",(s=>{s.data&&"SKIP_WAITING"===s.data.type&&self.skipWaiting()})),s.precacheAndRoute([{url:"/index.html",revision:"02aa2d3d8cb218f52d47aaec0d164032"},{url:"/manifest.json",revision:"4b14c64efaf846819b9a229b4193c8b7"},{url:"/robots.txt",revision:"b6216d61c03e6ce0c9aea6ca7808f7ca"},{url:"/static/css/899.4ffe13cc.css",revision:null},{url:"/static/css/chunk-vendors.cf2a4b9c.css",revision:null},{url:"/static/img/FRR.17adbd06.png",revision:null},{url:"/static/js/746.30cad5a8.js",revision:null},{url:"/static/js/899.c0ac2c92.js",revision:null},{url:"/static/js/app.45bb9818.js",revision:null},{url:"/static/js/chunk-vendors.af249de8.js",revision:null}],{})}));
//# sourceMappingURL=service-worker.js.map
