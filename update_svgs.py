import re

with open('c:/xampp/htdocs/ananya/index.php', 'r', encoding='utf-8') as f:
    html = f.read()

old_svg = r'<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>'
old_svg_form = r'<svg class="btn-icon-circle" width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>'

new_svg = """<svg width="34" height="34" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="17" cy="17" r="17" fill="white"/>
<path d="M9.5 26.5L24.5 11.5M24.5 22.75V11.5H13.25" stroke="#03428E" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

html = html.replace(old_svg, new_svg)
html = html.replace(old_svg_form, new_svg)

with open('c:/xampp/htdocs/ananya/index.php', 'w', encoding='utf-8') as f:
    f.write(html)

print("Replaced all arrow SVGs with the new design!")
