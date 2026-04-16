import re
import os

def process_styles(content):
    # 1. Update :root variables
    content = re.sub(r'(--primary:\s*)#[a-zA-Z0-9]+', r'\g<1>#E85D04', content)
    content = re.sub(r'(--primary-light:\s*)#[a-zA-Z0-9]+', r'\g<1>#FFCC99', content)
    content = re.sub(r'(--primary-dark:\s*)#[a-zA-Z0-9]+', r'\g<1>#C14A03', content)
    
    content = re.sub(r'(--secondary:\s*)#[a-zA-Z0-9]+', r'\g<1>#FFFFFF', content)
    content = re.sub(r'(--secondary-light:\s*)#[a-zA-Z0-9]+', r'\g<1>#F0F0F0', content)
    
    content = re.sub(r'(--midnight:\s*)#[a-zA-Z0-9]+', r'\g<1>#1B2F5E', content)
    content = re.sub(r'(--obsidian:\s*)#[a-zA-Z0-9]+', r'\g<1>#1B2F5E', content)
    
    content = re.sub(r'(--text-main:\s*)#[a-zA-Z0-9]+', r'\g<1>#1B2F5E', content)
    content = re.sub(r'(--text-light:\s*)#[a-zA-Z0-9]+', r'\g<1>#3A5FCD', content)
    
    content = re.sub(r'(--bg-light:\s*)#[a-zA-Z0-9]+', r'\g<1>#FFFFFF', content)
    content = re.sub(r'(--border-color:\s*)#[a-zA-Z0-9]+', r'\g<1>#3A5FCD', content)
    
    # Shadows
    content = content.replace('rgba(212, 175, 55,', 'rgba(232, 93, 4,')
    content = content.replace('rgba(212,175,55,', 'rgba(232, 93, 4,')
    
    # 2. Hardcoded gold
    content = content.replace('#d4af37', '#E85D04')
    content = content.replace('#c9a84c', '#E85D04')
    content = content.replace('#a68434', '#C14A03')
    
    # 3. Navbar fixes
    content = re.sub(r'\.navbar\.scrolled\s*\{\s*background:\s*rgba\([^)]+\);', '.navbar.scrolled {\n    background: rgba(27, 47, 94, 0.95);', content)
    content = re.sub(r'\.nav-links a\s*\{[^}]*color:[^;]+;', lambda m: m.group(0).replace('var(--text-main)', '#FFFFFF').replace('var(--white)', '#FFFFFF'), content)
    # Ensure nav links are white
    content = content.replace('color: var(--text-main); /* or whatever nav-links a has */', 'color: #FFFFFF;')
    
    # 4. Hero bg
    content = re.sub(r'\.hero-bg::before\s*\{[^}]*background:[^;]+;', '.hero-bg::before {\n    content: \'\';\n    position: absolute;\n    top: 0;\n    left: 0;\n    width: 100%;\n    height: 100%;\n    background: rgba(27, 47, 94, 0.85);', content)
    
    # 5. Badges
    content = content.replace('.badge-green { background: rgba(46,204,113,.15); color: var(--green); }', '.badge-green { background: #FFCC99; color: #1B2F5E; }')
    content = content.replace('.badge-blue { background: rgba(52,152,219,.15); color: var(--blue); }', '.badge-blue { background: #FFCC99; color: #1B2F5E; }')
    # Or in css where badges are defined (events mainly)
    
    # 6. Replace all generic dark backgrounds (e.g., #0a0a0f, #1c1c28, #161b22, #0d1117) that weren't captured by variables
    content = content.replace('#0a0a0f', '#FFFFFF')
    content = content.replace('#13131a', '#FFFFFF')
    content = content.replace('#1c1c28', '#FFFFFF')
    content = content.replace('#1c2128', '#FFFFFF')
    content = content.replace('#0d1117', '#1B2F5E')
    content = content.replace('#161b22', '#1B2F5E')
    content = content.replace('#0d0d0d', '#1B2F5E')
    content = content.replace('#161616', '#FFFFFF')
    content = content.replace('#1a1a1a', '#F0F0F0')
    content = content.replace('#222', '#E8E8E8')
    content = content.replace('#12121a', '#FFFFFF')
    
    return content

def process_admin(content):
    # CSS variables in admin.html
    content = re.sub(r'--gold:\s*#[a-zA-Z0-9]+;', '--gold: #E85D04;', content)
    content = re.sub(r'--gold-light:\s*#[a-zA-Z0-9]+;', '--gold-light: #FFCC99;', content)
    content = re.sub(r'--dark:\s*#[a-zA-Z0-9]+;', '--dark: #FFFFFF;', content)
    content = re.sub(r'--dark2:\s*#[a-zA-Z0-9]+;', '--dark2: #F0F0F0;', content)
    content = re.sub(r'--dark3:\s*#[a-zA-Z0-9]+;', '--dark3: #FFFFFF;', content)
    content = re.sub(r'--dark4:\s*#[a-zA-Z0-9]+;', '--dark4: #F5F5F5;', content)
    content = re.sub(r'--text:\s*#[a-zA-Z0-9]+;', '--text: #1B2F5E;', content)
    content = re.sub(r'--text-muted:\s*#[a-zA-Z0-9]+;', '--text-muted: #3A5FCD;', content)
    content = re.sub(r'--border:\s*rgba\([^)]+\);', '--border: #3A5FCD;', content)
    
    content = content.replace('rgba(212,175,55,', 'rgba(232, 93, 4,')
    content = content.replace('rgba(212, 175, 55,', 'rgba(232, 93, 4,')
    content = content.replace('.badge-blue { background: rgba(52,152,219,.15); color: var(--blue); }', '.badge-blue { background: #FFCC99; color: #1B2F5E; }')
    content = content.replace('.badge-green { background: rgba(46,204,113,.15); color: var(--green); }', '.badge-green { background: #FFCC99; color: #1B2F5E; }')
    content = content.replace('background: rgba(212,175,55,.15);', 'background: #FFCC99;')
    content = content.replace('color: var(--gold);', 'color: #E85D04;')
    
    return content

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}/styles.css", "r", encoding="utf-8") as f:
    css = f.read()

# Custom manual adjustments for strictly required styles per prompt
css = process_styles(css)
# Update text-white to not be pure white if it sits on white bg... wait, hero is dark, so text-white can remain white in hero. I'll let the variables do their job.

with open(f"{base_dir}/styles.css", "w", encoding="utf-8") as f:
    f.write(css)

with open(f"{base_dir}/admin.html", "r", encoding="utf-8") as f:
    html = f.read()

html = process_admin(html)

with open(f"{base_dir}/admin.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done")
