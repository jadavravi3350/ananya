import re

with open('c:/xampp/htdocs/ananya/index.php', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    r'<i class="fa-solid fa-arrow-right"></i>': r'<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>',
    r'<i class="fa-solid fa-check"></i>': r'<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    r'<i class="fa-solid fa-building"></i>': r'<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"></rect><path d="M9 22v-4h6v4"></path><path d="M8 6h.01"></path><path d="M16 6h.01"></path><path d="M12 6h.01"></path><path d="M12 10h.01"></path><path d="M12 14h.01"></path><path d="M16 10h.01"></path><path d="M16 14h.01"></path><path d="M8 10h.01"></path><path d="M8 14h.01"></path></svg>',
    r'<i class="fa-solid fa-flask"></i>': r'<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3H15"></path><path d="M10 3V8L3 21H21L14 8V3"></path><path d="M4.5 17H19.5"></path></svg>',
    r'<i class="fa-solid fa-book-open"></i>': r'<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>',
    r'<i class="fa-solid fa-trophy"></i>': r'<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 21h8"></path><path d="M12 17v4"></path><path d="M7 4h10"></path><path d="M17 4v8a5 5 0 0 1-10 0V4"></path><path d="M7 4H4a2 2 0 0 0-2 2v2a5 5 0 0 0 5 5h0"></path><path d="M17 4h3a2 2 0 0 1 2 2v2a5 5 0 0 1-5 5h0"></path></svg>',
    r'<i class="fa-solid fa-graduation-cap"></i>': r'<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>',
    r'<i class="fa-solid fa-award"></i>': r'<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>',
    r'<i class="fa-solid fa-users"></i>': r'<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>',
    r'<i class="fa-solid fa-building-columns"></i>': r'<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18"></path><path d="M4 21v-7"></path><path d="M20 21v-7"></path><path d="M8 21v-7"></path><path d="M16 21v-7"></path><path d="M12 21v-7"></path><path d="M2 14h20"></path><path d="M12 3l10 5H2L12 3z"></path></svg>',
    r'<i class="fa-solid fa-address-card"></i>': r'<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2" ry="2"></rect><circle cx="9" cy="10" r="2"></circle><line x1="15" y1="10" x2="19" y2="10"></line><line x1="15" y1="14" x2="19" y2="14"></line><path d="M13 16a4 4 0 0 0-8 0"></path></svg>',
    r'<i class="fa-solid fa-desktop"></i>': r'<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>',
    r'<i class="fa-solid fa-file-circle-check"></i>': r'<svg width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><polyline points="9 15 11 17 15 13"></polyline></svg>',
    r'<i class="fa-solid fa-arrow-right-long btn-icon-circle"></i>': r'<svg class="btn-icon-circle" width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>'
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open('c:/xampp/htdocs/ananya/index.php', 'w', encoding='utf-8') as f:
    f.write(html)

# Also remove FontAwesome from header.php
with open('c:/xampp/htdocs/ananya/header.php', 'r', encoding='utf-8') as f:
    header = f.read()

header = re.sub(r'<!-- FontAwesome -->\s*<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css\">\s*', '', header)

with open('c:/xampp/htdocs/ananya/header.php', 'w', encoding='utf-8') as f:
    f.write(header)

print("Replaced FontAwesome with SVGs!")
