"""Build the profile's custom vector artwork with no external assets."""
from pathlib import Path
from html import escape
import math

OUT = Path(__file__).resolve().parents[1] / 'assets'


def svg(name, w, h, body, label):
    (OUT / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label, quote=True)}"><style>text{{font-family:Arial,Helvetica,sans-serif}}.mono{{font-family:Consolas,monospace}}@media(prefers-reduced-motion:reduce){{.motion{{display:none}}}}</style>{body}</svg>', encoding='utf-8')


def build():
    rings = ''
    for angle in range(0, 180, 20):
        rings += f'<ellipse cx="994" cy="252" rx="155" ry="62" transform="rotate({angle} 994 252)" fill="none" stroke="#AE9AFF" stroke-opacity=".32"/>'
    body = '''<defs>
    <radialGradient id="glow"><stop stop-color="#7C3AED" stop-opacity=".5"/><stop offset="1" stop-color="#0C0B12" stop-opacity="0"/></radialGradient>
    <linearGradient id="type" x2="1" y2="1"><stop stop-color="#F4F0FF"/><stop offset=".5" stop-color="#C7B7FF"/><stop offset="1" stop-color="#FCA7C8"/></linearGradient>
    <linearGradient id="orbit"><stop stop-color="#FF8F70"/><stop offset="1" stop-color="#AA8AFF"/></linearGradient>
    </defs>
    <rect x="1" y="1" width="1278" height="478" rx="24" fill="#0C0B12" stroke="#352A48"/>
    <circle cx="995" cy="245" r="290" fill="url(#glow)"/>
    <path d="M32 73H1248M32 421H1248" stroke="#30253E"/>
    <circle cx="40" cy="40" r="5" fill="#FF8F70"/><circle cx="60" cy="40" r="5" fill="#C7B7FF"/><circle cx="80" cy="40" r="5" fill="#6BE4C3"/>
    <text class="mono" x="108" y="45" fill="#B9A9CD" font-size="14" letter-spacing="2">SOUMA888 / THE BUILDER'S LOG</text>
    <text class="mono" x="1240" y="45" text-anchor="end" fill="#AA8AFF" font-size="13">IIT MANDI · INDIA</text>
    <text x="44" y="142" fill="#FFAA8C" font-size="18" letter-spacing="6">SOUMADIP KARAN</text>
    <text x="39" y="237" fill="url(#type)" font-size="88" font-weight="900" letter-spacing="-5">Ideas into code.</text>
    <text x="43" y="313" fill="#F4F0FF" font-size="67" font-weight="800" letter-spacing="-3">Code into impact<tspan fill="#FF8F70">.</tspan></text>
    <text class="mono" x="47" y="369" fill="#B9A9CD" font-size="16">software engineer in the making / endlessly curious</text>
    <text class="mono" x="45" y="454" fill="#C7B7FF" font-size="13" letter-spacing="1">01 SOFTWARE</text>
    <text class="mono" x="288" y="454" fill="#FFAA8C" font-size="13" letter-spacing="1">02 APPLIED AI</text>
    <text class="mono" x="555" y="454" fill="#6BE4C3" font-size="13" letter-spacing="1">03 COMPUTATIONAL ENGINEERING</text>'''
    body += rings
    body += '''<ellipse cx="994" cy="252" rx="204" ry="49" transform="rotate(-28 994 252)" fill="none" stroke="url(#orbit)" stroke-width="2.5"/>
    <g class="motion"><circle r="5" fill="#FFAA8C"><animateMotion dur="9s" repeatCount="indefinite" path="M814 348 Q735 300 972 191 Q1238 107 1174 156 Q1264 183 1013 302 Q830 390 814 348"/></circle></g>
    <circle cx="994" cy="252" r="32" fill="#D0BFFF"/><text x="994" y="260" text-anchor="middle" fill="#25183D" font-size="23" font-weight="800">SK</text>
    <g transform="translate(1058 335) rotate(-6)"><rect width="153" height="44" rx="10" fill="#1C1429" stroke="#634589"/><text class="mono" x="17" y="28" fill="#6BE4C3" font-size="14">&gt; keep building_</text></g>
    <path d="M819 119v18m-9-9h18M1176 92v12m-6-6h12M1210 288v16m-8-8h16" stroke="#FFAA8C" stroke-width="2"/>
    <circle cx="821" cy="374" r="2" fill="#C7B7FF"/><circle cx="1150" cy="397" r="2" fill="#C7B7FF"/>'''
    svg('banner.svg',1280,480,body,'Soumadip Karan. Ideas into code. Code into impact. Software, applied AI, computational engineering. IIT Mandi.')

    svg('about.svg',1200,246,'''<rect x="1" y="1" width="1198" height="244" rx="18" fill="#100E18" stroke="#352A48"/>
    <path d="M620 28V218" stroke="#352A48"/>
    <text class="mono" x="30" y="39" fill="#756587" font-size="13">~/soumadip/about.ts</text>
    <g class="mono" font-size="19"><text x="30" y="83" fill="#C7B7FF">const <tspan fill="#F4F0FF">builder</tspan> = {</text>
    <text x="52" y="119" fill="#B9A9CD">education: <tspan fill="#6BE4C3">"General Engineering @ IIT Mandi"</tspan>,</text>
    <text x="52" y="155" fill="#B9A9CD">interests: <tspan fill="#FFAA8C">["software", "math", "AI"]</tspan>,</text>
    <text x="52" y="191" fill="#B9A9CD">approach: <tspan fill="#6BE4C3">"build, question, improve"</tspan></text>
    <text x="30" y="220" fill="#C7B7FF">};</text></g>
    <text x="655" y="59" fill="#FFAA8C" font-size="12" letter-spacing="3">WHAT DRIVES ME</text>
    <g fill="#EEE7FA" font-size="23" font-weight="600"><text x="655" y="102">Make the abstract interactive.</text><text x="655" y="139">Make the complex understandable.</text><text x="655" y="176">Make something worth using.</text></g>
    <text class="mono" x="655" y="215" fill="#9684AB" font-size="14">learning in public, one project at a time.</text>''','About Soumadip: General Engineering at IIT Mandi. Interested in software, mathematics, and AI. Build, question, improve.')

    sections=[('work','01','SELECTED WORK','five projects / different kinds of curiosity'),('stack','02','THE TOOLBOX','languages, frameworks & the things in between'),('activity','03','COMMIT FREQUENCY','a year of showing up')]
    for name,num,title,sub in sections:
        svg(f'{name}-heading.svg',1200,100,f'<text class="mono" x="2" y="49" fill="#FFAA8C" font-size="15">/{num}</text><text x="55" y="53" fill="#EDE5FA" font-size="34" font-weight="800" letter-spacing="-1">{title}</text><text class="mono" x="1198" y="50" text-anchor="end" fill="#9684AB" font-size="13">{escape(sub)}</text><path d="M2 80H1198" stroke="#352A48"/>',title)

    projects=[
        ('tastera','01','TASTERA','CROSS-MEDIA DISCOVERY','#C7B7FF',['Movies. Music. Books. A map of your taste.','Explainable discovery, personal libraries,','and pathways across the things you love.'],'React / TypeScript / FastAPI / PostgreSQL','PRODUCT'),
        ('vectora','02','Vectora','MATHEMATICS, MADE VISIBLE','#6BE4C3',['Turn matrices into something you can explore.','Transformations, decompositions, PCA, and','robotics through interactive experiments.'],'TypeScript / React / NumPy / FastAPI','WORKBENCH'),
        ('terrasight','03','TerraSight','FROM PIXELS TO TERRAIN','#FFAA8C',['Capture the terrain. Inspect the geometry.','Image-quality checks, local reconstruction,','and a point-cloud viewer with explicit limits.'],'Python / OpenCV / COLMAP / Three.js','IN DEVELOPMENT'),
        ('nexora','04','Nexora','THE ENGINEERING PLAYGROUND','#E9A8D5',['Change a parameter. Watch the physics respond.','An interactive lab spanning mechanics,','circuits, electronics, and signals.'],'TypeScript / Simulations / Visual solvers','IN DEVELOPMENT'),
        ('reparo','05','Reparo','REASON BEFORE YOU REPAIR','#C7B7FF',['Designing evidence-backed appliance troubleshooting.','Structured symptoms, uncertainty-aware guidance,','and a clear boundary between safe checks and expert help.'],'Applied AI / Retrieval / System design','CONCEPT & ARCHITECTURE')]
    for name,num,title,kicker,color,lines,stack,status in projects:
        w=1200 if name=='reparo' else 590
        body=f'<defs><linearGradient id="fade"><stop stop-color="{color}" stop-opacity=".12"/><stop offset="1" stop-color="{color}" stop-opacity="0"/></linearGradient></defs><rect x="1" y="1" width="{w-2}" height="268" rx="18" fill="#100E18" stroke="#352A48"/><rect x="2" y="2" width="{w-4}" height="105" rx="17" fill="url(#fade)"/><text class="mono" x="26" y="32" fill="{color}" font-size="11" letter-spacing="1.5">{kicker}</text><text x="24" y="86" fill="#F4F0FF" font-size="42" font-weight="800" letter-spacing="-1">{title}<tspan fill="{color}"> ↗</tspan></text><text class="mono" x="{w-27}" y="85" text-anchor="end" fill="{color}" opacity=".22" font-size="64" font-weight="700">{num}</text>'
        for i,line in enumerate(lines):
            body+=f'<text x="26" y="{125+i*25}" fill="#BBAECF" font-size="17">{escape(line)}</text>'
        body+=f'<path d="M26 197H{w-26}" stroke="#352A48"/><text class="mono" x="26" y="224" fill="{color}" font-size="12">{escape(stack)}</text><circle cx="30" cy="247" r="3" fill="{color}"/><text class="mono" x="40" y="251" fill="#9684AB" font-size="10" letter-spacing="1.3">{escape(status)}</text>'
        if name=='reparo':
            body+='<g transform="translate(940 112)" fill="none" stroke="#C7B7FF"><circle r="64" opacity=".25"/><circle r="44" opacity=".5" stroke-dasharray="5 6"/><path d="M-17 0l12 13 24-28" stroke-width="3"/><path d="M-100 0H-70M70 0H100M0-100V-70M0 70V100" opacity=".5"/></g><text class="mono" x="940" y="231" text-anchor="middle" fill="#9684AB" font-size="12">EVIDENCE → REASONING → GUIDANCE</text>'
        svg(f'project-{name}.svg',w,270,body,title+'. '+ ' '.join(lines)+' '+status+'. '+stack)

    svg('footer.svg',1200,180,'''<defs><linearGradient id="line"><stop stop-color="#C7B7FF"/><stop offset="1" stop-color="#FF8F70"/></linearGradient></defs><path d="M0 1H1200" stroke="url(#line)"/><text x="600" y="68" text-anchor="middle" fill="#F4F0FF" font-size="36" font-weight="800" letter-spacing="-1">Have an interesting problem? Let's talk.</text><text class="mono" x="600" y="111" text-anchor="middle" fill="#C7B7FF" font-size="20">soumadipkaran88@gmail.com ↗</text><text class="mono" x="600" y="157" text-anchor="middle" fill="#796889" font-size="12" letter-spacing="3">BUILT WITH CURIOSITY / ALWAYS A WORK IN PROGRESS</text>''','Contact Soumadip: soumadipkaran88@gmail.com. Have an interesting problem? Let us talk.')


if __name__ == '__main__':
    build()
