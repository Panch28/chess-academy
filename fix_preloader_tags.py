import re
base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"
with open(f"{base_dir}/index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(
    r'<div class="preloader" id="preloader">.*?<header class="navbar" id="navbar">',
    '<div class="preloader" id="preloader">\n        <div class="preloader-content">\n            <div class="preloader-logo">\n                  <img src="logo.png" style="height: 64px; width: auto; animation: pulse 2s infinite;" alt="Loading Logo">\n              </div>\n            <div class="preloader-text">Sri Sai Chess Academy</div>\n            <div class="preloader-bar">\n                <div class="preloader-progress"></div>\n            </div>\n        </div>\n    </div>\n\n    <header class="navbar" id="navbar">',
    html,
    flags=re.DOTALL
)

with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Fixed HTML preloader closing tags.")
