"""Render the user's real public GitHub calendar as a constellation."""
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen


class Calendar(HTMLParser):
    def __init__(self):
        super().__init__()
        self.days = {}

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if 'data-date' in data and 'data-level' in data:
            self.days[data['data-date']] = int(data['data-level'])


def generate():
    req = Request('https://github.com/users/souma888/contributions', headers={'User-Agent': 'souma888-profile'})
    with urlopen(req, timeout=30) as response:
        html = response.read().decode('utf-8')
    calendar = Calendar()
    calendar.feed(html)
    days = sorted(calendar.days.items())
    if len(days) < 300:
        raise ValueError('Incomplete contribution calendar; keeping the last good image')
    first = datetime.strptime(days[0][0], '%Y-%m-%d').date()
    offset = (first.weekday() + 1) % 7
    colors = ['#1B3050', '#37517E', '#8260B4', '#B593EC', '#E0C7FF']
    active = sum(level > 0 for _, level in days)
    s = ['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-label="Real GitHub contribution activity, last year. Higher intensity means more contributions.">',
         '<rect x="1" y="1" width="1198" height="298" rx="18" fill="#13233B" stroke="#344C70"/>',
         '<g font-family="Consolas,monospace"><text x="30" y="38" fill="#C7B7FF" font-size="13" letter-spacing="2">THE CONTRIBUTION CONSTELLATION</text>',
         f'<text x="1170" y="38" text-anchor="end" fill="#FFAA8C" font-size="13">{active} ACTIVE DAYS / LAST YEAR</text>']
    for i, (day, level) in enumerate(days):
        pos = i + offset
        x, y = 48 + (pos // 7) * 21, 82 + (pos % 7) * 21
        r = 4 if level == 0 else 4.5 + level * .4
        s.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{colors[level]}"><title>{day}: activity level {level} of 4</title></circle>')
        if level == 4:
            s.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{colors[level]}" opacity=".1"/>')
    s += ['<path d="M30 245H1170" stroke="#344C70"/>',
          f'<text x="30" y="276" fill="#9684AB" font-size="12">{days[0][0]} → {days[-1][0]} / public GitHub contribution calendar</text>',
          '<text x="977" y="276" fill="#9684AB" font-size="12">LESS</text>']
    for i, color in enumerate(colors):
        s.append(f'<circle cx="{1030+i*21}" cy="272" r="5" fill="{color}"/>')
    s.append('<text x="1142" y="276" fill="#9684AB" font-size="12">MORE</text></g></svg>')
    (Path(__file__).resolve().parents[1] / 'assets/contributions.svg').write_text('\n'.join(s), encoding='utf-8')


if __name__ == '__main__':
    generate()
