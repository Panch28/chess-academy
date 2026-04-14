import re
import os

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(os.path.join(base_dir, "old_index.html"), "r", encoding="utf-16") as f:
    old_html = f.read()

preloader_match = re.search(r'(<div class="preloader" id="preloader">.*?</div>\s*</div>\s*</div>)', old_html, re.DOTALL)
preloader_block = ""
if preloader_match:
    preloader_block = preloader_match.group(1)
    preloader_block = re.sub(
        r'<div class="preloader-logo">\s*<i class="fa-solid fa-chess-knight"></i>\s*</div>',
        '<div class="preloader-logo">\n                  <img src="logo.png" style="height: 64px; width: auto; animation: pulse 2s infinite;" alt="Loading Logo">\n              </div>',
        preloader_block
    )

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    curr_html = f.read()

# 1. Restore Preloader
if 'id="preloader"' not in curr_html and preloader_block:
    curr_html = curr_html.replace('<body>', '<body>\n\n    ' + preloader_block)

# 2. Remove the 'NOW ENROLLING' badge completely so it doesn't collide
curr_html = re.sub(r'<div class="event-badge.*?</div>', '', curr_html, flags=re.DOTALL)

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(curr_html)

# Restore JS preloader timeouts
with open(os.path.join(base_dir, "script.js"), "r", encoding="utf-8") as f:
    c_js = f.read()

if "getElementById('preloader')" not in c_js:
    c_js = c_js.replace(
        "const navbar = document.getElementById('navbar');",
        "const preloader = document.getElementById('preloader');\n      const navbar = document.getElementById('navbar');"
    )

if "setTimeout(() => {" not in c_js or "preloader.classList.add('hidden')" not in c_js:
    c_js = re.sub(
        r'initHeroAnimations\(\);[\s\S]*?initCountdown\(\);',
        "setTimeout(() => {\n          if (preloader) preloader.classList.add('hidden');\n          initHeroAnimations();\n          initTypewriter();\n          initCountdown();\n      }, 2200);",
        c_js
    )

with open(os.path.join(base_dir, "script.js"), "w", encoding="utf-8") as f:
    f.write(c_js)

print("Restored preloader & removed badge.")
