import re

with open('c:/xampp/htdocs/ananya/index.php', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all Unsplash images
urls = set(re.findall(r'src=\"(https://images\.unsplash\.com[^\"]+)\"', html))

# Replace them with reliable picsum.photos with appropriate seed to keep them consistent but different
counter = 1
for url in urls:
    # try to extract width if possible, default to 800
    w = 800
    h = 600
    if 'w=1920' in url:
        w = 1920
        h = 1080
    elif 'w=1200' in url:
        w = 1200
        h = 800
    elif 'w=1000' in url:
        w = 1000
        h = 700
    
    new_url = f"https://picsum.photos/seed/ananya{counter}/{w}/{h}"
    html = html.replace(url, new_url)
    counter += 1

with open('c:/xampp/htdocs/ananya/index.php', 'w', encoding='utf-8') as f:
    f.write(html)

print("Replaced all Unsplash images with Picsum images.")
