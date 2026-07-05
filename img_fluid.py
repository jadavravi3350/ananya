import re

files = [
    'c:/xampp/htdocs/ananya/index.php',
    'c:/xampp/htdocs/ananya/header.php',
    'c:/xampp/htdocs/ananya/footer.php'
]

def add_img_fluid(match):
    img_tag = match.group(0)
    if 'img-fluid' in img_tag:
        return img_tag
    
    if 'class=\"' in img_tag:
        img_tag = img_tag.replace('class=\"', 'class=\"img-fluid ')
    else:
        # no class attribute, add it at the end before >
        img_tag = img_tag.replace('>', ' class=\"img-fluid\">')
        
    # Also remove w-100 if present as img-fluid handles responsiveness
    img_tag = img_tag.replace('img-fluid w-100 ', 'img-fluid ')
    img_tag = img_tag.replace(' w-100', '')
    
    return img_tag

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(r'<img [^>]+>', add_img_fluid, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print('Added img-fluid to all images and removed w-100 from images.')
