import re

base_dir = r"c:\Users\Panchakshari S H\Downloads\website demos\chess academy"

with open(f"{base_dir}\index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(r'<canvas id="chessKing3D" class="chess-king-canvas"></canvas>', '', html)

with open(f"{base_dir}\index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open(f"{base_dir}\script.js", "r", encoding="utf-8") as f:
    js = f.read()

js = js.replace('initChessKing3D();', '// initChessKing3D();')

with open(f"{base_dir}\script.js", "w", encoding="utf-8") as f:
    f.write(js)

css_patch = """
/* Better mobile hero image crop */
@media (max-width: 992px) {
    .hero-right {
        height: auto !important;
        min-height: unset !important;
        aspect-ratio: 4/5 !important;
    }
}
"""
with open(f"{base_dir}\styles.css", "a", encoding="utf-8") as f:
    f.write(css_patch)

print('Done removing 3D model and fixing crop')
