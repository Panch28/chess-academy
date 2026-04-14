import re

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove Preloader
html = re.sub(
    r'<div class="preloader" id="preloader">.*?</div>\n    </div>\n</div>\n',
    '',
    html,
    flags=re.DOTALL
)

# Wait, the closing tags might be tricky. Let's just remove everything from <div class="preloader" to the start of <header
html = re.sub(
    r'<div class="preloader" id="preloader">.*?<header',
    '<header',
    html,
    flags=re.DOTALL
)

with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Preloader removed from HTML.")
