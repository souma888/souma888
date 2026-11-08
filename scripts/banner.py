"""A periodic interference field: every path returns exactly to its first frame."""
import math


def build_banner(svg):
    def wave(row, phase):
        pts = []
        for j in range(33):
            u = j / 32
            x = 738 + u * 525
            envelope = math.sin(math.pi * u) ** .85
            y = 112 + row * 12 + envelope * (
                38 * math.sin(u * math.pi * 2 - phase + row * .16)
                + 18 * math.sin(u * math.pi * 3 + phase + row * .09))
            pts.append(f'{x:.0f},{y:.1f}')
        return 'M' + ' L'.join(pts)

    body = '''<defs>
      <linearGradient id="bg" x2="1" y2="1"><stop stop-color="#100E19"/><stop offset="1" stop-color="#090C14"/></linearGradient>
      <linearGradient id="ink" x2="1" y2="1"><stop stop-color="#FAF7FF"/><stop offset="1" stop-color="#B8ABF3"/></linearGradient>
      <linearGradient id="field"><stop stop-color="#9C8AD7"/><stop offset=".5" stop-color="#C6B5FF"/><stop offset="1" stop-color="#70DBC9"/></linearGradient>
      <linearGradient id="mask"><stop stop-color="black"/><stop offset=".17" stop-color="white"/><stop offset=".86" stop-color="white"/><stop offset="1" stop-color="black"/></linearGradient>
      <mask id="edges"><rect x="730" y="50" width="540" height="350" fill="url(#mask)"/></mask>
      <radialGradient id="halo"><stop stop-color="#8C6DD9" stop-opacity=".14"/><stop offset="1" stop-color="#8C6DD9" stop-opacity="0"/></radialGradient>
    </defs>
    <style>.static-field{display:none}@media(prefers-reduced-motion:reduce){.moving-field{display:none}.static-field{display:inline}}</style>
    <rect x="1" y="1" width="1278" height="428" rx="22" fill="url(#bg)" stroke="#332C43"/>
    <circle cx="1000" cy="223" r="230" fill="url(#halo)"/>
    <path d="M40 64H1240M40 366H1240" stroke="#302A3D"/>
    <text class="mono" x="43" y="40" fill="#AC9AC6" font-size="13" letter-spacing="2">SOUMA888</text>
    <text class="mono" x="1238" y="40" text-anchor="end" fill="#AC9AC6" font-size="13" letter-spacing="1">IIT MANDI</text>
    <text x="39" y="184" fill="url(#ink)" font-size="100" font-weight="700" letter-spacing="-5">Soumadip</text>
    <text x="39" y="285" fill="url(#ink)" font-size="100" font-weight="700" letter-spacing="-5">Karan<tspan fill="#72D7C3">.</tspan></text>
    <text class="mono" x="44" y="328" fill="#A99DB9" font-size="16">Software development · Computer vision · Scientific computing</text>
    <text class="mono" x="43" y="403" fill="#A99DB9" font-size="12" letter-spacing="1">PYTHON / TYPESCRIPT / C++</text>
    <text class="mono" x="1238" y="403" text-anchor="end" fill="#A99DB9" font-size="12" letter-spacing="1">SIGNAL FIELD / 001</text>
    <g mask="url(#edges)" fill="none" stroke="url(#field)" stroke-width="1.4">'''
    paths = []
    for row in range(17):
        # Reusing the first string for the final frame guarantees a closed temporal loop.
        frames = [wave(row, t * 2 * math.pi / 32) for t in range(32)]
        frames.append(frames[0])
        paths.append((frames, .38 + .5 * math.sin(math.pi * row / 16)))
    body += '<g class="moving-field">'
    for frames, opacity in paths:
        body += f'<path d="{frames[0]}" opacity="{opacity:.2f}"><animate attributeName="d" dur="16s" repeatCount="indefinite" calcMode="linear" values="{";".join(frames)}"/></path>'
    body += '</g><g class="static-field">'
    for frames, opacity in paths:
        body += f'<path d="{frames[0]}" opacity="{opacity:.2f}"/>'
    body += '</g></g>'
    svg('banner.svg', 1280, 430, body, 'Soumadip Karan. IIT Mandi. Software development, computer vision, scientific computing. Animated interference field.')
