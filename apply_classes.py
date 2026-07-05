import re

with open('c:/xampp/htdocs/ananya/index.php', 'r', encoding='utf-8') as f:
    html = f.read()

# Apply title_white_24 to <h3> tags inside .card-overlay
# The pattern looks for <div class="card-overlay"> followed by <h3>
# We can just match <h3> where we know it's a 24px title.
html = re.sub(r'<div class="card-overlay">\s*<h3>', '<div class="card-overlay">\n                            <h3 class="title_white_24">', html)

# Some are nested deeper, like in the footer or different indentation
html = html.replace('<h3>Clubs & Activities</h3>', '<h3 class="title_white_24">Clubs & Activities</h3>')
html = html.replace('<h3>Arts & Crafts</h3>', '<h3 class="title_white_24">Arts & Crafts</h3>')
html = html.replace('<h3>Celebrations & Events</h3>', '<h3 class="title_white_24">Celebrations & Events</h3>')
html = html.replace('<h3>Sports & Games</h3>', '<h3 class="title_white_24">Sports & Games</h3>')
html = html.replace('<h3>Our Story</h3>', '<h3 class="title_white_24">Our Story</h3>')

with open('c:/xampp/htdocs/ananya/index.php', 'w', encoding='utf-8') as f:
    f.write(html)
