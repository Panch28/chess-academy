import re
import os

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

def process_gallery(content):
    content = content.replace('rgba(212, 175, 55,', 'rgba(232, 93, 4,')
    content = content.replace('rgba(212,175,55,', 'rgba(232, 93, 4,')
    content = content.replace('#161b22', '#FFFFFF')
    content = content.replace('#d4af37', '#E85D04')
    content = content.replace('#0a0a0f', '#FFFFFF')
    return content

with open(f"{base_dir}/CircularGallery.css", "r", encoding="utf-8") as f:
    css = f.read()

css = process_gallery(css)

with open(f"{base_dir}/CircularGallery.css", "w", encoding="utf-8") as f:
    f.write(css)

def process_html(content):
    # Inline styles like hero-bg style in HTML if any, and any hardcoded colors
    content = content.replace('#d4af37', '#E85D04')
    content = content.replace('#c9a84c', '#E85D04')
    content = content.replace('rgba(212, 175, 55,', 'rgba(232, 93, 4,')
    content = content.replace('rgba(212,175,55,', 'rgba(232, 93, 4,')
    return content

with open(f"{base_dir}/index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = process_html(html)

with open(f"{base_dir}/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Done gallery and index update")
