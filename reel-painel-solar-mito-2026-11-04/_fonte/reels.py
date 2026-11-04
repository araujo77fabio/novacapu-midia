import os, re, sys, subprocess, shutil
from common import *
D = "/home/box/novacapu/marketing/artes/reel-painel-solar-mito-2026-11-04"
os.makedirs(D, exist_ok=True)
FPS = 30
DUR = 38.0

def words(line):
    out = []
    for tok in re.findall(r'\*[^*]+\*\S*|\S+', line):
        if tok.startswith('*'):
            m = re.match(r'\*([^*]+)\*(\S*)', tok); ws = m.group(1).split()
            for j, w in enumerate(ws):
                tail = m.group(2) if j == len(ws) - 1 else ""
                out.append(f'<span class="w"><span class="k">{w}</span>{tail}</span>')
        else: out.append(f'<span class="w">{tok}</span>')
    return " ".join(out)

def cap(lines, size=66):
    return "".join(f'<p class="cap" style="font-size:{size}px"><span class="tarja">{words(l)}</span></p>' for l in lines)

PHOTO = "file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), "fotos/painel.jpg"))
MITO = '<div class="pop" style="text-align:center;margin-bottom:60px"><span style="display:inline-block;border:8px solid #FFBA00;color:#FFBA00;font:900 64px Inter;letter-spacing:.08em;padding:6px 30px;border-radius:14px;transform:rotate(-6deg);background:rgba(26,26,26,.8)">MITO?</span></div>'
SEGS = [
  (0.0, 4.5, MITO + cap(["\u201cSeguro residencial *NÃO cobre* painel solar\u201d"], 80) + cap(["Você já ouviu isso?"], 54)),
  (4.5, 10.0, cap(["Será?"], 120) + cap(["*Depende.*"], 120)),
  (10.0, 20.0, cap(["Painel solar costuma ser um bem de *alto valor*.", "Em muitas apólices residenciais, ele só entra com *endosso* ou cláusula específica — ou fica de fora.", "Cada apólice é uma."], 60)),
  (20.0, 28.0, cap(["Antes de assumir que está coberto:", "*revise a apólice* e o que está declarado, com um *corretor independente*."], 66)),
  (28.0, 33.0, cap(["Seu painel está na apólice?", "Comente *PAINEL* ou chame no WhatsApp"], 64) + f'<div class="pop" style="margin-top:50px;display:inline-flex;align-items:center;gap:22px;background:{Y};color:{G};font:900 66px Inter;padding:28px 44px;border-radius:999px">{icon("chat",70,G,3.6)}(92) 99146-9536</div>'),
  (33.0, DUR + 1, f'''<div class="pop" style="text-align:center"><span style="background:#fff;border-radius:22px;padding:26px 34px;display:inline-flex"><img src="{LOGO}" style="height:120px;display:block"></span></div>
     <div class="pop" style="text-align:center;margin-top:90px;font:600 48px Inter;color:#fff">Revise seu seguro residencial com a <span style="color:#FFBA00">Novacapu</span></div>
     <div class="pop" style="text-align:center;margin-top:50px"><span style="display:inline-flex;align-items:center;gap:22px;background:{Y};color:{G};font:900 64px Inter;padding:26px 44px;border-radius:999px">{icon("chat",66,G,3.6)}(92) 99146-9536</span></div>
     <div class="pop" style="text-align:center;margin-top:36px;font:600 44px Inter;color:#fff">WhatsApp · seg a sex, 09h às 17h</div>
     <div class="pop" style="text-align:center;margin-top:70px;font:400 28px Inter;color:rgba(255,255,255,.75);line-height:1.4">Material informativo; coberturas conforme apólice;<br>sujeito a análise da seguradora.<br>Análise/cotação não garante cobertura. Imagem gerada por IA.</div>'''),
]
segs_html = "".join(f'<div class="seg" data-s="{s}" data-e="{e}">{h}</div>' for s, e, h in SEGS)
HTML = f"""<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}
body{{width:1080px;height:1920px;overflow:hidden;background:{K}}}
.stage{{position:relative;width:1080px;height:1920px;overflow:hidden;background:radial-gradient(ellipse at 50% 35%,#2b292a 0%,{K} 70%)}}
.shape{{position:absolute;width:0;height:0}}
.seg{{position:absolute;left:96px;right:120px;top:360px;height:1060px;display:flex;flex-direction:column;justify-content:center;opacity:0}}
.cap{{margin:0 0 34px;font-family:Inter;font-weight:800;line-height:1.42;color:#fff}}
.tarja{{background:{G};padding:6px 18px;border-radius:10px;box-decoration-break:clone;-webkit-box-decoration-break:clone}}
.w{{display:inline-block;opacity:0}}
.k{{color:{Y}}}
.pop{{opacity:0}}
.logo-top{{position:absolute;top:230px;left:50%;transform:translateX(-50%);background:#fff;border-radius:14px;padding:12px 18px;display:flex}}
.logo-top img{{height:54px;display:block}}
.reelfoot{{position:absolute;left:60px;right:60px;top:1450px;text-align:center;font:500 25px Inter;color:rgba(255,255,255,.72)}}
.prog{{position:absolute;left:0;top:0;height:8px;background:{Y}}}
</style></head><body><div class="stage">
<div class="shape" id="t1" style="left:-80px;top:1500px;border-left:520px solid rgba(255,186,0,.10);border-top:520px solid transparent"></div>
<div class="shape" id="t2" style="right:-60px;top:80px;border-right:380px solid rgba(255,186,0,.08);border-bottom:380px solid transparent"></div>
<div id="bg" style="position:absolute;inset:0;background:linear-gradient(rgba(26,26,26,.72),rgba(26,26,26,.86)),url({PHOTO}) center/cover"></div>
<div class="prog" id="prog"></div>
<div class="logo-top" id="logotop"><img src="{LOGO}"></div>
{segs_html}
<div class="reelfoot">{FOOT}</div>
</div>
<script>
const ease=x=>1-Math.pow(1-Math.min(Math.max(x,0),1),3);
function setTime(t){{
  document.getElementById('bg').style.opacity=Math.max(0.0,1-Math.max(0,t-9)/1.0)*1;document.getElementById('bg').style.transform=`scale(${{1.05+t*0.004}})`;
  document.getElementById('prog').style.width=(t/{DUR}*1080)+'px';
  document.getElementById('t1').style.transform=`translateY(${{-Math.sin(t/6)*40}}px)`;
  document.getElementById('t2').style.transform=`translateY(${{Math.sin(t/5)*30}}px)`;
  const endScreen = t>=33.0;
  document.getElementById('logotop').style.opacity = endScreen ? Math.max(0,1-(t-33)/0.4) : 1;
  document.querySelectorAll('.seg').forEach(seg=>{{
    const s=+seg.dataset.s, e=+seg.dataset.e;
    let o = (t<s||t>=e)?0: Math.min(1,(t-s)/0.25, (e-t)/0.3);
    seg.style.opacity=o; seg.style.display = o>0?'flex':'none';
    if(o<=0) return;
    const items=[...seg.querySelectorAll('.w, .pop')];
    // palavras e blocos entram em sequência
    let cur=s+0.15;
    items.forEach(el=>{{
      const st=cur; cur += el.classList.contains('w')?0.09:0.4;
      const p=ease((t-st)/0.28);
      el.style.opacity=p; el.style.transform=`translateY(${{(1-p)*24}}px)`;
    }});
  }});
}}
</script></body></html>"""

def main(preview=False):
    tmp = "/workspace/painel_tmp/_reels.html"; open(tmp, "w").write(HTML)
    fr = "/workspace/painel_tmp/frames"
    if not preview:
        shutil.rmtree(fr, ignore_errors=True); os.makedirs(fr)
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        pg.goto("file://" + tmp); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
        if preview:
            for t in [0.0,3.0, 8.0, 17.0, 26.0, 31.0, 37.0]:
                pg.evaluate(f"setTime({t})"); pg.screenshot(path=f"/workspace/painel_tmp/rv_{t:05.1f}.png")
        else:
            n = int(DUR * FPS)
            for i in range(n):
                pg.evaluate(f"setTime({i / FPS})")
                pg.screenshot(path=f"{fr}/f{i:05d}.jpg", type="jpeg", quality=95)
                if i % 150 == 0: print("frame", i, flush=True)
        b.close()
    pg2=None
    if not preview:
        out = f"{D}/reels.mp4"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{fr}/f%05d.jpg",
                        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
                        "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS),
                        "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", out], check=True)
        print("video", out)

if __name__ == "__main__":
    main(preview="preview" in sys.argv)
