import re

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace Preloader Logo
html = re.sub(
    r'<div class="preloader-logo">\s*<i class="fa-solid fa-chess-knight"></i>\s*</div>',
    '<div class="preloader-logo">\n                  <img src="logo.png" style="height: 64px; width: auto; animation: pulse 2s infinite;" alt="Loading Logo">\n              </div>',
    html
)

# Replace Footer Logo
html = re.sub(
    r'<div class="footer-logo">\s*<i class="fa-solid fa-chess-knight"></i>\s*<span>Sri Sai Chess Academy</span>\s*</div>',
    '<div class="footer-logo" style="display: flex; align-items: center; gap: 10px;">\n                        <img src="logo.png" style="height: 48px; width: auto;" alt="Footer Logo">\n                        <span>Sri Sai Chess Academy</span>\n                    </div>',
    html
)

with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Preloader and Footer logos updated.")
