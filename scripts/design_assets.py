"""Build the profile's custom vector artwork with no external assets."""
from pathlib import Path
from html import escape
import math

OUT = Path(__file__).resolve().parents[1] / 'assets'


def svg(name, w, h, body, label):
    (OUT / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label, quote=True)}"><style>text{{font-family:Arial,Helvetica,sans-serif}}.mono{{font-family:Consolas,monospace}}@media(prefers-reduced-motion:reduce){{.motion{{display:none}}}}</style>{body}</svg>', encoding='utf-8')


def build():
    from banner import build_banner
    build_banner(svg)
    from contact_buttons import build_buttons
    build_buttons(svg)
    svg('about.svg',1200,120,'''<rect x="1" y="1" width="1198" height="118" rx="14" fill="#100E18" stroke="#352A48"/>
    <text x="30" y="48" fill="#EDE5FA" font-size="23">Student at IIT Mandi. Working on software, AI/ML, and computer vision.</text>
    <text x="30" y="84" fill="#A99DB9" font-size="18">Recent projects: media discovery, terrain reconstruction, and interactive engineering labs.</text>''','Student at IIT Mandi. Software, AI/ML, and computer vision. Media discovery, terrain reconstruction, and interactive engineering labs.')

    sections=[('work','01','SELECTED WORK','5 public repositories'),('stack','02','THE TOOLBOX','languages & frameworks'),('activity','03','COMMIT FREQUENCY','last 12 months')]
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

    svg('footer.svg',1200,180,'''<defs><linearGradient id="line"><stop stop-color="#C7B7FF"/><stop offset="1" stop-color="#FF8F70"/></linearGradient></defs><path d="M0 1H1200" stroke="url(#line)"/><text x="600" y="68" text-anchor="middle" fill="#F4F0FF" font-size="36" font-weight="800" letter-spacing="-1">Contact</text><text class="mono" x="600" y="111" text-anchor="middle" fill="#C7B7FF" font-size="20">soumadipkaran88@gmail.com ↗</text><text class="mono" x="600" y="157" text-anchor="middle" fill="#796889" font-size="12" letter-spacing="3">EMAIL / INSTAGRAM / WHATSAPP</text>''','Contact Soumadip: soumadipkaran88@gmail.com.')


if __name__ == '__main__':
    build()
