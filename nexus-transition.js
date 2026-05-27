(function(){
  // ── Styles ──
  var S=document.createElement('style');
  S.textContent='#nx-overlay{position:fixed;inset:0;background:#000;z-index:99999;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;opacity:1;transition:opacity 0.45s ease;pointer-events:none;}#nx-overlay.blocking{pointer-events:all;}#nx-overlay.gone{opacity:0;}.nx-bar-wrap{width:240px;height:1px;background:rgba(0,200,255,0.1);position:relative;overflow:visible;}.nx-bar-fill{position:absolute;left:0;top:0;height:1px;width:0%;background:#00c8ff;box-shadow:0 0 8px rgba(0,200,255,0.9),0 0 18px rgba(0,200,255,0.4);transition:none;}.nx-st{font-family:"IBM Plex Mono",monospace;font-size:8px;letter-spacing:0.45em;color:rgba(0,200,255,0.38);text-transform:uppercase;}.nx-pc{font-family:"IBM Plex Mono",monospace;font-size:10px;letter-spacing:0.18em;color:rgba(0,200,255,0.55);}';
  document.head.appendChild(S);

  // ── Preload transition sound ──
  var _dep=window.location.pathname.split('/').filter(Boolean).length-1;
  var _root=_dep>0?new Array(_dep).fill('..').join('/')+'/':'';
  var _sfx=new Audio(_root+'wait_sound_3_seconds.wav');
  _sfx.preload='auto';_sfx.volume=0.1;

  // ── Overlay DOM ──
  var ov=document.createElement('div');
  ov.id='nx-overlay';
  ov.innerHTML='<div class="nx-st" id="nx-status">LOADING</div><div class="nx-bar-wrap"><div class="nx-bar-fill" id="nx-fill"></div></div><div class="nx-pc" id="nx-pct">0%</div>';
  document.body.insertBefore(ov,document.body.firstChild);

  var fill=document.getElementById('nx-fill');
  var pct=document.getElementById('nx-pct');
  var status=document.getElementById('nx-status');

  // ── Fade in on page load (overlay starts black, fades to clear) ──
  function fadeIn(){
    fill.style.width='0%';
    pct.textContent='';
    status.textContent='';
    setTimeout(function(){
      ov.classList.add('gone');
      setTimeout(function(){ ov.classList.remove('blocking'); },500);
    },80);
  }

  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded',function(){ setTimeout(fadeIn,60); });
  } else {
    setTimeout(fadeIn,60);
  }
  window.addEventListener('pageshow',function(e){ if(e.persisted) fadeIn(); });

  // ── Auto tab title from URL ──
  (function(){
    var p=window.location.pathname;
    var m=p.match(/lesson-(\d+)-(\d+)/);
    if(m){ document.title='Lesson '+m[1]+'.'+m[2]+' · NEXUS Academy'; return; }
    var mi=p.match(/module-(\d+)\/intro/);
    if(mi){ document.title='Module '+mi[1]+' Intro · NEXUS Academy'; return; }
    if(/pre-course\/module-intro/.test(p)||/pre-course\/ciro-intro/.test(p)){ document.title='Pre-Course Intro · NEXUS Academy'; return; }
    var mc=p.match(/module-(\d+)\/complete/);
    if(mc){ document.title='Module '+mc[1]+' Complete · NEXUS Academy'; return; }
    if(/pre-course\/complete/.test(p)){ document.title='Pre-Course Complete · NEXUS Academy'; return; }
  })();

  // ── Transition out ──
  function runTransition(href){
    ov.classList.remove('gone');
    ov.classList.add('blocking');
    fill.style.width='0%';
    pct.textContent='0%';
    status.textContent='LOADING';
    _sfx.currentTime=0;_sfx.play().catch(function(){});

    // 3 speed variants: [progress%, time_ms] keyframes
    var variants=[
      [[0,0],[18,550],[40,1200],[65,2000],[85,2600],[100,3000]],      // smooth
      [[0,0],[42,450],[43,950],[68,1500],[69,2000],[90,2500],[100,3000]], // stutter
      [[0,0],[12,700],[14,1400],[14,1900],[55,2300],[100,3000]]       // slow surge
    ];
    var kfs=variants[Math.floor(Math.random()*3)];
    var labels=['LOADING','SCANNING MEMORY','INITIALIZING'];
    var start=null,kfi=0;

    function tick(ts){
      if(!start) start=ts;
      var e=ts-start;
      status.textContent=labels[Math.min(Math.floor(e/1000),labels.length-1)];
      while(kfi<kfs.length-1&&e>=kfs[kfi+1][1]) kfi++;
      var c=kfs[kfi],n=kfs[Math.min(kfi+1,kfs.length-1)];
      var p=c===n?c[0]:c[0]+(n[0]-c[0])*Math.min(1,(e-c[1])/(n[1]-c[1]));
      fill.style.width=p.toFixed(1)+'%';
      pct.textContent=Math.round(p)+'%';
      if(e<kfs[kfs.length-1][1]){ requestAnimationFrame(tick); }
      else {
        fill.style.width='100%'; pct.textContent='100%';
        setTimeout(function(){ window.location.href=href; },120);
      }
    }
    requestAnimationFrame(tick);
  }

  window.nxTransit=runTransition;

  // ── Intercept anchor clicks ──
  document.addEventListener('click',function(ev){
    var a=ev.target.closest('a[href]');
    if(!a||a.hasAttribute('data-no-transit')) return;
    var href=a.getAttribute('href');
    if(!href||href.charAt(0)==='#'||/^(javascript|mailto|tel):/i.test(href)) return;
    if(/^https?:/i.test(href)) return;
    if(/lesson-\d+-\d+/.test(window.location.pathname)&&/lesson-\d+-\d+/.test(a.href)) return;
    ev.preventDefault();
    runTransition(a.href);
  });
})();
