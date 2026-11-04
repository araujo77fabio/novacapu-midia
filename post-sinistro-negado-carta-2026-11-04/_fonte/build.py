import sys,base64
sys.path.insert(0,"/home/box/novacapu/marketing/artes/2026-10-12_a_10-23/_fonte")
from common import FONTS
from playwright.sync_api import sync_playwright
OUT="/home/box/novacapu/marketing/artes/post-sinistro-negado-carta-2026-11-04"
LOGOD='data:image/png;base64,'+base64.b64encode(open('/home/box/novacapu/assets/logo-letras-escuras.png','rb').read()).decode()
LOGOL='data:image/webp;base64,'+base64.b64encode(open('/home/box/novacapu/assets/logo-letras-claras.webp','rb').read()).decode()
Y,G,K,C="#FFBA00","#373435","#1A1A1A","#5C5C5C"
FOOT="Novacapu Corretora de Seguros · SUSEP 202048954 · CNPJ 22.208.705/0001-31"
def hl(t): return f'<span class="hl">{t}</span>'
def b64(f): return 'data:image/jpeg;base64,'+base64.b64encode(open(OUT+'/_fonte/fotos/'+f,'rb').read()).decode()
P1=b64('carta.jpg');P3=P1
XI={"truck":'<path d="M4 16h34v28H4zM38 26h12l10 10v8H38z"/><circle cx="16" cy="48" r="5"/><circle cx="48" cy="48" r="5"/>',
 "alert":'<path d="M32 6L60 56H4z"/><path d="M32 24v14M32 46v2"/>',
 "doc":'<path d="M14 5h26l10 10v44H14z"/><path d="M40 5v10h10M21 24h22M21 32h22M21 40h12"/>',
 "chat":'<path d="M32 7a25 25 0 0 0-21.6 37.6L7 57l12.8-3.3A25 25 0 1 0 32 7z"/><path d="M24 22c-2 0-4 3-2 8s6 9 11 11 8 0 8-2l-1-4-5-2-3 3c-3-1-6-4-7-7l3-3-2-5z"/>'}
def icon(n,size=52,color=G): return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">{XI[n]}</svg>'
def card(ic,t,d): return f'<div class="card"><div class="ib">{icon(ic)}</div><div><b>{t}</b><br><span>{d}</span></div></div>'
def dcard(t): return f'<div class="dcard">{t}</div>'
N=5
S=[
 ("dark photo1",'<div class="bar"></div><div class="kick">Sinistro negado</div><h1 style="font-size:78px">A carta chegou. O que fazer nos primeiros '+hl('10 minutos')+'?</h1>','<div class="swipe">ARRASTE PARA O LADO →</div>'),
 ("light",'<div class="bar"></div><div class="kick dk">Minuto 1–3</div><h1 class="dk" style="font-size:80px">Respire e leia<br>o '+hl('motivo')+'</h1><p class="sub">Anote o fundamento da negativa: cláusula, documentação ou prazo. Não rasgue nem ignore a carta.</p>',''),
 ("dark",'<div class="bar"></div><div class="kick">Minuto 4–7</div><h1 style="font-size:80px">Separe apólice<br>+ '+hl('provas')+'</h1>'+dcard('Apólice e condições gerais')+dcard('Fotos e notas fiscais')+dcard('Protocolo / e-mail da seguradora'),''),
 ("light",'<div class="bar"></div><div class="kick dk">Minuto 8–10</div><h1 class="dk" style="font-size:76px">Peça uma<br>'+hl('leitura técnica')+'</h1>'+card("doc","Análise inicial gratuita","revisamos carta, apólice e provas")+card("chat","Mesmo se o seguro não foi feito conosco","sem promessa de reversão"),''),
 ("light",'<div class="bar"></div><div class="kick dk">Novacapu Seguros</div><h1 class="dk" style="font-size:80px">Quer essa<br>'+hl('análise')+'?</h1><div class="wpp" style="font-size:48px;color:#373435">'+icon("chat",64,G)+'<div><b>(92) 99146-9536</b><br><small style="color:#5C5C5C">WhatsApp · seg a sex, 09h–17h</small></div></div>','<p class="disc" style="color:#5C5C5C">A análise é avaliação técnica do caso e não garante a reversão da negativa. Material informativo. Imagem gerada por IA (ilustrativa).</p>'),
]
H=1080
def html(i,kind,body,bottom):
  ph=kind.split()[1] if ' ' in kind else '';kind=kind.split()[0]
  bg,fg={"dark":(G,"#fff"),"light":("#fff",G),"yellow":(Y,G)}[kind]
  phc=''
  if ph=='photo1': phc=f'<div style="position:absolute;inset:0;background:url({P1}) center/cover"></div><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(55,52,53,0) 0%,rgba(55,52,53,0) 30%,rgba(55,52,53,.92) 46%,{G} 62%)"></div>'
  if ph=='photo3': phc=f'<div style="position:absolute;inset:0;background:url({P3}) center/cover"></div><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(55,52,53,.35) 0%,rgba(55,52,53,.88) 45%,{G} 75%)"></div>'
  pos=('bottom:'+str(190 if ph=='photo1' else 110)+'px;transform:scale(.84);transform-origin:left bottom') if ph else 'top:52%;transform:translateY(-50%) scale(.84);transform-origin:left center'
  return f"""<html><head><style>{FONTS}
*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:{H}px;background:{bg};color:{fg};font-family:Inter;position:relative;overflow:hidden}}
.tri{{position:absolute;right:0;bottom:0;width:0;height:0;border-left:420px solid transparent;border-bottom:420px solid {G if kind=='yellow' else Y};opacity:{.18 if kind!='light' else .35}}}
.logo{{position:absolute;left:96px;top:56px}}.logo img{{height:64px;display:block}}
.num{{position:absolute;right:96px;top:80px;font-weight:700;font-size:24px;color:{'#bbb' if kind=='dark' else C}}}
.main{{position:absolute;left:96px;right:96px;{pos}}}
.bar{{width:90px;height:8px;background:{Y};border-radius:4px;margin-bottom:34px}}
.kick{{color:{Y};font-weight:700;font-size:38px;margin-bottom:22px}}.kick.dk{{color:{C}}}
h1{{font-family:Fraunces;font-weight:800;font-size:84px;line-height:1.08;letter-spacing:-1px}}h1.big{{font-size:180px}}
.hl{{background:{Y};color:{G};padding:0 14px;border-radius:4px;-webkit-box-decoration-break:clone}}
.sub{{font-size:36px;line-height:1.4;margin-top:36px;color:{'#ddd' if kind=='dark' else C};max-width:860px}}
ul{{margin-top:36px;padding-left:0;list-style:none}}li{{font-size:36px;line-height:1.35;margin:22px 0;padding-left:46px;position:relative;color:{C}}}li:before{{content:'';position:absolute;left:0;top:14px;width:22px;height:22px;background:{Y};border-radius:4px}}
.wpp{{margin-top:50px;display:flex;align-items:center;gap:26px}}.wpp small{{font-size:30px}}
.bottom{{position:absolute;left:96px;right:96px;bottom:90px}}
.swipe{{color:{Y};font-weight:800;font-size:26px;letter-spacing:1px}}.disc{{font-size:24px;line-height:1.4;max-width:820px}}
.card{{display:flex;gap:30px;align-items:center;background:#fff;border:2px solid #e4e4e4;box-shadow:0 10px 26px rgba(0,0,0,.10);border-left:10px solid {Y};border-radius:20px;padding:30px 34px;margin-top:38px;font-size:34px;color:{G}}}.card span{{color:{C};font-size:29px}}.ib{{background:{Y};border-radius:14px;padding:12px;display:flex}}
.dl{{margin-top:30px}}.dcard{{background:rgba(255,255,255,.07);border:2px solid rgba(255,255,255,.18);border-left:10px solid {Y};border-radius:18px;padding:24px 34px;margin-top:22px;font-size:36px;color:#fff;font-weight:600}}
.foot{{position:absolute;left:0;right:0;bottom:36px;text-align:center;font-size:21px;color:{'#bbb' if kind=='dark' else C}}}
</style></head><body>{phc}{'' if i==N else '<div class="tri"></div>'}<div class="logo" style="{'background:#fff;padding:12px 20px;border-radius:12px;top:44px' if ph=='photo1' else ''}"><img src="{LOGOL if kind=='dark' and ph!='photo1' else LOGOD}"></div><div class="num" style="{'background:#fff;padding:6px 14px;border-radius:8px' if ph=='photo1' else ''}">0{i}/0{N}</div>
<div class="main">{body}</div><div class="bottom">{bottom}</div><div class="foot">{FOOT}</div></body></html>"""
with sync_playwright() as p:
  b=p.chromium.launch(channel="chrome"); pg=b.new_page(viewport={"width":1080,"height":H})
  for i,(k,bd,bt) in enumerate(S,1):
    pg.set_content(html(i,k,bd,bt)); pg.wait_for_timeout(300)
    print(i,pg.evaluate("(()=>{const m=document.querySelector('.main').getBoundingClientRect();const b=document.querySelector('.bottom').getBoundingClientRect();return [Math.round(m.top),Math.round(m.bottom),Math.round(b.top)]})()"))
    pg.screenshot(path=f"{OUT}/slide-0{i}.png")
  b.close()
from PIL import Image
w=h=360;c=Image.new("RGB",(N*(w+10)+10,h+20),"#ddd")
for i in range(N): c.paste(Image.open(f"{OUT}/slide-0{i+1}.png").resize((w,h)),(10+i*(w+10),10))
c.save(f"{OUT}/_previa-1080x1080.png")
