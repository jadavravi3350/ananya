import re

# Update style.css
with open('c:/xampp/htdocs/ananya/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .section-title h2 with .title_66
css = re.sub(
    r'\.section-title h2\s*\{[^}]*\}',
    r'.title_66 {\n    font-size: 66px;\n    line-height: 76px;\n    color: var(--primary-blue-dark);\n    font-weight: 300;\n    margin-bottom: 20px;\n}',
    css,
    flags=re.DOTALL
)

# Remove extra admissions title classes
css = re.sub(r'\.admissions-title-top\s*\{[^}]*\}\s*', '', css)
css = re.sub(r'\.admissions-title-bottom\s*\{[^}]*\}\s*', '', css)

with open('c:/xampp/htdocs/ananya/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update index.php
with open('c:/xampp/htdocs/ananya/index.php', 'r', encoding='utf-8') as f:
    html = f.read()

# For standard <h2> inside .section-title, they currently don't have a class.
# So replace <h2> with <h2 class="title_66">
html = re.sub(r'<h2>', r'<h2 class="title_66">', html)

# For the admissions ones:
html = html.replace('<h2 class="admissions-title-top">', '<h2 class="title_66 mb-0 text-white">')
html = html.replace('<h2 class="italic-serif admissions-title-bottom">', '<h2 class="title_66 italic-serif text-white">')

with open('c:/xampp/htdocs/ananya/index.php', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated h2 classes and removed redundant CSS.")
