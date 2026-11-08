"""Consistent contact buttons: 24px icons, shared baseline and padding."""


def build_buttons(svg):
    icons = {
        'email': ('Email', '#FFAA8C', '<rect x="2" y="4" width="20" height="16" rx="3"/><path d="m3 6 9 7 9-7"/>'),
        'instagram': ('Instagram', '#C7B7FF', '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/>'),
        'whatsapp': ('WhatsApp', '#6BE4C3', '<path d="M20.1 11.8a8.1 8.1 0 0 1-12 7.1L3.5 20l1.2-4.4a8.1 8.1 0 1 1 15.4-3.8Z"/><path d="m9 8 1 2-1 1c1 2 2 3 4 4l1-1 2 1c0 2-2 2-3 1-3-1-5-3-6-6 0-1 0-2 2-2Z" stroke-width="1.4"/>'),
        'github': ('Repositories', '#C7D1E0', '<path d="M9 19c-4.3 1.3-4.3-2.2-6-2.7m12 5v-3.4a3 3 0 0 0-.8-2.3c2.7-.3 5.5-1.3 5.5-6A4.7 4.7 0 0 0 18.4 6a4.3 4.3 0 0 0-.1-3.6s-1-.3-3.5 1.3a12 12 0 0 0-6.4 0C6 2.1 4.9 2.4 4.9 2.4A4.3 4.3 0 0 0 4.8 6a4.7 4.7 0 0 0-1.3 3.3c0 4.7 2.8 5.7 5.5 6a3 3 0 0 0-.8 2.3v3.7"/>'),
    }
    for name, (label, color, icon) in icons.items():
        body = f'''<rect x="1" y="1" width="198" height="54" rx="12" fill="#152840" stroke="#3A5274"/>
        <rect x="13" y="12" width="32" height="32" rx="8" fill="{color}" fill-opacity=".09"/>
        <g transform="translate(17 16)" fill="none" color="{color}" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{icon}</g>
        <text x="59" y="29" dominant-baseline="middle" fill="#EEE9F7" font-size="16" font-weight="600">{label}</text>'''
        svg(f'contact-{name}.svg', 200, 56, body, label)
