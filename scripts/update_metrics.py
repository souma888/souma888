"""Render a public-only GitHub dashboard; no third-party Python packages."""
import json
import os
from collections import Counter
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from urllib.request import Request, urlopen

OWNER = 'souma888'
ROOT = Path(__file__).resolve().parents[1]
COLORS = ['#C7B7FF', '#FFAA8C', '#6BE4C3', '#E9A8D5', '#74B9EE', '#C5A3ED']


def api(path):
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'souma888-profile'}
    token = os.environ.get('GH_TOKEN')
    if token:
        headers['Authorization'] = 'Bearer ' + token
    with urlopen(Request('https://api.github.com' + path, headers=headers), timeout=30) as response:
        return json.load(response)


def collect():
    repos = []
    page = 1
    while True:
        batch = api(f'/users/{OWNER}/repos?type=owner&per_page=100&page={page}')
        repos.extend(r for r in batch if not r.get('private') and not r.get('fork'))
        if len(batch) < 100:
            break
        page += 1
    languages = Counter()
    for repo in repos:
        languages.update(api(f'/repos/{OWNER}/{repo["name"]}/languages'))
    return repos, languages


def render(repos, languages):
    date = datetime.now(timezone.utc).strftime('%d %b %Y')
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="355" viewBox="0 0 1200 355" role="img" aria-labelledby="title desc">',
             '<title id="title">Public repository dashboard</title>',
             '<desc id="desc">Owned public repositories, languages, and public code size. Private repositories and forks are excluded.</desc>',
             '<rect x="1" y="1" width="1198" height="353" rx="16" fill="#13233B" stroke="#344C70"/>',
             '<g font-family="Segoe UI, Arial, sans-serif">',
             '<text x="36" y="41" fill="#C7B7FF" font-family="Consolas, monospace" font-size="12" letter-spacing="2">THE PUBLIC CODEBASE</text>',
             f'<text x="1164" y="41" text-anchor="end" fill="#9684AB" font-size="12">UPDATED {date.upper()} / UTC</text>']
    stats = [(len(repos), 'PUBLIC REPOSITORIES'),
             (len(languages), 'LANGUAGES'),
             (round(sum(languages.values()) / 1024), 'KiB OF PUBLIC CODE')]
    for i, (value, label) in enumerate(stats):
        x = 36 + i * 376
        parts += [f'<text x="{x}" y="113" fill="#F4F0FF" font-size="42" font-weight="600">{value:02d}</text>',
                  f'<text x="{x}" y="142" fill="#9684AB" font-size="12" letter-spacing="1.5">{label}</text>']
    parts += ['<path d="M36 169H1164" stroke="#344C70"/>',
              '<text x="36" y="207" fill="#EDE5FA" font-size="17" font-weight="600">Languages across my public code</text>']
    ranked = languages.most_common()
    shown = ranked[:5]
    if len(ranked) > 5:
        shown.append(('Other', sum(v for _, v in ranked[5:])))
    total = sum(languages.values())
    parts.append('<defs><clipPath id="bar"><rect x="36" y="229" width="1128" height="14" rx="7"/></clipPath></defs><g clip-path="url(#bar)">')
    cursor = 36.0
    for i, (_, count) in enumerate(shown):
        width = 1128 * count / total if total else 0
        parts.append(f'<rect x="{cursor:.3f}" y="229" width="{width:.3f}" height="14" fill="{COLORS[i]}"/>')
        cursor += width
    parts.append('</g>')
    for i, (name, count) in enumerate(shown):
        x = 36 + (i % 3) * 376
        y = 279 + (i // 3) * 34
        percentage = count / total * 100 if total else 0
        parts += [f'<circle cx="{x + 5}" cy="{y - 5}" r="5" fill="{COLORS[i]}"/>',
                  f'<text x="{x + 20}" y="{y}" fill="#BBAECF" font-size="14">{escape(name)} <tspan fill="#9684AB">{percentage:.1f}%</tspan></text>']
    if not shown:
        parts.append('<text x="36" y="279" fill="#9684AB" font-size="14">No public language data yet.</text>')
    parts.append('</g></svg>')
    return '\n'.join(parts) + '\n'


if __name__ == '__main__':
    repositories, language_bytes = collect()
    # Write only after every API request succeeds; retain the last good SVG on failure.
    (ROOT / 'assets' / 'github-metrics.svg').write_text(render(repositories, language_bytes), encoding='utf-8')
