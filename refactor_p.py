import re

with open('c:/xampp/htdocs/ananya/index.php', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(' class=\"feature-desc\"', '')
content = content.replace(' class=\"feature-desc-sm\"', '')

with open('c:/xampp/htdocs/ananya/index.php', 'w', encoding='utf-8') as f:
    f.write(content)

with open('c:/xampp/htdocs/ananya/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if 'p {\n    font-size: 15px;\n    color: #777;\n    line-height: 1.6;\n    margin-bottom: 0;\n}' not in css:
    css = css.replace('body {\n    font-family: \'Inter\', sans-serif;\n    color: #111;\n    line-height: 1.6;\n}', 'body {\n    font-family: \'Inter\', sans-serif;\n    color: #111;\n    line-height: 1.6;\n}\n\np {\n    font-size: 15px;\n    color: #777;\n    line-height: 1.6;\n    margin-bottom: 0;\n}')
    with open('c:/xampp/htdocs/ananya/style.css', 'w', encoding='utf-8') as f:
        f.write(css)

print("Removed p classes and added global p style")
