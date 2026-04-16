import re
import os

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

# 1. Restore HTML
with open(f"{base_dir}\old_index.html", "r", encoding="utf-8") as f:
    old_html = f.read()
with open(f"{base_dir}\index.html", "r", encoding="utf-8") as f:
    curr_html = f.read()

old_match = re.search(r'<div class="circular-gallery-wrapper".*?</section>', old_html, re.DOTALL)
if old_match:
    old_gall = old_match.group()
    # Remove drag hints
    old_gall = re.sub(r'<div class="gallery-drag-hint-3d">.*?</div>', '', old_gall, flags=re.DOTALL)
    old_gall = re.sub(r'<p class="text-center text-primary.*?>.*?Explore.*?our.*?moments.*?</p>', '', old_gall, flags=re.DOTALL | re.IGNORECASE)

    # Note: we should replace specifically `<section id="gallery"...` from current to match exactly what to replace
    curr_html = re.sub(r'<section id="gallery".*?</section>', '<section id="gallery" class="section">\n' + old_gall, curr_html, flags=re.DOTALL)
    with open(f"{base_dir}\index.html", "w", encoding="utf-8") as f:
        f.write(curr_html)

# 2. Restore script.js
with open(f"{base_dir}\old_script.js", "r", encoding="utf-8") as f:
    old_js = f.read()

start = old_js.find("function init3DGallery()")
brace_count = 0
in_func = False
end = start
for i in range(start, len(old_js)):
    if old_js[i] == '{':
        if not in_func: in_func = True
        brace_count += 1
    elif old_js[i] == '}':
        brace_count -= 1
        if in_func and brace_count == 0:
            end = i + 1
            break
old_init = old_js[start:end]

with open(f"{base_dir}\script.js", "r", encoding="utf-8") as f:
    curr_js = f.read()

start_curr = curr_js.find("function init3DGallery()")
brace_count = 0
in_func = False
end_curr = start_curr
for i in range(start_curr, len(curr_js)):
    if curr_js[i] == '{':
        if not in_func: in_func = True
        brace_count += 1
    elif curr_js[i] == '}':
        brace_count -= 1
        if in_func and brace_count == 0:
            end_curr = i + 1
            break

# Remove hardcoded items fallback code from restored snippet
old_init = re.sub(r'const galleryItems = \[.*?\];', 'const galleryItems = [];', old_init, flags=re.DOTALL)
old_init = re.sub(r'// Create initial fallback gallery items.*?track.appendChild\(galleryItem\);\n    \}\);', '', old_init, flags=re.DOTALL)

curr_js = curr_js[:start_curr] + old_init + curr_js[end_curr:]
with open(f"{base_dir}\script.js", "w", encoding="utf-8") as f:
    f.write(curr_js)

# 3. Clean CSS overrides
with open(f"{base_dir}\styles.css", "r", encoding="utf-8") as f:
    css = f.read()

css = re.sub(r'/\* ==========================================================================\s+NATIVE CSS GALLERY FIX\s+========================================================================== \*/.*?(?=/\* ==========================================================================|$|/\* FIX GALLERY SQUISH \*/)', '', css, flags=re.DOTALL)
css = re.sub(r'/\* FIX GALLERY SQUISH \*/.*?(?=/\* ==========================================================================|$|/\* GALLERY ULTIMATE HEIGHT FIX \*/)', '', css, flags=re.DOTALL)
css = re.sub(r'/\* GALLERY ULTIMATE HEIGHT FIX \*/.*?(?=/\* ==========================================================================|$)', '', css, flags=re.DOTALL)

with open(f"{base_dir}\styles.css", "w", encoding="utf-8") as f:
    f.write(css)

# 4. Remove wheel event from CircularGallery.js
with open(f"{base_dir}\CircularGallery.js", "r", encoding="utf-8") as f:
    cg = f.read()
cg = re.sub(r'// Wheel.*?\}\, \{ passive\: false \}\);', '', cg, flags=re.DOTALL)
with open(f"{base_dir}\CircularGallery.js", "w", encoding="utf-8") as f:
    f.write(cg)

print("Gallery restored perfectly without wheel hijack!")
