import re

files = [
    'c:/xampp/htdocs/ananya/header.php',
    'c:/xampp/htdocs/ananya/footer.php',
    'c:/xampp/htdocs/ananya/index.php'
]

def add_title(match):
    img_tag = match.group(0)
    if 'title=' in img_tag:
        return img_tag
    
    alt_match = re.search(r'alt=\"([^\"]+)\"', img_tag)
    if alt_match:
        alt_text = alt_match.group(1)
        # insert title right after alt
        return img_tag.replace(f'alt="{alt_text}"', f'alt="{alt_text}" title="{alt_text}"')
    return img_tag

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(r'<img [^>]+>', add_title, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Added title attribute to all images.")
