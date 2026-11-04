import os, base64
from playwright.sync_api import sync_playwright

OUT = "/home/box/novacapu/marketing/artes/2026-10-12_a_10-23"
LOGO = "file:///home/box/novacapu/assets/logo-oficial.png"
SELO = "file:///home/box/novacapu/assets/selo.webp"
Y, G, K, CINZA = "#FFBA00", "#373435", "#1A1A1A", "#5C5C5C"
FOOT = "Novacapu Corretora de Seguros · SUSEP 202048954 · CNPJ 22.208.705/0001-31"
WPP = "(92) 99146-9536"

FONTS = """
@font-face{font-family:'Fraunces';src:url('file:///usr/share/fonts/truetype/sand-box/google/Fraunces/Fraunces-VariableFont_SOFT,WONK,opsz,wght.ttf');font-weight:100 900;}
@font-face{font-family:'Inter';src:url('file:///usr/share/fonts/truetype/sand-box/google/Inter/Inter-VariableFont_opsz,wght.ttf');font-weight:100 900;}
"""

ICONS = {
 "truck": '<path d="M4 16h34v26H4z"/><path d="M38 26h12l9 11v5H38z"/><circle cx="15" cy="46" r="5"/><circle cx="48" cy="46" r="5"/>',
 "box": '<path d="M8 20l24-10 24 10v26L32 56 8 46z"/><path d="M8 20l24 10 24-10M32 30v26"/>',
 "boat": '<path d="M5 38h54l-9 12H14z"/><path d="M14 38V26h30v12M22 26v-9h12v9"/><path d="M4 57c5-3 9-3 14 0s9 3 14 0 9-3 14 0 9 3 14 0"/>',
 "plane": '<path d="M32 5c2 0 3.5 3 3.5 6.5V25L58 38v6l-22.5-7v11l7 5v5L32 55l-10.5 3v-5l7-5V37L6 44v-6l22.5-13V11.5C28.5 8 30 5 32 5z"/>',
 "multi": '<path d="M8 22h44M42 12l10 10-10 10"/><path d="M56 42H12M22 32L12 42l10 10"/>',
 "globe": '<circle cx="32" cy="32" r="25"/><ellipse cx="32" cy="32" rx="11" ry="25"/><path d="M7 32h50M11 19h42M11 45h42"/>',
 "car": '<path d="M7 42V32l7-13h36l7 13v10z"/><path d="M7 42v7h9v-7M48 42v7h9v-7M7 32h50"/><circle cx="16" cy="37" r="1.5"/><circle cx="48" cy="37" r="1.5"/>',
 "shield": '<path d="M32 5l22 8v17c0 14-9 24-22 29C19 54 10 44 10 30V13z"/><path d="M21 31l8 8 15-15"/>',
 "lockopen": '<rect x="12" y="28" width="40" height="28" rx="4"/><path d="M20 28V18a12 12 0 0 1 23-5"/><path d="M32 39v7"/>',
 "lock": '<rect x="12" y="28" width="40" height="28" rx="4"/><path d="M20 28V18a12 12 0 0 1 24 0v10"/><path d="M32 39v7"/>',
 "docseal": '<path d="M12 5h26l11 11v20M38 5v11h11M12 5v54h22"/><path d="M19 22h20M19 30h22M19 38h12"/><circle cx="46" cy="46" r="9"/><path d="M41 54l-2 8 7-3 7 3-2-8"/>',
 "money": '<rect x="5" y="17" width="54" height="30" rx="3"/><circle cx="32" cy="32" r="7"/><path d="M13 25v14M51 25v14"/>',
 "check": '<path d="M10 34l14 14 30-30"/>',
 "chat": '<path d="M32 7a25 25 0 0 0-21.6 37.6L7 57l12.8-3.3A25 25 0 1 0 32 7z"/><path d="M24 22c-2 0-4 3-2 8s6 9 11 11 8 0 8-2l-1-4-5-2-3 3c-3-1-6-4-7-7l3-3-2-5z"/>',
 "chart": '<path d="M8 56h48M14 48V34M26 48V24M38 48V30M50 48V14"/>',
 "star": '<path d="M32 6l7.6 16.5 18 2.1-13.3 12.3 3.6 17.8L32 45.8 16.1 54.7l3.6-17.8L6.4 24.6l18-2.1z"/>',
 "doc": '<path d="M14 5h26l10 10v44H14z"/><path d="M40 5v10h10M21 24h22M21 32h22M21 40h22M21 48h12"/>',
 "clock": '<circle cx="32" cy="32" r="25"/><path d="M32 18v15l10 6"/>',
 "pin": '<path d="M32 58S12 38 12 25a20 20 0 0 1 40 0c0 13-20 33-20 33z"/><circle cx="32" cy="25" r="7"/>',
}
def icon(name, size=96, color="currentColor", sw=3):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>'

BASE_CSS = FONTS + f"""
*{{box-sizing:border-box}}
html,body{{margin:0;padding:0}}
body{{font-family:'Inter',sans-serif;-webkit-font-smoothing:antialiased}}
.serif{{font-family:'Fraunces',serif;font-variation-settings:'SOFT' 0,'WONK' 0}}
.y{{color:{Y}}}
.hl{{background:{Y};color:{G};padding:0 .18em;border-radius:6px;box-decoration-break:clone;-webkit-box-decoration-break:clone}}
.slide{{position:relative;width:1080px;height:1350px;overflow:hidden;display:flex;flex-direction:column;padding:190px 96px 150px}}
.dark{{background:{G};color:#fff}}
.light{{background:#fff;color:{G}}}
.cream{{background:#F5F4F1;color:{G}}}
.yellow{{background:{Y};color:{G}}}
.top{{position:absolute;top:56px;left:96px;right:96px;display:flex;justify-content:space-between;align-items:center;z-index:5}}
.plate{{background:#fff;border-radius:14px;padding:12px 18px;display:inline-flex}}
.plate img{{height:52px;display:block}}
.light .plate,.cream .plate{{padding:0;background:none}}
.counter{{font-weight:700;font-size:24px;letter-spacing:.08em}}
.dark .counter{{color:rgba(255,255,255,.6)}} .light .counter,.cream .counter{{color:{CINZA}}} .yellow .counter{{color:{G}}}
.foot{{position:absolute;bottom:46px;left:96px;right:96px;text-align:center;font-size:20px;font-weight:500;letter-spacing:.02em;z-index:5}}
.dark .foot{{color:rgba(255,255,255,.62)}} .light .foot,.cream .foot{{color:{CINZA}}} .yellow .foot{{color:{G}}}
.disc{{font-size:20px;line-height:1.35;opacity:.75;text-align:center;margin-top:auto}}
.tri{{position:absolute;width:0;height:0;z-index:0}}
.content{{position:relative;z-index:2;flex:1;display:flex;flex-direction:column}}
.bar{{width:90px;height:10px;background:{Y};border-radius:5px;margin-bottom:34px}}
.swipe{{font-weight:700;font-size:26px;letter-spacing:.06em;display:flex;align-items:center;gap:12px}}
"""

def deco(theme):
    # triângulo da logo como elemento gráfico discreto (canto inferior direito)
    col = {"dark": "rgba(255,186,0,.10)", "light": "rgba(255,186,0,.18)", "cream": "rgba(255,186,0,.20)", "yellow": "rgba(55,52,53,.07)"}[theme]
    return f'<div class="tri" style="right:0;bottom:0;border-left:420px solid transparent;border-bottom:420px solid {col}"></div>'

def slide(theme, inner, counter=None, foot=True, extra_css="", plate=True):
    top = f'<div class="top"><span class="plate"><img src="{LOGO}"></span>' + (f'<span class="counter">{counter}</span>' if counter else '') + '</div>'
    f = f'<div class="foot">{FOOT}</div>' if foot else ''
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{extra_css}</style></head>
<body><div class="slide {theme}">{deco(theme)}{top}<div class="content">{inner}</div>{f}</div></body></html>"""

class Renderer:
    def __enter__(self):
        self.p = sync_playwright().start()
        self.b = self.p.chromium.launch(channel="chrome")
        return self
    def render(self, html, out, w=1080, h=1350):
        os.makedirs(os.path.dirname(out), exist_ok=True)
        tmp = "/workspace/novacapu_artes/_tmp.html"
        open(tmp, "w").write(html)
        pg = self.b.new_page(viewport={"width": w, "height": h})
        pg.goto("file://" + tmp)
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(150)
        # checagem de overflow: elementos que saem da área
        ov = pg.evaluate("""() => { const r=[]; document.querySelectorAll('.content *').forEach(e=>{ if(e.scrollWidth>e.clientWidth+2 && getComputedStyle(e).overflow!='visible') r.push(e.className)}); const c=document.querySelector('.content'); if(c && c.scrollHeight>c.clientHeight+2) r.push('CONTENT_OVERFLOW '+c.scrollHeight+'>'+c.clientHeight); return r;}""")
        if ov: print("WARN", out, ov)
        pg.screenshot(path=out)
        pg.close()
        print("ok", out)
    def __exit__(self, *a):
        self.b.close(); self.p.stop()
